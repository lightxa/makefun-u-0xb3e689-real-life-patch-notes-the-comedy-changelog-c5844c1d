"""Real-Life Patch Notes: The Comedy Changelog.

Writes the funniest one-line patch note for a bug in real life or
human biology to /output/entry.txt.

Chosen bug: hiccups. A hiccup is, in engineering terms, a retry loop
with no backoff and no max attempts: the diaphragm fires, fails to
settle, and fires again, indefinitely. That is the whole joke, stated
as a shipped fix. It beats the other candidates because the metaphor
is exact (not just the word "bug" dropped in), the wince is universal,
and the fix reads like a real release note. Revision: an earlier draft
said "retrying indefinitely with no backoff", but the fix never
addresses backoff, so those four words were cut; every remaining word
is answered by the punchline.
"""

from pathlib import Path

ENTRY = (
    "v1.4.2: fixed hiccups retrying indefinitely; "
    "diaphragm now gives up after three attempts."
)


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
