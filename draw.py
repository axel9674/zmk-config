from enum import Enum

KEY_W = 55
KEY_H = 55
KEY_RX = 6
KEY_RY = 6
INNER_PAD_W = 2
INNER_PAD_H = 2
OUTER_PAD_W = KEY_W / 2
OUTER_PAD_H = KEY_H / 2
LINE_SPACING = 18

STYLE = """
    svg {
        font-family: SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;
        font-size: 14px;
        font-kerning: normal;
        text-rendering: optimizeLegibility;
        fill: #24292e;
    }

    rect {
        fill: #f6f8fa;
    }

    .held {
        fill: #fdd;
    }
"""


class Size(Enum):
    s_0u = [0, 0]
    s_1u = [1, 1]
    s_2u_h = [2, 1]
    s_2u_v = [1, 2]


def held(key):
    return {"key": key, "class": "held"}


LAYOUT = [
    {
        "toprow": [
            [Size.s_1u, Size.s_1u, Size.s_1u, Size.s_1u],
        ],
        "numpad": [
            [Size.s_1u, Size.s_1u, Size.s_1u, Size.s_1u],
            [Size.s_1u, Size.s_1u, Size.s_1u, Size.s_2u_v],
            [Size.s_1u, Size.s_1u, Size.s_1u, Size.s_0u],
            [Size.s_1u, Size.s_1u, Size.s_1u, Size.s_2u_v],
            [Size.s_2u_h, Size.s_0u, Size.s_1u, Size.s_0u],
        ],
        "mods": [
            [Size.s_0u],
            [Size.s_0u],
            [Size.s_0u],
            [Size.s_1u],
            [Size.s_1u],
            [Size.s_1u],
        ],
    }
]


KEYMAP = [
    {
        "toprow": [
            ["f17", "f18", "f19", "f20"],
        ],
        "numpad": [
            ["bspc", "div", "mult", "minus"],
            ["7", "8", "9", "plus"],
            ["4", "5", "6", ""],
            ["1", "2", "3", "enter"],
            ["0", "", ".", ""],
        ],
        "mods": [
            [],
            [],
            [],
            ["mute"],
            ["rgb"],
            ["nav"],
        ],
    },
    {
        "toprow": [
            ["f17", "f18", "f19", "f20"],
        ],
        "numpad": [
            ["\\", "", "", ""],
            ["&lt;", "&gt;", "", ""],
            ["", "up", "", ""],
            ["left", "down", "right", ""],
            ["", "", "", ""],
        ],
        "mods": [
            [],
            [],
            [],
            ["mute"],
            ["default"],
            ["rgb"],
        ],
    },
    {
        "toprow": [
            ["f17", "f18", "f19", "f20"],
        ],
        "numpad": [
            ["rgb tog", "", "", ""],
            ["hue down", "hue up", "", ""],
            ["sat down", "sat up", "", ""],
            ["bri down", "bri up", "", ""],
            ["", "", "", ""],
        ],
        "mods": [
            [],
            [],
            [],
            ["mute"],
            ["nav"],
            ["default"],
        ],
    },
]

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
    if type(key) is dict:
        key_class = key["class"]
        key = key["key"]

    width = KEY_W * layout.value[0] + 4 * (layout.value[0] - 1)
    height = KEY_H * layout.value[1] + 4 * (layout.value[1] - 1)
    print(
        f'<rect rx="{KEY_RX}" ry="{KEY_RY}" x="{x + INNER_PAD_W}" y="{y + INNER_PAD_H}" width="{width}" height="{height}" class="{key_class}" />'
    )
    words = key.split()
    y += (KEYSPACE_H - (len(words) - 1) * LINE_SPACING) / 2
    for word in key.split():
        print(
            f'<text text-anchor="middle" dominant-baseline="middle" x="{x + KEYSPACE_W / 2}" y="{y}">{word}</text>'
        )
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


print(
    f'<svg width="{BOARD_W}" height="{BOARD_H}" viewBox="0 0 {BOARD_W} {BOARD_H}" xmlns="http://www.w3.org/2000/svg">'
)
print(f"<style>{STYLE}</style>")
print_board(0, 0, KEYMAP)
print("</svg>")
