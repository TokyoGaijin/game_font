import pygame
from pixel import Pixel


class GUI:
    def __init__(self, surface, size = 1, color = (255, 255, 255)):
        self.color = color
        self.surface = surface
        self.size = size
        self.surface.fill(color)
        self.output_string = []
        self.numbers_blueprint = [
            [
             "--",
             "--",
             "--",
             "--",
             "--",
             ],
             [
             "-111-",
             "1---1",
             "1-1-1",
             "1---1",
             "-111-",
             ],
             [
             "-11--",
             "--1--",
             "--1--",
             "--1--",
             "11111",
             ],
             [
             "-111-",
             "1---1",
             "---1-",
             "--1--",
             "11111",
             ],
             [
             "-111-",
             "1---1",
             "--111",
             "1---1",
             "-111-",
             ],
             [
             "-1--1",
             "1---1",
             "11111",
             "----1",
             "----1",
             ],
             [
             "11111",
             "1----",
             "-111-",
             "----1",
             "1111-",
             ],
             [
             "-1111",
             "1----",
             "1111-",
             "1---1",
             "-111-",
             ],
             [
             "11111",
             "----1",
             "---1-",
             "--1--",
             "-1---",
             ],
             [
             "-111-",
             "1---1",
             "-111-",
             "1---1",
             "-111-",
             ],
             [
             "-111-",
             "1---1",
             "-111-",
             "----1",
             "-111-",
             ],

        ]

        self.letters_blueprint = [
            [
             "-----",
             "-----",
             "-----",
             "-----",
             "-----",
             ],
             [
             "--1--",
             "-1-1-",
             "11111",
             "1---1",
             "1---1",
             ],
             [
             "1111-",
             "1---1",
             "1111-",
             "1---1",
             "1111-",
             ],
             [
             "-111-",
             "1---1",
             "1----",
             "1---1",
             "-111-",
             ],
             [
             "111--",
             "1--1-",
             "1---1",
             "1--1-",
             "111--",
             ],
             [
             "11111",
             "1----",
             "1111-",
             "1----",
             "11111",
             ],
             [
             "11111",
             "1----",
             "1111-",
             "1----",
             "1----",
             ],
             [
             "-1111",
             "1----",
             "1-111",
             "1---1",
             "-1111",
             ],
             [
             "1---1",
             "1---1",
             "11111",
             "1---1",
             "1---1",
             ],
             [
             "-111-",
             "--1--",
             "--1--",
             "--1--",
             "-111-",
             ],
             [
             "----1",
             "----1",
             "----1",
             "1---1",
             "-111-",
             ],
             [
             "1--1-",
             "1-1--",
             "111--",
             "1--1-",
             "1---1",
             ],
             [
             "1----",
             "1----",
             "1----",
             "1----",
             "11111",
             ],
             [
             "1---1",
             "11-11",
             "1-1-1",
             "1---1",
             "1---1",
             ],
             [
             "1---1",
             "11--1",
             "1-1-1",
             "1--11",
             "1---1",
             ],
             [
             "-111-",
             "1---1",
             "1---1",
             "1---1",
             "-111-",
             ],
             [
             "1111-",
             "1---1",
             "1111-",
             "1----",
             "1----",
             ],
             [
             "-111-",
             "1---1",
             "1---1",
             "1--11",
             "-11-1",
             ],
             [
             "1111-",
             "1---1",
             "1111-",
             "1---1",
             "1---1",
             ],
             [
             "-111-",
             "1----",
             "-111-",
             "----1",
             "-111-",
             ],
             [
             "11111",
             "--1--",
             "--1--",
             "--1--",
             "--1--",
             ],
             [
             "1---1",
             "1---1",
             "1---1",
             "1---1",
             "-111-",
             ],
             [
             "1---1",
             "1---1",
             "1---1",
             "-1-1-",
             "--1--",
             ],
             [
             "1---1",
             "1---1",
             "1-1-1",
             "1-1-1",
             "-1-1-",
             ],
             [
             "1---1",
             "-1-1-",
             "--1--",
             "-1-1-",
             "1---1",
             ],
             [
             "1---1",
             "-1-1-",
             "--1--",
             "--1--",
             "--1--",
             ],
             [
             "11111",
             "---1-",
             "--1--",
             "-1---",
             "11111",
             ],
             # lower case letters here
             [
             "-----",
             "-----",
             "-11-1",
             "1--11",
             "-11-1",
             ],
             [
             "1----",
             "1----",
             "1-11-",
             "11--1",
             "1-11-",
             ],
             [
             "-----",
             "-----",
             "-111-",
             "1----",
             "-111-",
             ],
             [
             "----1",
             "----1",
             "-11-1",
             "1--11",
             "-11-1",
             ],
             [
             "-11--",
             "1--1-",
             "11111",
             "1----",
             "-111--",
             ],
             [
             "--11-",
             "-1---",
             "11111",
             "-1---",
             "-1---",
             ],
             [
             "-----",
             "-----",
             "-11-1",
             "1--11",
             "-11-1",
             "----1",
             "-111-",
             ],
             [
             "1----",
             "1----",
             "1-11-",
             "11--1",
             "1---1",
             ],
             [
             "--1--",
             "-----",
             "--1--",
             "--1--",
             "--1--",
             ],
             [
             "----1",
             "-----",
             "----1",
             "----1",
             "----1",
             "----1",
             "-111-",
             ],
             [
             "1----",
             "1----",
             "1-1--",
             "11---",
             "1-1--",
             ],
             [
             "--1--",
             "--1--",
             "--1--",
             "--1--",
             "--1--",
             ],
             [
             "-----",
             "-----",
             "11-1-",
             "1-1-1",
             "1---1",
             ],
             [
             "-----",
             "-----",
             "1-11-",
             "11--1",
             "1---1",
             ],
             [
             "-----",
             "-----",
             "-111-",
             "1---1",
             "-111-",
             ],
             [
              "-----",
             "-----",
             "1-11-",
             "11--1",
             "1-11-",
             "1----",
             "1----",
             ],
             [
              "-----",
             "-----",
             "-11-1",
             "1--11",
             "-11-1",
             "----1",
             "----1",
             ],
             [
             "-----",
             "-----",
             "1-11-",
             "11---",
             "1----",
             ],
             [
             "-----",
             "-1111",
             "11---",
             "--111",
             "1111-",
             ],
             [
             "-----",
             "--1--",
             "-111-",
             "--1--",
             "--11-",
             ],
             [
             "-----",
             "-----",
             "1---1",
             "1--11",
             "-11-1",
             ],
             [
             "-----",
             "-----",
             "1---1",
             "-1-1-",
             "--1--",
             ],
             [
             "-----",
             "-----",
             "1---1",
             "1-1-1",
             "-1-1-",
             ],
             [
             "-----",
             "-----",
             "1---1",
             "-111-",
             "1---1",
             ],
             [
              "-----",
             "-----",
             "-1--1",
             "--1-1",
             "---11",
             "---1-",
             "--1--",
             ],
             [
             "-----",
             "11111",
             "--11-",
             "-11--",
             "11111",
             ],
        ]

        self.special_chars = [
            [
                "-----",
                "--1--",
                "-----",
                "--1--",
                "-----",
                ],

            [
                "--1--",
                "--1--",
                "--1--",
                "-----",
                "--1--",
                ],

            [
                "-111-",
                "1---1",
                "---1-",
                "-----",
                "--1--",
                ],

            [
                "-1-1-",
                "11111",
                "-1-1-",
                "111111",
                "-1-1-",
                ],

            [
                "1---1",
                "---1-",
                "--1--",
                "-1---",
                "1---1",
                ],

                [
                "-----",
                "-----",
                "11111",
                "-----",
                "-----",
                ],

                [
                "--1--",
                "--1--",
                "11111",
                "--1--",
                "--1--",
                ],

                [
                "-----",
                "11111",
                "-----",
                "11111",
                "-----",
                ],

                [
                    "-----",
                    "-----",
                    "-----",
                    "-----",
                    "11111"
                ],
                [
                    "--111",
                    "--1--",
                    "--1--",
                    "--1--",
                    "--111"
                ],
                [
                    "111--",
                    "--1--",
                    "--1--",
                    "--1--",
                    "111--"
                ],
                [
                    # Go back icon
                    "--1--",
                    "-1---",
                    "11111",
                    "-1---",
                    "--1--"
                ],
                [
                    # Cancel Icon
                    "-----",
                    "-1-1-",
                    "--1--",
                    "-1-1-",
                    "-----"
                ],
                [
                    # Confirm icon
                    "-----",
                    "----1",
                    "---1-",
                    "1-1--",
                    "-1---"
                ],
                [
                    # .
                    "-----",
                    "-----",
                    "-----",
                    "-----",
                    "1----"
                ],
                [
                    # '
                    "-1---",
                    "-1---",
                    "-----",
                    "-----",
                    "-----"
                ],
                
        ]

        self.font_dict = {
            " ": self.letters_blueprint[0],
            "0": self.numbers_blueprint[1],
            "1": self.numbers_blueprint[2],
            "2": self.numbers_blueprint[3],
            "3": self.numbers_blueprint[4],
            "4": self.numbers_blueprint[5],
            "5": self.numbers_blueprint[6],
            "6": self.numbers_blueprint[7],
            "7": self.numbers_blueprint[8],
            "8": self.numbers_blueprint[9],
            "9": self.numbers_blueprint[10],
            "A": self.letters_blueprint[1],
            "B": self.letters_blueprint[2],
            "C": self.letters_blueprint[3],
            "D": self.letters_blueprint[4],
            "E": self.letters_blueprint[5],
            "F": self.letters_blueprint[6],
            "G": self.letters_blueprint[7],
            "H": self.letters_blueprint[8],
            "I": self.letters_blueprint[9],
            "J": self.letters_blueprint[10],
            "K": self.letters_blueprint[11],
            "L": self.letters_blueprint[12],
            "M": self.letters_blueprint[13],
            "N": self.letters_blueprint[14],
            "O": self.letters_blueprint[15],
            "P": self.letters_blueprint[16],
            "Q": self.letters_blueprint[17],
            "R": self.letters_blueprint[18],
            "S": self.letters_blueprint[19],
            "T": self.letters_blueprint[20],
            "U": self.letters_blueprint[21],
            "V": self.letters_blueprint[22],
            "W": self.letters_blueprint[23],
            "X": self.letters_blueprint[24],
            "Y": self.letters_blueprint[25],
            "Z": self.letters_blueprint[26],
            "a": self.letters_blueprint[27],
            "b": self.letters_blueprint[28],
            "c": self.letters_blueprint[29],
            "d": self.letters_blueprint[30],
            "e": self.letters_blueprint[31],
            "f": self.letters_blueprint[32],
            "g": self.letters_blueprint[33],
            "h": self.letters_blueprint[34],
            "i": self.letters_blueprint[35],
            "j": self.letters_blueprint[36],
            "k": self.letters_blueprint[37],
            "l": self.letters_blueprint[38],
            "m": self.letters_blueprint[39],
            "n": self.letters_blueprint[40],
            "o": self.letters_blueprint[41],
            "p": self.letters_blueprint[42],
            "q": self.letters_blueprint[43],
            "r": self.letters_blueprint[44],
            "s": self.letters_blueprint[45],
            "t": self.letters_blueprint[46],
            "u": self.letters_blueprint[47],
            "v": self.letters_blueprint[48],
            "w": self.letters_blueprint[49],
            "x": self.letters_blueprint[50],
            "y": self.letters_blueprint[51],
            "z": self.letters_blueprint[52],
            ":": self.special_chars[0],
            ":": self.special_chars[0],
            "!": self.special_chars[1],
            "?": self.special_chars[2],
            "#": self.special_chars[3],
            "%": self.special_chars[4],
            "-": self.special_chars[5],
            "+": self.special_chars[6],
            "=": self.special_chars[7],
            "_": self.special_chars[8],
            "[": self.special_chars[9],
            "]": self.special_chars[10],
            "←": self.special_chars[11],
            "^": self.special_chars[12],
            "✓": self.special_chars[13],
            ".": self.special_chars[14],
            "'": self.special_chars[15],

        }

    def draw(self):
        for p in self.output_string:
            p.draw(self.surface)

    def gPrint(self, string, x= 0, y = 0):
        # Place this in the `draw()` function of
        # the main game code
        self.output_string.clear()
        x = x
        y = y
        letter_spacing = self.size * 7
        letter_width = self.size * 5

        parse_string = string
        loops = 0
        
        for c in parse_string:
            for row in self.font_dict[c]:
                for col in row:
                    if col == "1":
                        self.output_string.append(Pixel(x, y, self.color, self.size))
                    x += self.size
                y += self.size
                x -= letter_width
            loops += 1
            y = startY
            x += letter_spacing

        self.draw()
    
