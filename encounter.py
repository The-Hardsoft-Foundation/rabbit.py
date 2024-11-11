# encounter.py

from transpile import Transpilable, Row
from enemy import Enemy
from pattern import Pattern


# (NormalSingle, HardSingle, LunarSingle, NormalMult, HardMult, LunarMult)
EnemyPatterns = tuple[Pattern, Pattern, Pattern, Pattern, Pattern, Pattern]

# an encounter, which consists of an encounter_key and an enemy
# TODO: have some way to not have to preface keys with "enc"
# not sure if encounters can have multiple enemies??
class Encounter(Transpilable):
    def __init__(self, key: str, enemy: Enemy, pos: tuple[float, float], health: int, patterns: EnemyPatterns):
        assert type(key) == str, f"Encounter key must be str: {key}"
        
        self.key = key
        self.enemy = enemy
        self.pos = pos
        self.health = health
        self.patterns = patterns

    def transpile(self) -> list[Row]:
        rows = [Row(["encounter", self.key])]

        enemy_row = Row(["enemy", self.enemy.key, str(self.pos[0]), str(self.pos[1]), str(self.health)])
        enemy_row.extend(p.key for p in self.patterns)

        rows.append(enemy_row)
        return rows