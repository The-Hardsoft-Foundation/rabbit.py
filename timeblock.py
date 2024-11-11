# timeblock.py

from command import Command, CommandExpr
from transpile import Row, Transpilable


# class TimeBlockType(Enum):
#     TIME = "time",
#     TIME_REPEATING = "hw_nest",
#     TIME_REPEATING_FIXED = "hw_outskirts",
#     TIME_REPEATING_MULT = "hw_lighthouse",


# Specify a time when the following lines happen
class Time(Command):
    def __init__(self, start: CommandExpr):
        if type(start) == int or type(start) == float:
            assert start >= 0.0, f"Time: arg[0] cannot be negative: got {start}"
        elif type(start) == str:
            pass
        else:
            raise AssertionError(f"Time: arg[0] must be either number or str: got {type(start)}")
        
        self.start = start

    def transpile(self) -> list[Row]:
        return [Row(["time", str(self.start)])]


# Sets the following lines to happen every X milliseconds, starting at Y milliseconds
class TimeRepeating(Command):
    def __init__(self, start: CommandExpr, freq: CommandExpr):
        if type(start) == int or type(start) == float:
            assert start >= 0.0, f"TimeRepeating: arg[0] cannot be negative: got {start}"
        elif type(start) == str:
            pass
        else:
            raise AssertionError(f"TimeRepeating: arg[0] must be either number or str: got {type(start)}")
        
        if type(freq) == int or type(freq) == float:
            assert freq >= 0.0, f"TimeRepeating: arg[1] cannot be negative: got {freq}"
        elif type(freq) == str:
            pass
        else:
            raise AssertionError(f"TimeRepeating: arg[1] must be either number or str: got {type(freq)}")
        
        self.start = start
        self.freq = freq

    def transpile(self) -> list[Row]:
        return [Row(["timeRepeating", str(self.start), str(self.freq)])]


# Sets the following lines to happen every X milliseconds, starting at Y milliseconds, and only does it Z times
class TimeRepeatingFixed(Command):
    def __init__(self, start: CommandExpr, freq: CommandExpr, amount: int):
        if type(start) == int or type(start) == float:
            assert start >= 0.0, f"TimeRepeatingFixed: arg[0] cannot be negative: got {start}"
        elif type(start) == str:
            pass
        else:
            raise AssertionError(f"TimeRepeatingFixed: arg[0] must be either number or str: got {type(start)}")
        
        if type(freq) == int or type(freq) == float:
            assert freq >= 0.0, f"TimeRepeatingFixed: arg[1] cannot be negative: got {freq}"
        elif type(freq) == str:
            pass
        else:
            raise AssertionError(f"TimeRepeatingFixed: arg[1] must be either number or str: got {type(freq)}")
        
        if type(amount) == int:
            assert amount >= 0, f"TimeRepeatingFixed: arg[2] cannot be negative: got {amount}"
        else:
            raise AssertionError(f"TimeRepeatingFixed: arg[2] must be int: got {type(amount)}")
        
        self.start = start
        self.freq = freq
        self.amount = amount

    def transpile(self) -> list[Row]:
        return [Row(["timeRepeatingFixed", str(self.start), str(self.freq), str(self.amount)])]


# Sets the following lines to happen every X milliseconds, starting at Y milliseconds, and only does it Z times
class TimeRepeatingMult(Command):
    def __init__(self, freq: CommandExpr, *starts: list[CommandExpr]):        
        if type(freq) == int or type(freq) == float:
            assert freq >= 0.0, f"TimeRepeatingMult: arg[0] cannot be negative: got {freq}"
        elif type(freq) == str:
            pass
        else:
            raise AssertionError(f"TimeRepeatingMult: arg[0] must be either number or str: got {type(freq)}")
        
        assert len(starts) >= 1 and len(starts) <= 3, f"TimeRepeatingMult: len(arg) must be at least 2: got {len(starts)}"

        for i in range(len(starts)):
            t = type(starts[i])
            assert (t == int or t == float or t == str), f"TimeRepeatingMult: arg[{i + 1}] must be either number or str: got {t}"
        
        self.freq = freq
        self.starts = starts

    def transpile(self) -> list[Row]:
        row = Row(["timeRepeatingMult", str(self.duration)])
        row.extend(self.starts)
        return [row]


# a sum type that represents all time commands
TimeCommand = Time | TimeRepeating | TimeRepeatingFixed | TimeRepeatingMult


# given that every pattern consists of blocks indicated by their time / repetition
# we can group patterns into time blocks, which each start with a time
class TimeBlock(Transpilable):
    def __init__(self, tc: TimeCommand):
        # make sure it is actually a time command
        assert isinstance(tc, TimeCommand), f"{tc} is not a valid time command"
        self.tc = tc
        # all other non-time commands
        self.commands = []

    def add(self, cmd: Command):
        # you are not able to add another time command to a block
        # just make a new command
        assert isinstance(cmd, Command) and not isinstance(cmd, TimeCommand)
        self.commands.append(cmd)

    def transpile(self) -> list[Row]:
        # always one tc, so all time blocks start with that
        rows = self.tc.transpile()

        for cmd in self.commands:
            rows.extend(cmd.transpile())

        return rows