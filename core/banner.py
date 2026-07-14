# core/banner.py
import time
import random
from rich.live import Live
from rich.text import Text
from rich.console import Console
from rich.style import Style as RichStyle

letters = {
    'B': [" ___  ", "| _ ) ", "| _ \\", "|___/ ", "      "],
    'L': ["_      ", "| |    ", "| |    ", "| |___ ", "|_____|"],
    'A': ["   _     ", "  / \\   ", " / _ \\  ", "/ ___ \\ ", "/_/   \\_\\"],
    'C': [" ____  ", "/ ___| ", "| |    ", "| |___ ", "\\____|"],
    'K': ["_  __ ", "| |/ /", "| ' / ", "| . \\ ", "|_|\\_\\"],
    'M': ["___  ", "|_ _|", " | | ", " | | ", "|___|"],
    'I': ["_   _ ", "| \\ | |", "|  \\| |", "| |\\  |", "|_| \\_|"],
    'N': ["____  ", "|  _ \\ ", "| | | |", "| |_| |", "|____/ "],
    'D': ["____  ", "|  _ \\ ", "| | | |", "| |_| |", "|____/ "]
}

color_of = {
    'B': 'cyan', 'L': 'red', 'A': 'yellow', 'C': 'green',
    'K': 'blue', 'M': 'magenta', 'I': 'white', 'N': 'cyan', 'D': 'cyan'
}

def build_banner_rich(word):
    height = 5
    lines = [Text() for _ in range(height)]
    for ch in word.upper():
        if ch not in letters:
            continue
        color = color_of.get(ch, 'white')
        art = letters[ch]
        for i in range(height):
            lines[i].append(art[i], style=RichStyle(color=color))
    return lines

def glitch_banner_rich(word="BLACKMIND", glitch_prob=0.2, sleep_range=(0.05, 0.2)):
    original_lines = build_banner_rich(word)
    glitch_chars = '!@#$%^&*()_+-=~`|\\/<>'
    console = Console()

    # Первоначальный вывод, чтобы баннер не пропадал в начале
    initial_frame = Text('\n').join(original_lines)

    with Live(console=console, screen=False, auto_refresh=True) as live:
        live.update(initial_frame)          # сразу показать баннер
        start_time = time.time()
        while time.time() - start_time < 3:
            new_lines = []
            for orig_line in original_lines:
                plain = orig_line.plain
                glitched = ''.join(
                    c if random.random() > glitch_prob else random.choice(glitch_chars)
                    for c in plain
                )
                if random.random() < 0.1:
                    glitched = ''.join(random.choices('01', k=len(plain)))
                new_line = Text(glitched, style=orig_line.style)
                new_lines.append(new_line)
            frame = Text('\n').join(new_lines)
            live.update(frame)
            time.sleep(random.uniform(*sleep_range))

    # После 3 секунд глитча оставляем чистый баннер на экране
    final_frame = Text('\n').join(original_lines)
    console.print(final_frame)