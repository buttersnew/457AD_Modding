from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *

from module_constants import *

from compiler import *
####################################################################################################################
#  Each trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Delay interval: Time to wait before applying the consequences of the trigger
#    After its conditions have been evaluated as true.
# 3) Re-arm interval. How much time must pass after applying the consequences of the trigger for the trigger to become active again.
#    You can put the constant ti_once here to make sure that the trigger never becomes active again after it fires once.
# 4) Conditions block (list). This must be a valid operation block. See header_operations.py for reference.
#    Every time the trigger is checked, the conditions block will be executed.
#    If the conditions block returns true, the consequences block will be executed.
#    If the conditions block is empty, it is assumed that it always evaluates to true.
# 5) Consequences block (list). This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

# Some constants for use below
merchant_inventory_space = 30
num_merchandise_goods = 36



triggers = [

    (0,0,ti_once,[],[
      (call_script, "script_add_notification_menu","mnu_religion_selection",0,0),
    ]),

    (0,0,ti_once,[
    (troop_slot_eq, "trp_player", slot_troop_culture, 0),
    ],[
    (call_script, "script_add_notification_menu","mnu_culture_selection",0,0),
    ]),

# Tutorial:
  (0.1, 0, ti_once, [(map_free,0)], [(dialog_box,"str_tutorial_map1")]),

# Refresh Merchants
  (0.0, 0, 168.0, [],
  [
    (call_script, "script_refresh_center_inventories"),
                     ]),

# Refresh Armor sellers
  (0.0, 0, 168.0, [],
  [
    (call_script, "script_refresh_center_armories"),
                     ]),

# Refresh Weapon sellers
  (0.0, 0, 168.0, [],
  [
    (call_script, "script_refresh_center_weaponsmiths"),
                     ]),

# Refresh Horse sellers
  (0.0, 0, 168.0, [],
  [
    (call_script, "script_refresh_center_stables"),
                     ]),



  (5.7, 0, 0.0,
  [
    (store_num_parties_of_template, reg2, "pt_manhunters"),
    (lt, reg2, 4)
  ],
  [
    (set_spawn_radius, 1),
    # (store_add, ":p_town_22_plus_one", "p_town_22", 1), #SB : obvious random range
    (store_random_in_range, ":selected_town", towns_begin, towns_end),
    (spawn_around_party, ":selected_town", "pt_manhunters"),
  ]),



  (1.0, 0.0, 0.0, [
  (check_quest_active, "qst_track_down_bandits"),
  (neg|check_quest_failed, "qst_track_down_bandits"),
  (neg|check_quest_succeeded, "qst_track_down_bandits"),

  ],
   [
    (quest_get_slot, ":bandit_party", "qst_track_down_bandits", slot_quest_target_party),
	(try_begin),
		(party_is_active, ":bandit_party"),
		(store_faction_of_party, ":bandit_party_faction", ":bandit_party"),
		(neg|is_between, ":bandit_party_faction", kingdoms_begin, kingdoms_end), #ie, the party has not respawned as a non-bandit


		(assign, ":spot_range", 8),
		(try_begin),
			(is_currently_night),
			(assign, ":spot_range", 5),
		(try_end),

		(try_for_parties, ":party"),
			(gt, ":party", "p_spawn_points_end"),

			(store_faction_of_party, ":faction", ":party"),
			(is_between, ":faction", kingdoms_begin, kingdoms_end),


			(store_distance_to_party_from_party, ":distance", ":party", ":bandit_party"),
			(lt, ":distance", ":spot_range"),
			(try_begin),
				(eq, "$cheat_mode", 1),
				(str_store_party_name, s4, ":party"),
				(display_message, "@{!}DEBUG -- Wanted bandits spotted by {s4}"),
			(try_end),

			(call_script, "script_get_closest_center", ":bandit_party"),
			(assign, ":nearest_center", reg0),
#			(try_begin),
#				(get_party_ai_current_behavior, ":behavior", ":party"),
#				(eq, ":behavior", ai_bhvr_attack_party),
#				(call_script, "script_add_log_entry",  logent_party_chases_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
#			(else_try),
#				(eq, ":behavior", ai_bhvr_avoid_party),
#				(call_script, "script_add_log_entry",  logent_party_runs_from_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
#			(else_try),
			(call_script, "script_add_log_entry",  logent_party_spots_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
#			(try_end),
		(try_end),
	(else_try), #Party not found
		(display_message, "str_bandits_eliminated_by_another"),
        (call_script, "script_abort_quest", "qst_track_down_bandits", 0),
	(try_end),
   ]),


  (2.0, 0, 0, [(store_random_party_of_template, reg(2), "pt_prisoner_train_party"),
               (party_is_in_any_town,reg(2)),
               ],
              [(store_faction_of_party, ":faction_no", reg(2)),
               (call_script,"script_cf_select_random_walled_center_with_faction", ":faction_no", -1),
               (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
               (party_set_ai_object,reg(2),reg0),
               (party_set_flags, reg(2), pf_default_behavior, 0),
            ]),


  (4.0, 0, 0.0,
   [
     (eq, "$caravan_escort_state", 1), #cancel caravan_escort_state if caravan leaves the destination
     (assign, ":continue", 0),
     (try_begin),
       (neg|party_is_active, "$caravan_escort_party_id"),
       (assign, ":continue", 1),
     (else_try),
       (get_party_ai_object, ":ai_object", "$caravan_escort_party_id"),
       (neq, ":ai_object", "$caravan_escort_destination_town"),
       (assign, ":continue", 1),
     (try_end),
     (eq, ":continue", 1),
     ],
   [
     (assign, "$caravan_escort_state", 0),
     ]),


#Kingdom Parties
  (1.0, 0, 0.0, [],
   [(try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
      (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
##      (neq, ":cur_kingdom", "fac_player_supporters_faction"),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_forager),
##      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_scout),
##      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_patrol),
##      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_messenger),
##      (try_end),
      (try_begin),
        (store_random_in_range, ":random_no", 0, 100),
        (lt, ":random_no", 10),
        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_kingdom_caravan),
      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_prisoner_train),
##      (try_end),
    (try_end),
    ]),

###########################################################################
### Random Governer Quest triggers
###########################################################################

# Incriminate Loyal Advisor quest
  (0.2, 0.0, 0.0,
   [
       (check_quest_active, "qst_incriminate_loyal_commander"),
       (neg|check_quest_concluded, "qst_incriminate_loyal_commander"),
       (quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_current_state, 2),
       (quest_get_slot, ":quest_target_center", "qst_incriminate_loyal_commander", slot_quest_target_center),
       (quest_get_slot, ":quest_target_party", "qst_incriminate_loyal_commander", slot_quest_target_party),
       (try_begin),
         (neg|party_is_active, ":quest_target_party"),
         (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_current_state, 3),
         (call_script, "script_fail_quest", "qst_incriminate_loyal_commander"),
       (else_try),
         (party_is_in_town, ":quest_target_party", ":quest_target_center"),
         (remove_party, ":quest_target_party"),
         (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_current_state, 3),
         (quest_get_slot, ":quest_object_troop", "qst_incriminate_loyal_commander", slot_quest_object_troop),
         (assign, ":num_available_factions", 0),
         (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
           (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
           (neq, ":faction_no", "fac_player_supporters_faction"),
           (neg|quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_target_faction, ":faction_no"),
           (val_add, ":num_available_factions", 1),
         (try_end),
         (try_begin),
           (gt, ":num_available_factions", 0),
           (store_random_in_range, ":random_faction", 0, ":num_available_factions"),
           (assign, ":target_faction", -1),
           (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
             (eq, ":target_faction", -1),
             (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
             (neq, ":faction_no", "fac_player_supporters_faction"),
             (neg|quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_target_faction, ":faction_no"),
             (val_sub, ":random_faction", 1),
             (lt, ":random_faction", 0),
             (assign, ":target_faction", ":faction_no"),
           (try_end),
         (try_end),
         (try_begin),
           (gt, ":target_faction", 0),
           (call_script, "script_change_troop_faction", ":quest_object_troop", ":target_faction"),
         (else_try),
           (call_script, "script_change_troop_faction", ":quest_object_troop", "fac_robber_knights"),
         (try_end),
         (call_script, "script_succeed_quest", "qst_incriminate_loyal_commander"),
       (try_end),
    ],
   []
   ),
# Runaway Peasants quest
  (0.2, 0.0, 0.0,
   [
       (check_quest_active, "qst_bring_back_runaway_serfs"),
       (neg|check_quest_concluded, "qst_bring_back_runaway_serfs"),
       (quest_get_slot, ":quest_object_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
       (quest_get_slot, ":quest_target_center", "qst_bring_back_runaway_serfs", slot_quest_target_center),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_1"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_1", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_1"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_1", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_1"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_1"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_1", ":quest_target_center"),
         (try_end),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_2"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_2", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_2"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_2", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_2"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_2"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_2", ":quest_target_center"),
         (try_end),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_3"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_3", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_3"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_3", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_3"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_3"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_3", ":quest_target_center"),
         (try_end),
       (try_end),
       (assign, ":sum_removed", "$qst_bring_back_runaway_serfs_num_parties_returned"),
       (val_add, ":sum_removed", "$qst_bring_back_runaway_serfs_num_parties_fleed"),
       (ge, ":sum_removed", 3),
       (try_begin),
         (ge, "$qst_bring_back_runaway_serfs_num_parties_returned", 3),
         (call_script, "script_succeed_quest", "qst_bring_back_runaway_serfs"),
       (else_try),
         (eq, "$qst_bring_back_runaway_serfs_num_parties_returned", 0),
         (call_script, "script_fail_quest", "qst_bring_back_runaway_serfs"),
       (else_try),
         (call_script, "script_conclude_quest", "qst_bring_back_runaway_serfs"),
       (try_end),
    ],
   []
   ),

# Follow Spy quest
  (0.5, 0.0, 0.0,
   [
       (check_quest_active, "qst_follow_spy"),
       (eq, "$qst_follow_spy_no_active_parties", 0),
       (quest_get_slot, ":quest_giver_center", "qst_follow_spy", slot_quest_giver_center),
       (quest_get_slot, ":quest_object_center", "qst_follow_spy", slot_quest_object_center),
       (assign, ":abort_meeting", 0),
       (try_begin),
         (this_or_next|ge, "$qst_follow_spy_run_away", 2),
         (this_or_next|neg|party_is_active, "$qst_follow_spy_spy_party"),
         (neg|party_is_active, "$qst_follow_spy_spy_partners_party"),
       (else_try),
         (eq, "$qst_follow_spy_meeting_state", 0),
         (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_follow_spy_spy_party"),
         (try_begin),
           (assign, ":min_distance", 3),
           (try_begin),
             (is_currently_night),
             (assign, ":min_distance", 1),
           (try_end),
           (le, ":cur_distance", ":min_distance"),
           (store_distance_to_party_from_party, ":player_distance_to_quest_giver_center", "p_main_party", ":quest_giver_center"),
           (gt, ":player_distance_to_quest_giver_center", 1),
           (val_add, "$qst_follow_spy_run_away", 1),
           (try_begin),
             (eq, "$qst_follow_spy_run_away", 2),
             (assign, ":abort_meeting", 1),
             (display_message, "str_qst_follow_spy_noticed_you"),
           (try_end),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "$qst_follow_spy_spy_partners_party", "$qst_follow_spy_spy_party"),
           (le, ":cur_distance", 1),
           (party_attach_to_party, "$qst_follow_spy_spy_party", "$qst_follow_spy_spy_partners_party"),
           (assign, "$qst_follow_spy_meeting_state", 1),
           (assign, "$qst_follow_spy_meeting_counter", 0),
         (try_end),
       (else_try),
         (eq, "$qst_follow_spy_meeting_state", 1),
         (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_follow_spy_spy_partners_party"),
         (try_begin),
           (le, ":cur_distance", 1),
           (party_detach, "$qst_follow_spy_spy_party"),
           (val_add, "$qst_follow_spy_run_away", 1),
           (try_begin),
             (eq, "$qst_follow_spy_run_away", 2),
             (assign, ":abort_meeting", 1),
             (display_message, "str_qst_follow_spy_noticed_you"),
           (try_end),
         (else_try),
           (val_add, "$qst_follow_spy_meeting_counter", 1),
           (gt, "$qst_follow_spy_meeting_counter", 4),
           (party_detach, "$qst_follow_spy_spy_party"),
           (assign, ":abort_meeting", 1),
           (assign, "$qst_follow_spy_meeting_state", 2),
         (try_end),
       (try_end),
       (try_begin),
         (eq, ":abort_meeting", 1),
         (party_set_ai_object, "$qst_follow_spy_spy_party", ":quest_giver_center"),

         (party_set_ai_object, "$qst_follow_spy_spy_partners_party", ":quest_object_center"),

         (party_set_ai_behavior, "$qst_follow_spy_spy_party", ai_bhvr_travel_to_party),
         (party_set_ai_behavior, "$qst_follow_spy_spy_partners_party", ai_bhvr_travel_to_party),
         (party_set_flags, "$qst_follow_spy_spy_party", pf_default_behavior, 0),
         (party_set_flags, "$qst_follow_spy_spy_partners_party", pf_default_behavior, 0),
       (try_end),
       (assign, ":num_active", 0),
       (try_begin),
         (party_is_active, "$qst_follow_spy_spy_party"),
         (val_add, ":num_active", 1),
         (party_is_in_town, "$qst_follow_spy_spy_party", ":quest_giver_center"),
         (remove_party, "$qst_follow_spy_spy_party"),
         (assign, "$qst_follow_spy_spy_back_in_town", 1),
         (val_sub, ":num_active", 1),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_follow_spy_spy_partners_party"),
         (val_add, ":num_active", 1),
         (party_is_in_town, "$qst_follow_spy_spy_partners_party", ":quest_object_center"),
         (remove_party, "$qst_follow_spy_spy_partners_party"),
         (assign, "$qst_follow_spy_partner_back_in_town", 1),
         (val_sub, ":num_active", 1),
       (try_end),
       (try_begin),
         (eq, "$qst_follow_spy_partner_back_in_town",1),
         (eq, "$qst_follow_spy_spy_back_in_town",1),
         (call_script, "script_fail_quest", "qst_follow_spy"),
       (try_end),
       (try_begin),
         (eq, ":num_active", 0),
         (assign, "$qst_follow_spy_no_active_parties", 1),
         (party_count_prisoners_of_type, ":num_spies", "p_main_party", "trp_spy"),
         (party_count_prisoners_of_type, ":num_spy_partners", "p_main_party", "trp_spy_partner"),
         (gt, ":num_spies", 0),
         (gt, ":num_spy_partners", 0),
         (call_script, "script_succeed_quest", "qst_follow_spy"),
       (try_end),
    ],
   []
   ),
#########################################################################
# Random MERCHANT quest triggers
####################################
 # Apply interest to merchants guild debt  1% per week
  (24.0 * 7, 0.0, 0.0,
   [],
   [
       (val_mul,"$debt_to_merchants_guild",101),
       (val_div,"$debt_to_merchants_guild",100)
    ]
   ),

  (0.3, 0, 1.1, [
                 (check_quest_active, "qst_escort_merchant_caravan"),
                 (quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                 (neg|party_is_active,":quest_target_party"),
                ],
                [
                 (call_script, "script_abort_quest", "qst_escort_merchant_caravan", 2),
                ]),

# Troublesome bandits
  (0.3, 0.0, 1.1, [(check_quest_active, "qst_troublesome_bandits"),
                   (neg|check_quest_failed, "qst_troublesome_bandits"),
                   (store_num_parties_destroyed, ":cur_eliminated", "pt_troublesome_bandits"),
                   (lt, "$qst_troublesome_bandits_eliminated", ":cur_eliminated"),
                   (store_num_parties_destroyed_by_player, ":cur_eliminated_by_player", "pt_troublesome_bandits"),
                   (eq, ":cur_eliminated_by_player", "$qst_troublesome_bandits_eliminated_by_player"),
                   ],
                  [(display_message, "str_bandits_eliminated_by_another"),
                   (call_script, "script_abort_quest", "qst_troublesome_bandits", 0),
                   ]),

  (0.3, 0.0, 1.1, [(check_quest_active, "qst_troublesome_bandits"),
                   (neg|check_quest_succeeded, "qst_troublesome_bandits"),
                   (store_num_parties_destroyed, ":cur_eliminated", "pt_troublesome_bandits"),
                   (lt, "$qst_troublesome_bandits_eliminated", ":cur_eliminated"),
                   (store_num_parties_destroyed_by_player, ":cur_eliminated_by_player", "pt_troublesome_bandits"),
                   (neq, ":cur_eliminated_by_player", "$qst_troublesome_bandits_eliminated_by_player"),
                   ],
                  [(call_script, "script_succeed_quest", "qst_troublesome_bandits"),]),

# Kidnapped girl:
   (1, 0, 0,
   [(check_quest_active, "qst_kidnapped_girl"),
    (quest_get_slot, ":quest_target_party", "qst_kidnapped_girl", slot_quest_target_party),
    (party_is_active, ":quest_target_party"),
    (party_is_in_any_town, ":quest_target_party"),
    (remove_party, ":quest_target_party"),
    ],
   []
   ),


#Rebellion changes begin
#move

  (0, 0, 24 * 14,
   [
        (try_for_range, ":pretender", pretenders_begin, pretenders_end),
          (troop_set_slot, ":pretender", slot_troop_cur_center, 0),
          (neq, ":pretender", "$supported_pretender"),
          (troop_get_slot, ":target_faction", ":pretender", slot_troop_original_faction),
          (faction_slot_eq, ":target_faction", slot_faction_state, sfs_active),
          (faction_slot_eq, ":target_faction", slot_faction_has_rebellion_chance, 1),
          (neg|troop_slot_eq, ":pretender", slot_troop_occupation, slto_kingdom_hero),

          (assign, ":break", 30),
          (try_for_range, ":unused", 0, ":break"),
            (troop_slot_eq, ":pretender", slot_troop_cur_center, 0),
            (store_random_in_range, ":town", towns_begin, towns_end),
            (party_get_slot, ":town_lord", ":town", slot_town_lord),
            (ge, ":town_lord", "trp_player"), #not unassigned
            (store_faction_of_party, ":town_faction", ":town"),
            (store_relation, ":relation", ":town_faction", ":target_faction"),
            (le, ":relation", 0), #fail if nothing qualifies

            (troop_set_slot, ":pretender", slot_troop_cur_center, ":town"),
            (try_begin), #SB : cheat mode
              (eq, "$cheat_mode", 1),
              (str_store_troop_name_link, 4, ":pretender"),
              (str_store_party_name_link, 5, ":town"),
              (display_message, "@{!}{s4} is in {s5}"),
            (try_end),
            (try_begin), #SB : actually give out base gold and some renown
              (ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
              (call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", 100, ":pretender"),
              # do host relations
              (assign, ":renown", 5),
              (try_begin),
                (neq, ":town_lord", "trp_player"),
                (store_random_in_range, ":relation", -3, 4),
                (call_script, "script_troop_change_relation_with_troop", ":pretender", ":town_lord", ":relation"),
              (try_end),
              #do other relations
              (call_script, "script_get_heroes_attached_to_center", ":town", "p_temp_party"),
              (party_get_num_companion_stacks, ":num_stacks", "p_temp_party"),
              (try_for_range, ":stack_no", 0, ":num_stacks"),
                (party_stack_get_troop_id, ":troop_no", "p_temp_party", ":stack_no"),
                (neq, ":troop_no", ":pretender"),
                (neq, ":troop_no", ":town_lord"), #double effect if actually at home?
                (store_random_in_range, ":relation", -2, 3),
                (call_script, "script_troop_change_relation_with_troop", ":pretender", ":troop_no", ":relation"),
                (try_begin), #a bit of variation
                  (ge, ":relation", 0),
                  (val_add, ":renown", 1),
                (else_try),
                  (val_sub, ":renown", 1),
                (try_end),
              (try_end),
              (call_script, "script_change_troop_renown", ":troop_no", ":renown"),
            (try_end),
            (assign, ":break", 0),
          (try_end),

#        (try_for_range, ":rebel_faction", rebel_factions_begin, rebel_factions_end),
#            (faction_get_slot, ":rebellion_status", ":rebel_faction", slot_faction_state),
#            (eq, ":rebellion_status", sfs_inactive_rebellion),
#            (faction_get_slot, ":pretender", ":rebel_faction", slot_faction_leader),
#            (faction_get_slot, ":target_faction", ":rebel_faction", slot_faction_rebellion_target),#

#            (store_random_in_range, ":town", towns_begin, towns_end),
#            (store_faction_of_party, ":town_faction", ":town"),
#            (store_relation, ":relation", ":town_faction", ":target_faction"),
#            (le, ":relation", 0), #fail if nothing qualifies

 #           (faction_set_slot, ":rebel_faction", slot_faction_inactive_leader_location, ":town"),
        (try_end),
       ],
[]
),
#Rebellion changes end

#NPC system changes begin
#Move unemployed NPCs around taverns
   (24 * 15 , 0, 0,
   [
    (call_script, "script_update_companion_candidates_in_taverns"),
    ],
   []
   ),

#Process morale and determine personality clashes
  (0, 0, 24,
   [],
[

#Count NPCs in party and get the "grievance divisor", which determines how fast grievances go away
#Set their relation to the player
        (assign, ":npcs_in_party", 0),
        (assign, ":grievance_divisor", 100),
        (try_for_range, ":npc1", companions_begin, companions_end),
            (main_party_has_troop, ":npc1"),
            (val_add, ":npcs_in_party", 1),
        (try_end),
        (val_sub, ":grievance_divisor", ":npcs_in_party"),
        (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
        (val_add, ":grievance_divisor", ":persuasion_level"),
        (assign, reg7, ":grievance_divisor"),

#        (display_message, "@{!}Process NPC changes. GD: {reg7}"),



##Activate personality clash from 24 hours ago
        (try_begin), #scheduled personality clashes require at least 24hrs together
             (gt, "$personality_clash_after_24_hrs", 0),
             (eq, "$disable_npc_complaints", 0),
             (try_begin),
                  (troop_get_slot, ":other_npc", "$personality_clash_after_24_hrs", slot_troop_personalityclash_object),
                  (main_party_has_troop, "$personality_clash_after_24_hrs"),
                  (main_party_has_troop, ":other_npc"),
                  (assign, "$npc_with_personality_clash", "$personality_clash_after_24_hrs"),
             (try_end),
             (assign, "$personality_clash_after_24_hrs", 0),
        (try_end),
#


        (try_for_range, ":npc", companions_begin, companions_end),
###Reset meeting variables
            (troop_set_slot, ":npc", slot_troop_turned_down_twice, 0),
            (try_begin),
                (troop_slot_eq, ":npc", slot_troop_met, 1),
                (troop_set_slot, ":npc", slot_troop_met_previously, 1),
            (try_end),

###Check for coming out of retirement
            (troop_get_slot, ":occupation", ":npc", slot_troop_occupation),
            (try_begin),
                (eq, ":occupation", slto_retirement),
                (troop_get_slot, ":renown_min", ":npc", slot_troop_return_renown),

                (str_store_troop_name, s31, ":npc"),
                (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
                (assign, reg4, ":player_renown"),
                (assign, reg5, ":renown_min"),
#                (display_message, "@{!}Test {s31}  for retirement return {reg4}, {reg5}."),

                (gt, ":player_renown", ":renown_min"),
                (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, 0),
                (troop_set_slot, ":npc", slot_troop_morality_penalties, 0),
                (troop_set_slot, ":npc", slot_troop_occupation, 0),
            (try_end),


#Check for political issues
			(try_begin), #does npc's opponent pipe up?
				(troop_slot_ge, ":npc", slot_troop_days_on_mission, 5),
				(troop_slot_eq, ":npc", slot_troop_current_mission, npc_mission_kingsupport),

				(troop_get_slot, ":other_npc", ":npc", slot_troop_kingsupport_opponent),
				(troop_slot_eq, ":other_npc", slot_troop_kingsupport_objection_state, 0),

				(troop_set_slot, ":other_npc", slot_troop_kingsupport_objection_state, 1),

				(str_store_troop_name, s3, ":npc"),
				(str_store_troop_name, s4, ":other_npc"),

				(try_begin),
					(eq, "$cheat_mode", 1),
					(display_message, "str_s4_ready_to_voice_objection_to_s3s_mission_if_in_party"),
				(try_end),
			(try_end),

			#Check for quitting
            (try_begin),
                (main_party_has_troop, ":npc"),

                (call_script, "script_dplmc_npc_morale", ":npc", 0), #SB : just the number
                (assign, ":npc_morale", reg0),

                (try_begin),
                    (lt, ":npc_morale", 20),
                    (store_random_in_range, ":random", 0, 100),
                    (val_add, ":npc_morale", ":random"),
                    (lt, ":npc_morale", 20),
                    (neq, "$disable_npc_complaints", 1), #SB : disable
                    (assign, "$npc_is_quitting", ":npc"),
                (try_end),

				#Reduce grievance over time (or augment, if party is overcrowded
                (troop_get_slot, ":grievance", ":npc", slot_troop_personalityclash_penalties),
                (val_mul, ":grievance", 90),
                (val_div, ":grievance", ":grievance_divisor"),
                (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, ":grievance"),

                (troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
                (val_mul, ":grievance", 90),
                (val_div, ":grievance", ":grievance_divisor"),
                (troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),


				#Change personality grievance levels
                (try_begin),
                    (this_or_next|troop_slot_ge, ":npc", slot_troop_personalityclash_state, 1),
                        (eq, "$disable_npc_complaints", 1),
                    (troop_get_slot, ":object", ":npc", slot_troop_personalityclash_object),
                    (main_party_has_troop, ":object"),
                    (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", slot_troop_personalityclash_state),
                (try_end),
                (try_begin),
                    (this_or_next|troop_slot_ge, ":npc", slot_troop_personalityclash2_state, 1),
                        (eq, "$disable_npc_complaints", 1),
                    (troop_get_slot, ":object", ":npc", slot_troop_personalityclash2_object),
                    (main_party_has_troop, ":object"),
                    (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", slot_troop_personalityclash2_state),
                (try_end),
                (try_begin),
                    (this_or_next|troop_slot_ge, ":npc", slot_troop_personalitymatch_state, 1),
                        (eq, "$disable_npc_complaints", 1),
                    (troop_get_slot, ":object", ":npc", slot_troop_personalitymatch_object),
                    (main_party_has_troop, ":object"),
                    (troop_get_slot, ":grievance", ":npc", slot_troop_personalityclash_penalties),
                    (val_mul, ":grievance", 9),
                    (val_div, ":grievance", 10),
                    (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, ":grievance"),
                (try_end),



#Check for new personality clashes

				#Active personality clash 1 if at least 24 hours have passed
                (try_begin),
                    (eq, "$disable_npc_complaints", 0),
                    (eq, "$npc_with_personality_clash", 0),
                    (eq, "$npc_with_personality_clash_2", 0),
                    (eq, "$personality_clash_after_24_hrs", 0),
                    (troop_slot_eq, ":npc", slot_troop_personalityclash_state, 0),
                    (troop_get_slot, ":other_npc", ":npc", slot_troop_personalityclash_object),
                    (main_party_has_troop, ":other_npc"),
                    (assign, "$personality_clash_after_24_hrs", ":npc"),
                (try_end),

				#Personality clash 2 and personality match is triggered by battles
				(try_begin),
					(eq, "$npc_with_political_grievance", 0),

					(troop_slot_eq, ":npc", slot_troop_kingsupport_objection_state, 1),
					(assign, "$npc_with_political_grievance", ":npc"),
				(try_end),

			#main party does not have troop, and the troop is a companion
			(else_try),
				(neg|main_party_has_troop, ":npc"),
				(eq, ":occupation", slto_player_companion),

                (troop_get_slot, ":days_on_mission", ":npc", slot_troop_days_on_mission),

                (try_begin), #debug
                    (eq, "$cheat_mode", 1),
                    (str_store_troop_name, s10, ":npc"),
                    (assign, reg0, ":days_on_mission"),
                    (display_message, "@Checking rejoin of {s10} days on mission: {reg0}"),
                (try_end),

                (try_begin),
                    (gt, ":days_on_mission", 0),
                    (val_sub, ":days_on_mission", 1),
                    (troop_set_slot, ":npc", slot_troop_days_on_mission, ":days_on_mission"),
                ##diplomacy begin
                (else_try),
                  (this_or_next|troop_slot_eq, ":npc", slot_troop_current_mission, dplmc_npc_mission_spy_request), #spy mission
                  (troop_slot_eq, ":npc", slot_troop_current_mission, dplmc_npc_mission_rescue_prisoner), #SB : rescue mission
                  (troop_slot_ge, ":npc", dplmc_slot_troop_mission_diplomacy, 1), #caught

                  (try_begin), #use hired blade for spy
                    (troop_slot_eq, ":npc", slot_troop_current_mission, dplmc_npc_mission_spy_request),
                    (troop_set_slot, "trp_hired_blade", slot_troop_mission_object, ":npc"),
                    (assign, "$npc_to_rejoin_party", "trp_hired_blade"),
                  (else_try), #use town walker
                    (troop_slot_eq, ":npc", slot_troop_current_mission, dplmc_npc_mission_rescue_prisoner),
                    (troop_get_slot, ":town_no", ":npc", slot_troop_town_with_contacts),
                    (store_random_in_range, ":slot_no", slot_center_walker_0_troop, slot_center_walker_0_troop + num_town_walkers),
                    (party_get_slot, ":walker_no", ":town_no", ":slot_no"),
                    (troop_set_slot, ":walker_no", slot_troop_mission_object, ":npc"),
                    (assign, "$npc_to_rejoin_party", ":walker_no"),
                  (try_end),
                ##diplomacy end
				(else_try),
					(troop_slot_ge, ":npc", slot_troop_current_mission, 1),

					#If the hero can join
					(this_or_next|neg|troop_slot_eq, ":npc", slot_troop_current_mission, npc_mission_rejoin_when_possible),
					(hero_can_join, "p_main_party"), #SB : fix this stupid bug

					(assign, "$npc_to_rejoin_party", ":npc"),
				(try_end),
            (try_end),
        (try_end),
    ]),


# #NPC system changes end
# #SB : change interval
# # Lady of the lake achievement
   # (12, 0, 0,
   # [
     # # (troop_get_type, ":is_female", "trp_player"),
     # (eq, "$character_gender", tf_female),

    # ],
   # [
     # (assign, ":inv_cap", companions_end),
     # (try_for_range, ":companion", companions_begin, ":inv_cap"),
       # (troop_slot_eq, ":companion", slot_troop_occupation, slto_player_companion),

       # # (troop_get_inventory_capacity, ":inv_cap", ":companion"),
       # (try_for_range, ":i_slot", 0, ek_head),
         # (troop_get_inventory_slot, ":item_id", ":companion", ":i_slot"),

		 # (ge, ":item_id", 0),

	 	 # (this_or_next|eq, ":item_id", "itm_champion_sword_1"),
	 	 # (this_or_next|eq, ":item_id", "itm_sassanid_greatsword"),
		 # (eq, ":item_id", "itm_strange_great_sword"),

		 # (unlock_achievement, ACHIEVEMENT_LADY_OF_THE_LAKE),
		 # (assign, ":inv_cap", 0),
	   # (try_end),
	 # (try_end),
   # ]
   # ),

##diplomacy begin
  # Appoint chamberlain
   (24 , 0, 24 * 12,
   [],
   [
    (assign, ":has_fief", 0),
    (try_for_range, ":center_no", centers_begin, centers_end),
      (party_get_slot,  ":lord_troop_id", ":center_no", slot_town_lord),
      (eq, ":lord_troop_id", "trp_player"),
      (assign, ":has_fief", 1),
    (try_end),
    (eq, ":has_fief", 1),

    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (assign, reg0, "$g_player_chamberlain"),
      (display_message, "@{!}DEBUG : chamberlain: {reg0}"),
    (try_end),

    (assign, ":notification", 0),
    (try_begin),
      (eq, "$g_player_chamberlain", 0),
      (assign, ":notification", 1),
    (else_try),
      (neq, "$g_player_chamberlain", -1),
      (neq, "$g_player_chamberlain", "trp_dplmc_chamberlain"),
      (assign, ":notification", 1),
    (try_end),

    (try_begin),
      (eq, ":notification", 1),
      (call_script, "script_add_notification_menu", "mnu_dplmc_notification_appoint_chamberlain", 0, 0),
    (try_end),]
   ),

  # Appoint constable
   (24 , 0, 24 * 13,
   [],
   [
    (assign, ":has_fief", 0),
    (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
      (party_get_slot,  ":lord_troop_id", ":center_no", slot_town_lord),
      (eq, ":lord_troop_id", "trp_player"),
      (assign, ":has_fief", 1),
    (try_end),
    (eq, ":has_fief", 1),

    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (assign, reg0, "$g_player_constable"),
      (display_message, "@{!}DEBUG : constable: {reg0}"),
    (try_end),

    (assign, ":notification", 0),
    (try_begin),
      (eq, "$g_player_constable", 0),
      (assign, ":notification", 1),
    (else_try),
      (neq, "$g_player_constable", -1),
      (neq, "$g_player_constable", "trp_dplmc_constable"),
      (assign, ":notification", 1),
    (try_end),

    (try_begin),
      (eq, ":notification", 1),
      (call_script, "script_add_notification_menu", "mnu_dplmc_notification_appoint_constable", 0, 0),
    (try_end),
    ]
   ),

  # Appoint chancellor
   (24 , 0, 24 * 14,
   [],
   [
   (assign, ":has_fief", 0),
    (try_for_range, ":center_no", towns_begin, towns_end),
      (party_get_slot,  ":lord_troop_id", ":center_no", slot_town_lord),
      (eq, ":lord_troop_id", "trp_player"),
      (assign, ":has_fief", 1),
    (try_end),
    (eq, ":has_fief", 1),

    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (assign, reg0, "$g_player_chancellor"),
      (display_message, "@{!}DEBUG : chancellor: {reg0}"),
    (try_end),

    (assign, ":notification", 0),
    (try_begin),
      (eq, "$g_player_chancellor", 0),
      (assign, ":notification", 1),
    (else_try),
      (neq, "$g_player_chancellor", -1),
      (neq, "$g_player_chancellor", "trp_dplmc_chancellor"),
      (assign, ":notification", 1),
    (try_end),

    (try_begin),
      (eq, ":notification", 1),
      (call_script, "script_add_notification_menu", "mnu_dplmc_notification_appoint_chancellor", 0, 0),
    (try_end),
    ]),

  (0.1, 0.5, 0, [(map_free,0),(eq,"$g_move_fast", 1)], [(assign,"$g_move_fast", 0)]),

##diplomacy end

#new triggers so cool!

(24, 0, ti_once, [ 
  (neq, "$player_has_homage", 0),
  (eq, "$players_kingdom", "fac_kingdom_1"), #WRE
  (troop_get_slot, ":rank", "trp_player", slot_troop_rank),
  (neq, ":rank", slot_rank_officiorum), #cant already have the rank
  (call_script, "script_troop_get_relation_with_troop", "trp_kingdom_1_lord", "trp_player"),
  (ge, reg0, 40), #need to have high relations
],
[(jump_to_menu, "mnu_promotion_officorum"),]),

(24, 0, ti_once, [ 
  (neq, "$player_has_homage", 0),
  (eq, "$players_kingdom", "fac_kingdom_2"), #ERE
  (troop_get_slot, ":rank", "trp_player", slot_troop_rank),
  (neq, ":rank", slot_rank_officiorum), #cant already have the rank
  (call_script, "script_troop_get_relation_with_troop", "trp_kingdom_2_lord", "trp_player"),
  (ge, reg0, 40), #need to have high relations
],
[(jump_to_menu, "mnu_promotion_officorum"),]),

(168,0,ti_once,[(faction_slot_eq, "fac_kingdom_9", slot_faction_state, sfs_inactive),(faction_slot_eq, "fac_kingdom_1", slot_faction_state, sfs_active)],[ #majorian gains claims on vandal, visigoth, suebi territory after conquering burgundians
  #towns - primarily focuses on areas that he did conquer or try to conquer
  (party_set_slot, "p_town_17", slot_center_ex_faction, "fac_kingdom_1"), #WRE Claims carthage
  (party_set_slot, "p_town_23", slot_center_ex_faction, "fac_kingdom_1"), #WRE Claims bracara
  (party_set_slot, "p_town_25", slot_center_ex_faction, "fac_kingdom_1"), #WRE Claims emerita augusta
  (party_set_slot, "p_town_35", slot_center_ex_faction, "fac_kingdom_1"), #WRE Claims hippo
  (party_set_slot, "p_town_40", slot_center_ex_faction, "fac_kingdom_1"), #WRE Claims tarraco

  (party_set_slot, "p_castle_4", slot_center_ex_faction, "fac_kingdom_1"),
  (party_set_slot, "p_castle_8", slot_center_ex_faction, "fac_kingdom_1"),
  (party_set_slot, "p_castle_22", slot_center_ex_faction, "fac_kingdom_1"),
  (party_set_slot, "p_castle_40", slot_center_ex_faction, "fac_kingdom_1"),
  (party_set_slot, "p_castle_55", slot_center_ex_faction, "fac_kingdom_1"),

  (call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_1", "fac_kingdom_3", 0), #declares war
]),


(24, 0, ti_once, [  (store_character_level, ":level", "trp_player"),
  (ge, ":level", 10),
  (troop_slot_ge, "trp_player", slot_troop_renown, 350),
  (eq, "$g_player_faith", 1),], #changed so that the player must be chalcedonian to get quest
[(jump_to_menu, "mnu_holy_lance_messenger"),]),

(24, 0, ti_once, [  
    # (store_character_level, ":level", "trp_player"),
  (troop_slot_ge, "trp_player", slot_troop_renown, 100),
  (store_relation, ":players_religion_relation", "fac_roman_pagans", "fac_player_faction"),
  (gt, ":players_religion_relation", 30), #positive relations
  (eq, "$roman_pagan_quest_started", 1),
  (neg|check_quest_active, "qst_roman_pagan_quest"),
  (eq, "$g_player_faith", 6),], #must be roman pagan
[(jump_to_menu, "mnu_mithras_messenger"),]),

(24,0,ti_once,[(store_character_level, ":level", "trp_player"),(ge, ":level", 10),(eq, "$g_player_faith", 2),],[ #unique germanic pagan location
  (enable_party, "p_donar_forest"),
]),

(24,0,ti_once,[(eq, "$g_player_faith", 3),],[ #unique arian location
  (enable_party, "p_vidigoias_grave"),
]),
#Invasions Begin
(4800,0,ti_once,[],[ #4800 for 200 days
     (set_spawn_radius, 8),
     (try_for_range, ":unused", 0, 6), # number of invaders to spawn + 1, roughly 200 days
           (spawn_around_party, "p_town_21", "pt_coptic_rebellion"),
     (try_end),  
     (dialog_box, "@A messenger approaches your warband, bringing news of rebellion! It appears that a large number of Anti-Chalcedonian Christians have revolted near Alexandria, killing the local patriarch, Proterius!", "@A messenger approaches your warband"),
     (assign, "$g_coptic_rebellion_triggered", 1),
   ]),

(72,0,ti_once,[(eq, "$g_player_owns_farm", 1),],[ #several days after the player sides with basilius
     (set_spawn_radius, 12),
     (try_for_range, ":unused", 0, 4), # number of invaders to spawn + 1, roughly 200 days
           (spawn_around_party, "p_town_40", "pt_bagaudae_army_event"),
     (try_end),  
     (dialog_box, "@A messenger approaches your warband, bringing news of rebellion! It appears that a large number of Bagadua, under the leadership of Basilius have revolted in Hispania Tarraconensis!", "@A messenger approaches your warband"),
   ]),

(724,0,ti_once,[(eq, "$g_foederati_event", 0),],[
  (set_spawn_radius, 8),
  (try_for_range, ":unused", 0, 3),
    (spawn_around_party, "p_town_13", "pt_foederati_rebels"),
  (try_end),  
  (dialog_box, "@Foederati hired by Majorian for his campaigns have begun to pillage the italian countryside!", "@A messenger approaches your warband"),
  (assign, "$g_foederati_event", 1),
   ]),

#Invasions END
#Battle of Bolia
(2400,0,ti_once,[(faction_slot_eq, "fac_kingdom_4", slot_faction_state, sfs_active)],[ #2400 for 100 days, checks if ostrogoths are still around
    (try_begin), #Spawning in the Heruli
       (store_num_parties_of_template, ":num_parties", "pt_heruli_horde"),
       (lt,":num_parties",1),
       (store_random,":spawn_point",num_heruli_horde_spawn_points),
       (val_add,":spawn_point","p_heruli_spawn_point"),
       (spawn_around_party,":spawn_point","pt_heruli_horde"),
     #(assign,"$heruli_horde",reg(0)),
     #(party_set_banner_icon, "$heruli_horde", "icon_banner_14"),
     (try_end),
    (try_begin), #Spawning in the Danubian Suebi
       (store_num_parties_of_template, ":num_parties", "pt_scirii_horde"),
       (lt,":num_parties",1),
       (store_random,":spawn_point",num_scirii_horde_spawn_points),
       (val_add,":spawn_point","p_scirii_spawn_point"),
       (spawn_around_party,":spawn_point","pt_scirii_horde"),
     #(assign,"$scirii_horde",reg(0)),
     #(party_set_banner_icon, "$scirii_horde", "icon_banner_15"),
     (try_end),

    (try_begin), #additional ostrogothic armies (3)
       (store_num_parties_of_template, ":num_parties", "pt_ostrogothic_army"),
       (lt,":num_parties",3),
       (store_random,":spawn_point",1),
       (val_add,":spawn_point","p_village_147"),
       (spawn_around_party,":spawn_point","pt_ostrogothic_army"),
     #(assign,"$ostrogothic_horde",reg(0)),
     #(party_set_banner_icon, "$ostrogothic_horde", "icon_map_flag_kingdom_4"),
     (try_end),

     (try_begin), #now setting up diplomatic changes
      (faction_slot_eq, "fac_kingdom_14", slot_faction_state, sfs_active),
      (call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_4", "fac_kingdom_14", 0), #Ostrogoths vs Rugii
     (try_end),
     (try_begin), #now setting up diplomatic changes
      (faction_slot_eq, "fac_kingdom_21", slot_faction_state, sfs_active),
      (call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_4", "fac_kingdom_21", 0), #Ostrogoths vs Scirii
     (try_end),

     (dialog_box, "@A messenger approaches your warband, bringing news of war! The Ostrogoths have declared war on their former allies, the Rugii, Heruli, Scirii, and the danubian Suebi, with an attempt to conquer all of Illyria!", "@A messenger approaches your warband"),
     (assign, "$g_battle_of_bolia", 1)
   ]),

(24,0,ti_once,[],[ #adds merchant to tavern, zamb man
  (add_troop_to_site, "trp_visigothic_merchant", "scn_town_40_tavern", 12),
  (add_troop_to_site, "trp_zamb_man", "scn_town_17_tavern", 12),
   ]),

(72,0,ti_once,[(check_quest_active,"qst_agrippinus_quest"),(quest_slot_eq,"qst_agrippinus_quest",slot_quest_current_state, 4)],[ #agrippinus quest
  (quest_set_slot,"qst_agrippinus_quest", slot_quest_current_state, 5),
  (jump_to_menu,"mnu_lupicinus_encounter"),
]),

(24,0,ti_once,[(check_quest_active,"qst_agrippinus_quest"),(quest_slot_eq,"qst_agrippinus_quest",slot_quest_current_state, 7),(check_quest_succeeded, "qst_agrippinus_quest")],[ #agrippinus quest
  (jump_to_menu,"mnu_lupicinus_encounter"),
]),


(24,0,22,[(eq,"$prayer",1)],[
    (assign, "$prayer", 0),    
]),

(24,0,22,[(eq,"$memorial_performed",1)],[
    (assign, "$memorial_performed", 0),    
]),

(24,0,22,[],[
    (try_begin),
    (troop_clear_inventory, "trp_old_palace_farmer"),
        (troop_add_items,"trp_old_palace_farmer", "itm_cabbages",30),
    (try_end),   
]),
#triggers every 12 days
(288.5,0,22,[(faction_slot_eq, "fac_kingdom_8", slot_faction_state, sfs_active),],[ #checks if the suebi are still alive
    (store_faction_of_party, ":town_23_faction", "p_town_23"), #now to check to town
    (try_begin),
      (eq, ":town_23_faction", "fac_kingdom_8"),
      (set_spawn_radius, 8),
      (try_for_range, ":unused", 0, 4), # number of invaders to spawn + 1, roughly 200 days
        (spawn_around_party, "p_town_23", "pt_gallaecian_rebels"),
      (try_end),  
      (display_message, "@Gallaecians revolt against oppressive Suebi rule!", color_bad_news),
    (try_end),
]),

(2,0,ti_once,[(check_quest_active,"qst_conquest_gaul"),],[
    (store_faction_of_party, ":town_3_faction", "p_town_3"),
    (store_faction_of_party, ":town_5_faction", "p_town_5"),
    (store_faction_of_party, ":town_15_faction", "p_town_15"),
    (store_faction_of_party, ":town_16_faction", "p_town_16"),
    (store_faction_of_party, ":castle_12_faction", "p_castle_12"),
    (store_faction_of_party, ":castle_14_faction", "p_castle_14"),
    (store_faction_of_party, ":castle_18_faction", "p_castle_18"),
    (store_faction_of_party, ":castle_21_faction", "p_castle_21"),
    (try_begin),
      (eq, ":town_3_faction", "fac_player_supporters_faction"),
      (eq, ":town_5_faction", "fac_player_supporters_faction"),
      (eq, ":town_15_faction", "fac_player_supporters_faction"),
      (eq, ":town_16_faction", "fac_player_supporters_faction"),
      (eq, ":castle_12_faction", "fac_player_supporters_faction"),
      (eq, ":castle_14_faction", "fac_player_supporters_faction"),
      (eq, ":castle_18_faction", "fac_player_supporters_faction"),
      (eq, ":castle_21_faction", "fac_player_supporters_faction"),

      (call_script, "script_end_quest", "qst_conquest_gaul"), #ends the quest
      (call_script, "script_change_troop_renown", "trp_player", 250),
      (troop_add_item, "trp_player", "itm_caesar_gladius", 0), #gets special gladius
      (troop_add_gold, "trp_player", 50000),
    (try_end),
]),

(2,0,ti_once,[(check_quest_active,"qst_conquest_hispania"),],[
    (store_faction_of_party, ":town_23_faction", "p_town_23"),  #starts with towns first - player must own most of hispania
    (store_faction_of_party, ":town_25_faction", "p_town_25"), 
    (store_faction_of_party, ":town_40_faction", "p_town_40"), 
    (store_faction_of_party, ":castle_4_faction", "p_castle_4"), #now collects castle factions
    (store_faction_of_party, ":castle_33_faction", "p_castle_33"),
    (store_faction_of_party, ":castle_53_faction", "p_castle_53"),
    (store_faction_of_party, ":castle_55_faction", "p_castle_55"),
    (store_faction_of_party, ":castle_60_faction", "p_castle_60"),
    (try_begin),
      (eq, ":town_23_faction", "fac_player_supporters_faction"), #towns
      (eq, ":town_25_faction", "fac_player_supporters_faction"),
      (eq, ":town_40_faction", "fac_player_supporters_faction"),
      (eq, ":castle_4_faction", "fac_player_supporters_faction"), #castles
      (eq, ":castle_33_faction", "fac_player_supporters_faction"),
      (eq, ":castle_53_faction", "fac_player_supporters_faction"),
      (eq, ":castle_55_faction", "fac_player_supporters_faction"),
      (eq, ":castle_60_faction", "fac_player_supporters_faction"),
      (call_script, "script_end_quest", "qst_conquest_hispania"), #ends the quest
      (call_script, "script_change_troop_renown", "trp_player", 200),
      (troop_add_gold, "trp_player", 50000),
    (try_end),
]),

(2,0,ti_once,[(check_quest_active,"qst_conquest_africa"),],[
    (store_faction_of_party, ":town_17_faction", "p_town_17"),  #starts with towns first - player must own most of hispania
    (store_faction_of_party, ":town_34_faction", "p_town_34"), 
    (store_faction_of_party, ":town_35_faction", "p_town_35"), 
    (store_faction_of_party, ":castle_8_faction", "p_castle_8"), #now collects castle factions
    (store_faction_of_party, ":castle_22_faction", "p_castle_22"),
    (store_faction_of_party, ":castle_39_faction", "p_castle_39"),
    (store_faction_of_party, ":castle_40_faction", "p_castle_40"),
    (store_faction_of_party, ":castle_78_faction", "p_castle_78"),
    (store_faction_of_party, ":castle_79_faction", "p_castle_79"),
    (try_begin),
      (eq, ":town_17_faction", "fac_player_supporters_faction"), #towns
      (eq, ":town_34_faction", "fac_player_supporters_faction"),
      (eq, ":town_35_faction", "fac_player_supporters_faction"),
      (eq, ":castle_8_faction", "fac_player_supporters_faction"), #castles
      (eq, ":castle_22_faction", "fac_player_supporters_faction"),
      (eq, ":castle_39_faction", "fac_player_supporters_faction"),
      (eq, ":castle_40_faction", "fac_player_supporters_faction"),
      (eq, ":castle_78_faction", "fac_player_supporters_faction"),
      (eq, ":castle_79_faction", "fac_player_supporters_faction"),
      (call_script, "script_end_quest", "qst_conquest_africa"), #ends the quest
      (call_script, "script_change_troop_renown", "trp_player", 200),
      (troop_add_gold, "trp_player", 50000),
    (try_end),
]),

(1,0,ti_once,[(check_quest_active,"qst_unite_britannia"),],[
    (store_faction_of_party, ":town_2_faction", "p_town_2"),  #starts with towns first - player must own britannia
    (store_faction_of_party, ":town_18_faction", "p_town_18"), 
    (store_faction_of_party, ":town_24_faction", "p_town_24"),
    (store_faction_of_party, ":castle_2_faction", "p_castle_2"), 
    (store_faction_of_party, ":castle_15_faction", "p_castle_15"), #now collects castle factions
    (store_faction_of_party, ":castle_50_faction", "p_castle_50"),
    (store_faction_of_party, ":castle_57_faction", "p_castle_57"),
    (store_faction_of_party, ":castle_58_faction", "p_castle_58"),
    (store_faction_of_party, ":castle_73_faction", "p_castle_73"),
    (store_faction_of_party, ":castle_74_faction", "p_castle_74"),
    (try_begin),
      (eq, ":town_2_faction", "fac_player_supporters_faction"), #towns
      (eq, ":town_18_faction", "fac_player_supporters_faction"),
      (eq, ":town_24_faction", "fac_player_supporters_faction"),
      (eq, ":castle_2_faction", "fac_player_supporters_faction"), #castles
      (eq, ":castle_15_faction", "fac_player_supporters_faction"),
      (eq, ":castle_50_faction", "fac_player_supporters_faction"),
      (eq, ":castle_57_faction", "fac_player_supporters_faction"),
      (eq, ":castle_58_faction", "fac_player_supporters_faction"),
      (eq, ":castle_73_faction", "fac_player_supporters_faction"),
      (eq, ":castle_74_faction", "fac_player_supporters_faction"),

      (call_script, "script_end_quest", "qst_unite_britannia"), #ends the quest
      (call_script, "script_change_troop_renown", "trp_player", 220),
      (troop_add_item, "trp_player", "itm_excalibur", 0), #gets special sword
      (troop_add_gold, "trp_player", 30000),
    (try_end),
]),

(2,0,ti_once,[(check_quest_active,"qst_conquest_suebi"),],[
    (store_faction_of_party, ":town_23_faction", "p_town_23"),
    (store_faction_of_party, ":castle_53_faction", "p_castle_53"),
    (store_faction_of_party, ":castle_60_faction", "p_castle_60"),
    (try_begin),
      (eq, ":town_23_faction", "fac_player_supporters_faction"),
      (eq, ":castle_53_faction", "fac_player_supporters_faction"),
      (eq, ":castle_60_faction", "fac_player_supporters_faction"),

      (call_script, "script_end_quest", "qst_conquest_suebi"), #ends the quest
      (call_script, "script_change_troop_renown", "trp_player", 150),
      (troop_add_gold, "trp_player", 10000),
    (try_end),
]),

(2,0,ti_once,[(check_quest_active,"qst_conquest_northern_gaul"),],[
    (store_faction_of_party, ":town_15_faction", "p_town_15"),
    (store_faction_of_party, ":castle_12_faction", "p_castle_12"),
    (store_faction_of_party, ":castle_21_faction", "p_castle_21"),
    (try_begin),
      (eq, ":town_15_faction", "fac_player_supporters_faction"),
      (eq, ":castle_12_faction", "fac_player_supporters_faction"),
      (eq, ":castle_21_faction", "fac_player_supporters_faction"),

      (call_script, "script_end_quest", "qst_conquest_northern_gaul"), #ends the quest
      (call_script, "script_change_troop_renown", "trp_player", 150),
      (troop_add_gold, "trp_player", 10000),
    (try_end),
]),

(2,0,ti_once,[(check_quest_active,"qst_conquest_ripuari"),],[
    (store_faction_of_party, ":town_1_faction", "p_town_1"),
    (store_faction_of_party, ":castle_30_faction", "p_castle_30"),
    (try_begin),
      (eq, ":town_1_faction", "fac_player_supporters_faction"),
      (eq, ":castle_30_faction", "fac_player_supporters_faction"),

      (call_script, "script_end_quest", "qst_conquest_ripuari"), #ends the quest
      (call_script, "script_change_troop_renown", "trp_player", 100),
      (troop_add_gold, "trp_player", 8000),
    (try_end),
]),

(2,0,ti_once,[(check_quest_active,"qst_conquest_saxons"),],[
    (store_faction_of_party, ":town_32_faction", "p_town_32"),
    (store_faction_of_party, ":castle_11_faction", "p_castle_11"),
    (store_faction_of_party, ":castle_67_faction", "p_castle_67"),
    (store_faction_of_party, ":castle_72_faction", "p_castle_72"),
    (try_begin),
      (eq, ":town_32_faction", "fac_player_supporters_faction"),
      (eq, ":castle_11_faction", "fac_player_supporters_faction"),
      (eq, ":castle_67_faction", "fac_player_supporters_faction"),
      (eq, ":castle_72_faction", "fac_player_supporters_faction"),

      (call_script, "script_end_quest", "qst_conquest_saxons"), #ends the quest
      (call_script, "script_change_troop_renown", "trp_player", 150),
      (troop_add_gold, "trp_player", 12000),
    (try_end),
]),

(2,0,ti_once,[(check_quest_active,"qst_conquest_alemmani"),],[
    (store_faction_of_party, ":town_14_faction", "p_town_14"),
    (store_faction_of_party, ":castle_56_faction", "p_castle_56"),
    (store_faction_of_party, ":castle_66_faction", "p_castle_66"),
    (try_begin),
      (eq, ":town_14_faction", "fac_player_supporters_faction"),
      (eq, ":castle_56_faction", "fac_player_supporters_faction"),
      (eq, ":castle_66_faction", "fac_player_supporters_faction"),

      (call_script, "script_end_quest", "qst_conquest_alemmani"), #ends the quest
      (call_script, "script_change_troop_renown", "trp_player", 150),
      (troop_add_gold, "trp_player", 10000),
    (try_end),
]),

(2,0,ti_once,[(check_quest_active,"qst_conquest_mauri"),],[
    (store_faction_of_party, ":town_34_faction", "p_town_34"),
    (store_faction_of_party, ":castle_39_faction", "p_castle_39"),
    (store_faction_of_party, ":castle_78_faction", "p_castle_78"),
    (store_faction_of_party, ":castle_79_faction", "p_castle_79"),
    (try_begin),
      (eq, ":town_34_faction", "fac_player_supporters_faction"),
      (eq, ":castle_39_faction", "fac_player_supporters_faction"),
      (eq, ":castle_78_faction", "fac_player_supporters_faction"),
      (eq, ":castle_79_faction", "fac_player_supporters_faction"),

      (call_script, "script_end_quest", "qst_conquest_mauri"), #ends the quest
      (call_script, "script_change_troop_renown", "trp_player", 150),
      (troop_add_gold, "trp_player", 12000),
    (try_end),
]),

(2,0,ti_once,[(check_quest_active,"qst_conquest_sicily"),],[
    (store_faction_of_party, ":castle_20_faction", "p_castle_30"),
    (try_begin),
      (eq, ":castle_20_faction", "fac_player_supporters_faction"),
      (call_script, "script_end_quest", "qst_conquest_sicily"), #ends the quest
      (call_script, "script_change_troop_renown", "trp_player", 50),
      (troop_add_gold, "trp_player", 5000),
    (try_end),
]),




(2,0,ti_once,[(eq, "$jugador_rey", 9),],[
    (store_faction_of_party, ":town_12_faction", "p_town_12"),  #player must conquer apahida as the huns to get special reward
    (try_begin),
      (eq, ":town_12_faction", "fac_player_supporters_faction"), #towns
      (jump_to_menu, "mnu_hun_messenger"),
      (troop_add_gold, "trp_player", 10000),
    (try_end),
]),

(24*7,0,ti_once,[(eq, "$unique_sword_crafted", 2),],[
  (dialog_box, "@A messenger approaches your warband, carrying the sword wayland has forged for you...", "@A messenger approaches your warband"),
  (assign, "$unique_sword_crafted", 3),
  (troop_add_item, "trp_player", "itm_nagelring", 0),
]),
#+freelancer start

#  CHECKS IF "$enlisted_party" IS DEFEATED
    (0.0, 0, 0, [
    (eq, "$freelancer_state", 1),
    (gt, "$enlisted_party", 0),
    (neg|party_is_active, "$enlisted_party"),
    (check_quest_active, "qst_freelancer_enlisted"),
    ],
    [
    (call_script, "script_freelancer_event_player_captured"),   
    (assign, "$g_encountered_party", "$g_enemy_party"),
    (jump_to_menu, "mnu_captivity_start_wilderness"),
    ]),

 #  CHECKS IF "$enlisted_party" HAS JOINED BATTLE
    (0.0, 0, 0, [
        (eq, "$freelancer_state", 1),
    (check_quest_active, "qst_freelancer_enlisted"),
    
    #collected nearby enemies->detach (post-battle)
    (try_begin), 
      (party_slot_ge, "p_freelancer_party_backup", slot_party_last_in_combat, 1),
      (map_free),
      (party_set_slot, "p_freelancer_party_backup", slot_party_last_in_combat, 0),
      (party_get_num_attached_parties, ":num_attached", "p_main_party"),
      (try_for_range_backwards, ":i", 0, ":num_attached"),
        (party_get_attached_party_with_rank, ":party", "p_main_party", ":i"),
        (party_detach, ":party"),
      (try_end),
    (try_end),
    
    #Is currently in battle
        (party_get_battle_opponent, ":commander_enemy", "$enlisted_party"),
        (gt, ":commander_enemy", 0),
    
    #checks that the player's health is high enough to join battle
        (store_troop_health, ":player_health", "trp_player"),
        (ge, ":player_health", 50),
    ],
    [
        (jump_to_menu, "mnu_world_map_soldier"),
    ]),

#  CHECKS IF PLAYER WON THE REVOLT
    (1.0, 0, 0, [
        (check_quest_active, "qst_freelancer_revolt"),
    ],
    [ 
    (quest_get_slot, ":revolt_joiners", "qst_freelancer_revolt", slot_quest_target_party),
    (try_begin),
      (quest_slot_eq, "qst_freelancer_revolt", slot_quest_current_state, 0),
      (try_begin),
        (neg|party_is_active, "$enlisted_party"), #victory
        (try_begin),
          (gt, ":revolt_joiners", 0),
          (party_is_active, ":revolt_joiners"),
          (party_detach, ":revolt_joiners"),
          (quest_set_slot, "qst_freelancer_revolt", slot_quest_current_state, 1),
        (else_try),
          (call_script, "script_finish_quest", "qst_freelancer_revolt", 100),
        (try_end),
      (else_try),  #Defeat, enlisted party still active
        (try_begin),
          (gt, ":revolt_joiners", 0),
          (party_is_active, ":revolt_joiners"),
          (party_detach, ":revolt_joiners"),
          (remove_party, ":revolt_joiners"),
        (try_end),
        (call_script, "script_fail_quest", "qst_freelancer_revolt"),
        (call_script, "script_end_quest", "qst_freelancer_revolt"),
      (try_end),
      (assign, "$enlisted_party", 0),
    (try_end),
    
    (quest_slot_ge, "qst_freelancer_revolt", slot_quest_current_state, 1),

    (try_begin),
        (quest_slot_eq, "qst_freelancer_revolt", slot_quest_current_state, 1),

      (store_skill_level, ":cur_leadership", "skl_leadership", "trp_player"),
      (store_skill_level, ":cur_persuasion", "skl_persuasion", "trp_player"),
      (store_add, ":chance", ":cur_persuasion", ":cur_leadership"),
      (val_add, ":chance", 10),
      (store_random_in_range, ":prisoner_state", 0, ":chance"),

      (try_begin),
        (is_between, ":prisoner_state", 0, 5),
        (call_script, "script_party_calculate_strength", "p_main_party", 0),
        (assign, ":main_strength", reg0),
        (call_script, "script_party_calculate_strength", ":revolt_joiners", 0),
        (assign, ":temp_strength", reg0),
        (ge, ":temp_strength", ":main_strength"),

        (party_get_num_prisoner_stacks, ":num_stacks", ":revolt_joiners"),
        (try_for_range, ":cur_stack", 0, ":num_stacks"),
          (party_prisoner_stack_get_troop_id, ":cur_troops", ":revolt_joiners", ":cur_stack"),
          (party_prisoner_stack_get_size, ":cur_size", ":revolt_joiners", ":cur_stack"),
          (party_remove_prisoners, ":revolt_joiners", ":cur_troops", ":cur_size"),
        (try_end),

        (quest_set_slot, "qst_freelancer_revolt", slot_quest_current_state, 2),
        
        (dialog_box, "@The released prisoners were not be trusted and they are preparing to attack you!", "@Warning!"),
        (start_encounter, ":revolt_joiners"),
        (change_screen_map),
      (else_try),
        (is_between, ":prisoner_state", 5, 10),
        (dialog_box, "@The released prisoners scattered as soon as the battle finished. You will not be seeing them again.", "@Notice!"),
        (remove_party, ":revolt_joiners"),
        (call_script, "script_finish_quest", "qst_freelancer_revolt", 100),
        (quest_set_slot, "qst_freelancer_revolt", slot_quest_current_state, 0),
      (else_try),
        (dialog_box, "@The released prisoners have remained loyal and will join your party", "@Notice!"),
        (call_script, "script_party_add_party", "p_main_party", ":revolt_joiners"),
        (remove_party, ":revolt_joiners"),
        (call_script, "script_finish_quest", "qst_freelancer_revolt", 100),
        (quest_set_slot, "qst_freelancer_revolt", slot_quest_current_state, 0),
      (try_end),
    (else_try), #After fight with released prisoners
      (quest_slot_eq, "qst_freelancer_revolt", slot_quest_current_state, 2),
      (try_begin),
        (neg|party_is_active, ":revolt_joiners"),
        (neq, "$g_player_is_captive", 1),
        (call_script, "script_finish_quest", "qst_freelancer_revolt", 100),
      (else_try),
        (call_script, "script_fail_quest", "qst_freelancer_revolt"),
        (call_script, "script_end_quest", "qst_freelancer_revolt"),
      (try_end),
      (quest_set_slot, "qst_freelancer_revolt", slot_quest_current_state, 0),
    (try_end),
    ]),

# IF LEFT MOUSE CLICK GO TO SOLDIER'S MENU
    (0.0, 0, 0, [
        (eq, "$freelancer_state", 1),
        (key_clicked, key_left_mouse_button),

        (set_fixed_point_multiplier, 1000),
        (mouse_get_position, pos0),
        (position_get_y, ":y", pos0),
        (gt, ":y", 50), #allows the camp, reports, quests, etc. buttons to be clicked
    ],
    [
        (jump_to_menu, "mnu_world_map_soldier"),
        (rest_for_hours_interactive, 9999, 4, 0),
    ]),

(24.0, 0, 0, [
        (eq, "$freelancer_state", 2),
    ],
    [
    (try_for_range, ":cur_quest", freelancer_quests_begin, freelancer_quests_end),
      (check_quest_active, ":cur_quest"),
      (quest_get_slot, ":days_left", ":cur_quest", slot_quest_expiration_days),
      (ge, ":days_left", 1),
      (val_sub, ":days_left", 1), #to give extra warning...before this whole trigger is merged over to simple triggers or into the quest pack
      (try_begin),
        (eq, ":days_left", 5),
        (str_store_troop_name, s13, "$enlisted_lord"),
        (dialog_box, "@You have 5 days remaining in your leave from the party of {s13} before you will be declared a deserter.", "@Notice!"),
      (else_try),
        (is_between, ":days_left", 2, 5),
        (assign, reg0, ":days_left"),
        (display_message, "@You have {reg0} days left until you are declared as a deserter!"),
      (else_try),
        (eq, ":days_left", 1),
        (str_store_troop_name, s13, "$enlisted_lord"),
        (dialog_box, "@You must check in with your commander {s13} immediately or you will be declared a deserter!", "@Warning!"),
      (try_end),
    (try_end),
    ]),


#+freelancer end

]
