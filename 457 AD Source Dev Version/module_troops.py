import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *

#from compiler import *
####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

# Some constant and function declarations to be used below...
# wp_one_handed () | wp_two_handed () | wp_polearm () | wp_archery () | wp_crossbow () | wp_throwing ()
def wp(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
#  n |= wp_archery(x + random.randrange(r))
#  n |= wp_crossbow(x + random.randrange(r))
#  n |= wp_throwing(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wp_melee(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  return n

def wp_warrior(x):
  n = 0
  r = 10 + int(x / 10)
  n |= wp_one_handed(x + 10)
  n |= wp_two_handed(x + 10)
  n |= wp_polearm(x + 10)
  n |= wp_throwing(x + 20)
  return n

def wp_guard(x):
  n = 0
  r = 10 + int(x / 10)
  n |= wp_one_handed(x + 10)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 20)
  return n

#Skills
knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_3|knows_prisoner_management_1|knows_leadership_1
knows_common_multiplayer = knows_trade_10|knows_inventory_management_10|knows_prisoner_management_10|knows_leadership_10|knows_spotting_10|knows_pathfinding_10|knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10

#average wp for tiers - increases by 30 each tier, slight deviation by +/- 5 - 10 for cultural specializations
#tier 1: 100
#tier 2: 130
#tier 3: 160
#tier 4: 190
#tier 5: 220
#tier 6: 250 - rarely used

def_attrib = str_8 | agi_8 | int_6 | cha_7
def_attrib_multiplayer = int_30 | cha_30

#assuming lvl 1 with base of = 4|4|4|4
#total attribute points = 17 + 16 + level
#+5 lvl for each group
def_attrib_lvl_9 =  str_12|agi_12|int_8|cha_10 
def_attrib_lvl_13 = str_15|agi_13|int_8|cha_10
def_attrib_lvl_18 = str_18|agi_15|int_8|cha_10 
def_attrib_lvl_20 = str_20|agi_15|int_8|cha_10 
def_attrib_lvl_23 = str_22|agi_16|int_8|cha_10 
def_attrib_lvl_25 = str_22|agi_18|int_8|cha_10 
def_attrib_lvl_28 = str_25|agi_18|int_8|cha_10 
def_attrib_lvl_30 = str_27|agi_18|int_8|cha_10 
def_attrib_lvl_32 = str_29|agi_18|int_8|cha_10 
def_attrib_lvl_35 = str_30|agi_20|int_8|cha_10 
def_attrib_skirmisher = str_10|agi_18|int_8|cha_10 #roughly lvl 13

#Total Skill Points = 13 + Troop level + INT
#cav = greater riding, powerstrike, less, athletics, ironflesh, shield
#inf = less riding, greater athletics, ironflesh, shield
#1/3 of respective attribute
#10 + 9 + 8 = 27 points
knows_lvl_9 = knows_athletics_4|knows_riding_4|knows_ironflesh_4|knows_power_throw_3|knows_power_draw_2|knows_weapon_master_3|knows_inventory_management_3|knows_power_strike_2|knows_shield_2 #21 points, with 6 to spread between shield/powerstrike
#10 + 13 + 8 = 31 points
knows_lvl_13_inf = knows_athletics_4|knows_riding_2|knows_ironflesh_5|knows_power_throw_5|knows_power_draw_2|knows_weapon_master_4|knows_inventory_management_3 #26 points, with 6 points to spread between shield/powerstrike
knows_lvl_13_cav = knows_athletics_2|knows_riding_4|knows_ironflesh_4|knows_power_throw_4|knows_power_draw_2|knows_weapon_master_4|knows_inventory_management_3|knows_horse_archery_3 #28 points, with 6 extra points
#10 + 18 + 8 = 36 points
knows_lvl_18_inf = knows_athletics_5|knows_riding_2|knows_ironflesh_6|knows_power_throw_5|knows_power_draw_2|knows_weapon_master_5|knows_inventory_management_3 #28 points, with 8 points to spread between shield/powerstrike
knows_lvl_18_cav = knows_athletics_2|knows_riding_5|knows_ironflesh_5|knows_power_throw_5|knows_power_draw_2|knows_weapon_master_5|knows_inventory_management_3|knows_horse_archery_3 #32 points, with 6 extra points
#10 + 23 + 8 = 41 points
knows_lvl_23_inf = knows_athletics_5|knows_riding_2|knows_ironflesh_7|knows_power_throw_6|knows_power_draw_2|knows_weapon_master_5|knows_inventory_management_4 #31 points, with 10 points to spread between shield/powerstrike
knows_lvl_23_cav = knows_athletics_2|knows_riding_5|knows_ironflesh_7|knows_power_throw_6|knows_power_draw_3|knows_weapon_master_5|knows_inventory_management_4 #32 points, with 9 extra points
#10 + 28 + 8 = 46 points
knows_lvl_28_inf = knows_athletics_6|knows_riding_2|knows_ironflesh_8|knows_power_throw_6|knows_power_draw_2|knows_weapon_master_6|knows_inventory_management_4 #34 points, with 12 points to spread between shield/powerstrike
knows_lvl_28_cav = knows_athletics_2|knows_riding_6|knows_ironflesh_8|knows_power_throw_6|knows_power_draw_4|knows_weapon_master_6|knows_inventory_management_4 #36 points, with 10 extra points
#10 + 30 + 8 = 48 points
knows_lvl_30_inf = knows_athletics_6|knows_riding_2|knows_ironflesh_9|knows_power_throw_7|knows_power_draw_2|knows_weapon_master_6|knows_inventory_management_4 #36 points, with 12 points to spread between shield/powerstrike
knows_lvl_30_cav = knows_athletics_3|knows_riding_6|knows_ironflesh_9|knows_power_throw_6|knows_power_draw_4|knows_weapon_master_6|knows_inventory_management_4 #38 points, with 10 extra points

knows_skirmisher = knows_athletics_5|knows_riding_2|knows_ironflesh_3|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_4|knows_inventory_management_3|knows_shield_2|knows_power_strike_2 #lvl 13 / 31 points
knows_archer = knows_athletics_5|knows_riding_2|knows_ironflesh_4|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_5|knows_inventory_management_4|knows_shield_2|knows_power_strike_2 #36 points
knows_horse_archer = knows_athletics_3|knows_riding_5|knows_ironflesh_3|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_5|knows_inventory_management_3|knows_horse_archery_5 #36 points
knows_cataphract = knows_athletics_2|knows_riding_6|knows_ironflesh_8|knows_power_throw_4|knows_power_draw_6|knows_weapon_master_6|knows_inventory_management_4|knows_power_strike_6|knows_horse_archery_4 #lvl 28 - 46 pts
knows_berserker = knows_ironflesh_10|knows_power_strike_10|knows_power_throw_8|knows_athletics_10|knows_weapon_master_6|knows_inventory_management_4

knows_lord_1 = knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_tactics_4|knows_prisoner_management_4|knows_leadership_7

knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_1|knows_power_throw_1|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_shield_1|knows_inventory_management_2
knows_merchant_npc = knows_riding_2|knows_trade_3|knows_inventory_management_3 #knows persuasion
knows_tracker_npc = knows_weapon_master_1|knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2

lord_attrib = str_20|agi_20|int_20|cha_20|level(38)

knight_attrib_1 = str_24|agi_16|int_10|cha_16|level(22)
knight_attrib_2 = str_26|agi_18|int_14|cha_18|level(26)
knight_attrib_3 = str_28|agi_20|int_16|cha_20|level(30)
knight_attrib_4 = str_29|agi_22|int_19|cha_22|level(35)
knight_attrib_5 = str_30|agi_24|int_22|cha_25|level(41)
knight_skills_1 = knows_riding_3|knows_ironflesh_4|knows_power_strike_4|knows_athletics_1|knows_tactics_3|knows_prisoner_management_2|knows_leadership_4
knight_skills_2 = knows_riding_4|knows_ironflesh_5|knows_power_strike_5|knows_athletics_2|knows_tactics_4|knows_prisoner_management_3|knows_leadership_5
knight_skills_3 = knows_riding_5|knows_ironflesh_6|knows_power_strike_6|knows_athletics_3|knows_tactics_5|knows_prisoner_management_4|knows_leadership_6
knight_skills_4 = knows_riding_6|knows_ironflesh_7|knows_power_strike_7|knows_athletics_4|knows_tactics_6|knows_prisoner_management_5|knows_leadership_7
knight_skills_5 = knows_riding_7|knows_ironflesh_8|knows_power_strike_8|knows_athletics_5|knows_tactics_7|knows_prisoner_management_6|knows_leadership_9
knight_skills_6 = knows_riding_8|knows_ironflesh_9|knows_power_strike_9|knows_athletics_6|knows_tactics_8|knows_prisoner_management_7|knows_leadership_10

#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0

#updated faces
roman_face_1 = 0x000000002d00000144db6db6db6db6db00000000001db6da0000000000000000
roman_face_2 = 0x0000000b3f00910744db75b6ab6db2db00000000001db6e20000000000000000

germanic_face_1 = 0x000000000000000136db6db6db6db6db00000000001db6db0000000000000000
germanic_face_2 = 0x000000069700650b44db6db6db6db6d200000000001db6e20000000000000000

briton_face_1 = 0x000000001300000136db6db69b6db6d200000000001db6d30000000000000000
briton_face_2 = 0x000000071300910736db6db69b6db6d200000000001db6d30000000000000000

caucaus_face_1 = 0x000000003900200136db6db69b6db6d200000000001db6d30000000000000000
caucaus_face_2 = 0x000000083900914636db6db69b6db6d200000000001db6d30000000000000000

persian_face_1 = 0x000000000000f00136db6db8e36db6dc00000000001db6d30000000000000000
persian_face_2 = 0x000000093f01134644db6db8ab8db6d400000000001db6db0000000000000000

arab_face_1 = 0x000000000000f00136db6db8e36db6dc00000000001db6d30000000000000000
arab_face_2 = 0x0000000dbf01114844db6db8ab8db6d500000000001db6db0000000000000000

hunnic_face_1 = 0x000000002100c001355d6d48e34da4d300000000001db6db0000000000000000
hunnic_face_2 = 0x0000000a3e00e40d355d6d48e34da4d300000000001db6ea0000000000000000

mauri_face_1 = 0x000000002a01200136db6db6db6db6db00000000001db6db0000000000000000
mauri_face_2 = 0x0000000aea01414644db96b9546dbb6400000000001db6a20000000000000000

nubian_face_1 = 0x000000003f016001509b7268a36db4db00000000001d36e30000000000000000
nubian_face_2 = 0x0000000d7f016006509b7268a36db6dc00000000001d36e30000000000000000

celtic_face_1 = 0x000000000e00000132da71b69b6db4db00000000001d36d30000000000000000
celtic_face_2 = 0x0000000c9b006286491a70a8d34db2d300000000001db6e40000000000000000

steppe_face_1 = 0x0000000021007001529585c8ea71b4d200000000001d36eb0000000000000000
steppe_face_2 = 0x0000000bff0083cd529585c8eb71b8d200000000001d36eb0000000000000000

coptic_face_1 = 0x000000002300f00136db75b69b6db2db00000000001d36da0000000000000000
coptic_face_2 = 0x0000000b7f011007331b75b69b6db6da00000000001d36ec0000000000000000

sarmatian_face_1 = 0x000000000000000132db6d38a36db2da00000000001db6d30000000000000000
sarmatian_face_2 = 0x0000000b9800640b44db6db8db6db4db00000000001db6e40000000000000000

man_face_1 = 0x000000000000000136db6db6db6db4db00000000001d36d20000000000000000
man_face_2 = 0x0000000aff00910142db6db6a36db4da00000000001d36e30000000000000000

bandit_face_1 = 0x000000001700000144db75d89b4db2da00000000001db6ea0000000000000000
bandit_face_2 = 0x0000000a1700a28634db8dc69b4dbaed00000000001e36ec0000000000000000


swadian_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
swadian_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
swadian_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
swadian_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
swadian_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

swadian_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

vaegir_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
vaegir_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
vaegir_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
vaegir_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
vaegir_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

vaegir_face_younger_2 = 0x000000003f00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_young_2   = 0x00000003bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_middle_2  = 0x00000007bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_old_2     = 0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_older_2   = 0x0000000ff100230c4deeffffffffffff00000000001efff90000000000000000

khergit_face_younger_1 = 0x0000000009003109207000000000000000000000001c80470000000000000000
khergit_face_young_1   = 0x00000003c9003109207000000000000000000000001c80470000000000000000
khergit_face_middle_1  = 0x00000007c9003109207000000000000000000000001c80470000000000000000
khergit_face_old_1     = 0x0000000b89003109207000000000000000000000001c80470000000000000000
khergit_face_older_1   = 0x0000000fc9003109207000000000000000000000001c80470000000000000000

khergit_face_younger_2 = 0x000000003f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_young_2   = 0x00000003bf0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_middle_2  = 0x000000077f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_old_2     = 0x0000000b3f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_older_2   = 0x0000000fff0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000

nord_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
nord_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
nord_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
nord_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
nord_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

nord_face_younger_2 = 0x00000000310023084deeffffffffffff00000000001efff90000000000000000
nord_face_young_2   = 0x00000003b10023084deeffffffffffff00000000001efff90000000000000000
nord_face_middle_2  = 0x00000008310023084deeffffffffffff00000000001efff90000000000000000
nord_face_old_2     = 0x0000000c710023084deeffffffffffff00000000001efff90000000000000000
nord_face_older_2   = 0x0000000ff10023084deeffffffffffff00000000001efff90000000000000000

rhodok_face_younger_1 = 0x0000000009002003140000000000000000000000001c80400000000000000000
rhodok_face_young_1   = 0x0000000449002003140000000000000000000000001c80400000000000000000
rhodok_face_middle_1  = 0x0000000849002003140000000000000000000000001c80400000000000000000
rhodok_face_old_1     = 0x0000000cc9002003140000000000000000000000001c80400000000000000000
rhodok_face_older_1   = 0x0000000fc9002003140000000000000000000000001c80400000000000000000

rhodok_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
man_face_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
man_face_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
man_face_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

man_face_younger_2 = 0x000000003f0052064deeffffffffffff00000000001efff90000000000000000
man_face_young_2   = 0x00000003bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_middle_2  = 0x00000007bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_old_2     = 0x0000000bff0052064deeffffffffffff00000000001efff90000000000000000
man_face_2   = 0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000

imperial_face_younger_1 = 0x000000001d00200246db95b6a38da6db00000000001db6e30000000000000000
imperial_face_young_1   = 0x000000031d00200246db95b6a38da6db00000000001db6e30000000000000000
imperial_face_middle_1  = 0x000000061d00200246db95b6a38da6db00000000001db6e30000000000000000
imperial_face_old_1     = 0x00000009dd00200246db95b6a38da6db00000000001db6e30000000000000000
imperial_face_older_1   = 0x0000000c1d00200246db95b6a38da6db00000000001db6e30000000000000000

imperial_face_younger_2 = 0x000000002e01100246db95b6a38da6db00000000001db6e30000000000000000
imperial_face_young_2   = 0x00000002ee01100246db95b6a38da6db00000000001db6e30000000000000000
imperial_face_middle_2  = 0x000000052e01100246db95b6a38da6db00000000001db6e30000000000000000
imperial_face_old_2     = 0x000000086e01100246db95b6a38da6db00000000001db6e30000000000000000
imperial_face_older_2   = 0x0000000bee01100246db95b6a38da6db00000000001db6e30000000000000000

sarranid_face_younger_1 = 0x000000000000b48536db6db6db6db6db00000000001db6db0000000000000000
sarranid_face_young_1   = 0x000000000000c0c636db6db6db6db6db00000000001db6db0000000000000000
sarranid_face_middle_1  = 0x000000083a00a18636db6db6db6db6db00000000001db6db0000000000000000
sarranid_face_old_1     = 0x0000000cba00a28636db6db6db6db6db00000000001db6db0000000000000000
sarranid_face_older_1   = 0x0000000f2d00a44636db6db6db6db6db00000000001db6db0000000000000000

sarranid_face_younger_2 = 0x000000002d00b00636db6db6db6db6db00000000001db6db0000000000000000
sarranid_face_young_2 = 0x000000026f00b18436db6db6db6db6db00000000001db6db0000000000000000
sarranid_face_middle_2 = 0x000000082f00c14336db6db6db6db6db00000000001db6db0000000000000000
sarranid_face_old_2 = 0x0000000c7200b20636db6db6db6db6db00000000001db6db0000000000000000
sarranid_face_older_2 = 0x0000000e3200c0c636db6db6db6db6db00000000001db6db0000000000000000

merchant_face_1    = man_face_1
merchant_face_2    = man_face_2

woman_face_1    = 0x0000000009000001149b6d14c949a6d400000000001cd3130000000000000000
woman_face_2    = 0x00000007bf00500d36da7117638da6d400000000001e335b0000000000000000

roman_woman_face_1 = 0x0000000020000001149b6d14c949a6d400000000001cd3130000000000000000
roman_woman_face_2 = 0x00000007bf00500d36da7117638da6d400000000001e335b0000000000000000

african_woman_face_1 = 0x000000003f00800126db6db6db6db6db00000000001c230b0000000000000000
african_woman_face_2 = 0x0000000fff00800124ab76a71b6db6db00000000001c230b0000000000000000

swadian_woman_face_1 = 0x0000000009000001149b6d14c949a6d400000000001cd3130000000000000000
swadian_woman_face_2 = 0x00000007bf00500d36da7117638da6d400000000001e335b0000000000000000

khergit_woman_face_1 = 0x000000003f00600113dd6e27fc49369200000000001ca34a0000000000000000
khergit_woman_face_2 = 0x0000000a3f00700e13d54d27fc49369200000000001eb2e20000000000000000

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

man_face_1 = 0x000000003900118436db6db6db6db6db00000000001db6e30000000000000000
man_face_2 = 0x00000007da00200436db6db6db6db6db00000000001db6e30000000000000000

vaegir_face1  = vaegir_face_young_1
vaegir_face2  = vaegir_face_older_2

bandit_face1  = bandit_face_1
bandit_face2  = bandit_face_2

undead_face1  = 0x00000000002000000000000000000000
undead_face2  = 0x000000000020010000001fffffffffff

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield
#used for most non - roman/sassanid infantry, guarantees the most basic things a commoner would have in battle
tf_guarantee_basic = tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_polearm

roman_tunics_civ = [itm_roman_shirt_1,itm_roman_shirt_2,itm_roman_shirt_3,itm_roman_shirt_4,itm_roman_shirt_5,itm_roman_shirt_6,itm_roman_shirt_7,itm_roman_shirt_8,itm_roman_shirt_9,itm_roman_shirt_9,itm_roman_shirt_10,itm_roman_shirt_11,itm_roman_shirt_12,itm_roman_shirt_13]

roman_tunics = [itm_roman_shirt_3,itm_roman_shirt_4,itm_roman_shirt_5,itm_roman_shirt_8,itm_roman_shirt_10,itm_roman_shirt_10,itm_roman_shirt_2,itm_roman_shirt_14,itm_roman_shirt_3,itm_roman_shirt_8]

roman_tunics_rich = [itm_roman_shirt_3,itm_roman_shirt_7,itm_roman_shirt_2,itm_roman_shirt_9,itm_roman_shirt_14,itm_roman_shirt_3]

tunics_romans_military = [itm_roman_military_tunic_1,itm_roman_military_tunic_2,itm_roman_military_tunic_3,itm_roman_military_tunic_9,itm_roman_military_tunic_10] #red battle tunics

tunics_romans_low = [itm_roman_shirt_1,itm_roman_shirt_4,itm_roman_shirt_6,itm_roman_shirt_8] #less decorated tunics

tunics_romans_officer = [itm_roman_shirt_3,itm_roman_shirt_5,itm_roman_shirt_7,itm_roman_shirt_12,itm_roman_shirt_2,itm_roman_shirt_9,itm_roman_shirt_14,itm_roman_shirt_3] #for officer troops

tunics_foederati = [itm_roman_military_tunic_4,itm_roman_military_tunic_5,itm_roman_military_tunic_6]

tunics_coptic = [itm_roman_shirt_4,itm_roman_shirt_6,itm_roman_shirt_8,itm_roman_shirt_9,itm_roman_shirt_13,itm_roman_shirt_15,itm_roman_shirt_16,itm_roman_military_tunic_1,itm_roman_military_tunic_6,itm_roman_military_tunic_7,itm_roman_military_tunic_8,itm_roman_military_tunic_10]

tunics_roman_civilian = [itm_roman_peasant_tunic_1,itm_roman_peasant_tunic_2,itm_roman_peasant_tunic_3,itm_roman_peasant_tunic_4,itm_roman_peasant_tunic_5,itm_roman_peasant_tunic_6,itm_roman_peasant_tunic_7,itm_roman_peasant_tunic_9]

hoods_roman_1 = [itm_roman_civilian_hood_open_1,itm_roman_civilian_hood_open_2,itm_roman_civilian_hood_open_3] #hood lowered
hoods_roman_2 = [itm_roman_civilian_hood_1,itm_roman_civilian_hood_2,itm_roman_civilian_hood_3] 
hoods_roman_3 = [itm_roman_civilian_hood_closed_1,itm_roman_civilian_hood_closed_2,itm_roman_civilian_hood_closed_3] #hood with mask

#new tunic groups
#culture_1
tunics_goths = [itm_generic_tunic_7,itm_generic_tunic_15,itm_linen_shirt_1,itm_linen_shirt_10,itm_generic_tunic_3,itm_generic_tunic_5,itm_generic_tunic_8,itm_generic_tunic_12,itm_generic_tunic_13,itm_generic_tunic_14,itm_linen_shirt_4,itm_linen_shirt_5,itm_linen_tunic,itm_linen_shirt]
#culture_2
tunics_eastern_germanic = [itm_linen_shirt,itm_linen_shirt_9,itm_linen_shirt_10,itm_linen_shirt_2,itm_linen_shirt_1,itm_linen_shirt_3,itm_generic_tunic_2,itm_generic_tunic_4,itm_generic_tunic_6,itm_generic_tunic_8,itm_generic_tunic_7,itm_generic_tunic_9,itm_generic_tunic_10,itm_generic_tunic_11,itm_generic_tunic_13,itm_generic_tunic_14]
#culture_4 
tunics_northern_germanic = [itm_shirt,itm_generic_tunic_14,itm_generic_tunic_1,itm_linen_shirt_4,itm_linen_shirt_6,itm_linen_shirt_8,itm_linen_shirt_10,itm_linen_shirt_1,itm_linen_shirt_12]
#culture_7 or 9
tunics_western_germanic = [itm_shirt,itm_linen_tunic,itm_linen_shirt,itm_generic_tunic_6,itm_generic_tunic_13,itm_generic_tunic_14,itm_generic_tunic_15,itm_linen_shirt_11,itm_linen_shirt_10,itm_linen_shirt_1,itm_linen_shirt_2,itm_linen_shirt_3,itm_linen_shirt_13,itm_linen_shirt_14]
#culture_8
tunics_caucasian = [itm_shirt,itm_linen_tunic,itm_linen_shirt,itm_linen_shirt_10,itm_skirmisher_tunic_1,itm_skirmisher_tunic_4,itm_generic_tunic_11,itm_kaftan_tunic_2]

#rest are reused from previous version
#mid tier troops
#blues, greens, reds, mix of poorer tunics at end
tunics_britons = [itm_roman_shirt_4,itm_linen_shirt_2,itm_linen_shirt_14,itm_linen_shirt_16,itm_falkirk_tunic_1,itm_falkirk_tunic_4,itm_falkirk_tunic_5,itm_shirt,itm_linen_shirt,itm_linen_shirt_10,itm_linen_shirt_13,itm_roman_military_tunic_1,itm_roman_military_tunic_7] #several poorer tunics at the end
#celtic + pictish attire
tunics_pictish = [itm_long_shirt_2,itm_long_shirt_4,itm_long_shirt_5,itm_linen_shirt_14,itm_long_shirt_3,itm_long_shirt_7,itm_falkirk_tunic_1,itm_falkirk_tunic_2,itm_falkirk_tunic_3,itm_falkirk_tunic_4,itm_falkirk_tunic_5,itm_linen_shirt_16,itm_linen_shirt_18]
#used by tier 3
pictish_naked = [itm_pants_5,itm_pants_10,itm_pants_11,itm_pants_13,itm_pict_body_1m,itm_pict_body_2m,itm_pict_body_3m,itm_pict_body_4m]
#sassanid tunics
tunics_sassanid = [itm_rich_tunic_1,itm_rich_tunic_2,itm_rich_tunic_3,itm_rich_tunic_4,itm_rich_tunic_5,itm_kaftan_tunic_1,itm_kaftan_tunic_2,itm_kaftan_tunic_3,itm_kaftan_tunic_4,itm_kaftan_tunic_5,itm_kaftan_tunic_6,itm_kaftan_tunic_8,itm_kaftan_tunic_9,itm_kaftan_tunic_10]
#for skirmishers
tunics_sassanid_skirmisher = [itm_kaftan_sheepskin_1,itm_kaftan_sheepskin_2,itm_kaftan_sheepskin_3,itm_kaftan_sheepskin_4,itm_kaftan_sheepskin_5]
#for nobles
tunics_sassanid_rich = [itm_rich_tunic_1,itm_rich_tunic_2,itm_rich_tunic_3,itm_rich_tunic_4,itm_rich_tunic_5,itm_sassanid_rich_tunic_1,itm_sassanid_rich_tunic_2,itm_sassanid_rich_tunic_3,itm_sassanid_rich_tunic_4]

tunics_generic = [itm_linen_shirt,itm_linen_tunic,itm_shirt,itm_linen_shirt_1,itm_linen_shirt_2,itm_linen_shirt_3,itm_linen_shirt_10,itm_linen_shirt_13,itm_linen_shirt_14,itm_generic_tunic_11,itm_generic_tunic_13,itm_generic_tunic_14]

tunics_mauri = [itm_berber_tunic_1,itm_berber_tunic_2,itm_berber_tunic_3,itm_berber_tunic_4,itm_berber_tunic_5,itm_simple_tunic_2,itm_simple_tunic_5,itm_simple_tunic_6,itm_simple_tunic_8,itm_simple_tunic_10,itm_imperial_common_shirt]
#for the new slavic troops
tunics_slav = [itm_linen_tunic,itm_tunic_long_pants_5,itm_tunic_long_pants_6,itm_tunic_long_pants_7,itm_tunic_long_pants_9,itm_tunic_long_pants_10]

pants_slav = [itm_pants_7,itm_pants_8,itm_pants_9,itm_pants_9]
#used for town/village walkers
tunics_civ = [itm_linen_shirt_1,itm_linen_shirt_2,itm_linen_shirt_3,itm_linen_shirt_4,itm_linen_shirt_5,itm_linen_shirt_6,itm_linen_shirt_7,itm_linen_shirt_8,itm_linen_shirt_9,itm_linen_shirt_10,itm_linen_shirt_11,itm_coarse_tunic,itm_linen_shirt]

tunics_alans = [itm_linen_tunic,itm_linen_shirt_5,itm_linen_shirt_8,itm_linen_shirt_12,itm_linen_shirt_13,itm_linen_shirt_19,itm_linen_shirt_20]

tunics_hunnic = [itm_kaftan_tunic_1,itm_kaftan_tunic_2,itm_kaftan_tunic_3,itm_kaftan_tunic_6,itm_kaftan_tunic_7,itm_kaftan_sheepskin_1,itm_kaftan_sheepskin_2,itm_kaftan_sheepskin_3]

tunics_white_huns = [itm_khergit_vest_a,itm_khergit_vest_b,itm_khergit_vest_c,itm_khergit_vest_d,itm_kaftan_sheepskin_1,itm_kaftan_sheepskin_2,itm_kaftan_sheepskin_3,itm_kaftan_sheepskin_4,itm_kaftan_sheepskin_5,itm_kaftan_tunic_1,itm_kaftan_tunic_2,itm_kaftan_tunic_7,itm_kaftan_tunic_8,itm_shirt,itm_linen_shirt_22]

tunics_rich = [itm_rich_tunic_1,itm_rich_tunic_2,itm_rich_tunic_3,itm_rich_tunic_4,itm_rich_tunic_5,itm_rich_tunic_6]

tunics_bandits = [itm_bandit_tunic_1,itm_bandit_tunic_2,itm_bandit_tunic_3,itm_shirt,itm_linen_tunic,itm_generic_tunic_13,itm_linen_shirt_22,itm_linen_shirt_10,itm_linen_shirt_13]

tunics_nubians = [itm_african_kilt_1,itm_african_kilt_2,itm_african_kilt_3,itm_roman_shirt_10,itm_shirt,itm_sleeveless_tunic,itm_linen_shirt,itm_imperial_common_shirt,itm_simple_tunic_1,itm_simple_tunic_2,itm_simple_tunic_3]

tunics_goths_noble = [itm_tunic_long_pants_1,itm_tunic_long_pants_2,itm_tunic_long_pants_3,itm_tunic_long_pants_4]

tunics_eastern_germanic_steppe = [itm_rich_tunic_3,itm_rich_tunic_5,itm_rich_tunic_6] #for the more hunnic-influenced cavalry

shoes_generic = [itm_wrapping_boots,itm_ankle_boots,itm_simple_shoes,itm_hunter_boots]

shoes_roman = [itm_ankle_boots,itm_ankle_boots_white,itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4]

tunics_common = [itm_linen_tunic,itm_linen_shirt,itm_linen_shirt_10,itm_linen_shirt_13,itm_shirt]

tunics_caucasian_alans = [itm_shirt,itm_linen_shirt_10,itm_linen_shirt_14,itm_linen_shirt_13,itm_linen_shirt_15,itm_skirmisher_tunic_1,itm_skirmisher_tunic_2,itm_skirmisher_tunic_3,itm_skirmisher_tunic_4]

tunics_caucasian_alans_rich = [itm_rich_tunic_1,itm_rich_tunic_2,itm_rich_tunic_3,itm_rich_tunic_4,itm_rich_tunic_6]

tunics_basque = [itm_generic_tunic_4,itm_generic_tunic_6,itm_generic_tunic_7,itm_generic_tunic_12,itm_generic_tunic_14,itm_linen_shirt_2,itm_linen_shirt_3,itm_linen_shirt_10,itm_linen_shirt_13]

greaves_roman = [itm_roman_greaves_1,itm_roman_greaves_2,itm_roman_greaves_3]
greaves_generic = [itm_roman_greaves_2,itm_sarranid_boots_d,itm_ankle_greaves]

#mainly for tier 5 germanic troops
common_mail_heavy = [itm_mail_with_surcoat,itm_coat_of_plates_red]
#mainly for tier 3 germanic nobles
common_mail_noble = [itm_surcoat_over_mail,itm_mail_hauberk,itm_arabian_armor_b]

leather_armor = [itm_leather_armor_c,itm_leather_armor_d,itm_leather_armor_e] #general leather armor

#tier 2 - tier 5 troops
#shield colors
#western germanic - green, yellow - has greatest variation with tier 5 shields
#eastern germanic - green, grey/black
#northern germanic - red, blue, some yellow, spiral patterns
#goths - blue, white, red
#vandals - black, white, some yellow
#franks - orange, blue, black
#langobards - red, blue
#picts - blue, green
#alans - yellow
#balts - red, black
#slavic - red, white
#frisian - red, orange

shields_mercenary = [itm_tab_shield_round_d,itm_round_shield_wood_1,itm_round_shield_wood_2]

shields_mercenary_small = [itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_round_shield_wood_small_1,itm_round_shield_wood_2]

shields_generic = [itm_round_shield_wood_1,itm_round_shield_wood_2,itm_round_shield_wood_3,itm_round_shield_leather_1,itm_round_shield_leather_2,itm_round_shield_leather_3]

shields_bandit = [itm_round_shield_wood_1,itm_round_shield_wood_2,itm_round_shield_wood_3,itm_round_shield_leather_1,itm_round_shield_leather_2,itm_round_shield_leather_3,itm_round_shield_white_1,itm_round_shield_gray_1,itm_round_shield_gray_2]

shields_basic = [itm_round_shield_wood_1,itm_round_shield_wood_2,itm_round_shield_wood_3,itm_round_shield_wood_small_1,itm_round_shield_wood_small_2,itm_round_shield_wood_small_3,itm_wicker_round_shield,itm_wicker_round_shield,itm_simple_shield_1,itm_simple_shield_2,itm_simple_shield_3,itm_simple_shield_4] #used for tier 2 troops

shields_low_tier_oval = [itm_oval_shield_leather_2,itm_oval_shield_leather_3,itm_oval_shield_leather_1,itm_oval_shield_wicker,itm_oval_shield_wood_1]

shields_simple = [itm_simple_shield_1,itm_simple_shield_2,itm_simple_shield_3,itm_simple_shield_4]

shields_small = [itm_ad_small_shield_1,itm_ad_small_shield_2,itm_ad_small_shield_3,itm_ad_small_shield_4]

shields_western_germanic_1 = [itm_round_shield_red_1,itm_round_shield_orange_1,itm_round_shield_yellow_1,itm_round_shield_green_1,itm_round_shield_green_2,itm_round_shield_white_1,itm_round_shield_germanic_7,itm_round_shield_germanic_12,itm_round_shield_germanic_15] #solid colors, simple designs
shields_western_germanic_2 = [itm_round_shield_germanic_5,itm_round_shield_germanic_10,itm_round_shield_germanic_19,itm_concave_shield_germanic_5,itm_concave_shield_germanic_9,itm_concave_shield_germanic_10,itm_concave_shield_germanic_13,itm_concave_shield_germanic_14,itm_concave_shield_germanic_15,itm_concave_shield_germanic_19,itm_concave_shield_germanic_20,itm_concave_shield_germanic_22] #decorated
shields_western_germanic_cavalry_1 = [itm_concave_shield_germanic_small_5,itm_concave_shield_germanic_small_9,itm_concave_shield_germanic_small_10,itm_concave_shield_germanic_small_13,itm_concave_shield_germanic_small_14,itm_concave_shield_germanic_small_15,itm_concave_shield_germanic_small_19,itm_concave_shield_germanic_small_20]

shields_eastern_germanic_1 = [itm_round_shield_green_2,itm_round_shield_red_3,itm_round_shield_blue_2,itm_round_shield_gray_1,itm_round_shield_white_1,itm_round_shield_germanic_6,itm_round_shield_germanic_7,itm_round_shield_germanic_13] #solid colors, simple designs
shields_eastern_germanic_2 = [itm_round_shield_germanic_6,itm_round_shield_germanic_7,itm_round_shield_germanic_8,itm_round_shield_germanic_13,itm_round_shield_germanic_17,itm_round_shield_germanic_20,itm_concave_shield_germanic_2,itm_concave_shield_germanic_4,itm_concave_shield_germanic_6,itm_concave_shield_germanic_7,itm_concave_shield_germanic_8,itm_concave_shield_germanic_18,itm_concave_shield_germanic_21,itm_round_shield_germanic_21] #decorated
shields_eastern_germanic_cavalry_1 = [itm_round_shield_green_small_2,itm_round_shield_red_small_3,itm_round_shield_blue_small_2,itm_round_shield_gray_small_1,itm_round_shield_white_small_1,itm_round_shield_germanic_small_6,itm_round_shield_germanic_small_7,itm_round_shield_germanic_small_13] #solid colors, simple designs
shields_eastern_germanic_cavalry_2 = [itm_round_shield_germanic_small_17,itm_round_shield_germanic_small_20,itm_concave_shield_germanic_small_2,itm_concave_shield_germanic_small_4,itm_concave_shield_germanic_small_6,itm_concave_shield_germanic_small_7,itm_concave_shield_germanic_small_8,itm_concave_shield_germanic_small_18,itm_concave_shield_germanic_small_21,itm_round_shield_germanic_small_21] #decorated

shields_northern_germanic_1 = [itm_round_shield_blue_1,itm_round_shield_red_1,itm_round_shield_yellow_1,itm_round_shield_white_1,itm_round_shield_germanic_9,itm_round_shield_germanic_11]
shields_northern_germanic_2 = [itm_round_shield_germanic_5,itm_round_shield_germanic_9,itm_round_shield_germanic_10,itm_round_shield_germanic_11,itm_round_shield_germanic_19,itm_concave_shield_germanic_5,itm_concave_shield_germanic_11,itm_concave_shield_germanic_19]
shields_northern_germanic_cavalry_1 = [itm_round_shield_blue_small_1,itm_round_shield_red_small_1,itm_round_shield_yellow_small_1,itm_round_shield_white_small_1,itm_round_shield_germanic_small_9,itm_round_shield_germanic_small_11]

shields_gothic_1 = [itm_round_shield_blue_2,itm_round_shield_blue_3,itm_round_shield_white_1,itm_round_shield_gray_1,itm_round_shield_red_2,itm_round_shield_germanic_1,itm_round_shield_germanic_13,itm_round_shield_germanic_14,itm_round_shield_germanic_15,itm_round_shield_germanic_16,itm_round_shield_germanic_18,itm_round_shield_germanic_20,]
shields_gothic_2 = [itm_round_shield_germanic_1,itm_round_shield_germanic_13,itm_round_shield_germanic_14,itm_round_shield_germanic_15,itm_round_shield_germanic_16,itm_round_shield_germanic_18,itm_round_shield_germanic_20,itm_concave_shield_germanic_1,itm_concave_shield_germanic_3,itm_concave_shield_germanic_12,itm_concave_shield_germanic_16,itm_concave_shield_germanic_17,itm_round_shield_roman_15,itm_round_shield_roman_16]
shields_gothic_cavalry_1 = [itm_round_shield_blue_small_2,itm_round_shield_blue_small_3,itm_round_shield_white_small_1,itm_round_shield_gray_small_1,itm_round_shield_red_small_2,itm_round_shield_germanic_small_1,itm_round_shield_germanic_small_13,itm_round_shield_germanic_small_14,itm_round_shield_germanic_small_15,itm_round_shield_germanic_small_16,itm_round_shield_germanic_small_18,itm_round_shield_germanic_small_20]
shields_gothic_cavalry_2 = [itm_round_shield_germanic_small_1,itm_round_shield_germanic_small_13,itm_round_shield_germanic_small_14,itm_round_shield_germanic_small_15,itm_round_shield_germanic_small_16,itm_round_shield_germanic_small_18,itm_round_shield_germanic_small_20,itm_concave_shield_germanic_small_1,itm_concave_shield_germanic_small_3,itm_concave_shield_germanic_small_12,itm_concave_shield_germanic_small_16,itm_concave_shield_germanic_small_17]

shields_britons_1 = [itm_round_shield_blue_3,itm_round_shield_red_2,itm_round_shield_white_1,itm_concave_shield_red_2,itm_concave_shield_blue_3,itm_concave_shield_white_1]
shields_britons_2 = [itm_round_shield_roman_2,itm_round_shield_roman_3,itm_round_shield_roman_4,itm_round_shield_roman_5,itm_round_shield_roman_6,itm_round_shield_roman_26,itm_concave_shield_roman_1,itm_concave_shield_briton_1,itm_concave_shield_briton_2,itm_concave_shield_briton_3]
shields_britons_cavalry_1 = [itm_concave_shield_red_small_2,itm_concave_shield_blue_small_3,itm_concave_shield_white_small_1,itm_round_shield_roman_small_2,itm_round_shield_roman_small_3,itm_round_shield_roman_small_4,itm_round_shield_roman_small_5,itm_round_shield_roman_small_6,itm_concave_shield_roman_small_1,itm_round_shield_roman_small_26]

oval_shields_limitanei = [itm_oval_shield_red_1,itm_oval_shield_red_2,itm_oval_shield_blue_1,itm_oval_shield_blue_2,itm_oval_shield_green_1,itm_oval_shield_green_2,itm_oval_shield_1]

oval_shields_limitanei_1 = [itm_oval_shield_red_1,itm_oval_shield_red_2,itm_oval_shield_blue_1,itm_oval_shield_blue_2,itm_oval_shield_green_1,itm_oval_shield_green_2,itm_oval_shield_yellow_1]
oval_shields_limitanei_2 = [itm_oval_shield_1,itm_oval_shield_limitanei_1,itm_oval_shield_limitanei_2,itm_oval_shield_limitanei_3,itm_oval_shield_limitanei_4,itm_oval_shield_limitanei_5]
oval_shields_pseudo = [itm_oval_shield_red_1,itm_oval_shield_red_2,itm_oval_shield_blue_1,itm_oval_shield_blue_2,itm_oval_shield_pseudo_1,itm_oval_shield_pseudo_2,itm_oval_shield_pseudo_3]

round_shields_limitanei_1 = [itm_concave_shield_red_1,itm_concave_shield_red_2,itm_concave_shield_blue_1,itm_concave_shield_blue_3,itm_concave_shield_green_1,itm_concave_shield_yellow_1,itm_concave_shield_white_1] #basic colors
round_shields_limitanei_1_light = [itm_concave_shield_red_small_1,itm_concave_shield_red_small_2,itm_concave_shield_blue_small_1,itm_concave_shield_blue_small_3,itm_concave_shield_green_small_1,itm_concave_shield_yellow_small_1,itm_concave_shield_white_small_1] #basic colors
round_shields_limitanei_2 = [itm_concave_shield_roman_1,itm_concave_shield_roman_2,itm_concave_shield_roman_3,itm_concave_shield_roman_4,itm_concave_shield_roman_5,itm_concave_shield_roman_6] #Designs
round_shields_limitanei_2_light = [itm_concave_shield_roman_small_1,itm_concave_shield_roman_small_2,itm_concave_shield_roman_small_3,itm_concave_shield_roman_small_4,itm_concave_shield_roman_small_5,itm_concave_shield_roman_small_6] #Designs - for cav
round_shields_psuedo = [itm_concave_shield_red_1,itm_concave_shield_red_2,itm_tab_shield_round_b]
shields_dalmate = [itm_concave_shield_roman_11,itm_concave_shield_roman_12]
shields_promoti = [itm_concave_shield_roman_9,itm_concave_shield_roman_10]
shields_scutarii = [itm_concave_shield_roman_7,itm_concave_shield_roman_8]

oval_shields_britons = [itm_oval_shield_limitanei_2,itm_oval_shield_briton_1,itm_oval_shield_briton_2,itm_oval_shield_briton_3,itm_oval_shield_chi_rho_1,itm_oval_shield_chi_rho_5,itm_oval_shield_red_1,itm_oval_shield_blue_2,itm_oval_shield_limitanei_5,itm_oval_shield_limitanei_7]
oval_shields_noricum = [itm_oval_shield_blue_1,itm_oval_shield_blue_2,itm_oval_shield_chi_rho_2,itm_oval_shield_chi_rho_6,itm_oval_shield_chi_rho_7]

oval_shields_basic = [itm_oval_shield_wicker,itm_oval_shield_wood_1,itm_oval_shield_wood_2,itm_oval_shield_wood_3,itm_oval_shield_leather_1,itm_oval_shield_leather_2,itm_oval_shield_leather_3]

shields_picts = [itm_vae_cuadrado_3,itm_vae_cuadrado_4,itm_vae_cuadrado_21,itm_vae_cuadrado_27,itm_pictish_square_shield]
shields_pictish_small = [itm_concave_shield_red_small_1,itm_concave_shield_blue_small_1,itm_concave_shield_green_small_1]

shields_slavic_1 = [itm_round_shield_wood_1,itm_round_shield_wood_2,itm_round_shield_wood_3,itm_round_shield_leather_3,itm_round_shield_white_1,itm_round_shield_gray_1]
shields_slavic_cavalry_1 = [itm_round_shield_wood_small_1,itm_round_shield_wood_small_2,itm_round_shield_wood_small_3,itm_round_shield_leather_small_3,itm_round_shield_white_small_1,itm_round_shield_gray_small_1]

shields_bagadua_1 = [itm_round_shield_wood_1,itm_round_shield_wood_2,itm_round_shield_wood_3,itm_round_shield_green_1,itm_round_shield_green_2,itm_round_shield_green_small_1,itm_round_shield_green_small_2] #basic round shields, mainly green
shields_bagadua_1 = [itm_concave_shield_red_1,itm_concave_shield_green_1,itm_concave_shield_green_2,itm_concave_shield_roman_2,itm_concave_shield_roman_5,itm_concave_shield_roman_6,] #roman round shields

shields_coptic = [itm_concave_shield_red_1,itm_concave_shield_red_3,itm_concave_shield_blue_2,itm_concave_shield_white_1,itm_concave_shield_yellow_1,itm_concave_shield_orange_1]

shields_cantabrian_1 = [itm_round_shield_green_1,itm_round_shield_red_3]
shields_cantabrian_2 = [itm_round_shield_cantabrian_1,itm_round_shield_cantabrian_2,itm_round_shield_cantabrian_3,itm_round_shield_cantabrian_4,itm_round_shield_cantabrian_5,itm_round_shield_cantabrian_6,itm_round_shield_cantabrian_7]
shields_cantabrian_small = [itm_round_shield_cantabrian_small_1,itm_round_shield_cantabrian_small_2,itm_round_shield_cantabrian_small_3,itm_round_shield_cantabrian_small_4,itm_round_shield_cantabrian_small_5,itm_round_shield_cantabrian_small_6,itm_round_shield_cantabrian_small_7,itm_round_shield_green_small_1,itm_round_shield_red_small_3]

shields_crimean_goth_1 = [itm_round_shield_wood_1,itm_round_shield_wood_2,itm_round_shield_wood_3,itm_round_shield_white_1,itm_round_shield_green_1,itm_round_shield_blue_1,itm_round_shield_blue_2]
shields_crimean_goth_2 = [itm_round_shield_germanic_13,itm_round_shield_germanic_15,itm_round_shield_germanic_17,itm_round_shield_germanic_18,itm_round_shield_germanic_21,itm_concave_shield_germanic_small_1,itm_concave_shield_germanic_small_3,itm_concave_shield_germanic_small_17]
shields_crimean_goth_3 = [itm_kerch_shield_1,itm_kerch_shield_2,itm_kerch_shield_3,itm_kerch_shield_4,itm_kerch_shield_5,itm_kerch_shield_6,itm_kerch_shield_7,itm_kerch_shield_8,itm_kerch_shield_9,itm_kerch_shield_10,itm_kerch_shield_11,itm_kerch_shield_12,itm_kerch_shield_13,itm_kerch_shield_14,itm_kerch_shield_15,itm_kerch_shield_wood]

cloaked_tunics_western_germanic = [itm_cloaked_generic_tunic_2,itm_cloaked_generic_tunic_6,itm_cloaked_generic_tunic_13,itm_cloaked_tunic_4,itm_cloaked_tunic_5,itm_cloaked_tunic_9,itm_cloaked_tunic_10,itm_cloaked_tunic_11,itm_cloaked_tunic_12,itm_cloaked_tunic_17]
cloaked_tunics_eastern_germanic = [itm_cloaked_generic_tunic_2,itm_cloaked_generic_tunic_9,itm_cloaked_generic_tunic_10,itm_cloaked_generic_tunic_11,itm_cloaked_tunic_5,itm_cloaked_tunic_9,itm_cloaked_tunic_10,itm_cloaked_tunic_11,itm_cloaked_tunic_12,itm_cloaked_tunic_17]
cloaked_tunics_northern_germanic = [itm_cloaked_generic_tunic_1,itm_cloaked_generic_tunic_3,itm_cloaked_generic_tunic_4,itm_cloaked_generic_tunic_7,itm_cloaked_generic_tunic_13,itm_cloaked_tunic_16,itm_cloaked_tunic_1,itm_cloaked_tunic_6,itm_cloaked_tunic_8,itm_cloaked_tunic_3,itm_cloaked_tunic_5,itm_cloaked_tunic_9,itm_cloaked_tunic_10]
cloaked_tunics_gothic = [itm_cloaked_generic_tunic_1,itm_cloaked_generic_tunic_3,itm_cloaked_generic_tunic_5,itm_cloaked_generic_tunic_7,itm_cloaked_generic_tunic_8,itm_cloaked_generic_tunic_12,itm_cloaked_tunic_5,itm_cloaked_tunic_6,itm_cloaked_tunic_7,itm_cloaked_tunic_8]

#light armors - caped tunics/padded armors/leather armors/thick coats - used for tier 3 - 4 units + noble tier 1 troops
light_armor_briton = [itm_cloaked_tunic_briton_1,itm_cloaked_tunic_briton_2,itm_cloaked_tunic_briton_3,itm_cloaked_tunic_briton_4,itm_cloaked_tunic_briton_5,itm_cloaked_tunic_briton_6,itm_cloaked_tunic_briton_7,itm_cloaked_tunic_briton_8,itm_cloaked_tunic_briton_9,itm_cloaked_tunic_falkirk_1,itm_cloaked_tunic_falkirk_3,itm_cloaked_tunic_falkirk_5,itm_cloaked_tunic_10]
light_armor_pict = [itm_cloaked_tunic_falkirk_1,itm_cloaked_tunic_falkirk_2,itm_cloaked_tunic_falkirk_3,itm_cloaked_tunic_falkirk_4,itm_cloaked_tunic_falkirk_5]
#used by the germanic skirmishers
#germanic bandits 
german_thick_coats =  [itm_thick_coat_1,itm_thick_coat_2,itm_thick_coat_3,itm_thick_coat_6,itm_rawhide_coat1,itm_rawhide_coat5,itm_rawhide_coat7,itm_rawhide_coat8,itm_rawhide_coat9,itm_rawhide_coat11]

#mails for units
mail_gothic_noble = [itm_rich_mail_1,itm_rich_mail_2,itm_rich_mail_3,itm_rich_mail_4]

mail_numeri = [itm_mail_shirt,itm_mid_generic_mail_1,itm_mid_generic_mail_2,itm_mid_generic_mail_3,itm_mid_generic_mail_4,itm_mid_generic_mail_5]

#hats for low tier troops
#mix of phyringian caps, woolen/fur caps and other hats
hats_franks = [itm_woolen_cap_simple_4,itm_woolen_cap_2,itm_woolen_cap,itm_woolen_cap_simple_2,itm_woolen_cap_5]
hats_german = [itm_woolen_cap,itm_woolen_cap_4,itm_woolen_cap_1,itm_woolen_cap_6,itm_woolen_cap_simple_3,itm_woolen_cap_simple_4,itm_head_wrappings,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2]
hats_goth = [itm_woolen_cap_4,itm_woolen_cap_1,itm_woolen_cap_2,itm_woolen_cap_6,itm_woolen_cap_8]
hats_vandal = [itm_head_wrappings,itm_woolen_cap_b,itm_woolen_cap_3,itm_woolen_cap_4,itm_woolen_cap_c,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2]
hats_briton = [itm_woolen_cap_2,itm_woolen_cap_4,itm_woolen_cap_1]
hats_white_huns = [itm_chionite_hat_1,itm_chionite_hat_2,itm_chionite_hat_3,itm_chionite_hat_4,itm_chionite_hat_5]
hats_sassanids = [itm_bulb_cap_1,itm_bulb_cap_2,itm_bulb_cap_3,itm_bulb_cap_4,itm_bulb_cap_5,itm_bulb_cap_6,itm_woolen_cap_c,itm_woolen_cap_1,itm_woolen_cap_4]
#may not be used - lombards
hats_lombard = [itm_woolen_cap_1,itm_woolen_cap_2,itm_woolen_cap_6,itm_woolen_cap_simple_2,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2]
hats_northern = [itm_woolen_cap_simple_2,itm_woolen_cap_simple_1,itm_woolen_cap_1,itm_woolen_cap_2]
hats_pict = [itm_head_wrappings,itm_brown_hood1,itm_brown_hood1]
hats_huns = [itm_hunnic_phrygian_1,itm_hunnic_phrygian_2,itm_hunnic_phrygian_3,itm_hunnic_phrygian_4,itm_hunnic_phrygian_5,itm_hunnic_phrygian_6]
hats_arabs = [itm_turban,itm_desert_turban,itm_headcloth,itm_turban_white_1,itm_turban_white_2,itm_turban_brown_1,itm_turban_brown_2,itm_turban_black_1,itm_turban_black_2,itm_turban_red_1,itm_turban_red_2]
#used by roman troops
pannonian_hats = [itm_pannonian_cap_1,itm_pannonian_cap_2,itm_pannonian_cap_3,itm_pannonian_cap_4,itm_pannonian_cap_5,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2]
#used by germanic troops
germanic_caps = [itm_germanic_cap_1,itm_germanic_cap_2,itm_germanic_cap_3,itm_germanic_cap_4]
#used for townwalkers/villagers
woolen_caps = [itm_woolen_cap_simple_1,itm_woolen_cap_simple_2,itm_woolen_cap_simple_3,itm_woolen_cap_simple_4,itm_woolen_cap_simple_5]
phyringian_caps = [itm_woolen_cap,itm_woolen_cap_b,itm_woolen_cap_c,itm_woolen_cap_1,itm_woolen_cap_2,itm_woolen_cap_3,itm_woolen_cap_4,itm_woolen_cap_5,itm_woolen_cap_6]
#generic helmets for the various germanic cultures to use (germans, goths, vandals, northern)
#commoner units use roman helmets (idea captured + taken from battle)
#nobles use more decorative spangenhelms to denote their rank and influence (purchase helmets)

#tarasovsky, dura, metropolitan helmets
helmets_sassanid_1 = [itm_sassanid_helmet_cloth_1,itm_sassanid_helmet_cloth_2,itm_sassanid_helm_5,itm_tarasovsky_1784_helmet_leather,itm_tarasovsky_1784_helmet_cloth,itm_tsaritsyno_1_simple] #cloth backing
helmets_sassanid_2 = [itm_sassanid_helmet_mail_1,itm_sassanid_helmet_mail_2,itm_sassanid_helmet_mail_3,itm_sassanid_helmet_mail_4,itm_sassanid_helmet_mail_5,itm_sarranid_horseman_helmet,itm_tarasovsky_1784_helmet_mail_2,itm_tsaritsyno_1_light] #mail

#used by tier one recruits
weapons_basic = [itm_pitch_fork_1,itm_pitch_fork_2,itm_knife,itm_butchering_knife,itm_cleaver,itm_sickle,itm_staff,itm_iron_staff,itm_wooden_stick,itm_hatchet]
#franciscas for the franks primarily
franciscas_1 = [itm_light_throwing_axes,itm_light_throwing_axes,itm_light_throwing_axes,itm_light_throwing_axes]
franciscas_2 = [itm_throwing_axes,itm_throwing_axes,itm_throwing_axes,itm_throwing_axes]
franciscas_3 = [itm_heavy_throwing_axes,itm_heavy_throwing_axes,itm_heavy_throwing_axes,itm_heavy_throwing_axes]
#angons for franks, n. germanics and germanics
angons = [itm_angon_1,itm_angon_1,itm_angon_2,itm_angon_2]
#throwning spears for generic troops
throwing_spears_1 = [itm_throwing_spear_1,itm_throwing_spear_1,itm_throwing_spear_1]
throwing_spears_2 = [itm_throwing_spear_2,itm_throwing_spear_2,itm_throwing_spear_2]

#horses
horses_1 =[itm_sumpter_horse,itm_arabian_horse_a4,itm_arabian_horse_a3,itm_courser4,itm_normal_horse17]
horses_2 = [itm_saddle_horse,itm_saddle_horse_2,itm_saddle_horse_3,itm_saddle_horse_4,itm_saddle_horse_5,itm_normal_horse11,itm_normal_horse13,itm_normal_horse16]
horses_3 = [itm_courser,itm_warhorse,itm_charger,itm_saddle_horse_2]

horses_alans_1 = [itm_arabian_horse_b3,itm_normal_horse18,itm_normal_horse19,itm_normal_horse14,itm_normal_horse15,itm_normal_horse16,itm_normal_horse17,itm_normal_horse23,itm_normal_horse26,itm_imperial_saddle_horse_3]
horses_alans_2 = [itm_normal_horse14,itm_normal_horse15,itm_normal_horse16,itm_normal_horse17,itm_normal_horse23,itm_normal_horse26,itm_imperial_saddle_horse_3,itm_courser,itm_warhorse]

horses_roman_1 = [itm_asturco_roman_1,itm_asturco_roman_2,itm_asturco_roman_3] #asturco horses
horses_roman_2 = [itm_camargue_roman_1,itm_camargue_roman_2,itm_camargue_roman_3] #camargue horses
horses_roman_3 = [itm_iberian_warhorse_roman_1,itm_iberian_warhorse_roman_2] #iberian horses
horses_roman_4 = [itm_nisean_roman_1,itm_nisean_roman_2,itm_nisean_roman_3] #nisean horses

horses_mauri_1 = [itm_barb_light_1,itm_barb_light_2,itm_barb_light_3]
horses_mauri_2 = [itm_barb_1,itm_barb_2,itm_barb_3]
horses_mauri_3 = [itm_barb_cham_1,itm_barb_cham_2,itm_barb_cham_3]

horses_germanic_1 = [itm_asturco_germanic_1,itm_asturco_germanic_2,itm_asturco_germanic_3] #asturco horses
horses_germanic_2 = [itm_camargue_germanic_1,itm_camargue_germanic_2,itm_camargue_germanic_3] #camargue horses
horses_germanic_3 = [itm_iberian_warhorse_germanic_1,itm_iberian_warhorse_germanic_2] #iberian horses
horses_germanic_4 = [itm_westger_warhorse_1,itm_westger_warhorse_2] #northern horses

horses_hunnic_1 = [itm_hun_horse_1,itm_hun_horse_2,itm_hun_horse_3,itm_hun_horse_4]
horses_hunnic_2 = [itm_hun_rich_horse_nobard_1,itm_hun_rich_horse_nobard_2]
horses_hunnic_3 = [itm_hun_rich_horse_1,itm_hun_rich_horse_2]

horses_cataphract = [itm_nisean_cataphract_1,itm_nisean_cataphract_2,itm_nisean_cataphract_3,itm_nisean_cataphract_4]

#Generic weapons tiers for germanic troops //// OLD ////
#basic equipment for tier 1 units, have basic bow + arrow

veils_1 = [itm_turret_hat_ruby,itm_turret_hat_blue,itm_turret_hat_green,itm_court_hat,itm_wimple_a]
veils_2 = [itm_wimple_with_veil,itm_female_hood,itm_khergit_lady_hat,itm_khergit_lady_hat_b,itm_sarranid_felt_hat,itm_felt_hat,itm_felt_hat_b]

dresses = [itm_dress_4,itm_dress_5,itm_dress_4,itm_lady_dress_ruby,itm_lady_dress_blue,itm_khergit_lady_dress_b]

troops = [
  ["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,
   [],
   str_4|agi_4|int_4|cha_4,wp(15),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_leather_jerkin, itm_leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_tribal_warrior_outfit, itm_leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib|str_30|agi_30,0,knows_common|knows_inventory_management_10|knows_power_throw_10|knows_power_draw_10,0],
##  ["game","Game","Game",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
##  ["unarmed_troop","Unarmed Troop","Unarmed Troops",tf_hero,no_scene,reserved,fac_commoners,[itm_arrows,itm_short_bow],def_attrib|str_14,0,knows_common|knows_power_draw_2,0],

####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
  ["find_item_cheat","find_item_cheat","find_item_cheat",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["random_town_sequence","Random Town Sequence","Random Town Sequence",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tournament_participants","Tournament Participants","Tournament Participants",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tutorial_maceman","Maceman","Maceman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_club,itm_leather_jerkin,itm_hide_boots],
   str_6|agi_6|level(1),wp(50),knows_common,man_face_1,man_face_2],
  ["tutorial_archer","Archer","Archer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_tutorial_short_bow,itm_tutorial_arrows,itm_linen_tunic,itm_hide_boots],
   str_6|agi_6|level(5),wp(100),knows_common|knows_power_draw_4,man_face_1,man_face_2],
  ["tutorial_swordsman","Swordsman","Swordsman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_sword,itm_leather_vest,itm_hide_boots],
   str_6|agi_6|level(5),wp(80),knows_common,man_face_1,man_face_2],

  ["novice_fighter","Novice Fighter","Novice Fighters",tf_guarantee_basic,no_scene,reserved,fac_commoners,
   [itm_roman_spear_1,itm_round_shield_wood_1,itm_round_shield_wood_2,itm_round_shield_wood_3]+tunics_generic+shoes_generic, #tunic, boots, spear, shield
   def_attrib_lvl_9|level(5),wp(80),knows_lvl_9|knows_shield_2|knows_power_strike_2|knows_riding_2,man_face_1, man_face_2],
  ["regular_fighter","Regular Fighter","Regular Fighters",tf_guarantee_basic,no_scene,reserved,fac_commoners,
   [itm_roman_spear_2,itm_fighting_axe,itm_round_shield_wood_1,itm_round_shield_wood_2,itm_round_shield_wood_3,itm_woolen_cap_b,itm_woolen_cap_1]+tunics_generic+shoes_generic, #tunics, spear, axe, shield, cap
   def_attrib_lvl_13|level(11),wp(110),knows_lvl_13_inf|knows_shield_3|knows_power_strike_3|knows_riding_3,man_face_1, man_face_2],
  ["veteran_fighter","Veteran Fighter","Veteran Fighters",tf_guarantee_basic,no_scene,0,fac_commoners,
   [itm_sword_medieval_a,itm_round_shield_wood_1,itm_round_shield_wood_2,itm_round_shield_wood_3,itm_intercisa_helmet_1,itm_haditha_1,itm_narona_bandhelm_cloth]+tunics_generic+shoes_generic, #tunics, sword, shield, helmets
   def_attrib_lvl_18|level(17),wp(170),knows_lvl_18_inf|knows_shield_4|knows_power_strike_4|knows_riding_4,man_face_1, man_face_2],
  ["champion_fighter","Champion Fighter","Champion Fighters",tf_guarantee_basic,no_scene,reserved,fac_commoners,
   [itm_sword_medieval_a,itm_mail_shirt,itm_byrnie,itm_intercisa_helmet_1,itm_iatrus_1,itm_iatrus_helmet_mail,itm_augst_helmet_1,itm_haditha_1,itm_narona_bandhelm_mail,itm_round_shield_wood_1,itm_round_shield_wood_2,itm_round_shield_wood_3]+tunics_generic+shoes_generic, #sword, shield, mail, helmet
   def_attrib_lvl_23|level(23),wp(200),knows_lvl_23_inf|knows_shield_5|knows_power_strike_5|knows_riding_4,man_face_1, man_face_2],

  ["arena_training_fighter_1","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_6|agi_6|level(5),wp(60),knows_common,man_face_1, man_face_2],
  ["arena_training_fighter_2","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_7|agi_6|level(7),wp(70),knows_common,man_face_1, man_face_2],
  ["arena_training_fighter_3","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_7|level(9),wp(80),knows_common,man_face_1, man_face_2],
  ["arena_training_fighter_4","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_8|level(11),wp(90),knows_common,man_face_1, man_face_2],
  ["arena_training_fighter_5","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_9|agi_8|level(13),wp(110),knows_common,man_face_1, man_face_2],
  ["arena_training_fighter_6","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_10|agi_9|level(15),wp(140),knows_common,man_face_1, man_face_2],
  ["arena_training_fighter_7","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_10|agi_10|level(17),wp(150),knows_common,man_face_1, man_face_2],
  ["arena_training_fighter_8","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_11|agi_10|level(19),wp(170),knows_common,man_face_1, man_face_2],
  ["arena_training_fighter_9","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_11|level(21),wp(240),knows_common,man_face_1, man_face_2],
  ["arena_training_fighter_10","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_12|level(23),wp(250),knows_common,man_face_1, man_face_2],

  ["cattle","Cattle","Cattle",0,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),0,man_face_1, man_face_2],


#soldiers:
#This troop is the troop marked as soldiers_begin
  ["farmer","Farmer","Farmers",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_pitch_fork_1,itm_pitch_fork_2,itm_iron_staff,itm_staff,itm_sickle,itm_club,itm_quarter_staff,itm_flintlock_pistol,itm_cartridges,itm_cartridges,itm_wrapping_boots,itm_ankle_boots,itm_simple_shoes,itm_linen_tunic,itm_shirt,itm_linen_shirt_22,itm_linen_shirt_12,itm_linen_shirt_5,itm_linen_shirt_9,itm_straw_hat,itm_leather_cap,itm_new_hood_c,itm_new_hood_d,itm_brown_hood1],
   def_attrib_lvl_9|level(6),wp(90)|wp_firearm(90),knows_lvl_9,man_face_1, man_face_2],

  ["townsman","Townsman","Townsmen",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_pitch_fork_1,itm_pitch_fork_2,itm_iron_staff,itm_staff,itm_sickle,itm_club,itm_quarter_staff,itm_flintlock_pistol,itm_cartridges,itm_cartridges,itm_wrapping_boots,itm_ankle_boots,itm_simple_shoes,itm_linen_tunic,itm_shirt,itm_linen_shirt_22,itm_linen_shirt_12,itm_linen_shirt_5,itm_linen_shirt_9,itm_straw_hat,itm_leather_cap,itm_new_hood_c,itm_new_hood_d,itm_brown_hood1],
   def_attrib_lvl_9|level(6),wp(90)|wp_firearm(90),knows_lvl_9,man_face_1, man_face_2],

  ["caravan_guard","Eques Mercenarii","Equites Mercenarii",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm,no_scene,0,fac_commoners, #long spear, sword
   [itm_medium_spear_3,itm_sword_medieval_a,itm_intercisa_helmet_1,itm_woolen_cap_4,itm_woolen_cap_b,itm_woolen_cap_3,itm_woolen_cap_6,itm_woolen_cap_8,itm_woolen_cap_1,itm_leather_cap,itm_brown_hood1,itm_new_hood_b,itm_round_shield_wood_small_1,itm_round_shield_wood_small_2,itm_round_shield_wood_small_3]+shoes_generic+horses_roman_1+horses_roman_2+tunics_generic,
   def_attrib_lvl_18|level(17),wp(170),knows_lvl_18_cav|knows_shield_3|knows_power_strike_3,man_face_1, man_face_2],

#farmer -> watchman -> iuvenis -> pedes mercenarii
#                   -> mercenary archer 
#eques mercenarii -> eques contarii mercenarii
  #battle axe + javelin armed mercenary
  ["mercenary_swordsman","Iuvenis","Iuvenes",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners, #axe, throwing spears
   [itm_intercisa_helmet_1,itm_augst_helmet_1,itm_iatrus_1,itm_leather_cap,itm_brown_hood1,itm_new_hood_b,itm_battle_axe_2,itm_throwing_spear_1,itm_throwing_spear_1,itm_round_shield_wood_2,itm_round_shield_red_1,itm_round_shield_blue_2,itm_round_shield_green_1,itm_round_shield_yellow_1,itm_round_shield_white_1,itm_round_shield_gray_1,itm_round_shield_gray_2]+tunics_generic+shoes_generic,
   def_attrib_lvl_18|level(18),wp_one_handed(170)|wp_two_handed(170)|wp_polearm(160)|wp_throwing(170)|wp_archery(80)|wp_crossbow(80)|wp_firearm(80),knows_lvl_18_inf|knows_shield_4|knows_power_strike_4,man_face_1, man_face_2],
  #axe, throwing spear, spear
  ["hired_blade","Pedes Mercenarii","Pedites Mercenarii",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_intercisa_helmet_1,itm_augst_helmet_1,itm_iatrus_1,itm_generic_subarmalis_6,itm_generic_subarmalis_8,itm_mid_generic_mail_26,itm_mid_generic_mail_23,itm_mid_generic_mail_11,itm_mail_shirt,itm_short_ragged_mail_1,itm_short_ragged_mail_6,itm_short_ragged_mail_11,itm_battle_axe_4,itm_polehammer,itm_throwing_spear_1,itm_tab_shield_round_d]+shoes_generic,
   def_attrib_lvl_23|level(23),wp_one_handed(200)|wp_two_handed(180)|wp_polearm(200)|wp_throwing(190)|wp_archery(100)|wp_crossbow(100)|wp_firearm(100),knows_lvl_23_inf|knows_shield_5|knows_power_strike_5,man_face_1, man_face_2],
  #contus armed mercenary cavalry
  ["mercenary_horseman","Eques Contarius Mercenarius ","Equites Contarii Mercenarii",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse,no_scene,reserved,fac_commoners,
   [itm_intercisa_helmet_1,itm_augst_helmet_1,itm_iatrus_1,itm_generic_subarmalis_6,itm_generic_subarmalis_8,itm_mid_generic_mail_26,itm_mid_generic_mail_23,itm_mid_generic_mail_11,itm_mail_shirt,itm_short_ragged_mail_1,itm_short_ragged_mail_6,itm_short_ragged_mail_11,itm_sword_medieval_a,itm_polehammer,itm_tab_shield_small_round_b]+shoes_generic+horses_roman_3,
   def_attrib_lvl_23|level(23),wp_one_handed(190)|wp_two_handed(170)|wp_polearm(210)|wp_throwing(150)|wp_archery(100)|wp_crossbow(100)|wp_firearm(100),knows_lvl_23_cav|knows_shield_3|knows_power_strike_6,man_face_1, man_face_2],

  ["mercenary_archer","Sagittarius Mercenarii","Sagittarii Mercenarii",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_woolen_cap_4,itm_woolen_cap_b,itm_woolen_cap_3,itm_woolen_cap_6,itm_woolen_cap_8,itm_woolen_cap_1,itm_leather_cap,itm_new_hood_d,itm_brown_hood1,itm_new_hood_c,itm_short_bow,itm_long_bow,itm_arrows,itm_arrows,itm_fighting_axe]+shoes_generic+tunics_generic,
   def_attrib_lvl_18|level(17),wp_one_handed(130)|wp_two_handed(130)|wp_polearm(130)|wp_throwing(140)|wp_archery(150)|wp_crossbow(100)|wp_firearm(100),knows_archer,man_face_1, man_face_2],

  #Herulian slaves are known to have accompanied them into combat. Slaves were forbidden from donning a shield until having proven themselves brave on the battlefield
  ["heruli_slave","Heruli Slave","Heruli Slave",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_polearm,no_scene,reserved,fac_heruli,
   [itm_wrapping_boots,itm_simple_shoes,itm_roman_spear_3,itm_knife,itm_linen_tunic,itm_shirt,itm_linen_shirt_22,itm_skirmisher_tunic_1,itm_skirmisher_tunic_4,itm_throwing_spear_1,itm_throwing_spear_1,itm_new_hood_d,itm_new_hood_e,itm_brown_hood1] + germanic_caps, 
   def_attrib_lvl_13|level(13),wp_one_handed(140)|wp_two_handed(130)|wp_polearm(150)|wp_throwing(150)|wp_archery(100)|wp_crossbow(100)|wp_firearm(100),knows_lvl_13_inf|knows_power_strike_5|knows_shield_1,germanic_face_1, germanic_face_2],

  ["heruli_warrior","Heruli Warrior","Heruli Warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm,no_scene,reserved,fac_heruli,
   [itm_round_shield_germanic_4,itm_round_shield_germanic_15,itm_sword_medieval_a,itm_heavy_spear_1,itm_simple_shoes,itm_khergit_leather_boots,itm_hunter_boots,itm_tunic_long_pants_3,itm_tunic_long_pants_6,itm_generic_tunic_3,itm_generic_tunic_12,itm_cloaked_generic_tunic_3,itm_cloaked_generic_tunic_12,itm_generic_subarmalis_7,itm_short_ragged_mail_7,itm_short_ragged_mail_12,itm_mid_generic_mail_22,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_leather_cap,itm_generic_leather_helmet_cloth,itm_iatrus_helmet_mail,itm_iatrus_helmet_light,itm_intercisa_helmet_1,itm_augst_helmet_1,itm_iatrus_1]+throwing_spears_1+throwing_spears_1,
   def_attrib_lvl_23|level(23),wp_one_handed(220)|wp_two_handed(220)|wp_polearm(230)|wp_throwing(220),knows_lvl_23_inf|knows_shield_4|knows_power_strike_6,germanic_face_1, germanic_face_2],

  ["heruli_horseman","Heruli Horseman","Heruli Horsemen",tf_mounted|tf_guarantee_horse|tf_guarantee_basic,no_scene,reserved,fac_heruli,
   [itm_round_shield_germanic_small_4,itm_round_shield_germanic_small_15,itm_sword_medieval_a,itm_polehammer,itm_light_lance,itm_heavy_lance,itm_simple_shoes,itm_khergit_leather_boots,itm_hunter_boots,itm_tunic_long_pants_3,itm_tunic_long_pants_6,itm_generic_tunic_3,itm_generic_tunic_12,itm_cloaked_generic_tunic_3,itm_cloaked_generic_tunic_12,itm_generic_subarmalis_7,itm_short_ragged_mail_7,itm_short_ragged_mail_12,itm_mid_generic_mail_22,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_iatrus_helmet_mail,itm_iatrus_helmet_light,itm_intercisa_helmet_1,itm_augst_helmet_1,itm_iatrus_1]+horses_2,
   def_attrib_lvl_23|level(23),wp_one_handed(210)|wp_two_handed(220)|wp_polearm(240)|wp_throwing(230),knows_lvl_23_cav|knows_shield_4|knows_power_strike_6,germanic_face_1, germanic_face_2],

  ["bulgar_horseman","Onogur Eques Sagittarius","Onogurs Equites Sagittarii",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,no_scene,0,fac_commoners,
   [itm_rich_tunic_6,itm_linen_shirt_10,itm_skirmisher_tunic_2,itm_simple_shoes,itm_hunter_boots,itm_nomad_boots,itm_fur_hat,itm_brown_hood1,itm_strong_bow,itm_khergit_bow,itm_barbed_arrows,itm_barbed_arrows,itm_fighting_axe,itm_hunnic_spatha]+horses_hunnic_1,
   def_attrib_lvl_18|level(18),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(160)|wp_archery(160),knows_horse_archer,steppe_face_1, steppe_face_2],

  ["standard_bearer","Standard Bearer","Standard Bearer",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_flag_pole_1,itm_wrapping_boots,itm_ankle_boots,itm_simple_shoes,itm_linen_shirt_1,itm_linen_shirt_2,itm_linen_shirt_3,itm_linen_shirt_10,itm_linen_shirt_13,itm_linen_shirt_14,itm_intercisa_helmet_1,itm_triveres_mail],
   def_attrib_lvl_18|level(18),wp_two_handed(160) | wp_polearm(160),knows_common|knows_ironflesh_8|knows_athletics_6|knows_power_strike_4,man_face_1, man_face_2],

  ["draco_bearer","Draconarius","Draconarii",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,no_scene,reserved,fac_commoners,
   [itm_draco,itm_wrapping_boots,itm_ankle_boots,itm_simple_shoes,itm_linen_shirt_1,itm_linen_shirt_2,itm_linen_shirt_3,itm_linen_shirt_10,itm_linen_shirt_13,itm_linen_shirt_14,itm_steppe_horse,itm_warhorse],
   def_attrib_lvl_18|level(18),wp_two_handed(160) | wp_polearm(160),knows_common|knows_ironflesh_8|knows_athletics_4|knows_power_strike_5|knows_riding_5,man_face_1, man_face_2],

  ["mercenaries_end","mercenaries_end","mercenaries_end",0,no_scene,reserved,fac_commoners,
   [],
   def_attrib|level(4),wp(60),knows_common,man_face_1, man_face_2],

  ["hornman","Hornman","Hornmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_horn,itm_fighting_axe,itm_javelin]+shoes_generic+tunics_generic, #weaker gear so they aren't just walking tanks
   def_attrib_lvl_18|level(18),wp(130),knows_common|knows_ironflesh_2|knows_athletics_6|knows_power_strike_2|knows_power_throw_2,man_face_1, man_face_2],

#Proto-west Germanic
#oh boy, proto-west germanic names is gonna suck
#jo / jan - used to make a verb into an agent now - to hunt, hunter for example
#mann / manni - man
#Druhtinaz / Druhtinoz - leader/lord
#Gagado / Gagadan - Companion
#Gawjamann / Gawjamanni - small freeholder, yeoman, villager
#Daropu / Daropo - light spear, javelin, dart could be used for skirmishers?? daropo-mann, therefore possibily daropujo or daropumann
#Bogo / Bogan - bow, therefore bogomann (hehe it sounds silly)
#Aipastabas / Aipastabo - oath/oath-making
#Asni / Asnijos - worker/laborer
#Erlas / Erlo  - noble
#ehwas / ehwo - horse, can be used later?
#Haitijini / Haitijano - leader
#Halip / Halipo - hero
#Harjas / Harjo - army
#Harjatogo / Harjatogan - army leader, commander, general
#Hero / Heriwo - sword/dagger
#hirdijas / hirdijo - herdsman
#Jagonjo / Jagonjan - hunter, based off the construction of jagon (to hunt) and jo - which forms and agent noun
#Kampijo / Kampijan - soldier (combat soldier?) - formed with kampijan (to fight) and jo
#kuning - king
#Wardamann / Wardamanni - watchman 
#Wigamann / Wigamanni - warrior/champion
#Sagi / Saggjo / Saggjos - retainer, warrior - baro / baran, can also be servant/warrior or freeman as well, seems to sound similar to baron, probably developed into it
#Skalk / Skalkos - retainer, servant, even more with pegn / pegno (the weird germanic letter in front lol)
#Skakari / Skakarijo - robber
#Skeldu / Skeldiwi - shield 
#Ward / Wardo / Wardos - guard
#Maki / Makijo - sword - makimann (swordsman?) even better, didn't notice swerd/swerdu therefore a better sounding Swerdmann
#Hross / Hrossu - horse - hrossmann?
#Pik / Piko - pikmann? (pikeman?)
#Fot / Foti - fotmann? (footman?)
#Gair / Gairo - Gairmann (spearman?)
#Garafijo - Garafijan - count, officer, earl, etc?
#Akusi - axe, Akusimann?
#Jugunthi - youth(s)? 

#Gothic
#More gothic nonsense - ur (sing) -> ureis (pl)
#Gawaliths (pl. Gawalidai)
#Mekja / Mekjans - swordsman/men
#skalks - slave / Baurgja - citizen / Baurgjans - citizens
#aurtja - tenant farmer
#asneis laborer
#gardawaldands - master of the house?
#daurawards - gatekeeper
#kindins - governor
#ragineis - advisor
#hairdeis / hairdjos - herdsman
#waidedja - theif, bandit
#wardja - guard
#wilwa - robber, bandit
#ferja - spy
#spaikulatur - speculator, guard, sentinel (scout?)
#junda / jundos - youth
#galaista - follower
#gahlaiba / gahlaibans - companion, comrade
#gaman / gamana - also companion
#gajuka / gajukans - specifically male companion
#siponeis / siponjos - follower, student, could be used to refer to a companion
#haurnja / haurnjans - hornman
#guma / gumans - man(kind?)
#manna / mans - man
#fralets / fraletos - freeman
#ufarswara / ufarswarans - oathbreaker
#Waithja - hunter
#Druhtinaz - leader/lord
#Marhs - horse
#Skildja / Skildjans - shieldman (shieldbearer) - not entirely perfect

#Vandallic is interesting, as an east germanic language it will be similar to gothic in several ways. Gothic terms may be substituted if I can't try and recreate them
#Manna/Mans is man
#ja/jans is used to make a verb into an agent noun for gothic
#Ari - manna, ari = army, manna = man, therefore armyman or warrior
#Arimanna/Arimans (Soldier/Infantry)
#Geismanna/Geismans (spearman)
#Teus (slave)
#Triouamanna/Triouamans (Literally, loyal man or what can be described as companion or oathtaker)
#Gundaja/Gundajans - to battle + ja = warrior
#Munds - defender
#Ricus-munds (King defender, or kings-guard?)
#Baudes - master

#Constructing old frankish (used between the 4th-8th centuries) - some units will use late latin or latin terms to reflect roman influence on the franks
#extremely limited words known, mostly inferred through the advancement of proto-western germanic to old dutch, old frisian and old saxon
#more details here: have to check the sources but this is a mod, not a research paper: https://en.wiktionary.org/wiki/Wiktionary:About_Frankish
# - o added to similar fashion as proto-western jo, found in old dutch

#now for the words - frankish, direct words from it
#Miles Antrustio / Milites Antrustiones
#Baro - freeman, servant, warrior, from proto-western germanic
#Dubbano / Dubban(o)? - still figuring this out, old frankish for to strike
#wardon - to guard, protect - still figuring this out
#wrakkijo - mercenary, servant which was taken and used in the late/medieval latin word garcio (which means mercenary, servant, assassin, knave depending on context)
#marhskalk - aka horse servant 
#riki - rich, could be combined with other terms to mean "noble" then x
#treuwa - loyalty, agreement

#Frankish words inferred from Old Dutch and proto-western germanic
#Druhtin - Lord
#Kempo - fighter, warrior - similar to proto-western germanic kampijan
#Heritogo - army leader, similar to harajutga, harjatogo - useful for seeing how it derrived from proto-western germanic
#Mordth (morth?) - murderer
#swert - sword
#ger - spear, shared by both old saxon, dutch and frisian, likely the word for spear for the franks
#Ridan - to ride, therefore ridano?
#bogo - bow
#man, manna, its man lol
#ambahtman - service/servant (ambaht) + man, therefore servant/retainer -- would be better to use ambaht
#skilt - shield
#herro - master, lord - can see how it turns into the modern german word herr (sir?)
#dragan - to carry, shared with proto-western, therefore skiltdragano ("literally shield-bearer"), and I can try a swertdragano (literally "sword-bearer", similar to the latin spatharius, "spatha-bearer" which was a late roman guardsman title)
#lito - half-free serf? worked for lord but was not owned by a lord - mentioned in salic law compiled in 500, so less than 50 years after the mod takes place

#For the W. German troops
#Freeman -> Retainer -> Companion
#Skirmisher (latin, iuvenis) - Jugunthi
#Freeman - (latin, armatus) - Karli / Karlo ?
#Foot Comitatus/Retainer (probably better term) - (latin, optimati) - Sagi / Sagjo
#Mounted Comitatus/Companion - (latin, regales) - Herthganauti / Herthganauto

#E. German
#Freeman -> Retainer
#Skirmiser -> Mounted Skirmisher
#Mounted Warrior -> Mounted Companion
#Freeman (spearman?) - Gaizamanna / Gaizamans
#Retainer - Hairumanna / Hairumans
#Skirmisher - Junga / Jungans
#Mounted Skirmisher - Aihwamanna / Aihwamans
#Mounted Warrior - Aihwadrauhteis / Aihwardrauhtjos
#Mounted Companion - Athalings / Athalingos

#N Germanic
#still gotta figure out sng vs plural
#Freeman - Kotsetla / Kotsetlas? - or just use Duguthi?, herimannus? :http://www.koeblergerhard.de/as/4A/as_ne.html
#Warrior - Duguthi
#Skirmisher - Juguthi 
#Retainer/Foot Comitatus - Gasitho / Gasithos - could always use Herthganauto / Herthganautos?
#Mounted Warrior/Rider - Hrossmanna / Hrossmanni

#Gothic
#got a lot from here: https://www.twcenter.net/forums/showthread.php?681857-INVASIO-BARBARORVM-III/page9
#for "freeman" : https://germanic.ge/en/got/word/freis/ - masculine nominative
#Freeman -> Veteran/Warrior
#Skirmisher -> Mounted Skirmisher
#Mounted Warrior -> Mounted Companion (Comitatus)
#Freeman - Frijis / Frijai
#Veteran/Warrior - Gadrauhts / Gadrauhteis
#Skirmisher - Junga / Jungans
#Mounted Skirmisher (Scout?) - Spaikulatur / Spaikulatureis
#Mounted Warrior (will use just horseman?) - Aihvja / Aihvjans
#Mounted Comitatus (will just use companion) - Gasinthja / Gasinthjans - relates to later gothic (latinized) term Gardingos/Gardingi?

#Crimean Goth/Tetraxitae
#Skirmisher -> Mounted Skirmisher
#Freeman -> Warrior, Foot Comitatus, Retainer, etc...
#Mounted Warrior/Horseman -> Mounted Companion (Comitatus)
#Freeman - Frijis / Frijai
#Veteran/Warrior - Gadrauhts / Gadrauhteis
#Skirmisher - Junga / Jungans
#Mounted Skirmisher (Scout?) - Spaikulatur / Spaikulatureis
#Mounted Warrior (will use just horseman?) - Aihvja / Aihvjans
#Mounted Comitatus (will just use companion) - Gasinthja / Gasinthjans - relates to later gothic (latinized) term Gardingos/Gardingi?

#Sassanids:
#Cavalry
#Savaran/Aswaran - professional heavy cavalry (lance, sword/mace) 
#Janseparan - roman deserters/mercs/volunteers (lance, sword, shield?)
#Pustigban - emperor's personal heavy cavalry (cataphract) - only recruitable with high relations to shah or as shah start
#Infantry
#levy paighan -> prof. paighan -> heavy (armored) paighan - hoplite?
#equipped with axe (lower tier), mace (higher tier), spear, wicker shield, helmet, mail for higher tier troops
#daylamites - sword, shield, battle axe, generallt well equipped compared to the generic paighan
#Skirmisher - Selmandan 
#Archer - Kamanadar/ Kamanadaran
  
#GOTHS
  ["gothic_freeman","Gothic Freeman (Frijis)","Gothic Freemen (Frijai)",tf_guarantee_basic,0,0,fac_culture_1,
   [itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_tunic_long_pants_5,itm_tunic_long_pants_6,itm_tunic_long_pants_11,itm_khergit_leather_boots,itm_medium_spear_3,itm_medium_spear_4,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_roman_spear_1,itm_roman_spear_2,itm_medium_spear_2,itm_seax_8,itm_seax_1,itm_basic_axe,itm_fighting_axe,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_ridge_helm_c,itm_narona_bandhelm_cloth]+tunics_goths+shoes_generic+hats_goth+shields_gothic_1+shields_generic+cloaked_tunics_gothic,
   def_attrib_lvl_18|level(18),wp_one_handed(170)|wp_two_handed(150)|wp_polearm(180)|wp_throwing(160)|wp_archery(100),knows_lvl_18_inf|knows_shield_4|knows_power_strike_4,germanic_face_1, germanic_face_2],

  ["gothic_footman","Gothic Footman (Gadrauhts)","Gothic Footmen (Gadrauhteis)",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_1,
   [itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_khergit_leather_boots,itm_tab_shield_round_d,itm_cloaked_tunic_pants_3,itm_leather_armor_c,itm_generic_subarmalis_1,itm_generic_subarmalis_2,itm_short_ragged_mail_3,itm_short_ragged_mail_10,itm_mid_generic_mail_1,itm_mid_generic_mail_2,itm_mid_generic_mail_7,itm_mid_generic_mail_9,itm_mid_generic_mail_22,itm_rich_mail_5,itm_rich_mail_6,itm_rich_mail_11,
   itm_intercisa_helmet_1,itm_augst_helmet_1,itm_intercisa_helmet_2,itm_burgh_helmet_1,itm_burgh_helmet_mail,itm_ridge_helm_c,itm_koblenz_helmet_1,itm_fernpass_helmet_1,itm_fernpass_helmet_2,itm_fernpass_helmet_3,itm_christies_helmet_1,itm_iatrus_1,itm_war_spear,itm_poleaxe,itm_roman_spear_3,itm_late_roman_spear_1,itm_long_seax_4,itm_long_seax_5,itm_long_seax_2,itm_sword_medieval_c,itm_sword_viking_1]+shoes_generic+tunics_goths_noble+shields_gothic_2+cloaked_tunics_gothic,
   def_attrib_lvl_23|level(23),wp_one_handed(200)|wp_two_handed(170)|wp_polearm(210)|wp_throwing(190)|wp_archery(100),knows_lvl_23_inf|knows_shield_4|knows_power_strike_6,germanic_face_1, germanic_face_2],

  ["gothic_skirmisher","Gothic Skirmisher (Junga)","Gothic Skirmishers (Jungans)",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_culture_1,
   [itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,itm_khergit_leather_boots,itm_javelin,itm_javelin,itm_wooden_javelin,itm_wooden_javelin,itm_wooden_spear,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_new_hood_a,itm_new_hood_e,itm_brown_hood1,itm_seax_8]+tunics_goths+shields_simple+hats_goth+shoes_generic,
   def_attrib_skirmisher|level(13),wp_one_handed(130)|wp_two_handed(90)|wp_polearm(130)|wp_archery(140)|wp_throwing(150),knows_skirmisher,germanic_face_1, germanic_face_2],

  ["gothic_bowman","Gothic Bowman (Bugamanna)","Gothic Bowmen (Bugamans)",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_culture_1,
   [itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_khergit_leather_boots,itm_long_seax_4,itm_short_bow,itm_hunting_bow,itm_strong_bow,itm_roman_arrows_2,itm_roman_arrows_2,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_new_hood_a,itm_new_hood_e,itm_brown_hood1]+tunics_goths+hats_goth+shoes_generic,
   def_attrib_lvl_18|level(17),wp_one_handed(150)|wp_two_handed(140)|wp_polearm(160)|wp_archery(160)|wp_throwing(130),knows_archer,germanic_face_1, germanic_face_2],

  ["gothic_mounted_skirmisher","Gothic Scout (Spaikulatur)","Gothic Scout (Spaikulatureis)",tf_mounted|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_culture_1,
   [itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_khergit_leather_boots,itm_cavalry_javelins,itm_cavalry_javelins,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_new_hood_a,itm_new_hood_e,itm_brown_hood1,itm_fighting_axe,itm_roman_spear_3]+tunics_goths+horses_1+hats_goth+shoes_generic+shields_small,
   def_attrib_lvl_18|level(18),wp_one_handed(170)|wp_two_handed(100)|wp_polearm(180)|wp_throwing(180)|wp_archery(140),knows_lvl_18_cav|knows_shield_1|knows_power_strike_3|knows_power_throw_6,germanic_face_1, germanic_face_2],

  ["gothic_horseman","Gothic Horseman (Aihvja)","Gothic Horsemen (Aihvjans)",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_culture_1,
   [itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_khergit_leather_boots,itm_tab_shield_small_round_c,itm_tab_shield_small_round_b,itm_cloaked_tunic_pants_3,itm_koblenz_helmet_1,itm_fernpass_helmet_3,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_ridge_helm_c,itm_burgh_helmet_1,itm_fernpass_helmet_1,itm_iatrus_1,itm_burgh_helmet_mail,itm_narona_bandhelm_mail,itm_christies_helmet_1,itm_augst_helmet_1,itm_roman_spear_3,itm_sword_viking_2,itm_sword_viking_3]+shields_gothic_cavalry_1+horses_germanic_1+horses_germanic_2+tunics_goths_noble+shoes_generic+cloaked_tunics_gothic,
   def_attrib_lvl_23|level(23),wp_one_handed(210)|wp_two_handed(170)|wp_polearm(210)|wp_throwing(190)|wp_archery(100),knows_lvl_23_cav|knows_shield_3|knows_power_strike_6,germanic_face_1, germanic_face_2],

  ["gothic_companion","Gothic Companion (Gasinthja)","Gothic Companions (Gasinthjans)",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_culture_1,
   [itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_khergit_leather_boots,itm_tab_shield_small_round_c,itm_mid_generic_mail_1,itm_mid_generic_mail_2,itm_mid_generic_mail_9,itm_mid_generic_mail_13,itm_mid_generic_mail_22,itm_rich_mail_1,itm_rich_mail_2,itm_rich_mail_3,itm_long_mail_new_1,itm_long_mail_new_5,itm_medium_scale_1,itm_medium_scale_3,itm_koblenz_helmet_1,itm_christies_helmet_1,itm_koblenz_helmet_2,itm_burgh_helmet_1,itm_burgh_helmet_2,itm_fernpass_helmet_2,itm_koblenz_helmet_3,itm_augsburg_1_helmet,itm_intercisa_helmet_gilded_1,itm_iatrus_1,itm_iatrus_2,itm_concesti_helmet,itm_heteny_helmet_1,itm_heavy_lance,itm_sword_viking_2,itm_sword_viking_3]+horses_germanic_3+shoes_generic+shields_gothic_cavalry_2,
   def_attrib_lvl_28|level(28),wp_one_handed(240)|wp_two_handed(220)|wp_polearm(240)|wp_throwing(200)|wp_archery(100),knows_lvl_28_cav|knows_shield_3|knows_power_strike_7,germanic_face_1, germanic_face_2],

  ["gothic_messenger","Gothic Messenger (Airus)","Gothic Messengers (Airus)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_culture_1,
   [itm_narona_bandhelm_mail,itm_sword_viking_2,itm_cavalry_javelins]+tunics_goths+horses_2+shoes_generic,
   def_attrib_lvl_23|level(25),wp(230),knows_common|knows_riding_7|knows_horse_archery_5,germanic_face_1, germanic_face_2],
  ["gothic_deserter","Gothic Deserter","Gothic Deserters",tf_guarantee_basic,0,0,fac_culture_1,
   [itm_medium_spear_3,itm_medium_spear_4,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_roman_spear_1,itm_roman_spear_2,itm_medium_spear_2,itm_seax_8,itm_seax_1,itm_ridge_helm_c,itm_iatrus_helmet_light,itm_iatrus_helmet_mail,itm_narona_bandhelm_leather]+tunics_goths+shoes_generic+hats_goth+shields_gothic_1+shields_generic,
   def_attrib_lvl_18|level(17),wp_one_handed(170)|wp_two_handed(150)|wp_polearm(180)|wp_throwing(160)|wp_archery(100),knows_lvl_18_inf|knows_shield_4|knows_power_strike_4,germanic_face_1, germanic_face_2],
  ["gothic_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_1,
   [itm_tab_shield_round_d,itm_leather_gloves,itm_koblenz_helmet_1,itm_short_ragged_mail_10,itm_sword_viking_3]+shoes_generic,
   def_attrib_lvl_28|level(26),wp(230),knows_common|knows_athletics_4|knows_power_strike_5|knows_ironflesh_5|knows_shield_5,germanic_face_1, germanic_face_2],
  ["gothic_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_1,
   [itm_tab_shield_round_d,itm_leather_gloves,itm_koblenz_helmet_1,itm_short_ragged_mail_10,itm_sword_viking_3]+shoes_generic,
   def_attrib_lvl_28|level(26),wp(230),knows_common|knows_athletics_4|knows_power_strike_5|knows_ironflesh_5|knows_shield_5,germanic_face_1, germanic_face_2],

#AOR GOTHIC
#gepids
  ["iuthungi_scout","Iuthungi Scout","Iuthungi Scouts",tf_mounted|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_culture_1,
   [itm_cavalry_javelins,itm_cavalry_javelins,itm_late_roman_spear_1,itm_fighting_axe,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_generic_tunic_2,itm_generic_tunic_6,itm_generic_tunic_9,itm_linen_shirt_7,itm_linen_shirt_8,itm_simple_tunic_7,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_new_hood_a,itm_new_hood_e,itm_brown_hood1]+horses_germanic_1+shoes_generic+shields_small,
   def_attrib_lvl_18|level(19),wp_one_handed(180)|wp_two_handed(100)|wp_polearm(190)|wp_throwing(200)|wp_archery(140),knows_lvl_18_cav|knows_power_strike_3|knows_horse_archery_5,germanic_face_1, germanic_face_2],
  ["sadages_horse_archer","Sadages Horse Archer","Sadages Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_culture_1,
   [itm_nomad_boots,itm_simple_shoes,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_leather_steppe_cap_a,itm_hunnic_phrygian_leather,itm_steppe_kaftan_3,itm_khergit_vest_b,itm_leather_vest,itm_khergit_bow,itm_roman_spear_3,itm_roman_arrows_1,itm_roman_arrows_1]+horses_hunnic_1,
   def_attrib_lvl_18|level(17),wp_one_handed(150)|wp_two_handed(140)|wp_polearm(160)|wp_throwing(140)|wp_archery(160),knows_common|knows_riding_5|knows_horse_archery_5|knows_power_strike_1|knows_power_draw_4|knows_ironflesh_2,hunnic_face_1, hunnic_face_2],
  ["sadagarii_horseman","Sadagarii Horseman","Sadagarii Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_polearm,0,0,fac_culture_1,
   [itm_nomad_boots,itm_simple_shoes,itm_steppe_kaftan_2,itm_khergit_vest_a,itm_leather_vest,itm_roman_spear_4,itm_jarid,itm_jarid]+horses_hunnic_1,
   def_attrib_lvl_18|level(18),wp_one_handed(160)|wp_two_handed(140)|wp_polearm(180)|wp_throwing(180)|wp_archery(140),knows_common|knows_riding_5|knows_horse_archery_5|knows_power_strike_3|knows_power_throw_5|knows_ironflesh_4,hunnic_face_1, hunnic_face_2],
  ["victufali_mounted_warrior","Victufali Mounted Warrior","Victufali Mounted Warrior",tf_mounted|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_horse|tf_guarantee_polearm|tf_guarantee_shield,0,0,fac_culture_1,
   [itm_late_roman_spear_1,itm_sword_viking_3,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_1,itm_generic_tunic_4,itm_generic_tunic_11,itm_generic_tunic_12,itm_linen_shirt_3,itm_cloaked_tunic_9,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_woolen_cap_2,itm_generic_leather_helmet_cloth]+horses_germanic_2+shoes_generic+shields_small,
   def_attrib_lvl_23|level(21),wp_one_handed(210)|wp_two_handed(100)|wp_polearm(210)|wp_throwing(190)|wp_archery(140),knows_lvl_23_cav|knows_power_strike_5|knows_shield_4,germanic_face_1, germanic_face_2],
  ["daco_roman_militia","Miles Daco-Romani","Milites Daco-Romani",tf_guarantee_basic,0,0,fac_culture_1, #club, spear, oval shield
   [itm_roman_spear_1,itm_late_roman_spear_2,itm_throwing_spear_2,itm_throwing_spear_2,itm_winged_mace,itm_wrapping_boots,itm_khergit_leather_boots,itm_roman_military_tunic_8,itm_generic_tunic_15,itm_linen_shirt_12,itm_roman_shirt_8,itm_roman_shirt_10,itm_roman_subarmalis_new_8,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_woolen_cap_1,itm_woolen_cap_5,itm_intercisa_helmet_1,itm_augst_helmet_1,itm_oval_shield_blue_2,itm_oval_shield_orange_1]+shoes_roman,
   def_attrib_lvl_18|level(17),wp_one_handed(170)|wp_two_handed(160)|wp_polearm(180)|wp_archery(110)|wp_throwing(160),knows_lvl_18_inf|knows_shield_5|knows_power_strike_3,roman_face_1, roman_face_2],
#amali goths (ostrogoths)
  ["alpidzuri_rider","Alpidzuri Rider","Alpidzuri Riders",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_culture_1,
   [itm_nomad_boots,itm_simple_shoes,itm_sassanid_cavalry_boots_1,itm_skirmisher_tunic_1,itm_skirmisher_tunic_3,itm_kaftan_sheepskin_1,itm_kaftan_sheepskin_4,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_hunnic_phrygian_leather,itm_long_seax_5,itm_khergit_bow,itm_khergit_arrows,itm_khergit_arrows]+horses_hunnic_1+horses_hunnic_2,
   def_attrib_lvl_18|level(17),wp_one_handed(170)|wp_two_handed(140)|wp_polearm(140)|wp_throwing(140)|wp_archery(160),knows_common|knows_ironflesh_1|knows_power_strike_3|knows_riding_4|knows_horse_archery_6|knows_power_draw_5,hunnic_face_1, hunnic_face_2],
  ["tuncarsi_mounted_skirmisher","Tuncarsi Mounted Skirmisher","Tuncarsi Mounted Skirmishers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_culture_1,
   [itm_nomad_boots,itm_simple_shoes,itm_sassanid_cavalry_boots_1,itm_skirmisher_tunic_4,itm_kaftan_tunic_10,itm_kaftan_tunic_6,itm_kaftan_tunic_7,itm_kaftan_sheepskin_6,itm_hunnic_phrygian_1,itm_hunnic_phrygian_4,itm_hunnic_phrygian_5,itm_hunnic_phrygian_leather,itm_medium_spear_3,itm_cavalry_javelins,itm_cavalry_javelins]+shields_simple+shields_small+horses_hunnic_1,
   def_attrib_lvl_18|level(18),wp_one_handed(160)|wp_two_handed(140)|wp_polearm(180)|wp_throwing(200)|wp_archery(140),knows_common|knows_ironflesh_2|knows_power_strike_2|knows_riding_5|knows_horse_archery_5|knows_power_throw_5,hunnic_face_1, hunnic_face_2],
  ["boisci_lancer","Boisci Lancer","Boisci Lancers",tf_mounted|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_horse|tf_guarantee_polearm|tf_guarantee_shield,0,0,fac_culture_1,
   [itm_warhorse,itm_heavy_lance,itm_sword_khergit_2,itm_kaftan_alan_3,itm_kaftan_alan_4,itm_kaftan_alan_2,itm_old_spangenhelm_2,itm_tarasovsky_1784_helmet_mail_2,itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2]+horses_germanic_3,
   def_attrib_lvl_23|level(21),wp_one_handed(200)|wp_two_handed(100)|wp_polearm(220)|wp_throwing(190)|wp_archery(140),knows_lvl_23_cav|knows_power_strike_7|knows_shield_2,sarmatian_face_1, sarmatian_face_2],

  ["ostrogoth_guard","Amali Guard (Saiones)","Amali Guards (Saiones)",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_culture_1,
   [itm_half_cataphract_horse_1,itm_half_cataphract_horse_2,itm_half_cataphract_horse_8,itm_khergit_leather_boots,itm_hunter_boots,itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_2,itm_lombard_lamellar_2,itm_rich_mail_1,itm_rich_mail_2,itm_rich_mail_5,itm_mid_generic_mail_7,itm_mid_generic_mail_9,itm_long_mail_new_1,itm_fernpass_helmet_2,itm_concesti_helmet,itm_heteny_helmet_1,itm_iatrus_2,itm_christies_helmet_1,itm_christies_helmet_crest_2,itm_heavy_lance,itm_pannonhalma_spatha,itm_tab_shield_small_round_c,itm_tab_shield_round_e],
   def_attrib_lvl_30|level(30),wp_one_handed(250)|wp_two_handed(250)|wp_polearm(250)|wp_throwing(200)|wp_archery(100),knows_lvl_30_cav|knows_shield_5|knows_power_strike_8,germanic_face_1, germanic_face_2],

#balthi goths
  ["roxolani_horseman","Roxolani Horseman","Roxolani Horsemen",tf_mounted|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_horse|tf_guarantee_polearm|tf_guarantee_helmet,0,0,fac_culture_1,
   [itm_warhorse,itm_eastern_scale_1,itm_sassanid_cavalry_boots_1,itm_mid_generic_mail_20,itm_coat_of_plates_red,itm_narona_bandhelm_mail,itm_christies_helmet_1,itm_sword_khergit_2,itm_long_lance,itm_strong_bow,itm_roman_arrows_2],
   def_attrib_lvl_23|level(23),wp_one_handed(210)|wp_two_handed(100)|wp_polearm(230)|wp_throwing(180)|wp_archery(150),knows_lvl_23_cav|knows_power_strike_5|knows_horse_archery_4,sarmatian_face_1, sarmatian_face_2],

  ["visigoth_guard","Balthi Guard (Gardingi)","Balthi Guards (Gardingi)",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_culture_1,
   [itm_half_cataphract_horse_3,itm_half_cataphract_horse_4,itm_half_cataphract_horse_7,itm_khergit_leather_boots,itm_hunter_boots,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_rich_mail_3,itm_rich_mail_4,itm_rich_mail_6,itm_rich_mail_7,itm_long_mail_new_2,itm_medium_scale_1,itm_medium_scale_5,itm_fernpass_helmet_2,itm_heteny_helmet_1,itm_iatrus_2,itm_iatrus_plume_2,itm_christies_helmet_1,itm_christies_helmet_crest_1,itm_augsburg_2_helmet,itm_long_lance,itm_sword_viking_3,itm_jarid,itm_tab_shield_small_round_c,itm_tab_shield_round_e],
   def_attrib_lvl_30|level(30),wp_one_handed(250)|wp_two_handed(230)|wp_polearm(260)|wp_throwing(260)|wp_archery(100),knows_lvl_30_cav|knows_shield_5|knows_power_strike_8,germanic_face_1, germanic_face_2],

#rugii
  ["baiuvari_armati","Armatus Baiuvari","Armati Baiuvari",tf_guarantee_basic,0,0,fac_culture_1,
   [itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_3,itm_generic_tunic_7,itm_generic_tunic_13,itm_generic_tunic_15,itm_linen_shirt_1,itm_cloaked_generic_tunic_7,itm_cloaked_tunic_5,itm_cloaked_tunic_8,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_woolen_cap_1,itm_woolen_cap_3,itm_round_shield_blue_2,itm_round_shield_blue_3,itm_round_shield_germanic_14,itm_round_shield_gray_1,itm_throwing_spear_2,itm_battle_axe_3,itm_long_seax_4,itm_seax_2,itm_late_roman_spear_1]+shoes_generic+hats_german+shields_generic,
   def_attrib_lvl_18|level(17),wp_one_handed(180)|wp_two_handed(150)|wp_polearm(180)|wp_throwing(190)|wp_archery(100),knows_lvl_18_inf|knows_shield_4|knows_power_strike_4,germanic_face_1, germanic_face_2],

#ERE?
  ["moesian_goth","Moesian Gothic Footman","Moesian Gothic Footmen",tf_guarantee_basic,0,0,fac_culture_1,
   [itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,itm_khergit_leather_boots,itm_generic_tunic_11,itm_generic_tunic_8,itm_generic_tunic_1,itm_generic_tunic_3,itm_roman_shirt_5,itm_roman_shirt_10,itm_short_roman_mail_1,itm_roman_subarmalis_new_4,itm_late_roman_spear_1,itm_late_roman_spear_2,itm_sword_khergit_3,itm_long_seax_1,itm_round_shield_germanic_1,itm_round_shield_germanic_13,itm_round_shield_germanic_16,itm_round_shield_roman_1,itm_round_shield_roman_13,itm_round_shield_germanic_22,
   itm_narona_bandhelm_leather,itm_narona_bandhelm_mail,itm_intercisa_helmet_1,itm_augst_helmet_1,itm_intercisa_helmet_2,itm_ridge_helm_c,itm_iatrus_1,itm_christies_helmet_1,itm_woolen_cap_1,itm_woolen_cap_2,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_pannonian_cap_4,itm_pannonian_cap_5]+shoes_generic,
   def_attrib_lvl_20|level(20),wp_one_handed(190)|wp_two_handed(150)|wp_polearm(200)|wp_throwing(160)|wp_archery(100),knows_lvl_18_inf|knows_shield_4|knows_power_strike_5,germanic_face_1, germanic_face_2],

#EASTERN GERMANIC
  ["eastern_germanic_spearman","E. Germanic Spearman (Gaizamanna)","E. Germanic Spearmen (Gaizamans)",tf_guarantee_basic,0,0,fac_culture_2,
   [itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_woolen_cap,itm_woolen_cap_b,itm_woolen_cap_3,itm_woolen_cap_6,itm_tunic_long_pants_6,itm_tunic_long_pants_7,itm_tunic_long_pants_11,itm_germanic_cap_1,itm_germanic_cap_2,itm_brown_hood1,itm_new_hood_b,itm_new_hood_d,itm_medium_spear_3,itm_medium_spear_1,itm_spear,itm_basic_axe,itm_fighting_axe,itm_battle_axe_1,itm_seax_9,itm_throwing_spear_1,itm_throwing_spear_1,itm_ridge_helm_c,(itm_intercisa_helmet_1,imod_battered),(itm_intercisa_helmet_2,imod_battered),(itm_augst_helmet_1,imod_battered),itm_leather_cap,itm_iatrus_helmet_light,itm_iatrus_helmet_mail]+tunics_eastern_germanic+shoes_generic+shields_eastern_germanic_1+shields_generic+cloaked_tunics_eastern_germanic,
   def_attrib_lvl_18|level(17),wp_one_handed(160)|wp_two_handed(150)|wp_polearm(170)|wp_throwing(170)|wp_archery(100),knows_lvl_18_inf|knows_shield_4|knows_power_strike_4,germanic_face_1, germanic_face_2],

  ["eastern_germanic_retainer","E. Germanic Retainer (Hairumanna)","E. Germanic Retainers (Hairumans)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_culture_2, #no guaranteed polearm
   [itm_tab_shield_round_d,itm_leather_armor_d,itm_generic_subarmalis_6,itm_short_ragged_mail_1,itm_short_ragged_mail_6,itm_short_ragged_mail_12,itm_mid_generic_mail_23,itm_mid_generic_mail_26,itm_mid_generic_mail_28,itm_rich_mail_6,itm_rich_mail_7,itm_rich_mail_11,itm_augst_helmet_1,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_koblenz_helmet_light_old,itm_fernpass_helmet_1,itm_fernpass_helmet_3,itm_burgh_helmet_mail,itm_burgh_helmet_light,itm_sword_medieval_c,itm_seax_9,itm_long_seax_2,itm_polehammer,itm_throwing_spear_3,itm_throwing_spear_3]+shoes_generic+shields_eastern_germanic_2+cloaked_tunics_eastern_germanic,
   def_attrib_lvl_23|level(23),wp_one_handed(210)|wp_two_handed(170)|wp_polearm(190)|wp_throwing(190)|wp_archery(100),knows_lvl_23_inf|knows_shield_4|knows_power_strike_6,germanic_face_1, germanic_face_2],

  ["eastern_germanic_skirmisher","E. Germanic Skirmisher (Junga)","E. Germanic Skirmishers (Jungans)",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_culture_2,
   [itm_javelin,itm_javelin,itm_wooden_javelin,itm_wooden_javelin,itm_wooden_spear,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_woolen_cap,itm_woolen_cap_b,itm_woolen_cap_3,itm_woolen_cap_6,itm_germanic_cap_1,itm_germanic_cap_2,itm_brown_hood1,itm_new_hood_b,itm_new_hood_d,itm_hatchet]+tunics_eastern_germanic+shields_simple+shoes_generic,
   def_attrib_lvl_13|level(13),wp_one_handed(120)|wp_two_handed(90)|wp_polearm(110)|wp_archery(150)|wp_throwing(160),knows_skirmisher,germanic_face_1, germanic_face_2],

  ["eastern_germanic_bowman","E. Germanic Bowman (Bugamanna)","E. Germanic Bowmen (Bugamans)",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_culture_2,
   [itm_short_bow,itm_hunting_bow,itm_strong_bow,itm_long_bow,itm_germanic_arrows,itm_germanic_arrows,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_woolen_cap,itm_woolen_cap_b,itm_woolen_cap_3,itm_woolen_cap_6,itm_germanic_cap_1,itm_germanic_cap_2,itm_brown_hood1,itm_new_hood_b,itm_new_hood_d,itm_fighting_axe]+tunics_eastern_germanic+shields_simple+shoes_generic,
   def_attrib_lvl_18|level(17),wp_one_handed(150)|wp_two_handed(130)|wp_polearm(150)|wp_archery(170)|wp_throwing(160),knows_archer,germanic_face_1, germanic_face_2],

  ["eastern_germanic_mounted_skirmisher","E. Germanic Mounted Skirmisher (Aihwamanna)","E. Germanic Mounted Skirmishers (Aihwamans)",tf_mounted|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_culture_2,
   [itm_cavalry_javelins,itm_cavalry_javelins,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_woolen_cap,itm_woolen_cap_b,itm_woolen_cap_3,itm_woolen_cap_6,itm_germanic_cap_1,itm_germanic_cap_2,itm_brown_hood1,itm_new_hood_b,itm_new_hood_d,itm_fighting_axe,itm_medium_spear_3]+tunics_eastern_germanic+horses_germanic_1+shoes_generic+shields_small+shields_simple,
   def_attrib_lvl_18|level(17),wp_one_handed(160)|wp_two_handed(100)|wp_polearm(170)|wp_throwing(190)|wp_archery(130),knows_lvl_18_cav|knows_shield_1|knows_power_strike_4|knows_horse_archery_4,germanic_face_1, germanic_face_2],

  ["eastern_germanic_mounted_warrior","E. Germanic Mounted Warrior (Aihwadrauhteis)","E. Germanic Mounted Warriors (Aihwardrauhtjos)",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_culture_2,
   [itm_tab_shield_small_round_c,itm_tab_shield_small_round_b,itm_leather_armor_d,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_woolen_cap,itm_woolen_cap_b,itm_woolen_cap_3,itm_woolen_cap_6,itm_germanic_cap_1,itm_germanic_cap_2,itm_brown_hood1,itm_new_hood_b,itm_new_hood_d,itm_fernpass_helmet_3,itm_burgh_helmet_mail,itm_burgh_helmet_light,itm_generic_leather_helmet_cloth,itm_ridge_helm_c,itm_intercisa_helmet_1,itm_intercisa_helmet_2,(itm_intercisa_helmet_1,imod_battered),itm_sword_viking_3,itm_battle_axe_2,itm_war_spear]+shields_eastern_germanic_cavalry_1+horses_germanic_2+shoes_generic+cloaked_tunics_eastern_germanic,
   def_attrib_lvl_23|level(23),wp_one_handed(200)|wp_two_handed(170)|wp_polearm(200)|wp_throwing(190)|wp_archery(100),knows_lvl_23_cav|knows_shield_3|knows_power_strike_6,germanic_face_1, germanic_face_2],

  ["eastern_germanic_companion","E. Germanic Companion (Athalings)","E. Germanic Companions (Athalingos)",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_culture_2,
   [itm_khergit_leather_boots,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_tab_shield_small_round_c,itm_mid_generic_mail_10,itm_mid_generic_mail_11,itm_mid_generic_mail_12,itm_mid_generic_mail_17,itm_mid_generic_mail_28,itm_long_mail_new_4,itm_long_mail_new_8,itm_medium_scale_2,itm_roman_squamata_5,itm_iatrus_1,itm_iatrus_2,itm_intercisa_helmet_gilded_1,itm_intercisa_helmet_gilded_2,itm_koblenz_helmet_1,itm_koblenz_helmet_2,itm_burgh_helmet_1,itm_burgh_helmet_2,itm_augsburg_2_helmet,itm_augsburg_2_helmet_mail,itm_fernpass_helmet_2,itm_concesti_helmet,itm_christies_helmet_1,itm_heavy_lance,itm_sword_viking_3,itm_battle_axe]+horses_germanic_3+shields_eastern_germanic_cavalry_2,
   def_attrib_lvl_28|level(28),wp_one_handed(240)|wp_two_handed(220)|wp_polearm(230)|wp_throwing(200)|wp_archery(100),knows_lvl_28_cav|knows_shield_3|knows_power_strike_7,germanic_face_1, germanic_face_2],

  ["eastern_germanic_messenger","E. Germanic Messenger (Airus)","E. Germanic Messengers (Airus)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_culture_2,
   [itm_ridge_helm_c,itm_sword_viking_3,itm_cavalry_javelins]+tunics_eastern_germanic+horses_2+shoes_generic,
   def_attrib_lvl_23|level(25),wp(230),knows_common|knows_riding_7|knows_horse_archery_5,germanic_face_1, germanic_face_2],
  ["eastern_germanic_deserter","E. Germanic Deserter","E. Germanic Deserters",tf_guarantee_basic,0,0,fac_culture_2,
   [itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_woolen_cap,itm_woolen_cap_b,itm_woolen_cap_3,itm_woolen_cap_6,itm_germanic_cap_1,itm_germanic_cap_2,itm_brown_hood1,itm_new_hood_b,itm_new_hood_d,itm_medium_spear_3,itm_medium_spear_1,itm_spear,itm_fighting_axe,itm_battle_axe_1,itm_seax_9,itm_ridge_helm_c,itm_throwing_spear_1,itm_throwing_spear_1,itm_generic_leather_helmet_cloth,itm_leather_cap,itm_iatrus_helmet_light,itm_iatrus_helmet_mail]+tunics_eastern_germanic+shoes_generic+shields_eastern_germanic_1+shields_generic,
   def_attrib_lvl_18|level(17),wp_one_handed(160)|wp_two_handed(150)|wp_polearm(170)|wp_throwing(170)|wp_archery(100),knows_lvl_18_inf|knows_shield_4|knows_power_strike_4,germanic_face_1, germanic_face_2],
  ["eastern_germanic_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_2,
   [itm_tab_shield_round_d,itm_leather_gloves,itm_short_ragged_mail_1,itm_sword_viking_3]+shoes_generic,
   def_attrib_lvl_28|level(26),wp(230),knows_common|knows_athletics_4|knows_power_strike_5|knows_ironflesh_5|knows_shield_5,germanic_face_1, germanic_face_2],
  ["eastern_germanic_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_2,
   [itm_tab_shield_round_d,itm_leather_gloves,itm_short_ragged_mail_1,itm_sword_viking_3]+shoes_generic,
   def_attrib_lvl_28|level(26),wp(230),knows_common|knows_athletics_4|knows_power_strike_5|knows_ironflesh_5|knows_shield_5,germanic_face_1, germanic_face_2],
  
#eastern germanic AOR
  #thuringians
  ["warenae_armatus","Armatus Waerne","Armati Waerne",tf_guarantee_basic,0,0,fac_culture_2,
   [itm_roman_lorum_fasciari_3,itm_khergit_leather_boots,itm_linen_shirt_13,itm_linen_shirt,itm_generic_tunic_10,itm_cloaked_generic_tunic_10,itm_cloaked_tunic_10,itm_cloaked_tunic_12,itm_woolen_cap_c,itm_woolen_cap_4,itm_germanic_cap_2,itm_germanic_cap_3,itm_new_hood_b,itm_brown_hood1,itm_throwing_spear_3,itm_mace_1,itm_seax_1,itm_long_seax_3,itm_medium_spear_3,itm_round_shield_yellow_1,itm_round_shield_gray_1,itm_round_shield_gray_2,itm_kerch_shield_wood,itm_kerch_shield_5,itm_kerch_shield_2]+shoes_generic+shields_basic,
   def_attrib_lvl_20|level(19),wp_one_handed(190)|wp_two_handed(150)|wp_polearm(190)|wp_throwing(180)|wp_archery(100),knows_lvl_18_inf|knows_shield_4|knows_power_strike_6,germanic_face_1, germanic_face_2],
  ["warenae_optimas","Optimas Waerne","Optimates Waerne",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_culture_2,
   [itm_roman_lorum_fasciari_3,itm_khergit_leather_boots,itm_cloaked_generic_tunic_10,itm_cloaked_tunic_10,itm_cloaked_tunic_12,itm_fernpass_helmet_1,itm_fernpass_helmet_2,itm_triveres_leather,itm_triveres_mail,itm_sword_viking_3,itm_sword_medieval_c,itm_concave_shield_germanic_4,itm_concave_shield_germanic_18,itm_kerch_shield_6,itm_kerch_shield_14,itm_kerch_shield_8]+shoes_generic+angons,
   def_attrib_lvl_23|level(23),wp_one_handed(220)|wp_two_handed(150)|wp_polearm(220)|wp_throwing(210)|wp_archery(100),knows_lvl_23_inf|knows_shield_5|knows_power_strike_7,germanic_face_1, germanic_face_2],

  ["thuringian_horseman","Thuringian Horseman (Aihwadrauhteis)","Thuringian Horsemen (Aihwardrauhtjos)",tf_mounted|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_culture_2,
   [itm_skirmisher_tunic_4,itm_cloaked_tunic_10,itm_leather_armor_c,itm_short_ragged_mail_6,itm_short_ragged_mail_10,itm_mid_generic_mail_27,itm_mid_generic_mail_2,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_brown_hood1,itm_new_hood_b,itm_new_hood_d,(itm_augst_helmet_1,imod_battered),(itm_intercisa_helmet_1,imod_battered),itm_intercisa_helmet_1,itm_fernpass_helmet_2,
   itm_polehammer,itm_lance,itm_sword_viking_3,itm_tab_shield_small_round_c,itm_thuringian_warhorse,itm_round_shield_gray_small_1,itm_round_shield_gray_small_2,itm_round_shield_germanic_small_10,itm_concave_shield_germanic_small_17,itm_concave_shield_germanic_small_20]+shoes_generic+horses_germanic_4,
   def_attrib_lvl_23|level(23),wp_one_handed(210)|wp_two_handed(200)|wp_polearm(220)|wp_throwing(180)|wp_archery(140),knows_athletics_5|knows_riding_8|knows_ironflesh_8|knows_power_throw_5|knows_weapon_master_8|knows_inventory_management_2|knows_shield_4|knows_power_strike_7,germanic_face_1, germanic_face_2],

  #lombards
  ["cynocephalus","Cynocephalus","Cynocephali",tf_guarantee_basic,0,0,fac_culture_2,
   [itm_nomad_boots,itm_simple_shoes,itm_wrapping_boots,itm_carbatinae_1_blue,itm_carbatinae_2_blue,itm_rawhide_coat3,itm_rawhide_coat6,itm_rawhide_coat7,itm_rawhide_coat8,itm_rawhide_coat9,itm_rawhide_coat10,itm_throwing_spears,itm_war_spear,itm_sword_viking_3,itm_round_shield_germanic_12,itm_round_shield_germanic_21],
   def_attrib_lvl_23|level(23),wp_one_handed (210) | wp_two_handed (230) | wp_polearm (220) | wp_archery (100) | wp_crossbow (120) | wp_throwing (190),knows_berserker,germanic_face_1, germanic_face_2],
  ["charudes_retainer","Charudes Retainer","Charudes Retainers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_culture_2,
   [itm_tab_shield_round_d,itm_cloaked_generic_tunic_3,itm_cloaked_generic_tunic_4,itm_mid_generic_mail_21,itm_mid_generic_mail_24,itm_fernpass_helmet_2,itm_fernpass_helmet_3,itm_triveres_mail,itm_burgh_helmet_mail,itm_burgh_helmet_light,itm_sword_viking_3,itm_round_shield_germanic_11,itm_round_shield_germanic_12,itm_round_shield_germanic_14,itm_round_shield_germanic_20]+shoes_generic+angons,
   def_attrib_lvl_28|level(28),wp_one_handed(220)|wp_two_handed(170)|wp_polearm(190)|wp_throwing(200)|wp_archery(100),knows_lvl_28_inf|knows_shield_6|knows_power_strike_7,germanic_face_1, germanic_face_2],

  ["langobard_retainer","Langobard Retainer (Gasind)","Langobard Retainers (Gasindii)",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm|tf_guarantee_horse,0,0,fac_culture_2,
   [itm_khergit_leather_boots,itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,itm_cloaked_tunic_8,itm_cloaked_tunic_9,itm_cloaked_tunic_5,itm_cloaked_generic_tunic_3,itm_generic_tunic_15,itm_generic_tunic_3,itm_leather_armor_e,itm_narona_bandhelm_mail,itm_iatrus_1,itm_iatrus_helmet_mail,itm_sword_medieval_c,itm_medium_spear_3,itm_round_shield_germanic_small_12,itm_round_shield_germanic_small_14,itm_round_shield_germanic_small_19,itm_concave_shield_germanic_small_22,itm_tab_shield_small_round_b]+horses_germanic_2+shoes_generic,
   def_attrib_lvl_23|level(23),wp_one_handed(210)|wp_two_handed(210)|wp_polearm(200)|wp_throwing(170)|wp_archery(100),knows_lvl_23_cav|knows_shield_4|knows_power_strike_6,germanic_face_1, germanic_face_2],
  ["langobard_companion","Langobard Commander (Sculdahis)","Langobard Commanders (Sculdahis)",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_culture_2,
   [itm_khergit_leather_boots,itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,itm_mid_generic_mail_3,itm_mid_generic_mail_9,itm_mid_generic_mail_24,itm_mid_generic_mail_27,itm_roman_rigid_scale_5,itm_medium_scale_5,itm_lombard_lamellar_1,itm_lombard_lamellar_2,itm_iatrus_2,itm_fernpass_helmet_2,itm_kalhkni_helmet_1,itm_pannonhalma_spatha,itm_heavy_lance,itm_tab_shield_small_round_c]+horses_germanic_3,
   def_attrib_lvl_30|level(29),wp_one_handed(250)|wp_two_handed(250)|wp_polearm(240)|wp_throwing(200)|wp_archery(100),knows_lvl_30_cav|knows_shield_5|knows_power_strike_7,germanic_face_1, germanic_face_2],

  #shared with the scirii
  ["limigantes_rebel","Limigantes Rebel","Limigantes Rebels",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_culture_2,
   [itm_javelin,itm_javelin,itm_roman_spear_1,itm_winged_mace,itm_generic_tunic_11,itm_generic_tunic_13,itm_linen_tunic,itm_linen_shirt_13,itm_linen_shirt_10,itm_linen_shirt]+shoes_generic+shields_simple+shields_small,
   def_attrib_skirmisher|level(13),wp_one_handed(120)|wp_two_handed(90)|wp_polearm(130)|wp_archery(140)|wp_throwing(170),knows_skirmisher,sarmatian_face_1, sarmatian_face_2],

  #silingi - shared between the lombards + vandals
  ["silingi_warrior","Silingi Warrior","Silingi Warriors",tf_guarantee_basic,0,0,fac_culture_2,
   [itm_roman_lorum_fasciari_2,itm_khergit_leather_boots,itm_generic_tunic_1,itm_generic_tunic_13,itm_generic_tunic_14,itm_linen_shirt,itm_cloaked_generic_tunic_1,itm_cloaked_generic_tunic_13,itm_cloaked_tunic_17,itm_cloaked_tunic_10,itm_round_shield_wood_2,itm_round_shield_wood_3,itm_eastern_germanic_shield_1,itm_kerch_shield_wood,itm_kerch_shield_11,itm_kerch_shield_12,itm_sword_medieval_c_long,itm_long_seax_1,itm_winged_mace,itm_war_spear_1,itm_javelin]+shoes_generic+germanic_caps,
   def_attrib_lvl_18|level(18),wp_one_handed(190)|wp_two_handed(150)|wp_polearm(200)|wp_throwing(170)|wp_archery(100),knows_lvl_18_inf|knows_shield_4|knows_power_strike_6,germanic_face_1, germanic_face_2],
  ["silingi_horseman","Silingi Horseman","Silingi Horsemen",tf_mounted|tf_guarantee_horse|tf_guarantee_basic,0,0,fac_culture_2,
   [itm_warhorse,itm_roman_lorum_fasciari_2,itm_khergit_leather_boots,itm_generic_tunic_1,itm_generic_tunic_13,itm_generic_tunic_14,itm_linen_shirt,itm_cloaked_generic_tunic_1,itm_cloaked_generic_tunic_13,itm_cloaked_tunic_17,itm_cloaked_tunic_10,itm_kerch_shield_11,itm_kerch_shield_12,itm_sword_medieval_c_long,itm_heavy_lance]+shoes_generic+germanic_caps+horses_germanic_3+horses_germanic_4,
   def_attrib_lvl_23|level(22),wp_one_handed(190)|wp_two_handed(150)|wp_polearm(220)|wp_throwing(170)|wp_archery(100),knows_lvl_23_cav|knows_shield_3|knows_power_strike_7,germanic_face_1, germanic_face_2],

#BRITONS  
  ["briton_footman","Civis Armatura Britanni","Civites Armaturae Britanni",tf_guarantee_basic,0,0,fac_culture_3,
   [itm_roman_spear_2,itm_roman_spear_3,itm_dagger,itm_securis,(itm_sword_medieval_a,imod_rusty),itm_brown_hood1,(itm_intercisa_helmet_1,imod_battered),(itm_intercisa_helmet_2,imod_battered),itm_woolen_hose,itm_round_shield_roman_2,itm_round_shield_roman_3,itm_round_shield_roman_4,itm_round_shield_roman_5,itm_round_shield_roman_6,itm_round_shield_roman_26]+tunics_britons+shields_britons_1+hats_briton+shoes_roman+light_armor_briton+pannonian_hats,
   def_attrib_lvl_18|level(18),wp_one_handed(160)|wp_two_handed(140)|wp_polearm(170)|wp_throwing(160)|wp_archery(130),knows_lvl_18_inf|knows_shield_5|knows_power_strike_3,briton_face_1, briton_face_2],

  ["briton_infantry","Pedes Limitaneus Britanni","Pedites Limitanei Britanni",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_3,
   [itm_briton_subarmalis_1,itm_briton_subarmalis_2,itm_subarmalis_2,itm_short_roman_mail_1,itm_short_roman_mail_2,itm_short_roman_mail_3,itm_short_roman_mail_4,itm_mid_roman_mail_1,itm_mid_roman_mail_2,itm_mid_roman_mail_3,itm_mid_roman_mail_8,
   itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_burgh_helmet_1,itm_burgh_helmet_2,itm_iatrus_1,itm_iatrus_2,itm_christies_helmet_1,
   itm_oval_shield_limitanei_2,itm_oval_shield_limitanei_5,itm_oval_shield_limitanei_7,itm_oval_shield_briton_1,itm_oval_shield_briton_2,itm_roman_spear_3,itm_roman_spear_4,itm_late_roman_spear_1,itm_sword_medieval_a]+shoes_roman+light_armor_briton,
   def_attrib_lvl_23|level(23),wp_one_handed(190)|wp_two_handed(160)|wp_polearm(200)|wp_throwing(190)|wp_archery(140),knows_lvl_23_inf|knows_shield_6|knows_power_strike_4,briton_face_1, briton_face_2],

  ["briton_skirmisher","Exculcator Britanni","Exculcatores Britanni",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_culture_3,
   [itm_throwing_spears,itm_throwing_spears,itm_brown_hood1,itm_new_hood_c,itm_new_hood_d,itm_woolen_hose,itm_securis,itm_dagger,itm_club]+tunics_britons+shoes_roman+hats_briton+pannonian_hats,
   def_attrib_skirmisher|level(13),wp_one_handed(130)|wp_two_handed(100)|wp_polearm(130)|wp_throwing(160)|wp_archery(160),knows_skirmisher,briton_face_1, briton_face_2],

  ["briton_archer","Sagittarius Britanni","Sagittarii Britanni",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_culture_3,
   [itm_brown_hood1,itm_new_hood_c,itm_new_hood_d,itm_woolen_hose,itm_securis,itm_hunting_bow,itm_short_bow,itm_long_bow,itm_strong_bow,itm_roman_arrows_2,itm_roman_arrows_2]+tunics_britons+shoes_roman+hats_briton+pannonian_hats,
   def_attrib_lvl_18|level(17),wp_one_handed(150)|wp_two_handed(100)|wp_polearm(150)|wp_throwing(160)|wp_archery(170),knows_archer,briton_face_1, briton_face_2],

  ["briton_horseman","Eques Britanni","Equites Britanni",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_3,
   [itm_tab_shield_small_round_c,itm_short_roman_mail_1,itm_short_roman_mail_2,itm_short_roman_mail_3,itm_short_roman_mail_4,itm_pictish_short_mail_1,itm_pictish_short_mail_3,itm_mid_roman_mail_8,itm_ridge_helm_c,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_intercisa_helmet_gilded_1,itm_burgh_helmet_1,itm_koblenz_helmet_1,itm_iatrus_1,itm_arabian_sword_a,itm_throwing_spears]+shields_britons_cavalry_1+shoes_roman+tunics_britons+light_armor_briton+horses_roman_1+horses_roman_2,
   def_attrib_lvl_23|level(23),wp_one_handed(190)|wp_two_handed(160)|wp_polearm(200)|wp_throwing(190)|wp_archery(140),knows_lvl_23_cav|knows_shield_5|knows_power_strike_5,briton_face_1, briton_face_2],

  ["briton_companion","Comes Britanni","Comites Britanni",tf_mounted|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm|tf_guarantee_horse,0,0,fac_culture_3,
   [itm_imperial_courser,itm_leather_gloves,itm_burgh_helmet_plume_1,itm_burgh_helmet_plume_2,itm_burgh_helmet_plume_3,itm_iatrus_plume_1,itm_iatrus_plume_2,itm_intercisa_helmet_gilded_plume_1,itm_intercisa_helmet_rich_plume_3,itm_intercisa_helmet_rich_plume_1,itm_roman_squamata_3,itm_mid_roman_mail_8,
   itm_long_briton_mail_1,itm_long_briton_mail_2,itm_long_briton_mail_3,itm_vaegir_elite_armor,itm_plate_armor,itm_khergit_elite_armor,itm_long_roman_mail_1,itm_long_roman_mail_2,itm_long_roman_mail_3,itm_long_roman_mail_5,itm_tab_shield_small_round_c,itm_sword_khergit_4,itm_roman_spear_4,itm_late_roman_spear_1,itm_heavy_lance]+horses_roman_3+horses_roman_4+shoes_roman+greaves_roman,
   def_attrib_lvl_30|level(30),wp_one_handed(230)|wp_two_handed(200)|wp_polearm(240)|wp_throwing(220),knows_lvl_30_cav|knows_power_strike_8|knows_shield_5,briton_face_1, briton_face_2],

  #used if player rules briton as king
  ["briton_knight","Caballarius Britanni","Caballarii Britanni",tf_mounted|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_culture_3,
   [itm_heavy_lance,itm_arabian_sword_b,itm_tab_shield_small_round_c,itm_cuirass_roman_1,itm_cuirass_roman_2,itm_roman_scale_cuirass_1,itm_roman_scale_cuirass_2,itm_vaegir_elite_armor,itm_plate_armor,itm_khergit_elite_armor,itm_burgh_helmet_plume_2,itm_burgh_helmet_plume_3,itm_christies_helmet_crest_1,itm_christies_helmet_crest_2,itm_iatrus_plume_2,itm_koblenz_crested_2,itm_koblenz_crested_3,itm_augsburg_2_helmet]+greaves_roman+horses_roman_4,
   def_attrib_lvl_32|level(32),wp_one_handed(260)|wp_two_handed(260)|wp_polearm(260)|wp_throwing(260)|wp_archery(200)|wp_crossbow(200),knows_athletics_3|knows_riding_7|knows_ironflesh_10|knows_power_throw_6|knows_power_draw_4|knows_weapon_master_6|knows_inventory_management_4|knows_power_strike_8,briton_face_1, briton_face_2],

#limited to riothamus
  ["armorican_horseman","Caballarius Armoricae","Caballari Armoricani",tf_mounted|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_culture_3,
   [itm_half_cataphract_horse_7,itm_roman_squamata_4,itm_long_briton_mail_1,itm_long_briton_mail_3,itm_iatrus_2,itm_iatrus_plume_2,itm_koblenz_crested_2,itm_augsburg_2_helmet,itm_intercisa_helmet_gilded_1,itm_intercisa_helmet_rich_3,itm_christies_helmet_crest_1,itm_christies_helmet_crest_2,itm_burgh_helmet_2,itm_burgh_helmet_plume_2,itm_gold_ridge_helm,itm_koblenz_helmet_3,itm_intercisa_helmet_gilded_plume_1,itm_late_roman_spear_1,itm_jarid,itm_sword_khergit_4,itm_tab_shield_small_round_c]+shoes_roman+greaves_roman+horses_roman_3,
   def_attrib_lvl_30|level(30),wp_one_handed(240)|wp_two_handed(200)|wp_polearm(240)|wp_throwing(240),knows_lvl_30_cav|knows_power_strike_8|knows_shield_5|knows_horse_archery_5,briton_face_1, briton_face_2],

#british legion(s) - armed with spear, spiculum + sword (feltwell)
#based off of the secunda britannica
  ["pedes_secunda_britannica","Pedes Legionis Britannica","Pedites Legionis Britannica",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_culture_3,
   [itm_457_mail_short_2,itm_457_mail_shirt_3,itm_457_scale_hauberk_1,itm_iatrus_1,itm_iatrus_2,itm_burgh_helmet_1,itm_burgh_helmet_2,itm_late_roman_spear_1,itm_arabian_sword_a,itm_spiculum,itm_oval_shield_briton_3]+shoes_roman+greaves_roman,
   def_attrib_lvl_28|level(28),wp_one_handed(220)|wp_two_handed(160)|wp_polearm(220)|wp_archery(120)|wp_throwing(220),knows_lvl_28_inf|knows_shield_6|knows_power_strike_6,briton_face_1, briton_face_2],
#armed with spear, sword, angon
  ["abulci","Miles Numerus Abulci","Milites Numeri Abulci",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_culture_3,
   [itm_ankle_boots,itm_wrapping_boots,itm_khergit_leather_boots,itm_roman_military_tunic_2,itm_roman_military_tunic_5,itm_457_mail_short_2,itm_roman_light_scale_2,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_iatrus_1,itm_burgh_helmet_1,itm_late_roman_spear_1,itm_sword_medieval_a,itm_angon_1,itm_oval_shield_limitanei_7] + shoes_roman,
   def_attrib_lvl_25|level(25),wp_one_handed(200)|wp_two_handed(190)|wp_polearm(225)|wp_throwing(190),knows_lvl_23_inf|knows_shield_6|knows_power_strike_6,briton_face_1, briton_face_2],

  ["pedes_votadini","Votadini Footman (Pedyt)","Votadini Footmen (Pedyt)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_culture_3,
   [itm_ankle_boots,itm_wrapping_boots,itm_concave_shield_blue_2,itm_concave_shield_yellow_1,itm_falkirk_tunic_1,itm_falkirk_tunic_2,itm_falkirk_tunic_3,itm_roman_military_tunic_6,itm_roman_subarmalis_new_6,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_burgh_helmet_1,itm_iatrus_1,itm_burgh_helmet_light,itm_woolen_cap_c,itm_woolen_cap_1,itm_woolen_cap_4,itm_woolen_cap_6,itm_pannonian_cap_4,itm_pannonian_cap_2,itm_new_hood_a,itm_brown_hood1,itm_short_roman_mail_2,itm_short_roman_mail_3,itm_pictish_short_mail_1,itm_pict_axe_a,itm_late_roman_spear_2,itm_jarid] + shoes_roman,
   def_attrib_lvl_20|level(20),wp_one_handed(220)|wp_two_handed(190)|wp_polearm(205)|wp_throwing(190),knows_lvl_18_inf|knows_shield_4|knows_power_strike_6,celtic_face_1, celtic_face_2],

  ["eques_votadini","Votadini Horseman (Marchauc)","Votadini Horsemen (Marchauc)",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_culture_3,
   [itm_celtic_horse_1,itm_celtic_horse_2,itm_hunter,itm_ankle_boots,itm_wrapping_boots,itm_short_roman_mail_2,itm_short_roman_mail_3,itm_mid_generic_mail_27,itm_pictish_short_mail_1,itm_457_mail_shirt_2,itm_long_briton_mail_2,itm_intercisa_helmet_2,itm_burgh_helmet_1,itm_burgh_helmet_plume_3,itm_burgh_helmet_mail,itm_iatrus_plume_1,itm_iatrus_plume_2,itm_concave_shield_blue_small_2,itm_concave_shield_yellow_small_1,itm_late_roman_spear_1,itm_cavalry_javelins,itm_pictish_sword] + shoes_roman,
   def_attrib_lvl_28|level(28),wp_one_handed(260)|wp_two_handed(190)|wp_polearm(245)|wp_throwing(240),knows_lvl_28_cav|knows_shield_5|knows_power_strike_7|knows_horse_archery_5,celtic_face_1, celtic_face_2],

  ["briton_deserter","Briton Deserter","Briton Deserters",tf_guarantee_basic,0,0,fac_culture_3,
   [itm_roman_spear_1,itm_roman_spear_2,itm_roman_spear_3,itm_securis,itm_brown_hood1,itm_new_hood_c,itm_new_hood_d,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_ridge_helm_c,itm_intercisa_helmet_1,itm_iatrus_helmet_mail,itm_iatrus_1,itm_woolen_hose,itm_oval_shield_wood_1,itm_oval_shield_wood_2,itm_oval_shield_wood_3,itm_oval_shield_leather_1,itm_oval_shield_leather_2,itm_oval_shield_leather_3]+tunics_britons+shields_britons_1+hats_briton+shoes_roman+light_armor_briton+pannonian_hats,
   def_attrib_lvl_18|level(17),wp_one_handed(160)|wp_two_handed(140)|wp_polearm(170)|wp_throwing(160)|wp_archery(130),knows_lvl_18_inf|knows_shield_4|knows_power_strike_2,briton_face_1, briton_face_2],
  ["briton_messenger","Briton Messenger","Briton Messengers",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_3,
   [itm_short_roman_mail_1,itm_short_roman_mail_2,itm_short_roman_mail_3,itm_short_roman_mail_4,itm_ridge_helm_c,itm_arabian_sword_a]+shoes_roman+tunics_britons+light_armor_briton,
   def_attrib_lvl_23|level(25),wp_one_handed(190)|wp_two_handed(160)|wp_polearm(200)|wp_throwing(190)|wp_archery(140),knows_lvl_23_cav|knows_shield_5|knows_power_strike_5,briton_face_1, briton_face_2],
  ["briton_prison_guard","Prison Guard","Prison Guards",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_3,
   [itm_tab_shield_heater_a,itm_late_roman_spear_2,itm_short_roman_mail_1,itm_short_roman_mail_2,itm_short_roman_mail_3,itm_short_roman_mail_4,itm_ridge_helm_c,itm_intercisa_helmet_1,itm_burgh_helmet_1,itm_koblenz_helmet_1,itm_iatrus_1,itm_sword_khergit_4]+shoes_roman,
   def_attrib_lvl_28|level(26),wp(230),knows_common|knows_athletics_4|knows_power_strike_5|knows_ironflesh_5|knows_shield_5,briton_face_1, briton_face_2],
  ["briton_castle_guard","Castle Guard","Castle Guards",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_3,
   [itm_tab_shield_heater_a,itm_late_roman_spear_2,itm_short_roman_mail_1,itm_short_roman_mail_2,itm_short_roman_mail_3,itm_short_roman_mail_4,itm_ridge_helm_c,itm_intercisa_helmet_1,itm_burgh_helmet_1,itm_koblenz_helmet_1,itm_iatrus_1,itm_sword_khergit_4]+shoes_roman,
   def_attrib_lvl_28|level(26),wp(230),knows_common|knows_athletics_4|knows_power_strike_5|knows_ironflesh_5|knows_shield_5,briton_face_1, briton_face_2],

#NORTHERN GERMANS
  ["northern_germanic_freeman","N. Germanic Freeman (Faerdi)","N. Germanic Freemen (Faerdi)",tf_guarantee_basic,0,0,fac_culture_4,
   [itm_battle_axe_3,itm_carbatinae_1_red,itm_carbatinae_2_red,itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_kaftan_tunic_10,itm_kaftan_tunic_4,itm_kaftan_tunic_6,
   itm_spear,itm_medium_spear_1,itm_medium_spear_3,itm_seax_2,itm_fighting_axe,itm_basic_axe,itm_bearded_axe_1,(itm_intercisa_helmet_1,imod_battered),itm_ridge_helm_c,itm_intercisa_helmet_1,(itm_intercisa_helmet_1,imod_battered),itm_triveres_cloth,itm_triveres_leather,itm_drengsted_helmet_leather]+tunics_northern_germanic+shields_northern_germanic_1+angons+shields_generic+hats_northern+germanic_caps+shoes_generic+cloaked_tunics_northern_germanic,
   def_attrib_lvl_18|level(18),wp_one_handed(180)|wp_two_handed(160)|wp_polearm(160)|wp_archery(90)|wp_throwing(160),knows_lvl_18_inf|knows_shield_3|knows_power_strike_5,germanic_face_1, germanic_face_2],

  ["northern_germanic_warrior","N. Germanic Warrior (Duguthi)","N. Germanic Warriors (Duguthi)",tf_guarantee_basic,0,0,fac_culture_4,
   [itm_carbatinae_1_red,itm_carbatinae_2_red,itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_leather_armor_c,itm_leather_armor_d,itm_leather_armor_e,itm_thick_coat_1,itm_thick_coat_3,itm_triveres_mail,itm_burgh_helmet_1,itm_intercisa_helmet_1,(itm_augst_helmet_1,imod_battered),(itm_intercisa_helmet_1,imod_battered),itm_burgh_helmet_light,itm_burgh_helmet_mail,itm_drengsted_helmet_mail,
   itm_short_ragged_mail_3,itm_short_ragged_mail_7,itm_short_ragged_mail_5,itm_mid_generic_mail_19,itm_mid_generic_mail_1,itm_mid_generic_mail_3,itm_seax_10,itm_sword_medieval_c_long,itm_sword_medieval_a,itm_long_seax_2,itm_seax_2,itm_war_spear,itm_poleaxe,itm_battle_axe_3,itm_battle_axe_4,itm_battle_axe,itm_bearded_axe_2]+shoes_generic+shields_northern_germanic_2+angons+cloaked_tunics_northern_germanic,
   def_attrib_lvl_23|level(23),wp_one_handed(210)|wp_two_handed(190)|wp_polearm(180)|wp_archery(110)|wp_throwing(200),knows_lvl_23_inf|knows_shield_3|knows_power_strike_7,germanic_face_1, germanic_face_2],

  ["northern_germanic_companion","N. Germanic Companion (Herthganauti)","N. Germanic Companions (Herthganauto)",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_4,
   [itm_tab_shield_round_d,itm_carbatinae_1_red,itm_carbatinae_2_red,itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_triveres_mail,itm_burgh_helmet_1,itm_burgh_helmet_2,itm_mid_generic_mail_19,itm_mid_generic_mail_1,itm_mid_generic_mail_3,itm_long_mail_new_2,itm_long_mail_new_6,itm_long_mail_new_7,
   itm_war_spear,itm_poleaxe,itm_sword_viking_c_long,itm_arabian_sword_a,itm_battle_axe_5,itm_battle_axe,itm_seax_10]+shoes_generic+angons+shields_northern_germanic_2,
   def_attrib_lvl_28|level(28),wp_one_handed(240)|wp_two_handed(190)|wp_polearm(210)|wp_archery(110)|wp_throwing(230),knows_lvl_28_inf|knows_shield_4|knows_power_strike_8,germanic_face_1, germanic_face_2],

  ["northern_germanic_skirmisher","N. Germanic Skirmisher (Juguthi)","N. Germanic Skirmishers (Juguthi)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_4,
   [itm_javelin,itm_javelin,itm_wooden_javelin,itm_wooden_javelin,itm_carbatinae_1_red,itm_carbatinae_2_red,itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_seax_2,itm_fighting_axe,itm_club,itm_winged_mace]+tunics_northern_germanic+shields_simple+hats_northern,
   def_attrib_skirmisher|level(13),wp_one_handed (140) | wp_two_handed (130) | wp_polearm (120) | wp_archery (120) | wp_crossbow (90) | wp_throwing (140) | wp_firearm(140),knows_skirmisher,germanic_face_1, germanic_face_2],

  ["northern_germanic_bowman","N. Germanic Bowman (Bogomanna)","N. Germanic Bowmen (Bogomanni)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_4,
   [itm_carbatinae_1_red,itm_carbatinae_2_red,itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_germanic_arrows,itm_germanic_arrows,itm_hunting_bow,itm_short_bow,itm_long_bow,itm_seax_2,itm_fighting_axe]+tunics_northern_germanic+hats_northern,
   def_attrib_lvl_18|level(17),wp_one_handed (170) | wp_two_handed (170) | wp_polearm (170) | wp_archery (140) | wp_crossbow (90) | wp_throwing (140) | wp_firearm(140),knows_archer,germanic_face_1, germanic_face_2],

  ["northern_germanic_horseman","N. Germanic Horseman (Hrossmanna)","N. Germanic Horsemen (Hrossmanni)",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_polearm,0,0,fac_culture_4,
   [itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_leather_armor_c,itm_leather_armor_d,itm_leather_armor_e,itm_kaftan_tunic_10,itm_kaftan_tunic_4,itm_kaftan_tunic_6,itm_triveres_leather,itm_triveres_mail,itm_burgh_helmet_light,itm_burgh_helmet_mail,itm_drengsted_helmet_mail,itm_battle_axe,itm_medium_spear_3,itm_sword_medieval_c_long]+horses_germanic_4+shields_northern_germanic_cavalry_1+tunics_northern_germanic+hats_northern+shoes_generic,
   def_attrib_lvl_18|level(18),wp_one_handed (190) | wp_two_handed (180) | wp_polearm (195) | wp_archery (120) | wp_crossbow (125) | wp_throwing (190),knows_lvl_18_cav|knows_shield_2|knows_power_strike_4,germanic_face_1, germanic_face_2],

  ["northern_germanic_messenger","Northern Germanic Messenger","Northern Germanic Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_culture_4,
   [itm_sword_medieval_c_long,itm_wrapping_boots,itm_hunting_bow,itm_germanic_arrows,itm_saddle_horse]+tunics_northern_germanic,
   def_attrib_lvl_23|level(25),wp(200),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,germanic_face_1, germanic_face_2],
  ["northern_germanic_deserter","N. Germanic Deserter","N. Germanic Deserters",tf_guarantee_basic,0,0,fac_culture_4,
   [itm_battle_axe_3,itm_cloaked_tunic_16,itm_cloaked_tunic_1,itm_cloaked_tunic_6,itm_cloaked_tunic_8,itm_cloaked_tunic_3,itm_cloaked_tunic_5,itm_cloaked_tunic_9,itm_cloaked_tunic_10,itm_carbatinae_1_red,itm_carbatinae_2_red,itm_kaftan_tunic_10,itm_kaftan_tunic_4,itm_kaftan_tunic_6,
   itm_spear,itm_medium_spear_1,itm_medium_spear_3,itm_seax_2,itm_fighting_axe,itm_basic_axe,itm_triveres_cloth]+tunics_northern_germanic+shields_northern_germanic_1+angons+shields_generic+hats_northern+germanic_caps+shoes_generic,
   def_attrib_lvl_18|level(17),wp_one_handed(180)|wp_two_handed(160)|wp_polearm(160)|wp_archery(90)|wp_throwing(160),knows_lvl_18_inf|knows_shield_3|knows_power_strike_5,germanic_face_1, germanic_face_2],
  ["northern_germanic_prison_guard","Prison Guard","Prison Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_culture_4,
   [itm_sword_medieval_a,itm_battle_axe_1,itm_tab_shield_round_d,itm_long_spear_a,itm_burgh_helmet_1,itm_leather_gloves,itm_mid_generic_mail_3,itm_mid_generic_mail_18,itm_mid_generic_mail_9,itm_carbatinae_1_red,itm_carbatinae_2_red,itm_simple_shoes,itm_wrapping_boots,itm_hide_boots,itm_angon_1,itm_angon_2],
   def_attrib_lvl_28|level(24),wp_one_handed(240) | wp_throwing(190),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_athletics_5|knows_shield_4,germanic_face_1, germanic_face_2],
  ["northern_germanic_castle_guard","Castle Guard","Castle Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_culture_4,
   [itm_sword_medieval_a,itm_battle_axe_1,itm_tab_shield_round_d,itm_long_spear_a,itm_burgh_helmet_1,itm_leather_gloves,itm_mid_generic_mail_3,itm_mid_generic_mail_18,itm_mid_generic_mail_9,itm_carbatinae_1_red,itm_carbatinae_2_red,itm_simple_shoes,itm_wrapping_boots,itm_hide_boots,itm_angon_1,itm_angon_2],
   def_attrib_lvl_28|level(24),wp_one_handed(240) | wp_throwing(190),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_athletics_5|knows_shield_4,germanic_face_1, germanic_face_2],

  ["kouadoi_warrior","Kouadoi Warrior (Duguthi)","Kouadoi Warriors (Duguthi)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_4,
   [itm_generic_tunic_1,itm_generic_tunic_3,itm_generic_tunic_5,itm_cloaked_generic_tunic_1,itm_cloaked_generic_tunic_3,itm_cloaked_generic_tunic_5,itm_jarid,itm_jarid,itm_mace_1,itm_seax_2,itm_round_shield_germanic_small_13,itm_round_shield_germanic_small_20]+hats_northern+shoes_generic,
   def_attrib_lvl_18|level(16),wp_one_handed (160) | wp_two_handed (130) | wp_polearm (160) | wp_archery (120) | wp_crossbow (90) | wp_throwing (180) | wp_firearm(140),knows_skirmisher|knows_ironflesh_5|knows_power_strike_5,germanic_face_1, germanic_face_2],

  #germanic heroic-age inspired AOR troops
  ["jute_swordsman","Jute Sword-Keen (Sweordcenan)","Jute Sword-Keen (Sweordcenan)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_culture_4, #swordsman
   [itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_wrapping_boots,itm_cloaked_tunic_6,itm_leather_armor_c,itm_mid_generic_mail_1,itm_mid_generic_mail_16,itm_burgh_helmet_1,itm_burgh_helmet_mail,itm_drengsted_helmet_mail,itm_drengsted_helmet_leather,itm_arabian_sword_a,itm_concave_shield_germanic_20],
   def_attrib_lvl_25|level(25),wp_one_handed(230)|wp_two_handed(190)|wp_polearm(180)|wp_archery(110)|wp_throwing(200),knows_lvl_23_inf|knows_shield_4|knows_power_strike_8,germanic_face_1, germanic_face_2],

  ["angle_hero","Angle Hero (Sweordcenan)","Angle Heroes (Sweordcenan)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_culture_4, #cav?
   [itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_wrapping_boots],
   def_attrib_lvl_25|level(25),wp_one_handed(230)|wp_two_handed(190)|wp_polearm(180)|wp_archery(110)|wp_throwing(200),knows_lvl_23_inf|knows_shield_4|knows_power_strike_8,germanic_face_1, germanic_face_2],

  ["saxon_companion","Saxon Throne-Companion (Seldguman)","Saxon Throne-Companions (Seldgumanni)",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_4, #sword/spear
   [itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_simple_shoes,itm_mid_generic_mail_21,itm_mid_generic_mail_29,itm_burgh_helmet_1,itm_burgh_helmet_2,itm_triveres_mail,itm_arabian_sword_a,itm_war_spear_3,itm_concave_shield_germanic_11],
   def_attrib_lvl_28|level(28),wp_one_handed(230)|wp_two_handed(200)|wp_polearm(230)|wp_archery(110)|wp_throwing(220),knows_lvl_28_inf|knows_shield_5|knows_power_strike_7,germanic_face_1, germanic_face_2],

#PICTISH
  ["pictish_warrior","Pictish Warrior (Katuur)","Pictish Warriors (Katuur)",tf_guarantee_basic,0,0,fac_culture_5,
   [itm_war_spear,itm_medium_spear_1,itm_spear,itm_glaive,itm_pict_axe_a,itm_pict_axe_b,itm_sword_medieval_b_small,itm_sword_medieval_c_small,itm_new_hood_c,itm_new_hood_d,itm_p_hood,itm_brown_hood1,itm_brown_hood1,itm_ridge_helm_c,(itm_intercisa_helmet_1,imod_battered),(itm_augst_helmet_1,imod_battered),(itm_intercisa_helmet_1,imod_battered),itm_iatrus_helmet_light,itm_burgh_helmet_light,itm_woolen_hose,itm_ragged_outfit,itm_wrapping_boots,itm_javelin,itm_javelin]+tunics_pictish+shields_picts+hats_pict+shields_pictish_small+light_armor_pict,
   def_attrib_lvl_20|level(20),wp_one_handed (200) | wp_two_handed (165) | wp_polearm (200) | wp_archery (105) | wp_crossbow (105) | wp_throwing (190),knows_lvl_18_inf|knows_shield_4|knows_power_strike_6,celtic_face_1, celtic_face_2],

  ["pictish_skirmisher","Pictish Hunter (Selgauur)","Pictish Hunters (Selgauur)",tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_culture_5,
   [itm_short_bow,itm_hunting_bow,itm_long_bow,itm_barbed_arrows,itm_barbed_arrows,itm_pict_axe_a,itm_pict_axe_b,itm_simple_shoes,itm_p_hood,itm_brown_hood1,itm_brown_hood1,itm_woolen_hose,itm_brown_hood1,itm_nomad_boots,itm_wrapping_boots,itm_new_hood_c,itm_new_hood_d]+tunics_pictish+shields_simple+hats_pict+shields_picts,
   def_attrib_lvl_13|level(13),wp_one_handed(145)|wp_polearm(140)|wp_throwing(160)|wp_archery(170),knows_archer,celtic_face_1, celtic_face_2],

  ["pictish_companion","Pictish Companion (Uohheluur)","Pictish Companions (Uohheluur)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_culture_5,
   [itm_simple_shoes,itm_wrapping_boots,itm_nomad_boots,itm_hunter_boots,itm_hide_boots,itm_war_spear,itm_sword_viking_2_small,itm_pictish_sword,itm_celtic_horse_1,itm_celtic_horse_2,itm_leather_gloves,itm_brigandine_red,itm_pictish_short_mail_1,itm_pictish_short_mail_2,itm_pictish_short_mail_3,itm_koblenz_helmet_light_old,itm_intercisa_helmet_1,itm_burgh_helmet_1,itm_burgh_helmet_2,itm_burgh_helmet_light,itm_burgh_helmet_mail,itm_tab_shield_small_round_c]+shields_pictish_small+light_armor_pict,
   def_attrib_lvl_30|level(30),wp_one_handed (250) | wp_two_handed (230) | wp_polearm (240) | wp_archery (115) | wp_crossbow (115) | wp_throwing (115),knows_lvl_30_cav|knows_shield_3|knows_power_strike_8,celtic_face_1, celtic_face_2],

  ["pictish_messenger","Pictish Messenger","Pictish Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_culture_5,
   [itm_sword_medieval_c_small,itm_wrapping_boots,itm_courser,itm_leather_gloves,itm_spear,itm_javelin,itm_javelin]+tunics_pictish,
   def_attrib_lvl_23|agi_21|level(25),wp(200),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_throw_5,celtic_face_1, celtic_face_2],
  ["pictish_deserter","Pictish Deserter","Pictish Deserter",tf_guarantee_basic,0,0,fac_culture_5,
   [itm_war_spear,itm_medium_spear_1,itm_spear,itm_glaive,itm_pict_axe_a,itm_pict_axe_b,itm_sword_medieval_b_small,itm_sword_medieval_c_small,itm_new_hood_c,itm_new_hood_d,itm_p_hood,itm_brown_hood1,itm_brown_hood1,itm_ridge_helm_c,(itm_intercisa_helmet_1,imod_battered),itm_intercisa_helmet_1,itm_iatrus_helmet_mail,itm_iatrus_helmet_light,itm_woolen_hose,itm_ragged_outfit,itm_wrapping_boots,itm_javelin,itm_javelin]+tunics_pictish+shields_picts+pictish_naked+hats_pict+shields_pictish_small,
   def_attrib_lvl_18|level(18),wp_one_handed (170) | wp_two_handed (165) | wp_polearm (170) | wp_archery (105) | wp_crossbow (105) | wp_throwing (160),knows_lvl_18_inf|knows_shield_4|knows_power_strike_4,celtic_face_1, celtic_face_2],
  ["pictish_prison_guard","Prison Guard","Prison Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_culture_5,
   [itm_war_spear,itm_leather_gloves,itm_wrapping_boots,itm_ridge_helm_c,itm_pictish_sword,itm_pictish_short_mail_1,itm_pictish_short_mail_2,itm_pictish_short_mail_3]+shields_picts,
   def_attrib_lvl_28|level(28),wp_one_handed (230) | wp_two_handed (240) | wp_polearm (230) | wp_archery (115) | wp_crossbow (115) | wp_throwing (115),knows_common|knows_ironflesh_7|knows_shield_4|knows_power_strike_6|knows_athletics_5,celtic_face_1, celtic_face_2],
  ["pictish_castle_guard","Castle Guard","Castle Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_culture_5,
   [itm_war_spear,itm_leather_gloves,itm_wrapping_boots,itm_ridge_helm_c,itm_pictish_sword,itm_pictish_short_mail_1,itm_pictish_short_mail_2,itm_pictish_short_mail_3]+shields_picts,
   def_attrib_lvl_28|level(28),wp_one_handed (230) | wp_two_handed (240) | wp_polearm (230) | wp_archery (115) | wp_crossbow (115) | wp_throwing (115),knows_common|knows_ironflesh_7|knows_shield_4|knows_power_strike_6|knows_athletics_5,celtic_face_1, celtic_face_2],

  ["verturiones_horse_whisperers","Verturiones Horse Whisperer (Marhhauk)","Verturiones Horse Whisperers (Marhokyon)",tf_mounted|tf_guarantee_basic|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_culture_5,
   [itm_sword_medieval_b_small,itm_medium_spear_2,itm_cavalry_javelins,itm_concave_shield_leather_small_1,itm_concave_shield_leather_small_3,itm_concave_shield_red_small_3,itm_new_hood_c,itm_new_hood_d,itm_p_hood,itm_brown_hood1,itm_woolen_hose,itm_skirmisher_tunic_3,itm_falkirk_tunic_2,itm_falkirk_tunic_5,itm_wrapping_boots,itm_hunter_boots,itm_celtic_horse_1,itm_celtic_horse_2],
   def_attrib_lvl_18|level(18),wp_one_handed (180) | wp_two_handed (170) | wp_polearm (200) | wp_archery (105) | wp_crossbow (105) | wp_throwing (210),knows_athletics_2|knows_riding_6|knows_ironflesh_3|knows_power_throw_5|knows_weapon_master_3|knows_inventory_management_2|knows_power_strike_4|knows_shield_2|knows_horse_archery_5,celtic_face_1, celtic_face_2],

  ["dycalidones_fanatic","Dycalidones Fanatic (Llathuur)","Dycalidones Fanatics (Llathuuir)",tf_guarantee_basic,0,0,fac_culture_5,
   [itm_sword_viking_2_small,itm_concave_shield_red_small_2,itm_concave_shield_blue_small_2,itm_concave_shield_yellow_small_1,itm_woolen_hose,itm_wrapping_boots,itm_pict_body_1m,itm_pict_body_2m,itm_pict_body_3m,itm_pict_body_4m,itm_pants_5,itm_pants_10,itm_pants_11],
   def_attrib_lvl_20|level(19),wp_one_handed (220) | wp_two_handed (170) | wp_polearm (170) | wp_archery (105) | wp_crossbow (105) | wp_throwing (160),knows_lvl_18_inf|knows_shield_4|knows_power_strike_9,celtic_face_1, celtic_face_2],

#MERCS FOR BRITAIN
  ["attecotti_raider","Attecotti Raider (Mor-Lathr)","Attecotti Raiders (Mor-Lathr)",tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_culture_5,
   [itm_simple_shoes,itm_woolen_hose,itm_wrapping_boots,itm_generic_tunic_15,itm_falkirk_tunic_1,itm_falkirk_tunic_2,itm_falkirk_tunic_3,itm_p_hood,itm_brown_hood1,itm_new_hood_c,itm_new_hood_d,itm_pict_axe_b,itm_jarid,itm_jarid,itm_vae_cuadrado_21,itm_vae_cuadrado_27,itm_concave_shield_blue_small_2,itm_round_shield_blue_small_2,itm_round_shield_blue_small_3],
   def_attrib_lvl_18|level(15),wp_one_handed(16)|wp_polearm(150)|wp_throwing(180)|wp_archery(150),knows_skirmisher|knows_ironflesh_5|knows_power_strike_5,celtic_face_1, celtic_face_2],

  ["angle_mercenary","Angle Warrior (Duguthi)","Angle Warriors (Duguthi)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_culture_3,
   [itm_ankle_boots,itm_wrapping_boots,itm_simple_shoes,itm_seax_2,itm_war_spear,itm_battle_axe_5,itm_roman_military_tunic_5,itm_linen_shirt_7,itm_leather_armor_d,itm_mid_generic_mail_15,itm_mid_generic_mail_4,itm_intercisa_helmet_2,itm_burgh_helmet_1,itm_burgh_helmet_mail,itm_burgh_helmet_light,itm_triveres_leather,itm_triveres_mail,itm_drengsted_helmet_mail,itm_drengsted_helmet_leather,itm_round_shield_green_1,itm_round_shield_green_2,itm_round_shield_germanic_5,itm_round_shield_roman_17,itm_iatrus_helmet_mail] + angons,
   def_attrib_lvl_20|level(20),wp(200),knows_lvl_18_inf|knows_shield_3|knows_power_strike_7,germanic_face_1, germanic_face_2],

#SASSANIDS
#infantry + ranged troops first
 ["sassanid_levy","Persian Levy (Payg)","Persian Levies (Paygan)",tf_guarantee_basic,0,0,fac_culture_6,
   [itm_pitch_fork_1,itm_pitch_fork_2,itm_pitch_fork,itm_spear,itm_bamboo_spear,itm_hatchet,itm_sassanid_axe_1,itm_nomad_boots,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_linen_shirt_16,itm_linen_shirt_17,itm_linen_shirt_18,itm_linen_shirt_20,itm_linen_shirt_22,itm_shirt,itm_linen_shirt_22,itm_wicker_shields_rectangular_1,itm_wicker_shields_rectangular_2,itm_wicker_shields_rectangular_3]+tunics_sassanid+hats_sassanids, 
   def_attrib_lvl_13|level(13),wp_one_handed(120)|wp_two_handed(100)|wp_polearm(130),knows_lvl_13_inf|knows_shield_4|knows_power_strike_2,persian_face_1, persian_face_2], 

 ["sassanid_footman","Persian Footman (Nezak-dar)","Persian Footmen (Nezak-daran)",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_6,
   [itm_nomad_boots,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_linen_shirt_16,itm_linen_shirt_17,itm_linen_shirt_18,itm_linen_shirt_20,itm_linen_shirt_22,itm_shirt,itm_linen_shirt_22,itm_wicker_shields_rectangular_1,itm_wicker_shields_rectangular_2,itm_wicker_shields_rectangular_3,itm_wicker_shield_dura_1,itm_wicker_shield_dura_2,itm_wicker_shield_dura_3,itm_tab_shield_pavise_c,itm_tab_shield_pavise_d,itm_medium_spear_1,itm_medium_spear_4,itm_sassanid_axe_1]+tunics_sassanid+helmets_sassanid_1,
   def_attrib_lvl_18|level(18),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (160) | wp_archery (75) | wp_crossbow (75) | wp_throwing (100),knows_lvl_18_inf|knows_shield_6|knows_power_strike_2,persian_face_1, persian_face_2], 
 #could also be referred to as hoplite
 ["sassanid_armored_footman","Persian Armored Footman (Nezak-dar)","Persian Armored Footmen (Nezak-daran)",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_6,
   [itm_nomad_boots,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_war_spear,itm_poleaxe,itm_medium_spear_4,itm_mace_sassanid,itm_samad_sword,
   itm_sassanid_mail_shirt_1,itm_sassanid_mail_shirt_2,itm_sassanid_mail_shirt_3,itm_sassanid_mail_shirt_4,itm_sassanid_mail_shirt_5,itm_sassanid_mail_shirt_6,itm_sassanid_long_mail_1,itm_sassanid_scale_1,itm_sassanid_scale_2,itm_wicker_shield_dura_1,itm_wicker_shield_dura_2,itm_wicker_shield_dura_3,itm_tab_shield_pavise_d]+helmets_sassanid_2,
   def_attrib_lvl_23|level(23),wp_one_handed (180) | wp_two_handed (160) | wp_polearm (190) | wp_archery (75) | wp_crossbow (75) | wp_throwing (160),knows_lvl_23_inf|knows_shield_7|knows_power_strike_3,persian_face_1, persian_face_2], 
  #Selmandan / Skirmisher
 ["sassanid_skirmisher","Persian Skirmisher (Selmandan)","Persian Skirmishers (Selmandan)",tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor,0,0,fac_culture_6,
   [itm_javelin,itm_javelin,itm_sassanid_axe_1,itm_nomad_boots,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_woolen_cap_b,itm_woolen_cap_c,itm_woolen_cap_1,itm_woolen_cap_5,itm_simple_shield_1,itm_simple_shield_2,itm_simple_shield_3,itm_simple_shield_4]+tunics_sassanid_skirmisher+shields_simple,
   def_attrib_skirmisher|level(13),wp_one_handed(120)|wp_two_handed(100)|wp_polearm(120)|wp_throwing(140)|wp_archery(140)|wp_firearm(140),knows_skirmisher,persian_face_1, persian_face_2], 
  #Kamanadaran
 ["sassanid_archer","Persian Archer (Kamanadaran)","Persian Archers (Kamanadaran)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_6,
   [itm_roman_arrows_2,itm_roman_arrows_2,itm_yrzi_bow_1,itm_strong_bow,itm_nomad_boots,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_woolen_cap_b,itm_woolen_cap_c,itm_woolen_cap_1,itm_woolen_cap_5,itm_samad_sword,itm_linen_shirt_16,itm_linen_shirt_17,itm_linen_shirt_18,itm_linen_shirt_20,itm_linen_shirt_22,itm_shirt]+tunics_sassanid+hats_sassanids,
   def_attrib_lvl_18|level(18),wp_one_handed (130) | wp_two_handed (130) | wp_polearm (130) | wp_archery (170) | wp_crossbow (100) | wp_throwing (100),knows_archer,persian_face_1, persian_face_2], 
#cavalry
 ["sassanid_horse_archer","Persian Horse Archer","Persian Horse Archers",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_culture_6,
   [itm_strong_bow,itm_yrzi_bow_1,itm_roman_arrows_1,itm_roman_arrows_1,itm_nomad_boots,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_samad_sword,itm_arabian_horse_a3,itm_arabian_horse_a4,itm_normal_horse14,itm_normal_horse15,itm_normal_horse23,itm_normal_horse24,itm_woolen_cap_b,itm_woolen_cap_c,itm_woolen_cap_1,itm_woolen_cap_5]+tunics_sassanid,
   def_attrib_lvl_18|level(18),wp_one_handed (130) | wp_two_handed (130) | wp_polearm (130) | wp_archery (170) | wp_crossbow (100) | wp_throwing (100),knows_horse_archer,persian_face_1, persian_face_2], 

 ["sassanid_cavalry","Persian Cavalry (Aswar)","Persian Cavalry (Aswaran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_culture_6,
   [itm_normal_horse14,itm_normal_horse15,itm_normal_horse23,itm_normal_horse24,itm_tab_shield_small_round_c,itm_nomad_boots,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,
   itm_sassanid_mail_shirt_1,itm_sassanid_mail_shirt_2,itm_sassanid_mail_shirt_3,itm_sassanid_mail_shirt_4,itm_sassanid_mail_shirt_5,itm_sassanid_mail_shirt_6,itm_sassanid_long_mail_1,itm_sassanid_scale_1,itm_sassanid_scale_2,itm_sassanid_lamellenhelm_1,itm_sassanid_lamellenhelm_2,itm_sassanid_lamellenhelm_3,itm_sassanid_lamellenhelm_4,itm_sassanid_lamellenhelm_5,itm_lance,itm_samad_sword,itm_mace_sassanid,itm_yrzi_bow_1,itm_roman_arrows_2]+helmets_sassanid_2,
   def_attrib_lvl_23|level(23),wp_one_handed(190)|wp_two_handed(180)|wp_polearm(200)|wp_archery(150),knows_lvl_23_cav|knows_shield_4|knows_power_strike_5|knows_horse_archery_4,persian_face_1, persian_face_2],

 ["sassanid_cataphract","Persian Cataphract (Grivpanvar)","Persian Cataphracts (Grivpanvar)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_culture_6,
   [itm_heavy_lance,itm_long_lance,itm_mace_sassanid,itm_ingushetia_spatha,itm_sarranid_elite_armor,itm_long_cataphract_mail,itm_cataphract_armor_1,itm_cataphract_armor_4,itm_cataphract_armor_5,itm_sarranid_horseman_helmet,itm_tsaritsyno_1,itm_tsaritsyno_1_veiled,itm_sassanid_lamellenhelm_4,itm_sassanid_lamellenhelm_5,itm_sassanid_cataphract_helmet_1,itm_sassanid_cataphract_helmet_2,itm_sassanid_cataphract_helmet_3,itm_sassanid_cataphract_helmet_4,itm_sassanid_cataphract_helmet_5,itm_sassanid_helmet_mail_4,itm_sassanid_helmet_mail_5,
   itm_warhorse,itm_cataphract_horse_1,itm_cataphract_horse_4,itm_cataphract_horse_5,itm_half_cataphract_horse_3,itm_half_cataphract_horse_4,itm_half_cataphract_horse_7,itm_leather_gloves,itm_roman_arrows_2,itm_strong_bow,itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_heavy_greaves,itm_mail_boots_manica_1,itm_mail_boots_manica_2],
   def_attrib_lvl_28|level(28),wp_one_handed (220) | wp_two_handed (220) | wp_polearm (240) | wp_archery (160) | wp_crossbow (75) | wp_throwing (120),knows_cataphract,persian_face_1, persian_face_2],

 ["sassanid_bodyguard","Persian Bodyguard (Pustigban)","Persian Bodyguards (Pustigban)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_culture_6,
   [itm_battle_axe,itm_mace_sassanid,itm_sassanid_greatsword,itm_ingushetia_spatha,itm_long_lance,itm_tab_shield_small_round_c,itm_cataphract_armor_1,itm_cataphract_armor_4,itm_cataphract_armor_5,itm_sassanid_cataphract_helmet_1,itm_sassanid_cataphract_helmet_2,itm_sassanid_cataphract_helmet_3,itm_sassanid_cataphract_helmet_4,itm_sassanid_cataphract_helmet_5,itm_tsaritsyno_1_veiled,itm_sassanid_mask_helmet_1,itm_sassanid_mask_helmet_2,itm_sassanid_mask_helmet_3,
    itm_cataphract_horse_1,itm_cataphract_horse_4,itm_cataphract_horse_5,itm_half_cataphract_horse_3,itm_half_cataphract_horse_4,itm_mail_boots,itm_heavy_greaves,itm_mail_boots_manica_1,itm_mail_boots_manica_2,itm_mail_mittens,itm_leather_gloves,itm_niya_bow_2,itm_khergit_arrows],
   def_attrib_lvl_32|level(32),wp_one_handed (240) | wp_two_handed (240) | wp_polearm (250) | wp_archery (170) | wp_crossbow (75) | wp_throwing (120),knows_lvl_30_cav|knows_shield_3|knows_power_strike_7|knows_horse_archery_5,persian_face_1, persian_face_2], 

 ["sassanid_officer","Persian Officer (Dezhban)","Persian Officers (Dezhban)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_culture_6,
   [itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_sassanid_scale_2,itm_sassanid_mail_shirt_3,itm_sassanid_helmet_mail_4,itm_sassanid_helmet_mail_5,itm_leather_gloves,itm_ingushetia_spatha,itm_tab_shield_small_round_c],
   def_attrib_lvl_30|level(30),wp_one_handed(220)|wp_two_handed(220)|wp_polearm(210)|wp_archery(120)|wp_throwing(200),knows_lvl_30_inf|knows_shield_5|knows_power_strike_7|knows_trainer_4,persian_face_1, persian_face_2], 

 ["sassanid_camel_rider","Persian Camel Rider","Persian Camel Riders",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_culture_6,
   [itm_nomad_boots,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_samad_sword,itm_heavy_lance,itm_camel]+tunics_sassanid+helmets_sassanid_1,
   def_attrib_lvl_18|level(18),wp_one_handed (170) | wp_two_handed (150) | wp_polearm (180) | wp_archery (75) | wp_crossbow (75) | wp_throwing (100),knows_lvl_18_cav|knows_shield_2|knows_power_strike_6,persian_face_1, persian_face_2], 

 ["sassanid_guard_spearman","Persian Guard (Ham-Harz)","Persian Guards (Ham-Harzan)",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_6,
   [itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_polehammer,itm_mace_sassanid,itm_long_cataphract_mail,itm_sassanid_long_mail_1,itm_sassanid_scale_1,itm_sassanid_scale_2,itm_sassanid_cataphract_helmet_1,itm_sassanid_helmet_mail_4,itm_sassanid_helmet_mail_5,itm_wicker_shield_dura_1,itm_wicker_shield_dura_2,itm_wicker_shield_dura_3,itm_tab_shield_pavise_d],
   def_attrib_lvl_28|level(28),wp_one_handed (210) | wp_two_handed (160) | wp_polearm (230) | wp_archery (75) | wp_crossbow (75) | wp_throwing (160),knows_lvl_28_inf|knows_shield_8|knows_power_strike_4,persian_face_1, persian_face_2], 

#auxiliary
 ["sassanid_roman_deserter","Greco-Roman Cavalry (Jansepar)","Greco-Roman Cavalry (Janseparan)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_culture_6,
   [itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_coat_of_plates_red,itm_arabian_armor_b,itm_tarasovsky_1784_helmet_mail_2,itm_sassanid_helmet_mail_1,itm_sassanid_helmet_mail_2,itm_sassanid_helmet_mail_3,itm_sarranid_horseman_helmet,itm_mace_roman_1,itm_heavy_lance,itm_warhorse,itm_half_cataphract_horse_1,itm_half_cataphract_horse_2]+greaves_roman,
   def_attrib_lvl_23|level(23),wp_one_handed(190)|wp_two_handed(180)|wp_polearm(200)|wp_archery(150),knows_lvl_23_cav|knows_shield_4|knows_power_strike_5|knows_horse_archery_4,roman_face_1, roman_face_2],

 #daylamites
 ["daylamite_hillman","Daylamite Hillman","Daylamite Hillmen",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_6,
   [itm_nomad_boots,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_kaftan_sheepskin_1,itm_kaftan_sheepskin_2,itm_kaftan_sheepskin_3,itm_kaftan_sheepskin_4,itm_kaftan_sheepskin_5,itm_woolen_cap_b,itm_woolen_cap_c,itm_woolen_cap_1,itm_woolen_cap_5,itm_sassanid_axe_1,itm_javelin,itm_javelin]+shields_simple+shields_small,
   def_attrib_lvl_18|level(18),wp_one_handed (170) | wp_two_handed (160) | wp_polearm (160) | wp_archery (75) | wp_crossbow (75) | wp_throwing (160),knows_lvl_18_inf|knows_shield_3|knows_power_strike_5,persian_face_1, persian_face_2], 

 ["daylamite_infantry","Daylamite Infantryman","Daylamite Infantrymen",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_6,
   [itm_nomad_boots,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_samad_sword,itm_sassanid_war_axe_1,itm_javelin,itm_javelin,itm_sassanid_mail_shirt_1,itm_sassanid_mail_shirt_2,itm_sassanid_mail_shirt_3,itm_sassanid_mail_shirt_4,itm_sassanid_mail_shirt_5,itm_sassanid_mail_shirt_6,itm_sassanid_scale_1,itm_sassanid_scale_2,itm_tab_shield_round_e]+helmets_sassanid_2,
   def_attrib_lvl_23|level(23),wp_one_handed (230) | wp_two_handed (200) | wp_polearm (220) | wp_archery (75) | wp_crossbow (75) | wp_throwing (230),knows_lvl_23_inf|knows_shield_4|knows_power_strike_6,persian_face_1, persian_face_2], 
#kurds
 ["kurdish_javelinman","Kurdish Javelinman","Kurdish Javelinmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_6,
   [itm_throwing_spears,itm_throwing_spears,itm_throwing_spears,itm_sassanid_axe_1,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_kaftan_sheepskin_1,itm_kaftan_sheepskin_2,itm_kaftan_sheepskin_3,itm_kaftan_tunic_1,itm_kaftan_tunic_2,itm_kaftan_tunic_3,itm_kaftan_tunic_6,itm_woolen_cap_b,itm_woolen_cap_1,itm_woolen_cap_4,itm_woolen_cap_6,itm_bandana2,itm_bandana1],
   def_attrib_lvl_18|level(17),wp_one_handed (170) | wp_two_handed (140) | wp_polearm (170) | wp_archery (140) | wp_crossbow (100) | wp_throwing (190),knows_lvl_18_inf|knows_shield_2|knows_power_strike_5|knows_power_throw_6,persian_face_1, persian_face_2], 

 ["kurdish_slinger","Kurdish Slinger","Kurdish Slingers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_6,
   [itm_sassanid_axe_1,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_kaftan_sheepskin_1,itm_kaftan_sheepskin_2,itm_kaftan_sheepskin_3,itm_kaftan_tunic_1,itm_kaftan_tunic_2,itm_kaftan_tunic_3,itm_kaftan_tunic_6,itm_woolen_cap_b,itm_woolen_cap_1,itm_woolen_cap_4,itm_woolen_cap_6,itm_bandana2,itm_bandana1,itm_flintlock_pistol,itm_sling_bullet,itm_sling_bullet],
   def_attrib_lvl_18|level(17),wp_one_handed (160) | wp_two_handed (140) | wp_polearm (160) | wp_archery (140) | wp_crossbow (100) | wp_throwing (140) | wp_firearm(190),knows_lvl_18_inf|knows_power_strike_5|knows_athletics_7|knows_shield_2,persian_face_1, persian_face_2], 
#armenians
 ["armenian_bowman","Armenian Bowman","Armenian Bowmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_6,
   [itm_barbed_arrows,itm_barbed_arrows,itm_strong_bow,itm_nomad_boots,itm_kaftan_sheepskin_1,itm_kaftan_sheepskin_2,itm_skirmisher_tunic_1,itm_skirmisher_tunic_4,itm_kaftan_tunic_1,itm_kaftan_tunic_2,itm_hand_axe,itm_bandana1,itm_bandana2,itm_woolen_cap_simple_4],
   def_attrib_lvl_18|level(17),wp_one_handed (100) | wp_two_handed (80) | wp_polearm (100) | wp_archery (200) | wp_crossbow (100) | wp_throwing (100),knows_athletics_5|knows_ironflesh_5|knows_power_draw_6|knows_power_strike_6|knows_power_throw_3|knows_riding_3|knows_weapon_master_5|knows_inventory_management_3,caucaus_face_1, caucaus_face_2], 

 ["armenian_footman","Armenian Footman (Payik)","Armenian Footmen (Payik)",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_6,
   [itm_boar_spear,itm_medium_spear_4,itm_battle_axe_1,itm_javelin,itm_nomad_boots,itm_kaftan_sheepskin_1,itm_kaftan_sheepskin_2,itm_skirmisher_tunic_1,itm_skirmisher_tunic_4,itm_kaftan_tunic_1,itm_kaftan_tunic_2,itm_woolen_cap_simple_4,itm_tarasovsky_1784_helmet_cloth,itm_wicker_shields_rectangular_1,itm_wicker_shields_rectangular_2,itm_wicker_shields_rectangular_3],
   def_attrib_lvl_18|level(18),wp_one_handed(180)|wp_two_handed(140)|wp_polearm(180)|wp_throwing(170)|wp_archery(100),knows_lvl_18_inf|knows_power_strike_4|knows_shield_4,caucaus_face_1, caucaus_face_2],

 ["armenian_cataphract","Armenian Noble (Naxarar)","Armenian Nobles (Naxarars)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_culture_6,
   [itm_heavy_lance,itm_strong_bow,itm_barbed_arrows,itm_ingushetia_spatha,itm_tab_shield_small_round_c,itm_heavy_greaves,itm_sassanid_cavalry_boots_2,itm_mail_boots_manica_1,itm_mail_boots_manica_2,itm_leather_gloves,itm_coat_of_plates_red,itm_long_cataphract_mail,itm_eastern_scale_1,itm_eastern_scale_2,itm_tsaritsyno_1_veiled,itm_tsaritsyno_1,itm_sarranid_horseman_helmet,itm_half_cataphract_horse_3,itm_half_cataphract_horse_4,itm_cataphract_horse_4,itm_cataphract_horse_5],
   def_attrib_lvl_30|level(30),wp_one_handed (240) | wp_two_handed (190) | wp_polearm (230) | wp_archery (150) | wp_crossbow (100) | wp_throwing (100),knows_lvl_30_cav|knows_power_strike_5|knows_horse_archery_5|knows_shield_1,caucaus_face_1, caucaus_face_2], 
#others
 #sword armed - glass cannon like infantry recruited from castle_10
 ["parizi_warrior","Parizi Warrior","Parizi Warriors",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_6,
   [itm_nomad_boots,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_skirmisher_tunic_3,itm_kaftan_sheepskin_2,itm_kaftan_sheepskin_4,itm_sassanid_scale_1,itm_sassanid_scale_2,itm_sassanid_lamellenhelm_2,itm_sassanid_helmet_cloth_1,itm_sassanid_helmet_mail_1,itm_concave_shield_green_small_1,itm_concave_shield_green_small_2,itm_ingushetia_spatha,itm_throwing_spear_1,itm_throwing_spear_1],
   def_attrib_lvl_23|level(22),wp_one_handed (220) | wp_two_handed (220) | wp_polearm (190) | wp_archery (75) | wp_crossbow (75) | wp_throwing (190),knows_lvl_23_inf|knows_shield_3|knows_power_strike_7,persian_face_1, persian_face_2], 
 #Skirmisher cavalry, from gilan
 ["gilan_horseman","Gilan Horseman","Gilan Horsemen",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_culture_6,
   [itm_nomad_boots,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_skirmisher_tunic_1,itm_skirmisher_tunic_2,itm_kaftan_sheepskin_1,itm_kaftan_sheepskin_2,itm_kaftan_sheepskin_3,itm_cavalry_javelins,itm_cavalry_javelins,itm_battle_axe_4,itm_medium_spear_4,itm_normal_horse14,itm_normal_horse15,itm_normal_horse23,itm_normal_horse24],
   def_attrib_lvl_18|level(18),wp_one_handed (170) | wp_two_handed (130) | wp_polearm (170) | wp_archery (130) | wp_crossbow (100) | wp_throwing (190),knows_athletics_3|knows_riding_6|knows_ironflesh_2|knows_power_throw_6|knows_weapon_master_5|knows_inventory_management_3|knows_power_strike_6|knows_horse_archery_5,persian_face_1, persian_face_2], 

 ["chionite_horse_archer","Chionite Horse Archer","Chionite Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_culture_12,
   [itm_nomad_boots,itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_kaftan_eastern_1,itm_kaftan_eastern_2,itm_kaftan_hunnic_blue,itm_kaftan_hunnic_red,itm_chionite_hat_1,itm_chionite_hat_2,itm_chionite_hat_3,itm_chionite_hat_4,itm_chionite_hat_5,itm_normal_horse18,itm_normal_horse19,itm_steppe_horse,itm_steppe_horse,itm_normal_horse14,itm_normal_horse15,itm_normal_horse16,itm_normal_horse17,itm_khergit_bow,itm_sword_khergit_1,itm_khergit_arrows,itm_khergit_arrows]+horses_hunnic_1,
   def_attrib_lvl_18|level(17),wp_one_handed(150)|wp_two_handed(150)|wp_polearm(150)|wp_throwing(150)|wp_archery(170),knows_horse_archer,hunnic_face_1, hunnic_face_2],

 ["albanian_cavalry","Arran Cavalry","Arran Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_culture_6,
   [itm_long_lance,itm_khergit_bow,itm_khergit_arrows,itm_ingushetia_spatha,itm_sassanid_cavalry_boots_2,itm_leather_gloves,itm_long_cataphract_mail,itm_eastern_scale_5,itm_eastern_scale_6,itm_cataphract_armor_1,itm_tsaritsyno_1,itm_tarasovsky_1784_helmet_mail_1,itm_tarasovsky_1784_helmet_mail_2,itm_half_cataphract_horse_3,itm_half_cataphract_horse_4,itm_cataphract_horse_4,itm_cataphract_horse_5],
   def_attrib_lvl_28|level(28),wp_one_handed (230) | wp_two_handed (190) | wp_polearm (230) | wp_archery (150) | wp_crossbow (100) | wp_throwing (100),knows_lvl_28_cav|knows_power_strike_8|knows_horse_archery_4,caucaus_face_1, caucaus_face_2], 

 ["hephthalite_mercenary","Hephthalite Mercenary","Hephthalite Mercenaries",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_polearm,0,0,fac_culture_6,
   [itm_heavy_greaves,itm_sarranid_boots_b,itm_kizil_composite_armor,itm_kaftan_lamellar_12,itm_kaftan_lamellar_13,itm_sassanid_lamellenhelm_1,itm_rozhdestvensky_helmet_mail,itm_sword_khergit_1,itm_heavy_lance,itm_khergit_arrows,itm_khergit_bow,itm_warhorse_steppe],
   def_attrib_lvl_28|level(28),wp_one_handed(220)|wp_two_handed(220)|wp_polearm(250)|wp_throwing(200)|wp_archery(170),knows_riding_8|knows_horse_archery_8|knows_power_strike_7|knows_power_draw_5|knows_ironflesh_8|knows_athletics_3|knows_inventory_management_3|knows_shield_2|knows_power_throw_2,hunnic_face_1, hunnic_face_2],

#end auxiliaries
 ["sassanid_standard_bearer","Persian Standard Bearer","Persian Standard Bearers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_culture_6,
   [itm_nomad_boots,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_woolen_cap_b,itm_woolen_cap_c,itm_woolen_cap_1,itm_woolen_cap_5,itm_linen_shirt_16,itm_linen_shirt_17,itm_linen_shirt_18,itm_linen_shirt_20,itm_linen_shirt_22,itm_shirt,itm_linen_shirt_22,itm_flag_pole_1]+tunics_sassanid+helmets_sassanid_1,
   def_attrib_lvl_18|level(18),wp_one_handed (160) | wp_two_handed (180) | wp_polearm (180) | wp_archery (75) | wp_crossbow (75) | wp_throwing (100),knows_common|knows_athletics_4|knows_ironflesh_3|knows_power_strike_3,persian_face_1, persian_face_2], 

 ["sassanid_messenger","Sassanid Messenger","Sassanid Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_culture_6,
   [itm_nomad_boots,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_hunter,itm_arabian_horse_a3,itm_arabian_horse_a4,itm_normal_horse14,itm_normal_horse15,itm_normal_horse23,itm_normal_horse24,itm_medium_spear_1,itm_medium_spear_2]+tunics_sassanid+helmets_sassanid_1,
   def_attrib_lvl_23|level(25),wp(200),knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_power_throw_2|knows_horse_archery_2,persian_face_1, persian_face_2], 
 ["sassanid_deserter","Persian Deserter","Persian Deserters",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_6,
   [itm_nomad_boots,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_linen_shirt_16,itm_linen_shirt_17,itm_linen_shirt_18,itm_linen_shirt_20,itm_linen_shirt_22,itm_shirt,itm_linen_shirt_22,itm_wicker_shields_rectangular_1,itm_wicker_shields_rectangular_2,itm_wicker_shields_rectangular_3,itm_wicker_shield_dura_1,itm_wicker_shield_dura_2,itm_wicker_shield_dura_3,itm_tab_shield_pavise_c,itm_tab_shield_pavise_d,itm_medium_spear_1,itm_medium_spear_4,itm_sassanid_axe_1]+tunics_sassanid+helmets_sassanid_1,
   def_attrib_lvl_18|level(17),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (160) | wp_archery (75) | wp_crossbow (75) | wp_throwing (100),knows_lvl_18_inf|knows_shield_6|knows_power_strike_2,persian_face_1, persian_face_2], 
 ["sassanid_prison_guard","Prison Guard","Prison Guards",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_6,
   [itm_sassanid_cavalry_boots_1,itm_war_spear,itm_mace_sassanid,itm_sassanid_long_mail_1,itm_wicker_shield_dura_1,itm_wicker_shield_dura_2,itm_wicker_shield_dura_3,itm_tab_shield_pavise_d]+helmets_sassanid_2,
   def_attrib_lvl_28|level(26),wp(230),knows_lvl_28_inf|knows_shield_6|knows_power_strike_3,persian_face_1, persian_face_2], 
 ["sassanid_castle_guard","Castle Guard","Castle Guards",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_6,
   [itm_sassanid_cavalry_boots_1,itm_war_spear,itm_mace_sassanid,itm_sassanid_long_mail_1,itm_wicker_shield_dura_1,itm_wicker_shield_dura_2,itm_wicker_shield_dura_3,itm_tab_shield_pavise_d]+helmets_sassanid_2,
   def_attrib_lvl_28|level(26),wp(230),knows_lvl_28_inf|knows_shield_6|knows_power_strike_3,persian_face_1, persian_face_2], 

#WESTERN GERMANS
  ["western_germanic_freeman","W. Germanic Freeman (Karli)","W. Germanic Freemen (Karlo)",tf_guarantee_basic,0,0,fac_culture_7,
   [itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_club,itm_winged_mace,itm_mace_1,
   itm_spear,itm_seax_1,itm_long_seax_1,itm_seax_9,itm_fighting_axe,itm_basic_axe,itm_battle_axe_1,itm_battle_axe_3,itm_bearded_axe_1,itm_roman_spear_1,itm_medium_spear_1,itm_medium_spear_2,itm_medium_spear_4,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_ridge_helm_c,itm_narona_bandhelm_leather,itm_triveres_leather,(itm_intercisa_helmet_1,imod_battered),itm_burgh_helmet_light]+tunics_western_germanic+shoes_generic+hats_german+shields_western_germanic_1+shields_generic+angons+cloaked_tunics_western_germanic,
   def_attrib_lvl_18|level(18),wp_one_handed(180)|wp_two_handed(150)|wp_polearm(180)|wp_throwing(170)|wp_archery(100),knows_lvl_18_inf|knows_shield_4|knows_power_strike_4,germanic_face_1, germanic_face_2],

  ["western_germanic_retainer","W. Germanic Retainer (Sagi)","W. Germanic Retainers (Sagjo)",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_7,
   [itm_tab_shield_round_d,itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_leather_armor_d,itm_leather_armor_e,itm_short_ragged_mail_4,itm_short_ragged_mail_7,itm_short_ragged_mail_8,itm_mid_generic_mail_8,itm_mid_generic_mail_15,itm_mid_generic_mail_17,itm_mid_generic_mail_20,itm_mid_generic_mail_23,itm_mid_generic_mail_26,
   itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_iatrus_1,itm_burgh_helmet_1,itm_ridge_helm_c,itm_koblenz_helmet_1,itm_fernpass_helmet_1,itm_fernpass_helmet_2,itm_fernpass_helmet_3,itm_christies_helmet_1,itm_triveres_mail,itm_narona_bandhelm_mail,itm_burgh_helmet_mail,itm_war_spear,itm_poleaxe,itm_sword_viking_1,itm_sword_medieval_a,itm_sword_medieval_c,itm_long_seax_3,itm_battle_axe_4,itm_battle_axe_3,itm_bearded_axe_2,itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4]+shoes_generic+shields_western_germanic_2+cloaked_tunics_western_germanic+angons,
   def_attrib_lvl_23|level(23),wp_one_handed(210)|wp_two_handed(170)|wp_polearm(210)|wp_throwing(200)|wp_archery(100),knows_lvl_23_inf|knows_shield_4|knows_power_strike_6,germanic_face_1, germanic_face_2],

  ["western_germanic_skirmisher","W. Germanic Skirmisher (Jugunthi)","W. Germanic Skirmishers (Jugunthi)",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_culture_7,
   [itm_javelin,itm_javelin,itm_wooden_javelin,itm_wooden_javelin,itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_brown_hood1,itm_new_hood_b,itm_new_hood_c,itm_new_hood_d,itm_leather_cap,itm_club,itm_winged_mace,itm_fighting_axe,itm_seax_9]+tunics_western_germanic+shields_simple+hats_german+shoes_generic,
   def_attrib_skirmisher|level(13),wp_one_handed(140)|wp_two_handed(120)|wp_polearm(130)|wp_archery(120)|wp_throwing(150),knows_skirmisher,germanic_face_1, germanic_face_2],

  ["western_germanic_bowman","W. Germanic Bowman (Bogomanna)","W. Germanic Bowmen (Bogomanni)",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_culture_7,
   [itm_short_bow,itm_hunting_bow,itm_long_bow,itm_germanic_arrows,itm_germanic_arrows,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_brown_hood1,itm_new_hood_b,itm_new_hood_c,itm_new_hood_d,itm_leather_cap,itm_battle_axe_1]+tunics_western_germanic+hats_german+shoes_generic,
   def_attrib_lvl_18|level(18),wp_one_handed(160)|wp_two_handed(130)|wp_polearm(150)|wp_archery(150)|wp_throwing(120),knows_archer,germanic_face_1, germanic_face_2],

  ["western_germanic_companion","W. Germanic Companion (Gasintho)","W. Germanic Companions (Gasinthos)",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_culture_7,
   [itm_tab_shield_small_round_c,itm_tab_shield_small_round_b,itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_roman_squamata_5,itm_mid_generic_mail_4,itm_mid_generic_mail_5,itm_mid_generic_mail_13,itm_mid_generic_mail_18,itm_mid_generic_mail_19,itm_long_mail_new_3,itm_long_mail_new_8,itm_long_mail_new_9,itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,
   itm_triveres_mail,itm_koblenz_helmet_1,itm_koblenz_helmet_2,itm_burgh_helmet_1,itm_burgh_helmet_2,itm_fernpass_helmet_2,itm_gultlingen_helmet,itm_gultlingen_helmet_mail,itm_christies_helmet_1,itm_augsburg_2_helmet,itm_augsburg_1_helmet,itm_augsburg_2_helmet_mail,itm_intercisa_helmet_gilded_1,itm_iatrus_1,itm_iatrus_2,itm_war_spear,itm_poleaxe,itm_sword_viking_3,itm_sword_viking_3_small]+horses_germanic_3+horses_germanic_4+shields_western_germanic_cavalry_1,
   def_attrib_lvl_28|level(28),wp_one_handed(240)|wp_two_handed(220)|wp_polearm(240)|wp_throwing(200)|wp_archery(100),knows_lvl_28_cav|knows_shield_3|knows_power_strike_7,germanic_face_1, germanic_face_2],

  ["western_germanic_messenger","W. Germanic Messenger","W. Germanic Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_culture_7,
   [itm_tab_shield_round_c,itm_sword_medieval_a,itm_leather_armor_c,itm_spear,itm_wrapping_boots,itm_intercisa_helmet_1]+horses_2,
   def_attrib_lvl_23|level(25),wp(200),knows_common|knows_riding_7|knows_horse_archery_5,germanic_face_1, germanic_face_2],
  ["western_germanic_deserter","W. Germanic Deserter","W. Germanic Deserters",tf_guarantee_basic,0,0,fac_culture_7,
   [itm_cloaked_tunic_4,itm_cloaked_tunic_5,itm_cloaked_tunic_9,itm_cloaked_tunic_10,itm_cloaked_tunic_11,itm_cloaked_tunic_12,itm_cloaked_tunic_17,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,
   itm_spear,itm_seax_1,itm_seax_9,itm_fighting_axe,itm_roman_spear_1,itm_medium_spear_1,itm_medium_spear_2,itm_medium_spear_4,itm_ridge_helm_c,itm_triveres_leather,(itm_intercisa_helmet_1,imod_battered)]+tunics_western_germanic+shoes_generic+hats_german+shields_western_germanic_1+shields_generic+angons,
   def_attrib_lvl_18|level(18),wp_one_handed(180)|wp_two_handed(150)|wp_polearm(180)|wp_throwing(170)|wp_archery(100),knows_lvl_18_inf|knows_shield_4|knows_power_strike_4,germanic_face_1, germanic_face_2],
  ["western_germanic_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_culture_7,
   [itm_tab_shield_round_d,itm_roman_squamata_5,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,
   itm_triveres_mail,itm_koblenz_helmet_1,itm_burgh_helmet_1,itm_fernpass_helmet_2,itm_war_spear,itm_battle_axe_3],
   def_attrib_lvl_28|level(28),wp(230),knows_lvl_28_inf|knows_shield_6|knows_power_strike_6,germanic_face_1, germanic_face_2],
  ["western_germanic_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_culture_7,
   [itm_tab_shield_round_d,itm_roman_squamata_5,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,
   itm_triveres_mail,itm_koblenz_helmet_1,itm_burgh_helmet_1,itm_fernpass_helmet_2,itm_war_spear,itm_battle_axe_3],
   def_attrib_lvl_28|level(28),wp(230),knows_lvl_28_inf|knows_shield_6|knows_power_strike_6,germanic_face_1, germanic_face_2],

#AOR TROOPS - western germanic
#suebi
  ["burii_retainer","Burii Retainer (Sagi)","Burii Retainers (Sagjos)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm,no_scene,reserved,fac_culture_7,
   [itm_ankle_boots,itm_wrapping_boots,itm_nomad_boots,itm_eastern_germanic_shield_1,itm_eastern_germanic_shield_2,itm_eastern_germanic_shield_3,itm_eastern_germanic_shield_4,itm_eastern_germanic_shield_5,itm_eastern_germanic_shield_6,itm_tab_shield_round_c,itm_linen_shirt_8,itm_linen_shirt_16,itm_linen_shirt_20,itm_linen_shirt_21,itm_linen_shirt_22,itm_cloaked_tunic_4,itm_cloaked_tunic_5,itm_cloaked_tunic_16,itm_p_hood,(itm_intercisa_helmet_1,imod_battered),(itm_intercisa_helmet_2,imod_battered),(itm_augst_helmet_1,imod_battered),itm_poleaxe,itm_poleaxe,itm_seax_1,itm_long_seax_3,itm_battle_axe_3] + throwing_spears_1,
   def_attrib_lvl_20|level(20),wp_one_handed(210)|wp_two_handed(200)|wp_polearm(220)|wp_throwing(190),knows_lvl_18_inf|knows_shield_6|knows_power_strike_4,germanic_face_1, germanic_face_2],
  ["suebi_swordsman","Spatharius Comitatus Suevorum","Spatharii Comitati Suevorum",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,no_scene,reserved,fac_culture_7,
   [itm_ankle_greaves,itm_sword_viking_3,itm_long_mail_new_3,itm_long_mail_new_1,itm_long_mail_new_2,itm_long_mail_new_4,itm_mid_generic_mail_3,itm_mid_generic_mail_5,itm_mid_generic_mail_2,itm_mid_generic_mail_1,itm_leather_gloves,itm_gultlingen_helmet,itm_gultlingen_helmet_mail,itm_koblenz_helmet_2,itm_burgh_helmet_2,itm_koblenz_helmet_3,itm_tab_shield_round_d,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c] + throwing_spears_1,
   def_attrib_lvl_30|level(30),wp_one_handed(250)|wp_two_handed(230)|wp_polearm(240)|wp_throwing(260),knows_lvl_30_inf|knows_shield_4|knows_power_strike_7,germanic_face_1, germanic_face_2],
  ["quadi_spearman","Quadi Spearman (Gairmanna)","Quadi Spearmen (Gairmanni)",tf_guarantee_basic,0,0,fac_culture_7,
   [itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_4,itm_generic_tunic_2,itm_generic_tunic_14,itm_cloaked_tunic_17,itm_cloaked_tunic_5,itm_generic_tunic_10,itm_poleaxe,itm_great_lance,itm_fighting_axe,itm_round_shield_germanic_7,itm_concave_shield_germanic_8]+shoes_generic+germanic_caps,
   def_attrib_lvl_20|level(18),wp_one_handed(190)|wp_two_handed(150)|wp_polearm(190)|wp_throwing(190)|wp_archery(100),knows_lvl_18_inf|knows_shield_6|knows_power_strike_3,germanic_face_1, germanic_face_2],

#alamans
  ["brisgavi_retainer","Brisgavi Retainer (Sagi)","Brisgavi Retainers (Sagjos)",tf_guarantee_basic,0,0,fac_culture_7,
   [itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_woolen_cap_2,itm_woolen_cap_c,itm_woolen_cap_3,(itm_intercisa_helmet_1,imod_battered),itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,itm_generic_tunic_4,itm_generic_tunic_6,itm_generic_tunic_13,itm_cloaked_tunic_5,itm_cloaked_tunic_9,itm_cloaked_tunic_12,itm_round_shield_germanic_2,itm_war_spear,itm_sword_viking_1]+shoes_generic,
   def_attrib_lvl_18|level(19),wp_one_handed(200)|wp_two_handed(150)|wp_polearm(200)|wp_throwing(170)|wp_archery(100),knows_lvl_18_inf|knows_shield_5|knows_power_strike_4,germanic_face_1, germanic_face_2],
  ["lentienses_foederati","Lentienses Foederati","Lentienses Foederati",tf_guarantee_basic,0,0,fac_culture_7,
   [itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_3,itm_cloaked_tunic_8,itm_cloaked_tunic_10,itm_cloaked_tunic_5,itm_round_shield_yellow_1,itm_round_shield_blue_2,itm_ridge_helm_c,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_roman_spear_3,itm_throwing_axes,itm_throwing_axes]+shoes_generic,
   def_attrib_lvl_18|level(18),wp_one_handed(190)|wp_two_handed(150)|wp_polearm(190)|wp_throwing(190)|wp_archery(100),knows_lvl_18_inf|knows_shield_3|knows_power_strike_5,germanic_face_1, germanic_face_2],
  ["bucinobantes_oathgiver","Bucinobantes Oath-giver (Herthganauti)","Bucinobantes Oath-givers (Herthganauto)",tf_mounted|tf_guarantee_basic|tf_guarantee_horse,0,0,fac_culture_7,
   [itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,itm_cloaked_tunic_5,itm_cloaked_tunic_10,itm_cloaked_tunic_17,itm_mid_generic_mail_18,itm_mid_generic_mail_19,itm_intercisa_helmet_2,itm_augsburg_2_helmet,itm_augsburg_1_helmet,itm_augsburg_2_helmet_mail,itm_christies_helmet_1,itm_iatrus_1,itm_fernpass_helmet_1,itm_concave_shield_germanic_6,itm_concave_shield_germanic_15,itm_war_spear,itm_sword_viking_3_small]+shoes_generic+horses_germanic_2+horses_germanic_3,
   def_attrib_lvl_23|level(23),wp_one_handed(200)|wp_two_handed(150)|wp_polearm(210)|wp_throwing(170)|wp_archery(100),knows_lvl_23_cav|knows_shield_3|knows_power_strike_6,germanic_face_1, germanic_face_2],

  ["latro_alpium","Latro Alpium","Latrones Alpinorum",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_kingdom_1,
   [itm_roman_spear_2,itm_dagger,itm_securis,itm_javelin,itm_javelin,itm_shirt,itm_linen_shirt,itm_linen_tunic,itm_linen_shirt_10,itm_linen_shirt_14,itm_cloaked_tunic_5,itm_generic_tunic_14,itm_cloaked_tunic_17,itm_cloaked_tunic_10]+shoes_roman+pannonian_hats+shields_small+shields_simple,
   def_attrib_skirmisher|level(13),wp_one_handed(150)|wp_two_handed(140)|wp_polearm(160)|wp_throwing(170)|wp_archery(130),knows_skirmisher,briton_face_1, briton_face_2],
  #Historical notes: these are impoverished provincials of the Alps of celtic culture, former roman subjects, becoming bandits

#frankish
  ["chamavi_footman","Chamavi Follower (Thegn)","Chamavi Followers (Thegno)",tf_guarantee_basic,0,0,fac_culture_7,
   [itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_cloaked_tunic_12,itm_generic_tunic_4,itm_generic_tunic_7,itm_generic_tunic_8,itm_leather_cap,itm_triveres_leather,itm_seax_1,itm_medium_spear_4,itm_battle_axe_3,itm_battle_axe_4,itm_concave_shield_germanic_13,itm_concave_shield_germanic_14,itm_heavy_throwing_axes,itm_heavy_throwing_axes]+shoes_generic+angons,
   def_attrib_lvl_20|level(19),wp_one_handed(200)|wp_two_handed(170)|wp_polearm(180)|wp_throwing(200)|wp_archery(100),knows_lvl_18_inf|knows_shield_4|knows_power_strike_7,germanic_face_1, germanic_face_2],
  ["bructeri_skirmisher","Bructeri Skirmisher (Jugunthi)","Bructeri Skirmishers (Jugunthi)",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_culture_7,
   [itm_jarid,itm_jarid,itm_generic_tunic_3,itm_generic_tunic_14,itm_generic_tunic_15,itm_linen_shirt_12,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_brown_hood1,itm_leather_cap,itm_battle_axe,itm_seax_1]+shields_small+hats_german+shoes_generic,
   def_attrib_lvl_18|level(16),wp_one_handed(150)|wp_two_handed(90)|wp_polearm(130)|wp_archery(130)|wp_throwing(170),knows_skirmisher|knows_ironflesh_5|knows_power_strike_5,germanic_face_1, germanic_face_2],
  ["chauci_archer","Chauci Bowman (Bogomanna)","Chauci Bowmen (Bogomanni)",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_culture_7,
   [itm_linen_shirt_6,itm_generic_tunic_14,itm_linen_shirt_3,itm_simple_shirt_5,itm_simple_shirt_6,itm_linen_shirt_12,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_woolen_cap_2,itm_woolen_cap_b,itm_brown_hood1,itm_leather_cap,itm_battle_axe_3,itm_seax_1,itm_long_bow,itm_strong_bow,itm_germanic_arrows,itm_germanic_arrows]+hats_german+shoes_generic,
   def_attrib_lvl_18|level(16),wp_one_handed(160)|wp_two_handed(140)|wp_polearm(160)|wp_archery(150)|wp_throwing(130),knows_archer,germanic_face_1, germanic_face_2],

  #Sword, angon, francisca - mix of mail, (limited) scale, tunics, subarmalis, helmets
  ["frankish_optimas","Optimas Francorum","Optimates Francorum",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_culture_empire,
   [itm_wrapping_boots,itm_simple_shoes,itm_ankle_boots,itm_khergit_leather_boots,itm_roman_lorum_fasciari_2,itm_generic_tunic_6,itm_linen_shirt_11,itm_linen_shirt_12,itm_linen_shirt_13,itm_roman_military_tunic_6,itm_cloaked_tunic_12,itm_generic_subarmalis_5,itm_subarmalis_4,itm_short_ragged_mail_5,itm_mid_generic_mail_28,itm_mid_generic_mail_25,itm_mid_generic_mail_18,itm_medium_scale_4,itm_gultlingen_helmet_mail,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_ridge_helm_c,itm_fernpass_helmet_2,itm_triveres_mail,
   itm_throwing_axes,itm_throwing_axes,itm_sword_khergit_3,itm_angon_2,itm_angon_2,itm_tab_shield_round_d,itm_concave_shield_germanic_13,itm_concave_shield_germanic_14,itm_round_shield_germanic_10,itm_round_shield_germanic_12,itm_round_shield_germanic_14],
   def_attrib_lvl_23|level(23),wp_one_handed(220)|wp_two_handed(220)|wp_polearm(200)|wp_throwing(220),knows_lvl_23_inf|knows_shield_5|knows_power_strike_5,germanic_face_1, germanic_face_2],

  ["antrustion","Antrustio","Antrustiones",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_7,
   [itm_khergit_leather_boots,itm_wrapping_boots,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_4,itm_mid_generic_mail_28,itm_mid_generic_mail_25,itm_mid_generic_mail_18,itm_mid_generic_mail_21,itm_long_mail_new_9,itm_medium_scale_4,itm_457_scale_hauberk_2,itm_gultlingen_helmet_plume,itm_intercisa_helmet_gilded_1,itm_intercisa_helmet_rich_3,itm_iatrus_2,itm_fernpass_helmet_2,itm_augsburg_2_helmet,itm_augsburg_1_helmet,itm_christies_helmet_1,itm_tab_shield_round_e,itm_sword_khergit_4,itm_heavy_throwing_axes,itm_heavy_throwing_axes],
   def_attrib_lvl_30|level(30),wp_one_handed(250)|wp_two_handed(230)|wp_polearm(220)|wp_throwing(240)|wp_archery(100),knows_lvl_30_inf|knows_shield_5|knows_power_strike_7,germanic_face_1, germanic_face_2],

#burgundians 
  ["burgundian_oathtaker","Burgundian Oathtaker (Guarantor)","Burgundian Oathtakers (Guarantores)",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_7,
   [itm_tab_shield_heater_a,itm_oval_shield_red_2,itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,itm_mid_generic_mail_17,itm_mid_generic_mail_21,itm_short_ragged_mail_7,itm_roman_squamata_5,itm_medium_scale_2,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_triveres_mail,itm_fernpass_helmet_2,itm_christies_helmet_1,itm_augsburg_2_helmet,itm_augsburg_1_helmet,itm_augsburg_2_helmet_mail,itm_sword_viking_3_small,itm_war_spear_1]+angons,
   def_attrib_lvl_23|level(23),wp_one_handed(220)|wp_two_handed(210)|wp_polearm(200)|wp_throwing(200)|wp_archery(100),knows_lvl_23_inf|knows_shield_6|knows_power_strike_5,germanic_face_1, germanic_face_2],

  ["burgundian_tracker","Burgdunian Tracker (Vegius)","Burgundian Trackers (Vegii)",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_culture_7,
   [itm_strong_bow,itm_long_bow,itm_roman_arrows_1,itm_roman_arrows_1,itm_war_axe,itm_generic_tunic_4,itm_generic_tunic_13,itm_linen_shirt_3,itm_linen_shirt_10,itm_roman_military_tunic_1,itm_germanic_cap_2,itm_woolen_cap_2,itm_woolen_cap_4,itm_woolen_cap_5,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2]+shoes_generic,
   def_attrib_lvl_18|level(18),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(170)|wp_archery(160)|wp_throwing(150),knows_athletics_6|knows_ironflesh_5|knows_power_strike_6|knows_power_draw_7|knows_power_throw_2|knows_weapon_master_5|knows_inventory_management_3|knows_riding_2,germanic_face_1, germanic_face_2],

#CAUCASIANS
  ["caucasian_levy","Caucasian Levy","Caucasian Levies",tf_guarantee_basic,0,0,fac_culture_8,
   [itm_wrapping_boots,itm_simple_shoes,itm_nomad_boots,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_woolen_cap_1,itm_woolen_cap,itm_woolen_cap_2,itm_batumi_helmet_cloth,itm_batumi_helmet_leather,itm_tarasovsky_1784_helmet_leather,itm_tarasovsky_1784_helmet_cloth,itm_fighting_axe,itm_bearded_axe_1,itm_spear,itm_medium_spear_2,itm_medium_spear_4,itm_sarranid_two_handed_mace_1,itm_great_sword,itm_wicker_shields_rectangular_1,itm_wicker_shields_rectangular_2,itm_wicker_shields_rectangular_3,itm_oval_shield_wood_2,itm_oval_shield_wood_3,itm_oval_shield_leather_1]+tunics_caucasian,
   def_attrib_lvl_18|level(18),wp_one_handed(170)|wp_two_handed(150)|wp_polearm(170)|wp_throwing(160)|wp_archery(80)|wp_firearm(80),knows_lvl_18_inf|knows_shield_4|knows_power_strike_4,caucaus_face_1, caucaus_face_2],

  ["caucasian_footman","Caucasian Footman","Caucasian Footmen",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_8,
   [itm_simple_shoes,itm_nomad_boots,itm_wrapping_boots,itm_mid_generic_mail_11,itm_sassanid_mail_shirt_3,itm_sassanid_mail_shirt_4,itm_sassanid_mail_shirt_5,itm_eastern_scale_4,itm_eastern_scale_5,itm_batumi_helmet_aventail,itm_tarasovsky_1784_helmet_mail_1,itm_tarasovsky_1784_helmet_mail_2,itm_tsaritsyno_1_light,itm_medium_spear_4,itm_roman_spear_3,itm_poleaxe,itm_roman_spear_4,itm_bearded_axe_2,itm_battle_axe_4,itm_sarranid_two_handed_mace_1,itm_rgani_mace,itm_oval_shield_blue_2,itm_oval_shield_green_2,itm_tab_shield_heater_a],
   def_attrib_lvl_23|level(23),wp_one_handed(230)|wp_two_handed(210)|wp_polearm(220)|wp_throwing(210)|wp_archery(80)|wp_firearm(80),knows_lvl_23_inf|knows_shield_5|knows_power_strike_5,caucaus_face_1, caucaus_face_2],

  ["caucasian_skirmisher","Caucasian Skirmisher","Caucasian Skirmishers",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_culture_8,
   [itm_simple_shoes,itm_nomad_boots,itm_wrapping_boots,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_woolen_cap_1,itm_woolen_cap,itm_woolen_cap_2,itm_hunnic_phrygian_3,itm_hunnic_phrygian_4,itm_bandana1,itm_bandana2,itm_fighting_axe,itm_great_sword,itm_javelin,itm_javelin,itm_georgian_rectangular_shield_wood_1,itm_georgian_rectangular_shield_wood_2,itm_georgian_rectangular_shield_wood_3,itm_georgian_rectangular_shield_leather_1,itm_georgian_rectangular_shield_leather_2,itm_georgian_rectangular_shield_leather_3]+tunics_caucasian+shields_small,
   def_attrib_skirmisher|level(13),wp_one_handed(130)|wp_two_handed(60)|wp_polearm(110)|wp_throwing(140)|wp_archery(140)|wp_firearm(140),knows_skirmisher,caucaus_face_1, caucaus_face_2],

  ["caucasian_archer","Caucasian Archer","Caucasian Archers",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_culture_8,
   [itm_simple_shoes,itm_nomad_boots,itm_wrapping_boots,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_woolen_cap_1,itm_woolen_cap,itm_woolen_cap_2,itm_hunnic_phrygian_3,itm_hunnic_phrygian_4,itm_bandana1,itm_bandana2,itm_sarranid_two_handed_mace_1,itm_strong_bow,itm_bodkin_arrows,itm_bodkin_arrows,itm_georgian_rectangular_shield_leather_1,itm_georgian_rectangular_shield_leather_2,itm_georgian_rectangular_shield_leather_3]+tunics_caucasian,
   def_attrib_lvl_18|level(17),wp_one_handed(160)|wp_two_handed(100)|wp_polearm(140)|wp_throwing(150)|wp_archery(170),knows_archer,caucaus_face_1, caucaus_face_2],

  ["caucasian_nobleman","Caucasian Nobleman","Caucasian Noblemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_polearm|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_culture_8,
   [itm_ankle_boots,itm_nomad_boots,itm_hunter,itm_normal_horse26,itm_normal_horse25,itm_normal_horse23,itm_normal_horse22,itm_skirmisher_tunic_3,itm_generic_tunic_11,itm_kaftan_sheepskin_4,itm_kaftan_sheepskin_5,itm_linen_shirt_15,itm_mid_generic_mail_11,itm_sassanid_mail_shirt_3,itm_sassanid_mail_shirt_4,itm_sassanid_mail_shirt_5,itm_batumi_helmet_aventail,itm_tsaritsyno_1_light,itm_tsaritsyno_1,itm_tarasovsky_1784_helmet_mail_1,itm_tarasovsky_1784_helmet_mail_2,
   itm_lance,itm_battle_axe_4,itm_strong_bow,itm_barbed_arrows,itm_tab_shield_small_round_b],
   def_attrib_lvl_23|level(23),wp_one_handed(190)|wp_two_handed(150)|wp_polearm(190)|wp_throwing(190)|wp_archery(160),knows_lvl_23_cav|knows_shield_4|knows_power_strike_5|knows_horse_archery_4,caucaus_face_1, caucaus_face_2],

  ["caucasian_cataphract","Caucasian Cataphract","Caucasian Cataphracts",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_polearm|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_culture_8,
   [itm_sassanid_cavalry_boots_2,itm_heavy_greaves,itm_eastern_scale_1,itm_eastern_scale_2,itm_eastern_scale_3,itm_eastern_scale_4,itm_eastern_scale_5,itm_eastern_scale_6,itm_batumi_helmet_aventail,itm_tsaritsyno_1,itm_veiled_helmet_4,itm_tsaritsyno_1_veiled,itm_leather_gloves,itm_battle_axe,itm_rgani_mace,itm_heavy_lance,itm_khergit_bow,itm_bodkin_arrows,itm_tab_shield_small_round_c,itm_half_cataphract_horse_3,itm_half_cataphract_horse_4,itm_cataphract_horse_1,itm_cataphract_horse_4,itm_cataphract_horse_5,itm_half_cataphract_horse_7],
   def_attrib_lvl_30|level(30),wp_one_handed(230)|wp_two_handed(210)|wp_polearm(240)|wp_throwing(210)|wp_archery(160)|wp_firearm(80),knows_lvl_30_cav|knows_shield_4|knows_power_strike_6|knows_horse_archery_5,caucaus_face_1, caucaus_face_2],

  ["caucasian_messenger","Caucasian Messenger","Caucasian Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_polearm|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_culture_8,
   [itm_ankle_boots,itm_wrapping_boots,itm_batumi_helmet_cloth,itm_tarasovsky_1784_helmet_leather,itm_light_lance,itm_javelin,itm_javelin,itm_fighting_axe,itm_kaftan_sheepskin_1,itm_kaftan_sheepskin_2,itm_kaftan_sheepskin_3,itm_saddle_horse,itm_normal_horse28,itm_normal_horse26,itm_normal_horse25],
   def_attrib_lvl_18|level(18),wp_one_handed(190)|wp_two_handed(190)|wp_polearm(190)|wp_throwing(100)|wp_archery(80)|wp_firearm(80),knows_common|knows_athletics_3|knows_riding_7|knows_ironflesh_4|knows_power_strike_3|knows_power_throw_3,caucaus_face_1, caucaus_face_2],
  ["caucasian_deserter","Caucasian Deserter","Caucasian Deserters",tf_guarantee_basic,0,0,fac_culture_8,
   [itm_ankle_boots,itm_nomad_boots,itm_kaftan_tunic_1,itm_kaftan_tunic_2,itm_kaftan_sheepskin_1,itm_kaftan_sheepskin_2,itm_kaftan_sheepskin_3,itm_linen_shirt_22,itm_shirt,itm_tarasovsky_1784_helmet_cloth,itm_tarasovsky_1784_helmet_leather,itm_medium_spear_2,itm_fighting_axe,itm_javelin,itm_oval_shield_leather_1,itm_oval_shield_blue_2,itm_oval_shield_wood_1,itm_oval_shield_wicker,itm_oval_shield_wicker],
   def_attrib_lvl_18|level(18),wp_one_handed(170)|wp_two_handed(120)|wp_polearm(170)|wp_throwing(170)|wp_archery(120),knows_lvl_18_inf|knows_shield_4|knows_power_strike_4,caucaus_face_1, caucaus_face_2],
  ["caucasian_prison_guard","Prison Guard","Prison Guards",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_8,
   [itm_leather_gloves,itm_ankle_boots,itm_coat_of_plates_red,itm_javelin,itm_batumi_helmet_aventail,itm_tarasovsky_1784_helmet_leather,itm_tarasovsky_1784_helmet_mail_2,itm_tab_shield_heater_a,itm_war_spear,itm_bearded_axe_2],
   def_attrib_lvl_28|level(26),wp_one_handed(230)|wp_two_handed(220)|wp_polearm(240)|wp_throwing(240)|wp_archery(80)|wp_firearm(80),knows_common|knows_athletics_5|knows_shield_5|knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4,caucaus_face_1, caucaus_face_2],

#AOR/MERCS
  ["suanian_archer","Suani Archer","Suani Archers",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_culture_8,
   [itm_strong_bow,itm_barbed_arrows,itm_barbed_arrows,itm_ankle_boots,itm_wrapping_boots,itm_kaftan_sheepskin_1,itm_kaftan_sheepskin_3,itm_kaftan_sheepskin_4,itm_battle_axe_3,itm_glaive,itm_great_sword,itm_bandana1,itm_bandana2,itm_tarasovsky_1784_helmet_cloth],
   def_attrib_lvl_18|level(18),wp_one_handed(180)|wp_two_handed(80)|wp_polearm(180)|wp_throwing(120)|wp_archery(190)|wp_firearm(110),knows_archer,caucaus_face_1, caucaus_face_2],

  ["tzanni_footman","Tzanni Footman","Tzanni Footmen",tf_guarantee_basic,0,0,fac_culture_8,
   [itm_wrapping_boots,itm_simple_shoes,itm_roman_lorum_fasciari_1,itm_roman_military_tunic_4,itm_linen_shirt,itm_roman_shirt_10,itm_linen_shirt_18,itm_linen_shirt_10,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_tarasovsky_1784_helmet_leather,itm_tarasovsky_1784_helmet_mail_2,itm_ridge_helm_c,itm_intercisa_helmet_1,itm_sarranid_two_handed_mace_1,itm_great_sword,itm_throwing_spear_2,itm_roman_spear_4,itm_oval_shield_limitanei_7,itm_oval_shield_wood_2,itm_oval_shield_leather_1,itm_oval_shield_blue_1,itm_oval_shield_blue_2],
   def_attrib_lvl_18|level(18),wp_one_handed(190)|wp_two_handed(150)|wp_polearm(180)|wp_throwing(190)|wp_archery(80)|wp_firearm(80),knows_lvl_18_inf|knows_shield_5|knows_power_strike_3,caucaus_face_1, caucaus_face_2],

  ["sarir_horseman","Sarir Horseman","Sarir Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_polearm|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_culture_8,
   [itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_kaftan_alan_red,itm_kaftan_alan_white,itm_kaftan_alan_3,itm_tarasovsky_1784_helmet_mail_2,itm_kalhkni_helmet_mail,itm_heavy_lance,itm_yrzi_bow_1,itm_roman_arrows_2,itm_warhorse]+horses_hunnic_2,
   def_attrib_lvl_23|level(23),wp_one_handed(180)|wp_two_handed(150)|wp_polearm(210)|wp_throwing(180)|wp_archery(160),knows_lvl_23_cav|knows_shield_3|knows_power_strike_5|knows_horse_archery_4,persian_face_1, persian_face_2],

  ["caucasian_standard_bearer","Caucasian Standard Bearer","Caucasian Standard Bearers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_culture_8,
   [itm_nomad_boots,itm_wrapping_boots,itm_tarasovsky_1784_helmet_leather,itm_kaftan_sheepskin_1,itm_kaftan_sheepskin_2,itm_kaftan_sheepskin_3,itm_flag_pole_1],
   def_attrib_lvl_18|level(18),wp_one_handed (160) | wp_two_handed (180) | wp_polearm (180) | wp_archery (75) | wp_crossbow (75) | wp_throwing (100),knows_lvl_18_inf|knows_power_strike_5,caucaus_face_1, caucaus_face_2], 

  ["caucasian_alan_mercenary","Alan Mercenary","Alan Mercenaries",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_polearm,0,0,fac_culture_8,
   [itm_khergit_bow,itm_khergit_arrows,itm_hunnic_spatha,itm_heavy_lance,itm_sassanid_cavalry_boots_2,itm_nomad_boots,itm_rich_tunic_3,itm_rich_tunic_5,itm_rich_tunic_6,itm_khudashevsky_helmet_1,itm_old_spangenhelm_2,itm_khudashevsky_helmet_2,itm_kalhkni_helmet_mail,itm_kalhkni_helmet_1,itm_kalhkni_helmet_2] + horses_alans_2,
   def_attrib_lvl_20|level(20),wp_one_handed(190)|wp_two_handed(190)|wp_polearm(190)|wp_throwing(140)|wp_archery(180),knows_riding_7|knows_horse_archery_6|knows_power_draw_6|knows_ironflesh_4|knows_power_strike_5|knows_athletics_4|knows_power_throw_3|knows_inventory_management_3,sarmatian_face_1, sarmatian_face_2],

  ["adyghe_warrior","Adyghe Warrior","Adyghe Warriors",tf_guarantee_basic|tf_guarantee_ranged,0,0,fac_culture_8,
   [itm_leather_gloves,itm_ankle_boots,itm_wrapping_boots,itm_nomad_boots,itm_woolen_cap,itm_woolen_cap_1,itm_woolen_cap_6,itm_skirmisher_tunic_1,itm_skirmisher_tunic_2,itm_kaftan_sheepskin_2,itm_kaftan_sheepskin_3,itm_pelt_coat,itm_thick_coat_6,itm_thick_coat_2,itm_thick_coat_3,itm_jarid,itm_jarid,itm_battle_axe,itm_bearded_axe_1,itm_battle_axe_4,
   itm_georgian_rectangular_shield_wood_1,itm_georgian_rectangular_shield_wood_2,itm_georgian_rectangular_shield_wood_3,itm_georgian_rectangular_shield_leather_1,itm_georgian_rectangular_shield_leather_2,itm_georgian_rectangular_shield_leather_3],
   def_attrib_lvl_20|level(20),wp_one_handed(210)|wp_two_handed(200)|wp_polearm(180)|wp_throwing(210)|wp_archery(80)|wp_firearm(80),knows_lvl_23_inf|knows_power_strike_7|knows_shield_2,caucaus_face_1, caucaus_face_2],

  ["mazkut_cataphract","Maz'Kut Cataphract","Maz'Kut Cataphracts",tf_mounted|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_culture_16,
   [itm_warhorse,itm_warhorse_steppe,itm_cataphract_horse_1,itm_cataphract_horse_4,itm_half_cataphract_horse_1,itm_half_cataphract_horse_5,itm_half_cataphract_horse_6,itm_heavy_lance,itm_tab_shield_small_round_c,itm_hunnic_spatha,itm_eastern_scale_2,itm_eastern_scale_4,itm_sassanid_simple_boots_1,itm_sassanid_cavalry_boots_2,itm_khergit_leather_boots,itm_kalhkni_helmet_mail,itm_kalhkni_helmet_1,itm_kalhkni_helmet_2,itm_rozhdestvensky_helmet_mail,itm_khudashevsky_helmet_3,itm_khudashevsky_helmet_2],
   def_attrib_lvl_28|level(28),wp_one_handed(210)|wp_two_handed(50)|wp_polearm(250)|wp_archery(180)|wp_throwing(60)|wp_crossbow(60)|wp_firearm(60),knows_cataphract,sarmatian_face_1, sarmatian_face_2],

#AOR FOR MINOR FACTION
  #blue/green
  ["zikhes_warrior","Zikhes Warrior","Zikhes Warriors",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_polearm|tf_guarantee_shield,0,0,fac_culture_8,
   [itm_khergit_leather_boots,itm_wrapping_boots,itm_hunter_boots,itm_sassanid_cavalry_boots_1,itm_skirmisher_tunic_4,itm_kaftan_sheepskin_3,itm_kaftan_sheepskin_5,itm_hunnic_phrygian_leather,itm_hunnic_phrygian_3,itm_hunnic_phrygian_4,itm_club,itm_medium_spear_4,itm_throwing_spears,itm_ad_small_shield_2,itm_simple_shield_4],
   def_attrib_skirmisher|level(13),wp_one_handed(140)|wp_two_handed(60)|wp_polearm(150)|wp_throwing(150)|wp_archery(120)|wp_firearm(120),knows_skirmisher,caucaus_face_1, caucaus_face_2],

  ["zikhes_retainer","Zikhes Retainer","Zikhes Retainers",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_8,
   [itm_khergit_leather_boots,itm_wrapping_boots,itm_hunter_boots,itm_sassanid_cavalry_boots_1,itm_kaftan_alan_blue,itm_mid_generic_mail_9,itm_mid_generic_mail_26,itm_hunnic_phrygian_leather,itm_hunnic_phrygian_3,itm_hunnic_phrygian_4,itm_rozhdestvensky_helmet_leather,itm_rozhdestvensky_helmet_mail,itm_spear_sword,itm_polehammer,itm_long_seax_1,itm_kerch_shield_3,itm_kerch_shield_4,itm_kerch_shield_6],
   def_attrib_lvl_20|level(20),wp_one_handed(180)|wp_two_handed(170)|wp_polearm(200)|wp_throwing(160)|wp_archery(80)|wp_firearm(80),knows_lvl_18_inf|knows_shield_4|knows_power_strike_6,caucaus_face_1, caucaus_face_2],

  ["zikhes_horseman","Zikhes Horseman","Zikhes Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_polearm|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_culture_8,
   [itm_sassanid_cavalry_boots_1,itm_hunter_boots,itm_kaftan_alan_blue,itm_kaftan_alan_green,itm_khudashevsky_helmet_1,itm_khudashevsky_helmet_2,itm_djurso_spatha,itm_light_lance,itm_spear_sword,itm_strong_bow,itm_roman_arrows_2,itm_warhorse]+horses_alans_2,
   def_attrib_lvl_23|level(23),wp_one_handed(180)|wp_two_handed(150)|wp_polearm(200)|wp_throwing(180)|wp_archery(160),knows_lvl_23_cav|knows_shield_4|knows_power_strike_6|knows_horse_archery_5,caucaus_face_1, caucaus_face_2],

  ["lekh_warrior","Lekh Warrior","Lekh Warriors",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_culture_8,
   [itm_khergit_leather_boots,itm_wrapping_boots,itm_hunter_boots,itm_skirmisher_tunic_1,itm_kaftan_sheepskin_2,itm_linen_shirt_13,itm_rich_tunic_5,itm_rich_tunic_6,itm_kaftan_tunic_5,itm_fur_hat,itm_hunnic_phrygian_leather,itm_hunnic_phrygian_3,itm_hunnic_phrygian_5,itm_woolen_cap_c,itm_woolen_cap_2,itm_hand_axe,itm_throwing_spears,itm_throwing_spears,itm_simple_shield_1,itm_simple_shield_2,itm_wicker_round_shield,itm_oval_shield_wicker],
   def_attrib_skirmisher|level(15),wp_one_handed(160)|wp_two_handed(60)|wp_polearm(130)|wp_throwing(160)|wp_archery(120)|wp_firearm(120),knows_skirmisher|knows_power_strike_5,caucaus_face_1, caucaus_face_2],

  ["lekh_retainer","Lekh Retainer","Lekh Retainers",tf_guarantee_basic,0,0,fac_culture_8,
   [itm_hunter_boots,itm_sassanid_cavalry_boots_1,itm_kaftan_alan_white,itm_kaftan_alan_red,itm_kaftan_alan_7,itm_mid_generic_mail_23,itm_sassanid_mail_shirt_1,itm_fur_hat,itm_hunnic_phrygian_leather,itm_hunnic_phrygian_3,itm_hunnic_phrygian_5,itm_woolen_cap_c,itm_woolen_cap_2,itm_kalhkni_helmet_mail,itm_kalhkni_helmet_1,itm_kalhkni_helmet_2,itm_war_spear,itm_ringsword_1,itm_throwing_spear_2,itm_battle_axe_2,itm_oval_shield_yellow_2,itm_oval_shield_wood_3,itm_oval_shield_leather_1],
   def_attrib_lvl_20|level(20),wp_one_handed(190)|wp_two_handed(170)|wp_polearm(190)|wp_throwing(160)|wp_archery(80)|wp_firearm(80),knows_lvl_18_inf|knows_shield_5|knows_power_strike_5,caucaus_face_1, caucaus_face_2],

  ["lekh_horseman","Lekh Horseman","Lekh Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_polearm|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_culture_8,
   [itm_sassanid_cavalry_boots_1,itm_hunter_boots,itm_kaftan_alan_white,itm_kaftan_alan_red,itm_kaftan_alan_7,itm_mid_generic_mail_23,itm_sassanid_mail_shirt_1,itm_eastern_scale_6,itm_medium_scale_3,itm_hunnic_phrygian_leather,itm_hunnic_phrygian_3,itm_hunnic_phrygian_5,itm_kalhkni_helmet_mail,itm_kalhkni_helmet_1,itm_kalhkni_helmet_2,itm_ingushetia_spatha,itm_poleaxe,itm_concave_shield_yellow_small_1,itm_concave_shield_leather_small_3,itm_tab_shield_small_round_c,itm_warhorse]+horses_alans_2,
   def_attrib_lvl_23|level(23),wp_one_handed(180)|wp_two_handed(150)|wp_polearm(200)|wp_throwing(180)|wp_archery(160),knows_lvl_23_cav|knows_shield_4|knows_power_strike_6,caucaus_face_1, caucaus_face_2],

#MAURI
  ["mauri_skirmisher","Exculcator Romano-Mauri","Exculcatores Romano-Mauri",tf_mounted|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_culture_11,
   [itm_throwing_spears,itm_throwing_spears,itm_roman_spear_4,itm_securis,itm_dagger,itm_turban_white_2,itm_turban_red_2,
   itm_wrapping_boots,itm_roman_military_tunic_10]+tunics_mauri+shoes_roman+pannonian_hats+shields_simple,
   def_attrib_skirmisher|level(13),wp_one_handed(130)|wp_polearm(120)|wp_throwing(160),knows_skirmisher,mauri_face_1, mauri_face_2],

  ["mauri_footman","Pedes Romano-Mauri","Pedites Romano-Mauri",tf_mounted|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_culture_11,
   [itm_throwing_spears,itm_throwing_spears,itm_roman_spear_2,itm_roman_spear_3,itm_roman_spear_4,itm_securis,itm_dagger,itm_oval_shield_red_2,itm_oval_shield_green_1,itm_oval_shield_yellow_1,itm_concave_shield_red_1,itm_concave_shield_green_1,itm_concave_shield_green_2,itm_concave_shield_yellow_1,itm_round_shield_mauri_1,itm_round_shield_leather_1,itm_round_shield_leather_3,
   itm_wrapping_boots,itm_iatrus_helmet_light,itm_ridge_helm_c,itm_iatrus_helmet_mail,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_intercisa_helmet_2,(itm_intercisa_helmet_1,imod_battered),(itm_intercisa_helmet_1,imod_battered),itm_roman_military_tunic_10]+tunics_mauri+oval_shields_basic+shoes_roman+pannonian_hats,
   def_attrib_lvl_18|level(18),wp_one_handed(160)|wp_polearm(170)|wp_throwing(180),knows_lvl_18_inf|knows_shield_4|knows_power_strike_4,mauri_face_1, mauri_face_2],

  ["mauri_infantry","Miles Romano-Mauri","Milites Romano-Mauri",tf_mounted|tf_guarantee_basic,0,0,fac_culture_11,
   [itm_wrapping_boots,itm_throwing_spears,itm_roman_spear_4,itm_roman_spear_3,itm_late_roman_spear_1,itm_late_roman_spear_2,itm_sword_khergit_3,itm_roman_subarmalis_new_3,itm_roman_subarmalis_new_7,
   itm_short_roman_mail_1,itm_short_roman_mail_2,itm_short_roman_mail_3,itm_short_roman_mail_4,itm_mid_roman_mail_3,itm_mid_roman_mail_6,itm_mid_roman_mail_7,itm_mail_african_1,itm_concave_shield_mauri_1,itm_concave_shield_mauri_2,itm_concave_shield_mauri_3,itm_concave_shield_mauri_4,itm_concave_shield_mauri_5,itm_tab_shield_round_e,itm_oval_shield_red_2,itm_oval_shield_green_1,itm_oval_shield_yellow_1,itm_oval_shield_berber_1,itm_oval_shield_berber_2,itm_tab_shield_heater_a,itm_ridge_helm_c,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_christies_helmet_1,itm_intercisa_helmet_2,itm_iatrus_1,itm_haditha_1,itm_koblenz_helmet_1,itm_burgh_helmet_1,itm_iatrus_helmet_mail]+shoes_roman+pannonian_hats,
   def_attrib_lvl_23|level(23),wp_one_handed(190)|wp_polearm(200)|wp_throwing(200),knows_lvl_23_inf|knows_shield_5|knows_power_strike_5,mauri_face_1, mauri_face_2],

  ["mauri_mounted_skirmisher","Eques Romano-Mauri","Equites Romano-Mauri",tf_mounted|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_culture_11,
   [itm_turban_white_2,itm_turban_red_2,itm_cavalry_javelins,itm_cavalry_javelins,itm_roman_spear_3,itm_securis,itm_wrapping_boots,itm_concave_shield_leather_small_1,itm_concave_shield_leather_small_2,itm_concave_shield_leather_small_3,itm_round_shield_mauri_small_1,itm_wicker_round_shield,itm_bareback_horse_1,itm_roman_military_tunic_10]+tunics_mauri+shields_simple+shoes_roman+pannonian_hats+horses_mauri_1,
   def_attrib_lvl_18|level(18),wp_one_handed(160)|wp_polearm(170)|wp_throwing(200),knows_lvl_18_cav|knows_horse_archery_4|knows_shield_2|knows_power_strike_3,mauri_face_1, mauri_face_2],

  ["mauri_companion","Comes Romano-Mauri","Comites Romano-Mauri",tf_mounted|tf_guarantee_horse|tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_11,
   [itm_leather_gloves,itm_cavalry_javelins,itm_long_decorated_spear1,itm_long_decorated_spear2,itm_long_decorated_spear3,itm_late_roman_spear_1,itm_sword_khergit_4,itm_roman_scale_cuirass_1,itm_roman_scale_cuirass_2,itm_long_roman_mail_1,itm_long_roman_mail_3,itm_roman_squamata_1,itm_roman_squamata_2,itm_457_mail_shirt_1,itm_457_mail_long_1,itm_457_scale_hauberk_2,
   itm_koblenz_helmet_1,itm_koblenz_helmet_2,itm_koblenz_helmet_3,itm_intercisa_helmet_gilded_1,itm_intercisa_helmet_gilded_2,itm_christies_helmet_1,itm_dux_ridge_helm,itm_gold_ridge_helm,itm_intercisa_helmet_rich_3,itm_augst_helmet_3,itm_augst_helmet_rich_2,itm_augsburg_2_helmet,itm_augsburg_1_helmet,itm_heteny_helmet_1,
   itm_imperial_courser,itm_concave_shield_mauri_small_5,itm_concave_shield_roman_8,itm_tab_shield_small_round_c]+greaves_roman+shoes_roman+horses_mauri_2+horses_mauri_3,
   def_attrib_lvl_28|level(28),wp_one_handed(220)|wp_polearm(230)|wp_throwing(240),knows_lvl_28_cav|knows_horse_archery_4|knows_power_strike_6|knows_shield_4,mauri_face_1, mauri_face_2],

  ["mauri_deserter","Mauri Deserter","Mauri Deserters",tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_culture_11,
   [itm_throwing_spears,itm_throwing_spears,itm_roman_spear_2,itm_roman_spear_3,itm_roman_spear_4,itm_securis,itm_dagger,itm_oval_shield_red_2,itm_oval_shield_green_1,itm_oval_shield_yellow_1,itm_concave_shield_red_1,itm_concave_shield_green_1,itm_concave_shield_green_2,itm_concave_shield_yellow_1,itm_turban_white_2,itm_turban_red_2,
   itm_wrapping_boots,itm_iatrus_helmet_light,itm_ridge_helm_c,itm_iatrus_helmet_mail,(itm_intercisa_helmet_1,imod_battered)]+tunics_mauri+oval_shields_basic+shoes_roman+pannonian_hats,
   def_attrib_lvl_18|level(18),wp_one_handed(160)|wp_polearm(170)|wp_throwing(180),knows_lvl_18_inf|knows_shield_4|knows_power_strike_4,mauri_face_1, mauri_face_2],
  ["mauri_messenger","Mauri Messenger","Mauri Messenger",tf_mounted|tf_guarantee_basic,0,0,fac_culture_11,
   [itm_wrapping_boots,itm_ridge_helm_c,itm_cavalry_javelins,itm_roman_spear_3,itm_securis,itm_short_roman_mail_1,itm_short_roman_mail_2,itm_short_roman_mail_3,itm_short_roman_mail_4]+shoes_roman+tunics_mauri,
   def_attrib_lvl_23|level(23),wp_one_handed(190)|wp_polearm(200)|wp_throwing(200),knows_lvl_23_cav|knows_shield_5|knows_power_strike_5,mauri_face_1, mauri_face_2],
  ["mauri_prison_guard","Prison Guard","Prison Guards",tf_mounted|tf_guarantee_basic,0,0,fac_culture_11,
   [itm_wrapping_boots,itm_late_roman_spear_2,itm_short_roman_mail_1,itm_short_roman_mail_2,itm_short_roman_mail_3,itm_short_roman_mail_4,itm_sword_khergit_4,itm_tab_shield_round_e,itm_ridge_helm_c,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_iatrus_1,itm_koblenz_helmet_1,itm_burgh_helmet_1,itm_iatrus_helmet_mail]+shoes_roman,
   def_attrib_lvl_28|level(23),wp(230),knows_lvl_28_inf|knows_shield_5|knows_power_strike_5,mauri_face_1, mauri_face_2],

#AOR
  ["gaetuli_warrior","Gaetuli Warrior","Gaetuli Warriors",tf_mounted|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_culture_11,
   [itm_imperial_common_shirt,itm_simple_tunic_1,itm_simple_tunic_2,itm_simple_tunic_6,itm_mace_1,itm_roman_spear_2,itm_jarid,itm_jarid]+shields_simple,
   def_attrib_lvl_18|level(18),wp_one_handed(160)|wp_polearm(160)|wp_throwing(200),knows_skirmisher|knows_power_strike_6|knows_shield_2,mauri_face_1, mauri_face_2],

  ["gaetuli_horseman","Gaetuli Horseman","Gaetuli Horsemen",tf_mounted|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_culture_11,
   [itm_imperial_common_shirt,itm_simple_tunic_1,itm_simple_tunic_2,itm_simple_tunic_6,itm_roman_spear_3,itm_cavalry_javelins,itm_cavalry_javelins,itm_bareback_horse_1]+shields_simple+horses_mauri_1,
   def_attrib_lvl_18|level(19),wp_one_handed(150)|wp_polearm(180)|wp_throwing(190),knows_lvl_18_cav|knows_horse_archery_5|knows_power_strike_4|knows_shield_2,mauri_face_1, mauri_face_2],

#HUNS
  ["hunnic_skirmisher","Hunnic Skirmisher","Hun Skirmishers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_culture_12,
   [itm_hatchet,itm_cavalry_javelins,itm_cavalry_javelins,itm_cavalry_javelins,itm_nomad_boots,itm_simple_shoes,itm_kaftan_hunnic_red,itm_kaftan_hunnic_blue,itm_kaftan_hunnic_green,itm_kaftan_hunnic_white,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_chionite_hat_4,itm_chionite_hat_5,itm_leather_steppe_cap_a,itm_nomad_cap_b,itm_steppe_horse]+tunics_hunnic+hats_huns+shields_simple+horses_hunnic_1,
   def_attrib_lvl_13|level(13),wp_one_handed(130)|wp_two_handed(80)|wp_polearm(130)|wp_throwing(150)|wp_archery(130),knows_common|knows_riding_4|knows_power_throw_3|knows_horse_archery_3|knows_power_strike_2|knows_ironflesh_1,hunnic_face_1, hunnic_face_2],

  ["hunnic_horse_archer","Hunnic Horse Archer","Hun Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_culture_12,
   [itm_nomad_boots,itm_simple_shoes,itm_sarranid_boots_b,itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_hunnic_phrygian_leather,itm_kaftan_hunnic_red,itm_kaftan_hunnic_blue,itm_kaftan_hunnic_white,itm_khergit_bow,itm_long_seax_4,itm_sword_khergit_1,itm_roman_arrows_1,itm_roman_arrows_1]+tunics_hunnic+hats_huns+horses_hunnic_1,
   def_attrib_lvl_18|level(17),wp_one_handed(160)|wp_two_handed(150)|wp_polearm(150)|wp_throwing(160)|wp_archery(190),knows_riding_6|knows_horse_archery_6|knows_athletics_4|knows_power_strike_4|knows_power_draw_6|knows_power_throw_4|knows_ironflesh_3|knows_inventory_management_3,hunnic_face_1, hunnic_face_2],

  ["hunnic_retainer","Hunnic Retainer","Hun Retainers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_polearm|tf_guarantee_ranged,0,0,fac_culture_12,
   [itm_sarranid_boots_b,itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_hunnic_kaftan_lamellar_1,itm_hunnic_kaftan_lamellar_2,itm_hunnic_kaftan_lamellar_3,itm_kaftan_hunnic_red,itm_kaftan_hunnic_blue,itm_kaftan_hunnic_white,itm_kaftan_hunnic_1,itm_kaftan_hunnic_5,itm_kaftan_hunnic_6,itm_kaftan_lamellar_1,itm_kaftan_lamellar_5,itm_kaftan_lamellar_6,
   itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_hunnic_phrygian_leather,itm_khudashevsky_helmet_1,itm_khudashevsky_helmet_2,itm_kishpek_helmet_leather,itm_kalhkni_helmet_mail,itm_kerch_lamellenhelm,itm_kerch_lamellenhelm_light,itm_tarasovsky_1784_helmet_leather,itm_tarasovsky_1784_helmet_mail_1,itm_tarasovsky_1784_helmet_cloth,itm_tarasovsky_1784_helmet_mail_2,itm_turaevo_helmet,
   itm_hunnic_spatha,itm_khergit_bow,itm_khergit_arrows,itm_light_lance]+hats_huns+horses_hunnic_1+horses_hunnic_2,
   def_attrib_lvl_23|level(23),wp_one_handed(190)|wp_two_handed(190)|wp_polearm(200)|wp_throwing(200)|wp_archery(170),knows_athletics_5|knows_riding_6|knows_power_throw_2|knows_horse_archery_5|knows_power_strike_7|knows_power_draw_7|knows_ironflesh_6|knows_inventory_management_3,hunnic_face_1, hunnic_face_2],

  ["hunnic_veteran","Hunnic Veteran","Hun Veterans",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_culture_12,
   [itm_heavy_greaves,itm_sarranid_boots_b,itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_kaftan_lamellar_1,itm_kaftan_lamellar_5,itm_kaftan_lamellar_6,itm_hunnic_mail_1,itm_coat_of_plates_red,itm_leather_gloves,itm_kalhkni_helmet_1,itm_kalhkni_helmet_2,itm_khudashevsky_helmet_3,itm_kishpek_helmet_mail,itm_concesti_helmet,itm_turaevo_helmet,itm_turaevo_helmet_aventail,itm_pannonhalma_spatha,itm_djurso_spatha,itm_heavy_lance,itm_khergit_arrows,itm_niya_bow_2]+horses_hunnic_2+horses_hunnic_3,
   def_attrib_lvl_28|level(28),wp_one_handed(230)|wp_two_handed(220)|wp_polearm(240)|wp_throwing(230)|wp_archery(180),knows_riding_8|knows_horse_archery_6|knows_power_strike_7|knows_power_draw_8|knows_ironflesh_7|knows_inventory_management_3|knows_athletics_5|knows_shield_2,hunnic_face_1, hunnic_face_2],

  ["hunnic_prison_guard","Prison Guard","Prison Guards",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_culture_12,
   [itm_heavy_greaves,itm_sarranid_boots_b,itm_leather_gloves,itm_kaftan_lamellar_1,itm_kaftan_lamellar_5,itm_kaftan_lamellar_6,itm_hunnic_mail_1,itm_kalhkni_helmet_mail,itm_kalhkni_helmet_1,itm_kalhkni_helmet_2,itm_kerch_lamellenhelm,itm_burgh_helmet_1,itm_battle_axe_4,itm_concave_shield_leather_small_1,itm_concave_shield_leather_small_2,itm_concave_shield_leather_small_3,itm_tab_shield_small_round_b],
   def_attrib_lvl_28|level(28),wp_one_handed(250)|wp_two_handed(220)|wp_polearm(250)|wp_throwing(230)|wp_archery(180),knows_riding_8|knows_power_throw_5|knows_horse_archery_8|knows_power_strike_7|knows_power_draw_5|knows_ironflesh_6,hunnic_face_1, hunnic_face_2],
  ["hunnic_messenger","Hunnic Messenger","Hun Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_polearm|tf_guarantee_shield,0,0,fac_culture_12,
   [itm_nomad_boots,itm_simple_shoes,itm_leather_steppe_cap_a,itm_nomad_cap_b,itm_nomad_cap,itm_nomad_cap,itm_leather_warrior_cap,itm_khergit_armor,itm_nomad_armor,itm_nomad_vest,itm_leather_vest,itm_leather_jerkin,itm_steppe_horse,itm_steppe_horse,itm_normal_horse14,itm_normal_horse15,itm_normal_horse16,itm_normal_horse17,itm_roman_spear_3,itm_battle_axe_3,itm_fighting_axe,itm_battle_axe_3,itm_battle_axe_2,itm_khergit_bow,itm_barbed_arrows,itm_wicker_round_shield,itm_concave_shield_leather_small_1,itm_concave_shield_leather_small_2,itm_concave_shield_leather_small_3] + tunics_hunnic,
   def_attrib_lvl_18|level(18),wp_one_handed(170)|wp_two_handed(150)|wp_polearm(170)|wp_throwing(170)|wp_archery(150),knows_common|knows_riding_5|knows_power_throw_3|knows_horse_archery_4|knows_power_strike_4|knows_power_draw_3|knows_ironflesh_2,hunnic_face_1, hunnic_face_2],
  ["hunnic_deserter","Hunnic Deserter","Hun Deserters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_culture_12,
   [itm_nomad_boots,itm_simple_shoes,itm_sarranid_boots_b,itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_hunnic_phrygian_leather,itm_kaftan_hunnic_red,itm_kaftan_hunnic_blue,itm_kaftan_hunnic_white,itm_khergit_bow,itm_long_seax_4,itm_sword_khergit_1,itm_khergit_arrows,itm_khergit_arrows]+tunics_hunnic+hats_huns+horses_hunnic_1,
   def_attrib_lvl_18|level(17),wp_one_handed(160)|wp_two_handed(150)|wp_polearm(150)|wp_throwing(160)|wp_archery(190),knows_riding_6|knows_horse_archery_6|knows_athletics_4|knows_power_strike_4|knows_power_draw_6|knows_power_throw_4|knows_ironflesh_3|knows_inventory_management_3,hunnic_face_1, hunnic_face_2],

#AOR
  ["akatziri_tribesman","Akatziri Tribesman","Akatziri Tribesmen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_culture_12,
   [itm_nomad_boots,itm_sassanid_simple_boots_2,itm_hunnic_phrygian_leather,itm_skirmisher_tunic_3,itm_kaftan_sheepskin_4,itm_kaftan_tunic_5,itm_kaftan_tunic_8,itm_khergit_bow,itm_long_seax_5,itm_khergit_arrows,itm_khergit_arrows]+hats_huns+horses_hunnic_1,
   def_attrib_lvl_18|level(17),wp_one_handed(160)|wp_two_handed(150)|wp_polearm(140)|wp_throwing(150)|wp_archery(180),knows_riding_5|knows_horse_archery_6|knows_athletics_4|knows_power_strike_5|knows_power_draw_6|knows_power_throw_4|knows_ironflesh_4|knows_inventory_management_3,hunnic_face_1, hunnic_face_2],

  ["akatziri_retainer","Akatziri Retainer","Akatziri Retainers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_culture_12,
   [itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_sarranid_boots_b,itm_kaftan_hunnic_1,itm_kaftan_hunnic_2,itm_kaftan_hunnic_3,itm_kaftan_hunnic_4,itm_kaftan_hunnic_5,itm_kaftan_hunnic_6,itm_hunnic_phrygian_leather,itm_hunnic_phrygian_1,itm_turaevo_helmet,itm_kalhkni_helmet_mail,itm_kalhkni_helmet_1,itm_kalhkni_helmet_2,itm_concesti_helmet,itm_pannonhalma_spatha,itm_niya_bow_2,itm_khergit_arrows,itm_khergit_arrows]+horses_hunnic_2,
   def_attrib_lvl_23|level(23),wp_one_handed(190)|wp_two_handed(150)|wp_polearm(190)|wp_throwing(150)|wp_archery(190),knows_athletics_5|knows_riding_6|knows_horse_archery_5|knows_power_strike_7|knows_power_draw_6|knows_ironflesh_7|knows_inventory_management_3,hunnic_face_1, hunnic_face_2],

  ["meotian_horseman","Maeotian Horseman","Maeotian Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_culture_12,
   [itm_nomad_boots,itm_simple_shoes,itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_kaftan_alan_red,itm_kaftan_alan_blue,itm_kaftan_alan_green,itm_rozhdestvensky_helmet_leather,itm_rozhdestvensky_helmet_mail,itm_tarasovsky_1784_helmet_leather,itm_tarasovsky_1784_helmet_mail_2,itm_old_spangenhelm_3,itm_woolen_cap,itm_woolen_cap_c,itm_woolen_cap_2,itm_hunnic_phrygian_4,itm_hunnic_phrygian_5,itm_hunnic_phrygian_6,itm_steppe_horse,itm_hunnic_spatha,itm_polehammer,itm_ad_small_shield_2,itm_kerch_shield_6,itm_cavalry_javelins]+horses_alans_1,
   def_attrib_lvl_18|level(17),wp_one_handed(160)|wp_two_handed(150)|wp_polearm(170)|wp_throwing(170)|wp_archery(170),knows_common|knows_riding_6|knows_power_throw_6|knows_horse_archery_5|knows_power_strike_4|knows_power_draw_3|knows_ironflesh_2,sarmatian_face_1, sarmatian_face_2],


#NUBIANS
  ["nubian_tribesman","Nubian Spearman","Nubian Spearmen",tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_culture_15,
   [itm_nubian_sandals,itm_roman_spear_2,itm_throwing_spear_2,itm_throwing_spear_2,itm_wicker_round_shield,itm_nubian_shield_1,itm_nubian_shield_2,itm_round_shield_roman_small_28]+tunics_nubians,
   def_attrib_lvl_18|level(17),wp_one_handed(180)|wp_two_handed(100)|wp_polearm(180)|wp_throwing(180)|wp_archery(120)|wp_firearm(100),knows_lvl_18_inf|knows_shield_2|knows_power_strike_6,nubian_face_1, nubian_face_2],

  ["nubian_warrior","Nubian Guard","Nubian Guards",tf_guarantee_armor|tf_guarantee_polearm,0,0,fac_culture_15,
   [itm_nubian_sandals,itm_nubian_spear_1,itm_nubian_spear_2,itm_nubian_spear_3,itm_nubian_spear_4,itm_nubian_scale_armor_1,itm_nubian_scale_armor_2,itm_roman_shirt_4,itm_roman_shirt_15,itm_hide_helmet,itm_nubian_leather_helmet],
   def_attrib_lvl_23|level(23),wp_one_handed(200)|wp_two_handed(120)|wp_polearm(220)|wp_throwing(200)|wp_archery(120)|wp_firearm(100),knows_lvl_23_inf|knows_shield_3|knows_power_strike_8,nubian_face_1, nubian_face_2],

  ["nubian_bowman","Nubian Bowman","Nubian Bowmen",tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_polearm,0,0,fac_culture_15,
   [itm_nubian_sandals,itm_bamboo_spear,itm_hunting_bow,itm_short_bow,itm_arrows,itm_arrows]+tunics_nubians,
   def_attrib_lvl_18|level(16),wp_one_handed(110)|wp_two_handed(80)|wp_polearm(120)|wp_archery(170)|wp_firearm(100),knows_athletics_5|knows_ironflesh_4|knows_power_strike_6|knows_power_draw_7|knows_power_throw_4|knows_riding_3|knows_weapon_master_4|knows_inventory_management_3,nubian_face_1, nubian_face_2],

  ["nubian_archer","Nubian Retainer","Nubian Retainers",tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_culture_15,
   [itm_nubian_sandals,itm_nubian_scale_armor_1,itm_nubian_scale_armor_2,itm_roman_shirt_4,itm_roman_shirt_15,itm_war_bow,itm_long_bow,itm_bodkin_arrows,itm_bodkin_arrows,itm_nubian_spear_3,itm_hide_helmet,itm_nubian_leather_helmet]+tunics_nubians,
   def_attrib_lvl_20|level(20),wp_one_handed(190)|wp_two_handed(80)|wp_polearm(200)|wp_archery(210)|wp_firearm(100),knows_athletics_6|knows_ironflesh_6|knows_power_strike_7|knows_power_draw_9|knows_power_throw_2|knows_riding_3|knows_weapon_master_5|knows_inventory_management_3,nubian_face_1, nubian_face_2],

  ["nubian_horseman","Nubian Horseman","Nubian Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_horse,0,0,fac_culture_15,
   [itm_imperial_saddle_horse_2,itm_normal_horse12,itm_nubian_sandals,itm_nubian_scale_armor_1,itm_nubian_scale_armor_2,itm_mail_african_1,itm_roman_shirt_4,itm_roman_shirt_15,itm_hide_helmet,itm_nubian_leather_helmet,itm_intercisa_helmet_1,itm_haditha_1,itm_burgh_helmet_1,itm_burgh_helmet_mail,itm_burgh_helmet_light,itm_round_shield_roman_small_28,itm_tab_shield_small_round_c,itm_concave_shield_leather_small_1,itm_concave_shield_leather_small_2,itm_concave_shield_leather_small_3,itm_nubian_shield_1,itm_nubian_shield_2,itm_cavalry_javelins,itm_late_roman_spear_1,itm_sword_khergit_4],
   def_attrib_lvl_28|level(28),wp_one_handed(230)|wp_two_handed(140)|wp_polearm(240)|wp_throwing(240)|wp_archery(150)|wp_firearm(100),knows_lvl_28_cav|knows_shield_2|knows_power_strike_8|knows_horse_archery_5,nubian_face_1, nubian_face_2],

  ["nubian_deserter","Nubian Deserter","Nubian Deserters",tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_culture_15,
   [itm_nubian_sandals,itm_roman_spear_2,itm_wicker_round_shield,itm_nubian_shield_1,itm_nubian_shield_2]+tunics_nubians,
   def_attrib_lvl_18|level(17),wp_one_handed(180)|wp_two_handed(100)|wp_polearm(180)|wp_throwing(180)|wp_archery(120)|wp_firearm(100),knows_lvl_18_inf|knows_shield_2|knows_power_strike_6,nubian_face_1, nubian_face_2],
  ["nubian_prison_guard","Prison Guard","Prison Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_culture_15,
   [itm_nubian_sandals,itm_burgh_helmet_mail,itm_hide_helmet,itm_nubian_leather_helmet,itm_nubian_scale_armor_1,itm_nubian_scale_armor_2,itm_nubian_spear_1],
   def_attrib_lvl_28|level(28),wp_one_handed(240)|wp_two_handed(140)|wp_polearm(230)|wp_throwing(240)|wp_archery(120)|wp_firearm(100),knows_lvl_28_inf|knows_shield_3|knows_power_strike_8,nubian_face_1, nubian_face_2],
  ["nubian_messenger","Nubian Messenger","Nubian Messengers",tf_mounted|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_culture_15,
   [itm_arabian_horse_a,itm_arabian_horse_b,itm_arabian_horse_c,itm_arabian_horse_d,itm_nubian_sandals,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_cavalry_javelins,itm_sword_khergit_4,itm_late_roman_spear_1,itm_roman_spear_3,itm_concave_shield_leather_small_1,itm_concave_shield_leather_small_2,itm_concave_shield_leather_small_3,itm_tab_shield_small_round_c] + tunics_nubians,
   def_attrib_lvl_23|level(21),wp_one_handed(190)|wp_two_handed(120)|wp_polearm(190)|wp_throwing(220)|wp_archery(120)|wp_firearm(100),knows_lvl_23_cav|knows_shield_3|knows_power_strike_6,nubian_face_1, nubian_face_2],

#CAUCASIAN ALANS
  ["caucasian_alan_footman","Alan Footman","Alan Footmen",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_shield,0,0,fac_culture_16,
   [itm_simple_shoes,itm_wrapping_boots,itm_nomad_boots,itm_woolen_cap_c,itm_woolen_cap,itm_woolen_cap_b,itm_woolen_cap_6,itm_wicker_shields_rectangular_1,itm_wicker_shields_rectangular_2,itm_wicker_shields_rectangular_3,itm_spiked_club,itm_spiked_mace,itm_winged_mace,itm_fighting_axe,itm_bearded_axe_1,itm_glaive,itm_medium_spear_3,itm_medium_spear_4,itm_javelin]+tunics_caucasian_alans,
   def_attrib_lvl_18|level(17),wp_one_handed(160)|wp_two_handed(130)|wp_polearm(175)|wp_archery(90)|wp_throwing(160)|wp_crossbow(30)|wp_firearm(80),knows_lvl_18_inf|knows_shield_6|knows_power_strike_2,sarmatian_face_1, sarmatian_face_2],

  ["caucasian_alan_skirmisher","Alan Skirmisher","Alan Skirmishers",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_culture_16,
   [itm_simple_shoes,itm_wrapping_boots,itm_nomad_boots,itm_woolen_cap_c,itm_woolen_cap,itm_woolen_cap_b,itm_woolen_cap_6,itm_winged_mace,itm_club,itm_hand_axe,itm_fighting_axe,itm_throwing_spears,itm_throwing_spears]+tunics_caucasian_alans+shields_simple,
   def_attrib_skirmisher|level(13),wp_one_handed(120)|wp_two_handed(130)|wp_polearm(130)|wp_archery(150)|wp_throwing(160)|wp_crossbow(30)|wp_firearm(150),knows_skirmisher,sarmatian_face_1, sarmatian_face_2],

  ["caucasian_alan_tribesman","Alan Tribesman","Alan Tribesmen",tf_mounted|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_culture_16,
   [itm_simple_shoes,itm_wrapping_boots,itm_nomad_boots,itm_woolen_cap_c,itm_woolen_cap,itm_woolen_cap_b,itm_woolen_cap_6,itm_kaftan_alan_red,itm_kaftan_alan_blue,itm_kaftan_alan_green,itm_kaftan_alan_white,itm_medium_spear_4,itm_strong_bow,itm_roman_arrows_2,itm_roman_arrows_2]+tunics_caucasian_alans+horses_alans_1+tunics_caucasian_alans_rich,
   def_attrib_lvl_18|level(18),wp_one_handed(170)|wp_two_handed(170)|wp_polearm(170)|wp_archery(160)|wp_throwing(150)|wp_crossbow(50)|wp_firearm(80),knows_lvl_18_cav|knows_power_strike_4|knows_horse_archery_4,sarmatian_face_1, sarmatian_face_2],

  ["caucasian_alan_retainer","Alan Retainer","Alan Retainers",tf_mounted|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_culture_16, #will replace with proper sword when finished!
   [itm_simple_shoes,itm_wrapping_boots,itm_nomad_boots,itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_kaftan_alan_red,itm_kaftan_alan_blue,itm_kaftan_alan_green,itm_kaftan_alan_white,itm_kaftan_alan_1,itm_kaftan_alan_2,itm_kaftan_alan_3,itm_kaftan_alan_4,itm_kaftan_alan_7,itm_kaftan_lamellar_1,itm_kaftan_lamellar_2,itm_kaftan_lamellar_3,itm_kaftan_lamellar_4,itm_kaftan_lamellar_9,itm_kaftan_lamellar_10,itm_kaftan_lamellar_11,
   itm_woolen_cap_c,itm_woolen_cap,itm_woolen_cap_b,itm_woolen_cap_6,itm_rozhdestvensky_helmet_leather,itm_kishpek_helmet_leather,itm_khudashevsky_helmet_1,itm_khudashevsky_helmet_2,itm_rozhdestvensky_helmet_mail,itm_kishpek_helmet_mail,itm_kalhkni_helmet_mail,itm_kalhkni_helmet_1,itm_kalhkni_helmet_2,itm_heavy_lance,itm_spear_sword,itm_klin_yar_spatha,itm_hunnic_spatha,itm_battle_axe_2]+horses_alans_2,
   def_attrib_lvl_23|level(23),wp_one_handed(200)|wp_two_handed(220)|wp_polearm(210)|wp_archery(160)|wp_throwing(110)|wp_crossbow(30)|wp_firearm(80),knows_lvl_23_cav|knows_power_strike_7|knows_shield_2|knows_horse_archery_5,sarmatian_face_1, sarmatian_face_2],

  ["caucasian_alan_companion","Alan Companion","Alan Companions",tf_mounted|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_culture_16,
   [itm_warhorse_steppe,itm_warhorse,itm_heavy_greaves,itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_sarranid_boots_b,itm_kaftan_lamellar_1,itm_kaftan_lamellar_2,itm_kaftan_lamellar_3,itm_kaftan_lamellar_4,itm_kaftan_lamellar_11,itm_eastern_scale_2,itm_eastern_scale_5,itm_alan_cataphract_1,itm_leather_gloves,
   itm_kalhkni_helmet_1,itm_kalhkni_helmet_2,itm_kishpek_helmet_mail,itm_rozhdestvensky_helmet_mail,itm_khudashevsky_helmet_2,itm_khudashevsky_helmet_3,itm_heavy_lance,itm_spear_sword,itm_klin_yar_spatha],
   def_attrib_lvl_28|level(28),wp_one_handed(220)|wp_two_handed(230)|wp_polearm(240)|wp_archery(160)|wp_throwing(60)|wp_crossbow(60)|wp_firearm(60),knows_lvl_28_cav|knows_power_strike_8|knows_shield_3,sarmatian_face_1, sarmatian_face_2],

  ["caucasian_alan_deserter","Alan Deserter","Alan Deserters",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_shield,0,0,fac_culture_16,
   [itm_simple_shoes,itm_wrapping_boots,itm_nomad_boots,itm_woolen_cap_c,itm_woolen_cap,itm_woolen_cap_b,itm_woolen_cap_6,itm_wicker_shields_rectangular_1,itm_wicker_shields_rectangular_2,itm_wicker_shields_rectangular_3,itm_spiked_club,itm_spiked_mace,itm_winged_mace,itm_fighting_axe,itm_bearded_axe_1,itm_glaive,itm_medium_spear_3,itm_medium_spear_4,itm_javelin]+tunics_caucasian_alans,
   def_attrib_lvl_18|level(17),wp_one_handed(160)|wp_two_handed(130)|wp_polearm(175)|wp_archery(90)|wp_throwing(160)|wp_crossbow(30)|wp_firearm(80),knows_lvl_18_inf|knows_shield_6|knows_power_strike_2,sarmatian_face_1, sarmatian_face_2],
  ["caucasian_alan_messenger","Alan Messenger","Alan Messengers",tf_mounted|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_culture_16,
   [itm_simple_shoes,itm_wrapping_boots,itm_nomad_boots,itm_woolen_cap_c,itm_woolen_cap,itm_woolen_cap_b,itm_woolen_cap_6,itm_kaftan_alan_red,itm_kaftan_alan_blue,itm_kaftan_alan_green,itm_kaftan_alan_white,itm_kaftan_alan_1,itm_medium_spear_4,itm_fighting_axe,itm_strong_bow,itm_roman_arrows_2,itm_roman_arrows_2]+horses_alans_1,
   def_attrib_lvl_20|level(20),wp_one_handed(170)|wp_two_handed(170)|wp_polearm(170)|wp_archery(160)|wp_throwing(150)|wp_crossbow(50)|wp_firearm(80),knows_riding_5|knows_ironflesh_2|knows_power_strike_2|knows_power_draw_4|knows_horse_archery_6|knows_weapon_master_2|knows_inventory_management_2,sarmatian_face_1, sarmatian_face_2],
  ["caucasian_alan_prison_guard","Prison Guard","Prison Guards",tf_mounted|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_culture_16,
   [itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_sarranid_boots_b,itm_eastern_scale_2,itm_eastern_scale_5,itm_kalhkni_helmet_mail,itm_kalhkni_helmet_1,itm_kalhkni_helmet_2,itm_kishpek_helmet_mail,itm_rozhdestvensky_helmet_mail,itm_khudashevsky_helmet_2,itm_khudashevsky_helmet_3,itm_spear_sword,itm_klin_yar_spatha,itm_tab_shield_small_round_c],
   def_attrib_lvl_28|level(28),wp(230),knows_lvl_28_inf|knows_power_strike_8|knows_shield_5,sarmatian_face_1, sarmatian_face_2],

#Alan AOR
  ["barsil_horse_archer","Barsil Horse Archer","Barsil Horse Archers",tf_mounted|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_culture_16,
   [itm_nomad_boots,itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_sarranid_boots_b,itm_kaftan_alan_white,itm_kaftan_alan_3,itm_kaftan_hunnic_1,itm_kaftan_hunnic_5,itm_hunnic_phrygian_1,itm_hunnic_phrygian_5,itm_hunnic_phrygian_6,itm_hunnic_phrygian_leather,itm_kalhkni_helmet_mail,itm_turaevo_helmet,itm_pannonhalma_spatha,itm_khergit_bow,itm_khergit_arrows,itm_khergit_arrows,itm_steppe_horse]+horses_hunnic_1,
   def_attrib_lvl_20|level(19),wp_one_handed(170)|wp_two_handed(180)|wp_polearm(150)|wp_archery(180)|wp_throwing(160)|wp_crossbow(50)|wp_firearm(80),knows_riding_5|knows_ironflesh_3|knows_power_strike_4|knows_power_draw_6|knows_horse_archery_6|knows_weapon_master_2|knows_inventory_management_3,hunnic_face_1, hunnic_face_2],

  ["aursa_rider","Aursa Rider","Aursa Riders",tf_mounted|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_boots,0,0,fac_culture_16,
   [itm_nomad_boots,itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_sarranid_boots_b,itm_sassanid_mail_shirt_3,itm_hunnic_mail_1,itm_kaftan_alan_blue,itm_kaftan_sheepskin_5,itm_kaftan_tunic_7,itm_rozhdestvensky_helmet_mail,itm_hunnic_phrygian_leather,itm_hunnic_phrygian_4,itm_hunnic_phrygian_6,itm_hunnic_spatha,itm_light_lance,itm_khergit_bow,itm_strong_bow,itm_niya_bow_2,itm_roman_arrows_2,itm_concave_shield_leather_small_3,itm_concave_shield_green_small_2,itm_concave_shield_blue_small_2]+horses_alans_2+horses_hunnic_2,
   def_attrib_lvl_23|level(23),wp_one_handed(200)|wp_two_handed(200)|wp_polearm(200)|wp_archery(170)|wp_throwing(160)|wp_crossbow(50)|wp_firearm(80),knows_riding_6|knows_ironflesh_6|knows_power_strike_6|knows_power_draw_5|knows_horse_archery_5|knows_weapon_master_3|knows_inventory_management_3,hunnic_face_1, hunnic_face_2],

#Imperial Soldiers
  ["roman_messenger","Roman Messenger","Roman Messengers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_culture_empire,
   [itm_sword_khergit_3,itm_spear,itm_roman_spear_1,itm_roman_spear_2,itm_war_darts,itm_darts,itm_tab_shield_heater_a,
    itm_roman_shirt_1,itm_roman_shirt_2,itm_roman_shirt_3,itm_roman_shirt_4,itm_ridge_helm_c,itm_pannonian_cap_4,itm_ankle_boots],
   def_attrib_lvl_20|level(20),wp(200),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_5|knows_athletics_5|knows_shield_5,roman_face_1, roman_face_2],

  ["roman_deserter","Transfuga","Transfugae",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_empire,
   [itm_roman_spear_2,itm_roman_spear_4,itm_late_roman_spear_2,itm_sword_khergit_3,itm_narona_bandhelm_leather,itm_narona_bandhelm_cloth,itm_intercisa_helmet_1,itm_augst_helmet_1,itm_haditha_1,itm_darts,itm_roman_subarmalis_new_1,itm_roman_subarmalis_new_2,itm_roman_subarmalis_new_3,itm_457_mail_short_1,itm_457_mail_short_2,itm_457_mail_short_3] + tunics_romans_military + shoes_roman + oval_shields_limitanei_2 + round_shields_limitanei_2,
   def_attrib_lvl_18|level(18),wp_one_handed(160)|wp_two_handed(160)|wp_polearm(160)|wp_archery(110)|wp_throwing(160),knows_lvl_18_inf|knows_shield_5|knows_power_strike_3,roman_face_1, roman_face_2],

  ["roman_prison_guard","Prison Guard","Prison Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_culture_empire,
   [itm_roman_spear_2_c1,itm_sword_khergit_3,itm_457_mail_shirt_1,itm_457_mail_shirt_2,itm_457_mail_shirt_3,itm_intercisa_helmet_gilded_1,itm_heteny_helmet_1,itm_iatrus_2,itm_burgh_helmet_2,itm_tab_shield_heater_a] + greaves_roman,
   def_attrib_lvl_28|level(28),wp(230),knows_ironflesh_7|knows_power_strike_5|knows_power_throw_4|knows_athletics_5|knows_shield_7,roman_face_1, roman_face_2],

  ["roman_castle_guard","Pedes Palatinus","Pedites Palatinae",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_culture_empire,
   [itm_roman_spear_2_c1,itm_sword_khergit_3,itm_457_mail_shirt_1,itm_457_mail_shirt_2,itm_457_mail_shirt_3,itm_intercisa_helmet_gilded_1,itm_heteny_helmet_1,itm_iatrus_2,itm_burgh_helmet_2,itm_tab_shield_heater_a] + greaves_roman,
   def_attrib_lvl_28|level(28),wp(230),knows_ironflesh_7|knows_power_strike_5|knows_power_throw_4|knows_athletics_5|knows_shield_7,roman_face_1, roman_face_2],

#OVERHAULED ROMAN TROOPS
#LIMITANEI TREE
  ["tiro_limitanei","Tiro Limitaneus","Tirones Limitanei",tf_guarantee_basic,0,0,fac_culture_empire,
   [itm_dagger,itm_securis,itm_roman_spear_1,itm_roman_spear_2,itm_darts,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_roman_arming_cap_1,itm_roman_arming_cap_2] + tunics_romans_military + pannonian_hats + shoes_roman + oval_shields_limitanei_1 + round_shields_limitanei_1,
   def_attrib_lvl_13|level(13),wp_one_handed(130)|wp_two_handed(100)|wp_polearm(140)|wp_throwing(130),knows_lvl_13_inf|knows_shield_4|knows_power_strike_2,roman_face_1, roman_face_2],

  ["pedes_limitanei","Pedes Limitaneus","Pedites Limitanei",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_empire,
   [itm_roman_spear_2,itm_roman_spear_4,itm_late_roman_spear_2,itm_sword_khergit_3,itm_narona_bandhelm_leather,itm_narona_bandhelm_cloth,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_haditha_1,itm_koblenz_helmet_1,itm_christies_helmet_1,itm_darts,itm_roman_subarmalis_new_1,itm_roman_subarmalis_new_2,itm_roman_subarmalis_new_3,itm_457_mail_short_1,itm_457_mail_short_2,itm_457_mail_short_3] + tunics_romans_military + shoes_roman + oval_shields_limitanei_2 + round_shields_limitanei_2,
   def_attrib_lvl_18|level(18),wp_one_handed(160)|wp_two_handed(140)|wp_polearm(160)|wp_archery(110)|wp_throwing(160),knows_lvl_18_inf|knows_shield_5|knows_power_strike_3,roman_face_1, roman_face_2],
  #silvered + gilded intercisas
  ["pedes_psuedo","Pedes Pseudocomitatensis","Pedites Pseudocomitatenses",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_culture_empire,
   [itm_roman_spear_3,itm_roman_spear_4,itm_late_roman_spear_1,itm_late_roman_spear_2,itm_sword_medieval_d_long,itm_war_darts,itm_457_mail_shirt_1,itm_457_mail_shirt_2,itm_457_mail_shirt_3,itm_457_mail_short_1,itm_457_mail_short_2,itm_457_mail_short_3,itm_roman_light_scale_1,itm_roman_light_scale_2,itm_roman_rigid_scale_1,itm_roman_subarmalis_new_1,itm_roman_subarmalis_new_2,itm_roman_subarmalis_new_3,
   itm_haditha_1,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_augst_helmet_2,itm_augst_helmet_3,itm_intercisa_helmet_silvered_1,itm_intercisa_helmet_silvered_2,itm_intercisa_helmet_gilded_1,itm_intercisa_helmet_gilded_2,itm_iatrus_1,itm_iatrus_2,itm_narona_bandhelm,itm_narona_bandhelm_mail,itm_koblenz_helmet_1,itm_christies_helmet_1]+shoes_roman+oval_shields_pseudo+round_shields_psuedo,
   def_attrib_lvl_23|level(23),wp_one_handed(190)|wp_two_handed(170)|wp_polearm(190)|wp_archery(120)|wp_throwing(190),knows_lvl_23_inf|knows_shield_6|knows_power_strike_4,roman_face_1, roman_face_2],

  ["exculator_limitanei","Exculcator Limitaneus","Exculcatores Limitanei",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_culture_empire,
   [itm_securis,itm_roman_spear_1,itm_throwing_spears,itm_throwing_spears,itm_throwing_spears,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_haditha_1,itm_roman_arming_cap_1,itm_roman_arming_cap_2] + tunics_romans_military + shoes_roman + pannonian_hats + round_shields_limitanei_1_light,
   def_attrib_skirmisher|level(13),wp_one_handed (120)  | wp_polearm (120) | wp_archery (130) | wp_crossbow (100) | wp_throwing (150),knows_skirmisher,roman_face_1, roman_face_2],

  ["sagittarius_limitanei","Sagittarius Limitaneus","Sagittarii Limitanei",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_empire,
   [itm_securis,itm_strong_bow,itm_roman_arrows_2,itm_roman_arrows_2,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_haditha_1,itm_augst_helmet_1] + tunics_romans_military + shoes_roman + pannonian_hats,
   def_attrib_lvl_18|level(18),wp_one_handed (130)  | wp_polearm (120) | wp_archery (170) | wp_crossbow (130) | wp_throwing (140),knows_archer,roman_face_1, roman_face_2],
#CAVALRY
  ["eques_dalmatae","Eques Dalmata","Equites Dalmatae",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_culture_empire,
   [itm_roman_spear_2,itm_sword_khergit_3,itm_javelin,itm_javelin,itm_haditha_1,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1]+tunics_romans_military+shoes_roman+pannonian_hats+shields_dalmate+horses_roman_1,
   def_attrib_lvl_18|level(18),wp_one_handed(160)|wp_two_handed(100)|wp_polearm(160)|wp_archery(150)|wp_throwing(170),knows_lvl_18_cav|knows_power_strike_3|knows_shield_3,roman_face_1, roman_face_2],

  ["eques_limitanei","Eques Limitaneus","Equites Limitanei",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm|tf_guarantee_shield,0,0,fac_culture_empire,
   [itm_roman_spear_2,itm_roman_spear_4,itm_sword_khergit_3,itm_narona_bandhelm_mail,itm_narona_bandhelm_cloth,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_haditha_1,itm_roman_subarmalis_new_1,itm_roman_subarmalis_new_2,itm_roman_subarmalis_new_3,itm_457_mail_short_1,itm_457_mail_short_2,itm_457_mail_short_3]+tunics_romans_military+shoes_roman+round_shields_limitanei_2_light+horses_roman_1+horses_roman_2,
   def_attrib_lvl_18|level(18),wp_one_handed(160)|wp_two_handed(140)|wp_polearm(160)|wp_archery(120)|wp_throwing(160),knows_lvl_18_cav|knows_shield_3|knows_power_strike_3,roman_face_1, roman_face_2],

  ["eques_promoti","Eques Promotus","Equites Promoti",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm|tf_guarantee_shield,0,0,fac_culture_empire,
   [itm_roman_spear_3,itm_late_roman_spear_1,itm_sword_medieval_b,itm_457_mail_shirt_1,itm_457_mail_shirt_2,itm_457_mail_shirt_3,itm_457_mail_short_1,itm_457_mail_short_2,itm_457_mail_short_3,itm_roman_light_scale_1,itm_roman_light_scale_2,itm_haditha_1,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_augst_helmet_2,itm_augst_helmet_3,itm_intercisa_helmet_silvered_1,itm_intercisa_helmet_silvered_2,itm_intercisa_helmet_gilded_1,itm_intercisa_helmet_gilded_2,itm_iatrus_1,itm_iatrus_2,itm_narona_bandhelm,itm_narona_bandhelm_mail]+shields_promoti+shoes_roman+horses_roman_2+horses_roman_3,
   def_attrib_lvl_23|level(23),wp_one_handed(190)|wp_two_handed(170)|wp_polearm(190)|wp_archery(140)|wp_throwing(180),knows_lvl_23_cav|knows_shield_4|knows_power_strike_5,roman_face_1, roman_face_2],
#CAVALRY
  ["eques_sagittarii","Eques Sagittarius","Equites Sagittarii",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_culture_empire,
   [itm_roman_arrows_1,itm_roman_arrows_1,itm_sword_khergit_3,itm_strong_bow,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_haditha_1,itm_imperial_courser]+tunics_romans_military+shoes_roman+pannonian_hats+horses_roman_1+horses_roman_2,
   def_attrib_lvl_18|level(18),wp_one_handed(150)|wp_two_handed(130)|wp_polearm(150)|wp_archery(170)|wp_throwing(160),knows_horse_archer,roman_face_1, roman_face_2],

  ["eques_cataphractarii","Eques Cataphractarus","Equites Cataphractarii",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_culture_empire,
   [itm_heavy_lance,itm_mace_roman_1,itm_sword_medieval_b,itm_roman_military_mail_12,itm_457_scale_hauberk_1,itm_457_scale_hauberk_2,itm_burgh_helmet_1,itm_koblenz_helmet_1,itm_iatrus_1,itm_christies_helmet_1]+greaves_roman+horses_roman_3,
   def_attrib_lvl_23|level(23),wp_one_handed(190)|wp_polearm(200)|wp_throwing(160)|wp_archery(140),knows_lvl_23_cav|knows_power_strike_6|knows_shield_3,roman_face_1, roman_face_2],
 
  ["eques_clibanarii","Eques Clibanarius","Equites Clibanarii",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_culture_empire,
   [itm_mace_roman_1,itm_tab_shield_small_round_c,itm_long_lance,itm_long_cataphract_mail,itm_arabian_armor_b,itm_coat_of_plates_red,itm_roman_military_mail_12,itm_cataphract_armor_2,itm_cataphract_armor_3,itm_roman_greaves_manica_1,itm_roman_greaves_manica_2,itm_mail_boots_manica_1,itm_mail_boots_manica_2,
   itm_koblenz_helmet_1,itm_koblenz_helmet_2,itm_burgh_helmet_1,itm_burgh_helmet_2,itm_augsburg_2_helmet,itm_christies_helmet_1,itm_leather_gloves,itm_half_cataphract_horse_1,itm_half_cataphract_horse_2,itm_half_cataphract_horse_3,itm_half_cataphract_horse_4,itm_half_cataphract_horse_7]+greaves_roman+horses_cataphract,
   def_attrib_lvl_28|level(28),wp_one_handed(210)|wp_polearm(230)|wp_throwing(200)|wp_archery(140),knows_cataphract,roman_face_1, roman_face_2],

#garrison troops - armed with spears, swords, axes, maces
  ["vigilia","Vigilia","Vigiles",tf_guarantee_basic,0,0,fac_culture_empire, #civilian militia, for garrisons. armed with clubs + spears
   [itm_club,itm_roman_spear_1,itm_concave_shield_green_2,itm_concave_shield_blue_3,itm_concave_shield_yellow_1,itm_roman_military_tunic_7,itm_roman_military_tunic_8,itm_roman_shirt_4]+tunics_romans_military+pannonian_hats+shoes_roman,
   def_attrib_lvl_13|level(13),wp_one_handed(130)|wp_two_handed(100)|wp_polearm(130)|wp_throwing(130),knows_lvl_13_inf|knows_shield_3|knows_power_strike_3,roman_face_1, roman_face_2],

  ["pedes_burgarius","Pedes Burgarius","Pedites Burgarii",tf_guarantee_basic,0,0,fac_culture_empire,
   [itm_roman_spear_2,itm_late_roman_spear_2,itm_sword_khergit_3,itm_securis,itm_mace_roman_1,itm_winged_mace,itm_roman_subarmalis_new_1,itm_roman_subarmalis_new_2,itm_roman_subarmalis_new_3,itm_457_mail_short_1,itm_457_mail_short_2,itm_457_mail_short_3,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_haditha_1,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_pannonian_cap_4,itm_pannonian_cap_5,itm_roman_arming_cap_1,itm_roman_arming_cap_2,
   itm_concave_shield_green_2,itm_concave_shield_blue_3,itm_concave_shield_yellow_1,itm_oval_shield_blue_1,itm_oval_shield_green_1,itm_oval_shield_yellow_1]+tunics_romans_military+shoes_roman,
   def_attrib_lvl_18|level(18),wp_one_handed(170)|wp_two_handed(160)|wp_polearm(170)|wp_archery(130)|wp_throwing(150),knows_lvl_18_inf|knows_shield_4|knows_power_strike_4,roman_face_1, roman_face_2],

  #will be able to recruit as AOR in all roman towns in gaul, hispania, italy
  ["olibrones","Pedes Olibrones","Pedites Olibrones",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_culture_empire, #could prematurely retired Roman field forces, or roman mercenaries, listed as once Romans soldiers and now the flower of the allied forces by Jordanes
   [itm_roman_lorum_fasciari_5,itm_roman_lorum_fasciari_6,itm_roman_shirt_4,itm_roman_shirt_6,itm_roman_military_tunic_9,itm_roman_light_scale_1,itm_roman_light_scale_5,itm_roman_rigid_scale_4,itm_roman_rigid_scale_6,itm_short_roman_mail_3,itm_short_roman_mail_4,itm_457_mail_short_1,itm_457_mail_short_2,itm_457_mail_short_3,
   itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_augst_helmet_2,itm_augst_helmet_3,itm_intercisa_helmet_silvered_1,itm_intercisa_helmet_silvered_2,itm_intercisa_helmet_gilded_1,itm_intercisa_helmet_gilded_2,itm_haditha_1,itm_iatrus_1,itm_iatrus_2,itm_narona_bandhelm,itm_narona_bandhelm_mail,itm_burgh_helmet_1,itm_christies_helmet_1,itm_koblenz_helmet_1,
   itm_sword_khergit_4,itm_mace_roman_1,itm_late_roman_spear_2,itm_round_shield_roman_21,itm_round_shield_roman_24,itm_round_shield_roman_25,itm_concave_shield_roman_25]+shoes_roman,
   def_attrib_lvl_23|level(23),wp_one_handed(200)|wp_two_handed(200)|wp_polearm(200)|wp_archery(120)|wp_throwing(170),knows_lvl_23_inf|knows_shield_5|knows_power_strike_5,roman_face_1, roman_face_2],
  #roman militia units - can be recruited in Italy, gaul, hispania + appear in visigothic troop templates. armed with long spear, chipped (old) sword. limited intercisa style helmets
  ["miles_romani","Miles Romani","Milites Romani",tf_guarantee_basic,0,0,fac_culture_empire,
   [itm_roman_shirt_1,itm_roman_shirt_4,itm_roman_shirt_8,itm_roman_shirt_10,itm_roman_shirt_13,itm_roman_military_tunic_3,itm_roman_military_tunic_7,itm_roman_military_tunic_10,itm_straw_hat,itm_woolen_cap_1,itm_woolen_cap_2,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_burgh_helmet_1,itm_roman_spear_3,(itm_sword_khergit_3,imod_chipped),itm_oval_shield_red_1,itm_oval_shield_chi_rho_5]+shoes_roman+pannonian_hats,
   def_attrib_lvl_18|level(18),wp_one_handed(150)|wp_two_handed(150)|wp_polearm(180)|wp_archery(110)|wp_throwing(160),knows_lvl_18_inf|knows_shield_6|knows_power_strike_2,roman_face_1, roman_face_2],


# -- UNIQUE LEGIONS -- 
#PSEUDOCOMITATENSES - lvl 22
#COMITATENSES - lvl 24
#AUXILIA PALATINA - lvl 28
#PALATINA - lvl 30
#DOMESTICI/SCHOLA/EXCUBITORS - lvl 32

# -- HELMETS -- 
#IRON/SILVERED - lvl 22
#IRON/GILDED - lvl 24
#IRON/SILVERED/GILDED/DECORATED - lvl 28
#IRON/GILDED/DECORATED - lvl 30
#GILDED/DECORATED - lvl 32

  #found in noricum - still active until the 460s-470s
  ["pedes_cohortis_batavorum","Pedes Cohortis Batavorum","Pedites Cohortis Batavorum",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_kingdom_1,
   [itm_roman_lorum_fasciari_2,itm_wrapping_boots,itm_khergit_leather_boots,itm_roman_military_tunic_1,itm_roman_military_tunic_2,itm_457_mail_short_2,itm_457_mail_short_3,itm_iatrus_1,itm_iatrus_helmet_mail,itm_burgh_helmet_mail,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_narona_bandhelm_mail,itm_burgh_helmet_1,itm_mace_roman_1,itm_late_roman_spear_1,itm_war_darts,itm_oval_shield_chi_rho_7],
   def_attrib_lvl_23|level(22),wp_one_handed(210)|wp_two_handed(190)|wp_polearm(210)|wp_archery(150)|wp_throwing(190),knows_lvl_23_inf|knows_shield_6|knows_power_strike_6,roman_face_1, roman_face_2],

  #Praefectus legionis liburnariorum primorum Noricorum - also active (although poorly armed) from the 460s-470s in noricum
  ["miles_primorum_noricorum","Miles Primorum Noricorum","Milites Primorum Noricorum",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_kingdom_1,
   [itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_military_tunic_1,itm_roman_military_tunic_4,itm_intercisa_helmet_1,itm_augst_helmet_1,itm_narona_bandhelm_mail,itm_mace_roman_1,itm_javelin,itm_javelin,itm_concave_shield_blue_2]+pannonian_hats,
   def_attrib_lvl_18|level(17),wp_one_handed(170)|wp_two_handed(140)|wp_polearm(160)|wp_archery(130)|wp_throwing(180),knows_athletics_6|knows_riding_2|knows_ironflesh_6|knows_power_throw_6|knows_power_draw_3|knows_weapon_master_5|knows_inventory_management_3|knows_shield_2|knows_power_strike_5,roman_face_1, roman_face_2],

#WRE
#Pseudocomitatenses
  #Above average polearm skill - Italia
  ["pedes_pontinenses","Pedes Pontinenses","Pedites Pontinenses",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_1,
   [itm_late_roman_spear_1,itm_late_roman_spear_2,itm_sword_khergit_3,itm_war_darts,itm_457_mail_shirt_1,itm_457_mail_shirt_2,itm_457_mail_shirt_3,itm_457_mail_short_1,itm_457_mail_short_2,itm_457_mail_short_3,itm_intercisa_helmet_1,itm_augst_helmet_1,itm_iatrus_1,itm_narona_bandhelm,itm_burgh_helmet_1,itm_christies_helmet_1,itm_koblenz_helmet_1,itm_narona_bandhelm_mail,itm_narona_bandhelm_leather,itm_intercisa_helmet_silvered_1,itm_augst_helmet_2,itm_oval_shield_pontinenses] + shoes_roman,
   def_attrib_lvl_23|level(22),wp_one_handed(190)|wp_two_handed(190)|wp_polearm(215)|wp_archery(120)|wp_throwing(190),knows_lvl_23_inf|knows_shield_7|knows_power_strike_3,roman_face_1, roman_face_2],
  #Slightly higher shield, ironflesh skills - Gallia
  ["pedes_defensores_seniores","Pedes Defensores Seniores","Pedites Defensores Seniores",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_1,
   [itm_late_roman_spear_2,itm_sword_khergit_3,itm_war_darts,itm_oval_shield_defensores_seniores,itm_457_mail_short_1,itm_457_mail_short_2,itm_457_mail_short_3,itm_457_mail_shirt_1,itm_457_mail_shirt_2,itm_457_mail_shirt_3,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_iatrus_1,itm_christies_helmet_1,itm_narona_bandhelm_mail,itm_narona_bandhelm,itm_intercisa_helmet_silvered_1,itm_intercisa_helmet_silvered_2,itm_augst_helmet_2] + shoes_roman,
   def_attrib_lvl_23|level(22),wp_one_handed(190)|wp_two_handed(190)|wp_polearm(190)|wp_archery(120)|wp_throwing(190),knows_lvl_23_inf|knows_shield_8|knows_power_strike_2|knows_ironflesh_8,roman_face_1, roman_face_2],
  #Javelins, quality spears - Dalmatia
  ["pedes_lanciarii_lauriacenses","Pedes Lanciarii Lauriacenses","Pedites Lanciarii Lauriacenses",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_1,
   [itm_late_roman_spear_1,itm_roman_spear_4,itm_sword_khergit_3,itm_jarid,itm_457_mail_shirt_1,itm_457_mail_shirt_2,itm_457_mail_shirt_3,itm_457_mail_short_1,itm_457_mail_short_2,itm_457_mail_short_3,itm_intercisa_helmet_2,itm_intercisa_helmet_gilded_2,itm_iatrus_1,itm_narona_bandhelm,itm_burgh_helmet_1,itm_koblenz_helmet_1,itm_narona_bandhelm_mail,itm_christies_helmet_1,itm_oval_shield_pseudo_1] + shoes_roman,
   def_attrib_lvl_23|level(22),wp_one_handed(190)|wp_two_handed(190)|wp_polearm(210)|wp_archery(120)|wp_throwing(200),knows_lvl_23_inf|knows_shield_6|knows_power_strike_4,roman_face_1, roman_face_2],
#Comitatenses
  #Above average throwing skill - Italia
  ["pedes_mattiarii_iuniores","Pedes Mattiarii Iuniores","Pedites Mattiarii Iuniores",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_sword_khergit_4,itm_war_darts,itm_war_darts,itm_457_mail_shirt_1,itm_457_mail_shirt_2,itm_457_mail_shirt_3,itm_iatrus_1,itm_iatrus_2,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_intercisa_helmet_gilded_1,itm_intercisa_helmet_gilded_2,itm_oval_shield_mattiarii] + shoes_roman,
   def_attrib_lvl_25|level(25),wp_one_handed(210)|wp_two_handed(150)|wp_polearm(190)|wp_archery(120)|wp_throwing(240),knows_athletics_6|knows_riding_2|knows_ironflesh_7|knows_power_throw_7|knows_weapon_master_6|knows_inventory_management_4|knows_shield_5|knows_power_strike_5,roman_face_1, roman_face_2],
  #Higher weapon, defenses skills - Dalmatia
  ["pedes_propugnatores_iuniores","Pedes Propugnatores Iuniores","Pedites Propugnatores Iuniores",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_1,
   [itm_late_roman_spear_1,itm_late_roman_spear_2,itm_sword_khergit_3,itm_spiculum,itm_457_mail_shirt_1,itm_457_mail_shirt_2,itm_457_mail_shirt_3,itm_iatrus_1,itm_iatrus_2,itm_narona_bandhelm,itm_narona_bandhelm_mail,itm_christies_helmet_1,itm_burgh_helmet_1,itm_burgh_helmet_2,itm_koblenz_helmet_1,itm_koblenz_helmet_2,itm_oval_shield_propugnatores_iuniores] + shoes_roman,
   def_attrib_lvl_25|level(25),wp_one_handed(200)|wp_two_handed(170)|wp_polearm(200)|wp_archery(120)|wp_throwing(200),knows_athletics_5|knows_riding_2|knows_ironflesh_7|knows_power_throw_6|knows_power_draw_2|knows_weapon_master_5|knows_inventory_management_4|knows_shield_7|knows_power_strike_4,roman_face_1, roman_face_2],
  #Higher 1 handed skills - Gallia
  ["pedes_ursarienses","Pedes Ursarienses","Pedites Ursarienses",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_samson_spatha_2_rich,itm_spiculum,itm_spiculum,itm_457_mail_shirt_1,itm_457_mail_shirt_2,itm_457_mail_shirt_3,itm_intercisa_helmet_1,itm_intercisa_helmet_gilded_1,itm_narona_bandhelm_mail,itm_narona_bandhelm,itm_christies_helmet_1,itm_oval_shield_ursarienses] + shoes_roman,
   def_attrib_lvl_25|level(25),wp_one_handed(220)|wp_two_handed(160)|wp_polearm(190)|wp_archery(120)|wp_throwing(210),knows_athletics_5|knows_riding_2|knows_ironflesh_7|knows_power_throw_6|knows_power_draw_2|knows_weapon_master_5|knows_inventory_management_4|knows_shield_5|knows_power_strike_7,roman_face_1, roman_face_2],
#Aux. Palatina
  #Quality weapon skills - Italia
  ["pedes_cornuti_seniores","Pedes Cornuti Seniores","Pedites Cornuti Seniores",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_1,
   [itm_late_roman_spear_1,itm_arabian_sword_b,itm_spiculum,itm_457_mail_long_1,itm_457_mail_long_2,itm_457_mail_long_3,itm_roman_military_mail_12,itm_iatrus_1,itm_iatrus_2,itm_burgh_helmet_1,itm_burgh_helmet_2,itm_christies_helmet_1,itm_augsburg_1_helmet,itm_roman_greaves_manica_1,itm_roman_greaves_manica_2,itm_roman_greaves_manica_3,itm_oval_shield_5] + greaves_roman,
   def_attrib_lvl_28|level(28),wp_one_handed(240)|wp_two_handed(150)|wp_polearm(240)|wp_archery(120)|wp_throwing(220),knows_lvl_28_inf|knows_shield_4|knows_power_strike_8,roman_face_1, roman_face_2],
  #Quality defensive skills, good spears - Gallia
  ["pedes_mattiaci_seniores","Pedes Mattiaci Seniores","Pedites Mattiaci Seniores",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_1,
   [itm_late_roman_spear_1,itm_sword_khergit_4,itm_war_darts,itm_457_mail_long_1,itm_457_mail_long_2,itm_457_mail_long_3,itm_roman_military_mail_12,itm_457_scale_hauberk_1,itm_iatrus_2,itm_koblenz_helmet_1,itm_koblenz_helmet_2,itm_burgh_helmet_2,itm_christies_helmet_1,itm_oval_shield_mattiaci] + greaves_roman,
   def_attrib_lvl_28|level(28),wp_one_handed(220)|wp_two_handed(150)|wp_polearm(230)|wp_archery(120)|wp_throwing(220),knows_lvl_28_inf|knows_shield_8|knows_power_strike_4,roman_face_1, roman_face_2],
  #High one handed skills, has francisca - Dalmatia
  ["pedes_tungri","Pedes Tungri","Pedites Tungri",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_sword_khergit_4,itm_heavy_throwing_axes,itm_heavy_throwing_axes,itm_457_mail_long_1,itm_457_mail_long_2,itm_457_mail_long_3,itm_roman_military_mail_12,itm_457_scale_hauberk_1,itm_intercisa_helmet_gilded_1,itm_intercisa_helmet_rich_3,itm_augsburg_2_helmet,itm_iatrus_2,itm_gultlingen_helmet_plume,itm_concave_shield_roman_18]+greaves_roman,
   def_attrib_lvl_28|level(28),wp_one_handed(240)|wp_two_handed(150)|wp_polearm(220)|wp_archery(120)|wp_throwing(230),knows_lvl_28_inf|knows_shield_6|knows_power_strike_6,roman_face_1, roman_face_2],
  #Spears, slightly lower level - Italia
  ["pedes_felices_valentinianenses","Pedes Placidi Felices Valentinianenses","Pedites Placidi Felices Valentinianenses",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_1,
   [itm_indesheim_spatha_rich,itm_late_roman_spear_1,itm_spiculum,itm_roman_greaves_5,itm_roman_greaves_6,itm_roman_rigid_scale_1,itm_roman_rigid_scale_2,itm_roman_rigid_scale_3,itm_roman_rigid_scale_6,itm_roman_light_scale_2,itm_roman_light_scale_4,itm_457_scale_hauberk_5,itm_457_mail_long_3,itm_iatrus_2,itm_heteny_helmet_1,itm_concesti_helmet,itm_augsburg_1_helmet,itm_gultlingen_helmet_mail,itm_gultlingen_helmet,itm_oval_shield_felices_valentinianenses]+greaves_roman,
   def_attrib_lvl_28|level(27),wp_one_handed(230)|wp_two_handed(150)|wp_polearm(230)|wp_archery(120)|wp_throwing(220),knows_lvl_28_inf|knows_shield_7|knows_power_strike_5,roman_face_1, roman_face_2],
  #Quality sword skills/good quality sword - Italia
  ["pedes_heruli_seniores","Pedes Heruli Seniores","Pedites Heruli Seniores",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_samson_spatha_2_rich,itm_round_shield_germanic_4,itm_457_mail_long_4,itm_augst_helmet_rich_plume_2,itm_intercisa_helmet_rich_plume_3,itm_intercisa_helmet_rich_plume_4]+greaves_roman,
   def_attrib_lvl_28|level(28),wp_one_handed(245)|wp_two_handed(220)|wp_polearm(225)|wp_archery(120)|wp_throwing(230),knows_lvl_28_inf|knows_shield_5|knows_power_strike_7,germanic_face_1, germanic_face_2],
  #Unique archer - Dalmatia
  ["miles_sagittarii_venatores","Miles Sagittarii Venatores","Milites Sagittarii Venatores",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_1,
   [itm_sword_khergit_4,itm_strong_bow,itm_khergit_bow,itm_roman_arrows_1,itm_roman_arrows_1,itm_457_mail_short_1,itm_457_mail_short_2,itm_457_mail_short_3,itm_short_roman_mail_4,itm_roman_light_scale_1,itm_roman_light_scale_2,itm_roman_light_scale_3,itm_roman_light_scale_5,itm_roman_rigid_scale_1,itm_roman_rigid_scale_2,itm_roman_rigid_scale_3,itm_intercisa_helmet_1,itm_intercisa_helmet_silvered_1,itm_intercisa_helmet_gilded_1,itm_iatrus_1,itm_iatrus_2,itm_augsburg_1_helmet,itm_gultlingen_helmet_mail]+shoes_roman,
   def_attrib_lvl_28|level(26),wp_one_handed(200)|wp_two_handed(160)|wp_polearm(190)|wp_archery(180)|wp_throwing(160),knows_athletics_6|knows_ironflesh_7|knows_power_strike_6|knows_power_draw_8|knows_weapon_master_6|knows_inventory_management_3|knows_riding_4|knows_power_throw_4,roman_face_1, roman_face_2],
#Palatina - Italia
  #sword, spear, spiculum
  ["pedes_moesiaci_seniores","Pedes Moesiaci Seniores","Pedites Moesiaci Seniores",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_1,
   [itm_late_roman_spear_1,itm_arabian_sword_b,itm_spiculum,itm_roman_military_mail_12,itm_457_scale_hauberk_1,itm_457_scale_hauberk_6,itm_intercisa_helmet_gilded_plume_1,itm_intercisa_helmet_rich_plume_3,itm_intercisa_helmet_rich_plume_1,itm_koblenz_crested_2,itm_koblenz_crested_3,itm_burgh_helmet_plume_2,itm_iatrus_plume_2,itm_christies_helmet_crest_1,itm_oval_shield_moesiaci] + greaves_roman,
   def_attrib_lvl_30|level(30),wp_one_handed(220)|wp_two_handed(150)|wp_polearm(230)|wp_archery(120)|wp_throwing(220),knows_lvl_30_inf|knows_shield_8|knows_power_strike_4,roman_face_1, roman_face_2],
  #sword, spear, plumbata
  ["pedes_ioviani_seniores","Pedes Ioviani Seniores","Pedites Ioviani Seniores",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_1,
   [itm_oval_shield_ioviani_seniores,itm_indesheim_spatha_rich,itm_long_decorated_spear1,itm_war_darts,itm_roman_greaves_manica_3,itm_roman_greaves_1,itm_roman_greaves_5,itm_457_scale_hauberk_1,itm_457_scale_hauberk_2,itm_457_scale_hauberk_5,itm_457_scale_hauberk_8,itm_intercisa_helmet_rich_3,itm_heteny_helmet_1,itm_augsburg_1_helmet,itm_berkasovo_2_helmet,itm_concesti_helmet,itm_christies_helmet_1,itm_iatrus_2,itm_gultlingen_helmet],
   def_attrib_lvl_30|level(30),wp_one_handed(230)|wp_two_handed(150)|wp_polearm(220)|wp_archery(120)|wp_throwing(230),knows_lvl_30_inf|knows_shield_8|knows_power_strike_4,roman_face_1, roman_face_2],

#Comites - Italia
  ["comites_alani","Comes Alani","Comites Alani",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_1,
   [itm_roman_squamata_1,itm_roman_squamata_2,itm_roman_scale_cuirass_1,itm_roman_scale_cuirass_2,itm_roman_light_scale_1,itm_roman_light_scale_2,itm_roman_light_scale_3,itm_roman_light_scale_5,itm_roman_rigid_scale_1,itm_roman_rigid_scale_2,itm_roman_rigid_scale_3,itm_roman_rigid_scale_4,itm_eastern_scale_6,itm_burgh_helmet_2,itm_iatrus_2,itm_koblenz_helmet_3,itm_concesti_helmet,itm_augsburg_1_helmet,itm_gultlingen_helmet_mail,itm_intercisa_helmet_rich_3,itm_augsburg_2_helmet,itm_berkasovo_2_helmet,itm_heteny_helmet_1,itm_arabian_sword_b,itm_niya_bow_2,itm_roman_arrows_2,itm_heavy_lance,itm_roman_greaves_manica_3,itm_roman_greaves_manica_4,itm_roman_greaves_5,itm_roman_greaves_6,itm_concave_shield_roman_13]+greaves_roman+horses_roman_4,
   def_attrib_lvl_30|level(30),wp_one_handed(230)|wp_two_handed(150)|wp_polearm(230)|wp_throwing(150)|wp_crossbow(150)|wp_archery(180),knows_lvl_30_cav|knows_shield_4|knows_power_strike_8|knows_horse_archery_5,sarmatian_face_1, sarmatian_face_2],
#Equites stablesiani Italiciani - vexillationes comitatenses - Italia
  ["eques_stablesiani_italiciani","Eques Stablesiani Italiciani","Equites Stablesiani Italiciani",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_concave_shield_stablesiani,itm_arabian_sword_b,itm_mid_roman_mail_8,itm_457_mail_shirt_1,itm_457_mail_shirt_2,itm_457_mail_shirt_3,itm_dux_ridge_helm,itm_gold_ridge_helm,itm_koblenz_helmet_2,itm_koblenz_helmet_3,itm_concesti_helmet,itm_augsburg_2_helmet,itm_heteny_helmet_1,itm_roman_greaves_manica_1,itm_roman_greaves_manica_2]+greaves_roman+horses_roman_3,
   def_attrib_lvl_25|level(25),wp_one_handed(210)|wp_two_handed(130)|wp_polearm(190)|wp_throwing(130)|wp_crossbow(130)|wp_archery(130),knows_lvl_23_cav|knows_shield_6|knows_power_strike_5,roman_face_1, roman_face_2],
#Equites prima Gallia - vexillationes comitatenses - Gallia
  ["eques_prima_gallia","Eques Prima Gallia","Equites Prima Gallia",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_kingdom_1,
   [itm_457_mail_shirt_1,itm_457_mail_shirt_2,itm_457_mail_shirt_3,itm_457_mail_short_1,itm_457_mail_short_2,itm_457_mail_short_3,itm_narona_bandhelm_mail,itm_narona_bandhelm,itm_intercisa_helmet_1,itm_koblenz_helmet_1,itm_gultlingen_helmet_mail,itm_christies_helmet_1,itm_concave_shield_roman_16,itm_roman_spear_4,itm_indesheim_spatha_rich]+greaves_roman+shoes_roman+horses_roman_1+horses_roman_2,
   def_attrib_lvl_25|level(25),wp_one_handed(200)|wp_two_handed(130)|wp_polearm(200)|wp_throwing(190)|wp_crossbow(130)|wp_archery(130),knows_lvl_23_cav|knows_shield_5|knows_power_strike_5,roman_face_1, roman_face_2],
#Equites Honoriani Taifali iuniores - vexillationes comitatenses - Gallia
  ["eques_honoriani_taifali_iuniores","Eques Honoriani Taifali Iuniores","Equites Honoriani Taifali Iuniores",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_kingdom_1,
   [itm_roman_light_scale_2,itm_roman_rigid_scale_3,itm_roman_squamata_2,itm_457_scale_hauberk_2,itm_berkasovo_2_helmet,itm_augsburg_2_helmet,itm_iatrus_2,itm_gultlingen_helmet_feathers,itm_arabian_sword_b,itm_late_roman_spear_1,itm_round_shield_roman_12]+greaves_roman+shoes_roman+horses_roman_3,
   def_attrib_lvl_25|level(25),wp_one_handed(200)|wp_two_handed(130)|wp_polearm(200)|wp_throwing(190)|wp_crossbow(130)|wp_archery(130),knows_lvl_23_cav|knows_shield_4|knows_power_strike_6|knows_horse_archery_5,roman_face_1, roman_face_2],
#Equites Batavi seniores - vexillationes palatinae - Gallia
  ["eques_batavi_seniores","Eques Batavi Seniores","Equites Batavi Seniores",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_kingdom_1,
   [itm_457_mail_long_1,itm_457_mail_long_2,itm_457_mail_long_3,itm_koblenz_helmet_1,itm_gultlingen_helmet,itm_gultlingen_helmet_plume,itm_heteny_helmet_1,itm_augsburg_2_helmet,itm_augsburg_1_helmet,itm_christies_helmet_1,itm_concave_shield_roman_17,itm_late_roman_spear_1,itm_samson_spatha_2_rich]+greaves_roman+shoes_roman+horses_roman_3,
   def_attrib_lvl_28|level(28),wp_one_handed(220)|wp_two_handed(130)|wp_polearm(210)|wp_throwing(210)|wp_crossbow(130)|wp_archery(130),knows_lvl_28_cav|knows_shield_5|knows_power_strike_7,roman_face_1, roman_face_2],

#ERE
#Pseudocomitatenses
  #good polearm skill, mix of armor, slightly cheaper troops
  ["pedes_transtigritani","Pedes Transtigritani","Pedites Transtigritani",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_2,
   [itm_late_roman_spear_1,itm_late_roman_spear_2,itm_sword_khergit_3,itm_war_darts,itm_457_mail_short_1,itm_457_mail_short_2,itm_457_mail_short_3,itm_roman_light_scale_1,itm_roman_rigid_scale_1,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_iatrus_1,itm_haditha_1,itm_augst_helmet_1,itm_koblenz_helmet_1,itm_christies_helmet_1,itm_intercisa_helmet_silvered_1,itm_augst_helmet_2,itm_oval_shield_transtigritani] + shoes_roman,
   def_attrib_lvl_23|level(21),wp_one_handed(190)|wp_two_handed(190)|wp_polearm(210)|wp_archery(120)|wp_throwing(200),knows_lvl_23_inf|knows_shield_8|knows_power_strike_2,roman_face_1, roman_face_2],
  #Balistarii Theodosiaci - http://lukeuedasarson.com/NDbalistariiTheodosiaci.html
  #Chersoneus
  ["pedes_theodosiaci","Pedes Balistarii Theodosiaci","Pedites Balistarii Theodosiaci",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_2,
   [itm_sword_khergit_3,itm_late_roman_spear_2,itm_steel_bolts,itm_steel_bolts,itm_sniper_crossbow,itm_round_shield_roman_8,itm_roman_military_tunic_1,itm_roman_military_tunic_2,itm_roman_military_tunic_3,itm_roman_subarmalis_new_1,itm_roman_subarmalis_new_2,itm_roman_subarmalis_new_3,itm_457_mail_short_1,itm_457_mail_short_2,itm_457_mail_short_3,itm_roman_light_scale_1,itm_roman_rigid_scale_1,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_intercisa_helmet_silvered_1,itm_intercisa_helmet_silvered_2,itm_augst_helmet_2]+shoes_roman,
   def_attrib_lvl_20|level(20),wp_one_handed(180)|wp_two_handed(170)|wp_polearm(190)|wp_archery(160)|wp_crossbow(180)|wp_throwing(160),knows_lvl_18_inf|knows_shield_6|knows_power_strike_3,roman_face_1, roman_face_2],
  #Prima Isaura sagittaria - http://lukeuedasarson.com/NDprimaIsauraSagittaria.html
  ["miles_prima_isaura_sagitarria","Miles Prima Isaura Sagittaria","Milites Prima Isaura Sagittaria",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_2,
   [itm_roman_light_scale_2,itm_roman_light_scale_3,itm_roman_rigid_scale_1,itm_457_mail_short_2,itm_457_mail_short_3,itm_intercisa_helmet_1,itm_haditha_1,itm_iatrus_1,itm_augst_helmet_1,itm_augst_helmet_2,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_battle_axe_2,itm_strong_bow,itm_roman_arrows_1,itm_round_shield_roman_10]+shoes_roman,
   def_attrib_lvl_23|level(23),wp_one_handed(220)|wp_two_handed(220)|wp_polearm(200)|wp_throwing(200)|wp_archery(180),knows_power_strike_7|knows_power_draw_6|knows_ironflesh_7|knows_shield_4|knows_athletics_6|knows_inventory_management_3|knows_power_throw_3|knows_riding_4,roman_face_1, roman_face_2],

#Comitatenses
  #better equipment compared to counterparts, stronger defensively, made to last until 637 ;^) - per orientem, limitis aegypti
  ["pedes_quinta_macedonica","Pedes Quinta Macedonica","Pedites Quinta Macedonica",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_2,
   [itm_late_roman_spear_1,itm_roman_spear_4,itm_indesheim_spatha_rich,itm_war_darts,itm_roman_lorum_fasciari_5,itm_roman_lorum_fasciari_6,itm_roman_greaves_5,itm_roman_greaves_6,itm_roman_light_scale_1,itm_roman_light_scale_2,itm_roman_light_scale_3,itm_roman_light_scale_4,itm_457_mail_shirt_4,itm_legio_v_mail,itm_iatrus_1,itm_iatrus_2,itm_haditha_1,itm_intercisa_helmet_1,itm_intercisa_helmet_gilded_1,itm_augst_helmet_1,itm_augst_helmet_3,itm_narona_bandhelm_cloth,itm_narona_bandhelm,itm_narona_bandhelm_mail,itm_oval_shield_4]+shoes_roman,
   def_attrib_lvl_25|level(25),wp_one_handed(200)|wp_two_handed(150)|wp_polearm(200)|wp_archery(120)|wp_throwing(190),knows_athletics_6|knows_riding_2|knows_ironflesh_7|knows_power_throw_6|knows_weapon_master_5|knows_inventory_management_4|knows_shield_8|knows_power_strike_4,roman_face_1, roman_face_2],
  #above average one handed skill, uses maces, throwing darts, spears - per thracias
  ["pedes_tzaanni","Pedes Tzaanni","Pedites Tzaanni",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_mace_roman_1,itm_late_roman_spear_1,itm_war_darts,itm_roman_scale_cuirass_1,itm_roman_scale_cuirass_2,itm_roman_rigid_scale_1,itm_iatrus_1,itm_koblenz_helmet_1,itm_intercisa_helmet_1,itm_oval_shield_tzaanni] + shoes_roman,
   def_attrib_lvl_25|level(25),wp_one_handed(210)|wp_two_handed(190)|wp_polearm(190)|wp_archery(120)|wp_throwing(190),knows_athletics_6|knows_riding_2|knows_ironflesh_7|knows_power_throw_6|knows_power_draw_2|knows_weapon_master_5|knows_inventory_management_4|knows_shield_5|knows_power_strike_7,caucaus_face_1, caucaus_face_2],
  #possible aux? has access to good sword, throwing spear, slightly higher level + skills
  ["pedes_augustenses","Pedes Augustenses","Pedites Augustenses",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_2,
   [itm_roman_lorum_fasciari_5,itm_roman_greaves_5,itm_roman_greaves_manica_3,itm_457_mail_shirt_1,itm_457_mail_shirt_2,itm_roman_light_scale_1,itm_roman_light_scale_2,itm_intercisa_helmet_1,itm_haditha_1,itm_iatrus_1,itm_iatrus_2,itm_narona_bandhelm,itm_narona_bandhelm_mail,itm_narona_bandhelm_leather,itm_arabian_sword_b,itm_spiculum,itm_oval_shield_augustenses],
   def_attrib_lvl_25|level(25),wp_one_handed(190)|wp_two_handed(150)|wp_polearm(190)|wp_archery(120)|wp_throwing(190),knows_athletics_6|knows_riding_2|knows_ironflesh_7|knows_power_throw_6|knows_power_draw_2|knows_weapon_master_5|knows_inventory_management_4|knows_shield_7|knows_power_strike_5,roman_face_1, roman_face_2],
  #per orientem - good sword skills
  ["pedes_decima_gemina","Pedes Decima Gemina","Pedites Decima Gemina",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_roman_lorum_fasciari_5,itm_457_mail_shirt_3,itm_457_mail_shirt_4,itm_457_scale_hauberk_1,itm_iatrus_1,itm_iatrus_2,itm_haditha_1,itm_intercisa_helmet_1,itm_intercisa_helmet_gilded_1,itm_christies_helmet_1,itm_indesheim_spatha_rich,itm_concave_shield_roman_26]+shoes_roman,
   def_attrib_lvl_25|level(25),wp_one_handed(215)|wp_two_handed(150)|wp_polearm(180)|wp_archery(120)|wp_throwing(180),knows_athletics_6|knows_riding_2|knows_ironflesh_8|knows_power_throw_5|knows_weapon_master_5|knows_inventory_management_4|knows_shield_6|knows_power_strike_6,roman_face_1, roman_face_2],
#Aux. Palatina
  ["pedes_regii_east","Pedes Regii Orientalis","Pedites Regii Orientalis",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_2,
   [itm_late_roman_spear_1,itm_arabian_sword_b,itm_war_darts,itm_roman_military_mail_12,itm_457_scale_hauberk_2,itm_457_scale_hauberk_5,itm_iatrus_1,itm_iatrus_2,itm_koblenz_helmet_1,itm_koblenz_helmet_2,itm_intercisa_helmet_rich_3,itm_augsburg_2_helmet,itm_augsburg_1_helmet,itm_concesti_helmet,itm_heteny_helmet_1,itm_oval_shield_regii_east] + greaves_roman,
   def_attrib_lvl_28|level(28),wp_one_handed(220)|wp_two_handed(150)|wp_polearm(220)|wp_archery(120)|wp_throwing(220),knows_lvl_28_inf|knows_shield_7|knows_power_strike_5,roman_face_1, roman_face_2],
  #Quality weapon skills, has similar javs to excubitors
  ["pedes_thraces","Pedes Thraces","Pedites Thraces",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_2,
   [itm_late_roman_spear_2,itm_sword_khergit_4,itm_roman_javelin,itm_457_mail_long_1,itm_457_mail_long_2,itm_457_mail_long_3,itm_iatrus_1,itm_haditha_1,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_narona_bandhelm_mail,itm_narona_bandhelm,itm_christies_helmet_1,itm_roman_greaves_manica_1,itm_roman_greaves_manica_2,itm_roman_greaves_manica_3,itm_oval_shield_thraces],
   def_attrib_lvl_28|level(28),wp_one_handed(240)|wp_two_handed(150)|wp_polearm(240)|wp_archery(120)|wp_throwing(220),knows_lvl_28_inf|knows_shield_6|knows_power_strike_6,roman_face_1, roman_face_2],
  #Primi Theodosiani - Presentalis I
  ["pedes_primi_theodosiani","Pedes Primi Theodosiani","Pedites Primi Theodosiani",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_2,
   [itm_late_roman_spear_1,itm_sword_khergit_4,itm_war_darts,itm_457_mail_long_1,itm_457_mail_long_2,itm_457_mail_long_3,itm_long_roman_mail_1,itm_intercisa_helmet_gilded_1,itm_iatrus_2,itm_intercisa_helmet_rich_3,itm_koblenz_helmet_2,itm_augsburg_2_helmet,itm_concesti_helmet,itm_christies_helmet_1,itm_heteny_helmet_1,itm_augsburg_1_helmet,itm_oval_shield_primi_theodosiani] + greaves_roman,
   def_attrib_lvl_28|level(28),wp_one_handed(220)|wp_two_handed(150)|wp_polearm(220)|wp_archery(120)|wp_throwing(220),knows_lvl_28_inf|knows_shield_5|knows_power_strike_7,roman_face_1, roman_face_2],
  #Victores - Presenatlis I
  ["pedes_victores","Pedes Victores","Pedites Victores",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_2,
   [itm_late_roman_spear_1,itm_indesheim_spatha_rich,itm_war_darts,itm_457_mail_long_1,itm_457_mail_long_2,itm_457_mail_long_3,itm_long_roman_mail_1,itm_457_scale_hauberk_4,itm_roman_rigid_scale_1,itm_roman_rigid_scale_3,itm_intercisa_helmet_gilded_plume_1,itm_intercisa_helmet_rich_plume_3,itm_intercisa_helmet_rich_plume_1,itm_iatrus_2,itm_augsburg_1_helmet,itm_koblenz_crested_2,itm_koblenz_crested_3,itm_concesti_helmet,itm_heteny_helmet_1,itm_christies_helmet_crest_1,itm_christies_helmet_crest_2,itm_oval_shield_victores] + greaves_roman,
   def_attrib_lvl_28|level(28),wp_one_handed(230)|wp_two_handed(150)|wp_polearm(230)|wp_archery(140)|wp_throwing(220),knows_lvl_28_inf|knows_shield_8|knows_power_strike_4,roman_face_1, roman_face_2],

  #will eventually add in the Felices Theodosiani 
#Palatina
  #has long spear, javelins
  ["pedes_scythae","Pedes Scythae","Pedites Scythae",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_2,
   [itm_late_roman_spear_1,itm_long_decorated_spear1,itm_long_decorated_spear2,itm_long_decorated_spear3,itm_arabian_sword_b,itm_roman_javelin,itm_roman_military_mail_12,itm_457_scale_hauberk_3,itm_457_scale_hauberk_4,itm_iatrus_plume_2,itm_koblenz_crested_3,itm_intercisa_helmet_rich_plume_3,itm_intercisa_helmet_rich_plume_1,itm_christies_helmet_crest_1,itm_christies_helmet_crest_2,itm_gultlingen_helmet_plume,itm_gultlingen_helmet_feathers,itm_oval_shield_scythae] + greaves_roman,
   def_attrib_lvl_30|level(30),wp_one_handed(230)|wp_two_handed(150)|wp_polearm(240)|wp_archery(120)|wp_throwing(240),knows_lvl_30_inf|knows_shield_7|knows_power_strike_5,roman_face_1, roman_face_2],
  #only has swords, spiculum, strong melee skills
  ["pedes_daci","Pedes Daci","Pedites Daci",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_sword_khergit_4,itm_spiculum,itm_spiculum,itm_roman_military_mail_12,itm_457_scale_hauberk_1,itm_iatrus_2,itm_koblenz_helmet_2,itm_koblenz_helmet_3,itm_burgh_helmet_2,itm_christies_helmet_1,itm_intercisa_helmet_gilded_1,itm_augsburg_1_helmet,itm_roman_greaves_manica_1,itm_roman_greaves_manica_2,itm_oval_shield_daci] + greaves_roman,
   def_attrib_lvl_30|level(30),wp_one_handed(250)|wp_two_handed(150)|wp_polearm(230)|wp_archery(120)|wp_throwing(230),knows_lvl_30_inf|knows_shield_6|knows_power_strike_8,roman_face_1, roman_face_2],
  #Long spear, high spear skills, javelins, mail armored
  ["pedes_lanciarii_iuniores","Pedes Lanciarii Iuniores","Pedites Lanciarii Iuniores",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_samson_spatha_2_rich,itm_roman_javelin,itm_late_roman_spear_1,itm_long_decorated_spear1,itm_long_decorated_spear2,itm_long_decorated_spear3,itm_457_mail_long_1,itm_457_mail_long_2,itm_457_mail_long_3,itm_intercisa_helmet_gilded_plume_1,itm_intercisa_helmet_rich_plume_3,itm_intercisa_helmet_rich_plume_1,itm_iatrus_plume_2,itm_gultlingen_helmet_plume,itm_concesti_helmet,itm_concave_shield_roman_15] + greaves_roman,
   def_attrib_lvl_30|level(30),wp_one_handed(230)|wp_two_handed(150)|wp_polearm(250)|wp_archery(120)|wp_throwing(230),knows_lvl_30_inf|knows_shield_7|knows_power_strike_6,roman_face_1, roman_face_2],
  #Long Spear, spear skills, javelins, armored with scale, better armored than iuniores, less skills
  ["pedes_lanciarii_seniores","Pedes Lanciarii Seniores","Pedites Lanciarii Seniores",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_samson_spatha_2_rich,itm_roman_javelin,itm_late_roman_spear_1,itm_long_decorated_spear1,itm_long_decorated_spear2,itm_long_decorated_spear3,itm_457_scale_hauberk_5,itm_457_scale_hauberk_6,itm_koblenz_crested_2,itm_koblenz_crested_3,itm_iatrus_plume_2,itm_gultlingen_helmet_plume,itm_christies_helmet_crest_1,itm_concesti_helmet,itm_berkasovo_2_helmet,itm_roman_greaves_manica_1,itm_roman_greaves_manica_2,itm_roman_greaves_manica_3,itm_roman_greaves_5,itm_concave_shield_roman_14] + greaves_roman,
   def_attrib_lvl_30|level(30),wp_one_handed(230)|wp_two_handed(150)|wp_polearm(240)|wp_archery(120)|wp_throwing(230),knows_lvl_30_inf|knows_shield_6|knows_power_strike_7,roman_face_1, roman_face_2],
  #high throwing skill
  ["pedes_matiarii_iuniores","Pedes Matiarii Iuniores","Pedites Matiarii Iuniores",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_2,
   [itm_indesheim_spatha_rich,itm_war_darts,itm_war_darts,itm_457_mail_long_1,itm_457_mail_long_2,itm_457_mail_long_3,itm_roman_light_scale_5,itm_roman_rigid_scale_4,itm_457_scale_hauberk_1,itm_457_scale_hauberk_2,itm_intercisa_helmet_gilded_1,itm_iatrus_2,itm_concesti_helmet,itm_heteny_helmet_1,itm_christies_helmet_1,itm_augsburg_1_helmet,itm_oval_shield_matiarii_iuniores]+greaves_roman,
   def_attrib_lvl_30|level(30),wp_one_handed(230)|wp_two_handed(150)|wp_polearm(240)|wp_archery(120)|wp_throwing(240),knows_lvl_30_inf|knows_shield_6|knows_power_strike_7,roman_face_1, roman_face_2],

#Comites - only 1 unit!
  ["comites_sagittarius_armeni","Comes Sagittarius Armeni","Comites Sagittarii Armeni",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_2,
   [itm_imperial_courser,itm_roman_squamata_1,itm_roman_squamata_2,itm_roman_scale_cuirass_1,itm_roman_scale_cuirass_2,itm_roman_light_scale_1,itm_roman_light_scale_2,itm_roman_light_scale_3,itm_roman_light_scale_5,itm_roman_rigid_scale_4,itm_iatrus_2,itm_koblenz_helmet_2,itm_koblenz_helmet_3,itm_gultlingen_helmet_mail,itm_intercisa_helmet_gilded_1,itm_intercisa_helmet_rich_3,itm_augsburg_1_helmet,itm_augsburg_2_helmet,itm_heteny_helmet_1,itm_concesti_helmet,itm_sword_khergit_4,itm_strong_bow,itm_roman_arrows_2,itm_roman_arrows_2]+greaves_roman+horses_roman_2,
   def_attrib_lvl_30|level(30),wp_one_handed(230)|wp_two_handed(150)|wp_polearm(210)|wp_throwing(150)|wp_crossbow(150)|wp_archery(190),knows_lvl_30_cav|knows_shield_4|knows_power_strike_6|knows_horse_archery_6,caucaus_face_1, caucaus_face_2],
#others
  #Equites sexto Dalmatae - http://lukeuedasarson.com/NDequitesSextoDalmatae.html
  ["eques_sexto_dalmatae","Eques Sexto Dalmata","Equites Sexto Dalmatae",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_kingdom_2,
   [itm_roman_spear_4,itm_sword_khergit_4,itm_throwing_spears,itm_throwing_spears,itm_tab_shield_small_round_c,itm_imperial_courser,itm_457_mail_short_1,itm_457_mail_short_2,itm_457_mail_short_3,itm_roman_subarmalis_new_1,itm_roman_subarmalis_new_2,itm_roman_subarmalis_new_3,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_haditha_1,itm_iatrus_1]+tunics_romans_military+shoes_roman+horses_roman_1+horses_roman_2,
   def_attrib_lvl_23|level(23),wp_one_handed(190)|wp_two_handed(100)|wp_polearm(190)|wp_throwing(220),knows_lvl_23_cav|knows_power_strike_4|knows_shield_4|knows_horse_archery_5,roman_face_1, roman_face_2],
  #Equites tertii stablesiani - http://lukeuedasarson.com/NDequitesTertiiStablesiani.html
  ["eques_tertii_stablesiani","Eques Tertii Stablesiani","Equites Tertii Stablesiani",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_2,
   [itm_round_shield_roman_small_4,itm_arabian_sword_b,itm_mid_roman_mail_8,itm_457_mail_shirt_1,itm_457_mail_shirt_2,itm_457_mail_shirt_3,itm_roman_squamata_1,itm_roman_squamata_2,itm_dux_ridge_helm,itm_gold_ridge_helm,itm_koblenz_helmet_2,itm_iatrus_1,itm_iatrus_2,itm_koblenz_helmet_3,itm_christies_helmet_1,itm_augsburg_2_helmet,itm_intercisa_helmet_gilded_1,itm_intercisa_helmet_rich_3]+greaves_roman+horses_roman_3,
   def_attrib_lvl_25|level(25),wp_one_handed(230)|wp_two_handed(130)|wp_polearm(200)|wp_throwing(130)|wp_crossbow(130)|wp_archery(130),knows_athletics_2|knows_riding_6|knows_ironflesh_7|knows_power_throw_6|knows_weapon_master_5|knows_inventory_management_4|knows_shield_7|knows_power_strike_5,roman_face_1, roman_face_2],
  #Equites armigeri seniores orientales - http://lukeuedasarson.com/NDequitesArmigeriSenioresOrientales.html
  ["eques_armigeri_seniores_orientales","Eques Armigeri Seniores Orientales","Equites Armigeri Seniores Orientales",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_kingdom_2,
   [itm_half_cataphract_horse_1,itm_half_cataphract_horse_2,itm_half_cataphract_horse_8,itm_roman_light_scale_1,itm_roman_light_scale_2,itm_roman_light_scale_3,itm_roman_light_scale_4,itm_roman_light_scale_5,itm_roman_squamata_1,itm_roman_squamata_2,itm_roman_rigid_scale_1,itm_roman_rigid_scale_2,itm_roman_rigid_scale_3,itm_tab_shield_round_e,itm_heavy_lance,itm_mace_roman_1,itm_iatrus_1,itm_christies_helmet_1,itm_narona_bandhelm_mail,itm_narona_bandhelm,itm_iatrus_2,itm_roman_greaves_manica_1,itm_roman_greaves_manica_2,itm_roman_greaves_manica_3,itm_roman_greaves_manica_4]+horses_roman_4+horses_cataphract,
   def_attrib_lvl_25|level(25),wp_one_handed(220)|wp_two_handed(150)|wp_polearm(220)|wp_throwing(150)|wp_crossbow(150)|wp_archery(150),knows_athletics_2|knows_riding_6|knows_ironflesh_7|knows_power_throw_6|knows_weapon_master_5|knows_inventory_management_4|knows_shield_5|knows_power_strike_7,roman_face_1, roman_face_2],
  #Equites Clibanarii Parthi - primi + secundi in Presenatlis I + II, quarti in Orientem
  ["eques_clibanarii_parthi","Eques Clibanarius Parthi","Equites Clibanarii Parthi",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_kingdom_2,
   [itm_mace_sassanid,itm_heavy_lance,itm_yrzi_bow_1,itm_roman_arrows_1,itm_arabian_armor_b,itm_roman_military_mail_12,itm_eastern_scale_6,itm_cataphract_lamellar_1,itm_iatrus_plume_1,itm_koblenz_crested_1,itm_gultlingen_helmet_plume,itm_christies_helmet_crest_1,itm_half_cataphract_horse_7,itm_half_cataphract_horse_3,itm_half_cataphract_horse_4]+greaves_roman,
   def_attrib_lvl_28|level(28),wp_one_handed(230)|wp_polearm(240)|wp_throwing(200)|wp_archery(170),knows_cataphract,persian_face_1, persian_face_2],

#GUARDS, OFFICERS, ELITES, ETC
  ["centenarius","Centenarius","Centenarii",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_culture_empire,
   [itm_augst_helmet_crested_rich_1,itm_augst_helmet_crested_rich_2,itm_koblenz_crested_2,itm_iatrus_plume_2,itm_intercisa_helmet_gilded_plume_1,itm_burgh_helmet_plume_2,itm_indesheim_spatha_rich,itm_spiculum,itm_spiculum,itm_long_roman_mail_1,itm_long_roman_mail_5,itm_roman_light_scale_1,itm_roman_light_scale_2,itm_roman_squamata_1,itm_roman_squamata_2,itm_roman_scale_cuirass_1,itm_roman_scale_cuirass_2,itm_roman_leather_boots_1,itm_roman_lorum_fasciari_5,itm_roman_lorum_fasciari_6,itm_roman_greaves_5,itm_roman_greaves_6,itm_concave_shield_roman_19,itm_concave_shield_roman_20]+shoes_roman+greaves_roman,
   def_attrib_lvl_30|level(30),wp_one_handed(230)|wp_two_handed(190)|wp_polearm(180)|wp_archery(120)|wp_throwing(200),knows_lvl_30_inf|knows_shield_6|knows_power_strike_6|knows_trainer_4,roman_face_1, roman_face_2],

#Scholae Palatinum / Scholae Palatinae
  ["eques_domestici","Eques Domestici","Equites Domestici",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_gloves,0,0,fac_culture_empire,
   [itm_concave_shield_domestici,itm_arabian_sword_b,itm_roman_spear_2_c1,itm_roman_spear_2_c2,itm_roman_spear_2_c3,itm_sarranid_boots_c,itm_leather_gloves,itm_arabian_armor_b,itm_roman_military_mail_12,itm_457_scale_hauberk_1,itm_457_scale_hauberk_2,itm_457_scale_hauberk_4,itm_457_scale_hauberk_5,itm_457_scale_hauberk_6,itm_half_cataphract_horse_1,itm_half_cataphract_horse_2,itm_burgh_helmet_plume_2,itm_koblenz_crested_2,itm_deurne_helmet,itm_koblenz_crested_3,itm_gultlingen_helmet,itm_augsburg_1_helmet,itm_augsburg_2_helmet,itm_concesti_helmet,itm_heteny_helmet_1]+greaves_roman+horses_roman_3+horses_roman_4,
   def_attrib_lvl_32|level(32),wp_one_handed(240)|wp_two_handed(220)|wp_polearm(240)|wp_archery(140)|wp_throwing(200),knows_lvl_30_cav|knows_shield_7|knows_power_strike_7,roman_face_1, roman_face_2],

  ["pedes_domestici","Pedes Domestici","Pedites Domestici",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_culture_empire,
   [itm_oval_shield_domestici,itm_indesheim_spatha_rich,itm_spiculum,itm_spiculum,itm_spiculum,itm_sarranid_boots_c,itm_leather_gloves,itm_arabian_armor_b,itm_roman_military_mail_12,itm_457_scale_hauberk_1,itm_457_scale_hauberk_2,itm_457_scale_hauberk_4,itm_457_scale_hauberk_5,itm_457_scale_hauberk_6,itm_burgh_helmet_plume_2,itm_koblenz_crested_2,itm_deurne_helmet,itm_koblenz_crested_3,itm_gultlingen_helmet,itm_augsburg_1_helmet,itm_augsburg_2_helmet,itm_concesti_helmet,itm_heteny_helmet_1] + greaves_roman,
   def_attrib_lvl_32|level(32),wp_one_handed(240)|wp_two_handed(220)|wp_polearm(240)|wp_archery(140)|wp_throwing(230),knows_lvl_30_inf|knows_shield_7|knows_power_strike_7,roman_face_1, roman_face_2],
#Excubitors
  ["excubitor","Excubitor","Excubitores",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_excubitor_boots,itm_roman_lorum_fasciari_6,itm_roman_greaves_6,itm_roman_greaves_manica_4,itm_excubitor_mail,itm_deurne_helmet,itm_berkasovo_2_helmet,itm_augsburg_2_helmet,itm_gultlingen_helmet_plume,itm_excubitor_shield_1,itm_excubitor_spear,itm_mace_roman_2,itm_indesheim_spatha_rich,itm_roman_javelin],
   def_attrib_lvl_35|level(35),wp_one_handed(260)|wp_two_handed(240)|wp_polearm(250)|wp_archery(170)|wp_throwing(250),knows_ironflesh_10|knows_power_strike_8|knows_power_throw_8|knows_athletics_6|knows_shield_6|knows_riding_6|knows_power_draw_5|knows_inventory_management_3,roman_face_1, roman_face_2],
#Candidati
  ["candidatus","Candidatus","Candidati",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_culture_empire,
   [itm_candidati_squamata_1,itm_candidati_squamata_2,itm_candidati_squamata_3,itm_candidati_mail,itm_augsburg_1_helmet,itm_augsburg_2_helmet,itm_gultlingen_helmet_plume,itm_deurne_helmet,itm_concesti_helmet,itm_heteny_helmet_1,itm_berkasovo_2_helmet,itm_indesheim_spatha_rich,itm_tab_shield_heater_a,itm_roman_greaves_manica_1,itm_roman_greaves_manica_2,itm_roman_greaves_manica_3,itm_roman_greaves_manica_4]+greaves_roman,
   def_attrib_lvl_32|str_30|level(33),wp_one_handed(250)|wp_two_handed(230)|wp_polearm(240)|wp_archery(160)|wp_throwing(220),knows_lvl_30_inf|knows_shield_7|knows_power_strike_8|knows_ironflesh_10,roman_face_1, roman_face_2],
  #Schola scutariorum secunda - dropping secunda, renaming as Occidentalis - Western Roman Empire
  #Melee cav
  ["schola_scutariorum_west","Scholarius Scutariorum Occidentalis","Scholarii Scutariorum Occidentalis",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_culture_empire,
   [itm_half_cataphract_horse_1,itm_half_cataphract_horse_2,itm_half_cataphract_horse_8,itm_roman_rigid_scale_4,itm_roman_rigid_scale_5,itm_roman_squamata_1,itm_roman_squamata_2,itm_roman_squamata_4,itm_457_scale_hauberk_4,itm_457_scale_hauberk_5,itm_457_scale_hauberk_6,itm_concesti_helmet,itm_heteny_helmet_1,itm_augsburg_1_helmet,itm_deurne_helmet,itm_augsburg_2_helmet,itm_berkasovo_2_helmet,itm_gultlingen_helmet,itm_gultlingen_helmet_plume,itm_concave_shield_roman_21,itm_samson_spatha_2_rich,itm_long_decorated_spear3]+greaves_roman,
   def_attrib_lvl_32|level(32),wp_one_handed(250)|wp_two_handed(230)|wp_polearm(240)|wp_archery(160)|wp_throwing(200)|wp_crossbow(150)|wp_firearm(150),knows_ironflesh_9|knows_riding_6|knows_shield_6|knows_athletics_6|knows_power_strike_6|knows_power_draw_5|knows_inventory_management_3,roman_face_1, roman_face_2],
  #Cataphract
  ["schola_gentilium_west","Scholarius Gentilium Occidentalis","Scholarii Gentilium Occidentalis",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_culture_empire,
   [itm_half_cataphract_horse_1,itm_half_cataphract_horse_2,itm_half_cataphract_horse_8,itm_arabian_armor_b,itm_roman_military_mail_12,itm_cataphract_armor_6,itm_cataphract_armor_7,itm_iatrus_2,itm_burgh_helmet_2,itm_concesti_helmet,itm_heteny_helmet_1,itm_deurne_helmet,itm_augsburg_2_helmet,itm_augsburg_1_helmet,itm_berkasovo_2_helmet,itm_gultlingen_helmet,itm_gultlingen_helmet_plume,itm_concave_shield_roman_23,itm_arabian_sword_b,itm_heavy_lance,itm_mail_boots_manica_1,itm_mail_boots_manica_2]+greaves_roman,
   def_attrib_lvl_32|level(32),wp_one_handed(250)|wp_two_handed(240)|wp_polearm(250)|wp_archery(160)|wp_throwing(200)|wp_crossbow(150)|wp_firearm(150),knows_ironflesh_9|knows_riding_6|knows_shield_6|knows_athletics_6|knows_power_strike_6|knows_power_draw_5|knows_inventory_management_3,man_face_1, man_face_2],
  #ERE
  #Melee
  ["schola_scutariorum_east","Scholarius Scutariorum Orientalis","Scholarii Scutariorum Orientalis",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_culture_empire,
   [itm_half_cataphract_horse_1,itm_half_cataphract_horse_2,itm_half_cataphract_horse_8,itm_roman_rigid_scale_4,itm_roman_rigid_scale_5,itm_roman_squamata_1,itm_roman_squamata_2,itm_roman_squamata_4,itm_457_scale_hauberk_4,itm_457_scale_hauberk_5,itm_457_scale_hauberk_6,itm_concesti_helmet,itm_augsburg_1_helmet,itm_heteny_helmet_1,itm_deurne_helmet,itm_augsburg_2_helmet,itm_berkasovo_2_helmet,itm_gultlingen_helmet,itm_gultlingen_helmet_plume,itm_concave_shield_roman_22,itm_arabian_sword_b,itm_long_decorated_spear1]+greaves_roman,
   def_attrib_lvl_32|level(32),wp_one_handed(250)|wp_two_handed(240)|wp_polearm(240)|wp_archery(160)|wp_throwing(200)|wp_crossbow(150)|wp_firearm(150),knows_ironflesh_9|knows_riding_6|knows_shield_6|knows_athletics_6|knows_power_strike_6|knows_power_draw_5|knows_inventory_management_3,roman_face_1, roman_face_2],
  #Cataphract
  ["schola_gentilium_east","Scholarius Gentilium Orientalis","Scholarii Gentilium Orientalis",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_culture_empire,
   [itm_half_cataphract_horse_1,itm_half_cataphract_horse_2,itm_half_cataphract_horse_8,itm_arabian_armor_b,itm_roman_military_mail_12,itm_457_scale_hauberk_1,itm_457_scale_hauberk_4,itm_cataphract_armor_6,itm_cataphract_armor_7,itm_iatrus_2,itm_burgh_helmet_2,itm_concesti_helmet,itm_augsburg_1_helmet,itm_heteny_helmet_1,itm_deurne_helmet,itm_augsburg_2_helmet,itm_berkasovo_2_helmet,itm_gultlingen_helmet,itm_gultlingen_helmet_plume,itm_concave_shield_roman_24,itm_arabian_sword_b,itm_long_lance,itm_roman_greaves_manica_1,itm_roman_greaves_manica_2]+greaves_roman,
   def_attrib_lvl_32|level(32),wp_one_handed(240)|wp_two_handed(250)|wp_polearm(250)|wp_archery(160)|wp_throwing(200)|wp_crossbow(150)|wp_firearm(150),knows_ironflesh_9|knows_riding_6|knows_shield_6|knows_athletics_6|knows_power_strike_6|knows_power_draw_5|knows_inventory_management_3,man_face_1, man_face_2],

#FOEDERATI/OTHER TROOPS
  ["iuvenis_foederatus","Iuvenis Foederatus","Iuvenes Foederati",tf_guarantee_basic,0,0,fac_culture_empire, #tunic, pannonian/phrygian cap, spear, axe, seax, ridge/bandhelm
   [itm_wrapping_boots,itm_khergit_leather_boots,itm_roman_spear_2,itm_medium_spear_4,itm_securis,itm_seax_5,itm_intercisa_helmet_1,itm_augst_helmet_1,itm_ridge_helm_c,itm_narona_bandhelm_leather,itm_woolen_cap,itm_woolen_cap_c,itm_woolen_cap_1,itm_woolen_cap_2,itm_round_shield_blue_1,itm_round_shield_blue_3,itm_round_shield_green_2,itm_round_shield_red_1,itm_round_shield_red_2,itm_round_shield_yellow_1,itm_round_shield_white_1]+tunics_foederati+shoes_roman+pannonian_hats,
   def_attrib_lvl_13|level(13),wp_one_handed(150)|wp_two_handed(130)|wp_polearm(150)|wp_throwing(140),knows_lvl_13_inf|knows_shield_2|knows_power_strike_4,germanic_face_1, germanic_face_2],

  ["miles_foederatus","Miles Foederatus","Milites Foederati",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_empire,
   [itm_wrapping_boots,itm_khergit_leather_boots,itm_intercisa_helmet_1,itm_augst_helmet_1,itm_iatrus_1,itm_fernpass_helmet_1,itm_narona_bandhelm_mail,itm_heavy_spear_1,itm_long_seax_1,itm_round_shield_roman_1,itm_round_shield_roman_13]+tunics_foederati+shoes_roman,
   def_attrib_lvl_18|level(18),wp_one_handed(180)|wp_two_handed(160)|wp_polearm(180)|wp_archery(110)|wp_throwing(170),knows_lvl_18_inf|knows_shield_3|knows_power_strike_5,germanic_face_1, germanic_face_2],

  ["optimas_foederatus","Optimas Foederatus","Optimates Foederati",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_empire,
   [itm_wrapping_boots,itm_khergit_leather_boots,itm_mid_generic_mail_2,itm_mid_generic_mail_5,itm_mid_generic_mail_13,itm_mid_roman_mail_2,itm_mid_roman_mail_3,itm_457_mail_shirt_5,itm_short_roman_mail_1,itm_short_roman_mail_3,itm_457_mail_short_3,itm_fernpass_helmet_2,itm_koblenz_helmet_1,itm_gultlingen_helmet_mail,itm_gultlingen_helmet,itm_intercisa_helmet_gilded_1,itm_iatrus_1,itm_augsburg_2_helmet,itm_concesti_helmet,itm_iatrus_2,itm_christies_helmet_1,itm_tab_shield_round_e,itm_concave_shield_blue_1,itm_concave_shield_red_1,itm_concave_shield_green_2,itm_concave_shield_red_2,itm_concave_shield_yellow_1,itm_polehammer,itm_sword_medieval_a]+shoes_roman,
   def_attrib_lvl_23|level(23),wp_one_handed(220)|wp_two_handed(190)|wp_polearm(220)|wp_archery(120)|wp_throwing(210),knows_lvl_23_inf|knows_shield_4|knows_power_strike_6,roman_face_1, roman_face_2],

  ["eques_alae","Eques Ala","Equites Alae",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_culture_empire,
   [itm_ankle_boots,itm_roman_spear_3,itm_sword_medieval_a,itm_tab_shield_small_round_b,itm_normal_horse23,itm_normal_horse24,itm_narona_bandhelm,itm_narona_bandhelm_cloth,itm_narona_bandhelm_mail,itm_narona_bandhelm_leather,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_koblenz_helmet_1,itm_round_shield_roman_small_1,itm_round_shield_roman_small_13]+mail_numeri+tunics_foederati+horses_roman_1+horses_roman_2,
   def_attrib_lvl_23|level(23),wp_one_handed(200)|wp_polearm(200)|wp_throwing(200),knows_lvl_23_cav|knows_shield_3|knows_power_strike_6,germanic_face_1, germanic_face_2],

  ["eques_indiginae","Eques Indiginae Saraceni","Equites Indiginae Saraceni",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_horse|tf_guarantee_polearm|tf_guarantee_ranged,0,0,fac_culture_empire,
   [itm_arabian_horse_d,itm_arabian_horse_c,itm_arabian_horse_a,itm_arabian_horse_b,itm_cavalry_javelins,itm_roman_spear_3,itm_sword_khergit_3,itm_ridge_helm_c,itm_intercisa_helmet_1,itm_augst_helmet_1,itm_haditha_1,itm_iatrus_helmet_mail,itm_tarasovsky_1784_helmet_cloth,itm_tarasovsky_1784_helmet_leather,itm_tarasovsky_1784_helmet_arab]+tunics_romans_military+shoes_roman+hats_arabs,
   def_attrib_lvl_18|level(18),wp_one_handed(160)|wp_two_handed(150)|wp_polearm(170)|wp_throwing(170),knows_ironflesh_4|knows_power_strike_6|knows_power_throw_6|knows_riding_5|knows_horse_archery_5|knows_athletics_4,arab_face_1, arab_face_2],

  ["dromodarius","Dromodarius","Dromodarii",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_culture_empire,
   [itm_camel,itm_heavy_lance,itm_sword_khergit_3,itm_ridge_helm_c,itm_intercisa_helmet_1,itm_augst_helmet_1,itm_iatrus_helmet_mail,itm_tarasovsky_1784_helmet_cloth,itm_tarasovsky_1784_helmet_leather,itm_tarasovsky_1784_helmet_arab,itm_haditha_1]+tunics_romans_military+shoes_roman+hats_arabs,
   def_attrib_lvl_18|level(18),wp_one_handed(170)|wp_two_handed(150)|wp_polearm(160)|wp_throwing(160),knows_ironflesh_6|knows_power_strike_6|knows_riding_4|knows_shield_2|knows_athletics_4,arab_face_1, arab_face_2],

  ["eastern_archer","Sagittarius Mercenarius Orientalis","Sagittarii Mercenarii Orientalis",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bodkin_arrows,itm_bodkin_arrows,itm_nomad_bow,itm_strong_bow,itm_yrzi_bow_1,itm_nomad_boots,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_sarranid_boots_a,itm_arabian_tunic_1,itm_roman_arabian_kaftan,itm_kaftan_tunic_3,itm_roman_shirt_8,itm_sarranid_cloth_robe_c,itm_eastern_leather_cap,itm_padded_coif,itm_fighting_axe,itm_bamboo_spear],
   def_attrib_lvl_18|level(18),wp_one_handed (160) | wp_two_handed (100) | wp_polearm (170) | wp_archery (180) | wp_crossbow (100) | wp_throwing (100),knows_archer,persian_face_1, persian_face_2], 
 
  #only used if noviodunum or any castles in northern gaul falls
  ["miles_arborychoi","Miles Arborychoi","Milites Arborychoi",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_culture_empire,
   [itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_5,itm_hunter_boots,itm_khergit_leather_boots,itm_457_mail_short_2,itm_457_mail_shirt_2,itm_457_mail_long_2,itm_mid_roman_mail_3,itm_roman_subarmalis_new_2,itm_subarmalis_4,itm_intercisa_helmet_1,itm_augst_helmet_1,itm_burgh_helmet_1,itm_fernpass_helmet_2,itm_burgh_helmet_mail,itm_narona_bandhelm_mail,itm_late_roman_spear_2,itm_arabian_sword_a,itm_heavy_throwing_axes,itm_oval_shield_green_2,itm_oval_shield_orange_2],
   def_attrib_lvl_23|level(23),wp_one_handed(210)|wp_two_handed(210)|wp_polearm(210)|wp_throwing(220),knows_lvl_23_inf|knows_shield_5|knows_power_strike_5,germanic_face_1, germanic_face_2],

  ["gallic_infantry","Miles Gallo-Romanum","Milites Gallo-Romanum",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_7,
   [itm_roman_spear_3,itm_sword_medieval_a,itm_oval_shield_red_2,itm_oval_shield_green_2,itm_wrapping_boots,itm_roman_military_tunic_1,itm_roman_military_tunic_7,itm_roman_military_tunic_8,itm_roman_shirt_4,itm_roman_shirt_8,itm_roman_shirt_13,itm_ridge_helm_c,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_burgh_helmet_1,itm_iatrus_1]+shoes_roman,
   def_attrib_lvl_23|level(23),wp_one_handed(200)|wp_two_handed(190)|wp_polearm(225)|wp_throwing(190),knows_lvl_23_inf|knows_shield_6|knows_power_strike_4,roman_face_1, roman_face_2],
  #mounted
  ["gallic_bodyguard","Conviva Regis","Convivae Regis",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_7, #gallo-roman antrustion
   [itm_roman_light_scale_5,itm_medium_scale_4,itm_roman_rigid_scale_4,itm_banded_armor,itm_cuir_bouilli,itm_mid_roman_mail_6,itm_long_roman_mail_4,itm_457_scale_hauberk_2,itm_iatrus_2,itm_intercisa_helmet_gilded_1,itm_burgh_helmet_2,itm_gultlingen_helmet,itm_augsburg_2_helmet,itm_sword_khergit_4,itm_tab_shield_round_e]+greaves_roman,
   def_attrib_lvl_30|level(30),wp_one_handed(240)|wp_two_handed(230)|wp_polearm(220)|wp_throwing(230),knows_lvl_30_inf|knows_shield_7|knows_power_strike_6,roman_face_1, roman_face_2],

  ["roman_slinger","Funditor","Funditores",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_flintlock_pistol,itm_sling_bullet,itm_sling_bullet,itm_securis,itm_round_shield_roman_7,itm_intercisa_helmet_1,itm_augst_helmet_1,itm_intercisa_helmet_2]+tunics_romans_military+shoes_roman+pannonian_hats,
   def_attrib_lvl_18|level(18),wp_one_handed(160) | wp_archery(100) | wp_crossbow(10) | wp_throwing(100) | wp_firearm(200),knows_lvl_18_inf|knows_power_strike_5|knows_shield_3,roman_face_1, roman_face_2],

  ["imperial_signifer","Vexillarius","Vexillarii",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_culture_empire,
   [itm_flag_pole_1,itm_457_mail_shirt_1,itm_457_mail_shirt_2,itm_457_mail_short_1,itm_mid_roman_mail_8,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_intercisa_helmet_gilded_1]+shoes_roman,
   def_attrib_lvl_23|level(23),wp_polearm(190)|wp_one_handed(190)|wp_two_handed(190),knows_lvl_23_inf|knows_power_strike_6|knows_shield_4,roman_face_1, roman_face_2],

  ["roman_marine","Marinus","Marini",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_culture_empire, #dressed in blue, has round shield, javelins, spatha and potential falx
   [itm_roman_military_tunic_4,itm_roman_subarmalis_new_4,itm_457_mail_shirt_5,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_iatrus_1,itm_christies_helmet_1,itm_koblenz_helmet_1,itm_concave_shield_blue_1,itm_concave_shield_blue_2,itm_concave_shield_blue_3,itm_sword_medieval_a,itm_falx,itm_throwing_spears] + shoes_roman + pannonian_hats,
   def_attrib_lvl_20|level(20),wp_one_handed(220) | wp_two_handed (190) | wp_polearm(190) | wp_archery(100) | wp_crossbow(10) | wp_throwing(220) | wp_firearm(200),knows_lvl_18_inf|knows_athletics_7|knows_shield_5|knows_power_strike_5,roman_face_1, roman_face_2],

  ["bucellarius","Bucellarius","Bucellarii",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_culture_empire, #primarily melee guard cavalry, well equipped -> role of HA will come later with Belisarius
   [itm_half_cataphract_horse_1,itm_half_cataphract_horse_2,itm_imperial_courser,itm_imperial_saddle_horse_1,itm_imperial_saddle_horse_3,itm_roman_light_scale_5,itm_roman_rigid_scale_4,itm_cuir_bouilli,itm_mid_roman_mail_3,itm_roman_lamellar_1,itm_heteny_helmet_1,itm_iatrus_2,itm_burgh_helmet_2,itm_intercisa_helmet_gilded_1,itm_intercisa_helmet_rich_3,itm_concesti_helmet,itm_gultlingen_helmet_plume,itm_gultlingen_helmet_feathers,itm_augsburg_1_helmet,itm_augsburg_2_helmet,itm_tsaritsyno_2_2,itm_christies_helmet_1,itm_koblenz_helmet_1,itm_sword_khergit_4,itm_late_roman_spear_1,itm_tab_shield_small_round_c]+greaves_roman,
   def_attrib_lvl_28|level(28),wp_one_handed(230)|wp_two_handed(230)|wp_polearm(230)|wp_archery(150)|wp_throwing(160)|wp_crossbow(140)|wp_firearm(140),knows_ironflesh_8|knows_power_draw_5|knows_riding_6|knows_athletics_6|knows_horse_archery_6|knows_power_strike_7|knows_inventory_management_3|knows_shield_4,man_face_1, man_face_2],

  #team thugs - player will 
  ["blue_thug","Blue Thug","Blue Thugs",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_blue_team,
   [itm_wrapping_boots,itm_roman_military_tunic_4,itm_linen_shirt_1,itm_roman_shirt_10,itm_roman_shirt_13,itm_roman_shirt_16,itm_simple_tunic_3,itm_simple_tunic_7,itm_leather_cap,(itm_club,imod_heavy),itm_dagger,itm_stones]+pannonian_hats+shoes_roman,
   def_attrib_lvl_13|level(13),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(120)|wp_throwing(140),knows_lvl_13_inf|knows_power_strike_5|knows_shield_1,roman_face_1, roman_face_2],

  ["green_thug","Green Thug","Green Thugs",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_green_team,
   [itm_wrapping_boots,itm_roman_military_tunic_5,itm_linen_shirt_16,itm_generic_tunic_11,itm_leather_cap,(itm_club,imod_heavy),itm_dagger,itm_stones]+pannonian_hats+shoes_roman,
   def_attrib_lvl_13|level(13),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(120)|wp_throwing(140),knows_lvl_13_inf|knows_power_strike_5|knows_shield_1,roman_face_1, roman_face_2],

#CIVILIAN UNITS
#lvl 9, cheap troops that can spawn during siege events
  #armed with a club, chipped axe, sword - roman cultures
  ["roman_civilian","Civis Armatura","Civites Armaturae",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_commoners,
   [itm_straw_hat,itm_simple_shield_1,itm_simple_shield_2,(itm_club,imod_heavy),(itm_sword_khergit_3,imod_chipped),(itm_securis,imod_chipped)]+pannonian_hats+shoes_roman+tunics_roman_civilian+hoods_roman_1+hoods_roman_2+hoods_roman_3,
   def_attrib_lvl_9|level(9),wp(100),knows_lvl_9,roman_face_1, roman_face_2],
  #armed with a spear, old axe - germanic cultures
  ["germanic_civilian","Germanic Peasant (Gawjamann)","Germanic Peasants (Gawjamanni)",tf_guarantee_basic,0,0,fac_commoners,
   [itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,itm_linen_shirt_1,itm_linen_shirt_2,itm_linen_shirt_3,itm_linen_shirt_10,itm_linen_shirt_13,itm_linen_shirt_14,itm_woolen_cap_4,itm_woolen_cap_b,itm_woolen_cap_6,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_simple_shield_3,itm_simple_shield_4,itm_spear,(itm_hand_axe,imod_chipped),]+shoes_generic+hats_german,
   def_attrib_lvl_9|level(9),wp(100),knows_lvl_9,germanic_face_1, germanic_face_2],
  #armed with wooden javelins, clubs - gothic cultures
  ["gothic_civilian","Gothic Peasant (Thaurpja)","Gothic Peasants (Thaurpjans)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_commoners,
   [itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,itm_linen_shirt_1,itm_linen_shirt_2,itm_linen_shirt_3,itm_linen_shirt_10,itm_linen_shirt_13,itm_linen_shirt_14,itm_generic_tunic_1,itm_generic_tunic_5,itm_generic_tunic_12,itm_woolen_cap_4,itm_woolen_cap_b,itm_woolen_cap_6,itm_woolen_cap_1,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_simple_shield_3,itm_simple_shield_4,(itm_club,imod_heavy),itm_wooden_javelin,itm_wooden_javelin]+shoes_generic,
   def_attrib_lvl_9|level(9),wp(100),knows_lvl_9,germanic_face_1, germanic_face_2],
  #armed with simple bow, arrows, spear - alans
  ["alan_civilian","Alan Peasant","Alan Peasants",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_commoners,
   [itm_simple_shoes,itm_wrapping_boots,itm_hunter_boots,itm_nomad_boots,itm_woolen_cap_c,itm_woolen_cap,itm_woolen_cap_b,itm_woolen_cap_6,itm_spear,itm_hunting_bow,itm_roman_arrows_1,itm_roman_arrows_1]+tunics_caucasian_alans,
   def_attrib_lvl_9|level(9),wp(100),knows_lvl_9,sarmatian_face_1, sarmatian_face_2],
  #armed with a bow, arrows, seax - huns
  ["hunnic_civilian","Hunnic Tribesman","Hun Tribesmen",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_commoners,
   [itm_nomad_boots,itm_simple_shoes,itm_kaftan_hunnic_red,itm_kaftan_hunnic_blue,itm_kaftan_hunnic_green,itm_kaftan_hunnic_white,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_khergit_bow,itm_roman_arrows_1,itm_roman_arrows_1,itm_long_seax_2]+tunics_hunnic+hats_huns,
   def_attrib_lvl_9|level(9),wp(100),knows_lvl_9,hunnic_face_1, hunnic_face_2],
  #armed with an axe, shield - picts
  ["pictish_civilian","Pictish Peasant","Pictish Peasants",tf_guarantee_armor|tf_guarantee_shield,0,0,fac_commoners,
   [itm_simple_shoes,itm_woolen_hose,itm_wrapping_boots,itm_p_hood,itm_brown_hood1,itm_new_hood_c,itm_new_hood_d,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_simple_shield_3,itm_simple_shield_4,(itm_pict_axe_b,imod_chipped)]+tunics_pictish,
   def_attrib_lvl_9|level(9),wp(100),knows_lvl_9,celtic_face_1, celtic_face_2],
  #armed with an axe, shield - caucasians
  ["caucasian_civilian","Caucasian Peasant","Caucasian Peasants",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_commoners,
   [itm_wrapping_boots,itm_simple_shoes,itm_nomad_boots,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_woolen_cap_1,itm_woolen_cap,itm_woolen_cap_2,itm_simple_shield_1,itm_simple_shield_2,(itm_bearded_axe_1,imod_chipped)]+tunics_caucasian,
   def_attrib_lvl_9|level(9),wp(100),knows_lvl_9,caucaus_face_1, caucaus_face_2],
  #armed with a spear, shield - nubians
  ["nubian_civilian","Nubian Tribesman","Nubian Tribesmen",tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_commoners,
   [itm_simple_shield_1,itm_simple_shield_2,itm_nubian_shield_1,itm_bamboo_spear]+tunics_nubians,
   def_attrib_lvl_9|level(9),wp(100),knows_lvl_9,nubian_face_1, nubian_face_2],
  #armed with pitchforks
  ["persian_peasant","Persian Peasant","Persian Peasants",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_polearm,0,0,fac_commoners,
   [itm_pitch_fork_1,itm_pitch_fork_2,itm_pitch_fork,itm_sickle,itm_nomad_boots,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_linen_shirt_16,itm_linen_shirt_17,itm_linen_shirt_18,itm_linen_shirt_20,itm_linen_shirt_22,itm_shirt,itm_linen_shirt_22]+tunics_sassanid, 
   def_attrib_lvl_9|level(9),wp(100),knows_lvl_9,persian_face_1, persian_face_2], 

#MINOR CULTURES

#BASQUES
  ["basque_skirmisher","Cantabri Skirmisher","Cantabri Skirmishers",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_culture_minor_1,
   [itm_wrapping_boots,itm_simple_shoes,itm_ankle_boots,itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,itm_skirmisher_tunic_2,itm_skirmisher_tunic_3,itm_linen_shirt_16,itm_linen_shirt_22,itm_leather_cap,itm_new_hood_b,itm_new_hood_c,itm_brown_hood1,itm_simancas_dagger_1,itm_simancas_dagger_2,
   itm_dagger,itm_securis,itm_basic_axe,itm_fighting_axe,itm_jarid,itm_jarid]+shields_simple+shields_small+pannonian_hats+tunics_basque,
   def_attrib_skirmisher|level(14),wp_one_handed(170)|wp_two_handed(150)|wp_polearm(175)|wp_throwing(190)|wp_archery(160)|wp_firearm(180),knows_skirmisher|knows_shield_4|knows_power_strike_4,briton_face_1, briton_face_2],

  ["basque_footman","Cantabri Footman","Cantabri Footmen",tf_guarantee_basic,0,0,fac_culture_minor_1,
   [itm_wrapping_boots,itm_simple_shoes,itm_ankle_boots,itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,itm_leather_cap,itm_new_hood_b,itm_new_hood_c,itm_brown_hood1,itm_woolen_cap,itm_woolen_cap_1,itm_woolen_cap_2,itm_bearded_axe_2,itm_bearded_axe_1,itm_simancas_dagger_1,itm_simancas_dagger_2,itm_dagger,itm_late_roman_spear_1,itm_roman_spear_3,itm_throwing_spear_2,itm_throwing_spear_2]+shields_cantabrian_1+shields_cantabrian_2+shields_generic+pannonian_hats+tunics_basque,
   def_attrib_lvl_20|level(18),wp_one_handed(200)|wp_two_handed(190)|wp_polearm(200)|wp_throwing(200)|wp_archery(135),knows_lvl_18_inf|knows_shield_5|knows_power_strike_7,briton_face_1, briton_face_2],

  ["basque_horseman","Cantabri Mounted Skirmisher","Cantabri Mounted Skirmishers",tf_mounted|tf_guarantee_basic|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_culture_minor_1,
   [itm_wrapping_boots,itm_simple_shoes,itm_ankle_boots,itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,itm_leather_cap,itm_new_hood_b,itm_new_hood_c,itm_brown_hood1,itm_woolen_cap,itm_woolen_cap_1,itm_woolen_cap_2,itm_generic_leather_helmet_cloth,(itm_intercisa_helmet_1,imod_battered),itm_iatrus_helmet_light,
   itm_battle_axe_4,itm_roman_spear_3,itm_cavalry_javelins,itm_cavalry_javelins,itm_concave_shield_leather_small_1,itm_concave_shield_leather_small_2,itm_concave_shield_leather_small_3,itm_celtic_horse_1,itm_celtic_horse_2]+shields_cantabrian_small+tunics_basque+horses_roman_1+horses_roman_2+horses_roman_3,
   def_attrib_lvl_20|level(18),wp_one_handed(190)|wp_two_handed(160)|wp_polearm(190)|wp_throwing(230)|wp_archery(130),knows_lvl_18_cav|knows_shield_4|knows_power_strike_5|knows_horse_archery_6,briton_face_1, briton_face_2],

#SLAVS
  ["slav_skirmisher","Slavic Skirmisher","Slavic Skirmishers",tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_culture_minor_2,
   [itm_simple_shoes,itm_nomad_boots,itm_wrapping_boots,itm_basic_axe,itm_hand_axe,itm_club,itm_winged_mace,itm_fur_hat,itm_throwing_spears,itm_throwing_spears,itm_eastern_germanic_shield_5]+tunics_slav+pants_slav+shields_simple,
   def_attrib_skirmisher|level(13),wp_one_handed(150)|wp_two_handed(130)|wp_polearm(130)|wp_throwing(160)|wp_archery(150),knows_skirmisher, germanic_face_1, germanic_face_2],

  ["slav_footman","Slavic Footman","Slavic Footmen",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_culture_minor_2,
   [itm_simple_shoes,itm_nomad_boots,itm_wrapping_boots,itm_cloaked_tunic_pants_9,itm_cloaked_tunic_pants_10,itm_cloaked_tunic_pants_5,itm_cloaked_tunic_pants_6,itm_cloaked_tunic_pants_7,itm_fur_hat,itm_leather_cap,itm_iatrus_helmet_light,itm_iatrus_helmet_mail,itm_javelin,itm_wicker_shields_rectangular_1,itm_wicker_shields_rectangular_2,itm_wicker_shields_rectangular_3,itm_battle_axe_4,itm_battle_axe_3,itm_medium_spear_1,itm_medium_spear_3,itm_war_spear]+tunics_slav,
   def_attrib_lvl_20|level(18),wp_one_handed(200)|wp_two_handed(190)|wp_polearm(200)|wp_throwing(180),knows_lvl_18_inf|knows_shield_4|knows_power_strike_6, germanic_face_1, germanic_face_2],

  ["slav_horseman","Slavic Horseman","Slavic Horsemen",tf_mounted|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_culture_minor_2,
   [itm_simple_shoes,itm_nomad_boots,itm_wrapping_boots,itm_cloaked_tunic_pants_9,itm_cloaked_tunic_pants_10,itm_cloaked_tunic_pants_5,itm_cloaked_tunic_pants_6,itm_cloaked_tunic_pants_7,itm_short_slavic_mail_1,itm_short_slavic_mail_2,itm_fur_hat,itm_leather_cap,itm_iatrus_helmet_light,itm_iatrus_helmet_mail,itm_tarasovsky_782,itm_tarasovsky_782_mail,itm_khergit_bow,itm_strong_bow,itm_khergit_arrows,itm_war_spear,itm_hunnic_spatha,itm_steppe_horse,itm_normal_horse13,itm_normal_horse14,itm_normal_horse15,itm_warhorse]+tunics_slav,
   def_attrib_lvl_25|level(23),wp_one_handed(240)|wp_two_handed(240)|wp_polearm(240)|wp_throwing(230),knows_lvl_23_cav|knows_power_strike_9|knows_shield_5, germanic_face_1, germanic_face_2],

#NORICUM - culture has been dissolved, player can recruit troops from castles!
  ["noricum_footman","Pedes Norici","Pedites Norici",tf_guarantee_basic,0,0,fac_kingdom_1,
   [itm_ankle_boots,itm_generic_tunic_1,itm_roman_shirt_10,itm_roman_shirt_12,itm_roman_shirt_5,itm_linen_tunic,itm_linen_shirt_1,itm_linen_shirt_18,itm_shirt,itm_generic_tunic_3,itm_roman_military_tunic_4,itm_roman_military_tunic_1,itm_narona_bandhelm_mail,itm_intercisa_helmet_1,itm_augst_helmet_1,itm_intercisa_helmet_2,itm_iatrus_1,itm_roman_spear_3,itm_roman_spear_4,itm_late_roman_spear_1,itm_late_roman_spear_2,itm_dagger,itm_securis,itm_oval_shield_blue_1,itm_oval_shield_blue_2,itm_oval_shield_red_2,itm_oval_shield_leather_1,itm_oval_shield_wood_1,itm_oval_shield_wood_2,itm_oval_shield_wood_3,itm_darts]+shoes_roman+pannonian_hats,
   def_attrib_lvl_18|level(17),wp_one_handed(160)|wp_polearm(190)|wp_throwing(190)|wp_archery(110),knows_lvl_18_inf|knows_shield_5|knows_power_strike_3,roman_face_1, roman_face_2],

  ["noricum_horseman","Eques Norici","Equites Norici",tf_mounted|tf_guarantee_basic|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_ankle_boots,itm_roman_military_tunic_4,itm_roman_military_tunic_1,itm_generic_tunic_3,itm_roman_shirt_10,itm_roman_shirt_12,itm_roman_shirt_5,itm_457_mail_shirt_5,itm_roman_subarmalis_new_4,itm_roman_subarmalis_new_7,itm_leather_armor_c,itm_short_roman_mail_1,itm_short_roman_mail_3,itm_mid_roman_mail_2,itm_leather_gloves,itm_roman_spear_4,itm_roman_spear_3,itm_late_roman_spear_1,itm_sword_khergit_2,itm_iatrus_1,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_narona_bandhelm,itm_narona_bandhelm_mail,itm_concave_shield_blue_small_1,itm_concave_shield_white_small_1,itm_cavalry_javelins,itm_cavalry_javelins]+shoes_roman+horses_roman_1+horses_roman_2+horses_roman_3,
   def_attrib_lvl_23|level(22),wp_one_handed(200)|wp_polearm(205)|wp_throwing(210)|wp_archery(110),knows_lvl_23_cav|knows_power_strike_5|knows_shield_4|knows_horse_archery_5,roman_face_1, roman_face_2],

#FRISIANS
  ["frisian_freeman","Frisesk Freeman","Frisesk Freemen",tf_guarantee_basic,0,0,fac_culture_minor_4,
   [itm_ankle_boots,itm_simple_shoes,itm_wrapping_boots,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_4,itm_carbatinae_2_grey,itm_carbatinae_1_grey,itm_linen_tunic,itm_linen_shirt,itm_shirt,itm_generic_tunic_2,itm_generic_tunic_4,itm_generic_tunic_14,itm_linen_shirt_6,itm_linen_shirt_11,itm_linen_shirt_10,itm_cloaked_tunic_5,itm_cloaked_tunic_12,itm_cloaked_tunic_10,itm_concave_shield_blue_1,itm_concave_shield_red_1,itm_concave_shield_green_2,itm_concave_shield_orange_1,itm_round_shield_germanic_22,itm_javelin,itm_roman_spear_3,itm_roman_spear_4,itm_fighting_axe,itm_bearded_axe_1,itm_seax_1,itm_seax_2,itm_seax_10,itm_long_seax_1,itm_long_seax_3,itm_woolen_cap_1,itm_woolen_cap_2,itm_woolen_cap_5,itm_woolen_cap_8,itm_ridge_helm_c,itm_triveres_cloth,itm_triveres_leather,(itm_intercisa_helmet_1,imod_battered)]+shields_generic,
   def_attrib_lvl_18|level(17),wp_one_handed(180)|wp_two_handed(170)|wp_polearm(185)|wp_throwing(170)|wp_archery(100),knows_lvl_18_inf|knows_shield_5|knows_power_strike_4,germanic_face_1, germanic_face_2],

  ["frisian_companion","Frisesk Companion","Frisesk Companions",tf_mounted|tf_guarantee_horse|tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_minor_4,
   [itm_frisian_warhorse,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_4,itm_wrapping_boots,itm_mid_generic_mail_19,itm_mid_generic_mail_7,itm_mid_generic_mail_17,itm_mid_generic_mail_18,itm_triveres_mail,itm_augst_helmet_3,itm_burgh_helmet_1,itm_burgh_helmet_2,itm_tab_shield_small_round_c,itm_concave_shield_germanic_small_1,itm_round_shield_germanic_small_22,itm_late_roman_spear_1,itm_sword_viking_c_long]+horses_germanic_4,
   def_attrib_lvl_28|level(27),wp_one_handed(250)|wp_two_handed(240)|wp_polearm(240)|wp_throwing(230)|wp_archery(100),knows_lvl_28_cav|knows_shield_6|knows_power_strike_8,germanic_face_1, germanic_face_2],

#AESTII
  ["aestii_skirmisher","Aestii Skirmisher (Karaitis)","Aestii Skirmishers (Karaitis)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_culture_minor_5,
   [itm_wrapping_boots,itm_simple_shoes,itm_skirmisher_tunic_2,itm_generic_tunic_13,itm_generic_tunic_15,itm_generic_tunic_4,itm_generic_tunic_6,itm_generic_tunic_8,itm_linen_shirt_10,itm_linen_shirt_3,itm_leather_cap,
   itm_throwing_spears,itm_throwing_spears,itm_wooden_javelin,itm_wooden_javelin,itm_club,itm_winged_mace,itm_battle_knife_1,itm_socketed_axe,itm_eastern_germanic_shield_5,itm_balt_shield_2_red,itm_balt_shield_wood_2,itm_balt_shield_2_white]+germanic_caps+shields_simple,
   def_attrib_skirmisher|level(13),wp_one_handed(140)|wp_two_handed(80)|wp_polearm(140)|wp_archery(130)|wp_throwing(180),knows_skirmisher,germanic_face_1, germanic_face_2],  

  ["aestii_tribesman","Aestii Tribesman (Kargys)","Aestii Tribesmen (Kargys)",tf_guarantee_basic,0,0,fac_culture_minor_5,
   [itm_wrapping_boots,itm_simple_shoes,itm_generic_tunic_13,itm_generic_tunic_15,itm_generic_tunic_4,itm_generic_tunic_6,itm_generic_tunic_8,itm_linen_shirt_10,itm_linen_shirt_3,itm_cloaked_tunic_5,itm_cloaked_tunic_9,itm_cloaked_tunic_11,itm_cloaked_tunic_17,itm_new_hood_b,itm_new_hood_d,itm_brown_hood1,itm_fur_hat,itm_javelin,itm_medium_spear_3,itm_boar_spear,itm_great_lance,itm_fighting_axe,itm_battle_knife_1,itm_battle_knife_2,itm_socketed_axe,itm_throwing_spear_3,itm_throwing_spear_3,
   itm_eastern_germanic_shield_1,itm_eastern_germanic_shield_2,itm_eastern_germanic_shield_3,itm_eastern_germanic_shield_4,itm_eastern_germanic_shield_5,itm_eastern_germanic_shield_6,itm_kerch_shield_wood,itm_kerch_shield_2,itm_kerch_shield_4,itm_kerch_shield_15,itm_balt_shield_1_red,itm_balt_shield_2_red,itm_balt_shield_wood_1,itm_balt_shield_wood_2,itm_balt_shield_1_white,itm_balt_shield_2_white]+germanic_caps,
   def_attrib_lvl_20|level(17),wp_one_handed(190)|wp_two_handed(130)|wp_polearm(180)|wp_archery(100)|wp_throwing(170),knows_lvl_18_inf|knows_shield_5|knows_power_strike_5,germanic_face_1, germanic_face_2],  

  ["aestii_companion","Aestii Companion (Kargisirgis)","Aestii Companions (Kargisirgis)",tf_mounted|tf_guarantee_basic|tf_guarantee_horse,0,0,fac_culture_minor_5,
   [itm_wrapping_boots,itm_simple_shoes,itm_cloaked_tunic_5,itm_cloaked_tunic_9,itm_cloaked_tunic_11,itm_cloaked_tunic_17,itm_short_ragged_mail_12,itm_short_ragged_mail_6,itm_short_ragged_mail_7,itm_iatrus_helmet_mail,(itm_intercisa_helmet_1,imod_battered),(itm_intercisa_helmet_2,imod_battered),(itm_augst_helmet_1,imod_battered),itm_baltic_sword_1,itm_war_spear,itm_warhorse,itm_hunter,itm_tab_shield_small_round_c,itm_eastern_germanic_shield_2,itm_eastern_germanic_shield_4,itm_eastern_germanic_shield_6,itm_kerch_shield_2,itm_kerch_shield_4,itm_kerch_shield_15]+horses_germanic_3+horses_germanic_4,
   def_attrib_lvl_25|level(25),wp_one_handed(235)|wp_two_handed(220)|wp_polearm(230)|wp_archery(100)|wp_throwing(230),knows_lvl_23_cav|knows_shield_5|knows_power_strike_7,germanic_face_1, germanic_face_2],  

  ["sitones_retainer","Sitones Retainer","Sitones Retainers",tf_guarantee_basic,0,0,fac_culture_minor_5, #Shvarnas
   [itm_wrapping_boots,itm_simple_shoes,itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_cloaked_generic_tunic_1,itm_cloaked_generic_tunic_5,itm_leather_armor_c,itm_kovas_hat_1,itm_kovas_hat_2,itm_kovas_hat_3,itm_kovas_hat_4,itm_sword_viking_c_long,itm_war_spear,itm_throwing_spear_2,itm_round_shield_germanic_18,itm_round_shield_germanic_20],
   def_attrib_lvl_23|level(23),wp_one_handed(230)|wp_two_handed(210)|wp_polearm(230)|wp_archery(100)|wp_throwing(220),knows_lvl_23_inf|knows_shield_5|knows_power_strike_7,germanic_face_1, germanic_face_2],  

  ["suiones_guard","Suiones Guard","Suiones Guards",tf_mounted|tf_guarantee_basic|tf_guarantee_horse,0,0,fac_culture_minor_5, #Aiwarikiar Scylfingr
   [itm_wrapping_boots,itm_simple_shoes,itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_cloaked_generic_tunic_12,itm_cloaked_generic_tunic_4,itm_cloaked_tunic_1,itm_mid_generic_mail_3,itm_mid_generic_mail_22,itm_tarasovsky_782_mail,itm_sword_viking_3,itm_polehammer,itm_concave_shield_germanic_small_17,itm_concave_shield_germanic_small_20]+horses_germanic_4,
   def_attrib_lvl_25|level(25),wp_one_handed(245)|wp_two_handed(220)|wp_polearm(220)|wp_archery(100)|wp_throwing(210),knows_lvl_23_cav|knows_shield_5|knows_power_strike_7,germanic_face_1, germanic_face_2],  

#MORDENS
  ["mordvin_skirmisher","Morden Skirmisher","Morden Skirmishers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_culture_minor_6,
   [itm_wrapping_boots,itm_simple_shoes,itm_nomad_boots,itm_skirmisher_tunic_1,itm_skirmisher_tunic_2,itm_linen_shirt_22,itm_generic_tunic_13,itm_generic_tunic_14,itm_generic_tunic_7,itm_linen_shirt_10,itm_fur_hat,itm_new_hood_d,itm_new_hood_c,itm_brown_hood1,itm_throwing_spears,itm_throwing_spears,itm_wooden_javelin,itm_wooden_javelin,itm_club,itm_mace_1,itm_seax_8,itm_hatchet,itm_simple_shield_1,itm_simple_shield_2,itm_wicker_round_shield],
   def_attrib_skirmisher|level(13),wp_one_handed(150)|wp_two_handed(130)|wp_polearm(130)|wp_throwing(160)|wp_archery(160),knows_skirmisher,germanic_face_1, germanic_face_2],

  ["mordvin_footman","Morden Footman","Morden Footmen",tf_guarantee_basic,0,0,fac_culture_minor_6,
   [itm_wrapping_boots,itm_simple_shoes,itm_nomad_boots,itm_skirmisher_tunic_1,itm_skirmisher_tunic_2,itm_linen_shirt_22,itm_generic_tunic_13,itm_generic_tunic_14,itm_generic_tunic_7,itm_linen_shirt_10,itm_cloaked_tunic_10,itm_cloaked_tunic_11,itm_cloaked_tunic_5,itm_thick_coat_1,itm_thick_coat_3,itm_thick_coat_4,itm_kaftan_alan_red,itm_fur_hat,itm_batumi_helmet_leather,itm_suvorovsky_helmet_mail,itm_suvorovsky_helmet_cloth,
   itm_long_seax_4,itm_long_seax_5,itm_medium_spear_3,itm_medium_spear_4,itm_javelin,itm_eastern_germanic_shield_1,itm_tarasovo_axe_1,itm_eastern_germanic_shield_2,itm_eastern_germanic_shield_3,itm_eastern_germanic_shield_4],
   def_attrib_lvl_20|level(18),wp_one_handed(225)|wp_two_handed(200)|wp_polearm(220)|wp_throwing(200)|wp_archery(130),knows_lvl_18_inf|knows_shield_5|knows_power_strike_7,germanic_face_1, germanic_face_2], 

  ["mordvin_mounted_skirmisher","Morden Mounted Skirmisher","Morden Mounted Skirmishers",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_culture_minor_6,
   [itm_wrapping_boots,itm_simple_shoes,itm_nomad_boots,itm_skirmisher_tunic_1,itm_skirmisher_tunic_2,itm_linen_shirt_22,itm_generic_tunic_13,itm_generic_tunic_14,itm_generic_tunic_7,itm_linen_shirt_10,itm_cloaked_tunic_10,itm_cloaked_tunic_11,itm_cloaked_tunic_5,itm_kaftan_alan_red,itm_cavalry_javelins,itm_cavalry_javelins,itm_sword_khergit_1]+horses_alans_1,
   def_attrib_lvl_18|level(18),wp_one_handed(200)|wp_two_handed(200)|wp_polearm(200)|wp_throwing(200)|wp_archery(160),knows_lvl_18_cav|knows_horse_archery_5|knows_power_strike_5|knows_shield_1,germanic_face_1, germanic_face_2], 

  ["mordvin_companion","Morden Companion","Morden Companions",tf_mounted|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_culture_minor_6,
   [itm_wrapping_boots,itm_simple_shoes,itm_nomad_boots,itm_steppe_plated_armor_6,itm_steppe_plated_armor_9,itm_steppe_plated_armor_4,itm_steppe_plated_armor_1,itm_tarasovsky_782,itm_tarasovsky_782_mail,itm_suvorovsky_helmet_mail,itm_batumi_helmet_aventail,itm_hunnic_spatha,itm_lance,itm_heavy_lance]+horses_alans_2,
   def_attrib_lvl_28|level(28),wp_one_handed(250)|wp_two_handed(240)|wp_polearm(260)|wp_throwing(210)|wp_archery(130),knows_lvl_28_cav|knows_shield_5|knows_power_strike_8,germanic_face_1, germanic_face_2],

  ["komi_warrior","Roga Warrior","Roga Warriors",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_minor_6,
   [itm_wrapping_boots,itm_simple_shoes,itm_khergit_leather_boots,itm_nomad_boots,itm_mid_generic_mail_11,itm_mid_generic_mail_22,itm_mid_generic_mail_27,itm_kaftan_hunnic_4,itm_kaftan_hunnic_red,itm_kaftan_hunnic_white,itm_tarasovo_helmet_1,itm_suvorovsky_helmet_mail,itm_tarasovo_poleaxe_1,itm_spear_sword,itm_klin_yar_spatha,itm_tab_shield_small_round_b,itm_concave_shield_leather_3], #temp klin yar spatha
   def_attrib_lvl_28|level(28),wp_one_handed(250)|wp_two_handed(260)|wp_polearm(260)|wp_throwing(180)|wp_archery(130),knows_lvl_28_inf|knows_shield_6|knows_power_strike_7,germanic_face_1, germanic_face_2],

#SCANDANAVIANS
  ["scandinavian_freeman","Scandzae Freeman (Karilar)","Scandzae Freemen (Karilar)",tf_guarantee_basic,0,0,fac_culture_minor_7,
   [itm_wrapping_boots,itm_ankle_boots,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,itm_linen_shirt_1,itm_linen_shirt_2,itm_linen_shirt_3,itm_linen_shirt_10,itm_linen_shirt_13,itm_generic_tunic_5,itm_generic_tunic_15,itm_cloaked_tunic_8,itm_cloaked_tunic_9,itm_mace_1,itm_seax_1,itm_fighting_axe,itm_throwing_spear_3,itm_boar_spear,itm_medium_spear_3,itm_round_shield_white_1,itm_round_shield_yellow_1,itm_round_shield_blue_2,itm_drengsted_helmet_leather,itm_burgh_helmet_light]+shields_generic+germanic_caps,
   def_attrib_lvl_18|level(17),wp_one_handed(180)|wp_two_handed(160)|wp_polearm(160)|wp_throwing(160)|wp_archery(90),knows_lvl_18_inf|knows_shield_3|knows_power_strike_5,germanic_face_1, germanic_face_2],

  ["scandinavian_retainer","Scandzae Retainer (Heimathegar)","Scandzae Retainers (Heimathegar)",tf_guarantee_basic,0,0,fac_culture_minor_7,
   [itm_tab_shield_round_d,itm_wrapping_boots,itm_ankle_boots,itm_roman_lorum_fasciari_3,itm_roman_lorum_fasciari_4,itm_cloaked_tunic_8,itm_cloaked_tunic_9,itm_mid_generic_mail_9,itm_mid_generic_mail_7,itm_short_ragged_mail_3,itm_short_ragged_mail_7,itm_drengsted_helmet_leather,itm_burgh_helmet_light,itm_drengsted_helmet_mail,itm_burgh_helmet_mail,itm_tarasovsky_782_mail,itm_seax_10,itm_long_seax_3,itm_boar_spear,itm_war_spear,itm_sword_medieval_c_long,itm_sword_viking_1,itm_round_shield_germanic_9,itm_round_shield_germanic_20]+germanic_caps,
   def_attrib_lvl_23|level(23),wp_one_handed(210)|wp_two_handed(160)|wp_polearm(190)|wp_throwing(160)|wp_archery(90),knows_lvl_23_inf|knows_shield_5|knows_power_strike_6,germanic_face_1, germanic_face_2],

  ["scandinavian_comes","Scandzae Bodyguard (Thegnar)","Scandzae Bodyguards (Thegnar)",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_culture_minor_7,
   [itm_wrapping_boots,itm_ankle_boots,itm_mid_generic_mail_9,itm_mid_generic_mail_7,itm_mid_generic_mail_25,itm_mid_generic_mail_12,itm_mid_generic_mail_13,itm_gultlingen_helmet_mail,itm_gultlingen_helmet,itm_tarasovsky_782,itm_drengsted_helmet_mail,itm_burgh_helmet_mail,itm_burgh_helmet_1,itm_war_spear,itm_sword_viking_2,itm_sword_viking_c_long,itm_tab_shield_round_e,itm_tab_shield_small_round_c],
   def_attrib_lvl_28|level(28),wp_one_handed(240)|wp_two_handed(220)|wp_polearm(230)|wp_throwing(160)|wp_archery(90),knows_lvl_28_inf|knows_shield_6|knows_power_strike_8,germanic_face_1, germanic_face_2],

  ["dane_vanguard","Danir Vanguard (Ordfruman)","Danir Vanguards (Ordfruman)",tf_guarantee_basic,0,0,fac_culture_minor_7,
   [itm_obenaltendorf_shoes_1,itm_obenaltendorf_shoes_2,itm_wrapping_boots,itm_simple_shoes,itm_cloaked_generic_tunic_4,itm_cloaked_generic_tunic_12,itm_cloaked_tunic_1,itm_mid_generic_mail_3,itm_mid_generic_mail_6,itm_drengsted_helmet_mail,itm_woolen_cap_2,itm_woolen_cap_3,itm_battle_axe,itm_angon_1,itm_round_shield_germanic_19],
   def_attrib_lvl_23|level(23),wp_one_handed(210)|wp_two_handed(210)|wp_polearm(190)|wp_throwing(200)|wp_archery(90),knows_lvl_23_inf|knows_shield_4|knows_power_strike_7,germanic_face_1, germanic_face_2],

  ["saami_hunter","Scerefennae Hunter","Scerefennae Hunters",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_culture_minor_7,
   [itm_wrapping_boots,itm_simple_shoes,itm_skirmisher_tunic_4,itm_linen_shirt_10,itm_linen_shirt_14,itm_linen_shirt,itm_kovas_hat_1,itm_kovas_hat_2,itm_kovas_hat_3,itm_kovas_hat_4,itm_polehammer,itm_short_bow,itm_germanic_arrows,itm_germanic_arrows],
   def_attrib_lvl_18|level(18),wp_one_handed(170)|wp_two_handed(160)|wp_polearm(150)|wp_archery(155)|wp_throwing(130),knows_archer,germanic_face_1, germanic_face_2],

#CRIMEAN GOTHS/TETRAXITAE
  ["crimean_gothic_skirmisher","Tetraxitae Youth (Junga)","Tetraxitae Youth (Jungans)",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_culture_minor_8,
   [itm_wrapping_boots,itm_ankle_boots,itm_simple_shoes,itm_khergit_leather_boots,itm_hunter_boots,itm_tunic_long_pants_3,itm_tunic_long_pants_5,itm_tunic_long_pants_6,itm_tunic_long_pants_7,itm_hunnic_phrygian_2,itm_hunnic_phrygian_3,itm_woolen_cap_4,itm_woolen_cap_2,itm_woolen_cap_1,itm_javelin,itm_javelin,itm_winged_mace,itm_mace_1,itm_wicker_round_shield]+shields_simple,
   def_attrib_skirmisher|level(13),wp_one_handed(140)|wp_two_handed(120)|wp_polearm(130)|wp_throwing(160)|wp_archery(140),knows_skirmisher,germanic_face_1, germanic_face_2],

  ["crimean_gothic_mounted_skirmisher","Tetraxitae Scout (Spaikulatur)","Tetraxitae Scouts (Spaikulatureis)",tf_mounted|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_culture_minor_8,
   [itm_wrapping_boots,itm_ankle_boots,itm_simple_shoes,itm_khergit_leather_boots,itm_hunter_boots,itm_tunic_long_pants_3,itm_tunic_long_pants_5,itm_tunic_long_pants_6,itm_tunic_long_pants_7,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_hunnic_phrygian_2,itm_hunnic_phrygian_3,itm_woolen_cap_4,itm_woolen_cap_2,itm_woolen_cap_1,itm_cavalry_javelins,itm_cavalry_javelins,itm_roman_spear_3,itm_fighting_axe]+horses_alans_1+shields_crimean_goth_1+shields_crimean_goth_2,
   def_attrib_lvl_18|level(17),wp_one_handed(170)|wp_two_handed(100)|wp_polearm(180)|wp_throwing(190)|wp_archery(140),knows_lvl_18_cav|knows_shield_2|knows_power_strike_3|knows_horse_archery_5,germanic_face_1, germanic_face_2],

  ["crimean_gothic_freeman","Tetraxitae Freeman (Frijis)","Tetraxitae Freemen (Frijai)",tf_guarantee_basic,0,0,fac_culture_minor_8,
   [itm_wrapping_boots,itm_ankle_boots,itm_simple_shoes,itm_khergit_leather_boots,itm_hunter_boots,itm_tunic_long_pants_1,itm_tunic_long_pants_2,itm_tunic_long_pants_3,itm_tunic_long_pants_4,itm_tunic_long_pants_5,itm_tunic_long_pants_6,itm_tunic_long_pants_7,itm_tunic_long_pants_8,itm_cloaked_tunic_pants_1,itm_cloaked_tunic_pants_2,itm_cloaked_tunic_pants_3,itm_cloaked_tunic_pants_4,itm_cloaked_tunic_pants_5,itm_cloaked_tunic_pants_6,itm_cloaked_tunic_pants_7,itm_cloaked_tunic_pants_8,
   itm_woolen_cap_4,itm_woolen_cap_2,itm_woolen_cap_1,itm_hunnic_phrygian_2,itm_hunnic_phrygian_3,itm_hunnic_phrygian_leather,itm_tarasovsky_1784_helmet_cloth,itm_tarasovsky_1784_helmet_leather,itm_seax_1,itm_fighting_axe,itm_spear,itm_medium_spear_4,itm_boar_spear]+shields_crimean_goth_1+shields_crimean_goth_2+shields_crimean_goth_3,
   def_attrib_lvl_20|level(18),wp_one_handed(180)|wp_two_handed(150)|wp_polearm(180)|wp_throwing(160),knows_lvl_18_inf|knows_shield_5|knows_power_strike_5,germanic_face_1, germanic_face_2],

  ["crimean_gothic_warrior","Tetraxitae Warrior (Gadrauhts)","Tetraxitae Warriors (Gadrauhteis)",tf_guarantee_basic,0,0,fac_culture_minor_8,
   [itm_wrapping_boots,itm_ankle_boots,itm_simple_shoes,itm_khergit_leather_boots,itm_hunter_boots,itm_cloaked_tunic_pants_1,itm_cloaked_tunic_pants_2,itm_cloaked_tunic_pants_3,itm_cloaked_tunic_pants_4,itm_cloaked_tunic_pants_5,itm_cloaked_tunic_pants_6,itm_cloaked_tunic_pants_7,itm_cloaked_tunic_pants_8,itm_rich_mail_1,itm_rich_mail_2,itm_rich_mail_3,itm_rich_mail_4,itm_rich_mail_5,itm_rich_mail_6,itm_rich_mail_7,itm_rich_mail_8,
   itm_tarasovsky_1784_helmet_mail_1,itm_tarasovsky_1784_helmet_mail_2,itm_turaevo_helmet,itm_iatrus_1,itm_kalhkni_helmet_mail,itm_kalhkni_helmet_1,itm_great_lance,itm_spear_sword,itm_long_seax_4,itm_tetraxitae_spatha]+shields_crimean_goth_2+shields_crimean_goth_3,
   def_attrib_lvl_23|level(23),wp_one_handed(210)|wp_two_handed(170)|wp_polearm(210)|wp_throwing(180),knows_lvl_23_inf|knows_shield_6|knows_power_strike_6,germanic_face_1, germanic_face_2],

  ["crimean_gothic_horseman","Tetraxitae Horseman (Aihvja)","Tetraxitae Horsemen (Aihvjans)",tf_mounted|tf_guarantee_basic|tf_guarantee_horse,0,0,fac_culture_minor_8,
   [itm_wrapping_boots,itm_ankle_boots,itm_simple_shoes,itm_khergit_leather_boots,itm_hunter_boots,itm_cloaked_tunic_pants_1,itm_cloaked_tunic_pants_2,itm_cloaked_tunic_pants_3,itm_cloaked_tunic_pants_4,itm_cloaked_tunic_pants_5,itm_cloaked_tunic_pants_6,itm_cloaked_tunic_pants_7,itm_cloaked_tunic_pants_8,itm_tarasovsky_1784_helmet_leather,itm_tsaritsyno_2_1,itm_iatrus_helmet_mail,itm_woolen_cap_4,itm_woolen_cap_2,itm_woolen_cap_1,itm_hunnic_phrygian_leather,itm_roman_spear_3,itm_hunnic_spatha,itm_concave_shield_germanic_small_8,itm_concave_shield_germanic_small_9,itm_concave_shield_germanic_small_10,itm_concave_shield_germanic_small_11,itm_tab_shield_small_round_c,itm_normal_horse12,itm_normal_horse14,itm_normal_horse15,itm_imperial_saddle_horse_4]+shields_crimean_goth_1+shields_crimean_goth_2+shields_crimean_goth_3,
   def_attrib_lvl_23|level(23),wp_one_handed(200)|wp_two_handed(170)|wp_polearm(220)|wp_throwing(220),knows_lvl_23_cav|knows_shield_4|knows_power_strike_7,germanic_face_1, germanic_face_2],

  ["crimean_gothic_companion","Tetraxitae Companion (Gasinthja)","Tetraxitae Companions (Gasinthjans)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_polearm|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_culture_minor_8,
   [itm_wrapping_boots,itm_ankle_boots,itm_simple_shoes,itm_khergit_leather_boots,itm_hunter_boots,itm_rich_mail_1,itm_rich_mail_2,itm_rich_mail_3,itm_rich_mail_4,itm_rich_mail_5,itm_rich_mail_6,itm_rich_mail_7,itm_rich_mail_8,itm_eastern_scale_4,itm_leather_gloves,itm_tarasovsky_1784_helmet_mail_2,itm_concesti_helmet,itm_kalhkni_helmet_mail,itm_kalhkni_helmet_1,itm_kalhkni_helmet_2,itm_kishpek_helmet_mail,itm_kerch_lamellenhelm_gilded,itm_turaevo_helmet,itm_iatrus_1,itm_tetraxitae_spatha,itm_spear_sword,itm_heavy_lance,itm_warhorse,itm_courser,itm_tab_shield_small_round_c]+shields_crimean_goth_2+shields_crimean_goth_3,
   def_attrib_lvl_28|level(28),wp_one_handed(235)|wp_two_handed(220)|wp_polearm(250)|wp_throwing(210),knows_lvl_28_cav|knows_shield_6|knows_power_strike_8,germanic_face_1, germanic_face_2],

#WESTERN ALANS
  #Eques Laeti Alanorum -> Eques Alae Alanorum -> Eques Cataphracti Alanorum
  ["western_alan_rider","Eques Laeti Alanorum","Equites Laeti Alanorum",tf_mounted|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_horse,0,0,fac_culture_minor_9,
   [itm_simple_shoes,itm_wrapping_boots,itm_nomad_boots,itm_ankle_boots,itm_skirmisher_tunic_1,itm_skirmisher_tunic_3,itm_linen_shirt_10,itm_linen_shirt_2,itm_linen_shirt_13,itm_woolen_cap_4,itm_woolen_cap_2,itm_woolen_cap,itm_woolen_cap_8,itm_generic_leather_helmet_cloth,itm_iatrus_helmet_light,itm_intercisa_helmet_1,itm_roman_spear_3,itm_fighting_axe,itm_wicker_round_shield,itm_javelin] + horses_alans_1,
   def_attrib_lvl_18|level(17),wp_one_handed(170)|wp_two_handed(150)|wp_polearm(190)|wp_archery(120)|wp_throwing(150)|wp_crossbow(70)|wp_firearm(70),knows_lvl_18_cav|knows_shield_2|knows_power_strike_4|knows_horse_archery_5,sarmatian_face_1, sarmatian_face_2],

  ["western_alan_lancer","Eques Alae Alanorum","Equites Alae Alanorum",tf_mounted|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_horse,0,0,fac_culture_minor_9,
   [itm_simple_shoes,itm_wrapping_boots,itm_ankle_boots,itm_mid_generic_mail_26,itm_mid_generic_mail_23,itm_mid_generic_mail_3,itm_steppe_kaftan_1,itm_steppe_kaftan_3,itm_iatrus_helmet_mail,itm_intercisa_helmet_1,itm_iatrus_1,itm_augst_helmet_1,itm_light_lance,itm_sword_khergit_3] + horses_alans_1 + horses_alans_2,
   def_attrib_lvl_23|level(23),wp_one_handed(190)|wp_two_handed(190)|wp_polearm(230)|wp_archery(140)|wp_throwing(150)|wp_crossbow(70)|wp_firearm(70),knows_lvl_23_cav|knows_shield_2|knows_power_strike_6|knows_horse_archery_5,sarmatian_face_1, sarmatian_face_2],

  ["western_alan_cataphract","Eques Cataphracti Alanorum","Equites Cataphracti Alanorum",tf_mounted|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_polearm|tf_guarantee_horse,0,0,fac_culture_minor_9,
   [itm_wrapping_boots,itm_heavy_greaves,itm_coat_of_plates_red,itm_arabian_armor_b,itm_long_mail_new_8,itm_koblenz_helmet_1,itm_christies_helmet_1,itm_burgh_helmet_1,itm_iatrus_1,itm_burgh_helmet_2,itm_iatrus_2,itm_koblenz_helmet_2,itm_kishpek_helmet_mail,itm_heavy_lance,itm_beja_spatha,itm_strong_bow,itm_khergit_bow,itm_roman_arrows_2]+horses_alans_2,
   def_attrib_lvl_28|level(28),wp_one_handed(220)|wp_two_handed(220)|wp_polearm(260)|wp_archery(160)|wp_throwing(150)|wp_crossbow(70)|wp_firearm(70),knows_cataphract,sarmatian_face_1, sarmatian_face_2],

#TAIFALS
  #armed with sword, spear, shield - settled in pictavis + synnada - would serve under Roman, Hunnic, Visigothic + Frankish banners
  ["eques_laeti_taifali","Eques Laeti Taifali","Equites Laeti Taifali",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_commoners,
   [itm_roman_lorum_fasciari_1,itm_hunter_boots,itm_khergit_leather_boots,itm_generic_tunic_1,itm_generic_tunic_11,itm_roman_shirt_4,itm_roman_shirt_10,itm_subarmalis_3,itm_augst_helmet_1,itm_iatrus_1,itm_sword_medieval_b,itm_roman_spear_3,itm_round_shield_white_small_1]+horses_roman_1,
   def_attrib_lvl_18|level(17),wp_one_handed(180)|wp_two_handed(150)|wp_polearm(170)|wp_throwing(140)|wp_archery(140),knows_lvl_18_cav|knows_shield_2|knows_horse_archery_3|knows_power_strike_4,germanic_face_1, germanic_face_2],

  ["eques_alae_taifali","Eques Alae Taifali","Equites Alae Taifali",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_commoners,
   [itm_roman_lorum_fasciari_1,itm_hunter_boots,itm_khergit_leather_boots,itm_black_armor,itm_medium_scale_1,itm_medium_scale_2,itm_medium_scale_5,itm_augst_helmet_1,itm_iatrus_1,itm_iatrus_2,itm_augsburg_1_helmet,itm_arabian_sword_b,itm_roman_spear_4,itm_concave_shield_germanic_small_7,itm_round_shield_white_small_1,itm_round_shield_roman_12,itm_iberian_warhorse_germanic_2]+horses_roman_3,
   def_attrib_lvl_23|level(23),wp_one_handed(220)|wp_two_handed(200)|wp_polearm(220)|wp_throwing(160)|wp_archery(160),knows_lvl_23_cav|knows_shield_4|knows_horse_archery_4|knows_power_strike_6,germanic_face_1, germanic_face_2],

#OTHER MINOR CULTURES

#ABASGIANS
  ["abasgian_footman","Abasgian Footman","Abasgian Footmen",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_minor_abagasians,
   [itm_wrapping_boots,itm_nomad_boots,itm_kaftan_tunic_10,itm_kaftan_tunic_2,itm_kaftan_tunic_6,itm_linen_shirt_17,itm_linen_shirt_22,itm_skirmisher_tunic_2,itm_skirmisher_tunic_3,itm_kaftan_sheepskin_6,itm_kaftan_sheepskin_1,itm_kaftan_sheepskin_3,itm_javelin,itm_medium_spear_1,itm_medium_spear_3,itm_winged_mace,itm_mace_1,itm_spiked_club]+oval_shields_basic,
   def_attrib_lvl_18|level(17),wp_one_handed(170)|wp_two_handed(150)|wp_polearm(190)|wp_throwing(170)|wp_archery(90),knows_lvl_18_inf|knows_shield_5|knows_power_strike_3,caucaus_face_1, caucaus_face_2],

  ["abasgian_skirmisher","Abasgian Skirmisher","Abasgian Skirmishers",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_minor_abagasians,
   [itm_wrapping_boots,itm_nomad_boots,itm_kaftan_tunic_10,itm_kaftan_tunic_2,itm_kaftan_tunic_6,itm_linen_shirt_17,itm_linen_shirt_22,itm_skirmisher_tunic_2,itm_skirmisher_tunic_3,itm_kaftan_sheepskin_6,itm_kaftan_sheepskin_1,itm_kaftan_sheepskin_3,itm_woolen_cap,itm_woolen_cap_b,itm_woolen_cap_6,itm_woolen_cap_8,itm_jarid,itm_jarid,itm_georgian_rectangular_shield_wood_1,itm_georgian_rectangular_shield_wood_2,itm_georgian_rectangular_shield_wood_3,itm_shortened_spear,itm_fighting_axe]+shields_simple,
   def_attrib_skirmisher|level(13),wp_one_handed(120)|wp_two_handed(60)|wp_polearm(120)|wp_throwing(180)|wp_archery(150),knows_skirmisher,caucaus_face_1, caucaus_face_2],

  ["abasgian_horse_archer","Abasgian Horse Archer","Abasgian Horse Archers",tf_mounted|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_minor_abagasians,
   [itm_wrapping_boots,itm_nomad_boots,itm_kaftan_tunic_10,itm_kaftan_alan_red,itm_kaftan_alan_green,itm_steppe_kaftan_1,itm_steppe_kaftan_3,itm_kaftan_tunic_2,itm_kaftan_tunic_6,itm_linen_shirt_17,itm_linen_shirt_22,itm_skirmisher_tunic_2,itm_skirmisher_tunic_3,itm_kaftan_sheepskin_6,itm_kaftan_sheepskin_1,itm_kaftan_sheepskin_3,itm_woolen_cap,itm_woolen_cap_b,itm_woolen_cap_6,itm_woolen_cap_8,itm_strong_bow,itm_roman_arrows_2,itm_roman_arrows_2,itm_medium_spear_3,itm_fighting_axe]+horses_alans_1,
   def_attrib_lvl_18|level(18),wp_one_handed(160)|wp_two_handed(200)|wp_polearm(170)|wp_throwing(160)|wp_archery(160),knows_horse_archer,caucaus_face_1, caucaus_face_2],

  ["abasgian_nobleman","Abasgian Nobleman","Abasgian Noblemen",tf_mounted|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_minor_abagasians,
   [itm_sassanid_cavalry_boots_1,itm_sassanid_cavalry_boots_2,itm_coat_of_plates_red,itm_eastern_scale_5,itm_eastern_scale_6,itm_kaftan_lamellar_7,itm_kaftan_lamellar_9,itm_leather_gloves,itm_kalhkni_helmet_mail,itm_kalhkni_helmet_1,itm_kalhkni_helmet_2,itm_batumi_helmet_aventail,itm_khudashevsky_helmet_2,itm_long_lance,itm_hunnic_spatha,itm_hunter,itm_normal_horse26,itm_normal_horse25,itm_normal_horse23,itm_normal_horse22,itm_warhorse,itm_courser,itm_khergit_bow,itm_roman_arrows_2,itm_tab_shield_small_round_c,itm_kerch_shield_4,itm_kerch_shield_wood],
   def_attrib_lvl_28|level(28),wp_one_handed(230)|wp_two_handed(210)|wp_polearm(260)|wp_throwing(210)|wp_archery(160),knows_cataphract,caucaus_face_1, caucaus_face_2],

#POTATO-MEN (irish)
  ["irish_skirmisher","Irish Skirmisher (Ceithernach)","Irish Skirmishers (Ceithernach)",tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_minor_irish,
   [itm_woolen_hose,itm_wrapping_boots,itm_linen_shirt,itm_shirt,itm_linen_shirt_22,itm_falkirk_tunic_1,itm_falkirk_tunic_2,itm_falkirk_tunic_3,itm_falkirk_tunic_4,itm_falkirk_tunic_5,itm_roman_spear_1,itm_glaive,itm_fighting_axe,itm_celt_axe_1,itm_jarid,itm_jarid,itm_new_hood_b,itm_new_hood_c,itm_new_hood_d,itm_brown_hood1,itm_new_hood_a,itm_leather_cap]+shields_simple,
   def_attrib_lvl_18|level(16),wp_one_handed(170)|wp_two_handed(160)|wp_polearm(180)|wp_archery(155)|wp_throwing(170),knows_skirmisher|knows_shield_3|knows_power_strike_6,celtic_face_1, celtic_face_2],

  ["irish_warrior","Irish Warrior (Cliarthaire)","Irish Warriors (Cliarthaire)",tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_minor_irish,
   [itm_woolen_hose,itm_wrapping_boots,itm_linen_shirt,itm_shirt,itm_linen_shirt_22,itm_falkirk_tunic_1,itm_falkirk_tunic_2,itm_falkirk_tunic_3,itm_falkirk_tunic_4,itm_falkirk_tunic_5,itm_long_shirt_14,itm_roman_spear_1,itm_glaive,itm_fighting_axe,itm_pict_axe_a,itm_pict_axe_b,itm_coygan_dagger,itm_javelin,itm_javelin,itm_leather_cap,itm_new_hood_b,itm_new_hood_c,itm_new_hood_d,itm_brown_hood1,itm_new_hood_a,itm_vae_pictish_rectangle_1,itm_vae_pictish_rectangle_2,itm_vae_pictish_rectangle_3,itm_vae_pictish_rectangle_4,itm_vae_pictish_rectangle_5],
   def_attrib_lvl_18|level(16),wp_one_handed(180)|wp_two_handed(160)|wp_polearm(190)|wp_archery(100)|wp_throwing(180),knows_lvl_18_inf|knows_shield_4|knows_power_strike_6,celtic_face_1, celtic_face_2],

  ["irish_follower","Irish Follower (Forbfer)","Irish Followers (Forbfer)",tf_mounted|tf_guarantee_basic,0,0,fac_minor_irish,
   [itm_woolen_hose,itm_wrapping_boots,itm_long_shirt_2,itm_long_shirt_14,itm_long_shirt_15,itm_bl_tunic6,itm_bl_tunic7,itm_bl_tunic11,itm_burgh_helmet_mail,itm_burgh_helmet_light,(itm_intercisa_helmet_1,imod_battered),itm_irish_spatha_1,itm_throwing_spears,itm_throwing_spears,itm_tab_shield_small_round_c]+shields_pictish_small,
   def_attrib_lvl_28|level(28),wp_one_handed(260)|wp_two_handed(230)|wp_polearm(260)|wp_archery(100)|wp_throwing(180),knows_lvl_28_inf|knows_shield_6|knows_power_strike_8,celtic_face_1, celtic_face_2],

#ARABS
  ["arab_skirmisher","Arabian Skirmisher","Arab Skirmishers",tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
   [itm_sarranid_boots_a,itm_simple_tunic_2,itm_simple_tunic_1,itm_imperial_common_shirt,itm_kaftan_tunic_3,itm_arabian_tunic_3,itm_linen_shirt,itm_sleeveless_tunic,itm_beduin_armor_a,itm_beduin_armor_b,itm_bandana1,itm_fighting_axe,itm_short_bow,itm_nomad_bow,itm_oman_bow_2,itm_yrzi_bow_1,itm_barbed_arrows,itm_barbed_arrows]+shields_simple+hats_arabs,
   def_attrib_skirmisher|level(13),wp_one_handed(130)|wp_two_handed(90)|wp_polearm(130)|wp_throwing(150)|wp_archery(160),knows_archer,arab_face_1, arab_face_2],

  ["arab_tribesman","Arabian Tribesman","Arab Tribesmen",tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_commoners,
   [itm_sarranid_boots_a,itm_simple_tunic_2,itm_simple_tunic_1,itm_imperial_common_shirt,itm_kaftan_tunic_3,itm_arabian_tunic_3,itm_roman_arabian_kaftan,itm_arabian_tunic_1,itm_linen_shirt,itm_sleeveless_tunic,itm_beduin_armor_a,itm_beduin_armor_b,itm_bandana1,itm_sassanid_axe_1,itm_mace_1,itm_wicker_round_shield,itm_wicker_round_shield,itm_round_shield_leather_small_1,itm_concave_shield_leather_small_1,itm_concave_shield_leather_small_2,itm_concave_shield_leather_small_3,itm_roman_spear_2,itm_roman_spear_3,itm_roman_spear_4,itm_eastern_leather_cap,itm_intercisa_helmet_1,itm_tarasovsky_1784_helmet_arab]+shields_simple+hats_arabs,
   def_attrib_lvl_18|level(17),wp_one_handed(160)|wp_two_handed(90)|wp_polearm(170)|wp_throwing(160)|wp_archery(140),knows_lvl_18_inf|knows_shield_5|knows_power_strike_5,arab_face_1, arab_face_2],

  ["arab_light_cavalry","Arabian Light Cavalry","Arab Light Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_polearm|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_commoners,
   [itm_arabian_horse_a,itm_arabian_horse_b,itm_arabian_horse_c,itm_arabian_horse_d,itm_sarranid_boots_a,itm_sassanid_simple_boots_1,itm_kaftan_tunic_3,itm_arabian_tunic_3,itm_roman_arabian_kaftan,itm_arabian_tunic_1,itm_linen_shirt,itm_beduin_armor_a,itm_beduin_armor_b,itm_eastern_leather_cap,itm_tarasovsky_1784_helmet_arab,itm_intercisa_helmet_1,itm_samad_sword,itm_light_lance,itm_throwing_spears,
   itm_concave_shield_leather_small_1,itm_concave_shield_leather_small_2,itm_concave_shield_leather_small_3]+hats_arabs,
   def_attrib_lvl_20|level(20),wp_one_handed(200)|wp_two_handed(170)|wp_polearm(210)|wp_throwing(190)|wp_archery(150),knows_lvl_18_cav|knows_horse_archery_5|knows_shield_4|knows_power_strike_4,arab_face_1, arab_face_2],
   #Fawaris aka knight
  ["arab_heavy_cavalry","Arabian Heavy Cavalry","Arab Heavy Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_polearm|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_commoners,
   [itm_arabian_horse_a,itm_arabian_horse_b,itm_arabian_horse_c,itm_arabian_horse_d,itm_sassanid_cavalry_boots_2,itm_long_cataphract_mail,itm_sassanid_mail_shirt_2,itm_sassanid_long_mail_1,itm_eastern_scale_3,itm_leather_gloves,itm_warlord_coif_1,itm_warlord_coif_2,itm_coptic_scale_coif_1,itm_sarranid_horseman_helmet,itm_tarasovsky_1784_helmet_mail_1,itm_tarasovsky_1784_helmet_mail_2,itm_tarasovsky_1784_helmet_arab,itm_samad_sword,itm_polehammer,itm_lance,itm_tab_shield_small_round_c,itm_concave_shield_leather_small_1,itm_concave_shield_leather_small_2,itm_concave_shield_leather_small_3],
   def_attrib_lvl_25|level(25),wp_one_handed(230)|wp_two_handed(220)|wp_polearm(250)|wp_throwing(140)|wp_archery(160),knows_lvl_23_cav|knows_shield_6|knows_power_strike_7,arab_face_1, arab_face_2],

  #https://en.wikipedia.org/wiki/Parabalani - can be recruited by christians in alexandria, constantinople
  ["parabalanus","Parabalanus","Parabalani",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_roman_christians,
   [itm_wrapping_boots,itm_club,itm_winged_mace,itm_wooden_stick,itm_stones,itm_stones,itm_roman_peasant_tunic_1,itm_roman_peasant_tunic_2,itm_roman_peasant_tunic_3,itm_roman_peasant_tunic_4,itm_roman_peasant_tunic_6,itm_roman_peasant_tunic_10],
   def_attrib_lvl_18|level(15),wp_one_handed(140)|wp_two_handed(150)|wp_throwing(150),knows_lvl_18_inf|knows_power_strike_8,roman_face_1, roman_face_2],

#Tauri 
  ["tauri_axeman","Tauri Securiferus","Tauri Securiferi",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_minor_tauri,
   [itm_wrapping_boots,itm_khergit_leather_boots,itm_hunter_boots,itm_skirmisher_tunic_1,itm_skirmisher_tunic_4,itm_kaftan_sheepskin_5,itm_generic_tunic_13,itm_tunic_long_pants_4,itm_tunic_long_pants_8,itm_tunic_long_pants_5,itm_woolen_cap_1,itm_woolen_cap_8,itm_hunnic_phrygian_4,itm_hunnic_phrygian_leather,itm_battle_axe_3,itm_ad_small_shield_2,itm_throwing_spears],
   def_attrib_lvl_18|level(18),wp_one_handed(200)|wp_two_handed(170)|wp_polearm(180)|wp_archery(70)|wp_throwing(180)|wp_crossbow(70)|wp_firearm(70),knows_athletics_6|knows_ironflesh_6|knows_power_strike_6|knows_power_throw_6|knows_weapon_master_5|knows_inventory_management_3|knows_riding_2,sarmatian_face_1, sarmatian_face_2],

  ["tauri_horseman","Tauri Eques","Tauri Equites",tf_mounted|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_ranged,0,0,fac_minor_tauri,
   [itm_wrapping_boots,itm_khergit_leather_boots,itm_hunter_boots,itm_skirmisher_tunic_1,itm_skirmisher_tunic_4,itm_kaftan_sheepskin_5,itm_generic_tunic_13,itm_tunic_long_pants_4,itm_tunic_long_pants_8,itm_tunic_long_pants_5,itm_woolen_cap_1,itm_woolen_cap_8,itm_hunnic_phrygian_4,itm_hunnic_phrygian_leather,itm_roman_spear_3,itm_ad_small_shield_2,itm_throwing_spears,itm_throwing_spears]+horses_alans_1,
   def_attrib_lvl_18|level(18),wp_one_handed(190)|wp_two_handed(170)|wp_polearm(180)|wp_archery(70)|wp_throwing(190)|wp_crossbow(70)|wp_firearm(70),knows_athletics_4|knows_riding_5|knows_horse_archery_5|knows_ironflesh_5|knows_power_strike_5|knows_power_throw_6|knows_weapon_master_5|knows_inventory_management_3,sarmatian_face_1, sarmatian_face_2],

#OVERHAULED TROOPS ENDS HERE!
  #old/unused - staying in the mod for shits and giggles
  #Bosphorian Troops / Akontista Bosphorou / Bosphorian Skirmisher
  ["bosphor_recruit","Bosphoran Skirmisher (Akontista)","Bosphoran Skirmishers (Akontista)",tf_mounted|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_minor_bosphoran,
   [itm_khergit_leather_boots,itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_3,itm_skirmisher_tunic_1,itm_skirmisher_tunic_4,itm_roman_shirt_6,itm_generic_tunic_1,itm_generic_tunic_8,itm_kaftan_tunic_4,itm_kaftan_tunic_5,itm_kaftan_tunic_10,itm_linen_shirt_5,itm_roman_military_tunic_4,itm_roman_military_tunic_7,itm_roman_shirt_10,itm_roman_shirt_10,itm_linen_shirt_1,itm_woolen_cap_1,itm_woolen_cap_2,itm_woolen_cap_c,
   itm_fighting_axe,itm_roman_spear_1,itm_jarid,itm_jarid],
   def_attrib_skirmisher|level(13),wp_one_handed(130)|wp_polearm(140)|wp_throwing(170)|wp_archery(150)|wp_firearm(140),knows_skirmisher,roman_face_1, roman_face_2],
  #archer
  ["bosphor_archer","Bosphoran Archer (Toxotes)","Bosphoran Archers (Toxotai)",tf_mounted|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_minor_bosphoran,
   [itm_khergit_leather_boots,itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_3,itm_skirmisher_tunic_1,itm_skirmisher_tunic_4,itm_roman_shirt_6,itm_generic_tunic_1,itm_generic_tunic_8,itm_kaftan_tunic_4,itm_kaftan_tunic_5,itm_kaftan_tunic_10,itm_linen_shirt_5,itm_roman_military_tunic_4,itm_roman_military_tunic_7,itm_roman_shirt_10,itm_roman_shirt_10,itm_linen_shirt_1,itm_woolen_cap_1,itm_woolen_cap_2,itm_woolen_cap_c,
   itm_fighting_axe,itm_roman_spear_2,itm_khergit_bow,itm_strong_bow,itm_roman_arrows_2,itm_roman_arrows_2],
   def_attrib_lvl_18|level(17),wp_one_handed(150)|wp_polearm(160)|wp_throwing(170)|wp_archery(180)|wp_firearm(160),knows_archer,roman_face_1, roman_face_2],
  #Bosphorian Infantry / Doriphoros Bosphorou
  ["bosphor_infantry","Bosphoran Infantry (Doriphoros)","Bosphoran Infantry (Doriphoros)",tf_mounted|tf_guarantee_basic,0,0,fac_minor_bosphoran,
   [itm_khergit_leather_boots,itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_3,itm_roman_shirt_6,itm_generic_tunic_1,itm_generic_tunic_8,itm_linen_shirt_5,itm_roman_military_tunic_4,itm_roman_military_tunic_7,itm_roman_shirt_10,itm_roman_shirt_10,itm_linen_shirt_1,itm_cloaked_tunic_7,itm_cloaked_tunic_8,itm_cloaked_generic_tunic_8,itm_woolen_cap_1,itm_woolen_cap_2,itm_woolen_cap_c,itm_tarasovsky_1784_helmet_mail_2,itm_intercisa_helmet_1,itm_long_seax_2,itm_polehammer,itm_oval_shield_wood_2,itm_oval_shield_blue_1,itm_oval_shield_blue_2,itm_oval_shield_red_2,itm_oval_shield_leather_1],
   def_attrib_lvl_18|level(18),wp_one_handed(160)|wp_polearm(180)|wp_throwing(160)|wp_archery(140),knows_lvl_18_inf|knows_shield_5|knows_power_strike_3,roman_face_1, roman_face_2],
  #Bosphorian Retainer / Machairophoros Bosphorou
  ["bosphor_horseman","Bosphoran Horseman","Bosphoran Horsemen",tf_mounted|tf_guarantee_horse|tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_minor_bosphoran,
   [itm_khergit_leather_boots,itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_3,itm_sassanid_cavalry_boots_1,itm_cloaked_tunic_7,itm_cloaked_tunic_8,itm_cloaked_generic_tunic_8,itm_kaftan_alan_blue,itm_kaftan_alan_red,itm_short_ragged_mail_2,itm_short_ragged_mail_3,itm_short_roman_mail_1,itm_medium_scale_1,itm_medium_scale_3,itm_mid_generic_mail_27,itm_eastern_scale_4,itm_tarasovsky_1784_helmet_mail_2,itm_kerch_lamellenhelm,
   itm_hunnic_spatha,itm_heavy_lance,itm_kerch_shield_3,itm_kerch_shield_7,itm_nisean_roman_3,itm_hun_horse_1,itm_hun_horse_3,itm_hun_rich_horse_1],
   def_attrib_lvl_25|level(25),wp_one_handed(230)|wp_two_handed(230)|wp_polearm(250)|wp_throwing(170)|wp_archery(160),knows_lvl_23_cav|knows_shield_6|knows_power_strike_6,roman_face_1, roman_face_2],

#garamantians
  ["garamantian_warrior","Garamantian Warrior","Garamantian Warriors",tf_mounted|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_minor_garamantians,
   [itm_roman_spear_2,itm_winged_mace,itm_javelin,itm_imperial_common_shirt,itm_simple_tunic_6,itm_simple_tunic_5,itm_a_exomis_1,itm_a_exomis_2,itm_a_exomis_3,itm_berber_tunic_1,itm_african_band_1,itm_african_band_2,itm_turban,itm_desert_turban,itm_wicker_round_shield,itm_round_shield_mauri_1,itm_round_shield_mauri_small_1],
   def_attrib_lvl_20|level(18),wp_one_handed(170)|wp_polearm(200)|wp_throwing(200),knows_lvl_18_inf|knows_shield_4|knows_power_strike_6,mauri_face_1, mauri_face_2],

  ["garamantian_horseman","Garamantian Horseman","Garamantian Horsemen",tf_mounted|tf_guarantee_horse|tf_guarantee_polearm|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_minor_garamantians,
   [itm_roman_spear_3,itm_throwing_spears,itm_throwing_spears,itm_imperial_common_shirt,itm_simple_tunic_6,itm_simple_tunic_5,itm_a_exomis_1,itm_a_exomis_2,itm_a_exomis_3,itm_berber_tunic_1,itm_garamantian_armor_1,itm_garamantian_armor_2,itm_garamantian_armor_3,itm_african_band_1,itm_african_band_2,itm_turban,itm_desert_turban,itm_iatrus_helmet_light,itm_iatrus_helmet_mail,(itm_intercisa_helmet_1,imod_battered),(itm_augst_helmet_1,imod_battered),itm_wicker_round_shield,itm_round_shield_mauri_1,itm_round_shield_mauri_small_1,itm_bareback_horse_1]+horses_mauri_1,
   def_attrib_lvl_23|level(21),wp_one_handed(180)|wp_polearm(210)|wp_throwing(220),knows_lvl_18_cav|knows_shield_2|knows_power_strike_6|knows_power_throw_6|knows_horse_archery_4,mauri_face_1, mauri_face_2],

  ["african_mercenary","Subsaharan Mercenary","Subsaharan Mercenaries",tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_minor_garamantians,
   [itm_african_kilt_1,itm_a_exomis_1,itm_garamantian_armor_3,itm_african_band_1,itm_african_band_2,itm_turban,itm_desert_turban,itm_wicker_round_shield,itm_nubian_shield_2,itm_heavy_spear_1,itm_throwing_spear_2],
   def_attrib_lvl_20|level(20),wp_one_handed(170)|wp_polearm(220)|wp_throwing(190),knows_lvl_18_inf|knows_shield_4|knows_power_strike_6,nubian_face_1, nubian_face_2],

#armenian rebels
  ["armenian_bandit","Armenian Bandit","Armenian Bandits",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_armenian_rebels, #has spear, dagger, potential shield, bow, arrows + sling
   [itm_nomad_boots,itm_kaftan_sheepskin_1,itm_kaftan_sheepskin_2,itm_kaftan_tunic_1,itm_kaftan_tunic_2,itm_linen_shirt_22,itm_shirt,itm_linen_tunic,itm_skirmisher_tunic_2,itm_bandana1,itm_bandana2,itm_woolen_cap_simple_4,itm_spear,itm_great_sword,itm_flintlock_pistol,itm_cartridges,itm_cartridges]+shields_simple,
   def_attrib_lvl_13|level(12),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (130) | wp_archery (130) | wp_crossbow (100) | wp_throwing (100) | wp_firearm(130),knows_ironflesh_1|knows_power_strike_1|knows_power_draw_4|knows_athletics_3,caucaus_face_1, caucaus_face_2], 

  ["armenian_rebel","Armenian Rebel","Armenian Rebels",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_armenian_rebels, #short sword, small round shield, bow, sling
   [itm_nomad_boots,itm_kaftan_sheepskin_1,itm_kaftan_sheepskin_2,itm_kaftan_tunic_1,itm_kaftan_tunic_2,itm_linen_shirt_22,itm_shirt,itm_linen_tunic,itm_skirmisher_tunic_2,itm_bandana1,itm_bandana2,itm_woolen_cap_simple_4,itm_sarranid_two_handed_mace_1,itm_strong_bow,itm_yrzi_bow_1,itm_barbed_arrows,itm_barbed_arrows,itm_concave_shield_leather_small_1,itm_concave_shield_leather_small_2,itm_concave_shield_leather_small_3,itm_concave_shield_leather_small_1],
   def_attrib_lvl_18|level(17),wp_one_handed (160) | wp_two_handed (100) | wp_polearm (160) | wp_archery (180) | wp_crossbow (100) | wp_throwing (100) | wp_firearm(180),knows_ironflesh_3|knows_power_strike_4|knows_power_draw_7|knows_athletics_7,caucaus_face_1, caucaus_face_2], 

  ["armenian_brigand","Armenian Brigand","Armenian Brigands",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_armenian_rebels, 
   [itm_nomad_boots,itm_kaftan_sheepskin_1,itm_kaftan_sheepskin_2,itm_kaftan_tunic_1,itm_kaftan_tunic_2,itm_linen_shirt_22,itm_shirt,itm_linen_tunic,itm_skirmisher_tunic_2,itm_bandana1,itm_bandana2,itm_woolen_cap_simple_4,itm_sarranid_two_handed_mace_1,itm_light_lance,itm_strong_bow,itm_barbed_arrows,itm_barbed_arrows,itm_concave_shield_leather_small_1,itm_concave_shield_leather_small_2,itm_concave_shield_leather_small_3,itm_concave_shield_leather_small_1,itm_arabian_horse_a4,itm_normal_horse12,itm_normal_horse14,itm_normal_horse15,itm_normal_horse17],
   def_attrib_lvl_18|level(18),wp_one_handed (170) | wp_two_handed (100) | wp_polearm (170) | wp_archery (160) | wp_crossbow (100) | wp_throwing (160) | wp_firearm(100),knows_ironflesh_4|knows_power_strike_5|knows_power_draw_5|knows_athletics_3|knows_riding_5|knows_horse_archery_5,caucaus_face_1, caucaus_face_2], 

#Coptic Rebels
  ["coptic_youth","Coptic Youth (Masmatos)","Coptic Youth (Masmatoi)",tf_guarantee_basic|tf_guarantee_ranged,0,0,fac_coptic_rebels, #skirmisher
   [itm_wrapping_boots,itm_dark_bag_1,itm_dark_bag_2,itm_dark_bag_3,itm_roman_spear_1,itm_securis,itm_roman_arming_cap_1,itm_roman_arming_cap_2,itm_javelin,itm_javelin]+pannonian_hats+shields_simple+shoes_roman+tunics_coptic,
   def_attrib_skirmisher|level(13),wp_one_handed(130)|wp_two_handed(110)|wp_polearm(140)|wp_throwing(120)|wp_archery(100),knows_skirmisher,coptic_face_1, coptic_face_2],

  ["coptic_watchman","Coptic Watchman (Anurshe)","Coptic Watchmen (Anurshe)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_coptic_rebels, #archer
   [itm_ankle_boots,itm_wrapping_boots,itm_securis,itm_haditha_1,itm_roman_arming_cap_1,itm_roman_arming_cap_2,itm_strong_bow,itm_roman_arrows_2,itm_roman_arrows_2]+shoes_roman+tunics_coptic,
   def_attrib_lvl_18|level(17),wp_one_handed(150)|wp_two_handed(150)|wp_polearm(150)|wp_throwing(130)|wp_archery(150),knows_archer,coptic_face_1, coptic_face_2],

  ["coptic_footman","Coptic Footman (Matos)","Coptic Footman (Matoi)",tf_guarantee_basic,0,0,fac_coptic_rebels,
   [itm_coptic_subarmalis,itm_subarmalis_2,itm_short_roman_mail_1,itm_short_roman_mail_2,itm_short_roman_mail_3,itm_short_roman_mail_4,itm_ankle_boots,itm_wrapping_boots,itm_roman_spear_3,itm_roman_spear_4,itm_sword_khergit_3,itm_ridge_helm_c,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_haditha_1,itm_roman_arming_cap_1,itm_roman_arming_cap_2]+shields_coptic+shoes_roman+tunics_coptic,
   def_attrib_lvl_18|level(18),wp_one_handed(170)|wp_two_handed(150)|wp_polearm(180)|wp_throwing(160)|wp_archery(100),knows_lvl_18_inf|knows_shield_5|knows_power_strike_3,coptic_face_1, coptic_face_2],

  ["coptic_guard","Coptic Guard (Refteshma)","Coptic Guards (Refteshma)",tf_mounted|tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_coptic_rebels,
   [itm_coptic_scale_cuirass_1,itm_coptic_scale_cuirass_2,itm_coptic_scale_coif_1,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_iatrus_1,itm_intercisa_helmet_gilded_1,itm_haditha_1,itm_burgh_helmet_1,itm_koblenz_helmet_1,itm_christies_helmet_1,itm_roman_spear_2_c1,itm_roman_spear_2_c2,itm_roman_spear_2_c3,itm_sword_khergit_3,itm_round_shield_roman_25]+shields_coptic+shoes_roman,
   def_attrib_lvl_23|level(23),wp_one_handed(200)|wp_two_handed(190)|wp_polearm(210)|wp_throwing(190)|wp_archery(100),knows_lvl_23_inf|knows_shield_7|knows_power_strike_4,coptic_face_1, coptic_face_2],

#arab bandits
  ["arab_bandit","Saraceni","Saraceni",tf_mounted|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_polearm,0,0,fac_outlaws,
   [itm_camel,itm_arabian_horse_a,itm_arabian_horse_b,itm_arabian_horse_c,itm_arabian_horse_d,itm_arabian_tunic_2,itm_arabian_tunic_3,itm_a_exomis_1,itm_beduin_armor_a,itm_turban,itm_desert_turban,itm_turban_white_1,itm_turban_white_2,itm_turban_black_1,itm_turban_black_2,itm_beduin_armor_b,itm_light_lance,itm_sassanid_axe_1],
   def_attrib_lvl_18|level(18),wp_one_handed(150)|wp_two_handed(90)|wp_polearm(170)|wp_throwing(150)|wp_archery(140),knows_lvl_18_cav|knows_shield_2|knows_power_strike_3,arab_face_1, arab_face_2],

#samaritan rebels
  ["samaritan_zealot","Samaritan Zealot","Samaritan Zealots",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_samaritan_rebels, #rebelled in 484, if I add judaism in the future, could rebel if player is ERE and has low relations with judaism
   [itm_mace_1,itm_flintlock_pistol,itm_cartridges,itm_cartridges,itm_wrapping_boots,itm_ankle_boots,itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_3,itm_linen_shirt,itm_shirt,itm_linen_shirt_16,itm_linen_shirt_17,itm_linen_shirt_18],
   def_attrib_lvl_13|level(13),wp_one_handed(110)|wp_polearm(100)|wp_firearm(150),knows_lvl_13_inf|knows_power_strike_4|knows_shield_2,coptic_face_1, coptic_face_2],

  ["samaritan_rebel","Samaritan Rebel","Samaritan Rebels",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_samaritan_rebels, #rebelled in 484, if I add judaism in the future, could rebel if player is ERE and has low relations with judaism
   [itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_3,itm_coat_of_plates_red,itm_warlord_coif_2,itm_late_roman_spear_2,itm_sword_khergit_4,itm_round_shield_roman_15,itm_concave_shield_red_1],
   def_attrib_lvl_20|level(20),wp_one_handed(200)|wp_polearm(200),knows_lvl_18_inf|knows_shield_6|knows_power_strike_6,coptic_face_1, coptic_face_2],

#gallaecian rebels
  ["gallaecian_rebel","Latro Gallaeci","Latrones Gallaeci",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_gallaecian_rebels,
   [itm_roman_spear_1,itm_dagger,itm_simancas_dagger_1,itm_simancas_dagger_2,itm_fighting_axe,itm_javelin,itm_javelin,itm_javelin,itm_roman_shirt_1,itm_roman_shirt_2,itm_roman_shirt_3,itm_roman_shirt_4,itm_roman_shirt_5,itm_roman_shirt_8,itm_roman_shirt_10,itm_linen_shirt_18,itm_linen_shirt_16,itm_linen_shirt_17,itm_linen_shirt_10,itm_linen_shirt_13,itm_woolen_cap_1,itm_woolen_cap_2,itm_woolen_cap,itm_woolen_cap_c,itm_new_hood_b,itm_brown_hood1] + pannonian_hats + shoes_roman,
   def_attrib_skirmisher|level(13),wp_one_handed(100)|wp_two_handed(60)|wp_polearm(110)|wp_throwing(140),knows_skirmisher,roman_face_1, roman_face_2],

  ["gallaecian_militia","Rusticius Gallaeci","Rustici Gallaeci",tf_guarantee_basic,0,0,fac_gallaecian_rebels,
   [itm_roman_spear_3,itm_securis,itm_dagger,itm_simancas_dagger_1,itm_simancas_dagger_2,itm_roman_military_tunic_1,itm_roman_military_tunic_2,itm_roman_military_tunic_3,itm_roman_military_tunic_4,itm_roman_military_tunic_5,itm_roman_military_tunic_6,itm_roman_shirt_1,itm_roman_shirt_4,itm_roman_shirt_10,itm_woolen_cap_1,itm_woolen_cap_2,itm_woolen_cap,itm_woolen_cap_c,itm_new_hood_b,itm_brown_hood1,itm_narona_bandhelm_cloth,itm_ridge_helm_c,(itm_intercisa_helmet_1,imod_battered),itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_concave_shield_blue_1,itm_concave_shield_red_1,itm_concave_shield_green_2,itm_concave_shield_red_2,itm_concave_shield_yellow_1,itm_concave_shield_white_1] + pannonian_hats + shoes_roman,
   def_attrib_lvl_18|level(18),wp_one_handed(160)|wp_two_handed(60)|wp_polearm(170)|wp_throwing(160),knows_lvl_18_inf|knows_shield_5|knows_power_strike_3,roman_face_1, roman_face_2],

  ["gallaecian_guard","Burgarius Gallaeci","Burgarii Gallaeci",tf_guarantee_basic|tf_guarantee_helmet,0,0,fac_gallaecian_rebels,
   [itm_late_roman_spear_1,itm_sword_khergit_3,itm_short_roman_mail_1,itm_short_roman_mail_2,itm_short_roman_mail_3,itm_short_roman_mail_4,itm_457_mail_short_1,itm_457_mail_short_2,itm_457_mail_short_3,itm_woolen_cap_1,itm_woolen_cap_2,itm_woolen_cap,itm_woolen_cap_c,itm_narona_bandhelm_mail,itm_narona_bandhelm_cloth,itm_ridge_helm_c,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_intercisa_helmet_2,itm_iatrus_1,itm_christies_helmet_1,itm_concave_shield_blue_1,itm_concave_shield_red_1,itm_concave_shield_green_2,itm_concave_shield_red_2,itm_concave_shield_yellow_1,itm_concave_shield_white_1,itm_concave_shield_roman_5,itm_concave_shield_roman_6] + pannonian_hats + shoes_roman,
   def_attrib_lvl_23|level(23),wp_one_handed(200)|wp_two_handed(60)|wp_polearm(225)|wp_throwing(160),knows_lvl_23_inf|knows_shield_8|knows_power_strike_6,roman_face_1, roman_face_2],

#latin bandit names
#sicarius/sicarii - muderer, assassin
#praedo/pradones - robber/theif
#latro/latrones - brigand/mercenary/highwayman
#scamara/scamarae - late latin "robber" may only be related to northern italy + noricum/raetia?

#bandits
  ["looter","Sicarius","Sicarii",tf_guarantee_armor,0,0,fac_outlaws, #primarily will use slings, staffs, hammers, etc
   [itm_roman_peasant_tunic_1,itm_roman_peasant_tunic_3,itm_roman_peasant_tunic_10,itm_wrapping_boots,itm_ankle_boots,itm_hammer,itm_staff,itm_flintlock_pistol,itm_cartridges,itm_cartridges] +hoods_roman_2+hoods_roman_3,
   def_attrib_lvl_13|level(12),wp_one_handed(120)|wp_two_handed(90)|wp_polearm(120)|wp_throwing(120)|wp_crossbow(80)|wp_archery(100)|wp_firearm(120),knows_lvl_13_inf|knows_shield_1|knows_power_strike_1,roman_face_1, roman_face_2],

  ["robber","Praedo","Praedones",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_roman_peasant_tunic_1,itm_roman_peasant_tunic_3,itm_roman_peasant_tunic_10,itm_shirt,itm_linen_tunic,itm_generic_tunic_13,itm_linen_shirt_22,itm_linen_shirt_10,itm_linen_shirt_13,itm_roman_spear_1,itm_winged_mace,itm_spiked_club,itm_hunting_bow,itm_arrows,itm_wrapping_boots,itm_simple_shoes,itm_head_wrappings,itm_simple_shield_1,itm_simple_shield_2,itm_simple_shield_3,itm_simple_shield_4]+hoods_roman_2+hoods_roman_3,
   def_attrib_lvl_18|level(16),wp_one_handed(150)|wp_two_handed(120)|wp_polearm(150)|wp_throwing(130)|wp_crossbow(80)|wp_archery(140)|wp_firearm(130),knows_lvl_18_inf|knows_shield_2|knows_power_draw_2|knows_power_strike_2,roman_face_1, roman_face_2],

  ["bandit","Latro","Latrones",tf_guarantee_basic,0,0,fac_outlaws,
   [itm_wrapping_boots,itm_simple_shoes,itm_roman_spear_2,itm_spiked_mace,itm_seax_9,itm_short_bow,itm_long_bow,itm_arrows,itm_brown_hood1,itm_new_hood_d,itm_leather_cap]+tunics_bandits+shields_basic,
   def_attrib_lvl_20|level(20),wp_one_handed(180)|wp_two_handed(140)|wp_polearm(180)|wp_throwing(130)|wp_crossbow(80)|wp_archery(155)|wp_firearm(130),knows_lvl_18_inf|knows_shield_3|knows_power_strike_3|knows_power_draw_3,roman_face_1, roman_face_2],

  ["brigand","Scamara","Scamarae",tf_guarantee_basic,0,0,fac_outlaws,
   [itm_wrapping_boots,itm_simple_shoes,(itm_cloaked_tunic_5,imod_ragged),(itm_cloaked_tunic_10,imod_ragged),(itm_cloaked_tunic_11,imod_ragged),(itm_cloaked_tunic_17,imod_ragged),(itm_intercisa_helmet_1,imod_battered),(itm_intercisa_helmet_2,imod_battered),(itm_augst_helmet_1,imod_battered),(itm_narona_bandhelm_cloth,imod_battered),itm_roman_spear_3,(itm_sword_medieval_a,imod_chipped),(itm_sword_medieval_a,imod_rusty),itm_javelin]+shields_bandit,
   def_attrib_lvl_23|level(23),wp_one_handed(200)|wp_two_handed(160)|wp_polearm(200)|wp_throwing(190)|wp_crossbow(80)|wp_archery(155)|wp_firearm(140),knows_lvl_23_inf|knows_shield_4|knows_power_strike_4,roman_face_1, roman_face_2],

  ["pirate","Pirata","Piratae",tf_guarantee_ranged,0,0,fac_outlaws,
   [itm_head_wrappings,itm_new_hood_e,itm_linen_tunic,itm_generic_tunic_13,itm_imperial_common_shirt,itm_wrapping_boots,itm_simple_shoes,itm_javelin,itm_javelin,itm_club,itm_fighting_axe,itm_round_shield_wood_small_1,itm_round_shield_wood_small_2,itm_round_shield_wood_small_3,itm_round_shield_leather_small_1,itm_round_shield_gray_small_1],
   def_attrib_lvl_13|level(12),wp_one_handed(130)|wp_polearm(110)|wp_throwing(140),knows_power_strike_3|knows_athletics_3|knows_power_throw_4|knows_ironflesh_1,roman_face_1, roman_face_2],

  #Changed to isaurian - blue + green colors, axemen armed with javelin
  ["mountain_bandit","Latro Isaurorum","Latrones Isauri",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_mountain_bandits,
   [itm_simple_shoes,itm_wrapping_boots,itm_ankle_boots,itm_linen_shirt_1,itm_linen_shirt_2,itm_linen_shirt_14,itm_generic_tunic_11,itm_roman_shirt_13,itm_skirmisher_tunic_1,itm_skirmisher_tunic_3,itm_leather_cap,itm_pannonian_cap_4,itm_pannonian_cap_5,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_javelin,itm_javelin,itm_fighting_axe,itm_simple_shield_1,itm_simple_shield_2,itm_simple_shield_3,itm_simple_shield_4],
   def_attrib_lvl_18|level(17),wp_one_handed(170)|wp_two_handed(160)|wp_polearm(150)|wp_throwing(160)|wp_archery(130),knows_lvl_18_inf|knows_athletics_6|knows_power_strike_5|knows_shield_3,roman_face_1, roman_face_2],

  ["isaurian_warrior","Bellator Isaurorum","Bellatores Isauri",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_mountain_bandits,
   [itm_simple_shoes,itm_wrapping_boots,itm_ankle_boots,itm_leather_gloves,itm_linen_shirt_1,itm_linen_shirt_2,itm_linen_shirt_14,itm_generic_tunic_11,itm_roman_shirt_13,itm_skirmisher_tunic_1,itm_skirmisher_tunic_3,itm_roman_military_tunic_4,itm_short_ragged_mail_2,itm_short_ragged_mail_3,itm_short_ragged_mail_4,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_haditha_1,itm_javelin,itm_javelin,itm_bearded_axe_2,itm_concave_shield_blue_1,itm_concave_shield_blue_2,itm_concave_shield_blue_3],
   def_attrib_lvl_23|level(22),wp_one_handed(200)|wp_two_handed(200)|wp_polearm(190)|wp_throwing(200)|wp_archery(130),knows_lvl_23_inf|knows_athletics_6|knows_shield_4|knows_power_strike_6,roman_face_1, roman_face_2],

  ["isaurian_infantry","Miles Numeri Isaurorum","Milites Numeri Isauri",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_mountain_bandits,
   [itm_wrapping_boots,itm_khergit_leather_boots,itm_hunter_boots,itm_leather_gloves,itm_mid_generic_mail_20,itm_mid_generic_mail_16,itm_mid_generic_mail_15,itm_mid_generic_mail_14,itm_mid_generic_mail_11,itm_mid_roman_mail_1,itm_burgh_helmet_1,itm_christies_helmet_1,itm_intercisa_helmet_1,itm_augst_helmet_1,itm_iatrus_1,itm_haditha_1,itm_narona_bandhelm_mail,itm_narona_bandhelm,itm_jarid,itm_jarid,itm_battle_axe,itm_round_shield_roman_22]+shoes_roman,
   def_attrib_lvl_28|level(28),wp_one_handed(250)|wp_two_handed(250)|wp_polearm(230)|wp_throwing(230)|wp_archery(180),knows_lvl_23_inf|knows_athletics_7|knows_shield_5|knows_power_strike_8,roman_face_1, roman_face_2],

  #bow, arrows, hatchet
  ["forest_bandit_recruit","Praedo Bagauda","Praedones Bagaudae",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_forest_bandits,
   [itm_ankle_boots,itm_wrapping_boots,itm_skirmisher_tunic_3,itm_generic_tunic_6,itm_generic_tunic_13,itm_generic_tunic_14,itm_roman_shirt_8,itm_roman_shirt_13,itm_leather_cap,itm_brown_hood1,itm_new_hood_b,itm_new_hood_d,itm_hunting_bow,itm_short_bow,itm_strong_bow,itm_roman_arrows_1,itm_roman_arrows_1,itm_basic_axe,itm_club]+shoes_roman+pannonian_hats,
   def_attrib_lvl_13|level(13),wp_one_handed(115)|wp_two_handed(110)|wp_polearm(110)|wp_throwing(110)|wp_archery(145),knows_lvl_13_inf|knows_power_draw_3|knows_power_strike_2|knows_shield_2,roman_face_1, roman_face_2],
  #bow, arrows, javelins (not guaranteed), axe, shield
  ["forest_bandit","Latro Bagauda","Latrones Bagaudae",tf_guarantee_basic,0,0,fac_forest_bandits,
   [itm_ankle_boots,itm_wrapping_boots,itm_generic_tunic_13,itm_generic_tunic_14,itm_roman_shirt_4,itm_roman_shirt_8,itm_roman_shirt_13,itm_roman_military_tunic_3,itm_roman_military_tunic_5,itm_roman_military_tunic_7,(itm_subarmalis_2,imod_ragged),(itm_subarmalis_4,imod_ragged),(itm_intercisa_helmet_1,imod_battered),(itm_intercisa_helmet_2,imod_battered),itm_iatrus_helmet_light,itm_roman_spear_3,itm_securis,itm_short_bow,itm_roman_arrows_2,itm_round_shield_roman_1,itm_round_shield_roman_19,itm_round_shield_green_2,itm_round_shield_gray_1]+shoes_roman+pannonian_hats,
   def_attrib_lvl_18|level(17),wp_one_handed(170)|wp_two_handed(160)|wp_polearm(170)|wp_throwing(160)|wp_archery(130),knows_lvl_18_inf|knows_power_draw_3|knows_power_strike_3|knows_shield_3,roman_face_1, roman_face_2],
  #spatha, spear, oval shield / roman shield
  ["bagaudae_footman","Pedes Bagauda","Pedites Bagaudae",tf_guarantee_basic,0,0,fac_forest_bandits,
   [itm_ankle_boots,itm_wrapping_boots,itm_subarmalis_2,itm_subarmalis_4,itm_short_ragged_mail_1,itm_short_ragged_mail_6,itm_short_roman_mail_2,itm_mid_roman_mail_3,itm_intercisa_helmet_1,itm_intercisa_helmet_2,itm_augst_helmet_1,itm_iatrus_1,itm_iatrus_helmet_mail,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_concave_shield_roman_2,itm_concave_shield_roman_5,itm_concave_shield_roman_6,itm_oval_shield_limitanei_1,itm_oval_shield_wood_2,itm_oval_shield_green_2,itm_oval_shield_yellow_2,(itm_sword_khergit_3,imod_chipped),itm_late_roman_spear_1,itm_spiculum]+shoes_roman,
   def_attrib_lvl_20|level(20),wp_one_handed(200)|wp_two_handed(190)|wp_polearm(190)|wp_throwing(190)|wp_archery(130),knows_lvl_18_inf|knows_power_strike_5|knows_shield_4,roman_face_1, roman_face_2],

  ["sea_raider","Saxon Warrior (Duguthi)","Saxon Warriors (Duguthi)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_wrapping_boots,itm_hunter_boots,itm_carbatinae_1_red,itm_carbatinae_2_red,itm_generic_tunic_4,itm_cloaked_generic_tunic_4,itm_linen_shirt_21,itm_cloaked_tunic_16,itm_leather_armor_c,itm_leather_armor_d,itm_leather_armor_e,itm_short_ragged_mail_5,itm_mid_generic_mail_1,itm_mid_generic_mail_3,itm_mid_generic_mail_21,itm_burgh_helmet_light,itm_burgh_helmet_mail,itm_burgh_helmet_1,itm_drengsted_helmet_leather,itm_drengsted_helmet_mail,itm_triveres_leather,itm_triveres_mail,itm_woolen_cap_c,itm_woolen_cap_1,itm_woolen_cap_2,itm_angon_1,itm_boar_spear,itm_sword_medieval_a,itm_round_shield_germanic_5,itm_round_shield_germanic_11,itm_concave_shield_germanic_11,itm_round_shield_yellow_1,itm_round_shield_blue_2,itm_round_shield_red_2],
   def_attrib_lvl_23|level(23),wp_one_handed(230)|wp_two_handed(215)|wp_polearm(200)|wp_throwing(200),knows_ironflesh_8|knows_shield_4|knows_power_strike_7|knows_power_throw_6|knows_riding_2|knows_athletics_7,germanic_face_1, germanic_face_2],

  #Iazyg Fat Aexsdzhytae
  ["steppe_bandit","Iazyg Vagabond (Fat Aexsdzhytae)","Iazyg Vagabonds (Fat Aexsdzhytaes)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_mounted,0,0,fac_outlaws,
   [itm_leather_steppe_cap_a,itm_nomad_cap_b,itm_simple_shoes,itm_wrapping_boots,itm_nomad_boots,itm_steppe_horse,itm_saddle_horse_6,itm_rich_tunic_5,itm_rich_tunic_6,itm_generic_tunic_6,itm_linen_shirt_8,itm_linen_shirt_13,itm_roman_spear_3,itm_hand_axe,itm_strong_bow,itm_roman_arrows_2,itm_roman_arrows_2],
   def_attrib_lvl_13|level(14),wp_one_handed(100)|wp_two_handed(80)|wp_polearm(130)|wp_throwing(130)|wp_archery(170),knows_riding_4|knows_horse_archery_4|knows_power_draw_3|knows_ironflesh_1,sarmatian_face_1, sarmatian_face_2],
  #Iazyg Baexdzhyntae
  ["steppe_rider","Iazyg Rider (Baexdzhyntae)","Iazyg Riders (Baexdzhyntaes)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_polearm|tf_mounted,0,0,fac_outlaws,
   [itm_simple_shoes,itm_wrapping_boots,itm_nomad_boots,itm_steppe_horse,itm_saddle_horse_6,itm_rich_tunic_5,itm_rich_tunic_6,itm_generic_tunic_6,itm_linen_shirt_8,itm_linen_shirt_13,itm_old_spangenhelm_1,itm_old_spangenhelm_2,itm_roman_spear_3,itm_roman_spear_4,itm_lance,itm_fighting_axe,itm_fighting_axe,itm_battle_axe_3,itm_throwing_spears,itm_throwing_spears,itm_concave_shield_leather_small_1,itm_concave_shield_leather_small_2,itm_concave_shield_leather_small_3],
   def_attrib_lvl_20|level(20),wp_one_handed(170)|wp_two_handed(140)|wp_polearm(180)|wp_throwing(170)|wp_archery(170),knows_riding_5|knows_horse_archery_5|knows_power_draw_4|knows_ironflesh_4|knows_power_strike_2|knows_power_throw_3,sarmatian_face_1, sarmatian_face_2],
  #Iazyg Uaezdaettae
  ["steppe_cataphract","Iazyg Cataphract (Uaezdaettae)","Iazyg Cataphracts (Uaezdaettaes)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_polearm|tf_mounted,0,0,fac_outlaws,
   [itm_nomad_boots,itm_splinted_greaves,itm_ankle_greaves,itm_old_spangenhelm_3,itm_gultlingen_helmet_plume,itm_intercisa_helmet_1,itm_iatrus_1,itm_augst_helmet_1,itm_christies_helmet_1,itm_medium_scale_1,itm_medium_scale_2,itm_long_lance,itm_khergit_bow,itm_niya_bow_2,itm_khergit_arrows,itm_sword_khergit_2,itm_half_cataphract_horse_3,itm_half_cataphract_horse_5,itm_half_cataphract_horse_7],
   def_attrib_lvl_25|level(25),wp_one_handed(240)|wp_two_handed(190)|wp_polearm(250)|wp_throwing(220)|wp_archery(180),knows_riding_7|knows_horse_archery_5|knows_power_draw_5|knows_ironflesh_6|knows_power_strike_4,sarmatian_face_1, sarmatian_face_2],

  ["taiga_bandit","Germanic Brigand","Germanic Brigands",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_outlaws, #skirmishers
   [itm_wooden_javelin,itm_wooden_javelin,itm_throwing_spears,itm_throwing_spears,itm_fighting_axe,itm_club,itm_winged_mace]+shoes_generic+tunics_western_germanic+hats_german+germanic_caps+shields_simple,
   def_attrib_lvl_18|level(16),wp_one_handed(180)|wp_two_handed(160)|wp_polearm(170)|wp_archery(130)|wp_crossbow(100)|wp_throwing(180)|wp_firearm(100),knows_common|knows_power_throw_3|knows_power_strike_3|knows_ironflesh_3|knows_shield_2|knows_athletics_4,germanic_face_1, germanic_face_2],

  ["desert_bandit","Mauri Bandit","Mauri Bandits",tf_mounted|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_berber_rebels,
   [itm_berber_tunic_1,itm_berber_tunic_2,itm_berber_tunic_3,itm_berber_tunic_4,itm_wrapping_boots,itm_ankle_boots,itm_roman_spear_2,itm_securis,itm_cavalry_javelins,itm_imperial_saddle_horse_1,itm_imperial_saddle_horse_2]+shields_simple,
   def_attrib_lvl_13|level(12),wp(140),knows_riding_4|knows_horse_archery_3|knows_power_throw_4|knows_ironflesh_2,mauri_face_1, mauri_face_2],

  ["sabir_bandit","Sabir Bandit","Sabir Bandits",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_outlaws,
   [itm_nomad_boots,itm_sarranid_boots_b,itm_leather_vest,itm_kaftan_hunnic_red,itm_kaftan_hunnic_blue,itm_kaftan_hunnic_green,itm_kaftan_hunnic_white,itm_hunnic_kaftan_lamellar_2,itm_hunnic_phrygian_leather,itm_hunnic_phrygian_4,itm_hunnic_phrygian_5,itm_kalhkni_helmet_mail,itm_kalhkni_helmet_1,itm_kalhkni_helmet_2,itm_tarasovo_helmet_1,itm_suvorovsky_helmet_cloth,itm_suvorovsky_helmet_mail,itm_khergit_bow,itm_niya_bow_2,itm_khergit_arrows,itm_khergit_arrows,itm_battle_axe_2,itm_steppe_horse],
   def_attrib_lvl_18|level(18),wp_one_handed(155)|wp_two_handed(130)|wp_polearm(130)|wp_throwing(130)|wp_archery(185),knows_common|knows_riding_6|knows_horse_archery_7|knows_power_strike_2|knows_power_draw_6|knows_ironflesh_2,hunnic_face_1, hunnic_face_2],

  ["irish_raider","Scotos","Scoti",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_simple_shoes,itm_woolen_hose,itm_falkirk_tunic_1,itm_falkirk_tunic_2,itm_falkirk_tunic_3,itm_falkirk_tunic_4,itm_falkirk_tunic_5,itm_brown_hood1,itm_p_hood,itm_new_hood_b,itm_new_hood_c,itm_new_hood_d,itm_roman_spear_3,itm_pict_axe_a,itm_pict_axe_b,itm_jarid,itm_vae_pictish_rectangle_11,itm_vae_pictish_rectangle_12,itm_vae_pictish_rectangle_13,itm_vae_pictish_rectangle_14,itm_vae_pictish_rectangle_15,itm_vae_pictish_rectangle_16],
   def_attrib_lvl_20|level(21),wp(210),knows_ironflesh_5|knows_power_strike_7|knows_power_throw_8|knows_athletics_8|knows_shield_2,celtic_face_1, celtic_face_2],

#maybe will be used again???
  ["rich_bandit","Bandit Warrior","Bandit Warrior",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_war_spear,itm_sword_medieval_c_long,(itm_narona_bandhelm_mail,imod_battered),(itm_triveres_mail,imod_battered),(itm_ridge_helm_c,imod_battered),(itm_intercisa_helmet_1,imod_battered),(itm_short_ragged_mail_7,imod_battered),(itm_short_ragged_mail_8,imod_battered),(itm_mid_generic_mail_23,imod_battered),(itm_mid_generic_mail_26,imod_battered),itm_brigandine_red,itm_leather_gloves,itm_throwing_spears,]+shields_bandit+shoes_generic,
   def_attrib_lvl_23|level(23),wp_one_handed(210)|wp_two_handed(200)|wp_polearm(210)|wp_throwing(190),knows_common|knows_ironflesh_5|knows_power_strike_5|knows_shield_5|knows_power_throw_5,roman_face_1, roman_face_2],

  ["bandit_leader","Bandit Leader","Bandit Leaders",tf_hero|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_war_spear,itm_nomad_boots,itm_wrapping_boots,itm_ankle_boots,itm_sword_medieval_a,itm_war_spear,itm_javelin,itm_javelin,itm_javelin,itm_fighting_axe,(itm_short_ragged_mail_7,imod_battered),(itm_short_ragged_mail_8,imod_battered),(itm_mid_generic_mail_23,imod_battered),(itm_mid_generic_mail_26,imod_battered),itm_brigandine_red,itm_generic_subarmalis_8,itm_generic_subarmalis_9,itm_ridge_helm_c,(itm_intercisa_helmet_1,imod_battered)] + shields_bandit,
   def_attrib_lvl_23|level(25),wp(240),knows_common|knows_power_draw_2|knows_ironflesh_6|knows_power_strike_6|knows_shield_2,roman_face_1, roman_face_2],

  ["bandit_king","Bandit Warlord","Bandit Warlords",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_war_spear,itm_sword_viking_2,itm_heavy_greaves,itm_saddle_horse,itm_koblenz_helmet_light_old,itm_mid_generic_mail_17,itm_mid_generic_mail_23,itm_short_ragged_mail_6,itm_mid_generic_mail_19,itm_mid_generic_mail_15,itm_leather_gloves,itm_throwing_spears,itm_throwing_spears,itm_throwing_spears] + shields_bandit,
   def_attrib_lvl_28|level(28),wp(250),knows_common|knows_power_draw_2|knows_ironflesh_8|knows_power_strike_6|knows_shield_4|knows_power_throw_4,roman_face_1, roman_face_2],

   #hunnic guards - used at the end of the quest
  ["black_khergit_horseman","Hunnic Warrior","Hunnic Warriors",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_black_khergits,
   [],
   def_attrib_lvl_23|level(24),wpex(200,200,220,160,160,160),knows_riding_7|knows_ironflesh_6|knows_horse_archery_6|knows_power_draw_6|knows_power_strike_4,khergit_face_young_1, khergit_face_old_2],

  ["manhunter","Young Warrior","Young Warriors",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_manhunters,
   [itm_roman_spear_1,itm_club,itm_cudgel,itm_linen_tunic,itm_linen_shirt,itm_linen_shirt_14,itm_linen_shirt_10,itm_round_shield_wood_1,itm_round_shield_wood_2,itm_round_shield_wood_3,itm_round_shield_leather_1]+shoes_generic,
   def_attrib_lvl_13|level(13),wp_one_handed(130)|wp_two_handed(130)|wp_polearm(140)|wp_throwing(130),knows_lvl_13_inf|knows_shield_2|knows_power_strike_3,roman_face_1, roman_face_2],
  ["slave_driver","Veteran Warrior","Veteran Warriors",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_slavers,
   [itm_roman_spear_2,itm_winged_mace,itm_linen_tunic,itm_linen_shirt,itm_linen_shirt_14,itm_linen_shirt_10,itm_round_shield_leather_1,itm_round_shield_white_1]+shoes_generic,
   def_attrib_lvl_18|level(17),wp_one_handed(160)|wp_two_handed(160)|wp_polearm(170)|wp_throwing(160),knows_lvl_18_inf|knows_shield_3|knows_power_strike_4,roman_face_1, roman_face_2],
  ["slave_hunter","Slave Hunter","Slave Hunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_slavers,
   [itm_roman_spear_3,itm_winged_mace,itm_cloaked_tunic_5,itm_cloaked_tunic_10,itm_cloaked_tunic_11,itm_cloaked_tunic_17,itm_round_shield_white_1,itm_narona_bandhelm_cloth,itm_triveres_cloth,itm_ridge_helm_c]+shoes_generic,
   def_attrib_lvl_20|level(21),wp_one_handed(160)|wp_two_handed(160)|wp_polearm(170)|wp_throwing(160),knows_lvl_18_inf|knows_shield_4|knows_power_strike_5,roman_face_1, roman_face_2],
  ["slave_crusher","Slave Driver","Slave Drivers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_slavers,
   [itm_roman_spear_4,itm_mace_2,itm_generic_subarmalis_1,itm_generic_subarmalis_8,itm_narona_bandhelm_leather,itm_triveres_leather,itm_ridge_helm_c,itm_round_shield_white_1]+shoes_generic,
   def_attrib_lvl_23|level(25),wp_one_handed(190)|wp_two_handed(190)|wp_polearm(200)|wp_throwing(190),knows_lvl_23_inf|knows_shield_5|knows_power_strike_6,roman_face_1, roman_face_2],
  ["slaver_chief","Slaver Chief","Slaver Chiefs",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_slavers,
   [itm_late_roman_spear_2,itm_mace_roman_1,itm_mid_generic_mail_20,itm_mid_generic_mail_23,itm_mid_generic_mail_26,itm_brigandine_red,itm_ridge_helm_c,itm_koblenz_helmet_light_old,itm_triveres_mail,itm_narona_bandhelm_mail,itm_tab_shield_round_d]+shoes_generic,
   def_attrib_lvl_28|level(29),wp_one_handed(220)|wp_two_handed(210)|wp_polearm(220)|wp_throwing(210),knows_lvl_28_inf|knows_shield_6|knows_power_strike_7,roman_face_1, roman_face_2],

  ["follower_woman","Camp Woman","Camp Women",tf_female|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
   [itm_arrows,itm_arrows,itm_hunting_bow,itm_club,itm_wrapping_boots,itm_ankle_boots,itm_dress_5,itm_khergit_lady_dress_b,itm_sarranid_felt_hat,itm_felt_hat,itm_felt_hat_b,itm_turret_hat_blue],
   def_attrib_lvl_9|level(8),wp(90),knows_common|knows_athletics_1|knows_power_draw_1,refugee_face1,refugee_face2],

  ["hunter_woman","Camp Follower","Camp Followers",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
   [itm_arrows,itm_arrows,itm_short_bow,itm_spiked_club,itm_spear,itm_wrapping_boots,itm_ankle_boots,itm_dress_5,itm_khergit_lady_dress_b,itm_sarranid_felt_hat,itm_felt_hat,itm_felt_hat_b,itm_turret_hat_blue],
   def_attrib_lvl_13|level(11),wp(120),knows_common|knows_power_strike_1|knows_power_draw_2|knows_athletics_2|knows_ironflesh_1,refugee_face1,refugee_face2],

  ["fighter_woman","Soldier's Wife","Soldiers' Wives",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
   [itm_barbed_arrows,itm_barbed_arrows,itm_long_bow,itm_mace_1,itm_medium_spear_2,itm_wrapping_boots,itm_ankle_boots,itm_dress_5,itm_khergit_lady_dress_b,itm_sarranid_felt_hat,itm_felt_hat,itm_felt_hat_b,itm_turret_hat_blue],
   def_attrib_lvl_18|level(16),wp_one_handed(150)|wp_two_handed(130)|wp_polearm(150)|wp_archery(150),knows_common|knows_power_strike_2|knows_power_draw_3|knows_athletics_3|knows_ironflesh_2,refugee_face1,refugee_face2],

  ["sword_sister","Camp Defender","Camp Defenders",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
   [itm_barbed_arrows,itm_barbed_arrows,itm_war_bow,itm_mace_1,itm_war_spear,itm_wrapping_boots,itm_ankle_boots,itm_nomad_boots,itm_generic_subarmalis_1,itm_generic_subarmalis_2,itm_generic_subarmalis_5,itm_battle_axe_3,itm_leather_gloves],
   def_attrib_lvl_23|level(22),wp_one_handed(200)|wp_two_handed(150)|wp_polearm(200)|wp_archery(180),knows_common|knows_power_strike_3|knows_power_draw_5|knows_athletics_5|knows_ironflesh_4,refugee_face1,refugee_face2],

  ["refugee","Refugee","Refugees",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_pitch_fork_1,itm_pitch_fork_2,itm_club,itm_sickle,itm_wrapping_boots,itm_ankle_boots,itm_dress_5,itm_khergit_lady_dress_b,itm_sarranid_felt_hat,itm_felt_hat,itm_felt_hat_b,itm_turret_hat_blue],
   def_attrib|level(4),wp(70),knows_common,refugee_face1,refugee_face2],

  ["peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_pitch_fork_1,itm_pitch_fork_2,itm_club,itm_sickle,itm_wrapping_boots,itm_ankle_boots,itm_dress_5,itm_khergit_lady_dress_b,itm_sarranid_felt_hat,itm_felt_hat,itm_felt_hat_b,itm_turret_hat_blue],
   def_attrib|level(4),wp(70),knows_common,refugee_face1,refugee_face2],

  ["caravan_master","Caravan Master","Caravan Masters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_commoners,
   [itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_2,itm_roman_lorum_fasciari_3,itm_ankle_boots,itm_imperial_common_shirt,itm_linen_tunic,itm_linen_shirt,itm_brown_hood1,itm_new_hood_d,itm_arabian_sword_a]+horses_roman_1,
   def_attrib_lvl_18|level(18),wp(170),knows_common|knows_riding_5|knows_ironflesh_4|knows_power_strike_5,roman_face_1, roman_face_2],

  ["watchman","Watchman","Watchmen",tf_guarantee_basic,no_scene,reserved,fac_commoners,
   [itm_simple_shoes,itm_wrapping_boots,itm_ankle_boots,itm_leather_cap,itm_new_hood_d,itm_brown_hood1,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_roman_spear_2,itm_winged_mace,itm_round_shield_wood_1,itm_round_shield_wood_2,itm_round_shield_wood_3]+tunics_generic,
   def_attrib_lvl_13|level(13),wp(130),knows_lvl_13_inf|knows_shield_2|knows_power_strike_2,roman_face_1, roman_face_2],

  ["kidnapped_girl","Kidnapped Girl","Kidnapped Girls",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
   [itm_dress,itm_wrapping_boots],
   def_attrib|level(2),wp(50),knows_common|knows_riding_2,woman_face_1, woman_face_2],

#This troop is the troop marked as soldiers_end and town_walkers_begin
 ["town_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_brown_hood1] + tunics_civ + shoes_generic + woolen_caps + phyringian_caps,
   def_attrib|level(4),wp(60),knows_common,germanic_face_1, germanic_face_2],
 ["town_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [] + dresses + veils_1 + veils_2 + shoes_generic,
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["khergit_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_wrapping_boots,itm_sarranid_cloth_robe,itm_sarranid_cloth_robe_b,itm_khergit_vest_a,itm_khergit_vest_b,itm_khergit_vest_c,itm_khergit_vest_d,itm_nomad_boots,itm_simple_shoes,itm_chionite_hat_4,itm_chionite_hat_5,itm_fur_hat,itm_leather_steppe_cap_a,itm_nomad_cap_b] + tunics_hunnic,
   def_attrib|level(4),wp(60),knows_common,hunnic_face_1, hunnic_face_2],
 ["khergit_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["sarranid_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_nomad_boots,itm_wrapping_boots,itm_sarranid_cloth_robe,itm_sarranid_cloth_robe_b,itm_linen_shirt_13,itm_linen_shirt_14,itm_rich_tunic_6,itm_nomad_boots,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_woolen_cap_b,itm_woolen_cap_c,itm_woolen_cap_1,itm_woolen_cap_5,itm_linen_shirt_16,itm_linen_shirt_17,itm_linen_shirt_18,itm_linen_shirt_20,itm_linen_shirt_22,itm_shirt] + tunics_sassanid,
   def_attrib|level(4),wp(60),knows_common,persian_face_1, persian_face_2],
 ["sarranid_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_sarranid_common_dress,itm_sarranid_common_dress_b,itm_sarranid_dress_a,itm_nomad_boots,itm_wrapping_boots,itm_sarranid_felt_head_cloth,itm_sarranid_felt_head_cloth_b],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["imperial_town_walker_1","Civis","Civites",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_ankle_boots,itm_wrapping_boots,itm_dagger] + roman_tunics + pannonian_hats + shoes_roman,
   def_attrib|level(4),wp(60),knows_common,roman_face_1, roman_face_2],
 ["imperial_town_walker_2","Civis","Civites",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_ankle_boots,itm_wrapping_boots,itm_dress_7,itm_dress_8,itm_dress_5,itm_dress_4,itm_lady_dress_green] + veils_1,
   def_attrib|level(2),wp(40),knows_common,roman_woman_face_1,roman_woman_face_2],
 ["pict_town_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_ankle_boots,itm_wrapping_boots] + tunics_pictish + shoes_generic,
   def_attrib|level(4),wp(60),knows_common,man_face_1, man_face_old_2],
 ["pict_town_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_ankle_boots,itm_wrapping_boots,itm_dress_1,itm_dress_2,itm_dress_3,itm_dress_4],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["nubian_townsman","Townsman","Townsmen",tf_guarantee_armor,0,0,fac_commoners,
   [itm_nubian_sandals,itm_nomad_boots,itm_wrapping_boots] + tunics_nubians,
   def_attrib|level(8),wp_one_handed(90)|wp_two_handed(60)|wp_polearm(100)|wp_archery(110)|wp_firearm(110),knows_common,nubian_face_1, nubian_face_2],
 ["nubian_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [] + dresses + veils_1 + veils_2 + shoes_generic,
   def_attrib|level(2),wp(40),knows_common,african_woman_face_1,african_woman_face_2],
 ["caucasian_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_nomad_boots,itm_wrapping_boots,itm_linen_shirt_13,itm_linen_shirt_14,itm_rich_tunic_6,itm_nomad_boots,itm_sassanid_simple_boots_1,itm_sassanid_simple_boots_2,itm_sassanid_simple_boots_3,itm_woolen_cap_b,itm_woolen_cap_c,itm_woolen_cap_1,itm_woolen_cap_5,itm_linen_shirt_16,itm_linen_shirt_17,itm_linen_shirt_18,itm_linen_shirt_20,itm_linen_shirt_22,itm_shirt],
   def_attrib|level(4),wp(60),knows_common,caucaus_face_1, caucaus_face_2],
 ["caucasian_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_sarranid_common_dress,itm_sarranid_common_dress_b,itm_sarranid_dress_a,itm_nomad_boots,itm_wrapping_boots,itm_sarranid_felt_head_cloth,itm_sarranid_felt_head_cloth_b],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["mauri_town_walker_1","Townsman","Townsmen",tf_guarantee_armor,0,0,fac_commoners,
   [itm_ankle_boots,itm_wrapping_boots,itm_a_exomis_1,itm_a_exomis_2,itm_a_exomis_3,itm_berber_tunic_1,itm_berber_tunic_2,itm_berber_tunic_3,itm_berber_tunic_4,itm_berber_tunic_5,itm_imperial_common_shirt,itm_simple_tunic_5,itm_simple_tunic_10],
   def_attrib|level(4),wp(60),knows_common,mauri_face_1, mauri_face_2],
 ["mauri_town_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_ankle_boots,itm_wrapping_boots,] + dresses + veils_1 + veils_2 + shoes_generic,
   def_attrib|level(2),wp(40),knows_common,roman_woman_face_1,roman_woman_face_2],


#This troop is the troop marked as town_walkers_end and village_walkers_begin
 ["village_walker_1","Villager","Villagers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_brown_hood1] + tunics_civ + shoes_generic + woolen_caps + phyringian_caps,
   def_attrib|level(4),wp(60),knows_common,germanic_face_1, germanic_face_2],
 ["village_walker_2","Villager","Villagers",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [] + dresses + veils_1 + veils_2 + shoes_generic,
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],

#This troop is the troop marked as village_walkers_end and spy_walkers_begin
 ["spy_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_short_tunic,itm_leather_boots,itm_ankle_boots,itm_wrapping_boots, itm_linen_tunic,itm_woolen_cap,itm_new_hood_e,itm_imperial_common_shirt,itm_linen_shirt_1,itm_linen_shirt_2,itm_linen_shirt_3,itm_linen_shirt_4,itm_linen_shirt_5,itm_linen_shirt_6,itm_linen_shirt_7,itm_linen_shirt_8,itm_linen_shirt_9],
   def_attrib|level(4),wp(60),knows_common,man_face_1, man_face_old_2],
 ["spy_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_leather_boots,itm_ankle_boots,itm_wrapping_boots, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
# Ryan END

#This troop is the troop marked as spy_walkers_end
# Zendar
  ["tournament_master","Tournament Master","Tournament Master",tf_hero, scn_zendar_center|entry(1),reserved,  fac_commoners,[itm_nomad_armor,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["trainer","Trainer","Trainer",tf_hero, scn_zendar_center|entry(2),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x00000000000430c701ea98836781647f],
  ["Constable_Hareck","Constable Hareck","Constable Hareck",tf_hero, scn_zendar_center|entry(5),reserved,  fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x00000000000c41c001fb15234eb6dd3f],

# Ryan BEGIN
  ["Ramun_the_slave_trader","Ramun, the slave trader","Ramun, the slave trader",tf_hero, no_scene,reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x0000000fd5105592385281c55b8e44eb00000000001d9b220000000000000000],

  ["guide","Quick Jimmy","Quick Jimmy",tf_hero, no_scene,0,  fac_commoners,[itm_coarse_tunic,itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c318301f24e38a36e38e3],
# Ryan END

  ["Xerina","Bessas","Bessas",tf_hero, scn_the_happy_boar|entry(5),reserved,  fac_commoners,[itm_rich_mail_11,itm_wrapping_boots,itm_fernpass_helmet_2,itm_concave_shield_germanic_2,itm_battle_axe,itm_throwing_spear_3],def_attrib_lvl_32|level(32),wp_one_handed(320)|wp_two_handed(300)|wp_polearm(290)|wp_throwing(280)|wp_crossbow(150)|wp_archery(150)|wp_firearm(150),knows_power_strike_7|knows_ironflesh_7|knows_riding_2|knows_power_draw_2|knows_athletics_7|knows_shield_3,0x00000006d90000c758dc96b6dbcdbb1b00000000001eb6b80000000000000000], #germanic armed with axe, throwing spear, mail, helmet, shield
  ["Dranton","Laudaricus","Laudaricus",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,[itm_hunnic_kaftan_lamellar_3,itm_kalhkni_helmet_1,itm_khergit_leather_boots,itm_round_shield_roman_11,itm_khergit_arrows,itm_khergit_bow,itm_pannonhalma_spatha],def_attrib_lvl_32|level(32),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(280)|wp_throwing(200)|wp_crossbow(150)|wp_archery(200)|wp_firearm(150),knows_power_strike_6|knows_ironflesh_6|knows_riding_8|knows_power_draw_7|knows_athletics_6|knows_shield_3,0x000000087f00e3cd70db6db5cab1172a00000000001d36e80000000000000000], #hunnic armed with sword, shield, bow + arrow, lamellar, helmet
  ["Kradus","Pelagius","Pelagius",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[itm_roman_lorum_fasciari_5,itm_cuir_bouilli,itm_christies_helmet_1,itm_arabian_sword_b,itm_late_roman_spear_2,itm_round_shield_roman_24],def_attrib_lvl_32|level(32),wp_one_handed(300)|wp_two_handed(250)|wp_polearm(320)|wp_throwing(250)|wp_crossbow(150)|wp_archery(150)|wp_firearm(150),knows_power_strike_4|knows_ironflesh_8|knows_riding_5|knows_power_draw_4|knows_athletics_5|knows_shield_8,0x0000000d27009042518ab6469c912acd00000000001d36ea0000000000000000], #roman armed with spear, sword, shield, scale, helmet


#Tutorial
  ["tutorial_trainer","Training Ground Master","Training Ground Master",tf_hero, 0, 0, fac_commoners,[itm_robe,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["tutorial_student_1","{!}tutorial_student_1","{!}tutorial_student_1",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,(itm_intercisa_helmet_1,imod_battered)],
   def_attrib|level(2),wp(20),knows_common, germanic_face_1, germanic_face_2],
  ["tutorial_student_2","{!}tutorial_student_2","{!}tutorial_student_2",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,(itm_intercisa_helmet_1,imod_battered)],
   def_attrib|level(2),wp(20),knows_common, germanic_face_1, germanic_face_2],
  ["tutorial_student_3","{!}tutorial_student_3","{!}tutorial_student_3",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,(itm_intercisa_helmet_1,imod_battered)],
   def_attrib|level(2),wp(20),knows_common, germanic_face_1, germanic_face_2],
  ["tutorial_student_4","{!}tutorial_student_4","{!}tutorial_student_4",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,(itm_intercisa_helmet_1,imod_battered)],
   def_attrib|level(2),wp(20),knows_common, germanic_face_1, germanic_face_2],

#Sargoth
  #halkard, hardawk. lord_taucard lord_caupard. lord_paugard

#Salt mine
  ["Galeas","Galeas","Galeas",tf_hero, 0, reserved, fac_commoners,[itm_leather_jacket,itm_wrapping_boots],def_attrib|level(5),wp(20),knows_common,0x000000000004718201c073191a9bb10c],
#Dhorak keep

  ["farmer_from_bandit_village","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_linen_tunic,itm_coarse_tunic,itm_shirt,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(90),knows_common,man_face_1, man_face_2],

#Relgious troops
  ["roman_priest","Chalcedonian Priest","Chalcedonian Priests",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_roman_christians,
   [itm_wrapping_boots,itm_robes_church,itm_knife],
   def_attrib|level(8),wp(90),knows_common,roman_face_1, roman_face_2],

  ["arian_priest","Arian Priest","Arian Priests",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_arian_christians,
   [itm_wrapping_boots,itm_robes_church,itm_knife],
   def_attrib|level(8),wp(90),knows_common,germanic_face_1, germanic_face_2],

  ["coptic_priest","Miaphysite Priest","Miaphysite Priests",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_coptic_christians,
   [itm_wrapping_boots,itm_robes_church,itm_knife],
   def_attrib|level(8),wp(90),knows_common,roman_face_1, roman_face_2],

  ["pagan_priest","Pagan Priest","Pagan Priests",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_pagans,
   [itm_wrapping_boots,itm_robe,itm_sarranid_cloth_robe_b,itm_knife],
   def_attrib|level(8),wp(90),knows_common,germanic_face_1, germanic_face_2],

  ["zoroastrian_priest","Zoroastrian Mobad","Zoroastrian Mobads",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_zoroastrians,
   [itm_wrapping_boots,itm_kaftan_tunic_3,itm_knife],
   def_attrib|level(8),wp(90),knows_common,persian_face_1, persian_face_2],

  ["roman_pagan_priest","Greco-Roman Pagan Priest","Greco-Roman Pagan Priest",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_roman_pagans,
   [itm_wrapping_boots,itm_long_tunic_c,itm_sarranid_cloth_robe_c,itm_knife],
   def_attrib|level(8),wp(90),knows_common,persian_face_1, persian_face_2],

  ["monk","Monk","Monks",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners, #shared by all 3 christian religions
   [itm_wrapping_boots,itm_robe,itm_sarranid_cloth_robe_b,itm_knife,itm_wooden_stick],
   def_attrib|level(8),wp(90),knows_common,roman_face_1, roman_face_2],

  ["roman_abbot","Chalcedonian Abbot","Chalcedonian Abbots",tf_hero,scn_christian_monastery|entry(1),reserved,fac_roman_christians,
   [itm_wrapping_boots,itm_robes_church,itm_knife],
   def_attrib|level(8),wp(90),knows_common,roman_face_1, roman_face_2],

  ["arian_abbot","Arian Abbot","Arian Abbots",tf_hero,scn_arian_monastery|entry(1),reserved,fac_arian_christians,
   [itm_wrapping_boots,itm_robes_church,itm_knife],
   def_attrib|level(8),wp(90),knows_common,roman_face_1, roman_face_2],

  ["coptic_abbot","Miaphysite Abbot","Miaphysite Abbots",tf_hero,scn_christian_monastery_desert|entry(1),reserved,fac_coptic_christians,
   [itm_wrapping_boots,itm_robes_church,itm_knife],
   def_attrib|level(8),wp(90),knows_common,roman_face_1, roman_face_2],

  ["pagan_high_priest","Pagan High Priest","Pagan High Priests",tf_hero,scn_pagan_grove|entry(1),reserved,fac_pagans,
   [itm_wrapping_boots,itm_robe,itm_sarranid_cloth_robe_b,itm_knife],
   def_attrib|level(8),wp(90),knows_common,germanic_face_1, germanic_face_2],

  ["zoroastrian_high_priest","Zoroastrian Moabadan-Moabad","Zoroastrian Moabadan-Moabads",tf_hero,scn_fire_temple|entry(1),reserved,fac_zoroastrians,
   [itm_wrapping_boots,itm_kaftan_tunic_3,itm_knife],
   def_attrib|level(8),wp(90),knows_common,persian_face_1, persian_face_2],

  ["severinus","Severinus of Noricum","Severinus",tf_hero,scn_fortified_monastery|entry(1),reserved,fac_roman_christians, #St. Severinus of Noricum, would help the people of Noricum in a post roman world
   [itm_wrapping_boots,itm_robes_church],
   def_attrib|level(8),wp(90),knows_common,0x00000004eb00300e43196eb8aa712b1300000000001d36d30000000000000000],

  ["roman_pagan_villager_1","Roman Pagan","Roman Pagans",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_roman_pagans,
   [itm_wrapping_boots,itm_ankle_boots,itm_knife] + tunics_roman_civilian, 
   def_attrib|level(8),wp(90),knows_common,roman_face_1, roman_face_2],

  ["roman_pagan_villager_2","Roman Pagan","Roman Pagans",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_roman_pagans,
   [itm_ankle_boots,itm_wrapping_boots,itm_dress_7,itm_dress_8,itm_dress_5,itm_dress_4,itm_lady_dress_green] + veils_1,
   def_attrib|level(2),wp(40),knows_common,roman_woman_face_1,roman_woman_face_2],

  ["roman_pagan_high_priest","Greco-Roman Pagan Priest","Greco-Roman Pagan Priest",tf_hero,scn_roman_pagan_temple|entry(1),reserved,fac_roman_pagans,
   [itm_wrapping_boots,itm_sarranid_cloth_robe_c,itm_knife],
   def_attrib|level(8),wp(90),knows_common,roman_face_1, roman_face_2],

   #SB : semi-random arena training rewards
  ["trainer_1","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_1|entry(6),reserved,  fac_commoners,[itm_practice_sword,itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000d0d1030c74ae8d661b651c6840000000000000e220000000000000000],
  ["trainer_2","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_2|entry(6),reserved,  fac_commoners,[itm_arena_axe,itm_nomad_vest,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e5a04360428ec253846640b5d0000000000000ee80000000000000000],
  ["trainer_3","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_3|entry(6),reserved,  fac_commoners,[itm_practice_crossbow,itm_padded_leather,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e4a0445822ca1a11ab1e9eaea0000000000000f510000000000000000],
  ["trainer_4","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_4|entry(6),reserved,  fac_commoners,[itm_heavy_practice_sword,itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e600452c32ef8e5bb92cf1c970000000000000fc20000000000000000],
  ["trainer_5","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_5|entry(6),reserved,  fac_commoners,[itm_arena_lance,itm_leather_vest,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e77082000150049a34c42ec960000000000000e080000000000000000],

# Ransom brokers. added new unique faces for each ransom broker, each rough and mercenary like
  ["ransom_broker_1","Ransom_Broker","Ransom_Broker",tf_hero, 0, reserved, fac_commoners,[itm_mid_generic_mail_3,itm_ankle_boots,itm_seax_1],def_attrib_lvl_9|level(5),wp(20),knows_common,0x000000026e01718528d39139536db6db00000000001db6e90000000000000000],
  ["ransom_broker_2","Ransom_Broker","Ransom_Broker",tf_hero, 0, reserved, fac_commoners,[itm_mid_generic_mail_15,itm_wrapping_boots,itm_seax_2],def_attrib_lvl_9|level(5),wp(20),knows_common,0x000000026e01625124d3913953b1b6db00000000001db6eb0000000000000000], 
  ["ransom_broker_3","Ransom_Broker","Ransom_Broker",tf_hero, 0, reserved, fac_commoners,[itm_mid_generic_mail_20,itm_ankle_boots,itm_seax_9],def_attrib_lvl_9|level(5),wp(20),knows_common,0x000000026e01210f24d39136ec71b31b00000000001db6eb0000000000000000],
  ["ransom_broker_4","Ransom_Broker","Ransom_Broker",tf_hero, 0, reserved, fac_commoners,[itm_mid_generic_mail_24,itm_simple_shoes,itm_sword_medieval_a],def_attrib_lvl_9|level(5),wp(20),knows_common,0x000000026e01020828d36e56ec71b31b00000000001db6eb0000000000000000],
  ["ransom_broker_5","Ransom_Broker","Ransom_Broker",tf_hero, 0, reserved, fac_commoners,[itm_mid_generic_mail_11,itm_ankle_boots,itm_sword_viking_1],def_attrib_lvl_9|level(5),wp(20),knows_common,0x000000026e00f00726d36e56ec71b31b00000000001db6eb0000000000000000],
  ["ransom_broker_6","Ransom_Broker","Ransom_Broker",tf_hero, 0, reserved, fac_commoners,[itm_short_ragged_mail_9,itm_ankle_boots,itm_sword_medieval_a],def_attrib_lvl_9|level(5),wp(20),knows_common,0x000000025e00b5c544936e66ec6db31b00000000001db6eb0000000000000000],
  ["ransom_broker_7","Ransom_Broker","Ransom_Broker",tf_hero, 0, reserved, fac_commoners,[itm_short_ragged_mail_6,itm_wrapping_boots,itm_sword_medieval_c],def_attrib_lvl_9|level(5),wp(20),knows_common,0x000000026500540444936e44ec71baea00000000001db6eb0000000000000000],
  ["ransom_broker_8","Ransom_Broker","Ransom_Broker",tf_hero, 0, reserved, fac_commoners,[itm_generic_subarmalis_3,itm_ankle_boots,itm_long_seax_4],def_attrib_lvl_9|level(5),wp(20),knows_common,0x000000024600424444936db6e46d24db00000000001db6eb0000000000000000],
  ["ransom_broker_9","Ransom_Broker","Ransom_Broker",tf_hero, 0, reserved, fac_commoners,[itm_generic_subarmalis_7,itm_hide_boots,itm_long_seax_3],def_attrib_lvl_9|level(5),wp(20),knows_common,0x000000024600314436936db6e46d22db00000000001db6eb0000000000000000],
  ["ransom_broker_10","Ransom_Broker","Ransom_Broker",tf_hero, 0, reserved, fac_commoners,[itm_generic_subarmalis_9,itm_ankle_boots,itm_long_seax_5],def_attrib_lvl_9|level(5),wp(20),knows_common,0x000000024601430342936db6e46d22db00000000001db6a30000000000000000],

# Tavern traveler.
  ["tavern_traveler_1","Traveller","Traveller",tf_hero, 0, reserved, fac_commoners,[itm_linen_shirt_12,itm_wrapping_boots],def_attrib|level(5),wp(20),knows_common,0x00000009c900040436db6db6db6db6db00000000001db6db0000000000000000],
  ["tavern_traveler_2","Traveller","Traveller",tf_hero, 0, reserved, fac_commoners,[itm_linen_shirt_9,itm_ankle_boots],def_attrib|level(5),wp(20),knows_common,0x0000000afd00019326da6d34d36db2db00000000001db6d20000000000000000],
  ["tavern_traveler_3","Traveller","Traveller",tf_hero, 0, reserved, fac_commoners,[itm_leather_vest,itm_nomad_boots],def_attrib|level(5),wp(20),knows_common,0x00000008830083883ada6d389371b4db00000000001db6db0000000000000000],
  ["tavern_traveler_4","Traveller","Traveller",tf_hero, 0, reserved, fac_commoners,[itm_roman_shirt_6,itm_ankle_boots],def_attrib|level(5),wp(20),knows_common,0x000000043d00100244da71c6eb6db2db00000000001db6d20000000000000000],
  ["tavern_traveler_5","Traveller","Traveller",tf_hero, 0, reserved, fac_commoners,[itm_linen_shirt_10,itm_carbatinae_1],def_attrib|level(5),wp(20),knows_common,0x00000008830102413ada6d389371b4db00000000001db6db0000000000000000],
  ["tavern_traveler_6","Traveller","Traveller",tf_hero, 0, reserved, fac_commoners,[itm_linen_shirt_11,itm_carbatinae_1_grey],def_attrib|level(5),wp(20),knows_common,0x00000002ae01110a3ada69b69351b4db00000000001db6db0000000000000000],
  ["tavern_traveler_7","Traveller","Traveller",tf_hero, 0, reserved, fac_commoners,[itm_linen_shirt,itm_ankle_boots],def_attrib|level(5),wp(20),knows_common,0x000000077500040234db7727246db6db00000000001db6dd0000000000000000],
  ["tavern_traveler_8","Traveller","Traveller",tf_hero, 0, reserved, fac_commoners,[itm_linen_shirt_12,itm_wrapping_boots],def_attrib|level(5),wp(20),knows_common,0x00000006e200300342da7537246db6db00000000001d36dd0000000000000000],
  ["tavern_traveler_9","Traveller","Traveller",tf_hero, 0, reserved, fac_commoners,[itm_linen_shirt_13,itm_simple_shoes],def_attrib|level(5),wp(20),knows_common,0x00000006e20045c43adb6db6ddb2dcdb00000000001cb6db0000000000000000],
  ["tavern_traveler_10","Traveller","Traveller",tf_hero, 0, reserved, fac_commoners,[itm_linen_shirt_14,itm_simple_shoes],def_attrib|level(5),wp(20),knows_common,0x00000006e20050043adb6da523b2d6db00000000001cb6db0000000000000000],

# Tavern traveler.
  ["tavern_bookseller_1","Codex_Merchant","Codex_Merchant",tf_hero|tf_is_merchant, 0, reserved, fac_commoners,[itm_robe,itm_wrapping_boots,
               itm_book_tactics, itm_book_persuasion, itm_book_wound_treatment_reference, itm_book_leadership,
               itm_book_intelligence, itm_book_training_reference, itm_book_surgery_reference],def_attrib|level(5),wp(20),knows_common,0x0000000d730013c45edb6db6db6db6db00000000001db6d10000000000000000],
  ["tavern_bookseller_2","Codex_Merchant","Codex_Merchant",tf_hero|tf_is_merchant, 0, reserved, fac_commoners,[itm_linen_shirt,itm_ankle_boots,
               itm_book_wound_treatment_reference, itm_book_leadership, itm_book_intelligence, itm_book_trade,
               itm_book_engineering, itm_book_weapon_mastery],def_attrib|level(5),wp(20),knows_common,0x000000099900400346db95bae36da2db00000000001db6ab0000000000000000],

# Tavern minstrel.
  ["tavern_minstrel_1","Wandering Poet","Poet",tf_hero|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_linen_tunic, itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x00000006e200c00436db6d56db6da2db00000000001d369c0000000000000000], #lute
  ["tavern_minstrel_2","Wandering Poet","Poet",tf_hero|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_linen_shirt_1, itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x00000006e200318546db6d56db6da2db00000000001db6ab0000000000000000],  #early harp/lyre
  ["tavern_minstrel_3","Wandering Poet","Poet",tf_hero|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_linen_shirt_7, itm_wrapping_boots],def_attrib|level(5),wp(20),knows_common,0x0000000a3301100646db9556db6da2db00000000001db6ab0000000000000000], #lute/oud or rebab
  ["tavern_minstrel_4","Wandering Poet","Poet",tf_hero|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_linen_shirt_12, itm_wrapping_boots],def_attrib|level(5),wp(20),knows_common,0x000000004001030646db95bae36da2db00000000001db6ab0000000000000000], #No instrument or lyre
  ["tavern_minstrel_5","Wandering Poet","Poet",tf_hero|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_linen_shirt_21, itm_ankle_boots],def_attrib|level(5),wp(20),knows_common,0x000000021900000246db95bae36da2db00000000001db6ab0000000000000000], #Lute or Byzantine/Occitan lyra

  ["musican_male","Musican","Musican",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_short_tunic,itm_linen_tunic,itm_wrapping_boots,itm_ankle_boots],def_attrib|level(4),wp(60),knows_common,man_face_1, man_face_old_2],
  ["musican_female","Musican","Musican",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_wrapping_boots] + dresses + veils_1, def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
  ["musicans_end","Musican","Musican",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_short_tunic,itm_linen_tunic,itm_wrapping_boots,itm_ankle_boots],def_attrib|level(4),wp(60),knows_common,man_face_1, man_face_old_2],
#NPC system changes begin
#Companions
  ["kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  tf_hero, 0,reserved,  fac_kingdom_1,[],          lord_attrib,wp(220),knows_lord_1, 0x000000000010918a01f248377289467d],

  ["npc1","Bogdan","Bogdan",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_tunic_long_pants_11,itm_wrapping_boots,itm_seax_8,itm_hunting_bow,itm_germanic_arrows], #seax, bow, arrows
   str_9|agi_12|int_12|cha_8|level(8),wp_one_handed(120)|wp_two_handed(100)|wp_polearm(100)|wp_archery(130)|wp_crossbow(80)|wp_throwing(130)|wp_firearm(130),
   knows_weapon_master_4|knows_ironflesh_3|knows_power_strike_3|knows_pathfinding_4|knows_athletics_4|knows_tracking_4|knows_power_draw_3|knows_inventory_management_3|knows_power_throw_3|knows_horse_archery_2, #33 starting points
   0x00000004810074cb289b89a752ade6db00000000001e36ec0000000000000000],
  ["npc2","Narseh","Narseh", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_kaftan_tunic_3,itm_wrapping_boots,itm_staff], #staff
   str_6|agi_6|int_12|cha_12|level(3),wp_one_handed(90)|wp_two_handed(90)|wp_polearm(100)|wp_archery(90)|wp_crossbow(60)|wp_throwing(80)|wp_firearm(60),
   knows_trade_6|knows_weapon_master_2|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_2|knows_leadership_2|knows_power_draw_1|knows_power_throw_1|knows_riding_3|knows_inventory_management_4,
   0x00000008f71110c536dc6d351b65b69b00000000001db6db0000000000000000],
  ["npc3","Valentina","Valentina",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_dress_7,itm_wrapping_boots,itm_dagger], #dagger
   str_6|agi_9|int_11|cha_8|level(1),wp(70),
   knows_trade_3|knows_inventory_management_3|knows_wound_treatment_1|knows_trade_2|knows_first_aid_3|knows_surgery_1|knows_athletics_3|knows_riding_3,
   0x000000003f10500a2a5270931989b69c00000000001d53140000000000000000],
  ["npc4","Mastigas","Mastigas",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_berber_tunic_4,itm_ankle_boots,itm_roman_spear_1,itm_securis,itm_javelin], #javelins, spear, axe
   str_12|agi_12|int_9|cha_10|level(10),wp_one_handed(140)|wp_two_handed(120)|wp_polearm(140)|wp_archery(80)|wp_crossbow(60)|wp_throwing(130)|wp_firearm(60),
   knows_ironflesh_4|knows_shield_1|knows_weapon_master_3|knows_power_strike_3|knows_power_throw_3|knows_athletics_4|knows_riding_4|knows_first_aid_1|knows_inventory_management_2|knows_surgery_1|knows_tactics_2|knows_leadership_2|knows_horse_archery_2, #32
   0x00000000350940834735493ae391a8d300000000001dcd230000000000000000],
  ["npc5","Sunicas","Sunicas",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_khergit_1,itm_khergit_bow,itm_khergit_arrows,itm_sassanid_cavalry_boots_1,itm_kaftan_tunic_7,itm_hun_horse_1], #hunnic bow, arrows, spatha, horse - rather well off for being hated by everyone
   str_12|agi_15|int_10|cha_7|level(13),wp_one_handed(150)|wp_two_handed(130)|wp_polearm(150)|wp_archery(150)|wp_crossbow(60)|wp_throwing(60)|wp_firearm(60),
   knows_ironflesh_3|knows_power_throw_2|knows_athletics_4|knows_power_strike_4|knows_riding_5|knows_horse_archery_5|knows_power_draw_4|knows_leadership_2|knows_inventory_management_2|knows_tactics_1|knows_weapon_master_4, #36
   0x000000000908d3cc2cddaa355b712ada00000000001db6ad0000000000000000],
  ["npc6","Wadomar","Wadomar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_generic_tunic_12,itm_wrapping_boots,itm_sword_medieval_d_long,itm_round_shield_germanic_1], #starts with sword, shield
   str_12|agi_12|int_10|cha_8|level(8),wp_one_handed(150)|wp_two_handed(130)|wp_polearm(130)|wp_archery(60)|wp_crossbow(60)|wp_throwing(90)|wp_firearm(60),
   knows_weapon_master_4|knows_ironflesh_4|knows_power_throw_2|knows_athletics_4|knows_power_strike_3|knows_riding_3|knows_shield_3|knows_inventory_management_2|knows_athletics_4|knows_trainer_1|knows_leadership_1, #31
  0x000000024200414234db9236e491b4db00000000001db6e10000000000000000],
  ["npc7","Ingrid","Ingrid",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_skirmisher_tunic_3,itm_wrapping_boots,itm_hunting_bow,itm_arrows,itm_spear], #bow, arrows, spear
   str_8|agi_12|int_9|cha_6|level(2),wp_one_handed(90)|wp_two_handed(90)|wp_polearm(90)|wp_archery(110)|wp_crossbow(60)|wp_throwing(100)|wp_firearm(60),
   knows_weapon_master_3|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_2|knows_inventory_management_2|knows_tracking_2|knows_athletics_4|knows_power_draw_3|knows_power_strike_1|knows_riding_1, #24
   0x000000038600000628d28a988c2dc91b00000000001ed36c0000000000000000],
  ["npc8","Beorhtric","Beorhtric",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_peasant_man_7,itm_wrapping_boots,itm_basic_axe,itm_angon_1,itm_round_shield_germanic_11], #axe, angon, spear
   str_13|agi_10|int_9|cha_9|level(8),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(60)|wp_crossbow(60)|wp_throwing(130)|wp_firearm(60),
   knows_power_throw_4|knows_power_strike_4|knows_power_draw_2|knows_riding_3|knows_shield_3|knows_inventory_management_2|knows_weapon_master_3|knows_ironflesh_4|knows_athletics_3|knows_leadership_2|knows_tactics_1, #30
   0x00000006c60044894cd38948d18d2ada00000000001e36e90000000000000000],
  ["npc9","Thalassius","Thalassius",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_roman_shirt_3,itm_roman_lorum_fasciari_6,itm_sword_medieval_a,itm_roman_spear_2,itm_round_shield_roman_2], #sword, shield, spear
   str_12|agi_9|int_9|cha_9|level(6),wp_one_handed(130)|wp_two_handed(100)|wp_polearm(130)|wp_archery(60)|wp_crossbow(60)|wp_throwing(60)|wp_firearm(60),
   knows_weapon_master_3|knows_ironflesh_4|knows_power_throw_3|knows_athletics_3|knows_power_strike_2|knows_power_draw_1|knows_riding_3|knows_shield_4|knows_inventory_management_2|knows_leadership_1|knows_tactics_2, #28
   0x00000008d6006042375a69a8e36db4d300000000001db6d10000000000000000],
  ["npc10","Aistulf","Aistulf",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_wrapping_boots,itm_fighting_axe,itm_medium_spear_2,itm_round_shield_germanic_14,itm_linen_shirt_4], #axe, spear, shield
   str_12|agi_9|int_9|cha_12|level(9),wp_one_handed(130)|wp_two_handed(130)|wp_polearm(120)|wp_archery(60)|wp_crossbow(60)|wp_throwing(90)|wp_firearm(60),
   knows_power_throw_3|knows_athletics_3|knows_power_strike_4|knows_riding_2|knows_shield_2|knows_inventory_management_2|knows_weapon_master_3|knows_tactics_1|knows_leadership_3|knows_ironflesh_4|knows_trainer_2|knows_first_aid_2, #31
   0x0000000a05081384572c91c71c8d46cb00000000001e468a0000000000000000],
  ["npc11","Alodia","Alodia",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_dress_3,itm_seax_9,itm_wrapping_boots], #seax
   str_7|agi_9|int_12|cha_12|level(7),wp(70),
   knows_riding_3|knows_athletics_4|knows_power_throw_2|knows_power_strike_2|knows_trade_4|knows_weapon_master_3|knows_first_aid_2|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5|knows_prisoner_management_2, #32
   0x0000000a24041001685292daea6dc6dc00000000001d52ad0000000000000000],
  ["npc12","Artemios","Artemios",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_roman_military_tunic_3,itm_pannonian_cap_fur_2,itm_wrapping_boots,itm_staff,itm_dagger,itm_flintlock_pistol,itm_cartridges], #staff, dagger, sling
   str_6|agi_9|int_15|cha_7|level(4),wp_one_handed(80)|wp_two_handed(60)|wp_polearm(90)|wp_archery(60)|wp_crossbow(60)|wp_throwing(60)|wp_firearm(100),
   knows_riding_3|knows_athletics_3|knows_trade_3|knows_weapon_master_2|knows_inventory_management_3|knows_ironflesh_1|knows_power_strike_1|knows_power_throw_1|knows_surgery_5|knows_wound_treatment_5|knows_first_aid_5, #32
   0x00000007b200500e490ba62a9c71d76d00000000001db6640000000000000000],
  ["npc13","Eirpanome","Eirpanome",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_winged_mace,itm_hunting_bow,itm_roman_arrows_2,itm_simple_tunic_2,itm_ankle_boots], #bow + arrows, club
   str_12|agi_10|int_9|cha_11|level(9),wp_one_handed(130)|wp_two_handed(110)|wp_polearm(130)|wp_archery(150)|wp_crossbow(60)|wp_throwing(80)|wp_firearm(60),
   knows_weapon_master_3|knows_power_throw_3|knows_shield_1|knows_inventory_management_2|knows_riding_3|knows_leadership_1|knows_athletics_3|knows_ironflesh_4|knows_power_draw_4|knows_power_strike_4|knows_horse_archery_2|knows_tactics_1, #31
   0x00000007bf09610246db6d3c6471b4da00000000001d36e40000000000000000],
  ["npc14","Rufinius","Rufinius",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_roman_military_tunic_2,itm_roman_lorum_fasciari_3,itm_augst_helmet_crested_1,itm_sword_khergit_3,itm_darts,itm_concave_shield_roman_19], #sword, shield, helmet
   str_12|agi_9|int_15|cha_8|level(11),wp_one_handed(140)|wp_two_handed(120)|wp_polearm(130)|wp_archery(60)|wp_crossbow(60)|wp_throwing(120)|wp_firearm(60),
   knows_weapon_master_3|knows_ironflesh_4|knows_power_strike_3|knows_power_throw_4|knows_power_draw_1|knows_athletics_3|knows_riding_3|knows_shield_3|knows_inventory_management_2|knows_trainer_5|knows_tactics_5|knows_leadership_3, #39
   0x00000007ae00300644db6e571c6da8d300000000001db6eb0000000000000000],
  ["npc15","Marcus Lincinus Posca","Marcus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_roman_shirt_6,itm_wrapping_boots,itm_dagger,itm_flintlock_pistol,itm_cartridges], #dagger, sling
   str_9|agi_9|int_15|cha_8|level(7),wp_one_handed(100)|wp_two_handed(80)|wp_polearm(100)|wp_archery(90)|wp_crossbow(60)|wp_throwing(90)|wp_firearm(90),
   knows_weapon_master_3|knows_ironflesh_2|knows_power_throw_2|knows_athletics_3|knows_power_strike_2|knows_riding_2|knows_shield_2|knows_inventory_management_3|knows_tactics_4|knows_engineer_5|knows_trade_3|knows_tracking_1|knows_spotting_3, #35
   0x0000000f2e1020862b4c7123594eab5300000000001d55360000000000000000],
  ["npc16","Shapurdukhtak","Shapurdukhtak",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sarranid_cloth_robe_b,itm_nomad_boots,itm_knife,itm_throwing_knives], #knife, throwing daggers
   str_8|agi_12|int_8|cha_8|level(5),wp_one_handed(100)|wp_two_handed(140)|wp_polearm(140)|wp_archery(110)|wp_crossbow(60)|wp_throwing(100)|wp_firearm(80),
   knows_weapon_master_4|knows_athletics_4|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_2|knows_inventory_management_2|knows_power_throw_4|knows_power_strike_2|knows_riding_2, #26
   0x00000000240060071b6471795a7594dc00000000001dd32c0000000000000000],
  ["npc17","Alachis","Alachis",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_round_shield_germanic_12,itm_wrapping_boots,itm_medium_spear_3,itm_long_seax_2,itm_linen_shirt_3], #shield, seax, spear
   str_15|agi_9|int_9|cha_9|level(9),wp_one_handed(150)|wp_two_handed(150)|wp_polearm(150)|wp_archery(60)|wp_crossbow(60)|wp_throwing(60)|wp_firearm(60),
   knows_power_throw_3|knows_athletics_3|knows_riding_2|knows_shield_2|knows_inventory_management_2|knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_power_strike_5|knows_ironflesh_5|knows_trainer_2|knows_first_aid_2, #31
   0x00000004c008548a489a6dbb246dab1b00000000001db6f10000000000000000],
  ["npc18","Khaetag","Khaetag",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_skirmisher_tunic_3,itm_khergit_leather_boots,itm_light_lance,itm_arrows,itm_strong_bow,itm_steppe_horse], #horse, lance, bow + arrows
   str_12|agi_13|int_8|cha_8|level(8),wp_one_handed(100)|wp_two_handed(150)|wp_polearm(150)|wp_archery(160)|wp_crossbow(60)|wp_throwing(100)|wp_firearm(50),
   knows_weapon_master_4|knows_ironflesh_4|knows_power_throw_2|knows_athletics_3|knows_power_strike_3|knows_inventory_management_2|knows_riding_4|knows_horse_archery_4|knows_power_draw_3, #29
   0x000000001808024236db91b6db6dbb1200000000001d368a0000000000000000],
  ["npc19","Siestrzewit","Siestrzewit",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tunic_long_pants_6,itm_wrapping_boots,itm_steppe_horse,itm_hunnic_spatha,itm_suvorovsky_helmet_cloth], #sword, horse
   str_12|agi_12|int_9|cha_9|level(9),wp_one_handed(140)|wp_two_handed(120)|wp_polearm(130)|wp_archery(130)|wp_crossbow(60)|wp_throwing(130)|wp_firearm(60),
   knows_weapon_master_4|knows_power_strike_3|knows_riding_4|knows_shield_1|knows_inventory_management_2|knows_power_throw_3|knows_athletics_4|knows_ironflesh_3|knows_tracking_2|knows_spotting_2|knows_riding_3, #31
   0x00000000530003cb531c69486251b91b00000000001d36eb0000000000000000],
  #can be convinced to join player's party after 
  ["npc20","Ildico","Ildico",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_dress_4,itm_wrapping_boots], #warrior-like npc, fitting of her character in germanic legends
   str_15|agi_12|int_9|cha_9|level(12),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(120)|wp_crossbow(60)|wp_throwing(140)|wp_firearm(60),
   knows_weapon_master_4|knows_riding_4|knows_inventory_management_2|knows_ironflesh_5|knows_power_strike_5|knows_power_throw_3|knows_power_draw_2|knows_shield_3|knows_athletics_4|knows_wound_treatment_2, #34
   0x000000000e004006484a70036989a49c00000000001d53520000000000000000],

#NPC system changes end

#wp_one_handed(300)|wp_two_handed(250)|wp_polearm(230)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100)|wp_firearm(100)

#Was Anthemius
["kingdom_1_lord",  "Flavius Julius Valerius Majorianus Augustus",  "Majorianus",  tf_hero, 0,reserved,  fac_kingdom_1,[itm_nisean_cataphract_1, itm_cuirass_roman_emperor, itm_roman_emperor_tunic, itm_crown_1, itm_roman_emperor_boots, itm_roman_emperor_greaves, itm_tab_shield_small_round_c, itm_arabian_sword_d, itm_berk_helmet], knight_attrib_5,wp_one_handed(310)|wp_two_handed(250)|wp_polearm(300)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100)|wp_firearm(100),knight_skills_6|knows_trainer_8, 0x000000060e002045345251b69369b4db00000000001d36e20000000000000000],

["kingdom_2_lord",  "Flavius Valerius Leo Augustus",  "Leo Marcellus",  tf_hero, 0,reserved,  fac_kingdom_2,[itm_nisean_cataphract_1, itm_roman_squamata_emperor, itm_roman_emperor_tunic, itm_crown_1, itm_roman_emperor_boots, itm_roman_emperor_greaves,  itm_tab_shield_small_round_c, itm_arabian_sword_d, itm_berk_helmet], knight_attrib_5,wp_one_handed(300)|wp_two_handed(260)|wp_polearm(310)|wp_archery(140)|wp_crossbow(100)|wp_throwing(100)|wp_firearm(100),knight_skills_5|knows_trainer_5, 0x00000007ac005002325251c69b6db8da00000000001d36db0000000000000000],
#Theodoric II, was Euric
["kingdom_3_lord",  "Reiks Theodoric II",  "Theodoric II",  tf_hero, 0,reserved,  fac_kingdom_3,[itm_warhorse, itm_nobleman_outfit, itm_simple_shoes, itm_splinted_greaves, itm_arabian_armor_b, itm_sword_viking_3, itm_tab_shield_round_e, itm_berk_helmet],knight_attrib_5,wp_one_handed(300)|wp_two_handed(270)|wp_polearm(310)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100)|wp_firearm(100),knight_skills_4|knows_trainer_5,0x000000021d00414144db8a4a9b6db91a00000000001db6ea0000000000000000],
#was Theodemir
["kingdom_4_lord",  "Reiks Valamir",  "Valamir",  tf_hero, 0,reserved,  fac_kingdom_4,[itm_half_cataphract_horse_7, itm_nobleman_outfit, itm_ankle_boots, itm_roman_greaves_3, itm_arabian_armor_b, itm_sword_viking_3, itm_tab_shield_round_e, itm_gultlingen_helmet_plume],knight_attrib_5,wp_one_handed(310)|wp_two_handed(310)|wp_polearm(280)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100)|wp_firearm(100),knight_skills_6|knows_trainer_5,0x0000000a8000028542db894aa36db51c00000000001db6dc0000000000000000],

["kingdom_5_lord",  "Ardri Nechtan Morbet",  "Nechtan Morbet",  tf_hero, 0,reserved,  fac_kingdom_5,[itm_saddle_horse_2, itm_linen_shirt_1, itm_leather_boots, itm_splinted_leather_greaves, itm_arabian_armor_b,  itm_sword_viking_2, itm_tab_shield_small_round_c, itm_burgh_helmet_2],knight_attrib_5,wp_one_handed(290)|wp_two_handed(290)|wp_polearm(290)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100)|wp_firearm(100),knight_skills_4|knows_trainer_5,0x00000007c00022495cdcb128db6db6da00000000001d37150000000000000000],
#Was peroz
["kingdom_6_lord",  "Shahanshah Hormizd III",  "Hormizd III",  tf_hero, 0,reserved,  fac_kingdom_6,[itm_warhorse_sarranid,  itm_emperor_armor_c, itm_mail_boots_manica_2, itm_sassanid_helmet_shah, itm_crown_3,  itm_ingushetia_spatha, itm_tab_shield_small_round_c, itm_sarranid_decorated_boots, itm_sassanid_rich_tunic_4],knight_attrib_5,wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_archery(170)|wp_crossbow(100)|wp_throwing(100)|wp_firearm(100),knight_skills_5|knows_trainer_5,0x00000002f101010536db6db6da6db8db00000000001db6d10000000000000000],

["kingdom_7_lord",  "Rex Childeric",  "Childeric",  tf_hero, 0,reserved,  fac_kingdom_7,[itm_warhorse, itm_generic_tunic_5, itm_simple_shoes, itm_roman_greaves_3, itm_childeric_armor, itm_sword_khergit_4, itm_tab_shield_round_d, itm_gultlingen_helmet_plume],knight_attrib_5,wp_one_handed(310)|wp_two_handed(290)|wp_polearm(270)|wp_archery(150)|wp_crossbow(100)|wp_throwing(290)|wp_firearm(100),knight_skills_6|knows_trainer_5,0x000000030000138736da75369a6db6da00000000001d36c90000000000000000],
#Richimund was Remismund
["kingdom_8_lord",  "Rex Maldras",  "Maldras",  tf_hero, 0,reserved,  fac_kingdom_8,[itm_warhorse, itm_generic_tunic_7, itm_simple_shoes, itm_splinted_greaves, itm_arabian_armor_b,  itm_arabian_sword_a, itm_tab_shield_round_e, itm_gultlingen_helmet_plume],knight_attrib_5,wp_one_handed(300)|wp_two_handed(250)|wp_polearm(300)|wp_archery(100)|wp_crossbow(100)|wp_throwing(280)|wp_firearm(100),knight_skills_6|knows_trainer_5,0x00000008400043c3329b6936db6da8d200000000001e36e20000000000000000],

["kingdom_9_lord",  "Rex Gundioc",  "Gundioc",  tf_hero, 0,reserved,  fac_kingdom_9,[itm_warhorse, itm_generic_tunic_9, itm_simple_shoes, itm_ankle_greaves, itm_long_mail_new_2,  itm_sword_viking_3_small, itm_tab_shield_round_e, itm_gultlingen_helmet_plume],knight_attrib_5,wp_one_handed(290)|wp_two_handed(250)|wp_polearm(290)|wp_archery(140)|wp_crossbow(100)|wp_throwing(100)|wp_firearm(100),knight_skills_6|knows_trainer_5,0x000000078e0020c5589b7138e349a2db00000000001d36ea0000000000000000],

["kingdom_10_lord",  "Rex Gibuld",  "Gibuld",  tf_hero, 0,reserved,  fac_kingdom_10,[itm_warhorse, itm_generic_tunic_1, itm_wrapping_boots, itm_roman_greaves_4, itm_roman_squamata_5, itm_sword_viking_3, itm_tab_shield_round_e, itm_gultlingen_helmet_plume],knight_attrib_5,wp_one_handed(280)|wp_two_handed(280)|wp_polearm(280)|wp_archery(100)|wp_crossbow(100)|wp_throwing(200)|wp_firearm(100),knight_skills_5|knows_trainer_5,0x000000024e00014b589b7248db49a6db00000000001db6dc0000000000000000],

["kingdom_11_lord",  "Reiks Ardaric",  "Ardaric",  tf_hero, 0,reserved,  fac_kingdom_11,[itm_half_cataphract_horse_3, itm_tunic_long_pants_2, itm_simple_shoes, itm_splinted_greaves, itm_rich_squamata_3, itm_pannonhalma_spatha, itm_tab_shield_round_e, itm_kalhkni_helmet_1],knight_attrib_5,wp_one_handed(310)|wp_two_handed(310)|wp_polearm(260)|wp_archery(180)|wp_crossbow(100)|wp_throwing(180)|wp_firearm(100),knight_skills_5|knows_trainer_5,0x0000000b960063c9329c6ab4db69a6db00000000001db6e10000000000000000],

["kingdom_12_lord",  "Rex Aelle",  "Aelle",  tf_hero, 0,reserved,  fac_kingdom_12,[itm_warhorse, itm_generic_tunic_5, itm_simple_shoes, itm_splinted_greaves, itm_mid_generic_mail_3, itm_sword_viking_3, itm_tab_shield_round_e, itm_gultlingen_helmet_plume],knight_attrib_5,wp_one_handed(300)|wp_two_handed(300)|wp_polearm(270)|wp_archery(100)|wp_crossbow(100)|wp_throwing(280)|wp_firearm(100),knight_skills_6|knows_trainer_5,0x00000002cb003145329c6936db71a6db00000000001e36db0000000000000000],
#was riothamus
["kingdom_13_lord",  "Rex Ambrosius Aurelianus",  "Ambrosius Aurelianus",  tf_hero, 0,reserved,  fac_kingdom_13,[itm_half_cataphract_horse_2, itm_roman_shirt_3, itm_roman_lorum_fasciari_1, itm_roman_greaves_1, itm_arthur_scale, itm_tab_shield_small_round_c, itm_sword_viking_2, itm_deurne_helmet], knight_attrib_5,wp_one_handed(320)|wp_two_handed(230)|wp_polearm(270)|wp_archery(150)|wp_crossbow(100)|wp_throwing(250)|wp_firearm(100),knight_skills_6|knows_trainer_5, 0x000000071c00108744da5126a28db2db00000000001db6da0000000000000000],

["kingdom_14_lord",  "Reiks Flaccitheus",  "Flaccitheus",  tf_hero, 0,reserved,  fac_kingdom_14,[itm_half_cataphract_horse_4, itm_long_tunic_c, itm_ankle_boots, itm_roman_greaves_3, itm_arabian_armor_b, itm_tab_shield_small_round_c, itm_sword_viking_3_small, itm_gultlingen_helmet_plume], knight_attrib_5,wp_one_handed(300)|wp_two_handed(250)|wp_polearm(300)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100)|wp_firearm(100),knight_skills_4|knows_trainer_5, 0x0000000a9b00210b1adb69cacb6db8da00000000001e36e50000000000000000],

["kingdom_15_lord",  "Vandalirice Gaiseric",  "Gaiseric",  tf_hero, 0,reserved,  fac_kingdom_15,[itm_half_cataphract_horse_2, itm_roman_shirt_5, itm_simple_shoes, itm_splinted_greaves, itm_mamluke_mail, itm_beja_spatha, itm_tab_shield_small_round_c, itm_berk_helmet],knight_attrib_5,wp_one_handed(310)|wp_two_handed(280)|wp_polearm(270)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100)|wp_firearm(100),knight_skills_6|knows_trainer_5,0x0000000b0500a28548db6d48d375b8da00000000001db6e20000000000000000],

#changed 10/27/20 - very young, age probably around 19?
["kingdom_16_lord",  "Mepe Vakhtang",  "Vakhtang",  tf_hero, 0,reserved,  fac_kingdom_16,[itm_half_cataphract_horse_4,itm_linen_shirt_21,itm_sassanid_cavalry_boots_2,itm_heavy_greaves,itm_arabian_armor_b,itm_sassanid_cataphract_helmet_1,itm_ingushetia_spatha,itm_strong_bow,itm_barbed_arrows,itm_tab_shield_small_round_c], knight_attrib_5,wp_one_handed(300)|wp_two_handed(300)|wp_polearm(260)|wp_archery(190)|wp_crossbow(100)|wp_throwing(100)|wp_firearm(100),knight_skills_6|knows_trainer_6, 0x000000001e00710244da91b8e36db4db00000000001db6db0000000000000000],

["kingdom_17_lord",  "Rex Ildeoc Leting",  "Ildeoc Leting",  tf_hero, 0,reserved,  fac_kingdom_17,[itm_warhorse, itm_generic_tunic_5, itm_simple_shoes, itm_splinted_greaves, itm_arabian_armor_b,  itm_arabian_sword_a, itm_tab_shield_round_e, itm_gultlingen_helmet_feathers],knight_attrib_5,wp_one_handed(300)|wp_two_handed(280)|wp_polearm(300)|wp_archery(150)|wp_crossbow(100)|wp_throwing(300)|wp_firearm(100),knight_skills_6|knows_trainer_5,0x0000000c400005085adb6db8e391badb00000000001db6e40000000000000000],

["kingdom_18_lord",  "Rex Bisnius",  "Bisnius",  tf_hero, 0,reserved,  fac_kingdom_18,[itm_warhorse, itm_generic_tunic_2, itm_simple_shoes, itm_splinted_greaves, itm_coat_of_plates_red,  itm_sword_viking_c_long, itm_tab_shield_round_e, itm_concesti_helmet],knight_attrib_5,wp_one_handed(290)|wp_two_handed(290)|wp_polearm(300)|wp_archery(180)|wp_crossbow(100)|wp_throwing(300)|wp_firearm(100),knight_skills_6|knows_trainer_5,0x000000048400348b44db6db8e391b4da00000000001db6e40000000000000000],

["kingdom_19_lord",  "Rex Horsa",  "Horsa",  tf_hero, 0,reserved,  fac_kingdom_19,[itm_warhorse, itm_generic_tunic_1, itm_simple_shoes, itm_splinted_greaves, itm_long_mail_new_7,  itm_sword_viking_3_small, itm_tab_shield_round_e, itm_burgh_helmet_2],knight_attrib_5,wp_one_handed(310)|wp_two_handed(310)|wp_polearm(310)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100)|wp_firearm(100),knight_skills_6|knows_trainer_5,0x00000006450044c934db4d48eb71b8db00000000001db6ea0000000000000000],

["kingdom_20_lord",  "Regulus Sigobert",  "Sigobert",  tf_hero, 0,reserved,  fac_kingdom_20,[itm_warhorse, itm_yellow_tunic, itm_simple_shoes, itm_heavy_greaves, itm_medium_scale_2, itm_leather_gloves, itm_sword_viking_3_small, itm_tab_shield_round_d, itm_koblenz_helmet_2],knight_attrib_5,wp_one_handed(290)|wp_two_handed(270)|wp_polearm(290)|wp_archery(100)|wp_crossbow(100)|wp_throwing(290)|wp_firearm(100),knight_skills_6|knows_trainer_5,0x00000000470051c648db6d48db71b8db00000000001e36dc0000000000000000],

["kingdom_21_lord",  "Rex Edeko",  "Edeko",  tf_hero, 0,reserved,  fac_kingdom_21,[itm_warhorse, itm_generic_tunic_10, itm_simple_shoes, itm_splinted_greaves, itm_long_mail_new_4, itm_leather_gloves, itm_sword_viking_3_small, itm_tab_shield_round_d, itm_gultlingen_helmet_plume],knight_attrib_5,wp_one_handed(290)|wp_two_handed(290)|wp_polearm(290)|wp_archery(170)|wp_crossbow(100)|wp_throwing(200)|wp_firearm(100),knight_skills_6|knows_trainer_5,0x0000000b1c0061832a5b6656ec8db4db00000000001db6dc0000000000000000],

["kingdom_22_lord",  "Rex Masties",  "Masties",  tf_hero, 0,reserved,  fac_kingdom_22,[itm_half_cataphract_horse_2, itm_libyan_king_mail, itm_roman_shirt_13, itm_ankle_boots, itm_splinted_greaves, itm_tab_shield_small_round_c, itm_arabian_sword_d, itm_koblenz_crested_3], knight_attrib_5,wp_one_handed(300)|wp_two_handed(250)|wp_polearm(300)|wp_archery(100)|wp_crossbow(100)|wp_throwing(300)|wp_firearm(100),knight_skills_5|knows_trainer_5, 0x0000000cdc013002229b6db6d36db8db00000000001db6e20000000000000000],

["kingdom_23_lord",  "Dengizich",  "Dengizich",  tf_hero, 0,reserved,  fac_kingdom_23,[itm_warhorse_steppe,itm_kaftan_hunnic_2, itm_leather_boots,itm_heavy_greaves,itm_kaftan_lamellar_2,itm_pannonhalma_spatha,itm_mace_sassanid,itm_tab_shield_small_round_c,itm_kishpek_helmet_mail], knight_attrib_5,wp_one_handed(300)|wp_two_handed(300)|wp_polearm(280)|wp_archery(200)|wp_crossbow(100)|wp_throwing(200)|wp_firearm(100),knight_skills_5|knows_trainer_6, 0x000000002d00c3cb50db6a451351b6db00000000001db72a0000000000000000],

["kingdom_24_lord",  "Mepe Gubazes",  "Gubazes",  tf_hero, 0,reserved,  fac_kingdom_24,[itm_half_cataphract_horse_3,itm_long_tunic_a,itm_sassanid_cavalry_boots_2,itm_heavy_greaves,itm_coat_of_plates_red,itm_veiled_helmet_4,itm_battle_axe_4,itm_heavy_lance,itm_tab_shield_small_round_c], knight_attrib_5,wp_one_handed(300)|wp_two_handed(250)|wp_polearm(300)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100)|wp_firearm(100),knight_skills_5|knows_trainer_5, 0x0000000cc90090c21adb6db6db6dbadb00000000001db6da0000000000000000],

["kingdom_25_lord",  "Basiliskos Aburni",  "Aburni",  tf_hero, 0,reserved,  fac_kingdom_25,[itm_half_cataphract_horse_7,itm_long_tunic_a,itm_nomad_boots,itm_heavy_greaves,itm_coat_of_plates_red,itm_koblenz_helmet_3,itm_arabian_sword_a,itm_tab_shield_small_round_c], knight_attrib_5,wp_one_handed(290)|wp_two_handed(280)|wp_polearm(290)|wp_archery(190)|wp_crossbow(100)|wp_throwing(100)|wp_firearm(100),knight_skills_5|knows_trainer_5, 0x0000000b3f01608236db8a3a2b6db6db00000000001db6e20000000000000000],

["kingdom_26_lord",  "Basiliskos Phonen",  "Phonen",  tf_hero, 0,reserved,  fac_kingdom_26,[itm_half_cataphract_horse_7,itm_roman_shirt_10,itm_sassanid_simple_boots_2,itm_heavy_greaves,itm_457_scale_hauberk_5,itm_koblenz_helmet_3,itm_sword_khergit_4,itm_tab_shield_small_round_c], knight_attrib_5,wp_one_handed(290)|wp_two_handed(280)|wp_polearm(290)|wp_archery(190)|wp_crossbow(100)|wp_throwing(100)|wp_firearm(100),knight_skills_5|knows_trainer_5, 0x0000000b3f01600030db8a3a2b6db6da00000000001db7150000000000000000],

["kingdom_27_lord",  "Rex Kandak",  "Kandak",  tf_hero, 0,reserved,  fac_kingdom_27,[itm_half_cataphract_horse_6,itm_linen_shirt_13,itm_wrapping_boots,itm_heavy_greaves,itm_alan_cataphract_1,itm_kishpek_helmet_mail,itm_klin_yar_spatha,itm_tab_shield_small_round_c], knight_attrib_5,wp_one_handed(290)|wp_two_handed(300)|wp_polearm(290)|wp_archery(200)|wp_crossbow(100)|wp_throwing(250)|wp_firearm(100),knight_skills_5|knows_trainer_5, 0x00000007000063c244db6db6eb71b51b00000000001db6d50000000000000000],

#                                                                               Horse                   Bodywear                Armor                               Footwear_in                 Footwear_out                        Headwear                    Weapon               Shield

#Western Roman Empire Caecina Decius Basilius
#Nepotianus - married to marcellinus's sister, was father of Julius Nepos
#Aegidius - Syagrius
#Agrippinus - magister militum per gallias
#Caecina Decius Basilius
#Gennadius Avienus - consul
#Astyrius - general + consul
#Nomus - possible general
#Ecdicius - son of former emperor Avitus, served as magister milium in late empire, would be 37 at this time
#comes Burco - defeated alemanni invasion in 457, would be general
#Changed dux to be Comes Rei Militaris
["knight_1_1", "Magister Utriusque Militiae Flavius Ricimer", "Flavius Ricimer", tf_hero, 0, reserved,  fac_kingdom_1,[itm_half_cataphract_horse_2, itm_roman_shirt_12, itm_roman_lorum_fasciari_3, itm_roman_greaves_manica_2, itm_457_mail_long_2, itm_tab_shield_small_round_c, itm_arabian_sword_a, itm_gultlingen_helmet_feathers],knight_attrib_5,wp_one_handed(290)|wp_two_handed(270)|wp_polearm(290)|wp_archery(150)|wp_crossbow(100)|wp_throwing(100)|wp_firearm(100),knight_skills_5|knows_trainer_1|knows_trainer_3,0x00000005ca0001c823db6f59644426cc00000000001e26900000000000000000], #was 0x000000079000428236db6d1a9b6db2da00000000001d36b10000000000000000
#Was Bilimer
["knight_1_2", "Magister Militum per Gallia Aegidius", "Aegidius", tf_hero, 0, reserved,  fac_kingdom_1, [itm_nisean_cataphract_3, itm_roman_shirt_2, itm_roman_lorum_fasciari_1, itm_roman_greaves_manica_3,  itm_rich_squamata_1, itm_tab_shield_small_round_c, itm_sword_viking_3, itm_berk_helmet],       knight_attrib_5,wp_one_handed(300)|wp_two_handed(280)|wp_polearm(290)|wp_archery(140)|wp_crossbow(120)|wp_throwing(200)|wp_firearm(120),knight_skills_5, 0x0000000cac00100f4adb7138db6db4db00000000001db6db0000000000000000],
["knight_1_3", "Comes Rei Militaris Julius Nepos", "Julius Nepos", tf_hero, 0, reserved,  fac_kingdom_1, [itm_nisean_roman_1, itm_roman_shirt_9, itm_roman_lorum_fasciari_2, itm_roman_greaves_2,  itm_roman_squamata_4,itm_tab_shield_small_round_c, itm_sword_viking_c_long, itm_augsburg_2_helmet],  knight_attrib_5,wp_one_handed(270)|wp_two_handed(250)|wp_polearm(260)|wp_archery(140)|wp_crossbow(120)|wp_throwing(200)|wp_firearm(120),knight_skills_5|knows_trainer_3, 0x00000001bf0010841c99763ff982491000000000001ce2de0000000000000000],
#title was Magister Militum per Dalmatia
["knight_1_4", "Comes Illyricum Marcellinus", "Marcellinus", tf_hero, 0, reserved,  fac_kingdom_1, [itm_nisean_roman_2, itm_roman_shirt_2, itm_roman_lorum_fasciari_4, itm_roman_greaves_manica_4, itm_457_scale_hauberk_8, itm_tab_shield_small_round_c, itm_arabian_sword_a, itm_heteny_helmet_1], knight_attrib_5,wp_one_handed(300)|wp_two_handed(280)|wp_polearm(290)|wp_archery(140)|wp_crossbow(120)|wp_throwing(200)|wp_firearm(120),knight_skills_4|knows_trainer_6, 0x00000009eb006082289a71b6934db4db00000000001d36dc0000000000000000],
["knight_1_5", "Comes Rei Militaris Nepotianus", "Nepotianus", tf_hero, 0, reserved,  fac_kingdom_1, [itm_iberian_warhorse_roman_1, itm_roman_shirt_3, itm_roman_lorum_fasciari_1, itm_roman_greaves_3, itm_cuirass_roman_2, itm_tab_shield_small_round_c, itm_sword_viking_3, itm_berkasovo_2_helmet], knight_attrib_5,wp_one_handed(290)|wp_two_handed(270)|wp_polearm(280)|wp_archery(140)|wp_crossbow(120)|wp_throwing(200)|wp_firearm(120),knight_skills_4|knows_trainer_4, 0x000000082b007005289a71b6934db4db00000000001d36eb0000000000000000],
["knight_1_6", "Comes Rei Militaris Anicius Olybrius", "Anicius Olybrius", tf_hero, 0, reserved,  fac_kingdom_1, [itm_camargue_roman_1, itm_roman_shirt_4, itm_roman_lorum_fasciari_2, itm_roman_greaves_2, itm_457_mail_long_3, itm_tab_shield_small_round_c, itm_sword_viking_c_long, itm_augst_helmet_rich_2], knight_attrib_5,wp_one_handed(280)|wp_two_handed(270)|wp_polearm(280)|wp_archery(140)|wp_crossbow(120)|wp_throwing(200)|wp_firearm(120),knight_skills_4|knows_trainer_4, 0x000000001700204236dc76491b6db8db00000000001db6ed0000000000000000],
["knight_1_7", "Comes Rei Militaris Burco", "Burco", tf_hero, 0, reserved,  fac_kingdom_1, [itm_camargue_roman_3, itm_roman_shirt_5, itm_roman_lorum_fasciari_3, itm_roman_greaves_2, itm_roman_squamata_4, itm_tab_shield_small_round_c, itm_sword_viking_3_small, itm_intercisa_helmet_rich_3],  knight_attrib_5,wp_one_handed(290)|wp_two_handed(250)|wp_polearm(290)|wp_archery(170)|wp_crossbow(120)|wp_throwing(200)|wp_firearm(120),knight_skills_4, 0x00000005ea0030865adb89a4db4db6da00000000001d36e20000000000000000],
#added to the WRE instead as a lord over his former territory
["knight_1_8",  "Dux Arbogast",  "Arbogast",  tf_hero, 0,reserved,  fac_kingdom_1,[itm_westger_warhorse_1, itm_generic_tunic_2, itm_roman_lorum_fasciari_1, itm_roman_greaves_3, itm_roman_squamata_2, itm_leather_gloves, itm_sword_viking_3, itm_tab_shield_small_round_c, itm_gultlingen_helmet_plume],knight_attrib_5,wp_one_handed(300)|wp_two_handed(250)|wp_polearm(250)|wp_archery(150)|wp_crossbow(120)|wp_throwing(200)|wp_firearm(120),knight_skills_6|knows_trainer_5,0x000000078100024350db6d2aa36db51a00000000001db6db0000000000000000],
#was agrippinus - hunnic ally that helped majorian with campaign. will have hunnic HA's, retainers, etc with federate inf
["knight_1_12", "Comes Foederatorum Tuldila", "Tuldila", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hun_rich_horse_1, itm_roman_shirt_3, itm_wrapping_boots, itm_roman_greaves_2, itm_roman_lamellar_1, itm_tab_shield_small_round_c, itm_pannonhalma_spatha, itm_niya_bow_2, itm_khergit_arrows, itm_iatrus_2],    knight_attrib_5,wp_one_handed(290)|wp_two_handed(290)|wp_polearm(270)|wp_archery(190)|wp_crossbow(100)|wp_throwing(100)|wp_firearm(100),knight_skills_3|knows_trainer_6, 0x00000007e700b3cc57556db3696d26db00000000001db7290000000000000000],
#Now sun of aegidius
["knight_1_14",  "Dux Syagrius",  "Syagrius",  tf_hero, 0,reserved,  fac_kingdom_1,[itm_asturco_roman_3, itm_long_tunic_a, itm_roman_lorum_fasciari_4, itm_roman_greaves_3, itm_457_mail_short_1, itm_tab_shield_small_round_c, itm_sword_viking_3_small, itm_intercisa_helmet_gilded_plume_1], knight_attrib_5,wp_one_handed(270)|wp_two_handed(250)|wp_polearm(270)|wp_archery(140)|wp_crossbow(120)|wp_throwing(200)|wp_firearm(120),knight_skills_4|knows_trainer_5, 0x000000003800404524db6e46936db6da00000000001dc6ec0000000000000000],

#Eastern Roman Empire
#Anatolius - consul / magister militum
#Apollonius - magister militum of eastern empire
#Anthemius - magister militum of eastern roman empire
#Consantinus - consul in 457
#Rufus - also consul in 457
#anthemius will be given greece + surrounding area
["knight_2_1", "Magister Militum Praesentalis Procopius Anthemius", "Procopius Anthemius", tf_hero, 0, reserved,  fac_kingdom_2,[itm_nisean_cataphract_1, itm_roman_shirt_12, itm_roman_lorum_fasciari_4, itm_roman_greaves_manica_4, itm_cuirass_roman_1, itm_tab_shield_small_round_c, itm_arabian_sword_a, itm_deurne_helmet, itm_mace_roman_1],knight_attrib_5,wp_one_handed(310)|wp_two_handed(280)|wp_polearm(280)|wp_archery(140)|wp_crossbow(120)|wp_throwing(200)|wp_firearm(120),knight_skills_5|knows_trainer_3,0x00000004e600200646da95b6a371b6da00000000001db6dd0000000000000000],
#will be given ephesus, surrounding area
["knight_2_2", "Magister Militum Praesentalis Flavius Ardabur Aspar", "Flavius Ardabur Aspar", tf_hero, 0, reserved,  fac_kingdom_2, [itm_nisean_cataphract_2, itm_roman_shirt_9, itm_roman_lorum_fasciari_2, itm_roman_greaves_manica_3, itm_aspar_armor,  itm_tab_shield_small_round_c, itm_klin_yar_spatha, itm_gultlingen_helmet_plume],  knight_attrib_5,wp_one_handed(300)|wp_two_handed(300)|wp_polearm(280)|wp_archery(180)|wp_crossbow(120)|wp_throwing(220)|wp_firearm(120),knight_skills_5|knows_trainer_3, 0x0000000adc003182286b32db327658da00000000001ec7180000000000000000], #was 0x000000084f00028734db9538e36db4ea00000000001db6db0000000000000000
#Another son of Aspar (2_3)
#will be given antioch surrounding area
["knight_2_3", "Magister Militum per Orientem Ardabur", "Ardabur", tf_hero, 0, reserved,  fac_kingdom_2, [itm_nisean_roman_2, itm_roman_shirt_3, itm_roman_lorum_fasciari_1, itm_roman_greaves_1, itm_rich_squamata_2,  itm_tab_shield_small_round_c, itm_sword_viking_3, itm_concesti_helmet], knight_attrib_5,wp_one_handed(280)|wp_two_handed(280)|wp_polearm(270)|wp_archery(140)|wp_crossbow(120)|wp_throwing(200)|wp_firearm(120),knight_skills_4|knows_trainer_4, 0x000000008500124646db9538e36db4ea00000000001db6db0000000000000000],
#will be given alexandria, would later become magister militum per Orientem - changed to Nicolaus - https://de.zxc.wiki/wiki/Liste_der_Pr%C3%A4fekten_von_%C3%84gypten ???
["knight_2_4", "Comes Limitis Aegypti Nicolaus", "Nicolaus", tf_hero, 0, reserved,  fac_kingdom_2, [itm_iberian_warhorse_roman_2, itm_roman_shirt_4, itm_roman_lorum_fasciari_3, itm_roman_greaves_3, itm_roman_rigid_scale_4, itm_tab_shield_small_round_c, itm_sword_viking_3_small, itm_heteny_helmet_1],    knight_attrib_5,wp_one_handed(280)|wp_two_handed(250)|wp_polearm(280)|wp_archery(150)|wp_crossbow(120)|wp_throwing(200)|wp_firearm(120),knight_skills_5|knows_trainer_4, 0x0000000c8800908238db6dba5b6db8db00000000001db6db0000000000000000],
#Dux
["knight_2_5", "Comes Rei Militaris Flavius Armatus", "Flavius Armatus", tf_hero, 0, reserved,  fac_kingdom_2, [itm_camargue_roman_3, itm_roman_shirt_2, itm_roman_lorum_fasciari_1, itm_roman_greaves_3, itm_rich_squamata_1,  itm_tab_shield_small_round_c, itm_arabian_sword_a, itm_iatrus_plume_2], knight_attrib_5,wp_one_handed(270)|wp_two_handed(250)|wp_polearm(260)|wp_archery(140)|wp_crossbow(120)|wp_throwing(200)|wp_firearm(120),knight_skills_4|knows_trainer_6, 0x000000002200604538dc8a495b4db85a00000000001db6ed0000000000000000],
#Was Zeno, but in this period he went by his Isaurian name, was married to a woman named Arcadia, and later married Ariadne, daughter of Leo
["knight_2_7", "Comes Rei Militaris Tarasikodissa", "Tarasikodissa", tf_hero, 0, reserved,  fac_kingdom_2, [itm_asturco_roman_2, itm_roman_military_tunic_7, itm_roman_lorum_fasciari_2, itm_roman_greaves_2, itm_457_scale_hauberk_7, itm_mace_roman_2, itm_tab_shield_small_round_c, itm_augsburg_1_helmet], knight_attrib_5,wp_one_handed(280)|wp_two_handed(280)|wp_polearm(280)|wp_archery(170)|wp_crossbow(120)|wp_throwing(200)|wp_firearm(120),knight_skills_4|knows_trainer_4, 0x00000002bb00108124db6a569b6db4db00000000001db6e20000000000000000],
#control over eastern castles
["knight_2_8", "Comes Rei Militaris Heraclius of Edessa", "Heraclius of Edessa", tf_hero, 0, reserved,  fac_kingdom_2, [itm_iberian_warhorse_roman_1, itm_roman_shirt_5, itm_roman_lorum_fasciari_3, itm_roman_greaves_3, itm_roman_squamata_2,  itm_tab_shield_small_round_c, itm_sword_viking_3_small, itm_iatrus_2],  knight_attrib_5,wp_one_handed(280)|wp_two_handed(250)|wp_polearm(260)|wp_archery(130)|wp_crossbow(120)|wp_throwing(250)|wp_firearm(120),knight_skills_4, 0x00000003100030022adb6dc8da6db4da00000000001db6ea0000000000000000],
#Just starting career in the Roman Military at this point, was married to an Aelia Zeononis
["knight_2_10", "Comes Rei Militaris Flavius Basiliscus", "Flavius Basiliscus", tf_hero, 0, reserved,  fac_kingdom_2, [itm_nisean_roman_1, itm_roman_shirt_2, itm_roman_lorum_fasciari_4, itm_roman_greaves_1, itm_roman_squamata_4, itm_tab_shield_small_round_c, itm_sword_viking_3, itm_burgh_helmet_2],   knight_attrib_5,wp_one_handed(270)|wp_two_handed(240)|wp_polearm(280)|wp_archery(120)|wp_crossbow(120)|wp_throwing(230)|wp_firearm(120),knight_skills_3, 0x000000056c0081024adb6da6dc6db6db00000000001e36e40000000000000000],
#will be given control over moesia
["knight_2_11", "Comes Rei Militaris Theodoric Strabo", "Theodoric Strabo", tf_hero, 0, reserved,  fac_kingdom_2, [itm_iberian_warhorse_germanic_1, itm_roman_shirt_9, itm_roman_lorum_fasciari_2, itm_roman_greaves_2, itm_strabo_armor, itm_tab_shield_round_e, itm_sword_viking_c_long, itm_gultlingen_helmet_plume],knight_attrib_5,wp_one_handed(270)|wp_two_handed(270)|wp_polearm(270)|wp_archery(140)|wp_crossbow(120)|wp_throwing(200)|wp_firearm(120),knight_skills_3, 0x00000001c900424334da9136db6db4da00000000001db6e20000000000000000], #was 0x0000000bb90010014adb6dd4eb6db6db00000000001db6d50000000000000000
#Of gothic descent, son of Arnegisclus, killed by Attila in 447. Would end up killing Dengizich during his invasion of the ERE in 468
["knight_2_12", "Comes Rei Militaris Anagast", "Anagast", tf_hero, 0, reserved,  fac_kingdom_2, [itm_asturco_roman_1, itm_roman_shirt_2, itm_roman_lorum_fasciari_2, itm_roman_greaves_2, itm_457_mail_short_3, itm_tab_shield_small_round_c, itm_arabian_sword_a, itm_koblenz_helmet_3],   knight_attrib_5,wp_one_handed(300)|wp_two_handed(250)|wp_polearm(250)|wp_archery(100)|wp_crossbow(120)|wp_throwing(100)|wp_firearm(120),knight_skills_2, 0x00000004850053c226db6db6cb6db6d900000000001db6d80000000000000000],
#Visigoths
#new lords
#Suneric 
["knight_3_1", "Harjatuga Suneric", "Suneric", tf_hero, 0, reserved,  fac_kingdom_3,[itm_iberian_warhorse_germanic_2, itm_linen_shirt_1,itm_rich_mail_2,itm_ankle_boots,itm_gultlingen_helmet_plume,itm_sword_khergit_2,itm_tab_shield_small_round_c],knight_attrib_5,wp(270),knight_skills_5|knows_trainer_1|knows_trainer_3,0x00000008880053cf48db6db6cb6db6d900000000001d36e30000000000000000],
["knight_3_2", "Harjatuga Vultuulf", "Vultuulf", tf_hero, 0, reserved,  fac_kingdom_3, [itm_iberian_warhorse_germanic_1, itm_linen_shirt_2,itm_rich_squamata_3,itm_ankle_boots,itm_gultlingen_helmet,itm_sword_viking_2,itm_tab_shield_small_round_c],       knight_attrib_5,wp(280),knight_skills_5, 0x0000000fc500128236927656a36db4db00000000001db6db0000000000000000],
["knight_3_3", "Harjatuga Athaulf", "Athaulf", tf_hero, 0, reserved,  fac_kingdom_3, [itm_iberian_warhorse_germanic_1, itm_linen_shirt_3,itm_rich_mail_4,itm_wrapping_boots,itm_koblenz_helmet_2,itm_sword_viking_2,itm_tab_shield_small_round_c],  knight_attrib_5,wp(300),knight_skills_5|knows_trainer_3, 0x0000000d4500020336d27256a471b4db00000000001db6db0000000000000000],
#Unknown name? Mentioned by Hidatius as an indigenous noble under the visigoths
["knight_3_4", "Harjatuga Cantabrus", "Cantabrus", tf_hero, 0, reserved,  fac_kingdom_3, [itm_camargue_germanic_1, itm_linen_shirt_4,itm_mid_generic_mail_1,itm_wrapping_boots,itm_burgh_helmet_2,itm_sword_viking_3_small,itm_simancas_dagger_2,itm_tab_shield_round_c],    knight_attrib_5,wp(280),knight_skills_5|knows_trainer_4, 0x000000091700018438d26db6a371b8db00000000001db6db0000000000000000],
["knight_3_5", "Harjatuga Cyrila", "Cyrila", tf_hero, 0, reserved,  fac_kingdom_3, [itm_camargue_germanic_2, itm_linen_shirt_5,itm_mid_generic_mail_6,itm_wrapping_boots,itm_augsburg_1_helmet,itm_sword_viking_1,itm_tab_shield_round_d],      knight_attrib_5,wp(300),knight_skills_4|knows_trainer_6, 0x000000068c00204538d26db6a371b8db00000000001db6da0000000000000000],
["knight_3_6", "Harjatuga Alfbern", "Alfbern", tf_hero, 0, reserved,  fac_kingdom_3, [itm_camargue_germanic_3, itm_linen_shirt_6,itm_long_mail_new_6,itm_wrapping_boots,itm_intercisa_helmet_2,itm_sword_viking_2,itm_tab_shield_small_round_c], knight_attrib_5,wp(280),knight_skills_4|knows_trainer_4, 0x00000002c400124638d26db6a371b8db00000000001db6da0000000000000000],
["knight_3_7", "Harjatuga Waldhar", "Waldhar", tf_hero, 0, reserved,  fac_kingdom_3, [itm_asturco_germanic_1, itm_linen_shirt_7,itm_mid_generic_mail_1,itm_ankle_boots,itm_dux_ridge_helm,itm_sword_viking_2,itm_tab_shield_round_c], knight_attrib_5,wp(280),knight_skills_4|knows_trainer_4, 0x00000002cf00614546d26db6a371badb00000000001db6da0000000000000000],
["knight_3_8", "Harjatuga Harduwich", "Harduwich", tf_hero, 0, reserved,  fac_kingdom_3, [itm_asturco_germanic_2, itm_linen_shirt_8,itm_mid_generic_mail_2,itm_ankle_boots,itm_koblenz_helmet_1,itm_sword_viking_3_small,itm_tab_shield_small_round_c],  knight_attrib_5,wp(290),knight_skills_4, 0x000000008700118646d26db6a371bcdb00000000001db6da0000000000000000],

#Ostrogoths
["knight_4_1", "Harjatuga Theodemir", "Theodemir", tf_hero, 0, reserved,  fac_kingdom_4,[itm_iberian_warhorse_germanic_1, itm_generic_tunic_12,itm_rich_squamata_4,itm_ankle_boots,itm_gultlingen_helmet_plume,itm_sword_viking_1,itm_tab_shield_round_d],knight_attrib_5,wp(270),knight_skills_5|knows_trainer_1|knows_trainer_3,0x00000006ea00154258d24db66351b8d200000000001db6d40000000000000000],
["knight_4_2", "Harjatuga Widimir", "Widimir", tf_hero, 0, reserved,  fac_kingdom_4, [itm_iberian_warhorse_germanic_2, itm_linen_shirt_2,itm_rich_mail_3,itm_ankle_boots,itm_gultlingen_helmet_mail,itm_sword_viking_2,itm_tab_shield_round_d],       knight_attrib_5,wp(280),knight_skills_5, 0x00000008a910328636e455226634b92300000000001dc30b0000000000000000],
["knight_4_3", "Harjatuga Berimud", "Berimud", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hun_rich_horse_nobard_2, itm_linen_shirt_3,itm_mid_generic_mail_4,itm_wrapping_boots,itm_burgh_helmet_2,itm_sword_viking_2,itm_tab_shield_round_d],  knight_attrib_5,wp(300),knight_skills_5|knows_trainer_3, 0x00000001b90972c45a9d6928948638e300000000001153580000000000000000],
["knight_4_4", "Harjatuga Sidimund", "Sidimund", tf_hero, 0, reserved,  fac_kingdom_4, [itm_camargue_germanic_1, itm_linen_shirt_4,itm_mid_generic_mail_5,itm_wrapping_boots,itm_koblenz_helmet_1,itm_sword_viking_3_small,itm_tab_shield_round_c],    knight_attrib_5,wp(280),knight_skills_5|knows_trainer_4, 0x000000088a044050370c86271bee14a400000000001d25120000000000000000],
["knight_4_5", "Harjatuga Aidoingus", "Aidoingus", tf_hero, 0, reserved,  fac_kingdom_4, [itm_camargue_germanic_2, itm_linen_shirt_5,itm_mid_generic_mail_3,itm_wrapping_boots,itm_koblenz_helmet_1,itm_sword_viking_3_small,itm_tab_shield_round_d],      knight_attrib_5,wp(300),knight_skills_4|knows_trainer_6, 0x000000018a0054025ed4762aea8d176d00000000001f3b5c0000000000000000],
["knight_4_6", "Harjatuga Gento", "Gento", tf_hero, 0, reserved,  fac_kingdom_4, [itm_asturco_germanic_1, itm_linen_shirt_6,itm_mid_generic_mail_5,itm_wrapping_boots,itm_augst_helmet_1,itm_sword_viking_3,itm_tab_shield_small_round_c], knight_attrib_5,wp(280),knight_skills_4|knows_trainer_4, 0x000000019b0d758f355b7ac57392bd2d00000000000545190000000000000000],
["knight_4_7", "Harjatuga Dagistheus", "Dagistheus", tf_hero, 0, reserved,  fac_kingdom_4, [itm_asturco_germanic_2, itm_linen_shirt_7,itm_rich_mail_1,itm_ankle_boots,itm_intercisa_helmet_2,itm_sword_viking_3,itm_tab_shield_round_c], knight_attrib_5,wp(280),knight_skills_4|knows_trainer_4, 0x000000018700014739256e4b1caaaad800000000001e378c0000000000000000],
#would later be roman commander - as many others here would be!
["knight_4_8", "Harjatuga Ostryis", "Ostryis", tf_hero, 0, reserved,  fac_kingdom_4, [itm_asturco_germanic_3, itm_linen_shirt_8,itm_medium_scale_3,itm_ankle_boots,itm_iatrus_1,itm_sword_viking_3,itm_tab_shield_round_d],  knight_attrib_5,wp(290),knight_skills_4, 0x0000000187004144546d85e75553482500000000001e48e40000000000000000],
#Picts
["knight_5_1", "Mael Drest Gurthinmoch", "Drest Gurthinmoch", tf_hero, 0, reserved,  fac_kingdom_5, [ itm_long_sword_a, itm_burgh_helmet_2, itm_pictish_short_mail_1, itm_falkirk_tunic_1, itm_ankle_boots, itm_tab_shield_small_round_c],     knight_attrib_5,wp(300),knight_skills_1|knows_trainer_3, 0x0000000d4d04610f36db6db6db6db6db00000000001db6db0000000000000000],
["knight_5_2", "Mael Cathasach", "Cathasach", tf_hero, 0, reserved,  fac_kingdom_5, [ itm_long_sword_b, itm_augst_helmet_1, itm_pictish_short_mail_2, itm_falkirk_tunic_5, itm_ankle_boots, itm_tab_shield_small_round_c],     knight_attrib_5,wp(300),knight_skills_2|knows_trainer_4, 0x00000009930434c336db6db6db6db6db00000000001db6db0000000000000000],
["knight_5_3", "Mael Drustan", "Drustan", tf_hero, 0, reserved,  fac_kingdom_5,[  itm_long_sword_a, itm_ridge_helm_c, itm_pictish_short_mail_3, itm_linen_tunic, itm_ankle_boots, itm_tab_shield_small_round_c],knight_attrib_5,wp(280),knight_skills_3,0x000000000e0412c21adb6db6db6db6dd00000000001e36df0000000000000000],
#Sassanids
#father of knight_6_8
["knight_6_1", "Eran-Spahbed Mihr-Narseh", "Mihr-Narseh", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_horse_5, itm_cataphract_armor_1, itm_ingushetia_spatha, itm_mail_boots_manica_2, itm_mace_3, itm_tab_shield_small_round_c, itm_tsaritsyno_1_veiled, itm_sarranid_decorated_boots, itm_sassanid_rich_tunic_1],     knight_attrib_5,wp(300),knight_skills_3|knows_trainer_3, 0x0000000ae2010205230a9230db9528db00000000001db4d10000000000000000],
#father of knight_6_9 hypothetical, probably not actually historical
["knight_6_2", "Marzban Raham Mihran", "Raham Mihran", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_horse_5, itm_cataphract_armor_5, itm_ingushetia_spatha, itm_mail_boots_manica_2, itm_mace_3, itm_tab_shield_small_round_c, itm_sassanid_cataphract_helmet_1, itm_sarranid_decorated_boots, itm_sassanid_rich_tunic_2],     knight_attrib_5,wp(300),knight_skills_3|knows_trainer_4, 0x0000000ae2011343469271b4db9528db00000000001db4d30000000000000000],
#father of knight_6_10 hypothetical, probably not actually historical
["knight_6_3", "Marzban Izad Gushnasp", "Izad Gushnasp", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_horse_4, itm_cataphract_armor_4,itm_ingushetia_spatha, itm_mail_boots_manica_1, itm_mace_3, itm_tab_shield_small_round_c, itm_sassanid_cataphract_helmet_2, itm_sarranid_decorated_boots, itm_sassanid_rich_tunic_3],    knight_attrib_5,wp(260),knight_skills_3, 0x0000000e220114c4469271b4db9528db00000000001db4f50000000000000000],
#fought against armenians in rebellion, was wounded and sent back to iran
["knight_6_4", "Marzban Mushkan Niusalavurt", "Mushkan Niusalavurt", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_horse_4, itm_sassanid_heavy_mail_1, itm_ingushetia_spatha, itm_heavy_greaves, itm_mace_3, itm_tab_shield_small_round_c, itm_tsaritsyno_1_light, itm_sarranid_decorated_boots, itm_sassanid_rich_tunic_4],    knight_attrib_5,wp(260),knight_skills_4, 0x000000066200b44348926db8db6d28db00000000001db4bb0000000000000000],
#ruled over caucasian albania
["knight_6_5", "Marzban Vache II of Arran", "Marzban Vache II of Arran", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_horse_4, itm_long_cataphract_mail, itm_ingushetia_spatha, itm_heavy_greaves, itm_mace_3, itm_tab_shield_small_round_c, itm_sassanid_lamellenhelm_4, itm_sarranid_decorated_boots, itm_sassanid_rich_tunic_1], knight_attrib_5,wp(290),knight_skills_5, 0x0000000ca20094c448926db8db6d24d300000000001db49a0000000000000000],
#ruled over lahkmid territory as king
["knight_6_6", "Marzban Al-Mundhir I ibn al-Nu'man", "Al-Mundhir I ibn al-Nu'man", tf_hero, 0, reserved,  fac_kingdom_6, [itm_half_cataphract_horse_4, itm_eastern_scale_3, itm_ingushetia_spatha, itm_heavy_greaves, itm_mace_3, itm_tab_shield_small_round_c, itm_sassanid_lamellenhelm_5, itm_sarranid_decorated_boots, itm_sassanid_rich_tunic_2],    knight_attrib_5,wp(300),knight_skills_1, 0x00000008a200f4c7489269c91b6d22d300000000001db49a0000000000000000],
#ruled over armenia
["knight_6_7", "Marzban Adur-Hormizd", "Adur-Hormizd", tf_hero, 0, reserved,  fac_kingdom_6, [itm_half_cataphract_horse_4, itm_sassanid_long_mail_1, itm_ingushetia_spatha, itm_heavy_greaves, itm_mace_3, itm_tab_shield_small_round_c, itm_sassanid_lamellenhelm_2, itm_sarranid_decorated_boots, itm_sassanid_rich_tunic_3],     knight_attrib_5,wp(300),knight_skills_2, 0x00000004a2011104489271ca636d22d300000000001db49a0000000000000000],
#son of mihr-narseh was given arteshtaran-salar ("chief of the warriors") rank
["knight_6_8", "Arteshtaran-Salar Kardar", "Kardar", tf_hero, 0, reserved,  fac_kingdom_6, [itm_half_cataphract_horse_3, itm_sassanid_long_mail_1,itm_samad_sword, itm_heavy_greaves, itm_mace_3, itm_tab_shield_small_round_c, itm_tsaritsyno_1_simple, itm_sarranid_decorated_boots, itm_sassanid_rich_tunic_4],    knight_attrib_5,wp(390),knight_skills_3|knows_trainer_3, 0x00000004aa00a0c5489271cadc75b6d300000000001db49a0000000000000000],
#hypothetical, probably not actually historical
["knight_6_9", "Argbed Shapur Mihran", "Shapur Mihran", tf_hero, 0, reserved,  fac_kingdom_6, [itm_half_cataphract_horse_3, itm_sassanid_long_mail_1, itm_samad_sword, itm_heavy_greaves, itm_mace_3, itm_tab_shield_small_round_c, itm_sassanid_lamellenhelm_3, itm_sarranid_decorated_boots, itm_sassanid_rich_tunic_1],   knight_attrib_5,wp(260),knight_skills_4|knows_trainer_6, 0x00000004b401118444926dcadc75b91d00000000001db4ab0000000000000000],
#hypothetical, probably not actually historical
["knight_6_10", "Argbed Adur Gushnasp", "Adur Gushnasp", tf_hero, 0, reserved,  fac_kingdom_6, [itm_half_cataphract_horse_7, itm_sassanid_long_mail_1,itm_samad_sword, itm_heavy_greaves, itm_mace_3, itm_tab_shield_small_round_c, itm_sassanid_helmet_mail_2, itm_sarranid_decorated_boots, itm_sassanid_rich_tunic_2],  knight_attrib_5,wp(290),knight_skills_5|knows_trainer_4, 0x000000047400820444926dcadc75b91d00000000001db4ab0000000000000000],
#Franks
["knight_7_1", "Comes Paul", "Paul", tf_hero, 0, reserved,  fac_kingdom_7, [itm_roman_shirt_8, itm_coat_of_plates_red, itm_roman_lorum_fasciari_4, itm_roman_greaves_1, itm_deurne_helmet, itm_leather_gloves, itm_sword_viking_3_small, itm_tab_shield_round_d, itm_half_cataphract_horse_7], knight_attrib_5,wp(310),knight_skills_1|knows_trainer_4, 0x00000007d3003006469276569b6db4db00000000001db6db0000000000000000], #of roman descent
["knight_7_2", "Comes Lothar", "Lothar", tf_hero, 0, reserved,  fac_kingdom_7, [itm_generic_tunic_10, itm_coat_of_plates_red, itm_wrapping_boots,itm_gultlingen_helmet_plume, itm_sword_viking_1, itm_tab_shield_round_d, itm_throwing_axes],  knight_attrib_5,wp(300),knight_skills_2|knows_trainer_3, 0x0000000dc500118646927656a36db4db00000000001db6db0000000000000000],
["knight_7_3", "Comes Reginald", "Reginald", tf_hero, 0, reserved,  fac_kingdom_7, [itm_linen_shirt_14, itm_mid_generic_mail_18, itm_ankle_boots,itm_gultlingen_helmet, itm_leather_gloves,itm_sword_viking_3, itm_tab_shield_round_d, itm_throwing_axes],  knight_attrib_5,wp(290),knight_skills_3, 0x00000008c800024446927656a36db4db00000000001db6db0000000000000000],
["knight_7_4", "Comes Blutmund", "Blutmund", tf_hero, 0, reserved,  fac_kingdom_7, [itm_linen_shirt_11, itm_coat_of_plates_red, itm_ankle_boots,itm_burgh_helmet_1, itm_leather_gloves, itm_sword_medieval_a, itm_tab_shield_round_d, itm_throwing_axes],  knight_attrib_5,wp(310),knight_skills_4, 0x000000000500824536927656a36db4db00000000001db6db0000000000000000],
["knight_7_5", "Comes Walaric", "Walaric", tf_hero, 0, reserved,  fac_kingdom_7, [itm_linen_shirt_5, itm_mid_generic_mail_5, itm_ankle_boots,itm_koblenz_helmet_1, itm_sword_medieval_a, itm_tab_shield_round_d, itm_throwing_axes], knight_attrib_5,wp(300),knight_skills_5,0x000000000500124136927656a36db4db00000000001db6db0000000000000000],
#Suebians
#Comes used for Galician/Roman nobility, Harjatogo for germans
["knight_8_1", "Harjatogo Richimund", "Richimund", tf_hero, 0, reserved,  fac_kingdom_8, [itm_generic_tunic_1, itm_arabian_armor_b, itm_ankle_boots, itm_gultlingen_helmet, itm_sword_viking_1, itm_tab_shield_round_d], knight_attrib_5,wp(310),knight_skills_3, 0x0000000cca00018336db6db6636db6db00000000001db6da0000000000000000],
["knight_8_2", "Harjatogo Frumar", "Frumar", tf_hero, 0, reserved,  fac_kingdom_8, [itm_generic_tunic_7, itm_coat_of_plates_red, itm_ankle_boots, itm_koblenz_helmet_1, itm_sword_viking_2, itm_tab_shield_round_d],  knight_attrib_5,wp(300),knight_skills_2|knows_trainer_3, 0x0000000cdd00224436d38db6636db6db00000000001db6eb0000000000000000],
["knight_8_3", "Comes Ospinio", "Ospinio", tf_hero, 0, reserved,  fac_kingdom_8, [itm_roman_shirt_5, itm_mid_generic_mail_22, itm_ankle_boots,itm_roman_greaves_2, itm_burgh_helmet_1, itm_leather_gloves, itm_arabian_sword_a, itm_simancas_dagger_1, itm_tab_shield_round_e],  knight_attrib_4,wp(280),knight_skills_4, 0x00000008bf003002591ab2d64ab2c91d00000000001e36d50000000000000000],
["knight_8_4", "Comes Palagorius", "Palagorius", tf_hero, 0, reserved,  fac_kingdom_8, [itm_roman_shirt_10, itm_457_mail_shirt_2, itm_ankle_boots,itm_roman_greaves_4, itm_burgh_helmet_2, itm_leather_gloves, itm_sword_viking_2, itm_simancas_dagger_2, itm_tab_shield_round_e],  knight_attrib_5,wp(290),knight_skills_3, 0x00000005700090045cdc92382c95b4d100000000001d36f50000000000000000],
["knight_8_5", "Harjatogo Remismund", "Remismund", tf_hero, 0, reserved,  fac_kingdom_8, [itm_linen_shirt_6, itm_mid_generic_mail_15, itm_ankle_boots, itm_intercisa_helmet_2,itm_sword_medieval_b, itm_tab_shield_round_d], knight_attrib_5,wp(270),knight_skills_3,0x000000001e00230846938db6636db6db00000000001db6da0000000000000000],
["knight_8_6", "Comes Ascanius", "Ascanius", tf_hero, 0, reserved,  fac_kingdom_8, [itm_roman_shirt_8, itm_457_mail_shirt_2, itm_ankle_boots,itm_roman_greaves_1, itm_intercisa_helmet_gilded_1, itm_sword_khergit_4, itm_simancas_dagger_2, itm_tab_shield_round_e], knight_attrib_5,wp(270),knight_skills_2, 0x00000000bf00100422da71b6eb6db31800000000001db6d10000000000000000],
#Burgundians
["knight_9_1", "Harjatogo Gundobad", "Gundobad", tf_hero, 0, reserved,  fac_kingdom_9, [itm_generic_tunic_6, itm_coat_of_plates_red, itm_ankle_boots, itm_gultlingen_helmet_mail, itm_leather_gloves, itm_sword_viking_2, itm_tab_shield_small_round_c, itm_iberian_warhorse_germanic_1], knight_attrib_5,wp(310),knight_skills_2, 0x0000000bd40023c936938db6636db6db00000000001db6eb0000000000000000],
["knight_9_2", "Harjatogo Chilperic I", "Chilperic I", tf_hero, 0, reserved,  fac_kingdom_9, [itm_generic_tunic_3, itm_roman_squamata_5, itm_ankle_boots, itm_burgh_helmet_2, itm_leather_gloves, itm_sword_viking_3, itm_tab_shield_round_d],  knight_attrib_5,wp(300),knight_skills_2|knows_trainer_3, 0x000000091000040736938db6636db6db00000000001db6eb0000000000000000],
["knight_9_3", "Harjatogo Godegisel", "Godegisel", tf_hero, 0, reserved,  fac_kingdom_9, [itm_generic_tunic_5, itm_coat_of_plates_red, itm_ankle_boots, itm_koblenz_helmet_2, itm_leather_gloves,itm_sword_viking_2, itm_tab_shield_round_d, itm_throwing_axes],  knight_attrib_5,wp(290),knight_skills_3, 0x000000062d00118326938db6636db6db00000000001db6eb0000000000000000],
["knight_9_4", "Harjatogo Godomar", "Godomar", tf_hero, 0, reserved,  fac_kingdom_9, [itm_generic_tunic_10, itm_mid_generic_mail_3, itm_ankle_boots, itm_koblenz_helmet_1, itm_leather_gloves, itm_arabian_sword_a, itm_tab_shield_round_d, itm_throwing_axes],  knight_attrib_5,wp(290),knight_skills_4, 0x00000002910001c226938db6636db6db00000000001db6db0000000000000000],
["knight_9_5", "Harjatogo Chilperic II", "Chilperic II", tf_hero, 0, reserved,  fac_kingdom_9, [itm_linen_shirt_7, itm_mid_generic_mail_16, itm_ankle_boots, itm_intercisa_helmet_gilded_1, itm_sword_viking_1, itm_tab_shield_round_d, itm_angon_1], knight_attrib_5,wp(260),knight_skills_5,0x0000000008001201249369a6636db6db00000000001db4d30000000000000000],
#Alemanni also used as generic germanic noble template
["knight_10_1", "Harjatogo Gundolf", "Gundolf", tf_hero, 0, reserved,  fac_kingdom_10, [itm_generic_tunic_2, itm_roman_squamata_5, itm_wrapping_boots, itm_gultlingen_helmet_plume, itm_sword_viking_1, itm_tab_shield_small_round_c, itm_westger_warhorse_1], knight_attrib_5,wp(310),knight_skills_2, 0x0000000e4800120224936d16636db8db00000000001db4d30000000000000000],
["knight_10_2", "Harjatogo Chrocus", "Chrocus", tf_hero, 0, reserved,  fac_kingdom_10, [itm_generic_tunic_5, itm_coat_of_plates_red, itm_ankle_boots, itm_gultlingen_helmet_plume, itm_sword_viking_2, itm_tab_shield_round_d],  knight_attrib_5,wp(300),knight_skills_2|knows_trainer_3, 0x0000000a91000242249371a89b6db6db00000000001db4d30000000000000000],
["knight_10_3", "Harjatogo Actulf", "Actulf", tf_hero, 0, reserved,  fac_kingdom_10, [itm_generic_tunic_10, itm_mid_generic_mail_5, itm_ankle_boots, itm_augsburg_1_helmet, itm_leather_gloves, itm_sword_viking_2, itm_tab_shield_round_d],  knight_attrib_5,wp(290),knight_skills_3, 0x0000000680003281369b71a49b6db4db00000000001db6db0000000000000000],
["knight_10_4", "Harjatogo Erarich", "Erarich", tf_hero, 0, reserved,  fac_kingdom_10, [itm_linen_shirt_4, itm_mid_generic_mail_17, itm_ankle_boots, itm_burgh_helmet_1, itm_leather_gloves, itm_sword_viking_3_small, itm_tab_shield_round_d],  knight_attrib_4,wp(280),knight_skills_4, 0x00000001c8001305269b71a49b71a4db00000000001db6dc0000000000000000],
["knight_10_5", "Harjatogo Haisthilt", "Haisthilt", tf_hero, 0, reserved,  fac_kingdom_10, [itm_linen_shirt_8, itm_mid_generic_mail_18, itm_simple_shoes, itm_intercisa_helmet_gilded_1,itm_sword_medieval_a, itm_tab_shield_round_d], knight_attrib_5,wp(270),knight_skills_3,0x00000001d60023c644946d269b71a4db00000000001db6ac0000000000000000],
#Gepids
["knight_11_1", "Harjatuga Giesmus", "Giesmus", tf_hero, 0, reserved,  fac_kingdom_11,[itm_hun_rich_horse_1, itm_linen_shirt_1,itm_mid_generic_mail_19,itm_wrapping_boots,itm_concesti_helmet,itm_beja_spatha,itm_tab_shield_small_round_c],knight_attrib_5,wp(290),knight_skills_5|knows_trainer_1|knows_trainer_3,0x0000000c470023c544934d269b71a4db00000000001db6ac0000000000000000],
["knight_11_2", "Harjatuga Modaharius", "Modaharius", tf_hero, 0, reserved,  fac_kingdom_11, [itm_hun_rich_horse_2, itm_linen_shirt_2,itm_mid_generic_mail_20,itm_ankle_boots,itm_burgh_helmet_1,itm_sword_viking_2,itm_tab_shield_round_d],       knight_attrib_5,wp(280),knight_skills_5, 0x000000094d0033c434932db69b71a4db00000000001db6e30000000000000000],
["knight_11_3", "Harjatuga Mundo", "Mundo", tf_hero, 0, reserved,  fac_kingdom_11, [itm_hun_horse_4, itm_linen_shirt_3,itm_mid_generic_mail_3,itm_wrapping_boots,itm_koblenz_helmet_1,itm_sword_viking_2,itm_tab_shield_round_d],  knight_attrib_5,wp(300),knight_skills_5|knows_trainer_3, 0x00000005c000538334952db69b7126db00000000001db6db0000000000000000],
["knight_11_4", "Harjatuga Retemeris", "Retemeris", tf_hero, 0, reserved,  fac_kingdom_11, [itm_linen_shirt_4,itm_mid_generic_mail_21,itm_simple_shoes,itm_koblenz_helmet_2,itm_sword_viking_3_small,itm_tab_shield_round_d],    knight_attrib_5,wp(260),knight_skills_5|knows_trainer_4, 0x000000026600124234952db69b7126db00000000001db6db0000000000000000],
["knight_11_5", "Harjatuga Thraustila", "Thraustila", tf_hero, 0, reserved,  fac_kingdom_11, [itm_linen_shirt_5,itm_mid_generic_mail_8,itm_simple_shoes,itm_iatrus_1,itm_sword_medieval_a,itm_tab_shield_round_e],      knight_attrib_4,wp(310),knight_skills_4|knows_trainer_6, 0x000000000f00018124932db69b7126db00000000001db6e40000000000000000],
["knight_11_6", "Harjatuga Cannabaudes", "Cannabaudes", tf_hero, 0, reserved,  fac_kingdom_11, [itm_linen_shirt_7,itm_rich_mail_6,itm_simple_shoes,itm_intercisa_helmet_1,itm_sword_medieval_c,itm_tab_shield_round_d],      knight_attrib_4,wp(290),knight_skills_4|knows_trainer_5, 0x000000000400724336d44db4e371b51b00000000001db6e20000000000000000],
#Saxons
["knight_12_1", "Thegn Saebehrt", "Saebehrt", tf_hero, 0, reserved,  fac_kingdom_12, [itm_linen_shirt_8, itm_long_mail_new_6, itm_ankle_boots, itm_deurne_helmet, itm_leather_gloves, itm_sword_viking_1, itm_tab_shield_round_d, itm_angon_1], knight_attrib_5,wp(300),knight_skills_4, 0x00000009cf00030524934db69b7126db00000000001db6eb0000000000000000],
["knight_12_2", "Thegn Adovacrius", "Adovacrius", tf_hero, 0, reserved,  fac_kingdom_12, [itm_linen_shirt_3, itm_mid_generic_mail_25, itm_ankle_boots, itm_burgh_helmet_1, itm_leather_gloves, itm_sword_viking_1, itm_tab_shield_round_d, itm_angon_1],  knight_attrib_5,wp(300),knight_skills_4|knows_trainer_3, 0x0000000a8600128824934db69b75a8db00000000001db6e30000000000000000],
["knight_12_3", "Thegn Morcar", "Morcar", tf_hero, 0, reserved,  fac_kingdom_12, [itm_generic_tunic_5, itm_mid_generic_mail_4, itm_ankle_boots, itm_burgh_helmet_mail, itm_leather_gloves, itm_samson_spatha_2_rich, itm_tab_shield_round_d, itm_angon_1],  knight_attrib_5,wp(280),knight_skills_3, 0x000000054000018924944d369b75a8db00000000001db6db0000000000000000],
["knight_12_4", "Thegn Wlencing", "Wlencing", tf_hero, 0, reserved,  fac_kingdom_12, [itm_linen_shirt_4, itm_mid_generic_mail_16, itm_ankle_boots, itm_drengsted_helmet_mail, itm_sword_viking_3_small, itm_tab_shield_round_d, itm_angon_1],  knight_attrib_5,wp(260),knight_skills_4, 0x000000020600418236944d369b75a8db00000000001db6db0000000000000000],
["knight_12_5", "Thegn Cissa", "Cissa", tf_hero, 0, reserved,  fac_kingdom_12, [itm_linen_shirt_8, itm_mid_generic_mail_27, itm_ankle_boots, itm_drengsted_helmet_mail, itm_sword_viking_a_long, itm_tab_shield_round_d, itm_westger_warhorse_2], knight_attrib_5,wp(290),knight_skills_5, 0x000000020300114326944d369b75a8db00000000001db6d50000000000000000], #the only one of these lords to get a horse - primarily infantry faction
#Romano-Britons
#king of gwynedd to roughly 460
["knight_13_1", "Dux Cunedda ap Edern", "Cunedda ap Edern", tf_hero, 0, reserved,  fac_kingdom_13,[itm_half_cataphract_horse_2, itm_roman_shirt_12, itm_roman_lorum_fasciari_4, itm_roman_greaves_1, itm_roman_squamata_3, itm_tab_shield_small_round_c, itm_arabian_sword_a, itm_iatrus_plume_2],knight_attrib_5,wp(300),knight_skills_5|knows_trainer_1|knows_trainer_3,0x00000008cd00614426e349976c72ba7500000000001d42eb0000000000000000],
#mid-late 5th cent king of ergyng
["knight_13_2", "Dux Pepianus Spumosus", "Pepianus Spumosus", tf_hero, 0, reserved,  fac_kingdom_13, [itm_nisean_roman_1, itm_roman_shirt_2, itm_ankle_boots, itm_roman_greaves_2, itm_long_briton_mail_1, itm_tab_shield_small_round_c, itm_sword_viking_3, itm_heteny_helmet_1],       knight_attrib_5,wp(300),knight_skills_5, 0x0000000c2900200356db95976c71baf400000000001e46db0000000000000000],
#lead alt clut at this time, was excommunicated by st patrick
["knight_13_3", "Dux Coroticus", "Coroticus", tf_hero, 0, reserved,  fac_kingdom_13, [itm_iberian_warhorse_roman_2, itm_roman_shirt_9, itm_wrapping_boots, itm_roman_greaves_3,itm_long_briton_mail_2, itm_tab_shield_small_round_c, itm_sword_viking_c_long, itm_burgh_helmet_plume_2],  knight_attrib_5,wp(300),knight_skills_5|knows_trainer_3, 0x000000051100014126e359976cb14a4d00000000001d42eb0000000000000000],
#son of cunedda
["knight_13_4", "Dux Einion Yrth ap Cunedda", "Einion Yrth ap Cunedda", tf_hero, 0, reserved,  fac_kingdom_13, [itm_asturco_roman_1, itm_roman_shirt_1, itm_ankle_boots, itm_roman_greaves_4, itm_long_briton_mail_1, itm_tab_shield_small_round_c, itm_sword_viking_3_small, itm_burgh_helmet_2],    knight_attrib_5,wp(300),knight_skills_5|knows_trainer_4, 0x00000000270450035adb6db6eca9b6db00000000001db6dd0000000000000000],
#now is Riothamus
["knight_13_5", "Dux Riothamus", "Riothamus", tf_hero, 0, reserved,  fac_kingdom_13, [itm_iberian_warhorse_roman_1, itm_roman_shirt_2, itm_ankle_boots, itm_roman_greaves_1, itm_roman_squamata_1, itm_tab_shield_small_round_c, itm_arabian_sword_a, itm_intercisa_helmet_rich_3], knight_attrib_5,wp(260),knight_skills_4|knows_trainer_6, 0x000000021600108226db49976ab1464d00000000001d42d30000000000000000],

#Rugii
["knight_14_1", "Harjatogo Feletheus", "Feletheus", tf_hero, 0, reserved,  fac_kingdom_14,[itm_westger_warhorse_1, itm_linen_tunic, itm_wrapping_boots, itm_rich_mail_2, itm_tab_shield_small_round_c, itm_battle_axe_4, itm_arabian_sword_a, itm_gultlingen_helmet_plume],knight_attrib_5,wp(300),knight_skills_5|knows_trainer_1|knows_trainer_3,0x00000008c700004236dc6db4eb6db4db00000000001db6db0000000000000000],
["knight_14_2", "Harjatogo Tufa", "Tufa", tf_hero, 0, reserved,  fac_kingdom_14, [itm_iberian_warhorse_germanic_1, itm_linen_shirt_7, itm_ankle_boots,  itm_coat_of_plates_red, itm_tab_shield_small_round_c, itm_sword_viking_1, itm_gultlingen_helmet_mail],       knight_attrib_5,wp(300),knight_skills_5, 0x00000007df00240336dc6db4eb6db4db00000000001db6db0000000000000000],
["knight_14_3", "Harjatogo Frideric", "Frideric", tf_hero, 0, reserved,  fac_kingdom_14, [itm_linen_shirt_4, itm_ankle_boots, itm_heavy_greaves, itm_rich_mail_4, itm_tab_shield_small_round_c, itm_sword_viking_2, itm_heteny_helmet_1],  knight_attrib_5,wp(300),knight_skills_5|knows_trainer_3, 0x000000008600118436db6db4eb6db4db00000000001db6da0000000000000000],
#Vandals
["knight_15_1", "Harjatuga Huneric", "Huneric", tf_hero, 0, reserved,  fac_kingdom_15,[itm_charger, itm_long_tunic_b,itm_coat_of_plates_red,itm_ankle_boots,itm_heteny_helmet_1,itm_beja_spatha,itm_tab_shield_small_round_c,itm_battle_axe_4],knight_attrib_5,wp(270),knight_skills_5|knows_trainer_1|knows_trainer_3,0x000000078800024228934db6a391a4db00000000001db6e40000000000000000],
["knight_15_2", "Harjatuga Gento", "Gento", tf_hero, 0, reserved,  fac_kingdom_15, [itm_half_cataphract_horse_7, itm_linen_shirt_2,itm_long_mail_new_4,itm_ankle_boots,itm_concesti_helmet,itm_sword_viking_2 ,itm_tab_shield_round_d],       knight_attrib_5,wp(280),knight_skills_5, 0x00000004c200018328934db6e391a4db00000000001db6dc0000000000000000],
["knight_15_3", "Harjatuga Gunthamund", "Gunthamund", tf_hero, 0, reserved,  fac_kingdom_15, [itm_warhorse, itm_linen_shirt_3,itm_mid_generic_mail_23,itm_wrapping_boots,itm_koblenz_helmet_3,itm_sword_viking_3_small ,itm_tab_shield_round_d],  knight_attrib_5,wp(300),knight_skills_5|knows_trainer_3, 0x00000000ed00118426934d28db91a4db00000000001db6d40000000000000000],
["knight_15_4", "Harjatuga Athanagild", "Athanagild", tf_hero, 0, reserved,  fac_kingdom_15, [itm_courser, itm_long_tunic_c,itm_mid_generic_mail_22,itm_wrapping_boots,itm_burgh_helmet_2,itm_sword_viking_2 ,itm_tab_shield_round_d],    knight_attrib_5,wp(280),knight_skills_5|knows_trainer_4, 0x0000000d3200140636936d48db91a4db00000000001db6d30000000000000000],
["knight_15_5", "Harjatuga Sigismund", "Sigismund", tf_hero, 0, reserved,  fac_kingdom_15, [itm_saddle_horse, itm_long_tunic_a,itm_mid_generic_mail_24,itm_wrapping_boots,itm_koblenz_helmet_2,itm_sword_viking_3_small ,itm_tab_shield_round_d],      knight_attrib_5,wp(300),knight_skills_4|knows_trainer_6, 0x0000000c010053c836db6db6db6db6db00000000001db6db0000000000000000],
["knight_15_6", "Harjatuga Athaulf", "Athaulf", tf_hero, 0, reserved,  fac_kingdom_15, [itm_normal_horse24, itm_linen_shirt_6,itm_mid_generic_mail_25,itm_wrapping_boots,itm_burgh_helmet_1,itm_sword_viking_2 ,itm_tab_shield_small_round_c], knight_attrib_5,wp(280),knight_skills_4|knows_trainer_4, 0x0000000c0000018a36dc6db6db6db6db00000000001db6db0000000000000000],
["knight_15_7", "Harjatuga Rodolf", "Rodolf", tf_hero, 0, reserved,  fac_kingdom_15, [itm_normal_horse23, itm_linen_shirt_7,itm_mid_generic_mail_5,itm_ankle_boots,itm_iatrus_1,itm_sword_medieval_a ,itm_tab_shield_round_d], knight_attrib_5,wp(280),knight_skills_4|knows_trainer_4,0x000000004900a10236dc6db4eb6db4db00000000001db6db0000000000000000],
["knight_15_12", "Harjatuga Thrasamund", "Thrasamund", tf_hero, 0, reserved,  fac_kingdom_15, [itm_saddle_horse, itm_linen_shirt_8,itm_mid_generic_mail_9,itm_ankle_boots,itm_intercisa_helmet_2,itm_sword_medieval_a ,itm_tab_shield_round_d], knight_attrib_5,wp(280),knight_skills_4|knows_trainer_4, 0x000000005300204236dc6db4eb6db4db00000000001db6db0000000000000000],
#Iberia 
#Sort of historical? Really no background on him
["knight_16_1", "Saspet Adarnarseh", "Adarnarseh", tf_hero, 0, reserved,  fac_kingdom_16, [itm_half_cataphract_horse_4, itm_leather_vest, itm_sassanid_cavalry_boots_2, itm_arabian_armor_b, itm_sassanid_cataphract_helmet_1, itm_ingushetia_spatha, itm_tab_shield_small_round_c],  knight_attrib_5,wp(290),knight_skills_4|knows_trainer_3|knows_power_draw_3, 0x0000000bb500310536db6db6db6db6db00000000001db6db0000000000000000],
["knight_16_2", "Saspet Bakur", "Bakur", tf_hero, 0, reserved,  fac_kingdom_16, [itm_half_cataphract_horse_3, itm_long_tunic_a, itm_sassanid_cavalry_boots_2, itm_coat_of_plates_red, itm_sassanid_cataphract_helmet_1, itm_strong_bow, itm_barbed_arrows, itm_mace_sassanid, itm_tab_shield_small_round_b],  knight_attrib_4,wp(270),knight_skills_3|knows_trainer_4|knows_power_draw_5|knows_horse_archery_5, 0x0000000c7a00510344db6db6db6db6db00000000001db6e30000000000000000],
["knight_16_3", "Saspet Mirian", "Mirian", tf_hero, 0, reserved,  fac_kingdom_16, [itm_half_cataphract_horse_3, itm_kaftan_tunic_9, itm_ankle_boots, itm_sassanid_scale_1, itm_sarranid_horseman_helmet, itm_mace_sassanid, itm_tab_shield_small_round_c],  knight_attrib_4,wp(260),knight_skills_4|knows_trainer_5, 0x0000000c3f0010cf44db6db6db6db6db00000000001db6e30000000000000000],
["knight_16_4", "Saspet Narseh", "Narseh", tf_hero, 0, reserved,  fac_kingdom_16, [itm_half_cataphract_horse_7, itm_long_tunic_b, itm_ankle_boots, itm_coat_of_plates_red, itm_tarasovsky_1784_helmet_mail_2, itm_samad_sword, itm_tab_shield_small_round_b],  knight_attrib_3,wp(300),knight_skills_4|knows_trainer_5, 0x00000001fa00914248da71b6db6db6db00000000001db6aa0000000000000000],
["knight_16_5", "Saspet Varksen", "Varksen", tf_hero, 0, reserved,  fac_kingdom_16, [itm_half_cataphract_horse_7, itm_sassanid_rich_tunic_1, itm_sassanid_cavalry_boots_2, itm_heavy_greaves, itm_sassanid_scale_1, itm_sassanid_helmet_cloth_2, itm_mace_sassanid, itm_tab_shield_small_round_b],  knight_attrib_3,wp(300),knight_skills_4|knows_trainer_5, 0x00000000ab01010446d371d6db6db6db00000000001db6b10000000000000000],
#Lombards - now down to 5 lords
["knight_17_1", "Harjatogo Godeoc Leting", "Godeoc Leting", tf_hero, 0, reserved,  fac_kingdom_17, [itm_long_shirt_4, itm_coat_of_plates_red, itm_ankle_boots,  itm_gultlingen_helmet_plume, itm_sword_viking_1, itm_tab_shield_round_d,itm_warhorse], knight_attrib_5,wp(310),knight_skills_5, 0x0000000ac600048936db6db4eb6db4db00000000001db6e30000000000000000],
["knight_17_2", "Harjatogo Authari", "Authari", tf_hero, 0, reserved,  fac_kingdom_17, [itm_linen_shirt_3, itm_mid_generic_mail_1, itm_nomad_boots, itm_gultlingen_helmet_mail, itm_sword_viking_2, itm_tab_shield_round_d],  knight_attrib_5,wp(300),knight_skills_2|knows_trainer_3, 0x0000000b4000350726db6db4eb6db4db00000000001db6db0000000000000000],
["knight_17_3", "Harjatogo Hildeprand", "Hildeprand", tf_hero, 0, reserved,  fac_kingdom_17, [itm_green_tunic, itm_coat_of_plates_red, itm_ankle_boots, itm_kalhkni_helmet_1, itm_leather_gloves, itm_sword_viking_2, itm_tab_shield_round_d],  knight_attrib_5,wp(290),knight_skills_3, 0x00000008130064c336db6db4f371b51b00000000001db6db0000000000000000],
["knight_17_4", "Harjatogo Sigmar", "Sigmar", tf_hero, 0, reserved,  fac_kingdom_17, [itm_linen_shirt_7, itm_coat_of_plates_red, itm_wrapping_boots, itm_kalhkni_helmet_mail, itm_leather_gloves, itm_sword_medieval_a, itm_tab_shield_round_d],  knight_attrib_5,wp(310),knight_skills_4, 0x000000024400444252db6db4f371b51b00000000001db6ea0000000000000000],
#["knight_17_5", "Harjatogo Ansfrit", "Ansfrit", tf_hero, 0, reserved,  fac_kingdom_17, [itm_generic_tunic_10, itm_coat_of_plates_red, itm_ankle_boots, itm_gultlingen_helmet_mail, itm_sword_viking_3_small, itm_tab_shield_round_d], knight_attrib_5,wp(290),knight_skills_5,0x000000000401524336d44db4e371b51b00000000001db6e20000000000000000],
#young lord, 16, very basic armor compared to contemporaries
["knight_17_6", "Harjatogo Cleph", "Cleph", tf_hero, 0, reserved,  fac_kingdom_17, [itm_long_shirt_1, itm_mid_generic_mail_3, itm_ankle_boots,  itm_narona_bandhelm_mail, itm_sword_medieval_b, itm_tab_shield_round_d], knight_attrib_5,wp(290),knight_skills_1,0x0000000004001141369c4db4e36db4db00000000001db6d30000000000000000],
#Thuringian
["knight_18_1", "Harjatogo Ansericus", "Ansericus", tf_hero, 0, reserved,  fac_kingdom_18, [itm_generic_tunic_4, itm_coat_of_plates_red, itm_wrapping_boots, itm_gultlingen_helmet_plume, itm_sword_viking_1, itm_tab_shield_round_d, itm_warhorse], knight_attrib_5,wp(310),knight_skills_2, 0x0000000dc60c204422da92454952b98c00000000001ec36c0000000000000000],
["knight_18_2", "Harjatogo Monobredo", "Monobredo", tf_hero, 0, reserved,  fac_kingdom_18, [itm_generic_tunic_8, itm_coat_of_plates_red, itm_ankle_boots, itm_tsaritsyno_2_2, itm_sword_viking_2, itm_tab_shield_round_d, itm_warhorse],  knight_attrib_5,wp(300),knight_skills_2|knows_trainer_3, 0x000000090b04428175658ed69aaecb0a00000000001d27240000000000000000],
["knight_18_3", "Harjatogo Fridiverto", "Fridiverto", tf_hero, 0, reserved,  fac_kingdom_18, [itm_generic_tunic_9, itm_mid_generic_mail_2, itm_ankle_boots, itm_tsaritsyno_2_1, itm_leather_gloves, itm_sword_viking_2, itm_tab_shield_round_d, itm_saddle_horse],  knight_attrib_5,wp(290),knight_skills_3, 0x00000008b500018a5ad9c9592a3b46e3000000000005b8eb0000000000000000],
["knight_18_4", "Harjatogo Geldemirus", "Geldemirus", tf_hero, 0, reserved,  fac_kingdom_18, [itm_linen_shirt_3, itm_mid_generic_mail_7, itm_ankle_boots, itm_fernpass_helmet_2, itm_leather_gloves, itm_sword_viking_3_small, itm_tab_shield_round_d, itm_normal_horse25],  knight_attrib_4,wp(280),knight_skills_4, 0x00000001c8001305269b71a49b71a4db00000000001db6dc0000000000000000],
["knight_18_5", "Harjatogo Malaredus", "Malaredus", tf_hero, 0, reserved,  fac_kingdom_18, [itm_linen_shirt_10, itm_mid_generic_mail_2, itm_simple_shoes, itm_fernpass_helmet_1,itm_sword_medieval_a, itm_tab_shield_round_d, itm_normal_horse23], knight_attrib_5,wp(270),knight_skills_3,0x0000000184000303630bb9c723ce379200000000000a34690000000000000000],
#Jutes
["knight_19_1", "Thegn Ohthere", "Ohthere", tf_hero, 0, reserved,  fac_kingdom_19, [itm_linen_shirt_8, itm_long_mail_new_4, itm_ankle_boots, itm_burgh_helmet_2, itm_leather_gloves, itm_sword_viking_1, itm_tab_shield_round_d, itm_angon_1], knight_attrib_5,wp(300),knight_skills_4, 0x00000007ed0041c536d9adb75c2d249d00000000001aa5910000000000000000],
["knight_19_2", "Thegn Tatuini", "Tatuini", tf_hero, 0, reserved,  fac_kingdom_19, [itm_linen_shirt_3, itm_mid_generic_mail_21, itm_ankle_boots, itm_gultlingen_helmet_mail, itm_leather_gloves, itm_sword_viking_1, itm_tab_shield_round_d, itm_angon_1],  knight_attrib_5,wp(300),knight_skills_4|knows_trainer_3, 0x0000000b060044864d0b57592b3abb6c00000000001e35690000000000000000],
["knight_19_3", "Thegn Brocwulf", "Brocwulf", tf_hero, 0, reserved,  fac_kingdom_19, [itm_generic_tunic_5, itm_mid_generic_mail_1, itm_ankle_boots, itm_drengsted_helmet_mail, itm_leather_gloves, itm_samson_spatha_2_rich, itm_tab_shield_round_d, itm_angon_1],  knight_attrib_5,wp(280),knight_skills_3, 0x00000005500822885ba455acdca93b1a00000000001dc7210000000000000000],
["knight_19_4", "Thegn Freomund", "Freomund", tf_hero, 0, reserved,  fac_kingdom_19, [itm_linen_shirt_4, itm_mid_generic_mail_9, itm_ankle_boots, itm_burgh_helmet_mail, itm_sword_viking_3_small, itm_tab_shield_round_d, itm_angon_1],  knight_attrib_5,wp(260),knight_skills_4, 0x000000019010024264da91b2d496a71c00000000001db9a30000000000000000],
["knight_19_5", "Thegn Oisc", "Oisc", tf_hero, 0, reserved,  fac_kingdom_19, [itm_linen_shirt_8, itm_mid_generic_mail_1, itm_ankle_boots, itm_drengsted_helmet_mail, itm_sword_viking_a_long, itm_tab_shield_round_d, itm_saddle_horse], knight_attrib_5,wp(290),knight_skills_5, 0x000000014e0010094ce5713a9db254a100000000001db6eb0000000000000000], #the only one of these lords to get a horse - primarily infantry faction
# ripuarian franks
["knight_20_1", "Comes Faroinus", "Faroinus", tf_hero, 0, reserved,  fac_kingdom_20, [itm_green_tunic, itm_mid_generic_mail_18, itm_ankle_boots, itm_burgh_helmet_2, itm_sword_viking_2, itm_tab_shield_round_d, itm_warhorse], knight_attrib_5,wp(300),knight_skills_1, 0x0000000c84000202369c4db4e36db4db00000000001db6d30000000000000000],
["knight_20_2", "Comes Lantbertus", "Lantbertus", tf_hero, 0, reserved,  fac_kingdom_20, [itm_linen_shirt_22,  itm_mid_generic_mail_18, itm_wrapping_boots, itm_fernpass_helmet_2, itm_sword_viking_1, itm_tab_shield_round_d, itm_warhorse],  knight_attrib_5,wp(300),knight_skills_2|knows_trainer_3, 0x0000000958002243369c51b6db6db4db00000000001db6d30000000000000000],
["knight_20_3", "Comes Chararic", "Chararic", tf_hero, 0, reserved,  fac_kingdom_20, [itm_linen_shirt_1, itm_mid_generic_mail_17, itm_ankle_boots,  itm_intercisa_helmet_gilded_1, itm_leather_gloves,itm_sword_viking_3, itm_tab_shield_round_d, itm_throwing_axes],  knight_attrib_5,wp(290),knight_skills_3, 0x00000002cb003304369c51b6db6db4db00000000001db6d30000000000000000],
["knight_20_4", "Comes Gedalbertus", "Gedalbertus", tf_hero, 0, reserved,  fac_kingdom_20, [itm_linen_shirt_3, itm_coat_of_plates_red, itm_ankle_boots, itm_intercisa_helmet_1, itm_leather_gloves, itm_sword_medieval_a, itm_tab_shield_round_d, itm_throwing_axes],  knight_attrib_5,wp(310),knight_skills_4, 0x00000001130022c6369c51b6db6db4db00000000001db6d20000000000000000],
#Replaced with scirii, 2 lords + 1 king, very small faction, mainly to slow down potential ostrogothic snowball
["knight_21_1", "Harjatuga Odoacer", "Odoacer", tf_hero, 0, reserved,  fac_kingdom_21, [itm_linen_shirt_8, itm_long_mail_new_4, itm_wrapping_boots,itm_ankle_greaves, itm_koblenz_helmet_3, itm_sword_viking_2, itm_tab_shield_round_d, itm_warhorse, itm_bearded_axe_2], knight_attrib_5,wp(380),knight_skills_1, 0x0000000027000042249a6e36db6db6db00000000001db6d20000000000000000],
["knight_21_2", "Harjatuga Onoulphus", "Onoulphus", tf_hero, 0, reserved,  fac_kingdom_21, [itm_linen_shirt_2, itm_long_mail_new_4, itm_wrapping_boots,itm_ankle_greaves, itm_fernpass_helmet_2, itm_sword_viking_2, itm_tab_shield_round_d, itm_warhorse, itm_bearded_axe_2], knight_attrib_5,wp(380),knight_skills_1, 0x000000002700118426da6e36db6db6db00000000001db6d20000000000000000],

#romano-bebers
["knight_22_1", "Comes Castinus", "Castinus", tf_hero, 0, reserved,  fac_kingdom_22,[itm_nisean_cataphract_4, itm_roman_shirt_12, itm_wrapping_boots, itm_heavy_greaves, itm_457_scale_hauberk_3, itm_tab_shield_small_round_c, itm_sword_viking_3, itm_heteny_helmet_1],knight_attrib_5,wp(270),knight_skills_5|knows_trainer_1|knows_trainer_3,0x0000000dff012142595b92496b6d9b2300000000001db6e20000000000000000],
["knight_22_2", "Comes Maurianus", "Maurianus", tf_hero, 0, reserved,  fac_kingdom_22, [itm_barb_cham_1, itm_roman_shirt_2, itm_ankle_boots_white, itm_ankle_greaves, itm_long_roman_mail_1, itm_tab_shield_small_round_c, itm_sword_viking_3, itm_koblenz_helmet_3],       knight_attrib_5,wp(280),knight_skills_5, 0x0000000da3010005169b75c76c8db91a00000000001db6db0000000000000000],
["knight_22_3", "Comes Mettius", "Mettius", tf_hero, 0, reserved,  fac_kingdom_22, [itm_barb_cham_2, itm_roman_shirt_9, itm_ankle_boots, itm_ankle_greaves, itm_long_roman_mail_3, itm_tab_shield_small_round_c, itm_sword_viking_c_long, itm_burgh_helmet_2],  knight_attrib_5,wp(300),knight_skills_5|knows_trainer_3, 0x0000000427013004369b75b6dc6db91b00000000001db6d40000000000000000],
["knight_22_4", "Comes Julianus", "Julianus", tf_hero, 0, reserved,  fac_kingdom_22, [itm_barb_cham_3, itm_roman_shirt_2, itm_ankle_boots,  itm_mid_roman_mail_8,itm_tab_shield_small_round_c, itm_arabian_sword_a, itm_iatrus_2,itm_javelin], knight_attrib_5,wp(260),knight_skills_4|knows_trainer_6, 0x0000000715014003569b7646e46db91a00000000001db6e20000000000000000],
["knight_22_5", "Comes Manius", "Manius", tf_hero, 0, reserved,  fac_kingdom_22, [itm_barb_2, itm_roman_shirt_3, itm_ankle_boots, itm_ankle_greaves, itm_mid_roman_mail_6, itm_tab_shield_small_round_c, itm_sword_viking_3, itm_burgh_helmet_1,itm_javelin], knight_attrib_5,wp(280),knight_skills_4|knows_trainer_4, 0x000000002d012002369b7646e46db91a00000000001db6db0000000000000000],
#huns
["knight_23_1", "Chief Skottas", "Skottas", tf_hero, 0, reserved,  fac_kingdom_23, [itm_hun_rich_horse_1, itm_kaftan_hunnic_4,  itm_hunnic_kaftan_lamellar_2,itm_nomad_boots,  itm_heavy_greaves, itm_kalhkni_helmet_1,  itm_leather_gloves,  itm_arabian_sword_a, itm_tab_shield_small_round_c, itm_niya_bow_2, itm_khergit_arrows],  knight_attrib_1,wp(270),knight_skills_1|knows_trainer_3|knows_power_draw_4, 0x0000000d0000c28a47146d34f44db6db00000000001db6990000000000000000],
["knight_23_2", "Chief Avitohol",  "Avitohol", tf_hero, 0, reserved,  fac_kingdom_23, [itm_hun_rich_horse_2, itm_kaftan_hunnic_2,   itm_hunnic_kaftan_lamellar_1, itm_hide_boots,  itm_heavy_greaves, itm_concesti_helmet,  itm_leather_gloves, itm_bearded_axe_2,  itm_tab_shield_small_round_b, itm_niya_bow_2, itm_khergit_arrows], knight_attrib_2,wp(260),knight_skills_2|knows_power_draw_4, 0x0000000d5100e3ca47146920f44db4db00000000001db6990000000000000000],
#sorta historical
["knight_23_3", "Chief Emnetzur",  "Emnetzur", tf_hero, 0, reserved,  fac_kingdom_23, [itm_hun_rich_horse_2, itm_kaftan_hunnic_5, itm_kaftan_lamellar_1,itm_nomad_boots,  itm_heavy_greaves,  itm_kerch_lamellenhelm_gilded, itm_sword_viking_3,  itm_tab_shield_small_round_c, itm_niya_bow_2, itm_khergit_arrows],  knight_attrib_3,wp(280),knight_skills_3|knows_trainer_5|knows_power_draw_4, 0x0000000a4000d10b470a8930f44db4db00000000001db6990000000000000000],
["knight_23_4", "Chief Ultzindur", "Ultzindur", tf_hero, 0, reserved,  fac_kingdom_23, [itm_hun_rich_horse_nobard_1, itm_kaftan_hunnic_1,  itm_kaftan_lamellar_3, itm_hide_boots,     itm_kalhkni_helmet_2, itm_sword_khergit_2,  itm_tab_shield_small_round_c],  knight_attrib_4,wp(260),knight_skills_4|knows_power_draw_4, 0x000000078000d24c470a9230db9528db00000000001db6990000000000000000],
["knight_23_5", "Chief Chelchal",  "Chelchal", tf_hero, 0, reserved,  fac_kingdom_23, [itm_hun_rich_horse_nobard_2, itm_kaftan_hunnic_3,  itm_kaftan_lamellar_4, itm_hide_boots,  itm_heavy_greaves, itm_turaevo_helmet,  itm_sword_viking_c_long, itm_lance,itm_battle_axe_4, itm_tab_shield_small_round_c],  knight_attrib_5,wp(290),knight_skills_5|knows_power_draw_4, 0x00000005f000c249430a9230db9528db00000000001db6990000000000000000],
#alan lord
["knight_23_6", "Chief Madakos", "Madakos", tf_hero, 0, reserved,  fac_kingdom_23, [itm_hun_rich_horse_nobard_1, itm_kaftan_alan_2,itm_alan_cataphract_1,itm_nomad_boots, itm_heavy_greaves,  itm_kishpek_helmet_mail, itm_klin_yar_spatha,  itm_tab_shield_small_round_b], knight_attrib_1,wp(270),knight_skills_1|knows_power_draw_4, 0x000000019a0851c2369b762b8b8da6b300000000001048a50000000000000000],
#crimean gothic lord
["knight_23_7", "Regulus Hariulfus","Hariulfus", tf_hero, 0, reserved,  fac_kingdom_23, [itm_khergit_leather_boots,itm_rich_mail_8,itm_tunic_long_pants_8,itm_leather_gloves,itm_concesti_helmet,itm_tetraxitae_spatha,itm_spear_sword,itm_tab_shield_round_e], knight_attrib_2,wp(300),knight_skills_2|knows_power_draw_4, 0x000000054e00628b525b6dd6ec91a71400000000001e14ed0000000000000000],
#historical
["knight_23_8", "Chief Ernak", "Ernak", tf_hero, 0, reserved,  fac_kingdom_23, [itm_hun_rich_horse_1,  itm_kaftan_hunnic_6, itm_kaftan_lamellar_6,itm_nomad_boots, itm_turaevo_helmet_aventail,   itm_tab_shield_small_round_c,itm_khergit_bow,itm_khergit_arrows,itm_sword_viking_3],  knight_attrib_3,wp(310),knight_skills_3|knows_power_draw_4, 0x000000009e00d3c147147134f44db6db00000000001db6990000000000000000],

["knight_24_1", "Saspet Demetre", "Demetre", tf_hero, 0, reserved,  fac_kingdom_24, [itm_half_cataphract_horse_4, itm_leather_vest, itm_sassanid_cavalry_boots_2, itm_arabian_armor_b, itm_sassanid_cataphract_helmet_3, itm_ingushetia_spatha, itm_tab_shield_small_round_c],  knight_attrib_5,wp(290),knight_skills_4|knows_trainer_3|knows_power_draw_3, 0x0000000ded00708539537aeade49249200000000001e35560000000000000000],
["knight_24_2", "Saspet Saurmage", "Saurmage", tf_hero, 0, reserved,  fac_kingdom_24, [itm_half_cataphract_horse_3, itm_long_tunic_a, itm_sassanid_cavalry_boots_2, itm_coat_of_plates_red, itm_sassanid_cataphract_helmet_3, itm_strong_bow, itm_barbed_arrows, itm_mace_roman_1, itm_tab_shield_small_round_b],  knight_attrib_4,wp(270),knight_skills_3|knows_trainer_4|knows_power_draw_5|knows_horse_archery_5, 0x00000006f300f48e5adb52d5d765913800000000001eb7690000000000000000],
["knight_24_3", "Saspet Nersaran", "Nersaran", tf_hero, 0, reserved,  fac_kingdom_24, [itm_half_cataphract_horse_3, itm_kaftan_tunic_9, itm_ankle_boots, itm_cataphract_armor_1, itm_tsaritsyno_1_light,  itm_mace_sassanid, itm_tab_shield_small_round_c],  knight_attrib_4,wp(260),knight_skills_4|knows_trainer_5, 0x00000007f80090ce4adc89b6e46db6db00000000001e36e20000000000000000],
["knight_24_4", "Saspet Artavaz", "Artavaz", tf_hero, 0, reserved,  fac_kingdom_24, [itm_long_tunic_b, itm_ankle_boots, itm_coat_of_plates_red, itm_tarasovsky_1784_helmet_mail_2, itm_sword_medieval_a, itm_tab_shield_small_round_b],  knight_attrib_3,wp(300),knight_skills_4|knows_trainer_5, 0x00000005680460845914d5bad4929a9200000000001db6e30000000000000000],
["knight_24_5", "Saspet Damnazes", "Damnazes", tf_hero, 0, reserved,  fac_kingdom_24, [itm_kaftan_tunic_10, itm_sassanid_cavalry_boots_2, itm_heavy_greaves, itm_long_mail_new_8, itm_tarasovsky_1784_helmet_mail_2, itm_mace_roman_1, itm_tab_shield_small_round_b],  knight_attrib_3,wp(300),knight_skills_4|knows_trainer_5, 0x00000001bb007105395c7258f525255d00000000001e36dc0000000000000000],

["knight_25_1", "Phylarch Mouses", "Mouses", tf_hero, 0, reserved,  fac_kingdom_25, [itm_half_cataphract_horse_7, itm_leather_vest, itm_sassanid_simple_boots_1, itm_457_scale_hauberk_1, itm_gultlingen_helmet, itm_arabian_sword_a, itm_tab_shield_small_round_c],  knight_attrib_5,wp(290),knight_skills_4|knows_trainer_3|knows_power_draw_3, 0x0000000fe90151836adb91b8327236db00000000001db6ac0000000000000000],
["knight_25_2", "Phylarch Tantani", "Tantani", tf_hero, 0, reserved,  fac_kingdom_25, [itm_arabian_horse_a, itm_long_tunic_a, itm_sassanid_simple_boots_2, itm_coat_of_plates_red, itm_koblenz_helmet_2, itm_arabian_sword_a, itm_tab_shield_small_round_c],  knight_attrib_4,wp(270),knight_skills_3|knows_trainer_4|knows_power_draw_5|knows_horse_archery_5, 0x00000006fc01600154db91b83271b6db00000000001db65b0000000000000000],
["knight_25_3", "Phylarch Silko", "Silko", tf_hero, 0, reserved,  fac_kingdom_25, [itm_arabian_horse_d, itm_roman_shirt_10, itm_sassanid_simple_boots_3, itm_mid_roman_mail_7, itm_burgh_helmet_1,  itm_arabian_sword_a, itm_tab_shield_small_round_c],  knight_attrib_4,wp(260),knight_skills_4|knows_trainer_5, 0x000000003f016002609a91b87371b4db00000000001d36a40000000000000000],

["knight_26_1", "Phylarch Breytek", "Breytek", tf_hero, 0, reserved,  fac_kingdom_26, [itm_half_cataphract_horse_1, itm_leather_vest, itm_sassanid_simple_boots_2, itm_457_scale_hauberk_2, itm_koblenz_helmet_3, itm_arabian_sword_a, itm_tab_shield_small_round_c],  knight_attrib_5,wp(290),knight_skills_4|knows_trainer_3|knows_power_draw_3, 0x000000003f016003449b71b87371b4db00000000001d36a90000000000000000],

["knight_27_1", "Chief Saros", "Saros", tf_hero, 0, reserved,  fac_kingdom_27, [itm_half_cataphract_horse_6, itm_kaftan_alan_2, itm_nomad_boots, itm_alan_cataphract_1, itm_kishpek_helmet_mail, itm_klin_yar_spatha, itm_tab_shield_small_round_c],  knight_attrib_5,wp(290),knight_skills_4|knows_trainer_3|knows_power_draw_3, 0x0000000fc20073c6429b6e38db6db2db00000000001d34e50000000000000000],
["knight_27_2", "Chief Saurmag", "Saurmag", tf_hero, 0, reserved,  fac_kingdom_27, [itm_half_cataphract_horse_5, itm_kaftan_alan_3, itm_nomad_boots, itm_alan_cataphract_1, itm_kishpek_helmet_mail, itm_strong_bow, itm_barbed_arrows, itm_beja_spatha, itm_tab_shield_small_round_b],  knight_attrib_4,wp(270),knight_skills_3|knows_trainer_4|knows_power_draw_5|knows_horse_archery_5, 0x0000000cd50052875b1b6e38db6db6db00000000001db4f30000000000000000],
["knight_27_3", "Chief Sangipan", "Sangipan", tf_hero, 0, reserved,  fac_kingdom_27, [itm_hun_rich_horse_1, itm_kaftan_alan_5, itm_wrapping_boots, itm_coat_of_plates_red, itm_kalhkni_helmet_1,  itm_ingushetia_spatha, itm_tab_shield_small_round_c],  knight_attrib_4,wp(260),knight_skills_4|knows_trainer_5, 0x00000006c0009285379b8dd89b8ca6d300000000001e34d90000000000000000],
["knight_27_4", "Chief Beorgor", "Beorgor", tf_hero, 0, reserved,  fac_kingdom_27, [itm_hun_rich_horse_nobard_2, itm_kaftan_alan_green, itm_simple_shoes, itm_kaftan_lamellar_2, itm_khudashevsky_helmet_2, itm_hunnic_spatha, itm_tab_shield_small_round_b],  knight_attrib_3,wp(300),knight_skills_4|knows_trainer_5, 0x000000039e000146579b8dd89b8ca8db00000000001db4fb0000000000000000],
["knight_27_5", "Chief Safrak", "Safrak", tf_hero, 0, reserved,  fac_kingdom_27, [itm_hun_horse_2, itm_kaftan_alan_white, itm_simple_shoes, itm_kaftan_lamellar_3, itm_rozhdestvensky_helmet_mail, itm_hunnic_spatha, itm_tab_shield_small_round_b],  knight_attrib_3,wp(300),knight_skills_4|knows_trainer_5, 0x00000000d6001287351b8dc69b8ca4db00000000001db4db0000000000000000],


  ["kingdom_1_pretender",  "Libius Severus", "Libius Severus",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_1,[itm_warhorse,itm_roman_shirt_14,itm_ankle_boots_white,itm_roman_greaves_2,itm_cuirass_roman_2,itm_sword_viking_3,itm_tab_shield_small_round_c,itm_gultlingen_helmet],          lord_attrib,wp(320),knight_skills_5, 0x0000000a6300200236d36db4ab6db6db00000000001d36da0000000000000000],
#claims military general

  ["kingdom_2_pretender",  "Iulius Patricius", "Iulius Patricius",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_2,[itm_cataphract_horse_3,itm_roman_shirt_14,itm_ankle_boots_white,itm_roman_greaves_1,itm_roman_scale_cuirass_1,itm_arabian_sword_a,itm_tab_shield_small_round_c,itm_gultlingen_helmet_plume],    lord_attrib,wp(320),knight_skills_5, 0x000000000a00104244db6dc6a36db6db00000000001db6d30000000000000000],
#high popularity, weak current emperor

  ["kingdom_3_pretender",  "Euric II", "Euric II",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_3,[itm_courser, itm_linen_shirt_6, itm_ankle_boots, itm_splinted_greaves, itm_mid_generic_mail_12, itm_sword_viking_3, itm_tab_shield_small_round_c, itm_burgh_helmet_2],      lord_attrib,wp(320),knight_skills_5, 0x000000002700210954da9136db6db6db00000000001db6ea0000000000000000],
#of the family

  ["kingdom_4_pretender",  "Odoin",   "Odoin",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_4,[itm_warhorse, itm_linen_shirt_2, itm_leather_boots, itm_heavy_greaves, itm_mid_generic_mail_5, itm_sword_viking_2, itm_tab_shield_round_e,itm_koblenz_helmet_3],            lord_attrib,wp(320),knight_skills_5, 0x0000000b8900020a54da7136db6db6db00000000001d36d40000000000000000],
#dispossessed and wronged

  ["kingdom_5_pretender",  "Lord Kastor of Veluca",  "Kastor",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_5,[],         lord_attrib,wp(220),knight_skills_5, 0x0000000bed1031051da9abc49ecce25e00000000001e98680000000000000000, rhodok_face_old_2],
#republican

  ["kingdom_6_pretender",  "Peroz", "Peroz", tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_6,[itm_warhorse_sarranid, itm_sassanid_cavalry_boots_2, itm_kaftan_tunic_9,  itm_emperor_armor_c, itm_heavy_greaves, itm_sassanid_helmet_shah, itm_crown_3, itm_ingushetia_spatha, itm_tab_shield_small_round_c],          lord_attrib,wp(360),knight_skills_5, 0x00000000230100c248db71b8eb95c6db00000000001db6f10000000000000000],

#Royal family members

  ["knight_1_1_wife","Error - knight_1_1_wife should not appear in game","knight_1_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners, [itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],

  ["kingdom_1_lady_1","Comitessa Valeriana","Valeriana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_roman_noble_dress_1,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000fb7000002371b711bec91b8db00000000001dc7140000000000000000],
  ["kingdom_1_lady_2","Comitessa Marcellina","Marcellina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_roman_noble_dress_2,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007ef0010043adb923d7491b8db00000000001dc6d40000000000000000],
  #was licinia eudoxia
  ["kingdom_1_lady_3","Comitessa Julia","Julia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_roman_noble_dress_3,     itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000daf00200c36d9699d7449a69a00000000001d42e30000000000000000],
  ["kingdom_1_lady_4","Comitessa Eudocia","Eutropia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [    itm_roman_noble_dress_4 ,     itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000aaa00400c36d1b2b8e251b69a00000000001d42e30000000000000000],
  ["kingdom_1_lady_5","Comitessa Placidia","Placidia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_roman_noble_dress_1,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002b400000336d1b2d8e2b2a69100000000001d42e30000000000000000],
  ["kingdom_1_lady_6","Comitessa Lysandra","Lysandra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_roman_noble_dress_2,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000a5001006165195d8eaca471a00000000001ca1130000000000000000],
  ["kingdom_1_lady_7","Comitessa Blandina","Blandina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [    itm_roman_noble_dress_sleeveless_1,     itm_ankle_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000bef001009145196156b92471a00000000001ca1530000000000000000],
  ["kingdom_1_lady_8","Comitessa Prisca","Prisca",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [    itm_roman_noble_dress_sleeveless_2,     itm_ankle_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000022f00300312597658ab8e471a00000000001cc1630000000000000000],
  ["kingdom_1_lady_9","Comitessa Agape","Agape",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_roman_noble_dress_sleeveless_3,       itm_ankle_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000370050122499762524a634d300000000001cb1930000000000000000], #added in to support 1 more lord
  ["kingdom_1_lady_11","Comitessa Anapsychia","Anapsychia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [    itm_roman_noble_dress_sleeveless_4 ,     itm_ankle_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002900000a571a75b2a3b234d300000000001cb18b0000000000000000],
  ["kingdom_1_lady_14","Comitessa Anastasia","Anastasia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_roman_noble_dress_sleeveless_2,       itm_ankle_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000012300400d371a76451b8e38d300000000001d319b0000000000000000],

  ["kingdom_2_lady_1","Comitessa Verina","Verina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_roman_noble_dress_1,       itm_ankle_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000af40010103aa17646e391d8d300000000001d51530000000000000000],
  ["kingdom_2_lady_2","Comitessa Ariadne","Ariadne",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_roman_noble_dress_sleeveless_1,       itm_excubitor_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003600400a465a7619234a469a00000000001cd19b0000000000000000],
  #Wife of Basiliscus
  ["kingdom_2_lady_3","Comitessa Aelia Zenonis","Aelia Zenonis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [itm_roman_noble_dress_2 ,itm_ankle_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000032c00500b585a7519238a469a00000000001cd18b0000000000000000],
  #No longer daughters of leo, was born later
  #Wife of Anthemius
  ["kingdom_2_lady_4","Comitessa Marcia Euphemia","Marcia Euphemia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_roman_noble_dress_3 ,     itm_ankle_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000092000100d585a762db3d24a9a00000000001cd18b0000000000000000],
  #gotta change this up, she wasn't even born yet when the mod starts
  ["kingdom_2_lady_5","Comitessa Leontia","Leontia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_lady_dress_ruby,       itm_ankle_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000220000008585a762db291b49a00000000001cc14b0000000000000000],
  #end
  ["kingdom_2_lady_6","Comitessa Sigilda","Sigilda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_lady_dress_green,       itm_ankle_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000800002009465a7619b251b49a00000000001cc16b0000000000000000], #theoderic strabo's wife
  ["kingdom_2_lady_7","Comitessa Arcadia","Arcadia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_roman_noble_dress_4,     itm_ankle_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000277000004375a6c45598dc69b00000000001db6db0000000000000000],
  ["kingdom_2_lady_8","Comitessa Pomponia","Pomponia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_roman_noble_dress_sleeveless_2 ,     itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000004b100300436dcd1a111a9d2e400000000001db32b0000000000000000],
  ["kingdom_2_lady_9","Comitessa Faustina","Faustina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_roman_noble_dress_sleeveless_4 ,     itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000e0050043b142c956da946da00000000001d235b0000000000000000],
  ["kingdom_2_lady_10","Comitessa Honoria","Honoria",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_roman_noble_dress_sleeveless_3 ,     itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000032001003469ab21b6b8d2b6a00000000001d24d20000000000000000],

  ["kingdom_3_lady_1","Ragnahild","Ragnahild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [itm_dress_4, itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c910000107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_3_lady_2","Nelda","Nelda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [ itm_dress_8, itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000a4f08100232636aa92c6e395c00000000001e43130000000000000000],
  ["kingdom_3_lady_3","Bela","Bela",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [  itm_dress_6, itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000194041006175371d565ad36d200000000001e256b0000000000000000],
  ["kingdom_3_lady_4","Elina","Elina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [ itm_dress_5, itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000575101005686c55a4e98ab51400000000001d332b0000000000000000],
  ["kingdom_3_lady_5","Constanis","Constanis",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [  itm_dress_4,     itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018208000d392164c3564dcb1c00000000001d46e10000000000000000],
  ["kingdom_3_lady_6","Vera","Vera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [ itm_dress_4,      itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000002a10500b34dbc5b71d39cb9d00000000000d46940000000000000000],
  ["kingdom_3_lady_7","Auberina","Auberina",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [  itm_dress_5,     itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000c0c401028426e456d9148e400000000001f472a0000000000000000],
  ["kingdom_3_lady_8","Tibal","Tibal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [   itm_dress_5, itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000006080009574c4145514ed8db00000000001c52a60000000000000000],

  ["kingdom_4_lady_1","Ereleuva","Ereleuva",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [itm_dress_4, itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000074910101046db84a5a551b2db00000000001db2ae0000000000000000],
  ["kingdom_4_lady_2","Geleswintha","Geleswintha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [itm_dress_5, itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000088f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_4_lady_3","Euthymia","Euthymia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [ itm_dress_6, itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000d04300624927133228da6dc00000000001d13530000000000000000],
  ["kingdom_4_lady_4","Gailavira","Gailavira",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [ itm_dress_7, itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000f9604200729b131e94d6a8ae400000000001e24dd0000000000000000],
  ["kingdom_4_lady_5","Avagisa","Avagisa",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [ itm_dress_8, itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000074b00200618956a34a44db4a200000000001c92890000000000000000],
  ["kingdom_4_lady_6","Brunihild","Brunihild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [ itm_dress_4,  itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x00000000130840012b1b52372a89c4db00000000001eb56d0000000000000000],
  ["kingdom_4_lady_7","Seda","Seda",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [ itm_dress_4, itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000004500500c2852709362a934d400000000001cd2e40000000000000000],
  ["kingdom_4_lady_8","Amalda","Amalda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [ itm_dress_6, itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000035f00000b151c70c2d5adb6db00000000001ea77a0000000000000000],

  ["kingdom_5_lady_1","Brina","Brina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,     itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000fca00200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_lady_2","Aliena","Aliena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,      itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000070208100222d432cf6d4a2ae300000000001d36c90000000000000000],
  ["kingdom_5_lady_3","Aneth","Aneth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019c0030021b5b71b6db6db6db00000000001d231b0000000000000000],
  ["kingdom_5_lady_5","Saraten","Saraten",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,    itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000091040052a9b74a30badb6e500000000001d53640000000000000000],

  ["kingdom_6_lady_1","Rayma","Rayma",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,  itm_sarranid_head_cloth,        itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000fd800600116db6db6db6db6db00000000001dd6db0000000000000000],
  ["kingdom_6_lady_2","Thanaikha","Thanaikha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000b3f007004292c6db6e16d36db00000000001d56f80000000000000000],
  ["kingdom_6_lady_3","Sagdukht","Sagdukht",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000abf006005292b6f5aabadb6db00000000001d32cc0000000000000000],
  ["kingdom_6_lady_4","Shatha","Shatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007b6002004252d524cd925c89b00000000001d569d0000000000000000],
  ["kingdom_6_lady_5","Bawthan","Bawthan",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007fd001008168a694b15a9a91b00000000001cc4d40000000000000000],
  ["kingdom_6_lady_6","Mahayl","Mahayl",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x00000003bf0010061b5cb5d8ed75b4db00000000001e271c0000000000000000],
  ["kingdom_6_lady_7","Isna","Isna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000033f000002185b4d5aebcd2b2a00000000001d52e30000000000000000],
  ["kingdom_6_lady_8","Siyafan","Siyafan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,        itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001be006008155b8a4d2a8dc4db00000000001cd2c30000000000000000],
  ["kingdom_6_lady_9","Ifar","Ifar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000007f005005395a6ca52b8da4da00000000001d405b0000000000000000],
  ["kingdom_6_lady_10","Yasmin","Yasmin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x00000003780070024a9471392bae36d300000000001ea56d0000000000000000],
  #["kingdom_6_lady_11","Dula","Dula",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320120040f64adb0a120004800000000001c70000000000000000000],

  ["kingdom_7_lady_1","Basina II","Basina II",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000070b100003274d65d35239eb1300000000001d350b0000000000000000],
  ["kingdom_7_lady_2","Wivecin","Wivecin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000003c610100664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_7_lady_3","Rotlenda","Rotlenda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [    itm_peasant_dress, itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000fe00c20062a928db55589aae300000000001ea5540000000000000000],
  ["kingdom_7_lady_4","Hildegund","Hildegund",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [    itm_peasant_dress,  itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000fd80c500856928db4ed71aae300000000001ec4e40000000000000000],
  ["kingdom_7_lady_5","Genofeva","Genofeva",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000012f103005195271c922a9d72300000000001e35540000000000000000],
  ["kingdom_7_lady_6","Andovera","Andovera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000610100d285970a52525b8ec00000000001d45520000000000000000],

  ["kingdom_8_lady_1","Rimionda","Rimionda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000fcb0020091751aeaa9549d91a00000000001ea4950000000000000000], #germanic
  ["kingdom_8_lady_2","Fredesinda","Fredesinda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000fc0003006345c89572baa25a500000000001ca4840000000000000000], #germanic
  ["kingdom_8_lady_3","Galeria","Galeria",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [    itm_roman_noble_dress_2, itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000005f00010040f512ed8da92c91b00000000001cb6940000000000000000], #roman
  ["kingdom_8_lady_4","Aelia","Aelia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [    itm_roman_noble_dress_3,  itm_ankle_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001db00200646da53172cc926db00000000001e46a50000000000000000], #roman
  ["kingdom_8_lady_5","Camilia","Camilia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [      itm_roman_noble_dress_sleeveless_4,   itm_ankle_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003200000c1b63894729b5bb2300000000001eb4a30000000000000000], #roman
  ["kingdom_8_lady_6","Ebrailli","Ebrailli",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [      itm_dress_5 ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000040072b5276252d6a36e500000000001d24a40000000000000000], #germanic

  ["kingdom_9_lady_1","Helene","Helene",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000095510100456517124a9b5b91b00000000001d56c30000000000000000],
  ["kingdom_9_lady_2","Gunda","Gunda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000c001030075b218d9a8d6594d400000000001dc74d0000000000000000],
  ["kingdom_9_lady_3","Arda","Arda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [    itm_peasant_dress, itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000005d00c2009382295c756b1349c00000000001cd6620000000000000000],
  ["kingdom_9_lady_4","Rosamunde","Rosamunde",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [    itm_peasant_dress,  itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000033724b5971aaa271400000000001ca52a0000000000000000],
  ["kingdom_9_lady_5","Menia","Menia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000012308000d3965a64d1b49d9a400000000001d96d40000000000000000],

  ["kingdom_10_lady_1","Edeltraud","Edeltraud",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000dc3082006090a4a44b411cd5a00000000001e2aa50000000000000000],
  ["kingdom_10_lady_2","Frederika","Frederika",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000fd70450092ca69236b489b71b00000000001eb6e30000000000000000],
  ["kingdom_10_lady_3","Elva","Elva",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10,  [    itm_peasant_dress, itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001010300c389a6eeae457c48a00000000001e151a0000000000000000],
  ["kingdom_10_lady_4","Helmgard","Helmgard",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10,  [    itm_peasant_dress,  itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000003c110100242e57ac3796eeac300000000001d44ed0000000000000000],
  ["kingdom_10_lady_5","Engla","Engla",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000070c200c24e0c6c702c9b16300000000001dc55c0000000000000000],

  ["kingdom_11_lady_1","Rautgundis","Rautgundis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000c0504200a4c948ecb23294a6300000000001db5240000000000000000],
  ["kingdom_11_lady_2","Gosvintha","Gosvintha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000fb700400558e54fc95c91ea9d00000000000e67260000000000000000],
  ["kingdom_11_lady_3","Matasvintha","Matasvintha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11,  [    itm_peasant_dress, itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002b04200e32ddd1d726725ae300000000000d48950000000000000000],
  ["kingdom_11_lady_4","Hermesind","Hermesind",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11,  [    itm_peasant_dress,  itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000404500a2af46cb56151a75d00000000001e42bd0000000000000000],
  ["kingdom_11_lady_5","Amalasontha","Amalasontha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000014708201238622998cc6d48d200000000001e42650000000000000000],

  ["kingdom_12_lady_1","Aethelthryth","Aethelthryth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [      itm_brown_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000fee045009452532bb645736dc000000000005b2db0000000000000000],
  ["kingdom_12_lady_2","Wassa","Wassa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [      itm_green_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000fc50c000459223232b373330c000000000012479b0000000000000000],
  ["kingdom_12_lady_3","Aelfthryth","Aelfthryth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_red_dress ,     itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0850041b26abeb6570b252000000000019c92d0000000000000000],
  ["kingdom_12_lady_4","Aethelflaed","Aethelflaed",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12,  [    itm_red_dress ,     itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001110100154e432252a66c79900000000001f23a30000000000000000],
  ["kingdom_12_lady_5","Godiva","Godiva",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [      itm_green_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000210410043b5d6d38a256391c0000000000113ae20000000000000000],

  #wife of Cunedda
  ["kingdom_13_lady_1","Gwawl","Gwawl",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13, [      itm_roman_noble_dress_2 ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000fe10000015aabb236dbb1b6db00000000001ed8dc0000000000000000],
  #daughters of Cunedda, older 1, younger one
  ["kingdom_13_lady_2","Gwen","Gwen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13, [      itm_lady_dress_ruby ,   itm_ankle_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000038a001003291b4a3b6b6db6db00000000001d46da0000000000000000],
  ["kingdom_13_lady_3","Tegeingl","Tegeingl",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13,  [    itm_dress_4, itm_ankle_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000002009465291155485b6ec00000000001d655b0000000000000000],
  #daughters of Pepianus, one older, one younger
  ["kingdom_13_lady_4","Efrddyl","Efrddyl",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13,  [    itm_roman_noble_dress_sleeveless_3,  itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000021f0450074723444f4c22379c00000000001e96f40000000000000000],
  ["kingdom_13_lady_5","Cadwy","Cadwy",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13, [      itm_roman_noble_dress_3 ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001c00300a189491a15ca228e400000000001d55430000000000000000],

  ["kingdom_14_lady_1","Gisa","Gisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008910c00024a545aa93371450c00000000001cc6e20000000000000000],
  ["kingdom_14_lady_2","Blandia","Blandia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000fe30c50011925725ad44c471e00000000000cd8cd0000000000000000],
  ["kingdom_14_lady_3","Clovia","Clovia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14,  [    itm_peasant_dress, itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000044004551d35971471ba8c00000000001e59360000000000000000],

  ["kingdom_15_lady_1","Eudocia","Eudocia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15, [ itm_dress_4, itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002e10200107632d675a92b8ad00000000001e45620000000000000000],
  ["kingdom_15_lady_2","Bruttia","Bruttia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15, [itm_dress_6, itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_15_lady_3","Matonia","Matonia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15,  [itm_dress_5, itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000fff0010037735722af555c8e300000000001fc82c0000000000000000],
  ["kingdom_15_lady_4","Lorelei","Lorelei",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15,  [itm_dress_5, itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131c58d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_15_lady_5","Feenja","Feenja",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15, [itm_dress_6,  itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000004005007476b6ad6448ee71d00000000001db90b0000000000000000],
  ["kingdom_15_lady_6","Talida","Talida",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15, [itm_dress_4, itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_15_lady_7","Gailesvintha","Gailesvintha",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15, [ itm_dress_4,  itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019f002007269a6d14da49a6d400000000001d435b0000000000000000],
  ["kingdom_15_lady_8","Algonda","Algonda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15, [ itm_dress_8, itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002610400a495b5636e4693414000000000015b8da0000000000000000],

  ["kingdom_16_lady_1","Salome","Salome",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_16, [      itm_brown_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000ff600700d3a6256850a2e68db00000000001ca5220000000000000000],
  ["kingdom_16_lady_2","Tsiuri","Tsiuri",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_16, [      itm_green_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000009bf0c3005671a30b0ab4e270c00000000001e189c0000000000000000],
  ["kingdom_16_lady_3","Abeshura","Abeshura",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_16, [itm_red_dress ,     itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000330010111526cc31216c1ae400000000001f36b90000000000000000],
  ["kingdom_16_lady_4","Balendukht","Balendukht",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_16,  [    itm_red_dress ,     itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001b007004485b6d9b2bcd371a00000000001d54d20000000000000000],
  ["kingdom_16_lady_5","Shushanik","Shushanik",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_16, [      itm_green_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003800100336db4db6db8d36db00000000001d36ca0000000000000000],
  ["kingdom_16_lady_6","Ketevan","Ketevan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_16, [      itm_green_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003f082003650dadc49692396300000000001e57a40000000000000000],

  ["kingdom_17_lady_1","Gogilli","Gogilli",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000c8808000a2ad9d5aa8c70b91a0000000000113adb0000000000000000],
  ["kingdom_17_lady_2","Rotilda","Rotilda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000070000300c36a38e252b88b8a200000000001ea9990000000000000000],
  ["kingdom_17_lady_3","Adelinda","Adelinda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17,  [    itm_peasant_dress, itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000c8008200b14b43ed53411c92a00000000001d49140000000000000000],
  ["kingdom_17_lady_4","Ansobrida","Ansobrida",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17,  [    itm_peasant_dress,  itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008400d1b5cb5e3289516db00000000001d471a0000000000000000],
  ["kingdom_17_lady_5","Tederona","Tederona",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000110000456da53071b8536a400000000001dc6990000000000000000],

  ["kingdom_18_lady_1","Mansuara","Mansuara",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000009dc085001444355c91aa7b4d4000000000014c4a60000000000000000],
  ["kingdom_18_lady_2","Fremosilli","Fremosilli",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000fef04400156d49355142a9ccb00000000001ec8ad0000000000000000],
  ["kingdom_18_lady_3","Senderiga","Senderiga",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18,  [    itm_peasant_dress, itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000051c04500768a96ae88bca531c00000000001d9b940000000000000000],
  ["kingdom_18_lady_4","Saruilli","Saruilli",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18,  [    itm_peasant_dress,  itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002c0840022b5d91b32b511acd00000000001f294d0000000000000000],
  ["kingdom_18_lady_5","Alobrida","Alobrida",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000210c300d257b75dadd8db92b00000000001db90e0000000000000000],

  ["kingdom_19_lady_1","Waerhild","Waerhild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_19, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000d050040031973d8a92e34caed00000000001cb51b0000000000000000],
  ["kingdom_19_lady_2","Hounilda","Hounilda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_19, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000fc800100842ea91b99b85c08b00000000001e16dd0000000000000000],
  ["kingdom_19_lady_3","Eaba","Eaba",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_19,  [    itm_peasant_dress, itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000003d50c400d250990d21c4ac65e00000000001e53210000000000000000],
  ["kingdom_19_lady_4","Erkengota","Erkengota",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_19,  [    itm_peasant_dress,  itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002b100004375d09c6636e585300000000000957540000000000000000],
  ["kingdom_19_lady_5","Osgyth","Osgyth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_19, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001050020043a6e4dc5936b2cea00000000001cc9240000000000000000],

  ["kingdom_20_lady_1","Theodelinde","Theodelinde",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20, [itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000121040062a89cecad27726eb00000000001dc92a0000000000000000],
  ["kingdom_20_lady_2","Adela","Adela",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20, [      itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000d91002001290ada352265c59c00000000001ed4a20000000000000000],
  ["kingdom_20_lady_3","Wavin","Wavin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20,  [    itm_peasant_dress, itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000068408200c48e3b0d5e376acd300000000001cc55d0000000000000000],
  ["kingdom_20_lady_4","Ideswif","Ideswif",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20,  [    itm_peasant_dress,  itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000026108500a68936ed72c8755630000000000011c9c0000000000000000],
  ["kingdom_20_lady_5","Olburgis","Olburgis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20,  [    itm_peasant_dress,  itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000f10400c17246e28cc9394a100000000001e36b30000000000000000],

  ["kingdom_21_lady_1","Sunigilda","Sunigilda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_21, [itm_court_dress ,   itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000420c300a552c6a22a58db4e300000000001d364c0000000000000000],

  ["kingdom_22_lady_1","Comitessa Leocadia","Leocadia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [      itm_brown_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000df20070013ae92db7746db6db00000000001db56b0000000000000000],
  ["kingdom_22_lady_2","Comitessa Talmudia","Talmudia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [      itm_green_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000083f00700238d36db6db6db6db00000000001db6db0000000000000000],
  ["kingdom_22_lady_3","Comitessa Nepia","Nepia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [itm_red_dress ,     itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000004f4000006254b474d18694cdc00000000001d485b0000000000000000],
  ["kingdom_22_lady_4","Comitessa Carvilia","Eutropia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22,  [    itm_red_dress ,     itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000340c50063a4a534494d648f400000000001fc7710000000000000000],
  ["kingdom_22_lady_5","Comitessa Papiria","Papiria",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [      itm_green_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002708700b569a49a50c70a66300000000001e545c0000000000000000],

  ["kingdom_23_lady_1","Nikara","Nikara",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [      itm_brown_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000097f00600113dd6e27fc49369200000000001ca34a0000000000000000],
  ["kingdom_23_lady_2","Ell","Ell",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [      itm_green_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000e330870073da58a46b38e632e00000000001d52990000000000000000],
  ["kingdom_23_lady_3","Sifka","Sifka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [itm_red_dress ,     itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000fff00700b13d54d27fc49369200000000001eb2e20000000000000000],
  ["kingdom_23_lady_4","Rika","Rika",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23,  [    itm_red_dress ,     itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002ff0c60033bdc967ffc46391c00000000001eb4cb0000000000000000],
  ["kingdom_23_lady_5","Kreka","Kreka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [      itm_green_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006ba0c700a65dc967ffc46391c00000000001eb4db0000000000000000],
  ["kingdom_23_lady_6","Carkota","Carkota",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [      itm_green_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000017a0c70073b5c9127fc0e272300000000001eb56b0000000000000000],
  ["kingdom_23_lady_7","Emese","Emese",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23,  [    itm_brown_dress,     itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002e0c70076adab1a69fa156da00000000001e57850000000000000000],
  ["kingdom_23_lady_8","Amalindis","Amalindis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23,  [    itm_brown_dress ,     itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a101002194265b8e3b0c4ec00000000001dc5130000000000000000],

  ["kingdom_24_lady_1","Tamar","Tamar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [      itm_brown_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000ffc08000d56cc55a87471a35b00000000001eb7220000000000000000],
  ["kingdom_24_lady_2","Elene","Elene",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [      itm_green_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000cbf00200c3b1f5226a395c96300000000001d32d40000000000000000],
  ["kingdom_24_lady_3","Makvala","Makvala",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [itm_red_dress ,     itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000003be08100e56958662f39158e100000000001ebb340000000000000000],
  ["kingdom_24_lady_4","Gulisa","Gulisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24,  [    itm_red_dress ,     itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003f00500d5adc462893c934a500000000001d39a40000000000000000],
  ["kingdom_24_lady_5","Rusudani","Rusudani",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [      itm_green_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003f08001042da6d271899a66b00000000001d435c0000000000000000],

  ["kingdom_25_lady_1","Appa","Appa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_25, [      itm_brown_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000cff0080021692765c9151a6db00000000001d25530000000000000000],
  ["kingdom_25_lady_2","Nulwa","Nulwa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_25, [      itm_green_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008bf0080031692aa5c915196db00000000001d25530000000000000000],
  ["kingdom_25_lady_3","Duwana","Duwana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_25, [itm_red_dress ,     itm_nomad_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003f0080043459715d11b1992300000000001cb5930000000000000000],

  ["kingdom_26_lady_1","Lahideamani","Lahideamani",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_26, [      itm_brown_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000037f0080031692765c915196db00000000001d25530000000000000000],

  ["kingdom_27_lady_1","Maiosara","Maiosara",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_27, [      itm_brown_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000fd3103008372d95c65169ac63000000000012c3180000000000000000],
  ["kingdom_27_lady_2","Alda","Alda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_27, [      itm_green_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000ca70c500b051a4aea6379b85900000000000cc6e30000000000000000],
  ["kingdom_27_lady_3","Amage","Amage",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_27, [itm_red_dress ,     itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000045c08300e192a52a5245ec66400000000001cd56e0000000000000000],
  ["kingdom_27_lady_4","Storena","Storena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_27,  [    itm_red_dress ,     itm_wrapping_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000200c500b1ab74d389672459200000000001ea34e0000000000000000],
  ["kingdom_27_lady_5","Borena","Borena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_27, [      itm_green_dress,       itm_wrapping_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000006080003276495b3256d3ce200000000001cb11b0000000000000000],

  ["heroes_end", "{!}heroes end", "{!}heroes end", tf_hero, 0,reserved,  fac_neutral,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],
#Merchants                                                                              AT                      SILAH                   ZIRH                        BOT                         Head_wear

#Seneschals
  ["town_1_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_2_seneschal", "{!}Town 2 Seneschal", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["town_3_seneschal", "{!}Town 3 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["town_4_seneschal", "{!}Town 4 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["town_5_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000249101e7898999ac54c6],
  ["town_6_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["town_7_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000018101f9487aa831dce4],
  ["town_8_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["town_9_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["town_10_seneschal", "{!}Town 10 Seneschal", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000010230c01ef41badb50465e],
  ["town_11_seneschal", "{!}Town 11 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["town_12_seneschal", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["town_13_seneschal", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["town_14_seneschal", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_15_seneschal", "{!}Town 15 Seneschal", "{!}Town 15 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_16_seneschal", "{!}Town 16 Seneschal", "{!}Town 16 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_17_seneschal", "{!}Town 17 Seneschal", "{!}Town 17 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_18_seneschal", "{!}Town 18 Seneschal", "{!}Town 18 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_19_seneschal", "{!}Town 19 Seneschal", "{!}Town 19 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_20_seneschal", "{!}Town 20 Seneschal", "{!}Town 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_21_seneschal", "{!}Town 21 Seneschal", "{!}Town 21 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_22_seneschal", "{!}Town 22 Seneschal", "{!}Town 22 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_23_seneschal", "{!}Town 23 Seneschal", "{!}Town 23 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_24_seneschal", "{!}Town 24 Seneschal", "{!}Town 24 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_25_seneschal", "{!}Town 25 Seneschal", "{!}Town 25 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_26_seneschal", "{!}Town 26 Seneschal", "{!}Town 26 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_27_seneschal", "{!}Town 27 Seneschal", "{!}Town 27 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_28_seneschal", "{!}Town 28 Seneschal", "{!}Town 27 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_29_seneschal", "{!}Town 29 Seneschal", "{!}Town 27 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_30_seneschal", "{!}Town 30 Seneschal", "{!}Town 27 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_31_seneschal", "{!}Town 31 Seneschal", "{!}Town 27 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_32_seneschal", "{!}Town 32 Seneschal", "{!}Town 27 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_33_seneschal", "{!}Town 33 Seneschal", "{!}Town 27 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_34_seneschal", "{!}Town 34 Seneschal", "{!}Town 34 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_35_seneschal", "{!}Town 35 Seneschal", "{!}Town 34 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_36_seneschal", "{!}Town 36 Seneschal", "{!}Town 34 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_37_seneschal", "{!}Town 37 Seneschal", "{!}Town 34 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_38_seneschal", "{!}Town 38 Seneschal", "{!}Town 34 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_39_seneschal", "{!}Town 39 Seneschal", "{!}Town 34 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_40_seneschal", "{!}Town 40 Seneschal", "{!}Town 34 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_41_seneschal", "{!}Town 41 Seneschal", "{!}Town 34 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_42_seneschal", "{!}Town 42 Seneschal", "{!}Town 34 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_43_seneschal", "{!}Town 43 Seneschal", "{!}Town 34 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_44_seneschal", "{!}Town 43 Seneschal", "{!}Town 34 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_linen_tunic,      itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],


  ["castle_1_seneschal", "{!}Castle 1 Seneschal", "{!}Castle 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["castle_2_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_3_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_4_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_5_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_6_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_7_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_8_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_9_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_10_seneschal", "{!}Castle 10 Seneschal", "{!}Castle 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_11_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_12_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_13_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_14_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_15_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_16_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_17_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_18_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_19_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_20_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_21_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_22_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_23_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_24_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_25_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_26_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_27_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_28_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_29_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_30_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_31_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_32_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_33_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_34_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_35_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_36_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_37_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_38_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_39_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_40_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_41_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_42_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_43_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_44_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_45_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_46_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_47_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_48_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_49_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_50_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_51_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_52_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_53_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_54_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_55_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_56_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_57_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_58_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_59_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_60_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_61_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_62_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_63_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_64_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_65_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_66_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_67_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_68_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_69_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_70_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_71_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_72_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_73_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_74_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_75_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_76_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_77_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_78_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_79_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_80_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_81_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_82_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_83_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_84_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_85_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_86_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],

#Arena Masters
  ["town_1_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_1_arena|entry(52),reserved,   fac_commoners,[itm_generic_tunic_5,      itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_2_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_2_arena|entry(52),reserved,   fac_commoners,[itm_generic_tunic_1,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_3_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_3_arena|entry(52),reserved,   fac_commoners,[itm_generic_tunic_3,       itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_4_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_4_arena|entry(52),reserved,   fac_commoners,[itm_kaftan_tunic_2,      itm_sassanid_simple_boots_1],    def_attrib|level(2),wp(20),knows_common,persian_face_1, persian_face_2],
  ["town_5_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_5_arena|entry(52),reserved,   fac_commoners,[itm_roman_shirt_9,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_6_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_6_arena|entry(52),reserved,   fac_commoners,[itm_roman_shirt_12,    itm_roman_lorum_fasciari_3], def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_7_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_7_arena|entry(52),reserved,   fac_commoners,[itm_roman_shirt_10,    itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_8_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_8_arena|entry(52),reserved,   fac_commoners,[itm_roman_shirt_2,       itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_9_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_9_arena|entry(52),reserved,   fac_commoners,[itm_roman_shirt_8,    itm_wrapping_boots], def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_10_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_10_arena|entry(52),reserved,  fac_commoners,[itm_roman_shirt_5,       itm_roman_lorum_fasciari_1],   def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_11_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_11_arena|entry(52),reserved,  fac_commoners,[itm_roman_shirt_2,      itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_12_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_12_arena|entry(52),reserved,  fac_commoners,[itm_generic_tunic_15,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_13_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_13_arena|entry(52),reserved,  fac_commoners,[itm_roman_shirt_14,      itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_14_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_14_arena|entry(52),reserved,  fac_commoners,[itm_generic_tunic_10,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_15_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_15_arena|entry(52),reserved,  fac_commoners,[itm_roman_shirt_3,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_16_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_16_arena|entry(52),reserved,  fac_commoners,[itm_roman_shirt_4,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_17_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_17_arena|entry(52),reserved,  fac_commoners,[itm_generic_tunic_8,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_18_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_18_arena|entry(52),reserved,  fac_commoners,[itm_roman_shirt_6,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_19_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_19_arena|entry(52),reserved,  fac_commoners,[itm_kaftan_tunic_9,   itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_20_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_20_arena|entry(52),reserved,  fac_commoners,[itm_kaftan_tunic_6,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_21_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_21_arena|entry(52),reserved,  fac_commoners,[itm_roman_shirt_2,    itm_roman_lorum_fasciari_2],    def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_22_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_22_arena|entry(52),reserved,  fac_commoners,[itm_roman_shirt_5,    itm_ankle_boots],    def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_23_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_23_arena|entry(52),reserved,   fac_commoners,[itm_generic_tunic_14,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_24_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_24_arena|entry(52),reserved,   fac_commoners,[itm_roman_shirt_3,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_25_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_25_arena|entry(52),reserved,   fac_commoners,[itm_roman_shirt_5,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_26_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_26_arena|entry(52),reserved,   fac_commoners,[itm_kaftan_tunic_4,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,persian_face_1, persian_face_2],
  ["town_27_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_27_arena|entry(52),reserved,   fac_commoners,[itm_roman_shirt_3,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_28_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_28_arena|entry(52),reserved,   fac_commoners,[itm_kaftan_tunic_3,       itm_sassanid_simple_boots_1],   def_attrib|level(2),wp(20),knows_common,persian_face_1, persian_face_2],
  ["town_29_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_29_arena|entry(52),reserved,   fac_commoners,[itm_linen_shirt_8,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_30_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_30_arena|entry(52),reserved,   fac_commoners,[itm_linen_shirt_7,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_31_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_31_arena|entry(52),reserved,   fac_commoners,[itm_linen_shirt_14,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_32_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_32_arena|entry(52),reserved,   fac_commoners,[itm_linen_shirt_20,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_33_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_33_arena|entry(52),reserved,   fac_commoners,[itm_roman_shirt_10,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_34_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_34_arena|entry(52),reserved,   fac_commoners,[itm_roman_shirt_5,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,mauri_face_1, mauri_face_2],
  ["town_35_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_35_arena|entry(52),reserved,   fac_commoners,[itm_generic_tunic_12,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_36_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_36_arena|entry(52),reserved,   fac_commoners,[itm_roman_shirt_3,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_37_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_37_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_38_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_38_arena|entry(52),reserved,   fac_commoners,[itm_roman_shirt_8,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_39_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_39_arena|entry(52),reserved,   fac_commoners,[itm_roman_shirt_2,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_40_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_40_arena|entry(52),reserved,   fac_commoners,[itm_roman_shirt_10,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_41_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_41_arena|entry(52),reserved,   fac_commoners,[itm_roman_shirt_10,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,man_face_1, man_face_2],
  ["town_42_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_42_arena|entry(52),reserved,   fac_commoners,[itm_linen_shirt_1,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,nubian_face_1, nubian_face_2],
  ["town_43_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_43_arena|entry(52),reserved,   fac_commoners,[itm_steppe_kaftan_1,       itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,sarmatian_face_1, sarmatian_face_2],
  ["town_44_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_44_arena|entry(52),reserved,   fac_commoners,[itm_steppe_kaftan_3,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,sarmatian_face_1, sarmatian_face_2],

# Armor Merchants
  #arena_masters_end = zendar_armorer

  ["town_1_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_wrapping_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_2_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_shirt_20,          itm_wrapping_boots       ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_3_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_generic_tunic_14,        itm_wrapping_boots      ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_4_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_kaftan_sheepskin_1,         itm_sassanid_simple_boots_1   ],def_attrib|level(5),wp(20),knows_inventory_management_10, persian_face_1, persian_face_2],
  ["town_5_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,          itm_ankle_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_6_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_12,       itm_roman_lorum_fasciari_2     ],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_7_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_2,       itm_roman_lorum_fasciari_4       ],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_8_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_12,       itm_roman_lorum_fasciari_3   ],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_9_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_8,        itm_wrapping_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_10_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_5,       itm_wrapping_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_11_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_10,        itm_khergit_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_12_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_generic_tunic_8,         itm_khergit_leather_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_13_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_6,       itm_roman_lorum_fasciari_1     ],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_14_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_generic_tunic_10,         itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_15_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_1,        itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_16_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_2,         itm_roman_lorum_fasciari_4,itm_pannonian_cap_fur_2],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_17_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_10,       itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_18_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_3,         itm_roman_lorum_fasciari_2],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_19_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_kaftan_tunic_1,        itm_leather_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, persian_face_1, persian_face_2],
  ["town_20_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_kaftan_tunic_4,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, persian_face_1, persian_face_2],
  ["town_21_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_roman_military_tunic_3,       itm_roman_lorum_fasciari_4,itm_pannonian_cap_fur_1],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_22_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_roman_military_tunic_1,         itm_roman_lorum_fasciari_3,itm_pannonian_cap_5       ],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_23_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_generic_tunic_5,           itm_wrapping_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_24_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_falkirk_tunic_3,           itm_roman_lorum_fasciari_1   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_25_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_generic_tunic_3,           itm_wrapping_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_26_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_kaftan_sheepskin_2,           itm_wrapping_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, persian_face_1, persian_face_2],
  ["town_27_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_kaftan_tunic_10,           itm_khergit_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, persian_face_1, persian_face_2],
  ["town_28_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_kaftan_tunic_3,           itm_nomad_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, persian_face_1, persian_face_2],
  ["town_29_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_generic_tunic_1,           itm_ankle_boots ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_30_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_generic_tunic_6,           itm_ankle_boots ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_31_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_generic_tunic_2,           itm_ankle_boots ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_32_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_generic_tunic_15,           itm_ankle_boots ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_33_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_1,           itm_ankle_boots ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_34_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_10,           itm_ankle_boots ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_35_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_4,           itm_ankle_boots ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_36_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_2,           itm_ankle_boots ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_37_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_kaftan_sheepskin_3,           itm_ankle_boots ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_38_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_12,           itm_roman_lorum_fasciari_1 ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_39_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_10,           itm_ankle_boots ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_40_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_10,           itm_ankle_boots ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_41_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_8,           itm_ankle_boots ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_42_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_simple_tunic_1,           itm_ankle_boots ],def_attrib|level(2),wp(20),knows_inventory_management_10, nubian_face_1, nubian_face_2],
  ["town_43_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_kaftan_alan_green,          itm_wrapping_boots ],def_attrib|level(2),wp(20),knows_inventory_management_10, sarmatian_face_1, sarmatian_face_2],
  ["town_44_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_kaftan_alan_1,          itm_khergit_leather_boots ],def_attrib|level(2),wp(20),knows_inventory_management_10, hunnic_face_1, hunnic_face_2],

# Weapon merchants

  ["town_1_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_shirt_10,itm_wrapping_boots,itm_woolen_cap_6],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_2_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_falkirk_tunic_2,itm_wrapping_boots,itm_brown_hood1],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_3_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_generic_tunic_15,   itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_4_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_kaftan_tunic_9,     itm_sassanid_simple_boots_1],def_attrib|level(5),wp(20),knows_inventory_management_10, persian_face_1, persian_face_2],
  ["town_5_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_5,   itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_6_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_12,itm_roman_lorum_fasciari_4,itm_pannonian_cap_fur_2],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_7_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_8,itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_8_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_2,itm_roman_lorum_fasciari_1,itm_pannonian_cap_fur_1],def_attrib|level(5),wp(20),knows_inventory_management_10, roman_face_1, roman_face_2],
  ["town_9_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_3,   itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_10_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_2,     itm_roman_lorum_fasciari_4,itm_pannonian_cap_fur_2],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_11_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_1,  itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_12_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_generic_tunic_10,itm_wrapping_boots,itm_woolen_cap_5],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_13_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_10,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_14_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_generic_tunic_14,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_15_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_generic_tunic_8,  itm_roman_lorum_fasciari_4],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_16_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_7,           itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_17_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_roman_military_tunic_7,     itm_roman_lorum_fasciari_2,itm_woolen_cap_8],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_18_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_falkirk_tunic_4,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_19_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_kaftan_sheepskin_1,  itm_sassanid_cavalry_boots_2],def_attrib|level(5),wp(20),knows_inventory_management_10, persian_face_1, persian_face_2],
  ["town_20_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_kaftan_tunic_2,        itm_sassanid_cavalry_boots_1],def_attrib|level(5),wp(20),knows_inventory_management_10, persian_face_1, persian_face_2],
  ["town_21_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_4,itm_roman_lorum_fasciari_3,itm_pannonian_cap_1],def_attrib|level(5),wp(20),knows_inventory_management_10, coptic_face_1, coptic_face_2],
  ["town_22_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_10,itm_roman_lorum_fasciari_1],def_attrib|level(5),wp(20),knows_inventory_management_10, persian_face_1, persian_face_2],
  ["town_23_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_generic_tunic_15,      itm_wrapping_boots,itm_pannonian_cap_fur_1],def_attrib|level(2),wp(20),knows_inventory_management_10, germanic_face_1, germanic_face_2],
  ["town_24_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_cloaked_tunic_falkirk_3,itm_roman_lorum_fasciari_2,itm_pannonian_cap_2],def_attrib|level(2),wp(20),knows_inventory_management_10, briton_face_1, briton_face_2],
  ["town_25_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_12,      itm_roman_lorum_fasciari_4,itm_pannonian_cap_fur_1],def_attrib|level(2),wp(20),knows_inventory_management_10, roman_face_1, roman_face_2],
  ["town_26_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_kaftan_sheepskin_4,itm_wrapping_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,  persian_face_1, persian_face_2],
  ["town_27_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,itm_wrapping_boots,itm_woolen_cap_5],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_28_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_kaftan_tunic_7,itm_wrapping_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, persian_face_1, persian_face_2],
  ["town_29_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_generic_tunic_9,itm_wrapping_boots,itm_woolen_cap_1],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_30_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_shirt_1,itm_wrapping_boots,itm_woolen_cap_1],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_31_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_shirt_14,itm_wrapping_boots,itm_woolen_cap_3],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_32_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_shirt_3,itm_wrapping_boots,itm_woolen_cap_6],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_33_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_1,itm_wrapping_boots,itm_woolen_cap_3],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_34_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_2,itm_wrapping_boots,itm_woolen_cap_6],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_35_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_shirt_6,itm_wrapping_boots,itm_woolen_cap_1],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_36_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_shirt_8,itm_wrapping_boots,itm_pannonian_cap_fur_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_37_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_shirt_9,itm_wrapping_boots,itm_woolen_cap_4],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_38_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_10,itm_wrapping_boots,itm_woolen_cap_2],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_39_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_3,itm_wrapping_boots,itm_woolen_cap_4],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_40_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_10,itm_wrapping_boots,itm_woolen_cap_3],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_41_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_4,itm_wrapping_boots,itm_woolen_cap_1],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_42_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_roman_shirt_2,itm_wrapping_boots,itm_woolen_cap_2],def_attrib|level(2),wp(20),knows_inventory_management_10, nubian_face_1, nubian_face_2],
  ["town_43_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_leather_apron,itm_wrapping_boots,itm_hunnic_phrygian_3],def_attrib|level(2),wp(20),knows_inventory_management_10, sarmatian_face_1, sarmatian_face_2],
  ["town_44_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_steppe_kaftan_2,itm_wrapping_boots,itm_hunnic_phrygian_3],def_attrib|level(2),wp(20),knows_inventory_management_10, hunnic_face_1, hunnic_face_2],

#Tavern keepers

  ["town_1_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_1_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["town_2_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_2_tavern|entry(9),0,   fac_commoners,[itm_cloaked_tunic_falkirk_2,itm_leather_boots],def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["town_3_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_3_tavern|entry(9),0,   fac_commoners,[itm_dress_8,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_4_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_4_tavern|entry(9),0,   fac_commoners,[itm_kaftan_tunic_3,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, persian_face_1, persian_face_2],
  ["town_5_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_5_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["town_6_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_6_tavern|entry(9),0,   fac_commoners,[itm_dress_4,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_7_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_7_tavern|entry(9),0,   fac_commoners,[itm_dress_5,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_8_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_8_tavern|entry(9),0,   fac_commoners,[itm_roman_shirt_8,itm_roman_lorum_fasciari_4,itm_pannonian_cap_fur_1],def_attrib|level(2),wp(20),knows_common, roman_face_1, roman_face_2],
  ["town_9_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_9_tavern|entry(9),0,   fac_commoners,[itm_dress_4,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_10_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_10_tavern|entry(9),0,  fac_commoners,[itm_dress_5,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_11_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_11_tavern|entry(9),0,  fac_commoners,[itm_lady_dress_ruby,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_12_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_12_tavern|entry(9),0,  fac_commoners,[itm_generic_tunic_14,itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["town_13_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_13_tavern|entry(9),0,  fac_commoners,[itm_roman_noble_dress_1,itm_roman_lorum_fasciari_4],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_14_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_14_tavern|entry(9),0,  fac_commoners,[itm_generic_tunic_3,itm_roman_lorum_fasciari_4],def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["town_15_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_15_tavern|entry(9),0,  fac_commoners,[itm_roman_noble_dress_3,itm_ankle_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_16_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_16_tavern|entry(9),0,  fac_commoners,[itm_roman_shirt_2,itm_roman_lorum_fasciari_3,itm_pannonian_cap_6],def_attrib|level(2),wp(20),knows_common, roman_face_1, roman_face_2],
  ["town_17_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_17_tavern|entry(9),0,  fac_commoners,[itm_lady_dress_green,itm_roman_lorum_fasciari_1,itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_18_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_18_tavern|entry(9),0,  fac_commoners,[itm_shirt,itm_leather_boots],def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["town_19_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_19_tavern|entry(9),0,  fac_commoners,[itm_sarranid_dress_a,itm_sassanid_simple_boots_1],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_20_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_20_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cloth_robe,itm_sassanid_simple_boots_3],def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["town_21_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_21_tavern|entry(9),0,  fac_commoners,[itm_sarranid_common_dress,itm_roman_lorum_fasciari_2,itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_22_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_22_tavern|entry(9),0,  fac_commoners,[itm_roman_shirt_6,itm_wrapping_boots,itm_headcloth],def_attrib|level(2),wp(20),knows_common, arab_face_1, arab_face_2],
  ["town_23_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_23_tavern|entry(9),0,   fac_commoners,[itm_generic_tunic_10,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["town_24_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_24_tavern|entry(9),0,   fac_commoners,[itm_falkirk_tunic_5,itm_wrapping_boots,itm_pannonian_cap_fur_2],def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["town_25_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_25_tavern|entry(9),0,   fac_commoners,[itm_roman_shirt_1,itm_roman_lorum_fasciari_2,itm_pannonian_cap_5],def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["town_26_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_26_tavern|entry(9),0,   fac_commoners,[itm_kaftan_sheepskin_4,itm_wrapping_boots,itm_woolen_cap_8],def_attrib|level(2),wp(20),knows_common, persian_face_1, persian_face_2],
  ["town_27_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_27_tavern|entry(9),0,   fac_commoners,[itm_roman_shirt_4,itm_wrapping_boots,itm_pannonian_cap_fur_1],def_attrib|level(2),wp(20),knows_common, caucaus_face_1, caucaus_face_2],
  ["town_28_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_28_tavern|entry(9),0,   fac_commoners,[itm_kaftan_tunic_7,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, persian_face_1, persian_face_2],
  ["town_29_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_29_tavern|entry(9),0,   fac_commoners,[itm_generic_tunic_12,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, germanic_face_1, germanic_face_2],
  ["town_30_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_30_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, germanic_face_1, germanic_face_2],
  ["town_31_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_31_tavern|entry(9),0,   fac_commoners,[itm_generic_tunic_9,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, germanic_face_1, germanic_face_2],
  ["town_32_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_32_tavern|entry(9),0,   fac_commoners,[itm_generic_tunic_1,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, germanic_face_1, germanic_face_2],
  ["town_33_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_33_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, germanic_face_1, germanic_face_2],
  ["town_34_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_34_tavern|entry(9),0,   fac_commoners,[itm_roman_shirt_8,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mauri_face_1, mauri_face_2],
  ["town_35_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_35_tavern|entry(9),0,   fac_commoners,[itm_roman_shirt_10,itm_wrapping_boots,itm_woolen_cap_3],def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["town_36_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_36_tavern|entry(9),0,   fac_commoners,[itm_roman_shirt_10,itm_wrapping_boots,itm_woolen_cap_2],def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["town_37_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_37_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, caucaus_face_1, caucaus_face_2],
  ["town_38_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_38_tavern|entry(9),0,   fac_commoners,[itm_roman_shirt_4,itm_wrapping_boots,itm_pannonian_cap_1],def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["town_39_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_39_tavern|entry(9),0,   fac_commoners,[itm_roman_shirt_7,itm_roman_lorum_fasciari_2],def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["town_40_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_40_tavern|entry(9),0,   fac_commoners,[itm_roman_shirt_5,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["town_41_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_41_tavern|entry(9),0,   fac_commoners,[itm_roman_shirt_7,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["town_42_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_42_tavern|entry(9),0,   fac_commoners,[itm_simple_tunic_10,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, nubian_face_1, nubian_face_2],
  ["town_43_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_43_tavern|entry(9),0,   fac_commoners,[itm_kaftan_alan_red,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, sarmatian_face_1, sarmatian_face_2],
  ["town_44_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_44_tavern|entry(9),0,   fac_commoners,[itm_kaftan_hunnic_white,itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, hunnic_face_1, hunnic_face_2],

#Goods Merchants

  ["town_1_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_1_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_wrapping_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_2_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_2_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_wrapping_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_3_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_3_store|entry(9),0, fac_commoners,     [itm_dress_4,       itm_wrapping_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_4_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_4_store|entry(9),0, fac_commoners,     [itm_kaftan_sheepskin_3, itm_wrapping_boots              ],def_attrib|level(2),wp(20),knows_inventory_management_10, persian_face_1, persian_face_2],
  ["town_5_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_5_store|entry(9),0, fac_commoners,     [itm_nomad_armor,   itm_wrapping_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_6_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_6_store|entry(9),0, fac_commoners,     [itm_woolen_dress,  itm_wrapping_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_7_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_7_store|entry(9),0, fac_commoners,     [itm_leather_jerkin,itm_wrapping_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_8_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_8_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_wrapping_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_9_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_9_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_wrapping_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_10_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_10_store|entry(9),0, fac_commoners,    [itm_leather_jerkin,itm_wrapping_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_11_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_11_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_wrapping_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_12_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_12_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_wrapping_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_13_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_13_store|entry(9),0, fac_commoners,    [itm_dress,         itm_wrapping_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_14_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_14_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_wrapping_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_15_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_15_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_wrapping_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_16_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_16_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_wrapping_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_17_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_17_store|entry(9),0, fac_commoners,    [itm_dress,         itm_wrapping_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_18_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_18_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_wrapping_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_19_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_19_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_wrapping_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_20_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_20_store|entry(9),0, fac_commoners,    [itm_sarranid_common_dress_b,  itm_sarranid_boots_a, itm_sarranid_felt_head_cloth_b  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_21_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_21_store|entry(9),0, fac_commoners,    [itm_sarranid_dress_a,         itm_sarranid_boots_a,  itm_sarranid_felt_head_cloth  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_22_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_22_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_wrapping_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_23_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_23_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_wrapping_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_24_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_24_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_wrapping_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_25_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_25_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_wrapping_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_26_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_26_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_wrapping_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_27_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_27_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_wrapping_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_28_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_28_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_wrapping_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_29_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_29_store|entry(9),0, fac_commoners,     [itm_linen_shirt_8, itm_ankle_boots                  ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_30_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_30_store|entry(9),0, fac_commoners,     [itm_linen_shirt_8, itm_ankle_boots                  ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_31_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_31_store|entry(9),0, fac_commoners,     [itm_linen_shirt_8, itm_ankle_boots                  ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_32_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_32_store|entry(9),0, fac_commoners,     [itm_linen_shirt_8, itm_ankle_boots                  ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_33_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_33_store|entry(9),0, fac_commoners,     [itm_linen_shirt_8, itm_ankle_boots                  ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_34_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_34_store|entry(9),0, fac_commoners,     [itm_linen_shirt_8, itm_ankle_boots                  ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_35_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_35_store|entry(9),0, fac_commoners,     [itm_linen_shirt_8, itm_ankle_boots                  ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_36_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_36_store|entry(9),0, fac_commoners,     [itm_linen_shirt_8, itm_ankle_boots                  ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_37_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_37_store|entry(9),0, fac_commoners,     [itm_linen_shirt_8, itm_ankle_boots                  ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_38_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_38_store|entry(9),0, fac_commoners,     [itm_linen_shirt_8, itm_ankle_boots                  ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_39_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_39_store|entry(9),0, fac_commoners,     [itm_linen_shirt_8, itm_ankle_boots                  ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_40_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_40_store|entry(9),0, fac_commoners,     [itm_linen_shirt_8, itm_ankle_boots                  ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_41_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_41_store|entry(9),0, fac_commoners,     [itm_linen_shirt_8, itm_ankle_boots                  ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_42_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_42_store|entry(9),0, fac_commoners,     [itm_linen_shirt, itm_ankle_boots                  ],def_attrib|level(2),wp(20),knows_inventory_management_10, nubian_face_1, nubian_face_2],
  ["town_43_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_43_store|entry(9),0, fac_commoners,     [itm_kaftan_alan_3, itm_ankle_boots                  ],def_attrib|level(2),wp(20),knows_inventory_management_10, sarmatian_face_1, sarmatian_face_2],
  ["town_44_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_44_store|entry(9),0, fac_commoners,     [itm_kaftan_hunnic_1, itm_ankle_boots                  ],def_attrib|level(2),wp(20),knows_inventory_management_10, hunnic_face_1, hunnic_face_2],

  ["salt_mine_merchant","Barezan","Barezan",                tf_hero|tf_is_merchant, scn_salt_mine|entry(1),0, fac_commoners,        [itm_leather_apron, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c528601ea69b6e46dbdb6],

# Horse Merchants

  ["town_1_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_wrapping_boots,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_3_horse_merchant","Horse Merchant","{!}Town 3 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,          itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_4_horse_merchant","Horse Merchant","{!}Town 4 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_5_horse_merchant","Horse Merchant","{!}Town 5 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_dress,                itm_wrapping_boots,    itm_woolen_hood],   def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_6_horse_merchant","Horse Merchant","{!}Town 6 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_7_horse_merchant","Horse Merchant","{!}Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_8_horse_merchant","Horse Merchant","{!}Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_khergit_vest_b,         itm_sassanid_cavalry_boots_1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, hunnic_face_1, hunnic_face_2],
  ["town_9_horse_merchant","Horse Merchant","{!}Town 9 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_wrapping_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_10_horse_merchant","Horse Merchant","{!}Town 10 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_blue_dress,          itm_wrapping_boots,      itm_straw_hat],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_11_horse_merchant","Horse Merchant","{!}Town 11 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_12_horse_merchant","Horse Merchant","{!}Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_13_horse_merchant","Horse Merchant","{!}Town 13 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_14_horse_merchant","Horse Merchant","{!}Town 14 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_wrapping_boots,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_16_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_17_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_18_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_wrapping_boots,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,         itm_sarranid_boots_a],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_20_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_cloth_robe,      itm_sarranid_boots_a],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_21_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_cloth_robe_b,        itm_sarranid_boots_a],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_22_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_sarranid_common_dress_b,       itm_wrapping_boots,      itm_sarranid_felt_head_cloth_b],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_23_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_24_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_25_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_26_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_27_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_28_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_29_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,          itm_wrapping_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_30_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,          itm_wrapping_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_31_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,          itm_wrapping_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_32_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,          itm_wrapping_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_33_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,          itm_wrapping_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_34_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,          itm_wrapping_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_35_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,          itm_wrapping_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_36_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,          itm_wrapping_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_37_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,          itm_wrapping_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_38_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,          itm_wrapping_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_39_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,          itm_wrapping_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_40_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,          itm_wrapping_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_41_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,          itm_wrapping_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["town_42_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,          itm_wrapping_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, nubian_face_1, nubian_face_2],
  ["town_43_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_kaftan_alan_4,itm_sassanid_cavalry_boots_2],                      def_attrib|level(5),wp(20),knows_inventory_management_10, sarmatian_face_1, sarmatian_face_2],
  ["town_44_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_kaftan_hunnic_6,itm_sassanid_cavalry_boots_1],                      def_attrib|level(5),wp(20),knows_inventory_management_10, hunnic_face_1, hunnic_face_2],


#Town Mayors
#Roman towns: itm_roman_shirt_2, itm_roman_shirt_9, itm_roman_shirt_12, itm_roman_shirt_3
#Germanic towns: itm_generic_tunic_2, itm_generic_tunic_4, itm_generic_tunic_9
#Kaftans: itm_kaftan_tunic_7, itm_kaftan_alan_1, itm_kaftan_hunnic_1
#Sassanid: 
  ["town_1_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_generic_tunic_2,itm_wrapping_boots], def_attrib|level(2),wp(20),knows_common, germanic_face_1, germanic_face_2],
  ["town_2_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_generic_tunic_3,itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,  germanic_face_1, germanic_face_2],
  ["town_3_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_generic_tunic_4,itm_wrapping_boots], def_attrib|level(2),wp(20),knows_common,  germanic_face_1, germanic_face_2],
  ["town_4_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kaftan_tunic_7,itm_sassanid_simple_boots_1],     def_attrib|level(2),wp(20),knows_common,  persian_face_1, persian_face_2],
  ["town_5_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_generic_tunic_9,itm_wrapping_boots],   def_attrib|level(2),wp(20),knows_common,  germanic_face_1, germanic_face_2],
  ["town_6_mayor", "Flavius Constantinus", "Flavius Constantinus", tf_hero, 0,reserved,  fac_neutral,[itm_roman_shirt_9,itm_roman_lorum_fasciari_3,itm_pannonian_cap_6],   def_attrib|level(2),wp(20),knows_common,  0x0000000cef005007525a4f58a2713b1a00000000001d36910000000000000000],
  ["town_7_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_roman_shirt_12,itm_roman_lorum_fasciari_1,itm_pannonian_cap_fur_2],   def_attrib|level(2),wp(20),knows_common,  roman_face_1, roman_face_2],
  ["town_8_mayor", "Aemilianus", "Aemilianus", tf_hero, 0,reserved,  fac_neutral,[itm_roman_shirt_2,itm_roman_lorum_fasciari_2,itm_pannonian_cap_5],   def_attrib|level(2),wp(20),knows_common,  0x0000000952006082465a6f58a2713b1a00000000001d289b0000000000000000],
  ["town_9_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_roman_shirt_3,itm_roman_lorum_fasciari_4,itm_pannonian_cap_fur_2], def_attrib|level(2),wp(20),knows_common,  roman_face_1, roman_face_2],
  ["town_10_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_roman_shirt_12,itm_roman_lorum_fasciari_1,itm_pannonian_cap_fur_1],     def_attrib|level(2),wp(20),knows_common,  roman_face_1, roman_face_2],
  ["town_11_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_roman_shirt_6,itm_roman_lorum_fasciari_3],   def_attrib|level(2),wp(20),knows_common,  roman_face_1, roman_face_2],
  ["town_12_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_generic_tunic_12,itm_wrapping_boots,itm_woolen_cap_8], def_attrib|level(2),wp(20),knows_common,  germanic_face_1, germanic_face_2],
  ["town_13_mayor", "Caecina Decius Basilius", "Caecina Decius Basilius", tf_hero, 0,reserved,  fac_neutral,[itm_roman_shirt_2,itm_roman_lorum_fasciari_2,itm_pannonian_cap_3],   def_attrib|level(2),wp(20),knows_common,  0x00000008ff000006525a9638a27134db00000000001cb6910000000000000000],
  ["town_14_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_generic_tunic_1,itm_wrapping_boots,itm_woolen_cap_6],     def_attrib|level(2),wp(20),knows_common,  germanic_face_1, germanic_face_2],
  ["town_15_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_roman_shirt_3,itm_roman_lorum_fasciari_4,itm_woolen_cap_b],   def_attrib|level(2),wp(20),knows_common,  roman_face_1, roman_face_2],
  ["town_16_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_roman_shirt_9,itm_roman_lorum_fasciari_1,itm_woolen_cap_2], def_attrib|level(2),wp(20),knows_common,  roman_face_1, roman_face_2],
  ["town_17_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_roman_shirt_9,itm_wrapping_boots,itm_woolen_cap_3],   def_attrib|level(2),wp(20),knows_common,  roman_face_1, roman_face_2],
  ["town_18_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_roman_shirt_6,itm_roman_lorum_fasciari_3,itm_pannonian_cap_fur_1],     def_attrib|level(2),wp(20),knows_common,  roman_face_1, roman_face_2],
  ["town_19_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sassanid_rich_tunic_1,itm_sassanid_cavalry_boots_1],   def_attrib|level(2),wp(20),knows_common,  persian_face_1, persian_face_2],
  ["town_20_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sassanid_rich_tunic_2,itm_sassanid_cavalry_boots_2], def_attrib|level(2),wp(20),knows_common,  persian_face_1, persian_face_2],
  ["town_21_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_roman_shirt_9,itm_roman_lorum_fasciari_4,itm_pannonian_cap_2],   def_attrib|level(2),wp(20),knows_common,  roman_face_1, roman_face_2],
  ["town_22_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_arabian_tunic_1,itm_roman_lorum_fasciari_2,itm_pannonian_cap_4],     def_attrib|level(2),wp(20),knows_common,  arab_face_1, arab_face_2],
  ["town_23_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_linen_shirt_3,itm_khergit_leather_boots],     def_attrib|level(2),wp(20),knows_common,  germanic_face_1, germanic_face_2],
  ["town_24_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_falkirk_tunic_1,itm_wrapping_boots,itm_woolen_cap_5],     def_attrib|level(2),wp(20),knows_common,  roman_face_1, roman_face_2],
  ["town_25_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_roman_shirt_2,itm_khergit_leather_boots,itm_pannonian_cap_5],     def_attrib|level(2),wp(20),knows_common,  roman_face_1, roman_face_2],
  ["town_26_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sassanid_rich_tunic_3,itm_sassanid_cavalry_boots_1], def_attrib|level(2),wp(20),knows_common,  persian_face_1, persian_face_2],
  ["town_27_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kaftan_sheepskin_1,itm_nomad_boots],     def_attrib|level(2),wp(20),knows_common,  caucaus_face_1, caucaus_face_2],
  ["town_28_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sassanid_rich_tunic_4,itm_sassanid_cavalry_boots_2], def_attrib|level(2),wp(20),knows_common,  persian_face_1, persian_face_2],
  ["town_29_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_generic_tunic_2,itm_ankle_boots,itm_woolen_cap_1],     def_attrib|level(2),wp(20),knows_common,  germanic_face_1, germanic_face_2],
  ["town_30_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_generic_tunic_4,itm_ankle_boots,itm_woolen_cap_2],     def_attrib|level(2),wp(20),knows_common,  germanic_face_1, germanic_face_2],
  ["town_31_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_generic_tunic_9,itm_wrapping_boots,itm_woolen_cap_3],     def_attrib|level(2),wp(20),knows_common,  germanic_face_1, germanic_face_2],
  ["town_32_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_generic_tunic_5,itm_ankle_boots,itm_woolen_cap_4],     def_attrib|level(2),wp(20),knows_common,  germanic_face_1, germanic_face_2],
  ["town_33_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_generic_tunic_11,itm_ankle_boots,itm_woolen_cap_5],     def_attrib|level(2),wp(20),knows_common,  germanic_face_1, germanic_face_2],
  ["town_34_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_roman_shirt_3,itm_roman_lorum_fasciari_1,itm_pannonian_cap_1],     def_attrib|level(2),wp(20),knows_common,  roman_face_1, roman_face_2],
  ["town_35_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_roman_shirt_12,itm_roman_lorum_fasciari_1,itm_pannonian_cap_2],     def_attrib|level(2),wp(20),knows_common,  roman_face_1, roman_face_2],
  ["town_36_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_roman_shirt_2,itm_roman_lorum_fasciari_1,itm_pannonian_cap_3],     def_attrib|level(2),wp(20),knows_common,  roman_face_1, roman_face_2],
  ["town_37_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_skirmisher_tunic_3,itm_ankle_boots],     def_attrib|level(2),wp(20),knows_common,  caucaus_face_1, caucaus_face_2],
  ["town_38_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_roman_shirt_5,itm_roman_lorum_fasciari_2,itm_pannonian_cap_4],     def_attrib|level(2),wp(20),knows_common,  roman_face_1, roman_face_2],
  ["town_39_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_roman_shirt_7,itm_roman_lorum_fasciari_3,itm_pannonian_cap_5],     def_attrib|level(2),wp(20),knows_common,  roman_face_1, roman_face_2],
  ["town_40_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_roman_shirt_2,itm_roman_lorum_fasciari_4,itm_pannonian_cap_6],     def_attrib|level(2),wp(20),knows_common,  roman_face_1, roman_face_2],
  ["town_41_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_roman_shirt_2,itm_roman_lorum_fasciari_2,itm_pannonian_cap_1],     def_attrib|level(2),wp(20),knows_common,  roman_face_1, roman_face_2],
  ["town_42_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_roman_shirt_9,itm_ankle_boots],     def_attrib|level(2),wp(20),knows_common,  nubian_face_1, nubian_face_2],
  ["town_43_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kaftan_alan_2,itm_ankle_boots,itm_hunnic_phrygian_5],     def_attrib|level(2),wp(20),knows_common,  sarmatian_face_1, sarmatian_face_2],
  ["town_44_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kaftan_hunnic_1,itm_ankle_boots,itm_hunnic_phrygian_5],     def_attrib|level(2),wp(20),knows_common,  hunnic_face_1, hunnic_face_2],


#Village stores
  ["village_1_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_woolen_cap_b],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_1, man_face_2],
  ["village_2_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_3_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_1, man_face_2],
  ["village_4_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_1, man_face_2],
  ["village_5_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_1, man_face_2],
  ["village_6_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_1, man_face_2],
  ["village_7_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_1, man_face_2],
  ["village_8_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_woolen_cap_b],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_1, man_face_2],
  ["village_9_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,         man_face_1, man_face_2],
  ["village_10_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_11_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_1, man_face_2],
  ["village_12_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_1, man_face_2],
  ["village_13_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_1, man_face_2],
  ["village_14_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_15_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_woolen_cap_b],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_1, man_face_2],
  ["village_16_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_17_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_1, man_face_2],
  ["village_18_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_19_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_1, man_face_2],
  ["village_20_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_21_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_1, man_face_2],
  ["village_22_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_1, man_face_2],
  ["village_23_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_woolen_cap_b],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_1, man_face_2],
  ["village_24_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_25_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_1, man_face_2],
  ["village_26_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_1, man_face_2],
  ["village_27_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_woolen_cap_b],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_1, man_face_2],
  ["village_28_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_29_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_1, man_face_2],
  ["village_30_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_1, man_face_2],
  ["village_31_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_1, man_face_2],
  ["village_32_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_33_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_1, man_face_2],
  ["village_34_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_1, man_face_2],
  ["village_35_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_36_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_1, man_face_2],
  ["village_37_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_38_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_1, man_face_2],
  ["village_39_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_1, man_face_2],
  ["village_40_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_41_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_1, man_face_2],
  ["village_42_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_43_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_1, man_face_2],
  ["village_44_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_1, man_face_2],
  ["village_45_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_46_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_1, man_face_2],
  ["village_47_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_48_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_1, man_face_2],
  ["village_49_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_1, man_face_2],
  ["village_50_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_51_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_1, man_face_2],
  ["village_52_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_1, man_face_2],
  ["village_53_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_woolen_cap_b],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_1, man_face_2],
  ["village_54_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_55_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_56_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_57_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_woolen_cap_b],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_58_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_59_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_60_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_61_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_62_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_63_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_woolen_cap_b],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_64_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_65_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_66_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_67_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_woolen_cap_b],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_68_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_69_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_70_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_71_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_72_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_73_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_woolen_cap_b],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_74_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_75_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_76_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_77_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_woolen_cap_b],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_78_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_79_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_80_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_1, man_face_2],
  ["village_81_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_1, man_face_2],
  ["village_82_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_83_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_1, man_face_2],
  ["village_84_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_1, man_face_2],
  ["village_85_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_86_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_1, man_face_2],
  ["village_87_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_88_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_1, man_face_2],
  ["village_89_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_1, man_face_2],
  ["village_90_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_91_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_1, man_face_2],
  ["village_92_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_93_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_1, man_face_2],
  ["village_94_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_1, man_face_2],
  ["village_95_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_96_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_1, man_face_2],
  ["village_97_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_98_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_1, man_face_2],
  ["village_99_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_1, man_face_2],
  ["village_100_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_101_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_1, man_face_2],
  ["village_102_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_103_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_1, man_face_2],
  ["village_104_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_1, man_face_2],
  ["village_105_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_106_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_1, man_face_2],
  ["village_107_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_108_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_1, man_face_2],
  ["village_109_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_1, man_face_2],
  ["village_110_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_111_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_112_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_113_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_114_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_115_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_116_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_117_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_118_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_119_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_120_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_121_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_122_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_123_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_124_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_125_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_126_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_127_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_128_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_129_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_130_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_131_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_132_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_133_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_134_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_135_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_136_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_137_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_138_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_139_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_140_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_141_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_142_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_143_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_144_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_145_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_146_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_147_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_148_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_149_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_150_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_151_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],

  ["village_152_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_153_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_154_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_155_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_156_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_157_elder","Swarta", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_158_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_159_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_160_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_161_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_162_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_163_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_164_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_165_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_166_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_167_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_168_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_169_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_170_elder","Village_Elder", "{!}special npc",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_yellow_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_171_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_172_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_173_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_174_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_175_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_roman_shirt_8, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_176_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_177_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_178_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_179_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_180_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_181_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_182_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_183_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_184_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_185_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_186_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_187_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_188_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_189_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_190_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_191_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_192_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_193_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_194_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_195_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_196_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_197_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_198_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_199_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_200_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_201_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_202_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_203_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_204_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_205_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_206_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_207_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_208_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_209_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_210_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_211_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_212_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_213_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_214_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_215_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_216_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_217_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_218_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_219_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_220_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_221_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_222_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_223_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_224_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_225_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_226_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_227_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_228_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],

  ["village_229_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_230_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_231_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_232_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_233_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_234_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_235_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_236_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_237_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_238_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_239_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],

  ["village_240_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_241_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_242_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_243_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_244_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_245_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_246_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_247_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_248_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_249_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],
  ["village_250_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_1, man_face_2],

  ["village_251_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              nubian_face_1, nubian_face_2],
  ["village_252_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              nubian_face_1, nubian_face_2],
  ["village_253_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              nubian_face_1, nubian_face_2],
  ["village_254_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              nubian_face_1, nubian_face_2],
  ["village_255_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              nubian_face_1, nubian_face_2],
  ["village_256_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              nubian_face_1, nubian_face_2],

  ["village_257_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              sarmatian_face_1, sarmatian_face_2],
  ["village_258_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              sarmatian_face_1, sarmatian_face_2],
  ["village_259_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              sarmatian_face_1, sarmatian_face_2],
  ["village_260_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              sarmatian_face_1, sarmatian_face_2],
  ["village_261_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              sarmatian_face_1, sarmatian_face_2],
  ["village_262_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              sarmatian_face_1, sarmatian_face_2],
  ["village_263_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              sarmatian_face_1, sarmatian_face_2],


# Place extra merchants before this point
  ["merchants_end","merchants_end","merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

  #Used for player enterprises
  ["town_1_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_2_master_craftsman", "{!}Town 2 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x0000000f010811c92d3295e46a96c72300000000001f5a980000000000000000],
  ["town_3_master_craftsman", "{!}Town 3 Craftsman", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000001b083203151d2ad5648e52b400000000001b172e0000000000000000],
  ["town_4_master_craftsman", "{!}Town 4 Craftsman", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001a10114f091b2c259cd4c92300000000000228dd0000000000000000],
  ["town_5_master_craftsman", "{!}Town 5 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000d1044c578598cd92b5256db00000000001f23340000000000000000],
  ["town_6_master_craftsman", "{!}Town 6 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000001f046285493eaf1b048abcdb00000000001a8aad0000000000000000],
  ["town_7_master_craftsman", "{!}Town 7 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000002b0052c34c549225619356d400000000001cc6e60000000000000000],
  ["town_8_master_craftsman", "{!}Town 8 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x0000000fdb0c20465b6e51e8a12c82d400000000001e148c0000000000000000],
  ["town_9_master_craftsman", "{!}Town 9 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009f7005246071db236e296a45300000000001a8b0a0000000000000000],
  ["town_10_master_craftsman", "{!}Town 10 Craftsman", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000009f71012c2456a921aa379321a000000000012c6d90000000000000000],
  ["town_11_master_craftsman", "{!}Town 11 Craftsman", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000009f308514428db71b9ad70b72400000000001dc9140000000000000000],
  ["town_12_master_craftsman", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009e90825863853a5b91cd71a5b00000000000598db0000000000000000],
  ["town_13_master_craftsman", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000009fa0c708f274c8eb4c64e271300000000001eb69a0000000000000000],
  ["town_14_master_craftsman", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007590c3206155c8b475a4e439a00000000001f489a0000000000000000],
  ["town_15_master_craftsman", "{!}Town 15 Seneschal", "{!}Town 15 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007440022d04b2c6cb7d3723d5a00000000001dc90a0000000000000000],
  ["town_16_master_craftsman", "{!}Town 16 Seneschal", "{!}Town 16 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007680c3586054b8e372e4db65c00000000001db7230000000000000000],
  ["town_17_master_craftsman", "{!}Town 17 Seneschal", "{!}Town 17 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000766046186591b564cec85d2e200000000001e4cea0000000000000000],
  ["town_18_master_craftsman", "{!}Town 18 Seneschal", "{!}Town 18 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000e7e0075523a6aa9b6da61e8dd00000000001d96d30000000000000000],
  ["town_19_master_craftsman", "{!}Town 19 Seneschal", "{!}Town 19 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000002408314852a432e88aaa42e100000000001e284e0000000000000000],
  ["town_20_master_craftsman", "{!}Town 20 Seneschal", "{!}Town 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001104449136e44cbd1c9352bc000000000005e8d10000000000000000],
  ["town_21_master_craftsman", "{!}Town 21 Seneschal", "{!}Town 21 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000131032d3351c6e43226ec96c000000000005b5240000000000000000],
  ["town_22_master_craftsman", "{!}Town 22 Seneschal", "{!}Town 22 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],
  ["town_23_master_craftsman", "{!}Town 23 Craftsman", "{!}Town 23 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_24_master_craftsman", "{!}Town 24 Craftsman", "{!}Town 24 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_25_master_craftsman", "{!}Town 25 Craftsman", "{!}Town 25 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_26_master_craftsman", "{!}Town 26 Craftsman", "{!}Town 26 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_27_master_craftsman", "{!}Town 27 Craftsman", "{!}Town 27 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_28_master_craftsman", "{!}Town 28 Craftsman", "{!}Town 28 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_wrapping_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_29_master_craftsman", "{!}Town 29 Craftsman", "{!}Town 29 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_wrapping_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_30_master_craftsman", "{!}Town 30 Craftsman", "{!}Town 30 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_wrapping_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_31_master_craftsman", "{!}Town 31 Craftsman", "{!}Town 31 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_wrapping_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_32_master_craftsman", "{!}Town 32 Craftsman", "{!}Town 32 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_wrapping_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_33_master_craftsman", "{!}Town 33 Craftsman", "{!}Town 33 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_wrapping_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_34_master_craftsman", "{!}Town 34 Craftsman", "{!}Town 34 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_wrapping_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_35_master_craftsman", "{!}Town 35 Craftsman", "{!}Town 35 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_wrapping_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_36_master_craftsman", "{!}Town 36 Craftsman", "{!}Town 36 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_wrapping_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_37_master_craftsman", "{!}Town 37 Craftsman", "{!}Town 37 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_wrapping_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_38_master_craftsman", "{!}Town 38 Craftsman", "{!}Town 38 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_wrapping_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_39_master_craftsman", "{!}Town 39 Craftsman", "{!}Town 39 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_wrapping_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_40_master_craftsman", "{!}Town 40 Craftsman", "{!}Town 40 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_wrapping_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_41_master_craftsman", "{!}Town 41 Craftsman", "{!}Town 41 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_wrapping_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_42_master_craftsman", "{!}Town 42 Craftsman", "{!}Town 42 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_wrapping_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_43_master_craftsman", "{!}Town 43 Craftsman", "{!}Town 43 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_wrapping_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_44_master_craftsman", "{!}Town 44 Craftsman", "{!}Town 44 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_wrapping_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],

# Chests
  ["zendar_chest","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,
   [],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_1","{!}Melee Weapons Chest","{!}Melee Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_sword, itm_tutorial_axe, itm_tutorial_spear, itm_tutorial_club, itm_tutorial_battle_axe],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_2","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_short_bow, itm_tutorial_arrows, itm_tutorial_crossbow, itm_tutorial_bolts, itm_tutorial_throwing_daggers],def_attrib|level(18),wp(60),knows_common, 0],

  ["bonus_chest_1","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_concave_shield_domestici,itm_arabian_sword_d,itm_gold_jewelry,itm_wine],def_attrib|level(18),wp(60),knows_common, 0], #hidden at the palace
  ["bonus_chest_2","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_vidigoia_spear,itm_gold_jewelry],def_attrib|level(18),wp(60),knows_common, 0], #grave
  ["bonus_chest_3","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_gold_jewelry],def_attrib|level(18),wp(60),knows_common, 0], #reuse
  ["bonus_chest_4","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_long_hafted_spiked_mace,itm_wine],def_attrib|level(18),wp(60),knows_common, 0], #le bonker
  ["bonus_chest_5","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_heirloom],def_attrib|level(18),wp(60),knows_common, 0], #ring for the greek scythaboo
  ["bonus_chest_6","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_niya_bow_2,itm_raw_silk,itm_linen,itm_linen],def_attrib|level(18),wp(60),knows_common, 0], #hidden in attilas court ruins
  ["bonus_chest_7","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_mace_roman_1,itm_wool_cloth,itm_wool_cloth],def_attrib|level(18),wp(60),knows_common, 0], #hidden in noricum

  ["household_possessions","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],

# These are used as arrays in the scripts. #SB : give full inventory
  ["temp_array_a","{!}temp_array_a","{!}temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
  ["temp_array_b","{!}temp_array_b","{!}temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
  ["temp_array_c","{!}temp_array_c","{!}temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],

  ["stack_selection_amounts","{!}stack_selection_amounts","{!}stack_selection_amounts",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["stack_selection_ids","{!}stack_selection_ids","{!}stack_selection_ids",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["notification_menu_types","{!}notification_menu_types","{!}notification_menu_types",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var1","{!}notification_menu_var1","{!}notification_menu_var1",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var2","{!}notification_menu_var2","{!}notification_menu_var2",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["banner_background_color_array","{!}banner_background_color_array","{!}banner_background_color_array",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["multiplayer_data","{!}multiplayer_data","{!}multiplayer_data",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

# Add Extra Quest NPCs below this point

  ["local_merchant","Local Merchant","Local Merchants",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["tax_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_staff,itm_quarter_staff,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots,itm_woolen_cap,itm_new_hood_e,itm_imperial_common_shirt,itm_linen_shirt_1,itm_linen_shirt_2,itm_linen_shirt_3,itm_linen_shirt_4,itm_linen_shirt_5,itm_linen_shirt_6,itm_linen_shirt_7,itm_linen_shirt_8,itm_linen_shirt_9],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["trainee_peasant","Peasant","Peasants",tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_woolen_cap_b,itm_woolen_cap_b,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["fugitive","Nervous Man","Nervous Men",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_sword_medieval_a]+tunics_generic+shoes_generic,
   def_attrib|str_24|agi_25|level(20),wp(180),knows_common|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,man_face_1, man_face_old_2],

  ["belligerent_drunk","Belligerent Drunk","Belligerent Drunks",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_shirt,itm_coarse_tunic,itm_leather_vest,itm_linen_shirt_5,itm_linen_shirt_10,itm_linen_shirt_13,itm_skirmisher_tunic_4,itm_wrapping_boots,itm_ankle_boots,itm_khergit_leather_boots,itm_hunter_boots,itm_fur_hat,itm_leather_cap,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_long_seax_1], #seax
   def_attrib_lvl_13|str_20|agi_8|level(15),wp_one_handed(180),knows_common|knows_power_strike_4|knows_ironflesh_9,  bandit_face1, bandit_face2],

  ["hired_assassin","Hired Assassin","Hired Assassin",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners, #they look like belligerent drunks, but have swords
   [itm_short_tunic,itm_linen_tunic,itm_shirt,itm_coarse_tunic,itm_leather_vest,itm_linen_shirt_5,itm_linen_shirt_10,itm_linen_shirt_13,itm_skirmisher_tunic_4,itm_wrapping_boots,itm_ankle_boots,itm_khergit_leather_boots,itm_hunter_boots,itm_fur_hat,itm_leather_cap,itm_pannonian_cap_fur_1,itm_pannonian_cap_fur_2,itm_sword_medieval_a],
   def_attrib_lvl_23|level(25),wp(230),knows_common|knows_power_strike_6|knows_ironflesh_9,    bandit_face1, bandit_face2],

  ["fight_promoter","Rough-Looking Character","Rough-Looking Character",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_leather_vest, itm_nomad_boots, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,    bandit_face1, bandit_face2],

  ["spy","Ordinary Townsman","Ordinary Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_sword_viking_1,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves],
   def_attrib|agi_11|level(20),wp(130),knows_common,man_face_1, man_face_2],

  ["spy_partner","Unremarkable Townsman","Unremarkable Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_sword_viking_2,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves],
   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],

   ["nurse_for_lady","Nurse","Nurse",tf_female|tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_robe,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,woman_face_1, woman_face_2],
   ["temporary_minister","Minister","Minister",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners,
   [itm_long_tunic_a, itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_1, man_face_2],

  ["quick_battle_6_player", "{!}quick_battle_6_player", "{!}quick_battle_6_player", tf_hero, 0, reserved,  fac_player_faction, [itm_padded_cloth,itm_nomad_boots, itm_splinted_leather_greaves, itm_skullcap, itm_sword_medieval_b,  itm_crossbow, itm_bolts, itm_plate_covered_round_shield],    knight_attrib_1,wp(130),knight_skills_1, 0x000000000008010b01f041a9249f65fd],

#Multiplayer ai troops
  ["swadian_crossbowman_multiplayer_ai","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_sword_medieval_a,itm_tab_shield_round_d,
    itm_leather_jerkin,itm_leather_armor,itm_ankle_boots,(itm_intercisa_helmet_1,imod_battered)],
   def_attrib|level(19),wp_melee(90)|wp_crossbow(100),knows_common|knows_ironflesh_4|knows_athletics_6|knows_shield_5|knows_power_strike_3,germanic_face_1, germanic_face_2],
  ["swadian_infantry_multiplayer_ai","Swadian Infantry","Swadian Infantry",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_pike,itm_tab_shield_round_e,
    itm_studded_leather_coat,itm_ankle_boots,itm_iatrus_helmet_mail],
   def_attrib|level(19),wp_melee(105),knows_common|knows_ironflesh_5|knows_shield_4|knows_power_strike_5|knows_athletics_4,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_lance,itm_tab_shield_round_d,
    itm_mail_with_surcoat,itm_hide_boots,itm_intercisa_helmet_plume_1,itm_hunter],
   def_attrib|level(19),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_4|knows_shield_4|knows_power_strike_4|knows_athletics_1,germanic_face_1, germanic_face_2],
  ["vaegir_archer_multiplayer_ai","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_fighting_axe,itm_nomad_bow,
    itm_leather_vest,itm_nomad_boots,itm_kerch_lamellenhelm_light,itm_nomad_cap],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_4|knows_power_draw_5|knows_athletics_6|knows_shield_2,germanic_face_1, germanic_face_2],
  ["vaegir_spearman_multiplayer_ai","Vaegir Spearman","Vaegir Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_padded_leather,itm_nomad_boots,itm_kerch_lamellenhelm_light,itm_nomad_cap, itm_spear, itm_tab_shield_round_d, itm_mace_1, itm_javelin],
   def_attrib|str_12|level(19),wp_melee(90),knows_ironflesh_4|knows_athletics_6|knows_power_throw_3|knows_power_strike_3|knows_shield_2,germanic_face_1, germanic_face_2],
  ["vaegir_horseman_multiplayer_ai","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_battle_axe,itm_fighting_axe,itm_lance,itm_tab_shield_round_d,
     itm_studded_leather_coat,itm_lamellar_vest,itm_nomad_boots,itm_kerch_lamellenhelm_light,itm_saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_4|knows_ironflesh_4|knows_power_strike_4|knows_shield_3,germanic_face_1, germanic_face_2],
  ["khergit_dismounted_lancer_multiplayer_ai","Khergit Dismounted Lancer","Khergit Dismounted Lancer",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_spiked_mace,itm_battle_axe,itm_battle_axe_3,itm_battle_axe_3,itm_bearded_axe_1,itm_heavy_lance,itm_lance,
    itm_kerch_lamellenhelm_gilded,itm_kerch_lamellenhelm,itm_lamellar_vest_khergit,itm_tribal_warrior_outfit,itm_khergit_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_mail_mittens,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c],
   def_attrib|level(19),wp(100),knows_riding_4|knows_power_strike_1|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_1|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_veteran_horse_archer_multiplayer_ai","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_khergit_bow,itm_khergit_arrows,itm_tab_shield_small_round_b,
    itm_kerch_lamellenhelm_gilded,itm_tribal_warrior_outfit,itm_khergit_leather_boots,itm_steppe_horse],
   def_attrib|level(19),wp(90)|wp_archery(100),knows_riding_6|knows_power_draw_5|knows_shield_2|knows_horse_archery_5,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer_ai","Khergit Lancer","Khergit Lancers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_spiked_mace,itm_battle_axe,itm_battle_axe_3,itm_battle_axe_3,itm_bearded_axe_1,itm_heavy_lance,itm_lance,
    itm_kerch_lamellenhelm_gilded,itm_kerch_lamellenhelm,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_mail_mittens,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_courser],
   def_attrib|level(19),wp(100),knows_riding_7|knows_power_strike_2|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_1|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
  ["nord_veteran_multiplayer_ai","Nord Footman","Nord Footmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_4,
   [itm_sword_viking_2,itm_battle_axe_1,itm_two_handed_axe,itm_tab_shield_round_d,itm_throwing_axes,
    itm_intercisa_helmet_gilded_1,itm_mail_hauberk,itm_splinted_leather_greaves,itm_leather_boots,itm_leather_gloves],
   def_attrib|level(19),wp(130),knows_ironflesh_3|knows_power_strike_5|knows_power_throw_3|knows_athletics_5|knows_shield_3,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer_ai","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_sword_viking_1,itm_two_handed_axe,itm_spear,itm_tab_shield_round_a,
    itm_skullcap,itm_generic_leather_helmet_cloth,itm_leather_jerkin,itm_leather_boots,itm_saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3,nord_face_young_1, nord_face_older_2],
  ["nord_archer_multiplayer_ai","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_two_handed_axe,itm_sword_viking_2,itm_short_bow,
    itm_leather_jerkin,itm_blue_tunic,itm_leather_boots,itm_old_spangenhelm_3,itm_leather_cap],
   def_attrib|str_11|level(19),wp_melee(80)|wp_archery(110),knows_ironflesh_4|knows_power_strike_2|knows_shield_1|knows_power_draw_5|knows_athletics_6,germanic_face_1, germanic_face_2],
  ["rhodok_veteran_crossbowman_multiplayer_ai","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_fighting_axe,itm_maul,itm_tab_shield_pavise_c,itm_heavy_crossbow,itm_bolts,
    itm_leather_cap,itm_padded_leather,itm_nomad_boots],
   def_attrib|level(19),wp_melee(100)|wp_crossbow(120),knows_common|knows_ironflesh_4|knows_shield_5|knows_power_strike_3|knows_athletics_6,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_veteran_spearman_multiplayer_ai","Rhodok Spearman","Rhodok Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_5,
   [itm_ashwood_pike,itm_war_spear,itm_pike,itm_sledgehammer,itm_tab_shield_pavise_c,itm_sword_medieval_a,
    itm_leather_cap,itm_byrnie,itm_ragged_outfit,itm_nomad_boots],
   def_attrib|level(19),wp(115),knows_common|knows_ironflesh_5|knows_shield_3|knows_power_strike_4|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_scout_multiplayer_ai","Rhodok Scout","Rhodok Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_5,
   #TODO: Change weapons, copied from Nord Scout
   [itm_sword_medieval_a,itm_tab_shield_round_d,itm_light_lance,itm_skullcap,itm_aketon_green,
    itm_ragged_outfit,itm_nomad_boots,itm_ankle_boots,itm_saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3,rhodok_face_young_1, rhodok_face_older_2],
  ["sarranid_infantry_multiplayer_ai","Sarranid Infantry","Sarranid Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_sassanid_mail_shirt_1,itm_sarranid_horseman_helmet,itm_sarranid_boots_b,itm_sarranid_boots_c,itm_splinted_leather_greaves,itm_arabian_sword_b,itm_mace_3,itm_spear],
   def_attrib|level(20),wp_melee(105),knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3,swadian_face_middle_1, swadian_face_old_2],
  ["sarranid_archer_multiplayer_ai","Sarranid Archer","Sarranid Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_arrows,itm_nomad_bow,itm_arabian_sword_a,itm_archers_vest,itm_sarranid_boots_b,itm_iatrus_helmet_light,itm_turban,itm_desert_turban],
   def_attrib|level(19),wp_melee(90)|wp_archery(100),knows_common|knows_riding_2|knows_ironflesh_1,germanic_face_1, germanic_face_2],
  ["sarranid_horseman_multiplayer_ai","Sarranid Horseman","Sarranid Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_lance,itm_arabian_sword_b,itm_fighting_axe,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sassanid_mail_shirt_1,itm_sarranid_boots_b,itm_sarranid_boots_c,itm_sarranid_horseman_helmet,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,germanic_face_1, germanic_face_2],



#Multiplayer troops (they must have the base items only, nothing else)
  ["swadian_crossbowman_multiplayer","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_sword_medieval_b_small,itm_tab_shield_heater_a,itm_red_shirt,itm_ankle_boots],
   str_14 | agi_15 |def_attrib_multiplayer|level(19),wpe(90,60,180,90),knows_common_multiplayer|knows_ironflesh_2|knows_athletics_4|knows_shield_5|knows_power_strike_2|knows_riding_1,germanic_face_1, germanic_face_2],
  ["swadian_infantry_multiplayer","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_a,itm_tab_shield_heater_a,itm_red_tunic,itm_ankle_boots],
   str_15 | agi_15 |def_attrib_multiplayer|level(20),wpex(105,130,110,40,60,110),knows_common_multiplayer|knows_ironflesh_5|knows_shield_4|knows_power_strike_4|knows_power_throw_2|knows_athletics_6|knows_riding_1,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_lance,itm_sword_medieval_a,itm_tab_shield_heater_a,
    itm_red_tunic,itm_ankle_boots,itm_saddle_horse],
   str_14 | agi_16 |def_attrib_multiplayer|level(20),wp_melee(110),knows_common_multiplayer|knows_riding_5|knows_ironflesh_3|knows_shield_2|knows_power_throw_2|knows_power_strike_3|knows_athletics_3,germanic_face_1, germanic_face_2],
#  ["swadian_mounted_crossbowman_multiplayer","Swadian Mounted Crossbowman","Swadian Mounted Crossbowmen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
#   [itm_bolts,itm_light_crossbow,itm_tab_shield_round_d,
#    itm_red_shirt,itm_hide_boots,itm_saddle_horse],
#   def_attrib_multiplayer|level(20),wp_melee(100)|wp_crossbow(120),knows_common_multiplayer|knows_riding_4|knows_shield_3|knows_ironflesh_3|knows_horse_archery_2|knows_power_strike_3|knows_athletics_2|knows_shield_2,germanic_face_1, germanic_face_2],
  ["vaegir_archer_multiplayer","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_mace_1,itm_nomad_bow,
    itm_linen_tunic,itm_hide_boots],
   str_14 | agi_14 |def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80),knows_common_multiplayer|knows_ironflesh_2|knows_power_draw_7|knows_athletics_3|knows_shield_2|knows_riding_1,germanic_face_1, germanic_face_2],
  ["vaegir_spearman_multiplayer","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_spear, itm_tab_shield_round_d, itm_mace_1,
    itm_linen_tunic,itm_hide_boots],
   str_15 | agi_15 |def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120),knows_common_multiplayer|knows_ironflesh_4|knows_shield_2|knows_power_throw_3|knows_power_strike_4|knows_athletics_6|knows_riding_1,germanic_face_1, germanic_face_2],
  ["vaegir_horseman_multiplayer","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_fighting_axe,itm_lance,itm_tab_shield_round_d,
    itm_linen_tunic,itm_hide_boots,itm_saddle_horse],
   str_16 | agi_15 |def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_common_multiplayer|knows_riding_5|knows_ironflesh_4|knows_power_strike_3|knows_shield_3|knows_power_throw_4|knows_horse_archery_1,germanic_face_1, germanic_face_2],
  ["khergit_veteran_horse_archer_multiplayer","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_nomad_bow,itm_arrows,
    itm_khergit_armor,itm_leather_steppe_cap_a,itm_hide_boots,itm_steppe_horse],
   str_15 | agi_18 |def_attrib_multiplayer|level(21),wpe(70,142,60,100),knows_common_multiplayer|knows_riding_2|knows_power_draw_5|knows_horse_archery_3|knows_athletics_3|knows_shield_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_infantry_multiplayer","Khergit Infantry","Khergit Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_spear,itm_tab_shield_small_round_a,
    itm_steppe_armor,itm_hide_boots,itm_leather_gloves],
   str_14 | agi_15 |def_attrib_multiplayer|level(19),wp(110),knows_common_multiplayer|knows_ironflesh_3|knows_power_throw_3|knows_shield_4|knows_power_strike_3|knows_athletics_6|knows_riding_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_lance,itm_tab_shield_small_round_a,
    itm_khergit_armor,itm_leather_steppe_cap_a,itm_hide_boots,itm_steppe_horse],
   str_15 | agi_14 |def_attrib_multiplayer|level(21),wp(115),knows_common_multiplayer|knows_riding_6|knows_ironflesh_3|knows_power_throw_3|knows_shield_4|knows_power_strike_3|knows_athletics_4,khergit_face_middle_1, khergit_face_older_2],
  ["nord_archer_multiplayer","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_sword_viking_2_small,itm_short_bow,
    itm_blue_tunic,itm_leather_boots],
   str_15 | agi_14 |def_attrib_multiplayer|str_11|level(15),wpe(90,150,60,80),knows_common_multiplayer|knows_ironflesh_2|knows_power_strike_2|knows_shield_3|knows_power_draw_5|knows_athletics_3|knows_riding_1,germanic_face_1, germanic_face_2],
  ["nord_veteran_multiplayer","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_viking_1,itm_battle_axe_3,itm_tab_shield_round_a,
    itm_blue_tunic,itm_leather_boots],
   str_17 | agi_15 |def_attrib_multiplayer|level(24),wpex(110,135,100,40,60,140),knows_common_multiplayer|knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_athletics_6|knows_shield_3|knows_riding_1,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_sword_viking_1,itm_spear,itm_tab_shield_small_round_a,
    itm_blue_tunic,itm_leather_boots,itm_saddle_horse],
   str_16 | agi_15 |def_attrib_multiplayer|level(19),wp(105),knows_common_multiplayer|knows_riding_6|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_3|knows_power_throw_3|knows_athletics_3,germanic_face_1, germanic_face_2],
  ["rhodok_veteran_crossbowman_multiplayer","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_crossbow,itm_bolts,itm_fighting_axe,itm_tab_shield_pavise_a,
    itm_tunic_with_green_cape,itm_ankle_boots],
   str_16 | agi_15 |def_attrib_multiplayer|level(20),wpe(100,60,180,90),knows_common_multiplayer|knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_athletics_4|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_sergeant_multiplayer","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_fighting_axe,itm_tab_shield_pavise_a,itm_spear,
    itm_green_tunic,itm_ankle_boots],
   str_16 | agi_14 |def_attrib_multiplayer|level(20),wpex(110,100,140,30,50,110),knows_common_multiplayer|knows_ironflesh_4|knows_shield_5|knows_power_strike_4|knows_power_throw_1|knows_athletics_6|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_horseman_multiplayer","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_tab_shield_round_d, itm_light_lance,
    itm_green_tunic,itm_ankle_boots,itm_saddle_horse],
   str_15 | agi_15 |def_attrib_multiplayer|level(20),wp(100),knows_common_multiplayer|knows_riding_4|knows_ironflesh_3|knows_shield_3|knows_power_strike_3|knows_power_throw_1|knows_athletics_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["sarranid_archer_multiplayer","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arrows,itm_arabian_sword_a,itm_nomad_bow,
    itm_sarranid_cloth_robe, itm_sarranid_boots_b],
   str_15 | agi_16 |def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80),knows_common_multiplayer|knows_ironflesh_4|knows_power_draw_5|knows_athletics_3|knows_shield_2|knows_riding_1|knows_weapon_master_1,germanic_face_1, germanic_face_2],
  ["sarranid_footman_multiplayer","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_bamboo_spear, itm_tab_shield_round_d, itm_arabian_sword_a,
    itm_sarranid_cloth_robe, itm_sarranid_boots_b],
   str_14 | agi_15 |def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120),knows_common_multiplayer|knows_ironflesh_4|knows_shield_2|knows_power_throw_3|knows_power_strike_4|knows_athletics_6|knows_riding_1,germanic_face_1, germanic_face_2],
  ["sarranid_mamluke_multiplayer","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arabian_sword_a,itm_lance,itm_tab_shield_small_round_a,
    itm_sarranid_cloth_robe, itm_sarranid_boots_b,itm_saddle_horse],
   str_15 | agi_14 |def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_common_multiplayer|knows_riding_5|knows_ironflesh_3|knows_power_strike_2|knows_shield_3|knows_power_throw_2|knows_weapon_master_1,germanic_face_1, germanic_face_2],

  ["multiplayer_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

#Player history array
  ["log_array_entry_type",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_entry_time",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_actor",                 "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object",         "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_lord",    "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_faction", "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object",          "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object_faction",  "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_faction_object",        "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],

  ["quick_battle_troop_1","Majorianus","Majorianus", tf_hero,0,0,fac_kingdom_1,
   [itm_half_cataphract_horse_3,itm_roman_squamata_emperor,itm_roman_emperor_greaves,itm_tab_shield_small_round_c,itm_arabian_sword_d, itm_berk_helmet],
   knight_attrib_5|level(30),wpex(280,260,250,100,100,100),knows_riding_5|knows_athletics_6|knows_shield_6|knows_weapon_master_6|knows_power_strike_5|knows_ironflesh_8,0x000000060e002045345250369369b4db00000000001d36e20000000000000000],
  ["quick_battle_troop_2","Ardaric","Ardaric", tf_hero,0,0,fac_kingdom_1,
   [itm_half_cataphract_horse_7, itm_splinted_greaves, itm_coat_of_plates_red, itm_arabian_sword_a, itm_tab_shield_round_e, itm_koblenz_helmet_2, itm_heavy_lance],
   knight_attrib_5|level(30),wpex(300,260,270,100,100,100),knows_riding_4|knows_athletics_6|knows_shield_6|knows_weapon_master_6|knows_power_strike_8|knows_ironflesh_7,0x0000000b960063c9329c6ab4db69a6db00000000001db6e10000000000000000],
  ["quick_battle_troop_3","Attila","Attila", tf_hero,0,0,fac_kingdom_1,
   [itm_heavy_lance,itm_khergit_bow,itm_khergit_arrows,itm_sword_khergit_1,itm_turaevo_helmet_aventail,itm_lamellar_armor,itm_heavy_greaves,itm_warhorse_steppe],
   knight_attrib_5|level(30),wpex(250,200,260,200,200,200),knows_riding_8|knows_athletics_4|knows_shield_3|knows_weapon_master_4|knows_power_strike_5|knows_ironflesh_7|knows_power_draw_6|knows_horse_archery_8,0x000000019600c3cb5295aa431d6924d200000000001d36b80000000000000000],
  ["quick_battle_troop_4","Flavius Stilicho","Flavius Stilicho", tf_hero,0,0,fac_kingdom_1,
   [itm_half_cataphract_horse_2,itm_roman_greaves_3,itm_457_scale_hauberk_6,itm_berk_helmet,itm_arabian_sword_b,itm_heavy_lance,itm_tab_shield_round_e],
   knight_attrib_5|level(28),wpex(280,250,280,100,100,100),knows_riding_6|knows_athletics_5|knows_shield_4|knows_weapon_master_5|knows_power_strike_7|knows_ironflesh_8,0x000000088000308256dab258a38db6db00000000001db6e30000000000000000],
  ["quick_battle_troop_5","Flavius Aetius","Flavius Aetius", tf_hero,0,0,fac_kingdom_1,
   [itm_roman_greaves_1,itm_roman_squamata_3,itm_augsburg_1_helmet,itm_sword_khergit_4,itm_late_roman_spear_2,itm_war_darts,itm_round_shield_roman_5],
   knight_attrib_5|level(28),wpex(290,250,230,200,200,200),knows_athletics_7|knows_shield_8|knows_weapon_master_5|knows_power_throw_5|knows_power_strike_6|knows_ironflesh_10,0x0000000aff009002445a91b89b6db6e300000000001db68a0000000000000000],
  ["quick_battle_troop_6","Radagaisus","Radagaisus", tf_hero,0,0,fac_kingdom_1,
   [itm_warhorse,itm_ankle_boots,itm_medium_scale_1,itm_intercisa_helmet_gilded_1,itm_light_lance,itm_sword_viking_3,itm_tab_shield_small_round_c],
   knight_attrib_4|level(26),wpex(300,200,300,100,100,100),knows_riding_6|knows_athletics_5|knows_weapon_master_4|knows_power_strike_7|knows_ironflesh_6,0x0000000a800060452b1a95aae49134db00000000001db6ea0000000000000000],
  ["quick_battle_troop_7","Hunimund","Hunimund", tf_hero,0,0,fac_kingdom_1,
   [itm_simple_shoes,itm_long_mail_new_4,itm_fernpass_helmet_2,itm_leather_gloves,itm_tab_shield_round_d,itm_angon_1,itm_hunimund_axe],
   knight_attrib_4|level(25),wpex(250,300,200,100,100,100),knows_athletics_6|knows_shield_3|knows_weapon_master_5|knows_power_throw_7|knows_power_strike_9|knows_ironflesh_5,0x0000000905004084549c652a9b4dbadb00000000001d36ea0000000000000000],
  ["quick_battle_troop_8","Arbogast","Arbogast", tf_hero,0,0,fac_kingdom_1,
   [itm_imperial_saddle_horse_4,itm_roman_lorum_fasciari_2,itm_roman_squamata_1,itm_koblenz_helmet_1,itm_sword_viking_3_small,itm_tab_shield_small_round_c,itm_war_spear,itm_angon_2],
   knight_attrib_4|level(23),wpex(220,150,210,85,100,130),knows_riding_2|knows_athletics_5|knows_shield_2|knows_weapon_master_4|knows_power_draw_2|knows_power_throw_4|knows_power_strike_2|knows_ironflesh_2,0x0000000006040188355b6d951b6db6db00000000001db6db0000000000000000],
  ["quick_battle_troop_9","Beowulf ","Beowulf ", tf_hero,0,0,fac_kingdom_1,
   [itm_wrapping_boots,itm_unique_mail_armor,itm_burgh_helmet_2,itm_sword_viking_c_long,itm_war_spear,itm_angon_1,itm_round_shield_germanic_5],
   def_attrib_lvl_25|level(26),wpex(300,300,270,100,80,115),knows_athletics_7|knows_shield_2|knows_weapon_master_5|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_5,0x000000000000450946da6daaac9132db00000000001db6dc0000000000000000],
  ["quick_battle_troop_10","Vakhtang","Vakhtang", tf_hero,0,0,fac_kingdom_1,
   [itm_sassanid_cataphract_helmet_1,itm_eastern_scale_4,itm_heavy_greaves,itm_long_lance,itm_battle_axe,itm_tab_shield_small_round_c,itm_half_cataphract_horse_4],
   knight_attrib_4|level(24),wpex(220,150,230,140,100,100),knows_riding_8|knows_weapon_master_4|knows_power_strike_5|knows_ironflesh_6|knows_shield_3,0x000000001e00710244da91b8e36db4db00000000001db6db0000000000000000],
  ["quick_battle_troop_11","Peroz I","Peroz I", tf_hero,0,0,fac_kingdom_1,
   [itm_warhorse_sarranid,itm_emperor_armor_c,itm_heavy_greaves,itm_sassanid_cataphract_helmet_1,itm_ingushetia_spatha,itm_tab_shield_small_round_c,itm_long_lance],
   knight_attrib_5|level(28),wpex(240,160,300,100,100,100),knows_riding_7|knows_shield_5|knows_weapon_master_4|knows_power_strike_6|knows_ironflesh_7,0x000000002300b0c348db71b8eb95c6db00000000001db6e20000000000000000],
  ["quick_battle_troops_end","{!}quick_battle_troops_end","{!}quick_battle_troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

  ["tutorial_fighter_1","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088c1073144252b1929a85569300000000000496a50000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_2","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088b08049056ab56566135c46500000000001dda1b0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_3","Regular Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_nomad_boots],
   def_attrib|level(9),wp_melee(50),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x00000008bc00400654914a3b0d0de74d00000000001d584e0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_4","Veteran Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(16),wp_melee(110),knows_athletics_1|knows_ironflesh_3|knows_power_strike_2|knows_shield_2,0x000000089910324a495175324949671800000000001cd8ab0000000000000000, vaegir_face_older_2],
  ["tutorial_archer_1","Archer","Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_leather_jerkin,itm_leather_vest,itm_nomad_boots,itm_old_spangenhelm_3,itm_warlord_coif_1,itm_nomad_cap],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,germanic_face_1, germanic_face_2],
  ["tutorial_master_archer","Archery Trainer","Archery Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea508540642f34d461d2d54a300000000001d5d9a0000000000000000, vaegir_face_older_2],
  ["tutorial_rider_1","Rider","{!}Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_hunter, itm_saddle_horse,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_riding_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["tutorial_rider_2","Horse archer","{!}Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_tribal_warrior_outfit,itm_nomad_robe,itm_hide_boots,itm_tab_shield_small_round_a,itm_steppe_horse],
   def_attrib|level(14),wp(80)|wp_archery(110),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_power_throw_1,khergit_face_young_1, khergit_face_older_2],
  ["tutorial_master_horseman","Riding Trainer","Riding Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_leather_vest,itm_nomad_boots],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea0084140478a692894ba185500000000001d4af30000000000000000, vaegir_face_older_2],

  ["swadian_merchant", "Merchant of Dhirim", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_1, [itm_bearded_axe_2, itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["vaegir_merchant", "Merchant of Khundan", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_2, [itm_bearded_axe_2, itm_nobleman_outfit, itm_woolen_hose], def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["khergit_merchant", "Merchant of Tulga", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_3, [itm_bearded_axe_2, itm_red_gambeson, itm_nomad_boots], def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["nord_merchant", "Merchant of Wercheg", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_4, [itm_bearded_axe_2, itm_red_gambeson, itm_nomad_boots], def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["rhodok_merchant", "Merchant of Jelkala", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_5, [itm_bearded_axe_2, itm_leather_jerkin, itm_blue_hose], def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["sarranid_merchant", "Merchant of Shariz", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_6, [itm_bearded_axe_2, itm_sarranid_cloth_robe, itm_sarranid_boots_a], def_attrib|level(2),wp(20),knows_common, man_face_1, man_face_2],
  ["startup_merchants_end","startup_merchants_end","startup_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

  ["sea_raider_leader","Sea Raider Captain","Sea Raider Captains",tf_hero|tf_guarantee_all_wo_ranged,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_sword_viking_2,itm_fighting_axe,itm_battle_axe,itm_spear,itm_nordic_shield,itm_nordic_shield,itm_nordic_shield,itm_wooden_shield,itm_long_bow,itm_javelin,itm_throwing_axes,
    itm_intercisa_helmet_gilded_1,itm_intercisa_helmet_gilded_1,itm_old_spangenhelm_3,itm_mail_shirt,itm_byrnie,itm_mail_hauberk,itm_leather_boots, itm_nomad_boots],
   def_attrib|level(24),wp(110),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2,germanic_face_1, germanic_face_2],

  ["looter_leader","Robber","Looters",tf_hero,0,0,fac_outlaws,
   [itm_hatchet,itm_club,itm_butchering_knife,itm_fighting_axe,itm_rawhide_coat,itm_stones,itm_nomad_armor,itm_nomad_armor,itm_woolen_cap,itm_woolen_cap,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(20),knows_common,0x00000001b80032473ac49738206626b200000000001da7660000000000000000, bandit_face2],

  ["bandit_leaders_end","bandit_leaders_end","bandit_leaders_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

  ["relative_of_merchant", "Merchant's Brother", "{!}Prominent",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2, 0x00000000320410022d2595495491afa400000000001d9ae30000000000000000, man_face_2],

  ["relative_of_merchants_end","relative_of_merchants_end","relative_of_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

  #MINOR FACTION KINGS START
  ["aestii_king","Aiwarikiar Scylfingr","Aiwarikiar Scylfingr",tf_hero, no_scene, reserved, fac_minor_aestii,[itm_wrapping_boots,itm_mid_generic_mail_21,itm_gultlingen_helmet_plume,itm_taurapilis_spatha,itm_concave_shield_germanic_17],def_attrib_lvl_32|level(32),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_throwing(280)|wp_archery(160)|wp_crossbow(130)|wp_firearm(130),knows_ironflesh_10|knows_power_strike_8|knows_shield_6|knows_athletics_6|knows_riding_5,0x00000008c00000c236db6db6db6db6db00000000001db6db0000000000000000],
  ["irish_king","Dallan Dail Fiatach","Dallan Dail Fiatach",tf_hero, no_scene, reserved, fac_minor_irish,[itm_wrapping_boots,itm_pictish_short_mail_2,itm_burgh_helmet_2,itm_pictish_sword,itm_vae_pictish_rectangle_16],def_attrib_lvl_32|level(32),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_throwing(280)|wp_archery(160)|wp_crossbow(130)|wp_firearm(130),knows_ironflesh_10|knows_power_strike_8|knows_shield_6|knows_athletics_6|knows_riding_5,0x0000000da50060465051a0975b512b2300000000001db6980000000000000000],
  ["garamantian_king","Tikfarin","Tikfarin",tf_hero, no_scene, reserved, fac_minor_garamantians,[itm_sword_khergit_4,itm_war_spear,itm_wrapping_boots,itm_garamantian_king_scale,itm_african_band_1],def_attrib_lvl_32|level(32),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_throwing(280)|wp_archery(160)|wp_crossbow(130)|wp_firearm(130),knows_ironflesh_10|knows_power_strike_8|knows_shield_6|knows_athletics_6|knows_riding_5,0x0000000c7f0130885a9b4ac96bb1272500000000001e371b0000000000000000],
  ["dani_king","Gramr Skjoldungr","Gramr Skjoldungr",tf_hero, no_scene, reserved, fac_minor_dani,[itm_khergit_leather_boots,itm_danish_king_mail,itm_danish_king_mace,itm_gultlingen_helmet_plume,itm_round_shield_germanic_5],def_attrib_lvl_32|level(32),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_throwing(280)|wp_archery(160)|wp_crossbow(130)|wp_firearm(130),knows_ironflesh_10|knows_power_strike_8|knows_shield_6|knows_athletics_6|knows_riding_5,0x00000001bf0000823adb6db6db6db6db00000000001db6dd0000000000000000],
  ["morden_king","Terekh","Terekh",tf_hero, no_scene, reserved, fac_minor_mordens,[itm_simple_shoes,itm_steppe_plated_armor_1,itm_tsaritsyno_1_veiled,itm_borok_spatha,itm_niya_bow_2,itm_khergit_arrows],def_attrib_lvl_32|level(32),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_throwing(280)|wp_archery(160)|wp_crossbow(130)|wp_firearm(130),knows_ironflesh_10|knows_power_strike_8|knows_shield_6|knows_athletics_6|knows_riding_5,0x00000009210043cb32548dd91a4db4c900000000001db4e40000000000000000],
  ["sporoi_king","Gostislav","Gostislav",tf_hero, no_scene, reserved, fac_minor_sporoi,[itm_simple_shoes,itm_short_slavic_mail_2],def_attrib_lvl_32|level(32),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_throwing(280)|wp_archery(160)|wp_crossbow(130)|wp_firearm(130),knows_ironflesh_10|knows_power_strike_8|knows_shield_6|knows_athletics_6|knows_riding_5,0x00000008000033cc525596491a4db49a00000000001ea4ea0000000000000000],
  ["bosphoran_king","Basileus Amospados II","Amospados II",tf_hero, no_scene, reserved, fac_minor_bosphoran,[itm_roman_lorum_fasciari_2,itm_457_scale_hauberk_7,itm_kishpek_helmet_mail,itm_pannonhalma_spatha,itm_niya_bow_2,itm_khergit_arrows],def_attrib_lvl_32|level(32),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_throwing(280)|wp_archery(180)|wp_crossbow(130)|wp_firearm(130),knows_ironflesh_10|knows_power_strike_8|knows_shield_6|knows_athletics_6|knows_riding_5|knows_power_draw_5,0x000000097c00608f54956ed6e355b6db00000000001db6910000000000000000],
  ["abagasian_king","Xobas","Xobas",tf_hero, no_scene, reserved, fac_minor_abagasians,[itm_sassanid_cavalry_boots_2,itm_kaftan_lamellar_9,itm_kishpek_helmet_mail,itm_djurso_spatha,itm_niya_bow_2,itm_khergit_arrows],def_attrib_lvl_32|level(32),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_throwing(280)|wp_archery(180)|wp_crossbow(130)|wp_firearm(130),knows_ironflesh_10|knows_power_strike_8|knows_shield_6|knows_athletics_6|knows_riding_5,0x00000001b20032885b956ac8696db6db00000000001db72d0000000000000000],
  ["tauri_king","Dandaxarthos","Dandaxarthos",tf_hero, no_scene, reserved, fac_minor_tauri,[itm_hunter_boots,itm_mid_roman_mail_1,itm_iatrus_2,itm_tetraxitae_spatha,itm_concave_shield_blue_1],def_attrib_lvl_32|level(32),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_throwing(280)|wp_archery(180)|wp_crossbow(130)|wp_firearm(130),knows_ironflesh_10|knows_power_strike_8|knows_shield_6|knows_athletics_6|knows_riding_5,0x000000065100810b5a558ec84ab6d51a00000000001ec6f90000000000000000],
  ["augundzi_king","Svipdagr","Svipdagr",tf_hero, no_scene, reserved, fac_minor_augundzi,[itm_obenaltendorf_shoes_1,itm_mid_generic_mail_6,itm_gultlingen_helmet_plume,itm_evebo_spatha,itm_concave_shield_germanic_20],def_attrib_lvl_32|level(32),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_throwing(280)|wp_archery(160)|wp_crossbow(130)|wp_firearm(130),knows_ironflesh_10|knows_power_strike_8|knows_shield_6|knows_athletics_6|knows_riding_5,0x000000094000450b5d536a2a698d22dc00000000001d36aa0000000000000000],
  ["vidivarii_king","Gaisalaiks","Gaisalaiks",tf_hero, no_scene, reserved, fac_minor_vidivarii,[itm_obenaltendorf_shoes_2,itm_mid_generic_mail_9,itm_intercisa_helmet_rich_3,itm_hunnic_spatha,itm_concave_shield_germanic_13,itm_niya_bow_2,itm_roman_arrows_2],def_attrib_lvl_32|level(32),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_throwing(280)|wp_archery(160)|wp_crossbow(130)|wp_firearm(130),knows_ironflesh_10|knows_power_strike_8|knows_shield_6|knows_athletics_6|knows_riding_5|knows_power_draw_5,0x00000005e40063c75a5256bb636dbb2b00000000001f36d20000000000000000],
  ["frisian_king","Finn Folcwalding","Finn Folcwalding",tf_hero, no_scene, reserved, fac_minor_frisians,[itm_obenaltendorf_shoes_1,itm_mid_generic_mail_13,itm_intercisa_helmet_rich_plume_3,itm_sword_khergit_3,itm_concave_shield_germanic_24,itm_war_spear_2],def_attrib_lvl_32|level(32),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_throwing(280)|wp_archery(160)|wp_crossbow(130)|wp_firearm(130),knows_ironflesh_10|knows_power_strike_8|knows_shield_6|knows_athletics_6|knows_riding_5,0x000000062900648354948a38aa51badb00000000001db72d0000000000000000],

  #installed via quest
  ["aestii_rebel_king","Shvarnas","Shvarnas",tf_hero, no_scene, reserved, fac_minor_aestii,[itm_simple_shoes,itm_mid_generic_mail_17,itm_burgh_helmet_2,itm_baltic_sword_1,itm_eastern_germanic_shield_2,itm_warhorse],def_attrib_lvl_32|level(32),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_throwing(280)|wp_archery(160)|wp_crossbow(130)|wp_firearm(130),knows_ironflesh_10|knows_power_strike_10|knows_shield_8|knows_athletics_8|knows_riding_5,0x00000005d80061076b6d8a485b6db6db00000000001db6a90000000000000000],

  #MINOR FACTION KINGS END
  #MINOR FACTION MERCHANTS BEGIN
  ["aestii_merchant_1","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_wrapping_boots,itm_tunic_long_pants_4],def_attrib|level(6),wp(80),knows_common,germanic_face_1, germanic_face_2], #sells goods - amber, fur
  ["aestii_merchant_2","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_ankle_boots,itm_generic_tunic_15],def_attrib|level(6),wp(80),knows_common,germanic_face_1, germanic_face_2], #sells gear - shields, old swords

  ["irish_merchant_1","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_wrapping_boots,itm_falkirk_tunic_1],def_attrib|level(6),wp(80),knows_common,celtic_face_1, celtic_face_2], #sells goods
  ["irish_merchant_2","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_ankle_boots,itm_falkirk_tunic_4],def_attrib|level(6),wp(80),knows_common,celtic_face_1, celtic_face_2], #sells gear

  ["garamantian_merchant_1","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_a_exomis_1],def_attrib|level(6),wp(80),knows_common,mauri_face_1, mauri_face_2], #sells goods
  ["garamantian_merchant_2","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_garamantian_armor_1],def_attrib|level(6),wp(80),knows_common,mauri_face_1, mauri_face_2], #sells gear

  ["dani_merchant_1","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_wrapping_boots,itm_generic_tunic_1],def_attrib|level(6),wp(80),knows_common,germanic_face_1, germanic_face_2], #sells goods - amber, fur
  ["dani_merchant_2","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_ankle_boots,itm_generic_tunic_3],def_attrib|level(6),wp(80),knows_common,germanic_face_1, germanic_face_2], #sells gear - shields, old swords

  ["morden_merchant_1","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_wrapping_boots,itm_generic_tunic_2],def_attrib|level(6),wp(80),knows_common,germanic_face_1, germanic_face_2], #sells goods - amber, fur
  ["morden_merchant_2","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_ankle_boots,itm_generic_tunic_7],def_attrib|level(6),wp(80),knows_common,germanic_face_1, germanic_face_2], #sells gear - shields, old swords

  ["slavic_merchant_1","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_wrapping_boots,itm_tunic_long_pants_9],def_attrib|level(6),wp(80),knows_common,germanic_face_1, germanic_face_2], #sells goods - shared
  ["slavic_merchant_2","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_ankle_boots,itm_tunic_long_pants_10],def_attrib|level(6),wp(80),knows_common,germanic_face_1, germanic_face_2], #sells gear - shared

  ["bosphoran_merchant_1","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_roman_lorum_fasciari_1,itm_roman_shirt_1],def_attrib|level(6),wp(80),knows_common,roman_face_1, roman_face_2], #sells goods - shared
  ["bosphoran_merchant_2","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_roman_lorum_fasciari_3,itm_roman_shirt_13],def_attrib|level(6),wp(80),knows_common,roman_face_1, roman_face_2], #sells gear - shared

  ["abagasian_merchant_1","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_wrapping_boots,itm_kaftan_sheepskin_2],def_attrib|level(6),wp(80),knows_common,caucaus_face_1, caucaus_face_2], #sells goods - shared
  ["abagasian_merchant_2","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_sassanid_cavalry_boots_1,itm_skirmisher_tunic_2],def_attrib|level(6),wp(80),knows_common,caucaus_face_1, caucaus_face_2], #sells gear - shared

  ["tauri_merchant_1","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_wrapping_boots,itm_roman_shirt_1],def_attrib|level(6),wp(80),knows_common,roman_face_1, roman_face_2], #sells goods - shared

  ["augundzi_merchant_1","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_obenaltendorf_shoes_1,itm_generic_tunic_2],def_attrib|level(6),wp(80),knows_common,germanic_face_1, germanic_face_2], #sells goods - hides, leather, fish, grain
  ["augundzi_merchant_2","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_obenaltendorf_shoes_2,itm_generic_tunic_5],def_attrib|level(6),wp(80),knows_common,germanic_face_1, germanic_face_2], #sells gear - shields, sword(s)?

  ["vidivarii_merchant_1","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_wrapping_boots,itm_generic_tunic_3],def_attrib|level(6),wp(80),knows_common,germanic_face_1, germanic_face_2], #sells goods - grain, fish, amber, fur (baltic)
  ["vidivarii_merchant_2","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_wrapping_boots,itm_generic_tunic_6],def_attrib|level(6),wp(80),knows_common,germanic_face_1, germanic_face_2], #sells goods - germanic swords, shields, leather

  ["frisian_merchant_1","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_ankle_boots,itm_generic_tunic_4],def_attrib|level(6),wp(80),knows_common,germanic_face_1, germanic_face_2], #sells goods - grain, fish
  ["frisian_merchant_2","Merchant","Merchants",tf_hero|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_commoners,[itm_simple_shoes,itm_generic_tunic_7],def_attrib|level(6),wp(80),knows_common,germanic_face_1, germanic_face_2], #sells goods - spears, swords, etc

  #MINOR FACTION MERCHANTS END

  #quest NPCs
  #["old_roman_man","Placus Silius","Placus Silius",tf_hero|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,[itm_roman_shirt_8, itm_wrapping_boots],def_attrib_elite|level(19),wp(180),knows_ironflesh_10|knows_power_strike_7,man_face_younger_1, man_face_2],

  #reusing for extended mithras quest
  ["roman_landowner","Gnaeus Turibius","Gnaeus Turibius",tf_hero|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,[itm_roman_shirt_14,itm_roman_lorum_fasciari_4,itm_arabian_sword_b],def_attrib_lvl_32|level(30),wp(300),knows_ironflesh_10|knows_power_strike_10,0x00000001bf0000823adb6db6db6db6db00000000001db6dd0000000000000000],

  ["roman_landowner_wife","Gnaeus Turibius's Wife","Gnaeus Turibius's Wife",tf_female|tf_hero,0,0,fac_commoners,[itm_ankle_boots,itm_roman_noble_dress_2,itm_dagger],def_attrib|level(8),wp(110),knows_common|knows_athletics_3|knows_power_draw_2|knows_power_strike_2|knows_wound_treatment_2,0x0000000ca60c501026db9337b5b63cda00000000001dc4120000000000000000],

  ["gothic_historian","Alatheus","Alatheus",tf_hero|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,[itm_coarse_tunic,itm_ankle_boots,itm_fighting_axe,itm_woolen_cap_4],def_attrib_lvl_32|level(19),wp(180),knows_ironflesh_10|knows_power_strike_7,0x000000018d0000823adb6db6db6db6db00000000001db6dd0000000000000000],

  ["hunnic_guide","Cniva the Old","Cniva the Old",tf_hero|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,[itm_peasant_man_8,itm_wrapping_boots],def_attrib_lvl_32|level(4),wp(60),knows_common,0x000000019e0010823adb6db6db6db6db00000000001db6dd0000000000000000],

  #Will be reused again, for the dragon quest
  ["burgundian_looter","Avaldus","Avaldus",tf_hero|tf_guarantee_helmet, no_scene,0, fac_outlaws,[itm_wrapping_boots,itm_short_ragged_mail_6,itm_augst_helmet_1,itm_sword_medieval_c,itm_concave_shield_germanic_2],def_attrib_lvl_30|level(30),wp(230),knows_common|knows_riding_3|knows_athletics_4|knows_ironflesh_8|knows_shield_4|knows_power_throw_4,0x00000003de0071433adb6db6db6db6db00000000001db6f10000000000000000],

  #probably won't use but who knows
  ["burgundian_bandit","Burgundian Bandit","Burgundian Bandits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_outlaws,
   [],
   def_attrib_lvl_18|level(19),wp(190),knows_common|knows_power_throw_4|knows_power_strike_4|knows_ironflesh_4,germanic_face_1, germanic_face_2],  
 
  ["old_warrior","old warrior","old warrior",tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_outlaws,
   [],
   def_attrib_lvl_28|level(40),wp(400),knows_ironflesh_10|knows_power_strike_10|knows_power_throw_10|knows_athletics_10|knows_shield_10|knows_wound_treatment_3|knows_surgery_8,0x00000007a6002194125b6db6cb6db6db00000000001db6c30000000000000000],

  ["hunnic_warlord","Hunnic Warlord","Hunnic Warlords",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_black_khergits,
   [],
   def_attrib_lvl_23|level(24),wpex(240,250,260,160,160,160),knows_riding_7|knows_ironflesh_8|knows_horse_archery_6|knows_power_draw_6|knows_power_strike_4,0x00000003de00c10336db6db6db6db6db00000000001db6db0000000000000000],

  ["sidonius_apollinaris","Sidonius Apollinaris","Sidonius Apollinaris",tf_hero, 0, reserved, fac_kingdom_2,[itm_ankle_boots,itm_roman_shirt_12],def_attrib|level(3),wp(80),knows_wound_treatment_3,0x000000000000208236db6db6db6db6db00000000001db6e40000000000000000],

  ["roman_local_1","Local","Locals",tf_hero|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_kingdom_2,
   [itm_ankle_boots,itm_roman_shirt_8],
   def_attrib|level(6),wp(80),knows_wound_treatment_3,roman_face_1, roman_face_2],

  ["roman_local_2","Local","Locals",tf_hero|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_kingdom_2,
   [itm_ankle_boots,itm_roman_shirt_8],
   def_attrib|level(6),wp(80),knows_wound_treatment_3,roman_face_1, roman_face_2],

  ["roman_local_3","Local","Locals",tf_hero|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_kingdom_2,
   [itm_ankle_boots,itm_roman_shirt_8],
   def_attrib|level(6),wp(80),knows_wound_treatment_3,roman_face_1, roman_face_2],

  ["monophysite_rebel","Monophysite Rebel","Monophysite Rebels",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_outlaws,
   [itm_mace_1,itm_winged_mace,itm_roman_spear_2,itm_hunting_bow,itm_arrows,itm_simple_shield_1,itm_simple_shield_2,itm_new_hood_e,itm_brown_hood1,itm_desert_turban,itm_turban,itm_wrapping_boots,itm_roman_shirt_4,itm_roman_shirt_2,itm_roman_shirt_10,itm_roman_shirt_8,itm_roman_shirt_6],
   def_attrib_lvl_18|level(17),wp_one_handed(180)|wp_two_handed(150)|wp_polearm(195)|wp_throwing(180)|wp_archery(150),knows_common|knows_shield_2|knows_power_strike_2|knows_ironflesh_5,coptic_face_1, coptic_face_2],  

  ["monophysite_leader","Monophysite Leader","Monophysite Leaders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_roman_spear_3,itm_ankle_boots,itm_long_roman_mail_3,itm_augst_helmet_1,itm_leather_gloves,itm_sword_medieval_a,itm_concave_shield_roman_1],
   def_attrib_lvl_23|level(22),wp_one_handed(230)|wp_two_handed(150)|wp_polearm(225)|wp_throwing(180)|wp_archery(150),knows_common|knows_shield_4|knows_power_strike_4|knows_ironflesh_7,coptic_face_1, coptic_face_2],  

  ["suebi_king", "Rex Hunimund", "Hunimund", tf_hero, no_scene, 0, fac_hunimund_suebi,[itm_saddle_horse, itm_ankle_greaves, itm_tab_shield_small_round_c, itm_long_mail_new_4, itm_koblenz_helmet_3, itm_sword_viking_3_small],knight_attrib_5,wp(300),knight_skills_5|knows_trainer_1|knows_trainer_3,0x0000000905004084549c652a9b4dbadb00000000001d36ea0000000000000000],

  ["heruli_king", "Rex Visilaus", "Visilaus", tf_hero, 0, reserved, fac_heruli,[itm_saddle_horse, itm_ankle_greaves, itm_tab_shield_small_round_c, itm_long_mail_new_1, itm_gultlingen_helmet_mail, itm_sword_viking_2],knight_attrib_5,wp(300),knight_skills_5|knows_trainer_1|knows_trainer_3,0x000000068504324534db6db6eb6db6db00000000001db6db0000000000000000],

  ["ghassanid_king", "Phylarch Amr III ibn al-Numan", "Amr III ibn al-Numan", tf_hero, 0, reserved, fac_commoners,[itm_arabian_horse_d,itm_heavy_greaves,itm_long_cataphract_mail,itm_heavy_lance,itm_battle_axe,itm_sarranid_horseman_helmet],knight_attrib_5,wp(300),knight_skills_5|knows_trainer_1|knows_trainer_3,0x0000000c2e00f143491b6a58a36db6db00000000001d36d20000000000000000],

  ["salihid_king", "Phylarch Ziyad", "Ziyad", tf_hero, 0, reserved, fac_commoners,[itm_arabian_horse_d,itm_heavy_greaves,itm_long_cataphract_mail,itm_heavy_lance,itm_battle_axe,itm_burgh_helmet_1],knight_attrib_5,wp(300),knight_skills_5|knows_trainer_1|knows_trainer_3,0x0000000c2e0114c4491b6a58a36db6db00000000001d36d20000000000000000],

  ["persian_champion","Champion","NPC Quest Character",tf_hero|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,[itm_sassanid_heavy_mail_1,itm_sassanid_simple_boots_2,itm_sarranid_horseman_helmet],def_attrib_lvl_18|level(19),wp(250),knows_ironflesh_10|knows_power_strike_7,persian_face_1, persian_face_2],
  #isaurian rival king
  ["isaurian_leader","Regulus Lydius","NPC Quest Character",tf_hero|tf_guarantee_boots|tf_guarantee_armor, no_scene, 0, fac_outlaws,[itm_mid_generic_mail_7,itm_christies_helmet_1,itm_round_shield_roman_13,itm_ankle_boots,itm_battle_axe],def_attrib_lvl_20|level(19),wp(250),knows_ironflesh_10|knows_power_strike_7,0x000000078a0091436adc8647136db6db00000000001eb6b10000000000000000],

  ["isaurian_king","Regulus Trokondas","NPC Quest Character",tf_hero, no_scene, 0, fac_kingdom_2,[itm_roman_lorum_fasciari_1,itm_roman_shirt_9,itm_pannonian_cap_fur_2],def_attrib_lvl_13|level(19),wp(250),knows_ironflesh_10|knows_power_strike_7,0x0000000dcf00a5045aa38dd65c7526db00000000001db6a10000000000000000],
  
  ["germanic_pagan_quest_npc","NPC Quest Placeholder","NPC Quest Placeholder",tf_hero|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,[itm_roman_shirt_2,itm_ankle_boots,itm_sword_medieval_a],def_attrib_lvl_20|level(19),wp(180),knows_ironflesh_10|knows_power_strike_7,germanic_face_1, germanic_face_2],
  
  ["bagaudae_king","Basilius","Basilius",tf_hero|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, scn_roman_fort|entry(2), reserved, fac_forest_bandits,[itm_wrapping_boots,itm_mid_generic_mail_23,itm_leather_gloves,itm_intercisa_helmet_2,itm_arabian_sword_a,itm_round_shield_roman_1],def_attrib_lvl_23|level(24),wp(260),knows_ironflesh_8|knows_power_strike_6|knows_shield_3|knows_athletics_5,0x000000059f0060824adb6db6db6daae500000000001db6ea0000000000000000],

  ["bagaudae_leader","Bagauda Leader","Bagadua Leaders",tf_hero, no_scene, 0, fac_forest_bandits,[itm_wrapping_boots,itm_mid_generic_mail_15,itm_intercisa_helmet_2,itm_arabian_sword_a,itm_concave_shield_green_2],def_attrib_lvl_23|level(24),wp(230),knows_ironflesh_8|knows_power_strike_6|knows_shield_3|knows_athletics_5,0x000000059f0060824adb6db6db6daae500000000001db6ea0000000000000000],

  ["priscus","Priscus","Priscus",tf_hero, 0, reserved, fac_kingdom_2,[itm_ankle_boots,itm_roman_shirt_3],def_attrib_lvl_20|level(19),wp(180),knows_ironflesh_2|knows_power_strike_2|knows_athletics_2,0x0000000f3600314f46da91b6636db6db00000000001db6d20000000000000000],

  ["bigilas","Bigilas","Bigilas",tf_hero|tf_allways_fall_dead, no_scene, 0, fac_kingdom_2,[itm_roman_lorum_fasciari_1,itm_roman_shirt_4,itm_mid_roman_mail_3,itm_sword_khergit_4,itm_concesti_helmet,itm_concave_shield_roman_20],def_attrib_lvl_23|level(30),wp(260),knows_ironflesh_10|knows_power_strike_6|knows_shield_5|knows_athletics_7,0x000000090700408736db6d5b234db6db00000000001db6a20000000000000000],

  ["bigilas_son","Bigilas's Son","Bigilas's Son",tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,[itm_wrapping_boots,itm_roman_shirt_9,itm_sword_khergit_3],def_attrib_lvl_30|level(30),wp_one_handed(260)|wp_two_handed(200)|wp_polearm(260)|wp_throwing(250)|wp_archery(180),knows_ironflesh_8|knows_power_strike_7|knows_shield_5|knows_athletics_7|knows_riding_8|knows_power_draw_6|knows_horse_archery_5,0x00000001860050cb36db6d5b234db6db00000000001db69c0000000000000000],

  ["greek_scythaboo","Old Merchant","Old Merchant",tf_hero|tf_is_merchant, scn_court_of_attila|entry(1), reserved, fac_commoners,[itm_sassanid_cavalry_boots_1,itm_kaftan_hunnic_2],def_attrib_lvl_30|level(30),wp(260),knows_ironflesh_10|knows_power_strike_5|knows_power_draw_5|knows_shield_5|knows_athletics_7,0x00000009ff00508e36db8ec8e34db6db00000000001db68a0000000000000000],

  ["maximinus","Maximinus","Maximinus",tf_hero,0,0, fac_commoners,[itm_ankle_boots,itm_roman_shirt_14,itm_sword_viking_3_small],def_attrib_lvl_30|level(30),wp(260),knows_ironflesh_7|knows_power_strike_5|knows_shield_5|knows_athletics_7,0x00000009ff000004549b7246e396451b00000000001db6e20000000000000000],

  ["ildico","Ildico","Ildico",tf_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_wrapping_boots,itm_dress_4],def_attrib_lvl_9|level(8),wp(110),knows_common|knows_athletics_3|knows_power_draw_2|knows_power_strike_1|knows_wound_treatment_2,0x000000000e004006484a70036989a49c00000000001d53520000000000000000],

  ["attilas_bastard_son","Oebarsius","Oebarsius",tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,[itm_nomad_boots,itm_rich_tunic_3,itm_hunnic_spatha,itm_khergit_bow,itm_khergit_arrows,itm_concave_shield_leather_small_3],def_attrib_lvl_30|level(30),wp_one_handed(260)|wp_two_handed(200)|wp_polearm(260)|wp_throwing(250)|wp_archery(180),knows_ironflesh_8|knows_power_strike_7|knows_shield_5|knows_athletics_7|knows_riding_8|knows_power_draw_6|knows_horse_archery_5,0x000000000b00c2895495b240db25352200000000001db6e10000000000000000],

  #reused as gangstalker leader
  ["attilas_bastard_son_duel","Berchios","Berchios",tf_hero|tf_allways_fall_dead, no_scene, reserved, fac_commoners,[itm_nomad_boots,itm_steppe_plated_armor_2,itm_pannonhalma_spatha,itm_khergit_bow,itm_khergit_arrows,itm_concave_shield_leather_small_3,itm_turaevo_helmet],def_attrib_lvl_30|level(30),wp_one_handed(260)|wp_two_handed(200)|wp_polearm(260)|wp_throwing(250)|wp_archery(180),knows_ironflesh_8|knows_power_strike_7|knows_shield_5|knows_athletics_7|knows_riding_8|knows_power_draw_6|knows_horse_archery_5,0x000000000b00c2895495b240db25352200000000001db6e10000000000000000],

  ["onogur_leader","Hunnic Chief","Hunnic Chief",tf_hero|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,[itm_nomad_boots,itm_steppe_plated_armor_3,itm_sword_viking_c_long,itm_heavy_lance,itm_khergit_bow,itm_khergit_arrows,itm_steppe_horse],def_attrib_lvl_20|level(21),wp_one_handed(210)|wp_two_handed(180)|wp_polearm(200)|wp_throwing(180)|wp_archery(150),knows_ironflesh_4|knows_power_strike_5|knows_athletics_5|knows_riding_8|knows_power_draw_6|knows_horse_archery_5,0x0000000d9f0083cb555b6ec5124db6db00000000001d36ea0000000000000000],

  ["wayland","Wayland the Smith","Wayland the Smith",tf_hero|tf_is_merchant, scn_waylands_smithy|entry(1), reserved, fac_commoners,[itm_leather_apron,itm_wrapping_boots],def_attrib_lvl_23|level(23),wp(200),knows_common|knows_inventory_management_10,0x00000008c400414b36db6db6db6db6db00000000001db6e20000000000000000],

  ["donar_berserker","Berserker","Berserkers",tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged, no_scene, reserved, fac_commoners,[itm_jarid,itm_jarid,itm_jarid,itm_donars_club,itm_mid_generic_mail_21,itm_wrapping_boots,itm_fernpass_helmet_2],def_attrib_lvl_30|level(30),wp(400),knows_ironflesh_10|knows_power_strike_10|knows_shield_5|knows_athletics_10|knows_power_throw_10,germanic_face_1,germanic_face_2],

  #part 1: alexandria's pagans - characters that will be at the school, and will participate in a small battle with christians in defense of their school
  ["roman_pagan_quest_npc_1","Messius Phoebus Severus","Messius Phoebus Severus",tf_hero,0,0, fac_commoners,[itm_roman_shirt_2,itm_roman_boots_1,itm_sword_medieval_a],def_attrib_lvl_20|level(21),wp(210),knows_ironflesh_8|knows_power_strike_8|knows_athletics_6,0x00000003270060045b5bae36abadb6db00000000001db6e20000000000000000], #is armed

  ["roman_pagan_quest_npc_2","Pamprepius","Pamprepius",tf_hero,0,0, fac_commoners,[itm_roman_shirt_7,itm_ankle_boots],def_attrib_lvl_20|level(19),wp(180),knows_ironflesh_6|knows_power_strike_3|knows_athletics_5,0x000000002700214544db75b8a295b6db00000000001d36db0000000000000000], #was 17

  ["roman_pagan_quest_npc_3","Asclepigenia","Asclepigenia",tf_female|tf_hero,0,0,fac_commoners,[itm_ankle_boots,itm_dress_4],def_attrib_lvl_9|level(8),wp(110),knows_common|knows_athletics_3|knows_power_draw_2|knows_power_strike_1|knows_wound_treatment_2,0x000000002f0c701026db9337b5b63cda00000000001dc4120000000000000000], #was 27

  ["roman_pagan_quest_npc_4","Aedesia","Aedesia",tf_female|tf_hero,0,0,fac_commoners,[itm_ankle_boots,itm_dress_4],def_attrib_lvl_9|level(8),wp(110),knows_common|knows_athletics_3|knows_power_draw_2|knows_power_strike_1|knows_wound_treatment_2,0x0000000c271020060d127142ec97491400000000001d49a60000000000000000], #older

  ["roman_pagan_quest_npc_5","Pusaeus","Pusaeus",tf_hero,0,0, fac_commoners,[itm_roman_shirt_2,itm_ankle_boots],def_attrib_lvl_20|level(19),wp(180),knows_ironflesh_6|knows_power_strike_3|knows_athletics_5,0x00000002b100504144db75b8a295b6db00000000001db6dd0000000000000000], 
  #will be in athens
  ["roman_pagan_quest_npc_6","Severianus of Damascus","Severianus of Damascus",tf_hero,0,0, fac_commoners,[itm_roman_shirt_14,itm_ankle_boots],def_attrib_lvl_20|level(19),wp(180),knows_ironflesh_6|knows_power_strike_3|knows_athletics_5,0x0000000d290010c236db6db6db6db6db00000000001db6db0000000000000000], 

  ["roman_pagan_quest_npc_7","Marcellus the Book Merchant","Marcellus",tf_hero,0,0, fac_commoners,[itm_roman_shirt_13,itm_roman_boots_1],def_attrib_lvl_20|level(19),wp(180),knows_ironflesh_6|knows_power_strike_3|knows_athletics_5,0x0000000d290050855b5b9236d36db6db00000000001db7040000000000000000], 

  ["proclus","Proclus the Successor","Proclus Lycius",tf_hero|tf_is_merchant,scn_roman_villa|entry(2),reserved,fac_commoners,[itm_roman_shirt_8,itm_roman_boots_1],def_attrib_lvl_20|level(19),wp(180),knows_ironflesh_6|knows_power_strike_3|knows_athletics_5,0x000000076d00408258d38e471b6db6e400000000001d36e20000000000000000],

  ["mithraist_leader","Pater","Pater",tf_hero,scn_mithraeum|entry(2),reserved, fac_commoners,[itm_roman_shirt_2,itm_ankle_boots,itm_woolen_cap_2],def_attrib_lvl_20|level(19),wp(180),knows_ironflesh_6|knows_power_strike_3|knows_athletics_5,roman_face_1, roman_face_2],

  ["mithras_cultist","Syndexioi","Syndexioi",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_roman_pagans,[itm_dagger] + tunics_roman_civilian + tunics_romans_low + tunics_romans_officer + tunics_romans_military + shoes_roman, def_attrib_lvl_18|level(17),wp(160),knows_lvl_18_inf|knows_shield_4,roman_face_1, roman_face_2],

  ["mithraist_iniate","Julius","Julius",tf_hero|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,[itm_roman_shirt_12,itm_ankle_boots],def_attrib_lvl_18|level(19),wp(180),knows_ironflesh_6|knows_power_strike_3|knows_athletics_5,roman_face_1, roman_face_2],

  ["chrisitan_zealot","Zealot","Zealots",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_club] + shoes_roman + tunics_roman_civilian + tunics_romans_low + pannonian_hats,
   def_attrib_lvl_18|level(17),wp(130),knows_common|knows_athletics_2|knows_power_strike_2|knows_ironflesh_2,roman_face_1, roman_face_2],  

  ["mithras_bandit","Mysterious Man","lol he's a bandit",tf_hero, no_scene,0, fac_outlaws,[itm_wrapping_boots,itm_mid_generic_mail_7,(itm_intercisa_helmet_1,imod_battered),itm_battle_axe_2,itm_round_shield_gray_1],def_attrib_lvl_30|level(30),wp(230),knows_common|knows_riding_3|knows_athletics_4|knows_ironflesh_8|knows_shield_4|knows_power_throw_4,0x00000001b80032473ac49738206626b200000000001da7660000000000000000, bandit_face2],

  ["axumite_merchant","Kaleb","Kaleb",tf_hero|tf_is_merchant, scn_town_21_castle|entry(11), reserved, fac_commoners,[itm_nomad_boots,itm_roman_shirt_10],def_attrib_lvl_30|level(30),wp(260),knows_ironflesh_7|knows_power_strike_5|knows_shield_5|knows_athletics_7,0x0000000c3f0160c6535c6dba3271a51300000000001d36ca0000000000000000],

  ["persian_hero","Pahlavan","Pahlavans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_culture_6,[itm_sassanid_heavy_mail_1,itm_sarranid_elite_armor,itm_sassanid_simple_boots_2,itm_tsaritsyno_1_light,itm_tsaritsyno_1_veiled,itm_sassanid_cataphract_helmet_1,itm_sassanid_cataphract_helmet_2,itm_sassanid_cataphract_helmet_3,itm_sassanid_greatsword],def_attrib_lvl_30|level(30),wp_one_handed(230)|wp_two_handed(250),knows_ironflesh_8|knows_power_strike_6|knows_athletics_5,persian_face_1, persian_face_2],

  ["pilos_cultist","Mysterious Man","Mysterious Man",tf_hero,0,reserved, fac_commoners,[itm_roman_shirt_2,itm_roman_lorum_fasciari_1,itm_pilos_helmet],def_attrib_lvl_18|level(19),wp(180),knows_ironflesh_6|knows_power_strike_3|knows_athletics_5, 0x00000006370023427f135636f5e8af2000000000001e36c20000000000000000],

  ["antiquarian","Antiquarian","Antiquarian",tf_hero|tf_is_merchant,0,reserved, fac_commoners,[itm_roman_lorum_fasciari_1,itm_roman_shirt_16,itm_pannonian_cap_6],def_attrib_lvl_18|level(19),wp(180),knows_ironflesh_6|knows_power_strike_3|knows_athletics_5, 0x0000000b1600308236db6db6db6db6db00000000001db6db0000000000000000],

  #RELIGIOUS HEADS - Chalcedonian
  ["jerusalem_patriarch","Patriarch Juvenal of Jerusalem","Juvenal of Jerusalem",tf_hero|tf_guarantee_boots|tf_guarantee_armor, 0, reserved, fac_roman_christians,[itm_wrapping_boots,itm_robes_church],def_attrib|level(3),wp(80),knows_wound_treatment_3,0x0000000fc00004823adb6dcadb6dbadb00000000001db6dc0000000000000000],

  ["bishop_of_rome","Pope Leo","Pope Leo",tf_hero|tf_guarantee_boots|tf_guarantee_armor, 0, reserved, fac_roman_christians,[itm_wrapping_boots,itm_robes_church],def_attrib|level(3),wp(80),knows_wound_treatment_3,0x0000000fff000085469b6e46e36db6db00000000001db6d10000000000000000],

  ["bishop_of_alexandria","Patriarch Proterius of Alexandria","Proterius of Alexandria",tf_hero|tf_guarantee_boots|tf_guarantee_armor, 0, reserved, fac_roman_christians,[itm_wrapping_boots,itm_robes_church],def_attrib|level(3),wp(80),knows_wound_treatment_3,0x0000000c24003144369b6e46e28db6db00000000001db6dc0000000000000000],

  ["bishop_of_constantinople","Patriarch Anatolius of Constantinople","Anatolius of Constantinople",tf_hero|tf_guarantee_boots|tf_guarantee_armor, 0, reserved, fac_roman_christians,[itm_wrapping_boots,itm_robes_church],def_attrib|level(3),wp(80),knows_wound_treatment_3,0x0000000ffc0014c3369b69a6e28db6db00000000001db6dc0000000000000000],

  ["bishop_of_antioch","Patriarch Basil of Antioch","Basil of Antioch",tf_hero|tf_guarantee_boots|tf_guarantee_armor, 0, reserved, fac_roman_christians, [itm_wrapping_boots,itm_robes_church],def_attrib|level(3),wp(80),knows_wound_treatment_3,0x0000000c2e00214e369b69a6e28db6db00000000001db6dc0000000000000000],
  #Bishop of Aquae flavae
  ["hydatius","Hydatius","Hydatius",tf_hero, 0, reserved, fac_kingdom_1,[itm_wrapping_boots,itm_robes_church],def_attrib_lvl_20|level(19),wp(180),knows_ironflesh_2|knows_power_strike_2|knows_athletics_2,0x0000000a270040871b9472485248ab1200000000001da6e00000000000000000],

  ["chalcedonian_bishops_end","Bishop","Bishop",tf_hero, 0, reserved, fac_roman_christians, [itm_wrapping_boots,itm_robes_church],def_attrib|level(3),wp(80),knows_wound_treatment_3,0x0000000c2e00214e369b69a6e28db6db00000000001db6dc0000000000000000],

  #COPTIC
  ["coptic_pope","Pope Timothy II of Alexandria","Pope Timothy II of Alexandria",tf_hero|tf_guarantee_boots|tf_guarantee_armor, 0, reserved, fac_coptic_christians,
   [itm_wrapping_boots,itm_robes_church],
   def_attrib|level(3),wp(80),knows_wound_treatment_3,0x00000003f50040c2529b6926e28db6db00000000001db7120000000000000000],

  ["palace_farmer","Farmer","Farmers",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_wrapping_boots,itm_ankle_boots,itm_simple_shoes,itm_linen_tunic,itm_shirt,itm_linen_shirt_22,itm_linen_shirt_12,itm_linen_shirt_5,itm_linen_shirt_9,itm_straw_hat,itm_leather_cap,itm_new_hood_c,itm_new_hood_d,itm_brown_hood1],
   def_attrib|level(6),wp(90)|wp_firearm(90),knows_common,man_face_1, man_face_2],

  ["old_palace_farmer","Old Farmer","Old Farmer",tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_is_merchant, scn_diocletians_palace|entry(1), reserved, fac_kingdom_1,[itm_ankle_boots,itm_coarse_tunic],def_attrib_lvl_13|level(10),wp(100),knows_ironflesh_2|knows_power_strike_2|knows_athletics_2,0x0000000fcf00418536db6db6db6db6db00000000001db6db0000000000000000],

  ["diocletian","Mysterious Man","Mysterious Man",tf_hero|tf_guarantee_boots|tf_guarantee_armor, scn_diocletians_palace|entry(11), reserved, fac_kingdom_1,[itm_roman_emperor_boots,itm_roman_emperor_tunic,itm_crown_1],def_attrib_lvl_30|level(30),wp(400),knows_ironflesh_10|knows_power_strike_10|knows_athletics_10,0x0000000ffb0090854a5974b71b71492300000000001db6e30000000000000000],

  ["german_bard","Frumirus","Frumirus",tf_hero|tf_guarantee_boots|tf_guarantee_armor, scn_town_23_tavern|entry(12), reserved, fac_commoners,[itm_wrapping_boots,itm_linen_shirt_9],def_attrib|level(3),wp(80),knows_common,0x000000049e002408555b6db69badb2db00000000001db71a0000000000000000],

  ["visigothic_merchant","Arvandus the Merchant","Arvandus the Merchant",tf_hero|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor, 0, reserved, fac_commoners,[itm_wrapping_boots,itm_generic_tunic_10,itm_sword_viking_3_small],def_attrib_lvl_20|level(20),wp(180),knows_common|knows_ironflesh_10,0x00000009de0014045da27236ea8db6db00000000001db4cd0000000000000000],

  #name is actually going to be Hilarius Pupienus Maximus, haha funnie
  ["nero_larper","Nero Redivivus","Nero Redivivus",tf_hero|tf_allways_fall_dead, 0, reserved, fac_commoners,[itm_roman_lorum_fasciari_4,itm_roman_shirt_9,itm_sword_khergit_4],def_attrib_lvl_30|level(40),wp(400),knows_common|knows_ironflesh_10|knows_power_strike_10,0x00000000310010035adc7236dc8dbada00000000001d36e50000000000000000],

  ["nero_larper_poet","Longinus","Longinus",tf_hero, 0, reserved, fac_commoners,[itm_roman_lorum_fasciari_3,itm_roman_military_tunic_4,itm_pannonian_cap_6,itm_sword_medieval_b],def_attrib_lvl_13|level(13),wp(130),knows_common|knows_ironflesh_10,0x00000006f100558436db71c6dc8db6da00000000001d36d30000000000000000],

  ["gandhara_mercenary","Gandhara Mercenary","Gandhara Mercenaries",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_bearded_axe_2,itm_strange_armor,itm_bandana1,itm_bandana2,itm_padded_coif,itm_turban,itm_strong_bow,itm_barbed_arrows,itm_wicker_round_shield],
   def_attrib_lvl_28|level(28),wp_one_handed (250) | wp_two_handed (250) | wp_polearm (200) | wp_archery (160) | wp_crossbow (75) | wp_throwing (100),knows_common|knows_shield_5|knows_ironflesh_8|knows_power_strike_8|knows_athletics_8|knows_power_draw_4,persian_face_1, persian_face_2], 

  ["suebi_rebel", "placeholder", "placeholder", tf_hero, no_scene, 0, fac_faltras_suebi,[],knight_attrib_5,wp(300),knight_skills_5|knows_trainer_1|knows_trainer_3,0x00000004060563c844dc91b6eb6db6db00000000001db6e30000000000000000],

  ["suebi_rebel_king", "Faltras", "Faltras", tf_hero, no_scene, 0, fac_faltras_suebi,[],knight_attrib_5,wp(300),knight_skills_5|knows_trainer_1|knows_trainer_3,0x00000007400001c41cdb6daaec6db6db00000000001e37250000000000000000],

  ["vandal_raider_leader", "Visimar", "Visimar", tf_hero, no_scene, 0, fac_kingdom_15,[itm_wrapping_boots,itm_mid_generic_mail_5,itm_intercisa_helmet_gilded_1,itm_concave_shield_germanic_4,itm_beja_spatha],knight_attrib_5,wp_one_handed(300)|wp_two_handed(250)|wp_polearm(230)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100)|wp_firearm(100),knight_skills_5|knows_trainer_1|knows_trainer_3,0x000000080c0042825d5b8a1b1b6db91b00000000001db7610000000000000000],

  ["silingi_chief", "Silingi Chief", "Silingi Chief", tf_hero, scn_silingi_village|entry(1), reserved, fac_commoners,[itm_khergit_leather_boots,itm_mid_generic_mail_22,itm_sword_viking_3_small],knight_attrib_5,wp_one_handed(280)|wp_two_handed(250)|wp_polearm(230)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100)|wp_firearm(100),knight_skills_5|knows_trainer_1|knows_trainer_3,0x0000000d640030894adb6536dbb12b1b00000000001db6e50000000000000000],

  ["venedi_chief", "Venedi Chief", "Venedi Chief", tf_hero, no_scene, 0, fac_commoners,[itm_wrapping_boots,itm_mid_generic_mail_2,itm_kalhkni_helmet_mail,itm_round_shield_red_3,itm_pannonhalma_spatha],knight_attrib_5,wp_one_handed(300)|wp_two_handed(250)|wp_polearm(230)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100)|wp_firearm(100),knight_skills_5|knows_trainer_1|knows_trainer_3,0x000000080c0042825d5b8a1b1b6db91b00000000001db7610000000000000000],

  ["zamb_man","Zamb Man","Zamb Men",tf_hero,0,0,fac_commoners,
   [itm_wrapping_boots,itm_linen_shirt_12], #oh lord why did I do this???
   def_attrib_lvl_35|level(40),wp(400),knows_ironflesh_10|knows_power_strike_10|knows_power_throw_10|knows_athletics_10|knows_shield_10|knows_wound_treatment_3|knows_surgery_8,0x000000058000001071db6f183af5b6db00000000001eb7470000000000000000],

  #agrippinus quest
  ["agrippinus", "Agrippinus", "Agrippinus", tf_hero, no_scene, 0, fac_commoners,[itm_roman_lorum_fasciari_1,itm_roman_shirt_3,itm_arabian_sword_b],knight_attrib_5,wp(300),knight_skills_5|knows_trainer_1|knows_trainer_3,0x00000000d900500236db6e46936db2da00000000001d36e20000000000000000],

  ["lupicinus","Abbot Lupicinus","Lupicinus",tf_hero, 0, reserved, fac_roman_christians,[itm_wrapping_boots,itm_robes_church], def_attrib|level(3),wp(80),knows_wound_treatment_3,0x000000096700908f330dae56d26db6db00000000001db6f50000000000000000],

  #severinus quest
  ["severinus_companion","Aurelios","Aurelios",tf_hero, no_scene, 0, fac_commoners,[itm_roman_lorum_fasciari_2,itm_457_mail_shirt_3,itm_sword_khergit_4,itm_late_roman_spear_1,itm_pannonian_cap_fur_2],def_attrib_lvl_25|level(25),wp(220),knows_ironflesh_8|knows_power_strike_6|knows_shield_6|knows_athletics_6,0x00000008ec0090c51a5b92b8916dbb1200000000001d268a0000000000000000],

  
  
  #zerkon
  ["zerkon","Zercon","Zercon",tf_dwarf|tf_hero, no_scene, 0, fac_commoners,[itm_wrapping_boots,itm_roman_shirt_15],def_attrib_lvl_13|level(10),wp(130),knows_common|knows_ironflesh_2|knows_power_strike_3|knows_athletics_8,0x0000000a3f0130025693e6d92dd649ea00000000001e25060000000000000000],

  ["aurelian_fanatic","Crazy Old Man","Crazy Old Man",tf_hero, no_scene, 0, fac_commoners,[itm_roman_lorum_fasciari_4,itm_roman_shirt_4],def_attrib_lvl_13|level(12),wp(140),knows_common,0x0000000ffe0031505c4abeb86c6db51a00000000001fe96f0000000000000000],

#shitpost troops
  ["shitpost_unit","Langobardi Crossbow Cataphract Looter","Langobardi Crossbow Cataphract Looters",tf_mounted|tf_guarantee_all,0,0,fac_commoners,
   [itm_heavy_greaves,itm_coat_of_plates_red,itm_arabian_armor_b,itm_gultlingen_helmet_plume,itm_kalhkni_helmet_mail,itm_kalhkni_helmet_1,itm_kalhkni_helmet_2,itm_heavy_lance,itm_sword_viking_1,itm_light_crossbow,itm_steel_bolts,itm_cataphract_horse_1,itm_cataphract_horse_4,itm_half_cataphract_horse_7],
   def_attrib_lvl_30|level(30),wp(260),knows_ironflesh_10|knows_power_strike_10|knows_shield_5|knows_athletics_6|knows_riding_5|knows_horse_archery_6,germanic_face_1, germanic_face_2],  

  ["cimmerian_tribesman","Cimmerian Tribesman","Cimmerian Tribesmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners, #meme unit
   [itm_simple_shoes,itm_wrapping_boots,itm_hunter_boots,itm_rawhide_coat3,itm_rawhide_coat6,itm_rawhide_coat7,itm_rawhide_coat8,itm_rawhide_coat9,itm_rawhide_coat10,itm_fernpass_helmet_1,itm_fernpass_helmet_2,itm_fernpass_helmet_3,itm_two_handed_axe,itm_spear_sword,itm_long_bow,itm_war_bow,itm_strong_bow,itm_germanic_arrows,itm_germanic_arrows]+hats_german,
   def_attrib_lvl_20|level(21),wp_one_handed (220) | wp_two_handed (240) | wp_polearm (240) | wp_archery (200) | wp_crossbow (120) | wp_throwing (200),knows_berserker|knows_power_draw_6,germanic_face_1, germanic_face_2],
  #riders of rohan
  ["northern_germanic_horse_archer","N. Germanic Horse Archer","N. Germanic Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_culture_12,
   [itm_khergit_leather_boots,itm_wrapping_boots,itm_simple_shoes,itm_generic_subarmalis_4,itm_generic_subarmalis_9,itm_long_mail_new_8,itm_mid_generic_mail_8,itm_mid_generic_mail_15,itm_mid_generic_mail_19,itm_medium_scale_2,itm_fernpass_helmet_2,itm_triveres_mail,itm_burgh_helmet_1,itm_woolen_cap,itm_woolen_cap_b,itm_heavy_lance,itm_khergit_bow,itm_khergit_arrows,itm_beja_spatha,itm_round_shield_roman_small_1,itm_concave_shield_germanic_small_2,itm_concave_shield_germanic_small_6,itm_concave_shield_germanic_small_7,itm_concave_shield_germanic_small_8,itm_concave_shield_germanic_small_9,itm_concave_shield_germanic_small_18]+horses_alans_2,
   def_attrib_lvl_25|level(25),wp_one_handed(220)|wp_two_handed(210)|wp_polearm(220)|wp_throwing(200)|wp_archery(200),knows_common|knows_riding_7|knows_power_throw_4|knows_horse_archery_7|knows_power_strike_7|knows_power_draw_7|knows_ironflesh_8,germanic_face_1, germanic_face_2],
  #secret old style roman legionaries
  ["miles_legionis","Miles Legionis","Milites Legionis",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_culture_empire,
   [itm_roman_lorum_fasciari_1,itm_roman_lorum_fasciari_5,itm_roman_leather_boots_1,itm_roman_leather_boots_2,itm_roman_leather_boots_3,itm_roman_greaves_1,itm_roman_greaves_5,itm_roman_greaves_manica_1,itm_roman_greaves_manica_3,itm_457_mail_shirt_1,itm_457_mail_short_1,itm_roman_light_scale_1,itm_sword_viking_3_small,itm_spiculum,itm_spiculum,itm_oval_shield_1,itm_oval_shield_red_1,itm_florence_helmet_1],
   def_attrib_lvl_25|level(25),wp_one_handed(210)|wp_two_handed(190)|wp_polearm(190)|wp_archery(120)|wp_throwing(210),knows_lvl_23_inf|knows_shield_6|knows_power_strike_4,roman_face_1, roman_face_2],

####finnsburh quest characters
#DANI
  ["dani_hocing","Hnaef Hocing","Hnaef Hocing",tf_hero,0,0,fac_minor_dani,
   [itm_obenaltendorf_shoes_1,itm_mid_generic_mail_19,itm_tarasovsky_782,itm_indesheim_spatha_rich,itm_concave_shield_germanic_10],
   def_attrib_lvl_25|level(25),wp_one_handed(210)|wp_two_handed(190)|wp_polearm(190)|wp_archery(120)|wp_throwing(210),knows_lvl_23_inf|knows_shield_6|knows_power_strike_4,0x0000000196000509291a692862adb6db00000000001db6e90000000000000000],
  ["dani_sigeferth","Sigeferth","Sigeferth",tf_hero,0,0,fac_minor_dani,
   [itm_wrapping_boots,itm_mid_generic_mail_24,itm_drengsted_helmet_mail,itm_indesheim_spatha_rich,itm_round_shield_germanic_19],
   def_attrib_lvl_25|level(25),wp_one_handed(210)|wp_two_handed(190)|wp_polearm(190)|wp_archery(120)|wp_throwing(210),knows_lvl_23_inf|knows_shield_6|knows_power_strike_4,0x00000001890010ca291189286251b2da00000000001db6e80000000000000000],
  ["dani_eaha","Eaha","Eaha",tf_hero,0,0,fac_minor_dani,
   [itm_simple_shoes,itm_cloaked_tunic_1,itm_germanic_cap_1,itm_sword_medieval_c_long,itm_round_shield_germanic_12],
   def_attrib_lvl_25|level(25),wp_one_handed(210)|wp_two_handed(190)|wp_polearm(190)|wp_archery(120)|wp_throwing(210),knows_lvl_23_inf|knows_shield_6|knows_power_strike_4,0x00000005ab00144136536e586951b4e300000000001d36a30000000000000000],
  ["dani_hengest","Hengest Wodning","Hengest Wodning",tf_hero,0,0,fac_minor_dani,
   [itm_obenaltendorf_shoes_2,itm_mid_generic_mail_29,itm_tsaritsyno_2_2,itm_samson_spatha_2_rich,itm_concave_shield_germanic_25],
   def_attrib_lvl_25|level(25),wp_one_handed(210)|wp_two_handed(190)|wp_polearm(190)|wp_archery(120)|wp_throwing(210),knows_lvl_23_inf|knows_shield_6|knows_power_strike_4,0x00000006800044c759522e454b91231a00000000001eb6e20000000000000000],
  ["dani_ordlaf","Ordlaf","Ordlaf",tf_hero,0,0,fac_minor_dani,
   [itm_obenaltendorf_shoes_2,itm_cloaked_generic_tunic_3,itm_concave_shield_germanic_21,itm_angon_1,itm_long_seax_3],
   def_attrib_lvl_25|level(25),wp_one_handed(210)|wp_two_handed(190)|wp_polearm(190)|wp_archery(120)|wp_throwing(210),knows_lvl_23_inf|knows_shield_6|knows_power_strike_4,0x00000004e300508836536d3793aca91b00000000001db6d30000000000000000],
  ["dani_guthlaf","Guthlaf","Guthlaf",tf_hero,0,0,fac_minor_dani,
   [itm_ankle_boots,itm_cloaked_tunic_9,itm_round_shield_germanic_19,itm_war_spear_2],
   def_attrib_lvl_25|level(25),wp_one_handed(210)|wp_two_handed(190)|wp_polearm(190)|wp_archery(120)|wp_throwing(210),knows_lvl_23_inf|knows_shield_6|knows_power_strike_4,0x000000074f00030f46536e7a2951b2d900000000001db6da0000000000000000],
##FINNS
  ["finn_garulf","Garulf Guthlafing","Garulf Guthlafing",tf_hero,0,0,fac_minor_frisians,
   [itm_simple_shoes,itm_mid_generic_mail_18,itm_fernpass_helmet_2,itm_battle_axe,itm_concave_shield_germanic_22],
   def_attrib_lvl_25|level(25),wp_one_handed(210)|wp_two_handed(190)|wp_polearm(190)|wp_archery(120)|wp_throwing(210),knows_lvl_23_inf|knows_shield_6|knows_power_strike_4,0x00000001a700424b5b1189286251b8e300000000001db68c0000000000000000],

  ["finn_guthere","Guthere","Guthere",tf_hero,0,0,fac_minor_frisians,
   [itm_wrapping_boots,itm_cloaked_tunic_2,itm_woolen_cap_2,itm_round_shield_germanic_11,itm_sword_khergit_3],
   def_attrib_lvl_25|level(25),wp_one_handed(210)|wp_two_handed(190)|wp_polearm(190)|wp_archery(120)|wp_throwing(210),knows_lvl_23_inf|knows_shield_6|knows_power_strike_4,0x000000058f00644256536e586951b4e300000000001db6ea0000000000000000],

  ["finn_aethelbald","Aethelbald","Aethelbald",tf_hero,0,0,fac_minor_frisians,
   [itm_ankle_boots,itm_mid_generic_mail_27,itm_triveres_leather,itm_round_shield_germanic_22,itm_sword_viking_a_long],
   def_attrib_lvl_25|level(25),wp_one_handed(210)|wp_two_handed(190)|wp_polearm(190)|wp_archery(120)|wp_throwing(210),knows_lvl_23_inf|knows_shield_6|knows_power_strike_4,0x00000004c00020451651c248a195a49100000000001d368a0000000000000000],

  ["finn_hildeburh","Hildeburh","Hildeburh",tf_hero|tf_hero,0,0,fac_minor_frisians,
   [itm_wrapping_boots,itm_dress_5],
   def_attrib,wp(60),knows_common,woman_face_1, woman_face_2],
####finnsburh quest characters END

#other pagans of importance: Severianus of Damascus

  ##diplomacy begin
  #SB : fixed plural name (hero name), TODO actually use name/gender in hiring dialogues
  ["dplmc_chamberlain","Chamberlain Tullus Vagennius", "Tullus Vagennius",tf_hero|tf_male,0,0,fac_commoners,[itm_linen_shirt_10, itm_ankle_boots], def_attrib|level(10), wp(40),knows_inventory_management_10,0x0000000dfc0c238838e571c8d469c91b00000000001e39230000000000000000],

  ["dplmc_constable","Constable Cassius Carius Collatinus","Cassius Carius Collatinus",tf_hero|tf_male,0,0,fac_commoners,[itm_dplmc_coat_of_plates_red_constable, itm_ankle_boots],
   knight_attrib_4,wp_melee(240),knows_common|knows_shield_5|knows_ironflesh_6|knows_power_strike_5|knows_athletics_4,0x0000000b4b1015054b1b4d591cba28d300000000001e472b0000000000000000],

  ["dplmc_chancellor","Chancellor Marcus Gratius","Marcus Gratius",tf_hero|tf_male,0,0,fac_commoners,[itm_nobleman_outfit, itm_ankle_boots],def_attrib|level(10), wp(40),knows_inventory_management_10, 0x00000009a20c21cf491bad28a28628d400000000001e371a0000000000000000],

  ["dplmc_messenger","Messenger","Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
   [itm_sword_medieval_a,itm_mid_generic_mail_2,itm_intercisa_helmet_plume_2,itm_ankle_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   def_attrib_lvl_30|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7|knows_power_draw_4,roman_face_1, roman_face_2],
  ["dplmc_scout","Scout","Scouts",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
   [itm_sword_medieval_a,itm_mid_generic_mail_2,itm_intercisa_helmet_plume_2,itm_ankle_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   def_attrib_lvl_30|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7|knows_power_draw_4,roman_face_1, roman_face_2],
# recruiter kit begin
  ["dplmc_recruiter","Recruiter","Recruiter",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
   [itm_sword_medieval_a,itm_mid_generic_mail_2,itm_intercisa_helmet_plume_2,itm_ankle_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   def_attrib_lvl_30|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7|knows_power_draw_4,roman_face_1, roman_face_2],
# recruiter kit end

  ##diplomacy end
  ["no_troop","_","the place",tf_hero,0,0,fac_commoners,[],0,0,0,0,0],
  ["gate_aggravator","Gate_is_holding","_", tf_guarantee_armor| tf_guarantee_boots| tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_neutral,
   [itm_empty_body,itm_empty_hands,itm_empty_legs,itm_empty_head],
      str_30|level(80),wp(5),knows_shield_10|knows_ironflesh_10,0,0],

]


#Troop upgrade declarations

upgrade(troops,"farmer", "watchman")
upgrade(troops,"townsman","watchman")

#farmer -> watchman -> iuvenis -> pedes mercenarii
#                   -> mercenary archer 
#eques mercenarii -> eques contarii mercenarii
upgrade2(troops,"watchman","mercenary_swordsman","mercenary_archer")
upgrade(troops,"mercenary_swordsman","hired_blade")
upgrade(troops,"caravan_guard","mercenary_horseman")

#Goths
upgrade(troops,"gothic_freeman","gothic_footman")
upgrade2(troops,"gothic_skirmisher","gothic_mounted_skirmisher","gothic_bowman")
upgrade(troops,"gothic_horseman","gothic_companion")

#eastern germans
upgrade2(troops,"eastern_germanic_skirmisher","eastern_germanic_mounted_skirmisher","eastern_germanic_bowman")
upgrade(troops,"eastern_germanic_spearman","eastern_germanic_retainer")
upgrade(troops,"eastern_germanic_mounted_warrior","eastern_germanic_companion")

#britons
upgrade(troops,"briton_footman","briton_infantry")
upgrade(troops,"briton_horseman","briton_companion")
upgrade(troops,"briton_skirmisher","briton_archer")

#northern germans
upgrade(troops,"northern_germanic_freeman","northern_germanic_warrior")
upgrade(troops,"northern_germanic_warrior","northern_germanic_companion")
upgrade(troops,"northern_germanic_skirmisher","northern_germanic_bowman")

#nothing for the picts lol
#sassanids
upgrade(troops,"sassanid_levy","sassanid_footman")
upgrade(troops,"sassanid_footman","sassanid_armored_footman")
upgrade(troops,"sassanid_skirmisher","sassanid_archer")
upgrade(troops,"sassanid_cavalry","sassanid_cataphract")

upgrade(troops,"daylamite_hillman","daylamite_infantry")

#western germans
upgrade(troops,"western_germanic_freeman","western_germanic_retainer")
upgrade(troops,"western_germanic_retainer","western_germanic_companion")
upgrade(troops,"western_germanic_skirmisher","western_germanic_bowman")

#caucasians
upgrade(troops,"caucasian_skirmisher","caucasian_archer")
upgrade(troops,"caucasian_levy","caucasian_footman")
upgrade(troops,"caucasian_nobleman","caucasian_cataphract")

#romano-mauri
upgrade(troops,"mauri_skirmisher","mauri_mounted_skirmisher")
upgrade(troops,"mauri_mounted_skirmisher","mauri_companion")
upgrade(troops,"mauri_footman","mauri_infantry")

#le huns
upgrade(troops,"hunnic_skirmisher","hunnic_horse_archer")
upgrade(troops,"hunnic_retainer","hunnic_veteran")

#nubians
upgrade(troops,"nubian_bowman","nubian_archer")

#alans
upgrade2(troops,"caucasian_alan_skirmisher","caucasian_alan_footman","caucasian_alan_tribesman")
upgrade(troops,"caucasian_alan_retainer","caucasian_alan_companion")

#basques
upgrade2(troops,"basque_skirmisher","basque_footman","basque_horseman")

#scandanavians
upgrade(troops,"scandinavian_freeman","scandinavian_retainer")
upgrade(troops,"scandinavian_retainer","scandinavian_comes")

#my loves
upgrade(troops,"crimean_gothic_skirmisher","crimean_gothic_mounted_skirmisher")
upgrade(troops,"crimean_gothic_freeman","crimean_gothic_warrior")
upgrade(troops,"crimean_gothic_horseman","crimean_gothic_companion")

#mordens
upgrade(troops,"mordvin_mounted_skirmisher","mordvin_companion")

#arabs
upgrade(troops,"arab_light_cavalry","arab_heavy_cavalry")

upgrade(troops,"forest_bandit_recruit","forest_bandit")
upgrade(troops,"forest_bandit","bagaudae_footman")

upgrade(troops,"steppe_bandit","steppe_rider")
upgrade(troops,"steppe_rider","steppe_cataphract")

#new tree connections ended

upgrade(troops,"looter","robber")
upgrade(troops,"robber","bandit")
upgrade(troops,"bandit","brigand")
upgrade(troops,"pirate","bandit")

upgrade(troops,"manhunter","slave_driver")
upgrade(troops,"slave_driver","slave_hunter")
upgrade(troops,"slave_hunter","slave_crusher")
upgrade(troops,"slave_crusher","slaver_chief")

upgrade(troops,"follower_woman","hunter_woman")
upgrade(troops,"hunter_woman","fighter_woman")

upgrade(troops,"fighter_woman","sword_sister")
upgrade(troops,"refugee","follower_woman")
upgrade(troops,"peasant_woman","follower_woman")

#limitanei
upgrade2(troops,"tiro_limitanei","pedes_limitanei","eques_limitanei")
upgrade(troops,"pedes_limitanei","pedes_psuedo")
upgrade(troops,"eques_limitanei","eques_promoti")
upgrade2(troops,"exculator_limitanei","sagittarius_limitanei","eques_dalmatae")

upgrade(troops,"eques_cataphractarii","eques_clibanarii")

upgrade(troops,"vigilia","pedes_burgarius")

#Foederati Troops
upgrade(troops,"iuvenis_foederatus","miles_foederatus")
upgrade2(troops,"miles_foederatus","optimas_foederatus","eques_alae")

upgrade2(troops,"coptic_youth","coptic_footman","coptic_watchman")
upgrade(troops,"coptic_footman","coptic_guard")

upgrade(troops,"mountain_bandit","isaurian_warrior")
upgrade(troops,"isaurian_warrior","isaurian_infantry")

upgrade(troops,"heruli_slave","heruli_warrior")

upgrade(troops,"pedes_votadini","eques_votadini")

upgrade(troops,"samaritan_zealot","samaritan_rebel")

upgrade(troops,"gallaecian_rebel","gallaecian_militia")
upgrade(troops,"gallaecian_militia","gallaecian_guard")

upgrade(troops,"western_alan_rider","western_alan_lancer")
upgrade(troops,"western_alan_lancer","western_alan_cataphract")

upgrade(troops,"gallic_infantry","gallic_bodyguard")
upgrade(troops,"warenae_armatus","warenae_optimas")
upgrade(troops,"langobard_retainer","langobard_companion")

upgrade(troops,"bosphor_recruit","bosphor_archer")

upgrade(troops,"eques_laeti_taifali","eques_alae_taifali")