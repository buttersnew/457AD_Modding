from ID_items import *
from ID_quests import *
from ID_factions import *
from ID_parties import *
from ID_troops import *

from compiler import *
from header_triggers import *
##############################################################
# These constants are used in various files.
# If you need to define a value that will be used in those files,
# just define it here rather than copying it across each file, so
# that it will be easy to change it if you need to.
##############################################################

########################################################
##  ITEM SLOTS             #############################
########################################################

slot_item_is_checked               = 0
slot_item_food_bonus               = 1
slot_item_book_reading_progress    = 2
slot_item_book_read                = 3
slot_item_intelligence_requirement = 4

slot_item_amount_available         = 7

slot_item_urban_demand             = 11 #consumer demand for a good in town, measured in abstract units. The more essential the item (ie, like grain) the higher the price
slot_item_rural_demand             = 12 #consumer demand in villages, measured in abstract units
slot_item_desert_demand            = 13 #consumer demand in villages, measured in abstract units

slot_item_production_slot          = 14
slot_item_production_string        = 15

slot_item_tied_to_good_price       = 20 #ie, weapons and metal armor to tools, padded to cloth, leather to leatherwork, etc

slot_item_num_positions            = 22
slot_item_positions_begin          = 23 #reserve around 5 slots after this


slot_item_multiplayer_faction_price_multipliers_begin = 30 #reserve around 10 slots after this

slot_item_primary_raw_material          = 50
slot_item_is_raw_material_only_for      = 51
slot_item_input_number                  = 52 #ie, how many items of inputs consumed per run
slot_item_base_price                    = 53 #taken from module_items
#slot_item_production_site              = 54 #a string replaced with function - Armagan
slot_item_output_per_run                = 55 #number of items produced per run
slot_item_overhead_per_run              = 56 #labor and overhead per run
slot_item_secondary_raw_material        = 57 #in this case, the amount used is only one
slot_item_enterprise_building_cost      = 58 #enterprise building cost

slot_item_multiplayer_item_class   = 60 #temporary, can be moved to higher values
slot_item_multiplayer_availability_linked_list_begin = 61 #temporary, can be moved to higher values


########################################################
##  AGENT SLOTS            #############################
########################################################

slot_agent_target_x_pos           = 1
slot_agent_target_y_pos           = 2
slot_agent_is_alive_before_retreat= 3
slot_agent_is_in_scripted_mode    = 4
slot_agent_is_not_reinforcement   = 5
slot_agent_tournament_point       = 6
slot_agent_arena_team_set         = 7
slot_agent_spawn_entry_point      = 8
slot_agent_target_prop_instance   = 9
slot_agent_map_overlay_id         = 10
slot_agent_target_entry_point     = 11
slot_agent_initial_ally_power     = 12
slot_agent_initial_enemy_power    = 13
slot_agent_enemy_threat           = 14
slot_agent_is_running_away        = 15
slot_agent_courage_score          = 16
slot_agent_is_respawn_as_bot      = 17
slot_agent_cur_animation          = 18
slot_agent_next_action_time       = 19
slot_agent_state                  = 20
slot_agent_in_duel_with           = 21
slot_agent_duel_start_time        = 22

slot_agent_walker_occupation      = 23
slot_agent_bought_horse           = 24
slot_agent_is_poisoned            = 25    
#slot_possessed = 100
#slot_real_troop = 101

slot_agent_is_skirmishing        = 26
slot_agent_make_dist_with_enemy  = 27
slot_agent_skirmish_direction    = 28

#the following applied only to infantry in formation
slot_agent_formation_rank      = 29
slot_agent_inside_formation    = 30
slot_agent_nearest_enemy_agent = 31
slot_agent_new_division        = 32
slot_agent_positioned          = 33
slot_agent_volley_fire            = 34
slot_agent_courage_score_bonus	  = 35
slot_agent_rank_depth			  = 36
slot_agent_rank_closeness		  = 37
#banners
slot_agent_banner           = 38
slot_agent_scripted_mode    = 39
slot_agent_rotation         = 40
slot_agent_direction        = 41
slot_agent_banner           = 42

slot_agent_horse_rider      = 43

slot_agent_berserk_modeon         = 44	#berserker chief mode on
slot_agent_berserk_use_cooldown   = 45
slot_agent_berserk_cooldown       = 46
#slot_agent_new_division = 46

########################################################
##  FACTION SLOTS          #############################
########################################################
slot_faction_ai_state                   = 4
slot_faction_ai_object                  = 5
slot_faction_ai_rationale               = 6 #Currently unused, can be linked to strings generated from decision checklists
slot_faction_ai_diplomatic_object 		= 7

slot_faction_marshall                   = 8
slot_faction_ai_offensive_max_followers = 9

slot_faction_culture                    = 10
slot_faction_leader                     = 11

slot_faction_temp_slot                  = 12

slot_faction_religion                   = 13 #from vc

##slot_faction_vassal_of            = 11
slot_faction_banner                     = 15

##diplomacy start+
slot_faction_number_of_parties    = 20#Deprecated, use slot_faction_num_parties instead
slot_faction_num_parties          = slot_faction_number_of_parties
##diplomacy end+
slot_faction_state                = 21

slot_faction_adjective            = 22


slot_faction_player_alarm         		= 30
slot_faction_last_mercenary_offer_time 	= 31
slot_faction_recognized_player    		= 32

#overriding troop info for factions in quick start mode.
slot_faction_quick_battle_tier_1_infantry      = 41
slot_faction_quick_battle_tier_2_infantry      = 42
slot_faction_quick_battle_tier_1_archer        = 43
slot_faction_quick_battle_tier_2_archer        = 44
slot_faction_quick_battle_tier_1_cavalry       = 45
slot_faction_quick_battle_tier_2_cavalry       = 46

slot_faction_gender_ratio = 40 #SB : gender ratio slot
slot_faction_tier_1_troop         = 41
slot_faction_tier_2_troop         = 42
slot_faction_tier_3_troop         = 43
slot_faction_tier_4_troop         = 44
slot_faction_tier_5_troop         = 45

slot_faction_deserter_troop       = 48
slot_faction_guard_troop          = 49
slot_faction_messenger_troop      = 50
slot_faction_prison_guard_troop   = 51
slot_faction_castle_guard_troop   = 52

slot_faction_town_walker_male_troop      = 53
slot_faction_town_walker_female_troop    = 54
slot_faction_village_walker_male_troop   = 55
slot_faction_village_walker_female_troop = 56
slot_faction_town_spy_male_troop         = 57
slot_faction_town_spy_female_troop       = 58

slot_faction_has_rebellion_chance = 60

slot_faction_instability          = 61 #last time measured


#UNIMPLEMENTED FEATURE ISSUES
slot_faction_war_damage_inflicted_when_marshal_appointed = 62 #Probably deprecate
slot_faction_war_damage_suffered_when_marshal_appointed  = 63 #Probably deprecate

slot_faction_political_issue 							 = 64 #Center or marshal appointment
slot_faction_political_issue_time 						 = 65 #Now is used

#Faction Slot
slot_faction_freelancer_troop = 66 #should be unused

#Rebellion changes
#slot_faction_rebellion_target                     = 65
#slot_faction_inactive_leader_location         = 66
#slot_faction_support_base                     = 67
#Rebellion changes



#slot_faction_deserter_party_template       = 62

slot_faction_reinforcements_a        = 77
slot_faction_reinforcements_b        = 78
slot_faction_reinforcements_c        = 79

slot_faction_num_armies              = 80
slot_faction_num_castles             = 81
slot_faction_num_towns               = 82

slot_faction_last_attacked_center    = 85
slot_faction_last_attacked_hours     = 86
slot_faction_last_safe_hours         = 87

slot_faction_num_routed_agents       = 90

#useful for competitive consumption
slot_faction_biggest_feast_score      = 91
slot_faction_biggest_feast_time       = 92
slot_faction_biggest_feast_host       = 93


#Faction AI states
slot_faction_last_feast_concluded       = 94 #Set when a feast starts -- this needs to be deprecated
slot_faction_last_feast_start_time      = 94 #this is a bit confusing


slot_faction_ai_last_offensive_time 	= 95 #Set when an offensive concludes
slot_faction_last_offensive_concluded 	= 95 #Set when an offensive concludes

slot_faction_ai_last_rest_time      	= 96 #the last time that the faction has had default or feast AI -- this determines lords' dissatisfaction with the campaign. Set during faction_ai script
slot_faction_ai_current_state_started   = 97 #

slot_faction_ai_last_decisive_event     = 98 #capture a fortress or declaration of war

slot_faction_morale_of_player_troops    = 99
slot_faction_tributary_of	            = 100

#diplomacy
slot_faction_truce_days_with_factions_begin             = 120
slot_faction_provocation_days_with_factions_begin         = 150 #30 more than before, because we have 26 kingdoms
slot_faction_war_damage_inflicted_on_factions_begin     = 180 #30 more than before, because we have 26 kingdoms
slot_faction_sum_advice_about_factions_begin             = 210 #30 more than before, because we have 26 kingdoms
##diplomacy start+ end-points for the ranges for iteration and range checks
slot_faction_truce_days_with_factions_end 			= slot_faction_provocation_days_with_factions_begin
slot_faction_provocation_days_with_factions_end 		= slot_faction_war_damage_inflicted_on_factions_begin
slot_faction_war_damage_inflicted_on_factions_end 	= slot_faction_sum_advice_about_factions_begin
slot_faction_sum_advice_about_factions_end            = 240
slot_faction_neighbors_begin    = 241    #MOTO chief avoid center2 loop by storing results
##diplomacy end+

slot_faction_player_tributary               = 299

dplmc_slot_faction_policy_time                = 300
dplmc_slot_faction_centralization             = 301
dplmc_slot_faction_aristocracy                = 302
dplmc_slot_faction_serfdom                    = 303
dplmc_slot_faction_quality                    = 304
dplmc_slot_faction_patrol_time                = 305
##nested diplomacy start+
#dplmc_slot_faction_attitude                   = 206 #DEPRECATED - Not used anywhere in Diplomacy 3.3.2
##nested diplomacy end+
#dplmc_slot_faction_attitude_begin             = 160
##diplomacy end
##diplomacy start+ add faction slots for additional policies
dplmc_slot_faction_mercantilism               = 306 # + mercantilism / - free trade

slot_faction_levied_troops      =   307

dplmc_slot_faction_policies_begin = dplmc_slot_faction_centralization #Define these for convenient iteration.  Requires them to be continuous.
dplmc_slot_faction_policies_end   = dplmc_slot_faction_mercantilism + 1

#Other slots
#use faction slots to remember information between battles
slot_faction_d0_mem_formation           = 308 ##list of 9
slot_faction_d0_mem_formation_space     = 317
slot_faction_d0_mem_relative_x_flag     = 326
slot_faction_d0_mem_relative_y          = 335
#NEXT                                   = 236

#revolts -- notes for self
#type 1 -- minor revolt, aimed at negotiating change without changing the ruler
#type 2 -- alternate ruler revolt (ie, pretender, chinese dynastic revolt -- keep the same polity but switch the ruler)
	#subtype -- pretender (keeps the same dynasty)
	#"mandate of heaven" -- same basic rules, but a different dynasty
	#alternate/religious
	#alternate/political
#type 3 -- separatist revolt
	# reGonalist/dynastic (based around an alternate ruling house
	# regionalist/republican
	# messianic (ie, Canudos)

##diplomacy start+
#Treaty lengths.  Use these constants instead of "magic numbers" to make it
#obvious what code is supposed to do, and also make it easy to change the
#lengths without having to go through the entire mod.

# Truces (as exist in Native)
dplmc_treaty_truce_days_initial    = 20
dplmc_treaty_truce_days_expire     =  0

#Trade treaties convert to truces after 20 days.
dplmc_treaty_trade_days_initial    = 40
dplmc_treaty_trade_days_expire     = dplmc_treaty_truce_days_initial

#Defensive alliances convert to trade treaties after 20 days.
dplmc_treaty_defense_days_initial  = 60
dplmc_treaty_defense_days_expire   = dplmc_treaty_trade_days_initial

#Alliances convert to defensive alliances after 20 days.
dplmc_treaty_alliance_days_initial = 80
dplmc_treaty_alliance_days_expire  = dplmc_treaty_defense_days_initial

dplmc_treaty_tributary_days_initial = 160
dplmc_treaty_tributary_days_expire  = dplmc_treaty_alliance_days_initial

#Define these by name to make them more clear in the source code.
#They should not be altered from their definitions.
dplmc_treaty_truce_days_half_done = (dplmc_treaty_truce_days_initial + dplmc_treaty_truce_days_expire) // 2
dplmc_treaty_trade_days_half_done = (dplmc_treaty_trade_days_initial + dplmc_treaty_trade_days_expire) // 2
dplmc_treaty_defense_days_half_done = (dplmc_treaty_defense_days_initial + dplmc_treaty_defense_days_expire) // 2
dplmc_treaty_alliance_days_half_done = (dplmc_treaty_alliance_days_initial + dplmc_treaty_alliance_days_expire) // 2

##diplomacy end+

########################################################
##  PARTY SLOTS            #############################
########################################################
slot_party_type                = 0  #spt_caravan, spt_town, spt_castle

slot_party_retreat_flag        = 2
slot_party_ignore_player_until = 3
slot_party_ai_state            = 4
slot_party_ai_object           = 5
slot_party_ai_rationale        = 6 #Currently unused, but can be used to save a string explaining the lord's thinking

#slot_town_belongs_to_kingdom   = 6
slot_town_lord                 = 7

slot_minor_faction_levies_original_faction = 8

slot_party_ai_substate         = 8
slot_town_claimed_by_player    = 9

slot_cattle_driven_by_player = slot_town_lord #hack

slot_town_center        = 10
slot_town_castle        = 11
slot_town_prison        = 12
slot_town_tavern        = 13
slot_town_store         = 14
slot_town_arena         = 16
slot_town_alley         = 17
slot_town_walls         = 18
slot_center_culture     = 19

slot_town_tavernkeeper  = 20
slot_town_weaponsmith   = 21
slot_town_armorer       = 22
slot_town_merchant      = 23
slot_town_horse_merchant= 24
slot_town_elder         = 25
slot_center_player_relation = 26
##diplomacy start+ This range doesn't need to be exhaustive (e.g. the seneschal isn't included), but it should be continuous
dplmc_slot_town_merchants_begin = slot_town_tavernkeeper
dplmc_slot_town_merchants_end = slot_town_elder + 1
##diplomacy end+

slot_center_siege_with_belfry = 27
slot_center_last_taken_by_troop = 28

# party will follow this party if set:
slot_party_commander_party = 30 #default -1   #Deprecate
slot_party_following_player    = 31
slot_party_follow_player_until_time = 32
# slot_party_dont_follow_player_until_time = 33

slot_village_raided_by        = 34
slot_village_state            = 35 #svs_normal, svs_being_raided, svs_looted, svs_recovering, svs_deserted
slot_village_raid_progress    = 36
slot_village_recover_progress = 37
slot_village_smoke_added      = 38

slot_village_infested_by_bandits   = 39

slot_center_last_visited_by_lord   = 41

slot_center_last_player_alarm_hour = 42

slot_village_player_can_not_steal_cattle = 46

slot_center_accumulated_rents      = 47 #collected automatically by NPC lords
slot_center_accumulated_tariffs    = 48 #collected automatically by NPC lords
slot_town_wealth        = 49 #total amount of accumulated wealth in the center, pays for the garrison
slot_town_prosperity    = 50 #affects the amount of wealth generated
slot_town_player_odds   = 51


slot_party_last_toll_paid_hours = 52
slot_party_food_store           = 53 #used for sieges
slot_center_is_besieged_by      = 54 #used for sieges
slot_center_last_spotted_enemy  = 55

slot_party_cached_strength        = 56
slot_party_nearby_friend_strength = 57
slot_party_nearby_enemy_strength  = 58
slot_party_follower_strength      = 59

slot_town_reinforcement_party_template = 60
#SB : alias for slot
slot_village_reinforcement_party = slot_town_reinforcement_party_template
slot_center_original_faction           = 61
slot_center_ex_faction                 = 62

slot_party_follow_me                   = 63
slot_center_siege_begin_hours          = 64 #used for sieges
slot_center_siege_hardness             = 65

slot_center_sortie_strength            = 66
slot_center_sortie_enemy_strength      = 67

slot_party_last_in_combat              = 68 #used for AI
slot_party_last_in_home_center         = 69 #used for AI
slot_party_leader_last_courted         = 70 #used for AI
slot_party_last_in_any_center          = 71 #used for AI
slot_party_spawn_point         		   = 72

slot_castle_exterior    = slot_town_center

#SB : training ground scene slots
slot_grounds_melee = slot_town_center
slot_grounds_track = slot_town_castle
slot_grounds_count = slot_town_prison
slot_grounds_trainer = slot_town_lord

#slot_town_rebellion_contact   = 76
#trs_not_yet_approached  = 0
#trs_approached_before   = 1
#trs_approached_recently = 2

argument_none         = 0
argument_claim        = 1 #deprecate for legal
argument_legal        = 1

argument_ruler        = 2 #deprecate for commons
argument_commons      = 2

argument_benefit      = 3 #deprecate for reward
argument_reward       = 3

argument_victory      = 4
argument_lords        = 5
argument_rivalries    = 6 #new - needs to be added

slot_town_village_product = 76

slot_town_rebellion_readiness = 77
#(readiness can be a negative number if the rebellion has been defeated)

slot_town_arena_melee_mission_tpl = 78
slot_town_arena_torny_mission_tpl = 79
slot_town_arena_melee_1_num_teams = 80
slot_town_arena_melee_1_team_size = 81
slot_town_arena_melee_2_num_teams = 82
slot_town_arena_melee_2_team_size = 83
slot_town_arena_melee_3_num_teams = 84
slot_town_arena_melee_3_team_size = 85
slot_town_arena_melee_cur_tier    = 86
##slot_town_arena_template        = 87

slot_center_npc_volunteer_troop_type   = 88
slot_center_npc_volunteer_troop_amount = 89
slot_center_mercenary_troop_type  = 90
slot_center_mercenary_troop_amount= 91
slot_center_volunteer_troop_type  = 92
slot_center_volunteer_troop_amount= 93
slot_center_volunteer_noble_troop_amount  = 94

#slot_center_companion_candidate   = 94
slot_center_ransom_broker         = 95
slot_center_tavern_traveler       = 96
slot_center_traveler_info_faction = 97
slot_center_tavern_bookseller     = 98
slot_center_tavern_minstrel       = 99

num_party_loot_slots    = 5
slot_party_next_looted_item_slot  = 109
slot_party_looted_item_1          = 110
slot_party_looted_item_2          = 111
slot_party_looted_item_3          = 112
slot_party_looted_item_4          = 113
slot_party_looted_item_5          = 114
slot_party_looted_item_1_modifier = 115
slot_party_looted_item_2_modifier = 116
slot_party_looted_item_3_modifier = 117
slot_party_looted_item_4_modifier = 118
slot_party_looted_item_5_modifier = 119

slot_village_bound_center         = 120
slot_village_market_town          = 121
slot_village_farmer_party         = 122
slot_party_home_center            = 123 #Only use with caravans and villagers

slot_center_current_improvement   = 124
slot_center_improvement_end_hour  = 125

slot_party_last_traded_center     = 126



# slot_center_has_manor            = 130 #village
# slot_center_has_fish_pond        = 131 #village
# slot_center_has_watch_tower      = 132 #village
# slot_center_has_school           = 133 #village
# slot_center_has_messenger_post   = 134 #town, castle, village
# slot_center_has_temple1          = 135 #town, castle, village
# slot_center_has_temple2          = 136 #town, castle, village
# slot_center_has_temple3          = 137 #town, castle, village
# slot_center_has_temple4          = 138 #town, castle, village
# slot_center_has_temple5          = 139 #town, castle, village
# slot_center_has_temple6          = 140 #town, castle, village
# slot_center_has_prisoner_tower   = 141 #town, castle

##extort options:
extort_tax          = 1
extort_toll         = 2
extort_concile      = 3
extort_end          = 4

slot_center_capital                 = 127
##Buildings:
slot_center_has_silver_mine         = 128 #village

slot_center_has_manor                = 129 #village
slot_center_has_fish_pond            = 130 #village
slot_center_has_watch_tower          = 131 #village
slot_center_has_school               = 132 #village
slot_center_has_iron_mine            = 133 #village
slot_center_change_culture_village   = 134  #village
slot_center_has_farms                = 135  #village
slot_center_has_cattle               = 136  #village
slot_center_has_trader               = 137  #village
slot_center_has_quarry               = 138  #village
slot_center_has_irigation            = 139  #village

slot_center_has_messenger_post       = 140 #town, castle, village
slot_center_has_guard                = 141 #town, castle, village
slot_center_has_temple               = 142 #town, castle, village
slot_center_has_fishport             = 143 #town, castle, village
slot_center_has_roads                = 144 #town, castle, village
slot_center_has_hosptial             = 145 #town, castle, village

slot_center_change_culture_town      = 146 #town, castle
slot_center_has_prisoner_tower       = 147 #town, castle
slot_center_has_fire_fighter         = 148 #town, castle
slot_center_has_training_grounds     = 149 #town, castle
slot_center_has_slave_market 	     = 150 #town, castle
slot_center_has_barracks             = 151 #town, castle
slot_center_has_sewers               = 152 #town, castle
slot_center_has_industry             = 153 #town, castle
slot_center_has_loom                 = 154 #town, castle
slot_center_has_smith                = 155 #town, castle
slot_center_has_port                 = 156 #town, castle
##this are player only buildinga
slot_center_has_forum   		     = 157 #town, castle
slot_center_has_theatre   		     = 158 #town, castle
slot_center_has_triumph   		     = 159 #town, castle
slot_center_has_water   		     = 160 #town, castle

slot_center_has_temple_god           = 161 #town, castle
 ## player only ends

slot_center_current_improvement     = 162
slot_center_improvement_end_hour    = 163
slot_center_current_improvement_2   = 164
slot_center_improvement_2_end_hour  = 165
#slot_center_has_blacksmith     = 351 #town, castle

village_improvements_begin 					 = slot_center_has_silver_mine
village_improvements_end         			 = slot_center_change_culture_town

walled_center_improvements_begin 			 = slot_center_has_messenger_post
walled_center_improvements_end               = slot_center_has_temple_god

number_of_buildings_town =    walled_center_improvements_end - walled_center_improvements_begin
number_of_buildings_village = village_improvements_end - village_improvements_begin 


# village_improvements_begin = slot_center_has_manor
# village_improvements_end = 140

# walled_center_improvements_begin = slot_center_has_messenger_post
# walled_center_improvements_end = slot_center_has_prisoner_tower

slot_center_player_enterprise                     = 166 #noted with the item produced
slot_center_player_enterprise_production_order    = 167
slot_center_player_enterprise_consumption_order   = 168 #not used
slot_center_player_enterprise_days_until_complete = 169 #Used instead

slot_center_player_enterprise_balance             = 170 #not used
slot_center_player_enterprise_input_price         = 171 #not used
slot_center_player_enterprise_output_price        = 172 #not used



slot_center_has_bandits                        = 173
slot_town_has_tournament                       = 174
slot_town_tournament_max_teams                 = 175
slot_town_tournament_max_team_size             = 176

slot_center_faction_when_oath_renounced        = 177

slot_center_walker_0_troop                   = 178
slot_center_walker_1_troop                   = 179
slot_center_walker_2_troop                   = 180
slot_center_walker_3_troop                   = 181
slot_center_walker_4_troop                   = 182
slot_center_walker_5_troop                   = 183
slot_center_walker_6_troop                   = 184
slot_center_walker_7_troop                   = 185
slot_center_walker_8_troop                   = 186
slot_center_walker_9_troop                   = 187

slot_center_walker_0_dna                     = 188
slot_center_walker_1_dna                     = 189
slot_center_walker_2_dna                     = 190
slot_center_walker_3_dna                     = 191
slot_center_walker_4_dna                     = 192
slot_center_walker_5_dna                     = 193
slot_center_walker_6_dna                     = 194
slot_center_walker_7_dna                     = 195
slot_center_walker_8_dna                     = 196
slot_center_walker_9_dna                     = 197

slot_center_walker_0_type                    = 198
slot_center_walker_1_type                    = 199
slot_center_walker_2_type                    = 200
slot_center_walker_3_type                    = 201
slot_center_walker_4_type                    = 202
slot_center_walker_5_type                    = 203
slot_center_walker_6_type                    = 204
slot_center_walker_7_type                    = 205
slot_center_walker_8_type                    = 206
slot_center_walker_9_type                    = 207

slot_town_trade_route_1           = 208
slot_town_trade_route_2           = 209
slot_town_trade_route_3           = 210
slot_town_trade_route_4           = 211
slot_town_trade_route_5           = 212
slot_town_trade_route_6           = 213
slot_town_trade_route_7           = 214
slot_town_trade_route_8           = 215
slot_town_trade_route_9           = 216
slot_town_trade_route_10          = 217
slot_town_trade_route_11          = 218
slot_town_trade_route_12          = 219
slot_town_trade_route_13          = 220
slot_town_trade_route_14          = 221
slot_town_trade_route_15          = 222
slot_town_trade_routes_begin = slot_town_trade_route_1
slot_town_trade_routes_end = slot_town_trade_route_15 + 1


num_trade_goods = itm_siege_supply - itm_spice
slot_town_trade_good_productions_begin       = 500 #a harmless number, until it can be deprecated

#These affect production but in some cases also demand, so it is perhaps easier to itemize them than to have separate

slot_village_number_of_cattle   = 225
slot_center_head_cattle         = 225 #dried meat, cheese, hides, butter
slot_center_head_sheep			= 226 #sausages, wool
slot_center_head_horses		 	= 227 #horses can be a trade item used in tracking but which are never offered for sale

slot_center_acres_pasture       = 228 #pasture area for grazing of cattles and sheeps, if this value is high then number of cattles and sheeps increase faster
slot_center_acres_grain			= 229 #grain
slot_center_acres_olives        = 230 #olives
slot_center_acres_vineyard		= 231 #fruit
slot_center_acres_flax          = 232 #flax
slot_center_acres_dates			= 233 #dates

slot_center_fishing_fleet		= 234 #smoked fish
slot_center_salt_pans		    = 235 #salt

slot_center_apiaries       		= 236 #honey
slot_center_silk_farms			= 237 #silk
slot_center_kirmiz_farms		= 238 #dyes

slot_center_iron_deposits       = 239 #iron
slot_center_fur_traps			= 240 #furs
slot_center_silver_deposits	    = 241

slot_center_mills				= 242 #bread
slot_center_breweries			= 243 #ale
slot_center_wine_presses		= 244 #wine
slot_center_olive_presses		= 245 #oil

slot_center_linen_looms			= 246 #linen
slot_center_silk_looms          = 247 #velvet
slot_center_wool_looms          = 248 #wool cloth

slot_center_pottery_kilns		= 249 #pottery
slot_center_smithies			= 250 #tools
slot_center_tanneries			= 251 #leatherwork
slot_center_household_gardens   = 252 #cabbages

slot_production_sources_end = 253

slot_center_religion = 254 # 1 -roman christian, 2 -pagan, 3 arian, 4 zoroastrian, 5 coptic
#slot_center_faithratio = 235 # player religion vs other religion in town
slot_party_been_sacked	= 255
#slot_center_support_roman = 235 #Old system, now unused
#slot_center_support_pagan = 236
#slot_center_support_arian = 237 
#slot_center_support_zoroastrian = 238
#slot_center_support_coptic = 239


#all spice comes overland to Tulga
#all dyes come by sea to Jelkala

#chicken and pork are perishable and non-tradeable, and based on grain production
#timber and pitch if we ever have a shipbuilding industry
#limestone and timber for mortar, if we allow building

slot_town_last_nearby_fire_time                         = 260

#slot_town_trade_good_prices_begin            = slot_town_trade_good_productions_begin + num_trade_goods + 1
slot_party_following_orders_of_troop        = 264
slot_party_orders_type				        = 265
slot_party_orders_object				    = 266
slot_party_orders_time				    	= 267

slot_party_temp_slot_1			            = 268 #right now used only within a single script, merchant_road_info_to_s42, to denote closed roads. Now also used in comparative scripts
slot_party_under_player_suggestion			= 269 #move this up a bit

slot_center_disease                         = 270

#use only prime numbers
disease_consumption_timer     = 2
disease_consumption           = 5
    
disease_slow_fever_timer      = 7
disease_slow_fever            = 10

disease_camp_fever_timer      = 12
disease_camp_fever            = 15

disease_plague_timer          = 16
disease_plague                = 20

disease_measles_timer         = 22
disease_measles               = 25

disease_smallpox_timer        = 27
disease_smallpox              = 30

disease_greatpoxpox_timer     = 32
disease_greatpoxpox           = 35

slot_center_event                 = 271

slot_icon_backup        = 271
slot_party_on_water     = 270
speed_modifier_campaign = 90

#effects of catastrophic events will stay for two weeks, decrease tax revenue
event_earthquake_timer    =   97
event_earthquake          =   100

event_fire_timer          =   109
event_fire                =   110

event_drought_timer       =   116
event_drought             =   120

event_insects_timer       =   128
event_insects             =   130

event_conquered_timer     =   138
event_conquered           =   140

#slot_center_last_reconnoitered_by_faction_time 				= 350
#slot_center_last_reconnoitered_by_faction_cached_strength 	= 360
#slot_center_last_reconnoitered_by_faction_friend_strength 	= 370


# event_fire_of_rome_timer  =   165#
# event_fire_of_rome        =   200#

slot_center_current_improvement_builder     = 272
slot_center_current_improvement_2_builder   = 273

slot_town_trade_good_prices_begin 			= 274

slot_center_blockaded             = 275 #used for but a single value; global should be used
slot_center_blockaded_time        = 276 #used for but a single value; global should be used
slot_center_mantlets_placed       = 277 #used for but a single value; global should be used
slot_center_latrines              = 278 #used for but a single value; global should be used
slot_center_ladder_time           = 279 #used for but a single value; global should be used
slot_center_infiltration_type     = 280 #used for but a single value; global should be used
slot_center_starvation_time       = 281 #used for but a single value; global should be used

slot_party_messenger_time         = 282 #used for but a single value; global should be used

##assume 50 trade goods
#hence slots: 274-324 are for trade goods

##diplomacy begin
# recruiter kit begin
dplmc_slot_party_recruiter_needed_recruits = 325           # Amount of recruits the employer ordered.
dplmc_slot_party_recruiter_origin = 326                    # Walled center from where the recruiter was hired.
dplmc_slot_village_reserved_by_recruiter = 327             # This prevents recruiters from going to villages targeted by other recruiters.
dplmc_slot_party_recruiter_needed_recruits_faction = 328   # Alkhadias Master, you forgot this one from the PM you sent me :D
dplmc_spt_recruiter     = 12
# recruiter kit end
##diplomacy start+ Re-use those slots for other party types
dplmc_slot_party_origin = dplmc_slot_party_recruiter_origin
dplmc_slot_party_mission_parameter_1 = dplmc_slot_party_recruiter_needed_recruits
dplmc_slot_party_mission_parameter_2 = dplmc_slot_party_recruiter_needed_recruits_faction
##diplomacy end+

dplmc_slot_party_mission_diplomacy            = 329
#fa_slot_party_mission						  = 301
dplmc_slot_center_taxation                    = 330
##diplomacy start+ additional center slots
dplmc_slot_center_ex_lord                     = 331 #The last lord (not counting those who willingly transferred it)
dplmc_slot_center_original_lord               = 332 #The original lord
dplmc_slot_center_last_transfer_time          = 333 #The last time it was captured
dplmc_slot_center_last_attacked_time          = 334 #Last attempted raid or siege
dplmc_slot_center_last_attacker               = 335 #Last lord who attempted to raid or siege

dplmc_slot_village_trade_last_returned_from_market = 336#overlaps with dplmc_slot_town_trade_route_last_arrival_1
dplmc_slot_village_trade_last_arrived_to_market = 337#overlaps with dplmc_slot_town_trade_route_last_arrival_2

dplmc_slot_town_trade_route_last_arrival_1        = 338
dplmc_slot_town_trade_route_last_arrival_2        = 339
dplmc_slot_town_trade_route_last_arrival_3        = 340
dplmc_slot_town_trade_route_last_arrival_4        = 341
dplmc_slot_town_trade_route_last_arrival_5        = 342
dplmc_slot_town_trade_route_last_arrival_6        = 343
dplmc_slot_town_trade_route_last_arrival_7        = 344
dplmc_slot_town_trade_route_last_arrival_8        = 345
dplmc_slot_town_trade_route_last_arrival_9        = 346
dplmc_slot_town_trade_route_last_arrival_10        = 347
dplmc_slot_town_trade_route_last_arrival_11        = 348
dplmc_slot_town_trade_route_last_arrival_12        = 349
dplmc_slot_town_trade_route_last_arrival_13        = 350
dplmc_slot_town_trade_route_last_arrival_14        = 351
dplmc_slot_town_trade_route_last_arrival_15        = 352
dplmc_slot_town_trade_route_last_arrivals_begin    = dplmc_slot_town_trade_route_last_arrival_1
dplmc_slot_town_trade_route_last_arrivals_end      = dplmc_slot_town_trade_route_last_arrival_15 + 1

#slot_party_type values
##spt_caravan            = 1
spt_castle             = 2
spt_town               = 3
spt_village            = 4
##spt_forager            = 5
##spt_war_party          = 6
##spt_patrol             = 7
##spt_messenger          = 8
##spt_raider             = 9
##spt_scout              = 10
spt_reinforcement      = 6
#SB : add reinforcements as part of kingdom party range
spt_kingdom_caravan    = 11
##spt_prisoner_train     = 12
spt_kingdom_hero_party = 13
##spt_merchant_caravan   = 14
spt_village_farmer     = 15
spt_ship               = 16
spt_cattle_herd        = 17
spt_bandit_lair       = 18
#spt_deserter           = 20
spt_minor_faction_levies    = 100

kingdom_party_types_begin = spt_kingdom_caravan
kingdom_party_types_end = spt_kingdom_hero_party + 1

#slot_faction_state values
sfs_active                     = 0
sfs_defeated                   = 1
sfs_inactive                   = 2
sfs_inactive_rebellion         = 3
sfs_beginning_rebellion        = 4


#slot_faction_ai_state values
sfai_default                   		 = 0 #also defending
sfai_gathering_army            		 = 1
sfai_attacking_center          		 = 2
sfai_raiding_village           		 = 3
sfai_attacking_enemy_army      		 = 4
sfai_attacking_enemies_around_center = 5
sfai_feast             		 		 = 6 #can be feast, wedding, or major tournament
#Social events are a generic aristocratic gathering. Tournaments take place if they are in a town, and hunts take place if they are at a castle.
#Weddings will take place at social events between betrothed couples if they have been engaged for at least a month, if the lady's guardian is the town lord, and if both bride and groom are present


#Rebellion system changes begin
sfai_nascent_rebellion          = 7
#Rebellion system changes end

#slot_party_ai_state values
spai_undefined                  = -1
spai_besieging_center           = 1
spai_patrolling_around_center   = 4
spai_raiding_around_center      = 5
##spai_raiding_village            = 6
spai_holding_center             = 7
##spai_helping_town_against_siege = 9
spai_engaging_army              = 10
spai_accompanying_army          = 11
spai_screening_army             = 12
spai_trading_with_town          = 13
spai_retreating_to_center       = 14
##spai_trading_within_kingdom     = 15
spai_visiting_village           = 16 #same thing, I think. Recruiting differs from holding because NPC parties don't actually enter villages

#slot_village_state values
svs_normal                      = 0
svs_being_raided                = 1
svs_looted                      = 2
svs_recovering                  = 3
svs_deserted                    = 4
svs_under_siege                 = 5

#$g_player_icon_state values
pis_normal                      = 0
pis_camping                     = 1
pis_ship                        = 2

########################################################
##  SCENE SLOTS            #############################
########################################################
slot_scene_visited              = 0
slot_scene_belfry_props_begin   = 10



########################################################
##  TROOP SLOTS            #############################
########################################################
#slot_troop_role         = 0  # 10=Kingdom Lord

slot_troop_occupation          = 2  # 0 = free, 1 = merchant
#slot_troop_duty               = 3  # Kingdom duty, 0 = free
#slot_troop_homage_type         = 45
#homage_mercenary =             = 1 #Player is on a temporary contract
#homage_official =              = 2 #Player has a royal appointment
#homage_feudal   =              = 3 #


slot_troop_state               = 3
slot_troop_last_talk_time      = 4
slot_troop_met                 = 5 #i also use this for the courtship state -- may become cumbersome
slot_troop_courtship_state     = 5 #2 professed admiration, 3 agreed to seek a marriage, 4 ended relationship

slot_troop_party_template      = 6
#slot_troop_kingdom_rank        = 7

slot_troop_renown              = 7

##slot_troop_is_prisoner         = 8  # important for heroes only
slot_troop_prisoner_of_party   = 8  # important for heroes only
#slot_troop_is_player_companion = 9  # important for heroes only:::USE  slot_troop_occupation = slto_player_companion

slot_troop_present_at_event    = 9

slot_troop_leaded_party         = 10 # important for kingdom heroes only
slot_troop_wealth               = 11 # important for kingdom heroes only
slot_troop_cur_center           = 12 # important for royal family members only (non-kingdom heroes)

slot_troop_banner_scene_prop    = 13 # important for kingdom heroes and player only

slot_troop_original_faction     = 14 # for pretenders
#slot_troop_loyalty              = 15 #deprecated - this is now derived from other figures
#slot_troop_player_order_state   = 16 #Deprecated
#slot_troop_player_order_object  = 17 #Deprecated
#slot_troop_rank	= 15 #used for the new rank system for romans, sassanids + other organized empires
slot_troop_religion	= 15 #added from VC
slot_troop_conv = 16 # conversion attempted 0-initial state, 1-tried&failed 2-converted
#troop_player order state are all deprecated in favor of party_order_state. This has two reasons -- 1) to reset AI if the party is eliminated, and 2) to allow the player at a later date to give orders to leaderless parties, if we want that


#Post 0907 changes begin
slot_troop_age                 =  18
slot_troop_age_appearance      =  19

#Post 0907 changes end

slot_troop_does_not_give_quest = 20
slot_troop_player_debt         = 21
slot_troop_player_relation     = 22
#slot_troop_player_favor       = 23
slot_troop_last_quest          = 24
slot_troop_last_quest_betrayed = 25
slot_troop_last_persuasion_time= 26
slot_troop_last_comment_time   = 27
slot_troop_spawned_before      = 28

#Post 0907 changes begin
slot_troop_last_comment_slot   = 29
#Post 0907 changes end

slot_troop_spouse              = 30
slot_troop_father              = 31
slot_troop_mother              = 32
slot_troop_guardian            = 33 #Usually siblings are identified by a common parent.This is used for brothers if the father is not an active npc. At some point we might introduce geneologies
slot_troop_betrothed           = 34 #Obviously superseded once slot_troop_spouse is filled
#other relations are derived from one's parents
#slot_troop_daughter            = 33
#slot_troop_son                 = 34
#slot_troop_sibling             = 35
	##diplomacy start+
	#NOTE TO MODDERS: There is code that depends on these slots appearing in the correct order and being continuous.
dplmc_slot_troop_relatives_begin = slot_troop_spouse
dplmc_slot_troop_relatives_end   = slot_troop_betrothed
dplmc_slot_troop_relatives_including_betrothed_end = slot_troop_betrothed + 1
	##diplomacy end+
slot_troop_love_interest_1     = 35 #each unmarried lord has three love interests
slot_troop_love_interest_2     = 36
slot_troop_love_interest_3     = 37
slot_troop_love_interests_end  = 38
#ways to court -- discuss a book, commission/compose a poem, present a gift, recount your exploits, fulfil a specific quest, appear at a tournament
#preferences for women - (conventional - father's friends)
slot_lady_no_messages          				= 37
slot_lady_last_suitor          				= 38
slot_lord_granted_courtship_permission      = 38

slot_troop_betrothal_time                   = 39 #used in scheduling the wedding

slot_troop_trainer_met                       = 30
slot_troop_trainer_waiting_for_result        = 31
slot_troop_trainer_training_fight_won        = 32
slot_troop_trainer_num_opponents_to_beat     = 33
slot_troop_trainer_training_system_explained = 34
slot_troop_trainer_opponent_troop            = 35
slot_troop_trainer_training_difficulty       = 36
# slot_troop_trainer_training_fight_won        = 37 #SB : duplicate slot


slot_lady_used_tournament					= 40

slot_troop_culture            = 44

slot_troop_current_rumor       = 45
slot_troop_temp_slot           = 46
slot_troop_promised_fief       = 47

slot_troop_set_decision_seed       = 48 #Does not change
slot_troop_temp_decision_seed      = 49 #Resets at recalculate_ai
slot_troop_recruitment_random      = 50 #used in a number of different places in the intrigue procedures to overcome intermediate hurdles, although not for the final calculation, might be replaced at some point by the global decision seed
#Decision seeds can be used so that some randomness can be added to NPC decisions, without allowing the player to spam the NPC with suggestions
#The temp decision seed is reset 24 to 48 hours after the NPC last spoke to the player, while the set seed only changes in special occasions
#The single seed is used with varying modula to give high/low outcomes on different issues, without using a separate slot for each issue

slot_troop_intrigue_impatience = 51
#recruitment changes end

#slot_troop_honorable          = 50
#slot_troop_merciful          = 51
slot_lord_reputation_type             = 52
slot_lord_recruitment_argument        = 53 #the last argument proposed by the player to the lord
slot_lord_recruitment_candidate       = 54 #the last candidate proposed by the player to the lord

slot_troop_change_to_faction          = 55

##diplomacy start+ Use this slot to track owned center points (village = 1, castle = 2, town = 3)
#The value should be one more than the actual number of center points, because it makes
#it obvious when the slot has not been initialized.  (It also so happens that we often
#add 1 to the value anyway to avoid division by 0, so this can be convenient.)
dplmc_slot_troop_center_points_plus_one = 56
##diplomacy end+

#slot_troop_readiness_to_join_army     = 57 #possibly deprecate
#slot_troop_readiness_to_follow_orders = 58 #possibly deprecate

# NPC-related constants

#NPC companion changes begin
slot_troop_first_encountered          = 59
slot_troop_home                       = 60

slot_troop_morality_state       = 61
tms_no_problem         = 0
tms_acknowledged       = 1
tms_dismissed          = 2

slot_troop_morality_type = 62
tmt_aristocratic = 1
tmt_egalitarian = 2
tmt_humanitarian = 3
tmt_honest = 4
tmt_pious = 5 #SB : these are unused

slot_troop_morality_value = 63

slot_troop_2ary_morality_type  = 64
slot_troop_2ary_morality_state = 65
slot_troop_2ary_morality_value = 66

slot_troop_town_with_contacts  = 67
slot_troop_town_contact_type   = 68 #1 are nobles, 2 are commons

slot_troop_morality_penalties =  69 ### accumulated grievances from morality conflicts


slot_troop_personalityclash_object     = 71
#(0 - they have no problem, 1 - they have a problem)
slot_troop_personalityclash_state    = 72 #1 = pclash_penalty_to_self, 2 = pclash_penalty_to_other, 3 = pclash_penalty_to_other,
pclash_penalty_to_self  = 1
pclash_penalty_to_other = 2
pclash_penalty_to_both  = 3
#(a string)
slot_troop_personalityclash2_object   = 73
slot_troop_personalityclash2_state    = 74

slot_troop_personalitymatch_object   =  75
slot_troop_personalitymatch_state   =  76

slot_troop_personalityclash_penalties = 77 ### accumulated grievances from personality clash
slot_troop_personalityclash_penalties = 77 ### accumulated grievances from personality clash

slot_troop_home_speech_delivered = 78 #only for companions
slot_troop_discussed_rebellion   = 78 #only for pretenders

#courtship slots
slot_lady_courtship_heroic_recited      = 74
slot_lady_courtship_allegoric_recited   = 75
slot_lady_courtship_comic_recited       = 76
slot_lady_courtship_mystic_recited      = 77
slot_lady_courtship_tragic_recited      = 78



#NPC history slots
slot_troop_met_previously        = 80
slot_troop_turned_down_twice     = 81
slot_troop_playerparty_history   = 82

pp_history_scattered         = 1
pp_history_dismissed         = 2
pp_history_quit              = 3
pp_history_indeterminate     = 4
##diplomacy start+
dplmc_pp_history_appointed_office    = 5 #assigned an office (like Minister)
dplmc_pp_history_granted_fief        = 6 #was granted a fief, or (for pretenders) completed Pretender quest
dplmc_pp_history_lord_rejoined       = 7 #enfeoffed lord temporarily rejoined the party
dplmc_pp_history_nonplayer_entry     = 8 #became a lord without first being a companion of the player (normally this is assumed to be impossible)
##diplomacy end+

slot_troop_playerparty_history_string   = 83
slot_troop_return_renown        = 84

slot_troop_custom_banner_bg_color_1      = 85
slot_troop_custom_banner_bg_color_2      = 86
slot_troop_custom_banner_charge_color_1  = 87
slot_troop_custom_banner_charge_color_2  = 88
slot_troop_custom_banner_charge_color_3  = 89
slot_troop_custom_banner_charge_color_4  = 90
slot_troop_custom_banner_bg_type         = 91
slot_troop_custom_banner_charge_type_1   = 92
slot_troop_custom_banner_charge_type_2   = 93
slot_troop_custom_banner_charge_type_3   = 94
slot_troop_custom_banner_charge_type_4   = 95
slot_troop_custom_banner_flag_type       = 96
slot_troop_custom_banner_num_charges     = 97
slot_troop_custom_banner_positioning     = 98
slot_troop_custom_banner_map_flag_type   = 99

#conversation strings -- must be in this order!
slot_troop_intro 						= 101
slot_troop_intro_response_1 			= 102
slot_troop_intro_response_2 			= 103
slot_troop_backstory_a 					= 104
slot_troop_backstory_b 					= 105
slot_troop_backstory_c 					= 106
slot_troop_backstory_delayed 			= 107
slot_troop_backstory_response_1 		= 108
slot_troop_backstory_response_2 		= 109
slot_troop_signup   					= 110
slot_troop_signup_2 					= 111
slot_troop_signup_response_1 			= 112
slot_troop_signup_response_2 			= 113
slot_troop_mentions_payment 			= 114 #Not actually used
slot_troop_payment_response 			= 115 #Not actually used
slot_troop_morality_speech   			= 116
slot_troop_2ary_morality_speech 		= 117
slot_troop_personalityclash_speech 		= 118
slot_troop_personalityclash_speech_b 	= 119
slot_troop_personalityclash2_speech 	= 120
slot_troop_personalityclash2_speech_b 	= 121
slot_troop_personalitymatch_speech 		= 122
slot_troop_personalitymatch_speech_b 	= 123
slot_troop_retirement_speech 			= 124
slot_troop_rehire_speech 				= 125
slot_troop_home_intro           		= 126
slot_troop_home_description    			= 127
slot_troop_home_description_2 			= 128
slot_troop_home_recap         			= 129
slot_troop_honorific   					= 130
slot_troop_kingsupport_string_1			= 131
slot_troop_kingsupport_string_2			= 132
slot_troop_kingsupport_string_2a		= 133
slot_troop_kingsupport_string_2b		= 134
slot_troop_kingsupport_string_3			= 135
slot_troop_kingsupport_objection_string	= 136
slot_troop_intel_gathering_string	    = 137
slot_troop_fief_acceptance_string	    = 138
slot_troop_woman_to_woman_string	    = 139
slot_troop_turn_against_string	        = 140

slot_troop_strings_end 					= 141

slot_troop_payment_request 				= 141

#141, support base removed, slot now available

slot_troop_kingsupport_state			= 142
slot_troop_kingsupport_argument			= 143
slot_troop_kingsupport_opponent			= 144
slot_troop_kingsupport_objection_state  = 145 #0, default, 1, needs to voice, 2, has voiced

slot_troop_days_on_mission		        = 150
slot_troop_current_mission			    = 151
slot_troop_mission_object               = 152
npc_mission_kingsupport					= 1
npc_mission_gather_intel                = 2
npc_mission_peace_request               = 3
npc_mission_pledge_vassal               = 4
npc_mission_seek_recognition            = 5
npc_mission_test_waters                 = 6
npc_mission_non_aggression              = 7
npc_mission_rejoin_when_possible        = 8

#Number of routed agents after battle ends.
slot_troop_player_routed_agents                 = 146
slot_troop_ally_routed_agents                   = 147
slot_troop_enemy_routed_agents                  = 148

#Special quest slots
slot_troop_mission_participation        = 149
mp_unaware                              = 0
mp_stay_out                             = 1
mp_prison_break_fight                   = 2
mp_prison_break_stand_back              = 3
mp_prison_break_escaped                 = 4
mp_prison_break_caught                  = 5

#Below are some constants to expand the political system a bit. The idea is to make quarrels less random, but instead make them serve a rational purpose -- as a disincentive to lords to seek

slot_troop_controversy                     = 150 #Determines whether or not a troop is likely to receive fief or marshalship
slot_troop_recent_offense_type             = 151 #failure to join army, failure to support colleague
slot_troop_recent_offense_object           = 152 #to whom it happened
slot_troop_recent_offense_time             = 153
slot_troop_stance_on_faction_issue         = 154 #when it happened

slot_troop_military_title                  = 155 #unique military title, allows for lord to have unique (stronger) party template
slot_troop_honorary_title				   = 156 #honorary title for roman/post roman areas

#shared between ERE + WRE
mt_domestici = 1 #Comes Domesticorum
mt_officiorum = 2 #Magister Officiorum
#WRE
mt_gallia = 3 #Magister Militum per Gallia
mt_utriusque = 4 #Magister Utriusque Militiae
mt_dalmatia = 5 #Comes Illyricum
#lesser ranks
mt_hispenias = 6 #Granted over Hispania, vacant (open to player if they own Emerita Augusta)
mt_africae = 7 #Granted over Africa, vacant (open for player if they own carthage?)
#ERE
mt_praesentalis_1 = 8 #Magister Militum Praesentalis I - vacant at start
mt_praesentalis_2 = 9 #Magister Militum Praesentalis II
mt_orientem = 10 #Magister Militum per Orientem
mt_thracias = 11 #Magister Militum per Thracias - vacant at start
mt_illyricum = 12 #Magister Militum per Illyricum
#lesser ranks
mt_egypt = 13 #Comes Limits Aegypti
mt_foenicis = 14 #Dux Foenicis
mt_armeniae = 15 #Dux Armeniae
mt_daciae = 16 #Dux Daciae Ripensis
mt_palaestinae = 17 #Dux Palaestinae
#Sassanid Persia
mt_spahbed = 18 #Eran-Spahbed

ht_clarissimus = 1 #first title
ht_spectabilis = 2 #granted comes title
ht_illustris = 3 #magister title

tro_failed_to_join_army                    = 1
tro_failed_to_support_colleague            = 2

#CONTROVERSY
#This is used to create a more "rational choice" model of faction politics, in which lords pick fights with other lords for gain, rather than simply because of clashing personalities
#It is intended to be a limiting factor for players and lords in their ability to intrigue against each other. It represents the embroilment of a lord in internal factional disputes. In contemporary media English, a lord with high "controversy" would be described as "embattled."
#The main effect of high controversy is that it disqualifies a lord from receiving a fief or an appointment
#It is a key political concept because it provides incentive for much of the political activity. For example, Lord Red Senior is worried that his rival, Lord Blue Senior, is going to get a fied which Lord Red wants. So, Lord Red turns to his protege, Lord Orange Junior, to attack Lord Blue in public. The fief goes to Lord Red instead of Lord Blue, and Lord Red helps Lord Orange at a later date.


slot_troop_will_join_prison_break      = 161

#SB : 193 for npc as of 1.168
troop_slots_reserved_for_relations_start        = 165 #this is based on id_troops, and might change

slot_troop_relations_begin				= 0 #this creates an array for relations between troops
											#Right now, lords start at 165 and run to around 290, including pretenders



########################################################
##  PLAYER SLOTS           #############################
########################################################

slot_player_spawned_this_round                 = 0
slot_player_last_rounds_used_item_earnings     = 1
slot_player_selected_item_indices_begin        = 2
slot_player_selected_item_indices_end          = 11
slot_player_cur_selected_item_indices_begin    = slot_player_selected_item_indices_end
slot_player_cur_selected_item_indices_end      = slot_player_selected_item_indices_end + 9
slot_player_join_time                          = 21
slot_player_button_index                       = 22 #used for presentations
slot_player_can_answer_poll                    = 23
slot_player_first_spawn                        = 24
slot_player_spawned_at_siege_round             = 25
slot_player_poll_disabled_until_time           = 26
slot_player_total_equipment_value              = 27
slot_player_last_team_select_time              = 28
slot_player_death_pos_x                        = 29
slot_player_death_pos_y                        = 30
slot_player_death_pos_z                        = 31
slot_player_damage_given_to_target_1           = 32 #used only in destroy mod
slot_player_damage_given_to_target_2           = 33 #used only in destroy mod
slot_player_last_bot_count                     = 34
slot_player_bot_type_1_wanted                  = 35
slot_player_bot_type_2_wanted                  = 36
slot_player_bot_type_3_wanted                  = 37
slot_player_bot_type_4_wanted                  = 38
slot_player_spawn_count                        = 39

########################################################
##  TEAM SLOTS             #############################
########################################################

slot_team_flag_situation                       = 0




#Rebellion changes end
###########################################################################################################################
#####                                                MODULE SETTINGS                                                  #####
###########################################################################################################################



# script_mcc_generate_skill_set modes
limit_to_stats                         = 0
equip_the_player                       = 1

###########################################################################################################################
#####                                              CHARACTER BACKGROUNDS                                              #####
###########################################################################################################################

# character backgrounds
cb_slave = 0
cb_freeman = 1
cb_noble = 2

cb2_strong = 0
cb2_thin = 1
cb2_weak = 2

cb3_genius = 0
cb3_shrewd = 1
cb3_normal = 2
cb3_dull = 3

#NPC system changes end
#Encounter types
enctype_fighting_against_village_raid = 1
enctype_catched_during_village_raid   = 2


### Troop occupations slot_troop_occupation
##slto_merchant           = 1
slto_inactive           = 0 #for companions at the beginning of the game

slto_kingdom_hero       = 2

slto_player_companion   = 5 #This is specifically for companions in the employ of the player -- ie, in the party, or on a mission
slto_kingdom_lady       = 6 #Usually inactive (Calradia is a traditional place). However, can be made potentially active if active_npcs are expanded to include ladies
# slto_kingdom_seneschal  = 7
slto_robber_knight      = 8
slto_inactive_pretender = 9


stl_unassigned          = -1
stl_reserved_for_player = -2
stl_rejected_by_player  = -3

#NPC changes begin
slto_retirement      = 11
#slto_retirement_medium    = 12
#slto_retirement_short     = 13
#NPC changes end
##diplomacy start+

#These constants are not (yet) used, but they are defined so that other mods can
#extend diplomacy in a consistent way, and have confidence that base diplomacy
#will correctly respect the flags they set.

#Note that the existing code assumes that dplmc_slto_exile and dplmc_slto_dead are
#greater than slto_retirement.  If you had to change this, look around for every instance
#where diplomacy checks "troop_slot_ge" slto_retirement, and expand it to also check
#dead, exiled, etc.

dplmc_slto_exile           = 14 #Set for newly exiled lords.  In saved games, this is retroactively applied (once only).
dplmc_slto_dead            = 15 #not normally set
##diplomacy end+

########################################################
##  QUEST SLOTS            #############################
########################################################

slot_quest_target_center            = 1
slot_quest_target_troop             = 2
slot_quest_target_faction           = 3
slot_quest_object_troop             = 4
##slot_quest_target_troop_is_prisoner = 5
slot_quest_giver_troop              = 6
slot_quest_object_center            = 7
slot_quest_target_party             = 8
slot_quest_target_party_template    = 9
slot_quest_target_amount            = 10
slot_quest_current_state            = 11
slot_quest_giver_center             = 12
slot_quest_target_dna               = 13
slot_quest_target_item              = 14
slot_quest_object_faction           = 15

#only used for ernak quest
slot_quest_target_onoguroi          = 13
slot_quest_target_saraguroi         = 14
slot_quest_target_kutriguroi        = 15


slot_quest_target_state             = 16
slot_quest_object_state             = 17

slot_quest_convince_value           = 19
slot_quest_importance               = 20
slot_quest_xp_reward                = 21
slot_quest_gold_reward              = 22
slot_quest_expiration_days          = 23
slot_quest_dont_give_again_period   = 24
slot_quest_dont_give_again_remaining_days = 25

slot_quest_failure_consequence      = 26
slot_quest_temp_slot      			= 27
slot_quest_delegate_level      		= 28 #SB : threshold for delegating quests, -1 for disable

########################################################
##  PARTY TEMPLATE SLOTS   #############################
########################################################

# Ryan BEGIN
slot_party_template_num_killed   = 1

slot_party_template_lair_type    	 	= 3
slot_party_template_lair_party    		= 4
slot_party_template_lair_spawnpoint     = 5


# Ryan END


########################################################
##  SCENE PROP SLOTS       #############################
########################################################

scene_prop_open_or_close_slot       = 1
scene_prop_smoke_effect_done        = 2
scene_prop_number_of_agents_pushing = 3 #for belfries only
scene_prop_next_entry_point_id      = 4 #for belfries only
scene_prop_belfry_platform_moved    = 5 #for belfries only
scene_prop_slots_end                = 6

########################################################
rel_enemy   = 0
rel_neutral = 1
rel_ally    = 2


#Talk contexts
tc_town_talk                  = 0
tc_court_talk                 = 1
tc_party_encounter            = 2
tc_castle_gate                = 3
tc_siege_commander            = 4
tc_join_battle_ally           = 5
tc_join_battle_enemy          = 6
tc_castle_commander           = 7
tc_hero_freed                 = 8
tc_hero_defeated              = 9
tc_entering_center_quest_talk = 10
tc_back_alley                 = 11
tc_siege_won_seneschal        = 12
tc_ally_thanks                = 13
tc_tavern_talk                = 14
tc_rebel_thanks               = 15
tc_garden                     = 16
tc_courtship                  = 16
tc_after_duel                 = 17
tc_prison_break               = 18
tc_escape                     = 19
tc_give_center_to_fief        = 20
tc_merchants_house            = 21

tc_attila_bastard_son_duel    = 22

#Troop Commentaries begin
#Log entry types
#civilian
logent_village_raided            = 1
logent_village_extorted          = 2
logent_caravan_accosted          = 3 #in caravan accosted, center and troop object are -1, and the defender's faction is the object
logent_traveller_attacked        = 3 #in traveller attacked, origin and destination are center and troop object, and the attacker's faction is the object

logent_helped_peasants           = 4

logent_party_traded              = 5

logent_castle_captured_by_player              = 10
logent_lord_defeated_by_player                = 11
logent_lord_captured_by_player                = 12
logent_lord_defeated_but_let_go_by_player     = 13
logent_player_defeated_by_lord                = 14
logent_player_retreated_from_lord             = 15
logent_player_retreated_from_lord_cowardly    = 16
logent_lord_helped_by_player                  = 17
logent_player_participated_in_siege           = 18
logent_player_participated_in_major_battle    = 19
logent_castle_given_to_lord_by_player         = 20

logent_pledged_allegiance          = 21
logent_liege_grants_fief_to_vassal = 22


logent_renounced_allegiance      = 23

logent_player_claims_throne_1    		               = 24
logent_player_claims_throne_2    		               = 25


logent_troop_feels_cheated_by_troop_over_land		   = 26
logent_ruler_intervenes_in_quarrel                     = 27
logent_lords_quarrel_over_land                         = 28
logent_lords_quarrel_over_insult                       = 29
logent_marshal_vs_lord_quarrel                  	   = 30
logent_lords_quarrel_over_woman                        = 31

logent_lord_protests_marshall_appointment			   = 32
logent_lord_blames_defeat						   	   = 33

logent_player_suggestion_succeeded					   = 35
logent_player_suggestion_failed					       = 36

logent_liege_promises_fief_to_vassal				   = 37

logent_lord_insults_lord_for_cowardice                 = 38
logent_lord_insults_lord_for_rashness                  = 39
logent_lord_insults_lord_for_abandonment               = 40
logent_lord_insults_lord_for_indecision                = 41
logent_lord_insults_lord_for_cruelty                   = 42
logent_lord_insults_lord_for_dishonor                  = 43




logent_game_start                           = 45
logent_poem_composed                        = 46 ##Not added
logent_tournament_distinguished             = 47 ##Not added
logent_tournament_won                       = 48 ##Not added

#logent courtship - lady is always actor, suitor is always troop object
logent_lady_favors_suitor                   = 51 #basically for gossip
logent_lady_betrothed_to_suitor_by_choice   = 52
logent_lady_betrothed_to_suitor_by_family   = 53
logent_lady_rejects_suitor                  = 54
logent_lady_father_rejects_suitor           = 55
logent_lady_marries_lord                    = 56
logent_lady_elopes_with_lord                = 57
logent_lady_rejected_by_suitor              = 58
logent_lady_betrothed_to_suitor_by_pressure = 59 #mostly for gossip

logent_lady_and_suitor_break_engagement		= 60
logent_lady_marries_suitor				    = 61

logent_lord_holds_lady_hostages             = 62
logent_challenger_defeats_lord_in_duel      = 63
logent_challenger_loses_to_lord_in_duel     = 64

logent_player_stole_cattles_from_village    = 66

logent_party_spots_wanted_bandits           = 70


logent_border_incident_cattle_stolen          = 72 #possibly add this to rumors for non-player faction
logent_border_incident_bride_abducted         = 73 #possibly add this to rumors for non-player faction
logent_border_incident_villagers_killed       = 74 #possibly add this to rumors for non-player faction
logent_border_incident_subjects_mistreated    = 75 #possibly add this to rumors for non-player faction

#These supplement caravans accosted and villages burnt, in that they create a provocation. So far, they only refer to the player
logent_border_incident_troop_attacks_neutral  = 76
logent_border_incident_troop_breaks_truce     = 77
logent_border_incident_troop_suborns_lord   = 78


logent_policy_ruler_attacks_without_provocation             = 80
logent_policy_ruler_ignores_provocation                     = 81 #possibly add this to rumors for non-player factions
logent_policy_ruler_makes_peace_too_soon                    = 82
logent_policy_ruler_declares_war_with_justification         = 83
logent_policy_ruler_breaks_truce                            = 84
logent_policy_ruler_issues_indictment_just                  = 85 #possibly add this to rumors for non-player faction
logent_policy_ruler_issues_indictment_questionable          = 86 #possibly add this to rumors for non-player faction

logent_player_faction_declares_war                          = 90 #this doubles for declare war to extend power
logent_faction_declares_war_out_of_personal_enmity          = 91
logent_faction_declares_war_to_regain_territory             = 92
logent_faction_declares_war_to_curb_power                   = 93
logent_faction_declares_war_to_respond_to_provocation       = 94
##diplomacy begin
logent_faction_declares_war_to_fulfil_pact                  = 95
logent_war_declaration_types_end                            = 96
##diplomacy end
logent_player_renamed_capital = 97 #SB : unused logged event
# logent_executed_prisoners = 97
# logent_rejected_bodyguards = 98

#logent_lady_breaks_betrothal_with_lord      = 58
#logent_lady_betrothal_broken_by_lord        = 59

#lord reputation type, for commentaries
#"Martial" will be twice as common as the other types
lrep_none           = 0
lrep_martial        = 1 #chivalrous but not terribly empathetic or introspective, - eg Richard Lionheart, your average 14th century French baron
lrep_quarrelsome    = 2 #spiteful, cynical, a bit paranoid, possibly hotheaded - eg Robert Graves' Tiberius, some of Charles VI's uncles
lrep_selfrighteous  = 3 #coldblooded, moralizing, often cruel - eg William the Conqueror, Timur, Octavian, Aurangzeb (although he is arguably upstanding instead, particularly after his accession)
lrep_cunning        = 4 #coldblooded, pragmatic, amoral - eg Louis XI, Guiscard, Akbar Khan, Abd al-Aziz Ibn Saud
lrep_debauched      = 5 #spiteful, amoral, sadistic - eg Caligula, Tuchman's Charles of Navarre
lrep_goodnatured    = 6 #chivalrous, benevolent, perhaps a little too decent to be a good warlord - eg Hussein ibn Ali. Few well-known historical examples maybe. because many lack the drive to rise to faction leadership. Ranjit Singh has aspects
lrep_upstanding     = 7 #moralizing, benevolent, pragmatic, - eg Bernard Cornwell's Alfred, Charlemagne, Salah al-Din, Sher Shah Suri

lrep_roguish        = 8 #used for commons, specifically ex-companions. Tries to live life as a lord to the full
lrep_benefactor     = 9 #used for commons, specifically ex-companions. Tries to improve lot of folks on land
lrep_custodian      = 10 #used for commons, specifically ex-companions. Tries to maximize fief's earning potential

#lreps specific to dependent noblewomen
lrep_conventional    = 21 #Charlotte York in SATC seasons 1-2, probably most medieval aristocrats
lrep_adventurous     = 22 #Tomboyish. However, this basically means that she likes to travel and hunt, and perhaps yearn for wider adventures. However, medieval noblewomen who fight are rare, and those that attempt to live independently of a man are rarer still, and best represented by pre-scripted individuals like companions
lrep_otherworldly    = 23 #Prone to mysticism, romantic.
lrep_ambitious       = 24 #Lady Macbeth
lrep_moralist        = 25 #Equivalent of upstanding or benefactor -- takes nobless oblige, and her traditional role as repository of morality, very seriously. Based loosely on Christine de Pisa

#a more complicated system of reputation could include the following...

#successful vs unlucky -- basic gauge of success
#daring vs cautious -- maybe not necessary
#honorable/pious/ideological vs unscrupulous -- character's adherance to an external code of conduct. Fails to capture complexity of people like Aurangzeb, maybe, but good for NPCs
	#(visionary/altruist and orthodox/unorthodox could be a subset of the above, or the specific external code could be another tag)
#generous/loyal vs manipulative/exploitative -- character's sense of duty to specific individuals, based on their relationship. Affects loyalty of troops, etc
#merciful vs cruel/ruthless/sociopathic -- character's general sense of compassion. Sher Shah is example of unscrupulous and merciful (the latter to a degree).
#dignified vs unconventional -- character's adherance to social conventions. Very important, given the times

##diplomacy start+
#Define these for clarity and convenience elsewhere
dplmc_lrep_ladies_begin = lrep_conventional
dplmc_lrep_ladies_end = lrep_moralist + 1

dplmc_lrep_commoners_begin = lrep_roguish
dplmc_lrep_commoners_end = dplmc_lrep_ladies_begin

dplmc_lrep_nobles_including_liege_begin = lrep_none
dplmc_lrep_nobles_begin = lrep_martial
dplmc_lrep_nobles_end = dplmc_lrep_commoners_begin
##diplomacy end+

courtship_poem_tragic      = 1 #Emphasizes longing, Laila and Majnoon
courtship_poem_heroic      = 2 #Norse sagas with female heroines
courtship_poem_comic       = 3 #Emphasis on witty repartee -- Contrasto (Sicilian school satire)
courtship_poem_mystic      = 4 #Sufi poetry. Song of Songs
courtship_poem_allegoric   = 5 #Idealizes woman as a civilizing force -- the Romance of the Rose, Siege of the Castle of Love

#courtship gifts currently deprecated







#Troop Commentaries end

tutorial_fighters_begin = "trp_tutorial_fighter_1"
tutorial_fighters_end   = "trp_tutorial_archer_1"

#Walker types:
walkert_default            = 0
walkert_needs_money        = 1
walkert_needs_money_helped = 2
walkert_spy                = 3
num_town_walkers = 8
town_walker_entries_start = 32

reinforcement_cost_easy = 600
reinforcement_cost_moderate = 450
reinforcement_cost_hard = 300

merchant_toll_duration        = 72 #Tolls are valid for 72 hours

hero_escape_after_defeat_chance = 70


raid_distance = 4

surnames_begin = "str_surname_1"
surnames_end = "str_surnames_end"
names_begin = "str_name_1"
names_end = surnames_begin
countersigns_begin = "str_countersign_1"
countersigns_end = names_begin
secret_signs_begin = "str_secret_sign_1"
secret_signs_end = countersigns_begin

kingdom_titles_male_begin = "str_faction_title_male_player"
kingdom_titles_female_begin = "str_faction_title_female_player"

major_cultures_begin = "fac_culture_1"
major_cultures_end   = "fac_culture_minor_1"

minor_cultures_begin = "fac_culture_minor_1"
minor_cultures_end   = "fac_player_faction"

##diplomacy start+
cultures_begin = "fac_culture_1"
cultures_end   = major_cultures_end #changed so the player is unable to select minor cultures
#cultures_end   = "fac_player_faction"
##diplomacy end+

kingdoms_begin = "fac_player_supporters_faction"
kingdoms_end = "fac_kingdoms_end"

npc_kingdoms_begin = "fac_kingdom_1"
npc_kingdoms_end = kingdoms_end

minor_kingdoms_begin = "fac_minor_aestii"
minor_kingdoms_end = "fac_minor_factions_end"

bandits_begin = "trp_looter"
bandits_end = "trp_rich_bandit" #changed due to quest characters

kingdom_ladies_begin = "trp_knight_1_1_wife"
kingdom_ladies_end = "trp_heroes_end"

#active NPCs in order: companions, kings, lords, pretenders

pretenders_begin = "trp_kingdom_1_pretender"
pretenders_end = kingdom_ladies_begin

lords_begin = "trp_knight_1_1"
lords_end = pretenders_begin

kings_begin = "trp_kingdom_1_lord"
kings_end = lords_begin

companions_begin = "trp_npc1"
companions_end = kings_begin

active_npcs_begin = "trp_npc1"
active_npcs_end = kingdom_ladies_begin

minor_kings_begin = "trp_aestii_king"
minor_kings_end = "trp_aestii_merchant_1"

minor_merchants_begin = "trp_aestii_merchant_1"
minor_merchants_end = "trp_roman_landowner"
#"active_npcs_begin replaces kingdom_heroes_begin to allow for companions to become lords. Includes anyone who may at some point lead their own party: the original kingdom heroes, companions who may become kingdom heroes, and pretenders. (slto_kingdom_hero as an occupation means that you lead a party on the map. Pretenders have the occupation "slto_inactive_pretender", even if they are part of a player's party, until they have their own independent party)
#If you're a modder and you don't want to go through and switch every kingdom_heroes to active_npcs, simply define a constant: kingdom_heroes_begin = active_npcs_begin., and kingdom_heroes_end = active_npcs_end. I haven't tested for that, but I think it should work.

active_npcs_including_player_begin = "trp_kingdom_heroes_including_player_begin"
original_kingdom_heroes_begin = "trp_kingdom_1_lord"

heroes_begin = active_npcs_begin
heroes_end = kingdom_ladies_end

soldiers_begin = "trp_farmer"
soldiers_end = "trp_town_walker_1"

#Rebellion changes

##rebel_factions_begin = "fac_kingdom_1_rebels"
##rebel_factions_end =   "fac_kingdoms_end"

pretenders_begin = "trp_kingdom_1_pretender"
pretenders_end = active_npcs_end
#Rebellion changes

tavern_minstrels_begin = "trp_tavern_minstrel_1"
tavern_minstrels_end   = "trp_kingdom_heroes_including_player_begin"

tavern_booksellers_begin = "trp_tavern_bookseller_1"
tavern_booksellers_end   = tavern_minstrels_begin

tavern_travelers_begin = "trp_tavern_traveler_1"
tavern_travelers_end   = tavern_booksellers_begin

ransom_brokers_begin = "trp_ransom_broker_1"
ransom_brokers_end   = tavern_travelers_begin

mercenary_troops_begin = "trp_caravan_guard"
mercenary_troops_end = "trp_mercenaries_end"

multiplayer_troops_begin = "trp_swadian_crossbowman_multiplayer"
multiplayer_troops_end = "trp_multiplayer_end"

multiplayer_ai_troops_begin = "trp_swadian_crossbowman_multiplayer_ai"
multiplayer_ai_troops_end = multiplayer_troops_begin

multiplayer_scenes_begin = "scn_multi_scene_1"
multiplayer_scenes_end = "scn_multiplayer_maps_end"

multiplayer_scene_names_begin = "str_multi_scene_1"
multiplayer_scene_names_end = "str_multi_scene_end"

multiplayer_flag_projections_begin = "mesh_flag_project_sw"
multiplayer_flag_projections_end = "mesh_flag_projects_end"

multiplayer_flag_taken_projections_begin = "mesh_flag_project_sw_miss"
multiplayer_flag_taken_projections_end = "mesh_flag_project_misses_end"

multiplayer_game_type_names_begin = "str_multi_game_type_1"
multiplayer_game_type_names_end = "str_poll_kick_player_s1_by_s0" #SB : unused but moved range anyway

quick_battle_troops_begin = "trp_quick_battle_troop_1"
quick_battle_troops_end = "trp_quick_battle_troops_end"

quick_battle_troop_texts_begin = "str_quick_battle_troop_1"
quick_battle_troop_texts_end = "str_quick_battle_troops_end"

quick_battle_scenes_begin = "scn_quick_battle_scene_1"
quick_battle_scenes_end = "scn_quick_battle_maps_end"

quick_battle_scene_images_begin = "mesh_cb_ui_maps_scene_01"

quick_battle_battle_scenes_begin = quick_battle_scenes_begin
quick_battle_battle_scenes_end = "scn_quick_battle_scene_4"

quick_battle_siege_scenes_begin = quick_battle_battle_scenes_end
quick_battle_siege_scenes_end = quick_battle_scenes_end

quick_battle_scene_names_begin = "str_quick_battle_scene_1"

lord_quests_begin = "qst_deliver_message"
lord_quests_end   = "qst_follow_army"

lord_quests_begin_2 = "qst_destroy_bandit_lair"
lord_quests_end_2   = "qst_blank_quest_2"

enemy_lord_quests_begin = "qst_lend_surgeon"
enemy_lord_quests_end   = lord_quests_end

village_elder_quests_begin = "qst_deliver_grain"
village_elder_quests_end = "qst_eliminate_bandits_infesting_village"

village_elder_quests_begin_2 = "qst_blank_quest_6"
village_elder_quests_end_2   = "qst_blank_quest_6"

mayor_quests_begin  = "qst_move_cattle_herd"
mayor_quests_end    = village_elder_quests_begin

mayor_quests_begin_2 = "qst_blank_quest_11"
mayor_quests_end_2   = "qst_blank_quest_11"

lady_quests_begin = "qst_rescue_lord_by_replace"
lady_quests_end   = mayor_quests_begin

lady_quests_begin_2 = "qst_blank_quest_16"
lady_quests_end_2   = "qst_blank_quest_16"

army_quests_begin = "qst_deliver_cattle_to_army"
army_quests_end   = lady_quests_begin

army_quests_begin_2 = "qst_blank_quest_21"
army_quests_end_2   = "qst_blank_quest_21"

player_realm_quests_begin = "qst_resolve_dispute"
player_realm_quests_end = "qst_destroy_bandit_lair" #SB : probably right offset, it's unused anyway

player_realm_quests_begin_2 = "qst_blank_quest_26"
player_realm_quests_end_2 = "qst_blank_quest_26"

all_items_begin = 0
all_items_end = "itm_ccoop_new_items_end" #SB : new ccoop stuff
normal_items_end = "itm_dplmc_coat_of_plates_red_constable"

all_quests_begin = 0
all_quests_end = "qst_quests_end"
#SB : companion range - these are quests that can be reasonably completed by 1 non-political individual
delegate_quests_begin = all_quests_begin
delegate_quests_end = "qst_eliminate_bandits_infesting_village"

towns_begin = "p_town_1"
castles_begin = "p_castle_1"
villages_begin = "p_village_1"

towns_end = castles_begin
castles_end = villages_begin
villages_end   = "p_salt_mine"

walled_centers_begin = towns_begin
walled_centers_end   = castles_end

centers_begin = towns_begin
centers_end   = villages_end

#this is used for the asynchronous triggers
number_of_castles        = p_village_1 - p_castle_1
number_of_villages       = p_salt_mine - p_village_1
number_of_towns          = p_castle_1 - p_town_1
number_of_walled_centers = number_of_towns+number_of_castles
number_of_centers        = number_of_walled_centers + number_of_villages
number_of_factions       = fac_kingdoms_end - fac_player_supporters_faction
number_of_active_npcs    = trp_knight_1_1_wife - trp_npc1

training_grounds_begin   = "p_training_ground_1"
training_grounds_end     = "p_looter_spawn_point"

scenes_begin = "scn_town_1_center"
scenes_end = "scn_castle_1_exterior"

spawn_points_begin = "p_zendar"
spawn_points_end = "p_spawn_points_end"

regular_troops_begin       = "trp_novice_fighter"
regular_troops_end         = "trp_tournament_master"

# swadian_merc_parties_begin = "p_town_1_mercs"
# swadian_merc_parties_end   = "p_town_8_mercs"

# vaegir_merc_parties_begin  = "p_town_8_mercs"
# vaegir_merc_parties_end    = "p_zendar"


arena_masters_begin    = "trp_town_1_arena_master"
arena_masters_end      = "trp_town_1_armorer"

#SB : replaced spelling of "gound"
training_ground_trainers_begin    = "trp_trainer_1"
training_ground_trainers_end      = "trp_ransom_broker_1"

town_walkers_begin = "trp_town_walker_1"
town_walkers_end = "trp_village_walker_1"

village_walkers_begin = "trp_village_walker_1"
village_walkers_end   = "trp_spy_walker_1"

spy_walkers_begin = "trp_spy_walker_1"
spy_walkers_end = "trp_tournament_master"

walkers_begin = town_walkers_begin
walkers_end   = spy_walkers_end

armor_merchants_begin  = "trp_town_1_armorer"
armor_merchants_end    = "trp_town_1_weaponsmith"

weapon_merchants_begin = "trp_town_1_weaponsmith"
weapon_merchants_end   = "trp_town_1_tavernkeeper"

tavernkeepers_begin    = "trp_town_1_tavernkeeper"
tavernkeepers_end      = "trp_town_1_merchant"

goods_merchants_begin  = "trp_town_1_merchant"
goods_merchants_end    = "trp_town_1_horse_merchant"

horse_merchants_begin  = "trp_town_1_horse_merchant"
horse_merchants_end    = "trp_town_1_mayor"

mayors_begin           = "trp_town_1_mayor"
mayors_end             = "trp_village_1_elder"

village_elders_begin   = "trp_village_1_elder"
village_elders_end     = "trp_merchants_end"

startup_merchants_begin = "trp_swadian_merchant"
startup_merchants_end = "trp_startup_merchants_end"

##diplomacy start+
tournament_champions_begin = "trp_Xerina"
tournament_champions_end   = "trp_tutorial_trainer"

merchants_begin = armor_merchants_begin
merchants_end = village_elders_end

dplmc_employees_begin = "trp_dplmc_chamberlain" #Individual employees (chancellor, constable, chamberlain)
dplmc_employees_end   = "trp_dplmc_messenger"   #The messenger is not included, since it's a generic figure rather than a specific person.

dplmc_prev_employee = "trp_dplmc_chamberlain" #SB : trp_dplmc_chamberlain = 930 now some invasion template, we need this id for old savegames

#SB : salaries
dplmc_spouse_salary = 10
dplmc_minister_salary = 15
dplmc_employee_appoint_cost = 20
dplmc_chamberlain_salary = dplmc_minister_salary
dplmc_constable_salary = dplmc_chamberlain_salary
dplmc_chancellor_salary = dplmc_employee_appoint_cost
dplmc_recruiter_salary = dplmc_spouse_salary
dplmc_recruits_cost = dplmc_chancellor_salary
dplmc_trainers_cost = dplmc_recruiter_salary

#SB : craftsmen
craftsman_begin = "trp_town_1_master_craftsman"
craftsman_end = "trp_zendar_chest"
##diplomacy end+


num_max_items = 10000 #used for multiplayer mode

average_price_factor = 1000
minimum_price_factor = 100
maximum_price_factor = 10000

village_prod_min = 0 #was -5
village_prod_max = 20 #was 20

trade_goods_begin = "itm_spice"
trade_goods_end = "itm_siege_supply"
food_begin = "itm_smoked_fish"
food_end = "itm_siege_supply"
reference_books_begin = "itm_book_wound_treatment_reference"
reference_books_end   = trade_goods_begin
readable_books_begin = "itm_book_tactics"
readable_books_end   = reference_books_begin
books_begin = readable_books_begin
books_end = reference_books_end
horses_begin = "itm_sumpter_horse"
horses_end = "itm_arrows"
weapons_begin = "itm_wooden_stick"
weapons_end = "itm_tab_shield_round_a"
ranged_weapons_begin = "itm_stones"
ranged_weapons_end = "itm_torch_old"
armors_begin = "itm_leather_gloves"
armors_end = "itm_wooden_stick"
shields_begin = "itm_tab_shield_round_a"
shields_end = "itm_lyre"

coop_new_items_end = all_items_end

# Banner constants

banner_meshes_begin = "mesh_banner_a01"
banner_meshes_end_minus_one = "mesh_banner_end"

arms_meshes_begin = "mesh_arms_a01"
arms_meshes_end_minus_one = "mesh_arms_end"

custom_banner_charges_begin = "mesh_custom_banner_charge_01"
custom_banner_charges_end = "mesh_tableau_mesh_custom_banner"

custom_banner_backgrounds_begin = "mesh_custom_banner_bg"
custom_banner_backgrounds_end = custom_banner_charges_begin

custom_banner_flag_types_begin = "mesh_custom_banner_01"
custom_banner_flag_types_end = custom_banner_backgrounds_begin

custom_banner_flag_map_types_begin = "mesh_custom_map_banner_01"
custom_banner_flag_map_types_end = custom_banner_flag_types_begin

custom_banner_flag_scene_props_begin = "spr_custom_banner_01"
custom_banner_flag_scene_props_end = "spr_banner_a"

custom_banner_map_icons_begin = "icon_custom_banner_01"
custom_banner_map_icons_end = "icon_map_flag_kingdom_1"

#banner_map_icons_begin = "icon_banner_01"
banner_map_icons_begin = "icon_map_flag_kingdom_1"
banner_map_icons_end_minus_one = "icon_banner_169"

banner_scene_props_begin = "spr_banner_a"
banner_scene_props_end_minus_one = "spr_banner_end"

#visigoths - ostrogoths - vandals
vis_banners_begin_offset = 1
vis_banners_end_offset = 9

ost_banners_begin_offset = 10
ost_banners_end_offset = 19

van_banners_begin_offset = 20
van_banners_end_offset = 29
#alemmanni
g1_banners_begin_offset = 30
g1_banners_end_offset = 36
#salian
g2_banners_begin_offset = 37
g2_banners_end_offset = 43
#burgundian
g3_banners_begin_offset = 44
g3_banners_end_offset = 50
#suebi
g4_banners_begin_offset = 51
g4_banners_end_offset = 57
#ripuarian franks
g4_banners_begin_offset = 58
g4_banners_end_offset = 63
#gepids
g5_banners_begin_offset = 64
g5_banners_end_offset = 70
#jutes
g7_banners_begin_offset = 71
g7_banners_end_offset = 77
#saxons
g8_banners_begin_offset = 78
g8_banners_end_offset = 84

caucasian_1_banners_begin_offset = 99 #lazika
caucasian_1_banners_end_offset = 103

caucasian_2_banners_begin_offset = 104 #iberia
caucasian_2_banners_end_offset = 109

west_banners_begin_offset = 85
west_banners_end_offset = 97

east_banners_begin_offset = 98
east_banners_end_offset = 109

brit_banners_begin_offset = 110
brit_banners_end_offset = 115 

pict_banners_begin_offset = 116
pict_banners_end_offset = 120

berber_banners_begin_offset = 121
berber_banners_end_offset = 126

sarranid_banners_begin_offset = 127
sarranid_banners_end_offset = 138

khergit_banners_begin_offset = 138
khergit_banners_end_offset = 147
#lombards
g9_banners_begin_offset = 148
g9_banners_end_offset = 155
#thuringians
g10_banners_begin_offset = 156
g10_banners_end_offset = 163
#end germanic banners
#rugii
g6_banners_begin_offset = 164
g6_banners_end_offset = 168

banners_end_offset = 169

# Some constants for merchant invenotries
merchant_inventory_space = 30
num_merchandise_goods = 40

num_max_river_pirates = 25
num_max_zendar_peasants = 25
num_max_zendar_manhunters = 10

num_max_dp_bandits = 10
num_max_refugees = 10
num_max_deserters = 10

num_max_militia_bands = 15
num_max_armed_bands = 12

num_max_vaegir_punishing_parties = 20
num_max_rebel_peasants = 25

num_max_frightened_farmers = 50
num_max_undead_messengers  = 20

num_forest_bandit_spawn_points = 1
num_mountain_bandit_spawn_points = 1
num_steppe_bandit_spawn_points = 1
num_taiga_bandit_spawn_points = 1
num_desert_bandit_spawn_points = 1
num_black_khergit_spawn_points = 1
num_sea_raider_spawn_points = 2
num_pirate_spawn_points = 1
num_bagaudae_spawn_points = 1
num_sabir_spawn_points = 1
num_coptic_spawn_points = 1
num_armenian_spawn_points = 1
num_arab_bandit_spawn_points = 1

num_scirii_horde_spawn_points = 1
num_heruli_horde_spawn_points = 1

num_aestii_spawn_points = 1
num_morden_spawn_points = 1
num_irish_spawn_points = 1
num_garamantian_spawn_points = 1
num_danish_spawn_points = 1
num_sporoi_spawn_points = 1
num_bosphoran_spawn_points = 1
num_abagasian_spawn_points = 1
num_tauri_spawn_points = 1
num_augundzi_spawn_points = 1
num_vidivarii_spawn_points = 1
num_frisian_spawn_points = 1
num_vascones_spawn_points = 1
num_gallaeci_spawn_points = 1
num_venedi_spawn_points = 1

peak_prisoner_trains = 4
peak_kingdom_caravans = 12
peak_kingdom_messengers = 3


# Note positions
note_troop_location = 3

#battle tactics
btactic_hold = 1
btactic_follow_leader = 2
btactic_charge = 3
btactic_stand_ground = 4

#default right mouse menu orders
cmenu_move = -7
cmenu_follow = -6

#default ones
cmenu_notes = 1
#SB : context menu cheats, some we roll into a menu instead
cmenu_attach = 9
cmenu_detach = 10
# cmenu_exchange = 11
cmenu_encounter = 12
# cmenu_spawnbandit = 13
cmenu_losebattle = 14
cmenu_winbattle = 15
# cmenu_reinforce = 16
# cmenu_heal = 17
# cmenu_wound = 18

# Town center modes - resets in game menus during the options
tcm_default 		= 0
tcm_disguised 		= 1
tcm_prison_break 	= 2
tcm_escape      	= 3


# Arena battle modes
#abm_fight = 0
abm_training = 1
abm_visit = 2
abm_tournament = 3

# Camp training modes
ctm_melee    = 1
ctm_ranged   = 2
ctm_mounted  = 3
ctm_training = 4 #unused

# Village bandits attack modes
vba_normal          = 1
vba_after_training  = 2

arena_tier1_opponents_to_beat = 3
arena_tier1_prize = 5
arena_tier2_opponents_to_beat = 6
arena_tier2_prize = 10
arena_tier3_opponents_to_beat = 10
arena_tier3_prize = 25
arena_tier4_opponents_to_beat = 20
arena_tier4_prize = 60
arena_grand_prize = 250


#Additions
price_adjustment = 25 #the percent by which a trade at a center alters price

fire_duration = 4 #fires takes 4 hours

#NORMAL ACHIEVEMENTS
ACHIEVEMENT_NONE_SHALL_PASS = 1,
ACHIEVEMENT_MAN_EATER = 2,
ACHIEVEMENT_THE_HOLY_HAND_GRENADE = 3,
ACHIEVEMENT_LOOK_AT_THE_BONES = 4,
ACHIEVEMENT_KHAAAN = 5,
ACHIEVEMENT_GET_UP_STAND_UP = 6,
ACHIEVEMENT_BARON_GOT_BACK = 7,
ACHIEVEMENT_BEST_SERVED_COLD = 8,
ACHIEVEMENT_TRICK_SHOT = 9,
ACHIEVEMENT_GAMBIT = 10,
ACHIEVEMENT_OLD_SCHOOL_SNIPER = 11,
ACHIEVEMENT_CALRADIAN_ARMY_KNIFE = 12,
ACHIEVEMENT_MOUNTAIN_BLADE = 13,
ACHIEVEMENT_HOLY_DIVER = 14,
ACHIEVEMENT_FORCE_OF_NATURE = 15,

#SKILL RELATED ACHIEVEMENTS:
ACHIEVEMENT_BRING_OUT_YOUR_DEAD = 16,
ACHIEVEMENT_MIGHT_MAKES_RIGHT = 17,
ACHIEVEMENT_COMMUNITY_SERVICE = 18,
ACHIEVEMENT_AGILE_WARRIOR = 19,
ACHIEVEMENT_MELEE_MASTER = 20,
ACHIEVEMENT_DEXTEROUS_DASTARD = 21,
ACHIEVEMENT_MIND_ON_THE_MONEY = 22,
ACHIEVEMENT_ART_OF_WAR = 23,
ACHIEVEMENT_THE_RANGER = 24,
ACHIEVEMENT_TROJAN_BUNNY_MAKER = 25,

#MAP RELATED ACHIEVEMENTS:
ACHIEVEMENT_MIGRATING_COCONUTS = 26,
ACHIEVEMENT_HELP_HELP_IM_BEING_REPRESSED = 27,
ACHIEVEMENT_SARRANIDIAN_NIGHTS = 28,
ACHIEVEMENT_OLD_DIRTY_SCOUNDREL = 29,
ACHIEVEMENT_THE_BANDIT = 30,
ACHIEVEMENT_GOT_MILK = 31,
ACHIEVEMENT_SOLD_INTO_SLAVERY = 32,
ACHIEVEMENT_MEDIEVAL_TIMES = 33,
ACHIEVEMENT_GOOD_SAMARITAN = 34,
ACHIEVEMENT_MORALE_LEADER = 35,
ACHIEVEMENT_ABUNDANT_FEAST = 36,
ACHIEVEMENT_BOOK_WORM = 37,
ACHIEVEMENT_ROMANTIC_WARRIOR = 38,

#POLITICALLY ORIENTED ACHIEVEMENTS:
ACHIEVEMENT_HAPPILY_EVER_AFTER = 39,
ACHIEVEMENT_HEART_BREAKER = 40,
ACHIEVEMENT_AUTONOMOUS_COLLECTIVE = 41,
ACHIEVEMENT_I_DUB_THEE = 42,
ACHIEVEMENT_SASSY = 43,
ACHIEVEMENT_THE_GOLDEN_THRONE = 44,
ACHIEVEMENT_KNIGHTS_OF_THE_ROUND = 45,
ACHIEVEMENT_TALKING_HELPS = 46,
ACHIEVEMENT_KINGMAKER = 47,
ACHIEVEMENT_PUGNACIOUS_D = 48,
ACHIEVEMENT_GOLD_FARMER = 49,
ACHIEVEMENT_ROYALITY_PAYMENT = 50,
ACHIEVEMENT_MEDIEVAL_EMLAK = 51,
ACHIEVEMENT_CALRADIAN_TEA_PARTY = 52,
ACHIEVEMENT_MANIFEST_DESTINY = 53,
ACHIEVEMENT_CONCILIO_CALRADI = 54,
ACHIEVEMENT_VICTUM_SEQUENS = 55,

#MULTIPLAYER ACHIEVEMENTS:
ACHIEVEMENT_THIS_IS_OUR_LAND = 56,
ACHIEVEMENT_SPOIL_THE_CHARGE = 57,
ACHIEVEMENT_HARASSING_HORSEMAN = 58,
ACHIEVEMENT_THROWING_STAR = 59,
ACHIEVEMENT_SHISH_KEBAB = 60,
ACHIEVEMENT_RUIN_THE_RAID = 61,
ACHIEVEMENT_LAST_MAN_STANDING = 62,
ACHIEVEMENT_EVERY_BREATH_YOU_TAKE = 63,
ACHIEVEMENT_CHOPPY_CHOP_CHOP = 64,
ACHIEVEMENT_MACE_IN_YER_FACE = 65,
ACHIEVEMENT_THE_HUSCARL = 66,
ACHIEVEMENT_GLORIOUS_MOTHER_FACTION = 67,
ACHIEVEMENT_ELITE_WARRIOR = 68,

#COMBINED ACHIEVEMENTS
ACHIEVEMENT_SON_OF_ODIN = 69,
ACHIEVEMENT_KING_ARTHUR = 70,
ACHIEVEMENT_KASSAI_MASTER = 71,
ACHIEVEMENT_IRON_BEAR = 72,
ACHIEVEMENT_LEGENDARY_RASTAM = 73,
ACHIEVEMENT_SVAROG_THE_MIGHTY = 74,

ACHIEVEMENT_MAN_HANDLER = 75,
ACHIEVEMENT_GIRL_POWER = 76,
ACHIEVEMENT_QUEEN = 77,
ACHIEVEMENT_EMPRESS = 78,
ACHIEVEMENT_TALK_OF_THE_TOWN = 79,
ACHIEVEMENT_LADY_OF_THE_LAKE = 80,

###################################################################################
# AutoLoot: Modified Constants
# Most of these are slot definitions, make sure they do not clash with your mod's other slot usage
###################################################################################
# This is an item slot
dplmc_slot_item_difficulty = 5

  #### Autoloot improved by rubik begin
dplmc_slot_item_head_armor      = 6
dplmc_slot_item_body_armor      = 7
dplmc_slot_item_leg_armor       = 8

# slots redefine, no need to create more new slots, 3 is enough
dplmc_slot_item_thrust_damage      = dplmc_slot_item_head_armor
dplmc_slot_item_swing_damage       = dplmc_slot_item_body_armor
dplmc_slot_two_handed_one_handed   = dplmc_slot_item_leg_armor

dplmc_slot_item_horse_speed        = dplmc_slot_item_head_armor
dplmc_slot_item_horse_armor        = dplmc_slot_item_body_armor

dplmc_slot_item_shield_size        = dplmc_slot_item_head_armor
dplmc_slot_item_shield_armor       = dplmc_slot_item_body_armor

##diplomacy start+ slots redefined, re-use for rubik "auto buy food"
dplmc_slot_item_food_portion       = dplmc_slot_item_leg_armor

##New slot needed for rubik's Auto-Sell
dplmc_slot_item_type_not_for_sell  = 71
##diplomacy end+
  #### Autoloot improved by rubik end

# These are troops slots
##diplomacy start+ Altered because 154 is slot_troop_stance_on_faction_issue.
#(Companions can become lords, so parts of the auto-loot system had undesired consequences for promoted companions.)
dplmc_slot_upgrade_armor = 155 #was 153 before Diplomacy 4.0
dplmc_slot_upgrade_horse = 156 #was 154 before Diplomacy 4.0
##diplomacy end+
dplmc_slot_upgrade_wpn_0 = 157
dplmc_slot_upgrade_wpn_1 = 158
dplmc_slot_upgrade_wpn_2 = 159
dplmc_slot_upgrade_wpn_3 = 160

dplmc_wpn_setting_1                 = 1
dplmc_wpn_setting_2                 = 2
dplmc_armor_setting                 = 3
dplmc_horse_setting                 = 4
dplmc_loot_string = 30  #SB : string register to start recording loot changes
###################################################################################
# End Autoloot
###################################################################################

dplmc_npc_mission_war_request                 = 9
dplmc_npc_mission_alliance_request            = 10
dplmc_npc_mission_spy_request                 = 11
dplmc_npc_mission_gift_fief_request           = 12
dplmc_npc_mission_gift_horses_request         = 13
dplmc_npc_mission_threaten_request            = 14
dplmc_npc_mission_prisoner_exchange           = 15
dplmc_npc_mission_defensive_request           = 16
dplmc_npc_mission_trade_request               = 17
dplmc_npc_mission_nonaggression_request       = 18
dplmc_npc_mission_persuasion                  = 19
dplmc_npc_mission_rescue_prisoner             = 20 #SB : added for quest, using slot_troop_town_with_contacts
dplmc_npc_mission_delegate_quest              = 21 #SB : added for quest
npc_mission_tributary 						  = 22
#npc_mission_foederati_request				  = 23

dplmc_slot_troop_mission_diplomacy            = 162
dplmc_slot_troop_mission_diplomacy2           = 163
dplmc_slot_troop_political_stance             = 164 #dplmc+ deprecated, see note below
##diplomacy start+
#Though you may assume otherwise from the name,  dplmc_slot_troop_political_stance is
#actually used as a temporary slot (it's overwritten every time you start a conversation
#with your chancellor about who supports whom, and in Diplomacy 3.3.2 it isn't used
#elsewhere).
#   I'm giving it a new name to reflect its use, to avoid confusion.
dplmc_slot_troop_temp_slot                    = 164 #replaces dplmc_slot_troop_political_stance
##diplomacy end+
dplmc_slot_troop_affiliated                   = 165 ##notes: 0 is default, 1 is asked; on newer games 3 is affiliated and 4 is betrayed


##diplomacy end+

dplmc_spt_spouse                              = 19
dplmc_spt_gift_caravan                        = 21
spt_messenger                                 = 8 #no prefix since its outcommented in native
spt_patrol                                    = 7 #no prefix since its outcommented in native
#spt_player_field_army  						  = 22
spt_scout                                     = 10 #no prefix since its outcommented in native

# Merchantilism
# - Your caravans generate more revenue for your towns, but your benefit
#   from the caravans of other kingdoms is diminished.
# - Trade within the kingdom is made more efficient, while imports are
#   discouraged.
#

#For $g_dplmc_terrain_advantage
DPLMC_TERRAIN_ADVANTAGE_DISABLE     =  -1
DPLMC_TERRAIN_ADVANTAGE_ENABLE      =  0   #So I don't have to keep track of whether it is enabled or disabled by default

#For $g_dplmc_lord_recycling
DPLMC_LORD_RECYCLING_DISABLE           = -1
DPLMC_LORD_RECYCLING_ENABLE            =  0
DPLMC_LORD_RECYCLING_FREQUENT          =  1

#For $g_dplmc_ai_changes
DPLMC_AI_CHANGES_DISABLE        =  -1
DPLMC_AI_CHANGES_LOW            =   0
DPLMC_AI_CHANGES_MEDIUM         =   1
DPLMC_AI_CHANGES_HIGH           =   2
# Low:
#  - Center points for fief allocation are calculated (villages 1 / castles 2 / towns 3)
#    instead of (villages 1 / castles 1 / towns 2).
#  - For qst_rescue_prisoner and qst_offer_gift, the relatives that can be a target of the
#    quest have been extended to include uncles and aunts and in-laws.
#  - Alterations to script_calculate_troop_score_for_center (these changes currently are
#    only relevant during claimant quests).
#  - When picking a new faction, lords are more likely to return to their original faction
#    (except when that's the faction they're being exiled from), if the ordinary conditions
#    for rejoining are met.  A lord's decision may also be influenced by his relations with
#    other lords in the various factions, instead of just his relations with the faction
#    leaders.
# Medium:
#  - Some changes for lord relation gains/losses when fiefs are allocated.
#  - Kings overrule lords slightly less frequently on faction issues.
#  - In deciding who to support for a fief, minor parameter changes for certain personalities.
#    Some lords will still give priority to fiefless lords or to the lord who conquered the
#    center if they have a slightly negative relation (normally the cutoff is 0 for all
#    personalities).
#  - When a lord can't find any good candidates for a fief under the normal rules,
#    instead of automatically supporting himself he uses a weighted scoring scheme.
#  - In various places where "average renown * 3/2" appears, an alternate calculation is
#    sometimes used.
#  - Additional upgrades & hiring mercenaries in script_troop_does_business_in_center
#  - Pretenders random change relation with lords every 2 weeks when they move hosts
# High:
#  - The "renown factor" when an NPC lord or the player courts and NPC lady is adjusted by
#    the prestige of the lady's guardian.
#  - When a faction has fiefless lords and no free fiefs left, under some circumstances
#    the king will redistribute a village he owns.
#For $g_dplmc_gold_changes
DPLMC_GOLD_CHANGES_DISABLE = -1
DPLMC_GOLD_CHANGES_LOW     =  0
DPLMC_GOLD_CHANGES_MEDIUM  =  1
DPLMC_GOLD_CHANGES_HIGH    =  2
#Low:
# - Faction policy affects budget report (yours as ruler & centralization as vassal)
#   TODO: actually distribute vassal taxes to liege (whether player/npc)
# - Caravan trade benefits both the source and the destination
# - When the player surrenders, there is a chance his personal equipment
#   will not be looted, based on who accepted the surrender and the difficulty
#   setting.  (This is meant to address a gameplay issue.  In the first 700
#   days or so, there is no possible benefit to surrendering rather than
#   fighting to the last man.)  Also, a bug that made it possible for
#   books etc. to be looted was corrected.
# - AI caravans take into consideration distance when choosing their next
#   destination and will be slightly more like to visit their own faction.
#   This strategy is mixed with the Native one, so the trade pattern will
#   differ but not wildly.
# - Scale town merchant gold by prosperity (up to a maximum 40% change).
# - Food prices increase in towns that have been under siege for at least
#   48 hours.
# - In towns the trade penalty script has been tweaked to make it more
#   efficient to sell goods to merchants specializing in them.
# - Food has a chance of not spoiling depending on inventory management.
# - Villages being raided now delays construction projects.
# - Players can be ransomed by spouse or affiliated lord after being captured
#
#Medium:
# - Food consumption increases in towns as prosperity increases.
#   Consumption also increases with garrison sizes.
# - Lords' looting skill affects how much gold they take from the player
#   when they defeat him.
# - Lords' leadership skill modifies their troop wage costs the same way
#   it does for the player.
# - The player can lose gold when his fiefs are looted, like lords.
# - The same way that lord party sizes increase as the player progresses,
#   mercenary party sizes also increase to maintain their relevance.
#   (The rate is the same as for lords: a 1.25% increase per level.)
# - If the player has a kingdom of his own, his spouse will receive
#   part of the bonus that ordinarily would be due a liege.  The extent
#   of this bonus depends on the number of fiefs the players holds.
#   This bonus is non-cumulative with the marshall bonus.
# - Attrition is inflicted on NPC-owned centers if they can't pay wages,
#   but only above a certain threshold.
# - Strangers cannot acquire enterprises (enforced at 1 instead of at 0,
#   so you have to do something).
# - Village prosperity has an impact on bandit infestation (chance of death spiral).
# - Village elder now receives the gold when you buy cattle
# - Resting at neutral centers cost extra for wounded troops
# - Tournament wins are modified and applied to NPC
#
#High:
# - The total amount of weekly bonus gold awarded to kings in Calradia
#   remains constant: as kings go into exile, their bonuses are divided
#   among the remaining kings.
# - If lord's run a personal gold surplus after party wages, the extra is
#   divided among the lord and his garrisons budgets (each castle and town
#   has its own pool of funds to pay for soldiers) on the basis of whether
#   the lord is low on gold or any of his fortresses are.  (If none are low
#   on gold, the lord takes everything, like before.)
# - The honor loss from an offense depends in part on the player's honor
#   at the time.  The purer the reputation, the greater the effect of a single
#   disagrace.
# - Raiding change: village gold lost is removed from uncollected taxes before
#   the balance (if any) is removed from the lord.
# - Trading parties will drop off prisoners at walled centers.
# - Cash for prisoners slowly sold off in town garrison
# - allows cancelling improvements (cash goes back to local economy)

#For relatives: a standard way of generating IDs for "relatives" that are not
#implemented in the game as troops, but nevertheless should be taken into
#account for the purpose of script_troop_get_family_relation_to_troop
DPLMC_VIRTUAL_RELATIVE_MULTIPLIER = -4
DPLMC_VIRTUAL_RELATIVE_FATHER_OFFSET = -1#e.g. father for x = (DPLMC_VIRTUAL_RELATIVE_MULTIPLIER * x) + DPLMC_VIRTUAL_RELATIVE_FATHER_OFFSET
DPLMC_VIRTUAL_RELATIVE_MOTHER_OFFSET = -2
DPLMC_VIRTUAL_RELATIVE_SPOUSE_OFFSET = -3

#For cultural terms, with "script_dplmc_store_cultural_word_reg0" :
DPLMC_CULTURAL_TERM_WEAPON = 1#sword
DPLMC_CULTURAL_TERM_WEAPON_PLURAL = 2#"swords"
DPLMC_CULTURAL_TERM_USE_MY_WEAPON = 3#"swing my sword", etc.
DPLMC_CULTURAL_TERM_KING = 4#"king"
DPLMC_CULTURAL_TERM_KING_FEMALE = 5#"queen"
DPLMC_CULTURAL_TERM_KING_PLURAL = 6#"kings"
DPLMC_CULTURAL_TERM_LORD = 7#"lord"
DPLMC_CULTURAL_TERM_LORD_PLURAL = 8#"lords"
DPLMC_CULTURAL_TERM_SWINEHERD = 9
DPLMC_CULTURAL_TERM_TAVERNWINE = 10#"wine" (used in tavern talk)

## Possible return values from "script_dplmc_get_troop_standing_in_faction"
DPLMC_FACTION_STANDING_LEADER = 60
DPLMC_FACTION_STANDING_LEADER_SPOUSE = 50
DPLMC_FACTION_STANDING_MARSHALL = 40
DPLMC_FACTION_STANDING_LORD = 30
DPLMC_FACTION_STANDING_DEPENDENT = 20
DPLMC_FACTION_STANDING_MEMBER = 10#includes mercenaries
DPLMC_FACTION_STANDING_PETITIONER = 5
DPLMC_FACTION_STANDING_UNAFFILIATED = 0

#SB : bunch of constants

#ranges
bandit_party_templates_begin = "pt_steppe_bandits"
bandit_party_templates_end   = "pt_deserters"

fighters_begin = "trp_novice_fighter"
fighters_end = "trp_cattle"

#threshold for lord upgrades
#slot_troop_wealth must exceed the calculated amount for action in script_troop_does_business_in_center
dplmc_improvement_limit = 10000
dplmc_equipment_limit = 3000
dplmc_command_renown_limit = 300

dplmc_ransom_commission = 500
dplmc_ransom_debt_mask = 100000

dplmc_companion_skill_renown = 3
dplmc_companion_emissary_renown = 2
dplmc_companion_battle_renown = 1

#the following used in mnu_party_size_report, script_game_get_party_companion_limit, script_party_get_ideal_size
dplmc_castle_party_bonus  = 20
dplmc_marshal_party_bonus = 20
dplmc_monarch_party_bonus = 100

#increase/decrease in relation, renown, etc
message_positive = 0x33FF33
message_neutral  = 0xFFFF33
message_negative = 0xFF3333
#notifying defeat of player kingdom messengers, caravans etc
message_defeated = 0xFF0000
#other messages of note
message_alert = 0xF0DD33
message_locked = 0xFFAAAA

#camera mode constants, see module_strings or info-pages
camera_keyboard = 1
camera_mouse = 2
camera_follow = 3

rename_kingdom = 1
rename_center = 2
rename_party = 3
# rename_troop = 4
# rename_troop_plural = 5
rename_companion = 4

#recolor modes
recolor_kingdom = 0
recolor_heraldic = 1
recolor_groups = 2

#disguise mods, roughly correspond to bg archetypes or common troops
# slot_troop_player_disguise_choice = slot_troop_met
slot_troop_player_disguise_sets = slot_troop_met_previously
num_disguises = 6

disguise_none = 0
disguise_pilgrim = 1 #default vile beggar
disguise_farmer = 2 #trp_farmer
disguise_hunter = 4 #trp_forest_bandit
disguise_guard = 8 #trp_caravan_guard
disguise_merchant = 16 #trp_caravan_master
disguise_bard = 32

## VERSION NUMBERS FOR TRACKING NEEDED CHANGES
#(These change numbers are only for things which require the game to alter saved games.)
#Version 0: Diplomacy 3.3.2 and prior, and all Diplomacy 3.3.2+ versions released before 2011-06-06
#Version 1: The 2011-06-06 release of Diplomacy 3.3.2+
#Version 110611: The 2011-06-11 release of Diplomacy 3.3.2+.
#Version 110612
#Version 110615: Correct "half-siblings"
#Version 111001: Diplomacy 4.0 for Warband 1.143 (targeted for release on 2011-10-01),
#    Makes slot_faction_leader and slot_faction_marshall default to -1 instead of 0
#       (so if the player is the leader of a faction we do not have to check whether
#       he is actually a member of that faction).  fac_player_faction and
#       fac_player_supporters_faction are exempt from this.
#    Sets slot_troop_home for town merchants, elders, etc. and startup merchants

DPLMC_CURRENT_VERSION_CODE = 190101
DPLMC_VERSION_LOW_7_BITS = 68 #Number that comes after the rest of the version code

DPLMC_DIPLOMACY_VERSION_STRING = "4.3+ for Steam"
DPLMC_NUM_PREFERENCE_OPTIONS = 12 #for prsnt_adv_diplomacy_preferences

# #Perform a check to make sure constants are defined in a reasonable way.
# def _validate_constants(verbose=False):
    # """Makes sure begin/end pairs have length of at least zero."""
    # d = globals()
    # for from_key in d:
        # if not from_key.endswith("_begin"):
            # continue
        # to_key = from_key[:-len("_begin")]+"_end"
        # if not to_key in d:
            # if verbose:
                # print "%s has no matching %s" % (from_key, to_key)
            # continue
        # from_value = d[from_key]
        # to_value = d[to_key]
        # if not type(from_value) in (int, float, long):
            # continue
        # if not from_value <= to_value:
            # raise Exception("ERROR, condition %s <= %s failed [not true that %s <= %s]" % (from_key, to_key, str(from_value), str(to_value)))
        # elif verbose:
            # print "%s <= %s [%s <= %s]" % (from_key, to_key, str(from_value), str(to_value))

# #Automatically run this on module import, so errors are detected
# #during building.
# _validate_constants(verbose=(__name__=="__main__"))
# ##diplomacy end+

morale_items_begin = "itm_flag_pole_1"
morale_items_end = "itm_dplmc_coat_of_plates_red_constable"

militia_begin = "trp_follower_woman"
militia_end =  "trp_kidnapped_girl"

#jumne_begin = "trp_jumne_levy"
#jumne_end =  "trp_looter"

# Formations AI v5 by Motomataru
# rel. 02/12/2016

#Team Data
slot_team_faction                       = 1
slot_team_starting_x                    = 2
slot_team_starting_y                    = 3
slot_team_reinforcement_stage           = 4

#Reset with every call of Store_Battlegroup_Data
slot_team_size                          = 5
slot_team_adj_size                      = 6 #cavalry double counted for AI considerations
slot_team_num_infantry                  = 7	#class counts
slot_team_num_archers                   = 8
slot_team_num_cavalry                   = 9
slot_team_level                         = 10
slot_team_avg_zrot                      = 11
slot_team_avg_x                         = 12
slot_team_avg_y                         = 13

#Battlegroup slots (1 for each of 9 divisions). A "battlegroup" is uniquely defined by team and division
slot_team_d0_size                       = 14
slot_team_d0_percent_ranged             = 23
slot_team_d0_percent_throwers           = 32
slot_team_d0_low_ammo                   = 41
slot_team_d0_level                      = 50
slot_team_d0_armor                      = 59
slot_team_d0_weapon_length              = 68
slot_team_d0_swung_weapon_length        = 77
slot_team_d0_front_weapon_length        = 86
slot_team_d0_front_agents               = 95	#for calculating slot_team_d0_front_weapon_length
slot_team_d0_is_fighting                = 104
slot_team_d0_enemy_supporting_melee     = 113
slot_team_d0_closest_enemy              = 122
slot_team_d0_closest_enemy_dist         = 131	#for calculating slot_team_d0_closest_enemy
slot_team_d0_closest_enemy_special      = 140	#tracks non-cavalry for AI infantry division, infantry for AI archer division
slot_team_d0_closest_enemy_special_dist = 149	#for calculating slot_team_d0_closest_enemy_special
slot_team_d0_avg_x                      = 158
slot_team_d0_avg_y                      = 167
slot_team_d0_avg_zrot                   = 176
#End Reset Group

slot_team_d0_type                       = 185
sdt_infantry   = 0
sdt_archer     = 1
sdt_cavalry    = 2
sdt_polearm    = 3
sdt_skirmisher = 4
sdt_harcher    = 5
sdt_support    = 6
sdt_bodyguard  = 7
sdt_unknown    = -1

slot_team_d0_formation                  = 194
formation_none      = 0
formation_default   = 1
formation_ranks     = 2
formation_shield    = 3
formation_wedge     = 4
formation_square    = 5

#Native formation modes
#Constants actually correspond to number of "Stand Closer" commands required by WB to create formation
#Extended to 5 line for WFaS
formation_1_row    = 0
formation_2_row    = -1
formation_3_row    = -2
formation_4_row    = -3
formation_5_row    = -4

slot_team_d0_formation_space            = 203	#number of extra 50cm spaces currently in use
slot_team_d0_move_order                 = 212	#now used only for player divisions
slot_team_d0_fclock                     = 221	#now used only for player divisions
slot_team_d0_first_member               = 230	#-1 if division not in formation
slot_team_d0_prev_first_member          = 239
slot_team_d0_speed_limit                = 248
slot_team_d0_percent_in_place           = 257
slot_team_d0_destination_x              = 266
slot_team_d0_destination_y              = 275
slot_team_d0_destination_zrot           = 284
slot_team_d0_target_team                = 293	#targeted battlegroup (team ID)
slot_team_d0_target_division            = 302	#targeted battlegroup (division ID)
slot_team_d0_formation_num_ranks        = 311
slot_team_d0_exists                     = 320
#NEXT                                   = 329
#Battlegroup slots end

reset_team_stats_begin = slot_team_size  
reset_team_stats_end   = slot_team_d0_type

minimum_ranged_ammo = 3	#below this not considered ranged type troop

#Formation tweaks
formation_minimum_spacing	= 57	#historical shieldwall was spaced about 47cm, the width of a man's shoulders. Here we loosen for ease of troop movement.
formation_minimum_spacing_horse_length	= 300
formation_minimum_spacing_horse_width	= 200
formation_start_spread_out	= 2	#extra 50cm spacings for ease of movement for new formations
formation_min_foot_troops	= 12	#minimum to make foot formation
formation_min_cavalry_troops	= 5	#minimum to make cavalry wedge
formation_native_ai_use_formation = 1
formation_delay_for_spawn	= .4	#used for M&B 1.011 implementation
formation_reequip	= 1	#allow troops in formations to switch weapons
formation_reform_interval	= 2 #seconds
formation_rethink_for_formations_only	= 0
AI_charge_distance	= 2200

#Other constants (not tweaks)
Third_Max_Weapon_Length = 220 / 3
Km_Per_Hour_To_Cm = formation_reform_interval * 100000 / 3600
Reform_Trigger_Modulus = formation_reform_interval * 2	#trigger is half-second
Top_Speed	= 13
Far_Away	= 1000000

#positions used through formations and AI triggers
Current_Pos     = 34	#pos34
Speed_Pos       = 36	#pos36
Target_Pos      = 37	#pos37
Enemy_Team_Pos  = 38	#pos38
Temp_Pos        = 39	#pos39

#keys used for old M&B
from header_triggers import *
key_for_ranks       = key_j
key_for_shieldwall  = key_k
key_for_wedge       = key_l
key_for_square      = key_semicolon
key_for_undo        = key_u

#Hold Over There Command Tracking
HOT_no_order           = 0
HOT_F1_pressed         = 1
HOT_F1_held            = 2

#Team Slots SEE SECTION

scratch_team = 7	#Should be used just for above slots. If you use it, check for conflicts.

WB_Implementation   = 0
WFaS_Implementation = 1
Native_Formations_Implementation = WB_Implementation

slot_item_alternate            = 46	#table between swing/noswing versions of same weapon

#Battle Phases
BP_Ready  = 0
BP_Init   = 1
BP_Deploy = 2
BP_Setup  = 3
BP_Jockey = 4
BP_Duel   = 5
BP_Fight  = 6

#Presentations Constants Moto chief
Screen_Border_Width = 24
Screen_Width = 1024-Screen_Border_Width
Screen_Height = 768-Screen_Border_Width
Screen_Text_Height = 35
Screen_Checkbox_Height_Adj = 4
Screen_Numberbox_Width = 64
Screen_Title_Height = Screen_Height-Screen_Border_Width-Screen_Text_Height
Screen_Check_Box_Dimension = 20
Screen_Undistort_Width_Num = 7  #distortion midway between 1024x768 and 1366x768 -- things will appear a little narrow on thin screens and vice versa
Screen_Undistort_Width_Den = 8

#Bit switches for global $first_time for keeping track of what has been done at least once in a given game
# first_time_death_camera    = 0x001
# first_time_strategy_camera = 0x002
# first_time_game_rules      = 0x004
# first_time_available       = 0x008
# first_time_available       = 0x010
# first_time_available       = 0x020
# first_time_available       = 0x040
# first_time_load_main_party = 0x080  #this used in reverse
# first_time_cam_battle      = 0x100
first_time_hold_F1         = 0x200
first_time_formations      = 0x400

Outfit_Thorax_Length = 60  #length dark ages human thorax
Outfit_Fast_Weapon_Speed = 100

mission_tpl_are_all_agents_spawned     = 1943   # (mission_tpl_are_all_agents_spawned), #agents >300 may keep spawning after ti_after_mission_start (still fires .1 second too early)

# Formations AI v5 by Motomataru
# rel. 02/12/2016

#AI variables
AI_long_range	= 13000	#do not put over 130m if you want archers to always fire
AI_firing_distance	= AI_long_range / 2
AI_for_kingdoms_only	= 0
Percentage_Cav_For_New_Dest	= 40
Hold_Point	= 100	#archer hold if outnumbered
Advance_More_Point	= 100 - Hold_Point * 100 / (Hold_Point + 100)	#advance 'cause expect other side is holding
AI_Max_Reinforcements	= 2	#maximum number of reinforcement stages in a battle
AI_Replace_Dead_Player	= 1
AI_Poor_Troop_Level	= 15	#average level of troops under which a division may lose discipline

#positions used in a script, named for convenience
Nearest_Enemy_Troop_Pos	= 48	#pos48	used only by infantry AI
Nearest_Enemy_Battlegroup_Pos	= 50	#pos50	used only by ranged AI
Nearest_Threat_Pos	= Nearest_Enemy_Troop_Pos	#used only by cavalry AI
Nearest_Target_Pos	= Nearest_Enemy_Battlegroup_Pos	#used only by cavalry AI
Infantry_Pos	= 51	#pos51
Archers_Pos	= 53	#pos53
Cavalry_Pos	= 54	#pos54
Team_Starting_Point	= 55	#pos55

#positions used through battle
Team0_Cavalry_Destination	= 56	#pos56
Team1_Cavalry_Destination	= 57	#pos57
Team2_Cavalry_Destination	= 58	#pos58
Team3_Cavalry_Destination	= 59	#pos59

#+FREELANCER start
freelancer_version = 15
#Floris or no Diplomacy:
freelancer_can_use_item  = "script_dplmc_troop_can_use_item" 
#with Diplomacy: 
#freelancer_can_use_item = "script_dplmc_troop_can_use_item"

#Party Slots #only used for freelancer_party_backup
slot_freelancer_equip_start = 100 #only used for freelancer_party_backup
slot_freelancer_version     = slot_freelancer_equip_start - 2 #only used for freelancer_party_backup

#Quest Slots
#Only for Freelancer_Enlisted
slot_quest_freelancer_start_xp       = slot_quest_object_state 
slot_quest_freelancer_start_date     = slot_quest_target_state
slot_quest_freelancer_banner_backup  = slot_quest_object_faction
slot_quest_freelancer_next_payday    = slot_quest_target_item
slot_quest_freelancer_upgrade_xp     = slot_quest_target_dna 
slot_quest_freelancer_orig_morale    = slot_quest_giver_center

#Non-Slot Constants for Quests
freelancer_quests_begin = "qst_freelancer_enlisted"
freelancer_quests_end   = "qst_freelancer_end"
plyr_mission_vacation = 1
plyr_mission_captured = 2


#Slots -- deprecated; for the savegame transition
# slot_party_orig_morale           = slot_party_ai_rationale
slot_troop_freelancer_start_xp   = slot_troop_signup   #110 -only used for player
slot_troop_freelancer_start_date = slot_troop_signup_2 #111 -only used for player
#+Freelancer end

skirmish_min_distance = 1500 #Min distance you wish maintained, in cm. Where agent will retreat
skirmish_max_distance = 2500 #Max distance to maintain, in cm. Where agent will stop retreating

##main party slot
slot_party_skirmish_d0 = slot_town_arena_melee_mission_tpl
slot_party_skirmish_d1 = slot_town_arena_torny_mission_tpl
slot_party_skirmish_d2 = slot_town_arena_melee_1_num_teams
slot_party_skirmish_d3 = slot_town_arena_melee_1_team_size
slot_party_skirmish_d4 = slot_town_arena_melee_2_num_teams
slot_party_skirmish_d5 = slot_town_arena_melee_2_team_size
slot_party_skirmish_d6 = slot_town_arena_melee_3_num_teams
slot_party_skirmish_d7 = slot_town_arena_melee_3_team_size
slot_party_skirmish_d8 = slot_town_arena_melee_cur_tier

key_for_skirmish   = key_f8

slot_team_d0_order_volley     = 10 #plus 8 more for the other divisions

key_for_volley   = key_f9

#Morale
battle_ratio_multiple = 7000
max_morale = 35000
max_ratio = max_morale/2
initial_morale = 10000


camels_begin = "itm_camel"
camels_end = "itm_camel"

color_great_news = 0xCCFFCC
color_good_news = 0xCCFFCC
color_terrible_news = 0xFFCCCC  #0xFF2222
color_bad_news = 0xFFCCCC
color_neutral_news = 0xFFFFFF
color_quest_and_faction_news = 0xCCCCFF
color_hero_news = 0xFFFF99

#Start as king/lord
cb_king = 8
cb_vassal = 9


#### shaders
shader_float_default = 15
shader_float_day = 50
#### shaders

#banner background colors!
banner_background_white = 0xFFe9e3db
banner_background_blue = 0xFF1176d4
banner_background_red = 0xFFbb2323
banner_background_green = 0xFF2d7b34
banner_background_yellow = 0xFFceb036
banner_background_orange = 0xFFae5b14
banner_background_dblue = 0xFF024f97
banner_background_lgreen = 0xFF818978
banner_background_dgreen = 0xFF2c5021
banner_background_dred = 0xFF5d1b18
banner_background_black = 0x1c1c1c

banner_bg_default = 0xFFC0B090

slot_religion_chalcedonian = 1
slot_religion_paganism = 2
slot_religion_arianism = 3
slot_religion_zoroastrianism = 4
slot_religion_coptic = 5
slot_religion_roman_paganism = 6


minor_towns_begin = "p_aestii_village"
minor_towns_end   = "p_religious_site_1"

Troop_Tree_Area_Height = Screen_Title_Height-4*Screen_Text_Height
Troop_Tree_Area_Width = Screen_Width-2*Screen_Border_Width
Troop_Tree_Line_Color = 0x001380
Troop_Tree_Tableau_Height = 800
Troop_Tree_Tableau_Width = Troop_Tree_Tableau_Height*Screen_Undistort_Width_Num/Screen_Undistort_Width_Den

#shader
shader_snow_line	= 230
shader_spring		= 0
shader_summer		= 1
shader_autumn		= 2
shader_winter		= 3


###########################################################################################################################
#####                                            PRESENTATION DEFINITIONS                                             #####
###########################################################################################################################
# mcc_objects                            = "trp_tpe_presobj"
# mcc_data                               = "trp_tpe_xp_table"

# Slots of mcc_OBJECTS
mcc_obj_button_done                    = 1
mcc_obj_button_default                 = 2
mcc_obj_button_random                  = 3
mcc_obj_label_menus                    = 4
mcc_obj_label_story                    = 5
mcc_obj_label_gender                   = 6
mcc_obj_label_father                   = 7
mcc_obj_label_earlylife                = 8
mcc_obj_label_later                    = 9
mcc_obj_label_reason                   = 10
mcc_obj_menu_gender                    = 11
mcc_obj_menu_father                    = 12
mcc_obj_menu_earlylife                 = 13
mcc_obj_menu_later                     = 14
mcc_obj_menu_reason                    = 15
mcc_obj_label_options                  = 16
# mcc_obj_menu_trooptrees                = 17
# mcc_val_menu_trooptrees                = 18
# mcc_obj_checkbox_fogofwar              = 19
# mcc_val_checkbox_fogofwar              = 20
# mcc_obj_label_mtt                      = 21
# mcc_obj_checkbox_gather_npcs           = 22
# mcc_val_checkbox_gather_npcs           = 23
mcc_obj_menu_initial_region            = 24
mcc_val_menu_initial_region            = 25
mcc_obj_label_region                   = 26
mcc_obj_label_strength                 = 27
mcc_obj_stat_strength                  = 28
mcc_obj_label_agility                  = 29
mcc_obj_stat_agility                   = 30
mcc_obj_label_intelligence             = 31
mcc_obj_stat_intelligence              = 32
mcc_obj_label_charisma                 = 33
mcc_obj_stat_charisma                  = 34
mcc_obj_stat_gold                      = 35
mcc_obj_stat_renown                    = 36
mcc_obj_stat_weapon_onehand            = 37
mcc_obj_stat_weapon_twohand            = 38
mcc_obj_stat_weapon_polearm            = 39
mcc_obj_stat_weapon_archery            = 40
mcc_obj_stat_weapon_crossbow           = 41
mcc_obj_stat_weapon_throwing           = 42
mcc_obj_stat_container                 = 43
mcc_obj_button_back                    = 44

# Slots of mcc_DATA
# Slots 0-99 reserved.
mcc_item_storage_begin                 = 100
# Slots 101-120 reserved.
mcc_item_storage_end                   = 121

#######################################
##WE DIVIDE WORLDMAP INTO REGIONS
##REGIONS:
region_spain                            = 1
region_north_africa                     = 2
region_southitaly                       = 3
region_nile                             = 4
region_syria_palestine                  = 5
region_anatolia_central                 = 6
region_anatolia_coastal                 = 7
region_mesopotamia                      = 8
region_persianhill_green                = 9
region_persianhill_desert               =10
region_caucasus                         =11
region_greece                           =12
region_nile_delta                       =13
region_mountain_europe_alps             =14
region_mountain_europe_spain_france     =15
region_mountain_europe_romania          =16
region_mountain_europe_bohemia          =17
###END REGIONS
#######################################