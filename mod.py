# mod.py

import os

from hallway import Hallway
from pattern import Pattern
from encounter import Encounter
from enemy import Enemy
from animation import Animation


class Mod:
    def __init__(self, name: str, thumbnail: str):
        # name of the mod, doesn't do that much rn
        self.name = name
        # thumbnail image, should be a relative filepath
        self.thumbnail = thumbnail
        # unique list of patterns
        self.patterns = []
        self.animations = []
        self.enemies = []
        self.encounters = []

    # will change to add if there can be multiple hallways
    def set_hallway(self, hallway: Hallway):
        self.hallway = hallway

    # add a pattern to the mod
    def add_pattern(self, pattern: Pattern):
        # make sure the pattern has a unique key
        for p in self.patterns:
            if pattern.key == p.key:
                raise AssertionError(f"Pattern {pattern.key} already exists")
        
        # add that to the list of patterns
        self.patterns.append(pattern)

    # attempts to remove the pattern corresponding with the key, returns true if successful
    def remove_pattern(self, key: str) -> bool:
        for i in range(len(self.patterns)):
            if self.patterns[i].key == key:
                self.patterns.pop(i)
                return True
        return False
    
    def add_encounter(self, encounter: Encounter):
        # make sure the pattern has a unique key
        for p in self.patterns:
            if encounter.key == p.key:
                raise AssertionError(f"Pattern {encounter.key} already exists")
        
        # add that to the list of patterns
        self.encounters.append(encounter)

    def remove_encounter(self, key: str):
        for i in range(len(self.encounters)):
            if self.encounters[i].key == key:
                self.encounters.pop(i)
                return True
        return False

    def add_enemy(self, enemy: Enemy):
        # make sure the pattern has a unique key
        for p in self.patterns:
            if enemy.key == p.key:
                raise AssertionError(f"Pattern {enemy.key} already exists")
        
        # add that to the list of patterns
        self.enemies.append(enemy)

    def remove_enemy(self, key: str):
        for i in range(len(self.enemies)):
            if self.enemies[i].key == key:
                self.enemies.pop(i)
                return True
        return False

    def add_animation(self, anim: Animation):
        # make sure the pattern has a unique key
        for p in self.patterns:
            if anim.key == p.key:
                raise AssertionError(f"Pattern {anim.key} already exists")
        
        # add that to the list of patterns
        self.animations.append(anim)

    def remove_animation(self, key: str):
        for i in range(len(self.animations)):
            if self.animations[i].key == key:
                self.animations.pop(i)
                return True
        return False

    def save(self, folder: str, annotations: bool = True):
        # create the mod folder
        try:
            os.makedirs(f"{folder}/{self.name}")
        except:
            pass

        # create the hallways file
        with open(f"{folder}/{self.name}/{self.name}_Hallway.csv", "w") as hallway_file:
            # header
            hallway_file.write("lineType,key\n")

            rows = self.hallway.transpile()
            for row in rows:
                hallway_file.write(str(row))
                hallway_file.write("\n")

        # create the animation file
        with open(f"{folder}/{self.name}/{self.name}_Animation.csv", "w") as anim_file:
            # header
            anim_file.write("key,filepath,filepathLowQuality,spriteNumber,centerX,centerY,headOffsetX,headOffsetY,standing,forward,backward,hurt,death,attCharge0,attSmear0,attAttack0,attCharge1,attSmear1,attAttack1,attCharge2,attSmear2,attAttack2,attCharge3,attSmear3,attAttack3\n")

            for anim in self.animations:
                rows = anim.transpile()
                for row in rows:
                    anim_file.write(str(row))
                    anim_file.write("\n")
                    
        # create the encounters file
        with open(f"{folder}/{self.name}/{self.name}_Encounter.csv", "w") as enc_file:
            # header
            enc_file.write("lineType,enemyKey,enemyPosX,enemyPosY,health,pattNormalSingle,pattHardSingle,pattLunarSingle,pattNormal,pattHard,pattLunar\n")
            
            for encounter in self.encounters:
                rows = encounter.transpile()
                for row in rows:
                    enc_file.write(str(row))
                    enc_file.write("\n")

        # create the enemy file
        with open(f"{folder}/{self.name}/{self.name}_Enemy.csv", "w") as enemy_file:
            # header
            enemy_file.write("key,animationKey,animationKeyTransform,color,colorSaturated,radius,drawScale,focusScale,isSpawn,spawnDrawType\n")
            
            for enemy in self.enemies:
                rows = enemy.transpile()
                for row in rows:
                    enemy_file.write(str(row))
                    enemy_file.write("\n")

        # create the pattern file
        with open(f"{folder}/{self.name}/{self.name}_Pattern.csv", "w") as pattern_file:
            # patterns don't have headers
            for pattern in self.patterns:
                rows = pattern.transpile()
                for row in rows:
                    pattern_file.write(str(row))
                    pattern_file.write("\n")

        # create the title file
        with open(f"{folder}/{self.name}/{self.name}_Title.csv", "w") as title_file:
            # header
            title_file.write("key,level,English,Japanese,Chinese,Korean,Ukrainian\n")
            
            # hardcoded stuff for now
            title_file.write(f"en_glizzygoblin,0,Glizzy Goblin,Glizzy Goblin,Glizzy Goblin,Glizzy Goblin,Glizzy Goblin\n")

        # create the sheets file
        with open(f"{folder}/{self.name}/SheetList.csv", "w") as sheets_file:
            sheets_file.write("Sheet Type,filename\n")
            sheets_file.write(f"AnimationSheet,{self.name}_Animation\n")
            sheets_file.write(f"EnemySheet,{self.name}_Enemy\n")
            sheets_file.write(f"EncounterSheet,{self.name}_Encounter\n")
            sheets_file.write(f"HallwaySheet,{self.name}_Hallway\n")
            sheets_file.write(f"PatternSheet,{self.name}_Pattern\n")
            sheets_file.write(f"TitleSheet,{self.name}_Title\n")
