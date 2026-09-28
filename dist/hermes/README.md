# Hermes Agent distribution

Hermes Agent natively supports SKILL.md directories with optional references and uses progressive disclosure.

## Install locally

Copy the desired skill directory under your Hermes profile:

```bash
mkdir -p ~/.hermes/skills/research
cp -R purchase-research ~/.hermes/skills/research/
cp -R vae-research ~/.hermes/skills/research/
```

The skills become available automatically and can be invoked as `/purchase-research` and `/vae-research`.

## Recommended Git workflow

Clone this repository somewhere read-only for the research profiles, then copy or synchronize only the desired `dist/hermes/<skill>` directories into `~/.hermes/skills/research/`.

## Security

These distributions are intentionally research-only. Their SKILL.md explicitly forbids OS, network, DevOps, package-installation and Hermes-configuration changes as part of purchase research. Skill creation/update also requires explicit user authorization.

This complements — and does not replace — profile/channel restrictions configured in Hermes itself.

## Updating

Pull the repository, review the diff, then replace the local skill directory. Do not blindly auto-update skills on a privileged Hermes profile.
