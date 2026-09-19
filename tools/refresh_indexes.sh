#!/bin/sh
# Rebuild the indexes the validator checks packs against, straight from the public
# repositories. Run this when either library gains or loses a skill.
#
# copilot-skills.txt holds discipline/skill paths rather than bare names, because the
# same file has to answer two questions: does this skill exist, and where does its
# link point. Two files would be two chances to disagree.
set -eu
cd "$(dirname "$0")/indexes"

api() { curl -sSf -H "Accept: application/vnd.github+json" "$1"; }

api "https://api.github.com/repos/kesslernity/awesome-copilot-agent-skills/git/trees/main?recursive=1" \
  | python3 -c "import json,sys,re;t=json.load(sys.stdin)['tree'];print('\n'.join(sorted({m.group(1) for p in t if (m:=re.fullmatch(r'skills/([^/]+/[^/]+)',p['path'])) and p['type']=='tree'})))" \
  > copilot-skills.txt

api "https://api.github.com/repos/kesslernity/awesome-mistral-vibe-skills/git/trees/main?recursive=1" \
  | python3 -c "import json,sys,re;t=json.load(sys.stdin)['tree'];print('\n'.join(sorted({m.group(1) for p in t if (m:=re.fullmatch(r'\.agents/skills/([^/]+)',p['path'])) and p['type']=='tree'})))" \
  > mistral-skills.txt

api "https://api.github.com/repos/kesslernity/awesome-mistral-vibe-prompts/git/trees/main?recursive=1" \
  | python3 -c "import json,sys,re;t=json.load(sys.stdin)['tree'];print('\n'.join(sorted({m.group(1) for p in t if (m:=re.fullmatch(r'prompts/scheduled/(.+\.md)',p['path'])) and p['type']=='blob'})))" \
  > mistral-scheduled.txt

# copilot-scheduled.txt holds the numbered headings of the single scheduled prompts
# README, in the order they appear, because a heading is what a deep link anchors to.
# This one reads the file rather than the tree: the prompts are sections, not files.
curl -sSf "https://raw.githubusercontent.com/kesslernity/awesome-microsoft-copilot-prompts/main/prompts/scheduled-prompts/README.md" \
  | python3 -c "import re,sys;print('\n'.join(re.findall(r'^### (\d+\..+?)\s*\$', sys.stdin.read(), re.M)))" \
  > copilot-scheduled.txt

api "https://api.github.com/repos/kesslernity/awesome-mistral-vibe-agents/git/trees/main?recursive=1" \
  | python3 -c "import json,sys,re;t=json.load(sys.stdin)['tree'];print('\n'.join(sorted({m.group(1) for p in t if (m:=re.fullmatch(r'\.vibe/agents/(.+)\.toml',p['path'])) and p['type']=='blob'})))" \
  > mistral-profiles.txt

wc -l ./*.txt
