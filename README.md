# Abliterated LLM APIs

A sourced price comparison of hosted APIs that serve abliterated or uncensored open-weight models, plus
copy-paste configs for Claude Code, Codex, OpenCode and the OpenAI SDK.

Prices change without notice. Every number below was read on **2026-10-27** from the source linked in the
[Sources](#sources) section. If you find a stale price, open an issue or a PR with the new source.

> **Disclosure.** The Refuseless links in this repo are affiliate links: if you sign up through them and deposit
> at least $10, you get a $5 bonus and I earn a commission. Other providers are listed because they are relevant,
> and their links carry no referral code. Nobody paid for placement.

## What "abliterated" means

Abliteration finds the direction in the model's activations that drives refusals and removes it from the weights.
It differs from a jailbreak, which injects text into the prompt and has to be reapplied every session.

It adds no knowledge. An abliterated model is as capable as its base model at best, and a sloppy edit makes it
worse. Judge a build by its base model's benchmarks and by testing it on your own tasks.

"Uncensored" in a provider's catalog does not always mean abliteration: some providers do not say whether the
refusals were removed from the weights, by fine-tuning or by a permissive system prompt. Ask before you pay.

## GLM 5.3 (full size)

US$ per 1M tokens, input / output.

| Provider | Model id | Input / output | Context | API formats | How refusals were removed |
|---|---|---|---|---|---|
| [Refuseless](https://refuseless.com/?ref=56iahu9u) | `glm-5.3-abliterated` | 1.25 / 2.25 | 1,048,576 | OpenAI, Anthropic | Weight edit (abliteration), per the provider |
| [NanoGPT](https://nano-gpt.com) | `z-ai/glm-5.3-uncensored` | 1.25 / 2.25 (cache read 0.30) | 1,048,576 | OpenAI | Not stated ("experimental uncensored") |
| [abliteration.ai](https://abliteration.ai) | `abliterated-model-large-v2` | 3.00 / 5.00 | ~1.05M | OpenAI, Anthropic | Abliteration |
| [Venice](https://venice.ai) | Abliterated Large V2 | 3.00 / 5.00 | ~1.05M | OpenAI | Not stated |
| [Dagon Inference](https://inference.dagon.so) (router) | `glm-5.3-abliterated` | 1.10 / 2.20 (cache read 0.165) | 1,048,576 | OpenAI, Anthropic | Not stated beyond "refusal behavior removed". Resold from Refuseless, Experiential Labs or Silk Compute, cheapest healthy one per request |
| Dagon Inference (router) | `abliterated-model-large-v2` | 3.30 / 5.50 (cache read 0.33) | 1,000,000 | OpenAI, Anthropic | Abliterated and post-trained by abliteration.ai, per Dagon's model notes. Resold from abliteration.ai |

## GLM 5.3 Flash and other small models

| Provider | Model | Input / output | Notes |
|---|---|---|---|
| NanoGPT | GLM 5.3 Flash Uncensored | 0.20 / 0.80 | Output limit 32,768 |
| NanoGPT | GLM 5.3 Flash Cybersecurity | 0.15 / 0.50 | Uncensored base with moderation for illegal activity |
| [MagmaRouter](https://magmarouter.com) | `glm-5.3-flash-xploded` | 0.30 / 1.00 | OpenAI and Anthropic formats, per-key spend cap |
| Venice | DeepSeek V4.1 Flash Uncensored | 0.33 / 1.32 | |
| Venice | Abliterated Large Flash | 1.25 / 2.50 | |
| Refuseless | `glm-5.3-flash-abliterated` | Not published | Price not listed in the public docs |
| Dagon Inference (router) | `glm-5.3-flash-abliterated` | 0.132 / 0.55 (cache read 0.0275) | Resold from Refuseless, Experiential Labs or Silk Compute. Method not stated beyond "refusal behavior removed" |
| Dagon Inference (router) | `deepseek-v4.1-flash-abliterated` | 0.11 / 0.44 (cache read 0.022) | Resold from Lutheos, Refuseless, Experiential Labs or Silk Compute. Method not stated beyond "refusal behavior removed" |
| Dagon Inference (router) | `abliterated-model-large-flash` | 1.10 / 2.20 (cache read 0.11) | Resold from abliteration.ai. Text and image input |
| [OrcaRouter](https://www.orcarouter.ai) | OrcaCyber GLM 5.3 Flash | Not published per token | Publishes its weights and refusal-rate method on Hugging Face |

For price alone on the Flash tier, NanoGPT and MagmaRouter are the cheapest options listed here.

[OpenRouter](https://openrouter.ai) listed no abliterated or uncensored model in its public `/api/v1/models`
catalog on 2026-10-27.

## Configs

Each file in [`configs/`](configs) points one tool at Refuseless. For another provider, swap the base URL,
the key and the model id.

| Tool | File | Wire format |
|---|---|---|
| Claude Code | [`configs/claude-code.md`](configs/claude-code.md) | Anthropic Messages |
| Codex CLI | [`configs/codex.toml`](configs/codex.toml) | OpenAI Responses |
| OpenCode | [`configs/opencode.json`](configs/opencode.json) | OpenAI Chat Completions |
| OpenAI SDK (Python) | [`configs/openai_sdk.py`](configs/openai_sdk.py) | OpenAI Chat Completions |

## Use it on systems you are allowed to test

Removing refusals moves the judgment to you. Every provider above forbids attacking systems you do not own or are
not authorized to test, and so does the law in most places.

## Sources

Read on 2026-10-27.

- Refuseless: [docs.refuseless.com](https://docs.refuseless.com) (models, SDKs, OpenAPI spec) and the pricing shown on
  refuseless.com.
- NanoGPT: [nano-gpt.com/pricing](https://nano-gpt.com/pricing) and the
  [GLM 5.3 Uncensored model page](https://cake.nano-gpt.com/models/text/z-ai/glm-5.3-uncensored).
- abliteration.ai and MagmaRouter: [magmarouter.com/alternatives/abliteration-ai](https://magmarouter.com/alternatives/abliteration-ai/).
- Venice: [docs.venice.ai/overview/pricing](https://docs.venice.ai/overview/pricing.md).
- OrcaRouter: [orcarouter.ai](https://www.orcarouter.ai) model pages and [huggingface.co/orcarouter](https://huggingface.co/orcarouter).
- OpenRouter: `GET https://openrouter.ai/api/v1/models`.
- Dagon Inference: `GET https://inference.dagon.so/v1/models` (public, no key; price version 2026-11-10.7, read on
  2026-11-10; the [pricing page](https://inference.dagon.so/abliterated-llm-pricing) and model pages can show an earlier
  build snapshot) and the [terms](https://inference.dagon.so/terms), which name the upstream providers and say a
  Refuseless-routed request may be served by a deployment that has not had refusals removed. Prices include Dagon's 10%
  markup over the cheapest provider; a request that falls back to another provider is billed at that provider's rate.
  Added by the operator of Dagon.

## License

MIT.
