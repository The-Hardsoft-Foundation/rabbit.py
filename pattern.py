# pattern.py

from transpile import Row, Transpilable
from timeblock import TimeBlock

from command import EndPattern


# a pattern is just a header and (optional) footer with time blocks in between
class Pattern(Transpilable):
    def __init__(self, pattern_key: str, compress: bool = False):
        # make sure the pattern key is a string
        assert type(pattern_key) == str, f"{pattern_key} is not a valid pattern key"

        # key to identify the current pattern
        self.key = pattern_key
        # list of time blocks
        self.blocks = []
        # whether or not to include extra spaces
        self.compress = compress

    def add_block(self, tb: TimeBlock):
        self.blocks.append(tb)

    def transpile(self) -> list[Row]:
        rows = []
        rows.append(Row(["newPattern", self.key]))

        # extra space
        if not self.compress:
            rows.append(Row())

        # add every time block to the pattern
        for tb in self.blocks[:-1]:
            rows.extend(tb.transpile())
            if not self.compress:
                rows.append(Row())
        rows.extend(self.blocks[-1].transpile())

        # extra space
        if not self.compress:
            rows.append(Row())

        rows.extend(EndPattern().transpile())
        return rows


'''
# need to figure out if patterns should do some factory builder stuff

star_pattern = Pattern("star_patt")
star_pattern.add("warningDelay;param1")

# other_pattern.clearPatternVars()
other_pattern.setPatternVar(param1 = 5)
other_pattern.add(star_pattern)

another_p = star_pattern.params("param1 = 5")
other_pattern.add(another_p)

or 

StarPattern = Pattern("star_patt")
other_pattern.add(StarPattern(param1 = 5))
'''
