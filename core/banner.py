import time
import random
from colorama import init, Fore, Back, Style

init(autoreset=True)

# --- Твои буквы (ровно те, что в комментарии) ---
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

# Цвета по буквам (можно менять)
color_of = {
    'B': Fore.CYAN,
    'L': Fore.RED,
    'A': Fore.YELLOW,
    'C': Fore.GREEN,
    'K': Fore.BLUE,
    'M': Fore.MAGENTA,
    'I': Fore.WHITE,
    'N': Fore.CYAN,
    'D': Fore.CYAN
}

def build_banner(word, letter_height=5):
    """Собирает слово из больших букв в одну строку (с цветом)."""
    lines = ["" for _ in range(letter_height)]
    for ch in word.upper():
        if ch not in letters:
            continue
        color = color_of.get(ch, '')
        art = letters[ch]
        for i in range(letter_height):
            lines[i] += f"{color}{art[i]}{Style.RESET_ALL}"
    return lines   # возвращаем список строк, а не одну строку с \n

# ---------- Глитч-анимация баннера ----------
def glitch_banner(word="BLACKMIND", glitch_prob=0.2, sleep_range=(0.05, 0.2)):
    original_lines = build_banner(word)
    height = len(original_lines)
    max_width = max(len(line) for line in original_lines)

    # Скрываем курсор (может не сработать в cmd, но не мешает)
    print('\033[?25l', end='')

    glitch_chars = '!@#$%^&*()_+-=~`|\\/<>'

    # Первый кадр рисуем без лишних движений
    for line in original_lines:
        print(line)

    try:
        while True:
            # Поднимаемся на height строк вверх, чтобы оказаться в начале баннера
            print(f"\033[{height}A", end='')

            for line in original_lines:
                glitched = ''.join(
                    c if random.random() > glitch_prob
                    else random.choice(glitch_chars)
                    for c in line
                )
                shift = random.randint(0, 3)
                bg = random.choice([Back.BLACK, Back.RED, Back.GREEN, Back.BLUE])
                if random.random() < 0.1:
                    glitched = ''.join(random.choices('01', k=len(line)))
                output = " " * shift + f"{bg}{glitched}{Style.RESET_ALL}"
                # Дополняем до max_width + shift, чтобы затирать предыдущий кадр
                output = output.ljust(max_width + shift)
                print(output)

            time.sleep(random.uniform(*sleep_range))
    except KeyboardInterrupt:
        # Спускаемся на height строк вниз (чтобы не остаться внутри баннера)
        print(f"\033[{height}B", end='')
        print('\033[?25h', end='')   # показать курсор
        print("\nГлитч остановлен.")