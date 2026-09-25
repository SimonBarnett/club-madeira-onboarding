# Functional spec: club-madeira-onboarding

LOCKED pulled from `docs/vision.md`. Skill pack. Phase 0 is the pack
skeleton + gates contract.

## Phase 0

1. `.grok/skills/harvest-agent-skills/SKILL.md` — honesty box foundation;
   `github: https://github.com/SimonBarnett/club-madeira-onboarding`.
   Harvest is branch + PR only; never push main for harvest.
2. `docs/vision.md` + `docs/mocks/{home,empty,error}.html`.
3. Umbrella skill stub `club-madeira-onboarding` (invite-only, flow order,
   dual gate before GUID) — Phase 0 stub OK if vision is complete.
4. `docs/skill-harvest-log.md` started.

## Acceptance

| id | statement |
|----|-----------|
| A1 | Invite-only stated on umbrella skill and home mock. |
| A2 | Dual gates: traffic >= £20/mo feasibility; engagement Club-over-Amazon. |
| A3 | request-guid forbidden without dual PASS evidence. |
| A4 | After GUID: DNS TXT walkthrough via provider skills + verify. |
| A5 | Harvest MUST use honesty box harvest-agent-skills (PR to home repo). |
| A6 | `python tools/validate-vision-pack.py docs/vision.md --mocks-dir docs/mocks` exits 0. |

## UNKNOWN

- Club Madeira API and TXT record schema.
- Commission coefficients for live S2 formula.
