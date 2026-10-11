# "Sign in with GitHub" for the Warehouse page

The page's **Add or update a patch** form opens pull requests as the contributor.
With this set up, contributors click **Sign in with GitHub** instead of pasting a token.
Without it, the form still works with a personal access token.

GitHub gives out a sign-in token only in exchange for an OAuth App's client secret,
and a public page can't keep a secret. `worker.js` is a tiny Cloudflare Worker (free plan)
that holds the secret and does only that exchange. It stores nothing.

## Setup (about 10 minutes, once)

1. **Create the OAuth App.** GitHub → Settings → Developer settings → OAuth Apps → New OAuth App
   (or, under an organization, its settings).
   - Application name: `FPSLocker Warehouse`
   - Homepage URL: `https://masagrator.github.io/FPSLocker-Warehouse/`
   - Authorization callback URL: `https://masagrator.github.io/FPSLocker-Warehouse/`

   Copy the **Client ID**, then **Generate a new client secret** and copy it.

2. **Deploy the Worker.** In the Cloudflare dashboard: Workers & Pages → Create →
   **Create Worker** ("Start with Hello World!"), name it, and click **Deploy**.
   Then click **Edit code**, replace everything with the contents of `worker.js`, and click **Deploy** again.
   (Don't use "Upload and deploy": that's for static sites and rejects Worker code.)
   Then in the Worker's Settings → Variables and Secrets add:
   - `GITHUB_CLIENT_ID` (text): the Client ID
   - `GITHUB_CLIENT_SECRET` (secret): the client secret
   - `ALLOWED_ORIGIN` (text, optional): `https://masagrator.github.io`. Without it, any `https://<name>.github.io` page may use the Worker.

   **Deploying from GitHub instead** (Worker connected to this repository): in the Worker's
   Settings → Build, set **Root directory** to `tools/oauth-worker`, otherwise the build fails with
   "Could not detect a directory containing static files". The Worker's name must match `name`
   in `wrangler.toml`. Add the client ID and secret as **Secrets** so deploys never remove them.

   Or from this folder: `npx wrangler deploy`, then
   `npx wrangler secret put GITHUB_CLIENT_ID` and `npx wrangler secret put GITHUB_CLIENT_SECRET`.

   Note the Worker URL, like `https://fpslocker-warehouse.<you>.workers.dev`.
   Opening it in a browser should show `{"error":"Not found"}`, which means it's running.

3. **Tell the page.** In the repository: Settings → Secrets and variables → Actions → Variables
   → New repository variable:
   - `OAUTH_CLIENT_ID`: the Client ID
   - `OAUTH_TOKEN_URL`: the Worker URL followed by `/token`

   Then run the **Build Warehouse page** workflow (Actions tab → Run workflow).

## What contributors see

The first time, GitHub asks them to authorize "FPSLocker Warehouse" with access to public
repositories. That access is needed to fork the Warehouse and open the pull request.
Later sign-ins skip that screen. The token stays in their browser until they click
**Sign out**, and they can revoke it any time under GitHub → Settings → Applications.
