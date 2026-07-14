# core/banner.py

import random
import time

from rich.console import Console
from rich.live import Live
from rich.style import Style
from rich.text import Text

console = Console()

BANNER = r"""
:::::::::       :::                 :::           ::::::::       :::    :::      ::::    ::::       :::::::::::      ::::    :::      :::::::::  
:+:    :+:      :+:               :+: :+:        :+:    :+:      :+:   :+:       +:+:+: :+:+:+          :+:          :+:+:   :+:      :+:    :+: 
+:+    +:+      +:+              +:+   +:+       +:+             +:+  +:+        +:+ +:+:+ +:+          +:+          :+:+:+  +:+      +:+    +:+ 
+#++:++#+       +#+             +#++:++#++:      +#+             +#++:++         +#+  +:+  +#+          +#+          +#+ +:+ +#+      +#+    +:+ 
+#+    +#+      +#+             +#+     +#+      +#+             +#+  +#+        +#+       +#+          +#+          +#+  +#+#+#      +#+    +#+ 
#+#    #+#      #+#             #+#     #+#      #+#    #+#      #+#   #+#       #+#       #+#          #+#          #+#   #+#+#      #+#    #+# 
#########       ##########      ###     ###       ########       ###    ###      ###       ###      ###########      ###    ####      #########  
""".strip("\n")


def build_banner():
    """
    Возвращает список строк Rich Text.
    """
    return [
        Text(line, style=Style(color="bright_cyan"))
        for line in BANNER.splitlines()
    ]


def render(lines):
    return Text("\n").join(lines)


def glitch_banner_rich():
    """
    Показывает баннер.

    • 2 секунды случайные CRT-глитчи
    • затем баннер остаётся на экране
    """

    original = build_banner()

    start = time.time()

    with Live(
        render(original),
        console=console,
        refresh_per_second=60,
        screen=False,
        auto_refresh=False,
    ) as live:

        while time.time() - start < 2:

            frame = []

            for line in original:

                new_line = line.copy()

                # Иногда смещаем строку
                if random.random() < 0.12:

                    offset = random.randint(-5, 5)

                    if offset > 0:
                        new_line = Text(
                            " " * offset,
                            style=Style(color="bright_cyan"),
                        ) + new_line

                frame.append(new_line)

            live.update(render(frame))
            live.refresh()

            time.sleep(random.uniform(0.04, 0.08))

        # Финальный кадр остаётся
        live.update(render(original))
        live.refresh()