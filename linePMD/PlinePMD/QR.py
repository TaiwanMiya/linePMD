from __future__ import absolute_import, division, print_function, with_statement, unicode_literals
from PlinePMD.Png import *
from PlinePMD.Canvas import Name
from PlinePMD.CryptoApi import CryptoCanvas
import io
import itertools
import math
modes = {
    'numeric': 1,
    'alphanumeric': 2,
    'binary': 4,
    'kanji': 8,
}
error_level = {'L': 'L', 'l': 'L', '7%': 'L', .7: 'L',
               'M': 'M', 'm': 'M', '15%': 'M', .15: 'M',
               'Q': 'Q', 'q': 'Q', '25%': 'Q', .25: 'Q',
               'H': 'H', 'h': 'H', '30%': 'H', .30: 'H'}
data_length_field = {9: {1: 10, 2: 9, 4: 8, 8: 8},
                     26: {1: 12, 2: 11, 4: 16, 8: 10},
                     40: {1: 14, 2: 13, 4: 16, 8: 12}}
ascii_codes = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
               'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21,
               'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28,
               'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35,
               ' ': 36, '$': 37, '%': 38, '*': 39, '+': 40, '-': 41, '.': 42,
               '/': 43, ':': 44}
version_size = [None, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57,
                61, 65, 69, 73, 77, 81, 85, 89, 93, 97,
                101, 105, 109, 113, 117, 121, 125, 129, 133, 137,
                141, 145, 149, 153, 157, 161, 165, 169, 173, 177]
data_capacitys = {
    1: {
        "L": {0: 152, 1: 41, 2: 25, 4: 17, 8: 10, },
        "M": {0: 128, 1: 34, 2: 20, 4: 14, 8: 8, },
        "Q": {0: 104, 1: 27, 2: 16, 4: 11, 8: 7, },
        "H": {0: 72, 1: 17, 2: 10, 4: 7, 8: 4, }},
    2: {
        "L": {0: 272, 1: 77, 2: 47, 4: 32, 8: 20, },
        "M": {0: 224, 1: 63, 2: 38, 4: 26, 8: 16, },
        "Q": {0: 176, 1: 48, 2: 29, 4: 20, 8: 12, },
        "H": {0: 128, 1: 34, 2: 20, 4: 14, 8: 8, }},
    3: {
        "L": {0: 440, 1: 127, 2: 77, 4: 53, 8: 32, },
        "M": {0: 352, 1: 101, 2: 61, 4: 42, 8: 26, },
        "Q": {0: 272, 1: 77, 2: 47, 4: 32, 8: 20, },
        "H": {0: 208, 1: 58, 2: 35, 4: 24, 8: 15, }},
    4: {
        "L": {0: 640, 1: 187, 2: 114, 4: 78, 8: 48, },
        "M": {0: 512, 1: 149, 2: 90, 4: 62, 8: 38, },
        "Q": {0: 384, 1: 111, 2: 67, 4: 46, 8: 28, },
        "H": {0: 288, 1: 82, 2: 50, 4: 34, 8: 21, }},
    5: {
        "L": {0: 864, 1: 255, 2: 154, 4: 106, 8: 65, },
        "M": {0: 688, 1: 202, 2: 122, 4: 84, 8: 52, },
        "Q": {0: 496, 1: 144, 2: 87, 4: 60, 8: 37, },
        "H": {0: 368, 1: 106, 2: 64, 4: 44, 8: 27, }},
    6: {
        "L": {0: 1088, 1: 322, 2: 195, 4: 134, 8: 82, },
        "M": {0: 864, 1: 255, 2: 154, 4: 106, 8: 65, },
        "Q": {0: 608, 1: 178, 2: 108, 4: 74, 8: 45, },
        "H": {0: 480, 1: 139, 2: 84, 4: 58, 8: 36, }},
    7: {
        "L": {0: 1248, 1: 370, 2: 224, 4: 154, 8: 95, },
        "M": {0: 992, 1: 293, 2: 178, 4: 122, 8: 75, },
        "Q": {0: 704, 1: 207, 2: 125, 4: 86, 8: 53, },
        "H": {0: 528, 1: 154, 2: 93, 4: 64, 8: 39, }},
    8: {
        "L": {0: 1552, 1: 461, 2: 279, 4: 192, 8: 118, },
        "M": {0: 1232, 1: 365, 2: 221, 4: 152, 8: 93, },
        "Q": {0: 880, 1: 259, 2: 157, 4: 108, 8: 66, },
        "H": {0: 688, 1: 202, 2: 122, 4: 84, 8: 52, }},
    9: {
        "L": {0: 1856, 1: 552, 2: 335, 4: 230, 8: 141, },
        "M": {0: 1456, 1: 432, 2: 262, 4: 180, 8: 111, },
        "Q": {0: 1056, 1: 312, 2: 189, 4: 130, 8: 80, },
        "H": {0: 800, 1: 235, 2: 143, 4: 98, 8: 60, }},
    10: {
        "L": {0: 2192, 1: 652, 2: 395, 4: 271, 8: 167, },
        "M": {0: 1728, 1: 513, 2: 311, 4: 213, 8: 131, },
        "Q": {0: 1232, 1: 364, 2: 221, 4: 151, 8: 93, },
        "H": {0: 976, 1: 288, 2: 174, 4: 119, 8: 74, }},
    11: {
        "L": {0: 2592, 1: 772, 2: 468, 4: 321, 8: 198, },
        "M": {0: 2032, 1: 604, 2: 366, 4: 251, 8: 155, },
        "Q": {0: 1440, 1: 427, 2: 259, 4: 177, 8: 109, },
        "H": {0: 1120, 1: 331, 2: 200, 4: 137, 8: 85, }},
    12: {
        "L": {0: 2960, 1: 883, 2: 535, 4: 367, 8: 226, },
        "M": {0: 2320, 1: 691, 2: 419, 4: 287, 8: 177, },
        "Q": {0: 1648, 1: 489, 2: 296, 4: 203, 8: 125, },
        "H": {0: 1264, 1: 374, 2: 227, 4: 155, 8: 96, }},
    13: {
        "L": {0: 3424, 1: 1022, 2: 619, 4: 425, 8: 262, },
        "M": {0: 2672, 1: 796, 2: 483, 4: 331, 8: 204, },
        "Q": {0: 1952, 1: 580, 2: 352, 4: 241, 8: 149, },
        "H": {0: 1440, 1: 427, 2: 259, 4: 177, 8: 109, }},
    14: {
        "L": {0: 3688, 1: 1101, 2: 667, 4: 458, 8: 282, },
        "M": {0: 2920, 1: 871, 2: 528, 4: 362, 8: 223, },
        "Q": {0: 2088, 1: 621, 2: 376, 4: 258, 8: 159, },
        "H": {0: 1576, 1: 468, 2: 283, 4: 194, 8: 120, }},
    15: {
        "L": {0: 4184, 1: 1250, 2: 758, 4: 520, 8: 320, },
        "M": {0: 3320, 1: 991, 2: 600, 4: 412, 8: 254, },
        "Q": {0: 2360, 1: 703, 2: 426, 4: 292, 8: 180, },
        "H": {0: 1784, 1: 530, 2: 321, 4: 220, 8: 136, }},
    16: {
        "L": {0: 4712, 1: 1408, 2: 854, 4: 586, 8: 361, },
        "M": {0: 3624, 1: 1082, 2: 656, 4: 450, 8: 277, },
        "Q": {0: 2600, 1: 775, 2: 470, 4: 322, 8: 198, },
        "H": {0: 2024, 1: 602, 2: 365, 4: 250, 8: 154, }},
    17: {
        "L": {0: 5176, 1: 1548, 2: 938, 4: 644, 8: 397, },
        "M": {0: 4056, 1: 1212, 2: 734, 4: 504, 8: 310, },
        "Q": {0: 2936, 1: 876, 2: 531, 4: 364, 8: 224, },
        "H": {0: 2264, 1: 674, 2: 408, 4: 280, 8: 173, }},
    18: {
        "L": {0: 5768, 1: 1725, 2: 1046, 4: 718, 8: 442, },
        "M": {0: 4504, 1: 1346, 2: 816, 4: 560, 8: 345, },
        "Q": {0: 3176, 1: 948, 2: 574, 4: 394, 8: 243, },
        "H": {0: 2504, 1: 746, 2: 452, 4: 310, 8: 191, }},
    19: {
        "L": {0: 6360, 1: 1903, 2: 1153, 4: 792, 8: 488, },
        "M": {0: 5016, 1: 1500, 2: 909, 4: 624, 8: 384, },
        "Q": {0: 3560, 1: 1063, 2: 644, 4: 442, 8: 272, },
        "H": {0: 2728, 1: 813, 2: 493, 4: 338, 8: 208, }},
    20: {
        "L": {0: 6888, 1: 2061, 2: 1249, 4: 858, 8: 528, },
        "M": {0: 5352, 1: 1600, 2: 970, 4: 666, 8: 410, },
        "Q": {0: 3880, 1: 1159, 2: 702, 4: 482, 8: 297, },
        "H": {0: 3080, 1: 919, 2: 557, 4: 382, 8: 235, }},
    21: {
        "L": {0: 7456, 1: 2232, 2: 1352, 4: 929, 8: 572, },
        "M": {0: 5712, 1: 1708, 2: 1035, 4: 711, 8: 438, },
        "Q": {0: 4096, 1: 1224, 2: 742, 4: 509, 8: 314, },
        "H": {0: 3248, 1: 969, 2: 587, 4: 403, 8: 248, }},
    22: {
        "L": {0: 8048, 1: 2409, 2: 1460, 4: 1003, 8: 618, },
        "M": {0: 6256, 1: 1872, 2: 1134, 4: 779, 8: 480, },
        "Q": {0: 4544, 1: 1358, 2: 823, 4: 565, 8: 348, },
        "H": {0: 3536, 1: 1056, 2: 640, 4: 439, 8: 270, }},
    23: {
        "L": {0: 8752, 1: 2620, 2: 1588, 4: 1091, 8: 672, },
        "M": {0: 6880, 1: 2059, 2: 1248, 4: 857, 8: 528, },
        "Q": {0: 4912, 1: 1468, 2: 890, 4: 611, 8: 376, },
        "H": {0: 3712, 1: 1108, 2: 672, 4: 461, 8: 284, }},
    24: {
        "L": {0: 9392, 1: 2812, 2: 1704, 4: 1171, 8: 721, },
        "M": {0: 7312, 1: 2188, 2: 1326, 4: 911, 8: 561, },
        "Q": {0: 5312, 1: 1588, 2: 963, 4: 661, 8: 407, },
        "H": {0: 4112, 1: 1228, 2: 744, 4: 511, 8: 315, }},
    25: {
        "L": {0: 10208, 1: 3057, 2: 1853, 4: 1273, 8: 784, },
        "M": {0: 8000, 1: 2395, 2: 1451, 4: 997, 8: 614, },
        "Q": {0: 5744, 1: 1718, 2: 1041, 4: 715, 8: 440, },
        "H": {0: 4304, 1: 1286, 2: 779, 4: 535, 8: 330, }},
    26: {
        "L": {0: 10960, 1: 3283, 2: 1990, 4: 1367, 8: 842, },
        "M": {0: 8496, 1: 2544, 2: 1542, 4: 1059, 8: 652, },
        "Q": {0: 6032, 1: 1804, 2: 1094, 4: 751, 8: 462, },
        "H": {0: 4768, 1: 1425, 2: 864, 4: 593, 8: 365, }},
    27: {
        "L": {0: 11744, 1: 3514, 2: 2132, 4: 1465, 8: 902, },
        "M": {0: 9024, 1: 2701, 2: 1637, 4: 1125, 8: 692, },
        "Q": {0: 6464, 1: 1933, 2: 1172, 4: 805, 8: 496, },
        "H": {0: 5024, 1: 1501, 2: 910, 4: 625, 8: 385, }},
    28: {
        "L": {0: 12248, 1: 3669, 2: 2223, 4: 1528, 8: 940, },
        "M": {0: 9544, 1: 2857, 2: 1732, 4: 1190, 8: 732, },
        "Q": {0: 6968, 1: 2085, 2: 1263, 4: 868, 8: 534, },
        "H": {0: 5288, 1: 1581, 2: 958, 4: 658, 8: 405, }},
    29: {
        "L": {0: 13048, 1: 3909, 2: 2369, 4: 1628, 8: 1002, },
        "M": {0: 10136, 1: 3035, 2: 1839, 4: 1264, 8: 778, },
        "Q": {0: 7288, 1: 2181, 2: 1322, 4: 908, 8: 559, },
        "H": {0: 5608, 1: 1677, 2: 1016, 4: 698, 8: 430, }},
    30: {
        "L": {0: 13880, 1: 4158, 2: 2520, 4: 1732, 8: 1066, },
        "M": {0: 10984, 1: 3289, 2: 1994, 4: 1370, 8: 843, },
        "Q": {0: 7880, 1: 2358, 2: 1429, 4: 982, 8: 604, },
        "H": {0: 5960, 1: 1782, 2: 1080, 4: 742, 8: 457, }},
    31: {
        "L": {0: 14744, 1: 4417, 2: 2677, 4: 1840, 8: 1132, },
        "M": {0: 11640, 1: 3486, 2: 2113, 4: 1452, 8: 894, },
        "Q": {0: 8264, 1: 2473, 2: 1499, 4: 1030, 8: 634, },
        "H": {0: 6344, 1: 1897, 2: 1150, 4: 790, 8: 486, }},
    32: {
        "L": {0: 15640, 1: 4686, 2: 2840, 4: 1952, 8: 1201, },
        "M": {0: 12328, 1: 3693, 2: 2238, 4: 1538, 8: 947, },
        "Q": {0: 8920, 1: 2670, 2: 1618, 4: 1112, 8: 684, },
        "H": {0: 6760, 1: 2022, 2: 1226, 4: 842, 8: 518, }},
    33: {
        "L": {0: 16568, 1: 4965, 2: 3009, 4: 2068, 8: 1273, },
        "M": {0: 13048, 1: 3909, 2: 2369, 4: 1628, 8: 1002, },
        "Q": {0: 9368, 1: 2805, 2: 1700, 4: 1168, 8: 719, },
        "H": {0: 7208, 1: 2157, 2: 1307, 4: 898, 8: 553, }},
    34: {
        "L": {0: 17528, 1: 5253, 2: 3183, 4: 2188, 8: 1347, },
        "M": {0: 13800, 1: 4134, 2: 2506, 4: 1722, 8: 1060, },
        "Q": {0: 9848, 1: 2949, 2: 1787, 4: 1228, 8: 756, },
        "H": {0: 7688, 1: 2301, 2: 1394, 4: 958, 8: 590, }},
    35: {
        "L": {0: 18448, 1: 5529, 2: 3351, 4: 2303, 8: 1417, },
        "M": {0: 14496, 1: 4343, 2: 2632, 4: 1809, 8: 1113, },
        "Q": {0: 10288, 1: 3081, 2: 1867, 4: 1283, 8: 790, },
        "H": {0: 7888, 1: 2361, 2: 1431, 4: 983, 8: 605, }},
    36: {
        "L": {0: 19472, 1: 5836, 2: 3537, 4: 2431, 8: 1496, },
        "M": {0: 15312, 1: 4588, 2: 2780, 4: 1911, 8: 1176, },
        "Q": {0: 10832, 1: 3244, 2: 1966, 4: 1351, 8: 832, },
        "H": {0: 8432, 1: 2524, 2: 1530, 4: 1051, 8: 647, }},
    37: {
        "L": {0: 20528, 1: 6153, 2: 3729, 4: 2563, 8: 1577, },
        "M": {0: 15936, 1: 4775, 2: 2894, 4: 1989, 8: 1224, },
        "Q": {0: 11408, 1: 3417, 2: 2071, 4: 1423, 8: 876, },
        "H": {0: 8768, 1: 2625, 2: 1591, 4: 1093, 8: 673, }},
    38: {
        "L": {0: 21616, 1: 6479, 2: 3927, 4: 2699, 8: 1661, },
        "M": {0: 16816, 1: 5039, 2: 3054, 4: 2099, 8: 1292, },
        "Q": {0: 12016, 1: 3599, 2: 2181, 4: 1499, 8: 923, },
        "H": {0: 9136, 1: 2735, 2: 1658, 4: 1139, 8: 701, }},
    39: {
        "L": {0: 22496, 1: 6743, 2: 4087, 4: 2809, 8: 1729, },
        "M": {0: 17728, 1: 5313, 2: 3220, 4: 2213, 8: 1362, },
        "Q": {0: 12656, 1: 3791, 2: 2298, 4: 1579, 8: 972, },
        "H": {0: 9776, 1: 2927, 2: 1774, 4: 1219, 8: 750, }},
    40: {
        "L": {0: 23648, 1: 7089, 2: 4296, 4: 2953, 8: 1817, },
        "M": {0: 18672, 1: 5596, 2: 3391, 4: 2331, 8: 1435, },
        "Q": {0: 13328, 1: 3993, 2: 2420, 4: 1663, 8: 1024, },
        "H": {0: 10208, 1: 3057, 2: 1852, 4: 1273, 8: 784, }}
}
eccwbi = {
    1: {
        'L': [7, 1, 19, 0, 0, ],
        'M': [10, 1, 16, 0, 0, ],
        'Q': [13, 1, 13, 0, 0, ],
        'H': [17, 1, 9, 0, 0, ],
    },
    2: {
        'L': [10, 1, 34, 0, 0, ],
        'M': [16, 1, 28, 0, 0, ],
        'Q': [22, 1, 22, 0, 0, ],
        'H': [28, 1, 16, 0, 0, ],
    },
    3: {
        'L': [15, 1, 55, 0, 0, ],
        'M': [26, 1, 44, 0, 0, ],
        'Q': [18, 2, 17, 0, 0, ],
        'H': [22, 2, 13, 0, 0, ],
    },
    4: {
        'L': [20, 1, 80, 0, 0, ],
        'M': [18, 2, 32, 0, 0, ],
        'Q': [26, 2, 24, 0, 0, ],
        'H': [16, 4, 9, 0, 0, ],
    },
    5: {
        'L': [26, 1, 108, 0, 0, ],
        'M': [24, 2, 43, 0, 0, ],
        'Q': [18, 2, 15, 2, 16, ],
        'H': [22, 2, 11, 2, 12, ],
    },
    6: {
        'L': [18, 2, 68, 0, 0, ],
        'M': [16, 4, 27, 0, 0, ],
        'Q': [24, 4, 19, 0, 0, ],
        'H': [28, 4, 15, 0, 0, ],
    },
    7: {
        'L': [20, 2, 78, 0, 0, ],
        'M': [18, 4, 31, 0, 0, ],
        'Q': [18, 2, 14, 4, 15, ],
        'H': [26, 4, 13, 1, 14, ],
    },
    8: {
        'L': [24, 2, 97, 0, 0, ],
        'M': [22, 2, 38, 2, 39, ],
        'Q': [22, 4, 18, 2, 19, ],
        'H': [26, 4, 14, 2, 15, ],
    },
    9: {
        'L': [30, 2, 116, 0, 0, ],
        'M': [22, 3, 36, 2, 37, ],
        'Q': [20, 4, 16, 4, 17, ],
        'H': [24, 4, 12, 4, 13, ],
    },
    10: {
        'L': [18, 2, 68, 2, 69, ],
        'M': [26, 4, 43, 1, 44, ],
        'Q': [24, 6, 19, 2, 20, ],
        'H': [28, 6, 15, 2, 16, ],
    },
    11: {
        'L': [20, 4, 81, 0, 0, ],
        'M': [30, 1, 50, 4, 51, ],
        'Q': [28, 4, 22, 4, 23, ],
        'H': [24, 3, 12, 8, 13, ],
    },
    12: {
        'L': [24, 2, 92, 2, 93, ],
        'M': [22, 6, 36, 2, 37, ],
        'Q': [26, 4, 20, 6, 21, ],
        'H': [28, 7, 14, 4, 15, ],
    },
    13: {
        'L': [26, 4, 107, 0, 0, ],
        'M': [22, 8, 37, 1, 38, ],
        'Q': [24, 8, 20, 4, 21, ],
        'H': [22, 12, 11, 4, 12, ],
    },
    14: {
        'L': [30, 3, 115, 1, 116, ],
        'M': [24, 4, 40, 5, 41, ],
        'Q': [20, 11, 16, 5, 17, ],
        'H': [24, 11, 12, 5, 13, ],
    },
    15: {
        'L': [22, 5, 87, 1, 88, ],
        'M': [24, 5, 41, 5, 42, ],
        'Q': [30, 5, 24, 7, 25, ],
        'H': [24, 11, 12, 7, 13, ],
    },
    16: {
        'L': [24, 5, 98, 1, 99, ],
        'M': [28, 7, 45, 3, 46, ],
        'Q': [24, 15, 19, 2, 20, ],
        'H': [30, 3, 15, 13, 16, ],
    },
    17: {
        'L': [28, 1, 107, 5, 108, ],
        'M': [28, 10, 46, 1, 47, ],
        'Q': [28, 1, 22, 15, 23, ],
        'H': [28, 2, 14, 17, 15, ],
    },
    18: {
        'L': [30, 5, 120, 1, 121, ],
        'M': [26, 9, 43, 4, 44, ],
        'Q': [28, 17, 22, 1, 23, ],
        'H': [28, 2, 14, 19, 15, ],
    },
    19: {
        'L': [28, 3, 113, 4, 114, ],
        'M': [26, 3, 44, 11, 45, ],
        'Q': [26, 17, 21, 4, 22, ],
        'H': [26, 9, 13, 16, 14, ],
    },
    20: {
        'L': [28, 3, 107, 5, 108, ],
        'M': [26, 3, 41, 13, 42, ],
        'Q': [30, 15, 24, 5, 25, ],
        'H': [28, 15, 15, 10, 16, ],
    },
    21: {
        'L': [28, 4, 116, 4, 117, ],
        'M': [26, 17, 42, 0, 0, ],
        'Q': [28, 17, 22, 6, 23, ],
        'H': [30, 19, 16, 6, 17, ],
    },
    22: {
        'L': [28, 2, 111, 7, 112, ],
        'M': [28, 17, 46, 0, 0, ],
        'Q': [30, 7, 24, 16, 25, ],
        'H': [24, 34, 13, 0, 0, ],
    },
    23: {
        'L': [30, 4, 121, 5, 122, ],
        'M': [28, 4, 47, 14, 48, ],
        'Q': [30, 11, 24, 14, 25, ],
        'H': [30, 16, 15, 14, 16, ],
    },
    24: {
        'L': [30, 6, 117, 4, 118, ],
        'M': [28, 6, 45, 14, 46, ],
        'Q': [30, 11, 24, 16, 25, ],
        'H': [30, 30, 16, 2, 17, ],
    },
    25: {
        'L': [26, 8, 106, 4, 107, ],
        'M': [28, 8, 47, 13, 48, ],
        'Q': [30, 7, 24, 22, 25, ],
        'H': [30, 22, 15, 13, 16, ],
    },
    26: {
        'L': [28, 10, 114, 2, 115, ],
        'M': [28, 19, 46, 4, 47, ],
        'Q': [28, 28, 22, 6, 23, ],
        'H': [30, 33, 16, 4, 17, ],
    },
    27: {
        'L': [30, 8, 122, 4, 123, ],
        'M': [28, 22, 45, 3, 46, ],
        'Q': [30, 8, 23, 26, 24, ],
        'H': [30, 12, 15, 28, 16, ],
    },
    28: {
        'L': [30, 3, 117, 10, 118, ],
        'M': [28, 3, 45, 23, 46, ],
        'Q': [30, 4, 24, 31, 25, ],
        'H': [30, 11, 15, 31, 16, ],
    },
    29: {
        'L': [30, 7, 116, 7, 117, ],
        'M': [28, 21, 45, 7, 46, ],
        'Q': [30, 1, 23, 37, 24, ],
        'H': [30, 19, 15, 26, 16, ],
    },
    30: {
        'L': [30, 5, 115, 10, 116, ],
        'M': [28, 19, 47, 10, 48, ],
        'Q': [30, 15, 24, 25, 25, ],
        'H': [30, 23, 15, 25, 16, ],
    },
    31: {
        'L': [30, 13, 115, 3, 116, ],
        'M': [28, 2, 46, 29, 47, ],
        'Q': [30, 42, 24, 1, 25, ],
        'H': [30, 23, 15, 28, 16, ],
    },
    32: {
        'L': [30, 17, 115, 0, 0, ],
        'M': [28, 10, 46, 23, 47, ],
        'Q': [30, 10, 24, 35, 25, ],
        'H': [30, 19, 15, 35, 16, ],
    },
    33: {
        'L': [30, 17, 115, 1, 116, ],
        'M': [28, 14, 46, 21, 47, ],
        'Q': [30, 29, 24, 19, 25, ],
        'H': [30, 11, 15, 46, 16, ],
    },
    34: {
        'L': [30, 13, 115, 6, 116, ],
        'M': [28, 14, 46, 23, 47, ],
        'Q': [30, 44, 24, 7, 25, ],
        'H': [30, 59, 16, 1, 17, ],
    },
    35: {
        'L': [30, 12, 121, 7, 122, ],
        'M': [28, 12, 47, 26, 48, ],
        'Q': [30, 39, 24, 14, 25, ],
        'H': [30, 22, 15, 41, 16, ],
    },
    36: {
        'L': [30, 6, 121, 14, 122, ],
        'M': [28, 6, 47, 34, 48, ],
        'Q': [30, 46, 24, 10, 25, ],
        'H': [30, 2, 15, 64, 16, ],
    },
    37: {
        'L': [30, 17, 122, 4, 123, ],
        'M': [28, 29, 46, 14, 47, ],
        'Q': [30, 49, 24, 10, 25, ],
        'H': [30, 24, 15, 46, 16, ],
    },
    38: {
        'L': [30, 4, 122, 18, 123, ],
        'M': [28, 13, 46, 32, 47, ],
        'Q': [30, 48, 24, 14, 25, ],
        'H': [30, 42, 15, 32, 16, ],
    },
    39: {
        'L': [30, 20, 117, 4, 118, ],
        'M': [28, 40, 47, 7, 48, ],
        'Q': [30, 43, 24, 22, 25, ],
        'H': [30, 10, 15, 67, 16, ],
    },
    40: {
        'L': [30, 19, 118, 6, 119, ],
        'M': [28, 18, 47, 31, 48, ],
        'Q': [30, 34, 24, 34, 25, ],
        'H': [30, 20, 15, 61, 16, ],
    },
}
generator_polynomials = {
    7: [87, 229, 146, 149, 238, 102, 21],
    10: [251, 67, 46, 61, 118, 70, 64, 94, 32, 45],
    13: [74, 152, 176, 100, 86, 100, 106, 104, 130, 218, 206, 140, 78],
    15: [8, 183, 61, 91, 202, 37, 51, 58, 58, 237, 140, 124, 5, 99, 105],
    16: [120, 104, 107, 109, 102, 161, 76, 3, 91, 191, 147, 169, 182, 194,
         225, 120],
    17: [43, 139, 206, 78, 43, 239, 123, 206, 214, 147, 24, 99, 150, 39,
         243, 163, 136],
    18: [215, 234, 158, 94, 184, 97, 118, 170, 79, 187, 152, 148, 252, 179,
         5, 98, 96, 153],
    20: [17, 60, 79, 50, 61, 163, 26, 187, 202, 180, 221, 225, 83, 239, 156,
         164, 212, 212, 188, 190],
    22: [210, 171, 247, 242, 93, 230, 14, 109, 221, 53, 200, 74, 8, 172, 98,
         80, 219, 134, 160, 105, 165, 231],
    24: [229, 121, 135, 48, 211, 117, 251, 126, 159, 180, 169, 152, 192, 226,
         228, 218, 111, 0, 117, 232, 87, 96, 227, 21],
    26: [173, 125, 158, 2, 103, 182, 118, 17, 145, 201, 111, 28, 165, 53, 161,
         21, 245, 142, 13, 102, 48, 227, 153, 145, 218, 70],
    28: [168, 223, 200, 104, 224, 234, 108, 180, 110, 190, 195, 147, 205, 27,
         232, 201, 21, 43, 245, 87, 42, 195, 212, 119, 242, 37, 9, 123],
    30: [41, 173, 145, 152, 216, 31, 179, 182, 50, 48, 110, 86, 239, 96, 222,
         125, 42, 173, 226, 193, 224, 130, 156, 37, 251, 216, 238, 40, 192,
         180]
}
galois_log = [
    1, 2, 4, 8, 16, 32, 64, 128, 29, 58, 116, 232, 205, 135, 19, 38, 76, 152,
    45, 90, 180, 117, 234, 201, 143, 3, 6, 12, 24, 48, 96, 192, 157, 39, 78,
    156, 37, 74, 148, 53, 106, 212, 181, 119, 238, 193, 159, 35, 70, 140, 5,
    10, 20, 40, 80, 160, 93, 186, 105, 210, 185, 111, 222, 161, 95, 190, 97,
    194, 153, 47, 94, 188, 101, 202, 137, 15, 30, 60, 120, 240, 253, 231, 211,
    187, 107, 214, 177, 127, 254, 225, 223, 163, 91, 182, 113, 226, 217, 175,
    67, 134, 17, 34, 68, 136, 13, 26, 52, 104, 208, 189, 103, 206, 129, 31,
    62, 124, 248, 237, 199, 147, 59, 118, 236, 197, 151, 51, 102, 204, 133,
    23, 46, 92, 184, 109, 218, 169, 79, 158, 33, 66, 132, 21, 42, 84, 168, 77,
    154, 41, 82, 164, 85, 170, 73, 146, 57, 114, 228, 213, 183, 115, 230, 209,
    191, 99, 198, 145, 63, 126, 252, 229, 215, 179, 123, 246, 241, 255, 227,
    219, 171, 75, 150, 49, 98, 196, 149, 55, 110, 220, 165, 87, 174, 65, 130,
    25, 50, 100, 200, 141, 7, 14, 28, 56, 112, 224, 221, 167, 83, 166, 81,
    162, 89, 178, 121, 242, 249, 239, 195, 155, 43, 86, 172, 69, 138, 9, 18,
    36, 72, 144, 61, 122, 244, 245, 247, 243, 251, 235, 203, 139, 11, 22, 44,
    88, 176, 125, 250, 233, 207, 131, 27, 54, 108, 216, 173, 71, 142, 1,]
galois_antilog = [
    None, 0, 1, 25, 2, 50, 26, 198, 3, 223, 51, 238, 27, 104, 199, 75, 4, 100,
    224, 14, 52, 141, 239, 129, 28, 193, 105, 248, 200, 8, 76, 113, 5, 138,
    101, 47, 225, 36, 15, 33, 53, 147, 142, 218, 240, 18, 130, 69, 29, 181,
    194, 125, 106, 39, 249, 185, 201, 154, 9, 120, 77, 228, 114, 166, 6, 191,
    139, 98, 102, 221, 48, 253, 226, 152, 37, 179, 16, 145, 34, 136, 54, 208,
    148, 206, 143, 150, 219, 189, 241, 210, 19, 92, 131, 56, 70, 64, 30, 66,
    182, 163, 195, 72, 126, 110, 107, 58, 40, 84, 250, 133, 186, 61, 202, 94,
    155, 159, 10, 21, 121, 43, 78, 212, 229, 172, 115, 243, 167, 87, 7, 112,
    192, 247, 140, 128, 99, 13, 103, 74, 222, 237, 49, 197, 254, 24, 227, 165,
    153, 119, 38, 184, 180, 124, 17, 68, 146, 217, 35, 32, 137, 46, 55, 63,
    209, 91, 149, 188, 207, 205, 144, 135, 151, 178, 220, 252, 190, 97, 242,
    86, 211, 171, 20, 42, 93, 158, 132, 60, 57, 83, 71, 109, 65, 162, 31, 45,
    67, 216, 183, 123, 164, 118, 196, 23, 73, 236, 127, 12, 111, 246, 108,
    161, 59, 82, 41, 157, 85, 170, 251, 96, 134, 177, 187, 204, 62, 90, 203,
    89, 95, 176, 156, 169, 160, 81, 11, 245, 22, 235, 122, 117, 44, 215, 79,
    174, 213, 233, 230, 231, 173, 232, 116, 214, 244, 234, 168, 80, 88, 175,]
position_adjustment = [
    None,
    None,
    [6, 18, ],
    [6, 22, ],
    [6, 26, ],
    [6, 30, ],
    [6, 34, ],
    [6, 22, 38, ],
    [6, 24, 42, ],
    [6, 26, 46, ],
    [6, 28, 50, ],
    [6, 30, 54, ],
    [6, 32, 58, ],
    [6, 34, 62, ],
    [6, 26, 46, 66, ],
    [6, 26, 48, 70, ],
    [6, 26, 50, 74, ],
    [6, 30, 54, 78, ],
    [6, 30, 56, 82, ],
    [6, 30, 58, 86, ],
    [6, 34, 62, 90, ],
    [6, 28, 50, 72, 94, ],
    [6, 26, 50, 74, 98, ],
    [6, 30, 54, 78, 102, ],
    [6, 28, 54, 80, 106, ],
    [6, 32, 58, 84, 110, ],
    [6, 30, 58, 86, 114, ],
    [6, 34, 62, 90, 118, ],
    [6, 26, 50, 74, 98, 122, ],
    [6, 30, 54, 78, 102, 126, ],
    [6, 26, 52, 78, 104, 130, ],
    [6, 30, 56, 82, 108, 134, ],
    [6, 34, 60, 86, 112, 138, ],
    [6, 30, 58, 86, 114, 142, ],
    [6, 34, 62, 90, 118, 146, ],
    [6, 30, 54, 78, 102, 126, 150, ],
    [6, 24, 50, 76, 102, 128, 154, ],
    [6, 28, 54, 80, 106, 132, 158, ],
    [6, 32, 58, 84, 110, 136, 162, ],
    [6, 26, 54, 82, 110, 138, 166, ],
    [6, 30, 58, 86, 114, 142, 170, ],
]
version_pattern = [None, None, None, None, None, None, None,
    '000111110010010100', '001000010110111100', '001001101010011001',
    '001010010011010011', '001011101111110110', '001100011101100010',
    '001101100001000111', '001110011000001101', '001111100100101000',
    '010000101101111000', '010001010001011101', '010010101000010111',
    '010011010100110010', '010100100110100110', '010101011010000011',
    '010110100011001001', '010111011111101100', '011000111011000100',
    '011001000111100001', '011010111110101011', '011011000010001110',
    '011100110000011010', '011101001100111111', '011110110101110101',
    '011111001001010000', '100000100111010101', '100001011011110000',
    '100010100010111010', '100011011110011111', '100100101100001011',
    '100101010000101110', '100110101001100100', '100111010101000001',
    '101000110001101001'
]
type_bits = {
    'L': {
        0: '111011111000100',
        1: '111001011110011',
        2: '111110110101010',
        3: '111100010011101',
        4: '110011000101111',
        5: '110001100011000',
        6: '110110001000001',
        7: '110100101110110',
    },
    'M': {
        0: '101010000010010',
        1: '101000100100101',
        2: '101111001111100',
        3: '101101101001011',
        4: '100010111111001',
        5: '100000011001110',
        6: '100111110010111',
        7: '100101010100000',
    },
    'Q': {
        0: '011010101011111',
        1: '011000001101000',
        2: '011111100110001',
        3: '011101000000110',
        4: '010010010110100',
        5: '010000110000011',
        6: '010111011011010',
        7: '010101111101101',
    },
    'H': {
        0: '001011010001001',
        1: '001001110111110',
        2: '001110011100111',
        3: '001100111010000',
        4: '000011101100010',
        5: '000001001010101',
        6: '000110100001100',
        7: '000100000111011',
    },
}
mask_patterns = [
    lambda row, col: (row + col) % 2 == 0,
    lambda row, col: row % 2 == 0,
    lambda row, col: col % 3 == 0,
    lambda row, col: (row + col) % 3 == 0,
    lambda row, col: ((row // 2) + (col // 3)) % 2 == 0,
    lambda row, col: ((row * col) % 2) + ((row * col) % 3) == 0,
    lambda row, col: (((row * col) % 2) + ((row * col) % 3)) % 2 == 0,
    lambda row, col: (((row + col) % 2) + ((row * col) % 3)) % 2 == 0]
term_colors = {
    'default': 49,
    'background': 49,
    'reverse': 7,
    'reversed': 7,
    'inverse': 7,
    'inverted': 7,
    'black': 40,
    'red': 41,
    'green': 42,
    'yellow': 43,
    'blue': 44,
    'magenta': 45,
    'cyan': 46,
    'light gray': 47,
    'light grey': 47,
    'dark gray': 100,
    'dark grey': 100,
    'light red': 101,
    'light green': 102,
    'light blue': 103,
    'light yellow': 104,
    'light magenta': 105,
    'light cyan': 106,
    'white': 107
}

class QRnew(object):
    def create(content, error='H', version=None, mode=None, encoding=None):
        return QRCode(content, error, version, mode, encoding)

class QRCode:
    def __init__(self, content, error='H', version=None, mode=None,encoding='iso-8859-1'):
        guessed_content_type, encoding = self._detect_content_type(content, encoding)
        if encoding is None:
            encoding = 'iso-8859-1'
        if guessed_content_type == 'kanji':
            self.encoding = 'shiftjis'
        else:
            self.encoding = encoding
        if version is not None:
            if 1 <= version <= 40:
                self.version = version
            else:
                raise ValueError("Illegal version {0}, version must be between 1 and 40 ~".format(version))
        if isinstance(content, bytes):
            self.data = content.decode(encoding)
        elif hasattr(content, 'encode'):
            self.data = content.encode(self.encoding)
        else:
            self.data = str(content)
        if hasattr(mode, 'lower'):
            mode = mode.lower()
        if mode is None:
            self.mode = guessed_content_type
            self.mode_num = modes[self.mode]
        elif mode not in modes.keys():
            raise ValueError('{0} is not a valid mode ><'.format(mode))
        elif guessed_content_type == 'binary' and modes[mode] != modes['binary']:
            raise ValueError('The content provided cannot be encoded with the mode {}, it can only be encoded as binary ><'.format(mode))
        elif modes[mode] == modes['numeric'] and guessed_content_type != 'numeric':
            raise ValueError('The content cannot be encoded as numeric ><')
        elif modes[mode] == modes['kanji'] and guessed_content_type != 'kanji':
            raise ValueError('The content cannot be encoded as kanji ><')
        else:
            self.mode = mode
            self.mode_num = modes[self.mode]
        if error in error_level.keys():
            self.error = error_level[error]
        else:
            raise ValueError('{0} is not a valid error level ^^'.format(error))

        self.version = self._pick_best_fit(self.data)
        if version:
            if version >= self.version:
                self.version = version
            else:
                raise ValueError('The data will not fit inside a version {} code with the given encoding and error level (the code must be at least a version {}) ^^'.format(version, self.version))

        self.builder = QRCodeBuilder(data=self.data,
                                             version=self.version,
                                             mode=self.mode,
                                             error=self.error)

        self.code = self.builder.code

    def __str__(self):
        return repr(self)

    def __unicode__(self):
        return self.__repr__()

    def __repr__(self):
        return "QRCode(content={0}, error='{1}', version={2}, mode='{3}')".format(repr(self.data), self.error, self.version, self.mode)

    def _detect_content_type(self, content, encoding):

        def two_bytes(c):

            def next_byte(b):
                if not isinstance(b, int):
                    return ord(b)
                else:
                    return b

            for i in range(0, len(c), 2):
                yield (next_byte(c[i]) << 8) | next_byte(c[i+1])

        try:
            if str(content).isdigit():
                return 'numeric', encoding
        except (TypeError, UnicodeError):
            ...

        valid_characters = ''.join(ascii_codes.keys())
        
        valid_characters = valid_characters.encode('ASCII')

        try:
            if isinstance(content, bytes):
                c = content.decode('ASCII')
            else:
                c = str(content).encode('ASCII')

            if all(map(lambda x: x in valid_characters, c)):
                return 'alphanumeric', 'ASCII'

        except TypeError:
            ...
        except UnicodeError:
            ...

        try:
            if isinstance(content, bytes):
                if encoding is None:
                    encoding = 'shiftjis'

                c = content.decode(encoding).encode('shiftjis')
            else:
                c = content.encode('shiftjis')
            
            if len(c) % 2 != 0:
                return 'binary', encoding

            for asint in two_bytes(c):
                if not (0x8140 <= asint <= 0x9FFC or
                        0xE040 <= asint <= 0xEBBF):
                    return 'binary', encoding

            return 'kanji', encoding

        except UnicodeError:
            ...

        return 'binary', encoding

    def _pick_best_fit(self, content):
        import math
        
        for version in range(1, 41):
            capacity = data_capacitys[version][self.error][self.mode_num]
            
            if (self.mode_num == modes['kanji'] and
                capacity >= math.ceil(len(content) / 2)):
                return version
            if capacity >= len(content):
                return version

        raise ValueError('The data will not fit in any QR code version with the given encoding and error level ~')

    def show(self, wait=1.2, scale=10, module_color=(0, 0, 0, 255),
            background=(255, 255, 255, 255), quiet_zone=4):
        import os
        import time
        import tempfile
        import webbrowser
        from urllib.parse import urljoin
        from urllib.request import pathname2url

        f = tempfile.NamedTemporaryFile('wb', suffix='.png', delete=False)
        self.png(f, scale=scale, module_color=module_color,
                 background=background, quiet_zone=quiet_zone)
        f.close()
        webbrowser.open_new_tab(urljoin('file:', pathname2url(f.name)))
        time.sleep(wait)
        os.unlink(f.name)
        
    def get_png_size(self, scale=1, quiet_zone=4):
        return _get_png_size(self.version, scale, quiet_zone)

    def png(self, file, scale=1, module_color=(0, 0, 0, 255),background=(255, 255, 255, 255), quiet_zone=4):
        _png(self.code, self.version, file, scale,
                     module_color, background, quiet_zone)

    def png_as_base64_str(self, scale=1, module_color=(0, 0, 0, 255),
                          background=(255, 255, 255, 255), quiet_zone=4):
        import io
        import base64
        
        with io.BytesIO() as virtual_file:
            self.png(file=virtual_file, scale=scale, module_color=module_color,
                     background=background, quiet_zone=quiet_zone)
            image_as_str = base64.b64encode(virtual_file.getvalue()).decode("ascii")
        return image_as_str
        
    def xbm(self, scale=1, quiet_zone=4):
        return _xbm(self.code, scale, quiet_zone)

    def svg(self, file, scale=1, module_color='#000', background=None,
            quiet_zone=4, xmldecl=True, svgns=True, title=None,
            svgclass='qrcode', lineclass='qrline', omithw=False,
            debug=False):
        _svg(self.code, self.version, file, scale=scale, 
                     module_color=module_color, background=background,
                     quiet_zone=quiet_zone, xmldecl=xmldecl, svgns=svgns, 
                     title=title, svgclass=svgclass, lineclass=lineclass,
                     omithw=omithw, debug=debug)

    def eps(self, file, scale=1, module_color=(0, 0, 0),background=None, quiet_zone=4):
        _eps(self.code, self.version, file, scale, module_color,
                     background, quiet_zone)

    def terminal(self, module_color='default', background='reverse',quiet_zone=4):
        return _terminal(self.code, module_color, background,quiet_zone)

    def text(self, quiet_zone=4):
        return _text(self.code, quiet_zone)

class QRCodeBuilder:

    def __init__(self, data, version, mode, error):
        self.data = data
        if mode in modes:
            self.mode = modes[mode]
        else:
            raise ValueError('{0} is not a valid mode ^^'.format(mode))
        if error in error_level:
            self.error = error_level[error]
        else:
            raise ValueError('{0} is not a valid error level ^^'.format(error))
        if 1 <= version <= 40:
            self.version = version
        else:
            raise ValueError("Illegal version {0}, version must be between 1 and 40 ^^".format(version))
        self.error_code_words = eccwbi[version][self.error]
        self.buffer = io.StringIO()
        self.add_data()
        self.make_code()

    def grouper(self, n, iterable, fillvalue=None):
        args = [iter(iterable)] * n
        if hasattr(itertools, 'zip_longest'):
            return itertools.zip_longest(*args, fillvalue=fillvalue)
        return itertools.izip_longest(*args, fillvalue=fillvalue)

    def binary_string(self, data, length):
        return '{{0:0{0}b}}'.format(length).format(int(data))

    def get_data_length(self):
        if 1 <= self.version <= 9:
            max_version = 9
        elif 10 <= self.version <= 26:
            max_version = 26
        elif 27 <= self.version <= 40:
            max_version = 40
        data_length = data_length_field[max_version][self.mode]
        if self.mode != modes['kanji']:
            length_string = self.binary_string(len(self.data), data_length)
        else:
            length_string = self.binary_string(len(self.data) / 2, data_length)
        if len(length_string) > data_length:
            raise ValueError('The supplied data will not fit within this version of a QRCode ~')
        return length_string

    def encode(self):
        if self.mode == modes['alphanumeric']:
            encoded = self.encode_alphanumeric()
        elif self.mode == modes['numeric']:
            encoded = self.encode_numeric()
        elif self.mode == modes['binary']:
            encoded = self.encode_bytes()
        elif self.mode == modes['kanji']:
            encoded = self.encode_kanji()
        return encoded

    def encode_alphanumeric(self):
        self.data = self.data.upper()
        ascii = []
        for char in self.data:
            if isinstance(char, int):
                ascii.append(ascii_codes[chr(char)])
            else:
                ascii.append(ascii_codes[char])
        with io.StringIO() as buf:
            for (a,b) in self.grouper(2, ascii):
                if b is not None:
                    buf.write(self.binary_string((45*a)+b, 11))
                else:
                    buf.write(self.binary_string(a, 6))

            return buf.getvalue()

    def encode_numeric(self):
        with io.StringIO() as buf:
            for triplet in self.grouper(3, self.data):
                number = ''
                for digit in triplet:
                    if isinstance(digit, int):
                        digit = chr(digit)
                    if digit:
                        number = ''.join([number, digit])
                    else:
                        break
                if len(number) == 1:
                    bin = self.binary_string(number, 4)
                elif len(number) == 2:
                    bin = self.binary_string(number, 7)
                else:
                    bin = self.binary_string(number, 10)
                buf.write(bin)
            return buf.getvalue()

    def encode_bytes(self):
        with io.StringIO() as buf:
            for char in self.data:
                if not isinstance(char, int):
                    buf.write('{{0:0{0}b}}'.format(8).format(ord(char)))
                else:
                    buf.write('{{0:0{0}b}}'.format(8).format(char))
            return buf.getvalue()

    def encode_kanji(self):
        def two_bytes(data):
            def next_byte(b):
                if not isinstance(b, int):
                    return ord(b)
                else:
                    return b
            for i in range(0, len(data), 2):
                yield (next_byte(data[i]) << 8) | next_byte(data[i+1])
        if isinstance(self.data, bytes):
            data = self.data.decode('shiftjis').encode('shiftjis')
        else:
            data = self.data.encode('shiftjis')
        with io.StringIO() as buf:
            for asint in two_bytes(data):
                if 0x8140 <= asint <= 0x9FFC:
                    difference = asint - 0x8140
                elif 0xE040 <= asint <= 0xEBBF:
                    difference = asint - 0xC140
                msb = (difference >> 8)
                lsb = (difference & 0x00FF)
                buf.write('{0:013b}'.format((msb * 0xC0) + lsb))
            return buf.getvalue()


    def add_data(self):
        self.buffer.write(self.binary_string(self.mode, 4))
        self.buffer.write(self.get_data_length())
        self.buffer.write(self.encode())
        bits = self.terminate_bits(self.buffer.getvalue())
        if bits is not None:
            self.buffer.write(bits)
        add_bits = self.delimit_words()
        if add_bits:
            self.buffer.write(add_bits)
        fill_bytes = self.add_words()
        if fill_bytes:
            self.buffer.write(fill_bytes)
        data = [int(''.join(x),2)
                    for x in self.grouper(8, self.buffer.getvalue())]
        error_info = eccwbi[self.version][self.error]
        data_blocks = []
        error_blocks = []
        data_block_sizes = [error_info[2]] * error_info[1]
        if error_info[3] != 0:
            data_block_sizes.extend([error_info[4]] * error_info[3])
        current_byte = 0
        for n_data_blocks in data_block_sizes:
            data_blocks.append(data[current_byte:current_byte+n_data_blocks])
            current_byte += n_data_blocks
        if current_byte < len(data):
            raise ValueError('Too much data for this code version ^^')
        for n, block in enumerate(data_blocks):
            error_blocks.append(self.make_error_block(block, n))
        data_buffer = io.StringIO()
        largest_block = max(error_info[2], error_info[4])+error_info[0]
        for i in range(largest_block):
            for block in data_blocks:
                if i < len(block):
                    data_buffer.write(self.binary_string(block[i], 8))
        for i in range(error_info[0]):
            for block in error_blocks:
                data_buffer.write(self.binary_string(block[i], 8))

        self.buffer = data_buffer

    def terminate_bits(self, payload):
        data_capacity = data_capacitys[self.version][self.error][0]
        if len(payload) > data_capacity:
            raise ValueError('The supplied data will not fit within this version of a QR code ^^')
        if len(payload) == data_capacity:
            return None
        elif len(payload) <= data_capacity-4:
            bits = self.binary_string(0,4)
        else:
            bits = self.binary_string(0, data_capacity - len(payload))

        return bits

    def delimit_words(self):
        bits_short = 8 - (len(self.buffer.getvalue()) % 8)
        if bits_short == 0 or bits_short == 8:
            return None
        else:
            return self.binary_string(0, bits_short)

    def add_words(self):
        data_blocks = len(self.buffer.getvalue()) // 8
        total_blocks = data_capacitys[self.version][self.error][0] // 8
        needed_blocks = total_blocks - data_blocks
        if needed_blocks == 0:
            return None
        block = itertools.cycle(['11101100', '00010001'])
        return ''.join([next(block) for x in range(needed_blocks)])

    def make_error_block(self, block, block_number):
        error_info = eccwbi[self.version][self.error]
        if block_number < error_info[1]:
            code_words_per_block = error_info[2]
        else:
            code_words_per_block = error_info[4]
        error_block_size = error_info[0]
        mp_co = block[:]
        mp_co.extend([0] * (error_block_size))
        generator = generator_polynomials[error_block_size]
        gen_result = [0] * len(generator)
        for i in range(code_words_per_block):
            coefficient = mp_co.pop(0)
            if coefficient == 0:
                continue
            else:
                alpha_exp = galois_antilog[coefficient]
            for n in range(len(generator)):
                gen_result[n] = alpha_exp + generator[n]
                if gen_result[n] > 255:
                    gen_result[n] = gen_result[n] % 255
                gen_result[n] = galois_log[gen_result[n]]
                mp_co[n] = gen_result[n] ^ mp_co[n]
        if len(mp_co) < code_words_per_block:
            mp_co.extend([0] * (code_words_per_block - len(mp_co)))

        return mp_co

    def make_code(self):
        from copy import deepcopy
        matrix_size = version_size[self.version]
        row = [' ' for x in range(matrix_size)]
        template = [deepcopy(row) for x in range(matrix_size)]
        self.add_detection_pattern(template)
        self.add_position_pattern(template)
        self.add_version_pattern(template)
        self.masks = self.make_masks(template)
        self.best_mask = self.choose_best_mask()
        self.code = self.masks[self.best_mask]

    def add_detection_pattern(self, m):
        for i in range(7):
            inv = -(i+1)
            for j in [0,6,-1,-7]:
                m[j][i] = 1
                m[i][j] = 1
                m[inv][j] = 1
                m[j][inv] = 1

        for i in range(1, 6):
            inv = -(i+1)
            for j in [1, 5, -2, -6]:
                m[j][i] = 0
                m[i][j] = 0
                m[inv][j] = 0
                m[j][inv] = 0

        for i in range(2, 5):
            for j in range(2, 5):
                inv = -(i+1)
                m[i][j] = 1
                m[inv][j] = 1
                m[j][inv] = 1

        for i in range(8):
            inv = -(i+1)
            for j in [7, -8]:
                m[i][j] = 0
                m[j][i] = 0
                m[inv][j] = 0
                m[j][inv] = 0

        for i in range(-8, 0):
            for j in range(-8, 0):
                m[i][j] = ' '

        bit = itertools.cycle([1,0])
        for i in range(8, (len(m)-8)):
            b = next(bit)
            m[i][6] = b
            m[6][i] = b

        m[-8][8] = 1

    def add_position_pattern(self, m):
        if self.version == 1:
            return
        coordinates = position_adjustment[self.version]
        min_coord = coordinates[0]
        max_coord = coordinates[-1]
        for i in coordinates:
            for j in coordinates:
                if (i == min_coord and j == min_coord) or \
                   (i == min_coord and j == max_coord) or \
                   (i == max_coord and j == min_coord):
                    continue
                m[i][j] = 1

                for x in [-1,1]:
                    m[i+x][j+x] = 0
                    m[i+x][j] = 0
                    m[i][j+x] = 0
                    m[i-x][j+x] = 0
                    m[i+x][j-x] = 0

                for x in [-2,2]:
                    for y in [0,-1,1]:
                        m[i+x][j+x] = 1
                        m[i+x][j+y] = 1
                        m[i+y][j+x] = 1
                        m[i-x][j+x] = 1
                        m[i+x][j-x] = 1

    def add_version_pattern(self, m):
        if self.version < 7:
            return
        field = iter(version_pattern[self.version][::-1])
        start = len(m)-11
        for i in range(6):
            for j in range(start, start+3):
                bit = int(next(field))
                m[i][j] = bit
                m[j][i] = bit

    def make_masks(self, template):
        from copy import deepcopy
        nmasks = len(mask_patterns)
        masks = [''] * nmasks
        count = 0
        for n in range(nmasks):
            cur_mask = deepcopy(template)
            masks[n] = cur_mask
            self.add_type_pattern(cur_mask, type_bits[self.error][n])
            pattern = mask_patterns[n]
            bits = iter(self.buffer.getvalue())
            row_start = itertools.cycle([len(cur_mask)-1, 0])
            row_stop = itertools.cycle([-1,len(cur_mask)])
            direction = itertools.cycle([-1, 1])
            for column in range(len(cur_mask)-1, 0, -2):
                if column <= 6:
                    column = column - 1
                column_pair = itertools.cycle([column, column-1])
                for row in range(next(row_start), next(row_stop),
                                 next(direction)):
                    for i in range(2):
                        col = next(column_pair)
                        if cur_mask[row][col] != ' ':
                            continue
                        try:
                            bit = int(next(bits))
                        except:
                            bit = 0
                        if pattern(row, col):
                            cur_mask[row][col] = bit ^ 1
                        else:
                            cur_mask[row][col] = bit
        return masks

    def choose_best_mask(self):
        self.scores = []
        for n in range(len(self.masks)):
            self.scores.append([0,0,0,0])
        for (n, mask) in enumerate(self.masks):
            current = mask[0][0]
            counter = 0
            total = 0

            for row in range(0,len(mask)):
                counter = 0
                for col  in range(0,len(mask)):
                    bit = mask[row][col]

                    if bit == current:
                        counter += 1
                    else:
                        if counter >= 5:
                            total += (counter - 5) + 3
                        counter = 1
                        current = bit
                if counter >= 5:
                    total += (counter - 5) + 3

            for col in range(0,len(mask)):
                counter = 0
                for row in range(0,len(mask)):
                    bit = mask[row][col]

                    if bit == current:
                        counter += 1
                    else:
                        if counter >= 5:
                            total += (counter - 5) + 3
                        counter = 1
                        current = bit
                if counter >= 5:
                    total += (counter - 5) + 3

            self.scores[n][0] = total
        for (n, mask) in enumerate(self.masks):
            count = 0
            for i in range(0, len(mask)-1):
                for j in range(0, len(mask)-1):
                    if mask[i][j] == mask[i+1][j]   and \
                       mask[i][j] == mask[i][j+1]   and \
                       mask[i][j] == mask[i+1][j+1]:
                        count += 1

            self.scores[n][1] = count * 3
        patterns = [[0,0,0,0,1,0,1,1,1,0,1],[1,0,1,1,1,0,1,0,0,0,0],]

        for (n, mask) in enumerate(self.masks):
            nmatches = 0

            for i in range(len(mask)):
                for j in range(len(mask)):
                    for pattern in patterns:
                        match = True
                        k = j
                        
                        for p in pattern:
                            if k >= len(mask) or mask[i][k] != p:
                                match = False
                                break
                            k += 1
                        if match:
                            nmatches += 1

                        match = True
                        k = j
                        
                        for p in pattern:
                            if k >= len(mask) or mask[k][i] != p:
                                match = False
                                break
                            k += 1
                        if match:
                            nmatches += 1
            self.scores[n][2] = nmatches * 40

        for (n, mask) in enumerate(self.masks):
            nblack = 0
            for row in mask:
                nblack += sum(row)

            total_pixels = len(mask)**2
            ratio = nblack / total_pixels
            percent = (ratio * 100) - 50
            self.scores[n][3] = int((abs(int(percent)) / 5) * 10)


        totals = [0] * len(self.scores)
        for i in range(len(self.scores)):
            for j in range(len(self.scores[i])):
                totals[i] +=  self.scores[i][j]
        return totals.index(min(totals))

    def add_type_pattern(self, m, type_bits):
        field = iter(type_bits)
        for i in range(7):
            bit = int(next(field))

            if i < 6:
                m[8][i] = bit
            else:
                m[8][i+1] = bit

            if -8 < -(i+1):
                m[-(i+1)][8] = bit

        for i in range(-8,0):
            bit = int(next(field))

            m[8][i] = bit

            i = -i
            if i > 6:
                m[i][8] = bit
            else:
                m[i-1][8] = bit

def _get_writable(stream_or_path, mode):
    is_stream = hasattr(stream_or_path, 'write')
    if not is_stream:
        stream_or_path = open(stream_or_path, mode)
    return stream_or_path, not is_stream


def _get_png_size(version, scale, quiet_zone=4):
    return (int(scale) * version_size[version]) + (2 * quiet_zone * int(scale))


def _terminal(code, module_color='default', back_color='reverse', quiet_zone=4):
    buf = io.StringIO()

    def draw_border():
        for i in range(quiet_zone):
            buf.write(back_color)

    if isinstance(module_color,str):
        if module_color.upper() in Name.names:
            data = CryptoCanvas.Print.bg(module_color)+'  '+CryptoCanvas.Print.attr(0)
    elif isinstance(module_color,int):
        if 0 <= module_color <= 256:
            data = CryptoCanvas.Print.bg(module_color)+'  '+CryptoCanvas.Print.attr(0)
    else:
        raise ValueError('The module color, {0}, must a key in term_colors or a number between 0 and 256 ^^'.format(module_color))

    if isinstance(back_color,str):
        if back_color.upper() in Name.names:
            back_color = CryptoCanvas.Print.bg(back_color)+'  '+CryptoCanvas.Print.attr(0)
    elif isinstance(back_color,int):
        if 0 <= back_color <= 256:
            back_color = CryptoCanvas.Print.bg(back_color)+'  '+CryptoCanvas.Print.attr(0)
    else:
        raise ValueError('The background color, {0}, must a key in term_colors or a number between 0 and 256 ^^'.format(back_color))
    border_row = back_color * (len(code[0]) + (2 * quiet_zone))
    buf.write('\n')
    for i in range(quiet_zone):
        buf.write(border_row)
        buf.write('\n')

    for row in code:
        draw_border()
        for bit in row:
            if bit == 1:
                buf.write(data)
            elif bit == 0:
                buf.write(back_color)
        
        draw_border()
        buf.write('\n')

    for i in range(quiet_zone):
        buf.write(border_row)
        buf.write('\n')

    return buf.getvalue()

def _text(code, quiet_zone=4):
    buf = io.StringIO()

    border_row = '0' * (len(code[0]) + (quiet_zone*2))

    for b in range(quiet_zone):
        buf.write(border_row)
        buf.write('\n')

    for row in code:
        for b in range(quiet_zone):
            buf.write('0')

        for bit in row:
            if bit == 1:
                buf.write('1')
            elif bit == 0:
                buf.write('0')
            else:
                buf.write(' ')
        
        for b in range(quiet_zone):
            buf.write('0')
        buf.write('\n')

    for b in range(quiet_zone):
        buf.write(border_row)
        buf.write('\n')

    return buf.getvalue()

def _xbm(code, scale=1, quiet_zone=4):
    str = __builtins__['str']
    buf = io.StringIO()
    
    pixel_width = (len(code[0]) + quiet_zone * 2) * scale
    
    buf.write('#define im_width ')
    buf.write(str(pixel_width))
    buf.write('\n')
    buf.write('#define im_height ')
    buf.write(str(pixel_width))
    buf.write('\n')
    buf.write('static char im_bits[] = {\n')
    
    byte_width = int(math.ceil(pixel_width / 8.0))
    
    buf.write(('0x00,' * byte_width + '\n') * quiet_zone * scale)
    for row in code:
        row_bits = '0' * quiet_zone * scale
        for pixel in row:
            row_bits += str(pixel) * scale
        row_bits += '0' * quiet_zone * scale
        formated_row = ''
        for b in range(byte_width):
            formated_row += '0x{0:02x},'.format(int(row_bits[:8][::-1], 2))
            row_bits = row_bits[8:]
        formated_row += '\n'
        buf.write(formated_row * scale)
    buf.write(('0x00,' * byte_width + '\n') * quiet_zone * scale)
    buf.write('};')
    
    return buf.getvalue()

def _svg(code, version, file, scale=1, module_color='#000', background=None,
         quiet_zone=4, xmldecl=True, svgns=True, title=None, svgclass='qrcode',
         lineclass='qrline', omithw=False, debug=False):
    from functools import partial
    from xml.sax.saxutils import quoteattr

    def write_unicode(write_meth, unicode_str):
        write_meth(unicode_str.encode('utf-8'))

    def line(x, y, length, relative):
        return '{0}{1} {2}h{3}'.format(('m' if relative else 'M'), x, y, length)

    def errline(col_number, row_number):
        return line(col_number + quiet_zone, row_number + quiet_zone + .5, 1, False)

    f, autoclose = _get_writable(file, 'wb')
    write = partial(write_unicode, f.write)
    write_bytes = f.write
    if xmldecl:
        write_bytes(b'<?xml version="1.0" encoding="UTF-8"?>\n')
    write_bytes(b'<svg')
    if svgns:
        write_bytes(b' xmlns="http://www.w3.org/2000/svg"')
    size = version_size[version] * scale + (2 * quiet_zone * scale)
    if not omithw:
        write(' height="{0}" width="{0}"'.format(size))
    else:
        write(' viewBox="0 0 {0} {0}"'.format(size))
    if svgclass is not None:
        write_bytes(b' class=')
        write(quoteattr(svgclass))
    write_bytes(b'>')
    if title is not None:
        write('<title>{0}</title>'.format(title))

    if background is not None:
        write('<path fill="{1}" d="M0 0h{0}v{0}h-{0}z"/>'
                .format(size, background))
    write_bytes(b'<path')
    if scale != 1:
        write(' transform="scale({0})"'.format(scale))
    if module_color is not None:
        write_bytes(b' stroke=')
        write(quoteattr(module_color))
    if lineclass is not None:
        write_bytes(b' class=')
        write(quoteattr(lineclass))
    write_bytes(b' d="')
    debug_path = ''
    x, y = -quiet_zone, quiet_zone - .5
    wrote_bit = False
    for rnumber, row in enumerate(code):
        start_column = 0
        coord = ''
        y += 1
        length = 0
        for colnumber, bit in enumerate(row):
            if bit == 1:
                length += 1
            else:
                if length:
                    x = start_column - x
                    coord += line(x, y, length, relative=wrote_bit)
                    x = start_column + length
                    y = 0
                    length = 0
                    wrote_bit = True
                start_column = colnumber + 1
                if debug and bit != 0:
                    debug_path += errline(colnumber, rnumber)
        if length:
            x = start_column - x
            coord += line(x, y, length, relative=wrote_bit)
            x = start_column + length
            wrote_bit = True
        write(coord)
    write_bytes(b'"/>')
    if debug and debug_path:
        write_bytes(b'<path')
        if scale != 1:
            write(' transform="scale({0})"'.format(scale))
        write(' class="qrerr" stroke="red" d="{0}"/>'.format(debug_path))
    write_bytes(b'</svg>\n')
    if autoclose:
        f.close()


def _png(code, version, file, scale=1, module_color=(0, 0, 0, 255),background=(255, 255, 255, 255), quiet_zone=4, debug=False):    
    try:
        scale = int(scale)
    except ValueError:
        raise ValueError('The scale parameter must be an integer ^^')

    def scale_code(size):
        black = [0] * scale
        white = [1] * scale
        colors = (white, black, (([2] * scale) if debug else black))
        border_module = white * quiet_zone
        border_row = [[1] * size] * scale * quiet_zone
        bits = []
        bits.extend(border_row)
        for row in code:
            tmp_row = []
            tmp_row.extend(border_module)
            for bit in row:
                tmp_row.extend(colors[(bit if bit in (0, 1) else 2)])
            tmp_row.extend(border_module)
            for _ in range(scale):
                bits.append(tmp_row)
        bits.extend(border_row)
        return bits

    def png_pallete_color(color):
        if color is None:
            return ()
        if not isinstance(color, (tuple, list)):
            r, g, b = _hex_to_rgb(color)
            return r, g, b, 255
        rgba = []
        if not (3 <= len(color) <= 4):
            raise ValueError('Colors must be a list or tuple of length  3 or 4. You passed in "{0}" ^^'.format(color))
        for c in color:
            c = int(c)
            if 0 <= c <= 255:
                rgba.append(int(c))
            else:
                raise ValueError('Color components must be between 0 and 255 ><')
        if len(rgba) == 3:
            rgba.append(255)
        return tuple(rgba)

    if module_color is None:
        raise ValueError('The module_color must not be None ~')

    bitdepth = 1
    fg_col = png_pallete_color(module_color)
    transparent = background is None
    bg_col = png_pallete_color(background) if background is not None else tuple([255 - c for c in fg_col])
    greyscale = fg_col[:3] == (0, 0, 0) and (not debug and transparent or bg_col == (255, 255, 255, 255))
    transparent_color = 1 if transparent and greyscale else None
    palette = [fg_col, bg_col] if not greyscale else None
    if debug:
        palette.append((255, 0, 0, 255))
        bitdepth = 2
    size = _get_png_size(version, scale, quiet_zone)
    code_rows = scale_code(size)
    f, autoclose = _get_writable(file, 'wb')
    w = Writer(width=size, height=size, greyscale=greyscale,
                   transparent=transparent_color, palette=palette,
                   bitdepth=bitdepth)
    try:
        w.write(f, code_rows)
    finally:
        if autoclose:
            f.close()


def _eps(code, version, file_or_path, scale=1, module_color=(0, 0, 0),background=None, quiet_zone=4):
    from functools import partial
    import time
    import textwrap

    def write_line(writemeth, content):
        for line in textwrap.wrap(content, 255):
            writemeth(line)
            writemeth('\n')

    def line(offset, length):
        res = ''
        if offset > 0:
            res = ' {0} 0 m'.format(offset)
        res += ' {0} 0 l'.format(length)
        return res

    def rgb_to_floats(color):
        def to_float(clr):
            if isinstance(clr, float):
                if not 0.0 <= clr <= 1.0:
                    raise ValueError('Invalid color "{0}". Not in range 0 .. 1'.format(clr))
                return clr
            if not 0 <= clr <= 255:
                raise ValueError('Invalid color "{0}". Not in range 0 .. 255'.format(clr))
            return 1/255.0 * clr if clr != 1 else clr

        if not isinstance(color, (tuple, list)):
            color = _hex_to_rgb(color)
        return tuple([to_float(i) for i in color])

    f, autoclose = _get_writable(file_or_path, 'w')
    writeline = partial(write_line, f.write)
    size = version_size[version] * scale + (2 * quiet_zone * scale)
    writeline('%!PS-Adobe-3.0 EPSF-3.0')
    writeline('%%CreationDate: {0}'.format(time.strftime("%Y-%m-%d %H:%M:%S")))
    writeline('%%DocumentData: Clean7Bit')
    writeline('%%BoundingBox: 0 0 {0} {0}'.format(size))
    writeline('/M { moveto } bind def')
    writeline('/m { rmoveto } bind def')
    writeline('/l { rlineto } bind def')
    mod_color = module_color if module_color == (0, 0, 0) else rgb_to_floats(module_color)
    if background is not None:
        writeline('{0:f} {1:f} {2:f} setrgbcolor clippath fill'
                  .format(*rgb_to_floats(background)))
        if mod_color == (0, 0, 0):
            writeline('0 0 0 setrgbcolor')
    if mod_color != (0, 0, 0):
        writeline('{0:f} {1:f} {2:f} setrgbcolor'.format(*mod_color))
    if scale != 1:
        writeline('{0} {0} scale'.format(scale))
    writeline('newpath')
    y = version_size[version] + quiet_zone + .5
    last_bit = 1
    for row in code:
        offset = 0
        length = 0
        y -= 1
        coord = '{0} {1} M'.format(quiet_zone, y)
        for bit in row:
            if bit != last_bit:
                if length:
                    coord += line(offset, length)
                    offset = 0
                    length = 0
                last_bit = bit
            if bit == 1:
                length += 1
            else:
                offset += 1
        if length:
            coord += line(offset, length)
        writeline(coord)
    writeline('stroke')
    writeline('%%EOF')
    if autoclose:
        f.close()

def _hex_to_rgb(color):
    if color[0] == '#':
        color = color[1:]
    if len(color) == 3:
        color = color[0] * 2 + color[1] * 2 + color[2] * 2
    if len(color) != 6:
        raise ValueError('Input #{0} is not in #RRGGBB format ><'.format(color))
    return [int(n, 16) for n in (color[:2], color[2:4], color[4:])]
