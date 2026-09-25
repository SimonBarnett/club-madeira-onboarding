# Vision: club-madeira-onboarding

Skill: `visionary`. New-product intake for Club Madeira affiliate
onboarding via the human's own agent.

## Objective

An invite-only Club Madeira affiliate path where a human's own agent
reviews the human's website, refuses weak traffic or Amazon-default
shoppers, and only after evidenced dual-gate PASS requests a Club
Madeira affiliate GUID and walks DNS TXT proof of control.

LOCKED

## Success

| id | metric | target | how measured | fail-when |
|----|--------|--------|--------------|-----------|
| S1 | GUID requested only after dual gate PASS | 100% of `request-guid` calls have prior PASS for traffic and engagement | `pytest` fixtures: API client not called on FAIL/UNKNOWN; called only on dual PASS with evidence hash in `tests/` | GUID API callable with no PASS evidence or after FAIL |
| S2 | Traffic gate is monetary | Estimate supports >= £20 / month under documented assumptions | Skill formula (visits x conversion band x commission band); tool writes numeric estimate to `evidence/traffic.json`; tests lock formula; fail when estimate < 20 or inputs missing | Gate passes on vibes with no number |
| S3 | Engagement prefers Club over Amazon | Checklist threshold PASS | Website review scores disclosure, Club CTA, Amazon deep-link dominance; fixture HTML in `tests/fixtures/`; threshold in skill | PASS when site only Amazon-deep-links with no Club path |
| S4 | Invite-only is unmistakable | Phrase present on entry surfaces | `rg -i "invite-only"` on umbrella `SKILL.md` and `docs/mocks/home.html`; CI or script exit 0 | Primary skill omits invite-only |
| S5 | DNS TXT walkthrough for common providers | Generic + Cloudflare, Route53, Namecheap, GoDaddy, Google DNS skills | Each provider skill has steps + verify; checklist in docs | GUID issued then dead-end "add a TXT somewhere" |
| S6 | Harvest uses honesty box | Foundation `harvest-agent-skills` with `github:` this repo; learnings return as PR (never push main) | Frontmatter `github: https://github.com/SimonBarnett/club-madeira-onboarding`; other skills link Foundation line; `docs/skill-harvest-log.md` on harvest PRs | Harvest only to `~/.grok`, push main, or skip honesty box |
| S7 | Vision pack validates | Validator exit 0 | `python tools/validate-vision-pack.py docs/vision.md --mocks-dir docs/mocks` | Create/park without pack |

LOCKED

## Shape

Primary: service

Hybrid note: the product is an agent skill pack (playbooks, gate tools,
DNS provider specs). Delivery is public git markdown plus HTML wireframes
of onboarding gate states, not a Club Madeira consumer website.

LOCKED

## Stack

Default: Markdown `SKILL.md` under `.grok/skills/`, evidence JSON in the
human's agent working tree, thin post-PASS API client (env secrets),
DNS provider skills + dig/DoH verify, public GitHub
`SimonBarnett/club-madeira-onboarding`, foundation honesty-box harvest
(`.grok/skills/harvest-agent-skills` twin with this repo `github:`).

Why: fleet agents already load `.grok/skills`; local evidence makes the
dual gate testable; honesty box returns DNS and gate learnings as PRs.

Why-not: consumer web app as product; auto-approve form (breaks
invite-only); invented Madeira API URLs; PNG mock pipeline; harvest
only on agent home disk.

LOCKED

## Architecture

Who talks to what. Phase 0 only.

```
Human
  |  clone/scaffold agent repo; load skills
  v
club-madeira-onboarding (umbrella, invite-only)
  |- affiliate-marketing-basics
  |- club-madeira-affiliates (invite-only, Club vs Amazon)
  |- website-review tool --> evidence/traffic.json
  |                      --> evidence/engagement.json
  |- dual-gate (human conviction + website evidence)
  |     FAIL --> stop; never request-guid
  |     PASS --> request-guid --> Club Madeira API [URL UNKNOWN]
  |                --> GUID + TXT instructions
  |- dns-* provider skills --> human adds TXT
  |- verify-txt
  v
harvest-agent-skills (honesty box)
  --> branch + PR to SimonBarnett/club-madeira-onboarding
  --> else issue harvest:/FR: on home repo
  --> never git push origin main for harvest

Trust: public repo has no secrets/GUIDs; human machine holds tokens;
Club API auth UNKNOWN; DNS proves domain control.
```

LOCKED

## Screens

HTML mocks in `docs/mocks/` (kebab-case). Operator gate states. No PNGs.

| id | file | state |
|----|------|-------|
| M1 | docs/mocks/home.html | primary — dual PASS, GUID path, DNS TXT, invite-only |
| M2 | docs/mocks/empty.html | empty — no site/evidence; GUID disabled |
| M3 | docs/mocks/error.html | error — traffic/engagement FAIL or API/DNS error |

## LOCKED

- Shape is skill-pack service.
- Dual gates: >= £20/mo traffic feasibility and Club-over-Amazon engagement.
- Invite-only on entry surfaces.
- GUID only after evidenced dual PASS.
- DNS TXT multi-provider walkthrough after GUID.
- Harvest MUST use honesty box `harvest-agent-skills` (PR to home repo).

## UNKNOWN

- Club Madeira API base URL, auth, GUID schema, TXT name/value template.
- Live commission % / cookie window (S2 coefficients stay ASSUMED until supplied).
- Whether Club re-checks TXT server-side before activate.
- Required legal disclosure copy from Club.
