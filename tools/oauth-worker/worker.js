// Token exchange for the Warehouse page's "Sign in with GitHub" button.
//
// GitHub only hands out a user token in exchange for the OAuth App's client secret,
// which can't live in a public page. This Worker holds the secret and does that one
// exchange: POST /token {"code": "..."} -> {"access_token": "..."}.
// It stores nothing and only answers the Warehouse page's origin.
//
// Settings (Cloudflare dashboard → Worker → Settings → Variables and secrets):
//   GITHUB_CLIENT_ID      OAuth App client ID
//   GITHUB_CLIENT_SECRET  OAuth App client secret (add it as a Secret)
//   ALLOWED_ORIGIN        optional: the page's origin, e.g. https://masagrator.github.io
//                         (several can be separated by commas). When it isn't set,
//                         any https://<name>.github.io page is allowed.

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || "";
    const list = (env.ALLOWED_ORIGIN || "").split(",").map((s) => s.trim().replace(/\/+$/, "")).filter(Boolean);
    const allowed = list.length ? list.includes(origin) : /^https:\/\/[a-z0-9-]+\.github\.io$/i.test(origin);
    const cors = {
      "Access-Control-Allow-Origin": allowed ? origin : "null",
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
      "Access-Control-Max-Age": "86400",
      Vary: "Origin",
    };
    const json = (body, status = 200) =>
      new Response(JSON.stringify(body), { status, headers: { ...cors, "Content-Type": "application/json" } });

    if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: cors });
    if (new URL(request.url).pathname !== "/token" || request.method !== "POST") return json({ error: "Not found" }, 404);
    if (!allowed) return json({ error: "This origin isn't allowed" }, 403);
    if (!env.GITHUB_CLIENT_ID || !env.GITHUB_CLIENT_SECRET) return json({ error: "The Worker is missing GITHUB_CLIENT_ID or GITHUB_CLIENT_SECRET" }, 500);

    let code;
    try { ({ code } = await request.json()); } catch (e) {}
    if (typeof code !== "string" || !/^[\w-]{1,100}$/.test(code)) return json({ error: "Missing or invalid code" }, 400);

    const r = await fetch("https://github.com/login/oauth/access_token", {
      method: "POST",
      headers: { Accept: "application/json", "Content-Type": "application/json", "User-Agent": "fpslocker-warehouse-oauth" },
      body: JSON.stringify({ client_id: env.GITHUB_CLIENT_ID, client_secret: env.GITHUB_CLIENT_SECRET, code }),
    });
    const data = await r.json().catch(() => ({}));
    if (!data.access_token) return json({ error: data.error_description || data.error || "GitHub didn't return a token" }, 400);
    return json({ access_token: data.access_token, scope: data.scope });
  },
};
