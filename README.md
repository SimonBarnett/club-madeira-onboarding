# club-madeira-onboarding

Invite-only Club Madeira affiliate onboarding **skill pack**. A human loads
these skills into their own agent; the agent reviews the human's website,
enforces dual gates (£20/mo traffic feasibility and Club-over-Amazon
engagement), requests a GUID only after evidenced PASS, then walks DNS TXT
proof.

See `docs/vision.md`.

## Honesty box

Foundation skill: `.grok/skills/harvest-agent-skills/SKILL.md`

Home: https://github.com/SimonBarnett/club-madeira-onboarding

Learnings return as a **branch + pull request**. Never `git push origin main`
for harvest. Pattern:
https://github.com/SimonBarnett/agentic_build/blob/main/.grok/skills/harvest-agent-skills/SKILL.md

## Vision gate

```
python tools/validate-vision-pack.py docs/vision.md --mocks-dir docs/mocks
```

## Bob URLs (no secrets)

| Role | URL |
|------|-----|
| GitHub webhook | `https://irc.ntsa.uk/bob/v1/git` |
| Digest report (not a GitHub hook) | `https://irc.ntsa.uk/bob/v1/report` |
