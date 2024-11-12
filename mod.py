# mod.py

import os

from hallway import Hallway
from pattern import Pattern
from encounter import Encounter
from enemy import Enemy
from animation import Animation


class Mod:
    def __init__(self, name: str, thumbnail: str):
        # name of the mod, this will be prefixed to all keys
        self.name = name
        # thumbnail image, should be a relative filepath
        self.thumbnail = thumbnail
        
        # self.hallways = {}
        self.hallway = None
        self.patterns = {}
        self.animations = {}
        self.enemies = {}
        self.encounters = {}

    # # TODO: check if there can be multiple hallways, since hallways dont have keys?
    # def create_hallway(self, name: str, *args, **kwargs) -> Hallway:
    #     hw_key = f"{self.name}_hallway_{name}"
        
    #     if name in self.hallways:
    #         raise ValueError(f"Mod {self.name} already contains hallway {name}")
    #     # temporary assert, still unsure if mods can have more than one hallway, the probably can?
    #     assert len(self.hallways) == 0, f"Mod {self.name} already contains a hallway" 

    #     hw = Hallway(*args, **kwargs)
    #     self.hallways[name] = hw

    #     return hw

    def create_hallway(self, *args, **kwargs) -> Hallway:
        if self.hallway != None:
            raise ValueError(f"Mod {self.name} already contains a hallway")

        hw = Hallway(*args, **kwargs)
        self.hallway = hw

        return hw 

    def get_hallway(self, name: str) -> Hallway:
        return self.hallways[name]

    def remove_hallway(self, name: str) -> Hallway:
        return self.hallways.pop(name)
    


    def create_animation(self, name: str, *args, **kwargs) -> Animation:
        anim_key = f"{self.name}_animation_{name}"
        
        if name in self.animations:
            raise ValueError(f"Mod {self.name} already contains animation {name}")

        anim = Animation(anim_key, *args, **kwargs)
        self.animations[name] = anim

        return anim

    def get_animation(self, name: str) -> Animation:
        return self.animations[name]

    def remove_animation(self, name: str) -> Animation:
        return self.animations.pop(name)
    


    def create_enemy(self, name: str, *args, **kwargs) -> Enemy:
        en_key = f"{self.name}_enemy_{name}"
        
        if name in self.enemies:
            raise ValueError(f"Mod {self.name} already contains enemy {name}")

        en = Enemy(en_key, *args, **kwargs)
        self.enemies[name] = en

        return en

    def get_enemy(self, name: str) -> Enemy:
        return self.enemies[name]

    def remove_enemy(self, name: str) -> Enemy:
        return self.enemies.pop(name)
    


    def create_encounter(self, name: str, *args, **kwargs) -> Encounter:
        enc_key = f"{self.name}_encounter_{name}"
        
        if name in self.encounters:
            raise ValueError(f"Mod {self.name} already contains encounter {name}")

        enc = Encounter(enc_key, *args, **kwargs)
        self.encounters[name] = enc

        return enc

    def get_encounter(self, name: str) -> Encounter:
        return self.encounters[name]

    def remove_encounter(self, name: str) -> Encounter:
        return self.encounters.pop(name)
    


    def create_pattern(self, name: str, *args, **kwargs) -> Pattern:
        patt_key = f"{self.name}_pattern_{name}"
        
        if name in self.patterns:
            raise ValueError(f"Mod {self.name} already contains pattern {name}")

        patt = Pattern(patt_key, *args, **kwargs)
        self.patterns[name] = patt

        return patt

    def get_pattern(self, name: str) -> Pattern:
        return self.patterns[name]

    def remove_pattern(self, name: str) -> Pattern:
        return self.patterns.pop(name)


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

            for anim in self.animations.values():
                rows = anim.transpile()
                for row in rows:
                    anim_file.write(str(row))
                    anim_file.write("\n")
                    
        # create the encounters file
        with open(f"{folder}/{self.name}/{self.name}_Encounter.csv", "w") as enc_file:
            # header
            enc_file.write("lineType,enemyKey,enemyPosX,enemyPosY,health,pattNormalSingle,pattHardSingle,pattLunarSingle,pattNormal,pattHard,pattLunar\n")
            
            for encounter in self.encounters.values():
                rows = encounter.transpile()
                for row in rows:
                    enc_file.write(str(row))
                    enc_file.write("\n")

        # create the enemy file
        with open(f"{folder}/{self.name}/{self.name}_Enemy.csv", "w") as enemy_file:
            # header
            enemy_file.write("key,animationKey,animationKeyTransform,color,colorSaturated,radius,drawScale,focusScale,isSpawn,spawnDrawType\n")
            
            for enemy in self.enemies.values():
                rows = enemy.transpile()
                for row in rows:
                    enemy_file.write(str(row))
                    enemy_file.write("\n")

        # create the pattern file
        with open(f"{folder}/{self.name}/{self.name}_Pattern.csv", "w") as pattern_file:
            # patterns don't have headers
            for pattern in self.patterns.values():
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
