# Claude Code → Refuseless

Claude Code speaks the Anthropic Messages API. Refuseless serves it at `/v1/messages`, so point Claude Code at the
host **without** `/v1`: Claude Code appends `/v1/messages` itself.

```bash
export ANTHROPIC_BASE_URL="https://api.refuseless.com"
export ANTHROPIC_AUTH_TOKEN="abl_your_key_here"   # keys start with abl_
export ANTHROPIC_MODEL="glm-5.3-abliterated"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="glm-5.3-flash-abliterated"   # used for background tasks
claude
```

To keep it per project instead of per shell, put the same values in `.claude/settings.json`:

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.refuseless.com",
    "ANTHROPIC_MODEL": "glm-5.3-abliterated",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-5.3-flash-abliterated"
  }
}
```

Keep the key out of that file if the repo is shared: export `ANTHROPIC_AUTH_TOKEN` in your shell instead.

## Status of this config

The `/v1/messages` and `/v1/messages/count_tokens` routes answer in the Anthropic error format
(`{"type":"error","error":{"type":"authentication_error",...}}`) when called with an invalid key, checked on
2026-10-27. The public OpenAPI spec does not list them yet, and this config has not been run end to end with a paid
key. If it fails for you, open an issue with the error message.

Sign up (affiliate link, $5 bonus on a first deposit of $10 or more): https://refuseless.com/?ref=56iahu9u
