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
