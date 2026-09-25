"""MRB tests for harvest-agent-skills CAST IRON auto-harvest (PR #2)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".grok" / "skills" / "harvest-agent-skills" / "SKILL.md"


def test_harvest_skill_exists():
    assert SKILL.is_file()


def test_frontmatter_home_is_this_repo():
    text = SKILL.read_text(encoding="utf-8")
    assert "github: https://github.com/SimonBarnett/club-madeira-onboarding" in text


def test_automatic_harvest_cast_iron_section():
    text = SKILL.read_text(encoding="utf-8")
    assert "## AUTOMATIC harvest (CAST IRON - no waiting)" in text
    assert "MUST ALWAYS harvest" in text
    assert "AUTOMATICALLY in the same turn" in text
    assert "Do not ask permission" in text
    assert "Do not defer" in text


def test_harvest_path_is_branch_pr_not_main():
    text = SKILL.read_text(encoding="utf-8")
    assert "Branch + PR" in text or "branch + **pull" in text.lower() or "branch + pull" in text.lower()
    assert "never push main" in text.lower() or "Never `git push origin main`" in text


def test_blocked_pr_opens_harvest_or_fr_issue_same_turn():
    text = SKILL.read_text(encoding="utf-8")
    assert "harvest:" in text
    assert "FR:" in text
    assert "same turn" in text.lower()


def test_empty_harvest_only_when_nothing_new():
    text = SKILL.read_text(encoding="utf-8")
    assert "Empty harvest only when nothing new" in text
