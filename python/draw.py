from layout import *
from keymap import *

KEY_W = 55
KEY_H = 55
KEY_RX = 6
KEY_RY = 6
INNER_PAD_W = 2
INNER_PAD_H = 2
OUTER_PAD_W = KEY_W / 2
OUTER_PAD_H = KEY_H / 2
LINE_SPACING = 18
FONT_SIZE = 12

STYLE = f"""
    svg {{
        font-family: SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;
        font-size: {FONT_SIZE}px;
        font-kerning: normal;
        text-rendering: optimizeLegibility;
        fill: #fdd;
    }}

    rect {{
        fill: #24292e;
    }}

    .inverse {{
        fill: #fdd;
    }}
    
    .text_inverted {{
        fill: #24292e;
    }}
"""


KEYSPACE_W = KEY_W + 2 * INNER_PAD_W
KEYSPACE_H = KEY_H + 2 * INNER_PAD_H
HAND_W = 5 * KEYSPACE_W
HAND_H = 7 * KEYSPACE_H
LAYER_W = 2 * HAND_W + OUTER_PAD_W
LAYER_H = HAND_H
BOARD_W = LAYER_W + OUTER_PAD_W
BOARD_H = len(KEYMAP) * LAYER_H + 5 * OUTER_PAD_H


def print_key(x, y, key, layout):
    key_class = ""
    text_class = ""
    if type(key) is dict:
        key_class = key["class"]
        text_class = "text_inverted" if key_class != "" else ""
        key = key["key"]

    width = KEY_W * layout.value[0] + 4 * (layout.value[0] - 1)
    height = KEY_H * layout.value[1] + 4 * (layout.value[1] - 1)
    file.write(f'<rect rx="{KEY_RX}" ry="{KEY_RY}" x="{x + INNER_PAD_W}" y="{y + INNER_PAD_H}" width="{width}" height="{height}" class="{key_class}" />')
    words = key.split()
    y += (height + 2 * INNER_PAD_H - (len(words) - 1) * LINE_SPACING + FONT_SIZE / 2) / 2
    x += (width + 2 * INNER_PAD_W) / 2
    for word in key.split():
        file.write(f'<text text-anchor="middle" dominant-baseline="middle" x="{x}" y="{y}" class="{text_class}">{word}</text>')
        y += LINE_SPACING


def print_row(x, y, row, layout):
    for i in range(len(row)):
        if layout[i] is not Size.s_0u:
            print_key(x, y, row[i], layout[i])
        x += KEYSPACE_W


def print_block(x, y, block, layout):
    for i in range(len(block)):
        print_row(x, y, block[i], layout[i])
        y += KEYSPACE_H


def print_layer(x, y, layer, layout):
    print_block(x, y + .5 * KEYSPACE_H, layer["mods"], layout["mods"])
    print_block(
        x + 1.5 * KEYSPACE_W, y, layer["toprow"], layout["toprow"]
    )
    print_block(
        x + 1.5 * KEYSPACE_W, y + 1.5 * KEYSPACE_H, layer["numpad"], layout["numpad"]
    )


def print_board(x, y, keymap):
    x += OUTER_PAD_W
    for layer in keymap:
        y += OUTER_PAD_H
        print_layer(x, y, layer, LAYOUT[0])
        y += LAYER_H


file = open("keymap.svg", "w")
file.write(f'<svg width="{BOARD_W}" height="{BOARD_H}" viewBox="0 0 {BOARD_W} {BOARD_H}" xmlns="http://www.w3.org/2000/svg">')
file.write(f"<style>{STYLE}</style>")
print_board(0, 0, KEYMAP)
file.write("</svg>")
file.close()
