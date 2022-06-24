import enum
import os
import platform
import sys

class EnumColorHex(enum.Enum):
    _0 = 0x000000
    _1 = 0x800000
    _2 = 0x008000
    _3 = 0x808000
    _4 = 0x000080
    _5 = 0x800080
    _6 = 0x008080
    _7 = 0xc0c0c0
    _8 = 0x808080
    _9 = 0xff0000
    _10 = 0x00ff00
    _11 = 0xffff00
    _12 = 0x0000ff
    _13 = 0xff00ff
    _14 = 0x00ffff
    _15 = 0xffffff
    _16 = 0x000000
    _17 = 0x00005f
    _18 = 0x000087
    _19 = 0x0000af
    _20 = 0x0000d7
    _21 = 0x0000ff
    _22 = 0x005f00
    _23 = 0x005f5f
    _24 = 0x005f87
    _25 = 0x005faf
    _26 = 0x005fd7
    _27 = 0x005fff
    _28 = 0x008700
    _29 = 0x00875f
    _30 = 0x008787
    _31 = 0x0087af
    _32 = 0x0087d7
    _33 = 0x0087ff
    _34 = 0x00af00
    _35 = 0x00af5f
    _36 = 0x00af87
    _37 = 0x00afaf
    _38 = 0x00afd7
    _39 = 0x00afff
    _40 = 0x00d700
    _41 = 0x00d75f
    _42 = 0x00d787
    _43 = 0x00d7af
    _44 = 0x00d7d7
    _45 = 0x00d7ff
    _46 = 0x00ff00
    _47 = 0x00ff5f
    _48 = 0x00ff87
    _49 = 0x00ffaf
    _50 = 0x00ffd7
    _51 = 0x00ffff
    _52 = 0x5f0000
    _53 = 0x5f005f
    _54 = 0x5f0087
    _55 = 0x5f00af
    _56 = 0x5f00d7
    _57 = 0x5f00ff
    _58 = 0x5f5f00
    _59 = 0x5f5f5f
    _60 = 0x5f5f87
    _61 = 0x5f5faf
    _62 = 0x5f5fd7
    _63 = 0x5f5fff
    _64 = 0x5f8700
    _65 = 0x5f875f
    _66 = 0x5f8787
    _67 = 0x5f87af
    _68 = 0x5f87d7
    _69 = 0x5f87ff
    _70 = 0x5faf00
    _71 = 0x5faf5f
    _72 = 0x5faf87
    _73 = 0x5fafaf
    _74 = 0x5fafd7
    _75 = 0x5fafff
    _76 = 0x5fd700
    _77 = 0x5fd75f
    _78 = 0x5fd787
    _79 = 0x5fd7af
    _80 = 0x5fd7d7
    _81 = 0x5fd7ff
    _82 = 0x5fff00
    _83 = 0x5fff5f
    _84 = 0x5fff87
    _85 = 0x5fffaf
    _86 = 0x5fffd7
    _87 = 0x5fffff
    _88 = 0x870000
    _89 = 0x87005f
    _90 = 0x870087
    _91 = 0x8700af
    _92 = 0x8700d7
    _93 = 0x8700ff
    _94 = 0x875f00
    _95 = 0x875f5f
    _96 = 0x875f87
    _97 = 0x875faf
    _98 = 0x875fd7
    _99 = 0x875fff
    _100 = 0x878700
    _101 = 0x87875f
    _102 = 0x878787
    _103 = 0x8787af
    _104 = 0x8787d7
    _105 = 0x8787ff
    _106 = 0x87af00
    _107 = 0x87af5f
    _108 = 0x87af87
    _109 = 0x87afaf
    _110 = 0x87afd7
    _111 = 0x87afff
    _112 = 0x87d700
    _113 = 0x87d75f
    _114 = 0x87d787
    _115 = 0x87d7af
    _116 = 0x87d7d7
    _117 = 0x87d7ff
    _118 = 0x87ff00
    _119 = 0x87ff5f
    _120 = 0x87ff87
    _121 = 0x87ffaf
    _122 = 0x87ffd7
    _123 = 0x87ffff
    _124 = 0xaf0000
    _125 = 0xaf005f
    _126 = 0xaf0087
    _127 = 0xaf00af
    _128 = 0xaf00d7
    _129 = 0xaf00ff
    _130 = 0xaf5f00
    _131 = 0xaf5f5f
    _132 = 0xaf5f87
    _133 = 0xaf5faf
    _134 = 0xaf5fd7
    _135 = 0xaf5fff
    _136 = 0xaf8700
    _137 = 0xaf875f
    _138 = 0xaf8787
    _139 = 0xaf87af
    _140 = 0xaf87d7
    _141 = 0xaf87ff
    _142 = 0xafaf00
    _143 = 0xafaf5f
    _144 = 0xafaf87
    _145 = 0xafafaf
    _146 = 0xafafd7
    _147 = 0xafafff
    _148 = 0xafd700
    _149 = 0xafd75f
    _150 = 0xafd787
    _151 = 0xafd7af
    _152 = 0xafd7d7
    _153 = 0xafd7ff
    _154 = 0xafff00
    _155 = 0xafff5f
    _156 = 0xafff87
    _157 = 0xafffaf
    _158 = 0xafffd7
    _159 = 0xafffff
    _160 = 0xd70000
    _161 = 0xd7005f
    _162 = 0xd70087
    _163 = 0xd700af
    _164 = 0xd700d7
    _165 = 0xd700ff
    _166 = 0xd75f00
    _167 = 0xd75f5f
    _168 = 0xd75f87
    _169 = 0xd75faf
    _170 = 0xd75fd7
    _171 = 0xd75fff
    _172 = 0xd78700
    _173 = 0xd7875f
    _174 = 0xd78787
    _175 = 0xd787af
    _176 = 0xd787d7
    _177 = 0xd787ff
    _178 = 0xd7af00
    _179 = 0xd7af5f
    _180 = 0xd7af87
    _181 = 0xd7afaf
    _182 = 0xd7afd7
    _183 = 0xd7afff
    _184 = 0xd7d700
    _185 = 0xd7d75f
    _186 = 0xd7d787
    _187 = 0xd7d7af
    _188 = 0xd7d7d7
    _189 = 0xd7d7ff
    _190 = 0xd7ff00
    _191 = 0xd7ff5f
    _192 = 0xd7ff87
    _193 = 0xd7ffaf
    _194 = 0xd7ffd7
    _195 = 0xd7ffff
    _196 = 0xff0000
    _197 = 0xff005f
    _198 = 0xff0087
    _199 = 0xff00af
    _200 = 0xff00d7
    _201 = 0xff00ff
    _202 = 0xff5f00
    _203 = 0xff5f5f
    _204 = 0xff5f87
    _205 = 0xff5faf
    _206 = 0xff5fd7
    _207 = 0xff5fff
    _208 = 0xff8700
    _209 = 0xff875f
    _210 = 0xff8787
    _211 = 0xff87af
    _212 = 0xff87d7
    _213 = 0xff87ff
    _214 = 0xffaf00
    _215 = 0xffaf5f
    _216 = 0xffaf87
    _217 = 0xffafaf
    _218 = 0xffafd7
    _219 = 0xffafff
    _220 = 0xffd700
    _221 = 0xffd75f
    _222 = 0xffd787
    _223 = 0xffd7af
    _224 = 0xffd7d7
    _225 = 0xffd7ff
    _226 = 0xffff00
    _227 = 0xffff5f
    _228 = 0xffff87
    _229 = 0xffffaf
    _230 = 0xffffd7
    _231 = 0xffffff
    _232 = 0x080808
    _233 = 0x121212
    _234 = 0x1c1c1c
    _235 = 0x262626
    _236 = 0x303030
    _237 = 0x3a3a3a
    _238 = 0x444444
    _239 = 0x4e4e4e
    _240 = 0x585858
    _241 = 0x626262
    _242 = 0x6c6c6c
    _243 = 0x767676
    _244 = 0x808080
    _245 = 0x8a8a8a
    _246 = 0x949494
    _247 = 0x9e9e9e
    _248 = 0xa8a8a8
    _249 = 0xb2b2b2
    _250 = 0xbcbcbc
    _251 = 0xc6c6c6
    _252 = 0xd0d0d0
    _253 = 0xdadada
    _254 = 0xe4e4e4
    _255 = 0xeeeeee

class HexColor:

    hex_color = {
        "0": "#000000",
        "1": "#800000",
        "2": "#008000",
        "3": "#808000",
        "4": "#000080",
        "5": "#800080",
        "6": "#008080",
        "7": "#c0c0c0",
        "8": "#808080",
        "9": "#ff0000",
        "10": "#00ff00",
        "11": "#ffff00",
        "12": "#0000ff",
        "13": "#ff00ff",
        "14": "#00ffff",
        "15": "#ffffff",
        "16": "#000000",
        "17": "#00005f",
        "18": "#000087",
        "19": "#0000af",
        "20": "#0000d7",
        "21": "#0000ff",
        "22": "#005f00",
        "23": "#005f5f",
        "24": "#005f87",
        "25": "#005faf",
        "26": "#005fd7",
        "27": "#005fff",
        "28": "#008700",
        "29": "#00875f",
        "30": "#008787",
        "31": "#0087af",
        "32": "#0087d7",
        "33": "#0087ff",
        "34": "#00af00",
        "35": "#00af5f",
        "36": "#00af87",
        "37": "#00afaf",
        "38": "#00afd7",
        "39": "#00afff",
        "40": "#00d700",
        "41": "#00d75f",
        "42": "#00d787",
        "43": "#00d7af",
        "44": "#00d7d7",
        "45": "#00d7ff",
        "46": "#00ff00",
        "47": "#00ff5f",
        "48": "#00ff87",
        "49": "#00ffaf",
        "50": "#00ffd7",
        "51": "#00ffff",
        "52": "#5f0000",
        "53": "#5f005f",
        "54": "#5f0087",
        "55": "#5f00af",
        "56": "#5f00d7",
        "57": "#5f00ff",
        "58": "#5f5f00",
        "59": "#5f5f5f",
        "60": "#5f5f87",
        "61": "#5f5faf",
        "62": "#5f5fd7",
        "63": "#5f5fff",
        "64": "#5f8700",
        "65": "#5f875f",
        "66": "#5f8787",
        "67": "#5f87af",
        "68": "#5f87d7",
        "69": "#5f87ff",
        "70": "#5faf00",
        "71": "#5faf5f",
        "72": "#5faf87",
        "73": "#5fafaf",
        "74": "#5fafd7",
        "75": "#5fafff",
        "76": "#5fd700",
        "77": "#5fd75f",
        "78": "#5fd787",
        "79": "#5fd7af",
        "80": "#5fd7d7",
        "81": "#5fd7ff",
        "82": "#5fff00",
        "83": "#5fff5f",
        "84": "#5fff87",
        "85": "#5fffaf",
        "86": "#5fffd7",
        "87": "#5fffff",
        "88": "#870000",
        "89": "#87005f",
        "90": "#870087",
        "91": "#8700af",
        "92": "#8700d7",
        "93": "#8700ff",
        "94": "#875f00",
        "95": "#875f5f",
        "96": "#875f87",
        "97": "#875faf",
        "98": "#875fd7",
        "99": "#875fff",
        "100": "#878700",
        "101": "#87875f",
        "102": "#878787",
        "103": "#8787af",
        "104": "#8787d7",
        "105": "#8787ff",
        "106": "#87af00",
        "107": "#87af5f",
        "108": "#87af87",
        "109": "#87afaf",
        "110": "#87afd7",
        "111": "#87afff",
        "112": "#87d700",
        "113": "#87d75f",
        "114": "#87d787",
        "115": "#87d7af",
        "116": "#87d7d7",
        "117": "#87d7ff",
        "118": "#87ff00",
        "119": "#87ff5f",
        "120": "#87ff87",
        "121": "#87ffaf",
        "122": "#87ffd7",
        "123": "#87ffff",
        "124": "#af0000",
        "125": "#af005f",
        "126": "#af0087",
        "127": "#af00af",
        "128": "#af00d7",
        "129": "#af00ff",
        "130": "#af5f00",
        "131": "#af5f5f",
        "132": "#af5f87",
        "133": "#af5faf",
        "134": "#af5fd7",
        "135": "#af5fff",
        "136": "#af8700",
        "137": "#af875f",
        "138": "#af8787",
        "139": "#af87af",
        "140": "#af87d7",
        "141": "#af87ff",
        "142": "#afaf00",
        "143": "#afaf5f",
        "144": "#afaf87",
        "145": "#afafaf",
        "146": "#afafd7",
        "147": "#afafff",
        "148": "#afd700",
        "149": "#afd75f",
        "150": "#afd787",
        "151": "#afd7af",
        "152": "#afd7d7",
        "153": "#afd7ff",
        "154": "#afff00",
        "155": "#afff5f",
        "156": "#afff87",
        "157": "#afffaf",
        "158": "#afffd7",
        "159": "#afffff",
        "160": "#d70000",
        "161": "#d7005f",
        "162": "#d70087",
        "163": "#d700af",
        "164": "#d700d7",
        "165": "#d700ff",
        "166": "#d75f00",
        "167": "#d75f5f",
        "168": "#d75f87",
        "169": "#d75faf",
        "170": "#d75fd7",
        "171": "#d75fff",
        "172": "#d78700",
        "173": "#d7875f",
        "174": "#d78787",
        "175": "#d787af",
        "176": "#d787d7",
        "177": "#d787ff",
        "178": "#d7af00",
        "179": "#d7af5f",
        "180": "#d7af87",
        "181": "#d7afaf",
        "182": "#d7afd7",
        "183": "#d7afff",
        "184": "#d7d700",
        "185": "#d7d75f",
        "186": "#d7d787",
        "187": "#d7d7af",
        "188": "#d7d7d7",
        "189": "#d7d7ff",
        "190": "#d7ff00",
        "191": "#d7ff5f",
        "192": "#d7ff87",
        "193": "#d7ffaf",
        "194": "#d7ffd7",
        "195": "#d7ffff",
        "196": "#ff0000",
        "197": "#ff005f",
        "198": "#ff0087",
        "199": "#ff00af",
        "200": "#ff00d7",
        "201": "#ff00ff",
        "202": "#ff5f00",
        "203": "#ff5f5f",
        "204": "#ff5f87",
        "205": "#ff5faf",
        "206": "#ff5fd7",
        "207": "#ff5fff",
        "208": "#ff8700",
        "209": "#ff875f",
        "210": "#ff8787",
        "211": "#ff87af",
        "212": "#ff87d7",
        "213": "#ff87ff",
        "214": "#ffaf00",
        "215": "#ffaf5f",
        "216": "#ffaf87",
        "217": "#ffafaf",
        "218": "#ffafd7",
        "219": "#ffafff",
        "220": "#ffd700",
        "221": "#ffd75f",
        "222": "#ffd787",
        "223": "#ffd7af",
        "224": "#ffd7d7",
        "225": "#ffd7ff",
        "226": "#ffff00",
        "227": "#ffff5f",
        "228": "#ffff87",
        "229": "#ffffaf",
        "230": "#ffffd7",
        "231": "#ffffff",
        "232": "#080808",
        "233": "#121212",
        "234": "#1c1c1c",
        "235": "#262626",
        "236": "#303030",
        "237": "#3a3a3a",
        "238": "#444444",
        "239": "#4e4e4e",
        "240": "#585858",
        "241": "#626262",
        "242": "#6c6c6c",
        "243": "#767676",
        "244": "#808080",
        "245": "#8a8a8a",
        "246": "#949494",
        "247": "#9e9e9e",
        "248": "#a8a8a8",
        "249": "#b2b2b2",
        "250": "#bcbcbc",
        "251": "#c6c6c6",
        "252": "#d0d0d0",
        "253": "#dadada",
        "254": "#e4e4e4",
        "255": "#eeeeee"
    }

    def HEX(self,color):

        if len(color) == 4:
            color = '#'+color[1]*2+color[2]*2+color[3]*2

        for xterm_color, hexcolor in self.hex_color.items():
            if hexcolor == color:
                return xterm_color

        r,g,b = (int(color[1:3],16), int(color[3:5],16), int(color[5:7],16))

        cube = lambda x : x*x
        f = lambda hex_val,ref : cube(int(hex_val,16) - ref)

        min_cube_d=cube(0xFFFFFF)
        nearest = '15'

        for k,h in self.hex_color.items():
            cube_d = f(h[1:3],r) + f(h[3:5],g) + f(h[5:7],b)
            if cube_d < min_cube_d:
                min_cube_d = cube_d
                nearest = k

        return nearest

class StringColor:
    BLACK = (0,0x000000)
    RED = (1,0x800000)
    GREEN = (2,0x008000)
    YELLOW = (3,0x808000)
    BLUE = (4,0x000080)
    MAGENTA = (5,0x800080)
    CYAN = (6,0x008080)
    LIGHT_GRAY = (7,0xc0c0c0)
    DARK_GRAY = (8,0x808080)
    LIGHT_RED = (9,0xff0000)
    LIGHT_GREEN= (10,0x00ff00)
    LIGHT_YELLOW= (11,0xffff00)
    LIGHT_BLUE= (12,0x0000ff)
    LIGHT_MAGENTA= (13,0xff00ff)
    LIGHT_CYAN= (14,0x00ffff)
    WHITE= (15,0xffffff)
    GREY_0= (16,0x000000)
    NAVY_BLUE= (17,0x00005f)
    DARK_BLUE= (18,0x000087)
    BLUE_3A= (19,0x0000af)
    BLUE_3B= (20,0x0000d7)
    BLUE_1= (21,0x0000ff)
    DARK_GREEN= (22,0x005f00)
    DEEP_SKY_BLUE_4A= (23,0x005f5f)
    DEEP_SKY_BLUE_4B= (24,0x005f87)
    DEEP_SKY_BLUE_4C= (25,0x005faf)
    DODGER_BLUE_3= (26,0x005fd7)
    DODGER_BLUE_2= (27,0x005fff)
    GREEN_4= (28,0x008700)
    SPRING_GREEN_4= (29,0x00875f)
    TURQUOISE_4= (30,0x008787)
    DEEP_SKY_BLUE_3A= (31,0x0087af)
    DEEP_SKY_BLUE_3B= (32,0x0087d7)
    DODGER_BLUE_1= (33,0x0087ff)
    GREEN_3A= (34,0x00af00)
    SPRING_GREEN_3A= (35,0x00af5f)
    DARK_CYAN= (36,0x00af87)
    LIGHT_SEA_GREEN= (37,0x00afaf)
    DEEP_SKY_BLUE_2= (38,0x00afd7)
    DEEP_SKY_BLUE_1= (39,0x00afff)
    GREEN_3B= (40,0x00d700)
    SPRING_GREEN_3B= (41,0x00d75f)
    SPRING_GREEN_2A= (42,0x00d787)
    CYAN_3= (43,0x00d7af)
    DARK_TURQUOISE= (44,0x00d7d7)
    TURQUOISE_2= (45,0x00d7ff)
    GREEN_1= (46,0x00ff00)
    SPRING_GREEN_2B= (47,0x00ff5f)
    SPRING_GREEN_1= (48,0x00ff87)
    MEDIUM_SPRING_GREEN= (49,0x00ffaf)
    CYAN_2= (50,0x00ffd7)
    CYAN_1= (51,0x00ffff)
    DARK_RED_1= (52,0x5f0000)
    DEEP_PINK_4A= (53,0x5f005f)
    PURPLE_4A= (54,0x5f0087)
    PURPLE_4B= (55,0x5f00af)
    PURPLE_3= (56,0x5f00d7)
    BLUE_VIOLET= (57,0x5f00ff)
    ORANGE_4A= (58,0x5f5f00)
    GREY_37= (59,0x5f5f5f)
    MEDIUM_PURPLE_4= (60,0x5f5f87)
    SLATE_BLUE_3A= (61,0x5f5faf)
    SLATE_BLUE_3B= (62,0x5f5fd7)
    ROYAL_BLUE_1= (63,0x5f5fff)
    CHARTREUSE_4= (64,0x5f8700)
    DARK_SEA_GREEN_4A= (65,0x5f875f)
    PALE_TURQUOISE_4= (66,0x5f8787)
    STEEL_BLUE= (67,0x5f87af)
    STEEL_BLUE_3= (68,0x5f87d7)
    CORNFLOWER_BLUE= (69,0x5f87ff)
    CHARTREUSE_3A= (70,0x5faf00)
    DARK_SEA_GREEN_4B= (71,0x5faf5f)
    CADET_BLUE_2= (72,0x5faf87)
    CADET_BLUE_1= (73,0x5fafaf)
    SKY_BLUE_3= (74,0x5fafd7)
    STEEL_BLUE_1A= (75,0x5fafff)
    CHARTREUSE_3B= (76,0x5fd700)
    PALE_GREEN_3A= (77,0x5fd75f)
    SEA_GREEN_3= (78,0x5fd787)
    AQUAMARINE_3= (79,0x5fd7af)
    MEDIUM_TURQUOISE= (80,0x5fd7d7)
    STEEL_BLUE_1B= (81,0x5fd7ff)
    CHARTREUSE_2A= (82,0x5fff00)
    SEA_GREEN_2= (83,0x5fff5f)
    SEA_GREEN_1A= (84,0x5fff87)
    SEA_GREEN_1B= (85,0x5fffaf)
    AQUAMARINE_1A= (86,0x5fffd7)
    DARK_SLATE_GRAY_2= (87,0x5fffff)
    DARK_RED_2= (88,0x870000)
    DEEP_PINK_4B= (89,0x87005f)
    DARK_MAGENTA_1= (90,0x870087)
    DARK_MAGENTA_2= (91,0x8700af)
    DARK_VIOLET_1A= (92,0x8700d7)
    PURPLE_1A= (93,0x8700ff)
    ORANGE_4B= (94,0x875f00)
    LIGHT_PINK_4= (95,0x875f5f)
    PLUM_4= (96,0x875f87)
    MEDIUM_PURPLE_3A= (97,0x875faf)
    MEDIUM_PURPLE_3B= (98,0x875fd7)
    SLATE_BLUE_1= (99,0x875fff)
    YELLOW_4A = (100,0x878700)
    WHEAT_4 = (101,0x87875f)
    GREY_53 = (102,0x878787)
    LIGHT_SLATE_GREY = (103,0x8787af)
    MEDIUM_PURPLE = (104,0x8787d7)
    LIGHT_SLATE_BLUE = (105,0x8787ff)
    YELLOW_4B = (106,0x87af00)
    DARK_OLIVE_GREEN_3A = (107,0x87af5f)
    DARK_GREEN_SEA = (108,0x87af87)
    LIGHT_SKY_BLUE_3A = (109,0x87afaf)
    LIGHT_SKY_BLUE_3B = (110,0x87afd7)
    SKY_BLUE_2 = (111,0x87afff)
    CHARTREUSE_2B = (112,0x87d700)
    DARK_OLIVE_GREEN_3B = (113,0x87d75f)
    PALE_GREEN_3B = (114,0x87d787)
    DARK_SEA_GREEN_3A = (115,0x87d7af)
    DARK_SLATE_GRAY_3 = (116,0x87d7d7)
    SKY_BLUE_1 = (117,0x87d7ff)
    CHARTREUSE_1 = (118,0x87ff00)
    LIGHT_GREEN_2 = (119,0x87ff5f)
    LIGHT_GREEN_3 = (120,0x87ff87)
    PALE_GREEN_1A = (121,0x87ffaf)
    AQUAMARINE_1B = (122,0x87ffd7)
    DARK_SLATE_GRAY_1 = (123,0x87ffff)
    RED_3A = (124,0xaf0000)
    DEEP_PINK_4C = (125,0xaf005f)
    MEDIUM_VIOLET_RED = (126,0xaf0087)
    MAGENTA_3A = (127,0xaf00af)
    DARK_VIOLET_1B = (128,0xaf00d7)
    PURPLE_1B = (129,0xaf00ff)
    DARK_ORANGE_3A = (130,0xaf5f00)
    INDIAN_RED_1A = (131,0xaf5f5f)
    HOT_PINK_3A = (132,0xaf5f87)
    MEDIUM_ORCHID_3 = (133,0xaf5faf)
    MEDIUM_ORCHID = (134,0xaf5fd7)
    MEDIUM_PURPLE_2A = (135,0xaf5fff)
    DARK_GOLDENROD = (136,0xaf8700)
    LIGHT_SALMON_3A = (137,0xaf875f)
    ROSY_BROWN = (138,0xaf8787)
    GREY_63 = (139,0xaf87af)
    MEDIUM_PURPLE_2B = (140,0xaf87d7)
    MEDIUM_PURPLE_1 = (141,0xaf87ff)
    GOLD_3A = (142,0xafaf00)
    DARK_KHAKI = (143,0xafaf5f)
    NAVAJO_WHITE_3 = (144,0xafaf87)
    GREY_69 = (145,0xafafaf)
    LIGHT_STEEL_BLUE_3 = (146,0xafafd7)
    LIGHT_STEEL_BLUE = (147,0xafafff)
    YELLOW_3A = (148,0xafd700)
    DARK_OLIVE_GREEN_3 = (149,0xafd75f)
    DARK_SEA_GREEN_3B = (150,0xafd787)
    DARK_SEA_GREEN_2 = (151,0xafd7af)
    LIGHT_CYAN_3 = (152,0xafd7d7)
    LIGHT_SKY_BLUE_1 = (153,0xafd7ff)
    GREEN_YELLOW = (154,0xafff00)
    DARK_OLIVE_GREEN_2 = (155,0xafff5f)
    PALE_GREEN_1B = (156,0xafff87)
    DARK_SEA_GREEN_5B = (157,0xafffaf)
    DARK_SEA_GREEN_5A = (158,0xafffd7)
    PALE_TURQUOISE_1 = (159,0xafffff)
    RED_3B = (160,0xd70000)
    DEEP_PINK_3A = (161,0xd7005f)
    DEEP_PINK_3B = (162,0xd70087)
    MAGENTA_3B = (163,0xd700af)
    MAGENTA_3C = (164,0xd700d7)
    MAGENTA_2A = (165,0xd700ff)
    DARK_ORANGE_3B = (166,0xd75f00)
    INDIAN_RED_1B = (167,0xd75f5f)
    HOT_PINK_3B = (168,0xd75f87)
    HOT_PINK_2 = (169,0xd75faf)
    ORCHID = (170,0xd75fd7)
    MEDIUM_ORCHID_1A = (171,0xd75fff)
    ORANGE_3 = (172,0xd78700)
    LIGHT_SALMON_3B = (173,0xd7875f)
    LIGHT_PINK_3 = (174,0xd78787)
    PINK_3 = (175,0xd787af)
    PLUM_3 = (176,0xd787d7)
    VIOLET = (177,0xd787ff)
    GOLD_3B = (178,0xd7af00)
    LIGHT_GOLDENROD_3 = (179,0xd7af5f)
    TAN = (180,0xd7af87)
    MISTY_ROSE_3 = (181,0xd7afaf)
    THISTLE_3 = (182,0xd7afd7)
    PLUM_2 = (183,0xd7afff)
    YELLOW_3B = (184,0xd7d700)
    KHAKI_3 = (185,0xd7d75f)
    LIGHT_GOLDENROD_2A = (186,0xd7d787)
    LIGHT_YELLOW_3 = (187,0xd7d7af)
    GREY_84 = (188,0xd7d7d7)
    LIGHT_STEEL_BLUE_1 = (189,0xd7d7ff)
    YELLOW_2 = (190,0xd7ff00)
    DARK_OLIVE_GREEN_1A = (191,0xd7ff5f)
    DARK_OLIVE_GREEN_1B = (192,0xd7ff87)
    DARK_SEA_GREEN_1 = (193,0xd7ffaf)
    HONEYDEW_2 = (194,0xd7ffd7)
    LIGHT_CYAN_1 = (195,0xd7ffff)
    RED_1 = (196,0xff0000)
    DEEP_PINK_2 = (197,0xff005f)
    DEEP_PINK_1A = (198,0xff0087)
    DEEP_PINK_1B = (199,0xff00af)
    MAGENTA_2B = (200,0xff00d7)
    MAGENTA_1 = (201,0xff00ff)
    ORANGE_RED_1 = (202,0xff5f00)
    INDIAN_RED_1C = (203,0xff5f5f)
    INDIAN_RED_1D = (204,0xff5f87)
    HOT_PINK_1A = (205,0xff5faf)
    HOT_PINK_1B = (206,0xff5fd7)
    MEDIUM_ORCHID_1B = (207,0xff5fff)
    DARK_ORANGE = (208,0xff8700)
    SALMON_1 = (209,0xff875f)
    LIGHT_CORAL = (210,0xff8787)
    PALE_VIOLET_RED_1 = (211,0xff87af)
    ORCHID_2 = (212,0xff87d7)
    ORCHID_1 = (213,0xff87ff)
    ORANGE_1 = (214,0xffaf00)
    SANDY_BROWN = (215,0xffaf5f)
    LIGHT_SALMON_1 = (216,0xffaf87)
    LIGHT_PINK_1 = (217,0xffafaf)
    PINK_1 = (218,0xffafd7)
    PLUM_1 = (219,0xffafff)
    GOLD_1 = (220,0xffd700)
    LIGHT_GOLDENROD_2B = (221,0xffd75f)
    LIGHT_GOLDENROD_2C = (222,0xffd787)
    NAVAJO_WHITE_1 = (223,0xffd7af)
    MISTY_ROSE1 = (224,0xffd7d7)
    THISTLE_1 = (225,0xffd7ff)
    YELLOW_1 = (226,0xffff00)
    LIGHT_GOLDENROD_1 = (227,0xffff5f)
    KHAKI_1 = (228,0xffff87)
    WHEAT_1 = (229,0xffffaf)
    CORNSILK_1 = (230,0xffffd7)
    GREY_100 = (231,0xffffff)
    GREY_3 = (232,0x080808)
    GREY_7 = (233,0x121212)
    GREY_11 = (234,0x1c1c1c)
    GREY_15 = (235,0x262626)
    GREY_19 = (236,0x303030)
    GREY_23 = (237,0x3a3a3a)
    GREY_27 = (238,0x444444)
    GREY_30 = (239,0x4e4e4e)
    GREY_35 = (240,0x585858)
    GREY_39 = (241,0x626262)
    GREY_42 = (242,0x6c6c6c)
    GREY_46 = (243,0x767676)
    GREY_50 = (244,0x808080)
    GREY_54 = (245,0x8a8a8a)
    GREY_58 = (246,0x949494)
    GREY_62 = (247,0x9e9e9e)
    GREY_66 = (248,0xa8a8a8)
    GREY_70 = (249,0xb2b2b2)
    GREY_74 = (250,0xbcbcbc)
    GREY_78 = (251,0xc6c6c6)
    GREY_82 = (252,0xd0d0d0)
    GREY_85 = (253,0xdadada)
    GREY_89 = (254,0xe4e4e4)
    GREY_9 = (255,0xeeeeee)

class Name:

    names = [
    'BLACK',
    'RED',
    'GREEN',
    'YELLOW',
    'BLUE',
    'MAGENTA',
    'CYAN',
    'LIGHT_GRAY',
    'DARK_GRAY',
    'LIGHT_RED',
    'LIGHT_GREEN',
    'LIGHT_YELLOW',
    'LIGHT_BLUE',
    'LIGHT_MAGENTA',
    'LIGHT_CYAN',
    'WHITE',
    'GREY_0',
    'NAVY_BLUE',
    'DARK_BLUE',
    'BLUE_3A',
    'BLUE_3B',
    'BLUE_1',
    'DARK_GREEN',
    'DEEP_SKY_BLUE_4A',
    'DEEP_SKY_BLUE_4B',
    'DEEP_SKY_BLUE_4C',
    'DODGER_BLUE_3',
    'DODGER_BLUE_2',
    'GREEN_4',
    'SPRING_GREEN_4',
    'TURQUOISE_4',
    'DEEP_SKY_BLUE_3A',
    'DEEP_SKY_BLUE_3B',
    'DODGER_BLUE_1',
    'GREEN_3A',
    'SPRING_GREEN_3A',
    'DARK_CYAN',
    'LIGHT_SEA_GREEN',
    'DEEP_SKY_BLUE_2',
    'DEEP_SKY_BLUE_1',
    'GREEN_3B',
    'SPRING_GREEN_3B',
    'SPRING_GREEN_2A',
    'CYAN_3',
    'DARK_TURQUOISE',
    'TURQUOISE_2',
    'GREEN_1',
    'SPRING_GREEN_2B',
    'SPRING_GREEN_1',
    'MEDIUM_SPRING_GREEN',
    'CYAN_2',
    'CYAN_1',
    'DARK_RED_1',
    'DEEP_PINK_4A',
    'PURPLE_4A',
    'PURPLE_4B',
    'PURPLE_3',
    'BLUE_VIOLET',
    'ORANGE_4A',
    'GREY_37',
    'MEDIUM_PURPLE_4',
    'SLATE_BLUE_3A',
    'SLATE_BLUE_3B',
    'ROYAL_BLUE_1',
    'CHARTREUSE_4',
    'DARK_SEA_GREEN_4A',
    'PALE_TURQUOISE_4',
    'STEEL_BLUE',
    'STEEL_BLUE_3',
    'CORNFLOWER_BLUE',
    'CHARTREUSE_3A',
    'DARK_SEA_GREEN_4B',
    'CADET_BLUE_2',
    'CADET_BLUE_1',
    'SKY_BLUE_3',
    'STEEL_BLUE_1A',
    'CHARTREUSE_3B',
    'PALE_GREEN_3A',
    'SEA_GREEN_3',
    'AQUAMARINE_3',
    'MEDIUM_TURQUOISE',
    'STEEL_BLUE_1B',
    'CHARTREUSE_2A',
    'SEA_GREEN_2',
    'SEA_GREEN_1A',
    'SEA_GREEN_1B',
    'AQUAMARINE_1A',
    'DARK_SLATE_GRAY_2',
    'DARK_RED_2',
    'DEEP_PINK_4B',
    'DARK_MAGENTA_1',
    'DARK_MAGENTA_2',
    'DARK_VIOLET_1A',
    'PURPLE_1A',
    'ORANGE_4B',
    'LIGHT_PINK_4',
    'PLUM_4',
    'MEDIUM_PURPLE_3A',
    'MEDIUM_PURPLE_3B',
    'SLATE_BLUE_1',
    'YELLOW_4A',
    'WHEAT_4',
    'GREY_53',
    'LIGHT_SLATE_GREY',
    'MEDIUM_PURPLE',
    'LIGHT_SLATE_BLUE',
    'YELLOW_4B',
    'DARK_OLIVE_GREEN_3A',
    'DARK_GREEN_SEA',
    'LIGHT_SKY_BLUE_3A',
    'LIGHT_SKY_BLUE_3B',
    'SKY_BLUE_2',
    'CHARTREUSE_2B',
    'DARK_OLIVE_GREEN_3B',
    'PALE_GREEN_3B',
    'DARK_SEA_GREEN_3A',
    'DARK_SLATE_GRAY_3',
    'SKY_BLUE_1',
    'CHARTREUSE_1',
    'LIGHT_GREEN_2',
    'LIGHT_GREEN_3',
    'PALE_GREEN_1A',
    'AQUAMARINE_1B',
    'DARK_SLATE_GRAY_1',
    'RED_3A',
    'DEEP_PINK_4C',
    'MEDIUM_VIOLET_RED',
    'MAGENTA_3A',
    'DARK_VIOLET_1B',
    'PURPLE_1B',
    'DARK_ORANGE_3A',
    'INDIAN_RED_1A',
    'HOT_PINK_3A',
    'MEDIUM_ORCHID_3',
    'MEDIUM_ORCHID',
    'MEDIUM_PURPLE_2A',
    'DARK_GOLDENROD',
    'LIGHT_SALMON_3A',
    'ROSY_BROWN',
    'GREY_63',
    'MEDIUM_PURPLE_2B',
    'MEDIUM_PURPLE_1',
    'GOLD_3A',
    'DARK_KHAKI',
    'NAVAJO_WHITE_3',
    'GREY_69',
    'LIGHT_STEEL_BLUE_3',
    'LIGHT_STEEL_BLUE',
    'YELLOW_3A',
    'DARK_OLIVE_GREEN_3',
    'DARK_SEA_GREEN_3B',
    'DARK_SEA_GREEN_2',
    'LIGHT_CYAN_3',
    'LIGHT_SKY_BLUE_1',
    'GREEN_YELLOW',
    'DARK_OLIVE_GREEN_2',
    'PALE_GREEN_1B',
    'DARK_SEA_GREEN_5B',
    'DARK_SEA_GREEN_5A',
    'PALE_TURQUOISE_1',
    'RED_3B',
    'DEEP_PINK_3A',
    'DEEP_PINK_3B',
    'MAGENTA_3B',
    'MAGENTA_3C',
    'MAGENTA_2A',
    'DARK_ORANGE_3B',
    'INDIAN_RED_1B',
    'HOT_PINK_3B',
    'HOT_PINK_2',
    'ORCHID',
    'MEDIUM_ORCHID_1A',
    'ORANGE_3',
    'LIGHT_SALMON_3B',
    'LIGHT_PINK_3',
    'PINK_3',
    'PLUM_3',
    'VIOLET',
    'GOLD_3B',
    'LIGHT_GOLDENROD_3',
    'TAN',
    'MISTY_ROSE_3',
    'THISTLE_3',
    'PLUM_2',
    'YELLOW_3B',
    'KHAKI_3',
    'LIGHT_GOLDENROD_2A',
    'LIGHT_YELLOW_3',
    'GREY_84',
    'LIGHT_STEEL_BLUE_1',
    'YELLOW_2',
    'DARK_OLIVE_GREEN_1A',
    'DARK_OLIVE_GREEN_1B',
    'DARK_SEA_GREEN_1',
    'HONEYDEW_2',
    'LIGHT_CYAN_1',
    'RED_1',
    'DEEP_PINK_2',
    'DEEP_PINK_1A',
    'DEEP_PINK_1B',
    'MAGENTA_2B',
    'MAGENTA_1',
    'ORANGE_RED_1',
    'INDIAN_RED_1C',
    'INDIAN_RED_1D',
    'HOT_PINK_1A',
    'HOT_PINK_1B',
    'MEDIUM_ORCHID_1B',
    'DARK_ORANGE',
    'SALMON_1',
    'LIGHT_CORAL',
    'PALE_VIOLET_RED_1',
    'ORCHID_2',
    'ORCHID_1',
    'ORANGE_1',
    'SANDY_BROWN',
    'LIGHT_SALMON_1',
    'LIGHT_PINK_1',
    'PINK_1',
    'PLUM_1',
    'GOLD_1',
    'LIGHT_GOLDENROD_2B',
    'LIGHT_GOLDENROD_2C',
    'NAVAJO_WHITE_1',
    'MISTY_ROSE1',
    'THISTLE_1',
    'YELLOW_1',
    'LIGHT_GOLDENROD_1',
    'KHAKI_1',
    'WHEAT_1',
    'CORNSILK_1',
    'GREY_100',
    'GREY_3',
    'GREY_7',
    'GREY_11',
    'GREY_15',
    'GREY_19',
    'GREY_23',
    'GREY_27',
    'GREY_30',
    'GREY_35',
    'GREY_39',
    'GREY_42',
    'GREY_46',
    'GREY_50',
    'GREY_54',
    'GREY_58',
    'GREY_62',
    'GREY_66',
    'GREY_70',
    'GREY_74',
    'GREY_78',
    'GREY_82',
    'GREY_85',
    'GREY_89',
    'GREY_93'
    ]

class back(object):

    ESC = '\x1b[48;5;'
    END = 'm'
    num = 0
    for color in Name().names:
        vars()[color] = '{}{}{}'.format(ESC, num, END)
        num += 1

class fore(object):

    ESC = '\x1b[38;5;'
    END = 'm'
    num = 0
    for color in Name().names:
        vars()[color] = '{}{}{}'.format(ESC, num, END)
        num += 1

class style(object):

    ESC = "\x1b["
    END = "m"

    names = {
        'BOLD': 1,
        'DIM': 2,
        'UNDERLINED': 4,
        'BLINK': 5,
        'REVERSE': 7,
        'HIDDEN': 8,
        'RESET': 0,
        'RES_BOLD': 21,
        'RES_DIM': 22,
        'RES_UNDERLINED': 24,
        'RES_BLINK': 25,
        'RES_REVERSE': 27,
        'RES_HIDDEN': 28
    }

    for color, num in names.items():
        vars()[color] = '{}{}{}'.format(ESC, num, END)


TTY_AWARE = True
IS_TTY = sys.stdout.isatty() and sys.stderr.isatty()

_win_vterm_mode = None

class colored(object):

    def __init__(self, color='#000000'):

        self.ESC = "\x1b["
        self.END = "m"
        self.color = color
        self.enable_windows_terminal_mode()

        if str(color).startswith("#"):
            self.HEX = HexColor().HEX(color.casefold())
        else:
            self.HEX = ""

        self.paint = {
            "black": "0",
            "red": "1",
            "green": "2",
            "yellow": "3",
            "blue": "4",
            "magenta": "5",
            "cyan": "6",
            "light_gray": "7",
            "dark_gray": "8",
            "light_red": "9",
            "light_green": "10",
            "light_yellow": "11",
            "light_blue": "12",
            "light_magenta": "13",
            "light_cyan": "14",
            "white": "15",
            "grey_0": "16",
            "navy_blue": "17",
            "dark_blue": "18",
            "blue_3a": "19",
            "blue_3b": "20",
            "blue_1": "21",
            "dark_green": "22",
            "deep_sky_blue_4a": "23",
            "deep_sky_blue_4b": "24",
            "deep_sky_blue_4c": "25",
            "dodger_blue_3": "26",
            "dodger_blue_2": "27",
            "green_4": "28",
            "spring_green_4": "29",
            "turquoise_4": "30",
            "deep_sky_blue_3a": "31",
            "deep_sky_blue_3b": "32",
            "dodger_blue_1": "33",
            "green_3a": "34",
            "spring_green_3a": "35",
            "dark_cyan": "36",
            "light_sea_green": "37",
            "deep_sky_blue_2": "38",
            "deep_sky_blue_1": "39",
            "green_3b": "40",
            "spring_green_3b": "41",
            "spring_green_2a": "42",
            "cyan_3": "43",
            "dark_turquoise": "44",
            "turquoise_2": "45",
            "green_1": "46",
            "spring_green_2b": "47",
            "spring_green_1": "48",
            "medium_spring_green": "49",
            "cyan_2": "50",
            "cyan_1": "51",
            "dark_red_1": "52",
            "deep_pink_4a": "53",
            "purple_4a": "54",
            "purple_4b": "55",
            "purple_3": "56",
            "blue_violet": "57",
            "orange_4a": "58",
            "grey_37": "59",
            "medium_purple_4": "60",
            "slate_blue_3a": "61",
            "slate_blue_3b": "62",
            "royal_blue_1": "63",
            "chartreuse_4": "64",
            "dark_sea_green_4a": "65",
            "pale_turquoise_4": "66",
            "steel_blue": "67",
            "steel_blue_3": "68",
            "cornflower_blue": "69",
            "chartreuse_3a": "70",
            "dark_sea_green_4b": "71",
            "cadet_blue_2": "72",
            "cadet_blue_1": "73",
            "sky_blue_3": "74",
            "steel_blue_1a": "75",
            "chartreuse_3b": "76",
            "pale_green_3a": "77",
            "sea_green_3": "78",
            "aquamarine_3": "79",
            "medium_turquoise": "80",
            "steel_blue_1b": "81",
            "chartreuse_2a": "82",
            "sea_green_2": "83",
            "sea_green_1a": "84",
            "sea_green_1b": "85",
            "aquamarine_1a": "86",
            "dark_slate_gray_2": "87",
            "dark_red_2": "88",
            "deep_pink_4b": "89",
            "dark_magenta_1": "90",
            "dark_magenta_2": "91",
            "dark_violet_1a": "92",
            "purple_1a": "93",
            "orange_4b": "94",
            "light_pink_4": "95",
            "plum_4": "96",
            "medium_purple_3a": "97",
            "medium_purple_3b": "98",
            "slate_blue_1": "99",
            "yellow_4a": "100",
            "wheat_4": "101",
            "grey_53": "102",
            "light_slate_grey": "103",
            "medium_purple": "104",
            "light_slate_blue": "105",
            "yellow_4b": "106",
            "dark_olive_green_3a": "107",
            "dark_green_sea": "108",
            "light_sky_blue_3a": "109",
            "light_sky_blue_3b": "110",
            "sky_blue_2": "111",
            "chartreuse_2b": "112",
            "dark_olive_green_3b": "113",
            "pale_green_3b": "114",
            "dark_sea_green_3a": "115",
            "dark_slate_gray_3": "116",
            "sky_blue_1": "117",
            "chartreuse_1": "118",
            "light_green_2": "119",
            "light_green_3": "120",
            "pale_green_1a": "121",
            "aquamarine_1b": "122",
            "dark_slate_gray_1": "123",
            "red_3a": "124",
            "deep_pink_4c": "125",
            "medium_violet_red": "126",
            "magenta_3a": "127",
            "dark_violet_1b": "128",
            "purple_1b": "129",
            "dark_orange_3a": "130",
            "indian_red_1a": "131",
            "hot_pink_3a": "132",
            "medium_orchid_3": "133",
            "medium_orchid": "134",
            "medium_purple_2a": "135",
            "dark_goldenrod": "136",
            "light_salmon_3a": "137",
            "rosy_brown": "138",
            "grey_63": "139",
            "medium_purple_2b": "140",
            "medium_purple_1": "141",
            "gold_3a": "142",
            "dark_khaki": "143",
            "navajo_white_3": "144",
            "grey_69": "145",
            "light_steel_blue_3": "146",
            "light_steel_blue": "147",
            "yellow_3a": "148",
            "dark_olive_green_3": "149",
            "dark_sea_green_3b": "150",
            "dark_sea_green_2": "151",
            "light_cyan_3": "152",
            "light_sky_blue_1": "153",
            "green_yellow": "154",
            "dark_olive_green_2": "155",
            "pale_green_1b": "156",
            "dark_sea_green_5b": "157",
            "dark_sea_green_5a": "158",
            "pale_turquoise_1": "159",
            "red_3b": "160",
            "deep_pink_3a": "161",
            "deep_pink_3b": "162",
            "magenta_3b": "163",
            "magenta_3c": "164",
            "magenta_2a": "165",
            "dark_orange_3b": "166",
            "indian_red_1b": "167",
            "hot_pink_3b": "168",
            "hot_pink_2": "169",
            "orchid": "170",
            "medium_orchid_1a": "171",
            "orange_3": "172",
            "light_salmon_3b": "173",
            "light_pink_3": "174",
            "pink_3": "175",
            "plum_3": "176",
            "violet": "177",
            "gold_3b": "178",
            "light_goldenrod_3": "179",
            "tan": "180",
            "misty_rose_3": "181",
            "thistle_3": "182",
            "plum_2": "183",
            "yellow_3b": "184",
            "khaki_3": "185",
            "light_goldenrod_2a": "186",
            "light_yellow_3": "187",
            "grey_84": "188",
            "light_steel_blue_1": "189",
            "yellow_2": "190",
            "dark_olive_green_1a": "191",
            "dark_olive_green_1b": "192",
            "dark_sea_green_1": "193",
            "honeydew_2": "194",
            "light_cyan_1": "195",
            "red_1": "196",
            "deep_pink_2": "197",
            "deep_pink_1a": "198",
            "deep_pink_1b": "199",
            "magenta_2b": "200",
            "magenta_1": "201",
            "orange_red_1": "202",
            "indian_red_1c": "203",
            "indian_red_1d": "204",
            "hot_pink_1a": "205",
            "hot_pink_1b": "206",
            "medium_orchid_1b": "207",
            "dark_orange": "208",
            "salmon_1": "209",
            "light_coral": "210",
            "pale_violet_red_1": "211",
            "orchid_2": "212",
            "orchid_1": "213",
            "orange_1": "214",
            "sandy_brown": "215",
            "light_salmon_1": "216",
            "light_pink_1": "217",
            "pink_1": "218",
            "plum_1": "219",
            "gold_1": "220",
            "light_goldenrod_2b": "221",
            "light_goldenrod_2c": "222",
            "navajo_white_1": "223",
            "misty_rose1": "224",
            "thistle_1": "225",
            "yellow_1": "226",
            "light_goldenrod_1": "227",
            "khaki_1": "228",
            "wheat_1": "229",
            "cornsilk_1": "230",
            "grey_100": "231",
            "grey_3": "232",
            "grey_7": "233",
            "grey_11": "234",
            "grey_15": "235",
            "grey_19": "236",
            "grey_23": "237",
            "grey_27": "238",
            "grey_30": "239",
            "grey_35": "240",
            "grey_39": "241",
            "grey_42": "242",
            "grey_46": "243",
            "grey_50": "244",
            "grey_54": "245",
            "grey_58": "246",
            "grey_62": "247",
            "grey_66": "248",
            "grey_70": "249",
            "grey_74": "250",
            "grey_78": "251",
            "grey_82": "252",
            "grey_85": "253",
            "grey_89": "254",
            "grey_93": "255",
        }

    def attribute(self):
        if not self.enabled():
            return ""

        paint = {
            "bold": self.ESC + "1" + self.END,
            1: self.ESC + "1" + self.END,
            "dim": self.ESC + "2" + self.END,
            2: self.ESC + "2" + self.END,
            "underlined": self.ESC + "4" + self.END,
            4: self.ESC + "4" + self.END,
            "blink": self.ESC + "5" + self.END,
            5: self.ESC + "5" + self.END,
            "reverse": self.ESC + "7" + self.END,
            7: self.ESC + "7" + self.END,
            "hidden": self.ESC + "8" + self.END,
            8: self.ESC + "8" + self.END,
            "reset": self.ESC + "0" + self.END,
            0: self.ESC + "0" + self.END,
            "res_bold": self.ESC + "21" + self.END,
            21: self.ESC + "21" + self.END,
            "res_dim": self.ESC + "22" + self.END,
            22: self.ESC + "22" + self.END,
            "res_underlined": self.ESC + "24" + self.END,
            24: self.ESC + "24" + self.END,
            "res_blink": self.ESC + "25" + self.END,
            25: self.ESC + "25" + self.END,
            "res_reverse": self.ESC + "27" + self.END,
            27: self.ESC + "27" + self.END,
            "res_hidden": self.ESC + "28" + self.END,
            28: self.ESC + "28" + self.END,
        }
        return paint[self.color]

    def foreground(self):
        if not self.enabled():
            return ""
        code = self.ESC + "38;5;"
        if str(self.color).isdigit():
            self.reverse_dict()
            color = self.reserve_paint[str(self.color)]
            return code + self.paint[color] + self.END
        elif self.color.startswith("#"):
            return code + str(self.HEX) + self.END
        else:
            return code + self.paint[self.color] + self.END

    def background(self):
        if not self.enabled():
            return ""
        code = self.ESC + "48;5;"
        if str(self.color).isdigit():
            self.reverse_dict()
            color = self.reserve_paint[str(self.color)]
            return code + self.paint[color] + self.END
        elif self.color.startswith("#"):
            return code + str(self.HEX) + self.END
        else:
            return code + self.paint[self.color] + self.END

    def reverse_dict(self):
        self.reserve_paint = dict(zip(self.paint.values(), self.paint.keys()))

    def enable_windows_terminal_mode(self):
        global _win_vterm_mode
        if _win_vterm_mode != None:
            return _win_vterm_mode

        _win_vterm_mode = platform.system().casefold() == 'windows'
        if _win_vterm_mode == False:
            return

        from ctypes import windll, c_int, byref, c_void_p
        ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
        INVALID_HANDLE_VALUE = c_void_p(-1).value
        STD_OUTPUT_HANDLE = c_int(-11)

        hStdout = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        if hStdout == INVALID_HANDLE_VALUE:
            _win_vterm_mode = False
            return

        mode = c_int(0)
        ok = windll.kernel32.GetConsoleMode(c_int(hStdout), byref(mode))
        if not ok:
            _win_vterm_mode = False
            return

        mode = c_int(mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING)
        ok = windll.kernel32.SetConsoleMode(c_int(hStdout), mode)
        if not ok:
            _win_vterm_mode = False
            return

    def enabled(self):

        if "FORCE_COLOR" in os.environ:
            if int(os.environ["FORCE_COLOR"]) == 0:
                return False
            else:
                return True

        if "NO_COLOR" in os.environ:
            return False

        if TTY_AWARE and not IS_TTY:
            return False

        return True

class Printf:

    def attr(color):
        return colored(color).attribute()

    def fg(color):
        return colored(color).foreground()

    def bg(color):
        return colored(color).background()

def stylize(text, styles, reset=True):
    terminator = Printf.attr("reset") if reset else ""
    return "{}{}{}".format("".join(styles), text, terminator)


def _c0wrap(styles) -> str:
    C0_SOH = '\x01'
    C0_STX = '\x02'
    return "{}{}{}".format(C0_SOH, "".join(styles), C0_STX)


def stylize_interactive(text, styles, reset=True) -> str:
    terminator = _c0wrap(Printf.attr("reset")) if reset else ""
    return "{}{}{}".format(_c0wrap(styles), text, terminator)

def set_tty_aware(awareness=True):
    global TTY_AWARE
    TTY_AWARE = awareness
