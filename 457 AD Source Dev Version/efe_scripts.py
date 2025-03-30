# -*- coding: cp1254 -*-
from header_common import *
from header_operations import *
from module_constants import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from header_map_icons import *
from ID_animations import *
from module_factions import dplmc_factions_begin, dplmc_factions_end, dplmc_non_generic_factions_begin
from ID_info_pages import *
from header_presentations import tf_left_align
from module_items import *

efe_scripts = [

("efe_init", [

(assign, "$efe_debug", on),
(try_begin),
  (eq, "$efe_debug", on),
  (display_message, "@[EFE - DEBUG] - DEBUG is on", efe_debug_hex),
(try_end),
(display_message, "@[EFE - DEBUG] - Running efe_init", efe_debug_hex),

]),

("cf_start_siege_debug_trigger", [(eq, "$efe_debug", on), (key_clicked, key_1),]),
("cf_start_normal_debug_trigger", [(eq, "$efe_debug", on),]),

# Starts a random siege on the world map
("cf_efe_start_siege_debug", [

(display_message, "@[EFE - DEBUG] - Pressed 1 key", efe_debug_hex),
(eq, "$efe_debug", on),
(display_message, "@[EFE - DEBUG] - Running efe_start_siege_debug", efe_debug_hex),
(store_random_in_range, ":kingdom", npc_kingdoms_begin, npc_kingdoms_end), # Get a random kingdom
(call_script, "script_cf_get_random_lord_party_including_king_with_faction", ":kingdom"), # Find a random lord party from that kingdom
(assign, ":sieger_lord", reg0), # save it

(call_script, "script_cf_faction_get_random_enemy_faction", ":kingdom"), # find one of its enemy factions
(assign, ":target_enemy_faction", reg0), # save it
(call_script, "script_cf_get_random_lord_including_king_with_faction", ":target_enemy_faction"), # find a random target enemy lord troop from the faction
(assign, ":besieged_lord", reg0), # save it

(call_script, "script_cf_select_random_walled_center_with_faction_and_owner_priority_no_siege", ":target_enemy_faction", ":besieged_lord"), # find a random center to siege with priority on that enemy lord
(assign, ":siege_target", reg0), # save it

(set_camera_follow_party, "p_main_party"),
(party_relocate_near_party, "p_main_party", ":siege_target", 0), # just so we know
(party_relocate_near_party, ":sieger_lord", ":siege_target", 1),
(call_script, "script_party_set_ai_state", ":sieger_lord", spai_besieging_center, ":siege_target"),
(party_set_slot, ":siege_target", debug_focus_siege_center, on),


(str_store_party_name, s0, ":sieger_lord"), # get its name for debug
(str_store_party_name, s1, ":siege_target"), # get its name for debug
(display_message, "@[EFE - DEBUG] - {s0} is sieging {s1}", efe_debug_hex),

(assign, "$new_debug_enemy_faction", ":target_enemy_faction"),

]),

("cf_kill_parties_debug", [

(eq, "$efe_debug", on),
(ge, "$new_debug_enemy_faction", 0),
(try_for_parties, ":enemy_lords"),
  (party_is_active, ":enemy_lords"),
  (store_faction_of_party, ":faction", ":enemy_lords"),
  (eq, ":faction", "$new_debug_enemy_faction"),
  (party_slot_eq, ":enemy_lords", slot_party_type, spt_kingdom_hero_party),
  (str_store_party_name, s0, ":enemy_lords"),
  (remove_party, ":enemy_lords"),
  (display_message, "@[DEBUG - EFE] {s0} removed to make sieges happen easier.", efe_debug_hex),
(try_end),

]),

("get_siege_duration_in_hours", [

  (store_script_param_1, ":party_no"),
  (party_get_slot, ":siege_start", ":party_no", slot_center_siege_begin_hours),
  (store_current_hours, ":cur_hours"),
  (store_sub, reg0, ":cur_hours", ":siege_start"),

]),

("calculate_starvation_days_left_to_surrender", [

  (store_script_param_1, ":party_no"),
  (party_get_slot, ":town_food_store", ":party_no", slot_party_food_store),
  (call_script, "script_center_get_food_consumption", ":party_no"),
  (assign, ":food_consumption", reg0),
  (assign, reg7, ":food_consumption"),
  (assign, reg8, ":town_food_store"),
  (store_div, reg0, ":town_food_store", ":food_consumption"),

]),

("cf_update_lord_party_texts", [

(eq, "$efe_debug", on),
(try_for_parties, ":lord_parties"),
  (party_is_active, ":lord_parties"),
  (party_slot_eq, ":lord_parties", slot_party_type, spt_kingdom_hero_party),
  (party_get_slot, reg5, ":lord_parties", slot_party_ai_state),
  #(str_store_string, s27, reg5),
  (party_set_extra_text, ":lord_parties", "@~~~^State: {reg5}^~~~"),
(try_end),

]),

("cf_update_sieged_center_texts", [

(try_for_range, ":sieged_centers", walled_centers_begin, walled_centers_end),
#(try_for_parties, ":sieged_centers"),
  (party_is_active, ":sieged_centers"),
  (party_slot_eq, ":sieged_centers", slot_village_state, svs_under_siege),
  (call_script, "script_calculate_starvation_days_left_to_surrender", ":sieged_centers"),
  (assign, reg50, reg0),
  (party_get_slot, ":sieger", ":sieged_centers", slot_center_is_besieged_by),
  (str_store_party_name, s5, ":sieger"),
  (store_faction_of_party, ":faction_sieger", ":sieger"),
  (faction_get_color, ":sieger_color", ":faction_sieger"),
  (assign, reg40, ":sieger_color"),
  (call_script, "script_center_get_food_consumption", ":sieged_centers"),
  (assign, reg2, reg0),
  (call_script, "script_center_get_food_store_limit", ":sieged_centers"),
  (assign, reg3, reg0),
  (party_get_slot, reg4, ":sieged_centers", slot_party_food_store),
  (call_script, "script_get_siege_duration_in_hours", ":sieged_centers"),
  (assign, reg9, reg0),
  (party_set_extra_text, ":sieged_centers", "@(Under Siege)^~~~^- Sieger -^~~~^{s5}^Siege is ongoing for {reg9} hours.^~~~^- Food Stores -^~~~^{reg4}/{reg3} - {reg2} (Daily Consumption)^~~~^Starvation will start in {reg50} days.", reg40),
(try_end),

]),

# cf_get_random_lord_including_king_with_faction
# Input: arg1 = faction_no
# Output: reg0 = party_no, Can Fail!
("cf_get_random_lord_party_including_king_with_faction",
    [
      (store_script_param_1, ":faction_no"),
      (assign, ":result", -1),
      (assign, ":count_lords", 0),
      (try_for_range, ":lord_no", heroes_begin, heroes_end),
        (store_troop_faction, ":lord_faction_no", ":lord_no"),
        (eq, ":faction_no", ":lord_faction_no"),
        #(neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":lord_no"),
        (troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
        #(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
        (neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
        (troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
        (ge, ":lord_party", 0),
        (party_slot_eq, ":lord_party", slot_party_type, spt_kingdom_hero_party),
        (val_add, ":count_lords", 1),
      (try_end),
      (store_random_in_range, ":random_lord", 0, ":count_lords"),
      (assign, ":count_lords", 0),
      (try_for_range, ":lord_no", heroes_begin, heroes_end),
        (eq, ":result", -1),
        (store_troop_faction, ":lord_faction_no", ":lord_no"),
        (eq, ":faction_no", ":lord_faction_no"),
        #(neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":lord_no"),
        (troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
        #(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
        (neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
        (troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
        (party_slot_eq, ":lord_party", slot_party_type, spt_kingdom_hero_party),
        (ge, ":lord_party", 0),
        (val_add, ":count_lords", 1),
        (lt, ":random_lord", ":count_lords"),
        (assign, ":result", ":lord_party"),
      (try_end),
      (neq, ":result", -1),
      (assign, reg0, ":result"),
  ]),

  
# cf_get_random_lord_including_king_with_faction
# Input: arg1 = faction_no
# Output: reg0 = troop_no, Can Fail!
("cf_get_random_lord_including_king_with_faction",
    [
      (store_script_param_1, ":faction_no"),
      (assign, ":result", -1),
      (assign, ":count_lords", 0),
      (try_for_range, ":lord_no", heroes_begin, heroes_end),
        (store_troop_faction, ":lord_faction_no", ":lord_no"),
        (eq, ":faction_no", ":lord_faction_no"),
        #(neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":lord_no"),
        (troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
        #(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
        (neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
        (troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
        (ge, ":lord_party", 0),
        (party_slot_eq, ":lord_party", slot_party_type, spt_kingdom_hero_party),
        (val_add, ":count_lords", 1),
      (try_end),
      (store_random_in_range, ":random_lord", 0, ":count_lords"),
      (assign, ":count_lords", 0),
      (try_for_range, ":lord_no", heroes_begin, heroes_end),
        (eq, ":result", -1),
        (store_troop_faction, ":lord_faction_no", ":lord_no"),
        (eq, ":faction_no", ":lord_faction_no"),
        #(neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":lord_no"),
        (troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
        #(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
        (neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
        (troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
        (party_slot_eq, ":lord_party", slot_party_type, spt_kingdom_hero_party),
        (ge, ":lord_party", 0),
        (val_add, ":count_lords", 1),
        (lt, ":random_lord", ":count_lords"),
        (assign, ":result", ":lord_no"),
      (try_end),
      (neq, ":result", -1),
      (assign, reg0, ":result"),
  ]),

]

