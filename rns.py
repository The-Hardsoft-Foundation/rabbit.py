# rns.py

from mod import Mod
from pattern import Pattern
import hallway
from hallway import Hallway, HallwayBase
from animation import Animation
from enemy import Enemy
from encounter import Encounter
from command import *
import timeblock
from timeblock import TimeBlock


# maybe have a mod.create_X thing to create the new thing
# then have transpile take in the mod?
# and maybe commands or stuff take in the object if they have to link to them?

# instead of that, extend mod then build that way
# everything that needs to take in a key to something should take in the object instead (except for built ins)
# have the mod handle creating and setting them, so something like self.get_pattern("super_cleave") which can also validate for stuff









# create the mod
m = Mod("TestMod", "thumbnail.png")

anim = m.create_animation("testenemy", "Assets/mod_dreadwyrm.png", "Assets/mod_dreadwyrm_lq.png")

# create the enemies
glizzy = m.create_enemy("glizzygoblin", anim, anim, (0, 255, 0), (255, 0, 0), 300, 0.45, 1, False, False)

# glizzy goblin stuff
gg = m.create_pattern("mbp_glizzygoblin0")

init_values = TimeBlock(timeblock.Time(0))
init_values.add(Zoom(1))
init_values.add(SetResourceMult(6, 1.5))
init_values.add(Move("bfCenterX+700", "bfCenterY", 1400))
gg.add_block(init_values)

patt_repeat = TimeBlock(timeblock.TimeRepeating(5000, 6000))
patt_repeat.add(AddPatt("TestMod_pattern_mbp_glizzygoblin_f0"))
gg.add_block(patt_repeat)


# glizzy goblin f stuff
gg_f = m.create_pattern("mbp_glizzygoblin_f0")

center_block = TimeBlock(timeblock.Time(0))
center_block.add(Move("bfCenterX", "bfCenterY", 500))
gg_f.add_block(center_block)

cleave_block = TimeBlock(timeblock.Time(500))
cleave_block.add(OrderBinFourGroups())
cleave_block.add(PattVarReset())
cleave_block.add(PattVars(
    "warningDelay;0", "spawnDelay;5500", "warnMsg;2", 
    "orderBin_0;orderBin0", "rot_0;0", "orderBin_1;orderBin1", "rot_1;90", 
    "orderBin_2;orderBin2", "rot_2;180", "orderBin_3;orderBin3", "rot_3;270"
))
cleave_block.add(AddPatt("bp_cleave"))
gg_f.add_block(cleave_block)

spin_block = TimeBlock(timeblock.Time(1000))
spin_block.add(PattVarReset())
spin_block.add(PattVars(
    "warningDelay;0", "spawnDelay;4000", "eraseDelay;5500", 
    "angle;45*randomSign", "num;4", "width;500",
))
spin_block.add(AddPatt("bp_ray_spinfast"))
gg_f.add_block(spin_block)


# create the encounter
glizzy_enc = m.create_encounter("glizzygoblin", glizzy, (400, 0), 12000, tuple(gg for _ in range(6)))


# create the hallway
hallway = m.create_hallway(HallwayBase.KINGDOM_OUTSKIRTS)
hallway.add_bossbattle(glizzy_enc)

m.save("./target")