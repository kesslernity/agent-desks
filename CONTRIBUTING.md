# Contributing

Short version: **do not edit `PACK.md`, `GATE.md` or `MANIFEST.json`.** They are generated and
the next run overwrites them.

## Where the text lives

One file per pack, `packs/<slug>/pack.toml`. Everything a reader sees is built from it.

| Change | Where |
|---|---|
| A role's summary, owner, cadence, skill list, scheduled routines | `packs/<slug>/pack.toml` |
| What a desk never decides, or what a person signs | The same file, in `never_decides` and `human_signs` |
| The evidence a signer needs, if the default three are not right for that desk | `evidence` in the same file |
| What to do when that desk gets something wrong | `when_wrong` in the same file |
| The wording around the generated tables, or a new section | `tools/build.py` |
| A rule the validator should enforce | `tools/build.py`, with a case in `tools/test_build.py` |

## The loop

```sh
sh tools/refresh_indexes.sh     # only when a library gained or lost a skill
python3 tools/build.py
python3 tools/build.py --check
python3 tools/test_build.py
```

Commit the TOML and the generated files together. The generated tree is checked in on purpose:
people read this repository on github.com, and a page that only exists after you run a script
is not a page.

## Adding a pack

Copy an existing `pack.toml`, change every field, and run the build. It will stop if you have
named a skill that does not exist in both libraries, a scheduled prompt that is not in the
prompts repository, or a profile that is not in the agents repository. Two things it cannot
check for you:

- **An owner who is a role, not a person.** "The service desk lead" is an owner. "IT" is not.
- **A `never_decides` list that only contains things the desk was never going to do anyway.**
  If every line is obvious, the pack has not been thought about. The useful lines are the ones
  where somebody would plausibly have let the agent decide.

## A pack with no scheduled routines is fine

Two of the nine have none. A timer on a desk that has nothing to do produces output nobody
asked for, and the fastest way to get people to stop reading agent output is to send them some
every morning whether or not anything happened. Leave `scheduled` empty and say why in the
summary.

## House rules the text keeps

- **Every output is a draft.** No pack approves, authorises, signs off or decides.
- **Nothing is a safety authorisation.** No permit to work, isolation, confined space entry,
  job safety analysis, incident classification or inspection sign-off. AI prepares, a qualified
  human decides.
- **No pack decides anything about a named person.** Hiring, rating, pay, conduct and exit are
  human decisions, and the HR pack is deliberately the most restricted one here.
- No em dashes.

## If you add a rule to the validator

Add the case to `tools/test_build.py` in the same commit. It builds a deliberately broken pack
per rule and asserts the validator rejects it, plus a correct one it must pass. A checker with
no failing case is a checker nobody has proven runs.

## Licence

Contributions are accepted under CC BY-SA 4.0, the licence this repository ships under.
