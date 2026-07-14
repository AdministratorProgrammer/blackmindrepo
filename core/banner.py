# core/banner.py

import random
import time

from rich.console import Console
from rich.live import Live
from rich.style import Style
from rich.text import Text

console = Console()

BANNER = r"""
  ___   _        _      ___   _  __  __  __   ___   _  _   ___
 | _ ) | |      /_\    / __| | |/ / |  \/  | |_ _| | \| | |   \
 | _ \ | |__   / _ \  | (__  | ' <  | |\/| |  | |  | .` | | |) |
 |___/ |____| /_/ \_\  \___| |_|\_\ |_|  |_| |___| |_|\_| |___/
""".strip("\n")


def build_banner():
    """
    Создаёт баннер.
    """
    return [
        Text(line, style=Style(color="bright_cyan"))
        for line in BANNER.splitlines()
    ]


def render(lines):
    """
    Собирает список строк в один объект Rich Text.
    """
    return Text("\n").join(lines)


def glitch_banner_rich():
    """
    Показывает баннер с редкими глитчами в течение 2 секунд.
    После окончания анимации баннер остаётся на экране.
    """

    original = build_banner()

    start_time = time.time()

    with Live(
        render(original),
        console=console,
        screen=False,
        auto_refresh=False,
        refresh_per_second=60,
    ) as live:

        while time.time() - start_time < 2:

            frame = []

            glitch_now = random.random() < 0.25

            for line in original:

                new_line = line.copy()

                if glitch_now and random.random() < 0.4:

                    shift = random.randint(1, 6)

                    new_line = (
                        Text(
                            " " * shift,
                            style=Style(color="bright_cyan")
                        )
                        + new_line
                    )

                frame.append(new_line)

            live.update(render(frame))
            live.refresh()

            time.sleep(random.uniform(0.05, 0.10))

        # Финальный кадр без глитчей
        live.update(render(original))
        live.refresh()