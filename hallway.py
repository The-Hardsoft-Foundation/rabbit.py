# hallway.py

from enum import Enum
from transpile import Row, Transpilable
from encounter import Encounter


# the hallway base to overwrite
class HallwayBase(Enum):
    KINGDOM_OUTSKIRTS = "hw_outskirts"
    SCHOLARS_NEST = "hw_nest"
    KINGS_ARSENAL = "hw_outskirts"
    RED_DARKHOUSE = "hw_lighthouse"
    CHURCHMOUSE_STREETS = "hw_streets"
    EMERALD_LAKESIDE = "hw_lakeside"
    PALE_KEEP = "hw_keep"
    MOONLIT_PINNACLE = "hw_pinnacle"


# the type of stage in a hallway
class HallwayType(Enum):
    BATTLE = "battle"
    BOSS_BATTLE = "bossbattle"
    FINAL_BATTLE = "finalbattle"
    LOOT = "loot"
    ENDING = "ending"


# defines the pathway the character takes through a level
class Hallway(Transpilable):
    def __init__(self, hallway_base: HallwayBase):
        self.base = hallway_base
        # list[tuple[HallwayType, list[Encounter]]]
        self.elements = []

    def add_battle(self, *encounters: list[Encounter]):
        self.elements.append((HallwayType.BATTLE, encounters))
    
    def add_bossbattle(self, *encounters: list[Encounter]):
        self.elements.append((HallwayType.BOSS_BATTLE, encounters))

    def add_finalbattle(self, *encounters: list[Encounter]):
        self.elements.append((HallwayType.FINAL_BATTLE, encounters))
    
    def add_loot(self):
        self.elements.append((HallwayType.LOOT, []))

    def add_ending(self):
        self.elements.append((HallwayType.ENDING, []))
    
    def transpile(self) -> list[Row]:
        rows = []
        rows.append(Row(["hallway", self.base.value]))
        
        for hw_type, encs in self.elements:
            if len(encs) > 0:
                rows.append(Row([hw_type.value, ";".join(enc.key for enc in encs)]))
            else:
                rows.append(Row([hw_type.value]))

        return rows