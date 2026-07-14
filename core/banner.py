import time
import random
from rich.live import Live
from rich.text import Text
from rich.console import Console
from rich.style import Style as RichStyle

# Буквы остаются твои, без ANSI-кодов
letters = {
    'B': [
        " ___  ",
        "| _ ) ",
        "| _ \\",
        "|___/ ",
        "      "
    ],
    'L': [
        "_      ",
        "| |    ",
        "| |    ",
        "| |___ ",
        "|_____|"
    ],
    'A': [
        "   _     ",
        "  / \\   ",
        " / _ \\  ",
        "/ ___ \\ ",
        "/_/   \\_\\"
    ],
    'C': [
        " ____  ",
        "/ ___| ",
        "| |    ",
        "| |___ ",
        "\\____|"
    ],
    'K': [
        "_  __ ",
        "| |/ /",
        "| ' / ",
        "| . \\ ",
        "|_|\\_\\"
    ],
    'M': [
        "___  ",
        "|_ _|",
        " | | ",
        " | | ",
        "|___|"
    ],
    'I': [
        "_   _ ",
        "| \\ | |",
        "|  \\| |",
        "| |\\  |",
        "|_| \\_|"
    ],
    'N': [
        "____  ",
        "|  _ \\ ",
        "| | | |",
        "| |_| |",
        "|____/ "
    ],
    'D': [
        "____  ",
        "|  _ \\ ",
        "| | | |",
        "| |_| |",
        "|____/ "
    ]
}

# Цвета для rich (названия цветов или hex)
color_of = {
    'B': 'cyan',
    'L': 'red',
    'A': 'yellow',
    'C': 'green',
    'K': 'blue',
    'M': 'magenta',
    'I': 'white',
    'N': 'cyan',
    'D': 'cyan'
}

def build_banner_rich(word):
    """Собирает баннер как список Rich Text объектов (по одному на строку)."""
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

    # Live auto_refresh=False позволяет обновлять экран только когда мы сами захотим
    with Live(console=console, screen=False, auto_refresh=False) as live:
        while True:
            new_lines = []
            for orig_line in original_lines:
                # Получаем чистый текст без стилей
                plain = orig_line.plain
                # Заменяем символы
                glitched = ''.join(
                    c if random.random() > glitch_prob else random.choice(glitch_chars)
                    for c in plain
                )
                # Иногда полная замена на 0/1
                if random.random() < 0.1:
                    glitched = ''.join(random.choices('01', k=len(plain)))
                # Сохраняем оригинальный стиль строки (или можно рандомизировать фон)
                new_line = Text(glitched, style=orig_line.style)
                new_lines.append(new_line)
            # Собираем один Text с переносами строк и обновляем
            frame = Text('\n').join(new_lines)
            live.update(frame)
            time.sleep(random.uniform(*sleep_range))