#-*-coding:utf-8-*-
from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_music import *
##diplomacy start+
from header_terrain_types import *
from module_factions import dplmc_factions_end
from ID_info_pages import ip_morale
##diplomacy end+

from module_constants import *

from compiler import *
####################################################################################################################
# Simple triggers are the alternative to old style triggers. They do not preserve state, and thus simpler to maintain.
#
#  Each simple trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################



simple_triggers = [

# This trigger is deprecated. Use "script_game_event_party_encounter" in module_scripts.py instead
  (ti_on_party_encounter,
   [
    ]),


# This trigger is deprecated. Use "script_game_event_simulate_battle" in module_scripts.py instead
  (ti_simulate_battle,
   [
    ]),


  (1,
   [
      (gt,"$auto_besiege_town",0),
      (gt,"$g_player_besiege_town", 0),
      (ge, "$g_siege_method", 1),
      (store_current_hours, ":cur_hours"),
      (eq, "$g_siege_force_wait", 0),
      (ge, ":cur_hours", "$g_siege_method_finish_hours"),
      (neg|is_currently_night),
      #SB : add adjusted renown for ladder construction
      (try_begin), #we should have stored the original npc but composition is unlikely to change
        (call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
        (assign, ":troop_no", reg1),
        (neq, ":troop_no", "trp_player"),
        # (is_between, ":troop_no", companions_begin, companions_end),
        (store_mul, ":renown", "$g_siege_method", dplmc_companion_skill_renown + 1),
        (call_script, "script_change_troop_renown", ":troop_no", ":renown"),
      (try_end),
      (rest_for_hours, 0, 0, 0), #stop resting
    ]),


  (0,
   [
      (eq,"$g_player_is_captive",1),
      (gt, "$capturer_party", 0),
      (party_is_active, "$capturer_party"),
      (party_relocate_near_party, "p_main_party", "$capturer_party", 0),
    ]),


#Auto-menu
  (0,
   [
     (try_begin),
        (check_quest_active, "qst_the_wolfmen"),
        (quest_slot_ge, "qst_the_wolfmen", slot_quest_current_state, 3),
        (neg|quest_slot_ge, "qst_the_wolfmen", slot_quest_current_state, 12),
        (store_current_hours, ":hours"),
        (quest_slot_eq, "qst_the_wolfmen", slot_quest_gold_reward, ":hours"),
        (try_begin),
            (quest_slot_eq, "qst_the_wolfmen", slot_quest_current_state, 3),
            (jump_to_menu, "mnu_wolfmen_1"),
        (else_try),
            (quest_slot_eq, "qst_the_wolfmen", slot_quest_current_state, 5),
            (jump_to_menu, "mnu_wolfmen_duel"),
        (else_try),
            (quest_slot_eq, "qst_the_wolfmen", slot_quest_current_state, 7),
            (jump_to_menu, "mnu_wolfmen_initiation_1"),
        (else_try),
            (quest_slot_eq, "qst_the_wolfmen", slot_quest_current_state, 8),
            (jump_to_menu, "mnu_wolfmen_initiation_2"),
        (else_try),
            (quest_slot_eq, "qst_the_wolfmen", slot_quest_current_state, 9),
            (jump_to_menu, "mnu_wolfmen_initiation_3"),
        (else_try),
            (quest_slot_eq, "qst_the_wolfmen", slot_quest_current_state, 10),
            (jump_to_menu, "mnu_wolfmen_initiation_4"),
        (else_try),
            (quest_slot_eq, "qst_the_wolfmen", slot_quest_current_state, 11),
            (jump_to_menu, "mnu_wolfmen_initiation_5"),
        (try_end),
     (else_try),
       (is_between, "$g_last_rest_center",  centers_begin, centers_end), #SB : proper rest conditions
       (party_get_battle_opponent, ":besieger_party", "$g_last_rest_center"),
       (gt, ":besieger_party", 0),
       (store_faction_of_party, ":encountered_faction", "$g_last_rest_center"),
       (store_relation, ":faction_relation", ":encountered_faction", "fac_player_supporters_faction"),
       (store_faction_of_party, ":besieger_party_faction", ":besieger_party"),
       (store_relation, ":besieger_party_relation", ":besieger_party_faction", "fac_player_supporters_faction"),
       (ge, ":faction_relation", 0),
       (lt, ":besieger_party_relation", 0),
       (start_encounter, "$g_last_rest_center"),
       (rest_for_hours, 0, 0, 0), #stop resting
     (else_try),
       (store_current_hours, ":cur_hours"),
       (assign, ":check", 0),
       (try_begin),
         (neq, "$g_check_autos_at_hour", 0),
         (ge, ":cur_hours", "$g_check_autos_at_hour"),
         (assign, ":check", 1),
         (assign, "$g_check_autos_at_hour", 0),
       (try_end),
       (this_or_next|eq, ":check", 1),
       (map_free),
       (try_begin),
         (ge,"$auto_menu",1),
         (jump_to_menu,"$auto_menu"),
         (assign,"$auto_menu",-1),
       (else_try),
         (ge,"$auto_enter_town",1),
         (start_encounter, "$auto_enter_town"),
       (else_try),
         (ge,"$auto_besiege_town",1),
         (start_encounter, "$auto_besiege_town"),
       (else_try),
         (ge,"$g_camp_mode", 1),
         (assign, "$g_camp_mode", 0),
         (assign, "$g_infinite_camping", 0),
         (assign, "$g_player_icon_state", pis_normal),

         (rest_for_hours, 0, 0, 0), #stop camping

         (display_message, "@Breaking camp...", message_alert), #SB : colorize
       (else_try), #SB : restore after leaving town with disguises
         (gt, "$sneaked_into_town", disguise_none),
         (eq, "$g_dplmc_player_disguise", 1),
         (display_message, "@Removing disguise...", message_alert), #SB : colorize
         (try_begin),
           (eq, "$g_dplmc_player_disguise", 1),
           (set_show_messages, 0),
           #equipment is deposited back to inventory, it starts off blank
           (try_for_range, ":i_slot", ek_item_0, ek_food + 1),
             (troop_get_inventory_slot, ":item", "trp_player", ":i_slot"),
             (neq, ":item", -1),
             (troop_get_inventory_slot_modifier, ":imod", "trp_player", ":i_slot"),
             (troop_add_item, "trp_random_town_sequence", ":item", ":imod"),
           (try_end),
           #less efficient, but merge and respect original player inventory's order
           (call_script, "script_move_inventory_and_gold", "trp_player", "trp_random_town_sequence", 0), #do not move gold
           (call_script, "script_dplmc_copy_inventory", "trp_random_town_sequence", "trp_player"),
           (call_script, "script_troop_transfer_gold", "trp_random_town_sequence", "trp_player", 0), #move remaining gold now
           (set_show_messages, 1),
         (try_end),
         (assign, "$sneaked_into_town", disguise_none),
       (try_end),
     (try_end),
     ]),


#Notification menus
  (0,
   [
     (troop_slot_ge, "trp_notification_menu_types", 0, 1),
     (troop_get_slot, ":menu_type", "trp_notification_menu_types", 0),
     (troop_get_slot, "$g_notification_menu_var1", "trp_notification_menu_var1", 0),
     (troop_get_slot, "$g_notification_menu_var2", "trp_notification_menu_var2", 0),
     (jump_to_menu, ":menu_type"),
     (assign, ":end_cond", 2),
     (try_for_range, ":cur_slot", 1, ":end_cond"),
       (try_begin),
         (troop_slot_ge, "trp_notification_menu_types", ":cur_slot", 1),
         (val_add, ":end_cond", 1),
       (try_end),
       (store_sub, ":cur_slot_minus_one", ":cur_slot", 1),
       (troop_get_slot, ":local_temp", "trp_notification_menu_types", ":cur_slot"),
       (troop_set_slot, "trp_notification_menu_types", ":cur_slot_minus_one", ":local_temp"),
       (troop_get_slot, ":local_temp", "trp_notification_menu_var1", ":cur_slot"),
       (troop_set_slot, "trp_notification_menu_var1", ":cur_slot_minus_one", ":local_temp"),
       (troop_get_slot, ":local_temp", "trp_notification_menu_var2", ":cur_slot"),
       (troop_set_slot, "trp_notification_menu_var2", ":cur_slot_minus_one", ":local_temp"),
     (try_end),
    ]),

  #Music,
  (1,
   [
	(this_or_next|eq, "$freelancer_state", 1),
       (map_free),
       (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
        ]),

        #SB : change this block
    (1,
    [
      # #escort caravan quest auto dialog trigger, moved to menu while auto-entering towns
      # (try_begin),
        # (eq, "$caravan_escort_state", 1),
        # (party_is_active, "$caravan_escort_party_id"),

        # (store_distance_to_party_from_party, ":caravan_distance_to_destination","$caravan_escort_destination_town","$caravan_escort_party_id"),
        # (lt, ":caravan_distance_to_destination", 2),

        # (store_distance_to_party_from_party, ":caravan_distance_to_player","p_main_party","$caravan_escort_party_id"),
        # (lt, ":caravan_distance_to_player", 5),

        # (assign, "$talk_context", tc_party_encounter),
        # (assign, "$g_encountered_party", "$caravan_escort_party_id"),
        # (party_stack_get_troop_id, ":caravan_leader", "$caravan_escort_party_id", 0),
        # (party_stack_get_troop_dna, ":caravan_leader_dna", "$caravan_escort_party_id", 0),

        # (start_map_conversation, ":caravan_leader", ":caravan_leader_dna"),
      # (try_end),
      #SB : debug block
      (try_begin),
        (ge, "$cheat_mode", 1),
        (troop_is_hero, "$g_talk_troop"),
        (str_store_troop_name, s17, "$g_talk_troop"),
        (troop_get_slot, reg17, "$g_talk_troop", slot_troop_wealth),
        #(try_begin),
          #(neq, reg17, "$demanded_money"),
          #(display_message, "@{s17} has {reg17} denars"),
        #(try_end),
        (assign, "$demanded_money", reg17),
      (try_end),

      (try_begin),
        (gt, "$g_reset_mission_participation", 1),

        (try_for_range, ":troop", active_npcs_begin, heroes_end),
          (troop_set_slot, ":troop", slot_troop_mission_participation, 0),
        (try_end),
      (try_end),
    ]),

(24.0/number_of_factions,#9
[
    (store_random_in_range, ":kingdom_no", kingdoms_begin, kingdoms_end),
    (try_begin),
        (faction_slot_eq, ":kingdom_no", slot_faction_state, sfs_active),
        (call_script, "script_faction_recalculate_strength", ":kingdom_no"),
        (call_script, "script_evaluate_realm_stability", ":kingdom_no"),
        (try_begin),
            (ge, ":kingdom_no", npc_kingdoms_begin),
            (faction_get_slot, ":faction_morale", ":kingdom_no",  slot_faction_morale_of_player_troops),
            (store_sub, ":divisor", 140, "$player_right_to_rule"),
            (val_div, ":divisor", 14),
            (val_max, ":divisor", 1),
            (store_div, ":faction_morale_div_10", ":faction_morale", ":divisor"), #10 is the base, down to 2 for 100 rtr
            (val_sub, ":faction_morale", ":faction_morale_div_10"),
            (faction_set_slot, ":kingdom_no",  slot_faction_morale_of_player_troops, ":faction_morale"),
        (try_end),
    (try_end),
]),


 (0.04, #Locate kingdom ladies
    [
    #change location for all ladies
    (store_random_in_range, ":troop_id", kingdom_ladies_begin, kingdom_ladies_end),
    ##diplomacy start+ do not set the troop's center when the troop is leading a party
    (troop_slot_eq, ":troop_id", slot_troop_occupation, slto_kingdom_lady),
    (troop_get_slot, ":leaded_party", ":troop_id", slot_troop_leaded_party),
    (try_begin),
        (gt, ":leaded_party", 0),
        (neg|party_is_active, ":leaded_party"),
        (assign, ":leaded_party", -1),
    (try_end),
    (lt, ":leaded_party", 1),#if the value is 0, it's a bug, so overlook it

     #do not change location if under siege
    (assign, ":continue", 1),
    (try_begin),
      (troop_get_slot, ":location", ":troop_id",  slot_troop_cur_center),
      (gt, ":location", -1),
      (party_slot_eq, ":location", slot_village_state, svs_under_siege),
      (assign, ":continue", 0),
    (try_end),
    (eq, ":continue", 1),

    (neg|troop_slot_ge, ":troop_id", slot_troop_prisoner_of_party, 0),
    (call_script, "script_get_kingdom_lady_social_determinants", ":troop_id"),
    (assign, ":location", reg1),
    (troop_set_slot, ":troop_id", slot_troop_cur_center, ":location"),
	]),


 (24, #Kingdom ladies send messages
 [
#madsci lets use this 24 trigger for countdowns
(val_add, "$total_days_passed", 1),

(try_begin),
(eq, "$total_days_passed", 750), #let remaining factions eat the indigenoi if player has ignored them for long enough
	(try_for_range, ":fac", npc_kingdoms_begin, npc_kingdoms_end),
	(neq, ":fac", "$players_kingdom"),
	(set_relation, "fac_indigenoi", ":fac", -50),
	(try_end),
(try_end),

(try_for_range, ":center", towns_begin, towns_end),
(party_get_slot, ":rebellion_timer", ":center", slot_party_rebellion_timer),
(party_get_slot, ":rebellion_cooldown", ":center", slot_party_rebellion_cooldown),
	(try_begin),
	(gt, ":rebellion_timer", 1),
	(val_sub, ":rebellion_timer", 1),
	(party_set_slot, ":center", slot_party_rebellion_timer, ":rebellion_timer"),
	(try_end),
	(try_begin),
	(gt, ":rebellion_cooldown", 0),
	(val_sub, ":rebellion_cooldown", 1),
	(party_set_slot, ":center", slot_party_rebellion_cooldown, ":rebellion_cooldown"),
	(try_end),
(try_end),

(try_for_range, ":kingdom_no", kingdoms_begin, kingdoms_end),
(faction_slot_eq, ":kingdom_no", slot_faction_state, sfs_active),
(faction_get_slot, ":days_survived", ":kingdom_no", slot_faction_days_survived),
(val_add, ":days_survived", 1),
(faction_set_slot, ":kingdom_no", slot_faction_days_survived, ":days_survived"),
(try_end),

	(try_begin),
		(neg|check_quest_active, "qst_visit_lady"),
		(neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 1),
		(neg|troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin),

		(assign, ":lady_not_visited_longest_time", -1),
		(assign, ":longest_time_without_visit", 120), #five days

		(try_for_range, ":troop_id", kingdom_ladies_begin, kingdom_ladies_end),
            ##diplomacy start not dead, exiled, etc.
			(neg|troop_slot_ge, ":troop_id", slot_troop_occupation, slto_retirement),
            #not already betrothed
            (neg|troop_slot_eq, "trp_player", slot_troop_betrothed, ":troop_id"),
			##diplomacy end
			#set up message for ladies the player is courting
			(troop_slot_ge, ":troop_id", slot_troop_met, 2),
			(neg|troop_slot_eq, ":troop_id", slot_troop_met, 4),

			(troop_slot_eq, ":troop_id", slot_lady_no_messages, 0),
			(troop_slot_eq, ":troop_id", slot_troop_spouse, -1),

			(troop_get_slot, ":location", ":troop_id", slot_troop_cur_center),
			(is_between, ":location", walled_centers_begin, walled_centers_end),
			(call_script, "script_troop_get_relation_with_troop", "trp_player", ":troop_id"),
			(gt, reg0, 1),

			(store_current_hours, ":hours_since_last_visit"),
			(troop_get_slot, ":last_visit_hour", ":troop_id", slot_troop_last_talk_time),
			(val_sub, ":hours_since_last_visit", ":last_visit_hour"),

			(gt, ":hours_since_last_visit", ":longest_time_without_visit"),
			(assign, ":longest_time_without_visit", ":hours_since_last_visit"),
			(assign, ":lady_not_visited_longest_time", ":troop_id"),
			(assign, ":visit_lady_location", ":location"),

		(try_end),

		(try_begin),
			(gt, ":lady_not_visited_longest_time", 0),
			(call_script, "script_add_notification_menu", "mnu_notification_lady_requests_visit", ":lady_not_visited_longest_time", ":visit_lady_location"),
		(try_end),

	(try_end),
	]),


#Player raiding a village
# This trigger will check if player's raid has been completed and will lead control to village menu.
  (1,
   [
      (ge,"$g_player_raiding_village",1),
      (try_begin),
        (neq, "$g_player_is_captive", 0),
        #(rest_for_hours, 0, 0, 0), #stop resting - abort
        (assign,"$g_player_raiding_village",0),
     ### (else_try),         ###Remove this entire Else-Try###
       ### (map_free), #we have been attacked during raid
       ### (assign,"$g_player_raiding_village",0),
      (else_try),
        (this_or_next|party_slot_eq, "$g_player_raiding_village", slot_village_state, svs_looted),
        (party_slot_eq, "$g_player_raiding_village", slot_village_state, svs_deserted),
        (start_encounter, "$g_player_raiding_village"),
        (rest_for_hours, 0),
        (assign,"$g_player_raiding_village",0),
        (assign,"$g_player_raid_complete",1),
      (else_try),
        (party_slot_eq, "$g_player_raiding_village", slot_village_state, svs_being_raided),
        (rest_for_hours_interactive, 3, 5, 1), #rest while attackable    ###CHANGE rest_for_hours to rest_for_hours_interactive; ###OPTIONAL COMMENT OUT
      (else_try),
        (rest_for_hours, 0, 0, 0), #stop resting - abort
        (assign,"$g_player_raiding_village",0),
        (assign,"$g_player_raid_complete",0),
      (try_end),
    ]),

(0.25,
   [
      (ge,"$g_player_raiding_village",1),
      (store_distance_to_party_from_party, ":distance", "$g_player_raiding_village", "p_main_party"),
      (try_begin),
        (gt, ":distance", raid_distance),
        (str_store_party_name_link, s1, "$g_player_raiding_village"),
        (display_message, "@You have broken off your raid of {s1}."),
        (call_script, "script_village_set_state", "$current_town", 0),
        (party_set_slot, "$current_town", slot_village_raided_by, -1),
        (assign, "$g_player_raiding_village", 0),
        (rest_for_hours, 0, 0, 0), #stop resting - abort
      (else_try),
        (ge, ":distance", raid_distance / 2),
        (map_free),
        (jump_to_menu, "mnu_village_loot_continue"),
      (try_end),
    ]),
  #Pay day.
  (24 * 7,
   [
     ##diplomacy begin
     (store_current_hours, "$g_next_pay_time"),
     (val_add, "$g_next_pay_time", 24 * 7),
     ##diplomacy end
     (assign, "$g_presentation_lines_to_display_begin", 0),
     (assign, "$g_presentation_lines_to_display_end", 15),
     (assign, "$g_apply_budget_report_to_gold", 1),
     (try_begin),
       (eq, "$g_infinite_camping", 0),
       (start_presentation, "prsnt_budget_report"),
        ##diplomacy begin
        (try_begin),
          (gt, "$g_player_debt_to_party_members", 5000),
          (call_script, "script_add_notification_menu", "mnu_dplmc_deserters",20,0),
        (try_end),
        #SB : update the info pages coarsely once per week
        (try_for_range, ":kingdom_no", npc_kingdoms_begin, npc_kingdoms_end),
          (faction_get_slot, ":faction_morale", ":kingdom_no",  slot_faction_morale_of_player_troops),
          (store_div, ":value", ":faction_morale", 100),
          (neq, ":value", 0),
          (assign, reg6, ":value"),
          (store_mod, reg7, ":faction_morale", 100),
          (val_abs, reg7),
          (str_store_faction_name, s9, ":kingdom_no"),
          (store_sub, ":faction_offset", ":kingdom_no", kingdoms_begin), #SB : add one to index to not override default string
          (add_info_page_note_from_sreg, ip_morale, ":faction_offset", "@Morale for {s9} troops: {reg6}", 0),
         (try_end),
        ##diplomacy end

     (try_end),
    ]),

  # Oath fulfilled -- ie, mercenary contract expired?
  (24,
   [
      (le, "$auto_menu", 0),
      (gt, "$players_kingdom", 0),
      (neq, "$players_kingdom", "fac_player_supporters_faction"),
      (eq, "$player_has_homage", 0),

	  (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),

	  #A player bound to a kingdom by marriage will not have the contract expire. This should no longer be the case, as I've counted wives as having homage, but is in here as a fallback
	  (assign, ":player_has_marriage_in_faction", 0),
	  (try_begin),
		(is_between, ":player_spouse", active_npcs_begin, active_npcs_end),
		(store_faction_of_troop, ":spouse_faction", ":player_spouse"),
		(eq, ":spouse_faction", "$players_kingdom"),
	    (assign, ":player_has_marriage_in_faction", 1),
	  (try_end),
	  (eq, ":player_has_marriage_in_faction", 0),

      (store_current_day, ":cur_day"),
      (gt, ":cur_day", "$mercenary_service_next_renew_day"),
      (jump_to_menu, "mnu_oath_fulfilled"),
    ]),

  # Reducing luck by 1 in every 180 hours
  #(180,
  # [
  #   (val_sub, "$g_player_luck", 1),
  #   (val_max, "$g_player_luck", 0),
  #  ]),

  #courtship reset
  (72,
   [
     (assign, "$lady_flirtation_location", 0),

(store_random_in_range, ":troop_no", heroes_begin, heroes_end), #check one random lord every 72 hours
(call_script, "script_check_lord_religion", ":troop_no"),

#madsci roman rebels petition to join Rome
(try_begin),
(faction_slot_eq, "fac_kingdom_1", slot_faction_state, sfs_active),
(faction_get_slot, ":roman_culture", "fac_kingdom_1", slot_faction_culture),
(assign, ":rebel_found", -1),
(assign, ":end", "fac_rebel_kingdom_3"),
(val_add, ":end", 1),
	(try_for_range, ":kingdom_no", "fac_rebel_kingdom_1", ":end"),
	(eq, ":rebel_found", -1),
	(neq, "$players_kingdom", ":kingdom_no"),
	(faction_slot_eq, ":kingdom_no", slot_faction_state, sfs_active),
	(faction_get_slot, ":rebel_culture", ":kingdom_no", slot_faction_culture),
	(eq, ":rebel_culture", ":roman_culture"),
	(store_relation, ":reln", ":kingdom_no", "fac_kingdom_1"),
	(ge, ":reln", 0),
	(faction_get_slot, ":days_survived", ":kingdom_no", slot_faction_days_survived),
	(gt, ":days_survived", 30),
	(store_random_in_range, ":rnd", 0, 20), #shouldnt be guaranteed to happen after 30 days
	(eq, ":rnd", 1),
	(assign, ":rebel_found", ":kingdom_no"),
	(try_end),
(gt, ":rebel_found", 0),
(str_store_faction_name, s10, ":rebel_found"),
(str_store_faction_name, s11, "fac_kingdom_1"),
(display_log_message, "@The rebels of {s10} have successfully petitioned to join {s11}"),
(faction_set_slot, ":rebel_found", slot_faction_state, sfs_inactive),
(faction_set_slot, ":rebel_found",  slot_faction_days_survived, 0),
(faction_get_slot, ":faction_leader", ":rebel_found", slot_faction_leader),
 	(try_for_range, ":cur_troop", heroes_begin, heroes_end),
	(neq, ":cur_troop", ":faction_leader"),
	(troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
        (store_troop_faction, ":lord_faction_no", ":cur_troop"),
        (eq, ":rebel_found", ":lord_faction_no"),
	(call_script, "script_change_troop_faction", ":cur_troop", "fac_kingdom_1"),
	(try_end),

	(try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
	(store_faction_of_party, ":party_faction", ":cur_center"),
	(eq, ":party_faction", ":rebel_found"),
	(call_script, "script_give_center_to_faction", ":cur_center", "fac_kingdom_1"),
	(try_end),

	(try_begin),
	(gt, ":faction_leader", 0),
	(neg|troop_slot_eq, ":faction_leader", slot_troop_occupation, dplmc_slto_dead),
	#(troop_set_slot, ":faction_leader", slot_troop_occupation, slto_inactive),
		(try_begin), #madsci cant have a kingdom hero party of non-kingdom faction on the map
		(troop_get_slot, ":current_party", ":faction_leader", slot_troop_leaded_party),
		(gt, ":current_party", 0),
		(party_is_active, ":current_party"),
		(call_script, "script_remove_hero_prisoners", ":current_party"),
		(remove_party, ":current_party"),
		(else_try),
		(troop_get_slot, ":cur_prisoner_of_party", ":faction_leader", slot_troop_prisoner_of_party),
		(ge, ":cur_prisoner_of_party", 0),
		(party_remove_prisoners, ":cur_prisoner_of_party", ":faction_leader", 1),
		(call_script, "script_remove_troop_from_prison", ":faction_leader"),
		(str_store_troop_name, s4, ":faction_leader"),
		(display_message,"@{s4} has escaped from captivity."),
		(try_end),
	(call_script, "script_change_troop_faction", ":faction_leader", "fac_outlaws"),
	(call_script, "script_update_troop_notes", ":faction_leader"),
	(try_end),

	(try_for_parties, ":party"),
	(gt, ":party", last_static_party),
	(store_faction_of_party, ":party_faction", ":party"),
	(eq, ":party_faction", ":rebel_found"),
	(party_set_faction, ":party", "fac_kingdom_1"),
	(try_end),
(faction_set_note_available, ":rebel_found", 0),

	(try_begin),
        (eq, "$g_infinite_camping", 0),
	(assign, "$temp", ":rebel_found"),
	(jump_to_menu, "mnu_rebels_join_rome"),
	(try_end),
(try_end),
    ]),

  #reset time to spare
  (4,
   [
     (assign, "$g_time_to_spare", 1),

    (try_begin),
        (troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin),
        (assign, "$g_player_banner_granted", 1),
    (try_end),

     ]),


  # Banner selection menu
  (24,
   [
    (eq, "$g_player_banner_granted", 1),
    (troop_slot_eq, "trp_player", slot_troop_banner_scene_prop, 0),
    (le,"$auto_menu",0),
#normal_banner_begin
    (start_presentation, "prsnt_banner_selection"),
#custom_banner_begin
#    (start_presentation, "prsnt_custom_banner"),
    ]),

  # Party Morale: Move morale towards target value.
(24,[
    (call_script, "script_get_player_party_morale_values"),
    (assign, ":target_morale", reg0),
    (party_get_morale, ":cur_morale", "p_main_party"),
    (store_sub, ":dif", ":target_morale", ":cur_morale"),
    (store_div, ":dif_to_add", ":dif", 5),
    (store_mul, ":dif_to_add_correction", ":dif_to_add", 5),
    (try_begin),#finding ceiling of the value
        (neq, ":dif_to_add_correction", ":dif"),
        (try_begin),
            (gt, ":dif", 0),
            (val_add, ":dif_to_add", 1),
        (else_try),
            (val_sub, ":dif_to_add", 1),
        (try_end),
    (try_end),
    (val_add, ":cur_morale", ":dif_to_add"),
    (party_set_morale, "p_main_party", ":cur_morale"),
]),

(24.0*3.0/(number_of_centers),##every 3 days#28
[###every center has an ideal prosperity, this is to reach that
 #this is moved up from below , from a 24 x 15 slot to a 24 slot
    (store_random_in_range, ":center_no", centers_begin, centers_end),
    (assign, ":save_reg0", reg0),
    (call_script, "script_get_center_ideal_prosperity", ":center_no"),
    (assign, ":ideal_prosperity", reg0),
    (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
    (try_begin),
        (gt, ":prosperity", ":ideal_prosperity"),
        (store_random_in_range, ":change", 1, 3),##more negative effects now possible
        (val_mul, ":change", -1),
        (call_script, "script_change_center_prosperity", ":center_no", ":change"),
        (val_add, "$newglob_total_prosperity_from_convergence", ":change"),
    (else_try),
        (lt, ":prosperity", ":ideal_prosperity"),
        (store_random_in_range, ":change", 1, 3),
        (call_script, "script_change_center_prosperity", ":center_no", ":change"),
        (val_add, "$newglob_total_prosperity_from_convergence", ":change"),
    (try_end),
    (assign, reg0, ":save_reg0"),
]),

  #Adding net incomes to heroes (once a week)
  #Increasing debts to heroes by 1% (once a week)
  (24*7.0/(number_of_active_npcs),
   [
	(assign, ":save_reg0", reg0),
    (try_begin),
        (neg|is_between, "$g_hero_wealth", heroes_begin, heroes_end),
        (assign, "$g_hero_wealth", heroes_begin),
    (try_end),
    (try_begin),
        (this_or_next|is_between, "$g_hero_wealth", active_npcs_begin, active_npcs_end),
        (troop_slot_eq, "$g_hero_wealth", slot_troop_occupation, slto_kingdom_hero),
        (troop_get_slot, ":cur_debt", "$g_hero_wealth", slot_troop_player_debt),#Increasing debt
        (lt, ":cur_debt", dplmc_ransom_debt_mask), #qst_rescue_prisoner does not accumulate
        #SB : aristocracy/plutocracy debt modifier
        (store_faction_of_troop, ":faction_no", "$g_hero_wealth"),
        (faction_get_slot, ":aristocracy", ":faction_no", dplmc_slot_faction_aristocracy),
        (val_add, ":aristocracy", 205), #1.01x to 1.04x
        (val_mul, ":cur_debt", ":aristocracy"),
        (val_div, ":cur_debt", 200),
        (troop_set_slot, "$g_hero_wealth", slot_troop_player_debt, ":cur_debt"),
        (call_script, "script_calculate_hero_weekly_net_income_and_add_to_wealth", "$g_hero_wealth"),#Adding net income
    (try_end),
    (val_add, "$g_hero_wealth", 1),
    (assign, reg0, ":save_reg0"),
    ]),

  #Adding net incomes to centers (once a week)
(24*7.0/(number_of_walled_centers), [#once a week on average
    (assign, ":save_reg0", reg0),
       (store_random_in_range, ":center_no", walled_centers_begin, walled_centers_end),
       #(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
         #If non-player center, adding income to wealth
         (neg|party_slot_eq, ":center_no", slot_town_lord, "trp_player"), #center does not belong to player.
		 ##diplomacy start+
		 #Defer the ownership check so attrition can still occur for unowned centers.
		 #Give a slight grace period first, though.
		 (neg|party_slot_eq, ":center_no", slot_town_lord, 0),

           ##diplomacy start+
           (store_current_hours, ":two_weeks_ago"),
           (val_sub, ":two_weeks_ago", 24 * 14),
           ##diplomacy end+

		 (this_or_next|party_slot_ge, ":center_no", dplmc_slot_center_last_transfer_time, ":two_weeks_ago"),
			(party_slot_ge, ":center_no", slot_town_lord, 1), #center belongs to someone.
		 (this_or_next|ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
		 ##diplomacy end+
		 (party_slot_ge, ":center_no", slot_town_lord, 1), #center belongs to someone.
         (party_get_slot, ":cur_wealth", ":center_no", slot_town_wealth),
         (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
         (store_mul, ":added_wealth", ":prosperity", 15),
         (val_add, ":added_wealth", 700),
         (try_begin),
           (party_slot_eq, ":center_no", slot_party_type, spt_town),
           (val_mul, ":added_wealth", 3),
           (val_div, ":added_wealth", 2),
         (try_end),
         (val_add, ":cur_wealth", ":added_wealth"),
         (call_script, "script_calculate_weekly_party_wage", ":center_no"),
         (val_sub, ":cur_wealth", reg0),
		 ##diplomacy start+ Allow attrition to occur
		 (try_begin),
			(lt, ":cur_wealth", 0),
			(ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
			(assign, ":cur_weekly_wage", reg0),
			(store_party_size_wo_prisoners, ":garrison_size", ":center_no"),
			(call_script, "script_party_get_ideal_size", ":center_no"),#This script has been modified to support this use
			(val_mul, reg0, 5),
			(val_div, reg0, 4),
			(ge, ":garrison_size", reg0),

			(store_sub, ":percent_under", 0, ":cur_wealth"),
			(val_mul, ":percent_under", 100),
			(val_div, ":percent_under", ":cur_weekly_wage"),
			(val_div, ":percent_under", 5), #Max 20 percent (won't take garrison below ideal size)
			(call_script, "script_party_inflict_attrition", ":center_no", ":percent_under", 1),
		 (try_end),
		 (party_slot_ge, ":center_no", slot_town_lord, 1), #center belongs to someone.
		 ##diplomacy end+
         (val_max, ":cur_wealth", 0),
         (party_set_slot, ":center_no", slot_town_wealth, ":cur_wealth"),
      # (try_end),
	   ##diplomacy end+
	   (assign, reg0, ":save_reg0"),
	   ##diplomacy end+
]),


  #Hiring men with hero wealths (once a day)
  (24.0/(number_of_active_npcs),
   [
 (try_begin),
   (neg|is_between, "$g_hire_troops_and_controversy", heroes_begin, heroes_end),
   (assign, "$g_hire_troops_and_controversy", heroes_begin),
 (try_end),

     (try_begin),
     ##diplomacy end+
       (troop_slot_eq, "$g_hire_troops_and_controversy", slot_troop_occupation, slto_kingdom_hero),
       (troop_get_slot, ":party_no", "$g_hire_troops_and_controversy", slot_troop_leaded_party),
       (ge, ":party_no", 1),
       (party_is_active, ":party_no"),
       (party_get_attached_to, ":cur_attached_party", ":party_no"),
       (is_between, ":cur_attached_party", centers_begin, centers_end),
       (party_slot_eq, ":cur_attached_party", slot_center_is_besieged_by, -1), #center not under siege

       (store_faction_of_party, ":party_faction", ":party_no"),
	(try_begin),
	(this_or_next|eq, ":party_faction", "fac_player_supporters_faction"),
	(eq, ":party_faction", "$players_kingdom"),
	(store_random_in_range, ":num_hiring_rounds", 1, 3),
	(else_try),
         (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
		(try_begin),
		(eq, ":reduce_campaign_ai", 0), #hard (2x reinforcing)
		(assign, ":num_hiring_rounds", 2),
		(else_try),
		(eq, ":reduce_campaign_ai", 1), #medium (1x or 2x reinforcing)
		(store_random_in_range, ":num_hiring_rounds", 1, 3),
		(else_try),
		(eq, ":reduce_campaign_ai", 2), #easy (1x reinforcing)
		(assign, ":num_hiring_rounds", 1),
		(try_end),
	(try_end),

       (try_begin),
         (faction_slot_eq,  ":party_faction", slot_faction_marshall, "$g_hire_troops_and_controversy"),
         (val_add, ":num_hiring_rounds", 1),
       (try_end),

	(try_for_range, ":unused", 0, ":num_hiring_rounds"),
	(call_script, "script_hire_men_to_kingdom_hero_party", "$g_hire_troops_and_controversy"), #Hiring men with current wealth
	(try_end),

        (try_begin),#upgrade troops a bit
            (assign, ":xp_addition_for_party_no", 2500),
            (try_begin),
                (party_slot_ge, ":cur_attached_party", slot_center_has_training_grounds, 1),#training ground
                (val_add, ":xp_addition_for_party_no", 22500),
            (try_end),
            (party_upgrade_with_xp, ":party_no", ":xp_addition_for_party_no", 0),
        (try_end),

     (try_end),

    (val_add, "$g_hire_troops_and_controversy", 1),
    ]),

#hire men to towns and castles
(24.0/(number_of_walled_centers), [#24h on average
	(try_begin),
	(neg|is_between, "$center_to_check", walled_centers_begin, walled_centers_end),
	(assign, "$center_to_check", walled_centers_begin),
	(try_end),
(call_script, "script_prune_prisoners", "$center_to_check"),
(call_script, "script_hire_men_to_center", "$center_to_check"),
(val_add, "$center_to_check", 1),
]),

  #Checking if the troops are resting at a half payment point
  (6,
   [(store_current_day, ":cur_day"),
    (try_begin),
      (neq, ":cur_day", "$g_last_half_payment_check_day"),
      (assign, "$g_last_half_payment_check_day", ":cur_day"),
      (try_begin),
        (eq, "$g_half_payment_checkpoint", 1),
        (val_add, "$g_cur_week_half_daily_wage_payments", 1), #half payment for yesterday
      (try_end),
      (assign, "$g_half_payment_checkpoint", 1),
    (try_end),
    (assign, ":resting_at_manor_or_walled_center", 0),
    (try_begin),
      (neg|map_free),
      (is_between, "$g_last_rest_center", centers_begin, centers_end), #SB : proper rest conditions
      (this_or_next|party_slot_eq, "$g_last_rest_center", slot_center_has_manor, 1),
      (is_between, "$g_last_rest_center", walled_centers_begin, walled_centers_end),
      (assign, ":resting_at_manor_or_walled_center", 1),
    (try_end),
    (eq, ":resting_at_manor_or_walled_center", 0),
    (assign, "$g_half_payment_checkpoint", 0),
    ]),

   (1.25,#was 1, make it a little less frequent	#MOTO recycle trigger (to 1 from 24) from another 24-hour trigger#34
   [
  (assign, ":save_reg0", reg0),
	(store_time_of_day, ":oclock"),
	(store_current_day, ":day_mod"),
	(val_mod, ":day_mod", 8),	#eighth the rate of incidents moto chief
	(store_sub, ":num_villages", villages_end, villages_begin),
	(val_div, ":num_villages", 23),
	(store_mul, ":start_village", ":oclock", ":num_villages"),
	(val_add, ":start_village", villages_begin),
	(store_add, ":end_village", ":start_village", ":num_villages"),
	(val_min, ":end_village", villages_end),
	#MOTO ramp up border incidents
	(try_for_range, ":acting_village", ":start_village", ":end_village"),
		(store_mod, reg0, ":acting_village", 8),	#eighth the rate of incidents moto chief
		(eq, reg0, ":day_mod"),
	# (try_begin),
		# (store_random_in_range, ":acting_village", villages_begin, villages_end),
	#MOTO ramp up border incidents end
		(store_random_in_range, ":target_village", villages_begin, villages_end),
		(store_faction_of_party, ":acting_faction", ":acting_village"),
		(store_faction_of_party, ":target_faction", ":target_village"), #target faction receives the provocation
		(neq, ":acting_village", ":target_village"),
		(neq, ":acting_faction", ":target_faction"),
		(is_between, ":acting_faction", kingdoms_begin, kingdoms_end),
		(is_between, ":target_faction", kingdoms_begin, kingdoms_end),

		(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":target_faction", ":acting_faction"),
		(eq, reg0, 0),

		(try_begin),
			(party_slot_eq, ":acting_village", slot_center_original_faction, ":target_faction"),
			(call_script, "script_border_incident", ":acting_village", -1),
				(try_begin),
				(eq, "$g_infinite_camping", 0),
				(this_or_next|eq, ":acting_faction", "$players_kingdom"),
				(eq, ":target_faction", "$players_kingdom"),
				(call_script, "script_add_notification_menu", "mnu_notification_border_incident", 0, 0),
				(try_end),
		(else_try),
			(party_slot_eq, ":acting_village", slot_center_ex_faction, ":target_faction"),
			(call_script, "script_border_incident", ":acting_village", -1),
				(try_begin),
				(eq, "$g_infinite_camping", 0),
				(this_or_next|eq, ":acting_faction", "$players_kingdom"),
				(eq, ":target_faction", "$players_kingdom"),
				(call_script, "script_add_notification_menu", "mnu_notification_border_incident", 0, 0),
				(try_end),
		(else_try),
			#(set_fixed_point_multiplier, 1),
			(store_distance_to_party_from_party, ":distance", ":acting_village", ":target_village"),
			(lt, ":distance", 25),
			(call_script, "script_border_incident", ":acting_village", ":target_village"),
				(try_begin),
				(eq, "$g_infinite_camping", 0),
				(this_or_next|eq, ":acting_faction", "$players_kingdom"),
				(eq, ":target_faction", "$players_kingdom"),
				(call_script, "script_add_notification_menu", "mnu_notification_border_incident", 0, 0),
				(try_end),
		(try_end),
	(try_end),
  (assign, reg0, ":save_reg0"),
    ]),

#diplomatic indices
  (20,
   [
    (call_script, "script_find_neighbors"),#first find neighbours
    #(call_script, "script_randomly_start_war_peace_new", 1),

#madsci this fixes a situation where troops can be stuck as prisoners because defeated factions dont ransom their prisoners etc
(try_for_range, ":lord", heroes_begin, heroes_end),
(troop_get_slot, ":cur_prisoner_of_party", ":lord", slot_troop_prisoner_of_party),
(is_between, ":cur_prisoner_of_party", walled_centers_begin, walled_centers_end),
(neg|party_slot_eq, ":cur_prisoner_of_party", slot_town_lord, "trp_player"), #dont release from players towns, the player can do that himself
(store_troop_faction, ":lord_faction", ":lord"),
(store_faction_of_party, ":party_faction", ":cur_prisoner_of_party"),
(this_or_next|eq, ":lord_faction", ":party_faction"),
(faction_slot_eq, ":lord_faction", slot_faction_state, sfs_defeated),
(party_remove_prisoners, ":cur_prisoner_of_party", ":lord", 1),
(call_script, "script_remove_troop_from_prison", ":lord"),
(str_store_troop_name, s4, ":lord"),
(display_message,"@{s4} has been released from captivity."),
(try_end),

	(try_for_parties, ":party_no"), #madsci reduce prisoners in bandit and deserter parties over time so that they dont snowball too much
	(gt, ":party_no", last_static_party),
	(neg|party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
	(store_faction_of_party, ":faction_no", ":party_no"),
	(this_or_next|eq, ":faction_no", "fac_outlaws"), #only bandits and deserters
	(gt, ":faction_no", kingdoms_end),
        (party_get_battle_opponent, ":opponent", ":party_no"),
        (lt, ":opponent", 0), #not in a fight
	(party_get_num_prisoner_stacks, ":num_prisoner_stacks",":party_no"),
	(gt, ":num_prisoner_stacks", 0),
		(try_for_range_backwards, ":stack_no", 0, ":num_prisoner_stacks"),
		(party_prisoner_stack_get_troop_id, ":stack_troop",":party_no",":stack_no"),
		(neg|troop_is_hero, ":stack_troop"),
		(party_prisoner_stack_get_size, ":stack_size",":party_no",":stack_no"),
		(ge, ":stack_size", 5),
		(val_div, ":stack_size", 5),
		(party_remove_prisoners, ":party_no", ":stack_troop", ":stack_size"),
		(try_end),
	(try_end),
    ]),


    (24.0/(number_of_factions),
   [
#madsci lets rework faction AI so that factions dont do their business simultaneously to avoid lag spikes

(val_add, "$checked_faction2", 1),
	(try_begin),
	(neg|is_between, "$checked_faction2", npc_kingdoms_begin, npc_kingdoms_end),
	(assign, "$checked_faction2", npc_kingdoms_begin),
	(try_end),
    (call_script, "script_randomly_start_war_peace_new_for_faction", 1, "$checked_faction2"),

    (try_begin),
        (neg|is_between, "$g_faction_diplomacy", kingdoms_begin, kingdoms_end),
        (assign, "$g_faction_diplomacy", kingdoms_begin),
    (try_end),

    (try_begin),
		(faction_slot_eq, "$g_faction_diplomacy", slot_faction_state, sfs_active),
		(try_for_range, ":faction_2", kingdoms_begin, kingdoms_end),
			(neq, "$g_faction_diplomacy", ":faction_2"),
			(faction_slot_eq, ":faction_2", slot_faction_state, sfs_active),

			#remove provocations
			(store_add, ":slot_truce_days", ":faction_2", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":slot_truce_days", kingdoms_begin),
			(faction_get_slot, ":truce_days", "$g_faction_diplomacy", ":slot_truce_days"),
			(try_begin),
				(ge, ":truce_days", 1),
				(try_begin),
					(eq, ":truce_days", 1),
					(call_script, "script_update_faction_notes", "$g_faction_diplomacy"),
					(lt, "$g_faction_diplomacy", ":faction_2"),
#          (display_log_message, "@The truce between {s1} and {s2} has expired"),
#					(call_script, "script_add_notification_menu", "mnu_notification_truce_expired", "$g_faction_diplomacy", ":faction_2"),
				##diplomacy begin
		##nested diplomacy start+ Replace "magic numbers" with named constants
        (else_try),
          (eq, ":truce_days", dplmc_treaty_tributary_days_expire + 1),#replaced 61
          (call_script, "script_update_faction_notes", "$g_faction_diplomacy"),
          (lt, "$g_faction_diplomacy", ":faction_2"),
          (try_begin),
            (faction_slot_eq, "$g_faction_diplomacy", slot_faction_tributary_of, ":faction_2"),
            (call_script, "script_add_notification_menu", "mnu_dplmc_notification_tribute_expired_1_tribute_of_2", "$g_faction_diplomacy", ":faction_2"),
          (else_try),
            (faction_slot_eq, ":faction_2", slot_faction_tributary_of, "$g_faction_diplomacy"),
            (call_script, "script_add_notification_menu", "mnu_dplmc_notification_tribute_expired_2_tribute_of_1", "$g_faction_diplomacy", ":faction_2"),
          (try_end),
          (faction_set_slot, "$g_faction_diplomacy", slot_faction_tributary_of, 0),
          (faction_set_slot, ":faction_2", slot_faction_tributary_of, 0),
        (else_try),
          (eq, ":truce_days", dplmc_treaty_alliance_days_expire + 1),#replaced 61
          (call_script, "script_update_faction_notes", "$g_faction_diplomacy"),
          (lt, "$g_faction_diplomacy", ":faction_2"),
#          (display_log_message, "@The alliance between {s1} and {s2} has expired"),
 #         (call_script, "script_add_notification_menu", "mnu_dplmc_notification_alliance_expired", "$g_faction_diplomacy", ":faction_2"),
        (else_try),
          (eq, ":truce_days",dplmc_treaty_defense_days_expire + 1),#replaced 41
          (call_script, "script_update_faction_notes", "$g_faction_diplomacy"),
          (lt, "$g_faction_diplomacy", ":faction_2"),
 #         (display_log_message, "@The defensive pact between {s1} and {s2} has expired"),
   #       (call_script, "script_add_notification_menu", "mnu_dplmc_notification_defensive_expired", "$g_faction_diplomacy", ":faction_2"),
        (else_try),
          (eq, ":truce_days", dplmc_treaty_trade_days_expire + 1),#replaced 21
          (call_script, "script_update_faction_notes", "$g_faction_diplomacy"),
          (lt, "$g_faction_diplomacy", ":faction_2"),
   #       (display_log_message, "@The trade agreement between {s1} and {s2} has expired"),
   #       (call_script, "script_add_notification_menu", "mnu_dplmc_notification_trade_expired", "$g_faction_diplomacy", ":faction_2"),
  	    ##nested diplomacy end+
        ##diplomacy end
				(try_end),
				(val_sub, ":truce_days", 1),
				(faction_set_slot, "$g_faction_diplomacy", ":slot_truce_days", ":truce_days"),
			(try_end),

			(store_add, ":slot_provocation_days", ":faction_2", slot_faction_provocation_days_with_factions_begin),
			(val_sub, ":slot_provocation_days", kingdoms_begin),
			(faction_get_slot, ":provocation_days", "$g_faction_diplomacy", ":slot_provocation_days"),
			(try_begin),
				  (ge, ":provocation_days", 1),
          (try_begin),#factions already at war
              (store_relation, ":relation", "$g_faction_diplomacy", ":faction_2"),
              (lt, ":relation", 0),
              (faction_set_slot, "$g_faction_diplomacy", ":slot_provocation_days", 0),
          (else_try), #Provocation expires
              (eq, ":provocation_days", 1),
              (try_begin),
                  (faction_slot_eq, "$g_faction_diplomacy", slot_faction_leader, "trp_player"),
                  (call_script, "script_add_notification_menu", "mnu_notification_casus_belli_decide_player", "$g_faction_diplomacy", ":faction_2"),
              (else_try),
                  (call_script, "script_add_notification_menu", "mnu_notification_casus_belli_decide", "$g_faction_diplomacy", ":faction_2"),
              (try_end),
              (faction_set_slot, "$g_faction_diplomacy", ":slot_provocation_days", 0),
          (else_try),
              (val_sub, ":provocation_days", 1),
              (faction_set_slot, "$g_faction_diplomacy", ":slot_provocation_days", ":provocation_days"),
          (try_end),
			(try_end),

			(try_begin), #at war
				(store_relation, ":relation", "$g_faction_diplomacy", ":faction_2"),
				(lt, ":relation", 0),
				(store_add, ":slot_war_damage", ":faction_2", slot_faction_war_damage_inflicted_on_factions_begin),
				(val_sub, ":slot_war_damage", kingdoms_begin),
				(faction_get_slot, ":war_damage", "$g_faction_diplomacy", ":slot_war_damage"),
				(val_add, ":war_damage", 1),
				(faction_set_slot, "$g_faction_diplomacy", ":slot_war_damage", ":war_damage"),
			(try_end),

		(try_end),
		(call_script, "script_update_faction_notes", "$g_faction_diplomacy"),
	(try_end),

    (val_add, "$g_faction_diplomacy", 1),
    ]),

  # Give some xp to hero parties
   (48.0/(number_of_active_npcs),#48hours on average
   [
       ##diplomacy start+
       ##change to allow promoted kingdom ladies to hire troops
       #(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
       (store_random_in_range, ":troop_no", heroes_begin, heroes_end),
       (try_begin),
       ##diplomacy end+
         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),

         (troop_get_slot, ":hero_party", ":troop_no", slot_troop_leaded_party),
         (gt, ":hero_party", 0),
         (party_is_active, ":hero_party"),

         (store_skill_level, ":trainer_level", skl_trainer, ":troop_no"),
         (val_add, ":trainer_level", 5), #average trainer level is 3 for npc lords, worst : 0, best : 6
         (store_mul, ":xp_gain", ":trainer_level", 1000), #xp gain in two days of period for each lord, average : 8000.

         (assign, ":max_accepted_random_value", 30),
         (try_begin),
           (store_troop_faction, ":cur_troop_faction", ":troop_no"),
           (neq, ":cur_troop_faction", "$players_kingdom"),

           (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
           (try_begin),
             (eq, ":reduce_campaign_ai", 0), #hard (1.5x)
             (assign, ":max_accepted_random_value", 35),
             (val_mul, ":xp_gain", 3),
             (val_div, ":xp_gain", 2),
           (else_try),
             (eq, ":reduce_campaign_ai", 2), #easy (0.5x)
             (assign, ":max_accepted_random_value", 25),
             (val_div, ":xp_gain", 2),
           (try_end),
         (try_end),

         (store_random_in_range, ":rand", 0, 100),
         (le, ":rand", ":max_accepted_random_value"),

         (party_upgrade_with_xp, ":hero_party", ":xp_gain"),
       (try_end),

       (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
         (party_get_slot, ":center_lord", ":center_no", slot_town_lord),
         (neq, ":center_lord", "trp_player"),

         (assign, ":xp_gain", 3000), #xp gain in two days of period for each center, average : 3000.

         (assign, ":max_accepted_random_value", 30),
         (try_begin),
           (assign, ":cur_center_lord_faction", -1),
           (try_begin),
             (ge, ":center_lord", 0),
             (store_troop_faction, ":cur_center_lord_faction", ":center_lord"),
           (try_end),
           (neq, ":cur_center_lord_faction", "$players_kingdom"),

           (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
           (try_begin),
             (eq, ":reduce_campaign_ai", 0), #hard (1.5x)
             (assign, ":max_accepted_random_value", 35),
             (val_mul, ":xp_gain", 3),
             (val_div, ":xp_gain", 2),
           (else_try),
             (eq, ":reduce_campaign_ai", 2), #easy (0.5x)
             (assign, ":max_accepted_random_value", 25),
             (val_div, ":xp_gain", 2),
           (try_end),
         (try_end),

         (store_random_in_range, ":rand", 0, 100),
         (le, ":rand", ":max_accepted_random_value"),

         (party_upgrade_with_xp, ":center_no", ":xp_gain"),
       (try_end),
    ]),

  # Process sieges
   (24,
   [
       (call_script, "script_process_sieges"),
    ]),

  # Process village raids
   (2,
   [
       (call_script, "script_process_village_raids"),
    ]),


  # Decide vassal ai obsolete trigger
   (7,
    []),


   (24.0/(number_of_active_npcs),
    [
	##diplomacy start+ Add support for promoted kingdom ladies
	##OLD:
	#(try_for_range, ":kingdom_hero", active_npcs_begin, active_npcs_end),
	##NEW:
	(store_random_in_range, ":kingdom_hero", heroes_begin, heroes_end),

    (try_begin),
		(this_or_next|is_between, ":kingdom_hero", active_npcs_begin, active_npcs_end),
		(troop_slot_eq, ":kingdom_hero", slot_troop_occupation, slto_kingdom_hero),
	##diplomacy end+
		(troop_get_slot, ":impatience", ":kingdom_hero", slot_troop_intrigue_impatience),
		(val_sub, ":impatience", 5),
		(val_max, ":impatience", 0),
		(troop_set_slot, ":kingdom_hero", slot_troop_intrigue_impatience, ":impatience"),
	(try_end),
	(try_begin),
		(this_or_next|is_between, ":kingdom_hero", active_npcs_begin, active_npcs_end),
		(troop_slot_eq, ":kingdom_hero", slot_troop_occupation, slto_kingdom_hero),
		(neg|main_party_has_troop, ":kingdom_hero"),
		(troop_get_slot, ":controversy", ":kingdom_hero", slot_troop_controversy),
		(ge, ":controversy", 1),
		(val_sub, ":controversy", 2),
		(val_max, ":controversy", 0),
		(troop_set_slot, ":kingdom_hero", slot_troop_controversy, ":controversy"),
	(try_end),
	]),

    (24,
    [
	(troop_get_slot, ":controversy", "trp_player", slot_troop_controversy),
	(val_sub, ":controversy", 2),
	(val_max, ":controversy", 0),
	(troop_set_slot, "trp_player", slot_troop_controversy, ":controversy"),
	]),

    #POLITICAL TRIGGERS
	#POLITICAL TRIGGER #1`
   (8, #increased from 12
    [
	(call_script, "script_cf_random_political_event"),

	#Added Nov 2010 begins - do this twice
	#(call_script, "script_cf_random_political_event"),
	#Added Nov 2010 ends

	#This generates quarrels and occasional reconciliations and interventions
	]),

	#Individual lord political calculations
	#Check for lords without fiefs, auto-defections, etc
   (24.0*7.0/(number_of_active_npcs),
    [
	##diplomacy start+
	#This is fairly complicated, and it was getting nearly unreadable so I reformatted it.
	#The old version is visible in version control.
	(assign, ":save_reg0", reg0),
	(val_add, "$g_lord_long_term_count", 1),
	(try_begin),
		(neg|is_between, "$g_lord_long_term_count", active_npcs_including_player_begin, active_npcs_end),
		(assign, "$g_lord_long_term_count", active_npcs_including_player_begin),
	(try_end),

	##Add political calculations for kingdom ladies.  Just extending the range would
	##slow down the political calculations cycle, which would have possibly-unforeseen results.
	##Instead, add a second iteration to deal with extensions.
	(try_for_range, ":iteration", 0, 2),
		(assign, ":troop_no", "$g_lord_long_term_count"),
		(try_begin),
			(eq, ":iteration", 1),
			(val_sub, ":troop_no", active_npcs_including_player_begin),
			(val_add, ":troop_no", active_npcs_end),
		(try_end),
		#Crude check to make sure that a careless modder (i.e. me) didn't decide it
		#would be a good idea to redefine active_npcs to include kingdom_ladies,
		#which would make the second iteration run off the end of the heroes list.
		(is_between, ":troop_no", active_npcs_including_player_begin, heroes_end),

		#Special handling for trp_player, and get the troop's faction
		(try_begin),
			(eq, ":troop_no", "trp_kingdom_heroes_including_player_begin"),
			(assign, ":troop_no", "trp_player"),
			(assign, ":faction", "$players_kingdom"),
		(else_try),
			(store_faction_of_troop, ":faction", ":troop_no"),
		(try_end),

		(try_begin),
			(eq, "$cheat_mode", 1),
			(str_store_troop_name, s9, ":troop_no"),
			#(display_message, "@{!}DEBUG -- Doing political calculations for {s9}"),
		(try_end),

        #Tally the fiefs owned by the hero, and cache the value in slot.
		#If a lord owns no fiefs, his relations with his liege may deteriorate.
        (try_begin),
			(assign, reg0, 1),#Center points + 1
			(try_for_range, ":center", centers_begin, centers_end),
				(party_slot_eq, ":center", slot_town_lord, ":troop_no"),
				(try_begin),
					(is_between, ":center", towns_begin, towns_end),
					(val_add, reg0, 3),#3 points per town
				(else_try),
					(is_between, ":center", walled_centers_begin, walled_centers_end),
					(val_add, reg0, 2),#2 points per castle
				(else_try),
					(val_add, reg0, 1),#1 point per village
				(try_end),
			(try_end),
			#Update cached total
			(troop_set_slot, ":troop_no", dplmc_slot_troop_center_points_plus_one, reg0),
			#If a lord has no fiefs, relation loss potentially results.
			#Do not apply this to the player.
			(eq, reg0, 1),
			(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
			(neq, ":troop_no", "trp_player"),

			#Don't apply this to the leader
			(faction_get_slot, ":faction_leader", ":faction", slot_faction_leader),
			(gt, ":faction_leader", -1),
			(neq, ":faction_leader", ":troop_no"),
			(neg|troop_slot_eq, ":faction_leader", slot_troop_spouse, ":troop_no"),
			(neg|troop_slot_eq, ":troop_no", slot_troop_spouse, ":faction_leader"),

			(troop_get_slot, ":troop_reputation", ":troop_no", slot_lord_reputation_type),
			(try_begin),
				(this_or_next|eq, ":troop_reputation", lrep_quarrelsome),
				(this_or_next|eq, ":troop_reputation", lrep_selfrighteous),
				(this_or_next|eq, ":troop_reputation", lrep_cunning),
				(eq, ":troop_reputation", lrep_debauched),
				(call_script, "script_troop_change_relation_with_troop", ":troop_no", ":faction_leader", -4),
				(val_add, "$total_no_fief_changes", -4),
			(else_try),
				(this_or_next|eq, ":troop_reputation", lrep_ambitious),#add support for lady personalities
				(eq, ":troop_reputation", lrep_martial),
				(call_script, "script_troop_change_relation_with_troop", ":troop_no", ":faction_leader", -2),
				(val_add, "$total_no_fief_changes", -2),
			(try_end),
        (try_end),

        #Auto-indictment or defection
        (try_begin),
			(this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
			(eq, ":troop_no", "trp_player"),

			#There must be a valid faction leader.  The faction leader won't defect from his own kingdom.
			#To avoid certain potential complications, also skip the defection/indictment check for the
			#spouse of the faction leader.  (Code to make that possible can be added elsewhere if
			#necessary.)
			(faction_get_slot, ":faction_leader", ":faction", slot_faction_leader),
			(gt, ":faction_leader", -1),
			(neq, ":troop_no", ":faction_leader"),
			(neg|troop_slot_eq, ":troop_no", slot_troop_spouse, ":faction_leader"),
			(neg|troop_slot_eq, ":faction_leader", slot_troop_spouse, ":troop_no"),

          #I don't know why these are necessary, but they appear to be
			(neg|is_between, ":troop_no", kings_begin, kings_end), #SB : range consts
			(neg|is_between, ":troop_no", pretenders_begin, pretenders_end),

            (assign, ":num_centers", 0),
            (try_for_range,":cur_center", walled_centers_begin, walled_centers_end),
                (store_faction_of_party, ":faction_of_center", ":cur_center"),
                (eq, ":faction_of_center", ":faction"),
                (val_add, ":num_centers", 1),
            (try_end),

            #we are counting num_centers to allow defection although there is high relation between faction leader and troop.
            #but this rule should not applied for player's faction and player_supporters_faction so thats why here 1 is added to num_centers in that case.
            (try_begin),
                (this_or_next|eq, ":faction", "$players_kingdom"),
                (eq, ":faction", "fac_player_supporters_faction"),
                (val_add, ":num_centers", 1),
            (try_end),

            (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),
            (this_or_next|le, reg0, -50), #was -75
            (eq, ":num_centers", 0), #if there is no walled centers that faction has defection happens 100%.

            (call_script, "script_cf_troop_can_intrigue", ":troop_no", 0), #Should include battle, prisoner, in a castle with others

            (store_random_in_range, ":rand", 0, 4),
            (le, ":rand", 1),

            #The more centralized the faction, the greater the chance the liege will indict
            #the lord before he defects.
            (faction_get_slot, reg0, ":faction", dplmc_slot_faction_centralization),
            (val_clamp, reg0, -3, 4),
            (val_add, reg0, 10),#7 minimum, 13 maximum
            (store_random_in_range, ":random", 0, reg0),
            #Random  < 5: The lord defects
            #Random >= 5: The liege indicts the lord for treason

            (try_begin),
                #(this_or_next|eq, ":num_centers", 0), #Thanks Caba`drin & Osviux
		(eq, ":num_centers", 0),
                (store_random_in_range, ":who_moves_first", 0, 2),
                (neq, ":who_moves_first", 0),
                (lt, ":random", 5),
                (neq, ":troop_no", "trp_player"),
                #do a defection
                (try_begin),
                    (neq, ":num_centers", 0),
                    #Note that I assign the troop number instead of 1 as is done in Native
                    (assign, "$g_give_advantage_to_original_faction", ":troop_no"),
                (try_end),
                #(assign, "$g_give_advantage_to_original_faction", 1),

                (store_faction_of_troop, ":orig_faction", ":troop_no"),
                (call_script, "script_lord_find_alternative_faction", ":troop_no"),
                (assign, ":new_faction", reg0),
                (assign, "$g_give_advantage_to_original_faction", 0),
                (try_begin),
                    (neq, ":new_faction", ":orig_faction"),
                    (is_between, ":new_faction", kingdoms_begin, kingdoms_end),
                    (str_store_troop_name_link, s1, ":troop_no"),
                    (str_store_faction_name_link, s2, ":new_faction"),
                    (str_store_faction_name_link, s3, ":faction"),
                    (call_script, "script_dplmc_store_troop_is_female", ":troop_no"),
                    (assign, reg4, reg0),
                    #SB : factionalize colors
                    (str_store_string, s4, "str_lord_defects_ordinary"),
                    (faction_get_color, ":color", ":new_faction"),
                    (display_log_message, "@{s4}", ":color"),
                    (call_script, "script_change_troop_faction", ":troop_no", ":new_faction"),
                    (try_begin),
                        #(eq, "$cheat_mode", 1),
                        (this_or_next|eq, ":new_faction", "$players_kingdom"),
                        (eq, ":faction", "$players_kingdom"),
                        (call_script, "script_add_notification_menu", "mnu_notification_lord_defects", ":troop_no", ":faction"),
                    (try_end),
                (try_end),
            (else_try),
                (neq, ":faction_leader", "trp_player"),
                (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),
                (le, reg0, -50), #was -75
                (call_script, "script_indict_lord_for_treason", ":troop_no", ":faction"),
            (try_end),

			#Update :faction if it has changed
			(try_begin),
				(eq, ":troop_no", "trp_player"),
				(assign, reg0, "$players_kingdom"),
			(else_try),
				(store_faction_of_troop, reg0, ":troop_no"),
			(try_end),
			(neq, reg0, ":faction"),#Fall through if indictment/defection didn't happen
			(assign, ":faction", reg0),
		(else_try),  #Take a stand on an issue
			(neq, ":troop_no", "trp_player"),
			(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
			(faction_slot_ge, ":faction", slot_faction_political_issue, 1),
			#This bit of complication is needed for savegame compatibility -- if zero is in the slot, they'll choose anyway
			(neg|troop_slot_ge, ":troop_no", slot_troop_stance_on_faction_issue, 1),
			(this_or_next|troop_slot_eq, ":troop_no", slot_troop_stance_on_faction_issue, -1),
				(neq, "$players_kingdom", ":faction"),

			(call_script, "script_npc_decision_checklist_take_stand_on_issue", ":troop_no"),
			(troop_set_slot, ":troop_no", slot_troop_stance_on_faction_issue, reg0),
        (else_try),
			#OPTIONAL CHANGE (AI CHANGES HIGH):
			(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_HIGH),
			#If an AI kingdom has fiefless lords and no free fiefs, the king
			#will consider giving up a village.  The king will not give up fiefs if
			#doing so would give him less territory than another lord of his faction.
			#(For simplicity, the AI will not do this while a marshall appointment
			#is pending.)
			(faction_slot_eq, ":faction", slot_faction_leader, ":troop_no"),
			(neq, ":troop_no", "trp_player"),
			#With fewer than 3 points we don't need to bother continuing, since 2 points means he only owns a single village.
         (troop_get_slot, ":local_temp", ":troop_no", dplmc_slot_troop_center_points_plus_one),
			(ge, ":local_temp", 3),
			#Don't do this while other business is pending
			(neg|faction_slot_ge, ":faction", slot_faction_political_issue, 1),
			#Find the fiefless lord of his faction that the king likes best.
			#Terminate the search early if he finds another lord whose fiefs
			#equal or exceed his own, or a lord whose fief point slot is not
			#initialized.
			(assign, ":end_cond", heroes_end),
			(assign, ":any_found", -200),
			(assign, ":best_active_npc", -1),
			(try_for_range, ":active_npc", heroes_begin, ":end_cond"),
				(neq, ":active_npc", ":troop_no"),
				(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
				(store_faction_of_troop, reg0, ":active_npc"),
				(eq, reg0, ":faction"),
				(troop_get_slot, reg0, ":active_npc", dplmc_slot_troop_center_points_plus_one),
				(try_begin),
					#Terminate.  The king cannot give up any points without being outfieffed (if he isn't already)
					(ge, reg0, ":local_temp"),
					(assign, ":end_cond", ":active_npc"),
				(else_try),
					#Terminate.  The first pass of political calculations aren't done, or things are in flux.
					(lt, reg0, 1),
					(assign, ":end_cond", ":active_npc"),
				(else_try),
					(eq, reg0, 1),
					(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":active_npc"),
					(gt, reg0, ":any_found"),
					(assign, ":any_found", reg0),
					(assign, ":best_active_npc", ":active_npc"),
				(try_end),
			(try_end),
			(eq, ":end_cond", heroes_end),
			(is_between, ":best_active_npc", heroes_begin, heroes_end),
			(gt, ":any_found", -10),
			#Give up the least prosperous fief.
			(assign, ":local_temp", 101),
			(assign, ":any_found", -1),
			(try_for_range, ":center", villages_begin, villages_end),
				(party_slot_eq, ":center", slot_town_lord, ":troop_no"),
				(party_get_slot, reg0, ":center", slot_town_prosperity),
				(this_or_next|eq, ":any_found", -1),
				(lt, reg0, ":local_temp"),
				(assign, ":local_temp", reg0),
				(assign, ":any_found", ":center"),
			(try_end),
			#Clear village's lord
			(is_between, ":any_found", centers_begin, centers_end),
			(party_set_slot, ":any_found", slot_town_lord, -1),
			(troop_get_slot, reg0, ":troop_no", dplmc_slot_troop_center_points_plus_one),
			(val_sub, reg0, 1),
			(troop_set_slot, ":troop_no", dplmc_slot_troop_center_points_plus_one, reg0),
			(str_store_party_name_link, s4, ":any_found"),
			(str_store_troop_name_link, s5, ":troop_no"),
			(str_store_faction_name_link, s7, ":faction"),
            		(faction_get_color, ":color", ":faction"), #SB : color message
			(display_log_message, "@{s5} has decided to grant {s4} to another lord of the {s7}.", ":color"),
			#Reset faction issue
			(try_for_range, ":active_npc", heroes_begin, heroes_end),
				(store_faction_of_troop, reg0, ":active_npc"),
				(eq, reg0, ":faction"),
				(troop_set_slot, ":troop_no", slot_troop_stance_on_faction_issue, -1),
			(try_end),
			(store_current_hours, reg0),
			(faction_set_slot, ":faction", slot_faction_political_issue_time, reg0),
				(try_begin),
				(gt, ":any_found", 0),
				(faction_set_slot, ":faction", slot_faction_political_issue, ":any_found"),
				(else_try),
				(faction_set_slot, ":faction", slot_faction_political_issue, 0), #madsci this has to be 0 not -1
				(try_end),
			#Set the liege's position on the issue, since he gave up the village with
			#something specific in mind.
			(troop_set_slot, ":troop_no", slot_troop_stance_on_faction_issue, ":best_active_npc"),
		(try_end),

		#Reduce grudges over time
		(try_begin),
			#Skip this for the dead
			(neg|troop_slot_eq, ":troop_no", slot_troop_occupation, dplmc_slto_dead),
			#Do not perform this for kingdom ladies, since it will potentially mess up courtship.
			(neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_lady),

			(try_for_range, ":active_npc", heroes_begin, heroes_end),
				(neq, ":active_npc", ":troop_no"),
				(neg|troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_lady),#Don't do for ladies
				(neg|troop_slot_eq, ":active_npc", slot_troop_occupation, dplmc_slto_dead),#Don't do for the dead

				#Fix: there are some NPCs that have "initial" relations with the player set,
				#but they can decay before ever meeting him, so keep them until the first meeting.
				(this_or_next|neq, ":troop_no", "trp_player"),
				(troop_slot_ge, ":troop_no", slot_troop_met, 1),

				(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":active_npc"),
				(lt, reg0, 0),
				(store_sub, ":chance_of_convergence", 0, reg0),
				(store_random_in_range, ":random", 0, 300),
				(lt, ":random", ":chance_of_convergence"),
				(call_script, "script_troop_change_relation_with_troop", ":troop_no", ":active_npc", 1),
				(val_add, "$total_relation_changes_through_convergence", 1),
			(try_end),

			#Accelerate forgiveness for lords in exile (with their original faction only)
			(neq, ":troop_no", "trp_player"),
			(troop_slot_eq, ":troop_no", slot_troop_occupation, dplmc_slto_exile),
			(troop_get_slot, ":original_faction", ":troop_no", slot_troop_original_faction),
			(gt, ":original_faction", 0),

			(try_for_range, ":active_npc", heroes_begin, heroes_end),
				(neq, ":active_npc", ":troop_no"),
				(neg|troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_lady),#Don't do for ladies
				(neg|troop_slot_eq, ":active_npc", slot_troop_occupation, dplmc_slto_dead),#Don't do for the dead
				#Only apply to heroes with the same original faction
				(troop_slot_eq, ":active_npc", slot_troop_original_faction, ":original_faction"),
				(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":active_npc"),
				(lt, reg0, 0),
				(store_sub, ":chance_of_convergence", 0, reg0),
				(store_random_in_range, ":random", 0, 300),
				(lt, ":random", ":chance_of_convergence"),
				(call_script, "script_troop_change_relation_with_troop", ":troop_no", ":active_npc", 1),
				(val_add, "$total_relation_changes_through_convergence", 1),
			(try_end),
		(try_end),
	#Finish loop over the ":iteration" variable.
	(try_end),
	(assign, reg0, ":save_reg0"),
	##diplomacy end+
   ]),

#madsci new process alarms is less laggy
(3,
	[
	  (try_for_range, ":center_no", centers_begin, centers_end),
	    (try_begin), #if raided, sieged and only once!
	      (this_or_next|party_slot_ge, ":center_no", slot_center_is_besieged_by, 0),
	      (party_slot_eq, ":center_no", slot_village_state, svs_being_raided),
		  (party_slot_eq, ":center_no", slot_center_last_spotted_enemy, -1), #if this is not set yet
		  (call_script, "script_process_alarms_new", ":center_no"),
		(else_try), #not raided/sieged - reset the sorties
		  (this_or_next|neg|party_slot_ge, ":center_no", slot_center_is_besieged_by, 0),
	      (neg|party_slot_eq, ":center_no", slot_village_state, svs_being_raided),
		  (party_set_slot, ":center_no", slot_center_last_spotted_enemy, -1),
          (party_set_slot, ":center_no", slot_center_sortie_strength, 0),
          (party_set_slot, ":center_no", slot_center_sortie_enemy_strength, 0),
		(try_end),
	  (try_end),
	]),

   (1,
   [
    (call_script, "script_process_kingdom_parties_ai"),

(try_begin),
(check_quest_active, "qst_destroy_deserters"),
(neg|check_quest_succeeded, "qst_destroy_deserters"),
(neg|check_quest_failed, "qst_destroy_deserters"),
(quest_get_slot, ":quest_target_party", "qst_destroy_deserters", slot_quest_target_party),
(this_or_next|le, ":quest_target_party", 0),
(neg|party_is_active, ":quest_target_party"),
(call_script, "script_succeed_quest", "qst_destroy_deserters"),
(try_end),

(try_begin),
(check_quest_active, "qst_kill_slavers"),
(neg|check_quest_succeeded, "qst_kill_slavers"),
(neg|check_quest_failed, "qst_kill_slavers"),
(quest_get_slot, ":quest_target_party", "qst_kill_slavers", slot_quest_target_party),
(quest_get_slot, ":village_no", "qst_kill_slavers", slot_quest_object_center),
	(try_begin),
	(this_or_next|le, ":quest_target_party", 0),
	(neg|party_is_active, ":quest_target_party"),
	(call_script, "script_succeed_quest", "qst_kill_slavers"),
	(else_try),
	(gt, ":quest_target_party", 0),
	(party_is_in_any_town, ":quest_target_party"),
	(party_get_cur_town, ":attached_to_party", ":quest_target_party"),
	(party_set_flags, ":quest_target_party", pf_quest_party, 0),
		(try_begin),
		(eq, ":attached_to_party", ":village_no"),
		(str_store_party_name, s7, ":village_no"),
		(display_message, "@The slavers have taken villagers from {s7}!"),
		(call_script, "script_change_player_relation_with_center", ":village_no", -3),
		(party_add_prisoners, ":quest_target_party", "trp_peasant_woman", 10),
		(party_set_flags, ":quest_target_party", pf_quest_party, 0),
		(party_set_ai_behavior, ":quest_target_party", ai_bhvr_patrol_party),
		(party_set_ai_object, ":quest_target_party", ":village_no"),
		(party_set_flags, ":quest_target_party", pf_default_behavior, 0),
		(party_set_faction, ":quest_target_party", "fac_outlaws"),
		(call_script, "script_abort_quest", "qst_kill_slavers", 0),
		(else_try),
		(call_script, "script_remove_hero_prisoners", ":quest_target_party"),
			(try_begin),
			(eq, ":quest_target_party", "$capturer_party"),
			(assign, "$capturer_party", ":attached_to_party"),
			(try_end),
		(call_script, "script_cancel_quest", "qst_kill_slavers"),
		(remove_party, ":quest_target_party"),
		(try_end),
	(try_end),
(try_end),

	(try_begin),
		(check_quest_active,"qst_scout_enemy_town"),
		(neg|check_quest_succeeded, "qst_scout_enemy_town"),
		(quest_get_slot, ":quest_target_center", "qst_scout_enemy_town", slot_quest_target_center),
		(quest_get_slot, ":quest_target_visited", "qst_scout_enemy_town", slot_quest_target_troop),
		(try_begin),
			(eq, ":quest_target_visited", 0),
			(store_distance_to_party_from_party, ":distance", ":quest_target_center", "p_main_party"),
			(le, ":distance", 3),
			(assign, ":quest_target_visited", 1),
			(str_store_party_name_link, s1, ":quest_target_center"),
			(display_message, "@{s1} is scouted."),
		(try_end),
		(eq, ":quest_target_visited", 1),
		(quest_set_slot, "qst_scout_enemy_town", slot_quest_target_troop, ":quest_target_visited"),
		(call_script, "script_succeed_quest", "qst_scout_enemy_town"),
	(try_end),

	(try_begin),
		(check_quest_active,"qst_capture_enemy_hero"),
		(neg|check_quest_succeeded, "qst_capture_enemy_hero"),
		(quest_get_slot, ":quest_giver", "qst_capture_enemy_hero", slot_quest_giver_troop),
		(gt, ":quest_giver", 0),
		(store_troop_faction, ":giver_faction", ":quest_giver"),
		(quest_get_slot, ":quest_target", "qst_capture_enemy_hero", slot_quest_target_faction),
		(gt, ":quest_target", 0),
		(store_relation, ":relation", ":giver_faction", ":quest_target"),
		(this_or_next|eq, ":giver_faction", ":quest_target"),
		(ge, ":relation", 0),
		(call_script, "script_cancel_quest", "qst_capture_enemy_hero"),
	(try_end),

   ]),

  # Process alarms - perhaps break this down into several groups, with a modula
   (1, #this now calls 1/3 of all centers each time, thus hopefully lightening the CPU load
   [
    (call_script, "script_allow_vassals_to_join_indoor_battle"),

(assign, ":spotting", 3),
(try_begin),
(call_script, "script_get_max_skill_of_player_party", "skl_spotting"),
(assign, ":skill", reg0),
(gt, ":skill", 1),
(val_div, ":skill", 2),
(val_add, ":spotting", ":skill"),
(try_end),

    	(try_begin),
      	(quest_slot_eq, "qst_ernak_quest", slot_quest_target_onoguroi, 2),
      	(store_distance_to_party_from_party, ":distance", "p_main_party", "p_camp_of_tatra"),
      	(lt, ":distance", ":spotting"),
      	(quest_set_slot, "qst_ernak_quest", slot_quest_target_onoguroi, 3),
      	(party_set_flags, "p_camp_of_tatra", pf_disabled, 0),
      	(party_set_flags, "p_camp_of_tatra", pf_always_visible, 1),
      	(tutorial_box, "@You found the camp of Tatra. Report back to the Onoguroi chief.", "@Camp found!"),
	(try_end),

    	(try_for_parties, ":bandit_camp"),
      	(gt, ":bandit_camp", last_static_party), #madsci
      	(party_get_template_id, ":template", ":bandit_camp"), #SB : fix template range
		(try_begin),
		(this_or_next|eq, ":template", "pt_slave_hideout"),
      		(is_between, ":template", "pt_steppe_bandit_lair", "pt_bandit_lair_templates_end"),
      		(store_distance_to_party_from_party, ":distance", "p_main_party", ":bandit_camp"),
      		(lt, ":distance", ":spotting"),
      		(party_set_flags, ":bandit_camp", pf_disabled, 0),
      		(party_set_flags, ":bandit_camp", pf_always_visible, 1),
			(try_begin),
			(eq, ":template", "pt_slave_hideout"),
			(this_or_next|neg|check_quest_active, "qst_return_slave"),
			(neg|quest_slot_eq, "qst_return_slave", slot_quest_target_party, ":bandit_camp"),
			(remove_party, ":bandit_camp"),
			(try_end),
		(try_end),
    (try_end),
   ]),

  # Process siege ai
   (.024, #was 3, changed to 1/3 avg, 123 walled centers = ~0.024
   [
      ##diplomacy start+
	  (assign, ":save_reg0", reg0),#Save registers
	  (assign, ":save_reg1", reg1),
	  ##diplomacy end+
      (store_current_hours, ":cur_hours"),
      (store_random_in_range, ":center_no", walled_centers_begin, walled_centers_end),
      (try_begin),
        (party_get_slot, ":besieger_party", ":center_no", slot_center_is_besieged_by),
        (gt, ":besieger_party", 0),
        (party_is_active, ":besieger_party"),
        (store_faction_of_party, ":besieger_faction", ":besieger_party"),
        (party_slot_ge, ":center_no", slot_center_is_besieged_by, 1),
        (party_get_slot, ":siege_begin_hours", ":center_no", slot_center_siege_begin_hours),
        (store_sub, ":siege_begin_hours", ":cur_hours", ":siege_begin_hours"),
        (assign, ":launch_attack", 0),
        (assign, ":call_attack_back", 0),
        (assign, ":attacker_strength", 0),
        (assign, ":marshall_attacking", 0),
        (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
          (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
          (gt, ":party_no", 0),
          (party_is_active, ":party_no"),

          (store_troop_faction, ":troop_faction_no", ":troop_no"),
          (eq, ":troop_faction_no", ":besieger_faction"),
          (assign, ":continue", 0),
          (try_begin),
            (party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
            (party_slot_eq, ":party_no", slot_party_ai_object, ":center_no"),
            (assign, ":continue", 1),
          (else_try),
            (party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
            (party_get_slot, ":commander_party", ":party_no", slot_party_ai_object),
            (gt, ":commander_party", 0),
            (party_is_active, ":commander_party"),
            (party_slot_eq, ":commander_party", slot_party_ai_state, spai_besieging_center),
            (party_slot_eq, ":commander_party", slot_party_ai_object, ":center_no"),
            (assign, ":continue", 1),
          (try_end),
          (eq, ":continue", 1),
          (party_get_battle_opponent, ":opponent", ":party_no"),
          (this_or_next|lt, ":opponent", 0),
          (eq, ":opponent", ":center_no"),
          (try_begin),
            (faction_slot_eq, ":besieger_faction", slot_faction_marshall, ":troop_no"),
            (assign, ":marshall_attacking", 1),
          (try_end),
          (call_script, "script_party_calculate_regular_strength", ":party_no"),
		  ##diplomacy start+ terrain advantage
		  (try_begin),
			(ge, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
			(call_script, "script_dplmc_party_calculate_strength_in_terrain", ":party_no", dplmc_terrain_code_siege, 0, 0),
          (try_end),
		  ##diplomacy end+
          (val_add, ":attacker_strength", reg0),
        (try_end),
        (try_begin),
          (gt, ":attacker_strength", 0),
          (party_collect_attachments_to_party, ":center_no", "p_collective_enemy"),
          (call_script, "script_party_calculate_regular_strength", "p_collective_enemy"),
		  ##diplomacy start+ terrain advantage
		  (try_begin),
			(ge, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
			(call_script, "script_dplmc_party_calculate_strength_in_terrain", "p_collective_enemy", dplmc_terrain_code_siege, 0, 0),
          (try_end),
		  ##diplomacy end+
          (assign, ":defender_strength", reg0),
          (try_begin),
            (eq, "$auto_enter_town", ":center_no"),
            (eq, "$g_player_is_captive", 0),
            (call_script, "script_party_calculate_regular_strength", "p_main_party"),
			##diplomacy start+ terrain advantage
			(try_begin),
				(ge, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
				(call_script, "script_dplmc_party_calculate_strength_in_terrain", "p_collective_enemy", dplmc_terrain_code_siege, 0, 0),
			(try_end),
			##diplomacy end+
            (val_add, ":defender_strength", reg0),
            (val_mul, ":attacker_strength", 2), #double the power of attackers if the player is in the campaign
          (try_end),
          (party_get_slot, ":siege_hardness", ":center_no", slot_center_siege_hardness),
          (val_add, ":siege_hardness", 100),
          (val_mul, ":defender_strength", ":siege_hardness"),
          (val_div, ":defender_strength", 100),
          (val_max, ":defender_strength", 1),
          (try_begin),
            (eq, ":marshall_attacking", 1),
            (eq, ":besieger_faction", "$players_kingdom"),
            (check_quest_active, "qst_follow_army"),
            (val_mul, ":attacker_strength", 2), #double the power of attackers if the player is in the campaign
          (try_end),
          (store_mul, ":strength_ratio", ":attacker_strength", 100),
          (val_div, ":strength_ratio", ":defender_strength"),
          (store_sub, ":random_up_limit", ":strength_ratio", 250), #was 300 (1.126)

          (try_begin),
            (gt, ":random_up_limit", -100), #never attack if the strength ratio is less than 150%
            (store_div, ":siege_begin_hours_effect", ":siege_begin_hours", 2), #was 3 (1.126)
            (val_add, ":random_up_limit", ":siege_begin_hours_effect"),
          (try_end),

          (val_div, ":random_up_limit", 5),
          (val_max, ":random_up_limit", 0),
          (store_sub, ":random_down_limit", 175, ":strength_ratio"), #was 200 (1.126)
          (val_max, ":random_down_limit", 0),
          (try_begin),
            (store_random_in_range, ":rand", 0, 100),
            (lt, ":rand", ":random_up_limit"),
            (gt, ":siege_begin_hours", 24),#initial preparation
            (assign, ":launch_attack", 1),
          (else_try),
            (store_random_in_range, ":rand", 0, 100),
            (lt, ":rand", ":random_down_limit"),
            (assign, ":call_attack_back", 1),
          (try_end),
        (else_try),
          (assign, ":call_attack_back", 1),
        (try_end),

        #Assault the fortress
        (try_begin),
          (eq, ":launch_attack", 1),
          (call_script, "script_begin_assault_on_center", ":center_no"),
        (else_try),
          (eq, ":call_attack_back", 1),
          (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
            (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
            (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
            (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
            (gt, ":party_no", 0),
            (party_is_active, ":party_no"),

            (party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
            (party_slot_eq, ":party_no", slot_party_ai_object, ":center_no"),
            (party_slot_eq, ":party_no", slot_party_ai_substate, 1),
            (call_script, "script_party_set_ai_state", ":party_no", spai_undefined, -1),
            (call_script, "script_party_set_ai_state", ":party_no", spai_besieging_center, ":center_no"),
            #resetting siege begin time if at least 1 party retreats
            (party_set_slot, ":center_no", slot_center_siege_begin_hours, ":cur_hours"),
          (try_end),
        (try_end),
      (try_end),
	  ##diplomacy start+
	  #Revert registers
	  (assign, reg0, ":save_reg0"),
	  (assign, reg1, ":save_reg1"),
	  ##diplomacy end+
    ]),

    # this simple trigger is useless so lets put low priority quest stuff there
    (3,
    [
(try_begin), #madsci make troublesome bandits patrol around their original center so that the player doesnt have to hunt them across the map
(check_quest_active, "qst_troublesome_bandits"),
(neg|check_quest_succeeded, "qst_troublesome_bandits"),
(neg|check_quest_failed, "qst_troublesome_bandits"),
(quest_get_slot, ":quest_target_party", "qst_troublesome_bandits", slot_quest_target_party),
(gt, ":quest_target_party", 0),
(party_is_active, ":quest_target_party"),
(party_get_slot, ":home_center", ":quest_target_party", slot_party_home_center),
(gt, ":home_center", 0),
(party_set_ai_behavior, ":quest_target_party", ai_bhvr_patrol_party),
(party_set_ai_object, ":quest_target_party", ":home_center"),
(try_end),

(try_begin), 
(check_quest_active, "qst_kill_slavers"),
(neg|check_quest_succeeded, "qst_kill_slavers"),
(neg|check_quest_failed, "qst_kill_slavers"),
(quest_get_slot, ":quest_target_party", "qst_kill_slavers", slot_quest_target_party),
(gt, ":quest_target_party", 0),
(party_is_active, ":quest_target_party"),
(party_get_slot, ":home_center", ":quest_target_party", slot_party_home_center),
(gt, ":home_center", 0),
(party_set_ai_behavior, ":quest_target_party", ai_bhvr_travel_to_party),
(party_set_ai_object, ":quest_target_party", ":home_center"),
(try_end),

(try_begin),
(check_quest_active, "qst_ernak_quest"), #cancel this quest if Ernak somehow ends up being unavailable
(store_troop_faction, ":kingdom_hero_faction", "trp_knight_23_8"),
(this_or_next|faction_slot_eq, "fac_minor_kutriguroi", slot_faction_state, sfs_defeated),
(this_or_next|faction_slot_eq, "fac_minor_onoguroi", slot_faction_state, sfs_defeated),
(this_or_next|faction_slot_eq, "fac_minor_saraguroi", slot_faction_state, sfs_defeated),
(this_or_next|eq, ":kingdom_hero_faction", "fac_outlaws"),
(neg|troop_slot_eq, "trp_knight_23_8", slot_troop_occupation, slto_kingdom_hero),
(call_script, "script_cancel_quest", "qst_ernak_quest"),
(quest_set_slot, "qst_ernak_quest", slot_quest_current_state, -2),
(try_end),

(assign, ":end", "qst_haddingrs_revenge"),
(val_add, ":end", 1),
(try_for_range, ":quest", "qst_finnsburh_quest", ":end"), #madsci cancel quest if quest parties are razed by the player for some reason
(check_quest_active, ":quest"),
(store_faction_of_party, ":party_faction", "p_dani_village"),
(store_faction_of_party, ":party_faction2", "p_augundzi_village"),
(store_faction_of_party, ":party_faction3", "p_frisian_village"),
(this_or_next|eq, ":party_faction", "fac_neutral"),
(this_or_next|eq, ":party_faction2", "fac_neutral"),
(eq, ":party_faction3", "fac_neutral"),
(call_script, "script_cancel_quest", ":quest"),
(quest_set_slot, ":quest", slot_quest_current_state, -1),
(try_end),

(try_begin),
(neg|check_quest_active, "qst_hunt_down_fugitive"),
(party_count_prisoners_of_type, ":count", "p_main_party", "trp_fugitive"),
(gt, ":count", 0),
(str_store_troop_name_by_count, s10, "trp_fugitive", ":count"),
(party_remove_prisoners, "p_main_party", "trp_fugitive", ":count"),
(display_message, "@{s10} escaped from your party!"),
(try_end),

(try_begin),
(neq, "$g_king_start", 11),
(eq, "$suebi_war_ended", 0),
(faction_slot_eq, "fac_kingdom_8", slot_faction_state, sfs_defeated),
(faction_slot_eq, "fac_kingdom_30", slot_faction_state, sfs_active),
(assign, "$suebi_war_ended", 1),
(str_store_faction_name, s11, "fac_kingdom_30"),
(str_store_string, s10, "str_regnum_suevorum"),
(display_log_message, "@{s11} has won the Suebi civil war and is now known as {s10}"),
(faction_set_name, "fac_kingdom_30", s10),
		(try_begin),
        	(eq, "$g_infinite_camping", 0),
		(assign, "$temp", "fac_kingdom_30"),
		(jump_to_menu, "mnu_suebi_civil_war_ended"),
		(try_end),
(else_try),
(neq, "$g_king_start", 11),
(eq, "$suebi_war_ended", 0),
(faction_slot_eq, "fac_kingdom_30", slot_faction_state, sfs_defeated),
(faction_slot_eq, "fac_kingdom_8", slot_faction_state, sfs_active),
(assign, "$suebi_war_ended", 1),
(str_store_faction_name, s11, "fac_kingdom_8"),
(str_store_string, s10, "str_regnum_suevorum"),
(display_log_message, "@{s11} has won the Suebi civil war and is now known as {s10}"),
(faction_set_name, "fac_kingdom_8", s10),
		(try_begin),
        	(eq, "$g_infinite_camping", 0),
		(assign, "$temp", "fac_kingdom_8"),
		(jump_to_menu, "mnu_suebi_civil_war_ended"),
		(try_end),
(else_try),
(eq, "$g_king_start", 11),
(eq, "$suebi_war_ended", 0),
(faction_slot_eq, "fac_kingdom_30", slot_faction_state, sfs_defeated),
(faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
(assign, "$suebi_war_ended", 1),
(str_store_faction_name, s11, "fac_player_supporters_faction"),
(str_store_string, s10, "str_regnum_suevorum"),
(display_log_message, "@{s11} has won the Suebi civil war and is now known as {s10}"),
(faction_set_name, "fac_kingdom_8", s10),
		(try_begin),
        	(eq, "$g_infinite_camping", 0),
		(assign, "$temp", "fac_player_supporters_faction"),
		(jump_to_menu, "mnu_suebi_civil_war_ended"),
		(try_end),
(try_end),

(try_begin), #madsci end quest if Nero has been defeated by someone else already
(eq, "$nero_army_spawned", 1),
(quest_get_slot, ":target", "qst_nero_larper_quest", slot_quest_target_party),
(gt, ":target", 0),
(neg|party_is_active, ":target"),
(assign, "$nero_army_spawned", -1),
(display_log_message, "@Nero has been defeated!"),
	(try_begin),
	(check_quest_active, "qst_nero_larper_quest"),
	(call_script, "script_cancel_quest", "qst_nero_larper_quest"),
	(quest_set_slot,"qst_nero_larper_quest",slot_quest_current_state, -1),
	(try_end),
(try_end),

(try_begin), #water travel event
(eq, "$g_infinite_camping", 0),
(eq, "$g_player_is_captive", 0),
(neq, "$freelancer_state", 1),
(party_slot_eq, "p_main_party", slot_party_on_water, 1),
(party_get_current_terrain, ":terrain_type", "p_main_party"),
(eq, ":terrain_type", rt_deep_water),
(store_random_in_range, ":rnd", 0, 100),
(eq, ":rnd", 1),
(call_script, "script_party_count_fit_regulars", "p_main_party"),
(gt, reg0, 20),
(jump_to_menu, "mnu_men_drowned"),
(try_end),

(try_begin), #fail the uprising if somehow you end up leaving the town while it's active
(check_quest_active, "qst_jewish_riot"),
(call_script, "script_cancel_quest", "qst_jewish_riot"),
(assign, "$jewish_rebellion", -1),
(display_message, "@The uprising has failed."),
(troop_set_slot, "trp_jewish_agitator", slot_troop_occupation, dplmc_slto_dead),
(try_end),

(try_begin), #fail the uprising if somehow you end up leaving the town while it's active
(check_quest_active, "qst_armenian_riot"),
(call_script, "script_cancel_quest", "qst_armenian_riot"),
(assign, "$armenian_rebellion", -1),
(display_message, "@The uprising has failed."),
(troop_set_slot, "trp_armenian_agitator", slot_troop_occupation, dplmc_slto_dead),
(try_end),

(try_begin),
(check_quest_active, "qst_armenian_kingdom_quest_1"),
(store_faction_of_party, ":party_faction", "p_town_45"),
(neq, ":party_faction", "fac_kingdom_31"),
(call_script, "script_cancel_quest", "qst_armenian_kingdom_quest_1"),
(try_end),
(try_begin),
(check_quest_active, "qst_armenian_kingdom_quest_2"),
(faction_slot_eq, "fac_kingdom_31", slot_faction_state, sfs_defeated),
(call_script, "script_cancel_quest", "qst_armenian_kingdom_quest_2"),
(try_end),
(try_begin),
(check_quest_active, "qst_armenian_kingdom_quest_2"),
(eq, "$players_kingdom", "fac_kingdom_31"),
(call_script, "script_succeed_quest", "qst_armenian_kingdom_quest_2"),
(call_script, "script_finish_quest", "qst_armenian_kingdom_quest_2", 100),
(try_end),

(try_begin),
(check_quest_active, "qst_lend_companion"),
(quest_get_slot, ":quest_giver_troop", "qst_lend_companion", slot_quest_giver_troop),
(neg|troop_slot_eq, ":quest_giver_troop", slot_troop_occupation, slto_kingdom_hero),
(quest_get_slot, ":quest_target_troop", "qst_lend_companion", slot_quest_target_troop),
(troop_set_slot, ":quest_target_troop", slot_troop_current_mission, npc_mission_rejoin_when_possible),
(troop_set_slot, ":quest_target_troop", slot_troop_days_on_mission, 0),
(call_script, "script_abort_quest", "qst_lend_companion", 0),
(try_end),

(try_begin),
(check_quest_active, "qst_destroy_deserters"),
(neg|check_quest_succeeded, "qst_destroy_deserters"),
(neg|check_quest_failed, "qst_destroy_deserters"),
(quest_get_slot, ":quest_target_party", "qst_destroy_deserters", slot_quest_target_party),
(gt, ":quest_target_party", 0),
(party_is_active, ":quest_target_party"),
(quest_get_slot, ":quest_target_center", "qst_destroy_deserters", slot_quest_target_center),
(is_between, ":quest_target_center", centers_begin, centers_end),
(party_get_position, pos1, ":quest_target_center"),
(party_set_ai_behavior, ":quest_target_party", ai_bhvr_patrol_location),
(party_set_ai_target_position, ":quest_target_party", pos1),
(party_set_ai_object, ":quest_target_party", ":quest_target_center"),
(party_set_ai_patrol_radius, ":quest_target_party", 5),
(try_end),
    ]),


#simple trigger 43
  # Decide faction ai flag check
   #(0.11,
    (7/(number_of_factions),
   [
     #(eq, "$g_recalculate_ais", 1),
     #(assign, "$g_recalculate_ais", 0),
     #(call_script, "script_recalculate_ais"),

#madsci new system where faction AI gets decided one by one instead of everyone at the same time to avoid lag spike

(val_add, "$checked_faction", 1),
	(try_begin),
	(neg|is_between, "$checked_faction", kingdoms_begin, kingdoms_end),
	(assign, "$checked_faction", kingdoms_begin),
	(try_end),
(call_script, "script_check_king_has_town", "$checked_faction"),
(call_script, "script_check_lords_but_no_centers", "$checked_faction"),
(call_script, "script_recalculate_ais_for_faction", "$checked_faction"),
   ]),

    # Count faction armies #SB : moved to faction defeat check
    (24,
    [
    (ge, "$cheat_mode", 1),#only do this while in cheat mode

    (try_for_range, ":active_npc", heroes_begin, heroes_end),
        (this_or_next|is_between, ":active_npc", active_npcs_begin, active_npcs_end),
        (troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
        ##diplomacy end+
        (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
        (neg|faction_slot_eq, ":active_npc_faction", slot_faction_ai_state, sfai_default),
        (neg|faction_slot_eq, ":active_npc_faction", slot_faction_ai_state, sfai_feast),
        (neg|faction_slot_eq, ":active_npc_faction", slot_faction_ai_state, sfai_gathering_army),

        (troop_get_slot, ":active_npc_party", ":active_npc", slot_troop_leaded_party),
        (party_is_active, ":active_npc_party"),

        (val_add, "$total_vassal_days_on_campaign", 1),

        (party_slot_eq, ":active_npc_party", slot_party_ai_state, spai_accompanying_army),
        (val_add, "$total_vassal_days_responding_to_campaign", 1),
    (try_end),
    ]),

  # Reset hero quest status
  # Change hero relation
   (36,
   [
     (try_for_range, ":troop_no", heroes_begin, heroes_end),
       (troop_set_slot, ":troop_no", slot_troop_does_not_give_quest, 0),
     (try_end),

     (try_for_range, ":troop_no", village_elders_begin, village_elders_end),
       (troop_set_slot, ":troop_no", slot_troop_does_not_give_quest, 0),
     (try_end),
    ]),

  # Refresh merchant inventories weekly ON AVERAGE
   (24.0*7.0/(number_of_villages),
   [
    (store_random_in_range, ":village_no", villages_begin, villages_end),
    (call_script, "script_refresh_village_merchant_inventory", ":village_no"),
    # (try_end),
    ]),

  #Refreshing village defenders
  #Clearing slot_village_player_can_not_steal_cattle flags
   (24.0*3.0/(number_of_villages),#each two days
   [
    (store_random_in_range, ":village_no", villages_begin, villages_end),
    (call_script, "script_refresh_village_defenders", ":village_no"),
    (party_set_slot, ":village_no", slot_village_player_can_not_steal_cattle, 0),
    ]),

  # Refresh number of cattle in villages
  (24.0*7.0/(number_of_villages),#weekly
   [
   (store_random_in_range, ":village_no", centers_begin, centers_end),
     (try_begin),
	  (neg|is_between, ":village_no", castles_begin, castles_end),
      (party_get_slot, ":num_cattle", ":village_no", slot_center_head_cattle),
      (party_get_slot, ":num_sheep", ":village_no", slot_center_head_sheep),
      (party_get_slot, ":num_acres", ":village_no", slot_center_acres_pasture),
	  (val_max, ":num_acres", 1),

	  (store_mul, ":grazing_capacity", ":num_cattle", 400),
	  (store_mul, ":sheep_addition", ":num_sheep", 200),
	  (val_add, ":grazing_capacity", ":sheep_addition"),
	  (val_div, ":grazing_capacity", ":num_acres"),
	  (try_begin),
		(eq, "$cheat_mode", 1),
	    (assign, reg4, ":grazing_capacity"),
		(str_store_party_name, s4, ":village_no"),
	    #(display_message, "@{!}DEBUG -- Herd adjustment: {s4} at {reg4}% of grazing capacity"),
	  (try_end),


      (store_random_in_range, ":random_no", 0, 100),
      (try_begin), #Disaster
        (eq, ":random_no", 0),#1% chance of epidemic - should happen once every two years
        (val_min, ":num_cattle", 10),

        (try_begin),
#          (eq, "$cheat_mode", 1),
#          (str_store_party_name, s1, ":village_no"),
#          (display_message, "@{!}Cattle in {s1} are exterminated due to famine."),
           ##diplomacy start+ Add display message for the player's own fiefs
		   #(store_distance_to_party_from_party, ":dist", "p_main_party", ":village_no"),
		   #(this_or_next|lt, ":dist", 30),
	          (gt, "$g_player_chamberlain", 0),
		   (party_slot_eq, ":village_no", slot_town_lord, "trp_player"),
		   (party_get_slot, reg4, ":village_no", slot_center_head_cattle),
		   (val_sub, reg4, ":num_cattle"),
		   (gt, reg4, 0),
		   (str_store_party_name_link, s4, ":village_no"),
		   (display_log_message, "@A livestock epidemic has killed {reg4} cattle in {s4}."),
		   ##diplomacy end+
        (try_end),

      (else_try), #Overgrazing
	    (gt, ":grazing_capacity", 100),

         (val_mul, ":num_sheep", 90), #10% decrease at number of cattles
         (val_div, ":num_sheep", 100),

         (val_mul, ":num_cattle", 90), #10% decrease at number of sheeps
         (val_div, ":num_cattle", 100),

       (else_try), #superb grazing
         (lt, ":grazing_capacity", 30),

         (val_mul, ":num_cattle", 120), #20% increase at number of cattles
         (val_div, ":num_cattle", 100),
         (val_add, ":num_cattle", 1),

         (val_mul, ":num_sheep", 120), #20% increase at number of sheeps
         (val_div, ":num_sheep", 100),
         (val_add, ":num_sheep", 1),

       (else_try), #very good grazing
         (lt, ":grazing_capacity", 60),

         (val_mul, ":num_cattle", 110), #10% increase at number of cattles
         (val_div, ":num_cattle", 100),
		(val_add, ":num_cattle", 1),

         (val_mul, ":num_sheep", 110), #10% increase at number of sheeps
         (val_div, ":num_sheep", 100),
		(val_add, ":num_sheep", 1),

     (else_try), #good grazing
	    (lt, ":grazing_capacity", 100),
         (lt, ":random_no", 50),

         (val_mul, ":num_cattle", 105), #5% increase at number of cattles
         (val_div, ":num_cattle", 100),
         (try_begin), #if very low number of cattles and there is good grazing then increase number of cattles also by one
           (le, ":num_cattle", 20),
			(val_add, ":num_cattle", 1),
		(try_end),

         (val_mul, ":num_sheep", 105), #5% increase at number of sheeps
         (val_div, ":num_sheep", 100),
         (try_begin), #if very low number of sheeps and there is good grazing then increase number of sheeps also by one
           (le, ":num_sheep", 20),
			(val_add, ":num_sheep", 1),
		(try_end),


     (try_end),

     (party_set_slot, ":village_no", slot_center_head_cattle, ":num_cattle"),
     (party_set_slot, ":village_no", slot_center_head_sheep, ":num_sheep"),
    (try_end),
    ]),

   #Accumulate taxes
   (24.0*7.0/(number_of_centers),
   [#weekly
    (try_begin),
        (neg|is_between, "$g_center_trigger_taxes", centers_begin,centers_end),
        (assign, "$g_center_trigger_taxes", centers_begin),
    (try_end),

#BEGIN RENT CALCULATION #BEGIN RENT CALCULATION
    #finally calculate rents
    (try_begin),
        (call_script, "script_center_get_capital", "$g_center_trigger_taxes"),##moved it here
        (party_set_slot, "$g_center_trigger_taxes", slot_center_capital, reg49),
        ##only accumulate rents if the center has a lord
        (party_slot_ge, "$g_center_trigger_taxes", slot_town_lord, 0), #unassigned centers do not accumulate rents

        (party_get_slot, ":lord", "$g_center_trigger_taxes", slot_town_lord), #unassigned centers do not accumulate rents
        (party_get_slot, ":accumulated_rents", "$g_center_trigger_taxes", slot_center_accumulated_rents),

        (assign, ":cur_rents", 0),
        (try_begin),
            (party_slot_eq, "$g_center_trigger_taxes", slot_party_type, spt_village),
            (try_begin),
                (party_slot_eq, "$g_center_trigger_taxes", slot_village_state, svs_normal),
                (party_get_slot, ":cur_rents", "$g_center_trigger_taxes", slot_center_capital),
            (try_end),
        (else_try),
            # (neg|party_slot_ge, "$g_center_trigger_taxes", slot_party_looted_left_days, 1),
            (party_get_slot, ":cur_rents", "$g_center_trigger_taxes", slot_center_capital),
        (try_end),

        (try_begin),###tax for ai start
            (party_slot_ge, "$g_center_trigger_taxes", slot_town_lord, 1),
            (troop_get_slot, ":wealth", ":lord", slot_troop_wealth),
            (try_begin),#assign dynamic tax rate
                (le, ":wealth", 5000),#if it is very low he tries everything
                (assign, ":tax", 95),#to help poor lords a bit
                (call_script, "script_change_center_prosperity", "$g_center_trigger_taxes", -2),
            (else_try),
                (is_between, ":wealth", 5000, 10000),
                (assign, ":tax", 90),#to help poor lords a bit
                (call_script, "script_change_center_prosperity", "$g_center_trigger_taxes", -1),
            (else_try),
                (is_between, ":wealth", 10000, 20000),
                (assign, ":tax", 80),
            (else_try),
                (is_between, ":wealth", 20000, 30000),
                (assign, ":tax", 65),
            (else_try),
                (is_between, ":wealth", 30000, 40000),
                (assign, ":tax", 55),
            (else_try),
                (is_between, ":wealth", 40000, 60000),
                (assign, ":tax", 50),
            (else_try),
                (is_between, ":wealth", 60000, 100000),
                (assign, ":tax", 45),
                (call_script, "script_change_center_prosperity", "$g_center_trigger_taxes", 1),
            (else_try),
                (assign, ":tax", 40),
                (call_script, "script_change_center_prosperity", "$g_center_trigger_taxes", 2),
            (try_end),
            (val_mul, ":cur_rents", ":tax"),
            (val_div, ":cur_rents", 100),
            (val_add, ":accumulated_rents", ":cur_rents"), #cur rents changes between 23..1000
        (try_end), ### tax for ai end

        (try_begin),###difficulty effects players tax
            (party_slot_eq, "$g_center_trigger_taxes", slot_town_lord, "trp_player"),
            (options_get_campaign_ai, ":reduce_campaign_ai"),
            (try_begin),
                (eq, ":reduce_campaign_ai", 0), #hard (less money from rents)
                (val_mul, ":cur_rents", 5),
                (val_div, ":cur_rents", 6),
            (else_try),
                (eq, ":reduce_campaign_ai", 1), #medium (normal money from rents)
            #same
            (else_try),
                (eq, ":reduce_campaign_ai", 2), #easy (more money from rents)
                (val_mul, ":cur_rents", 4),
                (val_div, ":cur_rents", 3),
            (try_end),
        (try_end),

##TAXES FOR THE PLAYER BEGIN
     ##diplomacy begin
        (try_begin),
            (party_slot_eq, "$g_center_trigger_taxes", slot_town_lord, "trp_player"),
            (str_store_party_name, s6, "$g_center_trigger_taxes"),
            (party_get_slot, ":tax_rate2", "$g_center_trigger_taxes", dplmc_slot_center_taxation),
            # (neq, ":tax_rate", 0),
            #normal tax rate is 60%
            (store_add, ":tax_modifier", 100, ":tax_rate2"),
            (store_mul, ":tax_rate", 60, ":tax_modifier"),
            (val_div, ":tax_rate", 100),

            (val_mul, ":cur_rents", ":tax_rate"),
            (val_div, ":cur_rents", 100),
            (val_add, ":accumulated_rents", ":cur_rents"),
            (try_begin), #debug
                (eq, "$cheat_mode", 1),
                (assign, reg0, ":tax_rate"),
                #(display_message, "@{!}DEBUG : tax rate in {s6}: {reg0}"),
                (assign, reg0, ":accumulated_rents"),
                #(display_message, "@{!}DEBUG : accumulated_rents  in {s6}: {reg0}"),
                (assign, reg0, ":cur_rents"),
                #(display_message, "@{!}DEBUG : cur_rents in {s6}: {reg0}  in {s6}"),
            (try_end),
            (val_div, ":tax_rate2", -25),
            (call_script, "script_change_center_prosperity", "$g_center_trigger_taxes", ":tax_rate2"),
            (call_script, "script_change_player_relation_with_center", "$g_center_trigger_taxes", ":tax_rate2"),
            (try_begin),
                (lt, ":tax_rate2", 0), #double negative values
                (try_begin), #debug
                    (eq, "$cheat_mode", 1),
                    (assign, reg0, ":tax_rate2"),
                    #(display_message, "@{!}DEBUG : tax rate after modi in {s6}: {reg0}"),
                (try_end),
                (try_begin),
                    (this_or_next|is_between, "$g_center_trigger_taxes", villages_begin, villages_end),
                    (is_between, "$g_center_trigger_taxes", towns_begin, towns_end),
                    #SB : can't have a revolt right when player is in center
                    (neq, "$g_center_trigger_taxes", "$g_last_rest_center"),
                    (party_get_slot, ":center_relation", "$g_center_trigger_taxes", slot_center_player_relation),

                    (try_begin), #debug
                        (eq, "$cheat_mode", 1),
                        (assign, reg0, ":center_relation"),
                        #(display_message, "@{!}DEBUG : center relation: {reg0}"),
                    (try_end),

                    (lt, ":center_relation", -15),##was 5
                    (store_random_in_range, ":random",-110, 0),## bit less probability
                    (gt, ":random", ":center_relation"),

                    (neg|party_slot_eq, "$g_center_trigger_taxes", slot_village_infested_by_bandits, "trp_peasant_woman"),
                    (display_log_message, "@There has been a riot in {s6}!", message_negative), #SB : log message, colorize
                    (party_set_slot, "$g_center_trigger_taxes", slot_village_infested_by_bandits, "trp_peasant_woman"), #trp_peasant_woman used to simulate riot
                    (call_script, "script_change_center_prosperity", "$g_center_trigger_taxes", -1),
                    (call_script, "script_add_notification_menu", "mnu_dplmc_notification_riot", "$g_center_trigger_taxes", 0),

                    #add additional troops
                    (store_character_level, ":player_level", "trp_player"),
                    (store_div, ":player_leveld2", ":player_level", 2),
                    (store_mul, ":player_levelx2", ":player_level", 2),
                    (try_begin),
                        (is_between, "$g_center_trigger_taxes", villages_begin, villages_end),
                        (store_random_in_range, ":random",0, ":player_level"),
                        (party_add_members, "$g_center_trigger_taxes", "trp_mercenary_swordsman", ":random"),
                        (store_random_in_range, ":random", 0, ":player_leveld2"),
                        (party_add_members, "$g_center_trigger_taxes", "trp_hired_blade", ":random"),
                    (else_try),
                        (party_set_banner_icon, "$g_center_trigger_taxes", 0),
                        (party_get_num_companion_stacks, ":num_stacks","$g_center_trigger_taxes"),
                        (try_for_range, ":i_stack", 0, ":num_stacks"),
                            (party_stack_get_size, ":stack_size","$g_center_trigger_taxes",":i_stack"),
                            (val_div, ":stack_size", 2),
                            (party_stack_get_troop_id, ":troop_id", "$g_center_trigger_taxes", ":i_stack"),
                            (party_remove_members, "$g_center_trigger_taxes", ":troop_id", ":stack_size"),
                        (try_end),
                        (store_random_in_range, ":random",":player_leveld2", ":player_levelx2"),
                        (party_add_members, "$g_center_trigger_taxes", "trp_watchman", ":random"),
                        (store_random_in_range, ":random",0, ":player_level"),
                        (party_add_members, "$g_center_trigger_taxes", "trp_watchman", ":random"),
                    (try_end),
                (try_end),
            (try_end),
        (try_end),
##TAX FOR PLAYER ENDS ##TAX FOR PLAYER ENDS

        (try_begin),
            (party_slot_eq, "$g_center_trigger_taxes", slot_town_lord, "trp_player"),
            (party_slot_ge, "$g_center_trigger_taxes", slot_center_has_hosptial, 1),
            (party_get_slot, ":cur_relation", "$g_center_trigger_taxes", slot_center_player_relation),
            (val_add, ":cur_relation", 1),
            (val_min, ":cur_relation", 100),
            (party_set_slot, "$g_center_trigger_taxes", slot_center_player_relation, ":cur_relation"),
        (try_end),
        (try_begin),##effects of different culture
            (party_slot_eq, "$g_center_trigger_taxes", slot_town_lord, "trp_player"),
            (troop_get_slot, ":culture_player", "trp_player", slot_troop_culture),
            (neg|party_slot_eq, "$g_center_trigger_taxes", slot_center_culture, ":culture_player"),
            (store_random_in_range, ":ration", 0, 100),
            (le, ":ration", 25),
            (str_store_party_name, s4, "$g_center_trigger_taxes"),
            (display_log_message, "@People are angry in {s4}. They don't want to pay taxes to a foreigner like you.", color_bad_news),
            (call_script, "script_change_player_relation_with_center", "$g_center_trigger_taxes", -2),
        (try_end),
        (try_begin),###effects of relation on tax rate
            (party_slot_eq, "$g_center_trigger_taxes", slot_town_lord, "trp_player"),
            (troop_get_slot, ":culture_player", "trp_player", slot_troop_culture),
            (neg|party_slot_eq, "$g_center_trigger_taxes", slot_center_culture, ":culture_player"),
            (neg|party_slot_ge, "$g_center_trigger_taxes", slot_center_player_relation, -10),
            (store_random_in_range, ":ration", 0, 100),
            (lt, ":ration", 25),
            (str_store_party_name, s4, "$g_center_trigger_taxes"),
            (display_log_message, "@One of your tax collectors has been attacked in {s4}.", color_bad_news),
            (val_mul, ":accumulated_rents", 2),
            (val_div, ":accumulated_rents", 3),
        (else_try),###effects of relation on tax rate
              (party_slot_eq, "$g_center_trigger_taxes", slot_town_lord, "trp_player"),
              (neg|party_slot_ge, "$g_center_trigger_taxes", slot_center_player_relation, -50),
              (store_random_in_range, ":ration", 0, 100),
              (lt, ":ration", 25),
              (str_store_party_name, s4, "$g_center_trigger_taxes"),
              (display_log_message, "@One of your tax collectors has been attacked in {s4}.", color_bad_news),
              (val_mul, ":accumulated_rents", 2),
              (val_div, ":accumulated_rents", 3),
        (try_end),
        (val_max, ":accumulated_rents", 0),#to prefent from negative values here
        (try_begin),
            (troop_slot_eq, "trp_khergit_merchant", slot_troop_father, 2),
            (eq, "$g_center_trigger_taxes", "p_town_6"),
            (val_div, ":accumulated_rents", 4),
            (party_get_slot, ":tarrifs", "$g_center_trigger_taxes", slot_center_accumulated_tariffs),
            (val_div, ":tarrifs", 10),
            (party_set_slot, "$g_center_trigger_taxes", slot_center_accumulated_tariffs, ":tarrifs"),
            (display_message, "@Criminal activities lower your tariffs in Rome...", color_bad_news),
            (call_script, "script_change_center_prosperity", "$g_center_trigger_taxes", -3),
        (try_end),
        (party_set_slot, "$g_center_trigger_taxes", slot_center_accumulated_rents, ":accumulated_rents"),###set the tax rate
        # (try_begin),###castles may get rents from their bounded villages too
            # (is_between, "$g_center_trigger_taxes", villages_begin, villages_end),
            # (is_between, ":cur_rents", 0, 200000),##if there is something to add
            # #(party_slot_ge, "$g_center_trigger_taxes", slot_town_lord, 0), #unassigned centers do not accumulate rents
            # (party_get_slot, ":bound_castle", "$g_center_trigger_taxes", slot_village_bound_center),
            # (party_slot_ge, ":bound_castle", slot_town_lord, 0), #unassigned centers do not accumulate rents
            # (is_between, ":bound_castle", castles_begin, castles_end),
            # (party_get_slot, ":accumulated_rents", ":bound_castle", slot_center_accumulated_rents), #castle's accumulated rents
            # (val_mul, ":cur_rents", 2),
            # (val_div, ":cur_rents", 3),
            # (val_add, ":accumulated_rents", ":cur_rents"), #add village's rent to castle rents
            # (party_set_slot, ":bound_castle", slot_center_accumulated_rents, ":accumulated_rents"),
        # (try_end),
    (try_end),##END RENT CALCULATION
 ##END RENT CALCULATION##END RENT CALCULATION##END RENT CALCULATION


    # #check for diseases
    (try_begin),
        (party_get_slot, ":disease", "$g_center_trigger_taxes", slot_center_disease),
        (gt, ":disease", 0),
        (val_sub, ":disease", 1),
        (try_begin),
            (this_or_next|is_between, ":disease", disease_consumption_timer, disease_consumption+1),
            (this_or_next|is_between, ":disease", disease_slow_fever_timer, disease_slow_fever+1),
            (this_or_next|is_between, ":disease", disease_camp_fever_timer, disease_camp_fever+1),
            (this_or_next|is_between, ":disease", disease_plague_timer, disease_plague+1),
            (this_or_next|is_between, ":disease", disease_measles_timer, disease_measles+1),
            (this_or_next|is_between, ":disease", disease_smallpox_timer, disease_smallpox+1),
            (is_between, ":disease", disease_greatpoxpox_timer, disease_greatpoxpox+1),
            (party_set_slot, "$g_center_trigger_taxes", slot_center_disease, ":disease"),
        (else_try),
            (party_set_slot, "$g_center_trigger_taxes", slot_center_disease, -1),
            (try_begin),
                (party_slot_eq, "$g_center_trigger_taxes", slot_town_lord, "trp_player"),
                (str_store_party_name, s22, "$g_center_trigger_taxes"),
                (val_add, ":disease", 1),
                (call_script, "script_get_event_details", ":disease"),
                (display_log_message, "@The {s0} outbreak has ended in {s22}.", color_good_news),
            (try_end),
        (try_end),
    (else_try),
        (lt, ":disease", 0),
        (party_set_slot, "$g_center_trigger_taxes", slot_center_disease, 0),
    (try_end),

    #check for event
    (try_begin),
        (party_get_slot, ":event", "$g_center_trigger_taxes", slot_center_event),
        (gt, ":event", 0),
        (val_sub, ":event", 1),
        (try_begin),
            (this_or_next|is_between, ":event", event_earthquake_timer, event_earthquake+1),
            (this_or_next|is_between, ":event", event_fire_timer, event_fire+1),
            (this_or_next|is_between, ":event", event_drought_timer, event_drought+1),
            (this_or_next|is_between, ":event", event_insects_timer, event_insects+1),
            (is_between, ":event", event_conquered_timer, event_conquered+1),
            # (is_between, ":event", event_fire_of_rome_timer, event_fire_of_rome+1),
            (party_set_slot, "$g_center_trigger_taxes", slot_center_event, ":event"),
        (else_try),
            (party_set_slot, "$g_center_trigger_taxes", slot_center_event, -1),
            (try_begin),
                (party_slot_eq, "$g_center_trigger_taxes", slot_town_lord, "trp_player"),
                (str_store_party_name, s22, "$g_center_trigger_taxes"),
                (val_add, ":event", 1),
                (call_script, "script_get_event_details", ":event"),
                (display_log_message, "@{s22} has recovered from {s0}.", color_good_news),
            (try_end),
        (try_end),
    (else_try),
        (lt, ":event", 0),
        (party_set_slot, "$g_center_trigger_taxes", slot_center_event, 0),
    (try_end),


    (val_add, "$g_center_trigger_taxes", 1),
    ]),

#   (7 * 24,
#   [
##       (call_script, "script_get_number_of_unclaimed_centers_by_player"),
##       (assign, ":unclaimed_centers", reg0),
##       (gt, ":unclaimed_centers", 0),
# You are holding an estate without a lord.
#       (try_for_range, ":troop_no", heroes_begin, heroes_end),
#         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
#         (troop_get_slot, ":relation", ":troop_no", slot_troop_player_relation),
#         (val_sub, ":relation", 1),
#         (val_max, ":relation", -100),
#         (troop_set_slot, ":troop_no", slot_troop_player_relation, ":relation"),
#       (try_end),
# You relation with all kingdoms other than your own has decreased by 1.
#       (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
#         (neq, ":faction_no", "$players_kingdom"),
#         (store_relation,":faction_relation",":faction_no","fac_player_supporters_faction"),
#         (val_sub, ":faction_relation", 1),
#         (val_max, ":faction_relation", -100),
#		  WARNING: Never use set_relation!
#         (set_relation, ":faction_no", "fac_player_supporters_faction", ":faction_relation"),
#       (try_end),
#    ]),


  # Offer player to join faction
  # Only if the player is male -- female characters will be told that they should seek out a faction through NPCs, possibly
   (32,
   [
	(eq, "$freelancer_state", 0), #madsci
     	(eq, "$players_kingdom", 0),
     	(le, "$g_invite_faction", 0),
     	(eq, "$g_player_is_captive", 0),
	(neg|check_quest_active, "qst_armenian_kingdom_quest_2"),
	 ##diplomacy start+ Use script for gender
	 #(troop_get_type, ":type", "trp_player"),
	 (assign, ":type", "$character_gender"),#<-- this should have been set correctly during character creation
	 ##diplomacy end+
	 (try_begin),
	    ##diplomacy start+ In reduced prejudice mode, female players get the same offers.
		(lt, "$g_disable_condescending_comments", 2),
		##diplomacy end+
		(eq, ":type", tf_female),
		(eq, "$npc_with_sisterly_advice", 0),
		##diplomacy start+  Make the order less predictable (used below) #SB : fix range
		(store_sub, ":range", companions_end, companions_begin),
		(store_random_in_range, ":random", 0, ":range"),
		##diplomacy end+
		(try_for_range, ":npc", companions_begin, companions_end),
			##diplomacy start+ Make the order less predictable
			(val_add, ":npc", ":random"),
			(try_begin), #SB : fix range
				(ge, ":npc", companions_end),
				(val_sub, ":npc", ":range"),
			(try_end),
			##diplomacy end+
			(main_party_has_troop, ":npc"),
			##diplmacy start+ Use a script for gender
			##OLD:
			#(troop_get_type, ":npc_type", ":npc"),
			#(eq, ":npc_type", 1),
			##NEW:
			# (assign, ":npc_type", 0),
			# (try_begin),
				(call_script, "script_cf_dplmc_troop_is_female", ":npc"),
				# (assign, ":npc_type", 1),
			# (try_end),
			# (eq, ":npc_type", ":type"),
			##diplomacy end+
			(troop_slot_ge, "trp_player", slot_troop_renown, dplmc_command_renown_limit), #SB : const / 2
			(troop_slot_ge, ":npc", slot_troop_woman_to_woman_string, 1),
			(assign, "$npc_with_sisterly_advice", ":npc"),
		(try_end),
	 (else_try),
	     (store_random_in_range, ":kingdom_no", npc_kingdoms_begin, npc_kingdoms_end),
	     (assign, ":min_distance", 999999),
	     (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
	       (store_faction_of_party, ":center_faction", ":center_no"),
	       (eq, ":center_faction", ":kingdom_no"),
	       (store_distance_to_party_from_party, ":cur_distance", "p_main_party", ":center_no"),
	       (val_min, ":min_distance", ":cur_distance"),
	     (try_end),
	     (lt, ":min_distance", 30),
	     (store_relation, ":kingdom_relation", ":kingdom_no", "fac_player_supporters_faction"),
	     (faction_get_slot, ":kingdom_lord", ":kingdom_no", slot_faction_leader),
	     (call_script, "script_troop_get_player_relation", ":kingdom_lord"),
	     (assign, ":lord_relation", reg0),
	     #(troop_get_slot, ":lord_relation", ":kingdom_lord", slot_troop_player_relation),
	     (call_script, "script_get_number_of_hero_centers", "trp_player"),
	     (assign, ":num_centers_owned", reg0),
	     (eq, "$g_infinite_camping", 0),

	     (assign, ":player_party_size", 0),
	     (try_begin),
	       (ge, "p_main_party", 0),
	       (store_party_size_wo_prisoners, ":player_party_size", "p_main_party"),
	     (try_end),

	     (try_begin),
	       (eq, ":num_centers_owned", 0),
	       (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
	       (ge, ":player_renown", 160),
	       (ge, ":kingdom_relation", 0),
	       (ge, ":lord_relation", 0),
	       (ge, ":player_party_size", 45),
	       (store_random_in_range, ":rand", 0, 100),
	       (lt, ":rand", 50),
	       (call_script, "script_get_poorest_village_of_faction", ":kingdom_no"),
	       (assign, "$g_invite_offered_center", reg0),
	       (ge, "$g_invite_offered_center", 0),
	       (assign, "$g_invite_faction", ":kingdom_no"),
	       (jump_to_menu, "mnu_invite_player_to_faction"),
	     (else_try),
	       (gt, ":num_centers_owned", 0),
	       (neq, "$players_oath_renounced_against_kingdom", ":kingdom_no"),
	       (ge, ":kingdom_relation", -40),
	       (ge, ":lord_relation", -20),
	       (ge, ":player_party_size", 30),
	       (store_random_in_range, ":rand", 0, 100),
	       (lt, ":rand", 20),
	       (assign, "$g_invite_faction", ":kingdom_no"),
	       (assign, "$g_invite_offered_center", -1),
	       (jump_to_menu, "mnu_invite_player_to_faction_without_center"),
	     (try_end),
	 (try_end),
    ]),

    #recalculate lord random decision seeds once in every week
	(24.0*7.0/(number_of_active_npcs),
	[
	  (store_random_in_range, ":troop_no", heroes_begin, heroes_end),
	  (store_random_in_range, ":random", 0, 10000),
      (troop_set_slot, ":troop_no", slot_troop_temp_decision_seed, ":random"),
	]),

  # Attach Lord Parties to the town they are in
  (0.1,
   [
       (try_for_range, ":troop_no", heroes_begin, heroes_end),
         (this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive), #SB : fix stuck defector bug
         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
         (troop_get_slot, ":troop_party_no", ":troop_no", slot_troop_leaded_party),
         (ge, ":troop_party_no", 1),
         (party_is_active, ":troop_party_no"),

         (party_get_attached_to, ":cur_attached_town", ":troop_party_no"),
         (lt, ":cur_attached_town", 1),
         (party_get_cur_town, ":destination", ":troop_party_no"),
         (is_between, ":destination", centers_begin, centers_end),
         (call_script, "script_get_relation_between_parties", ":destination", ":troop_party_no"),
         (try_begin),
           (ge, reg0, 0),
           (party_attach_to_party, ":troop_party_no", ":destination"),
         (else_try),
           (party_set_ai_behavior, ":troop_party_no", ai_bhvr_hold),
         (try_end),

         (try_begin),
           (this_or_next|party_slot_eq, ":destination", slot_party_type, spt_town),
           (party_slot_eq, ":destination", slot_party_type, spt_castle),
           (store_faction_of_party, ":troop_faction_no", ":troop_party_no"),
           (store_faction_of_party, ":destination_faction_no", ":destination"),
           (eq, ":troop_faction_no", ":destination_faction_no"),
           (party_get_num_prisoner_stacks, ":num_stacks", ":troop_party_no"),
           (gt, ":num_stacks", 0),
           (assign, "$g_move_heroes", 1),
           (call_script, "script_party_prisoners_add_party_prisoners", ":destination", ":troop_party_no"),#Moving prisoners to the center
           (assign, "$g_move_heroes", 1),
           (call_script, "script_party_remove_all_prisoners", ":troop_party_no"),
         (try_end),
       (try_end),

    ]),

  # Check escape chances of hero prisoners.
  (48.0/(number_of_walled_centers),
   [
       (store_random_in_range, ":center_no", walled_centers_begin, walled_centers_end),
         (assign, ":chance", 30),
         (try_begin),
           (party_slot_eq, ":center_no", slot_center_has_prisoner_tower, 1),
           (assign, ":chance", 5),
         (try_end),
         (call_script, "script_randomly_make_prisoner_heroes_escape_from_party", ":center_no", ":chance"),
    ]),

    (48,
   [
       (call_script, "script_randomly_make_prisoner_heroes_escape_from_party", "p_main_party", 50),

	  ##diplomacy start+ Also update the temporary seed for the player
	  (store_random_in_range, ":random", 0, 10000),
	  (troop_set_slot, "trp_player", slot_troop_temp_decision_seed, ":random"),
	  ##diplomacy end+

    ]),

  # Asking the ownership of captured centers to the player
#  (3,
#   [
#    (assign, "$g_center_taken_by_player_faction", -1),
#    (try_for_range, ":center_no", centers_begin, centers_end),
#      (eq, "$g_center_taken_by_player_faction", -1),
#      (store_faction_of_party, ":center_faction", ":center_no"),
#      (eq, ":center_faction", "fac_player_supporters_faction"),
#      (this_or_next|party_slot_eq, ":center_no", slot_town_lord, stl_reserved_for_player),
#      (this_or_next|party_slot_eq, ":center_no", slot_town_lord, stl_unassigned),
#      (party_slot_eq, ":center_no", slot_town_lord, stl_rejected_by_player),
#      (assign, "$g_center_taken_by_player_faction", ":center_no"),
#    (try_end),
#    (faction_get_slot, ":leader", "fac_player_supporters_faction", slot_faction_leader),

#	(try_begin),
#		(ge, "$g_center_taken_by_player_faction", 0),

#		(eq, "$cheat_mode", 1),
#		(str_store_party_name, s14, "$g_center_taken_by_player_faction"),
#		(display_message, "@{!}{s14} should be assigned to lord"),
#	(try_end),

#    ]),


  # Respawn hero party after kingdom hero is released from captivity.
  (24.0/(number_of_active_npcs),
   [
       ##diplomacy start+ Support promoted kingdom ladies
       ##OLD:
       #(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
       ##NEW:
        (store_random_in_range, ":troop_no", heroes_begin, heroes_end),
       ##diplomacy end+
         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),

         (str_store_troop_name, s1, ":troop_no"),

         (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
         (neg|troop_slot_ge, ":troop_no", slot_troop_leaded_party, 1),

         (store_troop_faction, ":cur_faction", ":troop_no"),
         (try_begin),
           (this_or_next|eq, ":cur_faction", "fac_outlaws"), #Do nothing
           (eq, ":cur_faction", "fac_commoners"), #Do nothing
         (else_try), #dckplmc
         # (else_try), #SB : faction must be active to spawn
           (is_between, ":cur_faction", kingdoms_begin, kingdoms_end),
           (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
           (try_begin),
             (eq, "$cheat_mode", 2),
             (str_store_troop_name, s4, ":troop_no"),
             (display_message, "str_debug__attempting_to_spawn_s4"),
           (try_end),

           (call_script, "script_cf_select_random_walled_center_with_faction_and_owner_priority_no_siege", ":cur_faction", ":troop_no"),#Can fail
           (assign, ":center_no", reg0),

           (try_begin),
             (eq, "$cheat_mode", 2),
             (str_store_party_name, s7, ":center_no"),
             (str_store_troop_name, s0, ":troop_no"),
             (display_message, "str_debug__s0_is_spawning_around_party__s7"),
           (try_end),

           (call_script, "script_create_kingdom_hero_party", ":troop_no", ":center_no"),

           (try_begin),
             (eq, "$g_there_is_no_avaliable_centers", 0),
             (party_attach_to_party, "$pout_party", ":center_no"),
           (try_end),

           #new
           #(troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
           #(call_script, "script_npc_decision_checklist_party_ai", ":troop_no"), #This handles AI for both marshal and other parties
           #(call_script, "script_party_set_ai_state", ":party_no", reg0, reg1),
           #new end

           (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
           (call_script, "script_party_set_ai_state", ":party_no", spai_holding_center, ":center_no"),

         (else_try),
           (neg|faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
           (try_begin),
		(this_or_next|faction_slot_eq, ":cur_faction", slot_faction_leader, ":troop_no"), #madsci this also applies to victorious pretenders etc
             (is_between, ":troop_no", kings_begin, kings_end),
             (troop_set_slot, ":troop_no", slot_troop_change_to_faction, "fac_commoners"),
		(try_begin), #madsci cant have a kingdom hero party of non-kingdom faction on the map
		(troop_get_slot, ":current_party", ":troop_no", slot_troop_leaded_party),
		(gt, ":current_party", 0),
		(party_is_active, ":current_party"),
		(remove_party, ":current_party"),
		(try_end),
           (else_try),
             (store_random_in_range, ":random_no", 0, 100),
             (lt, ":random_no", 10),
             (call_script, "script_cf_get_random_active_faction_except_player_faction_and_faction", ":cur_faction"),
             (troop_set_slot, ":troop_no", slot_troop_change_to_faction, reg0),
           (try_end),
         (try_end),
       # (try_end),
    ]),

  # Spawn merchant caravan parties
##  (3,
##   [
##       (try_for_range, ":troop_no", merchants_begin, merchants_end),
##         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_merchant),
##         (troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
##         (neg|troop_slot_ge, ":troop_no", slot_troop_leaded_party, 1),
##
##         (call_script, "script_cf_create_merchant_party", ":troop_no"),
##       (try_end),
##    ]),

  # Spawn village farmer parties
  (24.0/(number_of_villages),
   [
       (store_random_in_range, ":village_no", villages_begin, villages_end),
         (party_slot_eq, ":village_no", slot_village_state, svs_normal),
         (party_get_slot, ":farmer_party", ":village_no", slot_village_farmer_party),
         (this_or_next|eq, ":farmer_party", 0),
         (neg|party_is_active, ":farmer_party"),
         (store_random_in_range, ":random_no", 0, 100),
         (lt, ":random_no", 60),
         (call_script, "script_create_village_farmer_party", ":village_no"),
         (party_set_slot, ":village_no", slot_village_farmer_party, reg0),
#         (str_store_party_name, s1, ":village_no"),
#         (display_message, "@Village farmers created at {s1}."),
    ]),


   (72,
   [
# Cows in inventory give food items
      (try_begin),
        (assign, ":cont", 0),
        (assign, ":space", 0),
        (store_free_inventory_capacity, ":space", "trp_player"),
        (gt, ":space", 0),
        (store_item_kind_count, ":cont", "itm_cow_1"),
        (ge, ":cont", 1),
        (store_random_in_range, ":rand", 0, 100),
        (lt, ":rand", 50),
        (troop_add_item,"trp_player","itm_butter"),
        (display_message, "@Your men made some delicious butter from cow's milk.", color_good_news),
      (try_end),
  # Updating trade good prices according to the productions
       (call_script, "script_update_trade_good_prices"),
 # Updating player odds
       (try_for_range, ":cur_center", centers_begin, centers_end),
         (party_get_slot, ":player_odds", ":cur_center", slot_town_player_odds),
         (try_begin),
           (gt, ":player_odds", 1000),
           (val_mul, ":player_odds", 95),
           (val_div, ":player_odds", 100),
           (val_max, ":player_odds", 1000),
         (else_try),
           (lt, ":player_odds", 1000),
           (val_mul, ":player_odds", 105),
           (val_div, ":player_odds", 100),
           (val_min, ":player_odds", 1000),
         (try_end),
         (party_set_slot, ":cur_center", slot_town_player_odds, ":player_odds"),
       (try_end),
    ]),


  #Troop AI: Merchants thinking
  (8,
   [
       (game_get_reduce_campaign_ai, ":reduce_campaign_ai"), #SB : moved this up top
       (val_sub, ":reduce_campaign_ai", 1),
       (val_mul, ":reduce_campaign_ai", 10), #pre-calculate amount
       (try_for_parties, ":party_no"),
      (gt, ":party_no", last_static_party), #madsci
         (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_caravan),
         (party_is_in_any_town, ":party_no"),

         (store_faction_of_party, ":merchant_faction", ":party_no"),
         (faction_get_slot, ":num_towns", ":merchant_faction", slot_faction_num_towns),
         (try_begin),
           (le, ":num_towns", 0),
           (remove_party, ":party_no"),
         (else_try),
           (party_get_cur_town, ":cur_center", ":party_no"),

           (store_random_in_range, ":random_no", 0, 100),
           (assign, ":tariff_succeed_limit", 45), #SB : base amount for medium
           (try_begin),
             (this_or_next|party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
             (eq, ":merchant_faction", "$players_kingdom"),
             (val_add, ":tariff_succeed_limit", ":reduce_campaign_ai"),
           (try_end),
           # (try_begin),
             # (party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),

             # # (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
             # (try_begin),
               # (eq, ":reduce_campaign_ai", 0), #hard (less money from tariffs)
               # (assign, ":tariff_succeed_limit", 35),
             # (else_try),
               # (eq, ":reduce_campaign_ai", 1), #medium (normal money from tariffs)
               # (assign, ":tariff_succeed_limit", 45),
             # (else_try),
               # (eq, ":reduce_campaign_ai", 2), #easy (more money from tariffs)
               # (assign, ":tariff_succeed_limit", 60),
             # (try_end),
           # (else_try),
             # (assign, ":tariff_succeed_limit", 45),
           # (try_end),

           (lt, ":random_no", ":tariff_succeed_limit"),

           #SB : todo queue caravans so they don't blob together, obvious if same destination
           (assign, ":can_leave", 1),
           (try_begin),
             (is_between, ":cur_center", walled_centers_begin, walled_centers_end),
             (neg|party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
             (assign, ":can_leave", 0),
           (try_end),
           (eq, ":can_leave", 1),

           (assign, ":do_trade", 0),
           (try_begin),
             (party_get_slot, ":cur_ai_state", ":party_no", slot_party_ai_state),
             (eq, ":cur_ai_state", spai_trading_with_town),
             (party_get_slot, ":cur_ai_object", ":party_no", slot_party_ai_object),
             (eq, ":cur_center", ":cur_ai_object"),
             (assign, ":do_trade", 1),
           (try_end),

           (assign, ":target_center", -1),

           (try_begin), #Make sure escorted caravan continues to its original destination.
             (eq, "$caravan_escort_state", 1),
             (eq, "$caravan_escort_party_id", ":party_no"), #SB : redo globals here
             (assign, ":caravan_distance_to_player", 9999),
             (try_begin), #code from triggers
               (eq, "$caravan_escort_state", 1),
               (eq, ":cur_center", "$caravan_escort_destination_town"),
               #arrived, check if player is nearby to prompt conversation (unless player triggered dialog first)
               (store_distance_to_party_from_party, ":caravan_distance_to_player","p_main_party","$caravan_escort_party_id"),
               (lt, ":caravan_distance_to_player", 5),
               (map_free), #in case player is fighting?
               (start_encounter, "$caravan_escort_party_id"),
             (else_try),
               (ge, ":caravan_distance_to_player", 5), #cancel quest
               (assign, "$caravan_escort_state", 0),
             (else_try),
               # (neg|party_is_in_town, ":party_no", "$caravan_escort_destination_town"),
               (neq, ":cur_center", "$caravan_escort_destination_town"),
               (assign, ":target_center", "$caravan_escort_destination_town"),
             (try_end),
           (else_try),
            ##diplomacy start+ added third parameter "-1" to use the town's location
             (call_script, "script_cf_select_most_profitable_town_at_peace_with_faction_in_trade_route", ":cur_center", ":merchant_faction", -1),
            ##diplomacy end+
             (assign, ":target_center", reg0),
           (try_end),
           (is_between, ":target_center", towns_begin, towns_end),
           (neg|party_is_in_town, ":party_no", ":target_center"),

            (try_begin),
                (eq, ":do_trade", 1),
                (str_store_party_name, s7, ":cur_center"),
                (call_script, "script_do_merchant_town_trade", ":party_no", ":cur_center"),
                ##drop of prisoners
                (call_script, "script_party_add_party_prisoners", ":cur_center", ":party_no"),
                (call_script, "script_party_remove_all_prisoners", ":party_no"),
            (try_end),
           (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
           (party_set_ai_object, ":party_no", ":target_center"),
           (party_set_flags, ":party_no", pf_default_behavior, 0),
           (party_set_slot, ":party_no", slot_party_ai_state, spai_trading_with_town),
           (party_set_slot, ":party_no", slot_party_ai_object, ":target_center"),
         (try_end),
       (try_end),
    ]),

  #Troop AI: Village farmers thinking
  (8.5/(number_of_villages),
   [
    #(try_for_parties, ":party_no"),
    #MOTO farmers start out early in day
    (store_time_of_day, ":oclock"),
    (is_between, ":oclock", 4, 17),
    #MOTO farmers start out early in day end
    (store_random_in_range, ":home_center", villages_begin, villages_end),
    (party_get_slot, ":party_no", ":home_center", slot_village_farmer_party),

    (try_begin),
         #(gt, ":party_no", "p_spawn_points_end"),
      (gt, ":party_no", last_static_party), #madsci
         (party_is_active, ":party_no"),
         (party_slot_eq, ":party_no", slot_party_type, spt_village_farmer),
         (party_is_in_any_town, ":party_no"),
         (party_get_slot, ":home_center", ":party_no", slot_party_home_center),
         (party_get_cur_town, ":cur_center", ":party_no"),

         (assign, ":can_leave", 1),
         (try_begin),
           (is_between, ":cur_center", walled_centers_begin, walled_centers_end),
            #siege warfare chief cambia #no villagers in siege
            (this_or_next|party_slot_ge, ":cur_center", slot_center_blockaded, 2),    #center blockaded (by player) OR
            (party_slot_ge, ":cur_center", slot_center_is_besieged_by, 1), #center besieged by someone else
            #siege warfare
           (neg|party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
           (assign, ":can_leave", 0),
         (try_end),
         (eq, ":can_leave", 1),

         (try_begin),
           (eq, ":cur_center", ":home_center"),

		   #Peasants trade in their home center
		   (call_script, "script_do_party_center_trade", ":party_no", ":home_center", 3), #this needs to be the same as the center
		   (store_faction_of_party, ":center_faction", ":cur_center"),
           (party_set_faction, ":party_no", ":center_faction"),
           (party_get_slot, ":market_town", ":home_center", slot_village_market_town),
           (party_set_slot, ":party_no", slot_party_ai_object, ":market_town"),
           (party_set_slot, ":party_no", slot_party_ai_state, spai_trading_with_town),
           (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
           (party_set_ai_object, ":party_no", ":market_town"),
           #SB : pick up up to 5 spare items in elder's inventory
           (try_begin), #technically we can just sell from the inventory directly and skip all this work
             (ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
             (party_get_slot, ":town_elder", ":home_center", slot_town_elder),
             (try_begin), #reaccumulate wealth, since we can't store the party's gold use a slot
               (party_get_slot, ":cur_wealth", ":party_no", slot_town_wealth),
               (troop_add_gold, ":town_elder", ":cur_wealth"),
               (party_set_slot, ":party_no", slot_town_wealth, 0),
             (try_end),
             (party_get_slot, ":num_items", ":party_no", slot_party_next_looted_item_slot),
             # (this_or_next|eq, ":num_items", 0),
             (lt, ":num_items", num_party_loot_slots), #not capped
             (val_add, ":num_items", slot_party_looted_item_1),
             (troop_get_inventory_capacity, ":inv_cap", ":town_elder"),
             (try_for_range, ":item_slot", 10, ":inv_cap"),
               (troop_get_inventory_slot, ":item_no", ":town_elder", ":item_slot"),
               (gt, ":item_no", -1),
               (item_get_type, ":itp", ":item_no"),
               (neq, ":itp", itp_type_goods), #whatever crap player sells
               (party_set_slot, ":party_no", ":num_items", ":item_no"),
               (store_add, ":imod_slot", ":num_items", num_party_loot_slots),
               (troop_get_inventory_slot_modifier, ":imod_no", ":town_elder", ":item_slot"),
               (party_set_slot, ":party_no", ":imod_slot", ":imod_no"),
               (troop_set_inventory_slot, ":town_elder", ":item_slot", -1), #remove
               (try_begin), #only 5 permited
                 (ge, ":num_items", slot_party_looted_item_1 + num_party_loot_slots),
                 (assign, ":inv_cap", 0),
               (else_try),
                 (val_add, ":num_items", 1),
               (try_end),
             (try_end),
           (try_end),

         (else_try),
           (try_begin),
             (party_get_slot, ":cur_ai_object", ":party_no", slot_party_ai_object),
             (eq, ":cur_center", ":cur_ai_object"),

             (call_script, "script_do_party_center_trade", ":party_no", ":cur_ai_object", 3), #raised from 10
             (assign, ":total_change", reg0),
		     #This is roughly 50% of what a caravan would pay

             #Adding tariffs to the town
             (party_get_slot, ":accumulated_tariffs", ":cur_ai_object", slot_center_accumulated_tariffs),
             (party_get_slot, ":prosperity", ":cur_ai_object", slot_town_prosperity),

			 (assign, ":tariffs_generated", ":total_change"),
			 (val_mul, ":tariffs_generated", ":prosperity"),
			 ##diplomacy start+
			 (val_add, ":tariffs_generated", 50),#round properly
			 ##diplomacy end+
			 (val_div, ":tariffs_generated", 100),
			 ##diplomacy start+
			 (val_div, ":tariffs_generated", 5),#round properly
			 ##diplomacy end+
			 (val_div, ":tariffs_generated", 20), #10 for caravans, 20 for villages

                (try_begin),
                    (party_slot_ge, ":home_center", slot_center_has_trader, 1),
                    (val_mul, ":tariffs_generated", 3),
                    (val_div, ":tariffs_generated", 2),
                (try_end),

                (try_begin),
                    (party_slot_ge, ":home_center", slot_center_has_forum, 1),
                    (val_mul, ":tariffs_generated", 3),
                    (val_div, ":tariffs_generated", 2),
                (try_end),

                (try_begin),
                    (party_slot_ge, ":home_center", slot_center_has_roads, 1),
                    (val_mul, ":tariffs_generated", 3),
                    (val_div, ":tariffs_generated", 2),
                (try_end),
                (try_begin),
                    (party_slot_ge, ":cur_ai_object", slot_center_has_roads, 1),
                    (val_mul, ":tariffs_generated", 3),
                    (val_div, ":tariffs_generated", 2),
                (try_end),

			 (val_add, ":accumulated_tariffs", ":tariffs_generated"),
			 ##diplomacy begin
        (try_begin), #no tariffs for infested villages and towns
          (party_slot_ge, ":cur_ai_object", slot_village_infested_by_bandits, 1),
          (assign,":accumulated_tariffs", 0),
        (try_end),
	     ##diplomacy end
			 (try_begin),
				(ge, "$cheat_mode", 3),
				(assign, reg4, ":tariffs_generated"),
				(str_store_party_name, s4, ":cur_ai_object"),
				(assign, reg5, ":accumulated_tariffs"),
				(display_message, "@{!}New tariffs at {s4} = {reg4}, total = {reg5}"),
			 (try_end),

             (party_set_slot, ":cur_ai_object", slot_center_accumulated_tariffs, ":accumulated_tariffs"),

             #Increasing food stocks of the town
             (party_get_slot, ":town_food_store", ":cur_ai_object", slot_party_food_store),
             (call_script, "script_center_get_food_store_limit", ":cur_ai_object"),
             (assign, ":food_store_limit", reg0),
             (val_add, ":town_food_store", 1000),
             (val_min, ":town_food_store", ":food_store_limit"),
             (party_set_slot, ":cur_ai_object", slot_party_food_store, ":town_food_store"),

                #Adding 1 to village prosperity
                (assign, ":luck", 5),
                (try_begin),
                    (party_slot_ge, ":home_center", slot_center_has_trader, 1),
                    (val_add, ":luck", 50),
                (try_end),
             (try_begin),
               (store_random_in_range, ":rand", 0, 100),
               (lt, ":rand",  ":luck"), #was 35
               (call_script, "script_change_center_prosperity", ":home_center", 1),
			   (val_add, "$newglob_total_prosperity_from_village_trade", 1),
             (try_end),
           (try_end),

           #Moving farmers to their home village
           (party_set_slot, ":party_no", slot_party_ai_object, ":home_center"),
           (party_set_slot, ":party_no", slot_party_ai_state, spai_trading_with_town),
           (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
           (party_set_ai_object, ":party_no", ":home_center"),
         (try_end),
       (try_end),
    ]),

 #Increase castle food stores
    (24.0/(number_of_villages),# was with a loop every 2 hours, I change it to a average daily event
    [
    (assign, ":save_reg0", reg0),
    (try_begin),
        (store_random_in_range, ":village_no", villages_begin, villages_end),#we have 216 villages
        (neg|party_slot_ge, ":village_no", slot_center_is_besieged_by, 0),
        (party_slot_eq, ":village_no", slot_village_state, svs_normal),
        (party_get_slot, ":center_no", ":village_no", slot_village_bound_center),
        (is_between, ":center_no", castles_begin, castles_end),
        (assign, ":can_leave", 1),
        (try_begin),
            #siege warfare chief cambia #no villagers in siege
            (this_or_next|party_slot_ge, ":center_no", slot_center_blockaded, 2),    #center blockaded (by player) OR
            (party_slot_ge, ":center_no", slot_center_is_besieged_by, 1), #center besieged by someone else
            #siege warfare
            (neg|party_slot_eq, ":center_no", slot_center_is_besieged_by, -1),
            (assign, ":can_leave", 0),
        (try_end),
        (eq, ":can_leave", 1),
        (party_get_slot, ":center_food_store", ":center_no", slot_party_food_store),
        (party_get_slot, reg0, ":village_no", slot_town_prosperity),
        (val_add, reg0, 75),
        (val_mul, reg0, 100),#base addition is 100
        (val_add, reg0, 62),
        (val_div, reg0, 125),#plus or minus 40%
        (val_add, ":center_food_store", reg0),
        (call_script, "script_center_get_food_store_limit", ":center_no"),
        (assign, ":food_store_limit", reg0),
        (val_min, ":center_food_store", ":food_store_limit"),
        (party_set_slot, ":center_no", slot_party_food_store, ":center_food_store"),
    (try_end),
    (assign, reg0, ":save_reg0"),
    ]),

  # Make heroes running away from someone retreat to friendly centers
  (0.5,
   [
       (try_for_range, ":cur_troop", heroes_begin, heroes_end),
         (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
         (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
         (gt, ":cur_party", 0),
         (try_begin),
           (party_is_active, ":cur_party"),
           (try_begin),
             (get_party_ai_current_behavior, ":ai_bhvr", ":cur_party"),
             (eq, ":ai_bhvr", ai_bhvr_avoid_party),

			 #Certain lord personalities will not abandon a battlefield to flee to a fortress
			 (assign, ":continue", 1),
			 (try_begin),
				(this_or_next|troop_slot_eq, ":cur_troop", slot_lord_reputation_type, lrep_upstanding),
					(troop_slot_eq, ":cur_troop", slot_lord_reputation_type, lrep_martial),
				(get_party_ai_current_object, ":ai_object", ":cur_party"),
				(party_is_active, ":ai_object"),
				(party_get_battle_opponent, ":battle_opponent", ":ai_object"),
				(party_is_active, ":battle_opponent"),
				(assign, ":continue", 0),
			 (try_end),
			 (eq, ":continue", 1),


             (store_faction_of_party, ":party_faction", ":cur_party"),
             (party_get_slot, ":commander_party", ":cur_party", slot_party_commander_party),
             (faction_get_slot, ":faction_marshall", ":party_faction", slot_faction_marshall),
             (neq, ":faction_marshall", ":cur_troop"),
             (assign, ":continue", 1),
             (try_begin),
               (ge, ":faction_marshall", 0),
               (troop_get_slot, ":faction_marshall_party", ":faction_marshall", slot_troop_leaded_party),
		(ge, ":faction_marshall_party", 0),
               (party_is_active, ":faction_marshall_party", 0),
               (eq, ":commander_party", ":faction_marshall_party"),
               (assign, ":continue", 0),
             (try_end),
             (eq, ":continue", 1),
             (assign, ":done", 0),
             (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
               (eq, ":done", 0),
               (party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
               (store_faction_of_party, ":center_faction", ":cur_center"),
               (store_relation, ":cur_relation", ":center_faction", ":party_faction"),
               (gt, ":cur_relation", 0),
               (store_distance_to_party_from_party, ":cur_distance", ":cur_party", ":cur_center"),
               (lt, ":cur_distance", 20),
               (party_get_position, pos1, ":cur_party"),
               (party_get_position, pos2, ":cur_center"),
               (neg|position_is_behind_position, pos2, pos1),
               (call_script, "script_party_set_ai_state", ":cur_party", spai_retreating_to_center, ":cur_center"),
               (assign, ":done", 1),
             (try_end),
           (try_end),
         (else_try),
           (troop_set_slot, ":cur_troop", slot_troop_leaded_party, -1),
         (try_end),
       (try_end),
    ]),

  # Centers give alarm if the player is around
  (0.5,
   [
     (store_current_hours, ":cur_hours"),
     (store_mod, ":cur_hours_mod", ":cur_hours", 11),
     (store_sub, ":hour_limit", ":cur_hours", 5),
     (party_get_num_companions, ":num_men", "p_main_party"),
     (party_get_num_prisoners, ":num_prisoners", "p_main_party"),
     (val_add, ":num_men", ":num_prisoners"),
     (convert_to_fixed_point, ":num_men"),
     (store_sqrt, ":num_men_effect", ":num_men"),
     (convert_from_fixed_point, ":num_men_effect"),
     (try_begin),
       (eq, ":cur_hours_mod", 0),
       #Reduce alarm by 2 in every 11 hours.
       (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
         (faction_get_slot, ":player_alarm", ":cur_faction", slot_faction_player_alarm),
         (val_sub, ":player_alarm", 1),
         (val_max, ":player_alarm", 0),
         (faction_set_slot, ":cur_faction", slot_faction_player_alarm, ":player_alarm"),
       (try_end),
     (try_end),
     (eq, "$g_player_is_captive", 0),
     (try_for_range, ":cur_center", centers_begin, centers_end),
       (store_faction_of_party, ":cur_faction", ":cur_center"),
       (store_relation, ":reln", ":cur_faction", "fac_player_supporters_faction"),
       (lt, ":reln", 0),
       (store_distance_to_party_from_party, ":dist", "p_main_party", ":cur_center"),
       (lt, ":dist", 5),
       (store_mul, ":dist_sqr", ":dist", ":dist"),
       (store_sub, ":dist_effect", 20, ":dist_sqr"),
       (store_sub, ":reln_effect", 20, ":reln"),
       (store_mul, ":total_effect", ":dist_effect", ":reln_effect"),
       (val_mul, ":total_effect", ":num_men_effect"),
       (store_div, ":spot_chance", ":total_effect", 10),
       (store_random_in_range, ":random_spot", 0, 1000),
       (lt, ":random_spot", ":spot_chance"),
       (faction_get_slot, ":player_alarm", ":cur_faction", slot_faction_player_alarm),
       (val_add, ":player_alarm", 1),
       (val_min, ":player_alarm", 100),
       (faction_set_slot, ":cur_faction", slot_faction_player_alarm, ":player_alarm"),
       (try_begin),
         (neg|party_slot_ge, ":cur_center", slot_center_last_player_alarm_hour, ":hour_limit"),
         (str_store_party_name_link, s1, ":cur_center"),
         (display_message, "@Your party is spotted by {s1}."),
         (party_set_slot, ":cur_center", slot_center_last_player_alarm_hour, ":cur_hours"),
       (try_end),
     (try_end),
    ]),

  # Consuming food at every 14 hours
  (14,
   [
    (eq, "$g_player_is_captive", 0),
    (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
    (assign, ":num_men", 0),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
      (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
      (val_add, ":num_men", ":stack_size"),
    (try_end),
    (val_div, ":num_men", 3),
    (val_max, ":num_men", 1),
    # (try_begin), #SB : val_max
      # (eq, ":num_men", 0),
      # (val_add, ":num_men", 1),
    # (try_end),

    (try_begin),
      (assign, ":number_of_foods_player_has", 0),
      (try_for_range, ":cur_edible", food_begin, food_end),
        (call_script, "script_cf_player_has_item_without_modifier", ":cur_edible", imod_rotten),
        (val_add, ":number_of_foods_player_has", 1),
      (try_end),
      (try_begin),
        (ge, ":number_of_foods_player_has", 6),
        (unlock_achievement, ACHIEVEMENT_ABUNDANT_FEAST),
      (try_end),
    (try_end),

    # #SB : pre-calculate consumption amount for qst_deliver_wine items, although as with deliver_grain we might not care
    # (try_begin),
      # (check_quest_active,"qst_deliver_wine"),
      # (quest_get_slot, ":quest_target_item", "qst_deliver_wine", slot_quest_target_item),
      # (quest_get_slot, ":quest_target_amount", "qst_deliver_wine", slot_quest_target_amount),
      # (assign, ":quest_amount", 0),
      # (troop_get_inventory_capacity, ":capacity", "trp_player"),
      # (try_for_range, ":cur_slot", 10, ":capacity"),
        # (troop_get_inventory_slot, ":cur_item", "trp_player", ":cur_slot"),
        # (eq, ":cur_item", ":quest_target_item"),
        # (troop_inventory_slot_get_item_amount, ":cur_amount", "trp_player", ":cur_slot"),
        # (val_add, ":quest_amount", ":cur_amount"),
      # (try_end),
    # (try_end),
    (assign, ":consumption_amount", ":num_men"),
    (assign, ":no_food_displayed", 0),
    (try_for_range, ":unused", 0, ":consumption_amount"),
      (assign, ":available_food", 0),
      (try_for_range, ":cur_food", food_begin, food_end),
        (item_set_slot, ":cur_food", slot_item_is_checked, 0),
        (call_script, "script_cf_player_has_item_without_modifier", ":cur_food", imod_rotten),
        (val_add, ":available_food", 1),
      (try_end),
      (try_begin),
        (gt, ":available_food", 0),
        (store_random_in_range, ":selected_food", 0, ":available_food"),
        (call_script, "script_consume_food", ":selected_food"),
      (else_try),
        (eq, ":no_food_displayed", 0),
        (display_message, "@Party has nothing to eat!", message_defeated), #SB : same colour const
        (call_script, "script_change_player_party_morale", -3),
        (assign, ":no_food_displayed", 1),
#NPC companion changes begin
        (try_begin),
          (gt, ":num_men", 1), #SB : easier check
            # (call_script, "script_party_count_fit_regulars", "p_main_party"),
            # (gt, reg0, 0),
          (call_script, "script_objectionable_action", tmt_egalitarian, "str_men_hungry"),
        (try_end),
#NPC companion changes end
      (try_end),
    (try_end),
    ]),

  # Setting item modifiers for food
  (24,
   [
     (troop_get_inventory_capacity, ":inv_size", "trp_player"),
     #SB : add chance to prevent spoilage
     (store_skill_level, ":management", "skl_inventory_management", "trp_player"),
     (val_mul, ":management", 4),
     (val_div, ":management", 5),
     (try_for_range, ":i_slot", 10, ":inv_size"),
       (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
       (this_or_next|eq, ":item_id", "itm_cattle_meat"),
       (this_or_next|eq, ":item_id", "itm_chicken"),
       (eq, ":item_id", "itm_pork"),

       (troop_get_inventory_slot_modifier, ":modifier", "trp_player", ":i_slot"),
       (try_begin),
         (is_between, ":modifier", imod_fresh, imod_rotten),
         (val_add, ":modifier", 1),
         (try_begin), # SB : spoilage, objection
           (eq, ":modifier", imod_rotten),
           (troop_inventory_slot_get_item_amount, ":amount", "trp_player", ":i_slot"),
           (troop_inventory_slot_get_item_max_amount, ":max", "trp_player", ":i_slot"),
           (store_sub, ":amount", ":max", ":amount"), #get amount consumed already
           (val_mul, ":amount", 100),
           (val_div, ":amount", ":max"),
           (store_random_in_range, ":max", 0, ":amount"),
           (try_begin),
             (lt, ":max", ":management"), # saving throw
             (ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
             (assign, ":modifier", imod_smelling),
           (else_try), # spoiled critic
             (call_script, "script_objectionable_action", tmt_aristocratic, "str_rotten_food"),
           (try_end),
         (try_end),
         (troop_set_inventory_slot_modifier, "trp_player", ":i_slot", ":modifier"),
       (else_try),
         (lt, ":modifier", imod_fresh),
         (troop_set_inventory_slot_modifier, "trp_player", ":i_slot", imod_fresh),
       (try_end),
     (try_end),
    ]),


# Updating player icon in every frame
	#madsci reworked icon thing
  (0.1,
   [
(assign, ":end", "p_sabiroi_village"),
(val_add, ":end", 1),
    (try_for_parties, ":party_no"),
	(this_or_next|eq, ":party_no", "p_main_party"),
	(this_or_next|is_between, ":party_no", "p_onoguroi_village", ":end"),
        (gt, ":party_no", last_static_party), #madsci
	(party_get_icon, ":icon", ":party_no"),
	(assign, ":new_icon", -1),
		(try_begin),
		(eq, ":party_no", "p_main_party"),
		(neg|party_slot_eq, ":party_no", slot_party_on_water, 1),
		(neq, "$g_player_icon_state", pis_camping),
			(try_begin),
			(gt, "$players_kingdom", 0),
      				(try_begin),
				(eq, "$players_kingdom", "fac_player_supporters_faction"),
				(faction_get_slot, ":culture", "$players_kingdom", slot_faction_culture),
					(try_begin),
					(eq, ":culture", "fac_culture_empire"),
					(assign, ":new_icon", "icon_roman_army_e"),
					(else_try),
					(eq, ":culture", "fac_culture_12"),
					(assign, ":new_icon", "icon_steppe_lord"),
					(else_try),
					(eq, ":culture", "fac_culture_6"),
					(assign, ":new_icon", "icon_sassanid_lord"),
					(else_try),
					(assign, ":new_icon", "icon_regular_army"),
					(try_end),
				(else_try),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_1"),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_2"),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_13"),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_22"),
      				(this_or_next|eq, "$players_kingdom", "fac_rebel_kingdom_1"),
      				(this_or_next|eq, "$players_kingdom", "fac_rebel_kingdom_2"),
      				(eq, "$players_kingdom", "fac_rebel_kingdom_3"),
      				(assign, ":new_icon", "icon_roman_army_1"),
      				(else_try),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_7"),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_8"),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_9"),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_10"),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_12"),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_14"),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_19"),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_20"),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_21"),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_30"),
      				(eq, "$players_kingdom", "fac_kingdom_29"),
     				(assign, ":new_icon", "icon_germanic_army_1"),
      				(else_try),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_3"),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_4"),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_11"),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_15"),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_17"),
      				(eq, "$players_kingdom", "fac_kingdom_18"),
      				(assign, ":new_icon", "icon_germanic_army_2"),
      				(else_try),
      				(eq, "$players_kingdom", "fac_kingdom_6"),
      				(assign, ":new_icon", "icon_sassanid_lord"),
      				(else_try),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_16"),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_24"),
      				(eq, "$players_kingdom", "fac_kingdom_28"),
      				(assign, ":new_icon", "icon_caucasian_army"),
      				(else_try),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_25"),
      				(eq, "$players_kingdom", "fac_kingdom_26"),
      				(assign, ":new_icon", "icon_african_army"),
      				(else_try),
      				(this_or_next|eq, "$players_kingdom", "fac_kingdom_23"),
      				(eq, "$players_kingdom", "fac_kingdom_27"),
      				(assign, ":new_icon", "icon_steppe_lord"),
      				(else_try),
      				(assign, ":new_icon", "icon_regular_army"),
      				(try_end),
			(else_try),
			(troop_get_inventory_slot, ":cur_horse", "trp_player", ek_horse),
      				(try_begin),
				(eq, ":icon", "icon_player"),
        			(ge, ":cur_horse", 0),
        			(assign, ":new_icon", "icon_player_horseman"),
      				(else_try),
				(eq, ":icon", "icon_player_horseman"),
        			(lt, ":cur_horse", 0),
        			(assign, ":new_icon", "icon_player"),
      				(try_end),
			(try_end),
		(try_end),

		(party_get_current_terrain, ":terrain_type", ":party_no"),
        	(try_begin),
		(this_or_next|eq, ":terrain_type", rt_water),
		(this_or_next|eq, ":terrain_type", rt_deep_water),
		(this_or_next|eq, ":terrain_type", rt_river),
		(eq, ":terrain_type", rt_bridge),
                (neq, ":icon", "icon_ship"),
		(call_script, "script_check_ports", ":party_no"),
		(this_or_next|eq, ":terrain_type", rt_water),
		(this_or_next|eq, ":terrain_type", rt_deep_water),
		(gt, reg0, -1), #port near
                (party_set_slot, ":party_no", slot_icon_backup, ":icon"),
            	(assign, ":new_icon", "icon_ship"),
		(party_set_slot, ":party_no", slot_party_on_water, 1),
        	(else_try),
		(neq, ":terrain_type", rt_water),
		(neq, ":terrain_type", rt_deep_water),
		(neq, ":terrain_type", rt_river),
		(neq, ":terrain_type", rt_bridge),
                (eq, ":icon", "icon_ship"),
    		(party_get_slot, ":icon", ":party_no", slot_icon_backup),
		(gt, ":icon", -1),
    		(assign, ":new_icon", ":icon"),
		(party_set_slot, ":party_no", slot_party_on_water, 0),
            	(try_end),
	(gt, ":new_icon", -1),
    	(party_set_icon, ":party_no", ":new_icon"),
    (try_end),
    ]),

 #Update how good a target player is for bandits
  (2,
   [
       (store_troop_gold, ":total_value", "trp_player"),
       (store_div, ":bandit_attraction", ":total_value", (10000/100)), #10000 gold = excellent_target

       (troop_get_inventory_capacity, ":inv_size", "trp_player"),
       (try_for_range, ":i_slot", 0, ":inv_size"),
         (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
         (ge, ":item_id", 0),
         (try_begin),
           (is_between, ":item_id", trade_goods_begin, trade_goods_end),
           (store_item_value, ":item_value", ":item_id"),
           (val_add, ":total_value", ":item_value"),
         (try_end),
       (try_end),
       (val_clamp, ":bandit_attraction", 0, 100),
       #SB : disallow bandit attraction while raiding villages so they don't join on the "side" of villagers
       # (try_begin),
         # (is_between, "$g_player_raiding_village", villages_begin, villages_end),
         # (assign, ":bandit_attraction", 0),
       # (try_end),
       (party_set_bandit_attraction, "p_main_party", ":bandit_attraction"),
    ]),


	#This is a backup script to activate the player faction if it doesn't happen automatically, for whatever reason
  (3,
	[
    (assign, ":break_loop", walled_centers_end),
	(try_for_range, ":center", walled_centers_begin, ":break_loop"),
		(faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
		(store_faction_of_party, ":center_faction", ":center"),
		(eq, ":center_faction", "fac_player_supporters_faction"),
        (call_script, "script_activate_player_faction", "trp_player"),
        (assign, ":break_loop", -1),
	(try_end),
	##diplomacy start+
	#Piggyback on this: if the minister somehow gets cleared, or wasn't set
	#automatically, reappoint one.
	(try_begin),
		(is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
		(le, "$g_player_minister", 0),
		(faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
		(ge, ":faction_leader", 0),
		(try_begin),
			(this_or_next|eq, ":faction_leader", "trp_player"),
            (troop_slot_eq, "trp_player", slot_troop_spouse, ":faction_leader"),
			(assign, "$g_player_minister", "trp_temporary_minister"),
			(troop_set_faction, "trp_temporary_minister", "fac_player_supporters_faction"),
		(else_try),
			(is_between, ":faction_leader", heroes_begin, heroes_end),
			(troop_slot_eq, ":faction_leader", slot_troop_spouse, "trp_player"),
			(assign, "$g_player_minister", "trp_temporary_minister"),
			(troop_set_faction, "trp_temporary_minister", "fac_player_supporters_faction"),
		(try_end),
	(try_end),
	##diplomacy end+
	]),

  # Checking escape chances of prisoners that joined the party recently.
  (6,
   [(gt, "$g_prisoner_recruit_troop_id", 0),
    (gt, "$g_prisoner_recruit_size", 0),
    (gt, "$g_prisoner_recruit_last_time", 0),
    (is_currently_night),
    (try_begin),
      (store_skill_level, ":leadership", "skl_leadership", "trp_player"),
      (val_mul, ":leadership", 5),
      (store_sub, ":chance", 66, ":leadership"),
      (gt, ":chance", 0),
      (assign, ":num_escaped", 0),
      (try_for_range, ":unused", 0, "$g_prisoner_recruit_size"),
        (store_random_in_range, ":random_no", 0, 100),
        (lt, ":random_no", ":chance"),
        (val_add, ":num_escaped", 1),
      (try_end),
      (party_remove_members, "p_main_party", "$g_prisoner_recruit_troop_id", ":num_escaped"),
      (assign, ":num_escaped", reg0),
      (gt, ":num_escaped", 0),
      (try_begin),
        (gt, ":num_escaped", 1),
        (assign, reg2, 1),
      (else_try),
        (assign, reg2, 0),
      (try_end),
      (assign, reg1, ":num_escaped"),
      (str_store_troop_name_by_count, s1, "$g_prisoner_recruit_troop_id", ":num_escaped"),
      (display_log_message, "@{reg1} {s1} {reg2?have:has} escaped from your party during the night."),
    (try_end),
    (assign, "$g_prisoner_recruit_troop_id", 0),
    (assign, "$g_prisoner_recruit_size", 0),
    ]),

  # Offering ransom fees for player's prisoner heroes
  (24,
   [(neq, "$g_ransom_offer_rejected", 1),
    (call_script, "script_offer_ransom_amount_to_player_for_prisoners_in_party", "p_main_party"),
    (eq, reg0, 0),#no prisoners offered
    (assign, ":end_cond", walled_centers_end),
    #SB : TODO also offer ransom for spouse/co-ruler's owned centers
    (try_for_range, ":center_no", walled_centers_begin, ":end_cond"),
      (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
      (call_script, "script_offer_ransom_amount_to_player_for_prisoners_in_party", ":center_no"),
      (eq, reg0, 1),#a prisoner is offered
      (assign, ":end_cond", 0),#break
    (try_end),
    ]),

  # Exchanging hero prisoners between factions and clearing old ransom offers
  (72.0/(number_of_walled_centers),#72 on average
   [(assign, "$g_ransom_offer_rejected", 0),
    (store_random_in_range, ":center_no", walled_centers_begin, walled_centers_end),
    (try_begin),
      (party_get_slot, ":town_lord", ":center_no", slot_town_lord),
      (gt, ":town_lord", 0),
      (party_get_num_prisoner_stacks, ":num_stacks", ":center_no"),
      #SB : moved to top
      (store_troop_faction, ":faction_no", ":town_lord"),
      (troop_get_slot, ":wealth", ":town_lord", slot_troop_wealth),
      (str_store_faction_name, s2, ":faction_no"),
      (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
        (party_prisoner_stack_get_troop_id, ":stack_troop", ":center_no", ":i_stack"),
        (troop_is_hero, ":stack_troop"),
        (troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
        (store_random_in_range, ":random_no", 0, 100),
        (try_begin),
          (le, ":random_no", 10),
          (call_script, "script_calculate_ransom_amount_for_troop", ":stack_troop"),
          (assign, ":ransom_amount", reg0),
          ##diplomacy start+ Remove the wealth from the stack troop
          (call_script, "script_dplmc_remove_gold_from_lord_and_holdings", ":ransom_amount", ":stack_troop"),
          ##diplomacy end+
          (val_add, ":wealth", ":ransom_amount"),

          (party_remove_prisoners, ":center_no", ":stack_troop", 1),
          (call_script, "script_remove_troop_from_prison", ":stack_troop"),

          (store_troop_faction, ":troop_faction", ":stack_troop"),
          (str_store_troop_name, s1, ":stack_troop"),
          (str_store_faction_name, s2, ":faction_no"),
          (str_store_faction_name, s3, ":troop_faction"),
          #SB : colorize faction, add s2 for imprisoning faction
          (faction_get_color, ":color", ":troop_faction"),
          (display_log_message, "@{s1} of {s3} has been released from captivity by {s2}.", ":color"),
        (try_end),
        #SB : moved to bottom
        (troop_set_slot, ":town_lord", slot_troop_wealth, ":wealth"),
      (try_end),
    (try_end),
    ]),

   (72.0/(number_of_villages),#72 hours on average
   [
    (store_random_in_range, ":village_no", villages_begin,villages_end),
     (call_script, "script_update_villages_infested_by_bandits", ":village_no"),
        (call_script, "script_update_volunteer_troops_in_village", ":village_no"),
       (call_script, "script_update_npc_volunteer_troops_in_village", ":village_no"),
    ]),

    (72.0/(number_of_walled_centers),#72 hours on average
   [

     (store_random_in_range, ":center_no", walled_centers_begin, walled_centers_end),
     (party_slot_eq, ":center_no", slot_center_is_besieged_by, -1),#not under siege
     (call_script, "script_update_volunteer_troops_in_towns_castles", ":center_no"),
     (call_script, "script_check_center_size", ":center_no"),
    ]),

    (2,
   [
    (store_random_in_range, ":center_no2", minor_towns_begin, minor_towns_end), #minor factions
    (call_script, "script_update_volunteer_troops_in_towns_castles", ":center_no2"),
    ]),

  (12,
   [
    (store_random_in_range, ":switch", 0, 8),
    (try_begin),
        (eq, ":switch", 0),
        (call_script, "script_update_mercenary_units_of_towns"),
    (else_try),
        (eq, ":switch", 1),
        (call_script, "script_update_ransom_brokers"),
    (else_try),
        (eq, ":switch", 2),
        (call_script, "script_update_tavern_travellers"),
    (else_try),
        (eq, ":switch", 3),
        (call_script, "script_update_tavern_minstrels"),
    (else_try),
        (eq, ":switch", 4),
        (call_script, "script_update_booksellers"),
    (else_try),
        (call_script, "script_update_other_taverngoers"),
    (try_end),
    ]),


  # Setting random walker types
  (24.0/(number_of_centers),
   [(store_random_in_range, ":center_no", centers_begin, centers_end),
      (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
      (party_slot_eq, ":center_no", slot_party_type, spt_village),
      (call_script, "script_center_remove_walker_type_from_walkers", ":center_no", walkert_needs_money),
      (call_script, "script_center_remove_walker_type_from_walkers", ":center_no", walkert_needs_money_helped),
      (store_random_in_range, ":rand", 0, 100),
      (try_begin),
        (lt, ":rand", 70),
        (neg|party_slot_ge, ":center_no", slot_town_prosperity, 60),
        (call_script, "script_cf_center_get_free_walker", ":center_no"),
        (call_script, "script_center_set_walker_to_type", ":center_no", reg0, walkert_needs_money),
      (try_end),
    ]),

  # Checking center upgrades
  (12.0/(number_of_centers),
   [#12/380
    (try_begin),
       (lt, "$g_set_center_upgrades", centers_begin),
       (assign, "$g_set_center_upgrades", centers_begin),
    (try_end),

    (try_begin),
       (ge, "$g_set_center_upgrades", centers_end),
       (assign, "$g_set_center_upgrades", centers_begin),
    (try_end),

    # (try_begin),
        # (neg|party_slot_ge, "$g_set_center_upgrades", slot_party_looted_left_days, 1),#is not looted
        (try_for_range, ":slot", 0, 2),
            (try_begin),
                (eq, ":slot", 0),
                (assign, ":improvement_slot", slot_center_current_improvement),
                (assign, ":improvement_time_slot", slot_center_improvement_end_hour),
            (else_try),
                (assign, ":improvement_slot", slot_center_current_improvement_2),
                (assign, ":improvement_time_slot", slot_center_improvement_2_end_hour),
            (try_end),
            (call_script, "script_cf_check_building_finished", ":improvement_slot", ":improvement_time_slot"),
        (try_end),
    # (try_end),
    (party_set_slot, "$g_set_center_upgrades", dplmc_slot_village_reserved_by_recruiter, 0),
    (val_add, "$g_set_center_upgrades", 1),    #pig packing
    ]),

  # Adding tournaments to towns
  # Adding bandits to towns and villages
  (24,
   [(assign, ":num_active_tournaments", 0),
    (try_for_range, ":center_no", towns_begin, towns_end),
      (party_get_slot, ":has_tournament", ":center_no", slot_town_has_tournament),
      (try_begin),
        (eq, ":has_tournament", 1),#tournament ended, simulate
        (call_script, "script_fill_tournament_participants_troop", ":center_no", 0),
        (call_script, "script_sort_tournament_participant_troops"),#may not be needed
        (call_script, "script_get_num_tournament_participants"),
        (store_sub, ":needed_to_remove_randomly", reg0, 1),
        (call_script, "script_remove_tournament_participants_randomly", ":needed_to_remove_randomly"),
        (call_script, "script_sort_tournament_participant_troops"),
        (troop_get_slot, ":winner_troop", "trp_tournament_participants", 0),
        (try_begin),
          (is_between, ":winner_troop", active_npcs_begin, active_npcs_end),
          (str_store_troop_name_link, s1, ":winner_troop"),
          (str_store_party_name_link, s2, ":center_no"),
          #SB : log message, change color, add money
          (display_log_message, "@{s1} has won the tournament at {s2}.", message_alert),
          (call_script, "script_change_troop_renown", ":winner_troop", 20),
          (try_begin),
            (ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
            (store_faction_of_party, ":center_faction", ":center_no"),
            (call_script, "script_dplmc_get_troop_standing_in_faction", ":winner_troop", ":center_faction"),
            (store_mul, ":reward", reg0, 20), #1200 for leader, 600 for lord etc
            (val_add, ":reward", 150),
            (call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", ":reward", ":winner_troop"), #add some wealth
          (else_try),
            (call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", 200, ":winner_troop"), #add some wealth
          (try_end),
        (try_end),
      (try_end),
      (val_sub, ":has_tournament", 1),
      (val_max, ":has_tournament", 0),
      (party_set_slot, ":center_no", slot_town_has_tournament, ":has_tournament"),
      (try_begin),
        (gt, ":has_tournament", 0),
        (val_add, ":num_active_tournaments", 1),
      (try_end),
    (try_end),

    (try_for_range, ":center_no", centers_begin, centers_end),
      (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
      (party_slot_eq, ":center_no", slot_party_type, spt_village),
      (party_get_slot, ":has_bandits", ":center_no", slot_center_has_bandits),
      (try_begin),
        (le, ":has_bandits", 0),
        (assign, ":continue", 0),
        (try_begin),
          (check_quest_active, "qst_deal_with_night_bandits"),
          (quest_slot_eq, "qst_deal_with_night_bandits", slot_quest_target_center, ":center_no"),
          (neg|check_quest_succeeded, "qst_deal_with_night_bandits"),
          (assign, ":continue", 1),
        (else_try),
          (store_random_in_range, ":random_no", 0, 100),
          (lt, ":random_no", 3),
          (assign, ":continue", 1),
        (try_end),

        ## SB : add variety to night bandits
        (try_begin),
          (eq, ":continue", 1),
          (call_script, "script_center_get_bandits", ":center_no", 1),
          (assign, ":bandit_troop", reg0),
          (party_set_slot, ":center_no", slot_center_has_bandits, ":bandit_troop"),
          (try_begin),
            (eq, "$cheat_mode", 1),
            (str_store_party_name, s1, ":center_no"),
            (str_store_troop_name_plural, s2, ":bandit_troop"),
            #(display_message, "@{!}{s1} is infested by {s2} (at night)."),
          (try_end),
        (try_end),
      (else_try),
        (try_begin),
          (assign, ":random_chance", 40),
          (try_begin),
            (party_slot_eq, ":center_no", slot_party_type, spt_town),
            (assign, ":random_chance", 20),
          (try_end),
          (store_random_in_range, ":random_no", 0, 100),
          (lt, ":random_no", ":random_chance"),
          (party_set_slot, ":center_no", slot_center_has_bandits, 0),
          (try_begin),
            (eq, "$cheat_mode", 1),
            (str_store_party_name, s1, ":center_no"),
            #(display_message, "@{s1} is no longer infested by bandits (at night)."),
          (try_end),
        (try_end),
      (try_end),
    (try_end),

    (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
	  (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_feast),

	  (faction_get_slot, ":faction_object", ":faction_no", slot_faction_ai_object),
	  (is_between, ":faction_object", towns_begin, towns_end),

	  (party_slot_ge, ":faction_object", slot_town_has_tournament, 1),
	  #continue holding tournaments during the feast
      (party_set_slot, ":faction_object", slot_town_has_tournament, 2),
    (try_end),

	(try_begin),
      (lt, ":num_active_tournaments", 3),
      (store_random_in_range, ":random_no", 0, 100),
      #Add new tournaments with a 30% chance if there are less than 3 tournaments going on
      (lt, ":random_no", 30),
      (store_random_in_range, ":random_town", towns_begin, towns_end),
      (store_random_in_range, ":random_days", 12, 15),
      (party_set_slot, ":random_town", slot_town_has_tournament, ":random_days"),
      (try_begin),
        (eq, "$cheat_mode", 1),
        (str_store_party_name, s1, ":random_town"),
        #(display_message, "@{!}{s1} is holding a tournament."),
      (try_end),
    (try_end),
    ]),

  (3,
[
	(assign, "$g_player_tournament_placement", 0),
]),


#(0.1,

#	[
#	(try_begin),
#		(troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin),
#		(troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
#		(store_faction_of_troop, ":spouse_faction", ":spouse"),
#		(neq, ":spouse_faction", "$players_kingdom"),
#		(display_message, "@{!}ERROR! Player and spouse are separate factions"),
#	(try_end),
#	]
#),

  # Asking to give center to player
  (8,
   [
#    (assign, ":done", 0),
#    (try_for_range, ":center_no", centers_begin, centers_end),
#      (eq, ":done", 0),
#      (party_slot_eq, ":center_no", slot_town_lord, stl_reserved_for_player),
#      (assign, "$g_center_to_give_to_player", ":center_no"),
 #     (try_begin),
  #      (eq, "$g_center_to_give_to_player", "$g_castle_requested_by_player"),
   #     (assign, "$g_castle_requested_by_player", 0),
	#	(try_begin),
	#		(eq, "$g_castle_requested_for_troop", "trp_player"),
	#		(jump_to_menu, "mnu_requested_castle_granted_to_player"),
	#	(else_try),
	#		(jump_to_menu, "mnu_requested_castle_granted_to_player_husband"),
	#	(try_end),
    #  (else_try),
    #    (jump_to_menu, "mnu_give_center_to_player"),
    # (try_end),
    #  (assign, ":done", 1),
    #(else_try),
    #  (eq, ":center_no", "$g_castle_requested_by_player"),
    #  (party_slot_ge, ":center_no", slot_town_lord, active_npcs_begin),
    #  (assign, "$g_castle_requested_by_player", 0),
    #  (store_faction_of_party, ":faction", ":center_no"),
    #  (eq, ":faction", "$players_kingdom"),
    #  (assign, "$g_center_to_give_to_player", ":center_no"),
	#  (try_begin),
#		(eq, "$player_has_homage", 1),
#		(jump_to_menu, "mnu_requested_castle_granted_to_another"),
#	  (else_try),
#		(jump_to_menu, "mnu_requested_castle_granted_to_another_female"),
#	  (try_end),
 #     (assign, ":done", 1),
  #  (try_end),
    ]),

  # Taking denars from player while resting in not owned centers
  (1,
   [

    (neg|map_free),
    (is_currently_night),
#    (ge, "$g_last_rest_center", 0),
    (this_or_next|is_between, "$g_last_rest_center", centers_begin, centers_end),
    (is_between, "$g_last_rest_center", minor_towns_begin, minor_towns_end),

    (assign, ":break", 0),
    (try_begin),
      (check_quest_active, "qst_finnsburh_quest"),
      (eq, "$g_last_rest_center", "p_frisian_village"),
      (assign, ":break", 1),
    (else_try),
      (check_quest_active, "qst_haddingrs_revenge"),
      (eq, "$g_last_rest_center", "p_dani_village"),
      (assign, ":break", 1),
    (try_end),

    (eq, ":break", 0),

    # (neg|party_slot_eq, "$g_last_rest_center", slot_town_lord, "trp_player"),

##diplomacy begin
    (party_get_slot, ":town_lord", "$g_last_rest_center", slot_town_lord),
    (assign, ":affiliated", 0), #SB : use local, not register to track
    (try_begin),
      (is_between, ":town_lord", lords_begin, kingdom_ladies_end),
      (call_script, "script_dplmc_is_affiliated_family_member", ":town_lord"),
      (neq, reg0, 0),
      #SB : moved this to when you start
      # (display_message, "@You are within the walls of an affiliated family member and don't have to pay for accommodation."),
      (assign, ":affiliated", 1),
    (try_end),
    # (eq, ":affiliated", 0),
##diplomacy end

    (store_faction_of_party, ":last_rest_center_faction", "$g_last_rest_center"),
    # (neq, ":last_rest_center_faction", "fac_player_supporters_faction"),
    (store_current_hours, ":cur_hours"),
    (ge, ":cur_hours", "$g_last_rest_payment_until"),
    (store_add, "$g_last_rest_payment_until", ":cur_hours", 24),
    (store_troop_gold, ":gold", "trp_player"),

    # (val_add, ":total_cost", 1),
    (try_begin), #SB : non-paying conditions
      (this_or_next|eq, ":affiliated", 1),
      (this_or_next|eq, ":town_lord", "trp_player"),
      (eq, ":last_rest_center_faction", "fac_player_supporters_faction"),
      (assign, ":total_cost", 0),
    (else_try), #SB : calculate extra accomodation costs for wounded + mounts
      (party_get_num_companions, ":num_men", "p_main_party"),
      (try_begin),
        (lt, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
        (store_div, ":total_cost", ":num_men", 4),
      (else_try),
        (call_script, "script_party_count_fit_for_battle", "p_main_party"),
        (store_sub, ":num_wounded", ":num_men", reg0),
        (store_div, ":total_cost", ":num_men", 4),
        (val_div, ":num_wounded", 2),
        (val_add, ":total_cost", ":num_wounded"),
        #TODO : deal with mounted troop stabling costs?
      (try_end),
      (val_add, ":total_cost", 1), #the player
    (try_end),
    (try_begin),
      (ge, ":gold", ":total_cost"),
      (try_begin),
        (gt, ":total_cost", 0),
        (display_message, "@You pay for accommodation."),
        (troop_remove_gold, "trp_player", ":total_cost"),
      (try_end),
      (try_begin), #SB : faction troop morale
        (party_get_slot, ":old_faction", "$g_last_rest_center", slot_center_original_faction),
        (party_get_slot, ":relation", "$g_last_rest_center", slot_center_player_relation),
        (store_random_in_range, ":relation", ":relation", 1100), #spread of 1200 or 1000
        (ge, ":relation", 900),
        (val_sub, ":relation", ":total_cost"), #around 800
        (val_div, ":relation", 100),
        (val_max, ":relation", 1),
        (call_script, "script_change_faction_troop_morale", ":old_faction", ":relation", 0),
      (try_end),
    (else_try),
      (gt, ":gold", 0),
      (troop_remove_gold, "trp_player", ":gold"),
      #SB : stop resting
      (display_message, "@You are unable to pay for accommodation!", message_alert),
      (play_sound, "snd_encounter_nobleman"),
      # (val_mul, ":total_cost", -1),
      # (call_script, "script_change_player_party_morale", ":total_cost"),
      (val_div, ":total_cost", -10),
      (call_script, "script_change_player_relation_with_center", "$g_last_rest_center", ":total_cost"),
      (rest_for_hours, 0, 0, 0),
    (try_end),
    ]),

  # Spawn some bandits.
  (24*3,
   [
       (call_script, "script_spawn_bandits"),
    ]),

  # Make parties larger as game progresses.
  (24,
   [
       (call_script, "script_update_party_creation_random_limits"),
    ]),

  # Check if a faction is defeated every day
  (24,
   [
    (assign, ":num_active_factions", 0),
    (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
      (faction_set_slot, ":cur_kingdom", slot_faction_number_of_parties, 0),
    (try_end),
    (try_for_parties, ":cur_party"),
      (this_or_next|is_between, ":cur_party", centers_begin, centers_end),
      (party_slot_eq, ":cur_party", slot_party_type, spt_kingdom_hero_party),
      (store_faction_of_party, ":party_faction", ":cur_party"),
      (is_between, ":party_faction", kingdoms_begin, kingdoms_end),
      (faction_get_slot, ":kingdom_num_parties", ":party_faction", slot_faction_number_of_parties),
      (val_add, ":kingdom_num_parties", 1),
      (faction_set_slot, ":party_faction", slot_faction_number_of_parties, ":kingdom_num_parties"),
    (try_end),
    (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
      #(try_begin),
        #(eq, "$cheat_mode", 1),
        #(str_store_faction_name, s1, ":cur_kingdom"),
        #(faction_get_slot, reg1, ":cur_kingdom", slot_faction_number_of_parties),
        #(display_message, "@{!}Number of parties belonging to {s1}: {reg1}"),
      #(try_end),

      (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
      #SB : moved strength + stability call every 24 hrs
      # (call_script, "script_faction_recalculate_strength", ":cur_kingdom"),
      # (call_script, "script_evaluate_realm_stability", ":cur_kingdom"),
      (val_add, ":num_active_factions", 1),
      (faction_slot_eq, ":cur_kingdom", slot_faction_number_of_parties, 0),
      (assign, ":faction_removed", 0),
      (try_begin),
        (eq, ":cur_kingdom", "fac_player_supporters_faction"),
        (try_begin),
          (le, "$supported_pretender", 0),
          (faction_set_slot, ":cur_kingdom", slot_faction_state, sfs_inactive),
          (assign, ":faction_removed", 1),
        (try_end),
      (else_try),
        (neq, "$players_kingdom", ":cur_kingdom"),
        (faction_set_slot, ":cur_kingdom", slot_faction_state, sfs_defeated),
	(faction_set_slot, ":cur_kingdom",  slot_faction_days_survived, 0),
	(str_store_faction_name_link, s10, ":cur_kingdom"),
	(display_log_message, "@{s10} has been defeated by its enemies."),
        (try_for_parties, ":cur_party"),
          (store_faction_of_party, ":party_faction", ":cur_party"),
          (eq, ":party_faction", ":cur_kingdom"),
          (party_get_slot, ":home_center", ":cur_party", slot_party_home_center),
		(gt, ":home_center", 0), #madsci
          (store_faction_of_party, ":home_center_faction", ":home_center"),
          (party_set_faction, ":cur_party", ":home_center_faction"),
        (try_end),
        (assign, ":kingdom_pretender", -1),
        (try_for_range, ":cur_pretender", pretenders_begin, pretenders_end),
          (troop_slot_eq, ":cur_pretender", slot_troop_original_faction, ":cur_kingdom"),
          (assign, ":kingdom_pretender", ":cur_pretender"),
        (try_end),
        (try_begin),
          (is_between, ":kingdom_pretender", pretenders_begin, pretenders_end),
          (neq, ":kingdom_pretender", "$supported_pretender"),
          (troop_set_slot, ":kingdom_pretender", slot_troop_cur_center, 0), #remove pretender from the world
        (try_end),
        (assign, ":faction_removed", 1),
        (try_begin),
          (eq, "$players_oath_renounced_against_kingdom", ":cur_kingdom"),
          (assign, "$players_oath_renounced_against_kingdom", 0),
          (assign, "$players_oath_renounced_given_center", 0),
          (assign, "$players_oath_renounced_begin_time", 0),
          (call_script, "script_add_notification_menu", "mnu_notification_oath_renounced_faction_defeated", ":cur_kingdom", 0),
        (try_end),
        #This menu must be at the end because faction banner will change after this menu if the player's supported pretender's original faction is cur_kingdom
        (call_script, "script_add_notification_menu", "mnu_notification_faction_defeated", ":cur_kingdom", 0),

        (try_begin), #SB : morale dumped
          (this_or_next|neg|is_between, "$supported_pretender", pretenders_begin, pretenders_end),
          (neq, "$supported_pretender_old_faction", ":cur_kingdom"),
          (call_script, "script_change_faction_troop_morale", ":cur_kingdom", -5000, 0),
        (try_end),
      (try_end),
      (try_begin),
        (eq, ":faction_removed", 1),
        (val_sub, ":num_active_factions", 1),
        #(call_script, "script_store_average_center_value_per_faction"),
      (try_end),
      (try_for_range, ":cur_kingdom_2", kingdoms_begin, kingdoms_end),
        (call_script, "script_update_faction_notes", ":cur_kingdom_2"),
      (try_end),
    (try_end),
    (try_begin),
      (eq, ":num_active_factions", 1),
      (eq, "$g_one_faction_left_notification_shown", 0),
      (assign, "$g_one_faction_left_notification_shown", 1),
      (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
        (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
        (call_script, "script_add_notification_menu", "mnu_notification_one_faction_left", ":cur_kingdom", 0),
      (try_end),
    (try_end),
    ]),

  (3, #check to see if player's court has been captured
   [
     ##diplomacy start+ The player might be the ruler of another kingdom
     (assign, ":save_reg0", reg0),
	 (assign, ":alt_led_faction", "fac_player_supporters_faction"),
	 (try_begin),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
	    (ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":alt_led_faction", "$players_kingdom"),
	 (try_end),
	 ##diplomacy end+
     (try_begin), #The old court has been lost
     ##diplomacy begin
       (is_between, "$g_player_court", centers_begin, centers_end),
       (party_slot_eq, "$g_player_court", slot_village_infested_by_bandits, "trp_peasant_woman"),
       (call_script, "script_add_notification_menu", "mnu_notification_court_lost", 0, 0),
     (else_try),
     ##diplomacy end
       (is_between, "$g_player_court", centers_begin, centers_end),
       (store_faction_of_party, ":court_faction", "$g_player_court"),
       (neq, ":court_faction", "fac_player_supporters_faction"),
	   ##diplomacy start+ The player might be ruler of a faction other than fac_player_supporters_faction
	   (neq, ":court_faction", ":alt_led_faction"),
	   ##diplomacy end+
       (call_script, "script_add_notification_menu", "mnu_notification_court_lost", 0, 0),
     (else_try),	#At least one new court has been found
       (lt, "$g_player_court", centers_begin),
       #Will by definition not active until a center is taken by the player faction
       #Player minister must have been appointed at some point
       (this_or_next|faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
		(gt, "$g_player_minister", 0),

       (assign, ":center_found", 0),
       (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
         (eq, ":center_found", 0),
         (store_faction_of_party, ":court_faction", ":walled_center"),
		   ##diplomacy start+ The player might be ruler of a faction other than fac_player_supporters_faction
		   (this_or_next|eq, ":court_faction", ":alt_led_faction"),
		   ##diplomacy end+
         (eq, ":court_faction", "fac_player_supporters_faction"),
         (assign, ":center_found", ":walled_center"),
       (try_end),
       (ge, ":center_found", 1),
       (call_script, "script_add_notification_menu", "mnu_notification_court_lost", 0, 0),
     (try_end),
    #Also, piggy-backing on this -- having bandits go to lairs and back
    (try_for_parties, ":party_no"),
      (gt, ":party_no", last_static_party), #madsci
      (party_is_active, ":party_no"),
      (party_get_template_id, ":party_template", ":party_no"),
      (try_begin),
	(this_or_next|eq, ":party_template", "pt_classis_ravenna"), #madsci naval patrol AI
  (this_or_next|eq, ":party_template", "pt_classis_naples"),
	(eq, ":party_template", "pt_classis_constantinople"),
	(party_is_in_any_town, ":party_no"),
	(party_get_slot, ":origin", ":party_no", slot_village_bound_center),
	(party_get_slot, ":target", ":party_no", slot_party_last_traded_center),
	(party_get_slot, ":ai_object", ":party_no", slot_party_ai_object),
		(try_begin),
		(eq, ":ai_object", ":target"),
		(assign, ":ai_target", ":origin"),
		(else_try),
		(assign, ":ai_target", ":target"),
		(try_end),
	(party_set_slot, ":party_no", slot_party_ai_object, ":ai_target"),
	(party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
	(party_set_ai_object, ":party_no", ":ai_target"),
		(try_begin),
		(store_faction_of_party, ":town_faction",":ai_target"),
		(store_faction_of_party, ":party_faction",":party_no"),
		(neq, ":town_faction", ":party_faction"),
		(call_script, "script_remove_hero_prisoners", ":party_no"),
		(remove_party, ":party_no"),
		(try_end),
	(else_try),
	(eq, ":party_template", "pt_pirates_mediterranean"), #madsci simple pirate AI
	(get_party_ai_behavior, ":behavior", ":party_no"),
	(neq, ":behavior", ai_bhvr_attack_party),
	(store_random_in_range, ":ai_target", "p_malta", "p_mediterranean_sea"),
	(party_get_position, pos1, ":ai_target"),
	(map_get_random_position_around_position, pos2, pos1, 2),
	(party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_point),
	(party_set_ai_target_position, ":party_no", pos2),
	(party_set_ai_object, ":party_no", ":ai_target"),
	(else_try),
        (is_between, ":party_template", bandit_party_templates_begin, bandit_party_templates_end), #SB : template range
        (party_template_get_slot, ":bandit_lair", ":party_template", slot_party_template_lair_party),
        (try_begin),#If party is active and bandit is far away, then move to location
	(gt, ":bandit_lair", last_static_party), #madsci
          (store_distance_to_party_from_party, ":distance", ":party_no", ":bandit_lair"), #this is the cause of the error
          (gt, ":distance", 30),
          #All this needs checking
          (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_point),
          (party_get_position, pos5, ":bandit_lair"),
          (party_set_ai_target_position, ":party_no", pos5),
        (else_try), #Otherwise, act freely
          (get_party_ai_behavior, ":behavior", ":party_no"),
          (eq, ":behavior", ai_bhvr_travel_to_point),
          (try_begin),
            #(gt, ":bandit_lair", "p_spawn_points_end"),
		(gt, ":bandit_lair", last_static_party), #madsci
            (store_distance_to_party_from_party, ":distance", ":party_no", ":bandit_lair"),
            (lt, ":distance", 3),
            (party_set_ai_behavior, ":party_no", ai_bhvr_patrol_party),
            (party_template_get_slot, ":spawnpoint", ":party_template", slot_party_template_lair_spawnpoint),
            (is_between, ":spawnpoint", "p_steppe_bandit_spawn_point", "p_spawn_points_end"),
            (party_set_ai_object, ":party_no", ":spawnpoint"),
            (party_set_ai_patrol_radius, ":party_no", 45),
          (else_try), #why is this identical behavior?
            (lt, ":bandit_lair", "p_spawn_points_end"),
            (party_set_ai_behavior, ":party_no", ai_bhvr_patrol_party),
            (party_template_get_slot, ":spawnpoint", ":party_template", slot_party_template_lair_spawnpoint),
            (is_between, ":spawnpoint", "p_steppe_bandit_spawn_point", "p_spawn_points_end"),
            (party_set_ai_object, ":party_no", ":spawnpoint"),
            (party_set_ai_patrol_radius, ":party_no", 45),
          (try_end),
        (try_end),
      (else_try),
	(eq, ":party_template", "pt_rebel_army"), #madsci rebellion AI
	(party_get_slot, ":home_center", ":party_no", slot_party_home_center),
	(gt, ":home_center", 0),
	(party_slot_eq, ":home_center", slot_center_is_besieged_by, -1),
	(store_faction_of_party, ":party_faction", ":party_no"),
	(store_faction_of_party, ":home_faction", ":home_center"),
		(try_begin),
		(eq, ":party_faction", ":home_faction"),
			(try_begin),
			(party_is_in_town, ":party_no", ":home_center"),
			(call_script, "script_party_add_party", ":home_center", ":party_no"),
			(remove_party, ":party_no"),
			(else_try),
			(party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
			(party_set_ai_object,":party_no",":home_center"),
			(try_end),
		(else_try),
            	(party_set_ai_behavior, ":party_no", ai_bhvr_patrol_party),
            	(party_set_ai_object, ":party_no", ":home_center"),
		(try_end),
	(else_try), #madsci rework this script
        (this_or_next|eq, ":party_template", "pt_center_reinforcements"),
        (eq, ":party_template", "pt_routed_warriors"),
        (party_slot_eq, ":party_no", slot_party_type, spt_reinforcement),
	(party_is_in_any_town, ":party_no"),
        (party_get_cur_town, ":cur_attached_town", ":party_no"),
	(party_get_slot, ":destination", ":party_no", slot_party_ai_object),
	(party_get_slot, ":village", ":party_no", slot_party_home_center),
        	(try_begin),
		(eq, ":party_template", "pt_center_reinforcements"),
		(is_between, ":cur_attached_town", centers_begin, centers_end),
		(eq, ":cur_attached_town", ":destination"),
		(store_faction_of_party, ":town_faction", ":cur_attached_town"),
		(store_faction_of_party, ":party_faction", ":party_no"),
		(neq, ":party_faction", ":town_faction"), #the faction has changed at some point so dont reinforce the enemy
			(try_begin),
			(is_between, ":village", centers_begin, centers_end),
			(party_set_slot, ":village", slot_village_reinforcement_party, -1),
        		(try_end),
		(remove_party, ":party_no"),
		(else_try),
		(is_between, ":cur_attached_town", centers_begin, centers_end),
          	(neq, ":cur_attached_town", ":destination"),
	  	(gt, ":destination", 0),
          	(party_detach, ":party_no"),  # stop and detach
          	(party_set_ai_behavior,":party_no",ai_bhvr_travel_to_party),
          	(party_set_ai_object,":party_no", ":destination"),
          	(party_set_flags, ":party_no", pf_default_behavior, 1), #madsci we want this turned on
        	(else_try),
		(eq, ":cur_attached_town", ":destination"),
        	(is_between, ":cur_attached_town", walled_centers_begin, walled_centers_end),
          	(party_get_num_companion_stacks, ":num_stacks", ":party_no"),
          	(store_faction_of_party, ":cur_faction", ":cur_attached_town"),
          		(try_begin), #player culture
			(gt, "$g_king_start", 0),
            		(this_or_next|eq, ":cur_faction", "fac_player_faction"),
            		(eq, ":cur_faction", "fac_player_supporters_faction"),
            		(is_between, "$g_player_culture", npc_kingdoms_begin, npc_kingdoms_end),
            		(assign, ":cur_faction", "$g_player_culture"),
          		(try_end),
          		(try_for_range_backwards, ":stack_no", 0, ":num_stacks"),
            		(party_stack_get_troop_id, ":troop_no", ":party_no", ":stack_no"),
            		(neg|troop_is_hero, ":troop_no"),
            		(assign, ":cur_relation", 100),
            			(try_begin), #routed parties sometimes contain extraneous units, players may also give random stuff to reinforcements
              			(store_faction_of_troop, ":faction_no", ":troop_no"),
				(neq, ":faction_no", ":cur_faction"),
					(try_begin),
					(is_between, ":faction_no", cultures_begin, cultures_end),
					(assign, ":troop_culture", ":faction_no"),
					(else_try),
					(faction_get_slot, ":troop_culture", ":faction_no", slot_faction_culture),
					(try_end),
					(try_begin),
					(is_between, ":cur_faction", cultures_begin, cultures_end),
					(assign, ":cur_culture", ":cur_faction"),
					(else_try),
					(faction_get_slot, ":cur_culture", ":cur_faction", slot_faction_culture),
					(try_end),
				(neq, ":troop_culture", ":cur_culture"),
              			(store_relation, ":cur_relation", ":cur_faction", ":faction_no"),
            			(try_end),
            		(this_or_next|is_between, ":troop_no", "trp_looter", bandits_end), #looters are easy to route, don't let them rejoin
            		(lt, ":cur_relation", 0),
            		(party_stack_get_size, ":stack_size", ":party_no", ":stack_no"),
            		(party_remove_members, ":party_no", ":troop_no", ":stack_size"),
            		(party_add_prisoners, ":cur_attached_town", ":troop_no", ":stack_size"),
          		(try_end),
        	(call_script, "script_party_add_party", ":cur_attached_town", ":party_no"),
			(try_begin), #unset slot before deallocating party
			(eq, ":party_template", "pt_center_reinforcements"),
			(is_between, ":village", centers_begin, centers_end),
			(party_set_slot, ":village", slot_village_reinforcement_party, -1),
        		(try_end),
		(remove_party, ":party_no"),
		(else_try),
			(try_begin), #unset slot before deallocating party
			(eq, ":party_template", "pt_center_reinforcements"),
			(is_between, ":village", centers_begin, centers_end),
			(party_set_slot, ":village", slot_village_reinforcement_party, -1),
        		(try_end),
		(remove_party, ":party_no"),
        	(try_end),
	(try_end),
    (try_end),
     #Piggybacking on trigger:
     (try_begin),
       (troop_get_slot, ":betrothed", "trp_player", slot_troop_betrothed),
       (gt, ":betrothed", 0),
       (neg|check_quest_active, "qst_wed_betrothed"),
       (neg|check_quest_active, "qst_wed_betrothed_female"),
       (str_store_troop_name, s5, ":betrothed"),
       (display_message, "@Betrothal to {s5} expires"),
       (troop_set_slot, "trp_player", slot_troop_betrothed, -1),
       (troop_set_slot, ":betrothed", slot_troop_betrothed, -1),
     (try_end),
	 ##diplomacy start+
	 (assign, reg0, ":save_reg0"),#revert register
	 ##diplomacy end+
     ]),

  # Reduce renown slightly by 0.5% every week
  (7 * 24,
   [
       (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
       (store_div, ":renown_decrease", ":player_renown", 200),
       (val_sub, ":player_renown", ":renown_decrease"),
       (troop_set_slot, "trp_player", slot_troop_renown, ":player_renown"),

       #SB : slowly increase renown of minister weekly instead of doing so upon assignment
       (try_begin),
         (gt, "$g_player_minister", 0),
         (neq, "$g_player_minister", "trp_temporary_minister"),
         (call_script, "script_change_troop_renown", "$g_player_minister", 10),
       (try_end)
    ]),

  # Read books if player is resting.
  (1, [(neg|map_free),
       (gt, "$g_player_reading_book", 0),
       (player_has_item, "$g_player_reading_book"),
       (store_attribute_level, ":int", "trp_player", ca_intelligence),
       (item_get_slot, ":int_req", "$g_player_reading_book", slot_item_intelligence_requirement),
       (le, ":int_req", ":int"),
       (item_get_slot, ":book_reading_progress", "$g_player_reading_book", slot_item_book_reading_progress),
       (item_get_slot, ":book_read", "$g_player_reading_book", slot_item_book_read),
       (eq, ":book_read", 0),
       (val_add, ":book_reading_progress", 7),
       (item_set_slot, "$g_player_reading_book", slot_item_book_reading_progress, ":book_reading_progress"),
       (ge, ":book_reading_progress", 1000),
       (item_set_slot, "$g_player_reading_book", slot_item_book_read, 1),
       (str_store_item_name, s1, "$g_player_reading_book"),
       (str_clear, s2),
       (try_begin),
         (eq, "$g_player_reading_book", "itm_book_tactics"),
         (troop_raise_skill, "trp_player", "skl_tactics", 1),
         (str_store_string, s2, "@ Your tactics skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_persuasion"),
         (troop_raise_skill, "trp_player", "skl_persuasion", 1),
         (str_store_string, s2, "@ Your persuasion skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_leadership"),
         (troop_raise_skill, "trp_player", "skl_leadership", 1),
         (str_store_string, s2, "@ Your leadership skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_intelligence"),
         (troop_raise_attribute, "trp_player", ca_intelligence, 1),
         (str_store_string, s2, "@ Your intelligence has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_trade"),
         (troop_raise_skill, "trp_player", "skl_trade", 1),
         (str_store_string, s2, "@ Your trade skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_weapon_mastery"),
         (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
         (str_store_string, s2, "@ Your weapon master skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_engineering"),
         (troop_raise_skill, "trp_player", "skl_engineer", 1),
         (str_store_string, s2, "@ Your engineer skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_proclus_1"),
         (troop_raise_attribute, "trp_player", ca_intelligence, 2),
         (str_store_string, s2, "@ Your intelligence has increased by 2."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_heretical_codex"),
         (troop_raise_attribute, "trp_player", ca_intelligence, 1),
         (troop_raise_skill, "trp_player", "skl_first_aid", 1),
         (str_store_string, s2, "@ Your intelligence and first aid has increased by 1."),
       (try_end),

       (unlock_achievement, ACHIEVEMENT_BOOK_WORM),

       (try_begin),
         (eq, "$g_infinite_camping", 0),
         (dialog_box, "@You have finished reading {s1}.{s2}", "@Book Read"),
       (try_end),

       (assign, "$g_player_reading_book", 0),
       ]),

# Removing cattle herds if they are way out of range
  (12, [
	(try_for_parties, ":cur_party"),
	(gt, ":cur_party", last_static_party), #madsci
          (party_slot_eq, ":cur_party", slot_party_type, spt_cattle_herd),
          (store_distance_to_party_from_party, ":dist",":cur_party", "p_main_party"),
          (try_begin),
            (gt, ":dist", 30),
            (remove_party, ":cur_party"),
            (try_begin),
              #Fail quest if the party is the quest party
              (check_quest_active, "qst_move_cattle_herd"),
              (neg|check_quest_concluded, "qst_move_cattle_herd"),
              (quest_slot_eq, "qst_move_cattle_herd", slot_quest_target_party, ":cur_party"),
              (call_script, "script_fail_quest", "qst_move_cattle_herd"),
            (end_try),
          (else_try),
            (gt, ":dist", 10),
            (party_set_slot, ":cur_party", slot_cattle_driven_by_player, 0),
            (party_set_ai_behavior, ":cur_party", ai_bhvr_hold),
          (try_end),
        (try_end),

  (try_for_range, ":leader", minor_kings_begin, minor_kings_end), #madsci disband minor faction levies if the player is very far
    (troop_get_slot, ":party_no", ":leader", slot_troop_leaded_party),
    (gt, ":party_no", 0),
    (party_is_active, ":party_no"),
    (party_get_battle_opponent, ":opponent",":party_no"),
    (lt, ":opponent", 0), #party is not itself involved in a battle
    (store_faction_of_party, ":party_faction", ":party_no"),
    (eq, ":party_faction", "fac_player_supporters_faction"),
    (store_distance_to_party_from_party, ":dist", ":party_no", "p_main_party"),
    (gt, ":dist", 30),
    (party_get_slot, ":minor_faction", ":party_no", slot_minor_faction_levies_original_faction),
    (str_store_party_name, s10, ":party_no"),
    (display_message, "@{s10} has disbanded."),
    (remove_party, ":party_no"),
    (troop_set_slot, ":leader", slot_troop_leaded_party, -1),
    (call_script, "script_change_player_relation_with_faction", ":minor_faction", -5),
    (try_begin),
      (troop_get_slot, ":home", ":leader", slot_troop_home),
      (is_between, ":home", minor_towns_begin, minor_towns_end),
      (party_add_leader, ":home", ":leader"),
    (try_end),
  (try_end),
(assign, "$last_joined_tournament", -1), #madsci
]),


#####!!!!!

# Village upgrade triggers

# School
  (24.0*14.0/(number_of_villages),
   [(store_random_in_range, ":cur_village", villages_begin, villages_end),
    (try_begin),
      # (party_slot_eq, ":cur_village", slot_town_lord, "trp_player"),
      (party_get_slot, ":town_lord", ":cur_village", slot_town_lord),
      #SB : also handle the case where player hands out villages
      (store_faction_of_party, ":faction_no", ":cur_village"),
      (try_begin),
        (eq, ":faction_no", "$players_kingdom"),
        (call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", ":faction_no"),
        (ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
        (assign, ":town_lord", "trp_player"),
      (try_end),
      (eq, ":town_lord", "trp_player"),

      (party_slot_eq, ":cur_village", slot_center_has_school, 1),
      (party_get_slot, ":cur_relation", ":cur_village", slot_center_player_relation),
      (val_add, ":cur_relation", 1),
      (val_min, ":cur_relation", 100),
      (party_set_slot, ":cur_village", slot_center_player_relation, ":cur_relation"),
    (try_end),

    (try_begin),
        (party_slot_ge, ":cur_village", slot_center_has_silver_mine, 1),
        (party_slot_eq, ":cur_village", slot_village_state, svs_normal),

        (store_random_in_range, ":goldmine_rent",5000,15000),
        (party_get_slot, ":rent", ":cur_village", slot_center_accumulated_rents),
        (val_add, ":rent", ":goldmine_rent"),
        (party_set_slot, ":cur_village", slot_center_accumulated_rents, ":rent"),
    (try_end),
    ]),

# Quest triggers:

# Remaining days text update
  (24, [(try_for_range, ":cur_quest", all_quests_begin, all_quests_end),
          (try_begin),
            (check_quest_active, ":cur_quest"),
            (try_begin),
              (eq, ":cur_quest", "qst_finnsburh_quest_2"),
              (quest_slot_eq, "qst_finnsburh_quest_2", slot_quest_current_state, 1),
              (quest_get_slot, ":timer", "qst_finnsburh_quest_2", slot_quest_temp_slot),
              (val_add, ":timer", 1),
              (try_begin),
                (eq, ":timer", 30),
                (call_script, "script_add_notification_menu", "mnu_finn_2_quest_start",0,0),
              (else_try),
                (quest_set_slot, "qst_finnsburh_quest_2", slot_quest_temp_slot, ":timer"),
                (store_sub, reg0, 30, ":timer"),
                (val_max, reg0, 0),
                (add_quest_note_from_sreg, "qst_finnsburh_quest_2", 7, "@The preparations will take approximately {reg0} days.", 0),
              (try_end),
            (else_try),
              (neg|check_quest_concluded, ":cur_quest"),
              (quest_slot_ge, ":cur_quest", slot_quest_expiration_days, 1),
              (quest_get_slot, ":exp_days", ":cur_quest", slot_quest_expiration_days),
              (val_sub, ":exp_days", 1),
              (try_begin),
                (eq, ":exp_days", 0),
                (eq, ":cur_quest", "qst_severinus_quest"),
                (call_script, "script_fail_quest", ":cur_quest"),
                (call_script, "script_end_quest", ":cur_quest"),
                (disable_party, "p_noricum_refugee_camp"),
                (call_script, "script_change_player_relation_with_faction", "fac_roman_christians", -1),
                (call_script, "script_change_player_honor", -1),
                (display_message, "@You hear news that a refugee camp in Noricum was pillaged by Germanic raiders."),
              (else_try),
                (eq, ":exp_days", 0),
                (call_script, "script_abort_quest", ":cur_quest", 1),
              (else_try),
                (quest_set_slot, ":cur_quest", slot_quest_expiration_days, ":exp_days"),
                (assign, reg0, ":exp_days"),
                (add_quest_note_from_sreg, ":cur_quest", 7, "@You have {reg0} days to finish this quest.", 0),
              (try_end),
            (try_end),
            #SB : delegate quest progression ticks
          (else_try),
            (quest_slot_ge, ":cur_quest", slot_quest_dont_give_again_remaining_days, 1),
            (quest_get_slot, ":value", ":cur_quest", slot_quest_dont_give_again_remaining_days),
            (val_sub, ":value", 1),
            (quest_set_slot, ":cur_quest", slot_quest_dont_give_again_remaining_days, ":value"),
          (try_end),
        (try_end),
    ]),

# Report to army quest
  (2,
   [
     (eq, "$g_infinite_camping", 0),
     (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
     (eq, "$g_player_is_captive", 0),

	 (try_begin),
		(check_quest_active, "qst_report_to_army"),
		(faction_slot_eq, "$players_kingdom", slot_faction_marshall, -1),
		(call_script, "script_abort_quest", "qst_report_to_army", 0),
	 (try_end),

	 (faction_get_slot, ":faction_object", "$players_kingdom", slot_faction_ai_object),

     (neg|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_default),
     (neg|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_feast),

     (assign, ":continue", 1),
     (try_begin),
       (this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_attacking_enemies_around_center),
       (this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_attacking_center),
       (faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_raiding_village),
       (neg|is_between, ":faction_object", walled_centers_begin, walled_centers_end),
       (assign, ":continue", 0),
     (try_end),
     (eq, ":continue", 1),

	 (assign, ":kingdom_is_at_war", 0),
	 (try_for_range, ":faction", kingdoms_begin, kingdoms_end),
		(neq, ":faction", "$players_kingdom"),
		(store_relation, ":relation", ":faction", "$players_kingdom"),
		(lt, ":relation", 0),
		(assign, ":kingdom_is_at_war", 1),
	 (try_end),
	 (eq, ":kingdom_is_at_war", 1),

     (neg|check_quest_active, "qst_report_to_army"),
     (neg|check_quest_active, "qst_follow_army"),

     (neg|quest_slot_ge, "qst_report_to_army", slot_quest_dont_give_again_remaining_days, 1),
     (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
     (gt, ":faction_marshall", 0),
     (troop_get_slot, ":faction_marshall_party", ":faction_marshall", slot_troop_leaded_party),
     (gt, ":faction_marshall_party", 0),
     (party_is_active, ":faction_marshall_party"),

     (store_distance_to_party_from_party, ":distance_to_marshal", ":faction_marshall_party", "p_main_party"),
     (le, ":distance_to_marshal", 96),

     (assign, ":has_no_quests", 1),
     (try_for_range, ":cur_quest", lord_quests_begin, lord_quests_end),
       (check_quest_active, ":cur_quest"),
       (quest_slot_eq, ":cur_quest", slot_quest_giver_troop, ":faction_marshall"),
       (assign, ":has_no_quests", 0),
     (try_end),
     (eq, ":has_no_quests", 1),

     (try_for_range, ":cur_quest", lord_quests_begin_2, lord_quests_end_2),
       (check_quest_active, ":cur_quest"),
       (quest_slot_eq, ":cur_quest", slot_quest_giver_troop, ":faction_marshall"),
       (assign, ":has_no_quests", 0),
     (try_end),
     (eq, ":has_no_quests", 1),

     (try_for_range, ":cur_quest", army_quests_begin, army_quests_end),
       (check_quest_active, ":cur_quest"),
       (assign, ":has_no_quests", 0),
     (try_end),
     (eq, ":has_no_quests", 1),

     (store_character_level, ":level", "trp_player"),
     (ge, ":level", 8),
     (assign, ":cur_target_amount", 2),
     (try_for_range, ":cur_center", centers_begin, centers_end),
       (party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
       (try_begin),
         (party_slot_eq, ":cur_center", slot_party_type, spt_town),
         (val_add, ":cur_target_amount", 3),
       (else_try),
         (party_slot_eq, ":cur_center", slot_party_type, spt_castle),
         (val_add, ":cur_target_amount", 1),
       (else_try),
         (val_add, ":cur_target_amount", 1),
       (try_end),
     (try_end),

     (val_mul, ":cur_target_amount", 4),
     (val_min, ":cur_target_amount", 60),
     (quest_set_slot, "qst_report_to_army", slot_quest_giver_troop, ":faction_marshall"),
     (quest_set_slot, "qst_report_to_army", slot_quest_target_troop, ":faction_marshall"),
     (quest_set_slot, "qst_report_to_army", slot_quest_target_amount, ":cur_target_amount"),
     (quest_set_slot, "qst_report_to_army", slot_quest_expiration_days, 4),
     (quest_set_slot, "qst_report_to_army", slot_quest_dont_give_again_period, 22),
     (jump_to_menu, "mnu_kingdom_army_quest_report_to_army"),
   ]),


# Army quest initializer
  (3,
   [
     (assign, "$g_random_army_quest", -1),
     (check_quest_active, "qst_follow_army", 1),
     (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
#Rebellion changes begin
#     (neg|is_between, "$players_kingdom", rebel_factions_begin, rebel_factions_end),
#Rebellion changes end
     (neg|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_default),
     (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
     (neq, ":faction_marshall", "trp_player"),
     (gt, ":faction_marshall", 0),
     (troop_get_slot, ":faction_marshall_party", ":faction_marshall", slot_troop_leaded_party),
     (gt, ":faction_marshall_party", 0),
     (party_is_active, ":faction_marshall_party"),
     (store_distance_to_party_from_party, ":dist", ":faction_marshall_party", "p_main_party"),
     (try_begin),
       (lt, ":dist", 15),
       (assign, "$g_player_follow_army_warnings", 0),
       (store_current_hours, ":cur_hours"),
       (faction_get_slot, ":last_offensive_time", "$players_kingdom", slot_faction_last_offensive_concluded),
       (store_sub, ":passed_time", ":cur_hours", ":last_offensive_time"),

       (assign, ":result", -1),
       (try_begin),
         (store_random_in_range, ":random_no", 0, 100),
         (lt, ":random_no", 30),
         (troop_slot_eq, ":faction_marshall", slot_troop_does_not_give_quest, 0),
         (try_for_range, ":unused", 0, 20), #Repeat trial twenty times
           (eq, ":result", -1),
           (store_random_in_range, ":quest_no", army_quests_begin, army_quests_end),
           (neg|quest_slot_ge, ":quest_no", slot_quest_dont_give_again_remaining_days, 1),
           (try_begin),
             (eq, ":quest_no", "qst_deliver_cattle_to_army"),
			# (eq, 1, 0), #disables temporarily
             (try_begin),
               (faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_attacking_center),
               (gt, ":passed_time", 120),#5 days
               (store_random_in_range, ":quest_target_amount", 5, 10),
               (assign, ":result","qst_deliver_cattle_to_army"),
               (quest_set_slot, ":result", slot_quest_target_amount, ":quest_target_amount"),
               (quest_set_slot, ":result", slot_quest_expiration_days, 10),
               (quest_set_slot, ":result", slot_quest_dont_give_again_period, 30),
             (try_end),
           (else_try),
             (eq, ":quest_no", "qst_join_siege_with_army"),
			 (eq, 1, 0),
             (try_begin),
               (faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_attacking_center),
               (faction_get_slot, ":ai_object", "$players_kingdom", slot_faction_ai_object),
               (is_between, ":ai_object", walled_centers_begin, walled_centers_end),
               (party_get_battle_opponent, ":besieged_center", ":faction_marshall_party"),
               (eq, ":besieged_center", ":ai_object"),
               #army is assaulting the center
               (assign, ":result", ":quest_no"),
               (quest_set_slot, ":result", slot_quest_target_center, ":ai_object"),
               (quest_set_slot, ":result", slot_quest_expiration_days, 2),
               (quest_set_slot, ":result", slot_quest_dont_give_again_period, 15),
             (try_end),
           (else_try),
             (eq, ":quest_no", "qst_scout_waypoints"),
             (try_begin),
               (assign, ":end_cond", 100),
               (assign, "$qst_scout_waypoints_wp_1", -1),
               (assign, "$qst_scout_waypoints_wp_2", -1),
               (assign, "$qst_scout_waypoints_wp_3", -1),
               (assign, ":continue", 0),
               (try_for_range, ":unused", 0, ":end_cond"),
                 (try_begin),
                   (lt, "$qst_scout_waypoints_wp_1", 0),
                   (call_script, "script_cf_get_random_enemy_center_within_range", ":faction_marshall_party", 50),
                   (assign, "$qst_scout_waypoints_wp_1", reg0),
                 (try_end),
                 (try_begin),
                   (lt, "$qst_scout_waypoints_wp_2", 0),
                   (call_script, "script_cf_get_random_enemy_center_within_range", ":faction_marshall_party", 50),
                   (neq, "$qst_scout_waypoints_wp_1", reg0),
                   (assign, "$qst_scout_waypoints_wp_2", reg0),
                 (try_end),
                 (try_begin),
                   (lt, "$qst_scout_waypoints_wp_3", 0),
                   (call_script, "script_cf_get_random_enemy_center_within_range", ":faction_marshall_party", 50),
                   (neq, "$qst_scout_waypoints_wp_1", reg0),
                   (neq, "$qst_scout_waypoints_wp_2", reg0),
                   (assign, "$qst_scout_waypoints_wp_3", reg0),
                 (try_end),
                 (neq, "$qst_scout_waypoints_wp_1", "$qst_scout_waypoints_wp_2"),
                 (neq, "$qst_scout_waypoints_wp_1", "$qst_scout_waypoints_wp_2"),
                 (neq, "$qst_scout_waypoints_wp_2", "$qst_scout_waypoints_wp_3"),
                 (ge, "$qst_scout_waypoints_wp_1", 0),
                 (ge, "$qst_scout_waypoints_wp_2", 0),
                 (ge, "$qst_scout_waypoints_wp_3", 0),
                 (assign, ":end_cond", 0),
                 (assign, ":continue", 1),
               (try_end),
               (eq, ":continue", 1),
               (assign, "$qst_scout_waypoints_wp_1_visited", 0),
               (assign, "$qst_scout_waypoints_wp_2_visited", 0),
               (assign, "$qst_scout_waypoints_wp_3_visited", 0),
               (assign, ":result", "qst_scout_waypoints"),
               (quest_set_slot, ":result", slot_quest_expiration_days, 7),
               (quest_set_slot, ":result", slot_quest_dont_give_again_period, 25),
             (try_end),
           (try_end),
         (try_end),

         (try_begin),
           (neq, ":result", -1),
           (quest_set_slot, ":result", slot_quest_current_state, 0),
           (quest_set_slot, ":result", slot_quest_giver_troop, ":faction_marshall"),
           (try_begin),
             (eq, ":result", "qst_join_siege_with_army"),
             (jump_to_menu, "mnu_kingdom_army_quest_join_siege_order"),
           (else_try),
             (assign, "$g_random_army_quest", ":result"),
             (quest_set_slot, "$g_random_army_quest", slot_quest_giver_troop, ":faction_marshall"),
             (jump_to_menu, "mnu_kingdom_army_quest_messenger"),
           (try_end),
         (try_end),
       (try_end),
     (else_try),
       (val_add, "$g_player_follow_army_warnings", 1),
       (try_begin),
         (lt, "$g_player_follow_army_warnings", 15),
         (try_begin),
           (store_mod, ":follow_mod", "$g_player_follow_army_warnings", 3),
           (eq, ":follow_mod", 0),
           (str_store_troop_name_link, s1, ":faction_marshall"),
           (try_begin),
             (lt, "$g_player_follow_army_warnings", 8),
#             (display_message, "str_marshal_warning"),
           (else_try),
             (display_message, "str_marshal_warning"),
           (try_end),
         (try_end),
       (else_try),
         (jump_to_menu, "mnu_kingdom_army_follow_failed"),
       (try_end),
     (try_end),
    ]),

# Move cattle herd
  (0.5, [(check_quest_active,"qst_move_cattle_herd"),
         (neg|check_quest_concluded,"qst_move_cattle_herd"),
         (quest_get_slot, ":target_party", "qst_move_cattle_herd", slot_quest_target_party),
         (quest_get_slot, ":target_center", "qst_move_cattle_herd", slot_quest_target_center),
         (store_distance_to_party_from_party, ":dist",":target_party", ":target_center"),
         (lt, ":dist", 3),
         (remove_party, ":target_party"),
         (call_script, "script_succeed_quest", "qst_move_cattle_herd"),
    ]),

  # (2, [
       # (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
		 # (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
		 # (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
         # (ge, ":party_no", 1),
		 # (party_is_active, ":party_no"),
         # (party_slot_eq, ":party_no", slot_party_following_player, 1),
         # (store_current_hours, ":cur_time"),
         # (neg|party_slot_ge, ":party_no", slot_party_follow_player_until_time, ":cur_time"),
         # (party_set_slot, ":party_no", slot_party_commander_party, -1),
         # (party_set_slot, ":party_no", slot_party_following_player, 0),
         # (assign,  ":dont_follow_period", 200),
         # (store_add, ":dont_follow_time", ":cur_time", ":dont_follow_period"),
         # (party_set_slot, ":party_no", slot_party_dont_follow_player_until_time,  ":dont_follow_time"),
       # (try_end),
    # ]),

# Deliver cattle and deliver cattle to army
  (0.5,
   [
     (try_begin),
       (check_quest_active,"qst_deliver_cattle"),
       (neg|check_quest_succeeded, "qst_deliver_cattle"),
       (quest_get_slot, ":target_center", "qst_deliver_cattle", slot_quest_target_center),
       (quest_get_slot, ":target_amount", "qst_deliver_cattle", slot_quest_target_amount),
       (quest_get_slot, ":cur_amount", "qst_deliver_cattle", slot_quest_current_state),
       (store_sub, ":left_amount", ":target_amount", ":cur_amount"),
       (call_script, "script_remove_cattles_if_herd_is_close_to_party", ":target_center", ":left_amount"),
       (val_add, ":cur_amount", reg0),
       (quest_set_slot, "qst_deliver_cattle", slot_quest_current_state, ":cur_amount"),
       (le, ":target_amount", ":cur_amount"),
       (call_script, "script_succeed_quest", "qst_deliver_cattle"),
     (try_end),
     (try_begin),
       (check_quest_active, "qst_deliver_cattle_to_army"),
       (neg|check_quest_succeeded, "qst_deliver_cattle_to_army"),
       (quest_get_slot, ":giver_troop", "qst_deliver_cattle_to_army", slot_quest_giver_troop),
       (troop_get_slot, ":target_party", ":giver_troop", slot_troop_leaded_party),
       (try_begin),
         (gt, ":target_party", 0),
         (quest_get_slot, ":target_amount", "qst_deliver_cattle_to_army", slot_quest_target_amount),
         (quest_get_slot, ":cur_amount", "qst_deliver_cattle_to_army", slot_quest_current_state),
         (store_sub, ":left_amount", ":target_amount", ":cur_amount"),
         (call_script, "script_remove_cattles_if_herd_is_close_to_party", ":target_party", ":left_amount"),
         (val_add, ":cur_amount", reg0),
         (quest_set_slot, "qst_deliver_cattle_to_army", slot_quest_current_state, ":cur_amount"),
         (try_begin),
           (le, ":target_amount", ":cur_amount"),
           (call_script, "script_succeed_quest", "qst_deliver_cattle_to_army"),
         (try_end),
       (else_try),
         (call_script, "script_abort_quest", "qst_deliver_cattle_to_army", 0),
       (try_end),
     (try_end),
     ]),

# Train peasants against bandits
  (1,
   [
     (neg|map_free),
     (check_quest_active, "qst_train_peasants_against_bandits"),
     (neg|check_quest_concluded, "qst_train_peasants_against_bandits"),
     (eq, "$qst_train_peasants_against_bandits_currently_training", 1),
     (val_add, "$qst_train_peasants_against_bandits_num_hours_trained", 1),
     (call_script, "script_get_max_skill_of_player_party", "skl_trainer"),
     (assign, ":trainer_skill", reg0),
     (store_sub, ":needed_hours", 20, ":trainer_skill"),
     (val_mul, ":needed_hours", 3),
     (val_div, ":needed_hours", 5),
     (ge, "$qst_train_peasants_against_bandits_num_hours_trained", ":needed_hours"),
     (assign, "$qst_train_peasants_against_bandits_num_hours_trained", 0),
     (rest_for_hours, 0, 0, 0), #stop resting
     (jump_to_menu, "mnu_train_peasants_against_bandits_ready"),
     ]),

# Scout waypoints
  (1,
   [
     (check_quest_active,"qst_scout_waypoints"),
     (neg|check_quest_succeeded, "qst_scout_waypoints"),
     (try_begin),
       (eq, "$qst_scout_waypoints_wp_1_visited", 0),
       (store_distance_to_party_from_party, ":distance", "$qst_scout_waypoints_wp_1", "p_main_party"),
       (le, ":distance", 3),
       (assign, "$qst_scout_waypoints_wp_1_visited", 1),
       (str_store_party_name_link, s1, "$qst_scout_waypoints_wp_1"),
       (display_message, "@{s1} is scouted."),
     (try_end),
     (try_begin),
       (eq, "$qst_scout_waypoints_wp_2_visited", 0),
       (store_distance_to_party_from_party, ":distance", "$qst_scout_waypoints_wp_2", "p_main_party"),
       (le, ":distance", 3),
       (assign, "$qst_scout_waypoints_wp_2_visited", 1),
       (str_store_party_name_link, s1, "$qst_scout_waypoints_wp_2"),
       (display_message, "@{s1} is scouted."),
     (try_end),
     (try_begin),
       (eq, "$qst_scout_waypoints_wp_3_visited", 0),
       (store_distance_to_party_from_party, ":distance", "$qst_scout_waypoints_wp_3", "p_main_party"),
       (le, ":distance", 3),
       (assign, "$qst_scout_waypoints_wp_3_visited", 1),
       (str_store_party_name_link, s1, "$qst_scout_waypoints_wp_3"),
       (display_message, "@{s1} is scouted."),
     (try_end),
     (eq, "$qst_scout_waypoints_wp_1_visited", 1),
     (eq, "$qst_scout_waypoints_wp_2_visited", 1),
     (eq, "$qst_scout_waypoints_wp_3_visited", 1),
     (call_script, "script_succeed_quest", "qst_scout_waypoints"),
     ]),

# Kill local merchant

  (3, [(neg|map_free),
       (check_quest_active, "qst_kill_local_merchant"),
       (quest_slot_eq, "qst_kill_local_merchant", slot_quest_current_state, 0),
       (quest_set_slot, "qst_kill_local_merchant", slot_quest_current_state, 1),
       (rest_for_hours, 0, 0, 0), #stop resting
       (assign, "$auto_enter_town", "$qst_kill_local_merchant_center"),
       (assign, "$quest_auto_menu", "mnu_kill_local_merchant_begin"),
       ]),

# Collect taxes
  (1, [(neg|map_free),
       (check_quest_active, "qst_collect_taxes"),
       (eq, "$g_player_is_captive", 0),
       (eq, "$qst_collect_taxes_currently_collecting", 1),
       #SB : TODO add siege/raid interruption
       (quest_get_slot, ":quest_current_state", "qst_collect_taxes", slot_quest_current_state),
       (this_or_next|eq, ":quest_current_state", 1),
       (this_or_next|eq, ":quest_current_state", 2),
       (eq, ":quest_current_state", 3),
       (quest_get_slot, ":left_hours", "qst_collect_taxes", slot_quest_target_amount),
       (val_sub, ":left_hours", 1),
       (quest_set_slot, "qst_collect_taxes", slot_quest_target_amount, ":left_hours"),
       (call_script, "script_get_max_skill_of_player_party", "skl_trade"),

       (try_begin),
         (lt, ":left_hours", 0),
         (assign, ":quest_current_state", 4),
         (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 4),
         (rest_for_hours, 0, 0, 0), #stop resting
         (jump_to_menu, "mnu_collect_taxes_complete"),
       (else_try),
         #Continue collecting taxes
         (assign, ":max_collected_tax", "$qst_collect_taxes_hourly_income"),
         (party_get_slot, ":prosperity", "$g_encountered_party", slot_town_prosperity),
         (store_add, ":multiplier", 30, ":prosperity"),
         (val_mul, ":max_collected_tax", ":multiplier"),
         (val_div, ":max_collected_tax", 80),#Prosperity of 50 gives the default values

         (try_begin),
           (eq, "$qst_collect_taxes_halve_taxes", 1),
           (val_div, ":max_collected_tax", 2),
         (try_end),
         (val_max, ":max_collected_tax", 2),
         (store_random_in_range, ":collected_tax", 1, ":max_collected_tax"),
         (quest_get_slot, ":cur_collected", "qst_collect_taxes", slot_quest_gold_reward),
         (val_add, ":cur_collected", ":collected_tax"),
         (quest_set_slot, "qst_collect_taxes", slot_quest_gold_reward, ":cur_collected"),
         (call_script, "script_troop_add_gold", "trp_player", ":collected_tax"),
       (try_end),
       (try_begin),
         (eq, ":quest_current_state", 1),
         (val_sub, "$qst_collect_taxes_menu_counter", 1),
         (le, "$qst_collect_taxes_menu_counter", 0),
         (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 2),
         (jump_to_menu, "mnu_collect_taxes_revolt_warning"),
       (else_try), #Chance of revolt against player
         (eq, ":quest_current_state", 2),
         (val_sub, "$qst_collect_taxes_unrest_counter", 1),
         (le, "$qst_collect_taxes_unrest_counter", 0),
         (eq, "$qst_collect_taxes_halve_taxes", 0),
         (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 3),

         (store_div, ":unrest_chance", 10000, "$qst_collect_taxes_total_hours"),
         (val_add, ":unrest_chance",30),

         (store_random_in_range, ":unrest_roll", 0, 1000),
         (try_begin),
           (lt, ":unrest_roll", ":unrest_chance"),
           (jump_to_menu, "mnu_collect_taxes_revolt"),
         (try_end),
       (try_end),
       ]),

#persuade_lords_to_make_peace begin #SB: range check instead of gt 0
  (72, [(is_between, "$g_force_peace_faction_1", kingdoms_begin, kingdoms_end),
        (is_between, "$g_force_peace_faction_2", kingdoms_begin, kingdoms_end),
        (try_begin),
          (store_relation, ":relation", "$g_force_peace_faction_1", "$g_force_peace_faction_2"),
          (lt, ":relation", 0),
          (call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_force_peace_faction_1", "$g_force_peace_faction_2", 1),
        (try_end),
        (assign, "$g_force_peace_faction_1", 0),
        (assign, "$g_force_peace_faction_2", 0),
       ]),

#NPC changes begin
#Resolve one issue each hour
(1,
   [
    (str_store_string, s51, "str_no_trigger_noted"),

    # Rejoining party
    (try_begin),
      (gt, "$npc_to_rejoin_party", 0),
      (eq, "$g_infinite_camping", 0),
	(neq, "$freelancer_state", 1),
      (try_begin), #SB : allow hired blade to pass
        (this_or_next|eq, "$npc_to_rejoin_party", "trp_hired_blade"),
        (this_or_next|is_between, "$npc_to_rejoin_party", town_walkers_begin, town_walkers_end),
        (neg|main_party_has_troop, "$npc_to_rejoin_party"),
        (neq, "$g_player_is_captive", 1),
        (str_store_string, s51, "str_triggered_by_npc_to_rejoin_party"),
        (assign, "$npc_map_talk_context", slot_troop_days_on_mission),
        (start_map_conversation, "$npc_to_rejoin_party", -1),
      (else_try),
        (is_between, "$npc_to_rejoin_party", companions_begin, companions_end),
        (troop_set_slot, "$npc_to_rejoin_party", slot_troop_current_mission, npc_mission_rejoin_when_possible),
        (assign, "$npc_to_rejoin_party", 0),
      (try_end),
      # Here do NPC that is quitting
    (else_try),
      (gt, "$npc_is_quitting", 0),
      (eq, "$g_infinite_camping", 0),
	(neq, "$freelancer_state", 1),
      (try_begin),
        (main_party_has_troop, "$npc_is_quitting"),
        (neq, "$g_player_is_captive", 1),
        ##diplomacy start+ disable spouse quitting to avoid problems
        (neg|troop_slot_eq, "trp_player", slot_troop_spouse, "$npc_is_quitting"),
        (neg|troop_slot_eq, "$npc_is_quitting", slot_troop_spouse, "trp_player"),
        ##diplomacy end+
        (str_store_string, s51, "str_triggered_by_npc_is_quitting"),
        (start_map_conversation, "$npc_is_quitting", -1),
      (else_try),
        (assign, "$npc_is_quitting", 0),
      (try_end),
    #NPC with grievance
    (else_try), #### Grievance
      (gt, "$npc_with_grievance", 0),
      (eq, "$g_infinite_camping", 0),
      (eq, "$disable_npc_complaints", 0),
	(neq, "$freelancer_state", 1),
      (try_begin),
        (main_party_has_troop, "$npc_with_grievance"),
        (neq, "$g_player_is_captive", 1),
        (str_store_string, s51, "str_triggered_by_npc_has_grievance"),
        (assign, "$npc_map_talk_context", slot_troop_morality_state),
        (start_map_conversation, "$npc_with_grievance", -1),
      (else_try),
        (assign, "$npc_with_grievance", 0),
      (try_end),
    (else_try),
      (gt, "$npc_with_personality_clash", 0),
      (eq, "$g_infinite_camping", 0),
      (eq, "$disable_npc_complaints", 0),
	(neq, "$freelancer_state", 1),
      (troop_get_slot, ":object", "$npc_with_personality_clash", slot_troop_personalityclash_object),
      (try_begin),
	(gt, ":object", 0),
        (main_party_has_troop, "$npc_with_personality_clash"),
        (main_party_has_troop, ":object"),
        (neq, "$g_player_is_captive", 1),

        (assign, "$npc_map_talk_context", slot_troop_personalityclash_state),
        (str_store_string, s51, "str_triggered_by_npc_has_personality_clash"),
        (start_map_conversation, "$npc_with_personality_clash", -1),
      (else_try),
        (assign, "$npc_with_personality_clash", 0),
      (try_end),
    (else_try), #### Political issue
      (gt, "$npc_with_political_grievance", 0),
      (eq, "$g_infinite_camping", 0),
      (eq, "$disable_npc_complaints", 0),
	(neq, "$freelancer_state", 1),
      (try_begin),
        (main_party_has_troop, "$npc_with_political_grievance"),
        (neq, "$g_player_is_captive", 1),

        (str_store_string, s51, "str_triggered_by_npc_has_political_grievance"),
        (assign, "$npc_map_talk_context", slot_troop_kingsupport_objection_state),
        (start_map_conversation, "$npc_with_political_grievance", -1),
      (else_try),
        (assign, "$npc_with_political_grievance", 0),
      (try_end),
    (else_try),
      (eq, "$disable_sisterly_advice", 0),
      (eq, "$g_infinite_camping", 0),
      (gt, "$npc_with_sisterly_advice", 0),
	(neq, "$freelancer_state", 1),
      (try_begin),
        (main_party_has_troop, "$npc_with_sisterly_advice"),
        (neq, "$g_player_is_captive", 1),

        ##diplomacy start+
        (troop_slot_ge, "$npc_with_sisterly_advice", slot_troop_woman_to_woman_string, 1),
        ##diplomacy end+
        (assign, "$npc_map_talk_context", slot_troop_woman_to_woman_string), #was npc_with_sisterly advice
        (start_map_conversation, "$npc_with_sisterly_advice", -1),
      (else_try),
        (assign, "$npc_with_sisterly_advice", 0),
      (try_end),
    (else_try), #check for regional background
      (eq, "$disable_local_histories", 0),
      (eq, "$g_infinite_camping", 0),
	(neq, "$freelancer_state", 1),
      (try_for_range, ":npc", companions_begin, companions_end),
        (main_party_has_troop, ":npc"),
        (troop_slot_eq, ":npc", slot_troop_home_speech_delivered, 0),
        (troop_get_slot, ":home", ":npc", slot_troop_home),
        (gt, ":home", 0),
        (store_distance_to_party_from_party, ":distance", ":home", "p_main_party"),
        (lt, ":distance", 7),
        (assign, "$npc_map_talk_context", slot_troop_home),
        (str_store_string, s51, "str_triggered_by_local_histories"),
        (start_map_conversation, ":npc", -1),
      (try_end),
    (try_end),

    #add pretender to party if not active
    (try_begin),
      (check_quest_active, "qst_rebel_against_kingdom"),
      (is_between, "$supported_pretender", pretenders_begin, pretenders_end),
      (neg|main_party_has_troop, "$supported_pretender"),
      (neg|troop_slot_eq, "$supported_pretender", slot_troop_occupation, slto_kingdom_hero),
      #(party_add_members, "p_main_party", "$supported_pretender", 1),
      (party_force_add_members, "p_main_party", "$supported_pretender", 1), #madsci
    (try_end),

    #make player marshal of rebel faction
    (try_begin),
      (check_quest_active, "qst_rebel_against_kingdom"),
      (is_between, "$supported_pretender", pretenders_begin, pretenders_end),
      (main_party_has_troop, "$supported_pretender"),
      (neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_marshall, "trp_player"),
      (call_script, "script_appoint_faction_marshall", "fac_player_supporters_faction", "trp_player"),
    (try_end),
]),
#NPC changes end

(24,
   ##diplomacy start+ Add support for promoted kingdom ladies
   ##OLD:
   #[(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
   ##NEW:
   [(try_for_range, ":troop_no", heroes_begin, heroes_end),
      (this_or_next|is_between, ":troop_no", active_npcs_begin, active_npcs_end),
      (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
   ##diplomacy end+
      (troop_slot_ge, ":troop_no", slot_troop_change_to_faction, 1),
      (store_troop_faction, ":faction_no", ":troop_no"),
      (troop_get_slot, ":new_faction_no", ":troop_no", slot_troop_change_to_faction),
      (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
      (assign, ":continue", 0),
      (try_begin),
        (this_or_next|le, ":party_no", 0),
	(neg|party_is_active, ":party_no"),
        #(troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
        (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
        (assign, ":continue", 1),
      (else_try),
        (gt, ":party_no", 0),

        #checking if the party is outside the centers
        (party_get_attached_to, ":cur_center_no", ":party_no"),
        (try_begin),
          (lt, ":cur_center_no", 0),
          (party_get_cur_town, ":cur_center_no", ":party_no"),
        (try_end),
        (this_or_next|neg|is_between, ":cur_center_no", centers_begin, centers_end),
        (party_slot_eq, ":cur_center_no", slot_town_lord, ":troop_no"),

        #checking if the party is away from his original faction parties
        ##diplomacy start+
        ##Add support for promoted kingdom lades.
        ##OLD:
        #(assign, ":end_cond", active_npcs_end),
        ##NEW:
        (assign, ":end_cond", heroes_end),
        ##diplomacy end+
        (try_for_range, ":enemy_troop_no", heroes_begin, ":end_cond"),
          #SB : self-check prevention
          (neq, ":enemy_troop_no", ":troop_no"),
          (troop_slot_eq, ":enemy_troop_no", slot_troop_occupation, slto_kingdom_hero),
          (troop_get_slot, ":enemy_party_no", ":enemy_troop_no", slot_troop_leaded_party),
	  (gt, ":enemy_party_no", 0),
          (party_is_active, ":enemy_party_no"),
          (store_faction_of_party, ":enemy_faction_no", ":enemy_party_no"),
          (eq, ":enemy_faction_no", ":faction_no"),
          (store_distance_to_party_from_party, ":dist", ":party_no", ":enemy_party_no"),
          (lt, ":dist", 4),
          (assign, ":end_cond", 0),
        (try_end),
        (neq, ":end_cond", 0),
        (assign, ":continue", 1),
      (try_end),
      (eq, ":continue", 1),

      (call_script, "script_change_troop_faction", ":troop_no", ":new_faction_no"),
      (troop_set_slot, ":troop_no", slot_troop_change_to_faction, 0),
      (try_begin),
        (is_between, ":new_faction_no", kingdoms_begin, kingdoms_end),
        (str_store_troop_name_link, s1, ":troop_no"),
        (str_store_faction_name_link, s2, ":faction_no"),
        (str_store_faction_name_link, s3, ":new_faction_no"),
        (faction_get_color, ":color", ":new_faction_no"),
        (display_log_message, "@{s1} has switched from {s2} to {s3}.", ":color"), #SB : colorize
        (try_begin),
          (eq, ":faction_no", "$players_kingdom"),
          (call_script, "script_add_notification_menu", "mnu_notification_troop_left_players_faction", ":troop_no", ":new_faction_no"),
        (else_try),
          (eq, ":new_faction_no", "$players_kingdom"),
          (call_script, "script_add_notification_menu", "mnu_notification_troop_joined_players_faction", ":troop_no", ":faction_no"),
        (try_end),
      (try_end),
    (try_end),
    ]),

(1,
   [
     (store_current_day, ":cur_day"),
     (gt, ":cur_day", "$g_last_report_control_day"),
     (store_time_of_day, ":cur_hour"),
     (ge, ":cur_hour", 18),

     (store_random_in_range, ":rand_no", 0, 4),
     (this_or_next|ge, ":cur_hour", 22),
     (eq, ":rand_no", 0),

     (assign, "$g_last_report_control_day", ":cur_day"),

     (store_troop_gold, ":gold", "trp_player"),

     (try_begin),
       (lt, ":gold", 0),
       (store_sub, ":gold_difference", 0, ":gold"),
       (troop_add_gold, "trp_player", ":gold_difference"),
     (try_end),

	(party_get_morale, ":main_party_morale", "p_main_party"),
	(party_clear, "p_temp_party"),

     (try_begin),
       (str_store_string, s1, "str_party_morale_is_low"),
       (str_clear, s2),

       (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
       (assign, ":num_deserters_total", 0),
       (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
         (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i_stack"),
         (neg|troop_is_hero, ":stack_troop"),
         (party_stack_get_size, ":stack_size", "p_main_party", ":i_stack"),

         (store_troop_faction, ":faction_no", ":stack_troop"),

         (assign, ":troop_morale", ":main_party_morale"),
         (try_begin),
           (is_between, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),

           (faction_get_slot, ":troop_morale_addition", ":faction_no",  slot_faction_morale_of_player_troops),
           (val_div, ":troop_morale_addition", 100),
           (val_add, ":troop_morale", ":troop_morale_addition"),
         (try_end),

         (lt, ":troop_morale", 32),

           (store_random_in_range, ":num_deserters_from_that_troop", 0, ":stack_size"),
	   (val_div, ":num_deserters_from_that_troop", 4),

         (try_begin),
           (ge, ":num_deserters_from_that_troop", 1),
		(party_remove_members, "p_main_party", ":stack_troop", ":num_deserters_from_that_troop"),
		(party_add_members, "p_temp_party", ":stack_troop", ":num_deserters_from_that_troop"),
           (str_store_troop_name, s2, ":stack_troop"),
           (assign, reg0, ":num_deserters_from_that_troop"),

           (try_begin),
             (ge, ":num_deserters_total", 1),
             (str_store_string, s1, "str_s1_reg0_s2"),
           (else_try),
             (str_store_string, s3, s1),
             (str_store_string, s1, "str_s3_reg0_s2"),
           (try_end),
           (val_add, ":num_deserters_total", ":num_deserters_from_that_troop"),
         (try_end),
       (try_end),

       (try_begin),
         (ge, ":num_deserters_total", 1),
		(try_begin),
		(neq, "$freelancer_state", 1),
		(eq, "$g_player_is_captive", 0),
		#(neg|party_slot_eq, "p_main_party", slot_party_on_water, 1),
		(set_spawn_radius, 0),
		(spawn_around_party, "p_main_party", "pt_deserters"),
		(assign, ":new_party", reg0),
		(call_script, "script_party_add_party", ":new_party", "p_temp_party"),
		(party_ignore_player, ":new_party", 1),
		(call_script, "script_get_closest_center", ":new_party"),
		(assign, ":closest_center", reg0),
		(party_set_ai_behavior, ":new_party", ai_bhvr_patrol_party),
		(party_set_ai_object, ":new_party", ":closest_center"),
		(try_end),

         	(try_begin),
           	(ge, ":num_deserters_total", 2),
           	(str_store_string, s2, "str_have_deserted_the_party"),
         	(else_try),
           	(str_store_string, s2, "str_has_deserted_the_party"),
         	(try_end),

		(try_begin),
        	(eq, "$g_infinite_camping", 0),
        	(str_store_string, s1, "str_s1_s2"),
	        (tutorial_box, s1, "str_weekly_report"),
		(try_end),
       (try_end),
     (try_end),
 ]),
 # reserved for future use. For backward compatibility, we need to use these triggers instead of creating new ones.


  (1,
   [
     (try_begin),
       (eq, "$g_player_is_captive", 1),
       (neg|party_is_active, "$capturer_party"),
       (rest_for_hours, 0, 0, 0),
     (try_end),

     ##diplomacy begin
      #seems to be a native bug
     (is_between, "$next_center_will_be_fired", villages_begin, villages_end),
     ##diplomacy end
     (assign, ":village_no", "$next_center_will_be_fired"),
     (party_get_slot, ":is_there_already_fire", ":village_no", slot_village_smoke_added),
     (eq, ":is_there_already_fire", 0),


     (try_begin),
       (party_get_slot, ":bound_center", ":village_no", slot_village_bound_center),
       (party_get_slot, ":last_nearby_fire_time", ":bound_center", slot_town_last_nearby_fire_time),
       (store_current_hours, ":cur_hours"),

	   (try_begin),
		(eq, "$cheat_mode", 1),
		(is_between, ":village_no", centers_begin, centers_end),
		(is_between, ":bound_center", centers_begin, centers_end),
		(str_store_party_name, s4, ":village_no"),
		(str_store_party_name, s5, ":bound_center"),
		(store_current_hours, reg3),
        (party_get_slot, reg4, ":bound_center", slot_town_last_nearby_fire_time),
		#(display_message, "@{!}DEBUG - Checking fire at {s4} for {s5} - current time {reg3}, last nearby fire {reg4}"),
	   (try_end),


       (eq, ":cur_hours", ":last_nearby_fire_time"),
       (party_add_particle_system, ":village_no", "psys_map_village_fire"),
       (party_add_particle_system, ":village_no", "psys_map_village_fire_smoke"),
     (else_try),
       (store_add, ":last_nearby_fire_finish_time", ":last_nearby_fire_time", fire_duration),
       (eq, ":last_nearby_fire_finish_time", ":cur_hours"),
       (party_clear_particle_systems, ":village_no"),
     (try_end),


   ]),

  (24,
   [
    (val_sub, "$g_dont_give_fief_to_player_days", 1),
    (val_max, "$g_dont_give_fief_to_player_days", -1),
    (val_sub, "$g_dont_give_marshalship_to_player_days", 1),
    (val_max, "$g_dont_give_marshalship_to_player_days", -1),

    # (call_script, "script_dplmc_version_checker"), #SB : moved to script call

    #The following scripts are to end quests which should have cancelled, but did not because of a bug
    (try_begin),
      (check_quest_active, "qst_formal_marriage_proposal"),
      (check_quest_failed, "qst_formal_marriage_proposal"),
      (call_script, "script_end_quest", "qst_formal_marriage_proposal"),
    (try_end),

    (try_begin),
      (check_quest_active, "qst_lend_companion"),
      (quest_get_slot, ":giver_troop", "qst_lend_companion", slot_quest_giver_troop),
      (store_faction_of_troop, ":giver_troop_faction", ":giver_troop"),
      (store_relation, ":faction_relation", ":giver_troop_faction", "$players_kingdom"),
      (this_or_next|lt, ":faction_relation", 0),
      (neg|is_between, ":giver_troop_faction", kingdoms_begin, kingdoms_end),
      (call_script, "script_abort_quest", "qst_lend_companion", 0),
    (try_end),

    (try_begin),
      (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
      (neq, "$players_kingdom", "fac_player_supporters_faction"),
      (faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"),
      (val_add, "$g_player_days_as_marshal", 1),
    (else_try),
      (assign, "$g_player_days_as_marshal", 0),
    (try_end),

    (try_for_range, ":town", towns_begin, towns_end),
      (party_get_slot, ":days_to_completion", ":town", slot_center_player_enterprise_days_until_complete),
      (ge, ":days_to_completion", 1),
      (val_sub, ":days_to_completion", 1),
      (party_set_slot, ":town", slot_center_player_enterprise_days_until_complete, ":days_to_completion"),
    (try_end),
    ]),
(24,
   [
      # Setting food bonuses in every 6 hours again and again because of a bug (we could not find its reason) which decreases especially slot_item_food_bonus slots of items to 0.
      #Staples
      (item_set_slot, "itm_bread", slot_item_food_bonus, 8), #brought up from 4
      (item_set_slot, "itm_grain", slot_item_food_bonus, 2), #new - can be boiled as porridge

      #Fat sources - preserved
      (item_set_slot, "itm_smoked_fish", slot_item_food_bonus, 4),
      (item_set_slot, "itm_dried_meat", slot_item_food_bonus, 5),
      (item_set_slot, "itm_cheese", slot_item_food_bonus, 5),
      (item_set_slot, "itm_sausages", slot_item_food_bonus, 5),
      (item_set_slot, "itm_butter", slot_item_food_bonus, 4), #brought down from 8

      #Fat sources - perishable
      (item_set_slot, "itm_chicken", slot_item_food_bonus, 8), #brought up from 7
      (item_set_slot, "itm_cattle_meat", slot_item_food_bonus, 7), #brought down from 7
      (item_set_slot, "itm_pork", slot_item_food_bonus, 6), #brought down from 6

      #Produce
      (item_set_slot, "itm_raw_olives", slot_item_food_bonus, 1),
      (item_set_slot, "itm_cabbages", slot_item_food_bonus, 2),
      (item_set_slot, "itm_raw_grapes", slot_item_food_bonus, 3),
      (item_set_slot, "itm_apples", slot_item_food_bonus, 4), #brought down from 5

      #Sweet items
      (item_set_slot, "itm_raw_date_fruit", slot_item_food_bonus, 4), #brought down from 8
      (item_set_slot, "itm_honey", slot_item_food_bonus, 6), #brought down from 12

      (item_set_slot, "itm_wine", slot_item_food_bonus, 5),
      (item_set_slot, "itm_ale", slot_item_food_bonus, 4),

    #Battle-Standards
      (item_set_slot, "itm_flag_pole_1", slot_item_food_bonus, 15),

   ]),

  ##diplomacy begin
  #Troop AI Spouse: Spouse thinking
  (6,
   [
    (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
    (ge, ":player_spouse", active_npcs_begin),#<-- skip the rest of the check when there is no spouse
    (try_for_parties, ":spouse_party"),
      (gt, ":spouse_party", last_static_party), #madsci
      (party_slot_eq, ":spouse_party", slot_party_type, dplmc_spt_spouse),

      (party_get_slot, ":spouse_target", ":spouse_party", slot_party_orders_object),
      (party_get_slot, ":home_center", ":spouse_party", slot_party_home_center),
      (store_distance_to_party_from_party, ":distance", ":spouse_party", ":spouse_target"),

      #Moving spouse to home village
      (try_begin),
        (le, ":distance", 1),
        (try_begin),
          (this_or_next|eq, ":spouse_target", "$g_player_court"),
          (eq, ":spouse_target", ":home_center"),
          (remove_party, ":spouse_party"),
          (troop_set_slot, ":player_spouse", slot_troop_cur_center, ":spouse_target"),
        (else_try),
          (try_begin),
            (is_between, ":spouse_target", villages_begin, villages_end),
            (party_get_slot,":cur_merchant",":spouse_target", slot_town_elder),
          (else_try),
            (party_get_slot,":cur_merchant",":spouse_target", slot_town_merchant),
          (try_end),
          (troop_get_slot, ":amount", ":player_spouse", dplmc_slot_troop_mission_diplomacy),
          (troop_remove_items, ":cur_merchant", "itm_bread", ":amount"),
          (party_set_ai_behavior, ":spouse_party", ai_bhvr_travel_to_party),
          (try_begin),
            (gt, "$g_player_court", 0),
            (party_set_slot, ":spouse_party", slot_party_ai_object, "$g_player_court"),
            (party_set_ai_object, ":spouse_party", "$g_player_court"),
          (else_try),
            (party_set_slot, ":spouse_party", slot_party_ai_object, ":home_center"),
            (party_set_ai_object, ":spouse_party", ":home_center"),
          (try_end),

          (troop_add_items, "trp_household_possessions", "itm_bread", ":amount"),
        (try_end),
      (try_end),
    (try_end),
    ]),

#Recruiter kit begin
## This trigger keeps the recruiters moving by assigning them targets.
 (1, #SB : half the number of calls
   [
   (try_for_parties, ":party_no"),
      (gt, ":party_no", last_static_party), #madsci
      (party_is_active, ":party_no"),
      (party_slot_eq,":party_no", slot_party_type, dplmc_spt_recruiter),

      (party_get_slot, ":needed", ":party_no", dplmc_slot_party_recruiter_needed_recruits),
      (party_get_slot, ":party_origin", ":party_no", dplmc_slot_party_recruiter_origin),
      (party_get_num_companion_stacks, ":stacks", ":party_no"),
      (assign, ":destruction", 1),
      (assign, ":quit", 0),

      (try_for_range, ":stack_no", 0, ":stacks"),
         (party_stack_get_troop_id, ":troop_id", ":party_no", ":stack_no"),
         (eq, ":troop_id", "trp_dplmc_recruiter"),
         (assign, ":destruction", 0),
      (try_end),
      (try_begin),
         (party_get_battle_opponent, ":opponent", ":party_no"),
         (lt, ":opponent", 0),
         (eq, ":destruction", 1),
         # (party_get_slot, ":party_origin", ":party_no", dplmc_slot_party_recruiter_origin), #SB : moved top
         (str_store_party_name_link, s13, ":party_origin"),
         (assign, reg10, ":needed"),
         #SB : less verbose recruits
         (display_log_message, "@Your recruiter who was commissioned to hire {reg10} recruits for {s13} has been defeated!", message_defeated), #SB : message code
         (remove_party, ":party_no"),
         (assign, ":quit", 1),
      (try_end),

      #waihti
      (try_begin),
        (eq, ":quit", 0),
        # (party_get_slot, ":party_origin", ":party_no", dplmc_slot_party_recruiter_origin), #SB : moved top
        (store_faction_of_party, ":origin_faction", ":party_origin"),
        (neq, ":origin_faction", "$players_kingdom"),
        (str_store_party_name_link, s13, ":party_origin"),
        # (assign, reg10, ":needed"),
        #SB : less verbose message, alternatively actually redirect the recruiter
        (display_log_message, "@{s13} has been taken by the enemy and your commissioned recruiter has vanished without a trace!", message_defeated), #SB : message code
        (remove_party, ":party_no"),
        (assign, ":quit", 1),
      (try_end),
      #waihti

      (eq, ":quit", 0),

      (party_get_num_companions, ":amount", ":party_no"),
      (val_sub, ":amount", 1),   #the recruiter himself doesn't count.

    #daedalus begin
    (party_get_slot, ":recruit_faction", ":party_no", dplmc_slot_party_recruiter_needed_recruits_faction),
    (try_begin),
      #daedalus end
      (lt, ":amount", ":needed"),  #If the recruiter has less troops than player ordered, new village will be set as target.
      (try_begin),
         #(get_party_ai_current_behavior, ":ai_bhvr", ":party_no"),
         #(eq, ":ai_bhvr", ai_bhvr_hold),
         (get_party_ai_object, ":previous_target", ":party_no"),
         (get_party_ai_behavior, ":previous_behavior", ":party_no"),
         (try_begin),
            (neq, ":previous_behavior", ai_bhvr_hold),
            (neq, ":previous_target", -1),
            (party_set_slot, ":previous_target", dplmc_slot_village_reserved_by_recruiter, 0),
         (try_end),
         (assign, ":min_distance", 999999),
         (assign, ":closest_village", -1),
         (try_for_range, ":village", villages_begin, villages_end),
            (store_distance_to_party_from_party, ":distance", ":party_no", ":village"),
            (lt, ":distance", ":min_distance"),
            (try_begin),
               (store_faction_of_party, ":village_current_faction", ":village"),
               (assign, ":faction_relation", 100),
               (try_begin),
                  (neq, ":village_current_faction", "$players_kingdom"),    # faction relation will be checked only if the village doesn't belong to the player's current faction
                  (store_relation, ":faction_relation", "$players_kingdom", ":village_current_faction"),
               (try_end),
               (ge, ":faction_relation", 0),
               (party_get_slot, ":village_relation", ":village", slot_center_player_relation),
               (ge, ":village_relation", 0),
               (party_get_slot, ":volunteers_in_village", ":village", slot_center_volunteer_troop_amount),
               (gt, ":volunteers_in_village", 0),
            #daedalus begin
               (party_get_slot, ":village_faction", ":village", slot_center_original_faction),
               (assign,":stop",1),
               (try_begin), #SB : or
                  (this_or_next|eq,":recruit_faction",-1),
                  (eq, ":village_faction", ":recruit_faction"),
                  (assign,":stop",0),
               (try_end),
               (neq,":stop",1),
            #daedalus end
               # (neg|party_slot_eq, ":village", slot_village_state, svs_looted),
               # (neg|party_slot_eq, ":village", slot_village_state, svs_being_raided),
               # (neg|party_slot_ge, ":village", slot_village_infested_by_bandits, 1),
               (call_script, "script_cf_village_normal_cond", ":village"), #SB : script condition
               (neg|party_slot_eq, ":village", dplmc_slot_village_reserved_by_recruiter, 1),
               (assign, ":min_distance", ":distance"),
               (assign, ":closest_village", ":village"),
            (try_end),
         (try_end),
         (gt, ":closest_village", -1),
         (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
         (party_set_ai_object, ":party_no", ":closest_village"),
         (party_set_slot, ":party_no", slot_party_ai_object, ":closest_village"),
         (party_set_slot, ":closest_village", dplmc_slot_village_reserved_by_recruiter, 1),
      (try_end),
      (party_get_slot, ":target", ":party_no", slot_party_ai_object),
      (gt, ":target", -1),
      (store_distance_to_party_from_party, ":distance_from_target", ":party_no", ":target"),
      (try_begin),
         (store_faction_of_party, ":target_current_faction", ":target"),
         (assign, ":faction_relation", 100),
         (try_begin),
            (neq, ":target_current_faction", "$players_kingdom"),    # faction relation will be checked only if the target doesn't belong to the player's current faction
            (store_relation, ":faction_relation", "$players_kingdom", ":target_current_faction"),
         (try_end),
         (ge, ":faction_relation", 0),
         (party_get_slot, ":target_relation", ":target", slot_center_player_relation),
         (ge, ":target_relation", 0),
      #daedalus begin
         (party_get_slot, ":target_faction", ":target", slot_center_original_faction),
         (assign,":stop",1),
         (try_begin), #SB : or
            (this_or_next|eq,":recruit_faction",-1),
            # (assign,":stop",0),
         # (else_try),
            (eq, ":target_faction", ":recruit_faction"),
            (assign,":stop",0),
         (try_end),
         (neq,":stop",1),
      #daedalus end
         (call_script, "script_cf_village_normal_cond", ":target"), #SB : script condition
         (le, ":distance_from_target", 0),
         (party_get_slot, ":volunteers_in_target", ":target", slot_center_volunteer_troop_amount),
         (party_get_slot, ":target_volunteer_type", ":target", slot_center_volunteer_troop_type),
         (store_sub, ":still_needed", ":needed", ":amount"), #SB : store sub

(try_begin),
(le, ":target_volunteer_type", 0),
(assign, ":target_volunteer_type", "trp_manhunter"), #madsci generic troop if actual troop isnt assigned
(try_end),

         (try_begin), #SB : use store subs
            (gt, ":volunteers_in_target", ":still_needed"),
            (store_sub, ":santas_little_helper", ":volunteers_in_target", ":still_needed"),
            (store_sub, ":amount_to_recruit", ":volunteers_in_target", ":santas_little_helper"),
            (store_sub, ":new_target_volunteer_amount", ":volunteers_in_target", ":amount_to_recruit"),
            (party_set_slot, ":target", slot_center_volunteer_troop_amount, ":new_target_volunteer_amount"),
            (party_add_members, ":party_no", ":target_volunteer_type", ":amount_to_recruit"),
            (party_set_ai_behavior, ":party_no", ai_bhvr_hold),
            (party_set_slot, ":target", dplmc_slot_village_reserved_by_recruiter, 0),
         (else_try),
            (le, ":volunteers_in_target", ":still_needed"),
            (gt, ":volunteers_in_target", 0),
            (party_set_slot, ":target", slot_center_volunteer_troop_amount, -1),
            (party_add_members, ":party_no", ":target_volunteer_type", ":volunteers_in_target"),
            (party_set_ai_behavior, ":party_no", ai_bhvr_hold),
            (party_set_slot, ":target", dplmc_slot_village_reserved_by_recruiter, 0),
            (val_sub, ":still_needed", ":volunteers_in_target"),
            (call_script, "script_dplmc_set_recruiter_extra_text", ":party_no", ":still_needed"),
         (else_try),
            (le, ":volunteers_in_target", 0),
            (party_set_ai_behavior, ":party_no", ai_bhvr_hold),
            (party_set_slot, ":target", dplmc_slot_village_reserved_by_recruiter, 0),
         (else_try),
            (display_message, "@ERROR IN THE RECRUITER KIT SIMPLE TRIGGERS!",message_locked), #SB : color const
            (party_set_slot, ":target", dplmc_slot_village_reserved_by_recruiter, 0),
         (try_end),
      (try_end),
   # (try_end),
   # #SB : merged loops
   # (try_for_parties, ":party_no"),
      # (party_slot_eq,":party_no", slot_party_type, dplmc_spt_recruiter),
      # (party_get_num_companions, ":amount", ":party_no"),
      # (val_sub, ":amount", 1),   #the recruiter himself doesn't count
      # (party_get_slot, ":needed", ":party_no", dplmc_slot_party_recruiter_needed_recruits),
    (else_try),
      (eq, ":amount", ":needed"),
      # (party_get_slot, ":party_origin", ":party_no", dplmc_slot_party_recruiter_origin),  #SB : moved top
      (try_begin),
         (neg|party_slot_eq, ":party_no", slot_party_ai_object, ":party_origin"),
         (party_set_slot, ":party_no", slot_party_ai_object, ":party_origin"),
         (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
         (party_set_ai_object, ":party_no", ":party_origin"),
         # (party_set_extra_text, ":party_no", "@Returning"), #SB : extra text
         (call_script, "script_dplmc_set_recruiter_extra_text", ":party_no", -1),
      (try_end),
      (store_distance_to_party_from_party, ":distance_from_origin", ":party_no", ":party_origin"),
      (try_begin),
         (le, ":distance_from_origin", 0),
         (party_get_num_companion_stacks, ":stacks", ":party_no"),
         (try_for_range, ":stack_no", 1, ":stacks"),
            (party_stack_get_size, ":size", ":party_no", ":stack_no"),
            (party_stack_get_troop_id, ":troop_id", ":party_no", ":stack_no"),
            (party_add_members, ":party_origin", ":troop_id", ":size"),
         (try_end),
         (str_store_party_name_link, s13, ":party_origin"),
         (assign, reg10, ":amount"),
         (display_log_message, "@A recruiter has brought {reg10} recruits to {s13}.", message_positive), #SB : message code
         (remove_party, ":party_no"),
      (try_end),
    (try_end),
  (try_end), #SB : close loop
   ]),

 #process gift_carvans
 (1, #SB : half frequency
 [
  (eq, "$g_player_chancellor", "trp_dplmc_chancellor"),
  ##nested diplomacy start+
  #These gifts are far too efficient.  To be balanced with Native, they
  #should not (at the best case) exceed an efficiency of 1000 gold per point.
  (assign, ":save_reg0", reg0),
  (assign, ":save_reg1", reg1),
  (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),#store for use below
  ##nested diplomacy end+
  (try_for_parties, ":party_no"),
      (gt, ":party_no", last_static_party), #madsci
    (party_is_active, ":party_no"),
    (party_slot_eq,":party_no", slot_party_type, dplmc_spt_gift_caravan),
    (party_get_slot, ":target_party", ":party_no", slot_party_ai_object),
    (party_get_slot, ":target_troop", ":party_no", slot_party_orders_object),

    (try_begin),
      (party_is_active, ":target_party"),

      (store_distance_to_party_from_party, ":distance_to_target", ":party_no", ":target_party"),
      (str_store_party_name, s14, ":party_no"),
      (str_store_party_name, s15,":target_party"),

      (try_begin), #debug
        (eq, "$cheat_mode", 1),
        (assign, reg0, ":distance_to_target"),
        #(display_message, "@Distance between {s14} and {s15}: {reg0}"),
      (try_end),

      (try_begin),
        (le, ":distance_to_target", 1),

        (party_get_slot, ":gift", ":party_no", dplmc_slot_party_mission_diplomacy),
        (str_store_item_name, s12, ":gift"),

        (try_begin), #SB : string links
          (gt, ":target_troop", 0),
          (str_store_troop_name_link, s13, ":target_troop"),
        (else_try),
          (str_store_party_name_link, s13, ":target_party"),
        (end_try),
        (display_log_message, "@Your caravan has brought {s12} to {s13}.", message_positive), #SB : message_positive

        (assign, ":relation_boost", 0),
        (store_faction_of_party, ":target_faction", ":target_party"),

        (try_begin),
          (gt, ":target_troop", 0),
          (faction_slot_eq,":target_faction",slot_faction_leader,":target_troop"),
          (try_begin),
            (eq, ":gift", "itm_wine"),
            (assign, ":relation_boost", 1),
          (else_try),
            (eq, ":gift", "itm_oil"),
            (assign, ":relation_boost", 2),
          (try_end),
        (else_try),
          (store_random_in_range, ":random", 1, 3),
          (try_begin),
            (eq, ":gift", "itm_ale"),
            (val_add, ":relation_boost", ":random"),
          (else_try),
            (eq, ":gift", "itm_wine"),
            (store_add, ":relation_boost", 1, ":random"),
          (else_try),
            (eq, ":gift", "itm_oil"),
            (store_add, ":relation_boost", 2, ":random"),
          (else_try),
            (eq, ":gift", "itm_raw_dyes"),
            (val_add, ":relation_boost", 1),
          (else_try),
            (eq, ":gift", "itm_raw_silk"),
            (val_add, ":relation_boost", 2),
          (else_try),
            (eq, ":gift", "itm_velvet"),
            (val_add, ":relation_boost", 4),
          (else_try),
            (eq, ":gift", "itm_smoked_fish"),
            (try_begin),
              (party_slot_eq, ":target_party", slot_party_type, spt_village),
              (val_add, ":relation_boost", 1),
            (try_end),
          (else_try),
            (eq, ":gift", "itm_cheese"),
            (val_add, ":relation_boost", 1),
            (try_begin),
              (party_slot_eq, ":target_party", slot_party_type, spt_village),
              (val_add, ":relation_boost", 1),
            (try_end),
          (else_try),
            (eq, ":gift", "itm_honey"),
            (val_add, ":relation_boost", 2),
            (try_begin),
              (party_slot_eq, ":target_party", slot_party_type, spt_village),
              (val_add, ":relation_boost", 2),
            (try_end),
          (try_end),
        (try_end),

        (try_begin),
          (this_or_next|eq, ":target_faction", "fac_player_supporters_faction"),
          (eq, ":target_faction", "$players_kingdom"),
          (val_add, ":relation_boost", 1),
        (try_end),

		##nested diplomacy start+
		#Determine the gold cost of the gifts.
		(store_item_value, ":gift_value", ":gift"),
		#Determine how many copies of the gift are used
		(party_get_slot, ":gift_value_factor", ":party_no", dplmc_slot_party_mission_parameter_1),
		(try_begin),
			#This should only fail if the game was saved using an old version while
			#a caravan was en route.
			(gt, ":gift_value_factor", 0),
			(val_mul, ":gift_value", ":gift_value_factor"),
		(else_try),
			#Gifts to ladies had no multiplier.
			#Also, don't do anything for non-trade-goods.
			(this_or_next|is_between, ":target_troop", kingdom_ladies_begin, kingdom_ladies_end),
			(neg|is_between, ":gift", trade_goods_begin, trade_goods_end),
		(else_try),
			 #Gifts to lords used 150 copies of an item
			(is_between, ":target_troop", active_npcs_begin, active_npcs_end),
			(val_mul, ":gift_value", 150),
		(else_try),
			#Gifts to centers used 300 copies of an item
			(is_between, ":target_party", centers_begin, centers_end),
			(val_mul, ":gift_value", 300),
		(try_end),
		(assign, ":gift_value_factor", 100),

		#(store_sub, ":gift_slot_no", ":gift", trade_goods_begin),
		#(val_add, ":gift_slot_no", slot_town_trade_good_prices_begin),

		(try_begin),
			#Gift isn't a trade good: this should never happen
			(neg|is_between, ":gift", trade_goods_begin, trade_goods_end),
			(try_begin),
				(this_or_next|gt, ":target_troop", 0),
					(party_slot_eq, ":target_party", slot_party_type, spt_town),
				(assign, ":gift_value_factor", 115),
			(else_try),
				(assign, ":gift_value_factor", 130),
			(try_end),
		(else_try),
			#Given to a lord.
			(gt, ":target_troop", 0),

			(assign, ":global_price_factor", 0),
			(assign, ":faction_price_factor", 0),
			(assign, ":faction_markets", 0),
			(assign, ":personal_price_factor", 0),
			(assign, ":personal_markets", 0),

			(try_for_range, ":center_no", towns_begin, towns_end),
				(call_script, "script_dplmc_get_item_buy_price_factor", ":gift", ":center_no", -2, -2),
				(val_add, ":global_price_factor", reg0),

				(store_faction_of_party, ":center_faction", ":center_no"),
				(eq, ":center_faction", ":target_faction"),
				(val_add, ":faction_price_factor", reg0),
				(val_add, ":faction_markets", 1),

				(party_slot_eq, ":center_no", slot_town_lord, ":target_troop"),
				(val_add, ":personal_price_factor", reg0),
				(val_add, ":personal_markets", 1),
			(try_end),

			(try_begin),
				(eq, ":personal_markets", 0),
				(try_for_range, ":center_no", villages_begin, villages_end),
					(try_begin),
						(party_slot_eq, ":center_no", slot_town_lord, ":target_troop"),
						(call_script, "script_dplmc_get_item_buy_price_factor", ":gift", ":center_no", -2, -2),
						(val_add, ":faction_markets", reg0),
						(val_add, ":personal_markets", 1),
					(try_end),
					#Check for castles (deliberately allow multiple-counting)
					(try_begin),
						(party_get_slot, reg1, ":center_no", slot_village_bound_center),
						(gt, reg1, 0),
						(party_slot_eq, reg1, slot_party_type, spt_castle),
						(party_slot_eq, reg1, slot_town_lord, ":target_troop"),
						(call_script, "script_dplmc_get_item_buy_price_factor", ":gift", ":center_no", -2, -2),
						(val_add, ":faction_markets", reg0),
						(val_add, ":personal_markets", 1),
					(try_end),
				(try_end),
			(try_end),

			(try_begin),
				#First use any markets at or near the target's fiefs
				(gt, ":personal_markets", 0),
				(store_div, ":gift_value_factor", ":personal_price_factor", ":personal_markets"),
			(else_try),
				#Alternately use any faction markets
				(gt, ":faction_markets", 0),
				(val_mul, ":faction_price_factor", 130),#Convert trade penalty from 115% to 130%
				(val_div, ":faction_price_factor", 115),
				(store_div, ":gift_value_factor", ":faction_price_factor", ":faction_markets"),
			(else_try),
				#As a final option use the global average price
				(gt, towns_end, towns_begin),#should always be true (if not, then the gift price factor stays average)
				(store_sub, reg1, towns_end, towns_begin),
				(val_mul, ":global_price_factor", 130),#Convert trade penalty from 115% to 130%
				(val_div, ":global_price_factor", 115),
				(store_div, ":gift_value_factor", ":global_price_factor", reg1),
			(try_end),
		(else_try),
			#Given to a town or village
			(gt, ":target_party", 0),
			(call_script, "script_dplmc_get_item_buy_price_factor", ":gift", ":center_no", -2, -2),
			(assign, ":gift_value_factor", reg0),
		(else_try),
			#This should never happen
			(assign, ":gift_value_factor", 115),
		(try_end),

		(try_begin),
			(ge, "$cheat_mode", 1),
			(assign, reg0, ":gift_value_factor"),
			(store_mul, reg1, ":gift_value", ":gift_value_factor"),
			(val_add, reg1, 50),
			(val_div, reg1, 100),
			(val_add, reg1, 50),
			#(display_message, "@{!} Gift price factor {reg0}/100, effective value {reg1}"),
		(try_end),

		(val_mul, ":gift_value", ":gift_value_factor"),
		(val_add, ":gift_value", 50),
		(val_div, ":gift_value", 100),

		(val_add, ":gift_value", 50),#the cost of the messenger
	    (store_random_in_range, ":random", 0, 1000),#randomly round up or down later, when dividing by 1000
		(assign, reg0, ":gift_value"),#<-- see (1) below, store gold value of gift
		(val_add, ":gift_value", ":random"),
		(val_div, ":gift_value", 1000),

		(try_begin),
		   (eq, ":reduce_campaign_ai", 0), #hard: do not exceed 1/1000 efficiency
		   (val_min, ":relation_boost", ":gift_value"),
		   (try_begin),
			  (eq, ":relation_boost", 0),
			  (store_random_in_range, ":random", 0, 1000),
			  (lt, ":random", reg0),#<-- (1) see above, has gold value of gift
			  (assign, ":relation_boost", 1),
		   (try_end),
		(else_try),
		   (eq, ":reduce_campaign_ai", 1), #medium: use a blend of the two
		   (lt, ":gift_value", ":relation_boost"),
		   (val_add, ":relation_boost", ":gift_value"),
		   (val_add, ":relation_boost", 1),
		   (val_div, ":relation_boost", 2),
	    (else_try),
		   (eq, ":reduce_campaign_ai", 2), #easy: do not use
		(try_end),

		(val_max, ":gift_value", 1),
		(val_min, ":relation_boost", ":gift_value"),
		##nested diplomacy end+

        (try_begin),
		##nested diplomacy start+
		#Write a message so the player doesn't think the lack of relation gain is an error.
			(lt, ":relation_boost", 1),
			(try_begin),
				(gt, ":target_troop", 0),
				(display_message, "@{s13} is unimpressed by your paltry gift."),
			(else_try),
				(display_message, "@The people of {s13} are unimpressed by your paltry gift."),
			(try_end),
		(else_try),
		##nested diplomacy+
          (gt, ":target_troop", 0),
		  (call_script, "script_change_player_relation_with_troop", ":target_troop", ":relation_boost"),
        (else_try),
          (call_script, "script_change_player_relation_with_center", ":target_party", ":relation_boost"),
        (try_end),
        (remove_party, ":party_no"),
      (try_end),
    (else_try),
      (display_log_message, "@Your caravan has lost it's way and gave up your mission!", message_defeated), #SB : message code
      (remove_party, ":party_no"),
    (try_end),
  (try_end),
  ##nested diplomacy start+
  (assign, reg0, ":save_reg0"),
  (assign, reg1, ":save_reg1"),
  ##nested diplomacy start+
 ]),

 #process messengers
 (1, #SB: half as often
 [
  (try_for_parties, ":party_no"),
      (gt, ":party_no", last_static_party), #madsci
    (party_slot_eq,":party_no", slot_party_type, spt_messenger),

    (party_get_slot, ":target_party", ":party_no", slot_party_ai_object),
    (party_get_slot, ":orders_object", ":party_no", slot_party_orders_object),

    (try_begin),
      (party_is_active, ":target_party"),
      (store_distance_to_party_from_party, ":distance_to_target", ":party_no", ":target_party"),
      (str_store_party_name, s14, ":party_no"),
      (str_store_party_name, s15,":target_party"),

      (try_begin), #debug
        (eq, "$cheat_mode", 1),
        (assign, reg0, ":distance_to_target"),
        #(display_message, "@Distance between {s14} and {s15}: {reg0}"),
      (try_end),

      (try_begin),
        (le, ":distance_to_target", 1),

        (try_begin), # returning to p_main_party
          (eq, ":target_party", "p_main_party"),
          (party_get_slot, ":party_leader", ":party_no", slot_party_orders_object),
          (party_get_slot, ":success", ":party_no", dplmc_slot_party_mission_diplomacy),
          (call_script, "script_add_notification_menu", "mnu_dplmc_messenger", ":party_leader", ":success"),
          (remove_party, ":party_no"),
        (else_try), # patrols
          (party_slot_eq, ":target_party", slot_party_type, spt_patrol),
          (party_get_slot, ":message", ":party_no", dplmc_slot_party_mission_diplomacy),

          #SB : quick string to strings
          (try_begin),
            (eq, ":message", spai_undefined),
            (remove_party, ":target_party"),
          (else_try),
            (eq, ":message", spai_retreating_to_center),
            (str_store_party_name, s5, ":orders_object"),
            (party_set_name, ":target_party", "str_s5_transfer"),
            (party_set_ai_behavior, ":target_party", ai_bhvr_travel_to_party),
            (party_set_ai_object, ":target_party", ":orders_object"),
            (party_set_slot, ":target_party", slot_party_ai_object, ":orders_object"),
            (party_set_slot, ":target_party", slot_party_ai_state, spai_retreating_to_center),
            (party_set_aggressiveness, ":target_party", 0),
            (party_set_courage, ":target_party", 3),
            (party_set_ai_initiative, ":target_party", 100),
          (else_try),
            (str_store_party_name, s5, ":orders_object"),
            (party_set_name, ":target_party", "str_s5_patrol"),
            (party_set_ai_behavior, ":target_party", ai_bhvr_travel_to_party),
            (party_set_ai_object, ":target_party", ":orders_object"),
            (party_set_slot, ":target_party", slot_party_ai_object, ":orders_object"),
            (party_set_slot, ":target_party", slot_party_orders_type, ":message"),
          (try_end),

          (remove_party, ":party_no"),
        (else_try), # SB : reached a center (waypoint) as target troop has not yet spawned
          (is_between, ":target_party", walled_centers_begin, walled_centers_end),
          (party_get_slot, ":target_troop", ":party_no", dplmc_slot_party_origin),
          (try_begin), #retarget
            (troop_get_slot, ":leaded_party", ":target_troop", slot_troop_leaded_party),
            (gt, ":leaded_party", 0),
            (party_is_active, ":leaded_party"),
            (neg|party_is_in_town, ":leaded_party", ":target_party"), #camping for some reason
            (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
            (party_set_ai_object, ":party_no", ":leaded_party"),
            (party_set_slot, ":party_no", slot_party_ai_object, ":leaded_party"), #drop down to the condition below
          (try_end),
        (else_try), # reached any other target
          (party_stack_get_troop_id, ":party_leader", ":target_party", 0),
          (str_store_troop_name, s13, ":party_leader"),

          (try_begin), #debug
            (eq, "$cheat_mode", 1),
            (display_log_message, "@Your messenger reached {s13}.", 0x00FF00),
            (assign, "$g_talk_troop", ":party_leader"), #debug
          (try_end),

          (party_get_slot, ":message", ":party_no", dplmc_slot_party_mission_diplomacy),
          (assign, ":success", 0),
          (try_begin),
            (party_set_slot, ":target_party", slot_party_commander_party, "p_main_party"),
          	(store_current_hours, ":hours"),
          	(party_set_slot, ":target_party", slot_party_following_orders_of_troop, "trp_kingdom_heroes_including_player_begin"),
          	(party_set_slot, ":target_party", slot_party_orders_object, ":orders_object"),
          	(party_set_slot, ":target_party", slot_party_orders_type, ":message"),

          	(party_set_slot, ":target_party", slot_party_orders_time, ":hours"),
            (call_script, "script_npc_decision_checklist_party_ai", ":party_leader"), #This handles AI for both marshal and other parties


            #(try_begin), #debug
              #(eq, "$cheat_mode", 1),
              #(display_message, "@{s14}"), #debug
            #(try_end),

            (try_begin),
              (eq, reg0, ":message"),
              (eq, reg1, ":orders_object"),
              (assign, ":success", 1),
            (try_end),
            (call_script, "script_party_set_ai_state", ":target_party", reg0, reg1),
          (try_end),

          (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
          (party_set_ai_object, ":party_no", "p_main_party"),
          (party_set_slot, ":party_no", slot_party_ai_object, "p_main_party"),
          (party_set_slot, ":party_no", slot_party_orders_object, ":party_leader"),
          (party_set_slot, ":party_no", dplmc_slot_party_mission_diplomacy, ":success"),
        (try_end),
      (try_end),
    (else_try),
      #SB : it's to its
      (display_log_message, "@Your messenger has lost its way and gave up your mission!", message_defeated),
      (remove_party, ":party_no"),
    (try_end),
  (try_end),
 ]),


  # Constable training
  (24, [
    (eq, "$g_player_constable", "trp_dplmc_constable"),
    (is_between, "$g_constable_training_center", walled_centers_begin, walled_centers_end),
    (party_slot_eq, "$g_constable_training_center", slot_town_lord, "trp_player"),
    (store_skill_level, ":trainer_level", skl_trainer, "trp_player"),
    (val_add, ":trainer_level", 4),
    (faction_get_slot, ":quality", "$players_kingdom", dplmc_slot_faction_quality),
    (try_begin), #quantity policy
      (is_between, ":quality", -4, 0),
      (val_mul, ":quality", -2), #-6 to -2
      (val_add, ":trainer_level", ":quality"),
    (try_end),
    (store_div, ":xp_gain", ":trainer_level", 2),

    (try_begin),
      # (ge, "$novice_training_difficulty", 1),
      (assign, ":max_distance", 50),
      (game_get_reduce_campaign_ai, ":base_number"), #0, 1, 2
      # (val_add, ":cur_number", "$novice_training_difficulty"), #1 to 6
      # (val_div, ":cur_number", 2),
      # (val_max, ":cur_number", 1),
      (assign, ":num_trainers", "$g_constable_training_improved"),
      (try_for_range, ":grounds", training_grounds_begin, training_grounds_end),
        (store_distance_to_party_from_party, ":distance", ":grounds", "$g_constable_training_center"),
        (lt, ":distance", ":max_distance"),
        # (assign, ":max_distance", ":distance"),
        (party_get_slot, ":trainer", slot_grounds_trainer, ":grounds"),
        (troop_get_slot, ":difficulty", ":trainer", slot_troop_trainer_training_difficulty),
        # (gt, ":difficulty", 0), #1-6
        (store_add, ":cur_number", ":base_number", ":difficulty"),
        (val_div, ":cur_number", 2),
        (val_max, ":cur_number", 1),
        (val_add, ":xp_gain", ":cur_number"),
        (val_add, ":num_trainers", 1),
      (try_end),
    (try_end),

   #SB : move calculations up
   (store_mul, ":troop_limit", ":num_trainers", 2), #from 0 to 4, +1 for each nearby ground
   (val_add, ":troop_limit", 7), #base recruit level in Natives + 1, values now can be 7/9/11/13/15

   (store_troop_gold, ":gold", "trp_household_possessions"), #player treasury
   (store_mul, ":total_cost", "$g_constable_training_improved", dplmc_trainers_cost), #base cost
   #probably do a message here notifying trainers have left your service
   (gt, ":gold", ":total_cost"),
   #SB : wtf is this
   # (try_for_parties, ":party_no"),
    # (party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
    # (eq, ":party_no", "$g_constable_training_center"),
    (assign, ":party_no", "$g_constable_training_center"),

    (party_get_num_companion_stacks, ":num_stacks", ":party_no"),

    # (assign, ":trained", 0),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
      # (eq, ":trained", 0),
      (gt, ":xp_gain", 0),
      (party_stack_get_troop_id, ":troop_id", ":party_no", ":i_stack"),
      (neg|troop_is_hero, ":troop_id"),

      #SB : lots of upgrade troop parsing
      (assign, ":upgrade_troop", -1),
      (troop_get_upgrade_troop, ":upgrade_troop_1", ":troop_id", 0),
      (gt, ":upgrade_troop_1", 0), #if first upgrade doesn't exist, it can't upgrade at all
      (try_begin),
        # (troop_get_class, ":grc", ":upgrade_troop_1"),
        # (eq, ":grc", "$g_constable_training_type"),
        (call_script, "script_cf_troop_is_class", "$g_constable_training_type", ":upgrade_troop_1"),
        (assign, ":upgrade_troop", ":upgrade_troop_1"),
      (else_try),
        (troop_get_upgrade_troop, ":upgrade_troop_2", ":troop_id" , 1),
        (call_script, "script_cf_troop_is_class", "$g_constable_training_type", ":upgrade_troop_2"),
        (assign, ":upgrade_troop", ":upgrade_troop_2"),
      (else_try), #do a look-ahead
        (assign, ":upgrade_troop", ":upgrade_troop_1"), #fixed
        (try_begin),
          (troop_get_upgrade_troop, ":upgrade_troop_3", ":upgrade_troop_1" , 0),
          (call_script, "script_cf_troop_is_class", "$g_constable_training_type", ":upgrade_troop_3"),
          (assign, ":upgrade_troop", ":upgrade_troop_3"),
        (else_try),
          (troop_get_upgrade_troop, ":upgrade_troop_4", ":upgrade_troop_1" , 1),
          (call_script, "script_cf_troop_is_class", "$g_constable_training_type", ":upgrade_troop_4"),
          (assign, ":upgrade_troop", ":upgrade_troop_4"),
        (try_end),
        (eq, ":upgrade_troop", ":upgrade_troop_1"), #unchanged, check upgrade_troop_2
        (try_begin),
          (troop_get_upgrade_troop, ":upgrade_troop_3", ":upgrade_troop_2" , 0),
          (call_script, "script_cf_troop_is_class", "$g_constable_training_type", ":upgrade_troop_3"),
          (assign, ":upgrade_troop", ":upgrade_troop_3"),
        (else_try),
          (troop_get_upgrade_troop, ":upgrade_troop_4", ":upgrade_troop_2" , 1),
          (call_script, "script_cf_troop_is_class", "$g_constable_training_type", ":upgrade_troop_4"),
          (assign, ":upgrade_troop", ":upgrade_troop_4"),
        (try_end),
      (try_end),
      #only proceed if troop is upgradable
      (gt, ":upgrade_troop", 0),

      (store_character_level, ":troop_level", ":troop_id"),
      (le, ":troop_level", ":troop_limit"),

      # (party_count_members_of_type,":cur_number",":party_no",":troop_id"),
      (party_stack_get_size, ":cur_number", ":party_no", ":i_stack"),
      (party_stack_get_num_wounded, ":num_wounded",":party_no",":i_stack"),
      (val_sub, ":cur_number", ":num_wounded"),
      (try_begin),
        (ge, "$g_constable_training_improved", 1),
        (le, ":troop_level", 6),
        (val_add, ":cur_number", 2), #more recruits are trained during improved training
      (try_end),
      (val_min, ":cur_number", ":xp_gain"),

      (call_script, "script_game_get_upgrade_cost", ":troop_id"),
      (store_mul, ":upgrade_cost", ":cur_number", reg0),

      # (try_for_range, ":troop_count", 0, ":cur_number"),
        # (gt, ":gold", ":total_cost"),
        # (val_add, ":total_cost", ":upgrade_cost"),
      # (else_try), #break and lower cur_number
        # (val_sub, ":total_cost", ":upgrade_cost"), #can't afford
        # (assign, ":cur_number", ":troop_count"),
      # (try_end),

      # (store_troop_gold, ":gold", "trp_household_possessions"),
      (val_add, ":total_cost", ":upgrade_cost"),
      (try_begin), #if we can only afford partial upgrades
        (lt, ":gold", ":total_cost"),
        (val_sub, ":total_cost", ":upgrade_cost"), #undo
        (val_div, ":upgrade_cost", ":cur_number"), #get original cost
        (store_sub, ":cur_number", ":gold", ":total_cost"), #get remainder
        (val_div, ":cur_number", ":upgrade_cost"), #get however many we can afford
        (val_mul, ":cur_number", ":upgrade_cost"), #then redo
        (val_add, ":total_cost", ":upgrade_cost"),
        (str_store_troop_name_plural, s6, ":troop_id"),
        (display_message, "@Not enough money in treasury to upgrade {s6}."),
      (try_end),

      # (val_add, ":total_cost", ":upgrade_cost"),
      # (call_script, "script_dplmc_withdraw_from_treasury", ":upgrade_cost"),
      (party_remove_members,":party_no",":troop_id",":cur_number"),
      (party_add_members, ":party_no", ":upgrade_troop", ":cur_number"),
      (val_sub, ":xp_gain", ":cur_number"),
      (assign, reg5, ":cur_number"),
      (str_store_troop_name_by_count, s6, ":troop_id", ":cur_number"),
      (str_store_troop_name_by_count, s7, ":upgrade_troop", ":cur_number"),
      (str_store_party_name_link, s8, ":party_no"),
      (display_log_message, "@Your constable upgraded {reg5} {s6} to {s7} in {s8}"),
    (try_end),

    #finalize costs
    (call_script, "script_dplmc_withdraw_from_treasury", ":total_cost"),
   # (try_end),
    ]),

  # Patrol wages
   (24 * 7,
   [

    (try_for_parties, ":party_no"),
      (gt, ":party_no", last_static_party), #madsci
      (party_slot_eq,":party_no", slot_party_type, spt_patrol),



      (party_get_slot, ":ai_state", ":party_no", slot_party_ai_state),
      (eq, ":ai_state", spai_patrolling_around_center),

      (try_begin),
		(party_slot_eq, ":party_no", dplmc_slot_party_mission_diplomacy, "trp_player"),
        (assign, ":total_wage", 0),
        (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop", ":party_no", ":i_stack"),
          (party_stack_get_size, ":stack_size", ":party_no", ":i_stack"),
          (call_script, "script_game_get_troop_wage", ":stack_troop", 0),
          (val_mul, reg0, ":stack_size"),
          (val_add, ":total_wage", reg0),
        (try_end),
        (store_troop_gold, ":gold", "trp_household_possessions"),
        (try_begin),
          (lt, ":gold", ":total_wage"),
          (party_get_slot, ":target_party", ":party_no", slot_party_ai_object),
          (str_store_party_name, s6, ":target_party"),
          (display_log_message, "@Your soldiers patrolling {s6} disbanded because you can't pay the wages!", message_defeated), #SB : message code
          (remove_party, ":party_no"),
        (try_end),
      (try_end),
    (try_end),
    ]),

  #create ai patrols
   (1.6, #daily on average
   [
    #(try_for_range, ":kingdom", npc_kingdoms_begin, npc_kingdoms_end),

      (store_random_in_range, ":kingdom", npc_kingdoms_begin, npc_kingdoms_end),

      (assign, ":max_patrols", 1),
      # (try_for_range, ":center", towns_begin, towns_end),
        # (store_faction_of_party, ":center_faction", ":center"),
        # (eq, ":center_faction", ":kingdom"),
        # (val_add, ":max_patrols", 1),
      # (try_end),
      #it is already counted
      (faction_get_slot, ":max_patrols", ":kingdom", slot_faction_num_towns),

     #I rethought this and think it is unnecessary
      # (try_begin), #Nero change
        # (eq, ":kingdom", "fac_kingdom_7"),
        # (val_mul, ":max_patrols", 2),
      # (try_end),

      (assign, ":count", 0),
      (try_for_parties, ":party_no"),
      (gt, ":party_no", last_static_party), #madsci
        (party_slot_eq, ":party_no", slot_party_type, spt_patrol),
        (store_faction_of_party, ":party_faction", ":party_no"),
        (eq, ":party_faction", ":kingdom"),
        (neg|party_slot_eq, ":party_no", dplmc_slot_party_mission_diplomacy, "trp_player"), #not player ordered
        (try_begin),
           #Remove patrols above the maximum number allowed.
           (ge, ":count", ":max_patrols"),
           (try_begin),
              (ge, "$cheat_mode", 1),
              (str_store_faction_name, s4, ":kingdom"),
              (str_store_party_name, s5, ":party_no"),
              #(display_message, "@{!}DEBUG - Removed {s5} because {s4} cannot support that many patrols"),
           (try_end),
           (remove_party, ":party_no"),
        (else_try),
           (val_add, ":count", 1),
        (try_end),
      (try_end),

      (try_begin),
        (lt, ":count", ":max_patrols"),

        (store_random_in_range, ":random", 0, 10),
        (le, ":random", 3),

        (assign, ":start_center", -1),
        (assign, ":target_center", -1),

        (try_for_range, ":center", towns_begin, towns_end),
          (store_faction_of_party, ":center_faction", ":center"),
          (eq, ":center_faction", ":kingdom"),

          (eq, ":start_center", -1),
          (eq, ":target_center", -1),

          (assign, ":continue", 1),
          (try_for_parties, ":party_no"),
		(gt, ":party_no", last_static_party), #madsci
            (party_slot_eq, ":party_no", slot_party_type, spt_patrol),
            (store_faction_of_party, ":party_faction", ":party_no"),
            (eq, ":party_faction", ":kingdom"),
            (party_get_slot, ":target", ":party_no", slot_party_ai_object),
            (eq, ":target", ":center"),
            (assign, ":continue", 0),
          (try_end),
          (eq, ":continue", 1),

          (call_script, "script_cf_select_random_town_with_faction", ":kingdom"),
          (neq, reg0, -1),

          (assign, ":start_center", reg0),
          (assign, ":target_center", ":center"),
        (try_end),

        (try_begin),
          (neq, ":start_center", -1),
          (neq, ":target_center", -1),
          (store_random_in_range, ":random_size", 0, 3),
          (faction_get_slot, ":faction_leader", ":kingdom", slot_faction_leader),
          (call_script, "script_dplmc_send_patrol", ":start_center", ":target_center", ":random_size",":kingdom", ":faction_leader"),
        (try_end),
      (try_end),
    #(try_end),
    ]),

  # Patrol ai
   (2,
   [

    (try_for_parties, ":party_no"),
      (gt, ":party_no", last_static_party), #madsci
      (party_slot_eq,":party_no", slot_party_type, spt_patrol),

      # (call_script, "script_party_remove_all_prisoners", ":party_no"), #SB : retain prisoners

      (try_begin),
        (get_party_ai_behavior, ":ai_behavior", ":party_no"),
        (eq, ":ai_behavior", ai_bhvr_travel_to_party),
        (party_get_slot, ":target_party", ":party_no", slot_party_ai_object),

        (try_begin),
          (gt, ":target_party", 0),
          (store_distance_to_party_from_party, ":distance_to_target", ":party_no", ":target_party"),
          (le, ":distance_to_target", 5),
          (try_begin), #SB : drop off prisoners
            (le, ":distance_to_target", 3),
            (is_between, ":target_party", walled_centers_begin, walled_centers_end),
            (call_script, "script_party_add_party_prisoners", ":target_party", ":party_no"),
            (call_script, "script_party_remove_all_prisoners", ":party_no"),
          (try_end),
          (try_begin),
            (party_get_slot, ":ai_state", ":party_no", slot_party_ai_state),
            (eq, ":ai_state", spai_retreating_to_center),
            (try_begin),
              (le, ":distance_to_target", 1),
              (call_script, "script_party_add_party", ":target_party", ":party_no"),
              (remove_party, ":party_no"),
            (try_end),
          (else_try),
            (party_get_position, pos1, ":target_party"),
            (party_set_ai_behavior,":party_no", ai_bhvr_patrol_location),
            (party_set_ai_patrol_radius, ":party_no", 1),
            (party_set_ai_target_position, ":party_no", pos1),
          (try_end),

        # (else_try),
          # #remove party?
        (try_end),

      (try_end),
    (try_end),
    ]),

  # Scout ai
   (1.5, #SB : moved to 1.5 hr
   [

    (try_for_parties, ":party_no"),
      (gt, ":party_no", last_static_party), #madsci
      (party_slot_eq,":party_no", slot_party_type, spt_scout),

      (try_begin),
        (get_party_ai_behavior, ":ai_behavior", ":party_no"),
        (this_or_next|eq, ":ai_behavior", ai_bhvr_travel_to_point),
        (eq, ":ai_behavior", ai_bhvr_travel_to_party),

        (party_get_slot, ":target_party", ":party_no", slot_party_ai_object),
        (store_distance_to_party_from_party, ":distance_to_target", ":party_no", ":target_party"),
        (le, ":distance_to_target", 1),

        (try_begin),
          (eq, ":target_party", "p_main_party"),

          (party_get_slot, ":mission_target", ":party_no", dplmc_slot_party_mission_diplomacy),
          (call_script, "script_add_notification_menu", "mnu_dplmc_scout", ":mission_target", 0),

          (remove_party, ":party_no"),
        (else_try),
          (neq, ":target_party", "p_main_party"),
          (party_get_slot, ":hours", ":party_no", dplmc_slot_party_mission_diplomacy),

          (try_begin),
            (le, ":hours", 100),
            (disable_party, ":party_no"),
            (val_add, ":hours", 1),
            (party_set_slot, ":party_no", dplmc_slot_party_mission_diplomacy, ":hours"),

            (try_begin),
              (store_random_in_range, ":random", 0, 1000),
              (eq, ":random", 0),
              (str_store_party_name, s11, ":target_party"),
              (display_log_message, "@It is rumoured that a spy has been caught in {s11}.", message_defeated), #SB : message code
              (remove_party, ":party_no"),
            (try_end),

          (else_try),
            (enable_party, ":party_no"),
            (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
            (party_set_ai_object, ":party_no", "p_main_party"),
            (party_set_slot, ":party_no", slot_party_ai_object, "p_main_party"),
            (party_set_slot, ":party_no", dplmc_slot_party_mission_diplomacy, ":target_party"),
          (try_end),

        (try_end),
      (try_end),
    (try_end),
    ]),

  # Policy
   (30 * 24,
   [
	##nested diplomacy start+
	##If the player is ruler or co-ruler of an NPC kingdom, make sure the
	#policy matches fac_player_supporters_faction.  (It should be synchronized
	#elsewhere, but do it here in case there has been an error.)
	(assign, ":player_is_coruler_of_npc_faction", 0),
	  (try_begin),
		(neq, "$players_kingdom", "fac_player_supporters_faction"),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),

		(assign, ":player_is_coruler_of_npc_faction", 1),

		(faction_get_slot, reg0, "$players_kingdom", dplmc_slot_faction_serfdom),
		(faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_serfdom, reg0),

		(faction_get_slot, reg0, "$players_kingdom", dplmc_slot_faction_centralization),
		(faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_centralization, reg0),

		(faction_get_slot, reg0, "$players_kingdom", dplmc_slot_faction_quality),
		(faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_quality, reg0),

		(faction_get_slot, reg0, "$players_kingdom", dplmc_slot_faction_aristocracy),
		(faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_aristocracy, reg0),

		(faction_get_slot, reg0, "$players_kingdom", dplmc_slot_faction_mercantilism),
		(faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_mercantilism, reg0),
	(try_end),
	##nested diplomacy end+
  (try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
    (faction_slot_eq, ":kingdom", slot_faction_state, sfs_active),

    (faction_get_slot, ":centralization", ":kingdom", dplmc_slot_faction_centralization),
    (faction_get_slot, ":aristocracy", ":kingdom", dplmc_slot_faction_aristocracy),
    (faction_get_slot, ":quality", ":kingdom", dplmc_slot_faction_quality),
    (faction_get_slot, ":serfdom", ":kingdom", dplmc_slot_faction_serfdom),
	 ##nested diplomacy start+
    (faction_get_slot, ":mercantilism", ":kingdom", dplmc_slot_faction_mercantilism),
	 ##nested diplomacy end+

    (try_begin),
      (eq, "$cheat_mode", 1),
      (str_store_faction_name, s9, ":kingdom"),
      (assign, reg1, ":centralization"),
      #(display_message, "@{!}DEBUG - centralization {reg1}"),
      (assign, reg1, ":aristocracy"),
      #(display_message, "@{!}DEBUG - aristocracy {reg1}"),
      (assign, reg1, ":quality"),
      #(display_message, "@{!}DEBUG - quality {reg1}"),
      (assign, reg1, ":serfdom"),
      #(display_message, "@{!}DEBUG - serfdom {reg1}"),
		##nested diplomacy start+
      (assign, reg1, ":mercantilism"),
      #(display_message, "@{!}DEBUG - mercantilism {reg1}"),
		##nested diplomacy end+
    (try_end),

    (try_begin),
      (is_between, ":kingdom", npc_kingdoms_begin, npc_kingdoms_end),
      ##nested diplomacy start+
      ##Ensure the player isn't the kingdom's ruler or co-ruler
      (this_or_next|neq, ":kingdom", "$players_kingdom"),
      (eq, ":player_is_coruler_of_npc_faction", 0),
      ##Add the chance to move around mercantilism.
      #(store_random_in_range, ":random", 0, 8),
      (store_random_in_range, ":random", 0, 10),
      ##nested diplomacy end+

      (try_begin),
        ##nested diplomacy start+
        #(is_between, ":random", 1, 5),
        (is_between, ":random", 1, 6),
        ##nested diplomacy end+
        (store_random_in_range, ":change", -1, 2),

        (try_begin),
          (eq, "$cheat_mode", 1),
          (str_store_faction_name, s12, ":kingdom"),
          (assign, reg1, ":change"),
          (assign, reg2, ":random"),
          #(display_message, "@{!}DEBUG - changing {reg1} of {reg2} for {s12}"),
        (try_end),

        (try_begin),
          (eq, ":random", 1),
          (val_add, ":centralization", ":change"),
          (val_max, ":centralization", -3),
          (val_min, ":centralization", 3),
          (faction_set_slot, ":kingdom", dplmc_slot_faction_centralization, ":centralization"),
        (else_try),
          (eq, ":random", 2),
          (val_add, ":aristocracy", ":change"),
          (val_max, ":aristocracy", -3),
          (val_min, ":aristocracy", 3),
          (faction_set_slot, ":kingdom", dplmc_slot_faction_aristocracy, ":aristocracy"),
        (else_try),
          (eq, ":random", 3),
          (val_add, ":quality", ":change"),
          (val_max, ":quality", -3),
          (val_min, ":quality", 3),
          (faction_set_slot, ":kingdom", dplmc_slot_faction_quality, ":quality"),
        (else_try),
          (eq, ":random", 4),
          (val_add, ":serfdom", ":change"),
          (val_max, ":serfdom", -3),
          (val_min, ":serfdom", 3),
          (faction_set_slot, ":kingdom", dplmc_slot_faction_serfdom, ":serfdom"),
          ##nested diplomacy start+
          (eq, ":random", 5),
          (val_add, ":mercantilism", ":change"),
          (val_clamp, ":mercantilism", -3, 4),#-3 min, +3 max
          (faction_set_slot, ":kingdom", dplmc_slot_faction_mercantilism, ":mercantilism"),
          ##nested diplomacy end+
        (try_end),
      (try_end),

    (else_try),

      #only player faction is affected by relation hits
      ##nested diplomacy start+
      ##Don't alter the values of centralization and aristocracy, since that's confusing.
      #(store_mul, ":centralization", ":centralization", -1),
      #(store_mul, ":aristocracy", ":aristocracy", 1),
      #(store_add, ":relation_change", ":centralization", ":aristocracy"),

		(store_sub, ":relation_change", ":aristocracy", ":centralization"),
      ##custodian (merchant) lords like plutocracy, unlike ordinary lords
      (store_mul, ":custodian_change", ":aristocracy", -1),
		(val_sub, ":custodian_change", ":centralization"),
      #benefactor lords like freedom and dislike serfdom
		(store_mul, ":benefactor_change", ":serfdom", -1),
		(val_sub, ":custodian_change", ":centralization"),
      ##nested diplomacy end+
      (try_begin),
        ##nested diplomacy start+
        (this_or_next|neq, ":benefactor_change", 0),
        (this_or_next|neq, ":custodian_change", 0),
        ##nested diplomacy end+
        (neq, ":relation_change", 0),

        (try_begin),
          (eq, "$cheat_mode", 1),
          (str_store_faction_name, s9, ":kingdom"),
          (assign, reg1, ":relation_change"),
          #(display_message, "@{!}DEBUG - relation_change =  {reg1} for {s9}"),
        (try_end),

        ##diplomacy start+ also include kingdom ladies who are kingdom heroes
        #(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
        (try_for_range, ":troop_no", heroes_begin, heroes_end),
        ##diplomacy end+
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (store_troop_faction, ":faction_no", ":troop_no"),
          (eq, ":kingdom", ":faction_no"),
          (faction_get_slot, ":faction_leader", ":kingdom", slot_faction_leader),
          ##diplomacy start+
          (neq, ":troop_no", ":faction_leader"),
          (assign, ":change_for_troop", ":relation_change"),
          (try_begin),
             (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_custodian),
             (assign, ":change_for_troop", ":custodian_change"),
          (else_try),
             (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_benefactor),
             (assign, ":change_for_troop", ":benefactor_change"),
          (try_end),
          ##Extra penalty for going back on a promise, extra bonus for keeping it
          (assign, ":promise_mod", 0),
          (try_begin),
             ##Following are only relevant for companions
				 (is_between, ":troop_no", companions_begin, companions_end),
             (troop_slot_eq, ":troop_no", slot_troop_kingsupport_state, 1),
             (try_begin),
                #Argument: Lords
                (troop_slot_eq, ":troop_no", slot_troop_kingsupport_argument, argument_lords),
                (try_begin),
                  #If more than slightly centralized, or more than slightly balanced against aristocrats
                  (this_or_next|neg|faction_slot_ge, ":faction_no", dplmc_slot_faction_aristocracy, -1),
                     (faction_slot_ge, ":faction_no", dplmc_slot_faction_centralization, 2),
                  (val_sub, ":promise_mod", 1),
                (else_try),
                  #If more than slightly decentralized or more than slightly balanced in favor of aristocrats
                  (this_or_next|faction_slot_ge, ":faction_no", dplmc_slot_faction_aristocracy, 2),
                  (neg|faction_slot_ge, ":faction_no", dplmc_slot_faction_centralization, -2),
                  (faction_slot_ge, ":faction_no", dplmc_slot_faction_aristocracy, -1),#redundant
                  (val_add, ":promise_mod", 1),
                (try_end),
             (else_try),
                  #Argument: Commons
                  (troop_slot_eq, ":troop_no", slot_troop_kingsupport_argument, argument_commons),
                  (try_begin),
                    (faction_slot_ge, ":faction_no", dplmc_slot_faction_serfdom, 2),
                    (val_sub, ":promise_mod", 1),
                  (else_try),
                    (neg|faction_slot_ge, ":faction_no", dplmc_slot_faction_serfdom, 0),
                    (store_add, ":local_temp", ":serfdom", ":aristocracy"),
                    (lt, ":local_temp", 0),
                    (val_add, ":promise_mod", 1),
                  (try_end),
             (try_end),
         (try_end),
         #Check other broken promises
         (try_begin),
             (troop_slot_eq, ":troop_no", slot_lord_recruitment_argument, argument_lords),
             (this_or_next|neg|faction_slot_ge, ":faction_no", dplmc_slot_faction_aristocracy, -1),
                (faction_slot_ge, ":faction_no", dplmc_slot_faction_centralization, 2),
             #Lord must actually have cared about argument
             (neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
             (neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
             (val_sub, ":promise_mod", 1),
         (else_try),
             (troop_slot_eq, ":troop_no", slot_lord_recruitment_argument, argument_commons),
             (faction_slot_ge, ":faction_no", dplmc_slot_faction_serfdom, 2),
             #Lord must actually have cared about argument
             (neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
             (neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
             (neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
             (val_sub, ":promise_mod", 1),
         (try_end),
         (val_clamp, ":promise_mod", -1, 2),#-1, 0, or 1
         (val_add, ":change_for_troop", ":promise_mod"),

		 (neq, ":change_for_troop", 0),
		 (call_script, "script_change_player_relation_with_troop", ":troop_no", ":change_for_troop"),
        ##diplomacy end+
        (try_end),
      (try_end),
    (try_end),
  (try_end),
  ]),

  # affilated family ai
   (24 * 7,
   [
	##nested diplomacy start+ (piggyback on this trigger) allow lords to return from exile
	(assign, ":save_reg0", reg0),
	(assign, ":save_reg1", reg1),
	(assign, ":save_reg4", reg4),
	(try_begin),
		#only proceed if setting is enabled
		(ge, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_ENABLE),
		#Kings/pretenders do not return in this manner (it should be different if it does happen).
		#Companions have a separate mechanism for return.
		(assign, ":chosen_lord", -1),
		(assign, ":best_score", -101),
		(assign, ":num_exiles", 0),
		#iterate over lords from a random start point, wrapping back to zero
		(store_random_in_range, ":rand_no", lords_begin, lords_end),
		(try_for_range, ":index", lords_begin, lords_end),
		  (store_add, ":troop_no", ":rand_no", ":index"),
		  (try_begin),
			 #wrap back around when you go off the end
			  (ge, ":troop_no", lords_end),
			(val_sub, ":troop_no", lords_end),
			(val_add, ":troop_no", lords_begin),
		  (try_end),
		  #Elsewhere we do the bookkeeping of ensuring that when a lord gets exiled
		  #his occupation changes to dplmc_slto_exile, and when loading a Native
		  #saved gamed with diplomacy we make this change for any lords required.
		  (troop_slot_eq, ":troop_no", slot_troop_occupation, dplmc_slto_exile),

		  (store_troop_faction, ":faction_no", ":troop_no"),
		  (this_or_next|eq, ":faction_no", -1),
		  (this_or_next|eq, ":faction_no", "fac_commoners"),
			 (eq, ":faction_no", "fac_outlaws"),
		  (val_add, ":num_exiles", 1),
		  (try_begin),
		     #Pick the lord with the best relation with his original liege.
			  #In most cases this will be the lord that has been in exile
			  #the longest.
			  (troop_get_slot, ":new_faction", ":troop_no", slot_troop_original_faction),
			  (is_between, ":new_faction", kingdoms_begin, kingdoms_end),
			  (faction_get_slot, ":faction_leader", ":new_faction", slot_faction_leader),
			  (gt, ":faction_leader", 0),
			  (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),
			  (this_or_next|eq, ":chosen_lord", -1),
			     (gt, reg0, ":best_score"),
			  (assign, ":chosen_lord", ":troop_no"),
			  (assign, ":best_score", reg0),
		  (else_try),
		     (eq, ":chosen_lord", -1),
			 (assign, ":chosen_lord", ":troop_no"),
		  (try_end),
      (try_end),
		#search is done
		(try_begin),
		 #no lord found
		 (eq, ":chosen_lord", -1),
		 (try_begin),
			(ge, "$cheat_mode", 1),
			#(display_message, "@{!}DEBUG - no eligible lords in exile"),
		 (try_end),
	    (else_try),
			#If there were fewer than 3 lords in exile, random chance that none will return.
			(lt, ":num_exiles", 3),
			(store_random_in_range, ":random", 0, 256),
			(ge, ":random", 128),
			(try_begin),
				(ge, "$cheat_mode", 1),
				(assign, reg0, ":num_exiles"),
				#(display_message, "@{!}DEBUG - {reg0} lords found in exile; randomly decided not to try to return anyone."),
			(try_end),
		(else_try),
		 #found a lord
		 (neq, ":chosen_lord", -1),
		 (try_begin),
			(ge, "$cheat_mode", 1),
			(str_store_troop_name, s4, ":chosen_lord"),
			(assign, reg0, ":best_score"),
			(assign, reg1, ":num_exiles"),
			#(display_message, "@{!}DEBUG - {reg1} lords found in exile; {s4} chosen to return, score was {reg0}"),
		 (try_end),
		 #To decrease the displeasing fragmentation of lord cultures, bias towards assigning
		 #the lord back to his original faction if possible.
		 (troop_get_slot, ":new_faction", ":chosen_lord", slot_troop_original_faction),
		 (try_begin),
			 #If the original faction is not active, or the lord's relation is too low, use a different faction
			 (this_or_next|lt, ":best_score", -50),
			 (this_or_next|neg|is_between, ":new_faction", kingdoms_begin, kingdoms_end),
			    (neg|faction_slot_eq, ":new_faction", slot_faction_state, sfs_active),
		    (call_script, "script_lord_find_alternative_faction", ":chosen_lord"),
			(assign, ":new_faction", reg0),
		 (try_end),
		 (try_begin),
		   (neg|is_between, ":new_faction", kingdoms_begin, kingdoms_end),
			(ge, "$cheat_mode", 1),
			(str_store_troop_name, s4, ":chosen_lord"),
			#(display_message, "@{!}DEBUG - {s4} found no faction to return to!"),
		 (try_end),
		 (is_between, ":new_faction", kingdoms_begin, kingdoms_end),
		 (assign, ":num_inactive", 0),
		 (try_begin),
			(eq, ":new_faction", "$players_kingdom"),
			(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
			(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
			(assign, ":num_inactive", 0),
			(try_for_range, ":other_lord", lords_begin, lords_end),
			   (store_troop_faction, ":other_lord_faction", ":other_lord"),
			   (this_or_next|eq, ":other_lord_faction", "fac_player_supporters_faction"),
				(eq, ":other_lord_faction", "$players_kingdom"),
			   (troop_slot_eq, ":other_lord", slot_troop_occupation, slto_inactive),
			   (val_add, ":num_inactive", 1),
			(try_end),
			(gt, ":num_inactive", 1),
			(try_begin),
				(ge, "$cheat_mode", 1),
				(assign, reg0, ":num_inactive"),
				#(display_message, "@{!}DEBUG - Not returning a lord to the player's kingdom, since there are already {reg0} lords waiting for their petitions to be heard."),
			(try_end),
		 (else_try),
			(call_script, "script_dplmc_lord_return_from_exile", ":chosen_lord", ":new_faction"),
		 (try_end),
		(try_end),
	(try_end),
	##More piggybacking
	##
	(assign, reg0, ":save_reg0"),
	(assign, reg1, ":save_reg1"),
	(assign, reg4, ":save_reg4"),
	##nested diplomacy end+
    (is_between, "$g_player_affiliated_troop", lords_begin, kingdom_ladies_end),
	##nested diplomacy start+
	(assign, ":best_relation", -101),
	(assign, ":worst_relation", 101),

	(assign, ":num_at_least_20", 0),
	(assign, ":num_below_0", 0),

	(assign, ":good_relation", 0),
	##nested diplomacy end+

    (assign, ":bad_relation", 0),
    (try_for_range, ":family_member", lords_begin, kingdom_ladies_end),
      (call_script, "script_dplmc_is_affiliated_family_member", ":family_member"),
      (gt, reg0, 0),
      (call_script, "script_troop_get_player_relation", ":family_member"),
	  ##nested diplomacy start+
	  #(le, reg0, -20),
	  #(assign, ":bad_relation", ":family_member"),
  	  (try_begin),
		(lt, reg0, 0),
		(val_add, ":num_below_0", 1),
		(le, reg0, ":worst_relation"),
		(assign, ":bad_relation", ":family_member"),
	  (else_try),
		(ge, reg0, 20),
		(val_add, ":num_at_least_20", 1),
		(gt, reg0, ":best_relation"),
		(assign, ":good_relation", ":family_member"),
	  (try_end),

	  (val_max, ":best_relation", reg0),
	  (val_min, ":worst_relation", reg0),
	  ##nested diplomacy end+
    (try_end),
	##nested diplomacy start+
	(try_begin),
		(gt, ":worst_relation", -15),
		(assign, ":bad_relation", 0),#suppress with no message
	(else_try),
		(gt, ":worst_relation", -20),
		(str_store_troop_name_link, s0, ":bad_relation"),  #SB : link message, no colours
		(display_message, "@{s0} is grumbling against you.  Your affiliation could be jeopardized if this continues."),
		(str_clear, s0),
	(else_try),
		(neq, ":bad_relation", 0),
		(ge, ":num_at_least_20", ":num_below_0"),
		(store_add, reg0, ":worst_relation", ":best_relation"),
		(ge, reg0, 0),
		(str_store_troop_name_link, s0, ":bad_relation"),
		(str_store_troop_name_link, s1, ":good_relation"),  #SB : link message
		(display_message, "@{s0} is grumbling against you, but with {s1}'s support you remain affiliated for now."),
		(str_clear, s0),
		(str_clear, s1),
		(assign, ":bad_relation", 0),
	(try_end),
	##nested diplomacy end+
    (try_begin),
      (eq, ":bad_relation", 0),

      (try_for_range, ":family_member", lords_begin, kingdom_ladies_end),
        (call_script, "script_dplmc_is_affiliated_family_member", ":family_member"),
        (gt, reg0, 0),
        (try_begin),
           (troop_slot_ge, ":family_member", slot_troop_prisoner_of_party, 0),
           ##diplomacy start+ skip relationship decay for imprisonment when the player himself is imprisoned or wounded
           (neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 1),
           (neg|troop_is_wounded, "trp_player"),
           ##diplomacy end+
           (call_script, "script_change_player_relation_with_troop", ":family_member", -1),
        (else_try),
          (call_script, "script_change_player_relation_with_troop", ":family_member", 1),
        (try_end),
      (try_end),
    (else_try),
      (call_script, "script_add_notification_menu", "mnu_dplmc_affiliate_end", ":bad_relation", 0),
      (call_script, "script_dplmc_affiliate_end", 1),
    (try_end),
    ##nested diplomacy start+
    (assign, reg0, ":save_reg0"),
    (assign, reg1, ":save_reg1"),
    (assign, reg4, ":save_reg4"),
    ##nested diplomacy end+
    ]),

   (2,
   [
    (assign, ":has_walled_center", 0),
    (assign, ":has_fief", 0),
    (try_for_range, ":center_no", centers_begin, centers_end),
      (party_get_slot,  ":lord_troop_id", ":center_no", slot_town_lord),
      (eq, ":lord_troop_id", "trp_player"),
      (try_begin),
        (is_between, ":center_no", walled_centers_begin, walled_centers_end),
        (assign, ":has_walled_center", 1),
      (try_end),
      (assign, ":has_fief", 1),
    (try_end),

    (try_begin),
      (eq, ":has_walled_center", 0),
      (this_or_next|neq, "$g_player_constable", 0),
      (neq, "$g_player_chancellor", 0),
      (assign, "$g_player_constable", 0),
      (assign, "$g_player_chancellor", 0),
    (try_end),

    (try_begin),
      (eq, ":has_fief", 0),
      (neq, "$g_player_chamberlain", 0),
      (assign, "$g_player_chamberlain", 0),

      ##nested diplomacy start+
      #Adjust gold loss by difficulty
      (assign, ":save_reg0", reg0),
      (assign, ":save_reg1", reg1),

      (assign, ":loss_numerator", 2),
      (assign, ":loss_denominator", 3),

      (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
      (try_begin),
        (eq, ":reduce_campaign_ai", 0), #hard, lose 5/6
        (assign, ":loss_numerator", 5),
        (assign, ":loss_denominator", 6),
      (else_try),
        (eq, ":reduce_campaign_ai", 1), #medium, lose 2/3
        (assign, ":loss_numerator", 2),
        (assign, ":loss_denominator", 3),
      (else_try),
        (eq, ":reduce_campaign_ai", 2), #easy, lose 1/2
        (assign, ":loss_numerator", 1),
        (assign, ":loss_denominator", 2),
      (try_end),

      (store_troop_gold, ":cur_gold", "trp_household_possessions"),
      (try_begin),
        (gt, ":cur_gold", 0),
        #(call_script, "script_dplmc_withdraw_from_treasury", ":cur_gold"),
        #(val_div, ":cur_gold", 3),
        #(call_script, "script_troop_add_gold", "trp_player", ":cur_gold"),
        #(display_message, "@Your last fief was captured and you lost 2/3 of your treasury"),
        (store_mul, ":lost_gold", ":cur_gold", ":loss_numerator"),
        (val_div, ":lost_gold", ":loss_denominator"),
        (val_mul, ":lost_gold", -1),
        (call_script, "script_dplmc_withdraw_from_treasury", ":lost_gold"),
        (assign, reg0, ":loss_numerator"),
        (assign, reg1, ":loss_denominator"),
        #SB : colorize
        (display_message, "@Your last fief was captured and you lost {reg0}/{reg1} of your treasury", message_negative),
      (try_end),

      (assign, reg0, ":save_reg0"),
      (assign, reg1, ":save_reg1"),
      ##nested diplomacy end+
    (try_end),
    ]),

  ##diplomacy end

#+freelancer start
  #  WEEKLY PAY AND CHECKS FOR UPGRADE
    (24 * 7, [
    (eq, "$freelancer_state", 1),
    (store_current_hours, reg0),
    (val_add, reg0, 24 * 7),
    (quest_set_slot, "qst_freelancer_enlisted", slot_quest_freelancer_next_payday, reg0),

    (try_begin),
      (troop_get_upgrade_troop, ":upgrade_troop", "$player_cur_troop", 0),
      (gt, ":upgrade_troop", 1), #make sure troop is valid and not player troop
      (quest_slot_ge, "qst_freelancer_enlisted", slot_quest_freelancer_upgrade_xp, 1),
      (quest_get_slot, ":service_xp_start", "qst_freelancer_enlisted", slot_quest_freelancer_start_xp),
      (troop_get_xp, ":player_xp_cur", "trp_player"),
      (store_sub, ":service_xp_cur", ":player_xp_cur", ":service_xp_start"),
      (neg|quest_slot_ge, "qst_freelancer_enlisted", slot_quest_freelancer_upgrade_xp, ":service_xp_cur"),
      (jump_to_menu, "mnu_upgrade_path"),
        (try_end),

        (store_character_level, ":level", "$player_cur_troop"),
        #pays player 10 times the troop level
        (store_mul, ":weekly_pay", 10, ":level"),
        (troop_add_gold, "trp_player", ":weekly_pay"),
        (add_xp_to_troop, 70, "trp_player"),
        (play_sound, "snd_money_received", 0),

        (assign, ":num_food", 0),
        (troop_get_inventory_capacity, ":max_inv_slot", "trp_player"),
        (try_for_range, ":cur_inv_slot", ek_item_0, ":max_inv_slot"),
           (troop_get_inventory_slot, ":cur_item", "trp_player", ":cur_inv_slot"),
           (ge, ":cur_item", 0),
           (is_between, ":cur_item", food_begin, food_end),
           (troop_inventory_slot_get_item_amount, reg0, "trp_player", ":cur_inv_slot"),
       (val_add, ":num_food", reg0),
        (try_end),
        (try_begin),
           (lt, ":num_food", 10),
           (troop_add_item, "trp_player", "itm_bread"),
        (try_end),
    ]),

#  HOURLY CHECKS

    (1,[
        (eq, "$freelancer_state", 1),
        #so that sight and camera follows near commander's party
        (party_is_active, "$enlisted_party"),
        (set_camera_follow_party, "$enlisted_party"),
        (party_relocate_near_party, "p_main_party", "$enlisted_party", 1),
    ]),

  #+freelancer end

 #simple trigger that checks if player has enough renown to start quest or not, as well as place quest starter NPC is specific tavern
  #spawns the unqiue hordes
  (72,
   [
       (call_script, "script_spawn_minor_faction_patrols"),

(try_for_range, ":fac", minor_kingdoms_begin, minor_kingdoms_end), #madsci minor faction king returns home
(faction_slot_eq, ":fac", slot_faction_state, sfs_active),
(faction_get_slot, ":leader", ":fac", slot_faction_leader),
(gt, ":leader", 0),
(neg|troop_slot_eq, ":leader", slot_troop_occupation, dplmc_slto_dead),
(neg|troop_slot_ge, ":leader", slot_troop_prisoner_of_party, 0),
(troop_get_slot, ":party_no", ":leader", slot_troop_leaded_party),
(gt, ":party_no", 0),
(neg|party_is_active, ":party_no"), #this guy had a party but it no longer exists whether destroyed or disbanded
(troop_set_slot, ":leader", slot_troop_leaded_party, -1),
(troop_get_slot, ":home", ":leader", slot_troop_home),
(is_between, ":home", minor_towns_begin, minor_towns_end),
(party_get_num_companion_stacks, ":num_stacks", ":home"),
(gt, ":num_stacks", 0),
(party_stack_get_troop_id, ":party_leader", ":home", 0),
(neg|troop_is_hero, ":party_leader"),
(party_add_leader, ":home", ":leader"),
(try_end),

(try_begin),
(store_num_parties_of_template, ":pirates", "pt_pirates_mediterranean"),
(lt, ":pirates", 3),
(call_script, "script_spawn_pirate"),
(try_end),

(try_begin),
  (store_faction_of_party, ":town_faction","p_town_13"),
  (eq, ":town_faction", "fac_kingdom_1"),
  (store_num_parties_of_template, ":classis", "pt_classis_ravenna"),
  (lt, ":classis", 1),
  (call_script, "script_spawn_naval_patrol_ravenna"),
(try_end),
(try_begin),
  (store_faction_of_party, ":town_faction","p_town_11"),
  (eq, ":town_faction", "fac_kingdom_1"),
  (store_num_parties_of_template, ":classis", "pt_classis_naples"),
  (lt, ":classis", 1),
  (call_script, "script_spawn_naval_patrol_naples"),
(try_end),
(try_begin),
  (store_faction_of_party, ":town_faction","p_town_6"),
  (eq, ":town_faction", "fac_kingdom_2"),
  (store_num_parties_of_template, ":classis", "pt_classis_constantinople"),
  (lt, ":classis", 1),
  (call_script, "script_spawn_naval_patrol_constantinople"),
(try_end),

	(try_for_range, ":center_no", walled_centers_begin, walled_centers_end), #madsci dont let commoners own centers
	(store_faction_of_party, ":center_faction", ":center_no"),
	(this_or_next|eq, ":center_faction", "fac_manhunters"),
	(eq, ":center_faction", "fac_commoners"),
	(party_slot_eq, ":center_no", slot_center_is_besieged_by, -1),
 	(set_spawn_radius, 0),
	(spawn_around_party, ":center_no", "pt_rebel_army"),
	(assign, ":rebel_army", reg0),
	(party_set_name, ":rebel_army", "@Rioting Citizens"),
	(party_set_slot, ":rebel_army", slot_party_home_center, ":center_no"),
	(party_add_members, ":rebel_army", "trp_bandit", 300),
	(party_add_members, ":rebel_army", "trp_brigand", 300),
	(party_set_faction, ":rebel_army", "fac_outlaws"),
	(party_ignore_player, ":rebel_army", 1),
	(party_set_ai_behavior, ":rebel_army", ai_bhvr_attack_party),
	(party_set_ai_object, ":rebel_army", ":center_no"),
	(party_set_flags, ":rebel_army", pf_default_behavior, 1),
	(party_set_slot, ":rebel_army", slot_party_ai_substate, 1),
	(party_set_slot, ":center_no", slot_center_is_besieged_by, ":rebel_army"),
	(store_current_hours, ":cur_hours"),
	(party_set_slot, ":center_no", slot_center_siege_begin_hours, ":cur_hours"),
	(call_script, "script_village_set_state", ":center_no", svs_under_siege),
	(try_end),

    ]),

  (168,
   [
(call_script, "script_spawn_merc_company"),
(call_script, "script_refresh_center_inventories"),
(call_script, "script_refresh_center_armories"),
(call_script, "script_refresh_center_weaponsmiths"),
(call_script, "script_refresh_center_stables"),

(try_begin), #armenian rebellion if the player is not involved
(eq, "$armenian_rebellion", 0),
(gt, "$total_days_passed", 90),
(faction_slot_eq, "fac_kingdom_31", slot_faction_state, sfs_inactive),
(this_or_next|eq, "$g_king_start", 6),
(faction_slot_eq, "fac_kingdom_6", slot_faction_state, sfs_active),
(party_slot_eq, "p_town_45", slot_center_is_besieged_by, -1), #center not under siege
(neg|party_slot_eq, "p_town_45", slot_town_lord, "trp_player"), #center does not belong to player.
(store_faction_of_party, ":party_faction", "p_town_45"), #dvin
(assign, ":player_persia", 0),
	(try_begin),
	(eq, "$g_king_start", 6),
	(eq, ":party_faction", "fac_player_supporters_faction"),
	(assign, ":player_persia", 1),
	(try_end),
(this_or_next|eq, ":player_persia", 1),
(eq, ":party_faction", "fac_kingdom_6"),
#(party_get_slot, ":prosperity", "p_town_45", slot_town_prosperity),
#(gt, ":prosperity", 80),
(store_random_in_range, ":rng", 0, 15),
(eq, ":rng", 1),
(assign, "$armenian_rebellion", -1),
      	(try_for_range, ":troop_2", heroes_begin, heroes_end),
        (troop_slot_eq, ":troop_2", slot_troop_occupation, slto_kingdom_hero),
        (troop_get_slot, ":led_party_2", ":troop_2", slot_troop_leaded_party),
	(gt, ":led_party_2", 0),
	(party_is_active, ":led_party_2"),
        (party_get_attached_to, ":led_party_2_attached", ":led_party_2"),
	(eq, ":led_party_2_attached", "p_town_45"),
	(party_detach, ":led_party_2"),
	(call_script, "script_party_set_ai_state", ":led_party_2",  spai_patrolling_around_center, "p_town_45"),
	(try_end),
(call_script, "script_remove_hero_prisoners", "p_town_45"),
(party_clear, "p_town_45"),
(party_set_slot, "p_town_45", slot_center_religion, slot_religion_christian_miaphysite),
(party_set_slot, "p_town_45", slot_center_culture, "fac_culture_17"),
(faction_set_slot, "fac_kingdom_31", slot_faction_state, sfs_active),
(troop_set_slot, "trp_kingdom_31_lord", slot_troop_occupation, slto_kingdom_hero),
(troop_set_note_available, "trp_kingdom_31_lord", 1),
(troop_set_slot, "trp_tiridates", slot_troop_occupation, slto_kingdom_hero),
(troop_set_note_available, "trp_tiridates", 1),
(troop_set_slot, "trp_kingdom_31_lady_1", slot_troop_occupation, slto_kingdom_lady),
(troop_set_note_available, "trp_kingdom_31_lady_1", 1),
(troop_set_slot, "trp_kingdom_31_lady_2", slot_troop_occupation, slto_kingdom_lady),
(troop_set_note_available, "trp_kingdom_31_lady_2", 1),
(troop_set_slot, "trp_armenag_artsruni", slot_troop_occupation, slto_kingdom_hero),
(troop_set_note_available, "trp_armenag_artsruni", 1),
(troop_set_slot, "trp_kingdom_31_lady_3", slot_troop_occupation, slto_kingdom_lady),
(troop_set_note_available, "trp_kingdom_31_lady_3", 1),
(troop_set_slot, "trp_kingdom_31_lady_4", slot_troop_occupation, slto_kingdom_lady),
(troop_set_note_available, "trp_kingdom_31_lady_4", 1),
(troop_set_slot, "trp_armenian_lord_1", slot_troop_occupation, slto_kingdom_hero),
(troop_set_note_available, "trp_armenian_lord_1", 1),
(troop_set_slot, "trp_armenian_lord_2", slot_troop_occupation, slto_kingdom_hero),
(troop_set_note_available, "trp_armenian_lord_2", 1),
(call_script, "script_give_center_to_faction", "p_town_45", "fac_kingdom_31"),
	(try_begin),
	(troop_get_slot, ":leaded_party", "trp_kingdom_31_lord", slot_troop_leaded_party),
	(this_or_next|le, ":leaded_party", 0),
	(neg|party_is_active, ":leaded_party"),
	(call_script, "script_create_kingdom_hero_party", "trp_kingdom_31_lord", "p_town_45"),
	(try_end),
(faction_set_note_available, "fac_kingdom_31", 1),
	(try_for_range, ":unused", 0, 20),
	(party_add_template, "p_town_45", "pt_kingdom_17_reinforcements_a"),
	(try_end),
(str_store_party_name_link, s10, "p_town_45"),
(display_log_message, "@The Armenians have established a new kingdom in {s10}!"),
(call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_31", ":party_faction", 0),
	(try_begin),
	(store_faction_of_party, ":castle_faction", "p_castle_48"),
	(eq, ":castle_faction", ":party_faction"),
	(party_slot_eq, "p_castle_48", slot_center_is_besieged_by, -1), #center not under siege
	(neg|party_slot_eq, "p_castle_48", slot_town_lord, "trp_player"), #center does not belong to player.
	(call_script, "script_give_center_to_faction", "p_castle_48", "fac_kingdom_31"),
	(try_end),
	(try_begin),
	(store_faction_of_party, ":castle_faction", "p_castle_54"),
	(eq, ":castle_faction", ":party_faction"),
	(party_slot_eq, "p_castle_54", slot_center_is_besieged_by, -1), #center not under siege
	(neg|party_slot_eq, "p_castle_54", slot_town_lord, "trp_player"), #center does not belong to player.
	(call_script, "script_give_center_to_faction", "p_castle_54", "fac_kingdom_31"),
	(try_end),
(set_spawn_radius, 1),
	(try_for_range, ":unused", 0, 10), #spawn little helpers
	(spawn_around_party, "p_town_45", "pt_patrol_party"),
	(party_set_faction, reg0, "fac_kingdom_31"),
	(party_add_template, reg0, "pt_kingdom_17_reinforcements_b"),
	(party_add_template, reg0, "pt_kingdom_17_reinforcements_a"),
	(party_add_template, reg0, "pt_kingdom_17_reinforcements_a"),
	(party_add_template, reg0, "pt_kingdom_17_reinforcements_a"),
	(party_set_name, reg0, "@Armenians"),
	(try_end),
	(try_begin),
	(eq, "$g_infinite_camping", 0),
	(assign, "$temp", "p_town_45"),
	(jump_to_menu, "mnu_armenian_uprising_no_player"),
	(try_end),
(try_end),

	(try_begin), #jewish rebellion if player isnt involved
	(eq, "$jewish_rebellion", 0),
	(gt, "$total_days_passed", 250),
	(party_slot_eq, "p_town_22", slot_center_is_besieged_by, -1),
	(store_faction_of_party, ":faction", "p_town_22"),
	(this_or_next|eq, ":faction", "fac_kingdom_2"),
	(eq, ":faction", "fac_kingdom_1"),
	(set_relation, "fac_samaritan_rebels", ":faction", -50),
		(try_begin),
		(neq, ":faction", "$players_kingdom"),
		(this_or_next|troop_slot_eq, "trp_player", slot_troop_culture, "fac_culture_18"),
		(troop_slot_eq, "trp_player", slot_troop_religion, slot_religion_judaism),
		(call_script, "script_set_player_relation_with_faction", "fac_samaritan_rebels", 0),
		(else_try),
		(eq, ":faction", "$players_kingdom"),
		(call_script, "script_set_player_relation_with_faction", "fac_samaritan_rebels", -50),
		(try_end),
 	(set_spawn_radius, 0),
	(spawn_around_party, "p_town_22", "pt_rebel_army"),
	(assign, ":rebel_army", reg0),
	(party_set_slot, ":rebel_army", slot_party_home_center, "p_town_22"),
	(party_add_members, ":rebel_army", "trp_samaritan_rebel", 300),
	(party_add_members, ":rebel_army", "trp_samaritan_zealot", 300),
	(party_add_members, ":rebel_army", "trp_jewish_levy", 300),
	(party_add_leader, ":rebel_army", "trp_jewish_agitator"),
	(party_set_faction, ":rebel_army", "fac_samaritan_rebels"),
	(party_ignore_player, ":rebel_army", 1),
	(party_set_ai_behavior, ":rebel_army", ai_bhvr_attack_party),
	(party_set_ai_object, ":rebel_army", "p_town_22"),
	(party_set_flags, ":rebel_army", pf_default_behavior, 1),
	(party_set_slot, ":rebel_army", slot_party_ai_substate, 1),
	(party_set_slot, "p_town_22", slot_center_is_besieged_by, ":rebel_army"),
	(store_current_hours, ":cur_hours"),
	(party_set_slot, "p_town_22", slot_center_siege_begin_hours, ":cur_hours"),
	(call_script, "script_village_set_state", "p_town_22", svs_under_siege),
	(assign, "$jewish_rebellion", -1),
	(str_store_party_name, s10, "p_town_22"),
	(display_message, "@A major rebellion has erupted in {s10}!"),
	(faction_set_note_available, "fac_samaritan_rebels", 1),
		(try_begin),
        	(eq, "$g_infinite_camping", 0),
		(assign, "$g_notification_menu_var1", "p_town_22"),
		(jump_to_menu, "mnu_jewish_rebellion_launched"),
		(try_end),
	(try_end),

#FOEDERATI REBELS
(try_begin),
(eq, "$g_foederati_event", 0),
(gt, "$total_days_passed", 100),
(set_spawn_radius, 8),
  	(try_for_range, ":unused", 2, 5),
	(spawn_around_party, "p_town_13", "pt_foederati_rebels"),
  	(try_end),
(spawn_around_party, "p_town_13", "pt_tuldila_rebels"),
	(try_begin),
	(eq, "$g_infinite_camping", 0),
	(neg|party_slot_eq, "p_main_party", slot_party_on_water, 1), #madsci a messenger doesnt appear if the player is sea traveling
  	(dialog_box, "@Foederati hired by Majorian for his campaigns have begun to pillage the Italian countryside!", "@A messenger approaches your warband"),
	(try_end),
(display_log_message, "@Foederati hired by Majorian for his campaigns have begun to pillage the Italian countryside!"),
(assign, "$g_foederati_event", 1),
(try_end),

#ARRAN REVOLT
(try_begin),
(neq,"$g_arran_revolt",1),
(gt, "$total_days_passed", 75),
(faction_slot_eq, "fac_kingdom_6", slot_faction_state, sfs_active),
(party_slot_eq, "p_castle_36", slot_center_is_besieged_by, -1),
(party_slot_eq, "p_castle_87", slot_center_is_besieged_by, -1),
(party_slot_eq, "p_castle_88", slot_center_is_besieged_by, -1),
(store_faction_of_party, ":fac", "p_castle_36"),
(neq, ":fac", "fac_kingdom_28"),
(party_get_slot, ":lord", "p_castle_36", slot_town_lord),
(ge, ":lord", 1),
(call_script, "script_cf_start_arran_revolt"),
(display_log_message, "@The king of Arran has raised his armies and is now challenging the Shahanshah in order to contest his authority."),
	(try_begin),
	(eq, "$g_infinite_camping", 0),
	(call_script, "script_add_notification_menu", "mnu_event_arran_revolt",0,0),
	(try_end),
(try_end),

#COPTIC REBELLION IN ALEXANDRIA
(try_begin),
(gt, "$total_days_passed", 200),
(party_slot_eq, "p_town_21", slot_center_is_besieged_by, -1),
(party_slot_eq,  "p_town_21", slot_town_lord, "trp_knight_2_4"), # belongs to a specific lord
(store_faction_of_party, ":party_faction", "p_town_21"),
(neq, ":party_faction", "fac_coptic_rebels"),
(set_relation, "fac_coptic_rebels", ":party_faction", -50),
(set_spawn_radius, 8),
	(try_for_range, ":unused", 1, 6),
	(spawn_around_party, "p_town_21", "pt_coptic_rebellion"),
	(try_end),
	(try_begin),
	(eq, "$g_infinite_camping", 0),
	(neg|party_slot_eq, "p_main_party", slot_party_on_water, 1), #madsci a messenger doesnt appear if the player is sea traveling
     	(dialog_box, "@A messenger approaches your warband, bringing news of rebellion! It appears that a large number of Anti-Chalcedonian Christians have revolted near Alexandria, killing the local patriarch, Proterius! The current Comes Limits Aegypti has been removed from his position, and has been replaced on orders from the Emperor.", "@A messenger approaches your warband"),
	(try_end),
(display_log_message, "@Anti-Chalcedonian Christians have revolted near Alexandria, killing the local patriarch, Proterius!"),
(troop_set_slot, "trp_knight_2_4", slot_troop_military_title, 0),
(party_set_slot, "p_town_21", slot_town_lord, -1),
	(try_begin),
	(troop_slot_eq, "trp_knight_2_12", slot_troop_occupation, slto_kingdom_hero),
	(store_troop_faction, ":troop_faction", "trp_knight_2_12"),
	(eq, ":troop_faction", ":party_faction"),
        (call_script, "script_give_center_to_lord", "p_town_21", "trp_knight_2_12", 0), #switch it to other shit lord
        (troop_set_slot, "trp_knight_2_12", slot_troop_military_title, mt_egypt), #new comes aegyptus
	(else_try),
	(assign, ":other_guy", 0), #choose someone else if the previous guys isnt available for some reason
		(try_for_range_backwards, ":other_npc", lords_begin, heroes_end),
		(eq, ":other_guy", 0),
		(neq, ":other_npc", "trp_knight_2_4"),
		(neg|faction_slot_eq, ":party_faction", slot_faction_leader, ":other_npc"),
		(troop_slot_eq, ":other_npc", slot_troop_occupation, slto_kingdom_hero),
		(troop_slot_eq, ":other_npc", slot_troop_military_title, 0), #no title
		(store_troop_faction, ":other_troop_faction", ":other_npc"),
		(eq, ":other_troop_faction", ":party_faction"),
		(assign, ":other_guy", ":other_npc"),
		(try_end),
	(gt, ":other_guy", 0),
        (call_script, "script_give_center_to_lord", "p_town_21", ":other_guy", 0), #switch it to other shit lord
        (troop_set_slot, ":other_guy", slot_troop_military_title, mt_egypt), #new comes aegyptus
	(try_end),
	(try_begin), #actually send the lord to the town
	(party_get_slot, ":center_lord", "p_town_21", slot_town_lord),
	(gt, ":center_lord", 0),
	(troop_get_slot, ":leaded_party", ":center_lord", slot_troop_leaded_party),
	(gt, ":leaded_party", 0),
	(party_is_active, ":leaded_party"),
	(call_script, "script_party_set_ai_state", ":leaded_party", spai_holding_center, "p_town_21"),
	(try_end),

#spawn actual rebels but very small group to attack the town, just to get the faction to react
 	(set_spawn_radius, 0),
	(spawn_around_party, "p_town_21", "pt_rebel_army"),
	(assign, ":rebel_army", reg0),
	(party_set_slot, ":rebel_army", slot_party_home_center, "p_town_21"),
	(party_add_members, ":rebel_army", "trp_coptic_youth", 100),
	(party_add_members, ":rebel_army", "trp_coptic_footman", 100),
	(party_set_faction, ":rebel_army", "fac_coptic_rebels"),
	(party_ignore_player, ":rebel_army", 1),
	(party_set_ai_behavior, ":rebel_army", ai_bhvr_attack_party),
	(party_set_ai_object, ":rebel_army", "p_town_21"),
	(party_set_flags, ":rebel_army", pf_default_behavior, 1),
	(party_set_slot, ":rebel_army", slot_party_ai_substate, 1),
	(party_set_slot, "p_town_21", slot_center_is_besieged_by, ":rebel_army"),
	(store_current_hours, ":cur_hours"),
	(party_set_slot, "p_town_21", slot_center_siege_begin_hours, ":cur_hours"),
	(call_script, "script_village_set_state", "p_town_21", svs_under_siege),

(assign, "$g_coptic_rebellion_triggered", 1),
(troop_set_note_available, "trp_mia_bishop_alexandria_1", 1),
(add_troop_note_from_sreg, "trp_mia_bishop_alexandria_1", 3, "@Timothy II is the Miaphysite Patriarch of Alexandria.", 0),
(add_troop_note_tableau_mesh, "trp_mia_bishop_alexandria_1", "tableau_troop_note_mesh"),
(troop_set_slot, "trp_chal_bishop_alexandria_1", slot_troop_occupation, dplmc_slto_dead),
(try_end),

(try_begin),
(eq, "$suebi_war_ended", 0),
(faction_slot_eq, "fac_kingdom_8", slot_faction_state, sfs_active),
(faction_slot_eq, "fac_kingdom_30", slot_faction_state, sfs_active),
(faction_get_slot, ":tributary_cur", "fac_kingdom_30", slot_faction_tributary_of),
(neg|is_between, ":tributary_cur", kingdoms_begin, kingdoms_end),
(store_relation, ":reln", "fac_kingdom_8", "fac_kingdom_30"),
(ge, ":reln", 0),
(call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_30", "fac_kingdom_8", 0), #restart the suebi civil war if it ends
(try_end),
    ]),

(24 * 7,
   [
    	(eq, "$g_player_owns_farm", 1),
    	(assign, "$g_earnings", 0), #resets earnings
    	(store_random_in_range, "$g_earnings", 300, 450),
	(party_get_num_prisoners, ":g_num_prisoners", "p_diocletians_palace"),

    		(try_begin),
        	(gt, ":g_num_prisoners", 0),
		(store_mul, ":earnings", 25, ":g_num_prisoners"), #tocan: change this to amount per prisoner you want
		(val_add, "$g_earnings", ":earnings"),
		(assign, reg1, "$g_earnings"),
    		(try_end),

    	(display_message, "@Your farm has made a profit of {reg1} siliquae this week."),
    	(troop_add_gold, "trp_player", "$g_earnings"),
    	(play_sound, "snd_money_received", 0),

		(try_begin), #maybe some escape if too many prisoners
		(party_get_num_prisoner_stacks, ":num_prisoner_stacks", "p_diocletians_palace"),
		(gt, ":num_prisoner_stacks", 0),
		(assign, ":escaped", 0),
			(try_for_range_backwards, ":stack_no", 0, ":num_prisoner_stacks"),
			(party_prisoner_stack_get_troop_id, ":stack_troop", "p_diocletians_palace", ":stack_no"),
				(try_begin),
				(troop_is_hero, ":stack_troop"),
				(call_script, "script_remove_troop_from_prison", ":stack_troop"),
				(party_remove_prisoners, "p_diocletians_palace", ":stack_troop", 1),
				(val_add, ":escaped", 1),
				(else_try),
				(gt, ":g_num_prisoners", 50),
				(party_stack_get_size, ":stack_size", "p_diocletians_palace", ":stack_no"),
				(gt, ":stack_size", 3),
				(store_random_in_range, ":remove", 1, ":stack_size"),
				(val_div, ":remove", 2),
				(party_remove_prisoners, "p_diocletians_palace", ":stack_troop", ":remove"),
				(val_add, ":escaped", ":remove"),
				(try_end),
			(try_end),
		(gt, ":escaped", 0),
		(assign, reg2, ":escaped"),
    		(display_message, "@{reg2} prisoners have escaped from your farm..."),
		(try_end),
    ]),

(24 * 7,
   [
   (eq, "$g_player_owns_villa", 1),
   (assign, "$g_earnings", 0), #resets earnings
   (store_random_in_range, "$g_earnings", 400, 650),
    (display_message, "@Your villa's farm has made a profit of {reg1} siliquae this week"),
    (troop_add_gold, "trp_player", "$g_earnings"),
    (play_sound, "snd_money_received", 0),
    ]),

(24.0*7.0/(number_of_centers),
  [
  #24/380, daily on average
    (store_random_in_range, ":center_no", centers_begin, centers_end),

    (party_slot_ge, ":center_no", slot_center_has_temple, 1),

    (store_random_in_range, ":prosperity_boost", 0, 3),
    (call_script, "script_change_center_prosperity", ":center_no", ":prosperity_boost"),
  ]),

  (24.0*3.0/(number_of_centers), #checks every (4) days - making sure that relations do not decrease at an insane rate
    [
    #(24*4)/380, as we have roughly 380 centers

    (store_random_in_range, ":center_no", centers_begin, centers_end),
#Nero: make it assynchron
      #player center
      #(try_for_range, ":center_no", centers_begin, centers_end),
        (troop_get_slot, ":religion_player","trp_player", slot_troop_religion),
        (party_get_slot, ":religion_original", ":center_no", slot_center_religion),
        (try_begin), #checks the player's religion and the center's religion. If they are the same, positive relations add, if opposite then negative
          (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
          (party_get_slot, ":cur_relation", ":center_no", slot_center_player_relation),
            (try_begin),
              (eq, ":religion_player", ":religion_original"),
              (store_random_in_range, ":rand", 0,3),
              (val_add, ":cur_relation", ":rand"),
            (else_try),
              (neq, ":religion_player",":religion_original"),
              (store_random_in_range, ":rand", -3,0),
              (val_add, ":cur_relation", ":rand"),
            (try_end),
        (try_end),
     # (try_end),
    ]),

(108, #resets locations from being sacked
  [
  (try_for_range, ":center_no", religious_sites_begin, religious_sites_end),
    (party_slot_eq, ":center_no", slot_party_been_sacked, 1),
    (party_set_slot, ":center_no", slot_party_been_sacked, 0),
(party_set_extra_text, ":center_no", "str_empty_string"), #clear extra text
  (try_end),
]),

(168, #resets locations from being sacked
  [
  (try_for_range, ":center_no", minor_towns_begin, minor_towns_end),
    	(party_slot_eq, ":center_no", slot_party_been_sacked, 1),
    	(party_set_slot, ":center_no", slot_party_been_sacked, 0),
	(party_set_extra_text, ":center_no", "str_empty_string"), #clear extra text
	(store_faction_of_party, ":fac", ":center_no"),
		(try_begin),
		(neq, ":fac", "fac_neutral"),
   		(faction_get_slot, ":template", ":fac", slot_faction_reinforcements_a),
   		(gt, ":template", 0),
   		(party_add_template, ":center_no", ":template"),
		(else_try),
		(neq, ":fac", "fac_neutral"),
		(party_add_members, ":center_no", "trp_manhunter", 45), #madsci failsafe if no valid template is found
		(try_end),
  (try_end),
]),

(24*7, #increases garrison
  [
(try_for_range, ":party", minor_towns_begin, minor_towns_end),
   (neg|party_slot_eq, ":party", slot_party_been_sacked, 1),
   (store_party_size_wo_prisoners, ":garrison", ":party"),
   (lt, ":garrison", 400),
   (store_faction_of_party, ":fac", ":party"),
   (neq, ":fac", "fac_neutral"),
	(try_begin),
   	(faction_get_slot, ":template", ":fac", slot_faction_reinforcements_a),
   	(gt, ":template", 0),
   	(party_add_template, ":party", ":template"),
	(else_try),
	(party_add_members, ":party", "trp_manhunter", 45), #madsci failsafe if no valid template is found
	(try_end),
   (party_set_slot, ":party", slot_center_volunteer_troop_type, -1),
(try_end),
]),

(24,
  [ #checks if player has hired sidonius to write about him/her
        (troop_get_slot,":val","trp_sidonius_apollinaris",slot_troop_days_on_mission),
        (neq,":val",0),
        (val_sub,":val",1),
        (val_max,":val",0),
        (troop_set_slot,"trp_sidonius_apollinaris",slot_troop_days_on_mission,":val"),
        (try_begin),
          (eq, ":val", 0),
          (troop_slot_eq, "trp_sidonius_apollinaris", slot_troop_current_mission, npc_mission_seek_recognition),
          (display_message, "@Sidonius Apollinaris's panegyric about you seems to be spreading throughout the land."),
          (tutorial_box, "@Sidonius Apollinaris's panegyric about you semes to be spreading throughout the land.", "@Fame spreads"),
          (call_script, "script_change_troop_renown", "trp_player", 30),
        (try_end),
  ]),

(24*2, [
#(eq, "$g_tributary_ai", 1),
#(try_for_range, ":faction_a", npc_kingdoms_begin, npc_kingdoms_end),
(store_random_in_range, ":faction_a", npc_kingdoms_begin, npc_kingdoms_end),
(try_begin),
  (faction_slot_eq, ":faction_a", slot_faction_state, sfs_active),#active
  #barbarian
  #(neg|faction_slot_eq, ":faction_a", slot_faction_culture, "fac_culture_7"),#not Roman
  (faction_get_slot, ":num_towns", ":faction_a", slot_faction_num_castles),
  (faction_get_slot, ":num_castles_a", ":faction_a", slot_faction_num_towns),
  (val_add, ":num_castles_a", ":num_towns"),
  (is_between, ":num_castles_a", 1, 4),#between 1 and 3 towns or castles (e.g. Quadi at game start)
  #get a true winner
  (assign, ":winner", -1),
  (assign, ":winner_score", -1),
  (assign, ":num_of_wars", 0),
  (assign, ":num_of_allies", 0),
  (try_for_range, ":faction_b", kingdoms_begin, npc_kingdoms_end),
    (faction_slot_eq, ":faction_b", slot_faction_state, sfs_active),#active
    (store_relation, ":relation", ":faction_a", ":faction_b"),
    (try_begin),##count allies
      (ge, ":relation", 0),#they are at peace
      (store_add, ":truce_slot", ":faction_a", slot_faction_truce_days_with_factions_begin),
      (val_sub, ":truce_slot", kingdoms_begin),
      (faction_get_slot, ":truce_days", ":faction_b", ":truce_slot"),

      (gt, ":truce_days", dplmc_treaty_defense_days_expire),
      (val_add, ":num_of_allies", 1),
    (try_end),

    (lt, ":relation", -1),#they are at war

    #(neg|faction_slot_eq, ":faction_b", slot_faction_culture, "fac_culture_7"),#not allowed for Romans
    (store_add, ":slot_war_damage_inflicted_on_a", ":faction_a", slot_faction_war_damage_inflicted_on_factions_begin),
    (val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
    (faction_get_slot, ":war_damage_inflicted_by_b", ":faction_b", ":slot_war_damage_inflicted_on_a"),

    (store_add, ":slot_war_damage_inflicted_on_b", ":faction_b", slot_faction_war_damage_inflicted_on_factions_begin),
    (val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
    (faction_get_slot, ":war_damage_inflicted_by_a", ":faction_a", ":slot_war_damage_inflicted_on_b"),

    (try_begin),#num of wars losing
      (gt, ":war_damage_inflicted_by_b", ":war_damage_inflicted_by_a"),
      (val_add, ":num_of_wars", 1),
    (try_end),

    (try_begin),
      (ge, "$cheat_mode", 1),
      (assign, reg33, ":war_damage_inflicted_by_b"),
      (assign, reg34, ":war_damage_inflicted_by_a"),
      (str_store_faction_name, s1, ":faction_a"),
      (str_store_faction_name, s2, ":faction_b"),
      #(display_message, "@war_damage_inflicted_by_b: {reg33} ({s2}) war_damage_inflicted_by_a: {reg34} ({s1})"),
    (try_end),
    (val_mul, ":war_damage_inflicted_by_a", 2),

    (faction_get_slot, ":num_towns", ":faction_b", slot_faction_num_castles),
    (faction_get_slot, ":num_castles_b", ":faction_b", slot_faction_num_towns),
    (val_add, ":num_castles_b", ":num_towns"),
    (gt, ":num_castles_b", ":num_castles_a"),#to avoid that a small nation vassalizes a large one

    (gt, ":war_damage_inflicted_by_b", ":war_damage_inflicted_by_a"),
    (gt, ":war_damage_inflicted_by_b", ":winner_score"),
    (assign, ":winner_score", ":war_damage_inflicted_by_b"),
    (assign, ":winner", ":faction_b"),
  (try_end),
  (val_mul, ":num_castles_a", 30),
  (val_mul, ":num_of_allies", 30),
  (store_mul, ":num_of_wars_effect", ":num_of_wars", 30),
  (store_sub, ":threshold", 300, ":num_of_wars_effect"),
  (val_add, ":threshold", ":num_castles_a"),
  (val_add, ":threshold", ":num_of_allies"),

  (try_begin),##debug information
    (ge, "$cheat_mode", 1),
    (assign, reg33, ":threshold"),
    (assign, reg34, ":num_castles_a"),
    (assign, reg35, ":num_of_allies"),
    (assign, reg36, ":num_of_wars"),
    (str_store_faction_name, s1, ":faction_a"),
    (try_begin),
      (gt, ":winner", -1),
      (str_store_faction_name, s3, ":winner"),
      (assign, reg37, ":winner_score"),
    (else_try),
      (str_store_string, s3, "str_dplmc_none"),
      (assign, reg37, ":winner_score"),
    (try_end),
    #(display_message, "@faction_a: {s1}, threshold: {reg33}, num_castles_a: {reg34}, num_of_allies: {reg35}. num_of_wars: {reg36}, winner: {s3}, winner_score: {reg37}"),
  (try_end),

  (try_begin),
    (ge, ":num_of_wars", 1),#at least one wars
    (try_begin),
      (ge, ":winner", npc_kingdoms_begin),
      (gt, ":winner_score", ":threshold"),
      (call_script, "script_dplmc_start_tributary_between_kingdoms", ":faction_a", ":winner", 1),
    (else_try),
      (eq, ":winner", "fac_player_supporters_faction"),
      (call_script, "script_add_notification_menu", "mnu_notification_tributary_offer", ":faction_a", 0),
    (try_end),
  (try_end),
(try_end),

]),

  # Masterless men AI (107)
  # JuJu70
  (1,
    [(try_for_parties, ":party_no"),
      (gt, ":party_no", last_static_party), #madsci
        (store_faction_of_party, ":faction", ":party_no"),
        (eq, ":faction", "fac_deserters"),
        (assign, ":closest_village", -1), #phaiak try fix
        (get_party_ai_behavior, ":ai_bhvr", ":party_no"),
        (party_get_slot, ":ai_behavior", ":party_no", slot_party_ai_state),
        (try_begin),
          (this_or_next|eq, ":ai_bhvr", ai_bhvr_travel_to_party),
          (eq, ":ai_bhvr", ai_bhvr_travel_to_point),
          (neq, ":ai_behavior", 0),
          (get_party_ai_object,":p_target",":party_no"),
          (gt, ":p_target", 0),
          (try_begin),
            (party_slot_eq, ":p_target", slot_party_type, spt_village),
            (store_distance_to_party_from_party, ":distance_from_target", ":party_no", ":p_target"),
            (try_begin),
              (lt, ":distance_from_target", 2),
              (party_set_slot, ":party_no", slot_party_ai_state ,spai_raiding_around_center),
              (party_set_ai_object, ":party_no", ":p_target"),
              (try_begin),
                (party_slot_eq, ":p_target", slot_village_state, svs_normal),
                (call_script, "script_village_set_state", ":p_target", svs_being_raided), #possible cause for VC-2085 but p_target = spt_village so it should be ok...
                (party_set_slot, ":p_target", slot_village_raided_by, ":party_no"),
                (try_begin),
                  (store_faction_of_party, ":village_faction", ":p_target"),
                  (this_or_next|party_slot_eq, ":p_target", slot_town_lord, "trp_player"),
                  (eq, ":village_faction", "fac_player_supporters_faction"),
                  (store_distance_to_party_from_party, ":dist", "p_main_party", ":p_target"),
                  (this_or_next|lt, ":dist", 30),
                  (party_slot_eq, ":p_target", slot_center_has_messenger_post, 1),

                  (try_begin),
                    (call_script, "script_add_notification_menu", "mnu_notification_village_raid_started", ":p_target", ":faction"),
                  (else_try),
                    (str_store_party_name, s10, ":p_target"),
                    (display_message, "@Village {s10} is under attack!", 0xFF0000),
                  (try_end),

                (try_end),
              (else_try),
                (party_slot_eq, ":p_target", slot_village_state, svs_being_raided),
              (else_try),
                (party_set_slot, ":party_no", slot_party_ai_substate, 0),
                (party_get_position, pos0,  ":party_no"),
                (party_set_ai_behavior, ":party_no", ai_bhvr_patrol_location),
                (party_set_ai_patrol_radius, ":party_no", 30),
                (party_set_ai_target_position, ":party_no", pos0),
                (party_set_slot, ":party_no", slot_party_ai_state, spai_patrolling_around_center),
              (try_end),
            (else_try),
              (party_get_position, pos1, ":p_target"),
              (map_get_random_position_around_position, pos2, pos1, 1),
              (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_point),
              (party_set_ai_target_position, ":party_no", pos2),
              (party_set_ai_object, ":party_no", ":p_target"),
              (party_set_slot, ":party_no", slot_party_ai_object, ":p_target"),
              (party_set_slot, ":party_no", slot_party_ai_state, spai_patrolling_around_center),
            (try_end),
          (else_try),
            (party_slot_eq, ":p_target", slot_party_type, spt_kingdom_hero_party),
            (neq, ":p_target", "p_main_party"),
            (store_distance_to_party_from_party, ":distance_from_target", ":party_no", ":p_target"),
            (try_begin),
              (lt, ":distance_from_target", 2),
              (party_set_slot, ":party_no", slot_party_ai_state ,spai_engaging_army),
              (party_set_ai_object, ":party_no", ":p_target"),
              (party_set_ai_behavior, ":party_no", ai_bhvr_attack_party),
            (else_try),
              (party_get_position, pos1, ":p_target"),
              (map_get_random_position_around_position, pos2, pos1, 1),
              (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_point),
              (party_set_ai_target_position, ":party_no", pos2),
              (party_set_ai_object, ":party_no", ":p_target"),
              (party_set_slot, ":party_no", slot_party_ai_object, ":p_target"),
              (party_set_slot, ":party_no", slot_party_ai_state, spai_engaging_army),
            (try_end),
          (else_try),
            (party_get_position, pos0,  ":party_no"),
            (party_set_ai_behavior, ":party_no", ai_bhvr_patrol_location),
            (party_set_ai_patrol_radius, ":party_no", 30),
            (party_set_ai_target_position, ":party_no", pos0),
            (party_set_slot, ":party_no", slot_party_ai_state, spai_patrolling_around_center),
          (try_end),
        (else_try),
          (store_party_size_wo_prisoners,":size", ":party_no"),
          (try_begin),
            (ge, ":size", 50),
            (store_random_in_range, ":rand", 0, 1000),
            (try_begin),
              (lt, ":rand", 50),
              (assign, ":minimum_distance", 40),
              (assign, ":closest_village", -1),
              (try_for_range, ":village_no", villages_begin, villages_end),
                (store_distance_to_party_from_party, ":dist", ":party_no",":village_no"),
                (lt, ":dist", ":minimum_distance"),
                (neg|party_slot_eq, ":village_no", slot_village_state, svs_looted),
                (neg|party_slot_eq, ":village_no", slot_village_state, svs_being_raided),
                (neg|party_slot_ge, ":village_no", slot_village_infested_by_bandits, 1),
                (assign, ":minimum_distance", ":dist"),
                (assign, ":closest_village", ":village_no"),
              (try_end),
            (try_end),
            (gt, ":closest_village", 0),
            (party_get_position, pos1, ":closest_village"),
            (map_get_random_position_around_position, pos2, pos1, 1),
            (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_point),
            (party_set_ai_target_position, ":party_no", pos2),
            (party_set_ai_object, ":party_no", ":closest_village"),
            (party_set_slot, ":party_no", slot_party_ai_object, ":closest_village"),
          (else_try),
            (party_get_position, pos0,  ":party_no"),
            (party_set_ai_behavior, ":party_no", ai_bhvr_patrol_location),
            (party_set_ai_patrol_radius, ":party_no", 30),
            (party_set_ai_target_position, ":party_no", pos0),
            (party_set_slot, ":party_no", slot_party_ai_state, spai_patrolling_around_center),
          (try_end),
        (try_end),
      (try_end),
  ]),

(24, [ #checks if Rome has fallen
    (party_get_slot, ":faction", "p_town_8", slot_center_original_faction),
    (store_faction_of_party, ":cur_faction", "p_town_8"),
    (neq, ":cur_faction", ":faction"),
    #(dialog_box, "@Once again this century, the great city of Rome has fallen. ", "@A messenger approaches your warband"),
    (call_script, "script_add_notification_menu", "mnu_rome_conquered", ":cur_faction", 0),
    (party_set_slot, "p_town_8", slot_center_original_faction, ":cur_faction"),
    ]),

(24, [ #checks if constantinople has been taken
    (party_get_slot, ":faction", "p_town_6", slot_center_original_faction),
    (store_faction_of_party, ":cur_faction", "p_town_6"),
    (neq, ":cur_faction", ":faction"),
    (call_script, "script_add_notification_menu", "mnu_constantinople_conquered", ":cur_faction", 0),
    (party_set_slot, "p_town_6", slot_center_original_faction, ":cur_faction"),
    ]),

(24, [ #checks if ctesiphon has been taken
    (party_get_slot, ":faction", "p_town_19", slot_center_original_faction),
    (store_faction_of_party, ":cur_faction", "p_town_19"),
    (neq, ":cur_faction", ":faction"),
    (call_script, "script_add_notification_menu", "mnu_ctesiphon_conquered", ":cur_faction", 0),
    (party_set_slot, "p_town_19", slot_center_original_faction, ":cur_faction"),
    ]),

  #random events
  (24 * 4, #every 4 days - 50% chance of an event
    [
	(map_free),
	(eq, "$freelancer_state", 0), #not freelancing
	(eq, "$g_infinite_camping", 0),
	(neq, "$g_player_is_captive", 1),
	(party_get_current_terrain, ":terrain", "p_main_party"),
	(neq, ":terrain", rt_river),
	(neq, ":terrain", rt_water),
	(neq, ":terrain", rt_deep_water),
	(store_random_in_range, ":rnd", 0, 5),
	(eq, ":rnd", 1),

      (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
      (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
      (assign, ":num_men", 0),
      (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
        (val_add, ":num_men", ":stack_size"),
      (try_end),

      (try_begin),
        (ge, ":player_renown", 200),
        (gt, ":num_men", 30),
        (store_random_in_range, ":rand", 0, 44), #50% chance to get an event
        (try_begin),
          (eq, ":rand", 0),
          (party_get_current_terrain, ":terrain", "p_main_party"), #cannot happen in the desert
          (neq, ":terrain", rt_desert),
          (neq, ":terrain", rt_desert_forest),
          (jump_to_menu,"mnu_event_01"),
        (else_try),
          (eq, ":rand", 1),
          (jump_to_menu,"mnu_event_02"),
        (else_try),
          (eq, ":rand", 2),
          (party_get_current_terrain, ":terrain", "p_main_party"), #cannot happen in the desert
          (neq, ":terrain", rt_desert),
          (neq, ":terrain", rt_desert_forest),
	(troops_can_join, 3), #madsci
          (jump_to_menu,"mnu_event_03"),
        (else_try),
          (eq, ":rand", 3),
          (jump_to_menu,"mnu_event_04"),
        (else_try),
          (eq, ":rand", 4),
          (jump_to_menu,"mnu_event_05"),
        (else_try),
          (eq, ":rand", 5),
          (jump_to_menu,"mnu_event_06"),
        (else_try),
          (eq, ":rand", 6),
          (jump_to_menu,"mnu_event_07"),
        (else_try),
          (eq, ":rand", 7),
          (jump_to_menu,"mnu_event_08"),
        (else_try),
          (eq, ":rand", 8),
          (jump_to_menu,"mnu_event_09"),
        (else_try),
          (eq, ":rand", 9),
          #(is_between, "$g_cur_month", 6, 10),#harvest season
          (party_get_current_terrain, ":terrain", "p_main_party"), #cannot happen in the desert
          (neq, ":terrain", rt_desert),
          (neq, ":terrain", rt_desert_forest),
          (jump_to_menu,"mnu_event_10"),
        (else_try),
          (eq, ":rand", 10),
          (jump_to_menu,"mnu_event_11"),
        (else_try),
          (eq, ":rand", 11),
          (jump_to_menu,"mnu_event_12"),
        (else_try),
          (eq, ":rand", 12),
          (jump_to_menu,"mnu_event_13"),
        (else_try),
          (eq, ":rand", 13),
          (party_get_current_terrain, ":terrain", "p_main_party"), #cannot happen in the desert
          (neq, ":terrain", rt_desert),
          (neq, ":terrain", rt_desert_forest),
          (jump_to_menu,"mnu_event_14"),
        (else_try),
          (eq, ":rand", 14),
	(troops_can_join, 6), #madsci
          (jump_to_menu,"mnu_event_15"),
        (else_try),
          (eq, ":rand", 15),
          (jump_to_menu,"mnu_event_16"),
        (else_try),
          (eq, ":rand", 16),
          (jump_to_menu,"mnu_event_17"),
        (else_try),
          (eq, ":rand", 17),
          (jump_to_menu,"mnu_event_18"),
        (else_try),
          (eq, ":rand", 18),
          (jump_to_menu,"mnu_event_19"),
        (else_try),
          (eq, ":rand", 19),
          (jump_to_menu,"mnu_event_20"),
        (else_try),
          (eq, ":rand", 20),
	(troops_can_join, 3), #madsci
          (jump_to_menu,"mnu_event_21"),
        (else_try),
          (eq, ":rand", 21),
          (eq, "$g_unique_event_1", 0),
          (jump_to_menu,"mnu_event_pilos_1"),
        (else_try),
          (eq, ":rand", 22),
          (eq, "$g_unique_event_2", 0),
          (jump_to_menu,"mnu_event_aurelian_1"),
        (else_try),
          (display_message,"@ "),
        (try_end),
      (try_end),
  ]),

(60,[
    (eq, "$g_empieza_asedio", 1),
    (neq, "$g_siege_saneamiento", 2),
    (neq, "$g_player_is_captive", 1),
    (neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
    (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
    (assign, ":num_men", 0),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
        (val_add, ":num_men", ":stack_size"),
    (try_end),
    (gt, ":num_men", 30),
    (store_random_in_range, ":rand", 0, 6),
    (try_begin),
        (eq, ":rand", 0),
        (jump_to_menu,"mnu_event_siege_01"),
    (else_try),
        (eq, ":rand", 1),
        (jump_to_menu,"mnu_event_siege_02"),
    (else_try),
        (eq, ":rand", 2),
        (jump_to_menu,"mnu_event_siege_03"),
    (else_try),
        (display_message,"@ "),
    (try_end),
]),

#eventos de guerrilla e infiltracion normales y rutina
(24,[
    (eq, "$g_empieza_asedio", 1),
    (neq, "$g_player_is_captive", 1),
    (neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
    (call_script, "script_party_count_fit_for_battle", "p_main_party"),
    (gt, reg0, 40),
    (store_random_in_range, ":rand", 0, 40),
    (try_begin),
        (eq, ":rand", 0),
        (jump_to_menu,"mnu_event_siege_04"),
    (else_try),
        (eq, ":rand", 1),
        (jump_to_menu,"mnu_event_siege_05"),
    (else_try),
        (eq, ":rand", 2),
        (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,2), #con block is no.
        (jump_to_menu,"mnu_event_siege_06"),
    (else_try),
        (eq, ":rand", 3),
        (jump_to_menu,"mnu_event_siege_07"),
    (else_try),
        (eq, ":rand", 4),
	(call_script, "script_party_count_fit_regulars", "p_main_party"),
	(gt, reg0, 1),
	(call_script, "script_remove_regular_troops", "p_main_party", 1),
        (jump_to_menu,"mnu_event_siege_08"),
    (else_try),
        (eq, ":rand", 5),
        (jump_to_menu,"mnu_event_siege_09"),
    (else_try),
        (eq, ":rand", 6),
        (jump_to_menu,"mnu_event_siege_10"),
    (else_try),
        (eq, ":rand", 7),
        (jump_to_menu,"mnu_event_siege_12"),
    (else_try),
        (eq, ":rand", 8),
        (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,2), #con block is no.
        (jump_to_menu,"mnu_event_siege_13"),
    (else_try),
        (eq, ":rand", 9),
        (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,2), #con block is no.
        (jump_to_menu,"mnu_event_siege_14"),
    (else_try),
        (eq, ":rand", 10),
        (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,2), #con block is no.
        (jump_to_menu,"mnu_event_siege_15"),
    (else_try),
        (eq, ":rand", 11),
        (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,2), #con block is no.
        (jump_to_menu,"mnu_event_siege_16"),
    (else_try),
        (eq, ":rand", 12),
        (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,2), #con block is no.
        (jump_to_menu,"mnu_event_siege_17"),
    (else_try),
        (eq, ":rand", 13),
        (jump_to_menu,"mnu_event_siege_18"),
    (else_try),
        (eq, ":rand", 14),
        (jump_to_menu,"mnu_event_siege_22"),
    (else_try),
        (eq, ":rand", 15),
        (jump_to_menu,"mnu_event_siege_24"),
    (else_try),
        (eq, ":rand", 16),
        (jump_to_menu,"mnu_event_siege_25"),
    (else_try),
        (eq, ":rand", 17),
        (jump_to_menu,"mnu_event_siege_26"),
    (else_try),
        (display_message,"@ "),
    (try_end),
]),

(48,[
    (ge, "$g_empieza_asedio", 1),
    (neq, "$g_player_is_captive", 1),
    (this_or_next|eq, "$g_cur_month", 12),
    (this_or_next|eq, "$g_cur_month", 1),
    (eq, "$g_cur_month", 2),
    (neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
    (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
    (assign, ":num_men", 0),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
        (val_add, ":num_men", ":stack_size"),
    (try_end),
    (gt, ":num_men", 30),
    (store_random_in_range, ":rand", 0, 6),
    (try_begin),
        (eq, ":rand", 0),
        (jump_to_menu,"mnu_event_siege_11"),
    (else_try),
        (display_message,"@ "),
    (try_end),
]),

(24,[
    (eq, "$g_empieza_asedio", 1),
    (neq, "$g_player_is_captive", 1),
    (neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
    (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
    (assign, ":num_men", 0),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
        (val_add, ":num_men", ":stack_size"),
    (try_end),
    (gt, ":num_men", 50),
    (store_random_in_range, ":rand", 0, 18),
    (try_begin),
        (eq, ":rand", 0),
        (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,0), #con block yes.
        (jump_to_menu,"mnu_event_siege_19"),
    (else_try),
        (eq, ":rand", 1),
        (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,0), #con block yes.
        (jump_to_menu,"mnu_event_siege_21"),
    (else_try),
        (eq, ":rand", 2),
        (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,0), #con block yes.
        (jump_to_menu,"mnu_event_siege_23"),
    (else_try),
        (eq, ":rand", 3),
        (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,0), #con block yes.
        (jump_to_menu,"mnu_event_siege_27"),
    (else_try),
        (eq, ":rand", 4),
        (neq, "$g_siege_method", 0),
        (jump_to_menu,"mnu_event_siege_20"),
    (else_try),
        (eq, ":rand", 5),
        (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,0), #con block yes.
        (jump_to_menu,"mnu_event_siege_28"),
    (else_try),
        (eq, ":rand", 6),
        (neg|party_slot_eq,"$g_encountered_party",slot_center_blockaded,0), #con block yes.
        (jump_to_menu,"mnu_event_siege_29"),
    (else_try),
        (display_message,"@ "),
    (try_end),
]),

###anadido Siege warfare, if player take far place, then break siege
(0.2,[
    (eq, "$g_empieza_asedio", 1),
    #(gt,"$auto_besiege_town",0),
    (ge,"$g_player_besiege_town", 0),
    # (ge, "$g_siege_method", 1),
    (str_clear, s10),
    (store_distance_to_party_from_party, ":distance", "$g_player_besiege_town", "p_main_party"),
    (try_begin),
        (ge, ":distance", 2),
        (str_store_party_name_link, s10, "$g_player_besiege_town"),
        (display_message, "str_your_men_break_off_the_siege_of_s10_to_follow_you"),
        (call_script, "script_lift_siege", "$g_player_besiege_town", 0),
        (assign, "$g_player_besiege_town", -1),
    (else_try),
        (ge, ":distance", 1),
        (str_store_party_name_link, s10, "$g_player_besiege_town"),
        (display_message, "str_if_you_get_too_far_from_s10_your_siege_will_end"),
    (try_end),
]),


(24*4,
    [
    # SEASONS (Check all 5 days)
    (try_begin),
        (is_between, "$g_cur_month", 3, 11), # spring
        (eq, "$season", 0),
        (jump_to_menu, "mnu_fruhling"),
        # (assign,"$alt_diffuse_on",0), # es wird sommer, fruhling
    (else_try),
        (this_or_next|eq, "$g_cur_month", 12), # winter
        (is_between, "$g_cur_month", 1, 3), # winter
        (eq, "$season", 1),
        (jump_to_menu, "mnu_winter"),
        # (assign,"$alt_diffuse_on",1), # es wird winter
    (try_end),
]),

    # season shader reset (fix for VC-463)
(ti_on_switch_to_map,
  [
   (set_fixed_point_multiplier, 1),
   (set_shader_param_float, "@vSeason", "$shader_season"),

   # (assign, "$declare_war_curb_power", 1),
   (try_begin),
      (check_quest_active, "qst_ernak_quest"),
      (quest_slot_eq, "qst_ernak_quest", slot_quest_target_onoguroi, 10),
      (quest_slot_ge, "qst_ernak_quest", slot_quest_target_saraguroi, 10),
      (quest_slot_eq, "qst_ernak_quest", slot_quest_target_kutriguroi, 4),
      (quest_slot_eq, "qst_ernak_quest", slot_quest_current_state, 1),
      (quest_set_slot, "qst_ernak_quest", slot_quest_current_state, 2),
      (str_store_troop_name_link, s22, "trp_knight_23_8"),
      (add_quest_note_from_sreg, "qst_ernak_quest", 8, "@All tribes accepted your proposal. Return to {s22} and report him about the news.", 0),
      (tutorial_box, "@All tribes accepted your proposal. Report to Ernak about your success.", "@Ernak's offer"),
   (try_end),
]),

(24,## SIMULATING WEATHER
  [
  (store_random_in_range, ":r", 1, 101),
  (try_begin),
    (this_or_next|is_between, "$g_cur_month", 1, 3),
      (eq, "$g_cur_month", 12),
      (try_begin),
        (is_between, ":r", 1, 15),
        (store_random_in_range, ":random", 0, 5),
        (set_global_cloud_amount, ":random"),
        (set_global_haze_amount, ":random"),
        (assign,"$wind_power",0),
      (else_try),
        (is_between, ":r", 15, 45),
        (store_random_in_range, ":random", 20, 35),
        (set_global_cloud_amount, ":random"),
        (set_global_haze_amount, ":random"),
        (assign,"$wind_power",1),
      (else_try),
        (is_between, ":r", 45, 65),
        (store_random_in_range, ":random", 50, 70),
        (set_global_cloud_amount, ":random"),
        (set_global_haze_amount, ":random"),
        (assign,"$wind_power",2),
      (else_try),
        (is_between, ":r", 65, 80),
        (store_random_in_range, ":random", 70, 80),
        (set_global_cloud_amount, ":random"),
        (set_global_haze_amount, ":random"),
        (assign,"$wind_power",3),
      (else_try),
        (is_between, ":r", 80, 101),
        (store_random_in_range, ":random", 80, 100),
        (set_global_cloud_amount, ":random"),
        (set_global_haze_amount, ":random"),
        (assign,"$wind_power",4),
      (try_end),
  (else_try),
    (is_between, "$g_cur_month", 3, 6),
      (try_begin),
        (is_between, ":r", 1, 15),
        (store_random_in_range, ":random1", 0, 5),
        (store_random_in_range, ":random2", 0, 5),
        (set_global_cloud_amount, ":random1"),
        (set_global_haze_amount, ":random2"),
        (assign,"$wind_power",0),
      (else_try),
        (is_between, ":r", 15, 45),
        (store_random_in_range, ":random1", 60, 90),
        (store_random_in_range, ":random2", 20, 30),
        (set_global_cloud_amount, ":random1"),
        (set_global_haze_amount, ":random2"),
        (assign,"$wind_power",1),
      (else_try),
        (is_between, ":r", 45, 65),
        (store_random_in_range, ":random1", 20, 25),
        (store_random_in_range, ":random2", 10, 15),
        (set_global_cloud_amount, ":random1"),
        (set_global_haze_amount, ":random2"),
        (assign,"$wind_power",2),
      (else_try),
        (is_between, ":r", 65, 80),
        (store_random_in_range, ":random1", 90, 101),
        (store_random_in_range, ":random2", 0, 50),
        (set_global_cloud_amount, ":random1"),
        (set_global_haze_amount, ":random2"),
        (assign,"$wind_power",3),
      (else_try),
        (is_between, ":r", 80, 101),
        (store_random_in_range, ":random1", 0, 50),
        (store_random_in_range, ":random2", 0, 5),
        (set_global_cloud_amount, ":random1"),
        (set_global_haze_amount, ":random2"),
        (assign,"$wind_power",4),
      (try_end),
  (else_try),
    (is_between, "$g_cur_month", 6, 9),
      (try_begin),
        (is_between, ":r", 1, 25),
        (store_random_in_range, ":random1", 0, 5),
        (store_random_in_range, ":random2", 0, 3),
        (set_global_cloud_amount, ":random1"),
        (set_global_haze_amount, ":random2"),
        (assign,"$wind_power",0),
      (else_try),
        (is_between, ":r", 25, 65),
        (store_random_in_range, ":random1", 0, 14),
        (store_random_in_range, ":random2", 0, 3),
        (set_global_cloud_amount, ":random1"),
        (set_global_haze_amount, ":random2"),
        (assign,"$wind_power",1),
      (else_try),
        (is_between, ":r", 65, 80),
        (store_random_in_range, ":random1", 30, 55),
        (store_random_in_range, ":random2", 0, 5),
        (set_global_cloud_amount, ":random1"),
        (set_global_haze_amount, ":random2"),
        (assign,"$wind_power",2),
      (else_try),
        (is_between, ":r", 80, 90),
        (store_random_in_range, ":random1", 0, 50),
        (store_random_in_range, ":random2", 0, 5),
        (set_global_cloud_amount, ":random1"),
        (set_global_haze_amount, ":random2"),
        (assign,"$wind_power",3),
      (else_try),
        (is_between, ":r", 90, 101),
        (store_random_in_range, ":random1", 80, 101),
        (store_random_in_range, ":random2", 30, 40),
        (set_global_cloud_amount, ":random1"),
        (set_global_haze_amount, ":random2"),
        (assign,"$wind_power",4),
      (try_end),
  (else_try),
    (is_between, "$g_cur_month", 9, 12),
      (try_begin),
        (is_between, ":r", 1, 10),
        (store_random_in_range, ":random1", 0, 5),
        (store_random_in_range, ":random2", 0, 5),
        (set_global_cloud_amount, ":random1"),
        (set_global_haze_amount, ":random2"),
        (assign,"$wind_power",0),
      (else_try),
        (is_between, ":r", 10, 65),
        (store_random_in_range, ":random1", 0, 14),
        (store_random_in_range, ":random2", 70, 101),
        (set_global_cloud_amount, ":random1"),
        (set_global_haze_amount, ":random2"),
        (assign,"$wind_power",1),
      (else_try),
        (is_between, ":r", 65, 80),
        (store_random_in_range, ":random1", 30, 55),
        (store_random_in_range, ":random2", 90, 101),
        (set_global_cloud_amount, ":random1"),
        (set_global_haze_amount, ":random2"),
        (assign,"$wind_power",2),
      (else_try),
        (is_between, ":r", 80, 90),
        (store_random_in_range, ":random1", 50, 65),
        (store_random_in_range, ":random2", 20, 55),
        (set_global_cloud_amount, ":random1"),
        (set_global_haze_amount, ":random2"),
        (assign,"$wind_power",3),
      (else_try),
        (is_between, ":r", 90, 101),
        (store_random_in_range, ":random1", 90, 101),
        (store_random_in_range, ":random2", 90, 101),
        (set_global_cloud_amount, ":random1"),
        (set_global_haze_amount, ":random2"),
        (assign,"$wind_power",4),
      (try_end),
  (try_end),


  #shader
	(store_random_in_range, "$beaufort", 1, 13),
        (store_sub, reg0, "$beaufort", 1),
        (val_max, reg0, 0),
        (store_div, ":shader_wind_strenght", reg0, 3),  #yields 0-3
        (set_fixed_point_multiplier,1),
        (set_shader_param_float, "@vWindStrength", ":shader_wind_strenght"),
]),


##this is for fires
#49 towns + 66 castles + 230 villages
(24.0*2.0*7.0/(number_of_walled_centers), [##means every two weeks on average
	(store_random_in_range, ":center", walled_centers_begin, walled_centers_end),
    # (neg|party_slot_ge, ":center", slot_party_looted_left_days, 1),
	##includes effects of new bildings
	#(store_random_in_range, ":r", 0, 100),
	(try_begin),
		#(ge, ":r", 50),
		(party_slot_ge, ":center", slot_center_has_forum, 1),#forum
		(party_get_slot, ":lord", ":center", slot_town_lord),
		(call_script, "script_change_center_prosperity",  ":center", 2),
		(call_script, "script_change_troop_renown", ":lord", 5),
		(try_begin),
			(eq, ":lord", "trp_player"),
			(str_store_party_name, s50, ":center"),
            (call_script, "script_get_improvement_details", slot_center_has_forum, ":center"),
			(display_message, "@Your {s0} adds prosperity to {s50} and fame to you.", message_positive),
			(call_script, "script_change_player_relation_with_center", ":center", 1),
		(try_end),
	(try_end),
	(try_begin),
		#(ge, ":r", 50),
		(party_slot_ge, ":center", slot_center_has_theatre, 1),#theater
		(party_get_slot, ":lord", ":center", slot_town_lord),
		(call_script, "script_change_center_prosperity",  ":center", 1),
		(call_script, "script_change_troop_renown",":lord", 5),
		(try_begin),
			(eq, ":lord", "trp_player"),
			(str_store_party_name, s50, ":center"),
            (call_script, "script_get_improvement_details", slot_center_has_theatre, ":center"),
			(display_message, "@Your {s0} adds prosperity to {s50} and fame to you.", message_positive),
			(call_script, "script_change_player_relation_with_center", ":center", 2),
		(try_end),
	(try_end),

	# (try_begin),
		# (party_slot_ge, ":center", slot_center_decree_housing, 1),
		# (party_get_slot, ":lord", ":center", slot_town_lord),
		# (eq, ":lord", "trp_player"),
		# (party_get_slot, ":cur_relation", ":center", slot_center_player_relation),
		# (lt, ":cur_relation", 50),
		# (call_script, "script_change_player_relation_with_center", ":center", 2),
        # (str_store_party_name, s50, ":center"),
        # (display_message, "@The social housing decree increases your relation with {s50}."),
	# (try_end),
	# (try_begin),
		# (party_slot_ge, ":center", slot_center_decree_curfew, 1),
		# (party_get_slot, ":lord", ":center", slot_town_lord),
		# (eq, ":lord", "trp_player"),
		# (party_get_slot, ":cur_relation", ":center", slot_center_player_relation),
		# (ge, ":cur_relation", -25),
		# (call_script, "script_change_player_relation_with_center", ":center", -1),
        # (str_store_party_name, s50, ":center"),
        # (display_message, "@The nightly curfew lowers your relation with {s50}."),
	# (try_end),
	# (try_begin),
		# (party_slot_ge, ":center", slot_center_decree_control, 1),
		# (party_get_slot, ":lord", ":center", slot_town_lord),
		# (eq, ":lord", "trp_player"),
		# (party_get_slot, ":cur_relation", ":center", slot_center_player_relation),
		# (ge, ":cur_relation", -35),
		# (call_script, "script_change_player_relation_with_center", ":center", -1),
        # (str_store_party_name, s50, ":center"),
        # (display_message, "@The decree about entry controls lowers your relation with {s50}."),
	# (try_end),
	# (try_begin),
		# (party_slot_ge, ":center", slot_center_decree_law_enforcement, 1),
		# (party_get_slot, ":lord", ":center", slot_town_lord),
		# (eq, ":lord", "trp_player"),
		# (party_get_slot, ":cur_relation", ":center", slot_center_player_relation),
		# (ge, ":cur_relation", -70),
		# (call_script, "script_change_player_relation_with_center", ":center", -3),
        # (str_store_party_name, s50, ":center"),
        # (display_message, "@The decree about law enforcement lowers your relation with {s50}."),
	# (try_end),

	(try_begin),
		#(ge, ":r", 50),
		(party_slot_ge, ":center", slot_center_has_training_grounds, 1),#training ground
		(party_get_slot, ":lord", ":center", slot_town_lord),
		(store_random_in_range, ":xp_addition_for_centers", 30000, 50000),
		(party_upgrade_with_xp, ":center", ":xp_addition_for_centers", 0),
		(try_begin),
			(eq, ":lord", "trp_player"),
			(str_store_party_name, s50, ":center"),
            (call_script, "script_get_improvement_details", slot_center_has_training_grounds, ":center"),
			(display_message, "@Troops gain experience in {s50} due to your {s0}.", message_positive),
		(try_end),
	(try_end),
	(try_begin),
		#(ge, ":r", 50),
		(party_slot_ge, ":center", slot_center_has_triumph, 1),#triumphbogen
		(party_get_slot, ":lord", ":center", slot_town_lord),
		(call_script, "script_change_troop_renown",":lord", 5),
		(str_store_party_name, s50, ":center"),
        (call_script, "script_get_improvement_details", slot_center_has_triumph, ":center"),
		(display_message, "@Your {s0} in {s50} adds fame to you.", message_positive),
	(try_end),
	(try_begin),
		#(ge, ":r", 50),
		(party_slot_ge, ":center", slot_center_has_water, 1),#baths
		(party_get_slot, ":lord", ":center", slot_town_lord),
		(call_script, "script_change_center_prosperity",  ":center", 1),
		(call_script, "script_change_troop_renown",":lord", 5),
		(try_begin),
			(eq, ":lord", "trp_player"),
			(call_script, "script_change_player_relation_with_center", ":center", 2),
			(str_store_party_name, s50, ":center"),
            (call_script, "script_get_improvement_details", slot_center_has_water, ":center"),
			(display_message, "@Your {s0} in {s50} add prosperity and fame.", message_positive),
		(try_end),
	(try_end),
	##buildings end
	# (try_begin),
		# (party_slot_ge, ":center",slot_center_capital, 10000),#has some wealth
		# (assign, ":bound", 115),

		# (assign, ":chance", 40),
		# (try_begin),
			# (party_slot_ge, ":center",slot_center_has_fire_fighter, 1),
			# (val_add, ":bound", 25),
			# (val_sub, ":chance", 30),
		# (try_end),
		# (try_begin),#
			# (party_slot_eq, ":center", slot_party_type, spt_village),
            # (val_add, ":bound", 25),
			# (val_sub, ":chance", 25),#fires are less desastrous in rural areas
		# (try_end),

		# (store_random_in_range, ":disaster", 0, ":bound"),
		# (try_begin),
			# (le, ":disaster", 2),
			# (store_random_in_range, ":rand", -13, -7),
			# (call_script, "script_change_center_prosperity", ":center", ":rand"),

            # (str_store_party_name, s60, ":center"),
            # (display_log_message, "@A huge fire devastated {s60}!", message_negative),

			# ##destroy buildings
            # (try_begin),
                # (party_slot_eq, ":center", slot_town_lord, "trp_player"),
                # (assign, ":count_end", 2),
            # (else_try),
                # (assign, ":count_end", 4),
            # (try_end),
            # (assign, ":count", 1),
            # (assign, ":loop_end", slot_center_has_forum),
			# (try_for_range, ":buildings", village_improvements_begin, ":loop_end"),
				# (neq, ":buildings", slot_center_has_iron_mine),
				# (neq, ":buildings", slot_center_has_silver_mine),
				# (neq, ":buildings", slot_center_has_roads),
				# (neq, ":buildings", slot_center_has_sewers),
				# (neq, ":buildings", slot_center_has_barracks),
				# (neq, ":buildings", slot_center_change_culture_village),
				# (neq, ":buildings", slot_center_change_culture_town),
				# (neq, ":buildings", slot_center_has_farms),
				# (neq, ":buildings", slot_center_has_irigation),
				# (neq, ":buildings", slot_center_has_cattle),
				# (neq, ":buildings", slot_center_has_port),
				# (neq, ":buildings", slot_center_has_fishport),
				# (neq, ":buildings", slot_center_has_quarry),
				# (neq, ":buildings", slot_center_has_fire_fighter),
				# (store_random_in_range, ":r", 0, ":bound"),
				# (lt, ":r", ":chance"),
				# (party_slot_ge, ":center",":buildings", 1),
				# (party_set_slot, ":center",":buildings", 0),
				# # (party_slot_eq, ":center", slot_town_lord, "trp_player"),
				# (str_store_party_name, s60, ":center"),
				# (call_script, "script_get_improvement_details", ":buildings", ":center"),
				# (display_log_message, "@The fire in {s60} destroyed ({s0})!", message_negative),
                # (try_begin),
                    # (eq, ":count", ":count_end"),
                    # (assign, ":loop_end", -1),
                # (else_try),
                    # (val_add, ":count", 1),
                # (try_end),
			# (try_end),
			# ##kill people
			# (try_begin),
				# (this_or_next|party_slot_eq, ":center", slot_party_type, spt_town),
				# (party_slot_eq, ":center", slot_party_type, spt_castle),
				# (store_random_in_range, ":str", 2, 4),
				# #(call_script, "script_inflict_casualties_to_party", ":center", ":str"),
				# (call_script, "script_party_inflict_attrition", ":center", ":str"),
			# (try_end),
			# ##lower rents
			# (party_get_slot, ":rents", ":center", slot_center_accumulated_rents),
			# (store_mul, ":rents_new", ":rents", 2),
			# (val_div, ":rents_new", 9),
			# (party_set_slot, ":center", slot_center_accumulated_rents, ":rents_new"),
		# (else_try),
			# (is_between, ":disaster", 3, 9),
			# (store_random_in_range, ":rand", -6, -4),
			# (call_script, "script_change_center_prosperity", ":center", ":rand"),

			# (try_begin),
				# (store_distance_to_party_from_party, ":distance", "p_main_party", ":center"),
				# (lt, ":distance", 30), ##only if the player is near
				# (str_store_party_name, s60, ":center"),
				# (display_log_message, "@A fire broke out in {s60} and destroyed many buildings!", message_negative),
			# (else_try),
				# (party_slot_eq, ":center", slot_town_lord, "trp_player"),
				# (str_store_party_name, s60, ":center"),
				# (display_log_message, "@A fire broke out in {s60} and destroyed many buildings!", message_negative),
			# (try_end),

			# ##destroy buildings
            # (try_begin),
                # (party_slot_eq, ":center", slot_town_lord, "trp_player"),
                # (assign, ":count_end", 1),
            # (else_try),
                # (assign, ":count_end", 2),
            # (try_end),
            # (assign, ":count", 1),
            # (assign, ":loop_end", slot_center_has_forum),
			# (try_for_range, ":buildings", village_improvements_begin, ":loop_end"),
				# (neq, ":buildings", slot_center_has_iron_mine),
				# (neq, ":buildings", slot_center_has_silver_mine),
				# (neq, ":buildings", slot_center_has_barracks),
				# (neq, ":buildings", slot_center_change_culture_village),
				# (neq, ":buildings", slot_center_change_culture_town),
				# (neq, ":buildings", slot_center_has_farms),
				# (neq, ":buildings", slot_center_has_irigation),
				# (neq, ":buildings", slot_center_has_cattle),
				# (neq, ":buildings", slot_center_has_port),
				# (neq, ":buildings", slot_center_has_fishport),
				# (neq, ":buildings", slot_center_has_quarry),
				# (neq, ":buildings", slot_center_has_fire_fighter),
				# (store_random_in_range, ":r", 0, ":bound"),
				# (lt, ":r", ":chance"),
				# (party_slot_ge, ":center",":buildings", 1),
				# (party_set_slot, ":center",":buildings", 0),
				# # (party_slot_eq, ":center", slot_town_lord, "trp_player"),
				# (str_store_party_name, s60, ":center"),
				# (call_script, "script_get_improvement_details", ":buildings", ":center"),
				# (display_log_message, "@The fire in {s60} destroyed ({s0})!", message_negative),
                # (try_begin),
                    # (eq, ":count", ":count_end"),
                    # (assign, ":loop_end", -1),
                # (else_try),
                    # (val_add, ":count", 1),
                # (try_end),
			# (try_end),

			# (party_get_slot, ":rents", ":center", slot_center_accumulated_rents),
			# (store_mul, ":rents_new", ":rents", 9),
			# (val_div, ":rents_new", 10),
			# (party_set_slot, ":center", slot_center_accumulated_rents, ":rents_new"),
			# (try_begin),
				# (this_or_next|party_slot_eq, ":center", slot_party_type, spt_town),
				# (party_slot_eq, ":center", slot_party_type, spt_castle),
				# #(call_script, "script_inflict_casualties_to_party", ":center", 1), #this code also effects other parties in the center
				# (call_script, "script_party_inflict_attrition", ":center", 1), #this only effects the center garrison
			# (try_end),
		# (try_end),
	# (try_end),
 ]
),

###we have sicknesses and fires which can devaste centers
##this is for illness
(2.0*24.0*7.0/(number_of_centers),
[##every two weeks on average
    (store_random_in_range, ":center", centers_begin, centers_end),
    (party_slot_eq, ":center", slot_center_disease, 0),#hs no disease yet
    #determine disease chances
    (try_begin),
        (this_or_next|is_between, "$g_cur_month", 1, 4),
        (is_between, "$g_cur_month", 10, 13),
        (assign, ":chance", 3),
    (else_try),
        (is_between, "$g_cur_month", 4, 7),
        (assign, ":chance", 2),
    (else_try),
        (assign, ":chance", 1),
    (try_end),

    (party_get_slot, ":prosperity", ":center", slot_town_prosperity),
    (store_sub, ":bound", 180, ":prosperity"),

    (val_add, ":bound", 25),
    # (try_begin),
        # (party_slot_ge, ":center", slot_center_decree_garbage_collection, 1),
        # (val_add, ":bound", 50),
    # (try_end),
    (try_begin),
        (party_slot_ge, ":center", slot_center_has_sewers, 1),
        (val_add, ":bound", 100),
    (try_end),
    (try_begin),
        (party_slot_ge, ":center", slot_center_has_hosptial, 1),
        (val_add, ":bound", 50),
    (try_end),
    (store_random_in_range, ":disaster", 0, ":bound"),
    (le, ":disaster", ":chance"),

    (store_random_in_range, ":disease_rand", 0, 15),
    (try_begin),
        (le, ":disease_rand", 2),
        (assign, ":disease", disease_consumption),
        # (troop_get_slot,":number","trp_global_variables", g_number_consumption),
        # (val_add, ":number", 1),
        # (troop_set_slot,"trp_global_variables", g_number_consumption, ":number"),
    (else_try),
        (eq, ":disease_rand", 4),
        (assign, ":disease", disease_slow_fever),
        # (troop_get_slot,":number","trp_global_variables", g_number_slow_fever),
        # (val_add, ":number", 1),
        # (troop_set_slot,"trp_global_variables", g_number_slow_fever, ":number"),
    (else_try),
        (eq, ":disease_rand", 6),
        (assign, ":disease", disease_camp_fever),
        # (troop_get_slot,":number","trp_global_variables", g_number_camp_fever),
        # (val_add, ":number", 1),
        # (troop_set_slot,"trp_global_variables", g_number_camp_fever, ":number"),
    (else_try),
        (eq, ":disease_rand", 7),
        (assign, ":disease", disease_plague),
        # (troop_get_slot,":number","trp_global_variables", g_number_plague),
        # (val_add, ":number", 1),
        # (troop_set_slot,"trp_global_variables", g_number_plague, ":number"),
    (else_try),
        (le, ":disease_rand", 9),
        (assign, ":disease", disease_measles),
        # (troop_get_slot,":number","trp_global_variables", g_number_measles),
        # (val_add, ":number", 1),
        # (troop_set_slot,"trp_global_variables", g_number_measles, ":number"),
    (else_try),
        (le, ":disease_rand", 11),
        (assign, ":disease", disease_smallpox),
        # (troop_get_slot,":number","trp_global_variables", g_number_smallpox),
        # (val_add, ":number", 1),
        # (troop_set_slot,"trp_global_variables", g_number_smallpox, ":number"),
    (else_try),
        (assign, ":disease", disease_greatpoxpox),
        # (troop_get_slot,":number","trp_global_variables", g_number_greatpox),
        # (val_add, ":number", 1),
        # (troop_set_slot,"trp_global_variables", g_number_greatpox, ":number"),
    (try_end),

    (try_begin),
        (party_slot_ge, ":center", slot_center_has_hosptial, 1),
        (party_slot_ge, ":center", slot_center_has_sewers, 1),
        (val_sub, ":disease", 1),
    (try_end),

    (call_script, "script_get_event_details", ":disease"),
    # (assign, ":modifier", reg0),
    (call_script, "script_change_center_prosperity", ":center", reg1),
    (party_set_slot, ":center", slot_center_disease, ":disease"),

    # (party_get_slot, ":accumulated_rents", ":center", slot_center_accumulated_rents),
    # (val_mul, ":accumulated_rents", 80),
    # (val_div, ":accumulated_rents", 100),
    # (party_set_slot, ":center",slot_center_accumulated_rents, ":accumulated_rents"),
    (try_begin),
        (party_slot_eq, ":center", slot_town_lord, "trp_player"),
        (call_script, "script_add_notification_menu", "mnu_epidemic_outbreak", ":center", 0),
    (try_end),

    # (str_store_party_name, s22, ":center"),
    # (call_script, "script_get_event_details", ":disease"),
    # (display_log_message, "@In {s22} has started a {s0} outbreak.", color_bad_news),

    ]),

#EVENT: DROUGHT
(24.0*7.0/(number_of_villages),
[##every two weeks on average
    (store_random_in_range, ":center", villages_begin, villages_end),
    (party_slot_eq, ":center", slot_center_event, 0),#no event yet
    #determine disease chances
    (try_begin),
        (this_or_next|is_between, "$g_cur_month", 1, 4),
        (is_between, "$g_cur_month", 10, 13),
        (assign, ":chance", 3),
        (assign, ":bound", 250),
    (else_try),
        (is_between, "$g_cur_month", 4, 7),
        (assign, ":chance", 2),
        (assign, ":bound", 275),
    (else_try),
        (assign, ":chance", 1),
        (assign, ":bound", 300),
    (try_end),

    (try_begin),
        (party_slot_ge, ":center", slot_center_has_irigation, 1),
        (val_add, ":bound", 200),
    (try_end),
    (try_begin),
        (party_slot_ge, ":center", slot_center_has_farms, 1),
        (val_sub, ":bound", 50),
    (try_end),
    (store_random_in_range, ":disaster", 0, ":bound"),
    (le, ":disaster", ":chance"),

    (call_script, "script_get_event_details", event_drought),
    # (assign, ":modifier", reg0),
    (call_script, "script_change_center_prosperity", ":center", reg1),
    (party_set_slot, ":center", slot_center_event, event_drought),

    (party_get_slot, ":accumulated_rents", ":center", slot_center_accumulated_rents),
    (val_mul, ":accumulated_rents", 75),
    (val_div, ":accumulated_rents", 100),
    (party_set_slot, ":center",slot_center_accumulated_rents, ":accumulated_rents"),
    (try_begin),
        (party_slot_eq, ":center", slot_town_lord, "trp_player"),
        (call_script, "script_add_notification_menu", "mnu_disaster_event", ":center", 0),
    (try_end),

    # (str_store_party_name, s22, ":center"),
    # (call_script, "script_get_event_details", ":disease"),
    # (display_log_message, "@In {s22} has started a {s0} outbreak.", color_bad_news),
    # (troop_get_slot,":number","trp_global_variables", g_number_drought),
    # (val_add, ":number", 1),
    # (troop_set_slot,"trp_global_variables", g_number_drought, ":number"),
    ]),
#EVENT: BEETLES INVASION
(24.0*7.0/(number_of_villages),
[##every two weeks on average
    (store_random_in_range, ":center", villages_begin, villages_end),
    (party_slot_eq, ":center", slot_center_event, 0),#no event yet
    #determine disease chances
    (try_begin),
        (this_or_next|is_between, "$g_cur_month", 1, 4),
        (is_between, "$g_cur_month", 10, 13),
        (assign, ":chance", 3),
        (assign, ":bound", 350),
    (else_try),
        (is_between, "$g_cur_month", 4, 7),
        (assign, ":chance", 2),
        (assign, ":bound", 375),
    (else_try),
        (assign, ":chance", 1),
        (assign, ":bound", 400),
    (try_end),

    # (try_begin),
        # (party_slot_ge, ":center", slot_center_has_irigation, 1),
        # (val_add, ":bound", 200),
    # (try_end),
    # (try_begin),
        # (party_slot_ge, ":center", slot_center_has_farms, 1),
        # (val_sub, ":bound", 50),
    # (try_end),
    (store_random_in_range, ":disaster", 0, ":bound"),
    (le, ":disaster", ":chance"),

    (call_script, "script_get_event_details", event_insects),
    # (assign, ":modifier", reg0),
    (call_script, "script_change_center_prosperity", ":center", reg1),
    (party_set_slot, ":center", slot_center_event, event_insects),

    (party_get_slot, ":accumulated_rents", ":center", slot_center_accumulated_rents),
    (val_mul, ":accumulated_rents", 75),
    (val_div, ":accumulated_rents", 100),
    (party_set_slot, ":center",slot_center_accumulated_rents, ":accumulated_rents"),
    (try_begin),
        (party_slot_eq, ":center", slot_town_lord, "trp_player"),
        (call_script, "script_add_notification_menu", "mnu_disaster_event", ":center", 0),
    (try_end),

    # (str_store_party_name, s22, ":center"),
    # (call_script, "script_get_event_details", ":disease"),
    # (display_log_message, "@In {s22} has started a {s0} outbreak.", color_bad_news),
    # (troop_get_slot,":number","trp_global_variables", g_number_insects),
    # (val_add, ":number", 1),
    # (troop_set_slot,"trp_global_variables", g_number_insects, ":number"),
    ]),
#EVENT: Earthquake
(2.0*24.0*7.0/(number_of_walled_centers),
[##every two weeks on average
    (store_random_in_range, ":center", walled_centers_begin, walled_centers_end),
    (party_slot_eq, ":center", slot_center_event, 0),#no event yet
    (store_random_in_range, ":disaster", 0, 700),
    (le, ":disaster", 1),

    # (call_script, "script_cf_can_have_earthquake", ":center"),

    (call_script, "script_get_event_details", event_earthquake),
    # (assign, ":modifier", reg0),
    (call_script, "script_change_center_prosperity", ":center", reg1),
    (party_set_slot, ":center", slot_center_event, event_earthquake),

    (party_get_slot, ":accumulated_rents", ":center", slot_center_accumulated_rents),
    (val_mul, ":accumulated_rents", 25),
    (val_div, ":accumulated_rents", 100),
    (party_set_slot, ":center",slot_center_accumulated_rents, ":accumulated_rents"),
    # (try_begin),
        # (party_slot_eq, ":center", slot_town_lord, "trp_player"),
    (call_script, "script_add_notification_menu", "mnu_disaster_event", ":center", 0),
    # (try_end),

    # (str_store_party_name, s22, ":center"),
    # (call_script, "script_get_event_details", ":disease"),
    # (display_log_message, "@In {s22} has started a {s0} outbreak.", color_bad_news),
    # (troop_get_slot,":number","trp_global_variables", g_number_earthquake),
    # (val_add, ":number", 1),
    # (troop_set_slot,"trp_global_variables", g_number_earthquake, ":number"),
    ]),

##FIRES
    (24.0*2.0*7.0/(number_of_centers),[
    (store_random_in_range, ":center", centers_begin, centers_end),
    (party_slot_eq, ":center", slot_center_event, 0),
    (assign, ":bound", 300),

    (try_begin),
        (this_or_next|is_between, "$g_cur_month", 1, 4),
        (is_between, "$g_cur_month", 10, 13),
        (assign, ":chance", 20),
    (else_try),
        (is_between, "$g_cur_month", 4, 7),
        (assign, ":chance", 30),
    (else_try),
        (assign, ":chance", 50),
    (try_end),

    (try_begin),
        (party_slot_ge, ":center",slot_center_has_fire_fighter, 1),
        (val_add, ":bound", 25),
        (val_sub, ":chance", 30),
    (try_end),
    (try_begin),#
        (party_slot_eq, ":center", slot_party_type, spt_village),
        (val_add, ":bound", 25),
        (val_div, ":chance", 2),#fires are less desastrous in rural areas
    (try_end),
    (store_random_in_range, ":disaster", 0, ":bound"),
    (le, ":disaster", ":chance"),


    (try_begin),
        (party_slot_eq, ":center", slot_town_lord, "trp_player"),
        (party_slot_ge, ":center", slot_center_has_fire_fighter, 1),
        (assign, ":count_end", 0),
        (assign, ":loop_end", -1),
    (else_try),
        (party_slot_eq, ":center", slot_town_lord, "trp_player"),
        (assign, ":count_end", 1),
    (else_try),
        (assign, ":count_end", 2),
    (try_end),
    (assign, ":count", 1),
    (assign, ":loop_end", slot_center_has_forum),
    (try_for_range, ":buildings", village_improvements_begin, ":loop_end"),
        (neq, ":buildings", slot_center_has_iron_mine),
        (neq, ":buildings", slot_center_has_silver_mine),
        (neq, ":buildings", slot_center_has_barracks),
        (neq, ":buildings", slot_center_change_culture_village),
        (neq, ":buildings", slot_center_change_culture_town),
        (neq, ":buildings", slot_center_has_farms),
        (neq, ":buildings", slot_center_has_irigation),
        (neq, ":buildings", slot_center_has_cattle),
        (neq, ":buildings", slot_center_has_port),
        (neq, ":buildings", slot_center_has_fishport),
        (neq, ":buildings", slot_center_has_quarry),
        (neq, ":buildings", slot_center_has_fire_fighter),
        (store_random_in_range, ":r", 0, ":bound"),
        (lt, ":r", ":chance"),
        (party_slot_ge, ":center",":buildings", 1),
        (party_set_slot, ":center",":buildings", 0),

        (try_begin),
            (party_slot_eq, ":center", slot_town_lord, "trp_player"),
            (str_store_party_name, s60, ":center"),
            (call_script, "script_get_improvement_details", ":buildings", ":center"),
            (display_log_message, "@The fire in {s60} destroyed ({s0})!", message_negative),
        (try_end),
        (try_begin),
            (eq, ":count", ":count_end"),
            (assign, ":loop_end", -1),
        (else_try),
            (val_add, ":count", 1),
        (try_end),
    (try_end),

    (party_set_slot, ":center", slot_center_event, event_fire),
    (call_script, "script_get_event_details", event_fire),
    (call_script, "script_change_center_prosperity", ":center", reg1),
    (party_get_slot, ":accumulated_rents", ":center", slot_center_accumulated_rents),
    (val_mul, ":accumulated_rents", 75),
    (val_div, ":accumulated_rents", 100),
    (party_set_slot, ":center",slot_center_accumulated_rents, ":accumulated_rents"),

    (try_begin),
        (party_slot_eq, ":center", slot_town_lord, "trp_player"),
        (call_script, "script_add_notification_menu", "mnu_disaster_event", ":center", 0),
    (try_end),
    ]),

#madsci rebellion stuff
 (3,[
(store_random_in_range, ":center", towns_begin, towns_end),
	(try_begin),
	(party_slot_eq, ":center", slot_center_is_besieged_by, -1), #no rebellion in besieged town
	(party_get_slot, ":rebellion_timer", ":center", slot_party_rebellion_timer),
	(eq, ":rebellion_timer", 1),
	(party_get_slot, ":rebel_faction", ":center", slot_party_rebel_faction),
	(gt, ":rebel_faction", 0),
	(neg|faction_slot_eq, ":rebel_faction", slot_faction_state, sfs_active),
	(store_faction_of_party, ":faction_now", ":center"),
	(neq, ":faction_now", ":rebel_faction"),
	(set_relation, ":faction_now", ":rebel_faction", -100),
	(party_get_slot, ":town_lord", ":center", slot_town_lord),
	(ge, ":town_lord", 0),
	(party_set_slot, ":center", slot_party_rebellion_timer, 0),
	(store_random_in_range, ":cooldown", 90, 120), #dont let another rebellion happen immediately
	(party_set_slot, ":center", slot_party_rebellion_cooldown, ":cooldown"),
	(call_script, "script_cf_launch_rebellion", ":center"),
		(try_begin),
        	(eq, "$g_infinite_camping", 0),
		(neq, "$freelancer_state", 1),
		(assign, "$g_notification_menu_var1", ":center"),
		(jump_to_menu, "mnu_rebellion_launched"),
		(try_end),
	(str_store_party_name_link, s10, ":center"),
	(display_log_message, "@{s10} has revolted!"),
	(else_try),
	(party_slot_eq, ":center", slot_center_is_besieged_by, -1), #no rebellion in besieged town
	(party_get_slot, ":rebellion_cooldown", ":center", slot_party_rebellion_cooldown),
	(eq, ":rebellion_cooldown", 0),
	(store_random_in_range, ":rng", 0, 50),
	(eq, ":rng", 1), #dont let it fire too often
		(try_begin),
		(this_or_next|eq, ":center", "p_town_25"),
		(eq, ":center", "p_town_40"),
		(store_faction_of_party, ":town_faction", ":center"),
		(assign, ":player_barbarian_owner", 0),
			(try_begin),
			(eq, ":town_faction", "fac_player_supporters_faction"),
			(faction_get_slot, ":player_culture", "fac_player_supporters_faction", slot_faction_culture),
			(neq, ":player_culture", "fac_culture_empire"),
			(neq, ":player_culture", "fac_culture_3"),
			(neq, ":player_culture", "fac_culture_11"),
			(assign, ":player_barbarian_owner", 1),
			(try_end),
		(this_or_next|eq, ":player_barbarian_owner", 1),
		(this_or_next|eq, ":town_faction", "fac_kingdom_3"),
		(this_or_next|eq, ":town_faction", "fac_kingdom_8"),
		(this_or_next|eq, ":town_faction", "fac_kingdom_30"),
		(eq, ":town_faction", "fac_kingdom_15"),
		(faction_slot_eq, "fac_kingdom_1", slot_faction_state, sfs_active), #only let Roman rebels appear if Rome still exists
		(call_script, "script_cf_start_rebellion", ":center", "fac_kingdom_1"), #second value determines the affiliation of the rebels, this script can fail
		(try_end),
	(try_end),

#migrating nomad camps
(try_for_range, ":camp", minor_towns_begin, minor_towns_end),
(party_get_icon, ":icon", ":camp"),
(this_or_next|eq, ":icon", "icon_ship"),
(this_or_next|eq, ":icon", "icon_steppe_lord"),
(eq, ":icon", "icon_nomad_camp"),
(store_faction_of_party, ":camp_faction", ":camp"),
(is_between, ":camp_faction", minor_kingdoms_begin, minor_kingdoms_end),
(faction_slot_eq, ":camp_faction", slot_faction_state, sfs_active),
(party_get_slot, ":anchor", ":camp", slot_party_home_center),
(gt, ":anchor", 0),
	(try_begin), #horde moves
	(neg|check_quest_active, "qst_ernak_quest"),
	(neq, "$g_last_rest_center", ":camp"), #dont do this if player is here
	(party_slot_eq, ":camp", slot_party_been_sacked, 0),
	(neq, ":icon", "icon_steppe_lord"),
	(neq, ":icon", "icon_ship"),
	(store_random_in_range, ":rng", 0, 180), #dont let them move all the time, adjust this if necessary
	(eq, ":rng", 1),
	(party_get_position, pos1, "p_religious_site_18"), #use a static landmark
        (map_get_land_position_around_position, pos2, pos1, 75), #migration range nomads dont like water so use land position only
	(get_distance_between_positions, ":dist", pos2, pos1),
	(gt, ":dist", 5),
	(assign, ":cont", 1),
		(try_for_range, ":other_party", centers_begin, last_static_party),
		(eq, ":cont", 1),
		(neq, ":other_party", ":camp"),
		(neq, ":other_party", ":anchor"),
		(party_get_position, pos3, ":other_party"),
		(get_distance_between_positions, ":dist", pos3, pos2),
		(lt, ":dist", 3), #dont let them settle on top of others
		(assign, ":cont", 0),
		(try_end),
	(eq, ":cont", 1),
	(party_set_position, ":anchor", pos2),
	(party_get_current_terrain, ":terrain_type", ":anchor"),
	(neq, ":terrain_type", rt_water),
	(neq, ":terrain_type", rt_river),
	(neq, ":terrain_type", rt_bridge),
	(neq, ":terrain_type", rt_deep_water),
	(party_set_icon, ":camp", "icon_steppe_lord"),
        (party_set_ai_behavior, ":camp", ai_bhvr_travel_to_point),
        (party_set_ai_target_position, ":camp", pos2),
	(str_store_faction_name, s13, ":camp_faction"),
	(display_message, "@The {s13} are on the move and their enemies are petrified with fear."),
	(party_set_flags, ":camp", pf_always_visible, 0),
	(party_set_flags, ":camp", pf_is_static, 0),
	(party_set_flags, ":camp", pf_quest_party, 1), #this keeps others from attacking them while they move
	(else_try),
	(eq, ":icon", "icon_steppe_lord"),
	(party_get_position, pos1, ":anchor"),
	(party_get_position, pos2, ":camp"),
	(get_distance_between_positions, ":dist", pos2, pos1),
	(this_or_next|party_slot_eq, ":camp", slot_party_been_sacked, 1),
	(lt, ":dist", 2),
	(party_get_current_terrain, ":terrain_type", ":camp"),
	(neq, ":terrain_type", rt_water),
	(neq, ":terrain_type", rt_river),
	(neq, ":terrain_type", rt_bridge),
	(neq, ":terrain_type", rt_deep_water),
	(party_set_icon, ":camp", "icon_nomad_camp"),
	(party_set_ai_behavior, ":camp", ai_bhvr_hold),
	(store_faction_of_party, ":camp_faction", ":camp"),
	(str_store_faction_name, s13, ":camp_faction"),
	(call_script, "script_get_closest_center", ":camp"),
	(assign, ":nearest", reg0),
	(str_store_party_name, s12, ":nearest"),
	(display_message, "@The {s13} have settled near {s12}."),
	(party_set_flags, ":camp", pf_always_visible, 1),
	(party_set_flags, ":camp", pf_is_static, 1),
	(party_set_flags, ":camp", pf_quest_party, 0),
	(else_try),
	(this_or_next|eq, ":icon", "icon_ship"),
	(eq, ":icon", "icon_steppe_lord"),
	(get_party_ai_behavior, ":behavior", ":camp"),
	(neq, ":behavior", ai_bhvr_travel_to_point),
	(party_get_position, pos1, ":anchor"),
        (party_set_ai_behavior, ":camp", ai_bhvr_travel_to_point),
        (party_set_ai_target_position, ":camp", pos1),
	(try_end),
(try_end),
 ]),

(24,[
  (check_quest_active, "qst_haddingrs_revenge"),
  (this_or_next|quest_slot_eq, "qst_haddingrs_revenge", slot_quest_current_state, 10),
  (quest_slot_eq, "qst_haddingrs_revenge", slot_quest_current_state, 11),
  (quest_get_slot, ":timer", qst_haddingrs_revenge, slot_quest_temp_slot),
  (store_current_day, ":cur_day"),
  (val_sub, ":timer", ":cur_day"),
  (val_max, ":timer", 0),
  (eq, ":timer", 0),
  (jump_to_menu, "mnu_haddingrs_revenge_message"),
]),

(0.7,[
    (check_quest_active, "qst_haddingrs_revenge"),
    (eq, "$g_player_is_captive", 1),
    (try_begin),
        (quest_slot_eq, "qst_haddingrs_revenge", slot_quest_current_state, 13),
        (set_fixed_point_multiplier, 100),
        (init_position, pos32),
        (position_set_x, pos32, -9500),
        (position_set_y, pos32, 15500),
        (party_get_position, pos31, "p_transporter"),
        (get_distance_between_positions, ":distance", pos31, pos32),
        (try_begin),
            (le, ":distance", 250),
            (init_position, pos33),
            (position_set_x, pos33, -9500),
            (position_set_y, pos33, 15300),
            (party_set_position, "p_main_party", pos33),
            (set_camera_follow_party, "p_main_party"),
            (rest_for_hours, 0, 0, 0),
            (assign, "$g_player_is_captive", 0),
            #(party_set_flags, "p_transporter", pf_is_ship, 0),
            (disable_party, "p_transporter"),
            #(change_screen_return),
            (jump_to_menu, "$auto_menu"),
            (assign, "$auto_menu", -1),
            #(store_current_hours, "$g_check_autos_at_hour"),	#new 02.01.14
        (else_try),
            (set_camera_follow_party, "p_transporter"),
        (try_end),
    (else_try),
        (quest_slot_eq, "qst_haddingrs_revenge", slot_quest_current_state, 14),
        (set_fixed_point_multiplier, 100),
        (init_position, pos32),
        (party_get_position, pos32, "p_haddingrs_revenge_aesti_village_1"),
        (party_get_position, pos31, "p_haddingrs_revenge_raiding_camp"),
        (get_distance_between_positions, ":distance", pos31, pos32),
        (try_begin),
            (le, ":distance", 150),
            (party_set_position, "p_main_party", pos32),
            (set_camera_follow_party, "p_main_party"),
            (rest_for_hours, 0, 0, 0),
            (assign, "$g_player_is_captive", 0),

            (start_encounter, "p_haddingrs_revenge_aesti_village_1"),
            (assign, "$auto_menu", -1),
            #(store_current_hours, "$g_check_autos_at_hour"),	#new 02.01.14
        (else_try),
            (set_camera_follow_party, "p_haddingrs_revenge_raiding_camp"),
        (try_end),
    (else_try),
        (quest_slot_eq, "qst_haddingrs_revenge", slot_quest_current_state, 15),
        (set_fixed_point_multiplier, 100),
        (init_position, pos32),
        (party_get_position, pos32, "p_haddingrs_revenge_aesti_sacred_grove"),
        (party_get_position, pos31, "p_haddingrs_revenge_raiding_camp"),
        (get_distance_between_positions, ":distance", pos31, pos32),
        (try_begin),
            (le, ":distance", 150),
            (party_set_position, "p_main_party", pos32),
            (set_camera_follow_party, "p_main_party"),
            (rest_for_hours, 0, 0, 0),
            (assign, "$g_player_is_captive", 0),

            (start_encounter, "p_haddingrs_revenge_aesti_sacred_grove"),
            (assign, "$auto_menu", -1),
            #(store_current_hours, "$g_check_autos_at_hour"),	#new 02.01.14
        (else_try),
            (set_camera_follow_party, "p_haddingrs_revenge_raiding_camp"),
        (try_end),
    (else_try),
        (quest_slot_eq, "qst_haddingrs_revenge", slot_quest_current_state, 16),
        (set_fixed_point_multiplier, 100),
        (init_position, pos32),
        (party_get_position, pos32, "p_haddingrs_revenge_aesti_trade_post"),
        (party_get_position, pos31, "p_haddingrs_revenge_raiding_camp"),
        (get_distance_between_positions, ":distance", pos31, pos32),
        (try_begin),
            (le, ":distance", 500),
            (party_set_position, "p_main_party", pos32),
            (set_camera_follow_party, "p_main_party"),
            (rest_for_hours, 0, 0, 0),
            (assign, "$g_player_is_captive", 0),

            (start_encounter, "p_haddingrs_revenge_aesti_trade_post"),
            (assign, "$auto_menu", -1),
            #(store_current_hours, "$g_check_autos_at_hour"),	#new 02.01.14
        (else_try),
            (set_camera_follow_party, "p_haddingrs_revenge_raiding_camp"),
        (try_end),
    (else_try),
        (quest_slot_eq, "qst_haddingrs_revenge", slot_quest_current_state, 19),
        (set_fixed_point_multiplier, 100),
        (init_position, pos32),
        (party_get_position, pos32, "p_haddingrs_revenge_aesti_trade_post"),
        (party_get_position, pos31, "p_haddingrs_revenge_raiding_camp"),
        (get_distance_between_positions, ":distance", pos31, pos32),
        (try_begin),
            (le, ":distance", 150),
            (party_set_position, "p_main_party", pos32),
            (set_camera_follow_party, "p_main_party"),
            (rest_for_hours, 0, 0, 0),
            (assign, "$g_player_is_captive", 0),

            (start_encounter, "p_haddingrs_revenge_aesti_trade_post"),
            (assign, "$auto_menu", -1),
            #(store_current_hours, "$g_check_autos_at_hour"),	#new 02.01.14
        (else_try),
            (set_camera_follow_party, "p_haddingrs_revenge_raiding_camp"),
        (try_end),
    (else_try),
        (quest_slot_eq, "qst_haddingrs_revenge", slot_quest_current_state, 23),
        (set_fixed_point_multiplier, 100),
        (init_position, pos32),
        (party_get_position, pos32, "p_haddingrs_revenge_aesti_village_1"),
        (party_get_position, pos31, "p_haddingrs_revenge_raiding_camp"),
        (get_distance_between_positions, ":distance", pos31, pos32),
        (try_begin),
            (le, ":distance", 150),
            (party_set_position, "p_main_party", pos32),
            (set_camera_follow_party, "p_main_party"),
            (rest_for_hours, 0, 0, 0),
            (assign, "$g_player_is_captive", 0),

            (start_encounter, "p_haddingrs_revenge_raiding_camp"),
            (assign, "$auto_menu", -1),
            #(store_current_hours, "$g_check_autos_at_hour"),	#new 02.01.14
        (else_try),
            (set_camera_follow_party, "p_haddingrs_revenge_raiding_camp"),
        (try_end),
    (else_try),
        (quest_slot_eq, "qst_haddingrs_revenge", slot_quest_current_state, 30),
        (set_fixed_point_multiplier, 100),
        (init_position, pos32),
        (party_get_position, pos32, "p_dani_village"),
        (party_get_position, pos31, "p_haddingrs_revenge_raiding_camp"),
        (get_distance_between_positions, ":distance", pos31, pos32),
        (try_begin),
            (le, ":distance", 150),
            (set_camera_follow_party, "p_main_party"),
            (rest_for_hours, 0, 0, 0),
            (assign, "$g_player_is_captive", 0),

            (start_encounter, "p_haddingrs_revenge_raiding_camp"),
            (assign, "$auto_menu", -1),
        (else_try),
            (set_camera_follow_party, "p_haddingrs_revenge_raiding_camp"),
        (try_end),
    (try_end),
]),

(5,[
(try_begin),
(eq, "$majorian_death", 0), #no player involvement
(gt, "$total_days_passed", 550),
(faction_slot_eq, "fac_kingdom_1", slot_faction_state, sfs_active),
(faction_slot_eq, "fac_kingdom_1", slot_faction_leader, "trp_kingdom_1_lord"),
(neg|faction_slot_eq, "fac_kingdom_1", slot_faction_marshall, "trp_kingdom_1_lord"),
(troop_slot_eq, "trp_kingdom_1_lord", slot_troop_occupation, slto_kingdom_hero), #still alive
(troop_get_slot, ":leaded_party", "trp_kingdom_1_lord", slot_troop_leaded_party),
(gt, ":leaded_party", 0),
(party_is_active, ":leaded_party"),
(neq, ":leaded_party", "$enlisted_party"), #not if the player is freelancing in this party
(party_is_in_any_town, ":leaded_party"),
(party_get_cur_town, ":cur_attached_town", ":leaded_party"),
(is_between, ":cur_attached_town", walled_centers_begin, walled_centers_end),
(neg|party_slot_ge, ":cur_attached_town", slot_center_is_besieged_by, 1),
(troop_slot_eq, "trp_knight_1_1", slot_troop_occupation, slto_kingdom_hero),
(neg|troop_slot_ge, "trp_knight_1_1", slot_troop_prisoner_of_party, 1),
(store_troop_faction, ":lord_faction", "trp_knight_1_1"),
(eq, ":lord_faction", "fac_kingdom_1"),
(party_detach, ":leaded_party"),
(call_script, "script_remove_hero_prisoners", ":leaded_party"),
(remove_party, ":leaded_party"),
(troop_set_slot, "trp_kingdom_1_lord", slot_troop_leaded_party, -1),
(troop_set_slot, "trp_kingdom_1_lord", slot_troop_occupation, dplmc_slto_dead),
(faction_set_slot, "fac_kingdom_1", slot_faction_leader, "trp_knight_1_1"),
	(try_for_range, ":center_no", centers_begin, centers_end),
	(party_get_slot, ":town_lord", ":center_no", slot_town_lord),
	(eq, ":town_lord", "trp_kingdom_1_lord"),
	(party_set_slot, ":center_no", slot_town_lord, -1),
	(try_end),
	(try_begin),
	(check_quest_active, "qst_agrippinus_quest"),
	(quest_set_slot,"qst_agrippinus_quest", slot_quest_current_state, 11),
	(call_script, "script_cancel_quest", "qst_agrippinus_quest"),
	(disable_party, "p_agrippinus_quest_villa"),
	(try_end),
(call_script, "script_change_troop_faction", "trp_kingdom_1_lord", "fac_outlaws"),
(assign, "$majorian_death", 1),
(str_store_party_name_link, s4, ":cur_attached_town"),
(str_store_troop_name_link, s10, "trp_kingdom_1_lord"),
(display_log_message, "@{s10} has died in {s4} and major riots have erupted across the empire!"),
	(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
	(party_slot_eq, ":center_no", slot_center_is_besieged_by, -1),
	(store_faction_of_party, ":faction", ":center_no"),
	(eq, ":faction", "fac_kingdom_1"),
 	(set_spawn_radius, 0),
	(spawn_around_party, ":center_no", "pt_rebel_army"),
	(assign, ":rebel_army", reg0),
	(party_set_name, ":rebel_army", "@Rioting Citizens"),
	(party_set_slot, ":rebel_army", slot_party_home_center, ":center_no"),
	(party_add_members, ":rebel_army", "trp_bandit", 300),
	(party_add_members, ":rebel_army", "trp_brigand", 300),
	(party_set_faction, ":rebel_army", "fac_outlaws"),
	(party_ignore_player, ":rebel_army", 1),
	(party_set_ai_behavior, ":rebel_army", ai_bhvr_attack_party),
	(party_set_ai_object, ":rebel_army", ":center_no"),
	(party_set_flags, ":rebel_army", pf_default_behavior, 1),
	(party_set_slot, ":rebel_army", slot_party_ai_substate, 1),
	(party_set_slot, ":center_no", slot_center_is_besieged_by, ":rebel_army"),
	(store_current_hours, ":cur_hours"),
	(party_set_slot, ":center_no", slot_center_siege_begin_hours, ":cur_hours"),
	(call_script, "script_village_set_state", ":center_no", svs_under_siege),
	(try_end),
	(try_begin),
        (eq, "$g_infinite_camping", 0),
	(jump_to_menu, "mnu_majorian_death"),
	(try_end),
(try_end),

(try_begin), #babai leaves if the player burns his village
(main_party_has_troop, "trp_npc25"),
(store_faction_of_party, ":party_faction", "p_iazyges_village"),
(eq, ":party_faction", "fac_neutral"), #razed by player
(party_remove_members, "p_main_party", "trp_npc25", 1),
(str_store_troop_name_link, s39, "trp_npc25"),
(faction_get_color, ":color", "fac_player_supporters_faction"),
(display_log_message, "@{s39} has left your party because you razed and burned his village.", ":color"),
(call_script, "script_change_player_relation_with_troop", "trp_npc25", -100),
(troop_set_slot, "trp_npc25", slot_troop_occupation, slto_kingdom_hero),
(call_script, "script_change_troop_faction", "trp_npc25", "fac_outlaws"),
(try_end),
]),

]#end of file