from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

#from compiler import *
####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################
def heraldic(item_tableau):
  return (ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", item_tableau, ":agent_no", ":troop_no")])
def add_mesh(item_meshes):
  cur_meshes = [(store_trigger_param_1, ":agent_no"),(ge, ":agent_no", 0)]
  for mesh in item_meshes if not isinstance(item_meshes, basestring) else [item_meshes]:
    cur_meshes.append((str_store_string, s1, mesh))
    cur_meshes.append((cur_item_add_mesh, s1))
  return (ti_on_init_item, cur_meshes)
def reskin(item_material):
  return (ti_on_init_item, [(str_store_string, s1, item_material),(cur_item_set_material, s1, 0),])
# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn

imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_thick
imodbits_leather = imodbits_cloth | imodbit_sturdy | imodbit_hardened
#new armor modifiers
imodbits_mail = imodbit_rusty | imodbit_battered | imodbit_thick | imodbit_reinforced 
imodbits_scale = imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced | imodbit_lordly

imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered |imodbit_masterwork
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy 
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent

#culture groups
culture_roman = [fac_culture_3,fac_culture_empire,fac_culture_11] #Romans, Britons, Mauri
culture_germanic = [fac_culture_2,fac_culture_4,fac_culture_7,fac_culture_minor_4,fac_culture_minor_7] #Northern, Western, Eastern
culture_gothic = [fac_culture_1,fac_culture_minor_8] #goths
culture_celtic = [fac_culture_3,fac_culture_5,fac_culture_minor_1] #picts, britons
culture_hunnic = [fac_culture_12] #huns
culture_alan = [fac_culture_16,fac_culture_minor_9] #alans
culture_caucasian = [fac_culture_8] #caucasians
culture_sassanid = [fac_culture_6] #sassanids
culture_african = [fac_culture_15] #nubians

items = [
# item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset
 ["no_item","INVALID ITEM", [("invalid_item",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

 ["tutorial_spear", "Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear_upstab, 0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
 ["tutorial_club", "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
 ["tutorial_battle_axe", "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile],
 ["tutorial_bolts","Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(55)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile],
 ["tutorial_short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 0 , weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(49) | thrust_damage(12 ,  pierce  ),imodbits_bow ],
 ["tutorial_crossbow", "Crossbow", [("roman_crossbow_1",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
 ["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
 ["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
 ["tutorial_shield", "Round Shield", [("round_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
 ["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
 ["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],
 ["tutorial_sword", "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
 ["tutorial_axe", "Axe", [("iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

 ["tutorial_dagger","Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(40)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],


 ["horse_meat","Horse Meat", [("raw_meat",0)], itp_type_goods|itp_consumable|itp_food, 0, 12,weight(40)|food_quality(30)|max_ammo(100),imodbits_none],
# Items before this point are hardwired and their order should not be changed!
 ["practice_sword", "Sword", [("feltwell_spatha",0),("feltwell_spatha_scabbard", ixmesh_carry),], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 243 , weight(1.5)|spd_rtng(89) | weapon_length(95)|swing_damage(23 , blunt) | thrust_damage(20 ,  blunt),imodbits_sword_high ],
 ["heavy_practice_sword","Heavy Practice Axe", [("vikingaxeb",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
   21, weight(6.25)|spd_rtng(84)|weapon_length(82)|swing_damage(30,blunt)|thrust_damage(24,blunt),imodbits_none],
 ["practice_dagger", "Hatchet", [("bb_hand_axe",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 24 , weight(2) | spd_rtng(88) | weapon_length(75) | swing_damage(24, blunt) | thrust_damage(0, pierce), imodbits_axe],
 ["practice_axe", "Practice Axe", [("bb_hand_axe",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 24 , weight(2) | spd_rtng(88) | weapon_length(75) | swing_damage(24, blunt) | thrust_damage(0, pierce), imodbits_axe],
 ["arena_axe", "Hand Axe", [("bb_hand_axe",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 137 , weight(1.5)|spd_rtng(91) | weapon_length(49)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["arena_sword", "Sword", [("feltwell_spatha",0),("feltwell_spatha_scabbard", ixmesh_carry),], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 243 , weight(1.5)|spd_rtng(89) | weapon_length(95)|swing_damage(23 , blunt) | thrust_damage(20 ,  blunt),imodbits_sword_high ],
 ["arena_sword_two_handed",  "Two-Handed Axe", [("vikingaxeb",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 670 , weight(2.75)|spd_rtng(84) | weapon_length(82)|swing_damage(30 , blunt) | thrust_damage(24 ,  blunt),imodbits_sword_high ],
 ["arena_lance",  "Lance", [("hasta_new_r1",0)], itp_type_polearm|itp_offset_lance|itp_primary|itp_wooden_parry, itc_spear_upstab|itcf_carry_spear,
 90 , weight(2.5)|spd_rtng(92) | weapon_length(180)|swing_damage(20 , blunt) | thrust_damage(26 ,  blunt),imodbits_polearm ],
 ["arena_spear",  "Spear", [("roman_spear_2",0)], itp_type_polearm|itp_offset_lance|itp_primary|itp_wooden_parry, itc_spear_upstab|itcf_carry_spear,
 90 , weight(1.5)|spd_rtng(96) | weapon_length(134)|swing_damage(20 , blunt) | thrust_damage(26 ,  blunt),imodbits_polearm ],
 ["practice_staff","Practice Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(2.5)|spd_rtng(103) | weapon_length(118)|swing_damage(18,blunt) | thrust_damage(18,blunt),imodbits_none],
 ["practice_lance","Practice Cavalry Spear", [("hasta_new_r1",0)], itp_type_polearm|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_spear_upstab, 18,weight(4.25)|spd_rtng(96)|weapon_length(180)|swing_damage(20,blunt)|thrust_damage(28,blunt),imodbits_none],
 ["practice_shield", "Wooden Practice Shield", [("round_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield ],
 ["practice_bow","Practice Bow", [("bb_hunting_bow_v2",0), ("bb_hunting_bow_v2_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_bow ],
##                                                     ("hunting_bow",0)],                  itp_type_bow|itp_two_handed|itp_primary|itp_attach_left_hand, itcf_shoot_bow, 4,weight(1.5)|spd_rtng(90)|shoot_speed(40)|thrust_damage(19,blunt),imodbits_none],
 ["practice_crossbow", "Practice Crossbow", [("roman_crossbow_1",0)], itp_type_crossbow |itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|spd_rtng(42)| shoot_speed(68) | thrust_damage(32,blunt)|max_ammo(1),imodbits_crossbow],
 ["practice_javelin", "Practice Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_primary|itp_next_item_as_melee,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 0, weight(5) | spd_rtng(91) | shoot_speed(28) | thrust_damage(27, blunt) | max_ammo(50) | weapon_length(75), imodbits_thrown],
 ["practice_javelin_melee", "practice_javelin_melee", [("javelin",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_staff, 0, weight(1)|difficulty(0)|spd_rtng(91) |swing_damage(12, blunt)| thrust_damage(14,  blunt)|weapon_length(75),imodbits_polearm ],
 ["practice_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(10)|weapon_length(0),imodbits_thrown ],
 ["practice_throwing_daggers_100_amount", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(100)|weapon_length(0),imodbits_thrown ],
# ["cheap_shirt","Cheap Shirt", [("shirt",0)], itp_type_body_armor|itp_covers_legs, 0, 4,weight(1.25)|body_armor(3),imodbits_none],
 ["practice_horse","Practice Horse", [("normal_horse32",0)], itp_type_horse, 0, 37,body_armor(10)|horse_speed(40)|horse_maneuver(37)|horse_charge(14),imodbits_none],
 ["practice_arrows","Practice Arrows", [("arena_arrow_new_v2",0),("flying_missile",ixmesh_flying_ammo),("quiver_new", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile],
## ["practice_arrows","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo)], itp_type_arrows, 0, 31,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_none],
 ["practice_bolts","Practice Bolts", [("bolt_new",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(49),imodbits_missile],
 ["practice_arrows_10_amount","Practice Arrows", [("arrow_new",0),("flying_missile",ixmesh_flying_ammo),("quiver_new", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(10),imodbits_missile],
 ["practice_arrows_100_amount","Practice Arrows", [("arrow_new",0),("flying_missile",ixmesh_flying_ammo),("quiver_new", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(100),imodbits_missile],
 ["practice_bolts_9_amount","Practice Bolts", [("bolt_new",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(9),imodbits_missile],
 ["practice_boots", "Practice Boots", [("boot_nomad_a",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10), imodbits_cloth ],
 ["red_tourney_armor","Red Tourney Armor", [("tourn_armor_a",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["blue_tourney_armor","Blue Tourney Armor", [("mail_shirt",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["green_tourney_armor","Green Tourney Armor", [("leather_vest",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["gold_tourney_armor","Gold Tourney Armor", [("padded_armor",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["red_tourney_helmet","Red Tourney Helmet",[("flattop_helmet",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["blue_tourney_helmet","Blue Tourney Helmet",[("segmented_helm",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["green_tourney_helmet","Green Tourney Helmet",[("hood_c",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["gold_tourney_helmet","Gold Tourney Helmet",[("hood_a",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],

["arena_shield_red", "Shield", [("round_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield ],
["arena_shield_blue", "Shield", [("round_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield ],
["arena_shield_green", "Shield", [("round_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield ],
["arena_shield_yellow", "Shield", [("round_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  295 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield ],

["arena_armor_white", "Arena Armor White", [("mid_generic_mail_2",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_red", "Arena Armor Red", [("mid_generic_mail_3",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_blue", "Arena Armor Blue", [("mid_generic_mail_1",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_green", "Arena Armor Green", [("mid_generic_mail_4",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_yellow", "Arena Armor Yellow", [("mid_generic_mail_5",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_tunic_white", "Arena Tunic White ", [("arena_tunicW_new",0)], itp_type_body_armor |itp_covers_legs ,0, 47 , weight(2)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(10), imodbits_cloth ],
["arena_tunic_red", "Arena Tunic Red", [("arena_tunicR_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(10), imodbits_cloth ],
["arena_tunic_blue", "Arena Tunic Blue", [("arena_tunicB_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(10), imodbits_cloth ],
["arena_tunic_green", "Arena Tunic Green", [("arena_tunicG_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(10), imodbits_cloth ],
["arena_tunic_yellow", "Arena Tunic Yellow", [("arena_tunicY_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(10), imodbits_cloth ],
#headwear
["arena_helmet_red", "Arena Helmet Red", [("old_spangenhelmaven",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_blue", "Arena Helmet Blue", [("old_spangenhelmaven",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_green", "Arena Helmet Green", [("old_spangenhelmaven",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_yellow", "Arena Helmet Yellow", [("old_spangenhelmaven",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_white", "Arena Helmet White", [("old_spangenhelmaven",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_red", "Arena Helmet Red", [("old_spangenhelmaven",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_blue", "Arena Helmet Blue", [("old_spangenhelmaven",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_green", "Arena Helmet Green", [("old_spangenhelmaven",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_yellow", "Arena Helmet Yellow", [("old_spangenhelmaven",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_white", "Arena Helmet", [("light_ridge",0)], itp_type_head_armor|itp_fit_to_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_red", "Arena Helmet", [("light_ridge",0)], itp_type_head_armor|itp_fit_to_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_blue", "Arena Helmet", [("light_ridge",0)], itp_type_head_armor|itp_fit_to_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_green", "Arena Helmet", [("light_ridge",0)], itp_type_head_armor|itp_fit_to_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_yellow", "Arena Helmet", [("light_ridge",0)], itp_type_head_armor|itp_fit_to_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_red", "Arena Helmet", [("sassanid_helmet_cloth_2",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_blue", "Arena Helmet", [("sassanid_helmet_cloth_2",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_green", "Arena Helmet", [("sassanid_helmet_cloth_2",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_yellow", "Arena Helmet", [("sassanid_helmet_cloth_2",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],

# A treatise on The Method of Mechanical Theorems Archimedes

#This book must be at the beginning of readable books
 ["book_tactics","De Re Militari", [("book_a",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],
 ["book_persuasion","Rhetorica ad Herennium", [("book_b",0)], itp_type_book, 0, 5000,weight(2)|abundance(100),imodbits_none],
 ["book_leadership","Orationes In Catilinam", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
 ["book_intelligence","Politeia", [("book_e",0)], itp_type_book, 0, 2900,weight(2)|abundance(100),imodbits_none],
 ["book_trade","Itinerarium Alexandri", [("book_f",0)], itp_type_book, 0, 3100,weight(2)|abundance(100),imodbits_none],
 ["book_weapon_mastery", "De Bello Civili", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
 ["book_engineering","De Architectura", [("book_open",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],
 ["book_proclus_1","Elements of Theology", [("book_e",0)], itp_type_book, 0, 3500,weight(2)|abundance(10),imodbits_none],

#Reference books
#This book must be at the beginning of reference books
 ["book_wound_treatment_reference","Corpus Hippocraticum", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
 ["book_training_reference","De Bello Gallico", [("book_open",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
 ["book_surgery_reference","De Arte Medica", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],

 #other trade goods (first one is spice)
 ["spice","Spice", [("spice_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none ],
 ["salt","Salt", [("salt_sack",0)], itp_merchandise|itp_type_goods, 0, 235,weight(50)|abundance(120),imodbits_none],

 ["oil","Oil", [("trade_goods_oil",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 450,weight(50)|abundance(60)|max_ammo(50),imodbits_none],

 ["pottery","Pottery", [("trade_goods_pottery",0)], itp_merchandise|itp_type_goods, 0, 100,weight(50)|abundance(90),imodbits_none],

 ["raw_flax","Flax Bundle", [("raw_flax",0)], itp_merchandise|itp_type_goods, 0, 150,weight(40)|abundance(90),imodbits_none],
 ["linen","Linen", [("trade_goods_linen",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbits_none],

 ["wool","Wool", [("wool_sack",0)], itp_merchandise|itp_type_goods, 0, 130,weight(40)|abundance(90),imodbits_none],
 ["wool_cloth","Wool Cloth", [("trade_goods_wool",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbits_none],

 ["raw_silk","Raw Silk", [("trade_goods_silk",0)], itp_merchandise|itp_type_goods, 0, 600,weight(30)|abundance(90),imodbits_none],
 ["raw_dyes","Dyes", [("dyes",0)], itp_merchandise|itp_type_goods, 0, 200,weight(10)|abundance(90),imodbits_none],
 ["velvet","Fine Cloth", [("trade_goods_tyrian",0)], itp_merchandise|itp_type_goods, 0, 1025,weight(40)|abundance(30),imodbits_none],

 ["iron","Iron", [("iron_ore",0)], itp_merchandise|itp_type_goods, 0,264,weight(60)|abundance(60),imodbits_none],
 ["tools","Tools", [("medieval_hammer_a",0)], itp_merchandise|itp_type_goods, 0, 410,weight(50)|abundance(90),imodbits_none],

 ["raw_leather","Hides", [("trade_goods_leather",0)], itp_merchandise|itp_type_goods, 0, 120,weight(40)|abundance(90),imodbits_none],
 ["leatherwork","Leatherwork", [("trade_goods_leatherwork_frame",0)], itp_merchandise|itp_type_goods, 0, 220,weight(40)|abundance(90),imodbits_none],

 ["raw_date_fruit","Date Fruit", [("date_inventory",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 120,weight(40)|food_quality(10)|max_ammo(10),imodbits_none],
 ["furs","Furs", [("fur_pack",0)], itp_merchandise|itp_type_goods, 0, 391,weight(40)|abundance(90),imodbits_none],

 #New trade goods
 ["gold_jewelry","Gold Jewelry", [("gold_rings",0)], itp_merchandise|itp_type_goods, 0, 945,weight(30)|abundance(50),imodbits_none],

 ["ivory","ivory", [("ivory",0)], itp_merchandise|itp_type_goods, 0, 1020,weight(30)|abundance(10),imodbits_none],

 ["wine","Wine", [("amphora_slim",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 220,weight(30)|abundance(60)|max_ammo(50),imodbits_none],
 ["ale","Ale", [("trade_goods_ale_barrel",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 120,weight(30)|abundance(70)|max_ammo(50),imodbits_none],

# ["dry_bread", "wheat_sack", itp_type_goods|itp_consumable, 0, slt_none,view_goods,95,weight(2),max_ammo(50),imodbits_none],
#foods (first one is smoked_fish)
 ["smoked_fish","Smoked Fish", [("smoked_fish",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 65,weight(15)|abundance(110)|food_quality(50)|max_ammo(150),imodbits_none],
 ["cheese","Cheese", [("cheese_b",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(6)|abundance(110)|food_quality(40)|max_ammo(100),imodbits_none],
 ["honey","Honey", [("honey_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 220,weight(5)|abundance(110)|food_quality(40)|max_ammo(100),imodbits_none],
 ["sausages","Sausages", [("sausages",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(10)|abundance(110)|food_quality(40)|max_ammo(100),imodbits_none],
 ["cabbages","Cabbages", [("cabbage",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 30,weight(15)|abundance(110)|food_quality(40)|max_ammo(150),imodbits_none],
 ["dried_meat","Dried Meat", [("smoked_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(15)|abundance(100)|food_quality(70)|max_ammo(100),imodbits_none],
 ["apples","Fruit", [("apple_basket",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 44,weight(20)|abundance(110)|food_quality(40)|max_ammo(100),imodbits_none],
 ["raw_grapes","Grapes", [("grapes_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 75,weight(40)|abundance(90)|food_quality(10)|max_ammo(50),imodbits_none], #x2 for wine
 ["raw_olives","Olives", [("olive_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 100,weight(40)|abundance(90)|food_quality(10)|max_ammo(50),imodbits_none], #x3 for oil
 ["grain","Grain", [("wheat_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 30,weight(30)|abundance(110)|food_quality(40)|max_ammo(200),imodbits_none],

 ["cattle_meat","Beef", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 80,weight(20)|abundance(100)|food_quality(80)|max_ammo(100),imodbits_none],
 ["bread","Bread", [("trade_goods_bread",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 50,weight(30)|abundance(110)|food_quality(40)|max_ammo(200),imodbits_none],
 ["chicken","Chicken", [("chicken",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 95,weight(10)|abundance(110)|food_quality(40)|max_ammo(100),imodbits_none],
 ["pork","Pork", [("pork",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(15)|abundance(100)|food_quality(70)|max_ammo(100),imodbits_none],
 ["butter","Butter", [("butter_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 150,weight(6)|abundance(110)|food_quality(40)|max_ammo(120),imodbits_none],


 #Would like to remove flour altogether and reduce chicken, pork and butter (perishables) to non-trade items. Apples could perhaps become a generic "fruit", also representing dried fruit and grapes
 # Armagan: changed order so that it'll be easier to remove them from trade goods if necessary.
#************************************************************************************************
# ITEMS before this point are hardcoded into item_codes.h and their order should not be changed!
#************************************************************************************************

# Quest Items

 ["siege_supply","Supplies", [("trade_goods_barrel",0)], itp_type_goods, 0, 96,weight(40)|abundance(250),imodbits_none],
 ["quest_wine","Wine", [("amphora_slim",0)], itp_type_goods, 0, 46,weight(40)|abundance(60)|max_ammo(100),imodbits_none],
 ["quest_ale","Ale", [("trade_goods_barrel",0)], itp_type_goods, 0, 31,weight(40)|abundance(70)|max_ammo(100),imodbits_none],

 ["heirloom","Old Ring", [("quest_ring",0)], itp_unique|itp_type_goods, 0, 10,weight(1.2)|abundance(10),imodbits_none],
 ["quest_gold","Gold", [("gold_ore",0)], itp_type_goods, 0, 2000,weight(20)|abundance(10),imodbits_none],
 ["amber","Amber", [("amber",0)], itp_type_goods, 0, 765,weight(20)|abundance(10),imodbits_none],

# Horses: sumpter horse/ pack horse, saddle horse, steppe horse, warm blood, geldling, stallion,   war mount, charger,
# Carthorse, hunter, heavy hunter, hackney, palfrey, courser, destrier.
#Mounts/Horses
["camel","Camel", [("bedyin_camel_a",0)], itp_merchandise|itp_type_horse, 0, 650,abundance(40)|hit_points(210)|body_armor(12)|difficulty(3)|horse_speed(34)|horse_maneuver(46)|horse_charge(40)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], culture_sassanid ],
["bareback_horse_1","Horse", [("bareback_horse_1",0)], itp_merchandise|itp_type_horse, 0, 1000,abundance(30)|hit_points(110)|body_armor(2)|difficulty(3)|horse_speed(46)|horse_maneuver(42)|horse_charge(12)|horse_scale(92),imodbits_horse_basic, [], [fac_culture_11,fac_culture_15] ], #nubians, mauri

#New half cataphract horses!
#roman
["half_cataphract_horse_1","Half-Cataphract Horse", [("half_cataphract_horse_1",0)], itp_merchandise|itp_type_horse, 0, 4300,abundance(30)|hit_points(170)|body_armor(30)|difficulty(3)|horse_speed(39)|horse_maneuver(42)|horse_charge(35)|horse_scale(98),imodbits_horse_basic|imodbit_champion, [], culture_roman+culture_sassanid+culture_caucasian ],
["half_cataphract_horse_2","Half-Cataphract Horse", [("half_cataphract_horse_2",0)], itp_merchandise|itp_type_horse, 0, 4300,abundance(30)|hit_points(170)|body_armor(30)|difficulty(3)|horse_speed(39)|horse_maneuver(42)|horse_charge(35)|horse_scale(98),imodbits_horse_basic|imodbit_champion, [], culture_roman+culture_sassanid+culture_caucasian ],
#roman, sassanid, alan, caucasian
["half_cataphract_horse_3","Half-Cataphract Horse", [("half_cataphract_horse_3",0)], itp_merchandise|itp_type_horse, 0, 4300,abundance(30)|hit_points(170)|body_armor(30)|difficulty(3)|horse_speed(39)|horse_maneuver(42)|horse_charge(35)|horse_scale(98),imodbits_horse_basic|imodbit_champion, [], culture_roman+culture_sassanid+culture_caucasian ],
["half_cataphract_horse_4","Half-Cataphract Horse", [("half_cataphract_horse_4",0)], itp_merchandise|itp_type_horse, 0, 4300,abundance(30)|hit_points(170)|body_armor(30)|difficulty(3)|horse_speed(39)|horse_maneuver(42)|horse_charge(35)|horse_scale(98),imodbits_horse_basic|imodbit_champion, [], culture_roman+culture_sassanid+culture_caucasian ],
#alan, hunnic?
["half_cataphract_horse_5","Half-Cataphract Horse", [("half_cataphract_horse_5",0)], itp_merchandise|itp_type_horse, 0, 4300,abundance(30)|hit_points(170)|body_armor(30)|difficulty(3)|horse_speed(39)|horse_maneuver(42)|horse_charge(35)|horse_scale(98),imodbits_horse_basic|imodbit_champion, [], culture_hunnic+culture_alan+culture_caucasian ],
["half_cataphract_horse_6","Half-Cataphract Horse", [("half_cataphract_horse_6",0)], itp_merchandise|itp_type_horse, 0, 4300,abundance(30)|hit_points(170)|body_armor(30)|difficulty(3)|horse_speed(39)|horse_maneuver(42)|horse_charge(35)|horse_scale(98),imodbits_horse_basic|imodbit_champion, [], culture_hunnic+culture_alan+culture_caucasian ],
#mail, "generic"
["half_cataphract_horse_7","Half-Cataphract Horse", [("half_cataphract_horse_7",0)], itp_merchandise|itp_type_horse, 0, 4300,abundance(30)|hit_points(170)|body_armor(30)|difficulty(3)|horse_speed(39)|horse_maneuver(42)|horse_charge(35)|horse_scale(98),imodbits_horse_basic|imodbit_champion, [], culture_roman+culture_sassanid+culture_caucasian ],
#more romans
["half_cataphract_horse_8","Half-Cataphract Horse", [("half_cataphract_horse_8",0)], itp_merchandise|itp_type_horse, 0, 4300,abundance(30)|hit_points(170)|body_armor(30)|difficulty(3)|horse_speed(39)|horse_maneuver(42)|horse_charge(35)|horse_scale(98),imodbits_horse_basic|imodbit_champion, [], culture_roman+culture_sassanid+culture_caucasian ],

#new full barded cataphract horse
#used by the various emperors
["warhorse_sarranid","Rich Cataphract Horse", [("cataphract_horse_5_1",0)], itp_type_horse, 0, 7500,abundance(10)|hit_points(165)|body_armor(50)|difficulty(4)|horse_speed(36)|horse_maneuver(42)|horse_charge(45)|horse_scale(99),imodbits_horse_basic|imodbit_champion ],
["warhorse_steppe","Steppe Cataphract Horse", [("horse1",0)], itp_merchandise|itp_type_horse, 0, 6500,abundance(25)|hit_points(150)|body_armor(40)|difficulty(4)|horse_speed(36)|horse_maneuver(50)|horse_charge(40)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], culture_hunnic+culture_alan+culture_caucasian ],
#mail
["cataphract_horse_1","Cataphract Horse", [("cataphract_horse_1",0)], itp_merchandise|itp_type_horse, 0, 6500,abundance(20)|hit_points(160)|body_armor(45)|difficulty(4)|horse_speed(36)|horse_maneuver(42)|horse_charge(45)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], culture_roman+culture_sassanid+culture_caucasian ],
#roman scale
["cataphract_horse_2","Cataphract Horse", [("cataphract_horse_2",0)], itp_merchandise|itp_type_horse, 0, 6500,abundance(20)|hit_points(160)|body_armor(45)|difficulty(4)|horse_speed(36)|horse_maneuver(42)|horse_charge(45)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], culture_roman+culture_sassanid+culture_caucasian ],
["cataphract_horse_3","Cataphract Horse", [("cataphract_horse_3",0)], itp_merchandise|itp_type_horse, 0, 6500,abundance(20)|hit_points(160)|body_armor(45)|difficulty(4)|horse_speed(36)|horse_maneuver(42)|horse_charge(45)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], culture_roman+culture_sassanid+culture_caucasian ],
#scale
["cataphract_horse_4","Cataphract Horse", [("cataphract_horse_4",0)], itp_merchandise|itp_type_horse, 0, 6500,abundance(20)|hit_points(160)|body_armor(45)|difficulty(4)|horse_speed(36)|horse_maneuver(42)|horse_charge(45)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], culture_roman+culture_sassanid+culture_caucasian ],
["cataphract_horse_5","Cataphract Horse", [("cataphract_horse_5",0)], itp_merchandise|itp_type_horse, 0, 6500,abundance(20)|hit_points(160)|body_armor(45)|difficulty(4)|horse_speed(36)|horse_maneuver(42)|horse_charge(45)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], culture_roman+culture_sassanid+culture_caucasian ],

["imperial_courser","Koursor", [("roman_courser",0)], itp_merchandise|itp_type_horse, 0, 4050,abundance(60)|body_armor(12)|hit_points(100)|difficulty(3)|horse_speed(48)|horse_maneuver(40)|horse_charge(22)|horse_scale(96),imodbits_horse_basic|imodbit_champion, [], culture_roman ],
["courser","Koursor", [("normal_horse32",0)], itp_merchandise|itp_type_horse, 0, 4050,abundance(70)|body_armor(12)|hit_points(100)|difficulty(3)|horse_speed(48)|horse_maneuver(40)|horse_charge(22)|horse_scale(96),imodbits_horse_basic|imodbit_champion],

["imperial_saddle_horse_1","Equus", [("roman_horse_1",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic, [], culture_roman ],
["imperial_saddle_horse_2","Equus", [("roman_horse_2",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic, [], culture_roman ],
["imperial_saddle_horse_3","Equus", [("roman_horse_3",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic, [], culture_roman ],
["imperial_saddle_horse_4","Equus", [("roman_horse_4",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic, [], culture_roman ],

["saddle_horse","Horse", [("normal_horse8",0),("normal_horse17",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["saddle_horse_2","Horse", [("gallic_horse_1",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["saddle_horse_3","Horse", [("gallic_horse_2",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["saddle_horse_4","Horse", [("gallic_horse_3",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["saddle_horse_5","Horse", [("WRoman1",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["saddle_horse_6","Horse", [("WRoman2",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],

 #brytenwalda horses
["normal_horse11","Horse", [("normal_horse11",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["normal_horse12","Horse", [("normal_horse12",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["normal_horse13","Horse", [("normal_horse13",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["normal_horse14","Horse", [("normal_horse14",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["normal_horse15","Horse", [("normal_horse15",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["normal_horse16","Horse", [("normal_horse16",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["normal_horse17","Horse", [("normal_horse17",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["normal_horse21","Horse", [("normal_horse21",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["normal_horse22","Horse", [("normal_horse22",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["normal_horse27","Horse", [("normal_horse27",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["normal_horse23","Horse", [("normal_horse23",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["normal_horse24","Horse", [("normal_horse24",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["normal_horse25","Horse", [("normal_horse25",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["normal_horse26","Horse", [("normal_horse26",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["normal_horse30","Horse", [("normal_horse30",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(40)|hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
 #work horses
["sumpter_horse",   "Work Horse", [("sumpter_horse",0)],  itp_merchandise|itp_type_horse, 0, 900,abundance(60)|body_armor(8)|hit_points(140)|difficulty(1)|horse_speed(40)|horse_maneuver(35)|horse_charge(17)|horse_scale(96),imodbits_horse_basic],
["arabian_horse_b2","Work Horse", [("normal_horse3",0)], itp_merchandise|itp_type_horse, 0, 900,abundance(60)|body_armor(8)|hit_points(140)|difficulty(1)|horse_speed(40)|horse_maneuver(35)|horse_charge(17)|horse_scale(96),imodbits_horse_basic],
["arabian_horse_a3","Work Horse", [("normal_horse4",0)], itp_merchandise|itp_type_horse, 0, 900,abundance(60)|body_armor(8)|hit_points(140)|difficulty(1)|horse_speed(40)|horse_maneuver(35)|horse_charge(17)|horse_scale(96),imodbits_horse_basic],
["arabian_horse_b3","Work Horse", [("normal_horse5",0)], itp_merchandise|itp_type_horse, 0, 900,abundance(60)|body_armor(8)|hit_points(140)|difficulty(1)|horse_speed(40)|horse_maneuver(35)|horse_charge(17)|horse_scale(96),imodbits_horse_basic],
["arabian_horse_a4","Work Horse", [("normal_horse6",0)], itp_merchandise|itp_type_horse, 0, 900,abundance(60)|body_armor(8)|hit_points(140)|difficulty(1)|horse_speed(40)|horse_maneuver(35)|horse_charge(17)|horse_scale(96),imodbits_horse_basic],
["courser4",        "Work Horse", [("normal_horse7",0)],       itp_merchandise|itp_type_horse, 0, 900,abundance(60)|body_armor(8)|hit_points(140)|difficulty(1)|horse_speed(40)|horse_maneuver(35)|horse_charge(17)|horse_scale(96),imodbits_horse_basic],
["arabian_horse_b4","Work Horse", [("normal_horse8",0)], itp_merchandise|itp_type_horse, 0, 900,abundance(60)|body_armor(8)|hit_points(140)|difficulty(1)|horse_speed(40)|horse_maneuver(35)|horse_charge(17)|horse_scale(96),imodbits_horse_basic],
["courser5",        "Work Horse", [("normal_horse9",0)],       itp_merchandise|itp_type_horse, 0, 900,abundance(60)|body_armor(8)|hit_points(140)|difficulty(1)|horse_speed(40)|horse_maneuver(35)|horse_charge(17)|horse_scale(96),imodbits_horse_basic],
["normal_horse18",  "Work Horse", [("normal_horse18",0)],  itp_merchandise|itp_type_horse, 0, 700,abundance(60)|body_armor(8)|hit_points(140)|difficulty(1)|horse_speed(40)|horse_maneuver(35)|horse_charge(17)|horse_scale(96),imodbits_horse_basic],
["normal_horse19",  "Work Horse", [("normal_horse19",0)],  itp_merchandise|itp_type_horse, 0, 900,abundance(60)|body_armor(8)|hit_points(140)|difficulty(1)|horse_speed(40)|horse_maneuver(35)|horse_charge(17)|horse_scale(96),imodbits_horse_basic],
["normal_horse20",  "Work Horse", [("normal_horse20",0)],  itp_merchandise|itp_type_horse, 0, 900,abundance(60)|body_armor(8)|hit_points(140)|difficulty(1)|horse_speed(40)|horse_maneuver(35)|horse_charge(17)|horse_scale(96),imodbits_horse_basic],
["normal_horse28",  "Work Horse", [("normal_horse28",0)],  itp_merchandise|itp_type_horse, 0, 900,abundance(60)|body_armor(8)|hit_points(140)|difficulty(1)|horse_speed(40)|horse_maneuver(35)|horse_charge(17)|horse_scale(96),imodbits_horse_basic],

["arabian_horse_a","Arabian Horse", [("ArabBay1",0)], itp_merchandise|itp_type_horse, 0, 1550,abundance(80)|hit_points(110)|body_armor(10)|difficulty(2)|horse_speed(46)|horse_maneuver(50)|horse_charge(16)|horse_scale(96),imodbits_horse_basic|imodbit_champion, [], culture_sassanid ],
["arabian_horse_b","Arabian Horse", [("ArabBay2",0)], itp_merchandise|itp_type_horse, 0, 1550,abundance(80)|hit_points(120)|body_armor(10)|difficulty(3)|horse_speed(46)|horse_maneuver(50)|horse_charge(16)|horse_scale(96),imodbits_horse_basic|imodbit_champion, [], culture_sassanid ],
["arabian_horse_c","Arabian Horse", [("ArabBay3",0)], itp_merchandise|itp_type_horse, 0, 1550,abundance(80)|hit_points(120)|body_armor(10)|difficulty(3)|horse_speed(46)|horse_maneuver(50)|horse_charge(16)|horse_scale(96),imodbits_horse_basic|imodbit_champion, [], culture_sassanid ],
["arabian_horse_d","Arabian Horse", [("ArabBay4",0)], itp_merchandise|itp_type_horse, 0, 1550,abundance(80)|hit_points(120)|body_armor(10)|difficulty(3)|horse_speed(46)|horse_maneuver(50)|horse_charge(16)|horse_scale(96),imodbits_horse_basic|imodbit_champion, [], culture_sassanid ],

["celtic_horse_1","Horse", [("WPict1",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(20)|hit_points(100)|body_armor(9)|difficulty(1)|horse_speed(43)|horse_maneuver(46)|horse_charge(8)|horse_scale(92),imodbits_horse_basic, [], culture_celtic ],
["celtic_horse_2","Horse", [("WPict2",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(20)|hit_points(100)|body_armor(9)|difficulty(1)|horse_speed(43)|horse_maneuver(46)|horse_charge(8)|horse_scale(92),imodbits_horse_basic, [], culture_celtic ],
["steppe_horse","Steppe Horse", [("steppe_horse_new",0)], itp_merchandise|itp_type_horse, 0, 1400,abundance(80)|hit_points(120)|body_armor(10)|difficulty(3)|horse_speed(44)|horse_maneuver(51)|horse_charge(8)|horse_scale(90),imodbits_horse_basic, [], culture_hunnic+culture_alan ],

["hunter","Hunter", [("normal_horse29",0),("normal_horse31",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 1400,abundance(60)|hit_points(160)|body_armor(10)|difficulty(3)|horse_speed(43)|horse_maneuver(44)|horse_charge(24)|horse_scale(90),imodbits_horse_basic|imodbit_champion],
["warhorse","Warhorse", [("warhorse_new",0)], itp_merchandise|itp_type_horse, 0, 4100,abundance(50)|hit_points(190)|body_armor(22)|difficulty(4)|horse_speed(43)|horse_maneuver(42)|horse_charge(30)|horse_scale(100),imodbits_horse_basic|imodbit_champion],
["charger","Warhorse", [("normal_horse19",0)], itp_merchandise|itp_type_horse, 0, 4100,abundance(40)|hit_points(190)|body_armor(22)|difficulty(4)|horse_speed(43)|horse_maneuver(44)|horse_charge(30)|horse_scale(100),imodbits_horse_basic|imodbit_champion ],

#Nisean warhorses
["nisean_roman_1","Nisean Warhorse", [("nisean_roman_1",0)], itp_merchandise|itp_type_horse, 0, 3500,abundance(20)|hit_points(200)|body_armor(20)|difficulty(4)|horse_speed(47)|horse_maneuver(45)|horse_charge(30)|horse_scale(98),imodbits_horse_basic|imodbit_champion, [], culture_roman ],
["nisean_roman_2","Nisean Warhorse", [("nisean_roman_2",0)], itp_merchandise|itp_type_horse, 0, 3500,abundance(20)|hit_points(200)|body_armor(20)|difficulty(4)|horse_speed(47)|horse_maneuver(45)|horse_charge(30)|horse_scale(98),imodbits_horse_basic|imodbit_champion, [], culture_roman ],
["nisean_roman_3","Nisean Warhorse", [("nisean_roman_3",0)], itp_merchandise|itp_type_horse, 0, 3500,abundance(20)|hit_points(200)|body_armor(20)|difficulty(4)|horse_speed(47)|horse_maneuver(45)|horse_charge(30)|horse_scale(98),imodbits_horse_basic|imodbit_champion, [], culture_roman ],

["nisean_cataphract_1","Nisean Cataphract", [("nisean_cataphract_1",0)], itp_merchandise|itp_type_horse, 0, 8000,abundance(20)|hit_points(200)|body_armor(50)|difficulty(4)|horse_speed(40)|horse_maneuver(36)|horse_charge(50)|horse_scale(98),imodbits_horse_basic|imodbit_champion, [], culture_roman+culture_sassanid ],
["nisean_cataphract_2","Nisean Cataphract", [("nisean_cataphract_2",0)], itp_merchandise|itp_type_horse, 0, 8000,abundance(20)|hit_points(200)|body_armor(50)|difficulty(4)|horse_speed(40)|horse_maneuver(36)|horse_charge(50)|horse_scale(98),imodbits_horse_basic|imodbit_champion, [], culture_roman+culture_sassanid ],
["nisean_cataphract_3","Nisean Cataphract", [("nisean_cataphract_3",0)], itp_merchandise|itp_type_horse, 0, 8000,abundance(20)|hit_points(200)|body_armor(50)|difficulty(4)|horse_speed(40)|horse_maneuver(36)|horse_charge(50)|horse_scale(98),imodbits_horse_basic|imodbit_champion, [], culture_roman+culture_sassanid ],
["nisean_cataphract_4","Nisean Cataphract", [("nisean_cataphract_4",0)], itp_merchandise|itp_type_horse, 0, 8000,abundance(20)|hit_points(200)|body_armor(50)|difficulty(4)|horse_speed(40)|horse_maneuver(36)|horse_charge(50)|horse_scale(98),imodbits_horse_basic|imodbit_champion, [], culture_roman+culture_sassanid ],

#Hunnic horses
["hun_horse_1","Hunnic Horse", [("hun_horse_1",0)], itp_merchandise|itp_type_horse, 0, 1500,abundance(70)|hit_points(120)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(55)|horse_charge(10)|horse_scale(90),imodbits_horse_basic, [], culture_hunnic+culture_alan ],
["hun_horse_2","Hunnic Horse", [("hun_horse_2",0)], itp_merchandise|itp_type_horse, 0, 1500,abundance(70)|hit_points(120)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(55)|horse_charge(10)|horse_scale(90),imodbits_horse_basic, [], culture_hunnic+culture_alan ],
["hun_horse_3","Hunnic Horse", [("hun_horse_3",0)], itp_merchandise|itp_type_horse, 0, 1500,abundance(70)|hit_points(120)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(55)|horse_charge(10)|horse_scale(90),imodbits_horse_basic, [], culture_hunnic+culture_alan ],
["hun_horse_4","Hunnic Horse", [("hun_horse_4",0)], itp_merchandise|itp_type_horse, 0, 1500,abundance(70)|hit_points(120)|body_armor(10)|difficulty(2)|horse_speed(44)|horse_maneuver(55)|horse_charge(10)|horse_scale(90),imodbits_horse_basic, [], culture_hunnic+culture_alan ],

["hun_rich_horse_nobard_1","Hunnic Noble Horse", [("hun_rich_horse_nobard_1",0)], itp_merchandise|itp_type_horse, 0, 4050,abundance(50)|body_armor(14)|hit_points(150)|difficulty(3)|horse_speed(45)|horse_maneuver(55)|horse_charge(12)|horse_scale(90),imodbits_horse_basic|imodbit_champion, [], culture_hunnic+culture_alan ],
["hun_rich_horse_nobard_2","Hunnic Noble Horse", [("hun_rich_horse_nobard_2",0)], itp_merchandise|itp_type_horse, 0, 4050,abundance(50)|body_armor(14)|hit_points(150)|difficulty(3)|horse_speed(45)|horse_maneuver(55)|horse_charge(12)|horse_scale(90),imodbits_horse_basic|imodbit_champion, [], culture_hunnic+culture_alan ],
["hun_rich_horse_nobard_3","Hunnic Noble Horse", [("hun_rich_horse_nobard_3",0)], itp_merchandise|itp_type_horse, 0, 4050,abundance(50)|body_armor(14)|hit_points(150)|difficulty(3)|horse_speed(45)|horse_maneuver(55)|horse_charge(12)|horse_scale(90),imodbits_horse_basic|imodbit_champion, [], culture_hunnic+culture_alan ],

["hun_rich_horse_1","Hunnic Barded Horse", [("hun_rich_horse_1",0)], itp_merchandise|itp_type_horse, 0, 6200,abundance(30)|body_armor(30)|hit_points(150)|difficulty(3)|horse_speed(43)|horse_maneuver(52)|horse_charge(28)|horse_scale(90),imodbits_horse_basic|imodbit_champion, [], culture_hunnic+culture_alan ],
["hun_rich_horse_2","Hunnic Barded Horse", [("hun_rich_horse_2",0)], itp_merchandise|itp_type_horse, 0, 6200,abundance(30)|body_armor(30)|hit_points(150)|difficulty(3)|horse_speed(43)|horse_maneuver(52)|horse_charge(28)|horse_scale(90),imodbits_horse_basic|imodbit_champion, [], culture_hunnic+culture_alan ],
["hun_rich_horse_3","Hunnic Barded Horse", [("hun_rich_horse_3",0)], itp_merchandise|itp_type_horse, 0, 6200,abundance(30)|body_armor(30)|hit_points(150)|difficulty(3)|horse_speed(43)|horse_maneuver(52)|horse_charge(28)|horse_scale(90),imodbits_horse_basic|imodbit_champion, [], culture_hunnic+culture_alan ],

#Asturco 
["asturco_germanic_1","Asturco", [("asturco_germanic_1",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(80)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(44)|horse_maneuver(50)|horse_charge(10)|horse_scale(90),imodbits_horse_basic, [], culture_germanic+culture_gothic ],
["asturco_germanic_2","Asturco", [("asturco_germanic_2",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(80)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(44)|horse_maneuver(50)|horse_charge(10)|horse_scale(90),imodbits_horse_basic, [], culture_germanic+culture_gothic ],
["asturco_germanic_3","Asturco", [("asturco_germanic_3",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(80)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(44)|horse_maneuver(50)|horse_charge(10)|horse_scale(90),imodbits_horse_basic, [], culture_germanic+culture_gothic ],

["asturco_roman_1","Asturco", [("asturco_roman_1",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(80)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(44)|horse_maneuver(50)|horse_charge(10)|horse_scale(90),imodbits_horse_basic, [], culture_roman ],
["asturco_roman_2","Asturco", [("asturco_roman_2",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(80)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(44)|horse_maneuver(50)|horse_charge(10)|horse_scale(90),imodbits_horse_basic, [], culture_roman ],
["asturco_roman_3","Asturco", [("asturco_roman_3",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(80)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(44)|horse_maneuver(50)|horse_charge(10)|horse_scale(90),imodbits_horse_basic, [], culture_roman ],

#Camargue
["camargue_germanic_1","Camargue Horse", [("camargue_germanic_1",0)], itp_merchandise|itp_type_horse, 0, 1500,abundance(60)|hit_points(120)|body_armor(10)|difficulty(1)|horse_speed(44)|horse_maneuver(45)|horse_charge(12)|horse_scale(92),imodbits_horse_basic, [], culture_germanic+culture_gothic ],
["camargue_germanic_2","Camargue Horse", [("camargue_germanic_2",0)], itp_merchandise|itp_type_horse, 0, 1500,abundance(60)|hit_points(120)|body_armor(10)|difficulty(1)|horse_speed(44)|horse_maneuver(45)|horse_charge(12)|horse_scale(92),imodbits_horse_basic, [], culture_germanic+culture_gothic ],
["camargue_germanic_3","Camargue Horse", [("camargue_germanic_3",0)], itp_merchandise|itp_type_horse, 0, 1500,abundance(60)|hit_points(120)|body_armor(10)|difficulty(1)|horse_speed(44)|horse_maneuver(45)|horse_charge(12)|horse_scale(92),imodbits_horse_basic, [], culture_germanic+culture_gothic ],

["camargue_roman_1","Camargue Horse", [("camargue_roman_1",0)], itp_merchandise|itp_type_horse, 0, 1500,abundance(70)|hit_points(120)|body_armor(10)|difficulty(1)|horse_speed(44)|horse_maneuver(45)|horse_charge(12)|horse_scale(92),imodbits_horse_basic, [], culture_roman ],
["camargue_roman_2","Camargue Horse", [("camargue_roman_2",0)], itp_merchandise|itp_type_horse, 0, 1500,abundance(70)|hit_points(120)|body_armor(10)|difficulty(1)|horse_speed(44)|horse_maneuver(45)|horse_charge(12)|horse_scale(92),imodbits_horse_basic, [], culture_roman ],
["camargue_roman_3","Camargue Horse", [("camargue_roman_3",0)], itp_merchandise|itp_type_horse, 0, 1500,abundance(70)|hit_points(120)|body_armor(10)|difficulty(1)|horse_speed(44)|horse_maneuver(45)|horse_charge(12)|horse_scale(92),imodbits_horse_basic, [], culture_roman ],

#Iberian Warhorses
["iberian_warhorse_germanic_1","Iberian Warhorse", [("iberian_warhorse_germanic_1",0)], itp_merchandise|itp_type_horse, 0, 3200,abundance(40)|hit_points(170)|body_armor(10)|difficulty(3)|horse_speed(47)|horse_maneuver(45)|horse_charge(20)|horse_scale(92),imodbits_horse_basic, [], culture_germanic+culture_gothic ],
["iberian_warhorse_germanic_2","Iberian Warhorse", [("iberian_warhorse_germanic_2",0)], itp_merchandise|itp_type_horse, 0, 3200,abundance(40)|hit_points(170)|body_armor(10)|difficulty(3)|horse_speed(47)|horse_maneuver(45)|horse_charge(20)|horse_scale(92),imodbits_horse_basic, [], culture_germanic+culture_gothic ],

["iberian_warhorse_roman_1","Iberian Warhorse", [("iberian_warhorse_roman_1",0)], itp_merchandise|itp_type_horse, 0, 3200,abundance(40)|hit_points(170)|body_armor(10)|difficulty(3)|horse_speed(47)|horse_maneuver(45)|horse_charge(20)|horse_scale(92),imodbits_horse_basic, [], culture_roman ],
["iberian_warhorse_roman_2","Iberian Warhorse", [("iberian_warhorse_roman_2",0)], itp_merchandise|itp_type_horse, 0, 3200,abundance(40)|hit_points(170)|body_armor(10)|difficulty(3)|horse_speed(47)|horse_maneuver(45)|horse_charge(20)|horse_scale(92),imodbits_horse_basic, [], culture_roman ],

#Germanic War horses
["westger_warhorse_1","Northern Warhorse", [("westger_warhorse_1",0)], itp_merchandise|itp_type_horse, 0, 3800,abundance(30)|hit_points(190)|body_armor(15)|difficulty(3)|horse_speed(40)|horse_maneuver(35)|horse_charge(30)|horse_scale(90),imodbits_horse_basic, [], culture_germanic ],
["westger_warhorse_2","Northern Warhorse", [("westger_warhorse_2",0)], itp_merchandise|itp_type_horse, 0, 3800,abundance(30)|hit_points(190)|body_armor(15)|difficulty(3)|horse_speed(40)|horse_maneuver(35)|horse_charge(30)|horse_scale(90),imodbits_horse_basic, [], culture_germanic ],

["barb_light_1","Mauri Horse", [("barb_light_1",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(80)|hit_points(120)|body_armor(6)|difficulty(2)|horse_speed(47)|horse_maneuver(55)|horse_charge(12)|horse_scale(90),imodbits_horse_basic, [], [fac_culture_11] ],
["barb_light_2","Mauri Horse", [("barb_light_2",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(80)|hit_points(120)|body_armor(6)|difficulty(2)|horse_speed(47)|horse_maneuver(55)|horse_charge(12)|horse_scale(90),imodbits_horse_basic, [], [fac_culture_11] ],
["barb_light_3","Mauri Horse", [("barb_light_3",0)], itp_merchandise|itp_type_horse, 0, 1340,abundance(80)|hit_points(120)|body_armor(6)|difficulty(2)|horse_speed(47)|horse_maneuver(55)|horse_charge(12)|horse_scale(90),imodbits_horse_basic, [], [fac_culture_11] ],

["barb_1","Mauri Horse", [("barb_1",0)], itp_merchandise|itp_type_horse, 0, 1800,abundance(50)|hit_points(170)|body_armor(10)|difficulty(3)|horse_speed(47)|horse_maneuver(48)|horse_charge(18)|horse_scale(90),imodbits_horse_basic, [], [fac_culture_11] ],
["barb_2","Mauri Horse", [("barb_2",0)], itp_merchandise|itp_type_horse, 0, 1800,abundance(50)|hit_points(170)|body_armor(10)|difficulty(3)|horse_speed(47)|horse_maneuver(48)|horse_charge(18)|horse_scale(90),imodbits_horse_basic, [], [fac_culture_11] ],
["barb_3","Mauri Horse", [("barb_3",0)], itp_merchandise|itp_type_horse, 0, 1800,abundance(50)|hit_points(170)|body_armor(10)|difficulty(3)|horse_speed(47)|horse_maneuver(48)|horse_charge(18)|horse_scale(90),imodbits_horse_basic, [], [fac_culture_11] ],

["barb_cham_1","Mauri Horse", [("barb_cham_1",0)], itp_merchandise|itp_type_horse, 0, 2200,abundance(20)|hit_points(170)|body_armor(18)|difficulty(3)|horse_speed(47)|horse_maneuver(48)|horse_charge(22)|horse_scale(90),imodbits_horse_basic, [], [fac_culture_11] ],
["barb_cham_2","Mauri Horse", [("barb_cham_2",0)], itp_merchandise|itp_type_horse, 0, 2200,abundance(20)|hit_points(170)|body_armor(18)|difficulty(3)|horse_speed(47)|horse_maneuver(48)|horse_charge(22)|horse_scale(90),imodbits_horse_basic, [], [fac_culture_11] ],
["barb_cham_3","Mauri Horse", [("barb_cham_3",0)], itp_merchandise|itp_type_horse, 0, 2200,abundance(20)|hit_points(170)|body_armor(18)|difficulty(3)|horse_speed(47)|horse_maneuver(48)|horse_charge(22)|horse_scale(90),imodbits_horse_basic, [], [fac_culture_11] ],

#both cultures were known for their horses
["frisian_warhorse","Frisian Warhorse", [("normal_horse12",0)], itp_merchandise|itp_type_horse, 0, 3800,abundance(30)|hit_points(170)|body_armor(19)|difficulty(4)|horse_speed(44)|horse_maneuver(43)|horse_charge(23)|horse_scale(96),imodbits_horse_basic|imodbit_champion, [], culture_germanic ],
["thuringian_warhorse","Thuringian Horse", [("normal_horse19",0)], itp_merchandise|itp_type_horse, 0, 3900,abundance(30)|hit_points(160)|body_armor(19)|difficulty(4)|horse_speed(45)|horse_maneuver(44)|horse_charge(20)|horse_scale(95),imodbits_horse_basic|imodbit_champion, [], culture_germanic ],

["donkey_mount","Donkey", [("donkey_mount",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(80)|hit_points(55)|body_armor(7)|difficulty(0)|horse_speed(32)|horse_maneuver(33)|horse_charge(8)|horse_scale(79),imodbits_horse_basic],
["mule","Mule", [("mule",0)], itp_merchandise|itp_type_horse, 0, 450,abundance(70)|hit_points(65)|body_armor(10)|difficulty(0)|horse_speed(35)|horse_maneuver(35)|horse_charge(8)|horse_scale(86),imodbits_horse_basic],

#whalebone crossbow, yew bow, war bow, arming sword
 ["arrows","Arrows", [("arrow_new",0),("arrow_new",ixmesh_flying_ammo),("quiver_new", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_quiver_back, 72,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(22,cut)|max_ammo(26),imodbits_missile],
 
 ["khergit_arrows","Steppe Arrows", [("yastid_arrow_1",0),("yastid_arrow_1",ixmesh_flying_ammo),("yastid_quiver_1", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_revolver_right, 410,weight(3.5)|abundance(30)|weapon_length(95)|thrust_damage(26,cut)|max_ammo(22),imodbits_missile],
 
 ["barbed_arrows","Barbed Arrows", [("barbed_arrow_new",0),("barbed_arrow_new",ixmesh_flying_ammo),("barbed_arrows_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 124,weight(3)|abundance(70)|weapon_length(95)|thrust_damage(24,cut)|max_ammo(26),imodbits_missile],
 
 ["bodkin_arrows","Bodkin Arrows", [("piercing_arrow_new",0),("piercing_arrow_new",ixmesh_flying_ammo),("piercing_arrows_new_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 350,weight(3)|abundance(50)|weapon_length(91)|thrust_damage(25,cut)|max_ammo(24),imodbits_missile],
 
 ["germanic_arrows","Arrows", [("nydam_arrow",0),("nydam_arrow",ixmesh_flying_ammo),("nydam_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_revolver_right, 72,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(24,cut)|max_ammo(28),imodbits_missile],
 
 ["roman_arrows_1","Arrows", [("roman_arrow",0),("roman_arrow",ixmesh_flying_ammo),("roman_quiver_1", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_revolver_right, 100,weight(3.5)|abundance(80)|weapon_length(95)|thrust_damage(24,cut)|max_ammo(32),imodbits_missile],
 
 ["roman_arrows_2","Arrows", [("roman_arrow",0),("roman_arrow",ixmesh_flying_ammo),("roman_quiver_2", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_revolver_right, 100,weight(3.5)|abundance(80)|weapon_length(95)|thrust_damage(24,cut)|max_ammo(32),imodbits_missile],
 
 ["bolts","Bolts", [("bolt_new",0),("bolt_new",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_a_new", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 64,weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(22,pierce)|max_ammo(26),imodbits_missile],
 
 ["steel_bolts","Steel Bolts", [("bolt_new",0),("bolt_new",ixmesh_flying_ammo),("bolt_bag_a_new", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 210,weight(2.5)|abundance(20)|weapon_length(63)|thrust_damage(24,pierce)|max_ammo(24),imodbits_missile],
 
 ["cartridges","Sling Stones", [("throwing_stone",0),("throwing_stone",ixmesh_flying_ammo)], itp_type_bullets|itp_merchandise|itp_default_ammo, 0, 41,weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(23,pierce)|max_ammo(50),imodbits_missile],
 
 ["sling_bullet","Sling Bullets", [("sling_bullet",0),("sling_bullet",ixmesh_flying_ammo)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_default_ammo, 0, 200,weight(3.5)|abundance(30)|weapon_length(3)|thrust_damage(25,pierce)|max_ammo(40),imodbits_missile],

["pilgrim_disguise", "Pilgrim Disguise", [("pilgrim_outfit",0)], 0| itp_type_body_armor |itp_covers_legs |itp_civilian ,0, 25 , weight(2)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["pilgrim_hood", "Pilgrim Hood", [("pilgrim_hood",0)], 0| itp_type_head_armor |itp_civilian  ,0, 35 , weight(1.25)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# ARMOR
#handwear
["leather_gloves","Leather Gloves", [("leather_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0, 500, weight(0.25)|abundance(10)|body_armor(2)|difficulty(0),imodbits_cloth],
["mail_mittens","Mail Gloves", [("mail_mittens_new_L",0)], itp_type_hand_armor,0, 2840, weight(1)|abundance(1)|body_armor(6)|difficulty(0),imodbits_armor],
#["scale_gauntlets","Scale Gauntlets", [("scale_gauntlets_b_L",0)], itp_type_hand_armor,0, 2500, weight(3)|abundance(1)|body_armor(6)|difficulty(6),imodbits_armor],
#["lamellar_gauntlets","Lamellar Gauntlets", [("glove6_L",0)], itp_type_hand_armor,0, 2500, weight(3)|abundance(1)|body_armor(6)|difficulty(6),imodbits_armor],

#footwear
["wrapping_boots", "Wrapping Boots", [("wrapping_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["woolen_hose", "Leather Shoes", [("ankle_boots_bare",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["blue_hose", "Leather Shoes", [("ankle_boots_bare",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["hunter_boots", "Leather Boots", [("simple_leather_boots_1",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature,0,
 75 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth, [], culture_germanic+culture_gothic ],
["hide_boots", "Hide Boots", [("hide_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 34 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], culture_germanic+culture_gothic ],
["ankle_boots", "Ankle Boots", [("ankle_boots_mod",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["nomad_boots", "Boots", [("nomad_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 90 , weight(1.25)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["leather_boots", "Leather Boots", [("leather_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 174 , weight(1.25)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["khergit_leather_boots", "Simple Leather Boots", [("gothic_boots_1",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, #used by the goths
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["sarranid_boots_a", "Sandals", [("civil_poor_boots_a",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["sarranid_boots_b", "Leather Boots", [("new_leather_boots_a",0)],  itp_merchandise|itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 120 , weight(2)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],

["roman_boots_1", "Fascia Crurales", [("roman_boots_1",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["roman_boots_2", "Fascia Crurales", [("roman_boots_2",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],

["roman_lorum_fasciari_1", "Lorum Fasciari", [("roman_lorum_fasciari_1",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth ],
["roman_lorum_fasciari_2", "Lorum Fasciari", [("roman_lorum_fasciari_2",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth ],
["roman_lorum_fasciari_3", "Lorum Fasciari", [("roman_lorum_fasciari_3",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth ],
["roman_lorum_fasciari_4", "Lorum Fasciari", [("roman_lorum_fasciari_4",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth ],
["roman_lorum_fasciari_5", "Lorum Fasciari", [("roman_lorum_fasciari_5",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth ],
["roman_lorum_fasciari_6", "Lorum Fasciari", [("roman_lorum_fasciari_6",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth ],

["generic_lorum_fasciari_1", "Lorum Fasciari", [("generic_lorum_fasciari_1",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth ],
["generic_lorum_fasciari_2", "Lorum Fasciari", [("generic_lorum_fasciari_2",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth ],

["obenaltendorf_shoes_1", "Carbatinae", [("obenaltendorf_shoes_1",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, #germanic
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth ],
["obenaltendorf_shoes_2", "Carbatinae", [("obenaltendorf_shoes_2",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth ],

#Boots/Shoes
["sassanid_simple_boots_1", "Simple Boots", [("boot13",0)], itp_merchandise|itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 90 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth, [], culture_sassanid ],
["sassanid_simple_boots_2", "Simple Boots", [("boot13b",0)], itp_merchandise|itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 90 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth, [], culture_sassanid ],
["sassanid_simple_boots_3", "Simple Boots", [("boot13c",0)], itp_merchandise|itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 90 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth, [], culture_sassanid ],
["sassanid_cavalry_boots_1", "Cavalry Boots", [("rus_cav_boots",0)], itp_merchandise|itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 250 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth, [], culture_sassanid ],
["sassanid_cavalry_boots_2", "Cavalry Boots", [("sassanid_boots_2",0)], itp_merchandise|itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 250 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth, [], culture_sassanid ],
["sarranid_decorated_boots", "Decorated Sassanid Boots", [("sassanid_boots_1",0)], itp_merchandise|itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 280 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth, [], culture_sassanid ],
["iron_greaves", "Greaves", [("carbatinae_1_greaves",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 860 , weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor ],
["mail_chausses", "Greaves", [("carbatinae_2_greaves",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 860 , weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor ],
["light_leather_shoes", "Leather shoes with Greaves", [("decorated_leather_shoes_greaves",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 , weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor ],
["carbatinae_greaves_a", "Greaves", [("carbatinae_1_greaves_green",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 , weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor ],
["carbatinae_greaves_b", "Greaves", [("carbatinae_2_greaves_green",0)],  itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 , weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor ],
["carbatinae_greaves_c", "Greaves", [("carbatinae_1_greaves_blue",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 , weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor ],
["carbatinae_greaves_d", "Greaves", [("carbatinae_2_greaves_blue",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 , weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor ],
["carbatinae_greaves_e", "Greaves", [("carbatinae_1_greaves_grey",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 , weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor ],
["carbatinae_greaves_f", "Greaves", [("carbatinae_2_greaves_grey",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 , weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor ],
["carbatinae_greaves_g", "Greaves", [("carbatinae_1_greaves_orange",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 , weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor ],
["carbatinae_greaves_h", "Greaves", [("carbatinae_2_greaves_orange",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 , weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor ],
["carbatinae_greaves_i", "Greaves", [("carbatinae_2_greaves_red",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 890 , weight(2)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor ],
["carbatinae_1", "Carbatinae", [("carbatinae_1",0)],  itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 280 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ], 
["carbatinae_2", "Carbatinae", [("carbatinae_2",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 280 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ], 
["carbatinae_2_green", "Carbatinae", [("carbatinae_2_green",0)],  itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 280 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ], 
["carbatinae_1_blue", "Carbatinae", [("carbatinae_1_blue",0)],  itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 280 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ], 
["carbatinae_2_blue", "Carbatinae", [("carbatinae_2_blue",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 280 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ], 
["carbatinae_2_grey", "Carbatinae", [("carbatinae_2_grey",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 280 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ], 
["carbatinae_1_grey", "Carbatinae", [("carbatinae_1_grey",0)],  itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 280 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ], 
["carbatinae_1_green", "Carbatinae", [("carbatinae_1_green",0)],  itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 280 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ], 
["carbatinae_1_orange", "Carbatinae", [("carbatinae_1_orange",0)],  itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 280 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ], 
["carbatinae_2_orange", "Carbatinae", [("carbatinae_2_orange",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 280 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ], 
["carbatinae_1_red", "Carbatinae", [("carbatinae_1_red",0)],  itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 480 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["carbatinae_2_red", "Carbatinae", [("carbatinae_2_red",0)],  itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 480 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["simple_shoes", "Shoes", [("rus_shoes",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 90 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],

["ankle_boots_white", "Ankle Boots", [("ankle_boots_white",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],

["roman_leather_boots_1", "Ankle Boots", [("roman_leather_boots_1",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth ],
["roman_leather_boots_2", "Ankle Boots", [("roman_leather_boots_2",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth ],
["roman_leather_boots_3", "Ankle Boots", [("roman_leather_boots_3",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth ],

["sarranid_boots_d", "Ankle Boots with Greaves", [("ankle_boots_greaves",0)], itp_type_foot_armor | itp_attach_armature ,0,
 1000 , weight(1.5)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(0) ,imodbits_armor ],
["ankle_greaves", "Ankle Boots with Greaves", [("splinted_ankle_boots",0)],  itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 1000 , weight(1.5)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(6) ,imodbits_cloth ],
["splinted_leather_greaves", "Splinted Greaves", [("splinted_greaves_a",0)], itp_type_foot_armor | itp_attach_armature,0,
 1000 , weight(3)|abundance(20)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(0) ,imodbits_armor ],
["splinted_greaves", "Splinted Greaves", [("splinted_greaves_a",0)], itp_type_foot_armor | itp_attach_armature,0,
 1000 , weight(2.75)|abundance(20)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_armor ],

["roman_greaves_1", "Greaves", [("roman_greaves_1",0)],  itp_merchandise| itp_type_foot_armor  | itp_attach_armature ,0,
 1000 , weight(2.5)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_plate, [], culture_roman ],
["roman_greaves_2", "Greaves", [("roman_greaves_2",0)],  itp_merchandise| itp_type_foot_armor  | itp_attach_armature ,0,
 1000 , weight(2.5)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_plate, [], culture_roman ],
["roman_greaves_3", "Greaves", [("roman_greaves_3",0)],  itp_merchandise| itp_type_foot_armor  | itp_attach_armature ,0,
 1000 , weight(2.5)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_plate, [], culture_roman ],
["roman_greaves_4", "Greaves", [("roman_greaves_4",0)],  itp_merchandise| itp_type_foot_armor  | itp_attach_armature ,0,
 1000 , weight(2.5)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_plate, [], culture_roman ],
["roman_greaves_5", "Greaves", [("roman_greaves_5",0)],  itp_merchandise| itp_type_foot_armor  | itp_attach_armature ,0,
 1000 , weight(2.5)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_plate, [], culture_roman ],
["roman_greaves_6", "Greaves", [("roman_greaves_6",0)],  itp_merchandise| itp_type_foot_armor  | itp_attach_armature ,0,
 1000 , weight(2.5)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_plate, [], culture_roman ],

["sarranid_boots_c", "Ankle Boots with Greaves", [("roman_greaves_5_1",0)],  itp_merchandise| itp_type_foot_armor  | itp_attach_armature ,0,
 1000 , weight(2.75)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_plate, [], culture_roman ],
["black_greaves", "Ankle Boots with Greaves", [("roman_greaves_6_1",0)], itp_merchandise| itp_type_foot_armor  | itp_attach_armature,0,
 1000 , weight(2.75)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_plate, [], culture_roman ],
["heavy_greaves", "Greaves", [("rus_splint_greaves",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 1000 , weight(3)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(0) ,imodbits_armor, [], culture_sassanid+culture_caucasian+culture_alan+culture_hunnic ],

["mail_boots", "Mail Boots", [("mail_chausses_new",0)], itp_merchandise|itp_type_foot_armor | itp_attach_armature  ,0,
 1250 , weight(3)|abundance(1)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(8) ,imodbits_mail, [], [fac_culture_empire,fac_culture_6] ],

["roman_greaves_manica_1", "Greaves with Manica", [("roman_greaves_manica_1",0)],  itp_merchandise| itp_type_foot_armor  | itp_attach_armature ,0,
 2500 , weight(5)|abundance(2)|head_armor(0)|body_armor(8)|leg_armor(28)|difficulty(10) ,imodbits_plate, [], [fac_culture_empire] ],
["roman_greaves_manica_2", "Greaves with Manica", [("roman_greaves_manica_2",0)],  itp_merchandise| itp_type_foot_armor  | itp_attach_armature ,0,
 2500 , weight(5)|abundance(2)|head_armor(0)|body_armor(8)|leg_armor(28)|difficulty(10) ,imodbits_plate, [], [fac_culture_empire] ],
["roman_greaves_manica_3", "Greaves with Manica", [("roman_greaves_manica_3",0)],  itp_merchandise| itp_type_foot_armor  | itp_attach_armature ,0,
 2500 , weight(5)|abundance(2)|head_armor(0)|body_armor(8)|leg_armor(28)|difficulty(10) ,imodbits_plate, [], [fac_culture_empire] ],
["roman_greaves_manica_4", "Greaves with Manica", [("roman_greaves_manica_4",0)],  itp_merchandise| itp_type_foot_armor  | itp_attach_armature ,0,
 2500 , weight(5)|abundance(2)|head_armor(0)|body_armor(8)|leg_armor(28)|difficulty(10) ,imodbits_plate, [], [fac_culture_empire] ],

["mail_boots_manica_1", "Mail Boots with Manica", [("mail_boots_manica_1",0)], itp_merchandise|itp_type_foot_armor | itp_attach_armature  ,0,
 3000 , weight(8)|abundance(1)|head_armor(0)|body_armor(14)|leg_armor(30)|difficulty(12) ,imodbits_mail, [], [fac_culture_empire,fac_culture_6] ],
["mail_boots_manica_2", "Mail Boots with Manica", [("mail_boots_manica_2",0)], itp_merchandise|itp_type_foot_armor | itp_attach_armature  ,0,
 3000 , weight(8)|abundance(1)|head_armor(0)|body_armor(14)|leg_armor(30)|difficulty(12) ,imodbits_mail, [], [fac_culture_empire,fac_culture_6] ],


#bodywear
["courtly_outfit", "Courtly Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nobleman_outfit", "Nobleman Outfit", [("nobleman_outfit_b_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["nomad_armor", "Nomad Armor", [("nomad_armor_new",0)], itp_type_body_armor |itp_covers_legs   ,0, 400 , weight(2)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["khergit_armor", "Nomad Armor", [("khergit_armor_new",0)], itp_type_body_armor | itp_covers_legs ,0, 38 , weight(2)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

#NEW:
["rawhide_coat", "Rawhide Coat", [("coat_of_plates_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 120 , weight(5)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#NEW: was lthr_armor_a

["leather_armor", "Leather Armor", [("rich_tunic_a",0)], itp_type_body_armor |itp_covers_legs  ,0, 450 , weight(7)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["fur_coat", "Rich Tunic", [("rich_tunic_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 117 , weight(2)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(8)|difficulty(0) ,imodbits_armor ],
["leather_jacket", "Rich Tunic", [("rich_tunic_a",0)], itp_merchandise| itp_type_body_armor | itp_covers_legs  |itp_civilian ,0, 117 , weight(2)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

#for future:
#end

#NEW: was leather_vest
 #NEW: was "leather_jerkin"
["nomad_vest", "Nomad Vest", [("nomad_vest_new",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 360 , weight(7)|abundance(50)|head_armor(0)|body_armor(22)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

 #NEW: was padded_leather

["skirmisher_armor", "Skirmisher Armor", [("skirmisher_armor",0)], itp_type_body_armor  |itp_covers_legs ,0,
 74 , weight(3)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],

#Quest-specific - perhaps can be used for prisoners,
["burlap_tunic", "Burlap Tunic", [("light_brown_tunic",0)], itp_type_body_armor  |itp_covers_legs ,0,
 5 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_armor ],

["dress", "Long Tunic", [("briton_dress_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["blue_dress", "Blue Long Tunic", [("briton_dress_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["peasant_dress", "Green Long Tunic", [("briton_dress_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["woolen_dress", "Woolen Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor|itp_civilian  |itp_covers_legs ,0,
 10 , weight(1.75)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["shirt", "Brown Tunic", [("light_brown_tunic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 85 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["robe", "Robes", [("robes_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 231 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["leather_apron", "Leather Apron", [("kowal_1",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 61 , weight(3)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["robes_church", "Robes", [("priest_1_combined",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 231 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],

["heraldic_mail_with_surcoat", "Rich Tunic", [("woolen_tunic_b",0)], itp_type_body_armor  |itp_covers_legs ,0,
 400 , weight(8)|abundance(10)|head_armor(0)|body_armor(20)|leg_armor(17)|difficulty(0) ,imodbits_cloth],
["heraldic_mail_with_tunic", "Rich Tunic", [("woolen_tunic_a",0)], itp_type_body_armor  |itp_covers_legs ,0,
 400 , weight(8)|abundance(10)|head_armor(0)|body_armor(20)|leg_armor(16)|difficulty(0) ,imodbits_cloth],
["heraldic_mail_with_tunic_b", "Rich Tunic", [("woolen_tunic_c",0)], itp_type_body_armor  |itp_covers_legs ,0,
 400 , weight(8)|abundance(10)|head_armor(0)|body_armor(20)|leg_armor(16)|difficulty(0) ,imodbits_cloth],
["heraldic_mail_with_tabard", "Rich Tunic", [("yellow_tunic_saxon",0)], itp_type_body_armor  |itp_covers_legs ,0,
 400 , weight(8)|abundance(10)|head_armor(0)|body_armor(20)|leg_armor(15)|difficulty(0) ,imodbits_cloth],

["tabard", "Tunic", [("green_tunic",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
 78 , weight(3)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],
["gambeson", "Tunic", [("linen_tunic_b",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 78 , weight(5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],
["blue_gambeson", "Tunic", [("blue_tunic",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 78 , weight(5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],
["red_gambeson", "Tunic", [("red_tunic",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 78 , weight(5)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(5)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],
["padded_cloth", "Tunic", [("shirt_tel",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 78 , weight(11)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],
["aketon_green", "Tunic", [("shirt_grn",0)], itp_type_body_armor  |itp_covers_legs ,0,
 78 , weight(11)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],
["studded_leather_coat", "Tunic", [("shirt_blk",0)],itp_type_body_armor  |itp_covers_legs ,0,
 78 , weight(14)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(7) ,imodbits_armor, [], culture_germanic ],

["roman_shirt_1", "Tunica Manicata", [("roman_shirt_1",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_shirt_2", "Tunica Manicata", [("roman_shirt_2",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_shirt_3", "Tunica Manicata", [("roman_shirt_3",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_shirt_4", "Tunica Manicata", [("roman_shirt_4",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_shirt_5", "Tunica Manicata", [("roman_shirt_5",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_shirt_6", "Tunica Manicata", [("roman_shirt_6",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_shirt_7", "Tunica Manicata", [("roman_shirt_7",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_shirt_8", "Tunica Manicata", [("roman_shirt_8",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_shirt_9", "Tunica Manicata", [("roman_shirt_9",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_shirt_10", "Tunica Manicata", [("roman_shirt_10",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_shirt_11", "Tunica Manicata", [("roman_shirt_11",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_shirt_12", "Tunica Manicata", [("roman_shirt_12",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_shirt_13", "Tunica Manicata", [("roman_shirt_13",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_shirt_14", "Tunica Manicata", [("roman_shirt_14",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_shirt_15", "Tunica Manicata", [("roman_shirt_15",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_shirt_16", "Tunica Manicata", [("roman_shirt_16",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],

["berber_tunic_1", "Tunic", [("berber_tunic_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_tunic_legs"),]),], culture_roman ],
["berber_tunic_2", "Tunic", [("berber_tunic_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_tunic_legs"),]),], culture_roman ],
["berber_tunic_3", "Tunic", [("berber_tunic_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_tunic_legs"),]),], culture_roman ],
["berber_tunic_4", "Tunic", [("berber_tunic_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_tunic_legs"),]),], culture_roman ],
["berber_tunic_5", "Tunic", [("berber_tunic_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_male_arms"),]),], culture_roman ],

["arabian_tunic_1", "Tunic", [("arabian_tunic_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["arabian_tunic_2", "Tunic", [("arabian_tunic_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_tunic_legs"),]),], culture_sassanid ],
["arabian_tunic_3", "Tunic", [("arabian_tunic_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_tunic_legs"),]),], culture_sassanid ],

["imperial_common_shirt", "Simple Tunic", [("simple_short_tunic",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_short_tunic_arms"),]),], culture_roman ],

["simple_tunic_1", "Simple Tunic", [("simple_tunic_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_short_tunic_arms"),]),], ],
["simple_tunic_2", "Simple Tunic", [("simple_tunic_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_short_tunic_arms"),]),], ],
["simple_tunic_3", "Simple Tunic", [("simple_tunic_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_short_tunic_arms"),]),], ],
["simple_tunic_4", "Simple Tunic", [("simple_tunic_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_short_tunic_arms"),]),], ],
["simple_tunic_5", "Simple Tunic", [("simple_tunic_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_short_tunic_arms"),]),], ],
["simple_tunic_6", "Simple Tunic", [("simple_tunic_6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_short_tunic_arms"),]),], ],
["simple_tunic_7", "Simple Tunic", [("simple_tunic_7",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_short_tunic_arms"),]),], ],
["simple_tunic_8", "Simple Tunic", [("simple_tunic_8",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_short_tunic_arms"),]),], ],
["simple_tunic_9", "Simple Tunic", [("simple_tunic_9",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_short_tunic_arms"),]),], ],
["simple_tunic_10", "Simple Tunic", [("simple_tunic_10",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_short_tunic_arms"),]),], ],

["a_exomis_1", "Exomis", [("a_exomis_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_exomis_body_1"),]),], [fac_culture_11,fac_culture_15] ],
["a_exomis_2", "Exomis", [("a_exomis_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_exomis_body_1"),]),], [fac_culture_11,fac_culture_15] ],
["a_exomis_3", "Exomis", [("a_exomis_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_exomis_body_1"),]),], [fac_culture_11,fac_culture_15] ],

["roman_military_tunic_1", "Tunica Blattea", [("roman_military_tunic_1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_military_tunic_2", "Tunica Blattea", [("roman_military_tunic_2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_military_tunic_3", "Tunica Blattea", [("roman_military_tunic_3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_military_tunic_4", "Tunica Blattea", [("roman_military_tunic_4",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_military_tunic_5", "Tunica Blattea", [("roman_military_tunic_5",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_military_tunic_6", "Tunica Blattea", [("roman_military_tunic_6",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_military_tunic_7", "Tunica Blattea", [("roman_military_tunic_7",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_military_tunic_8", "Tunica Blattea", [("roman_military_tunic_8",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_military_tunic_9", "Tunica Blattea", [("roman_military_tunic_9",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_military_tunic_10", "Tunica Blattea", [("roman_military_tunic_10",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_tunic_legs"),]),], culture_roman ], #no pants

["red_shirt", "Red Tunic", [("rich_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["rich_tunic_1", "Blue Tunic", [("rich_tunic_1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["rich_tunic_2", "Red Tunic", [("rich_tunic_2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["rich_tunic_3", "Green Tunic", [("rich_tunic_3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["rich_tunic_4", "Blue Tunic", [("rich_tunic_4",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["rich_tunic_5", "Brown Tunic", [("rich_tunic_5",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["rich_tunic_6", "Yellow Tunic", [("rich_tunic_e",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],

["kaftan_tunic_1", "Tunic", [("kaftan_tunic_1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["kaftan_tunic_2", "Tunic", [("kaftan_tunic_2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["kaftan_tunic_3", "Tunic", [("kaftan_tunic_3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["kaftan_tunic_4", "Tunic", [("kaftan_tunic_4",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["kaftan_tunic_5", "Tunic", [("kaftan_tunic_5",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["kaftan_tunic_6", "Tunic", [("kaftan_tunic_6",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["kaftan_tunic_7", "Tunic", [("kaftan_tunic_7",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["kaftan_tunic_8", "Tunic", [("kaftan_tunic_8",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["kaftan_tunic_9", "Tunic", [("kaftan_tunic_9",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["kaftan_tunic_10", "Tunic", [("kaftan_tunic_10",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],

["kaftan_sheepskin_1", "Tunic with Sheepskin", [("kaftan_sheepskin_1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["kaftan_sheepskin_2", "Tunic with Sheepskin", [("kaftan_sheepskin_2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["kaftan_sheepskin_3", "Tunic with Sheepskin", [("kaftan_sheepskin_3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["kaftan_sheepskin_4", "Tunic with Sheepskin", [("kaftan_sheepskin_4",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["kaftan_sheepskin_5", "Tunic with Sheepskin", [("kaftan_sheepskin_5",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["kaftan_sheepskin_6", "Tunic with Sheepskin", [("kaftan_sheepskin_6",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],

["skirmisher_tunic_1", "Tunic with Sheepskin", [("skirmisher_tunic_1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["skirmisher_tunic_2", "Tunic with Sheepskin", [("skirmisher_tunic_2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["skirmisher_tunic_3", "Tunic with Sheepskin", [("skirmisher_tunic_3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["skirmisher_tunic_4", "Tunic with Sheepskin", [("skirmisher_tunic_4",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["khergit_vest_a", "Riding Kaftan", [("khergit_vest_a",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 120 , weight(1)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["khergit_vest_b", "Riding Kaftan", [("khergit_vest_b",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 120 , weight(1)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["khergit_vest_c", "Riding Kaftan", [("khergit_vest_c",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 120 , weight(1)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["khergit_vest_d", "Riding Kaftan", [("khergit_vest_d",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 120 , weight(1)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],

["roman_arabian_kaftan", "Arabian Kaftan", [("roman_arabian_kaftan",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 120 , weight(1)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], [fac_culture_empire,fac_culture_6] ],

["steppe_kaftan_1", "Riding Kaftan", [("steppe_kaftan_1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 120 , weight(1)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["steppe_kaftan_2", "Riding Kaftan", [("steppe_kaftan_2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 120 , weight(1)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["steppe_kaftan_3", "Riding Kaftan", [("steppe_kaftan_3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 120 , weight(1)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],

#simple kaftans first
["kaftan_hunnic_red", "Red Kaftan", [("kaftan_hunnic_red",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 500 , weight(2)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(14)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_alan+culture_caucasian ],
["kaftan_hunnic_blue", "Blue Kaftan", [("kaftan_hunnic_blue",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 500 , weight(2)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(14)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_alan+culture_caucasian ],
["kaftan_hunnic_green", "Green Kaftan", [("kaftan_hunnic_green",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 500 , weight(2)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(14)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_alan+culture_caucasian ],
["kaftan_hunnic_white", "Kaftan", [("kaftan_hunnic_white",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 500 , weight(2)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(14)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_alan+culture_caucasian ],

["kaftan_alan_red", "Red Kaftan", [("kaftan_alan_red",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 500 , weight(2)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(14)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_alan+culture_caucasian ],
["kaftan_alan_blue", "Blue Kaftan", [("kaftan_alan_blue",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 500 , weight(2)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(14)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_alan+culture_caucasian ],
["kaftan_alan_green", "Green Kaftan", [("kaftan_alan_green",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 500 , weight(2)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(14)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_alan+culture_caucasian ],
["kaftan_alan_white", "Kaftan", [("kaftan_alan_white",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 500 , weight(2)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(14)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_alan+culture_caucasian ],

#rich kaftans
["kaftan_hunnic_1", "Rich Kaftan", [("kaftan_hunnic_1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 1000 , weight(2)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(15)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_alan+culture_caucasian ],
["kaftan_hunnic_2", "Rich Kaftan", [("kaftan_hunnic_2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 1000 , weight(2)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(15)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_alan+culture_caucasian ],
["kaftan_hunnic_3", "Rich Kaftan", [("kaftan_hunnic_3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 1000 , weight(2)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(15)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_alan+culture_caucasian ],
["kaftan_hunnic_4", "Rich Kaftan", [("kaftan_hunnic_4",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 1000 , weight(2)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(15)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_alan+culture_caucasian ],
["kaftan_hunnic_5", "Rich Kaftan", [("kaftan_hunnic_5",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 1000 , weight(2)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(15)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_alan+culture_caucasian ],
["kaftan_hunnic_6", "Rich Kaftan", [("kaftan_hunnic_6",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 1000 , weight(2)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(15)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_alan+culture_caucasian ],

["kaftan_alan_1", "Rich Kaftan", [("kaftan_alan_1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 1000 , weight(2)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(15)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_alan+culture_caucasian ],
["kaftan_alan_2", "Rich Kaftan", [("kaftan_alan_2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 1000 , weight(2)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(15)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_alan+culture_caucasian ],
["kaftan_alan_3", "Rich Kaftan", [("kaftan_alan_3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 1000 , weight(2)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(15)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_alan+culture_caucasian ],
["kaftan_alan_4", "Rich Kaftan", [("kaftan_alan_4",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 1000 , weight(2)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(15)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_alan+culture_caucasian ],
["kaftan_alan_5", "Rich Kaftan", [("kaftan_alan_5",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 1000 , weight(2)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(15)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_alan+culture_caucasian ],
["kaftan_alan_6", "Rich Kaftan", [("kaftan_alan_6",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 1000 , weight(2)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(15)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_alan+culture_caucasian ],
["kaftan_alan_7", "Rich Kaftan", [("kaftan_alan_7",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 1000 , weight(2)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(15)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_alan+culture_caucasian ],

["kaftan_eastern_1", "Rich Kaftan", [("kaftan_eastern_1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 1000 , weight(2)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(15)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_sassanid ],
["kaftan_eastern_2", "Rich Kaftan", [("kaftan_eastern_2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 1000 , weight(2)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(15)|difficulty(0) ,imodbits_cloth, [], culture_hunnic+culture_sassanid ],

["linen_tunic", "Tunic", [("shirt_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_1", "Blue Tunic", [("shirt_blu",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_2", "Green Tunic", [("shirt_grn",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_3", "Red Tunic", [("shirt_red",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_4", "Blue Tunic", [("linen_tunic_a",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_5", "White Tunic", [("linen_tunic_b",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_6", "Red Tunic", [("linen_tunic_c",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_7", "Green Tunic", [("woolen_tunic_a",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_8", "Yellow Tunic", [("woolen_tunic_b",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_9", "Black Tunic", [("woolen_tunic_c",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_10", "Brown Tunic", [("shirt_blk",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_11", "Orange Tunic", [("linen_tunic_d",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_12", "Tunic", [("linen_tunic_e",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_13", "Yellow Tunic", [("shirt_ylw",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_14", "Blue Tunic", [("shirt_tel",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_15", "Tunic", [("shirt_d2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_16", "Green Tunic", [("green_tunic",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_17", "Red Tunic", [("red_tunic",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_18", "Blue Tunic", [("blue_tunic",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_19", "Blue Tunic", [("shirt_d3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_20", "Yellow Tunic", [("yellow_tunic",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_21", "Yellow Tunic", [("yellow_tunic_saxon",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_22", "Brown Tunic", [("brown_tunic",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["generic_tunic_1", "Tunic", [("generic_tunic_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,
        [(store_random_in_range,":rand_accessory","str_accessory_bag_1","str_accessory_end"),    # Picking one random string and thus one random mesh
        (store_random_in_range,":probability",0,100),
        (try_begin),
            (lt, ":probability", 50),    # The script only continues with a probability of 50 %
            (cur_item_add_mesh, ":rand_accessory"),    # Adding the random mesh to the item
        (try_end),])]
],
["generic_tunic_2", "Green Tunic", [("generic_tunic_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,
        [(store_random_in_range,":rand_accessory","str_accessory_bag_1","str_accessory_end"),    # Picking one random string and thus one random mesh
        (store_random_in_range,":probability",0,100),
        (try_begin),
            (lt, ":probability", 50),    # The script only continues with a probability of 50 %
            (cur_item_add_mesh, ":rand_accessory"),    # Adding the random mesh to the item
        (try_end),])]
],
["generic_tunic_3", "Red Tunic", [("generic_tunic_3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,
        [(store_random_in_range,":rand_accessory","str_accessory_bag_1","str_accessory_end"),    # Picking one random string and thus one random mesh
        (store_random_in_range,":probability",0,100),
        (try_begin),
            (lt, ":probability", 50),    # The script only continues with a probability of 50 %
            (cur_item_add_mesh, ":rand_accessory"),    # Adding the random mesh to the item
        (try_end),])]
],
["generic_tunic_4", "Red Tunic", [("generic_tunic_4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,
        [(store_random_in_range,":rand_accessory","str_accessory_bag_1","str_accessory_end"),    # Picking one random string and thus one random mesh
        (store_random_in_range,":probability",0,100),
        (try_begin),
            (lt, ":probability", 50),    # The script only continues with a probability of 50 %
            (cur_item_add_mesh, ":rand_accessory"),    # Adding the random mesh to the item
        (try_end),])]
],
["generic_tunic_5", "Blue Tunic", [("generic_tunic_5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,
        [(store_random_in_range,":rand_accessory","str_accessory_bag_1","str_accessory_end"),    # Picking one random string and thus one random mesh
        (store_random_in_range,":probability",0,100),
        (try_begin),
            (lt, ":probability", 50),    # The script only continues with a probability of 50 %
            (cur_item_add_mesh, ":rand_accessory"),    # Adding the random mesh to the item
        (try_end),])]
],
["generic_tunic_6", "Brown Tunic", [("generic_tunic_6",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,
        [(store_random_in_range,":rand_accessory","str_accessory_bag_1","str_accessory_end"),    # Picking one random string and thus one random mesh
        (store_random_in_range,":probability",0,100),
        (try_begin),
            (lt, ":probability", 50),    # The script only continues with a probability of 50 %
            (cur_item_add_mesh, ":rand_accessory"),    # Adding the random mesh to the item
        (try_end),])]
],
["generic_tunic_7", "Brown Tunic", [("generic_tunic_7",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,
        [(store_random_in_range,":rand_accessory","str_accessory_bag_1","str_accessory_end"),    # Picking one random string and thus one random mesh
        (store_random_in_range,":probability",0,100),
        (try_begin),
            (lt, ":probability", 50),    # The script only continues with a probability of 50 %
            (cur_item_add_mesh, ":rand_accessory"),    # Adding the random mesh to the item
        (try_end),])]
],
["generic_tunic_8", "Tunic", [("generic_tunic_8",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,
        [(store_random_in_range,":rand_accessory","str_accessory_bag_1","str_accessory_end"),    # Picking one random string and thus one random mesh
        (store_random_in_range,":probability",0,100),
        (try_begin),
            (lt, ":probability", 50),    # The script only continues with a probability of 50 %
            (cur_item_add_mesh, ":rand_accessory"),    # Adding the random mesh to the item
        (try_end),])]
],
["generic_tunic_9", "Green Tunic", [("generic_tunic_9",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,
        [(store_random_in_range,":rand_accessory","str_accessory_bag_1","str_accessory_end"),    # Picking one random string and thus one random mesh
        (store_random_in_range,":probability",0,100),
        (try_begin),
            (lt, ":probability", 50),    # The script only continues with a probability of 50 %
            (cur_item_add_mesh, ":rand_accessory"),    # Adding the random mesh to the item
        (try_end),])]
],
["generic_tunic_10", "Tunic", [("generic_tunic_10",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,
        [(store_random_in_range,":rand_accessory","str_accessory_bag_1","str_accessory_end"),    # Picking one random string and thus one random mesh
        (store_random_in_range,":probability",0,100),
        (try_begin),
            (lt, ":probability", 50),    # The script only continues with a probability of 50 %
            (cur_item_add_mesh, ":rand_accessory"),    # Adding the random mesh to the item
        (try_end),])]
],
["generic_tunic_11", "Tunic", [("generic_tunic_11",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,
        [(store_random_in_range,":rand_accessory","str_accessory_bag_1","str_accessory_end"),    # Picking one random string and thus one random mesh
        (store_random_in_range,":probability",0,100),
        (try_begin),
            (lt, ":probability", 50),    # The script only continues with a probability of 50 %
            (cur_item_add_mesh, ":rand_accessory"),    # Adding the random mesh to the item
        (try_end),])]
],
["generic_tunic_12", "Tunic", [("generic_tunic_12",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,
        [(store_random_in_range,":rand_accessory","str_accessory_bag_1","str_accessory_end"),    # Picking one random string and thus one random mesh
        (store_random_in_range,":probability",0,100),
        (try_begin),
            (lt, ":probability", 50),    # The script only continues with a probability of 50 %
            (cur_item_add_mesh, ":rand_accessory"),    # Adding the random mesh to the item
        (try_end),])]
],
["generic_tunic_13", "Tunic", [("generic_tunic_13",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,
        [(store_random_in_range,":rand_accessory","str_accessory_bag_1","str_accessory_end"),    # Picking one random string and thus one random mesh
        (store_random_in_range,":probability",0,100),
        (try_begin),
            (lt, ":probability", 50),    # The script only continues with a probability of 50 %
            (cur_item_add_mesh, ":rand_accessory"),    # Adding the random mesh to the item
        (try_end),])]
],
["generic_tunic_14", "Tunic", [("generic_tunic_14",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,
        [(store_random_in_range,":rand_accessory","str_accessory_bag_1","str_accessory_end"),    # Picking one random string and thus one random mesh
        (store_random_in_range,":probability",0,100),
        (try_begin),
            (lt, ":probability", 50),    # The script only continues with a probability of 50 %
            (cur_item_add_mesh, ":rand_accessory"),    # Adding the random mesh to the item
        (try_end),])]
],
["generic_tunic_15", "Tunic", [("generic_tunic_15",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,
        [(store_random_in_range,":rand_accessory","str_accessory_bag_1","str_accessory_end"),    # Picking one random string and thus one random mesh
        (store_random_in_range,":probability",0,100),
        (try_begin),
            (lt, ":probability", 50),    # The script only continues with a probability of 50 %
            (cur_item_add_mesh, ":rand_accessory"),    # Adding the random mesh to the item
        (try_end),])]
],

["tunic_long_pants_1", "Tunic", [("tunic_long_pants_1",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], culture_gothic ],
["tunic_long_pants_2", "Tunic", [("tunic_long_pants_2",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], culture_gothic ],
["tunic_long_pants_3", "Tunic", [("tunic_long_pants_3",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], culture_gothic ],
["tunic_long_pants_4", "Tunic", [("tunic_long_pants_4",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], culture_gothic ],
["tunic_long_pants_5", "Tunic", [("tunic_long_pants_5",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], culture_gothic ],
["tunic_long_pants_6", "Tunic", [("tunic_long_pants_6",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], culture_gothic ],
["tunic_long_pants_7", "Tunic", [("tunic_long_pants_7",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], culture_gothic ],
["tunic_long_pants_8", "Tunic", [("tunic_long_pants_8",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], culture_gothic ],
["tunic_long_pants_9", "Tunic", [("tunic_long_pants_9",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], culture_gothic ],
["tunic_long_pants_10", "Tunic", [("tunic_long_pants_10",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], culture_gothic ],
["tunic_long_pants_11", "Tunic", [("tunic_long_pants_11",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], culture_gothic+culture_germanic ],

["sassanid_rich_tunic_1", "Rich Sassanid Tunic", [("sassanid_rich_tunic_1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 400 , weight(1)|abundance(50)|head_armor(0)|body_armor(12)|leg_armor(9)|difficulty(0) ,imodbits_cloth, [], culture_sassanid ],
["sassanid_rich_tunic_2", "Rich Sassanid Tunic", [("sassanid_rich_tunic_2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 400 , weight(1)|abundance(50)|head_armor(0)|body_armor(12)|leg_armor(9)|difficulty(0) ,imodbits_cloth, [], culture_sassanid ],
["sassanid_rich_tunic_3", "Rich Sassanid Tunic", [("sassanid_rich_tunic_3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 400 , weight(1)|abundance(50)|head_armor(0)|body_armor(12)|leg_armor(9)|difficulty(0) ,imodbits_cloth, [], culture_sassanid ],
["sassanid_rich_tunic_4", "Rich Sassanid Tunic", [("sassanid_rich_tunic_4",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 400 , weight(1)|abundance(50)|head_armor(0)|body_armor(12)|leg_armor(9)|difficulty(0) ,imodbits_cloth, [], culture_sassanid ],

#based off of falkirk tartarn pattern, found in briton, similar find in juteland
["falkirk_tunic_1", "Tunic", [("falkirk_tunic_1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_celtic ],
["falkirk_tunic_2", "Tunic", [("falkirk_tunic_2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_celtic ],
["falkirk_tunic_3", "Tunic", [("falkirk_tunic_3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_celtic ],
["falkirk_tunic_4", "Tunic", [("falkirk_tunic_4",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_celtic ],
["falkirk_tunic_5", "Tunic", [("falkirk_tunic_5",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_celtic ],

["simple_shirt_5", "Simple Tunic", [("short_tunic_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_male_arms"),]),], ],
["simple_shirt_6", "Simple Tunic", [("short_tunic_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_male_arms"),]),], ],

["african_kilt_1", "Nubian Kilt", [("african_kilt_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(4)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_african_kilt_body"),]),], culture_african ],
["african_kilt_2", "Nubian Kilt", [("african_kilt_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(4)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_african_kilt_body"),]),], culture_african ],
["african_kilt_3", "Nubian Kilt", [("african_kilt_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(4)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_african_kilt_body"),]),], culture_african ],

["long_tunic_a", "Blue Long Tunic", [("shirt_shirt_a",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["long_tunic_b", "Yellow Long Tunic", [("shirt_shirt_b",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["long_tunic_c", "White Long Tunic", [("shirt_shirt_c",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

["coarse_tunic", "Tunic with vest", [("coarse_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 107 , weight(2)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["bl_tunic6", "Rich Tunic", [("BL_Tunic06",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 112 , weight(1)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(9)|difficulty(0) ,imodbits_cloth, [], [fac_culture_4,fac_culture_5]  ],
["bl_tunic7", "Rich Tunic", [("BL_Tunic07",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 112 , weight(1)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(9)|difficulty(0) ,imodbits_cloth, [], [fac_culture_4,fac_culture_5]  ],
["bl_tunic11", "Rich Tunic", [("BL_Tunic11",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 112 , weight(1)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(9)|difficulty(0) ,imodbits_cloth, [], [fac_culture_4,fac_culture_5]  ],

#dresses
["dress_1", "Dress", [("pictishdress2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["dress_2", "Dress", [("pictishdress3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["dress_3", "Dress", [("pictishdress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["dress_4", "Dress", [("briton_dress_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["dress_5", "Dress", [("briton_dress_e",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["dress_6", "Dress", [("kenttunik",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["dress_7", "Dress", [("peasant_dress_roman_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["dress_8", "Dress", [("peasant_dress_roman_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],

["roman_noble_dress_1", "Rich Roman Dress", [("roman_noble_dress_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 400 , weight(1)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_noble_dress_2", "Rich Roman Dress", [("roman_noble_dress_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 400 , weight(1)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_noble_dress_3", "Rich Roman Dress", [("roman_noble_dress_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 400 , weight(1)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_noble_dress_4", "Rich Roman Dress", [("roman_noble_dress_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 400 , weight(1)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], culture_roman ],

["roman_noble_dress_sleeveless_1", "Rich Roman Dress", [("roman_noble_dress_sleeveless_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 400 , weight(1)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[  (call_script, "script_init_roman_dress_arms"),]),], culture_roman ],
["roman_noble_dress_sleeveless_2", "Rich Roman Dress", [("roman_noble_dress_sleeveless_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 400 , weight(1)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[  (call_script, "script_init_roman_dress_arms"),]),], culture_roman ],
["roman_noble_dress_sleeveless_3", "Rich Roman Dress", [("roman_noble_dress_sleeveless_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 400 , weight(1)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[  (call_script, "script_init_roman_dress_arms"),]),], culture_roman ],
["roman_noble_dress_sleeveless_4", "Rich Roman Dress", [("roman_noble_dress_sleeveless_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 400 , weight(1)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[  (call_script, "script_init_roman_dress_arms"),]),], culture_roman ],

["lady_dress_ruby", "Dress", [("briton_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["lady_dress_green", "Blue Dress", [("briton_dress_d",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["lady_dress_blue", "Blue Dress", [("suknia_4",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["red_dress", "Red Dress", [("suknia_3",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["brown_dress", "Brown Dress", [("suknia_1",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["green_dress", "Green Dress", [("suknia_2",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["khergit_lady_dress", "Dress", [("briton_dress_e",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["khergit_lady_dress_b", "Dress", [("briton_dress_c",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_lady_dress", "Dress", [("sarranid_lady_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_lady_dress_b", "Dress", [("sarranid_lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_common_dress", "Dress", [("sarranid_common_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_common_dress_b", "Dress", [("sarranid_common_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_dress_a", "Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["sarranid_dress_b", "Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["sarranid_cloth_robe", "Worn Robe", [("sar_robe",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["sarranid_cloth_robe_b", "Worn Black Robe", [("sar_robe_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["sarranid_cloth_robe_c", "Worn White Robe", [("sar_robe_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],

["beduin_armor_a", "Worn Robe", [("beduin_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["beduin_armor_b", "Worn Robe", [("beduin_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],

["peasant_man_1", "Tunic", [("peasant_man_b",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["peasant_man_2", "Tunic", [("peasant_man_c",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["peasant_man_3", "Tunic", [("peasant_man_d",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["peasant_man_4", "Tunic", [("peasant_man_e",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["peasant_man_5", "Tunic", [("peasant_man_f",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["peasant_man_6", "Tunic", [("peasant_man_1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["peasant_man_7", "Tunic", [("peasant_archer",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["peasant_man_8", "Tunic", [("peasant_man_2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["peasant_man_9", "Tunic", [("peasant_man_3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise|itp_civilian,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["tunic_with_green_cape", "Tunic", [("peasant_man_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

["pants_5", "Pants", [("BL_Celts05",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 40 , weight(1)|abundance(100)|head_armor(0)|body_armor(2)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["pants_6", "Pants", [("BL_Celts06",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 40 , weight(1)|abundance(100)|head_armor(0)|body_armor(2)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["pants_7", "Pants", [("BL_Celts07",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 40 , weight(1)|abundance(100)|head_armor(0)|body_armor(2)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["pants_8", "Pants", [("BL_Celts08",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 40 , weight(1)|abundance(100)|head_armor(0)|body_armor(2)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["pants_9", "Pants", [("BL_Celts09",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 40 , weight(1)|abundance(100)|head_armor(0)|body_armor(2)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["pants_10", "Pants", [("BL_Celts10",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 40 , weight(1)|abundance(100)|head_armor(0)|body_armor(2)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["pants_11", "Pants", [("BL_Celts11",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 40 , weight(1)|abundance(100)|head_armor(0)|body_armor(2)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["pants_13", "Pants", [("BL_Celts13",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 40 , weight(1)|abundance(100)|head_armor(0)|body_armor(2)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

["linen_shirt", "Linen Tunic", [("white_linen_shirt",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 148 , weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["sleeveless_tunic", "Linen Tunic", [("short_tunic_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_male_arms"),]),], ],

["long_shirt_1", "Blue Tunic", [("BL_NT_Blue01",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 148 , weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["long_shirt_2", "Green Tunic", [("BL_NT_Blue07",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 148 , weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["long_shirt_3", "Blue Tunic", [("BL_NT_Blue04",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 148 , weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["long_shirt_4", "Green Tunic", [("BL_NT_Green01",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 148 , weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["long_shirt_5", "Blue Tunic", [("BL_NT_Green03",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 148 , weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["long_shirt_6", "Red Tunic", [("BL_NT_Red01",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 148 , weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["long_shirt_7", "Red Tunic", [("BL_NT_Red04",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 148 , weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["long_shirt_8", "Blue Tunic", [("BL_NT_Red05",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 148 , weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["long_shirt_9", "Red Tunic", [("frankish_long_tunic",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 148 , weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["long_shirt_10", "Blue Tunic", [("BL_NT_Blue02",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 148 , weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["long_shirt_11", "Red Tunic", [("BL_NT_Red02",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 148 , weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["long_shirt_12", "Red Tunic", [("BL_NT_Red03",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 148 , weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["long_shirt_13", "Green Tunic", [("BL_NT_Green02",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 148 , weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["long_shirt_14", "Green Tunic", [("BL_NT_Green101",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 148 , weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["long_shirt_15", "Red Tunic", [("BL_NT_Red121",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 148 , weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],

["short_tunic", "White Tunic", [("arena_tunicW_new",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 148, weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
 ["red_tunic", "Red Tunic", [("arena_tunicR_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 148 , weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
 ["green_tunic", "Green Tunic", [("arena_tunicG_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 148 , weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
 ["blue_tunic", "Blue Tunic", [("arena_tunicB_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 148 , weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
 ["yellow_tunic", "Yellow Tunic", [("arena_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 148 , weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],

["bandit_tunic_1", "Old Tunic", [("BL_Tunic_bandit_1",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 148, weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["bandit_tunic_2", "Old Tunic", [("BL_Tunic_bandit_2",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 148, weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["bandit_tunic_3", "Old Tunic", [("BL_Tunic_bandit_3",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 148, weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],

["pict_body_1m", "Pictish Warpaint", [("2celtbody",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 10 , weight(0)|abundance(100)|head_armor(0)|body_armor(4)|leg_armor(4)|difficulty(0) ,imodbits_none ],
["pict_body_2m", "Pictish Warpaint", [("3celtbody",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 10 , weight(0)|abundance(100)|head_armor(0)|body_armor(4)|leg_armor(4)|difficulty(0) ,imodbits_none ],
["pict_body_3m", "Pictish Warpaint", [("5celtbody",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 10 , weight(0)|abundance(100)|head_armor(0)|body_armor(4)|leg_armor(4)|difficulty(0) ,imodbits_none ],
["pict_body_4m", "Pictish Warpaint", [("6celtbody",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 10 , weight(0)|abundance(100)|head_armor(0)|body_armor(4)|leg_armor(4)|difficulty(0) ,imodbits_none ],

["pict_body_1f", "Pictish Warpaint", [("picta1",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 10 , weight(0)|abundance(100)|head_armor(0)|body_armor(4)|leg_armor(4)|difficulty(0) ,imodbits_none ],
["pict_body_2f", "Pictish Warpaint", [("picta2",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 10 , weight(0)|abundance(100)|head_armor(0)|body_armor(4)|leg_armor(4)|difficulty(0) ,imodbits_none ],
["pict_body_3f", "Pictish Warpaint", [("picta3",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 10 , weight(0)|abundance(100)|head_armor(0)|body_armor(4)|leg_armor(4)|difficulty(0) ,imodbits_none ],
["pict_body_4f", "Pictish Warpaint", [("picta4",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 10 , weight(0)|abundance(100)|head_armor(0)|body_armor(4)|leg_armor(4)|difficulty(0) ,imodbits_none ],

["cloaked_tunic_1", "Tunic with Cloak", [("linen_tunic_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, #red
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_2", "Tunic with Cloak", [("linen_tunic_d",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, #orange
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_3", "Tunic with Cloak", [("frankish_long_tunic",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, #frankish
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_4", "Tunic with Cloak", [("woolen_tunic_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, #green
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_5", "Tunic with Cloak", [("shirt_blk",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, #brown
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_6", "Tunic with Cloak", [("linen_tunic_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, #blue
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_7", "Tunic with Cloak", [("linen_tunic_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, #white
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_8", "Tunic with Cloak", [("shirt_blu",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, #blue
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_9", "Tunic with Cloak", [("shirt_red",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, #red
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_10", "Tunic with Cloak", [("white_linen_shirt",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_11", "Tunic with Cloak", [("light_brown_tunic",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_12", "Tunic with Cloak", [("shirt_ylw",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_16", "Tunic with Cloak", [("yellow_tunic_saxon",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_17", "Tunic with Cloak", [("generic_tunic_14",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],

["cloaked_generic_tunic_1", "Tunic with Cloak", [("generic_tunic_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_generic_tunic_2", "Tunic with Cloak", [("generic_tunic_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_generic_tunic_3", "Tunic with Cloak", [("generic_tunic_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_generic_tunic_4", "Tunic with Cloak", [("generic_tunic_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_generic_tunic_5", "Tunic with Cloak", [("generic_tunic_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_generic_tunic_6", "Tunic with Cloak", [("generic_tunic_6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_generic_tunic_7", "Tunic with Cloak", [("generic_tunic_7",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_generic_tunic_8", "Tunic with Cloak", [("generic_tunic_8",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_generic_tunic_9", "Tunic with Cloak", [("generic_tunic_9",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_generic_tunic_10", "Tunic with Cloak", [("generic_tunic_10",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_generic_tunic_11", "Tunic with Cloak", [("generic_tunic_11",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_generic_tunic_12", "Tunic with Cloak", [("generic_tunic_12",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_generic_tunic_13", "Tunic with Cloak", [("generic_tunic_13",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_generic_tunic_14", "Tunic with Cloak", [("generic_tunic_14",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_generic_tunic_15", "Tunic with Cloak", [("generic_tunic_15",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],

["cloaked_tunic_pants_1", "Tunic with Cloak", [("tunic_long_pants_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_pants_2", "Tunic with Cloak", [("tunic_long_pants_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_pants_3", "Tunic with Cloak", [("tunic_long_pants_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_pants_4", "Tunic with Cloak", [("tunic_long_pants_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_pants_5", "Tunic with Cloak", [("tunic_long_pants_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_pants_6", "Tunic with Cloak", [("tunic_long_pants_6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_pants_7", "Tunic with Cloak", [("tunic_long_pants_7",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_pants_8", "Tunic with Cloak", [("tunic_long_pants_8",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_pants_9", "Tunic with Cloak", [("tunic_long_pants_9",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_pants_10", "Tunic with Cloak", [("tunic_long_pants_10",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_6"),(cur_item_add_mesh, ":rand_accessory"),])]],

["cloaked_tunic_briton_1", "Tunic with Cloak", [("roman_shirt_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_briton_2", "Tunic with Cloak", [("roman_military_tunic_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_briton_3", "Tunic with Cloak", [("roman_shirt_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_briton_4", "Tunic with Cloak", [("roman_shirt_10",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_briton_5", "Tunic with Cloak", [("roman_military_tunic_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_briton_6", "Tunic with Cloak", [("roman_military_tunic_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_briton_7", "Tunic with Cloak", [("red_tunic",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_briton_8", "Tunic with Cloak", [("blue_tunic",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_briton_9", "Tunic with Cloak", [("roman_military_tunic_7",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_end"),(cur_item_add_mesh, ":rand_accessory"),])]],


["cloaked_tunic_falkirk_1", "Tunic with Cloak", [("falkirk_tunic_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_falkirk_2", "Tunic with Cloak", [("falkirk_tunic_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_falkirk_3", "Tunic with Cloak", [("falkirk_tunic_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_falkirk_4", "Tunic with Cloak", [("falkirk_tunic_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cloaked_tunic_falkirk_5", "Tunic with Cloak", [("falkirk_tunic_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
300 , weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_end"),(cur_item_add_mesh, ":rand_accessory"),])]],

["garamantian_armor_1", "Tunic with Pelt", [("garamantian_armor_1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 400 , weight(2.5)|abundance(10)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_short_tunic_arms"),]),], ],
["garamantian_armor_2", "Tunic with Pelt", [("garamantian_armor_2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 400 , weight(2.5)|abundance(10)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_short_tunic_arms"),]),], ],
["garamantian_armor_3", "Tunic with Pelt", [("garamantian_armor_3",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 400 , weight(2.5)|abundance(10)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_short_tunic_arms"),]),], ],

["peasant_leather_1", "Leather Tunic", [("peasant_leather_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 460 , weight(4)|abundance(90)|head_armor(0)|body_armor(25)|leg_armor(7)|difficulty(0) ,imodbits_leather ],
["peasant_leather_2", "Leather Tunic", [("peasant_leather_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 460 , weight(4)|abundance(90)|head_armor(0)|body_armor(25)|leg_armor(7)|difficulty(0) ,imodbits_leather ],
["peasant_leather_3", "Leather Tunic", [("peasant_leather_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 460 , weight(4)|abundance(90)|head_armor(0)|body_armor(25)|leg_armor(7)|difficulty(0) ,imodbits_leather ],
["peasant_leather_4", "Leather Tunic", [("peasant_leather_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 460 , weight(4)|abundance(90)|head_armor(0)|body_armor(25)|leg_armor(7)|difficulty(0) ,imodbits_leather ],

["peasant_leather_long_1", "Leather Tunic", [("peasant_leather_LS_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 588 , weight(6)|abundance(90)|head_armor(0)|body_armor(29)|leg_armor(7)|difficulty(0) ,imodbits_leather ],
["peasant_leather_long_2", "Leather Tunic", [("peasant_leather_LS_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 588 , weight(6)|abundance(90)|head_armor(0)|body_armor(29)|leg_armor(7)|difficulty(0) ,imodbits_leather ],
["peasant_leather_long_3", "Leather Tunic", [("peasant_leather_LS_3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 588 , weight(6)|abundance(90)|head_armor(0)|body_armor(29)|leg_armor(7)|difficulty(0) ,imodbits_leather ],
["peasant_leather_long_4", "Leather Tunic", [("peasant_leather_LS_4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 588 , weight(6)|abundance(90)|head_armor(0)|body_armor(29)|leg_armor(7)|difficulty(0) ,imodbits_leather ],

["nomad_leather_vest_1", "Leather Vest", [("khergit_vest_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 360 , weight(4)|abundance(90)|head_armor(0)|body_armor(20)|leg_armor(12)|difficulty(0) ,imodbits_leather, [], culture_hunnic+culture_alan ],
["nomad_leather_vest_2", "Leather Vest", [("khergit_vest_b_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 360 , weight(4)|abundance(90)|head_armor(0)|body_armor(20)|leg_armor(12)|difficulty(0) ,imodbits_leather, [], culture_hunnic+culture_alan ],
["nomad_leather_vest_3", "Leather Vest", [("khergit_vest_c_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 360 , weight(4)|abundance(90)|head_armor(0)|body_armor(20)|leg_armor(12)|difficulty(0) ,imodbits_leather, [], culture_hunnic+culture_alan ],
["nomad_leather_vest_4", "Leather Vest", [("khergit_vest_d_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 360 , weight(4)|abundance(90)|head_armor(0)|body_armor(20)|leg_armor(12)|difficulty(0) ,imodbits_leather, [], culture_hunnic+culture_alan ],

#New Light Armors
["ragged_outfit", "Ragged Outfit", [("ragged_outfit_a_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 580 , weight(5)|abundance(60)|head_armor(0)|body_armor(23)|leg_armor(9)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],
["goatist_tunic", "Ragged Outfit", [("goatist_tunic",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 580 , weight(5)|abundance(60)|head_armor(0)|body_armor(23)|leg_armor(9)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],
["nomad_robe", "Nomad Robe", [("nomad_robe_a",0)], itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0,890 , weight(15)|abundance(60)|head_armor(0)|body_armor(22)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["thick_coat_1", "Thick Coat", [("vae_thick_coat1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 420 , weight(7)|abundance(60)|head_armor(0)|body_armor(26)|leg_armor(4)|difficulty(0) ,imodbits_cloth],
["thick_coat_2", "Thick Coat", [("vae_thick_coat2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 420 , weight(7)|abundance(60)|head_armor(0)|body_armor(26)|leg_armor(4)|difficulty(0) ,imodbits_cloth],
["thick_coat_3", "Thick Coat", [("vae_thick_coat3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 420 , weight(7)|abundance(60)|head_armor(0)|body_armor(26)|leg_armor(4)|difficulty(0) ,imodbits_cloth],
["thick_coat_4", "Thick Coat", [("vae_thick_coat6",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 420 , weight(7)|abundance(60)|head_armor(0)|body_armor(26)|leg_armor(4)|difficulty(0) ,imodbits_cloth],
["thick_coat_5", "Thick Coat", [("vae_thick_coat10",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 420 , weight(7)|abundance(60)|head_armor(0)|body_armor(26)|leg_armor(4)|difficulty(0) ,imodbits_cloth],
["thick_coat_6", "Thick Coat", [("wei_xiadi_rod_thick_coat",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 420 , weight(7)|abundance(60)|head_armor(0)|body_armor(26)|leg_armor(4)|difficulty(0) ,imodbits_cloth],
["pelt_coat", "Pelt Coat", [("thick_coat_a",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 420, weight(7)|abundance(60)|head_armor(0)|body_armor(26)|leg_armor(2)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],
["rawhide_coat1", "Fur Coat", [("coat_of_plates1",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 320 , weight(8)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],
["rawhide_coat2", "Fur Coat", [("coat_of_plates1m",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 320 , weight(8)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],
["rawhide_coat3", "Fur Coat", [("coat_of_plates2",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 320 , weight(8)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],
["rawhide_coat4", "Fur Coat", [("coat_of_plates2m",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 320 , weight(8)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],
["rawhide_coat5", "Fur Coat", [("coat_of_plates3",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 320 , weight(8)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],
["rawhide_coat6", "Fur Coat", [("coat_of_plates3m",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 320 , weight(8)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],
["rawhide_coat7", "Fur Coat", [("coat_of_plates4",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 320 , weight(8)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],
["rawhide_coat8", "Fur Coat", [("coat_of_plates4m",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 320 , weight(8)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],
["rawhide_coat9", "Fur Coat", [("coat_of_plates5",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 320 , weight(8)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],
["rawhide_coat10", "Fur Coat", [("coat_of_plates5m",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 320 , weight(8)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],
["rawhide_coat11", "Fur Coat", [("coat_of_plates6m",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 320 , weight(8)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],

["subarmalis_1", "Subarmalis", [("roman_subarmalis_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 800 , weight(7)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])], culture_roman ],
["subarmalis_2", "Subarmalis", [("roman_subarmalis_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 800 , weight(7)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])], culture_roman ],
["subarmalis_3", "Subarmalis", [("roman_subarmalis_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 800 , weight(7)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])], culture_roman ],
["subarmalis_4", "Subarmalis", [("roman_subarmalis_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 800 , weight(7)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])], culture_roman ],
["subarmalis_5", "Subarmalis", [("roman_subarmalis_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 800 , weight(7)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])], culture_roman ],
["subarmalis_6", "Subarmalis", [("roman_subarmalis_6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 800 , weight(7)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])], culture_roman ],

["generic_subarmalis_1", "Subarmalis", [("generic_subarmalis_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 800 , weight(6)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], culture_gothic ],
["generic_subarmalis_2", "Subarmalis", [("generic_subarmalis_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 800 , weight(6)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], culture_gothic],
["generic_subarmalis_3", "Subarmalis", [("generic_subarmalis_3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 800 , weight(6)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], culture_gothic],
["generic_subarmalis_4", "Subarmalis", [("generic_subarmalis_4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 800 , weight(6)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], culture_gothic],
["generic_subarmalis_5", "Subarmalis", [("generic_subarmalis_5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 800 , weight(6)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], culture_gothic],
["generic_subarmalis_6", "Subarmalis", [("generic_subarmalis_6",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 800 , weight(6)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], culture_gothic ],
["generic_subarmalis_7", "Subarmalis", [("generic_subarmalis_7",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 800 , weight(6)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["generic_subarmalis_8", "Subarmalis", [("generic_subarmalis_8",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 800 , weight(6)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["generic_subarmalis_9", "Subarmalis", [("generic_subarmalis_9",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 800 , weight(6)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

["briton_subarmalis_1", "Subarmalis", [("briton_subarmalis_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 800 , weight(7)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])], culture_roman ],
["briton_subarmalis_2", "Subarmalis", [("briton_subarmalis_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 800 , weight(7)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])], culture_roman ],

["roman_subarmalis_new_1", "Subarmalis", [("roman_subarmalis_new_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 800 , weight(7)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])], culture_roman ],
["roman_subarmalis_new_2", "Subarmalis", [("roman_subarmalis_new_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 800 , weight(7)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])], culture_roman ],
["roman_subarmalis_new_3", "Subarmalis", [("roman_subarmalis_new_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 800 , weight(7)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])], culture_roman ],
["roman_subarmalis_new_4", "Subarmalis", [("roman_subarmalis_new_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 800 , weight(7)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])], culture_roman ],
["roman_subarmalis_new_5", "Subarmalis", [("roman_subarmalis_new_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 800 , weight(7)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])], culture_roman ],
["roman_subarmalis_new_6", "Subarmalis", [("roman_subarmalis_new_6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 800 , weight(7)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])], culture_roman ],
["roman_subarmalis_new_7", "Subarmalis", [("roman_subarmalis_new_7",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 800 , weight(7)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])], culture_roman ],
["roman_subarmalis_new_8", "Subarmalis", [("roman_subarmalis_new_8",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 800 , weight(7)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])], culture_roman ],
["roman_subarmalis_new_9", "Subarmalis", [("roman_subarmalis_new_9",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0, #For Quinta Macedonica
 1000 , weight(8)|abundance(50)|head_armor(0)|body_armor(35)|leg_armor(10)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])], culture_roman ],

["coptic_subarmalis", "Thorocomachus", [("coptic_padded_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1000 , weight(9)|abundance(60)|head_armor(0)|body_armor(34)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], [fac_culture_empire] ],

["sleeveless_padded_1", "Thorocomachus", [("sleeveless_padded_1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 800 , weight(6)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_male_arms"),]),], culture_african ],
["sleeveless_padded_2", "Thorocomachus", [("sleeveless_padded_2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 800 , weight(6)|abundance(60)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_male_arms"),]),], culture_african ],

["padded_full_1", "Long Subarmalis", [("padded_full_1",0)], itp_type_body_armor  |itp_covers_legs ,0,
 1200 , weight(8)|abundance(50)|head_armor(0)|body_armor(36)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["padded_full_2", "Long Subarmalis", [("padded_full_2",0)], itp_type_body_armor  |itp_covers_legs ,0,
 1200 , weight(8)|abundance(50)|head_armor(0)|body_armor(36)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],

["padded_leather", "Padded Leather", [("leather_armor_b",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,890 , weight(12)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(10)|difficulty(0) ,imodbits_leather, [], culture_germanic ],
["tribal_warrior_outfit", "Tribal Warrior Outfit", [("tribal_warrior_outfit_a_new",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,890 , weight(14)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(10)|difficulty(0) ,imodbits_leather ],
["leather_armor_c", "Leather over Tunic", [("saxon_leather_vest_blue",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 890 , weight(6)|abundance(60)|head_armor(0)|body_armor(36)|leg_armor(8)|difficulty(4) ,imodbits_leather, [], culture_germanic ],
["leather_armor_d", "Leather over Tunic", [("saxon_leather_vest_green",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 890 , weight(6)|abundance(60)|head_armor(0)|body_armor(36)|leg_armor(8)|difficulty(4) ,imodbits_leather, [], culture_germanic ],
["leather_armor_e", "Leather over Tunic", [("saxon_leather_vest_red",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 890 , weight(6)|abundance(60)|head_armor(0)|body_armor(36)|leg_armor(8)|difficulty(4) ,imodbits_leather, [], culture_germanic ], 

["steppe_armor", "Light Lamellar Vest", [("lamellar_leather",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 890 , weight(5)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(8)|difficulty(0) ,imodbits_leather ],

["leather_vest", "Leather Vest", [("leather_vest_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 460 , weight(4)|abundance(20)|head_armor(0)|body_armor(22)|leg_armor(7)|difficulty(0) ,imodbits_leather ],
["leather_jerkin", "Leather Tunic", [("BL_Tunic_Leather_1",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 540 , weight(6)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(6)|difficulty(0) ,imodbits_leather ],

["sarranid_leather_armor", "Eastern Leather Armor", [("sarranid_leather_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 650 , weight(9)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_armor, [], culture_sassanid ],

["archers_vest", "Linen Coat", [("eastern_light_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 600 , weight(7)|abundance(60)|head_armor(0)|body_armor(28)|leg_armor(8)|difficulty(0) ,imodbits_leather, [], culture_sassanid ],
#Mail Armor

["brigandine_red", "Mail", [("peasant_leather_mail_LS",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2590 , weight(13)|abundance(45)|head_armor(0)|body_armor(46)|leg_armor(8)|difficulty(8) ,imodbits_mail, [], culture_gothic ],

#Mail armor
#sleeveless ~46 body, 12 legs

["short_ragged_mail_1", "Sleeveless Mail", [("short_ragged_mail_1",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2560 , weight(12)|abundance(50)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(7) ,imodbits_mail],
["short_ragged_mail_2", "Sleeveless Mail", [("short_ragged_mail_2",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2560 , weight(12)|abundance(50)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(7) ,imodbits_mail],
["short_ragged_mail_3", "Sleeveless Mail", [("short_ragged_mail_3",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2560 , weight(12)|abundance(50)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(7) ,imodbits_mail],
["short_ragged_mail_4", "Sleeveless Mail", [("short_ragged_mail_4",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2560 , weight(12)|abundance(50)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(7) ,imodbits_mail],
["short_ragged_mail_5", "Sleeveless Mail", [("short_ragged_mail_5",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2560 , weight(12)|abundance(50)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(7) ,imodbits_mail],
["short_ragged_mail_6", "Sleeveless Mail", [("short_ragged_mail_6",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2560 , weight(12)|abundance(50)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(7) ,imodbits_mail],
["short_ragged_mail_7", "Sleeveless Mail", [("short_ragged_mail_7",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2560 , weight(12)|abundance(50)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(7) ,imodbits_mail],
["short_ragged_mail_8", "Sleeveless Mail", [("short_ragged_mail_8",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2560 , weight(12)|abundance(50)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(7) ,imodbits_mail],
["short_ragged_mail_9", "Sleeveless Mail", [("short_ragged_mail_9",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2560 , weight(12)|abundance(50)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(7) ,imodbits_mail],
["short_ragged_mail_10", "Sleeveless Mail", [("short_ragged_mail_10",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2560 , weight(12)|abundance(50)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(7) ,imodbits_mail],
["short_ragged_mail_11", "Sleeveless Mail", [("short_ragged_mail_11",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2560 , weight(12)|abundance(50)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(7) ,imodbits_mail],
["short_ragged_mail_12", "Sleeveless Mail", [("short_ragged_mail_12",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2560 , weight(12)|abundance(50)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(7) ,imodbits_mail],

["short_slavic_mail_1", "Sleeveless Mail", [("short_slavic_mail_1",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 2560 , weight(12)|abundance(50)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(7) ,imodbits_mail ],
["short_slavic_mail_2", "Sleeveless Mail", [("short_slavic_mail_2",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 2560 , weight(12)|abundance(50)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(7) ,imodbits_mail ],
["pictish_short_mail_1", "Sleeveless Mail", [("pictish_short_mail_1",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 2560 , weight(12)|abundance(50)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(7) ,imodbits_mail, [], culture_celtic ],
["pictish_short_mail_2", "Sleeveless Mail", [("pictish_short_mail_2",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 2560 , weight(12)|abundance(50)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(7) ,imodbits_mail, [], culture_celtic ],
["pictish_short_mail_3", "Sleeveless Mail", [("pictish_short_mail_3",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 2560 , weight(12)|abundance(50)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(7) ,imodbits_mail, [], culture_celtic ],

["457_mail_short_1", "Hamata", [("457_mail_short_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 2600 , weight(13)|abundance(45)|head_armor(0)|body_armor(46)|leg_armor(14)|difficulty(8) ,imodbits_mail, [], culture_roman ],
["457_mail_short_2", "Hamata", [("457_mail_short_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 2600 , weight(13)|abundance(45)|head_armor(0)|body_armor(46)|leg_armor(14)|difficulty(8) ,imodbits_mail, [], culture_roman ],
["457_mail_short_3", "Hamata", [("457_mail_short_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 2600 , weight(13)|abundance(45)|head_armor(0)|body_armor(46)|leg_armor(14)|difficulty(8) ,imodbits_mail, [], culture_roman ],
["457_mail_short_4", "Hamata", [("457_mail_short_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 2600 , weight(13)|abundance(45)|head_armor(0)|body_armor(46)|leg_armor(14)|difficulty(8) ,imodbits_mail, [], culture_roman ],
["457_mail_short_5", "Hamata", [("457_mail_short_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 2600 , weight(13)|abundance(45)|head_armor(0)|body_armor(46)|leg_armor(14)|difficulty(8) ,imodbits_mail, [], culture_roman ], #for marines

["short_roman_mail_1", "Hamata", [("short_roman_mail_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 2600 , weight(13)|abundance(45)|head_armor(0)|body_armor(46)|leg_armor(14)|difficulty(8) ,imodbits_mail, [], culture_roman ],
["short_roman_mail_2", "Hamata", [("short_roman_mail_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 2600 , weight(13)|abundance(45)|head_armor(0)|body_armor(46)|leg_armor(14)|difficulty(8) ,imodbits_mail, [], culture_roman ],
["short_roman_mail_3", "Hamata", [("short_roman_mail_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 2600 , weight(13)|abundance(45)|head_armor(0)|body_armor(46)|leg_armor(14)|difficulty(8) ,imodbits_mail, [], culture_roman ],
["short_roman_mail_4", "Hamata", [("short_roman_mail_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 2600 , weight(13)|abundance(45)|head_armor(0)|body_armor(46)|leg_armor(14)|difficulty(8) ,imodbits_mail, [], culture_roman ],

["mail_african_1", "Sleeveless Mail", [("mail_african_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 2600 , weight(10)|abundance(40)|head_armor(0)|body_armor(45)|leg_armor(14)|difficulty(0) ,imodbits_mail, [(ti_on_init_item,[(call_script, "script_init_short_tunic_arms"),]),], culture_african ],

#short sleeved ~54 body, 12 legs

["sassanid_mail_shirt_1", "Mail Shirt", [("mid_sassanid_mail_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_sassanid ],
["sassanid_mail_shirt_2", "Mail Shirt", [("mid_sassanid_mail_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_sassanid ],
["sassanid_mail_shirt_3", "Mail Shirt", [("mid_sassanid_mail_3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_sassanid ],
["sassanid_mail_shirt_4", "Mail Shirt", [("mid_sassanid_mail_4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_sassanid ],
["sassanid_mail_shirt_5", "Mail Shirt", [("mid_sassanid_mail_5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_sassanid ],
["sassanid_mail_shirt_6", "Mail Shirt", [("mid_sassanid_mail_6",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_sassanid ],

["hunnic_mail_1", "Mail Shirt", [("hunnic_mail_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_hunnic+culture_alan ],

["mid_generic_mail_1", "Mail Shirt", [("mid_generic_mail_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ],
["mid_generic_mail_2", "Mail Shirt", [("mid_generic_mail_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_gothic ],
["mid_generic_mail_3", "Mail Shirt", [("mid_generic_mail_3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ],
["mid_generic_mail_4", "Mail Shirt", [("mid_generic_mail_4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ],
["mid_generic_mail_5", "Mail Shirt", [("mid_generic_mail_5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ],
["mid_generic_mail_6", "Mail Shirt", [("mid_generic_mail_6",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ],
["mid_generic_mail_7", "Mail Shirt", [("mid_generic_mail_7",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_gothic ],
["mid_generic_mail_8", "Mail Shirt", [("mid_generic_mail_8",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ],
["mid_generic_mail_9", "Mail Shirt", [("mid_generic_mail_9",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_gothic ], #was brunjo
["mid_generic_mail_10", "Mail Shirt", [("mid_generic_mail_10",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_gothic ],
["mid_generic_mail_11", "Mail Shirt", [("mid_generic_mail_11",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_gothic ],
["mid_generic_mail_12", "Mail Shirt", [("mid_generic_mail_12",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_gothic ],
["mid_generic_mail_13", "Mail Shirt", [("mid_generic_mail_13",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_gothic ],
["mid_generic_mail_14", "Mail Shirt", [("mid_generic_mail_14",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ],
["mid_generic_mail_15", "Mail Shirt", [("mid_generic_mail_15",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ],
["mid_generic_mail_16", "Mail Shirt", [("mid_generic_mail_16",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ],
["mid_generic_mail_17", "Mail Shirt", [("mid_generic_mail_17",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ],
["mid_generic_mail_18", "Mail Shirt", [("mid_generic_mail_18",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ],
["mid_generic_mail_19", "Mail Shirt", [("mid_generic_mail_19",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ],
["mid_generic_mail_20", "Mail Shirt", [("mid_generic_mail_20",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ],
["mid_generic_mail_21", "Mail Shirt", [("mid_generic_mail_21",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ],
["mid_generic_mail_22", "Mail Shirt", [("mid_generic_mail_22",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail ],
["mid_generic_mail_23", "Mail Shirt", [("mid_generic_mail_23",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ],
["mid_generic_mail_24", "Mail Shirt", [("mid_generic_mail_24",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ],
["mid_generic_mail_25", "Mail Shirt", [("mid_generic_mail_25",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ], #rich mail
["mid_generic_mail_26", "Mail Shirt", [("mid_generic_mail_26",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ], #rich mail
["mid_generic_mail_27", "Mail Shirt", [("mid_generic_mail_27",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ], #rich mail
["mid_generic_mail_28", "Mail Shirt", [("mid_generic_mail_28",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ], #rich mail
["mid_generic_mail_29", "Mail Shirt", [("mid_generic_mail_29",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ], #rich mail

["mail_shirt", "Mail Shirt", [("mercenary_mail",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail ],
["byrnie", "Mail Shirt", [("english_byrne",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 2840 , weight(15)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_germanic ],

["rich_mail_1", "Mail Shirt", [("rich_mail_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2840 , weight(15)|abundance(30)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_gothic+culture_germanic ], #to be used by the goths
["rich_mail_2", "Mail Shirt", [("rich_mail_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2840 , weight(15)|abundance(30)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_gothic+culture_germanic ], #to be used by the goths
["rich_mail_3", "Mail Shirt", [("rich_mail_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2840 , weight(15)|abundance(30)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_gothic+culture_germanic ], #to be used by the goths
["rich_mail_4", "Mail Shirt", [("rich_mail_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2840 , weight(15)|abundance(30)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_gothic+culture_germanic ], #to be used by the goths
["rich_mail_5", "Mail Shirt", [("rich_mail_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2840 , weight(15)|abundance(30)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_gothic+culture_germanic ], #to be used by the goths
["rich_mail_6", "Mail Shirt", [("rich_mail_6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2840 , weight(15)|abundance(30)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_gothic+culture_germanic ], #to be used by the goths
["rich_mail_7", "Mail Shirt", [("rich_mail_7",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2840 , weight(15)|abundance(30)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_gothic+culture_germanic ], #to be used by the goths
["rich_mail_8", "Mail Shirt", [("rich_mail_8",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2840 , weight(15)|abundance(30)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_gothic+culture_germanic ], #to be used by the goths
["rich_mail_9", "Mail Shirt", [("rich_mail_9",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2840 , weight(15)|abundance(30)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_gothic+culture_germanic ], #to be used by the slavs
["rich_mail_10", "Mail Shirt", [("rich_mail_10",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2840 , weight(15)|abundance(30)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_gothic+culture_germanic ], #to be used by the slavs
["rich_mail_11", "Mail Shirt", [("rich_mail_11",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 2840 , weight(15)|abundance(30)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_gothic+culture_germanic ], #to be used by the slavs

["457_mail_shirt_1", "Hamata", [("457_mail_shirt_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3000 , weight(16.5)|abundance(30)|head_armor(0)|body_armor(55)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],
["457_mail_shirt_2", "Hamata", [("457_mail_shirt_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3000 , weight(16.5)|abundance(30)|head_armor(0)|body_armor(55)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],
["457_mail_shirt_3", "Hamata", [("457_mail_shirt_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3000 , weight(16.5)|abundance(30)|head_armor(0)|body_armor(55)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],
["457_mail_shirt_4", "Hamata", [("457_mail_shirt_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3000 , weight(16.5)|abundance(30)|head_armor(0)|body_armor(55)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],
["457_mail_shirt_5", "Hamata", [("457_mail_shirt_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3000 , weight(16.5)|abundance(30)|head_armor(0)|body_armor(55)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ], #for marines
["legio_v_mail", "Hamata", [("legio_v_mail",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0, #unique variant for legio V
 3000 , weight(16.5)|abundance(20)|head_armor(0)|body_armor(55)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],

["mid_roman_mail_1", "Hamata", [("mid_roman_mail_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3000 , weight(16.5)|abundance(30)|head_armor(0)|body_armor(55)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],
["mid_roman_mail_2", "Hamata", [("mid_roman_mail_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3000 , weight(16.5)|abundance(30)|head_armor(0)|body_armor(55)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],
["mid_roman_mail_3", "Hamata", [("mid_roman_mail_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3000 , weight(16.5)|abundance(30)|head_armor(0)|body_armor(55)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],
["mid_roman_mail_4", "Hamata", [("mid_roman_mail_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3000 , weight(16.5)|abundance(30)|head_armor(0)|body_armor(55)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],
["mid_roman_mail_5", "Hamata", [("mid_roman_mail_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3000 , weight(16.5)|abundance(30)|head_armor(0)|body_armor(55)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],
["mid_roman_mail_6", "Hamata", [("mid_roman_mail_6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3000 , weight(16.5)|abundance(30)|head_armor(0)|body_armor(55)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],
["mid_roman_mail_7", "Hamata", [("mid_roman_mail_7",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3000 , weight(16.5)|abundance(30)|head_armor(0)|body_armor(55)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],
["mid_roman_mail_8", "Hamata", [("mid_roman_mail_8",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3000 , weight(16.5)|abundance(30)|head_armor(0)|body_armor(55)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],

#long sleeved ~58 body, 12 legs

["long_mail_new_1", "Long Mail", [("long_mail_new_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3500 , weight(19)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_gothic+culture_germanic],
["long_mail_new_2", "Long Mail", [("long_mail_new_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3500 , weight(19)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_gothic+culture_germanic],
["long_mail_new_3", "Long Mail", [("long_mail_new_3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3500 , weight(19)|abundance(20)|head_armor(4)|body_armor(58)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_gothic+culture_germanic],
["long_mail_new_4", "Long Mail", [("long_mail_new_4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3500 , weight(19)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_gothic+culture_germanic],
["long_mail_new_5", "Long Mail", [("long_mail_new_5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3500 , weight(19)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_gothic+culture_germanic],
["long_mail_new_6", "Long Mail", [("long_mail_new_6",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3500 , weight(19)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_gothic+culture_germanic ],
["long_mail_new_7", "Long Mail", [("long_mail_new_7",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3500 , weight(19)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_gothic+culture_germanic ],
["long_mail_new_8", "Long Mail", [("long_mail_new_8",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3500 , weight(19)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_gothic+culture_germanic ],
["long_mail_new_9", "Long Mail", [("long_mail_new_9",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3500 , weight(19)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_gothic+culture_germanic ],

["sassanid_heavy_mail", "Sassanid Mail", [("sassanid_heavy_mail",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3500 , weight(19)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_sassanid+culture_caucasian ],
["sassanid_heavy_inf_mail", "Sassanid Mail", [("sassanid_heavy_mail3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3500 , weight(19)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_sassanid+culture_caucasian ],
["sassanid_heavy_mail_1", "Sassanid Mail", [("sassanid_heavy_mail2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3500 , weight(19)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_sassanid+culture_caucasian ],
["sassanid_long_mail_1", "Mail", [("sassanid_long_mail_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3500 , weight(19)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(12)|difficulty(11) ,imodbits_mail, [], culture_sassanid+culture_caucasian ],

["457_mail_long_1", "Hamata", [("457_mail_long_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3700 , weight(19)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],
["457_mail_long_2", "Hamata", [("457_mail_long_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3700 , weight(19)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],
["457_mail_long_3", "Hamata", [("457_mail_long_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3700 , weight(19)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],
["457_mail_long_4", "Hamata", [("457_mail_long_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3700 , weight(19)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],

["long_roman_mail_1", "Hamata", [("long_roman_mail_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3700 , weight(19)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],
["long_roman_mail_2", "Hamata", [("long_roman_mail_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3700 , weight(19)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],
["long_roman_mail_3", "Hamata", [("long_roman_mail_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3700 , weight(19)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],
["long_roman_mail_4", "Hamata", [("long_roman_mail_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3700 , weight(19)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],
["long_roman_mail_5", "Hamata", [("long_roman_mail_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3700 , weight(19)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(14)|difficulty(11) ,imodbits_mail, [], culture_roman ],

["long_briton_mail_1", "Hamata with Cloak", [("long_roman_mail_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 3700 , weight(19)|abundance(15)|head_armor(0)|body_armor(58)|leg_armor(14)|difficulty(11) ,imodbits_mail,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["long_briton_mail_2", "Hamata with Cloak", [("long_roman_mail_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 3700 , weight(19)|abundance(15)|head_armor(0)|body_armor(58)|leg_armor(14)|difficulty(11) ,imodbits_mail,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["long_briton_mail_3", "Hamata with Cloak", [("long_roman_mail_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 3700 , weight(19)|abundance(15)|head_armor(0)|body_armor(58)|leg_armor(14)|difficulty(11) ,imodbits_mail,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_cloak_addon_1","str_cloak_addon_end"),(cur_item_add_mesh, ":rand_accessory"),])]],

["candidati_mail", "Hamata", [("candidati_mail",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3700 , weight(18)|abundance(1)|head_armor(0)|body_armor(59)|leg_armor(13)|difficulty(11) ,imodbits_mail, [], [fac_culture_empire] ],

#full mail (cataphract) ~60 body, 16 legs 

["sarranid_elite_armor", "Long Cataphract Mail", [("armor_medium_tyrk_e",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 5800 , weight(22)|abundance(10)|head_armor(0)|body_armor(60)|leg_armor(18)|difficulty(15) ,imodbits_mail, [], culture_sassanid ],
["long_cataphract_mail", "Long Cataphract Mail", [("cataphract_mail_3",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 5800 , weight(22)|abundance(10)|head_armor(0)|body_armor(60)|leg_armor(18)|difficulty(15) ,imodbits_mail, [], culture_sassanid ],
["coat_of_plates_red", "Mail", [("cataphract_mail_1",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 5800 , weight(20)|abundance(10)|head_armor(0)|body_armor(60)|leg_armor(18)|difficulty(15) ,imodbits_mail ],
["arabian_armor_b", "Mail", [("cataphract_mail_2",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 5800 , weight(20)|abundance(10)|head_armor(0)|body_armor(60)|leg_armor(18)|difficulty(15) ,imodbits_mail ],
["roman_military_mail_12", "Hamata", [("roman_military_mail_12",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 5800 , weight(20)|abundance(10)|head_armor(0)|body_armor(60)|leg_armor(18)|difficulty(15) ,imodbits_mail, [], culture_roman ],

#misc mail armors - mostly unused (for now)
["mail_with_surcoat", "Long Mail", [("mail_heavy_sleeveless_1",0)], itp_type_body_armor  |itp_covers_legs ,0, 4000 , weight(19)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(15)|difficulty(11) ,imodbits_mail, [(ti_on_init_item,[(call_script, "script_init_male_arms"),]),], ],
["surcoat_over_mail", "Long Mail", [("mail_heavy_sleeveless_2",0)], itp_type_body_armor  |itp_covers_legs ,0, 4000 , weight(19)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(15)|difficulty(11) ,imodbits_mail, [(ti_on_init_item,[(call_script, "script_init_male_arms"),]),], ],
["mail_hauberk", "Long Mail", [("mail_heavy_sleeveless_3",0)], itp_type_body_armor  |itp_covers_legs ,0, 4000 , weight(19)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(15)|difficulty(11) ,imodbits_mail, [(ti_on_init_item,[(call_script, "script_init_male_arms"),]),], ],

#only for nubians
["nubian_scale_armor_1", "Hide Scale Armor", [("nubian_scale_armor_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1500 , weight(7)|abundance(40)|head_armor(0)|body_armor(38)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_short_tunic_arms"),]),], culture_african ],
["nubian_scale_armor_2", "Hide Scale Armor", [("nubian_scale_armor_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1500 , weight(7)|abundance(40)|head_armor(0)|body_armor(38)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_short_tunic_arms"),]),], culture_african ],

#Scale and Lamellar Armor
#vest ~45 body, 10 legs

["steppe_plated_armor_6", "Plated Vest", [("steppe_plated_armor_6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0, #used for mordvins, huns
 2000 , weight(10)|abundance(40)|head_armor(0)|body_armor(43)|leg_armor(6)|difficulty(6) ,imodbits_scale, [], culture_hunnic ],
["steppe_plated_armor_7", "Plated Vest", [("steppe_plated_armor_7",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0, #used for mordvins, huns
 2000 , weight(10)|abundance(40)|head_armor(0)|body_armor(43)|leg_armor(6)|difficulty(6) ,imodbits_scale, [], culture_hunnic ],
["steppe_plated_armor_8", "Plated Vest", [("steppe_plated_armor_8",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0, #used for mordvins, huns
 2000 , weight(10)|abundance(40)|head_armor(0)|body_armor(43)|leg_armor(6)|difficulty(6) ,imodbits_scale, [], culture_hunnic ],
["steppe_plated_armor_9", "Plated Vest", [("steppe_plated_armor_9",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0, #used for mordvins, huns
 2000 , weight(10)|abundance(40)|head_armor(0)|body_armor(43)|leg_armor(6)|difficulty(6) ,imodbits_scale, [], culture_hunnic ],

["lamellar_vest_khergit", "Lamellar Vest", [("lamellar_vest_b",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 2200 , weight(12)|abundance(35)|head_armor(0)|body_armor(45)|leg_armor(10)|difficulty(6) ,imodbits_scale, [], culture_hunnic+culture_alan ],
["lamellar_vest", "Lamellar Vest", [("lamellar_vest_a",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 2200 , weight(12)|abundance(35)|head_armor(0)|body_armor(45)|leg_armor(10)|difficulty(6) ,imodbits_scale, [], culture_hunnic+culture_alan ],
["lamellar_vest_c", "Lamellar Vest", [("lamellar_vest_c",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 2200 , weight(12)|abundance(35)|head_armor(0)|body_armor(45)|leg_armor(10)|difficulty(6) ,imodbits_scale, [], culture_hunnic+culture_alan ],
["lamellar_vest_d", "Lamellar Vest", [("lamellar_vest_d",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 2200 , weight(12)|abundance(35)|head_armor(0)|body_armor(45)|leg_armor(10)|difficulty(6) ,imodbits_scale, [], culture_hunnic+culture_alan ],

["hunnic_kaftan_lamellar_1", "Lamellar Vest", [("hunnic_kaftan_lamellar_1",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 2200 , weight(12)|abundance(35)|head_armor(0)|body_armor(45)|leg_armor(10)|difficulty(6) ,imodbits_scale, [], culture_hunnic+culture_alan ],
["hunnic_kaftan_lamellar_2", "Lamellar Vest", [("hunnic_kaftan_lamellar_2",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 2200 , weight(12)|abundance(35)|head_armor(0)|body_armor(45)|leg_armor(10)|difficulty(6) ,imodbits_scale, [], culture_hunnic+culture_alan ],
["hunnic_kaftan_lamellar_3", "Lamellar Vest", [("hunnic_kaftan_lamellar_3",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 2200 , weight(12)|abundance(35)|head_armor(0)|body_armor(45)|leg_armor(10)|difficulty(6) ,imodbits_scale, [], culture_hunnic+culture_alan ],

["roman_lamellar_1", "Lamellar Vest", [("roman_lamellar_1",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 2200 , weight(12)|abundance(35)|head_armor(0)|body_armor(45)|leg_armor(10)|difficulty(6) ,imodbits_scale, [], [fac_culture_empire] ],

["lombard_lamellar_1", "Lamellar Vest", [("lombard_lamellar_1",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 2200 , weight(12)|abundance(35)|head_armor(0)|body_armor(45)|leg_armor(10)|difficulty(6) ,imodbits_scale, [], [fac_culture_2] ],
["lombard_lamellar_2", "Lamellar Vest", [("lombard_lamellar_2",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 2200 , weight(12)|abundance(35)|head_armor(0)|body_armor(45)|leg_armor(10)|difficulty(6) ,imodbits_scale, [], [fac_culture_2] ],

#mid ~48 body, 10 legs

["kaftan_lamellar_1", "Lamellar Vest", [("kaftan_lamellar_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3100 , weight(12)|abundance(25)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(7),imodbits_scale, [], culture_hunnic+culture_alan ],
["kaftan_lamellar_2", "Lamellar Vest", [("kaftan_lamellar_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3100 , weight(12)|abundance(25)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(7),imodbits_scale, [], culture_hunnic+culture_alan ],
["kaftan_lamellar_3", "Lamellar Vest", [("kaftan_lamellar_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3100 , weight(12)|abundance(25)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(7),imodbits_scale, [], culture_hunnic+culture_alan ],
["kaftan_lamellar_4", "Lamellar Vest", [("kaftan_lamellar_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3100 , weight(12)|abundance(25)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(7),imodbits_scale, [], culture_hunnic+culture_alan ],
["kaftan_lamellar_5", "Lamellar Vest", [("kaftan_lamellar_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3100 , weight(12)|abundance(25)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(7),imodbits_scale, [], culture_hunnic+culture_alan ],
["kaftan_lamellar_6", "Lamellar Vest", [("kaftan_lamellar_6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3100 , weight(12)|abundance(25)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(7),imodbits_scale, [], culture_hunnic+culture_alan ],
["kaftan_lamellar_7", "Lamellar Vest", [("kaftan_lamellar_7",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3100 , weight(12)|abundance(25)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(7),imodbits_scale, [], culture_hunnic+culture_alan ],
["kaftan_lamellar_8", "Lamellar Vest", [("kaftan_lamellar_8",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3100 , weight(12)|abundance(25)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(7),imodbits_scale, [], culture_hunnic+culture_alan ],
["kaftan_lamellar_9", "Lamellar Vest", [("kaftan_lamellar_9",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3100 , weight(12)|abundance(25)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(7),imodbits_scale, [], culture_hunnic+culture_alan ],
["kaftan_lamellar_10", "Lamellar Vest", [("kaftan_lamellar_10",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3100 , weight(12)|abundance(25)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(7),imodbits_scale, [], culture_hunnic+culture_alan ],
["kaftan_lamellar_11", "Lamellar Vest", [("kaftan_lamellar_11",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3100 , weight(12)|abundance(25)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(7),imodbits_scale, [], culture_hunnic+culture_alan ],
["kaftan_lamellar_12", "Lamellar Vest", [("kaftan_lamellar_12",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3100 , weight(12)|abundance(25)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(7),imodbits_scale, [], culture_hunnic+culture_sassanid ],
["kaftan_lamellar_13", "Lamellar Vest", [("kaftan_lamellar_13",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 3100 , weight(12)|abundance(25)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(7),imodbits_scale, [], culture_hunnic+culture_sassanid ],

["scale_armor", "Squamata", [("light_scale_armor_new",0)], itp_type_body_armor|itp_covers_legs ,0,
 3300 , weight(14)|abundance(10)|head_armor(0)|body_armor(48)|leg_armor(10)|difficulty(10) ,imodbits_scale ],

#sleeveless/short sleeved ~52 body, 10 legs

["medium_scale_1", "Squamata", [("medium_scale_1",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale ],
["medium_scale_2", "Squamata", [("medium_scale_2",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale ],
["medium_scale_3", "Squamata", [("medium_scale_3",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, #to be used by gothic lords
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale ],
["medium_scale_4", "Squamata", [("medium_scale_4",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale ],
["medium_scale_5", "Squamata", [("medium_scale_5",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale ],

["roman_light_scale_1", "Squamata", [("roman_light_scale_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["roman_light_scale_2", "Squamata", [("roman_light_scale_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["roman_light_scale_3", "Squamata", [("roman_light_scale_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["roman_light_scale_4", "Squamata", [("roman_light_scale_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["roman_light_scale_5", "Squamata", [("roman_light_scale_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])]],

["banded_armor", "Squamata", [("roman_squamata_new_1_light",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["cuir_bouilli", "Squamata", [("roman_squamata_new_2_light",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["black_armor", "Squamata", [("roman_squamata_new_3_light",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])]],

["roman_rigid_scale_1", "Squamata", [("roman_rigid_scale_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["roman_rigid_scale_2", "Squamata", [("roman_rigid_scale_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["roman_rigid_scale_3", "Squamata", [("roman_rigid_scale_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["roman_rigid_scale_4", "Squamata", [("roman_rigid_scale_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["roman_rigid_scale_5", "Squamata", [("roman_rigid_scale_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])]],
["roman_rigid_scale_6", "Squamata", [("roman_rigid_scale_6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale,
[(ti_on_init_item,[(store_random_in_range,":rand_accessory","str_roman_focale_1","str_roman_focale_end"),(cur_item_add_mesh, ":rand_accessory"),])]],

["roman_squamata_1", "Squamata", [("roman_squamata_1",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale, [], culture_roman ], #romans
["roman_squamata_2", "Squamata", [("roman_squamata_2",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale, [], culture_roman ], #romans
["roman_squamata_3", "Squamata", [("roman_squamata_3",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale, [], culture_roman ], #romano-britons
["roman_squamata_4", "Squamata", [("roman_squamata_4",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale, [], culture_roman ], #roman lords
["roman_squamata_5", "Squamata", [("roman_squamata_5",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale, [], culture_germanic ], #germans

["rich_squamata_1", "Rich Squamata", [("rich_squamata_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 4300 , weight(15)|abundance(5)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(9) ,imodbits_scale, [], [fac_culture_empire] ],
["rich_squamata_2", "Rich Squamata", [("rich_squamata_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 4300 , weight(15)|abundance(5)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(9) ,imodbits_scale, [], [fac_culture_empire] ],
["rich_squamata_3", "Rich Squamata", [("rich_squamata_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 4300 , weight(15)|abundance(5)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(9) ,imodbits_scale, [], culture_gothic ],
["rich_squamata_4", "Rich Squamata", [("rich_squamata_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,
 4300 , weight(15)|abundance(5)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(9) ,imodbits_scale, [], culture_gothic ],

["coptic_scale_cuirass_1", "Squamata", [("coptic_scale_cuirass_1",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale, [], [fac_culture_empire] ], #copts
["coptic_scale_cuirass_2", "Squamata", [("coptic_scale_cuirass_2",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale, [], [fac_culture_empire] ], #copts
["roman_scale_cuirass_1", "Squamata", [("roman_scale_cuirass_1",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale, [], culture_roman ], #romans
["roman_scale_cuirass_2", "Squamata", [("roman_scale_cuirass_2",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale, [], culture_roman ], #romans
["vaegir_elite_armor", "Briton Squamata", [("briton_scale_cuirass_1",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale, [], culture_roman ],
["plate_armor", "Briton Squamata", [("briton_scale_cuirass_2",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale, [], culture_roman ],
["khergit_elite_armor", "Briton Squamata", [("briton_scale_cuirass_3",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 3820 , weight(15)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(10)|difficulty(9) ,imodbits_scale, [], culture_roman ],

["candidati_squamata_1", "Squamata", [("candidati_squamata_1",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs ,0, #same style as the other ones, limited to one troop
 4200 , weight(15)|abundance(1)|head_armor(0)|body_armor(56)|leg_armor(11)|difficulty(10) ,imodbits_scale, [], [fac_culture_empire] ], #romans
["candidati_squamata_2", "Squamata", [("candidati_squamata_2",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs ,0, #same style as the other ones, limited to one troop
 4200 , weight(14)|abundance(1)|head_armor(0)|body_armor(56)|leg_armor(11)|difficulty(10) ,imodbits_scale, [], [fac_culture_empire] ], #romans
["candidati_squamata_3", "Squamata", [("candidati_squamata_3",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs ,0, #same style as the other ones, limited to one troop
 4200 , weight(14)|abundance(1)|head_armor(0)|body_armor(56)|leg_armor(11)|difficulty(10) ,imodbits_scale, [], [fac_culture_empire] ], #romans

#short sleeved ~54 body, 10-15 legs
["steppe_plated_armor_4", "Mail with Plates", [("steppe_plated_armor_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0, #used for mordvins, huns
 4150 , weight(18)|abundance(15)|head_armor(0)|body_armor(55)|leg_armor(12)|difficulty(11) ,imodbits_scale, [], culture_hunnic ],
["steppe_plated_armor_5", "Mail with Plates", [("steppe_plated_armor_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0, #used for mordvins, huns
 4150 , weight(18)|abundance(15)|head_armor(0)|body_armor(55)|leg_armor(12)|difficulty(11) ,imodbits_scale, [], culture_hunnic ],

["sassanid_scale_1", "Scale Coat", [("sassanid_scale_1",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 4150 , weight(18)|abundance(20)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_scale, [], culture_sassanid+culture_caucasian ],
["sassanid_scale_2", "Scale Coat", [("sassanid_scale_2",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 4150 , weight(18)|abundance(20)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_scale, [], culture_sassanid+culture_caucasian ],

["eastern_scale_1", "Scale Coat", [("eastern_scale_1",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 4300 , weight(19)|abundance(20)|head_armor(0)|body_armor(54)|leg_armor(15)|difficulty(11) ,imodbits_scale, [], culture_sassanid+culture_caucasian ],
["eastern_scale_2", "Scale Coat", [("eastern_scale_2",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 4300 , weight(19)|abundance(20)|head_armor(0)|body_armor(54)|leg_armor(15)|difficulty(11) ,imodbits_scale, [], culture_sassanid+culture_caucasian ],
["eastern_scale_3", "Scale Coat", [("eastern_scale_3",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 4300 , weight(19)|abundance(20)|head_armor(0)|body_armor(54)|leg_armor(15)|difficulty(11) ,imodbits_scale, [], culture_sassanid+culture_caucasian ],
["eastern_scale_4", "Scale Coat", [("eastern_scale_4",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 4300 , weight(19)|abundance(20)|head_armor(0)|body_armor(54)|leg_armor(15)|difficulty(11) ,imodbits_scale, [], culture_sassanid+culture_caucasian ],
["eastern_scale_5", "Scale Coat", [("eastern_scale_5",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 4300 , weight(19)|abundance(20)|head_armor(0)|body_armor(54)|leg_armor(15)|difficulty(11) ,imodbits_scale, [], culture_sassanid+culture_caucasian ],
["eastern_scale_6", "Scale Coat", [("eastern_scale_6",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 4300 , weight(19)|abundance(20)|head_armor(0)|body_armor(54)|leg_armor(15)|difficulty(11) ,imodbits_scale, [], culture_sassanid+culture_caucasian ],

["lamellar_armor", "Heavy Lamellar Armor", [("kranj_lamellar_1",0)], itp_type_body_armor  |itp_covers_legs ,0,
 4300 , weight(19)|abundance(20)|head_armor(0)|body_armor(54)|leg_armor(15)|difficulty(11) ,imodbits_scale ],

["steppe_plated_armor_1", "Mail with Plates", [("steppe_plated_armor_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0, #used for mordvins, huns
 5000 , weight(21)|abundance(10)|head_armor(0)|body_armor(58)|leg_armor(16)|difficulty(14) ,imodbits_scale, [], culture_hunnic ],
["steppe_plated_armor_2", "Mail with Plates", [("steppe_plated_armor_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0, #used for mordvins, huns
 5000 , weight(21)|abundance(10)|head_armor(0)|body_armor(58)|leg_armor(16)|difficulty(14) ,imodbits_scale, [], culture_hunnic ],
["steppe_plated_armor_3", "Mail with Plates", [("steppe_plated_armor_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0, #used for mordvins, huns
 5000 , weight(21)|abundance(10)|head_armor(0)|body_armor(58)|leg_armor(16)|difficulty(14) ,imodbits_scale, [], culture_hunnic ],


#full ~60 body, 18 legs

["457_scale_hauberk_1", "Squamata", [("457_scale_hauberk_1",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 5900 , weight(19)|abundance(18)|head_armor(0)|body_armor(56)|leg_armor(16)|difficulty(13) ,imodbits_scale, [], culture_roman ],
["457_scale_hauberk_2", "Squamata", [("457_scale_hauberk_2",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 5900 , weight(19)|abundance(18)|head_armor(0)|body_armor(56)|leg_armor(16)|difficulty(13) ,imodbits_scale, [], culture_roman ],
["457_scale_hauberk_3", "Squamata", [("457_scale_hauberk_3",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 5900 , weight(19)|abundance(18)|head_armor(0)|body_armor(56)|leg_armor(16)|difficulty(13) ,imodbits_scale, [], culture_roman ],
#richer scale armor - slightly better defense
["457_scale_hauberk_4", "Squamata", [("457_scale_hauberk_4",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 6100 , weight(19)|abundance(15)|head_armor(0)|body_armor(58)|leg_armor(16)|difficulty(13) ,imodbits_scale, [], culture_roman ],
["457_scale_hauberk_5", "Squamata", [("457_scale_hauberk_5",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 6100 , weight(19)|abundance(15)|head_armor(0)|body_armor(58)|leg_armor(16)|difficulty(13) ,imodbits_scale, [], culture_roman ],
["457_scale_hauberk_6", "Squamata", [("457_scale_hauberk_6",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 6100 , weight(19)|abundance(15)|head_armor(0)|body_armor(58)|leg_armor(16)|difficulty(13) ,imodbits_scale, [], culture_roman ],
["457_scale_hauberk_7", "Squamata", [("457_scale_hauberk_7",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 6100 , weight(19)|abundance(15)|head_armor(0)|body_armor(58)|leg_armor(16)|difficulty(13) ,imodbits_scale, [], culture_roman ],
["457_scale_hauberk_8", "Squamata", [("457_scale_hauberk_8",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 6100 , weight(19)|abundance(15)|head_armor(0)|body_armor(58)|leg_armor(16)|difficulty(13) ,imodbits_scale, [], culture_roman ],

#cataphract ~64 body, 20 legs
["cataphract_armor_1", "Cataphract Armor", [("sassanid_cataphract_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 8600 , weight(35)|abundance(5)|head_armor(0)|body_armor(64)|leg_armor(20)|difficulty(16) ,imodbits_scale, [], culture_sassanid+culture_caucasian ],
["cataphract_armor_2", "Cataphract Armor", [("roman_cataphract_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 8600 , weight(35)|abundance(5)|head_armor(0)|body_armor(64)|leg_armor(20)|difficulty(16) ,imodbits_scale, [], culture_roman ],
["cataphract_armor_3", "Cataphract Armor", [("roman_cataphract_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 8600 , weight(35)|abundance(5)|head_armor(0)|body_armor(64)|leg_armor(20)|difficulty(16) ,imodbits_scale, [], culture_roman ],
["cataphract_armor_4", "Cataphract Armor", [("sassanid_cataphract_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 8600 , weight(35)|abundance(5)|head_armor(0)|body_armor(64)|leg_armor(20)|difficulty(16) ,imodbits_scale, [], culture_sassanid+culture_caucasian ],
["cataphract_armor_5", "Cataphract Armor", [("sassanid_cataphract_3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 8600 , weight(35)|abundance(5)|head_armor(0)|body_armor(64)|leg_armor(20)|difficulty(16) ,imodbits_scale, [], culture_sassanid+culture_caucasian ],
["cataphract_armor_6", "Cataphract Armor", [("roman_cataphract_3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 8600 , weight(35)|abundance(5)|head_armor(0)|body_armor(64)|leg_armor(20)|difficulty(16) ,imodbits_scale, [], culture_sassanid+culture_caucasian ],
["cataphract_armor_7", "Cataphract Armor", [("roman_cataphract_4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 8600 , weight(35)|abundance(5)|head_armor(0)|body_armor(64)|leg_armor(20)|difficulty(16) ,imodbits_scale, [], culture_sassanid+culture_caucasian ],

["alan_cataphract_1", "Cataphract Armor", [("alan_cataphract_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 8600 , weight(35)|abundance(5)|head_armor(0)|body_armor(64)|leg_armor(20)|difficulty(16) ,imodbits_scale, [], culture_hunnic+culture_alan ],

["cataphract_lamellar_1", "Cataphract Armor", [("cataphract_lamellar_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 8600 , weight(35)|abundance(5)|head_armor(0)|body_armor(64)|leg_armor(20)|difficulty(16) ,imodbits_scale, [], culture_roman+culture_sassanid+culture_caucasian+culture_hunnic+culture_alan ],

#others

["kizil_composite_armor", "Compsite Armor", [("kizil_composite_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, #very rare, can only be sold by the alans and the huns
 8600 , weight(36)|abundance(1)|head_armor(0)|body_armor(64)|leg_armor(28)|difficulty(17) ,imodbits_plate, [], culture_hunnic+culture_alan ],

["cuirass_roman_1", "Roman Muscle Cuirass", [("cuirass_roman_1",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
 9000 , weight(22)|abundance(1)|head_armor(0)|body_armor(59)|leg_armor(12)|difficulty(10) ,imodbits_plate, [], culture_roman ],
["cuirass_roman_2", "Roman Muscle Cuirass", [("cuirass_roman_2",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
 9000 , weight(22)|abundance(1)|head_armor(0)|body_armor(59)|leg_armor(12)|difficulty(10) ,imodbits_plate, [], culture_roman ],

["roman_emperor_tunic", "Roman Emperor's Tunic", [("roman_emperor_tunic",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 600 , weight(4)|abundance(20)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["roman_emperor_boots", "Roman Emperor's Shoes", [("roman_emperor_boots",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 600 , weight(1)|abundance(20)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],

["emperor_armor_c", "Emperor's Armor", [("sassanid_emperor_armor",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,8000 , weight(22)|abundance(20)|head_armor(4)|body_armor(56)|leg_armor(16)|difficulty(10) ,imodbits_scale, [], culture_sassanid+culture_caucasian ],

["cuirass_roman_emperor", "Roman Emperor's Cuirass", [("cuirass_roman_emperor",0)], itp_type_body_armor  |itp_covers_legs ,0,9000 , weight(20)|abundance(20)|head_armor(0)|body_armor(59)|leg_armor(16)|difficulty(10) ,imodbits_plate ],
["roman_squamata_emperor", "Roman Emperor's Scale Curiass", [("roman_squamata_emperor",0)], itp_type_body_armor|itp_covers_legs ,0,9000 , weight(18)|abundance(20)|head_armor(4)|body_armor(56)|leg_armor(16)|difficulty(8) ,imodbits_scale ],
["roman_emperor_greaves", "Roman Emperor's Greaves", [("roman_emperor_greaves",0)], itp_type_foot_armor | itp_attach_armature ,0, 6000 , weight(2.5)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(36)|difficulty(0) ,imodbits_plate ],

#unique armor for certain lords
["childeric_armor", "Rigid Scale Curiass", [("childeric_armor",0)], itp_type_body_armor|itp_covers_legs ,0,9000 , weight(18)|abundance(20)|head_armor(4)|body_armor(56)|leg_armor(16)|difficulty(8) ,imodbits_scale ], #for childeric I
["arthur_scale", "Briton Scale Curiass", [("arthur_scale",0)], itp_unique|itp_type_body_armor|itp_covers_legs ,0,9000 , weight(17)|abundance(10)|head_armor(0)|body_armor(56)|leg_armor(16)|difficulty(8) ,imodbits_scale ],
["aspar_armor", "Scale Curiass", [("aspar_armor",0)], itp_unique|itp_type_body_armor|itp_covers_legs ,0,9000 , weight(17)|abundance(10)|head_armor(0)|body_armor(56)|leg_armor(16)|difficulty(8) ,imodbits_scale ],
["strabo_armor", "Scale Curiass", [("strabo_armor",0)], itp_unique|itp_type_body_armor|itp_covers_legs ,0,9000 , weight(17)|abundance(10)|head_armor(0)|body_armor(56)|leg_armor(16)|difficulty(8) ,imodbits_scale ],
["libyan_king_mail", "Mail", [("libyan_king_mail",0)], itp_unique|itp_type_body_armor|itp_covers_legs ,0, 7000 , weight(17)|abundance(1)|head_armor(0)|body_armor(56)|leg_armor(16)|difficulty(8) ,imodbits_scale ],
["danish_king_mail", "Mail", [("danish_king_mail",0)], itp_unique|itp_type_body_armor|itp_covers_legs ,0, 7000 , weight(17)|abundance(1)|head_armor(0)|body_armor(56)|leg_armor(16)|difficulty(8) ,imodbits_scale ],
["garamantian_king_scale", "Scale Curiass", [("garamantian_king_scale",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 6000 , weight(15)|abundance(1)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(8) ,imodbits_scale, [(ti_on_init_item,[(call_script, "script_init_short_tunic_arms"),]),], [fac_culture_11] ],
["mamluke_mail", "Squamata", [("gaiseric_scale",0)], itp_unique|itp_type_body_armor|itp_covers_legs ,0, 7000 , weight(19)|abundance(15)|head_armor(0)|body_armor(58)|leg_armor(16)|difficulty(13) ,imodbits_scale ],


["sarranid_head_cloth", "Lady Head Cloth", [("tulbent",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_head_cloth_b", "Lady Head Cloth", [("tulbent_b",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_felt_head_cloth", "Head Cloth", [("common_tulbent",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_felt_head_cloth_b", "Head Cloth", [("common_tulbent_b",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["headcloth", "Headcloth", [("headcloth_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_hood", "Woolen Hood", [("woolen_hood",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["arming_cap", "Arming Cap", [("roman_arming_cap_3_inv",0)], itp_type_head_armor  |itp_civilian ,0, 5 , weight(1)|abundance(100)|head_armor(7)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["fur_hat", "Fur Hat", [("slavic_cap",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 30 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#used for hunnic horsemen
["nomad_cap", "Nomad Cap", [("nomad_cap_a_new",0)], itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["nomad_cap_b", "Nomad Cap", [("nomad_cap_b_new",0)], itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["steppe_cap", "Steppe Cap", [("steppe_cap_a_new",0)], itp_type_head_armor  |itp_civilian ,0, 14 , weight(1)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["padded_coif", "Padded Coif", [("padded_hat_a",0)], itp_type_head_armor   ,0, 200 , weight(1)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_steppe_cap_a", "Steppe Cap", [("leather_steppe_cap_a_new",0)], itp_type_head_armor   ,0,
24 , weight(1)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["leather_steppe_cap_b", "Steppe Cap ", [("tattered_steppe_cap_b_new",0)], itp_type_head_armor   ,0,
36 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["leather_steppe_cap_c", "Steppe Cap", [("steppe_cap_a_new",0)], itp_type_head_armor   ,0, 51 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["turban", "Turban", [("tuareg_new_open",0)], itp_merchandise| itp_type_head_armor   ,0, 60 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["desert_turban", "Desert Turban", [("tuareg_new",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard ,0, 90 , weight(1.50)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],

#Helmets - Cloth

["turret_hat_ruby", "Veil", [("common_veil_a",0)], itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 90 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["turret_hat_blue", "Veil", [("common_veil_b",0)], itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 90 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["turret_hat_green", "Veil", [("common_veil_c",0)],itp_type_head_armor  |itp_civilian |itp_attach_armature,0,90, weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["court_hat", "Veil", [("common_veil_d",0)],itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 90 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["wimple_a", "Veil", [("common_veil_e",0)],itp_type_head_armor  |itp_civilian |itp_attach_armature,0,90, weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["wimple_with_veil", "Veil", [("veil_a",0)],itp_type_head_armor  |itp_civilian |itp_attach_armature,0,90, weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["female_hood", "Veil", [("veil_b",0)],itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 90 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["khergit_lady_hat", "Veil", [("veil_c",0)], itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 90 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["khergit_lady_hat_b", "Veil", [("veil_d",0)], itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 90 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_felt_hat", "Veil", [("veil_e",0)], itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 90 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["felt_hat", "Veil", [("veil_f",0)], itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 90 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["felt_hat_b", "Veil", [("veil_g",0)], itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 90 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

#["roman_noble_shawl_1", "Shawl", [("roman_noble_shawl_1",0),("roman_noble_shawl_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_doesnt_cover_hair,0,100 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_cloth],

["bandana1", "Bandana", [("bandana1",0)], itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_fit_to_head,0,60, weight(0.5)|abundance(10)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["bandana2", "Bandana", [("bandana2",0)],itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_fit_to_head,0,60, weight(0.5)|abundance(10)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],

["african_band_1", "Bandana with Feathers", [("african_band_1",0),("african_band_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian,0,60, weight(0.5)|abundance(20)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth, [], [fac_culture_11,fac_culture_15] ],
["african_band_2", "Bandana with Feathers", [("african_band_2",0),("african_band_2_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian,0,60, weight(0.5)|abundance(20)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth, [], [fac_culture_11,fac_culture_15] ],

["head_wrappings","Head Wrapping",[("head_wrapping",0)],itp_type_head_armor|itp_fit_to_head,0,16, weight(0.25)|head_armor(10),imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick],
["straw_hat", "Straw Hat", [("straw_hat_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],

["woolen_cap", "Green Phrygian Cap", [("phrygian_green",0)],  itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_cap_b", "Brown Phrygian Cap", [("phrygian_creme",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_cap_c", "Yellow Phrygian Cap", [("phrygian_yellow",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
["woolen_cap_1", "Blue Phrygian Cap", [("phrygian_blue",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
["woolen_cap_2", "Red Phrygian Cap", [("phrygian_red",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
["woolen_cap_3", "Black Phrygian Cap", [("phrygian_black",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
["woolen_cap_4", "White Phrygian Cap", [("phrygian_white",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
["woolen_cap_5", "Orange Phrygian Cap", [("phrygian_orange",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
["woolen_cap_6", "Brown Phrygian Cap", [("phrygian_brown",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
["woolen_cap_7", "Decorated Phrygian Cap", [("woolen_cap_decorated",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
["woolen_cap_8", "Gray Phrygian Cap", [("phrygian_gray",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],

["woolen_cap_simple_1", "White Woolen Cap", [("woolen_cap_simple_1",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
["woolen_cap_simple_2", "Red Woolen Cap", [("woolen_cap_simple_2",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
["woolen_cap_simple_3", "Green Woolen Cap", [("woolen_cap_simple_3",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
["woolen_cap_simple_4", "Brown Woolen Cap", [("woolen_cap_simple_4",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
["woolen_cap_simple_5", "Orange Woolen Cap", [("woolen_cap_simple_5",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],

["kovas_hat_1", "Simple Cap", [("kovas_hat_1",0)],  itp_type_head_armor|itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["kovas_hat_2", "Simple Cap", [("kovas_hat_2",0)],  itp_type_head_armor|itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["kovas_hat_3", "Simple Cap", [("kovas_hat_3",0)],  itp_type_head_armor|itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["kovas_hat_4", "Simple Cap", [("kovas_hat_4",0)],  itp_type_head_armor|itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

#white hun caps
["chionite_hat_1", "Woolen Cap", [("chionite_hat_1",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["chionite_hat_2", "Woolen Cap", [("chionite_hat_2",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["chionite_hat_3", "Woolen Cap", [("chionite_hat_3",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["chionite_hat_4", "Woolen Cap", [("chionite_hat_4",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["chionite_hat_5", "Woolen Cap", [("chionite_hat_5",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],

["hunnic_phrygian_1", "Phrygian Cap", [("hunnic_phrygian_1",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 120 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["hunnic_phrygian_2", "Phrygian Cap", [("hunnic_phrygian_2",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 120 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["hunnic_phrygian_3", "Phrygian Cap", [("hunnic_phrygian_3",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 120 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["hunnic_phrygian_4", "Phrygian Cap", [("hunnic_phrygian_4",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 120 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["hunnic_phrygian_5", "Phrygian Cap", [("hunnic_phrygian_5",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 120 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["hunnic_phrygian_6", "Phrygian Cap", [("hunnic_phrygian_6",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 120 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["pannonian_cap_1", "Pillbox Cap", [("pannonian_cap_cloth_1",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 90 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["pannonian_cap_2", "Pillbox Cap", [("pannonian_cap_cloth_2",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 90 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["pannonian_cap_3", "Pillbox Cap", [("pannonian_cap_cloth_3",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 90 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["pannonian_cap_4", "Pillbox Cap", [("pannonian_cap_leather_1",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 90 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["pannonian_cap_5", "Pillbox Cap", [("pannonian_cap_leather_2",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 90 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["pannonian_cap_6", "Pillbox Cap", [("pannonian_cap_cloth_4",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 90 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_roman ], #now for a specific, special character

["pannonian_cap_fur_1", "Fur Pillbox Cap", [("pannonian_cap_fur_1",0),("pannonian_cap_fur_1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor |itp_attach_armature ,0, 90 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth, [], culture_roman ],
["pannonian_cap_fur_2", "Fur Pillbox Cap", [("pannonian_cap_fur_2",0),("pannonian_cap_fur_2_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor |itp_attach_armature ,0, 90 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth, [], culture_roman ],

["germanic_cap_1", "Woolen Cap", [("germanic_cap_1",0)],  itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["germanic_cap_2", "Woolen Cap", [("germanic_cap_2",0)],  itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["germanic_cap_3", "Woolen Cap", [("germanic_cap_3",0)],  itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["germanic_cap_4", "Woolen Cap", [("germanic_cap_4",0)],  itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 80 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["bulb_cap", "Bulb Cap", [("sassanid_bulb_1",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 110 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["bulb_cap_1", "Bulb Cap", [("sassanid_bulb_1",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 110 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["bulb_cap_2", "Bulb Cap", [("sassanid_bulb_2",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 110 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["bulb_cap_3", "Bulb Cap", [("sassanid_bulb_3",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 110 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["bulb_cap_4", "Bulb Cap", [("sassanid_bulb_4",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 110 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["bulb_cap_5", "Bulb Cap", [("sassanid_bulb_5",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 110 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],
["bulb_cap_6", "Bulb Cap", [("sassanid_bulb_6",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 110 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_sassanid+culture_caucasian ],

#Hoods
["new_hood_a", "Blue Hood", [("sclavenia_hood_rigged_3",0),("sclavenia_hood_inv_3",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_civilian,0,75, weight(1)|abundance(50)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth, [], culture_germanic ],
["new_hood_b", "Red Hood", [("sclavenia_hood_rigged_4",0),("sclavenia_hood_inv_4",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_civilian,0,75, weight(1)|abundance(50)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth, [], culture_germanic ],
["new_hood_c", "Green Hood", [("sclavenia_hood_rigged_2",0),("sclavenia_hood_inv_2",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_civilian,0,75, weight(1)|abundance(50)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth, [], culture_germanic ],
["new_hood_d", "Black Hood", [("sclavenia_hood_rigged_5",0),("sclavenia_hood_inv_5",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_civilian,0,75, weight(1)|abundance(50)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth, [], culture_germanic ],
["new_hood_e", "White Hood", [("sclavenia_hood_rigged_6",0),("sclavenia_hood_inv_6",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_civilian,0,75, weight(1)|abundance(50)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth, [], culture_germanic ],

["p_hood", "Hood", [("pictish_hood",0)], 0| itp_type_head_armor |itp_civilian  ,0, 75 , weight(1.25)|abundance(30)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],
["brown_hood1", "Brown Hood", [("sclavenia_hood_rigged_1",0),("sclavenia_hood_inv_1",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_civilian,0,75, weight(1)|abundance(50)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth, [], culture_germanic ],

["bl_boar_fur", "Boar fur cloak", [("BL_boar",0)], itp_type_head_armor| itp_attach_armature| itp_fit_to_head|itp_civilian,0, 480 , weight(1)|abundance(80)|head_armor(24)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], culture_germanic ],

["turban_white_1", "Turban", [("turban_white_1",0),("turban_white_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_civilian,0,75, weight(1)|abundance(50)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth, [], culture_sassanid ],
["turban_white_2", "Turban", [("turban_white_2",0),("turban_white_2_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_civilian,0,75, weight(1)|abundance(50)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth, [], culture_sassanid ],
["turban_brown_1", "Turban", [("turban_brown_1",0),("turban_brown_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_civilian,0,75, weight(1)|abundance(50)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth, [], culture_sassanid ],
["turban_brown_2", "Turban", [("turban_brown_2",0),("turban_brown_2_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_civilian,0,75, weight(1)|abundance(50)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth, [], culture_sassanid ],
["turban_black_1", "Turban", [("turban_black_1",0),("turban_black_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_civilian,0,75, weight(1)|abundance(50)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth, [], culture_sassanid ],
["turban_black_2", "Turban", [("turban_black_2",0),("turban_black_2_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_civilian,0,75, weight(1)|abundance(50)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth, [], culture_sassanid ],
["turban_red_1", "Turban", [("turban_red_1",0),("turban_red_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_civilian,0,75, weight(1)|abundance(50)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth, [], culture_sassanid ],
["turban_red_2", "Turban", [("turban_red_2",0),("turban_red_2_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_civilian,0,75, weight(1)|abundance(50)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth, [], culture_sassanid ],

#Helmets - Light

["leather_cap", "Leather Cap", [("leather_cap_a_new",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 170, weight(1)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["roman_arming_cap_1", "Arming Cap", [("roman_arming_cap_1",0),("roman_arming_cap_1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_civilian ,0, 180 , weight(0.5)|abundance(30)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_roman ],
["roman_arming_cap_2", "Arming Cap", [("roman_arming_cap_2",0),("roman_arming_cap_2_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_civilian ,0, 180 , weight(0.5)|abundance(30)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_roman ],

["hunnic_phrygian_leather", "Leather Phrygian Cap", [("hunnic_phrygian_leather",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 200 , weight(1)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["eastern_leather_cap", "Leather Cap", [("sar_helmet3",0)], itp_merchandise| itp_type_head_armor|itp_civilian   ,0, 270 , weight(2)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth, [], culture_sassanid ],

["leather_warrior_cap", "Leather Warrior Cap", [("generic_leather_helmet_cloth_inv",0)], itp_type_head_armor  |itp_civilian ,0, 300 , weight(1)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["skullcap", "Leather Warrior Cap", [("generic_leather_helmet_cloth_inv",0)],itp_type_head_armor   ,0, 300 , weight(1.0)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["generic_leather_helmet_cloth", "Leather Cap", [("generic_leather_helmet_cloth",0),("generic_leather_helmet_cloth_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor |itp_attach_armature ,0, 320 , weight(1.0)|abundance(90)|head_armor(27)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["hide_helmet", "Hide Helmet", [("hide_helmet",0),("hide_helmet_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature ,0, 200 , weight(1.0)|abundance(40)|head_armor(29)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_african ], #for the nubians
["nubian_leather_helmet", "Hide Helmet", [("nubian_leather_helmet",0),("nubian_leather_helmet_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature ,0, 340 , weight(1.0)|abundance(40)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], culture_african ], #for the nubians

["boar_helmet", "Boar Cap", [("BL_boarhelmet",0)], itp_type_head_armor|itp_civilian ,0, 400, weight(2)|abundance(100)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["goat_cap", "Goat Cap", [("goat_cap",0)], itp_type_head_armor|itp_civilian ,0, 400, weight(2)|abundance(100)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["wolf_helmet", "Wolf Cap", [("veles_wolfskin_headdress",0)], itp_type_head_armor|itp_civilian ,0, 400, weight(2)|abundance(100)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["drengsted_helmet_leather", "Skeletal Helmet", [("drengsted_helmet_leather",0),("drengsted_helmet_leather_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,450 , weight(1.0)|abundance(60)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], [fac_culture_4] ],
["drengsted_helmet_mail", "Skeletal Helmet with Mail", [("drengsted_helmet_mail",0),("drengsted_helmet_mail_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,680 , weight(1.25)|abundance(50)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], [fac_culture_4] ],

#Helmets - Bowl/Bandhelm
#Roman
["iatrus_helmet_light", "Ridge Helmet", [("iatrus_helmet_light",0),("iatrus_helmet_light_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,520 , weight(1.25)|abundance(60)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_germanic+culture_gothic+culture_celtic ],

["narona_bandhelm_bowl", "Bandhelm", [("narona_bandhelm_bowl",0),("narona_bandhelm_bowl_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,520 , weight(1.25)|abundance(60)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],

#Generic
["old_spangenhelm_1", "Spangenhelm", [("old_spangenhelm",0)], itp_type_head_armor,0, 520 , weight(1.5)|abundance(60)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate ],

["batumi_helmet_simple", "Monopartite Helmet", [("batumi_simple",0),("batumi_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,520 , weight(1.0)|abundance(60)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_caucasian ],

["tarasovsky_1784_helmet_wb_3", "Eastern Spangenhelm", [("tarasovsky_1784_helmet_wb_3",0),("tarasovsky_1784_helmet_wb_3_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,520 , weight(1.0)|abundance(60)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_sassanid+culture_caucasian+culture_hunnic+culture_alan ],

#Helmets - Spagenhelms/Light Ridge Helmets

#Generic
["old_spangenhelm_2", "Spangenhelm", [("old_spangenhelmcheek",0)], itp_type_head_armor,0, 740 , weight(1.5)|abundance(50)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate ],
#Roman
["burgh_helmet_light", "Ridge Helmet", [("burgh_helmet_light",0),("burgh_helmet_light_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,700 , weight(1.5)|abundance(50)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_germanic+culture_gothic+culture_celtic ],

["narona_bandhelm_leather", "Bandhelm", [("narona_bandhelm_leather",0),("narona_bandhelm_leather_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,740 , weight(1.25)|abundance(50)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["narona_bandhelm_cloth", "Bandhelm", [("narona_bandhelm_cloth",0),("narona_bandhelm_cloth_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,740 , weight(1.25)|abundance(50)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],

["triveres_cloth", "Bandhelm", [("triveres_cloth",0),("triveres_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,740 , weight(1.25)|abundance(50)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_germanic+culture_gothic ],

["kerch_lamellenhelm_light", "Lamellenhelm", [("kerch_lamellenhelm_light",0),("kerch_lamellenhelm_light_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,740 , weight(1.5)|abundance(50)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_hunnic+culture_alan ],

["batumi_helmet_cloth", "Monopartite Helmet with Cloth", [("batumi_cloth",0),("batumi_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,865 , weight(1.25)|abundance(40)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_caucasian ],
["batumi_helmet_leather", "Monopartite Helmet with Leather", [("batumi_leather",0),("batumi_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,920 , weight(1.25)|abundance(40)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_caucasian ],

["suvorovsky_helmet_cloth", "Decorated Monopartite Helmet with Cloth", [("suvorovsky_helmet_cloth",0),("suvorovsky_helmet_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,865 , weight(1.25)|abundance(40)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_hunnic+culture_alan ],

["triveres_leather", "Bandhelm with Leather", [("triveres_leather",0),("triveres_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,865 , weight(1.25)|abundance(50)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_germanic+culture_gothic ],


#Sassanid Crossband Helmets
["sassanid_helmet_cloth_1", "Crossband Helmet", [("sassanid_helmet_cloth_1",0),("sassanid_helmet_cloth_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,865 , weight(1.25)|abundance(40)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(2) ,imodbits_plate, [], culture_sassanid  ],
["sassanid_helmet_cloth_2", "Crossband Helmet", [("sassanid_helmet_cloth_2",0),("sassanid_helmet_cloth_2_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,865 , weight(1.25)|abundance(40)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(2) ,imodbits_plate, [], culture_sassanid  ],
["sassanid_helm_5", "Sassanid Helmet", [("sassanid_helmet_cloth_5",0),("sassanid_helmet_cloth_5_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,865 , weight(1.25)|abundance(40)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(2) ,imodbits_plate, [], culture_sassanid ],

["tarasovsky_1784_helmet_wb_1", "Eastern Spangenhelm", [("tarasovsky_1784_helmet_wb_1",0),("tarasovsky_1784_helmet_wb_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,865 , weight(2.5)|abundance(30)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(3) ,imodbits_plate, [], culture_sassanid+culture_caucasian+culture_hunnic+culture_alan ],
["tarasovsky_1784_helmet_arab", "Eastern Spangenhelm", [("tarasovsky_1784_helmet_arab",0),("tarasovsky_1784_helmet_arab_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,865 , weight(2.5)|abundance(30)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(3) ,imodbits_plate, [], culture_sassanid ],

["warlord_coif_1", "Mail Hood", [("warlord_coif_1",0),("warlord_coif_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,900 , weight(2)|abundance(10)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(3) ,imodbits_mail, [], [fac_culture_empire] ],
["warlord_coif_2", "Mail Hood", [("warlord_coif_2",0),("warlord_coif_2_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,900 , weight(2)|abundance(10)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(3) ,imodbits_mail, [], [fac_culture_empire] ],

["khudashevsky_helmet_1", "Stacked Helmet", [("khudashevsky_helmet_1",0),("khudashevsky_helmet_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,900 , weight(2.5)|abundance(40)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(3) ,imodbits_plate, [], culture_hunnic+culture_alan ],

["tsaritsyno_2_1", "Gilded Spangenhelm", [("tsaritsyno_2_1",0),("tsaritsyno_2_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1000 , weight(1.25)|abundance(40)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate, [], culture_roman ],

["tsaritsyno_1_simple", "Eastern Bandhelm", [("tsaritsyno_1_simple",0),("tsaritsyno_1_light_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,900 , weight(1.75)|abundance(40)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_sassanid+culture_caucasian+culture_hunnic ],

["rozhdestvensky_helmet_leather", "Lamellenhelm", [("rozhdestvensky_helmet_leather",0),("rozhdestvensky_helmet_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,865 , weight(1.5)|abundance(30)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(3) ,imodbits_plate, [], culture_caucasian+culture_hunnic+culture_alan ],

["kishpek_helmet_leather", "Rich Lamellenhelm", [("kishpek_helmet_leather",0),("kishpek_helmet_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,942 , weight(1.5)|abundance(30)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(3) ,imodbits_plate, [], culture_caucasian+culture_hunnic+culture_alan ],

#Roman
["iatrus_helmet_mail", "Ridge Helmet with Mail", [("iatrus_helmet_mail",0),("iatrus_helmet_mail_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,900 , weight(1.5)|abundance(40)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_germanic+culture_gothic+culture_celtic ],

#Helmets Spagenhelms/Ridge Helmets High Tier
#Generic
["old_spangenhelm_3", "Spangenhelm", [("old_spangenhelmaven",0)], itp_type_head_armor,0, 1045 , weight(2)|abundance(30)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate ],

["burgh_helmet_mail", "Ridge Helmet with Mail", [("burgh_helmet_mail",0), ("burgh_helmet_mail_inv",ixmesh_inventory)], itp_type_head_armor | itp_fit_to_head | itp_attach_armature ,0, 1045 , weight(1.5)|abundance(30)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_germanic ],

["batumi_helmet_aventail", "Monopartite Helmet with Mail", [("batumi_mail",0),("batumi_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1055 , weight(1.50)|abundance(30)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_caucasian ],

["suvorovsky_helmet_mail", "Decorated Monopartite Helmet with Mail", [("suvorovsky_helmet_mail",0),("suvorovsky_helmet_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1055 , weight(1.50)|abundance(30)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_hunnic+culture_alan ],

["tarasovsky_1784_helmet_wb_2", "Eastern Spangenhelm with Mail", [("tarasovsky_1784_helmet_wb_2",0),("tarasovsky_1784_helmet_wb_2_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1055 , weight(1.50)|abundance(45)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_sassanid+culture_caucasian+culture_hunnic+culture_alan ],

["tarasovsky_1784_helmet_wb_4", "Eastern Spangenhelm", [("tarasovsky_1784_helmet_wb_4",0),("tarasovsky_1784_helmet_wb_4_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1065 , weight(1.50)|abundance(45)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_sassanid+culture_caucasian+culture_hunnic+culture_alan ], #sassanids, huns, caucasians

["kerch_lamellenhelm", "Lamellenhelm", [("kerch_lamellenhelm",0),("kerch_lamellenhelm_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1050 , weight(2)|abundance(45)|head_armor(44)|body_armor(0)|leg_armor(0) ,imodbits_plate, [], culture_sassanid+culture_caucasian ],

#Removed helmets, most are duplicates and are unneeded
["ridge_helm_c", "Ridge Helmet", [("light_ridge",0)], itp_merchandise|itp_type_head_armor,0,1045 , weight(1.5)|abundance(120)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(3) ,imodbits_plate, [], culture_roman ],

["haditha_1", "Band Helmet", [("haditha_1",0),("haditha_1_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1045 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["haditha_crested_1", "Band Helmet with Crest", [("haditha_crested_1",0),("haditha_crested_1_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1045 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],

#new intercisa styled helmets 4/11/22
["intercisa_helmet_1", "Ridge Helmet", [("intercisa_helmet_1",0),("intercisa_helmet_1_inv",ixmesh_inventory),("intercisa_helmet_old_1",imodbits_bad)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1045 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman+culture_germanic+culture_gothic ],
["intercisa_helmet_2", "Ridge Helmet", [("intercisa_helmet_2",0),("intercisa_helmet_2_inv",ixmesh_inventory),("intercisa_helmet_old_2",imodbits_bad)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1045 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman+culture_germanic+culture_gothic ],
["augst_helmet_1", "Ridge Helmet", [("augst_helmet_1",0),("augst_helmet_1_inv",ixmesh_inventory),("augst_helmet_old",imodbits_bad)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1045 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman+culture_germanic+culture_gothic ],

["intercisa_helmet_silvered_1", "Silvered Ridge Helmet", [("intercisa_helmet_silvered_1",0),("intercisa_helmet_silvered_1_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1150 , weight(1.5)|abundance(35)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["intercisa_helmet_silvered_2", "Silvered Ridge Helmet", [("intercisa_helmet_silvered_2",0),("intercisa_helmet_silvered_2_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1150 , weight(1.5)|abundance(35)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["augst_helmet_2", "Silvered Ridge Helmet", [("augst_helmet_2",0),("augst_helmet_2_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1150 , weight(1.5)|abundance(35)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],

["intercisa_helmet_gilded_1", "Gilded Ridge Helmet", [("intercisa_helmet_gilded_1",0),("intercisa_helmet_gilded_1_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1150 , weight(1.5)|abundance(30)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["intercisa_helmet_gilded_2", "Gilded Ridge Helmet", [("intercisa_helmet_gilded_2",0),("intercisa_helmet_gilded_2_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1150 , weight(1.5)|abundance(30)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["augst_helmet_3", "Gilded Ridge Helmet", [("augst_helmet_3",0),("augst_helmet_3_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1150 , weight(1.5)|abundance(30)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],

#Plumed Helmets
["intercisa_helmet_plume_1", "Ridge Helmet with Crest", [("intercisa_helmet_plume_1",0),("intercisa_helmet_plume_1_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1045 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["intercisa_helmet_plume_2", "Ridge Helmet with Crest", [("intercisa_helmet_plume_2",0),("intercisa_helmet_plume_2_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1045 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["augst_helmet_plume_1", "Ridge Helmet with Crest", [("augst_helmet_plume_1",0),("augst_helmet_plume_1_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1045 , weight(1.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],

["intercisa_helmet_silvered_plume_1", "Silvered Ridge Helmet with Crest", [("intercisa_helmet_silvered_plume_1",0),("intercisa_helmet_silvered_plume_1_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1150 , weight(1.5)|abundance(35)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["intercisa_helmet_silvered_plume_2", "Silvered Ridge Helmet with Crest", [("intercisa_helmet_silvered_plume_2",0),("intercisa_helmet_silvered_plume_2_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1150 , weight(1.5)|abundance(35)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["augst_helmet_plume_2", "Silvered Ridge Helmet with Crest", [("augst_helmet_plume_2",0),("augst_helmet_plume_2_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1150 , weight(1.5)|abundance(35)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],

["intercisa_helmet_gilded_plume_1", "Gilded Ridge Helmet with Crest", [("intercisa_helmet_gilded_plume_1",0),("intercisa_helmet_gilded_plume_1_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1150 , weight(1.5)|abundance(30)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["intercisa_helmet_gilded_plume_2", "Gilded Ridge Helmet with Crest", [("intercisa_helmet_gilded_plume_2",0),("intercisa_helmet_gilded_plume_2_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1150 , weight(1.5)|abundance(30)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["augst_helmet_plume_3", "Gilded Ridge Helmet with Crest", [("augst_helmet_plume_3",0),("augst_helmet_plume_3_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1150 , weight(1.5)|abundance(30)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],

#Metal Crested (uncommon - only augst variant)
["augst_helmet_crested_1", "Silvered Ridge Helmet with Crest", [("augst_helmet_crested_1",0),("augst_helmet_crested_1_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1150 , weight(1.5)|abundance(30)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["augst_helmet_crested_2", "Gilded Ridge Helmet with Crest", [("augst_helmet_crested_2",0),("augst_helmet_crested_2_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1150 , weight(1.5)|abundance(30)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],

#sassanid helmets with mail
["sassanid_helmet_mail_1", "Crossband Helmet with Mail", [("sassanid_helmet_mail_1",0),("sassanid_helmet_mail_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1145 , weight(2.5)|abundance(22)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_sassanid ],
["sassanid_helmet_mail_2", "Crossband Helmet with Mail", [("sassanid_helmet_mail_2",0),("sassanid_helmet_mail_2_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1145 , weight(2.5)|abundance(22)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_sassanid ],
["sassanid_helmet_mail_3", "Spangenhelm with Mail", [("sassanid_helmet_mail_3",0),("sassanid_helmet_mail_3_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1145 , weight(2.5)|abundance(22)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_sassanid ],
["sassanid_helmet_elite_5", "Sassanid Helmet with Aventail", [("sassanid_helmet_aventail_5",0),("sassanid_helmet_aventail_5_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1145 , weight(2.5)|abundance(22)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_sassanid ],

["sassanid_lamellenhelm_1", "Lamellenhelm with Mail", [("sassanid_lamellenhelm_1",0),("sassanid_lamellenhelm_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1145 , weight(2.5)|abundance(22)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_sassanid ],
["sassanid_lamellenhelm_2", "Lamellenhelm with Mail", [("sassanid_lamellenhelm_2",0),("sassanid_lamellenhelm_2_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1145 , weight(2.5)|abundance(22)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_sassanid ],
["sassanid_lamellenhelm_3", "Lamellenhelm with Mail", [("sassanid_lamellenhelm_3",0),("sassanid_lamellenhelm_3_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1145 , weight(2.5)|abundance(22)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_sassanid ],

["sarranid_horseman_helmet", "Sassanid Helmet with Aventail", [("wb_dura_rigged",0),("wb_dura_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1245 , weight(2.5)|abundance(30)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_sassanid+culture_caucasian ],

["khudashevsky_helmet_2", "Stacked Helmet with Mail", [("khudashevsky_helmet_2",0),("khudashevsky_helmet_2_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1145 , weight(2.0)|abundance(30)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate, [], culture_hunnic+culture_alan ],
["khudashevsky_helmet_3", "Stacked Helmet with Mail", [("khudashevsky_helmet_3",0),("khudashevsky_helmet_3_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1245 , weight(2.5)|abundance(30)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_hunnic+culture_alan ],

["tsaritsyno_1_light", "Eastern Bandhelm with Mail", [("tsaritsyno_1_light",0),("tsaritsyno_1_light_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1045 , weight(1.75)|abundance(32)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_sassanid+culture_caucasian+culture_hunnic ],

["rozhdestvensky_helmet_mail", "Lamellenhelm with Mail", [("rozhdestvensky_helmet_mail",0),("rozhdestvensky_helmet_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1045 , weight(2.25)|abundance(30)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate, [], culture_caucasian+culture_hunnic+culture_alan ],

["kishpek_helmet_mail", "Rich Lamellenhelm with Mail", [("kishpek_helmet_mail",0),("kishpek_helmet_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1145 , weight(2.25)|abundance(30)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate, [], culture_caucasian+culture_hunnic+culture_alan ],

["narona_bandhelm_mail", "Bandhelm with Mail", [("narona_bandhelm_mail",0),("narona_bandhelm_mail_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1045 , weight(1.55)|abundance(30)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["narona_bandhelm", "Bandhelm with Mail", [("narona_bandhelm",0),("narona_bandhelm_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1045 , weight(1.55)|abundance(30)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],

["triveres_mail", "Bandhelm with Mail", [("triveres_mail",0),("triveres_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1045 , weight(1.55)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate ],

["fernpass_helmet_3", "Ridge Helmet with Mail", [("fernpass_helmet_3",0),("fernpass_helmet_3_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1105 , weight(1.55)|abundance(40)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate ],

#Spangenhelms/Ridge Helmets Heavy
#Generic

["fernpass_helmet_1", "Ridge Helmet", [("fernpass_helmet_1",0),("fernpass_helmet_1_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1230, weight(2.0)|abundance(30)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_germanic+culture_gothic+culture_roman ],

["tsaritsyno_2_2", "Gilded Spangenhelm with Mail", [("tsaritsyno_2_2",0),("tsaritsyno_2_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1140 , weight(1.5)|abundance(30)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate, [], culture_roman ],

["kalhkni_helmet_mail", "Lamellenhelm", [("kalhkni_helmet_mail",0),("kalhkni_helmet_mail_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1130, weight(1.5)|abundance(30)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_caucasian+culture_hunnic+culture_alan ],

["coptic_scale_coif_1", "Scale Coif", [("coptic_scale_coif_1",0),("coptic_scale_coif_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1245 , weight(2.0)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_culture_empire,fac_culture_6] ],

["tarasovo_helmet_1", "Eastern Bandhelm", [("tarasovo_helmet_1",0),("tarasovo_helmet_1_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1130, weight(1.5)|abundance(30)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_hunnic+culture_alan ],

["turaevo_helmet", "Rich Bandhelm", [("charerg_turaevo",0),("charerg_turaevo_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1130, weight(1.5)|abundance(30)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_hunnic+culture_alan ],
["turaevo_helmet_aventail", "Rich Bandhelm", [("turaevo_aventail",0),("turaevo_aventail_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1230, weight(2.5)|abundance(20)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_hunnic+culture_alan ],

["tarasovsky_782_mail", "Gilded Spangenhelm with Mail", [("tarasovsky_782_mail",0),("tarasovsky_782_mail_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1230, weight(2.0)|abundance(30)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_hunnic ],

#Roman
["full_helm", "Ridge Helmet", [("burgh_helmet_a",0),("burgh_helmet_a_inv",ixmesh_inventory)],itp_attach_armature|itp_type_head_armor,0,1230 , weight(2.5)|abundance(30)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_roman ],

["iatrus_1", "Ridge Helmet", [("iatrus_helmet_1",0),("iatrus_helmet_1_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1230, weight(1.5)|abundance(30)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],

["iatrus_plume_1", "Ridge Helmet with Crest", [("iatrus_helmet_plume_1",0),("iatrus_helmet_plume_1_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1230, weight(1.5)|abundance(30)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],

["dux_ridge_helm", "Ridge Helmet", [("dux_ridge_helm",0)], itp_merchandise| itp_type_head_armor,0,1230 , weight(3)|abundance(22)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_roman ],

["koblenz_helmet_light_old", "Old Ridge Helmet", [("koblenz_helmet_old",0),("koblenz_helmet_old_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1040 , weight(2.20)|abundance(25)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ],

["koblenz_helmet_1", "Ridge Helmet", [("koblenz_helmet_1",0),("koblenz_helmet_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1230 , weight(2.50)|abundance(22)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_roman ],
["koblenz_crested_1", "Ridge Helmet with Crest", [("koblenz_helmet_plume_1",0),("koblenz_helmet_plume_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1230 , weight(2.50)|abundance(22)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_roman ],

["burgh_helmet_1", "Ridge Helmet", [("burgh_helmet_1",0),("burgh_helmet_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1230 , weight(2.50)|abundance(22)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_roman ],
["burgh_helmet_plume_1", "Ridge Helmet with Crest", [("burgh_helmet_plume_1",0),("burgh_helmet_plume_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1230 , weight(2.50)|abundance(22)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_roman ],
["burgh_helmet_plume_3", "Ridge Helmet with Crest", [("burgh_helmet_plume_3",0),("burgh_helmet_plume_3_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1230 , weight(2.50)|abundance(22)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_roman ], #britons

["christies_helmet_1", "Ridge Helmet", [("christies_helmet_1",0),("christies_helmet_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1230 , weight(2.50)|abundance(22)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_roman ],
["christies_helmet_crest_1", "Ridge Helmet with Crest", [("christies_helmet_crest_1",0),("christies_helmet_crest_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1230 , weight(2.50)|abundance(22)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_roman ],
["christies_helmet_crest_2", "Ridge Helmet with Crest", [("christies_helmet_crest_2",0),("christies_helmet_crest_2_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1230 , weight(2.50)|abundance(22)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_roman ],

["augsburg_2_helmet_mail", "Ornate Ridge Helmet with Mail", [("augsburg_2_helmet_mail",0),("augsburg_2_helmet_mail_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1190, weight(2.0)|abundance(30)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_germanic+culture_gothic ],

#Germanic
["fernpass_helmet_2", "Ridge Helmet with Mail", [("fernpass_helmet_2",0),("fernpass_helmet_2_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1230, weight(2.25)|abundance(22)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman+culture_germanic+culture_gothic ],

#Eastern
["kerch_lamellenhelm_gilded", "Gilded Lamellenhelm", [("kerch_lamellenhelm_gilded",0),("kerch_lamellenhelm_gilded_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1230 , weight(2)|abundance(20)|head_armor(48)|body_armor(0)|leg_armor(0) ,imodbits_plate, [], culture_sassanid+culture_caucasian ],
["tsaritsyno_1", "Eastern Bandhelm", [("tsaritsyno_1",0),("tsaritsyno_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1230 , weight(2.5)|abundance(30)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate, [], culture_sassanid+culture_caucasian+culture_hunnic ],

["kalhkni_helmet_1", "Lamellenhelm", [("kalhkni_helmet_1",0),("kalhkni_helmet_1_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1230, weight(1.5)|abundance(30)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_caucasian+culture_hunnic+culture_alan ],
["kalhkni_helmet_2", "Lamellenhelm", [("kalhkni_helmet_2",0),("kalhkni_helmet_2_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1230, weight(1.5)|abundance(30)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_caucasian+culture_hunnic+culture_alan ],

["sassanid_helmet_mail_4", "Crossband Helmet with Mail", [("sassanid_helmet_mail_4",0),("sassanid_helmet_mail_4_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1230 , weight(2.5)|abundance(22)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_sassanid ],
["sassanid_helmet_mail_5", "Crossband Helmet with Mail", [("sassanid_helmet_mail_5",0),("sassanid_helmet_mail_5_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1230 , weight(2.5)|abundance(22)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_sassanid ],

["sassanid_lamellenhelm_4", "Lamellenhelm with Mail", [("sassanid_lamellenhelm_4",0),("sassanid_lamellenhelm_4_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1230 , weight(2.5)|abundance(22)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_sassanid ],
["sassanid_lamellenhelm_5", "Lamellenhelm with Mail", [("sassanid_lamellenhelm_5",0),("sassanid_lamellenhelm_5_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1230 , weight(2.5)|abundance(22)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_sassanid ],

["tarasovsky_782", "Gilded Spangenhelm", [("tarasovsky_782",0),("tarasovsky_782_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1430 , weight(2.5)|abundance(20)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate, [], culture_hunnic ],

#veiled
["veiled_helmet_4", "Monopartite Helmet with Veil", [("batumi_cataphract",0),("batumi_cataphract_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_covers_beard,0,3600 , weight(4.25)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_caucasian ],

["tsaritsyno_1_veiled", "Veiled Eastern Bandhelm", [("tsaritsyno_1_veiled",0),("tsaritsyno_1_veiled_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,3600 , weight(4.25)|abundance(30)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate, [], culture_sassanid+culture_caucasian+culture_hunnic ],

["sassanid_cataphract_helmet_1", "Veiled Crossband Helmet", [("sassanid_cataphract_helmet_1",0),("sassanid_cataphract_helmet_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_covers_beard,0,3600 , weight(4.25)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_sassanid ],
["sassanid_cataphract_helmet_2", "Veiled Lamellenhelm", [("sassanid_cataphract_helmet_2",0),("sassanid_cataphract_helmet_2_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_covers_beard,0,3600 , weight(4.25)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_sassanid ],
["sassanid_cataphract_helmet_3", "Veiled Crossband Helmet", [("sassanid_cataphract_helmet_3",0),("sassanid_cataphract_helmet_3_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_covers_beard,0,3600 , weight(4.25)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_sassanid ],
["sassanid_cataphract_helmet_4", "Veiled Crossband Helmet", [("sassanid_cataphract_helmet_4",0),("sassanid_cataphract_helmet_4_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor|itp_covers_beard,0,3600 , weight(4.25)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_sassanid ],

#Heavy Helmets

#ridge helmets
["iatrus_2", "Gilded Ridge Helmet", [("iatrus_helmet_2",0),("iatrus_helmet_2_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1530, weight(1.5)|abundance(12)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["iatrus_plume_2", "Gilded Ridge Helmet with Crest", [("iatrus_helmet_plume_2",0),("iatrus_helmet_plume_2_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1530, weight(1.5)|abundance(12)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],

#new intercisa variants 4/11/2022
["augst_helmet_rich_1", "Ornate Silvered Ridge Helmet", [("augst_helmet_rich_1",0),("augst_helmet_rich_1_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1550 , weight(1.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["augst_helmet_rich_2", "Ornate Gilded Ridge Helmet", [("augst_helmet_rich_2",0),("augst_helmet_rich_2_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1550 , weight(1.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],

["intercisa_helmet_rich_1", "Ornate Silvered Ridge Helmet", [("intercisa_helmet_rich_1",0),("intercisa_helmet_rich_1_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1550 , weight(1.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["intercisa_helmet_rich_2", "Ornate Silvered Ridge Helmet", [("intercisa_helmet_rich_2",0),("intercisa_helmet_rich_2_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1550 , weight(1.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["intercisa_helmet_rich_3", "Ornate Gilded Ridge Helmet", [("intercisa_helmet_rich_3",0),("intercisa_helmet_rich_3_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1550 , weight(1.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["intercisa_helmet_rich_4", "Ornate Gilded Ridge Helmet", [("intercisa_helmet_rich_4",0),("intercisa_helmet_rich_4_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1550 , weight(1.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],

["augst_helmet_rich_plume_1", "Ornate Silvered Ridge Helmet with Crest", [("augst_helmet_rich_plume_1",0),("augst_helmet_rich_plume_1_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1550 , weight(1.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["augst_helmet_rich_plume_2", "Ornate Gilded Ridge Helmet with Crest", [("augst_helmet_rich_plume_2",0),("augst_helmet_rich_plume_2_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1550 , weight(1.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["augst_helmet_crested_rich_1", "Ornate Silvered Ridge Helmet with Crest", [("augst_helmet_crested_rich_1",0),("augst_helmet_crested_rich_1_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1550 , weight(1.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["augst_helmet_crested_rich_2", "Ornate Gilded Ridge Helmet with Crest", [("augst_helmet_crested_rich_2",0),("augst_helmet_crested_rich_2_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1550 , weight(1.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],

["intercisa_helmet_rich_plume_1", "Ornate Silvered Ridge Helmet with Crest", [("intercisa_helmet_rich_plume_1",0),("intercisa_helmet_rich_plume_1_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1550 , weight(1.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["intercisa_helmet_rich_plume_2", "Ornate Silvered Ridge Helmet with Crest", [("intercisa_helmet_rich_plume_2",0),("intercisa_helmet_rich_plume_2_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1550 , weight(1.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["intercisa_helmet_rich_plume_3", "Ornate Gilded Ridge Helmet with Crest", [("intercisa_helmet_rich_plume_3",0),("intercisa_helmet_rich_plume_3_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1550 , weight(1.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],
["intercisa_helmet_rich_plume_4", "Ornate Gilded Ridge Helmet with Crest", [("intercisa_helmet_rich_plume_4",0),("intercisa_helmet_rich_plume_4_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise,0,1550 , weight(1.5)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], culture_roman ],

["gold_ridge_helm", "Gilded Ridge Helmet", [("dux_ridge_helm_gold",0)], itp_merchandise| itp_type_head_armor,0,1550 , weight(2.5)|abundance(10)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_roman ],

["koblenz_helmet_2", "Gilded Ridge Helmet", [("koblenz_helmet_2",0),("koblenz_helmet_2_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor ,0,1550 , weight(2.5)|abundance(10)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_roman ],
["koblenz_crested_2", "Gilded Ridge Helmet with Crest", [("koblenz_helmet_plume_2",0),("koblenz_helmet_plume_2_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor ,0,1550 , weight(2.75)|abundance(10)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_roman ],

["burgh_helmet_2", "Gilded Ridge Helmet", [("burgh_helmet_2",0),("burgh_helmet_2_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1550 , weight(2.5)|abundance(10)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_roman ],
["burgh_helmet_plume_2", "Gilded Ridge Helmet with Crest", [("burgh_helmet_plume_2",0),("burgh_helmet_plume_2_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0,1550 , weight(2.75)|abundance(10)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], culture_roman ],

["koblenz_helmet_3", "Ornate Ridge Helmet", [("koblenz_helmet_3",0),("koblenz_helmet_3_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor   ,0, 1550 , weight(2.5)|abundance(10)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor, [], culture_roman ],
["koblenz_crested_3", "Ornate Ridge Helmet with Crest", [("koblenz_helmet_plume_3",0),("koblenz_helmet_plume_3_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor   ,0, 1550 , weight(2.75)|abundance(10)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor, [], culture_roman ],

["concesti_helmet", "Ornate Ridge Helmet", [("charerg_concesti",0),("charerg_concesti_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor   ,0, 1550 , weight(1.75)|abundance(10)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor, [], culture_roman+culture_gothic+culture_hunnic ], #concesti

["heteny_helmet_1", "Ornate Ridge Helmet", [("heteny_helmet_1",0),("heteny_helmet_1_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0, 1550 , weight(2.5)|abundance(10)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor, [], culture_roman+culture_gothic ], #heteny
["augsburg_1_helmet", "Ornate Ridge Helmet", [("augsburg_1_helmet",0),("augsburg_1_helmet_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0, 1550 , weight(2.5)|abundance(10)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor, [], culture_roman+culture_germanic ], #augsburg 1
["augsburg_2_helmet", "Ornate Ridge Helmet", [("augsburg_2_helmet",0),("augsburg_2_helmet_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0, 1550 , weight(2.5)|abundance(10)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor, [], culture_roman+culture_germanic ], #augsburg 2

["berkasovo_2_helmet", "Ornate Ridge Helmet", [("berkasovo_2_helmet",0),("berkasovo_2_helmet_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor,0, 1850 , weight(2.5)|abundance(5)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor, [], culture_roman ], #berk 2

#Ornate Ridge Helmets - rare and special helmets, for top tier lords + kings
["deurne_helmet", "Ornate Ridge Helmet", [("deurne_helmet",0),("deurne_helmet_inv",ixmesh_inventory)], itp_attach_armature|itp_type_head_armor   ,0, 2500 , weight(2.25)|abundance(5)|head_armor(54)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor, [], culture_roman ],
["berk_helmet", "Jewelled Ornate Ridge Helmet", [("berk_helmet",0),("berk_helmet_inv",ixmesh_inventory)], itp_attach_armature|itp_type_head_armor   ,0, 2500 , weight(2.75)|abundance(5)|head_armor(54)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor, [], culture_roman ],

["sassanid_mask_helmet_1", "Masked Crossband Helmet", [("sassanid_mask_helmet_1",0),("sassanid_mask_helmet_1_inv",ixmesh_inventory)], itp_merchandise|itp_covers_beard|itp_attach_armature|itp_type_head_armor ,0, 3200 , weight(7.5)|abundance(1)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_armor, [], culture_sassanid ],
["sassanid_mask_helmet_2", "Masked Crossband Helmet", [("sassanid_mask_helmet_2",0),("sassanid_mask_helmet_2_inv",ixmesh_inventory)], itp_merchandise|itp_covers_beard|itp_attach_armature|itp_type_head_armor ,0, 3200 , weight(7.5)|abundance(1)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_armor, [], culture_sassanid ],
["sassanid_mask_helmet_3", "Masked Crossband Helmet", [("sassanid_mask_helmet_3",0),("sassanid_mask_helmet_3_inv",ixmesh_inventory)], itp_merchandise|itp_covers_beard|itp_attach_armature|itp_type_head_armor ,0, 3200 , weight(7.5)|abundance(1)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_armor, [], culture_sassanid ],

["sassanid_helmet_shah", "Shah's Helmet", [("sassanid_helmet_shah",0),("sassanid_helmet_shah_inv",ixmesh_inventory)], itp_unique|itp_covers_beard|itp_attach_armature|itp_type_head_armor   ,0, 3600 , weight(8.5)|abundance(1)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_armor, [], culture_sassanid ],

["gultlingen_helmet_mail", "Ornate Spangenhelm with Mail", [("gultlingen_helmet_mail",0),("gultlingen_helmet_mail_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor ,0,1850 , weight(1.25)|abundance(4)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_culture_empire] ], #only sold in roman territories
["gultlingen_helmet", "Ornate Spangenhelm", [("gultlingen_helmet",0),("gultlingen_helmet_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor ,0,1850 , weight(1.75)|abundance(2)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_culture_empire] ], #only sold in roman territories
["gultlingen_helmet_plume", "Ornate Spangenhelm with Plume", [("gultlingen_helmet_plume",0),("gultlingen_helmet_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor ,0,1850 , weight(1.75)|abundance(2)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_culture_empire] ], #only sold in roman territories
["gultlingen_helmet_feathers", "Ornate Spangenhelm with Feathers", [("gultlingen_helmet_feathers",0),("gultlingen_helmet_inv",ixmesh_inventory)], itp_merchandise|itp_attach_armature|itp_type_head_armor ,0,1850 , weight(1.75)|abundance(2)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_culture_empire] ], #only sold in roman territories


#Crowns
["crown_1", "Roman Emperor's Crown", [("raw_laurel",0)], itp_unique| itp_type_head_armor| itp_doesnt_cover_hair |itp_civilian,0,2150 , weight(1.5)|abundance(10)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], culture_roman ],
["crown_2", "Roman Emperor's Crown", [("roman_crown_1",0)], itp_unique| itp_type_head_armor |itp_civilian | itp_doesnt_cover_hair,0,2150 , weight(1.5)|abundance(10)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], culture_roman ],
["crown_3", "Shah's Crown", [("sassanid_crown",0)], itp_unique| itp_type_head_armor|itp_civilian,0,2150 , weight(1.5)|abundance(10)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
["crown_4", "Crown", [("sib_couronne",0)], itp_unique| itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian,0,2150 , weight(1.5)|abundance(10)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],

#TODO:
#WEAPONS

#blunt weapons - common
["wooden_stick", "Simple Club", [("we_nor_blunt_stick",0)], itp_type_one_handed_wpn|itp_merchandise|itp_can_knock_down| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
25 , weight(2.5)|difficulty(0)|spd_rtng(94) | weapon_length(53)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["club", "Club", [("germanic_club_2",0)], itp_type_one_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
90 , weight(2.5)|difficulty(0)|spd_rtng(93) | weapon_length(41)|swing_damage(22 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["winged_mace", "Well Made Club", [("germanic_club_3",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_morningstar,
160 , weight(2.5)|difficulty(0)|spd_rtng(90) | weapon_length(67)|swing_damage(23 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["spiked_club", "Spiked Club", [("spiked_club_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
153 , weight(3)|difficulty(0)|spd_rtng(88) | weapon_length(70)|swing_damage(24 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["spiked_mace", "Spiked Club", [("club_one",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
210 , weight(3.5)|difficulty(0)|abundance(30)|spd_rtng(74) | weapon_length(70)|swing_damage(26 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["hammer",  "Hammer", [("bb_smith_hammer",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_wooden_parry, itc_scimitar,
45 , weight(3)|difficulty(8)|spd_rtng(80) | weapon_length(55)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],

#simple weapons - for peasants/tribesmen
["sickle",         "Sickle", [("sickle_swup",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver,
9 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(47)|swing_damage(20 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["cleaver",         "Cleaver", [("cleaver_swup",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver,
14 , weight(1.5)|difficulty(0)|spd_rtng(103) | weapon_length(30)|swing_damage(24 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["butchering_knife", "Butchering Knife", [("cleaver_1",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right,
23 , weight(0.75)|difficulty(0)|spd_rtng(108) | weapon_length(34)|swing_damage(24 , cut) | thrust_damage(17 ,  pierce),imodbits_sword ],

["cudgel", "Cudgel", [("club_swup",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
90 , weight(2.5)|difficulty(0)|spd_rtng(94) | weapon_length(70)|swing_damage(21 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["maul",         "Maul", [("maul_b",0)], itp_crush_through|itp_type_two_handed_wpn|itp_can_knock_down |itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,
97 , weight(6)|difficulty(11)|spd_rtng(83) | weapon_length(79)|swing_damage(36 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["sledgehammer", "Sledgehammer", [("maul_c",0)], itp_crush_through|itp_type_two_handed_wpn|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,
101 , weight(7)|difficulty(12)|spd_rtng(81) | weapon_length(82)|swing_damage(39, blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["warhammer",         "Great Hammer", [("maul_d",0)], itp_crush_through|itp_type_two_handed_wpn|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,
290 , weight(9)|difficulty(14)|spd_rtng(79) | weapon_length(75)|swing_damage(45 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["bec_de_corbin_a",  "Studded Cudgel", [("cudgel",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
 125 , weight(3.0)|difficulty(0)|spd_rtng(90) | weapon_length(80)|swing_damage(24, blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],

#unused
["great_axe",         "Great Axe", [("two_handed_battle_axe_e",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 316 , weight(4.5)|difficulty(10)|spd_rtng(88) | weapon_length(96)|swing_damage(47 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["long_spiked_club",         "Long Spiked Club", [("mace_long_c",0)], itp_type_two_handed_wpn|itp_can_knock_down| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
 600 , weight(3)|difficulty(0)|spd_rtng(82) | weapon_length(126)|swing_damage(25 , pierce) | thrust_damage(0, blunt),imodbits_mace ],
["long_hafted_knobbed_mace",         "Long Hafted Knobbed Mace", [("mace_long_a",0)], itp_type_two_handed_wpn| itp_can_knock_down|itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
 600 , weight(3)|difficulty(0)|spd_rtng(80) | weapon_length(133)|swing_damage(26 , blunt) | thrust_damage(23 ,  blunt),imodbits_mace ],


["long_hafted_spiked_mace", "Long Hafted Roman Mace", [("roman_mace_long_90",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 600 , weight(3.5)|difficulty(0)|spd_rtng(82) | weapon_length(90)|swing_damage(30 , blunt) | thrust_damage(26 ,  blunt),imodbits_mace ],


["scythe",         "Scythe", [("scythe",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear, 43 , weight(2)|difficulty(0)|spd_rtng(97) | weapon_length(182)|swing_damage(30 , cut) | thrust_damage(14 ,  pierce),imodbits_polearm ],
["pitch_fork",         "Pitch Fork", [("pitch_fork",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff, 19 , weight(1.5)|difficulty(0)|spd_rtng(87) | weapon_length(154)|swing_damage(16 , blunt) | thrust_damage(22 ,  pierce),imodbits_polearm ],
["military_fork", "Military Fork", [("military_fork",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_wooden_parry,itc_staff, 153 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(135)|swing_damage(15 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["battle_fork",         "Battle Fork", [("battle_fork",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_wooden_parry,itc_staff, 282 , weight(2.2)|difficulty(0)|spd_rtng(90) | weapon_length(144)|swing_damage(15, blunt) | thrust_damage(35 ,  pierce),imodbits_polearm ],

["pitch_fork_1", "Pitch Fork", [("pitchfork_1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff, 19 , weight(1.5)|difficulty(0)|spd_rtng(87) | weapon_length(154)|swing_damage(16 , blunt) | thrust_damage(22 ,  pierce),imodbits_polearm ],
["pitch_fork_2", "Pitch Fork", [("pitchfork_2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff, 19 , weight(1.5)|difficulty(0)|spd_rtng(87) | weapon_length(154)|swing_damage(16 , blunt) | thrust_damage(22 ,  pierce),imodbits_polearm ],

["staff",         "Staff", [("wooden_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 36 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(130)|swing_damage(18 , blunt) | thrust_damage(19 ,  blunt),imodbits_polearm ],
["quarter_staff", "Quarter Staff", [("quarter_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 60 , weight(2)|difficulty(0)|spd_rtng(104) | weapon_length(140)|swing_damage(20 , blunt) | thrust_damage(20 ,  blunt),imodbits_polearm ],
["iron_staff", "Crook", [("shepherds_crook",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary, itc_staff|itcf_carry_sword_back,
 36 , weight(2)|difficulty(0)|spd_rtng(96) | weapon_length(136)|swing_damage(19 , blunt) | thrust_damage(16 ,  blunt),imodbits_polearm ],

#Weapons
#["arabian_sword_e", "Sassanid Sword", [("sasword_c2",0),("sasword_scab_vertexanimated", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#950 , weight(1.5)|difficulty(0)|spd_rtng(88) | weapon_length(97)|swing_damage(30 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high, [], culture_sassanid+culture_caucasian],

#["sassanid_sword_1", "Sassanid Sword", [("east_sword87_1",0),("east_sword87_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#950 , weight(1.5)|difficulty(0)|spd_rtng(90) | weapon_length(86)|swing_damage(28 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high, [], culture_sassanid+culture_caucasian],
["irish_short_sword", "Short Sword", [("irish_sword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
950 , weight(2.5)|difficulty(8)|spd_rtng(94) | weapon_length(64)|swing_damage(23 , cut) | thrust_damage(26 ,  pierce),imodbits_sword, [], culture_celtic ],

["long_sword_a", "Longsword", [("Pictish_Longsword_2",0),("pictish_longsword_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 950 , weight(1.5)|difficulty(0)|spd_rtng(87) | weapon_length(110)|swing_damage(32 , cut) | thrust_damage(20 ,  pierce),imodbits_sword, [], [fac_culture_5] ],
["long_sword_b", "Longsword", [("Pictish_Longsword_1",0),("pictish_longsword_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 950 , weight(1.5)|difficulty(0)|spd_rtng(87) | weapon_length(110)|swing_damage(32 , cut) | thrust_damage(20 ,  pierce),imodbits_sword, [], [fac_culture_5] ],

["champion_sword_1", "Champion Sword", [("gaelic_champion_sword",0),("gaelic_champion_sword", ixmesh_carry)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword|itcf_carry_sword_back,
 1200 , weight(2.35)|difficulty(10)|spd_rtng(86) | weapon_length(110)|swing_damage(37 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high, [], [fac_culture_5] ],

#spathas lengths + speeds
# <90 l, ~90 speed
# >90 1, ~89 speed

#reg spathas ~28
#rich spathas ~31

#Regular spathas
["sword_viking_1", "Spatha", [("behmer_V",0),("behmer_V_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
 950 , weight(1.25)|abundance(60)|difficulty(0)|spd_rtng(89) | weapon_length(93)|swing_damage(27 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high, [], culture_germanic ], #generic

["sword_medieval_a", "Spatha", [("feltwell_spatha",0),("feltwell_spatha_scabbard", ixmesh_carry),("feltwell_spatha_rusty",imodbits_bad)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 950 , weight(1.25)|abundance(60)|difficulty(0)|spd_rtng(90) | weapon_length(85)|swing_damage(28 , cut) | thrust_damage(18 ,  pierce),imodbits_sword_high, [], culture_germanic+culture_gothic+culture_roman ], #primarily roman

["sword_medieval_b", "Spatha", [("cujik_spatha",0),("cujik_spatha_scabbard", ixmesh_carry),("cujik_spatha_rusty",imodbits_bad)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 950 , weight(1.5)|abundance(60)|difficulty(0)|spd_rtng(89) | weapon_length(90)|swing_damage(28 , cut) | thrust_damage(17 ,  pierce),imodbits_sword_high, [], culture_roman ], #roman

["sword_medieval_b_small", "Short Spatha", [("pict_sword_1",0),("pict_sword_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 950 , weight(1)|abundance(60)|difficulty(0)|spd_rtng(92) | weapon_length(77)|swing_damage(25, cut) | thrust_damage(21, pierce),imodbits_sword_high, [], culture_celtic ], #celtic/pictish

["sword_medieval_c", "Spatha", [("OrnateSpatha_S_ND",0),("ornatespatha2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 950 , weight(1.5)|abundance(60)|difficulty(0)|spd_rtng(88) | weapon_length(96)|swing_damage(28 , cut) | thrust_damage(16 ,  pierce),imodbits_sword_high, [], culture_germanic+culture_gothic ], #can be used by anyone

["sword_medieval_c_small", "Short Spatha", [("CelticShort1_1",0),("CelticShort1_1_Scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 950 , weight(1)|abundance(60)|difficulty(0)|spd_rtng(93) | weapon_length(69)|swing_damage(25, cut) | thrust_damage(20 ,  pierce),imodbits_sword_high, [], culture_celtic ], #celtic/pictish

["sword_medieval_c_long", "Spatha", [("kragenhul_spatha",0),("kragenhul_spatha_scabbard", ixmesh_carry),("kragenhul_spatha_rusty",imodbits_bad)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 950 , weight(1.7)|abundance(60)|difficulty(0)|spd_rtng(90) | weapon_length(85)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high, [], culture_germanic+culture_gothic ], #germanic

["sword_medieval_d_long", "Spatha", [("indesheim_spatha",0),("indesheim_spatha_scabbard", ixmesh_carry),("indesheim_spatha_rusty",imodbits_bad)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 950 , weight(1.5)|abundance(60)|difficulty(0)|spd_rtng(90) | weapon_length(84)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high, [], culture_germanic+culture_gothic+culture_roman ],

["sword_viking_a_long", "Spatha", [("samson_spatha_2",0),("samson_spatha_2_scabbard", ixmesh_carry),("samson_spatha_2_rusty",imodbits_bad)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 950 , weight(1.5)|abundance(60)|difficulty(0)|spd_rtng(90) | weapon_length(86)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high, [], culture_germanic+culture_gothic+culture_roman ],

["sarranid_two_handed_mace_1", "Short Sword", [("caucasian_dagger_2_60",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
 880 , weight(1.5)|abundance(60)|difficulty(0)|spd_rtng(94) | weapon_length(60)|swing_damage(26 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high, [], culture_caucasian ],

["sword_khergit_3", "Spatha", [("samson_spatha_1",0),("samson_spatha_1_scabbard", ixmesh_carry),("samson_spatha_1_rusty",imodbits_bad)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
 950 , weight(1.5)|abundance(60)|difficulty(0)|spd_rtng(90) | weapon_length(83)|swing_damage(28 , cut)| thrust_damage(18 ,  pierce),imodbits_sword_high, [], culture_roman+culture_gothic ],

["sword_khergit_1", "Spatha", [("proto_sabre",0),("proto_sabre_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 950 , weight(1.25)|abundance(60)|difficulty(0)|spd_rtng(90) | weapon_length(95)|swing_damage(27 , cut),imodbits_sword_high, [], culture_hunnic ],

["hunnic_spatha", "Spatha", [("hunnic_spatha",0),("hunnic_spatha_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 950 , weight(1.5)|abundance(60)|difficulty(0)|spd_rtng(88) | weapon_length(97)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high, [], culture_hunnic+culture_alan ],

["samad_sword", "Persian Spatha", [("samad_sword",0),("samad_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, #used by arab, sassanid cavalry forces (inf for sassanids only!)
 950 , weight(1.5)|abundance(60)|difficulty(0)|spd_rtng(90) | weapon_length(82)|swing_damage(28 , cut) | thrust_damage(16 ,  pierce),imodbits_sword_high, [], culture_sassanid ],

["baltic_sword_1", "Baltic Spatha", [("baltic_sword_1",0),("baltic_sword_1_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 950 , weight(1.85)|abundance(60)|difficulty(0)|spd_rtng(87) | weapon_length(107)|swing_damage(28 , cut) | thrust_damage(18 ,  pierce),imodbits_sword_high ],

["ringsword_1", "Spatha", [("ringsword_long",0),("ringsword_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 950 , weight(1.85)|abundance(60)|difficulty(0)|spd_rtng(89) | weapon_length(92)|swing_damage(29 , cut) | thrust_damage(16 ,  pierce),imodbits_sword_high ],

#Rich/Ornate Spathas
["tetraxitae_spatha", "Rich Tetraxitae Spatha", [("tetraxitae_spatha",0),("tetraxitae_spatha_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
1700 , weight(1.25)|abundance(30)|difficulty(0)|spd_rtng(90) | weapon_length(90)|swing_damage(30 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high, [], culture_hunnic+culture_caucasian ], #for the crimean goths/tetraxitae

["sword_viking_2", "Rich Germanic Spatha", [("behmer_V_rich",0),("behmer_V_rich_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
1700 , weight(1.25)|abundance(30)|difficulty(0)|spd_rtng(89) | weapon_length(93)|swing_damage(31 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high, [], culture_germanic+culture_gothic ], #generic

["sword_viking_2_small", "Rich Pictish Spatha", [("pict_sword_rich",0),("pict_sword_rich_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
1700 , weight(1.25)|abundance(30)|difficulty(0)|spd_rtng(92) | weapon_length(84)|swing_damage(29 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high, [], culture_celtic ], #celtic/pictish

["sword_viking_3", "Rich Spatha", [("OrnateSpatha_G_D",0),("ornatespatha1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
1700 , weight(1.5)|abundance(30)|difficulty(0)|spd_rtng(88) | weapon_length(96)|swing_damage(31 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high, [], culture_germanic+culture_gothic ], #germanic

["sword_viking_3_small", "Ornate Spatha", [("spathabarbaro_demasc",0),("spathabarbaro_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
1700 , weight(1.25)|abundance(30)|difficulty(0)|spd_rtng(91) | weapon_length(86)|swing_damage(30 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high, [], culture_germanic+culture_gothic ],

["sword_viking_c_long", "Rich Spatha", [("kragenhul_spatha_rich",0),("kragenhul_spatha_rich_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
1700 , weight(1.5)|abundance(30)|difficulty(0)|spd_rtng(90) | weapon_length(85)|swing_damage(30 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high, [], culture_germanic+culture_gothic ],

["arabian_sword_a", "Rich Spatha", [("feltwell_spatha_rich",0),("feltwell_spatha_rich_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
1700 , weight(1.5)|abundance(30)|difficulty(0)|spd_rtng(90) | weapon_length(85)|swing_damage(31 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high, [], culture_roman+culture_gothic+culture_germanic ], #roman

["arabian_sword_b", "Rich Spatha", [("cujik_spatha_rich",0),("cujik_spatha_rich_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
1700 , weight(1.5)|abundance(30)|difficulty(0)|spd_rtng(90) | weapon_length(88)|swing_damage(31 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high, [], culture_roman ], #roman

["pictish_sword", "Rich Celtic Spatha", [("CelticShort1_1_rich",0),("CelticShort1_1_rich_Scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
1700 , weight(1.25)|abundance(30)|difficulty(0)|spd_rtng(93) | weapon_length(69)|swing_damage(29 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high, [], culture_celtic ],

["sword_khergit_2", "Rich Spatha", [("aquincum_spatha",0),("aquincum_spatha_scabbard", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
1700 , weight(1.25)|abundance(30)|difficulty(0)|spd_rtng(91) | weapon_length(75)|swing_damage(31 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high, [], culture_gothic+culture_roman ],

["sword_khergit_4", "Rich Spatha", [("samson_spatha_1_rich",0),("samson_spatha_1_rich_scabbard", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
1700 , weight(1.5)|abundance(30)|difficulty(0)|spd_rtng(90) | weapon_length(83)|swing_damage(31 , cut)| thrust_damage(20 ,  pierce),imodbits_sword_high, [], culture_roman ],

["indesheim_spatha_rich", "Rich Spatha", [("indesheim_spatha_rich",0),("indesheim_spatha_rich_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
1700 , weight(1.5)|abundance(30)|difficulty(0)|spd_rtng(90) | weapon_length(84)|swing_damage(30 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high, [], culture_germanic+culture_gothic+culture_roman ], #roman

["samson_spatha_2_rich", "Rich Spatha", [("samson_spatha_2_rich",0),("samson_spatha_2_rich_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
1700 , weight(1.5)|abundance(30)|difficulty(0)|spd_rtng(90) | weapon_length(86)|swing_damage(30 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high, [], culture_germanic+culture_gothic+culture_roman ], #roman

["beja_spatha", "Ornate Spatha", [("beja_spatha",0),("beja_spatha_scabbard", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
1800 , weight(1.5)|abundance(30)|difficulty(0)|spd_rtng(89) | weapon_length(95)|swing_damage(31 , cut)| thrust_damage(21 ,  pierce),imodbits_sword_high, [], culture_germanic+culture_gothic+culture_hunnic+culture_alan ],

["djurso_spatha", "Ornate Spatha", [("djurso_spatha",0),("djurso_spatha_scabbard", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
1800 , weight(1.5)|abundance(30)|difficulty(0)|spd_rtng(89) | weapon_length(92)|swing_damage(31 , cut)| thrust_damage(21 ,  pierce),imodbits_sword_high, [], culture_hunnic+culture_alan ],

["pannonhalma_spatha", "Ornate Long Spatha", [("pannonhalma_spatha",0),("pannonhalma_spatha_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, #used by hunnic + gepid lords
2000 , weight(1.5)|abundance(10)|difficulty(7)|spd_rtng(90) | weapon_length(94)|swing_damage(32 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high, [], culture_gothic+culture_hunnic ],

["klin_yar_spatha", "Ornate Long Spatha", [("klin_yar_spatha",0),("klin_yar_spatha_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, #mainly used by alan troops + lords
2000 , weight(2.0)|abundance(10)|difficulty(9)|spd_rtng(88) | weapon_length(99)|swing_damage(32 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high, [], culture_alan ],

["ingushetia_spatha", "Rich Long Spatha", [("ingushetia_spatha",0),("ingushetia_spatha_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, #used by sassanid, hunnic, alan lords (maybe throw in a caucasian too)
2000 , weight(1.75)|abundance(10)|difficulty(8)|spd_rtng(89) | weapon_length(94)|swing_damage(33 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high, [], culture_sassanid ], #sassanids, caucasians, alans, huns

#others
["sword_of_war", "Old Germanic Sword", [("ancient_germanic_sword",0),("ancient_germanic_sword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 950 , weight(1.25)|abundance(10)|difficulty(6)|spd_rtng(90) | weapon_length(80)|swing_damage(29 , cut) | thrust_damage(16 ,  pierce),imodbits_sword_high ],

["sassanid_greatsword", "Persian Champion Sword", [("sassanid_greatsword",0)], itp_merchandise|itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword|itcf_carry_sword_back,
 3400 , weight(2.75)|abundance(1)|difficulty(13)|spd_rtng(85) | weapon_length(131)|swing_damage(38 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high, [], culture_sassanid ],

["borok_spatha", "Hunnic War Sword", [("borok_spatha",0),("borok_spatha_scabbard", ixmesh_carry)], itp_unique|itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 3800 , weight(2.5)|abundance(1)|difficulty(13)|spd_rtng(86) | weapon_length(101)|swing_damage(36 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high, [], culture_hunnic ],

#princely
#taurapilis spatha (aestii king)
["taurapilis_spatha", "Princely Spatha", [("taurapilis_spatha",0),("taurapilis_spatha_scabbard", ixmesh_carry)], itp_unique|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
4000 , weight(1.5)|abundance(0)|difficulty(0)|spd_rtng(90) | weapon_length(96)|swing_damage(34 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high ], 
#evebo spatha (norwegian king)
["evebo_spatha", "Princely Spatha", [("evebo_spatha",0),("evebo_spatha_scabbard", ixmesh_carry)], itp_unique|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
4000 , weight(1.5)|abundance(0)|difficulty(0)|spd_rtng(90) | weapon_length(94)|swing_damage(33 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ], 

["arabian_sword_d", "Ornate Emperor's Spatha", [("honorius_spatha_ornate",0),("honorius_spatha_ornate_scabbard", ixmesh_carry)], itp_unique|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 4000 , weight(1.5)|difficulty(0)|spd_rtng(89) | weapon_length(96)|swing_damage(35 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high, [], [fac_culture_empire] ], #used by special lords + roman emperors

["nagelring", "Nagelring", [("Ringsword",0),("Ringsword_scabbard", ixmesh_carry)], itp_unique|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 4000 , weight(1.5)|difficulty(0)|spd_rtng(91) | weapon_length(83)|swing_damage(35 , cut)| thrust_damage(21 ,  pierce),imodbits_sword_high ],

#Spears

#Light/Short Spears
["wooden_spear", "Wooden Spear", [("wooden_javelin",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab,200 , weight(1.0)|abundance(100)|difficulty(2)|spd_rtng(98) | weapon_length(125)|swing_damage(16 , blunt) | thrust_damage(24 ,  pierce),imodbits_polearm ],

["spear", "Light Spear", [("spear_4_133",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab,200 , weight(1.5)|abundance(100)|difficulty(4)|spd_rtng(96) | weapon_length(133)|swing_damage(18 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm ],
["roman_spear_1", "Short Contus", [("roman_spear_1",0)], itp_type_polearm|itp_merchandise|itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 200 , weight(1.25)|abundance(100)|difficulty(4)|spd_rtng(98) | weapon_length(117)|swing_damage(18 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["shortened_spear", "Short Spear", [("spear_g_1-9m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 200 , weight(1.25)|abundance(100)|difficulty(4)|spd_rtng(98) | weapon_length(120)|swing_damage(18 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["bamboo_spear", "Bamboo Spear", [("arabian_spear_a_3m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_penalty_with_shield|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 180 , weight(2.0)|abundance(97)|difficulty(4)|spd_rtng(96) | weapon_length(200)|swing_damage(19 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["glaive", "Spear", [("gallic_spear_2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 220 , weight(1.50)|difficulty(4)|spd_rtng(95) | weapon_length(132)|swing_damage(21 , cut) | thrust_damage(27 ,  pierce),imodbits_polearm ],

#Medium tier spears
["roman_spear_2","Contus", [("roman_spear_2",0)], itp_type_polearm|itp_merchandise|itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 250 , weight(2.25)|abundance(100)|difficulty(6)|spd_rtng(96) | weapon_length(134)|swing_damage(19 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm ],
["medium_spear_1", "Spear", [("medium_spear_1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 250 , weight(2.25)|abundance(100)|difficulty(6)|spd_rtng(95) | weapon_length(168)|swing_damage(19 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm ],
["medium_spear_2", "Spear", [("spear_4_158",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 250 , weight(2.25)|abundance(100)|difficulty(6)|spd_rtng(96) | weapon_length(158)|swing_damage(19 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm ],
["medium_spear_3", "Long Spear", [("spear_5_164",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 250 , weight(2.25)|abundance(100)|difficulty(6)|spd_rtng(96) | weapon_length(164)|swing_damage(19 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm ],
["medium_spear_4", "Spear", [("spear_6_154",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 250 , weight(2.25)|abundance(100)|difficulty(6)|spd_rtng(96) | weapon_length(154)|swing_damage(19 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm ],

#Heavy spears
["roman_spear_3","Contus", [("roman_spear_3",0)], itp_type_polearm|itp_merchandise|itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 400 , weight(2.25)|abundance(100)|difficulty(6)|spd_rtng(94) | weapon_length(178)|swing_damage(18 , cut) | thrust_damage(29 ,  pierce),imodbits_polearm ],
["boar_spear", "Spear", [("spear_1_160",0)], itp_type_polearm|itp_merchandise|itp_primary|itp_secondary|itp_penalty_with_shield|itp_wooden_parry,itc_spear_upstab,400 , weight(2.25)|difficulty(6)|abundance(100)|spd_rtng(95) | weapon_length(160)|swing_damage(20 , blunt) | thrust_damage(29 ,  pierce),imodbits_polearm ],
["great_lance", "Heavy Spear", [("spear_2_154",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 400 , weight(2.25)|abundance(100)|difficulty(6)|spd_rtng(95) | weapon_length(154)|swing_damage(20 , blunt) | thrust_damage(29 ,  pierce),imodbits_polearm ],
["heavy_spear_1", "Spear", [("spear_7_142",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 400 , weight(2.25)|abundance(100)|difficulty(6)|spd_rtng(95) | weapon_length(142)|swing_damage(25 , cut) | thrust_damage(29 ,  pierce),imodbits_polearm ],

#War Spears
["war_spear", "War Spear", [("spear_2_167",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab,440 , weight(2.5)|abundance(100)|difficulty(8)|spd_rtng(94) | weapon_length(167)|swing_damage(20 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["war_spear_1", "War Spear", [("roman_war_spear",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab,440 , weight(2.5)|abundance(100)|difficulty(8)|spd_rtng(94) | weapon_length(160)|swing_damage(20 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["polehammer",  "War Spear", [("langr_bryntvari_160",0)], itp_type_polearm|itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 440 , weight(2.5)|difficulty(8)|spd_rtng(94) | weapon_length(160)|swing_damage(20 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["poleaxe",   "War Spear", [("spear_3_167",0)], itp_type_polearm|itp_offset_lance|itp_primary|itp_secondary|itp_merchandise|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 440 , weight(2.25)|difficulty(6)|spd_rtng(94) | weapon_length(167)|swing_damage(21 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["roman_spear_4","Contus", [("hasta_new_r1",0)], itp_type_polearm|itp_merchandise|itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 440 , weight(2.5)|abundance(100)|difficulty(6)|spd_rtng(94) | weapon_length(170)|swing_damage(20 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm, [], culture_roman ],
["roman_spear_2_c1",  "Decorated Contus", [("roman_spear_2_c1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 495 , weight(2.5)|abundance(60)|difficulty(8)|spd_rtng(94) | weapon_length(134)|swing_damage(20 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm, [], culture_roman ],
["roman_spear_2_c2",  "Decorated Contus", [("roman_spear_2_c2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 495 , weight(2.5)|abundance(60)|difficulty(8)|spd_rtng(94) | weapon_length(134)|swing_damage(20 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm, [], culture_roman ],
["roman_spear_2_c3",  "Decorated Contus", [("roman_spear_2_c3",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 495 , weight(2.5)|abundance(60)|difficulty(8)|spd_rtng(94) | weapon_length(134)|swing_damage(20 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm, [], culture_roman ],
["long_decorated_spear1",  "Decorated Contus", [("hasta_new_c1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 495 , weight(2.5)|abundance(60)|difficulty(8)|spd_rtng(94) | weapon_length(170)|swing_damage(20 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm, [], culture_roman ],
["long_decorated_spear2",  "Decorated Contus", [("hasta_new_c2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 495 , weight(2.5)|abundance(60)|difficulty(8)|spd_rtng(94) | weapon_length(170)|swing_damage(20 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm, [], culture_roman ],
["long_decorated_spear3",  "Decorated Contus", [("hasta_new_c3",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 495 , weight(2.5)|abundance(60)|difficulty(8)|spd_rtng(94) | weapon_length(170)|swing_damage(20 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm, [], culture_roman ],

["late_roman_spear_1","Contus", [("late_roman_spear_1_160",0)], itp_type_polearm|itp_merchandise|itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 460 , weight(2.5)|abundance(100)|difficulty(6)|spd_rtng(94) | weapon_length(160)|swing_damage(19 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm, [], culture_roman ],
["late_roman_spear_2","Contus", [("late_roman_spear_2_134",0)], itp_type_polearm|itp_merchandise|itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 460 , weight(2.25)|abundance(100)|difficulty(6)|spd_rtng(96) | weapon_length(134)|swing_damage(18 , blunt) | thrust_damage(29 ,  pierce),imodbits_polearm, [], culture_roman ],

["spear_sword", "Long Cutting Spear", [("spear_sword",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_primary|itp_crush_through|itp_two_handed|itp_wooden_parry, itc_sword_spear,670 , weight(2.5)|abundance(100)|difficulty(8)|spd_rtng(92) | weapon_length(178)|swing_damage(32 , cut) | thrust_damage(27 ,  pierce),imodbits_polearm ], #to be used by the goths

["nubian_spear_1", "Nubian War Spear", [("nubian_spear_1",0)], itp_type_polearm|itp_merchandise|itp_cant_use_on_horseback|itp_offset_lance|itp_primary|itp_crush_through|itp_two_handed|itp_wooden_parry, itc_sword_spear,800 , weight(3)|abundance(20)|difficulty(10)|spd_rtng(86) | weapon_length(174)|swing_damage(34 , cut) | thrust_damage(26 ,  pierce),imodbits_polearm, [], culture_african ],
["nubian_spear_2", "Nubian War Spear", [("nubian_spear_2",0)], itp_type_polearm|itp_merchandise|itp_cant_use_on_horseback|itp_offset_lance|itp_primary|itp_crush_through|itp_two_handed|itp_wooden_parry, itc_sword_spear,800 , weight(4)|abundance(20)|difficulty(10)|spd_rtng(84) | weapon_length(181)|swing_damage(36 , cut) | thrust_damage(24 ,  pierce),imodbits_polearm, [], culture_african ],
["nubian_spear_3", "Nubian War Spear", [("nubian_spear_3",0)], itp_type_polearm|itp_merchandise|itp_cant_use_on_horseback|itp_offset_lance|itp_primary|itp_crush_through|itp_two_handed|itp_wooden_parry, itc_sword_spear,800 , weight(3)|abundance(20)|difficulty(10)|spd_rtng(87) | weapon_length(169)|swing_damage(33 , cut) | thrust_damage(28 ,  pierce),imodbits_polearm, [], culture_african ],
["nubian_spear_4", "Long Nubian War Spear", [("nubian_spear_4",0)], itp_type_polearm|itp_merchandise|itp_cant_use_on_horseback|itp_offset_lance|itp_primary|itp_crush_through|itp_two_handed|itp_wooden_parry, itc_sword_spear,800 , weight(5)|abundance(20)|difficulty(10)|spd_rtng(82) | weapon_length(200)|swing_damage(30 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm, [], culture_african ],

#Pikes/Lances
["ashwood_pike", "Pike", [("rus_pike",0)], itp_type_polearm|itp_offset_lance| itp_cant_use_on_horseback|itp_primary|itp_two_handed|itp_wooden_parry, itc_pike_upstab,
 405 , weight(3.5)|difficulty(9)|spd_rtng(92) | weapon_length(250)|swing_damage(19 , blunt) | thrust_damage(31,  pierce),imodbits_polearm ],
["pike",         "Pike", [("spear_a_3m",0)], itp_type_polearm|itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_pike_upstab,
 325 , weight(3.0)|difficulty(0)|spd_rtng(90) | weapon_length(245)|swing_damage(16 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm ],
["long_spear_a", "Long Bladed Spear", [("ped_heavy_spear_long",0)], itp_type_polearm|itp_merchandise|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry, itc_spear_upstab, 400, weight(3)|difficulty(7)|spd_rtng(93)|weapon_length(136)|swing_damage(28,cut)|thrust_damage(29,pierce), imodbits_polearm ],

["long_lance", "Long Kontos", [("kontos_new",0)], itp_couchable|itp_type_polearm|itp_two_handed|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_penalty_with_shield|itp_wooden_parry, itc_kontos_upstab,
 670 , weight(5)|difficulty(11)|spd_rtng(90) | weapon_length(273)|swing_damage(19 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],

["light_lance", "Light Kontos", [("bb_serbian_lance_new",0)], itp_couchable|itp_type_polearm|itp_two_handed|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_penalty_with_shield|itp_wooden_parry, itc_kontos_upstab,
 180 , weight(2.5)|difficulty(0)|spd_rtng(96) | weapon_length(200)|swing_damage(16 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm, [], culture_roman+culture_sassanid ],
["lance",         "Cavalry Spear", [("spjotkesja_165",0)], itp_type_polearm|itp_offset_lance|itp_primary|itp_secondary|itp_penalty_with_shield|itp_wooden_parry, itc_lance_upstab,
 270 , weight(2.5)|difficulty(0)|spd_rtng(94) | weapon_length(165)|swing_damage(16 , blunt) | thrust_damage(29 ,  pierce),imodbits_polearm, [], culture_roman+culture_sassanid ],
["heavy_lance", "Heavy Kontos", [("rus_pike",0)], itp_couchable|itp_type_polearm|itp_two_handed|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_penalty_with_shield|itp_wooden_parry, itc_kontos_upstab,
 360 , weight(2.75)|difficulty(6)|spd_rtng(91) | weapon_length(250)|swing_damage(16 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm, [], culture_roman+culture_sassanid ],
["double_sided_lance", "Contus", [("spear_6_154",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_wooden_parry, itc_lance_upstab, 261 , weight(4.0)|difficulty(0)|spd_rtng(97) | weapon_length(154)|swing_damage(25, cut) | thrust_damage(26 ,  pierce),imodbits_polearm, [], culture_roman+culture_sassanid ],

#Ranged
["stones",         "Stones", [("throwing_stone",0)], itp_type_thrown|itp_primary ,itcf_throw_stone, 1 , weight(4)|difficulty(0)|spd_rtng(97) | shoot_speed(30) | thrust_damage(11 ,  blunt)|max_ammo(18)|weapon_length(8),imodbit_large_bag ],

["throwing_knives", "Throwing Knives", [("throwing_knife_new",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 76 , weight(2.5)|difficulty(0)|spd_rtng(121) | shoot_speed(25) | thrust_damage(19 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_thrown ],
["throwing_daggers", "Throwing Daggers", [("throwing_dagger_new_a",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 193 , weight(2.5)|difficulty(0)|spd_rtng(110) | shoot_speed(24) | thrust_damage(25 ,  cut)|max_ammo(13)|weapon_length(0),imodbits_thrown ],
#TODO: Light Trowing axe, Heavy Throwing Axe

["hunting_bow",         "Hunting Bow", [("grim_hunting_bow_1",0),("grim_hunting_bow_1_carry",ixmesh_carry)],itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back,
200 , weight(1)|difficulty(0)|spd_rtng(100) | shoot_speed(52) | thrust_damage(5 ,  cut),imodbits_bow ],

["short_bow",         "Short Bow", [("grim_shortbow_1",0),("grim_shortbow_1_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,
300 , weight(1)|difficulty(1)|spd_rtng(97) | shoot_speed(55) | thrust_damage(6 ,  cut  ),imodbits_bow ],

["long_bow",         "Long Bow", [("long_bow_a",0),("long_bow_a_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_cant_use_on_horseback|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,
545 , weight(1.75)|difficulty(3)|spd_rtng(79) | shoot_speed(56) | thrust_damage(11 ,  cut),imodbits_bow ],

["war_bow",         "War Bow", [("bb_w2_war_bow",0),("bb_w2_war_bow_carry",ixmesh_carry)],itp_type_bow|itp_merchandise|itp_cant_use_on_horseback|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,
728 , weight(1.5)|difficulty(5)|spd_rtng(84) | shoot_speed(59) | thrust_damage(12 ,cut),imodbits_bow ],

#For Arabs
["nomad_bow","Recurve Bow", [("oman_bow_1",0),("oman_case_1", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
240 , weight(1.25)|difficulty(2)|spd_rtng(94) | shoot_speed(56) | thrust_damage(7 ,  cut),imodbits_bow, [], culture_sassanid ],
["oman_bow_2","Recurve Bow", [("oman_bow_2",0),("oman_case_2", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
240 , weight(1.25)|difficulty(2)|spd_rtng(94) | shoot_speed(56) | thrust_damage(7 ,  cut),imodbits_bow, [], culture_sassanid ],
#Arabs, Sassanids
["yrzi_bow_1","Eastern Bow", [("yrzi_bow_1",0),("yrzi_case_1", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
500 , weight(1.25)|difficulty(2)|spd_rtng(93) | shoot_speed(57) | thrust_damage(8 ,  cut),imodbits_bow, [], culture_sassanid ],
#Pretty much everyone - Romans, E Germans, Goths, Huns, Turks, Sassanids, Alans, Slavs, Mordens, Abasgians, Iazyges, Caucasians
["strong_bow","Reflex Bow", [("ed_dur_bow_1",0),("ed_dur_case_1", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
700 , weight(1.25)|difficulty(3)|spd_rtng(89) | shoot_speed(58) | thrust_damage(9 ,cut),imodbit_cracked | imodbit_bent | imodbit_masterwork ],
#Turks, Alans, Sassanids, Mordens, Slavs, Abasgians, Iazyges
["khergit_bow","Asymmetrical Reflex Bow", [("niya_bow_1",0),("niya_case_1", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
825 , weight(1.5)|difficulty(3)|spd_rtng(91) | shoot_speed(58) | thrust_damage(10 ,cut),imodbits_bow, [], culture_sassanid+culture_hunnic+culture_alan ],
["niya_bow_2","Decorated Asymmetrical Reflex Bow", [("niya_bow_2",0),("niya_case_2", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
1000 , weight(1.5)|difficulty(3)|abundance(20)|spd_rtng(91) | shoot_speed(59) | thrust_damage(11 ,cut),imodbits_bow, [], culture_hunnic+culture_alan ],

["hunting_crossbow", "Hunting Crossbow", [("light_crossbow",0)], itp_type_crossbow|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
700 , weight(2.25)|abundance(20)|difficulty(0)|spd_rtng(47) | shoot_speed(50) | thrust_damage(25 ,  pierce)|max_ammo(1),imodbits_crossbow ],
["light_crossbow", "Light Crossbow", [("roman_crossbow_1",0)], itp_type_crossbow |itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
800 , weight(2.5)|abundance(20)|difficulty(8)|spd_rtng(45) | shoot_speed(59) | thrust_damage(33 ,  pierce)|max_ammo(1),imodbits_crossbow ],
["crossbow",         "Crossbow",         [("roman_crossbow_1",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
900 , weight(3)|abundance(15)|difficulty(8)|spd_rtng(43) | shoot_speed(66) | thrust_damage(38,pierce)|max_ammo(1),imodbits_crossbow ],
["heavy_crossbow", "Heavy Crossbow", [("roman_crossbow_1",0)], itp_type_crossbow|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
1000 , weight(3.5)|abundance(10)|difficulty(9)|spd_rtng(41) | shoot_speed(68) | thrust_damage(45 ,pierce)|max_ammo(1),imodbits_crossbow ],
["sniper_crossbow", "Manuballistae", [("roman_crossbow_1",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
1200 , weight(5)|abundance(5)|difficulty(10)|spd_rtng(37) | shoot_speed(70) | thrust_damage(51 ,pierce)|max_ammo(1),imodbits_crossbow ],
["flintlock_pistol", "Sling", [("Sling",0)], itp_type_pistol |itp_merchandise|itp_cant_use_on_horseback|itp_cant_reload_on_horseback|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol, 60 , weight(0.5)|difficulty(0)|spd_rtng(100) | shoot_speed(65) | thrust_damage(18 ,pierce)|max_ammo(1)|accuracy(90),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_throw_stone")])]],

["torch_old",         "Torch", [("torch_h",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar, 11 , weight(2.5)|difficulty(0)|spd_rtng(98) | weapon_length(95)|swing_damage(31 , blunt) | thrust_damage(0 ,  pierce),imodbits_none,
 [(ti_on_init_item, [(set_position_delta,0,60,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),
])]],
["torch", "Torch", [("torch_h", imodbits_none)], itp_type_shield|itp_force_attach_left_hand|itp_merchandise, 0,33, weight(2)|abundance(100)|body_armor(5)|hit_points(4)|spd_rtng(96)|shield_height(1)|shield_width(1), imodbits_none,
	[(ti_on_init_item,
		[
			(set_position_delta, 0, 60, 0),
			(particle_system_add_new, "psys_torch_fire"),
			(particle_system_add_new, "psys_torch_smoke"),
			(set_current_color, 150, 130, 70),
			(add_point_light, 10, 30)
		])]
	],

#Throwing Spears/Angons

["angon_1", "Angon", [("angon1",0),("angon1", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itp_bonus_against_shield,
525 , weight(1)|difficulty(3)|spd_rtng(87) | shoot_speed(22) | thrust_damage(46 ,  pierce)|max_ammo(1)|weapon_length(100)|accuracy(85),imodbits_polearm, [], culture_gothic+culture_germanic ],
["angon_1_melee", "Angon", [("angon1",0),("angon1", ixmesh_carry)],itp_type_polearm|itp_primary|itp_wooden_parry , itc_spear_upstab,
525 , weight(1)|difficulty(1)|spd_rtng(96) | swing_damage(18, cut) | thrust_damage(29 ,  pierce)|weapon_length(100),imodbits_polearm ],

["angon_2", "Angon", [("gallic_spear_1",0),("gallic_spear_1", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itp_bonus_against_shield,
525 , weight(1)|difficulty(3)|spd_rtng(87) | shoot_speed(22) | thrust_damage(46 ,  pierce)|max_ammo(1)|weapon_length(131)|accuracy(85),imodbits_polearm, [], culture_gothic+culture_germanic ],
["angon_2_melee", "Angon", [("gallic_spear_1",0),("gallic_spear_1", ixmesh_carry)],itp_type_polearm|itp_primary|itp_wooden_parry , itc_spear_upstab,
525 , weight(1)|difficulty(1)|spd_rtng(96) | swing_damage(18, cut) | thrust_damage(29 ,  pierce)|weapon_length(131),imodbits_polearm ],

["spiculum", "Spiculum", [("spiculum_1",0),("spiculum_1", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itp_bonus_against_shield,
525 , weight(1)|difficulty(2)|spd_rtng(91) | shoot_speed(26) | thrust_damage(41 ,  pierce)|max_ammo(1)|weapon_length(109)|accuracy(85),imodbits_polearm, [], culture_roman ],
["spiculum_melee", "Spiculum", [("spiculum_1",0),("spiculum_1", ixmesh_carry)],itp_type_polearm|itp_primary|itp_wooden_parry , itc_spear_upstab,
525 , weight(1)|difficulty(1)|spd_rtng(98) | swing_damage(18, cut) | thrust_damage(30 ,  pierce)|weapon_length(109),imodbits_polearm ],

["throwing_spear_1", "Throwing Spear", [("spear_4_121",0),("spear_4_121", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itp_bonus_against_shield,
425 , weight(1)|difficulty(2)|spd_rtng(91) | shoot_speed(26) | thrust_damage(40 ,  pierce)|max_ammo(1)|weapon_length(121)|accuracy(88),imodbits_polearm ],
["throwing_spear_1_melee", "Throwing Spear", [("spear_4_121",0),("spear_4_121", ixmesh_carry)],itp_type_polearm|itp_primary|itp_wooden_parry , itc_spear_upstab,
425 , weight(1)|difficulty(2)|spd_rtng(98) | swing_damage(24, cut) | thrust_damage(27 ,  pierce)|weapon_length(121),imodbits_polearm ],

["throwing_spear_2", "Throwing Spear", [("roman_spear_1",0),("roman_spear_1", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itp_bonus_against_shield,
425 , weight(1)|difficulty(2)|spd_rtng(92) | shoot_speed(26) | thrust_damage(40 ,  pierce)|max_ammo(1)|weapon_length(117)|accuracy(88),imodbits_polearm ],
["throwing_spear_2_melee", "Throwing Spear", [("roman_spear_1",0),("roman_spear_1", ixmesh_carry)],itp_type_polearm|itp_primary|itp_wooden_parry , itc_spear_upstab,
425 , weight(1)|difficulty(2)|spd_rtng(99) | swing_damage(22, blunt) | thrust_damage(28 ,  pierce)|weapon_length(117),imodbits_polearm ],

["throwing_spear_3", "Throwing Spear", [("spear_1_122",0),("spear_1_122", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itp_bonus_against_shield,
425 , weight(1)|difficulty(2)|spd_rtng(91) | shoot_speed(26) | thrust_damage(40 ,  pierce)|max_ammo(1)|weapon_length(122)|accuracy(88),imodbits_polearm ],
["throwing_spear_3_melee", "Throwing Spear", [("spear_1_122",0),("spear_1_122", ixmesh_carry)],itp_type_polearm|itp_primary|itp_wooden_parry , itc_spear_upstab,
425 , weight(1)|difficulty(2)|spd_rtng(98) | swing_damage(20, blunt) | thrust_damage(29 ,  pierce)|weapon_length(122),imodbits_polearm ],

["darts",         "Plumbata", [("plumbata_1",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin,
155 , weight(4)|difficulty(1)|spd_rtng(96) | shoot_speed(28) | thrust_damage(22 ,  pierce)|max_ammo(7)|weapon_length(28),imodbits_thrown, [], culture_roman ],
["war_darts",         "Plumbata", [("plumbata_2",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin,
285 , weight(5)|difficulty(1)|spd_rtng(94) | shoot_speed(27) | thrust_damage(25 ,  pierce)|max_ammo(7)|weapon_length(28),imodbits_thrown, [], culture_roman ],

["wooden_javelin",         "Wooden Javelins", [("wooden_javelin_throw",0),("wooden_javelin_throw", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itp_bonus_against_shield,
100, weight(3)|difficulty(0)|spd_rtng(96) | shoot_speed(28) | thrust_damage(26 ,  pierce)|max_ammo(5)|weapon_length(104),imodbits_thrown ],
["wooden_javelin_melee",         "Wooden Javelin", [("wooden_javelin",0)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_spear_upstab,
100, weight(1)|difficulty(0)|spd_rtng(98) |swing_damage(18, blunt)| thrust_damage(22,  pierce)|weapon_length(125),imodbits_polearm ],

["javelin",         "Javelins", [("javelin_2",0),("javelin_x_carry", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itp_bonus_against_shield,
300, weight(4)|difficulty(1)|spd_rtng(91) | shoot_speed(26) | thrust_damage(32 ,  pierce)|max_ammo(4)|weapon_length(75),imodbits_thrown ],
["javelin_melee",         "Javelin", [("javelin_2",0)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_spear_upstab,
300, weight(1)|difficulty(1)|spd_rtng(98) |swing_damage(16, cut)| thrust_damage(25,  pierce)|weapon_length(75),imodbits_polearm ],

["throwing_spears",         "Skirmish Javelins", [("javelin_x",0),("javelin_x_carry", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn|itp_bonus_against_shield,
325 , weight(3)|difficulty(2)|spd_rtng(96) | shoot_speed(30) | thrust_damage(30 ,  pierce)|max_ammo(6)|weapon_length(75),imodbits_thrown ],
["throwing_spear_melee",         "Skirmish Javelin", [("javelin_x",0)],itp_type_polearm|itp_primary|itp_wooden_parry , itc_spear_upstab,
325 , weight(1)|difficulty(1)|spd_rtng(98) | swing_damage(16, cut) | thrust_damage(26 ,  pierce)|weapon_length(75),imodbits_thrown ],

["jarid",  "Javelins", [("javelin_3",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itp_bonus_against_shield,
660 , weight(4)|difficulty(2)|spd_rtng(93) | shoot_speed(26) | thrust_damage(34 ,  pierce)|max_ammo(4)|weapon_length(75),imodbits_thrown ],
["jarid_melee",   "Javelins", [("javelin_3",0)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_spear_upstab,
660 , weight(1)|difficulty(1)|spd_rtng(98) | swing_damage(16, cut) | thrust_damage(27 ,  pierce)|weapon_length(75),imodbits_thrown ],

["cavalry_javelins", "Cavalry Javelins", [("javelin_new",0),("javelins_new_quiver", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
500 , weight(8)|difficulty(2)|spd_rtng(94) | shoot_speed(25) | thrust_damage(22 ,  pierce)|max_ammo(7)|weapon_length(32),imodbits_thrown ],

#Throwing Axes

["light_throwing_axes", "Light Francisca", [("francisca",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
360, weight(1)|difficulty(1)|spd_rtng(99) | shoot_speed(18) | thrust_damage(32,cut)|max_ammo(1)|weapon_length(53),imodbits_axe, [], culture_germanic ],
["light_throwing_axes_melee", "Light Francisca", [("francisca",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
360, weight(1)|difficulty(1)|spd_rtng(92)|weapon_length(53)| swing_damage(27,cut),imodbits_axe, [], culture_germanic ],
["throwing_axes", "Francisca", [("francisca2",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
490, weight(1)|difficulty(2)|spd_rtng(98) | shoot_speed(18) | thrust_damage(34,cut)|max_ammo(1)|weapon_length(43),imodbits_axe ],
["throwing_axes_melee", "Francisca", [("francisca2",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
490, weight(1)|difficulty(2)|spd_rtng(91) | swing_damage(29,cut)|weapon_length(43),imodbits_axe, [], culture_germanic ],
["heavy_throwing_axes", "Heavy Francisca", [("gallic_axe_2",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
620, weight(5)|difficulty(3)|spd_rtng(97) | shoot_speed(18) | thrust_damage(36,cut)|max_ammo(1)|weapon_length(65),imodbits_axe ],
["heavy_throwing_axes_melee", "Heavy Francisca", [("gallic_axe_2",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
620, weight(1)|difficulty(3)|spd_rtng(90) | swing_damage(31,cut)|weapon_length(65),imodbits_axe, [], culture_germanic ],

#Axes
#Hatchet - Hand Axe - Fighting Axe - Battle Axe
#Mix between cutting + piercing damage based on size of axe head
#Axes - updated
#Low tier
["hatchet", "Hatchet", [("bb_small_hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 90 , weight(1.0)|difficulty(2)|spd_rtng(92) | weapon_length(54)|swing_damage(23 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["basic_axe", "Axe", [("axefaradon2",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 200 , weight(1.5)|difficulty(2)|spd_rtng(91) | weapon_length(52)|swing_damage(25 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["axe", "Axe", [("cavalry_Axe",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 220 , weight(2.0)|difficulty(3)|spd_rtng(88) | weapon_length(61)|swing_damage(26 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["hand_axe", "Hand Axe", [("bb_hand_axe",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 250 , weight(1.0)|difficulty(4)|spd_rtng(90) | weapon_length(61)|swing_damage(26 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["celt_axe_1","Hand Axe", [("celt_axe_1",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 250 , weight(1.5)|difficulty(2)|spd_rtng(90) | weapon_length(65)|swing_damage(26 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["fighting_axe", "Fighting Axe", [("gallic_axe_1",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 330 , weight(1.5)|difficulty(5)|spd_rtng(91) | weapon_length(58)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["securis", "Securis", [("securis",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, #used by the romans
 330 , weight(1.5)|difficulty(5)|spd_rtng(92) | weapon_length(51)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], culture_roman ],

["sassanid_axe_1", "Persian Fighting Axe", [("sassanid_axe_1",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 400 , weight(1.5)|difficulty(6)|spd_rtng(90) | weapon_length(69)|swing_damage(28 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], culture_sassanid ],

["pict_axe_a", "Short Pictish Axe", [("pictish_axe_1",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
 357 , weight(1.25)|difficulty(5)|spd_rtng(93) | weapon_length(38)|swing_damage(25 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_5] ],
["pict_axe_b", "Short Pictish Axe", [("pictish_axe_2",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
 357 , weight(1.25)|difficulty(5)|spd_rtng(93) | weapon_length(34)|swing_damage(25 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_5] ],

["socketed_axe", "Socketed Axe", [("socketed_axe",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 440 , weight(1.5)|difficulty(6)|spd_rtng(93) | weapon_length(47)|swing_damage(28 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["bearded_axe_1",  "Shortened Battle Axe", [("axe_d",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 420 , weight(1.25)|difficulty(7)|spd_rtng(90) | weapon_length(52)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["bearded_axe_2", "Shortened Battle Axe", [("bb_slavic_bearded_axe_3",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 460 , weight(1.5)|difficulty(7)|spd_rtng(90) | weapon_length(47)|swing_damage(33 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["battle_axe_1", "Battle Axe", [("axe_c",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 500 , weight(1.5)|difficulty(6)|spd_rtng(90) | weapon_length(60)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["battle_axe_2", "Battle Axe", [("bb_slavic_axe_1",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 540 , weight(1.25)|difficulty(6)|spd_rtng(90) | weapon_length(62)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["battle_axe_3", "Battle Axe", [("einhendi_hedmarkrox",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 580 , weight(1.25)|difficulty(5)|spd_rtng(90) | weapon_length(60)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["tarasovo_axe_1", "Battle Axe", [("tarasovo_axe_1",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 580 , weight(1.25)|difficulty(5)|spd_rtng(90) | weapon_length(58)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["battle_axe_4", "Battle Axe", [("bb_slavic_axe_2",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 620 , weight(1.25)|difficulty(5)|spd_rtng(91) | weapon_length(56)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["battle_axe_5", "Battle Axe", [("axe_b",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 660 , weight(1.5)|difficulty(6)|spd_rtng(91) | weapon_length(55)|swing_damage(33 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["battle_axe", "Battle Axe", [("bb_nordic_war_axe",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_morningstar|itcf_carry_axe_left_hip,
 700 , weight(1.75)|difficulty(6)|spd_rtng(88) | weapon_length(74)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

#two handed axes (quite uncommon in this period)

["sagaris", "Sagaris Battle Axe", [("lui_battleaxetwoh",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_morningstar|itcf_carry_axe_left_hip,
 620 , weight(2.5)|difficulty(8)|spd_rtng(84) | weapon_length(82)|swing_damage(38 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], culture_alan ],

["two_handed_axe", "Two Handed Fighting Axe", [("vikingaxeb",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_morningstar|itcf_carry_axe_left_hip,
 450 , weight(2)|difficulty(10)|spd_rtng(80) | weapon_length(78)|swing_damage(36 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["war_axe", "Long Battle Axe", [("axe_b_long_75",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_morningstar|itcf_carry_axe_left_hip,
 790 , weight(2.5)|difficulty(8)|spd_rtng(86) | weapon_length(75)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], culture_germanic ],

["tarasovo_poleaxe_1", "Pole Axe", [("tarasovo_poleaxe_1",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 815 , weight(5.5)|difficulty(10)|spd_rtng(86)|weapon_length(92)|swing_damage(37 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["sassanid_war_axe_1", "Persian War Axe", [("sassanid_war_axe_1",0)], itp_merchandise|itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_can_knock_down|itp_crush_through|itp_merchandise, itc_staff|itcf_carry_axe_back,
 850 , weight(4.5)|difficulty(10)|spd_rtng(84)|weapon_length(100)|swing_damage(38 , cut) | thrust_damage(15 ,  pierce),imodbits_axe, [], culture_sassanid+culture_caucasian ],

#Seax
["seax_1", "Seax", [("vikingr_seax",0),("vikingr_seax_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
380 , weight(0.5)|difficulty(0)|spd_rtng(98) | weapon_length(48)|swing_damage(20 , cut) | thrust_damage(17 ,  pierce),imodbits_sword, [], culture_germanic+culture_gothic ],
["seax_2", "Seax", [("saxon_seax",0),("saxon_seax_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
380 , weight(0.5)|difficulty(0)|spd_rtng(98) | weapon_length(47)|swing_damage(20 , cut) | thrust_damage(17 ,  pierce),imodbits_sword, [], culture_germanic+culture_gothic ],
["seax_4", "Seax", [("seax",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left,
380 , weight(0.5)|difficulty(0)|spd_rtng(98) | weapon_length(42)|swing_damage(20 , cut) | thrust_damage(17 ,  pierce),imodbits_sword, [], culture_germanic+culture_gothic ],
["seax_5", "Seax", [("simple_seax",0),("simple_seax_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_scimitar|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn,
380 , weight(0.5)|difficulty(0)|spd_rtng(98) | weapon_length(47)|swing_damage(22 , cut) | thrust_damage(0 ,  pierce),imodbits_sword, [], culture_germanic+culture_gothic ],
["seax_6", "Seax", [("had_seax",0),("had_seax_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn,
380 , weight(0.5)|difficulty(0)|spd_rtng(98) | weapon_length(47)|swing_damage(20 , cut) | thrust_damage(17 ,  pierce),imodbits_sword, [], culture_germanic+culture_gothic ],
["seax_8", "Hunting Dagger", [("hunting_dagger",0),("hunting_dagger_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
280 , weight(0.5)|difficulty(0)|spd_rtng(98) | weapon_length(42)|swing_damage(19 , cut) | thrust_damage(16 ,  pierce),imodbits_sword ],
["seax_9", "Seax", [("talak_seax",0),("talak_scab_seax", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
380 , weight(0.5)|difficulty(0)|spd_rtng(98) | weapon_length(47)|swing_damage(20 , cut) | thrust_damage(17 ,  pierce),imodbits_sword, [], culture_germanic+culture_gothic ],
["seax_10", "Ornate Seax", [("ornate_seax",0),("ornate_seax_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_scimitar|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn,
580 , weight(0.5)|difficulty(0)|spd_rtng(98) | weapon_length(54)|swing_damage(22 , cut) | thrust_damage(19 ,  pierce),imodbits_sword, [], culture_germanic+culture_gothic ],

["long_seax_1", "Seax", [("seax_1",0),("seax_1_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
620 , weight(1.25)|difficulty(0)|spd_rtng(96) | weapon_length(73)|swing_damage(23 , cut) | thrust_damage(17 ,  pierce),imodbits_sword, [], culture_germanic+culture_gothic ],
["long_seax_2", "Seax", [("seax_2",0),("seax_2_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
620 , weight(1.25)|difficulty(0)|spd_rtng(96) | weapon_length(73)|swing_damage(23 , cut) | thrust_damage(17 ,  pierce),imodbits_sword, [], culture_germanic+culture_gothic ],
["long_seax_3", "Seax", [("seax_3",0),("seax_3_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
620 , weight(1.25)|difficulty(0)|spd_rtng(96) | weapon_length(73)|swing_damage(23 , cut) | thrust_damage(17 ,  pierce),imodbits_sword, [], culture_germanic+culture_gothic ],
["long_seax_4", "Langseax", [("langseax_1",0),("langseax_1_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_quiver_back_right|itcf_show_holster_when_drawn,
620 , weight(1)|difficulty(0)|spd_rtng(96) | weapon_length(73)|swing_damage(23 , cut) | thrust_damage(17 ,  pierce),imodbits_sword, [], culture_germanic+culture_gothic ],
["long_seax_5", "Langseax", [("langseax_2",0),("langseax_2_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_quiver_back_right|itcf_show_holster_when_drawn, #itcf_carry_quiver_back_right
620 , weight(1)|difficulty(0)|spd_rtng(96) | weapon_length(75)|swing_damage(23 , cut) | thrust_damage(17 ,  pierce),imodbits_sword, [], culture_germanic+culture_gothic ],

["great_sword", "Dagger", [("caucasian_dagger_1_42",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right,
380 , weight(1.5)|difficulty(0)|spd_rtng(98) | weapon_length(42)|swing_damage(22 , cut) | thrust_damage(16 ,  pierce),imodbits_sword, [], culture_caucasian ],

["coygan_dagger", "Dagger", [("coygan_dagger",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right,
380 , weight(1.0)|difficulty(0)|spd_rtng(99) | weapon_length(36)|swing_damage(21 , cut) | thrust_damage(19 ,  pierce),imodbits_sword, [], culture_celtic ],

["knife", "Knife", [("dagger_new_1",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left,
18 , weight(0.5)|difficulty(0)|spd_rtng(100) | weapon_length(37)|swing_damage(21 , cut) | thrust_damage(13 ,  pierce),imodbits_sword ],

["dagger", "Roman Knife", [("roman_knife_24",0),("roman_knife_24_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn,
380 , weight(0.5)|difficulty(0)|spd_rtng(105) | weapon_length(24)|swing_damage(13 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high, [], [fac_culture_empire] ],

["simancas_dagger_1", "Dagger", [("simancas_dagger_1",0),("simancas_dagger_1_scabbard", ixmesh_carry),("simancas_dagger_1_rich",imodbits_good)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn,
420 , weight(0.75)|difficulty(0)|spd_rtng(105) | weapon_length(25)|swing_damage(21 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high, [], culture_roman ],
["simancas_dagger_2", "Dagger", [("simancas_dagger_2",0),("simancas_dagger_2_scabbard", ixmesh_carry),("simancas_dagger_2_rich",imodbits_good)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn,
420 , weight(0.75)|difficulty(0)|spd_rtng(105) | weapon_length(25)|swing_damage(21 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high, [], culture_roman ],

#unique weapons for aestii
["battle_knife_1", "Battle Knife", [("battle_knife_1",0),("battle_knife_1_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
500 , weight(0.5)|difficulty(0)|spd_rtng(100) | weapon_length(50)|swing_damage(23 , cut) | thrust_damage(26 ,  pierce),imodbits_sword ],
["battle_knife_2", "Battle Knife", [("battle_knife_2",0),("battle_knife_2_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
500 , weight(0.5)|difficulty(0)|spd_rtng(100) | weapon_length(41)|swing_damage(26 , cut) | thrust_damage(20 ,  pierce),imodbits_sword ],

#Maces
["mace_sassanid", "Sassanid Mace", [("sughdianmace",0)], itp_merchandise|itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 800 , weight(3.75)|difficulty(0)|abundance(10)|spd_rtng(84) | weapon_length(55)|swing_damage(30 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace, [], culture_sassanid+culture_caucasian ],
["mace_roman_1", "Roman Mace", [("late_roman_mace_1",0)], itp_merchandise|itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 700 , weight(3)|difficulty(0)|abundance(10)|spd_rtng(84) | weapon_length(67)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace, [], culture_roman ],
["mace_roman_2", "Excubitor Mace", [("excubitor_mace",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 700 , weight(4)|difficulty(0)|abundance(10)|spd_rtng(84) | weapon_length(67)|swing_damage(32 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace, [], culture_roman ],

["mace_1",         "Spiked Club", [("mace_d",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 500 , weight(1.5)|difficulty(0)|abundance(30)|spd_rtng(84) | weapon_length(70)|swing_damage(28 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_culture_empire,fac_culture_6] ],
["mace_2",         "Knobbed_Mace", [("mace_a",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 600 , weight(2.5)|difficulty(0)|abundance(30)|spd_rtng(83) | weapon_length(70)|swing_damage(26 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_culture_empire,fac_culture_6] ],
["mace_3",         "Spiked Mace", [("mace_c",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 700 , weight(2.75)|difficulty(0)|abundance(30)|spd_rtng(82) | weapon_length(70)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_culture_empire,fac_culture_6] ],
["mace_4",         "Winged Mace", [("mace_b",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 800 , weight(2.75)|difficulty(0)|abundance(10)|spd_rtng(81) | weapon_length(70)|swing_damage(30 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_culture_empire,fac_culture_6] ],

#Falx
["falx",  "Falx", [("falx",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
 810 , abundance(1)|weight(5.0)|difficulty(8)|spd_rtng(84) | weapon_length(100)|swing_damage(37 , cut) | thrust_damage(0 ,  blunt),imodbits_sword ],

# SHIELDS

["tab_shield_pavise_a", "Old Board Shield",   [("tableau_shield_pavise_2" ,0)], itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
60 , weight(3.5)|hit_points(280)|body_armor(4)|spd_rtng(89)|shield_width(43)|shield_height(100),imodbits_shield,
 [heraldic("tableau_pavise_shield_2")]],
["tab_shield_pavise_b", "Plain Board Shield",   [("tableau_shield_pavise_3" ,0)], itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
114 , weight(4)|hit_points(360)|body_armor(8)|spd_rtng(85)|shield_width(43)|shield_height(100),imodbits_shield,
 [heraldic("tableau_pavise_shield_3")]],

#New Shields

["tab_shield_round_a", "Old Round Shield", [("round_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, #not used
 100 , weight(2.5)|hit_points(195)|body_armor(8)|spd_rtng(93)|shield_width(45),imodbits_shield,
 [heraldic("tableau_round_shields_tableau_color")]],

["tab_shield_round_b", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, #not used
 165 , weight(3)|hit_points(400)|body_armor(10)|spd_rtng(88)|shield_width(42),imodbits_shield,
 [heraldic("tableau_round_shields_tableau_color")]],

["tab_shield_round_c", "Round Shield", [("round_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 305 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(89)|shield_width(45),imodbits_shield,
 [heraldic("tableau_round_shields_tableau_color")]],

["tab_shield_round_d", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 410 , weight(3.5)|hit_points(450)|body_armor(12)|spd_rtng(89)|shield_width(45),imodbits_shield,
 [heraldic("tableau_round_shield_tabular")]],

["tab_shield_round_e", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
 530 , weight(3.5)|hit_points(500)|body_armor(14)|spd_rtng(88)|shield_width(42),imodbits_shield,
 [heraldic("tableau_concave_shield_tableau")]],


["tab_shield_small_round_a", "Plain Small Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
196 , weight(2)|hit_points(310)|body_armor(8)|spd_rtng(94)|shield_width(35),imodbits_shield,
 [heraldic("tableau_round_shields_tableau_color")]],

["tab_shield_small_round_b", "Small Round Shield", [("round_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
295 , weight(2.5)|hit_points(340)|body_armor(14)|spd_rtng(92)|shield_width(35),imodbits_shield,
 [heraldic("tableau_round_shield_tabular")]],

["tab_shield_small_round_c", "Small Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
470 , weight(3)|hit_points(380)|body_armor(22)|spd_rtng(90)|shield_width(38),imodbits_shield,
 [heraldic("tableau_concave_shield_tableau")]],

["tab_shield_heater_a", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 
525 , weight(4.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield,
 [heraldic("tableau_oval_shield_tableau")]],

["tab_shield_pavise_c", "Rectangular Wicker Shield",   [("wicker_shields_rectangular",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_kite_shield, 400 , weight(5)|hit_points(430)|body_armor(10)|spd_rtng(82)|shield_width(36)|shield_height(128),imodbits_shield,
 [heraldic("tableau_wicker_shield")]],
["tab_shield_pavise_d", "Wicker Shield",[("wicker_shield_dura" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_kite_shield, 470 , weight(4)|hit_points(400)|body_armor(12)|spd_rtng(85)|shield_width(33)|shield_height(131),imodbits_shield,
 [heraldic("tableau_wicker_shield")]],

#basic oval shields
["oval_shield_wood_1", "Wooden Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.00)|hit_points(400)|body_armor(12)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_wood_1"),]),], culture_roman ],
["oval_shield_wood_2", "Wooden Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.00)|hit_points(400)|body_armor(12)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_wood_2"),]),], culture_roman ],
["oval_shield_wood_3", "Wooden Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.00)|hit_points(400)|body_armor(12)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_wood_3"),]),], culture_roman ],
["oval_shield_leather_1", "Leather Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.00)|hit_points(400)|body_armor(12)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_leather_1"),]),], culture_roman ],
["oval_shield_leather_2", "Leather Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.00)|hit_points(400)|body_armor(12)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_leather_2"),]),], culture_roman ],
["oval_shield_leather_3", "Leather Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.00)|hit_points(400)|body_armor(12)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_leather_3"),]),], culture_roman ],
["oval_shield_wicker", "Wicker Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 455 , weight(4.00)|hit_points(420)|body_armor(12)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_wicker"),]),], culture_roman ],

#basic colored oval shields
["oval_shield_red_1", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_red_1"),]),], culture_roman ],
["oval_shield_red_2", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_red_2"),]),], culture_roman ],
["oval_shield_blue_1", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_blue_1"),]),], culture_roman ],
["oval_shield_blue_2", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_blue_2"),]),], culture_roman ],
["oval_shield_green_1", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_green_1"),]),], culture_roman ],
["oval_shield_green_2", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_green_2"),]),], culture_roman ],
["oval_shield_yellow_1", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_yellow_1"),]),], culture_roman ],
["oval_shield_yellow_2", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_yellow_2"),]),], culture_roman ],
["oval_shield_orange_1", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_orange_1"),]),], culture_roman ],
["oval_shield_orange_2", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_orange_2"),]),], culture_roman ],
["oval_shield_grey_1", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_grey_1"),]),], culture_roman ],

["oval_shield_chi_rho_1", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_chi_rho_1"),]),], culture_roman ],
["oval_shield_chi_rho_2", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_chi_rho_2"),]),], culture_roman ],
["oval_shield_chi_rho_3", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_chi_rho_3"),]),], culture_roman ],
["oval_shield_chi_rho_4", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_chi_rho_4"),]),], culture_roman ],
["oval_shield_chi_rho_5", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_chi_rho_5"),]),], culture_roman ],
["oval_shield_chi_rho_6", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_chi_rho_6"),]),], culture_roman ],
["oval_shield_chi_rho_7", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_chi_rho_7"),]),], culture_roman ],

["oval_shield_1", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_1"),]),], culture_roman ],
["oval_shield_2", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_2"),]),], culture_roman ],
["oval_shield_3", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_3"),]),], culture_roman ],
["oval_shield_4", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_4"),]),], culture_roman ],
["oval_shield_5", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_5"),]),], culture_roman ],
["oval_shield_6", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_6"),]),], culture_roman ],

#briton shields
["oval_shield_briton_1", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_briton_1"),]),], [fac_culture_empire,fac_culture_3] ],
["oval_shield_briton_2", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_briton_2"),]),], [fac_culture_empire,fac_culture_3] ],
["oval_shield_briton_3", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_briton_3"),]),], [fac_culture_empire,fac_culture_3] ],

["oval_shield_domestici", "Domestici Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 625 , weight(3.25)|hit_points(520)|body_armor(15)|spd_rtng(87)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_domestici"),]),], culture_roman ],

["oval_shield_thraces", "Roman Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_thraces"),]),], culture_roman ],
["oval_shield_tzaanni", "Roman Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_tzaanni"),]),], culture_roman ],
["oval_shield_daci", "Roman Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_daci"),]),], culture_roman ],
["oval_shield_scythae", "Roman Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_scythae"),]),], culture_roman ],
["oval_shield_transtigritani", "Roman Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_transtigritani"),]),], culture_roman ],
["oval_shield_pontinenses", "Roman Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_pontinenses"),]),], culture_roman ],
["oval_shield_regii_west", "Roman Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_regii_west"),]),], culture_roman ],
["oval_shield_regii_east", "Roman Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_regii_east"),]),], culture_roman ],
["oval_shield_moesiaci", "Roman Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_moesiaci"),]),], culture_roman ],
["oval_shield_mattiaci", "Roman Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_mattiaci"),]),], culture_roman ],
["oval_shield_mattiarii", "Roman Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_mattiarii"),]),], culture_roman ],
["oval_shield_primi_theodosiani", "Roman Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_primi_theodosiani"),]),], culture_roman ],
["oval_shield_propugnatores_iuniores", "Roman Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_propugnatores_iuniores"),]),], culture_roman ],
["oval_shield_defensores_seniores", "Roman Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_defensores_seniores"),]),], culture_roman ],
["oval_shield_ursarienses", "Roman Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_ursarienses"),]),], culture_roman ],
["oval_shield_victores", "Roman Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_victores"),]),], culture_roman ],
["oval_shield_matiarii_iuniores", "Roman Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_matiarii_iuniores"),]),], culture_roman ],
["oval_shield_felices_valentinianenses", "Roman Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_felices_valentinianenses"),]),], culture_roman ],
["oval_shield_augustenses", "Roman Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_augustenses"),]),], culture_roman ],
["oval_shield_ioviani_seniores", "Roman Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_ioviani_seniores"),]),], culture_roman ],

["oval_shield_limitanei_1", "Limitanei Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_limitanei_1"),]),], culture_roman ],
["oval_shield_limitanei_2", "Limitanei Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_limitanei_2"),]),], culture_roman ],
["oval_shield_limitanei_3", "Limitanei Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_limitanei_3"),]),], culture_roman ],
["oval_shield_limitanei_4", "Limitanei Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_limitanei_4"),]),], culture_roman ],
["oval_shield_limitanei_5", "Limitanei Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_limitanei_5"),]),], culture_roman ],
["oval_shield_limitanei_6", "Limitanei Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_limitanei_6"),]),], culture_roman ],
["oval_shield_limitanei_7", "Limitanei Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_limitanei_7"),]),], culture_roman ],

["oval_shield_pseudo_1", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_pseudo_1"),]),], culture_roman ],
["oval_shield_pseudo_2", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_pseudo_2"),]),], culture_roman ],
["oval_shield_pseudo_3", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_pseudo_3"),]),], culture_roman ],

["oval_shield_berber_1", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_berber_1"),]),], culture_roman ],
["oval_shield_berber_2", "Oval Shield", [("oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_round_shield, 525 , weight(3.00)|hit_points(500)|body_armor(14)|spd_rtng(86)|shield_width(46)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_oval_shield_berber_2"),]),], culture_roman ],

#rectangular shields
["wicker_shields_rectangular_1", "Rectangular Wicker Shield", [("wicker_shields_rectangular",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_kite_shield, 400 , weight(5)|hit_points(430)|body_armor(10)|spd_rtng(82)|shield_width(36)|shield_height(128),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_wicker_shields_1"),]),], culture_sassanid+culture_caucasian ],
["wicker_shields_rectangular_2", "Rectangular Wicker Shield", [("wicker_shields_rectangular",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_kite_shield, 400 , weight(5)|hit_points(430)|body_armor(10)|spd_rtng(82)|shield_width(36)|shield_height(128),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_wicker_shields_2"),]),], culture_sassanid+culture_caucasian ],
["wicker_shields_rectangular_3", "Rectangular Wicker Shield", [("wicker_shields_rectangular",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_kite_shield, 400 , weight(5)|hit_points(430)|body_armor(10)|spd_rtng(82)|shield_width(36)|shield_height(128),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_wicker_shields_3"),]),], culture_sassanid+culture_caucasian ],
#dura styled shield
["wicker_shield_dura_1", "Wicker Shield", [("wicker_shield_dura",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_kite_shield, 440 , weight(4)|hit_points(400)|body_armor(12)|spd_rtng(85)|shield_width(33)|shield_height(131),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_wicker_shields_1"),]),], culture_sassanid+culture_caucasian ],
["wicker_shield_dura_2", "Wicker Shield", [("wicker_shield_dura",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_kite_shield, 440 , weight(4)|hit_points(400)|body_armor(12)|spd_rtng(85)|shield_width(33)|shield_height(131),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_wicker_shields_2"),]),], culture_sassanid+culture_caucasian ],
["wicker_shield_dura_3", "Wicker Shield", [("wicker_shield_dura",0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_kite_shield, 440 , weight(4)|hit_points(400)|body_armor(12)|spd_rtng(85)|shield_width(33)|shield_height(131),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_wicker_shields_3"),]),], culture_sassanid+culture_caucasian ],

["norman_shield_7", "Round Shield", [("leathershield_small_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  395 , weight(2.75)|hit_points(320)|body_armor(12)|spd_rtng(90)|shield_width(32),imodbits_shield],
["norman_shield_8", "Round Shield", [("leathershield_small_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  395 , weight(2.50)|hit_points(320)| body_armor(12)|spd_rtng(90)|shield_width(32),imodbits_shield],
["plate_covered_round_shield", "Round Shield", [("woodenshield_small",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  395 , weight(4)|hit_points(320)|body_armor(12)|spd_rtng(90)|shield_width(32),imodbits_shield ],
["steel_shield", "Round Shield", [("woodenshield_small_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  395 , weight(4)|hit_points(320)|body_armor(12)|spd_rtng(690)|shield_width(32),imodbits_shield ],
["leathershield_small_b_y", "Round Shield", [("leathershield_small_b_y",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  395 , weight(4)|hit_points(320)|body_armor(12)|spd_rtng(90)|shield_width(32),imodbits_shield ],

["medium_round_shield_1", "Round Shield", [("woodenshield_medium",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  395 , weight(3.00)|hit_points(400)|body_armor(12)|spd_rtng(88)|shield_width(40),imodbits_shield],
["medium_round_shield_2", "Round Shield", [("woodenshield_medium_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  395 , weight(3.00)|hit_points(400)|body_armor(12)|spd_rtng(88)|shield_width(40),imodbits_shield],
["medium_round_shield_3", "Round Shield", [("leathershield_medium",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  395 , weight(3.00)|hit_points(400)|body_armor(12)|spd_rtng(88)|shield_width(40),imodbits_shield],
["medium_round_shield_4", "Round Shield", [("leathershield_medium_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  395 , weight(3.00)|hit_points(400)|body_armor(12)|spd_rtng(88)|shield_width(40),imodbits_shield],
["medium_round_shield_5", "Round Shield", [("leathershield_medium_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  395 , weight(3.00)|hit_points(400)|body_armor(12)|spd_rtng(88)|shield_width(40),imodbits_shield],
["medium_round_shield_6", "Round Shield", [("leathershield_medium_y",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  395 , weight(3.00)|hit_points(400)|body_armor(12)|spd_rtng(88)|shield_width(40),imodbits_shield],
["medium_round_shield_7", "Round Shield", [("leathershield_medium_d_y",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  395 , weight(3.00)|hit_points(400)|body_armor(12)|spd_rtng(88)|shield_width(40),imodbits_shield],

#ROUND SHIELDS - THORSBERG
#90 Width
#70 Width

["round_shield_wood_1", "Wooden Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_wood_1"),]),]],
["round_shield_wood_2", "Wooden Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_wood_2"),]),]],
["round_shield_wood_3", "Wooden Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_wood_3"),]),]],

["round_shield_wood_small_1", "Small Wooden Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.0)|hit_points(360)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_wood_1"),]),]],
["round_shield_wood_small_2", "Small Wooden Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.0)|hit_points(360)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_wood_2"),]),]],
["round_shield_wood_small_3", "Small Wooden Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.0)|hit_points(360)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_wood_3"),]),]],

["round_shield_leather_1", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_leather_1"),]),]],
["round_shield_leather_2", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_leather_2"),]),]],
["round_shield_leather_3", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_leather_3"),]),]],

["round_shield_leather_small_1", "Small Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.0)|hit_points(360)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_leather_1"),]),]],
["round_shield_leather_small_2", "Small Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.0)|hit_points(360)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_leather_2"),]),]],
["round_shield_leather_small_3", "Small Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.0)|hit_points(360)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_leather_3"),]),]],

#Colors
["round_shield_red_1", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_red_1"),]),]],
["round_shield_red_2", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_red_2"),]),]],
["round_shield_red_3", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_red_3"),]),]],
["round_shield_red_small_1", "Small Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.0)|hit_points(360)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_red_1"),]),]],
["round_shield_red_small_2", "Small Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.0)|hit_points(360)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_red_2"),]),]],
["round_shield_red_small_3", "Small Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.0)|hit_points(360)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_red_3"),]),]],

["round_shield_blue_1", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_blue_1"),]),]],
["round_shield_blue_2", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_blue_2"),]),]],
["round_shield_blue_3", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_blue_3"),]),]],
["round_shield_blue_small_1", "Small Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.0)|hit_points(360)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_blue_1"),]),]],
["round_shield_blue_small_2", "Small Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.0)|hit_points(360)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_blue_2"),]),]],
["round_shield_blue_small_3", "Small Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.0)|hit_points(360)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_blue_3"),]),]],

["round_shield_green_1", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_green_1"),]),]],
["round_shield_green_2", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_green_2"),]),]],
["round_shield_green_small_1", "Small Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.0)|hit_points(360)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_green_1"),]),]],
["round_shield_green_small_2", "Small Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.0)|hit_points(360)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_green_2"),]),]],

["round_shield_gray_1", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_gray_1"),]),]],
["round_shield_gray_2", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_gray_2"),]),]],
["round_shield_gray_small_1", "Small Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.0)|hit_points(360)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_gray_1"),]),]],
["round_shield_gray_small_2", "Small Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.0)|hit_points(360)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_gray_2"),]),]],

["round_shield_orange_1", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_orange_1"),]),]],
["round_shield_orange_small_1", "Small Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.0)|hit_points(360)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_orange_1"),]),]],

["round_shield_yellow_1", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_yellow_1"),]),]],
["round_shield_yellow_small_1", "Small Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.0)|hit_points(360)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_yellow_1"),]),]],

["round_shield_white_1", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.5)|hit_points(400)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_white_1"),]),]],
["round_shield_white_small_1", "Small Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.0)|hit_points(360)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_white_1"),]),]],

#Germanic
["round_shield_germanic_1", "Round Shield", [("round_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_1"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_2", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_2"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_3", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_3"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_4", "Round Shield", [("round_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_4"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_5", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_5"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_6", "Round Shield", [("round_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_6"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_7", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_7"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_8", "Round Shield", [("round_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_8"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_9", "Round Shield", [("round_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_9"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_10", "Round Shield", [("round_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_10"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_11", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_11"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_12", "Round Shield", [("round_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_12"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_13", "Round Shield", [("round_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_13"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_14", "Round Shield", [("round_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_14"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_15", "Round Shield", [("round_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_15"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_16", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_16"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_17", "Round Shield", [("round_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_17"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_18", "Round Shield", [("round_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_18"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_19", "Round Shield", [("round_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_19"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_20", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_20"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_21", "Round Shield", [("round_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_21"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_22", "Round Shield", [("round_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_22"),]),], culture_germanic+culture_gothic ],

["round_shield_germanic_small_1", "Round Shield", [("round_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_1"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_small_2", "Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_2"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_small_3", "Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_3"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_small_4", "Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_4"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_small_5", "Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_5"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_small_6", "Round Shield", [("round_shield_small_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_6"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_small_7", "Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_7"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_small_8", "Round Shield", [("round_shield_small_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_8"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_small_9", "Round Shield", [("round_shield_small_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_9"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_small_10", "Round Shield", [("round_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_10"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_small_11", "Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_11"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_small_12", "Round Shield", [("round_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_12"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_small_13", "Round Shield", [("round_shield_small_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_13"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_small_14", "Round Shield", [("round_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_14"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_small_15", "Round Shield", [("round_shield_small_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_15"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_small_16", "Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_16"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_small_17", "Round Shield", [("round_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_17"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_small_18", "Round Shield", [("round_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_18"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_small_19", "Round Shield", [("round_shield_small_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_19"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_small_20", "Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_20"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_small_21", "Round Shield", [("round_shield_small_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_21"),]),], culture_germanic+culture_gothic ],
["round_shield_germanic_small_22", "Round Shield", [("round_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_22"),]),], culture_germanic+culture_gothic ],

#Roman
["round_shield_roman_1", "Round Shield", [("round_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_1"),]),], culture_roman ],
["round_shield_roman_2", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_2"),]),], culture_roman ],
["round_shield_roman_3", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_3"),]),], culture_roman ],
["round_shield_roman_4", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_4"),]),], culture_roman ],
["round_shield_roman_5", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_5"),]),], culture_roman ],
["round_shield_roman_6", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_6"),]),], culture_roman ],
["round_shield_roman_7", "Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_7"),]),], culture_roman ], #funditores
["round_shield_roman_8", "Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_8"),]),], culture_roman ], #balistarii
["round_shield_roman_9", "Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_9"),]),], culture_roman ], #balistarii theo.
["round_shield_roman_10", "Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_10"),]),], culture_roman ], #sagitarii isauri
["round_shield_roman_11", "Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_11"),]),], culture_roman ], 
["round_shield_roman_12", "Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_12"),]),], culture_roman ], #taifals
["round_shield_roman_13", "Round Shield", [("round_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_13"),]),], culture_roman ],
["round_shield_roman_14", "Round Shield", [("round_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_14"),]),], culture_roman ], #Thraces
["round_shield_roman_15", "Round Shield", [("round_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_15"),]),], culture_roman ], #Thervingi
["round_shield_roman_16", "Round Shield", [("round_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_16"),]),], culture_roman ], #Visi
["round_shield_roman_17", "Round Shield", [("round_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_17"),]),], culture_roman ], #Anglevarii
["round_shield_roman_18", "Round Shield", [("round_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_18"),]),], culture_roman ], #Falchovarii
["round_shield_roman_19", "Round Shield", [("round_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_19"),]),], culture_roman ],
["round_shield_roman_20", "Round Shield", [("round_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_20"),]),], culture_roman ],
["round_shield_roman_21", "Round Shield", [("round_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_21"),]),], culture_roman ],
["round_shield_roman_22", "Round Shield", [("round_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_22"),]),], culture_roman ],
["round_shield_roman_23", "Round Shield", [("round_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_23"),]),], culture_roman ],
["round_shield_roman_24", "Round Shield", [("round_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_24"),]),], culture_roman ],
["round_shield_roman_25", "Round Shield", [("round_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_25"),]),], culture_roman ],
["round_shield_roman_26", "Round Shield", [("round_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_26"),]),], culture_roman ],
["round_shield_roman_27", "Old Round Shield", [("round_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_27"),]),], culture_roman ],
["round_shield_roman_28", "Round Shield", [("round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_28"),]),], culture_roman ], #not really used for anything

["round_shield_roman_small_1", "Round Shield", [("round_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_1"),]),], culture_roman ],
["round_shield_roman_small_2", "Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_2"),]),], culture_roman ],
["round_shield_roman_small_3", "Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_3"),]),], culture_roman ],
["round_shield_roman_small_4", "Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_4"),]),], culture_roman ],
["round_shield_roman_small_5", "Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_5"),]),], culture_roman ],
["round_shield_roman_small_6", "Round Shield", [("round_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_6"),]),], culture_roman ],
["round_shield_roman_small_13", "Round Shield", [("round_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_13"),]),], culture_roman ],
["round_shield_roman_small_25", "Round Shield", [("round_shield_small_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_25"),]),], culture_roman ],
["round_shield_roman_small_26", "Round Shield", [("round_shield_small_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_26"),]),], culture_roman ],
["round_shield_roman_small_27", "Old Round Shield", [("round_shield_small_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_27"),]),], culture_roman ],
["round_shield_roman_small_28", "Small Round Shield", [("round_shield_small_no_boss",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_28"),]),], culture_roman+culture_african ],

#cantabrian
["round_shield_cantabrian_1", "Round Shield", [("round_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_mauri_1"),]),]],
["round_shield_cantabrian_2", "Round Shield", [("round_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_mauri_2"),]),]],
["round_shield_cantabrian_3", "Round Shield", [("round_shield_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_mauri_3"),]),]],
["round_shield_cantabrian_4", "Round Shield", [("round_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_mauri_4"),]),]],
["round_shield_cantabrian_5", "Round Shield", [("round_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_britons_1"),]),]],
["round_shield_cantabrian_6", "Round Shield", [("round_shield_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_britons_2"),]),]],
["round_shield_cantabrian_7", "Round Shield", [("round_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_britons_3"),]),]],

["round_shield_cantabrian_small_1", "Round Shield", [("round_shield_small_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_mauri_1"),]),], ],
["round_shield_cantabrian_small_2", "Round Shield", [("round_shield_small_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_mauri_2"),]),], ],
["round_shield_cantabrian_small_3", "Round Shield", [("round_shield_small_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_mauri_3"),]),], ],
["round_shield_cantabrian_small_4", "Round Shield", [("round_shield_small_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_mauri_4"),]),], ],
["round_shield_cantabrian_small_5", "Round Shield", [("round_shield_small_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_britons_1"),]),], ],
["round_shield_cantabrian_small_6", "Round Shield", [("round_shield_small_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_britons_2"),]),], ],
["round_shield_cantabrian_small_7", "Round Shield", [("round_shield_small_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_britons_3"),]),], ],

["round_shield_mauri_1", "Round Shield", [("round_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(420)|body_armor(10)|spd_rtng(86)|shield_width(45),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_mauri_5"),]),], [fac_culture_11] ],
["round_shield_mauri_small_1", "Round Shield", [("round_shield_small_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.0)|hit_points(400)|body_armor(12)|spd_rtng(90)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_mauri_5"),]),], [fac_culture_11] ],

#ROUND SHIELDS - CONCAVE/CONVEX
#Width 85
#Width 75

["concave_shield_wood_1", "Wooden Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.00)|hit_points(450)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_wood_1"),]),]],
["concave_shield_wood_2", "Wooden Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.00)|hit_points(450)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_wood_2"),]),]],
["concave_shield_wood_3", "Wooden Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.00)|hit_points(450)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_wood_3"),]),]],

["concave_shield_wood_small_1", "Small Wooden Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.50)|hit_points(400)|body_armor(14)|spd_rtng(91)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_wood_1"),]),]],
["concave_shield_wood_small_2", "Small Wooden Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.50)|hit_points(400)|body_armor(14)|spd_rtng(91)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_wood_2"),]),]],
["concave_shield_wood_small_3", "Small Wooden Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.50)|hit_points(400)|body_armor(14)|spd_rtng(91)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_wood_3"),]),]],

["concave_shield_leather_1", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.00)|hit_points(450)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_leather_1"),]),]],
["concave_shield_leather_2", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.00)|hit_points(450)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_leather_2"),]),]],
["concave_shield_leather_3", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.00)|hit_points(450)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_leather_3"),]),]],

["concave_shield_leather_small_1", "Small Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.50)|hit_points(400)|body_armor(14)|spd_rtng(91)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_leather_1"),]),]],
["concave_shield_leather_small_2", "Small Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.50)|hit_points(400)|body_armor(14)|spd_rtng(91)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_leather_2"),]),]],
["concave_shield_leather_small_3", "Small Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.50)|hit_points(400)|body_armor(14)|spd_rtng(91)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_leather_3"),]),]],

#Colors
["concave_shield_red_1", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.00)|hit_points(450)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_red_1"),]),]],
["concave_shield_red_2", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.00)|hit_points(450)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_red_2"),]),]],
["concave_shield_red_3", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.00)|hit_points(450)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_red_3"),]),]],
["concave_shield_red_small_1", "Small Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.50)|hit_points(400)|body_armor(14)|spd_rtng(91)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_red_1"),]),]],
["concave_shield_red_small_2", "Small Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.50)|hit_points(400)|body_armor(14)|spd_rtng(91)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_red_2"),]),]],
["concave_shield_red_small_3", "Small Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.50)|hit_points(400)|body_armor(14)|spd_rtng(91)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_red_3"),]),]],

["concave_shield_blue_1", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.00)|hit_points(450)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_blue_1"),]),]],
["concave_shield_blue_2", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.00)|hit_points(450)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_blue_2"),]),]],
["concave_shield_blue_3", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.00)|hit_points(450)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_blue_3"),]),]],
["concave_shield_blue_small_1", "Small Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.50)|hit_points(400)|body_armor(14)|spd_rtng(91)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_blue_1"),]),]],
["concave_shield_blue_small_2", "Small Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.50)|hit_points(400)|body_armor(14)|spd_rtng(91)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_blue_2"),]),]],
["concave_shield_blue_small_3", "Small Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.50)|hit_points(400)|body_armor(14)|spd_rtng(91)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_blue_3"),]),]],

["concave_shield_green_1", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.00)|hit_points(450)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_green_1"),]),]],
["concave_shield_green_2", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.00)|hit_points(450)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_green_2"),]),]],
["concave_shield_green_small_1", "Small Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.50)|hit_points(400)|body_armor(14)|spd_rtng(91)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_green_1"),]),]],
["concave_shield_green_small_2", "Small Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.50)|hit_points(400)|body_armor(14)|spd_rtng(91)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_green_2"),]),]],

["concave_shield_gray_1", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.00)|hit_points(450)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_gray_1"),]),]],
["concave_shield_gray_2", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.00)|hit_points(450)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_gray_2"),]),]],
["concave_shield_gray_small_1", "Small Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.50)|hit_points(400)|body_armor(14)|spd_rtng(91)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_gray_1"),]),]],
["concave_shield_gray_small_2", "Small Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.50)|hit_points(400)|body_armor(14)|spd_rtng(91)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_gray_2"),]),]],

["concave_shield_orange_1", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.00)|hit_points(450)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_orange_1"),]),]],
["concave_shield_orange_small_1", "Small Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.50)|hit_points(400)|body_armor(14)|spd_rtng(91)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_orange_1"),]),]],

["concave_shield_yellow_1", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.00)|hit_points(450)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_yellow_1"),]),]],
["concave_shield_yellow_small_1", "Small Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.50)|hit_points(400)|body_armor(14)|spd_rtng(91)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_yellow_1"),]),]],

["concave_shield_white_1", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(3.00)|hit_points(450)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_white_1"),]),]],
["concave_shield_white_small_1", "Small Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 395 , weight(2.50)|hit_points(400)|body_armor(14)|spd_rtng(91)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_white_1"),]),]],

#Germanic 
["concave_shield_germanic_1", "Round Shield", [("concave_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_1"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_2", "Round Shield", [("concave_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_2"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_3", "Round Shield", [("concave_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_3"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_4", "Round Shield", [("concave_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_4"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_5", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_5"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_6", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_6"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_7", "Round Shield", [("concave_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_7"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_8", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_8"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_9", "Round Shield", [("concave_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_9"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_10", "Round Shield", [("concave_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_10"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_11", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_11"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_12", "Round Shield", [("concave_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_12"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_13", "Round Shield", [("concave_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_13"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_14", "Round Shield", [("concave_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_14"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_15", "Round Shield", [("concave_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_15"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_16", "Round Shield", [("concave_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_16"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_17", "Round Shield", [("concave_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_17"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_18", "Round Shield", [("concave_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_18"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_19", "Round Shield", [("concave_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_19"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_20", "Round Shield", [("concave_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_20"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_21", "Round Shield", [("concave_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_21"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_22", "Round Shield", [("concave_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_22"),]),], culture_germanic+culture_gothic ],

["concave_shield_germanic_small_1", "Round Shield", [("concave_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_1"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_small_2", "Round Shield", [("concave_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_2"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_small_3", "Round Shield", [("concave_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_3"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_small_4", "Round Shield", [("concave_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_4"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_small_5", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_5"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_small_6", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_6"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_small_7", "Round Shield", [("concave_shield_small_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_7"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_small_8", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_8"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_small_9", "Round Shield", [("concave_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_9"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_small_10", "Round Shield", [("concave_shield_small_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_10"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_small_11", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_11"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_small_12", "Round Shield", [("concave_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_12"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_small_13", "Round Shield", [("concave_shield_small_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_13"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_small_14", "Round Shield", [("concave_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_14"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_small_15", "Round Shield", [("concave_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_15"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_small_16", "Round Shield", [("concave_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_16"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_small_17", "Round Shield", [("concave_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_17"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_small_18", "Round Shield", [("concave_shield_small_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_18"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_small_19", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_19"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_small_20", "Round Shield", [("concave_shield_small_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_20"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_small_21", "Round Shield", [("concave_shield_small_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_21"),]),], culture_germanic+culture_gothic ],
["concave_shield_germanic_small_22", "Round Shield", [("concave_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_germanic_22"),]),], culture_germanic+culture_gothic ],

#Romans
["concave_shield_roman_1", "Round Shield", [("concave_shield_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(4)|hit_points(500)|body_armor(13)|spd_rtng(87)|shield_width(47),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_1"),]),], culture_roman ], #limitanei
["concave_shield_roman_2", "Round Shield", [("concave_shield_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(4)|hit_points(500)|body_armor(13)|spd_rtng(87)|shield_width(47),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_2"),]),], culture_roman ], #limitanei
["concave_shield_roman_3", "Round Shield", [("concave_shield_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(4)|hit_points(500)|body_armor(13)|spd_rtng(87)|shield_width(47),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_3"),]),], culture_roman ], #limitanei
["concave_shield_roman_4", "Round Shield", [("concave_shield_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(4)|hit_points(500)|body_armor(13)|spd_rtng(87)|shield_width(47),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_4"),]),], culture_roman ], #limitanei
["concave_shield_roman_5", "Round Shield", [("concave_shield_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(4)|hit_points(500)|body_armor(13)|spd_rtng(87)|shield_width(47),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_5"),]),], culture_roman ], #limitanei
["concave_shield_roman_6", "Round Shield", [("concave_shield_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(4)|hit_points(500)|body_armor(13)|spd_rtng(87)|shield_width(47),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_6"),]),], culture_roman ], #limitanei
["concave_shield_roman_7", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_7"),]),], culture_roman ], #scutarii
["concave_shield_roman_8", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_8"),]),], culture_roman ], #scutarii
["concave_shield_roman_9", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_9"),]),], culture_roman ], #promoti
["concave_shield_roman_10", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_10"),]),], culture_roman ], #promoti
["concave_shield_roman_11", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_11"),]),], culture_roman ], #dalmatae
["concave_shield_roman_12", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_12"),]),], culture_roman ], #dalmatae
["concave_shield_roman_13", "Round Shield", [("concave_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_13"),]),], culture_roman ], #comites alani
["concave_shield_roman_14", "Round Shield", [("concave_shield_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(4)|hit_points(500)|body_armor(13)|spd_rtng(87)|shield_width(47),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_14"),]),], culture_roman ], #Lanciarii seniores
["concave_shield_roman_15", "Round Shield", [("concave_shield_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(4)|hit_points(500)|body_armor(13)|spd_rtng(87)|shield_width(47),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_15"),]),], culture_roman ], #Lanciarii iuniores
["concave_shield_roman_16", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_16"),]),], culture_roman ], #Equites Prima gallia
["concave_shield_roman_17", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_17"),]),], culture_roman ], #Equites Batavi seniores
["concave_shield_roman_18", "Round Shield", [("concave_shield_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_18"),]),], culture_roman ], #Tungri
["concave_shield_roman_19", "Round Shield", [("concave_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(4)|hit_points(500)|body_armor(13)|spd_rtng(87)|shield_width(47),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_19"),]),], culture_roman ],
["concave_shield_roman_20", "Round Shield", [("concave_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(3.5)|hit_points(500)|body_armor(12)|spd_rtng(88)|shield_width(42),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_20"),]),], culture_roman ],
["concave_shield_roman_21", "Round Shield", [("concave_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 500 , weight(2.5)|hit_points(480)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_21"),]),], [fac_culture_empire] ], #Schola scutariorum secunda - WRE
["concave_shield_roman_22", "Round Shield", [("concave_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 500 , weight(2.5)|hit_points(480)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_22"),]),], [fac_culture_empire] ], #Schola scutariorum secunda - ERE
["concave_shield_roman_23", "Round Shield", [("concave_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 500 , weight(2.5)|hit_points(480)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_23"),]),], [fac_culture_empire] ], #Schola gentilium seniorum - WRE
["concave_shield_roman_24", "Round Shield", [("concave_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 500 , weight(2.5)|hit_points(480)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_24"),]),], [fac_culture_empire] ], #Schola gentilium seniorum - ERE
["concave_shield_roman_25", "Round Shield", [("concave_shield_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 500 , weight(4)|hit_points(500)|body_armor(13)|spd_rtng(87)|shield_width(47),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_25"),]),], [fac_culture_empire] ], #was Felices Valentinianenses
["concave_shield_roman_26", "Round Shield", [("concave_shield_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 500 , weight(4)|hit_points(500)|body_armor(13)|spd_rtng(87)|shield_width(47),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_26"),]),], [fac_culture_empire] ], #Decima Gemina
#no 27 - used for unique shield
["concave_shield_roman_28", "Round Shield", [("concave_shield_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 500 , weight(4)|hit_points(500)|body_armor(13)|spd_rtng(87)|shield_width(47),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_28"),]),], [fac_culture_empire] ], #Huqoq mosaic

#for limitanei cav
["concave_shield_roman_small_1", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_1"),]),], culture_roman ],
["concave_shield_roman_small_2", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_2"),]),], culture_roman ],
["concave_shield_roman_small_3", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_3"),]),], culture_roman ],
["concave_shield_roman_small_4", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_4"),]),], culture_roman ],
["concave_shield_roman_small_5", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_5"),]),], culture_roman ],
["concave_shield_roman_small_6", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_6"),]),], culture_roman ],
["concave_shield_roman_small_25", "Round Shield", [("concave_shield_small_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_25"),]),], culture_roman ], #for romano mauri

["concave_shield_stablesiani", "Round Shield", [("concave_shield_4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(500)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_red_2"),]),], [fac_culture_empire] ],
["concave_shield_domestici", "Round Shield", [("concave_shield_4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(500)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_domestici"),]),], [fac_culture_empire] ],

#Mauri
["concave_shield_mauri_1", "Round Shield", [("concave_shield_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(4)|hit_points(500)|body_armor(13)|spd_rtng(87)|shield_width(47),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_mauri_1"),]),], [fac_culture_11] ],
["concave_shield_mauri_2", "Round Shield", [("concave_shield_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(4)|hit_points(500)|body_armor(13)|spd_rtng(87)|shield_width(47),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_mauri_2"),]),], [fac_culture_11] ],
["concave_shield_mauri_3", "Round Shield", [("concave_shield_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(4)|hit_points(500)|body_armor(13)|spd_rtng(87)|shield_width(47),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_mauri_3"),]),], [fac_culture_11] ],
["concave_shield_mauri_4", "Round Shield", [("concave_shield_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(4)|hit_points(500)|body_armor(13)|spd_rtng(87)|shield_width(47),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_mauri_4"),]),], [fac_culture_11] ],
["concave_shield_mauri_5", "Round Shield", [("concave_shield_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(4)|hit_points(500)|body_armor(13)|spd_rtng(87)|shield_width(47),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_mauri_5"),]),], [fac_culture_11] ],

["concave_shield_mauri_small_1", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_mauri_1"),]),], [fac_culture_11] ],
["concave_shield_mauri_small_2", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_mauri_2"),]),], [fac_culture_11] ],
["concave_shield_mauri_small_3", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_mauri_3"),]),], [fac_culture_11] ],
["concave_shield_mauri_small_4", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_mauri_4"),]),], [fac_culture_11] ],
["concave_shield_mauri_small_5", "Round Shield", [("concave_shield_small_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(2.5)|hit_points(450)|body_armor(14)|spd_rtng(90)|shield_width(37),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_mauri_5"),]),], [fac_culture_11] ],

#Britons
["concave_shield_briton_1", "Round Shield", [("concave_shield_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(4)|hit_points(500)|body_armor(13)|spd_rtng(87)|shield_width(47),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_britons_1"),]),], [fac_culture_empire,fac_culture_5] ],
["concave_shield_briton_2", "Round Shield", [("concave_shield_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(4)|hit_points(500)|body_armor(13)|spd_rtng(87)|shield_width(47),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_britons_2"),]),], [fac_culture_empire,fac_culture_5] ],
["concave_shield_briton_3", "Round Shield", [("concave_shield_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 450 , weight(4)|hit_points(500)|body_armor(13)|spd_rtng(87)|shield_width(47),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_britons_3"),]),], [fac_culture_empire,fac_culture_5] ],

["wicker_round_shield", "Wicker Round Shield", [("wicker_shield_small",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
395 , weight(3.5)|hit_points(300)|body_armor(8)|spd_rtng(92)|shield_width(35),imodbits_shield ],

["kerch_shield_1", "Hexagonal Shield", [("kerch_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.0)|hit_points(430)|body_armor(13)|spd_rtng(89)|shield_width(30)|shield_height(109),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_kerch_shield_1"),]),], [fac_culture_1,fac_culture_2] ],
["kerch_shield_2", "Hexagonal Shield", [("kerch_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.0)|hit_points(430)|body_armor(13)|spd_rtng(89)|shield_width(30)|shield_height(109),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_kerch_shield_2"),]),], [fac_culture_1,fac_culture_2] ],
["kerch_shield_3", "Hexagonal Shield", [("kerch_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.0)|hit_points(430)|body_armor(13)|spd_rtng(89)|shield_width(30)|shield_height(109),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_kerch_shield_3"),]),], [fac_culture_1,fac_culture_2] ],
["kerch_shield_4", "Hexagonal Shield", [("kerch_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.0)|hit_points(430)|body_armor(13)|spd_rtng(89)|shield_width(30)|shield_height(109),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_kerch_shield_4"),]),], [fac_culture_1,fac_culture_2] ],
["kerch_shield_5", "Hexagonal Shield", [("kerch_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.0)|hit_points(430)|body_armor(13)|spd_rtng(89)|shield_width(30)|shield_height(109),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_kerch_shield_5"),]),], [fac_culture_1,fac_culture_2] ],
["kerch_shield_6", "Hexagonal Shield", [("kerch_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.0)|hit_points(430)|body_armor(13)|spd_rtng(89)|shield_width(30)|shield_height(109),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_kerch_shield_6"),]),], [fac_culture_1,fac_culture_2] ],
["kerch_shield_7", "Hexagonal Shield", [("kerch_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.0)|hit_points(430)|body_armor(13)|spd_rtng(89)|shield_width(30)|shield_height(109),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_kerch_shield_7"),]),], [fac_culture_1,fac_culture_2] ],
["kerch_shield_8", "Hexagonal Shield", [("kerch_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.0)|hit_points(430)|body_armor(13)|spd_rtng(89)|shield_width(30)|shield_height(109),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_kerch_shield_8"),]),], [fac_culture_1,fac_culture_2] ],
["kerch_shield_9", "Hexagonal Shield", [("kerch_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.0)|hit_points(430)|body_armor(13)|spd_rtng(89)|shield_width(30)|shield_height(109),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_kerch_shield_9"),]),], [fac_culture_1,fac_culture_2] ],
["kerch_shield_10", "Hexagonal Shield", [("kerch_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.0)|hit_points(430)|body_armor(13)|spd_rtng(89)|shield_width(30)|shield_height(109),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_kerch_shield_10"),]),], [fac_culture_1,fac_culture_2] ],
["kerch_shield_11", "Hexagonal Shield", [("kerch_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.0)|hit_points(430)|body_armor(13)|spd_rtng(89)|shield_width(30)|shield_height(109),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_kerch_shield_11"),]),], [fac_culture_1,fac_culture_2] ],
["kerch_shield_12", "Hexagonal Shield", [("kerch_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.0)|hit_points(430)|body_armor(13)|spd_rtng(89)|shield_width(30)|shield_height(109),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_kerch_shield_12"),]),], [fac_culture_1,fac_culture_2] ],
["kerch_shield_13", "Hexagonal Shield", [("kerch_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.0)|hit_points(430)|body_armor(13)|spd_rtng(89)|shield_width(30)|shield_height(109),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_kerch_shield_13"),]),], [fac_culture_1,fac_culture_2] ],
["kerch_shield_14", "Hexagonal Shield", [("kerch_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.0)|hit_points(430)|body_armor(13)|spd_rtng(89)|shield_width(30)|shield_height(109),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_kerch_shield_14"),]),], [fac_culture_1,fac_culture_2] ],
["kerch_shield_15", "Hexagonal Shield", [("kerch_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.0)|hit_points(430)|body_armor(13)|spd_rtng(89)|shield_width(30)|shield_height(109),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_kerch_shield_15"),]),], [fac_culture_1,fac_culture_2] ],

["kerch_shield_wood", "Hexagonal Shield", [("kerch_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.0)|hit_points(430)|body_armor(13)|spd_rtng(89)|shield_width(30)|shield_height(109),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_kerch_shield_wood"),]),], [fac_culture_1,fac_culture_2] ],

["eastern_germanic_shield_1", "Germanic Shield", [("eastern_germanic_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.0)|hit_points(430)|body_armor(13)|spd_rtng(89)|shield_width(31)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_eastern_germanic_shield_1"),]),], [fac_culture_2] ],
["eastern_germanic_shield_2", "Germanic Shield", [("eastern_germanic_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.0)|hit_points(430)|body_armor(13)|spd_rtng(89)|shield_width(31)|shield_height(107),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_eastern_germanic_shield_2"),]),], [fac_culture_2] ],

["eastern_germanic_shield_3", "Germanic Shield", [("eastern_germanic_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.5)|hit_points(450)|body_armor(11)|spd_rtng(87)|shield_width(39)|shield_height(111),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_eastern_germanic_shield_3"),]),], [fac_culture_2] ],
["eastern_germanic_shield_4", "Germanic Shield", [("eastern_germanic_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(3.5)|hit_points(450)|body_armor(11)|spd_rtng(87)|shield_width(39)|shield_height(111),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_eastern_germanic_shield_4"),]),], [fac_culture_2] ],

["eastern_germanic_shield_5", "Germanic Shield", [("eastern_germanic_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(2.5)|hit_points(400)|body_armor(15)|spd_rtng(90)|shield_width(30)|shield_height(95),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_eastern_germanic_shield_5"),]),], [fac_culture_2] ],
["eastern_germanic_shield_6", "Germanic Shield", [("eastern_germanic_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(2.5)|hit_points(400)|body_armor(15)|spd_rtng(90)|shield_width(30)|shield_height(95),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_eastern_germanic_shield_6"),]),], [fac_culture_2] ],

["georgian_rectangular_shield_wood_1", "Wooden Rectangular Shield", [("georgian_rectangular_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 325 , weight(2.0)|hit_points(370)|body_armor(14)|spd_rtng(93)|shield_width(25)|shield_height(66),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_georgian_rectangular_shield_wood_1"),]),], culture_caucasian ],
["georgian_rectangular_shield_wood_2", "Wooden Rectangular Shield", [("georgian_rectangular_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 325 , weight(2.0)|hit_points(370)|body_armor(14)|spd_rtng(93)|shield_width(25)|shield_height(66),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_georgian_rectangular_shield_wood_2"),]),], culture_caucasian ],
["georgian_rectangular_shield_wood_3", "Wooden Rectangular Shield", [("georgian_rectangular_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 325 , weight(2.0)|hit_points(370)|body_armor(14)|spd_rtng(93)|shield_width(25)|shield_height(66),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_georgian_rectangular_shield_wood_3"),]),], culture_caucasian ],

["georgian_rectangular_shield_leather_1", "Wooden Rectangular Shield", [("georgian_rectangular_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 325 , weight(2.0)|hit_points(370)|body_armor(14)|spd_rtng(93)|shield_width(25)|shield_height(66),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_georgian_rectangular_shield_leather_1"),]),], culture_caucasian ],
["georgian_rectangular_shield_leather_2", "Wooden Rectangular Shield", [("georgian_rectangular_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 325 , weight(2.0)|hit_points(370)|body_armor(14)|spd_rtng(93)|shield_width(25)|shield_height(66),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_georgian_rectangular_shield_leather_2"),]),], culture_caucasian ],
["georgian_rectangular_shield_leather_3", "Wooden Rectangular Shield", [("georgian_rectangular_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 325 , weight(2.0)|hit_points(370)|body_armor(14)|spd_rtng(93)|shield_width(25)|shield_height(66),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_georgian_rectangular_shield_leather_3"),]),], culture_caucasian ],

["balt_shield_wood_1", "Board Shield", [("baltic_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(2.5)|abundance(10)|hit_points(410)|body_armor(14)|spd_rtng(90)|shield_width(25)|shield_height(113),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_balt_shields_1_wood"),]),],  ],
["balt_shield_wood_2", "Board Shield", [("baltic_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(2.0)|abundance(10)|hit_points(400)|body_armor(15)|spd_rtng(91)|shield_width(27)|shield_height(81),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_balt_shields_1_wood"),]),],  ],

["balt_shield_1_white", "Board Shield", [("baltic_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(2.5)|abundance(10)|hit_points(410)|body_armor(14)|spd_rtng(90)|shield_width(25)|shield_height(113),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_balt_shields_white_1"),]),],  ],
["balt_shield_2_white", "Board Shield", [("baltic_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(2.0)|abundance(10)|hit_points(400)|body_armor(15)|spd_rtng(91)|shield_width(27)|shield_height(81),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_balt_shields_white_1"),]),],  ],

["balt_shield_1_red", "Board Shield", [("baltic_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(2.5)|abundance(10)|hit_points(410)|body_armor(14)|spd_rtng(90)|shield_width(25)|shield_height(113),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_balt_shields_red_1"),]),],  ],
["balt_shield_2_red", "Board Shield", [("baltic_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(2.0)|abundance(10)|hit_points(400)|body_armor(15)|spd_rtng(91)|shield_width(27)|shield_height(81),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_balt_shields_red_1"),]),],  ],
["balt_shield_1_green", "Board Shield", [("baltic_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(2.5)|abundance(10)|hit_points(410)|body_armor(14)|spd_rtng(90)|shield_width(25)|shield_height(113),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_balt_shields_green_1"),]),],  ],
["balt_shield_2_green", "Board Shield", [("baltic_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(2.0)|abundance(10)|hit_points(400)|body_armor(15)|spd_rtng(91)|shield_width(27)|shield_height(81),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_balt_shields_green_1"),]),],  ],
["balt_shield_1_blue", "Board Shield", [("baltic_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(2.5)|abundance(10)|hit_points(410)|body_armor(14)|spd_rtng(90)|shield_width(25)|shield_height(113),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_balt_shields_blue_1"),]),],  ],
["balt_shield_2_blue", "Board Shield", [("baltic_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 425 , weight(2.0)|abundance(10)|hit_points(400)|body_armor(15)|spd_rtng(91)|shield_width(27)|shield_height(81),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_balt_shields_blue_1"),]),],  ],

["vae_cuadrado_3", "Square Shield", [("vae_cuadrado_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(2.5)|hit_points(280)|body_armor(7)|spd_rtng(95)|shield_width(20)|shield_height(40)|difficulty(1),imodbits_shield,
[], culture_celtic],
["vae_cuadrado_4", "Square Shield", [("vae_cuadrado_4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(2.5)|hit_points(280)|body_armor(7)|spd_rtng(95)|shield_width(20)|shield_height(40)|difficulty(1),imodbits_shield,
[], culture_celtic],
["vae_cuadrado_21", "Square Shield", [("vae_cuadrado_21",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(2.5)|hit_points(280)|body_armor(7)|spd_rtng(95)|shield_width(20)|shield_height(40)|difficulty(1),imodbits_shield,
[], culture_celtic],
["vae_cuadrado_27", "Square Shield", [("vae_cuadrado_27",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(2.5)|hit_points(280)|body_armor(7)|spd_rtng(95)|shield_width(20)|shield_height(40)|difficulty(1),imodbits_shield,
[], culture_celtic],
["pictish_square_shield", "Square Shield", [("pictish_square_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(2.5)|hit_points(280)|body_armor(7)|spd_rtng(95)|shield_width(20)|shield_height(40)|difficulty(1),imodbits_shield,
[], culture_celtic],

["vae_pictish_rectangle_1", "Rectangular Shield", [("vae_pictish_rectangle_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(1)|hit_points(260)|body_armor(8)|spd_rtng(101)|shield_width(20)|difficulty(0),imodbits_shield,
[], [fac_culture_5]],
["vae_pictish_rectangle_2", "Rectangular Shield", [("vae_pictish_rectangle_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(1)|hit_points(260)|body_armor(8)|spd_rtng(101)|shield_width(20)|difficulty(0),imodbits_shield,
[], [fac_culture_5]],
["vae_pictish_rectangle_3", "Rectangular Shield", [("vae_pictish_rectangle_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(1)|hit_points(260)|body_armor(8)|spd_rtng(101)|shield_width(20)|difficulty(0),imodbits_shield,
[], [fac_culture_5]],
["vae_pictish_rectangle_4", "Rectangular Shield", [("vae_pictish_rectangle_4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(1)|hit_points(260)|body_armor(8)|spd_rtng(101)|shield_width(20)|difficulty(0),imodbits_shield,
[], [fac_culture_5]],
["vae_pictish_rectangle_5", "Rectangular Shield", [("vae_pictish_rectangle_5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(1)|hit_points(260)|body_armor(8)|spd_rtng(101)|shield_width(20)|difficulty(0),imodbits_shield,
[], [fac_culture_5]],
["vae_pictish_rectangle_6", "Rectangular Shield", [("vae_pictish_rectangle_6",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(1)|hit_points(260)|body_armor(8)|spd_rtng(101)|shield_width(20)|difficulty(0),imodbits_shield,
[], [fac_culture_5]],
["vae_pictish_rectangle_7", "Rectangular Shield", [("vae_pictish_rectangle_7",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(1)|hit_points(260)|body_armor(8)|spd_rtng(101)|shield_width(20)|difficulty(0),imodbits_shield,
[], [fac_culture_5]],
["vae_pictish_rectangle_8", "Rectangular Shield", [("vae_pictish_rectangle_8",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(1)|hit_points(260)|body_armor(8)|spd_rtng(101)|shield_width(20)|difficulty(0),imodbits_shield,
[], [fac_culture_5]],
["vae_pictish_rectangle_9", "Rectangular Shield", [("vae_pictish_rectangle_9",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(1)|hit_points(260)|body_armor(8)|spd_rtng(101)|shield_width(20)|difficulty(0),imodbits_shield,
[], [fac_culture_5]],
["vae_pictish_rectangle_10", "Rectangular Shield", [("vae_pictish_rectangle_10",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(1)|hit_points(260)|body_armor(8)|spd_rtng(101)|shield_width(20)|difficulty(0),imodbits_shield,
[], [fac_culture_5]],
["vae_pictish_rectangle_11", "Rectangular Shield", [("vae_pictish_rectangle_11",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(1)|hit_points(260)|body_armor(8)|spd_rtng(101)|shield_width(20)|difficulty(0),imodbits_shield,
[], [fac_culture_5]],
["vae_pictish_rectangle_12", "Rectangular Shield", [("vae_pictish_rectangle_12",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(1)|hit_points(260)|body_armor(8)|spd_rtng(101)|shield_width(20)|difficulty(0),imodbits_shield,
[], [fac_culture_5]],
["vae_pictish_rectangle_13", "Rectangular Shield", [("vae_pictish_rectangle_13",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(1)|hit_points(260)|body_armor(8)|spd_rtng(101)|shield_width(20)|difficulty(0),imodbits_shield,
[], [fac_culture_5]],
["vae_pictish_rectangle_14", "Rectangular Shield", [("vae_pictish_rectangle_14",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(1)|hit_points(260)|body_armor(8)|spd_rtng(101)|shield_width(20)|difficulty(0),imodbits_shield,
[], [fac_culture_5]],
["vae_pictish_rectangle_15", "Rectangular Shield", [("vae_pictish_rectangle_15",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(1)|hit_points(260)|body_armor(8)|spd_rtng(101)|shield_width(20)|difficulty(0),imodbits_shield,
[], [fac_culture_5]],
["vae_pictish_rectangle_16", "Rectangular Shield", [("vae_pictish_rectangle_16",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  350 , weight(1)|hit_points(260)|body_armor(8)|spd_rtng(101)|shield_width(20)|difficulty(0),imodbits_shield,
[], [fac_culture_5]],

["simple_shield_1", "Small Wicker Shield", [("ad_small_shield_5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
100 , weight(1.5)|hit_points(180)|body_armor(7)|spd_rtng(106)|shield_width(20),imodbits_shield],
["simple_shield_2", "Small Wicker Shield", [("ad_small_shield_6",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
100 , weight(1.5)|hit_points(180)|body_armor(7)|spd_rtng(106)|shield_width(20),imodbits_shield],
["simple_shield_3", "Small Leather Shield", [("ad_small_shield_7",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
100 , weight(1.5)|hit_points(180)|body_armor(7)|spd_rtng(106)|shield_width(20),imodbits_shield],
["simple_shield_4", "Small Leather Shield", [("ad_small_shield_8",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
100 , weight(1.5)|hit_points(180)|body_armor(7)|spd_rtng(106)|shield_width(20),imodbits_shield],

["ad_small_shield_1", "Small Round Shield", [("ad_small_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
200 , weight(1.5)|hit_points(200)|body_armor(7)|spd_rtng(106)|shield_width(20),imodbits_shield],
["ad_small_shield_2", "Small Round Shield", [("ad_small_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
200 , weight(1.5)|hit_points(200)|body_armor(7)|spd_rtng(106)|shield_width(20),imodbits_shield],
["ad_small_shield_3", "Small Round Shield", [("ad_small_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
200 , weight(1.5)|hit_points(200)|body_armor(7)|spd_rtng(106)|shield_width(20),imodbits_shield],
["ad_small_shield_4", "Small Round Shield", [("ad_small_shield_4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
200 , weight(1.5)|hit_points(200)|body_armor(7)|spd_rtng(106)|shield_width(20),imodbits_shield],

["nubian_shield_1", "Hide Round Shield", [("nubian_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  395 , weight(2.00)|hit_points(400)|body_armor(10)|spd_rtng(90)|shield_width(20),imodbits_shield, [], culture_african],
["nubian_shield_2", "Hide Shield", [("nubian_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  395 , weight(2.5)|hit_points(420)|body_armor(14)|spd_rtng(88)|shield_height(40)|shield_width(25),imodbits_shield, [], culture_african],

 #RANGED


#TODO:

#TODO:
#TODO: Heavy throwing Spear

["lyre",         "Lyre", [("lyre",0)], itp_type_shield|itp_wooden_parry|itp_civilian|itp_two_handed, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],
["lute",         "Lute", [("lute",0)], itp_type_shield|itp_wooden_parry|itp_civilian|itp_secondary, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],

##["short_sword", "Short Sword",
## [("sword_norman",0),("sword_norman_scabbard", ixmesh_carry),("sword_norman_rusty",imodbit_rusty),("sword_norman_rusty_scabbard", ixmesh_carry|imodbit_rusty)],
## itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 183 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(75)|swing_damage(25 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],

#excubitor equipment
["excubitor_mail", "Excubitor Mail", [("excubitor_mail",0)], itp_civilian|itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,7000 , weight(17)|abundance(1)|head_armor(0)|body_armor(50)|leg_armor(13)|difficulty(12) ,imodbits_scale, [], [fac_culture_empire] ],
["excubitor_boots", "Cothurni", [("excubitor_boots",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature ,0, 600 , weight(1.5)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth, [], [fac_culture_empire] ],
["excubitor_shield_1", "Excubitor Shield", [("excubitor_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  1000 , weight(3.55)|abundance(5)|hit_points(520)|body_armor(16)|spd_rtng(87)|shield_width(42),imodbits_shield, [], [fac_culture_empire] ],
["excubitor_spear","Gilded Contus", [("excubitor_spear",0)], itp_type_polearm|itp_merchandise|itp_offset_lance|itp_primary|itp_secondary|itp_no_blur|itp_wooden_parry, itc_spear_upstab, 860 , weight(2.35)|abundance(2)|difficulty(6)|spd_rtng(96) | weapon_length(134)|swing_damage(19 , blunt) | thrust_damage(31 ,  pierce),imodbits_polearm ],
["roman_javelin", "Javelins", [("roman_jav",0)], itp_type_thrown|itp_merchandise|itp_primary,itcf_throw_javelin|itp_bonus_against_shield,500, weight(2.5)|difficulty(2)|spd_rtng(92) | shoot_speed(30) | thrust_damage(34 ,  pierce)|max_ammo(2)|weapon_length(75),imodbits_thrown ],

#now used for rare indian mercs
["strange_armor",  "Gandharan Padded Armor", [("gandhara_padded",0)], itp_type_body_armor|itp_covers_legs, 0, 1259 , weight(5)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(13)|difficulty(1) ,imodbits_cloth ],

#Heraldic Banners + Standards
["flag_pole_1","Battle Standard", [("roman_spear_banner",0)],itp_type_polearm|itp_cant_use_on_horseback|itp_two_handed|itp_primary|itp_wooden_parry|itp_wooden_attack,itc_pike_upstab,700, 
 weight(1.5)|spd_rtng(84) |abundance(5)| weapon_length(155)|swing_damage(25,blunt) | thrust_damage(15,blunt),imodbits_polearm,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_flag_pole_new", ":agent_no", ":troop_no")])]],

["draco", "Draco Standard", [("draco",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_wooden_parry|itp_wooden_attack,itc_staff,700, weight(2.5)|spd_rtng(80) |abundance(5)| weapon_length(155)|swing_damage(26,blunt) | thrust_damage(18,blunt),imodbits_polearm ],

 #horn used by hornmen
["horn","Horn",[("horn_new",0)],itp_type_one_handed_wpn|itp_primary|itp_no_parry,0,1000,weight(2.0),0], #itcf_carry_revolver_right

##diplomacy begin
["dplmc_coat_of_plates_red_constable", "Constable Mail", [("mid_generic_mail_23",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], []],
##diplomacy end
#SB : replace items_end to fit invasion items

#["sarranid_plate_mail_2", "Sarranid Plated Mail", [("sar_rough_mail_full_metalplates",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# 1740 , weight(22)|abundance(60)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(7) ,imodbits_armor ],

["dark_bag_1", "Wig", [("dark_bag_wig",0)], itp_unique|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,1, weight(0)|abundance(0)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["dark_bag_2", "Wig", [("black_long-medium_bag_wig",0)], itp_unique|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,1, weight(0)|abundance(0)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["dark_bag_3", "Wig", [("dark_bag_hair_wig",0)], itp_unique|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,1, weight(0)|abundance(0)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],

["wooden_shield", "Wooden Shield", [("round_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["round_shield_b", "Round Shield", [("round_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  95 , weight(2)|hit_points(300)|body_armor(6)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["nordic_shield", "Nordic Shield", [("round_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  95 , weight(2)|hit_points(440)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["fur_covered_shield",  "Fur Covered Shield", [("round_shield_1", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  227 , weight(3.5)|hit_points(600)|body_armor(1)|spd_rtng(76)|shield_width(35)|shield_height(81),imodbits_cloth],
["nomad_shield", "Leather Shield", [("round_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  12 , weight(2)|hit_points(260)|body_armor(6)|spd_rtng(110)|shield_width(30),imodbits_shield ],
["leather_covered_round_shield", "Leather Covered Round Shield", [("round_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  80 , weight(2.5)|hit_points(310)|body_armor(8)|spd_rtng(96)|shield_width(40),imodbits_shield ],
["hide_covered_round_shield", "Hide Covered Round Shield", [("round_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  40 , weight(2)|hit_points(260)|body_armor(3)|spd_rtng(100)|shield_width(40),imodbits_shield ],
["nordic_shield_a", "Shield", [("round_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  95 , weight(2)|hit_points(440)|body_armor(6)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["nordic_shield_b", "Shield", [("round_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  95 , weight(2)|hit_points(440)|body_armor(6)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["nordic_shield_c", "Shield", [("round_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  95 , weight(2)|hit_points(440)|body_armor(6)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["nordic_shield_d", "Shield", [("round_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  95 , weight(2)|hit_points(440)|body_armor(6)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["shield_heater_c", "Round Shield", [("round_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  395 , weight(2.75)|hit_points(400)|body_armor(12)|spd_rtng(88)|shield_width(80),imodbits_shield, [], culture_gothic ],
["norman_shield_1", "Round Shield", [("round_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  395 , weight(3.00)|hit_points(400)|body_armor(12)|spd_rtng(88)|shield_width(80),imodbits_shield, [], culture_gothic ],
["norman_shield_2", "Round Shield", [("round_shield_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  395 , weight(2.75)|hit_points(400)|body_armor(12)|spd_rtng(88)|shield_width(80),imodbits_shield, [], culture_gothic ],
["norman_shield_3", "Round Shield", [("round_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  395 , weight(3.00)|hit_points(400)|body_armor(12)|spd_rtng(88)|shield_width(80),imodbits_shield, [], culture_gothic ],
["norman_shield_4", "Round Shield", [("round_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  395 , weight(2.75)|hit_points(400)|body_armor(12)|spd_rtng(88)|shield_width(80),imodbits_shield, [], culture_gothic ],
["norman_shield_5", "Round Shield", [("round_shield_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  395 , weight(3.00)|hit_points(400)|body_armor(12)|spd_rtng(88)|shield_width(80),imodbits_shield, [], culture_gothic ],
["norman_shield_6", "Round Shield", [("round_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  395 , weight(2.75)|hit_points(400)|body_armor(12)|spd_rtng(88)|shield_width(80),imodbits_shield, [], culture_gothic ],
["strange_boots",  "Strange Boots", [("samurai_boots",0)], itp_type_foot_armor|itp_attach_armature,0, 465 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(0) ,imodbits_cloth ],
["strange_helmet", "Strange Helmet", [("samurai_helmet",0)], itp_type_head_armor   ,0, 824 , weight(2)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["strange_sword", "Strange Sword", [("katana",0),("katana_scabbard",ixmesh_carry)], itp_type_two_handed_wpn| itp_primary, itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn, 679 , weight(2.0)|difficulty(9)|spd_rtng(108) | weapon_length(95)|swing_damage(32 , cut) | thrust_damage(18 ,  pierce),imodbits_sword ],
["strange_great_sword",  "Strange Great Sword", [("no_dachi",0),("no_dachi_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back|itcf_show_holster_when_drawn, 920 , weight(3.5)|difficulty(11)|spd_rtng(92) | weapon_length(125)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["strange_short_sword", "Strange Short Sword", [("wakizashi",0),("wakizashi_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_wakizashi|itcf_show_holster_when_drawn, 321 , weight(1.25)|difficulty(0)|spd_rtng(108) | weapon_length(65)|swing_damage(25 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
["court_dress", "Court Dress", [("court_dress",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["rich_outfit", "Rich Outfit", [("merchant_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["khergit_guard_armor", "Lamellar Guard Armor", [("lamellar_armor_a",0)], itp_type_body_armor|itp_covers_legs   ,0,
3048 , weight(25)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(18)|difficulty(0) ,imodbits_armor ],
["felt_steppe_cap", "Tundra Cap", [("noel_helmet",0)], itp_type_head_armor   ,0, 237 , weight(2)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["khergit_helmet", "Nomad's Helmet", [("noel_helmet",0)], itp_type_head_armor   ,0, 361 , weight(2)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["khergit_guard_boots",  "Lamellar Guard Boots", [("lamellar_boots_a",0)], itp_type_foot_armor | itp_attach_armature,0, 254 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],

["keys", "Ring of Keys", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
240, weight(5)|spd_rtng(98) | swing_damage(29,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown ],
["bride_dress", "Bride Dress", [("bride_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["bride_crown", "Crown of Flowers", [("bride_crown",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bride_shoes", "Bride Shoes", [("bride_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

["practice_bow_2","Practice Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_bow ],
["practice_arrows_2","Practice Arrows", [("arena_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile],

["heraldic_mail_with_surcoat_for_tableau", "{!}Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_type_body_armor |itp_covers_legs ,0,
 1, weight(22)|abundance(100)|head_armor(0)|body_armor(1)|leg_armor(1),imodbits_armor,
 [heraldic("tableau_heraldic_armor_a")]],
["mail_boots_for_tableau", "Mail Boots", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1, weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
#NEW ITEMS
#for africans
["nubian_sandals", "Sandals", [("nubian_sandals",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["cow_1","Cow", [("cow_mod_a",0)], 0, 0, #produces milk
 1400,abundance(40)|hit_points(60)|body_armor(6)|horse_speed(18)|horse_maneuver(26)|horse_charge(12)|horse_scale(91),imodbits_horse_basic],

["items_end", "Items End", [("shield_round_a",0)], 0, 0, 1, 0, 0],

#animal walkers
["animal_donkey","Donkey", [("wild_donkey",0)], itp_type_animal|itp_disable_agent_sounds, 0, 10, abundance(10)|hit_points(30)|body_armor(5)|difficulty(11)|horse_speed(20)|horse_maneuver(100)|horse_charge(100),imodbits_none],
["animal_pig", "Pig", [("animal_pig",0)], itp_type_animal|itp_disable_agent_sounds, 0, 50, abundance(0)|hit_points(180)|body_armor(2)|difficulty(11)|horse_speed(20)|horse_maneuver(42)|horse_charge(1)|horse_scale(65), imodbits_none ],
["animal_sheep_a", "Sheep", [("sheep_mod_a",0)], itp_type_animal|itp_disable_agent_sounds, 0, 50, abundance(0)|hit_points(180)|body_armor(2)|difficulty(11)|horse_speed(20)|horse_maneuver(42)|horse_charge(1)|horse_scale(50), imodbits_none ],
["animal_sheep_b", "Sheep", [("sheep_mod_b",0)], itp_type_animal|itp_disable_agent_sounds, 0, 50, abundance(0)|hit_points(180)|body_armor(2)|difficulty(11)|horse_speed(20)|horse_maneuver(42)|horse_charge(1)|horse_scale(50), imodbits_none ],
["animal_cow", "Cow", [("cow_mod_a",0)], itp_type_animal|itp_disable_agent_sounds, 0, 300, abundance(0)|hit_points(300)|body_armor(8)|difficulty(11)|horse_speed(8)|horse_maneuver(42)|horse_charge(1)|horse_scale(100), imodbits_none ],
["animal_horse", "Horse", [("bareback_horse_1",0)], itp_type_animal, 0, 150, abundance(0)|hit_points(100)|body_armor(2)|difficulty(11)|horse_speed(40)|horse_maneuver(42)|horse_charge(1)|horse_scale(100), imodbits_none ],
["animal_mule", "Mule", [("mule",0)], itp_type_animal, 0, 150, abundance(0)|hit_points(100)|body_armor(2)|difficulty(11)|horse_speed(40)|horse_maneuver(42)|horse_charge(1)|horse_scale(100), imodbits_none ],
["animal_chicken", "Chicken", [("animal_chicken",0)], itp_type_animal|itp_disable_agent_sounds, 0, 50, abundance(0)|hit_points(50)|body_armor(0)|difficulty(11)|horse_speed(8)|horse_maneuver(42)|horse_charge(1)|horse_scale(15), imodbits_none ],
#unique armors/weapons so that cheat menu losers won't be able to get them/find them without actually doing the quests
#starting with weapons
["sword_of_mars", "Sword of Mars", [("sword_of_mars",0),("sword_of_mars_scabbard", ixmesh_carry)], itp_unique|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 9850 , weight(1.5)|difficulty(0)|spd_rtng(90) | weapon_length(91)|swing_damage(36 , cut)| thrust_damage(22 ,  pierce),imodbits_sword_high ],

["lance_of_longiunus","Lancea Longini", [("roman_spear_2",0)], itp_unique|itp_type_polearm|itp_offset_lance|itp_primary|itp_wooden_parry, itc_spear_upstab|itcf_carry_spear, 9000 , weight(1.5)|abundance(0)|difficulty(8)|spd_rtng(98) | weapon_length(158)|swing_damage(18 , cut) | thrust_damage(35 ,  pierce),imodbits_polearm],
["axe_of_zamb",  "Axe of Zamb", [("vikingaxeb",0)], itp_unique|itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_wooden_parry|itp_unbalanced, itc_nodachi|itp_can_penetrate_shield|itcf_carry_axe_back, 1000 , weight(5.5)|difficulty(14)|spd_rtng(80) | weapon_length(82)|swing_damage(48 , cut) | thrust_damage(0 ,  blunt),imodbits_axe ],
["caesar_gladius", "Crocea Mors", [("roman_gladius_1",0),("roman_gladius_1_scabbard", ixmesh_carry)], itp_unique|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 9850 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(68)|swing_damage(36 , cut)| thrust_damage(30 ,  pierce),imodbits_sword_high ],
["excalibur", "Excalibur", [("Kirkburn",0),("Kirkburn_scab", ixmesh_carry)], itp_unique|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,9000 , weight(1.75)|difficulty(0)|spd_rtng(89) | weapon_length(94)|swing_damage(36 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ],
["ranja","Ranja", [("runic_spear_2",0)], itp_unique|itp_type_polearm|itp_offset_lance|itp_primary|itp_wooden_parry, itc_spear_upstab|itcf_carry_spear, 5000 , weight(1.5)|abundance(0)|difficulty(8)|spd_rtng(99) | weapon_length(150)|swing_damage(22 , blunt) | thrust_damage(34 ,  pierce),imodbits_polearm],
["danish_king_mace", "Gramr's Mace", [("danish_king_mace",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 5000 , weight(3.5)|difficulty(7)|spd_rtng(86)|weapon_length(55)|swing_damage(34 , blunt)|thrust_damage(0 ,  pierce),imodbits_mace ],
["st_martin_axe", "Axe of St. Martin", [("st_martin_axe",0)], itp_unique|itp_can_knock_down|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 5000, weight(2)|difficulty(8)|spd_rtng(93)|weapon_length(55)|swing_damage(33 , pierce)|thrust_damage(0 ,  pierce),imodbits_axe ],

["donars_club", "Donar's Club", [("donars_club",0)], itp_unique|itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_unbalanced|itp_can_penetrate_shield|itp_crush_through|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
9600 , weight(5.5)|difficulty(16)|spd_rtng(82) | weapon_length(85)|swing_damage(38 , blunt) | thrust_damage(0 ,  pierce),imodbits_axe ],

["vidigoia_spear", "Vidigoia's Spear", [("runic_spear_1_ranged",0)], itp_type_thrown|itp_can_penetrate_shield|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itp_bonus_against_shield,
7000 , weight(1.5)|difficulty(5)|spd_rtng(88) | shoot_speed(22) | thrust_damage(50 ,  pierce)|max_ammo(1)|weapon_length(120)|accuracy(90),imodbits_polearm ],
["vidigoia_spear_melee", "Vidigoia's Spear", [("runic_spear_1",0)],itp_type_polearm|itp_can_penetrate_shield|itp_crush_through|itp_primary|itp_wooden_parry , itc_spear_upstab|itp_bonus_against_shield,
7000 , weight(1.5)|difficulty(8)|spd_rtng(96) | swing_damage(25, blunt) | thrust_damage(33 ,  pierce)|weapon_length(160),imodbits_polearm ],

["hunimund_axe", "Hunimund's Axe", [("bb_nordic_war_axe",0)], itp_unique|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee|itp_bonus_against_shield|itp_can_penetrate_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 3005 , weight(1.5)|difficulty(8)|spd_rtng(90) | weapon_length(75)|swing_damage(36 , cut) | thrust_damage(0 ,  pierce),imodbits_axe],
["hunimund_axe_alt", "Hunimund's Axe", [("bb_nordic_war_axe",0)], itp_unique|itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_penetrate_shield|itp_can_knock_down|itp_crush_through|itp_wooden_parry, itc_nodachi|itcf_carry_axe_left_hip,
 3005 , weight(1.5)|difficulty(8)|spd_rtng(86) | weapon_length(75)|swing_damage(42 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["attila_bow", "Bow of Attila", [("niya_bow_2",0),("niya_case_2", ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,9600 , weight(1.25)|difficulty(4)|spd_rtng(93) | shoot_speed(60) | thrust_damage(15 ,cut),imodbits_bow ], #unique item given to hunnic players who conquer apahdia as the huns

["old_practice_spatha", "Practice Spatha", [("old_practice_spatha",0)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip, #for gladiator quest
 100 , weight(2)|difficulty(0)|spd_rtng(88) | weapon_length(97)|swing_damage(22, blunt) | thrust_damage(18, blunt),imodbits_sword_high ],


#shields
["mithras_shield", "Mithrain Round Shield", [("mithras_shield",0)], itp_unique|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  9600 , weight(3.5)|hit_points(700)|body_armor(18)|spd_rtng(91)|shield_width(42),imodbits_shield ],
["aetius_shield", "Aetius's Shield", [("concave_shield_large",0)], itp_unique|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 5000 , weight(3.75)|hit_points(600)|body_armor(15)|spd_rtng(88)|shield_width(47),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_27"),]),], ],

["small_old_round_shield_1", "Small Round Shield", [("round_shield_small_4",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 400 , weight(2.0)|hit_points(380)|body_armor(12)|spd_rtng(92)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_1"),]),]],
["small_old_round_shield_2", "Small Round Shield", [("round_shield_small_4",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 400 , weight(2.0)|hit_points(380)|body_armor(12)|spd_rtng(92)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_3"),]),]],
["small_old_round_shield_3", "Small Round Shield", [("round_shield_small_4",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 400 , weight(2.0)|hit_points(380)|body_armor(12)|spd_rtng(92)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_8"),]),]],
["small_old_round_shield_4", "Small Round Shield", [("round_shield_small_4",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 400 , weight(2.0)|hit_points(380)|body_armor(12)|spd_rtng(92)|shield_width(35),imodbits_shield, [(ti_on_init_item,[(cur_item_set_material, "str_round_shields_roman_17"),]),]],


#armor
["lion_pelt", "Lion Pelt", [("lion_pelt",0),("lion_pelt_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_fit_to_head,0,3530, weight(2.5)|abundance(0)|head_armor(30)|body_armor(15)|leg_armor(0)|difficulty(2) ,imodbits_plate ],

["pilos_helmet", "Pilos", [("pilos_helmet",0)], itp_unique|itp_type_head_armor,0,300, weight(0)|abundance(0)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_plate],

["aurelian_scale_armor", "Aurelian's Squamata", [("aurelian_scale_armor",0)], itp_unique|itp_type_body_armor|itp_covers_legs ,0,9000 , weight(18)|abundance(0)|head_armor(0)|body_armor(56)|leg_armor(16)|difficulty(16) ,imodbits_plate ], #high difficulty to prevent early players from using off the bat

["unique_mail_armor", "Rich Mail Shirt", [("unique_mail_armor",0)], itp_unique|itp_type_body_armor |itp_covers_legs ,0,9000 , weight(14)|abundance(0)|head_armor(0)|body_armor(54)|leg_armor(15)|difficulty(8) ,imodbits_armor ],

["helmet_of_victory", "Ornate Ridge Helmet", [("victoria_intercisa",0),("victoria_intercisa_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature,0,7450, weight(1.75)|abundance(0)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],

["aurelian_helmet", "Aurelian's Helmet", [("aurelian_helmet",0),("aurelian_helmet_inv",ixmesh_inventory)], itp_unique|itp_type_head_armor|itp_attach_armature|itp_fit_to_head|itp_covers_beard,0,9850, weight(5.5)|abundance(0)|head_armor(56)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],

["richborough_helmet_1", "Refitted Antique Cavalry Helmet", [("richborough_helmet_1",0),("richborough_helmet_1_inv",ixmesh_inventory)], itp_unique|itp_type_head_armor|itp_attach_armature|itp_fit_to_head,0,8000, weight(2.0)|abundance(0)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["richborough_helmet_2", "Refitted Antique Cavalry Helmet", [("richborough_helmet_2",0),("richborough_helmet_2_inv",ixmesh_inventory)], itp_unique|itp_type_head_armor|itp_attach_armature|itp_fit_to_head,0,1250, weight(1.5)|abundance(0)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["florence_helmet_1", "Refitted Antique Helmet", [("florence_helmet_1",0),("florence_helmet_1_inv",ixmesh_inventory)], itp_unique|itp_type_head_armor|itp_attach_armature|itp_fit_to_head,0,1250 , weight(1.5)|abundance(0)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate ],

["old_gladiator_helmet_1", "Old Gladiator Helmet", [("old_gladiator_helmet_1",0),("old_gladiator_helmet_1_inv",ixmesh_inventory)],itp_attach_armature|itp_type_head_armor,0,2000 , weight(4.50)|abundance(0)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ], #quest related only!
["old_gladiator_helmet_2", "Old Gladiator Helmet", [("old_gladiator_helmet_2",0),("old_gladiator_helmet_2_inv",ixmesh_inventory)],itp_attach_armature|itp_type_head_armor,0,2000 , weight(4.50)|abundance(0)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],

#quest items
["book_roman_pagan_quest","Collection of the Works of Plato", [("book_f",0)], itp_type_book, 0, 1,weight(2)|abundance(100),imodbits_none], #cheap so the player hopefully doesn't sell it

["letter_roman_pagan_quest","Letter to Proclus", [("scroll",0)], itp_type_book, 0, 1,weight(2)|abundance(100),imodbits_none], #cheap so the player hopefully doesn't sell it

["mithras_relic","Relic", [("ritual_cup",0)], itp_unique|itp_type_goods, 0, 1,weight(2)|abundance(10),imodbits_none],

["maximian_statue","Statue of Maximian", [("quest_statue",0)], itp_unique|itp_type_goods, 0, 1,weight(2)|abundance(10),imodbits_none],

["scythian_bong","Scythian Bong", [("totally_not_temp_scythian_bong",0)], itp_unique|itp_type_goods, 0, 3000,weight(1)|abundance(0),imodbits_none],

["mithras_statue","Statue of Mithras", [("mithras_final",0)], itp_unique|itp_type_goods, 0, 10000,weight(50)|abundance(10),imodbits_none],

["nero_lyre","Nero's Lyre", [("lyre",0)], itp_unique|itp_type_shield|itp_wooden_parry|itp_civilian|itp_two_handed, itcf_carry_bow_back,  100 , weight(2.5)|hit_points(600)|body_armor(4)|spd_rtng(92)|weapon_length(90),imodbits_none ],

["nero_lyre_final","Nero's Lyre", [("lyre",0)], itp_unique|itp_type_goods, 0, 4000,weight(2.5)|abundance(0),imodbits_none],


["tavern_cup","Cup",[("dedal_kufelL",0)],itp_type_hand_armor,0, 1, weight(1.0)|abundance(1)|body_armor(0)|difficulty(0),imodbits_none],
["dedal_lutnia","Lyre",[("dedal_liraL",0)],	itp_type_hand_armor,0,0,weight(1),0],
["dedal_lira","Lyre",[("dedal_liraL",0)],		itp_type_hand_armor,0,0,weight(1),0],

["ccoop_new_items_end", "Items End", [("shield_round_a",0)], 0, 0, 1, 0, 0],
#INVASION MODE END
#invisible items
["empty_hands","empty_hands",[("dummy_object",0)],itp_type_hand_armor|itp_unique,0,130,weight(225)|body_armor(100)|difficulty(0),0],
["empty_legs","empty_legs",[("dummy_object",0)],itp_type_foot_armor|itp_unique,0,130,weight(225)|leg_armor(100)|difficulty(0),0],
["empty_head","empty head",[("dummy_object",0)],itp_type_head_armor|itp_unique|itp_covers_head,0,1,weight(250)|head_armor(100)|difficulty(0),0],
["empty_body","empty body",[("dummy_object",0)],itp_type_body_armor|itp_unique|itp_covers_legs,0,1,weight(250)|head_armor(100)|difficulty(0),0],
]
  
from copy import deepcopy

def modmerge(var_set):
  try:
    from modmerger_options import module_sys_info
    version = module_sys_info["version"]
  except:
    version = 1166 # version not specified.  assume latest warband or wfas at this time

  try:
    var_name_1 = "items"
    orig_items = var_set[var_name_1]
    
    add_item = deepcopy(orig_items)
    for i_item in range(1,len(add_item)):
      type = add_item[i_item][3] & 0x000000ff
      # if itp_type_one_handed_wpn <= type <= itp_type_polearm and add_item[i_item-1][3] & itp_next_item_as_melee == 0 and (get_thrust_damage(add_item[i_item][6]) % 256) > 0 and "tutorial" not in add_item[i_item][0] and "arena" not in add_item[i_item][0] and "practice" not in add_item[i_item][0] and "tpe" not in add_item[i_item][0]:
      if itp_type_one_handed_wpn <= type <= itp_type_polearm and (get_thrust_damage(add_item[i_item][6])&0xff) > 0 and "tutorial" not in add_item[i_item][0] and "arena" not in add_item[i_item][0] and "practice" not in add_item[i_item][0] and "tpe" not in add_item[i_item][0]:
        #Above checks that it is a weapon with thrust damage; also checks that it isn't a tournament-type weapon by checking the item ID (just to prevent not-used items)
        add_item[i_item][0] = 'noswing_'+add_item[i_item][0]                  #add noswing_ to the item's name
        add_item[i_item][6] = add_item[i_item][6] & ~(ibf_damage_mask << iwf_swing_damage_bits) #should set new item's swing damage to 0
        add_item[i_item][4] = add_item[i_item][4] & ~itcf_overswing_polearm  #remove itcf_ capabilties to prevent swinging without damage  
        add_item[i_item][4] = add_item[i_item][4] & ~itcf_slashright_polearm                     
        add_item[i_item][4] = add_item[i_item][4] & ~itcf_slashleft_polearm
        add_item[i_item][4] = add_item[i_item][4] & ~itcf_overswing_onehanded   
        add_item[i_item][4] = add_item[i_item][4] & ~itcf_slashright_onehanded                     
        add_item[i_item][4] = add_item[i_item][4] & ~itcf_slashleft_onehanded
        add_item[i_item][4] = add_item[i_item][4] & ~itcf_overswing_twohanded
        add_item[i_item][4] = add_item[i_item][4] & ~itcf_slashright_twohanded                     
        add_item[i_item][4] = add_item[i_item][4] & ~itcf_slashleft_twohanded
        if type == itp_type_polearm and add_item[i_item][3] & itp_two_handed == 0:
          add_item[i_item][4] = add_item[i_item][4] | itcf_thrust_onehanded  #so that the polearms use 'bent elbow' with shields, but normal without
        add_item[i_item][3] = add_item[i_item][3] & ~itp_merchandise
        orig_items.append(add_item[i_item])
    
  except KeyError:
    errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
    raise ValueError(errstring)