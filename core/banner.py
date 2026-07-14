# core/banner.py

import random
import time

from rich.console import Console
from rich.live import Live
from rich.style import Style
from rich.text import Text

console = Console()

letters = {
    "B": [
        "██████  ",
        "██   ██ ",
        "██████  ",
        "██   ██ ",
        "██████  ",
    ],
    "L": [
        "██      ",
        "██      ",
        "██      ",
        "██      ",
        "███████ ",
    ],
    "A": [
        " █████  ",
        "██   ██ ",
        "███████ ",
        "██   ██ ",
        "██   ██ ",
    ],
    "C": [
        " ██████ ",
        "██      ",
        "██      ",
        "██      ",
        " ██████ ",
    ],
    "K": [
        "██   ██ ",
        "██  ██  ",
        "█████   ",
        "██  ██  ",
        "██   ██ ",
    ],
    "M": [
        "███ ███ ",
        "███████ ",
        "██ █ ██ ",
        "██   ██ ",
        "██   ██ ",
    ],
    "I": [
        "███████ ",
        "   ██   ",
        "   ██   ",
        "   ██   ",
        "███████ ",
    ],
    "N": [
        "██   ██ ",
        "███  ██ ",
        "████ ██ ",
        "██ ████ ",
        "██  ███ ",
    ],
    "D": [
        "██████  ",
        "██   ██ ",
        "██   ██ ",
        "██   ██ ",
        "██████  ",
    ],
}

colors = {
    "B": "cyan",
    "L": "red",
    "A": "yellow",
    "C": "green",
    "K": "blue",
    "M": "magenta",
    "I": "white",
    "N": "bright_cyan",
    "D": "cyan",
}


def build_banner(word: str):
    height = 5
    result = [Text() for _ in range(height)]

    for letter in word.upper():
        art = letters[letter]
        color = colors.get(letter, "white")

        for i in range(height):
            result[i].append(
                art[i] + "  ",
                style=Style(color=color),
            )

    return result


def render(lines):
    return Text("\n").join(lines)


def shift_line(text: Text, amount: int):
    t = Text()

    if amount > 0:
        t.append(" " * amount)

    t.append(text)

    return t


def glitch_banner_rich(word="BLACKMIND"):
    original = build_banner(word)

    start = time.time()

    with Live(render(original), console=console, refresh_per_second=60, screen=False) as live:

        while time.time() - start < 2:

            frame = []

            for line in original:

                new_line = line.copy()

                # редко смещаем строку
                if random.random() < 0.12:
                    offset = random.randint(-4, 4)

                    if offset > 0:
                        new_line = shift_line(new_line, offset)

                frame.append(new_line)

            live.update(render(frame))

            # небольшая задержка
            time.sleep(random.uniform(0.04, 0.09))

        # финальный баннер остается навсегда
        live.update(render(original))