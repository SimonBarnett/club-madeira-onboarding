---
name: club-madeira-onboarding
description: >
  Invite-only Club Madeira affiliate onboarding via the human's agent:
  website review, dual gate (£20/mo traffic + Club-over-Amazon engagement),
  GUID request only after evidenced PASS, DNS TXT proof. Triggers: club
  madeira onboarding, affiliate invite, request guid, /club-madeira-onboarding.
---

# Club Madeira onboarding (umbrella)

**Invite-only.** Club Madeira affiliates are not open enrollment.

Foundation: harvest-agent-skills (honesty box) -> report back to
https://github.com/SimonBarnett/club-madeira-onboarding.

## Flow (strict)

1. Human loads this book into their own agent (scaffolded agent repo).
2. Website review tool scores the human's site -> `evidence/*.json`.
3. Human must convince the agent:
   - Traffic can support **>= £20 / month** affiliate-feasible revenue.
   - Visitors are engaged enough to buy via **Club Madeira** rather than
     Amazon directly.
4. Agent PASS only when **website evidence** supports the argument.
5. **Only then** call request-guid (Club Madeira API — URL UNKNOWN until
   Club supplies spec).
6. Walk DNS TXT add + verify via provider skills.
7. Harvest new DNS/gate learnings through honesty box (PR, not main).

## Do not

- Request a GUID without dual PASS evidence.
- Skip invite-only messaging.
- Push harvest to main.
- Invent API base URLs or secrets into git.
