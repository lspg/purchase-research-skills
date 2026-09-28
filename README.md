# Purchase Research Skills

Reusable Agent Skills for structured product-purchase research.

## Skills

### purchase-research — v1.1.0
Generic pre-purchase research orchestrator. It turns an initial buying idea into a requirements brief, asks only discriminating questions, researches the market, audits finalists, compares total cost and after-sales support, and can propose creation or improvement of a specialized domain skill.

### vae-research — v1.0.0
Specialized research workflow for electric bicycles (VAE/e-bikes), cargo bikes, longtails, fatbikes, accessories, trailers and car bike racks, with specific handling of payload/GVW, passenger limits, EU compliance, serviceability and subsidies.

## Structure

```
skills/
  purchase-research/
    SKILL.md
    CHANGELOG.md
    references/
  vae-research/
    SKILL.md
    references/
```

## Design principle

`purchase-research` is the generic orchestrator. Specialized skills contain durable domain methodology, not time-sensitive prices, rankings, promotions or “best product” claims.

## Usage

Each skill directory follows the Agent Skills convention with a `SKILL.md` containing YAML frontmatter and optional reference files.

## License

MIT.


## ChatGPT Free

A standalone edition for accounts without custom Skill import is available in:

`dist/chatgpt-free/purchase-research.md`

See `dist/chatgpt-free/README.md` for installation guidance and limitations. This edition preserves the core pre-purchase workflow but does not automatically load the modular reference files or specialized skills.


## Gemini and Hermes

- `dist/gemini/` contains Gemini Gem instructions plus Knowledge files for purchase-research and vae-research.
- `dist/hermes/` contains native Hermes Agent SKILL.md distributions with modular references and research-only safety boundaries.

See each distribution README for installation guidance.
