from enum import Enum


class Size(Enum):
    s_0u = [0, 0]
    s_1u = [1, 1]
    s_2u_h = [2, 1]
    s_2u_v = [1, 2]


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