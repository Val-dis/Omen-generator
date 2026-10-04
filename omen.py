#!/usr/bin/env python3
"""omen: a tiny cryptic fortune generator."""
import argparse
import random

SUBJECTS = [
    "the candle", "a pale visitor", "the third bell", "your reflection",
    "the old cathedral", "a raven", "the quiet hour", "the moon",
    "someone you forgot", "the door at the end of the hall",
]
VERBS = [
    "remembers", "refuses", "waits for", "forgives",
    "counts", "carries", "mourns", "answers to",
]
OBJECTS = [
    "your name", "what you buried", "the last of the light", "a debt you owe",
    "the shape of your grief", "tomorrow", "the thing you never said",
    "a name you stopped using",
]
CLOSERS = [
    "do not look back.", "it will pass.", "sleep anyway.", "light one candle.",
    "the dark is not your enemy.", "you are still here.", "rest when you can.",
    "begin again at dawn.",
]


def omen(rng: random.Random) -> str:
    subject = rng.choice(SUBJECTS)
    verb = rng.choice(VERBS)
    obj = rng.choice(OBJECTS)
    closer = rng.choice(CLOSERS)
    return f"{subject.capitalize()} {verb} {obj}. {closer.capitalize()}"


def main() -> None:
    parser = argparse.ArgumentParser(description="draw an omen from the dark.")
    parser.add_argument("-n", "--count", type=int, default=1, help="how many omens")
    parser.add_argument("--seed", type=int, default=None, help="same seed, same omens")
    args = parser.parse_args()

    rng = random.Random(args.seed)
    for _ in range(max(1, args.count)):
        print(omen(rng))


if __name__ == "__main__":
    main()
