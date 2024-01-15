from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

from compiler import *
####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
  ("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,0,4),(trp_watchman,1,5)]),

  ("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),
# Ryan BEGIN
  ("looters","Looters",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_looter,3,75)]),
# Ryan END
  ("manhunters","Manhunters",icon_axeman,0,fac_manhunters,soldier_personality,[(trp_manhunter,9,40)]),
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

#SB : changes to icons
#  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_black_khergit_guard,1,10),(trp_black_khergit_horseman,5,5)]),
  ("steppe_bandits","Iazyges Band",icon_khergit_horseman_b|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_steppe_bandit,4,30),(trp_steppe_rider,1,10),(trp_steppe_cataphract,0,5)]),
  ("taiga_bandits","Germanic Bandits",icon_sea_raider|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_taiga_bandit,8,30)]),
  ("desert_bandits","Austuriani Rebels",icon_khergit|carries_goods(2)|pf_show_faction,0,fac_berber_rebels,bandit_personality,[(trp_desert_bandit,6,30)]),
  ("forest_bandits","Bagaudae Band",icon_archer_1|carries_goods(2),0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit_recruit,4,10),(trp_forest_bandit,4,25),(trp_bagaudae_footman,2,15)]),
  ("mountain_bandits","Isaurian Bandits",icon_axeman|carries_goods(2),0,fac_mountain_bandits,bandit_personality,[(trp_mountain_bandit,4,30),(trp_isaurian_warrior,1,10)]),
  ("sea_raiders","Saxon Raiders",icon_sea_raider|carries_goods(2),0,fac_saxons,bandit_personality,[(trp_sea_raider,5,20)]),
  ("saxon_raiders","Saxon Warband",icon_sea_raider|carries_goods(2),0,fac_saxons,bandit_personality,[(trp_sea_raider,15,40)]),
  ("sabir_bandits","Sabir Bandits",icon_khergit_horseman_b|carries_goods(3),0,fac_outlaws,bandit_personality,[(trp_sabir_bandit,4,20)]),
  ("armenian_rebels","Armenian Rebels",icon_axeman|carries_goods(2),0,fac_armenian_rebels,bandit_personality,[(trp_armenian_bandit,5,15),(trp_armenian_rebel,3,10),(trp_armenian_brigand,3,10)]),
  ("coptic_rebels","Coptic Rebels",icon_axeman|carries_goods(2)|pf_show_faction,0,fac_coptic_rebels,bandit_personality,[(trp_coptic_youth,4,25),(trp_coptic_footman,4,15),(trp_coptic_watchman,2,10),(trp_coptic_guard,2,8)]),
  ("arab_bandits","Saraceni",icon_khergit|carries_goods(2)|pf_show_faction,0,fac_outlaws,bandit_personality,[(trp_arab_bandit,6,30)]),
  ("bandits","Bandits",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_robber,5,35),(trp_bandit,2,15),(trp_brigand,1,5)]),
  ("deserters","Deserters",icon_flagbearer_b|carries_goods(3),0,fac_deserters,bandit_personality,[]),

  ("samaritan_rebels","Samaritan Rebels",icon_axeman|carries_goods(2),0,fac_samaritan_rebels,bandit_personality,[(trp_samaritan_zealot,5,20),(trp_samaritan_rebel,3,10)]), #will be used later
  ("bagaudae","Bagaudae Army",icon_germanic_army|carries_goods(2),0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit_recruit,30,75),(trp_forest_bandit,20,100),(trp_bagaudae_footman,15,55)]),
  ("pirates","Piratae",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_pirate,9,60)]),
  ("bagaudae_army_event","Bagaudae Army",icon_germanic_army|carries_goods(5),0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit_recruit,50,155),(trp_forest_bandit,45,125),(trp_bagaudae_footman,35,80)]),
  ("gallaecian_rebels","Gallaecian Rebels",icon_peasant|carries_goods(8),0,fac_minor_gallaeci,soldier_personality,[(trp_hibero_roman_venator,20,40),(trp_hibero_roman_rusticus,15,25),(trp_hibero_roman_defensor,10,20)]),
  ("foederati_rebels","Foederati Rebels",icon_khergit_horseman_b|carries_goods(2),0,fac_deserters,bandit_personality,[(trp_miles_foederatus_germani,20,40),(trp_miles_foederatus_gothorum,20,30),(trp_eques_symmachi_hunnorum,10,20)]), #mix of huns, foederati troops - some time before majorians major campaigns, unruly federates + huns ravaged the countryside
  ("alpine_bandits","Latrones Alpinorum",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_latro_alpium,5,30),(trp_brigand,0,3)]),

  #SB : fix icon
  ("merchant_caravan","Merchant Caravan",icon_mule|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
  ("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,14,55)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,208),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

  ("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,5,10),(trp_peasant_woman,3,8),(trp_watchman,1,10)]),

  ("spy_partners", "Unremarkable Travellers", icon_player_horseman|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
  ("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Townsman", icon_player_horseman|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),

  ("forager_party","Foraging Party",icon_flagbearer_b|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("scout_party","Scouts",icon_flagbearer_b|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("patrol_party","Patrol",icon_flagbearer_b|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
  #SB : icon change to make it stand out more
  ("messenger_party","Messenger",icon_flagbearer_b|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("raider_party","Raiders",icon_flagbearer_b|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,12,40)]),
  ("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",icon_vaegir_knight,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

  ("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),

  #quest related parties
  ("raiders","Raiders",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_robber,10,35),(trp_bandit,5,15),(trp_brigand,5,9),(trp_bandit_leader,1,1)]),

  ("quest_irish_raiders","Irish Raiders",icon_sea_raider|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[]),
  ("quest_pictish_raiders","Pictish Raiders",icon_sea_raider|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[]),
  ("quest_saxon_raiders","Saxon Raiders",icon_sea_raider|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[]),

  ("isaurian_quest_army","Isaurian Band",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_isaurian_leader,1,1),(trp_mountain_bandit,15,40),(trp_isaurian_warrior,10,30)]),
  ("onogur_quest_army","Hunnic Band",icon_khergit_horseman_b|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_onogur_leader,1,1),(trp_hunnic_horse_archer,15,30),(trp_hunnic_retainer,10,15),(trp_bulgar_horseman,5,10),(trp_bigilas_son,1,1,pmf_is_prisoner)]),
  ("attilas_bastard_son_rescued","Oebarsius",icon_khergit_horseman_b|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_attilas_bastard_son,1,1)]),
  ("quest_bagaudae","Bagauda",icon_germanic_army|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit,30,40),(trp_forest_bandit_recruit,15,20),(trp_bagaudae_footman,15,25)]), #less than normal
  ("hunimund_horde_quest","Hunimund's Army",icon_germanic_army|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_suebi_king,1,1),(trp_western_germanic_freeman,55,105),(trp_western_germanic_skirmisher,15,40),(trp_steppe_bandit,10,40),(trp_steppe_cataphract,5,15)]),
  ("juliobriga_bagadua","Bagaudae Band",icon_archer_1|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit_recruit,25,35),(trp_forest_bandit,12,21),(trp_bagaudae_footman,5,10)]),
  ("quest_vandal_raiders","Vandal Raiders",icon_sea_raider|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_vandal_raider_leader,1,1),(trp_eastern_germanic_spearman,30,45),(trp_eastern_germanic_mounted_warrior,3,8),(trp_western_alan_lancer,2,5),(trp_gaetuli_horseman,5,15),]),
  ("faltras_suebi_band","Faltras's Loyalists",icon_germanic_army|carries_goods(9)|pf_auto_remove_in_town,0,fac_faltras_suebi,soldier_personality,[]),
  ("faltras_suebi_army","Faltras's Loyalists",icon_germanic_army|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,soldier_personality,[]),
  ("germanic_raiders","Scamarae",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_western_germanic_freeman,30,50),(trp_taiga_bandit,8,15),(trp_western_germanic_bowman,5,10)]),
  ("noricum_soldiers","Norici Militia",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,soldier_personality,[(trp_miles_romani,15,20),]),
  ("aestii_rebel_party","Aestii Rebels",icon_axeman|carries_goods(50)|pf_quest_party|pf_always_visible,0,fac_neutral,soldier_personality,[(trp_aestii_rebel_king,1,1),(trp_aestii_skirmisher,30,40),(trp_aestii_tribesman,30,40),(trp_sitones_retainer,20,30),(trp_aestii_companion,10,20)]),
  ("heretical_codex_bandits","Bandits",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_burgundian_looter,1,1),(trp_robber,5,35),(trp_bandit,2,15),(trp_brigand,1,5)]),

  #party size of about 200 each
  ("danubian_suebi_army","Hunimund's Host",icon_germanic_army|carries_goods(20)|pf_show_faction,0,fac_hunimund_suebi,soldier_personality,[(trp_quadi_spearman,70,100),(trp_western_germanic_bowman,30,50),(trp_steppe_bandit,10,20),(trp_steppe_rider,10,30),(trp_steppe_cataphract,10,20),(trp_suebi_king,1,1)]), #spearmen, bowmen, iazyges
  ("heruli_army","Visilaus's Host",icon_germanic_army|carries_goods(20)|pf_show_faction,0,fac_heruli,soldier_personality,[(trp_heruli_slave,40,60),(trp_limigantes_rebel,20,50),(trp_heruli_warrior,80,100),(trp_heruli_horseman,20,40),(trp_heruli_king,1,1)]), #spearmen, horsemen, skirmishers

  #event parties
  ("nero_rebel_army","Legio Neronia",icon_roman_army|carries_goods(30)|pf_auto_remove_in_town,0,fac_peasant_rebels,bandit_personality,[(trp_nero_larper_commander,1,1),(trp_miles_romani,200,215),(trp_sagittarius,60,70),(trp_bucellarius,45,55),(trp_imperial_signifer,5,5)]),
  ("agrippinus_rebel_army","Legio Gallia",icon_roman_army|carries_goods(30)|pf_auto_remove_in_town,0,fac_peasant_rebels,bandit_personality,[(trp_agrippinus,1,1),(trp_miles_romani,200,215),(trp_sagittarius,30,50),(trp_bucellarius,45,55),(trp_miles_foederatus_gothorum,50,60)]),
  ("tuldila_rebels","Foederati Rebels",icon_khergit_horseman_b|carries_goods(30),0,fac_deserters,bandit_personality,[(trp_tuldila,1,1),(trp_miles_foederatus_gothorum,40,60),(trp_eques_symmachi_hunnorum,20,40)]),
  ("vllibos_rebels","Gothic Rebels",icon_germanic_army|carries_goods(30)|pf_auto_remove_in_town,0,fac_peasant_rebels,bandit_personality,[(trp_vllibos,1,1),(trp_miles_foederatus_gothorum,100,200)]),

# Caravans
  # ("center_reinforcements","Reinforcements",icon_axeman|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,30),(trp_watchman,4,20)]),  
  #SB : use this instead of directly adding templates
  ("center_reinforcements","Reinforcements", icon_axeman|pf_show_faction|carries_goods(4),0,fac_commoners,escorted_merchant_personality,[]),

  ("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  
# Reinforcements
  # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
  # less-modernised templates are generally includes 7-14 troops in total, 
  # med-modernised templates are generally includes 5-10 troops in total, 
  # high-modernised templates are generally includes 3-5 troops in total

#Max temp 1 : 8-20
#Max temp 2: 6-15 exclude bearer
#Max temp 3: 4-10
#Each nation gets a standard bearer at tier 2

  ("kingdom_1_reinforcements_a", "{!}Gothic Reinforcements", 0, 0, fac_commoners, 0, [(trp_gothic_skirmisher,4,10),(trp_gothic_freeman,4,10)]),
  ("kingdom_1_reinforcements_b", "{!}Gothic Reinforcements", 0, 0, fac_commoners, 0, [(trp_gothic_freeman,3,8),(trp_gothic_mounted_skirmisher,3,5),(trp_standard_bearer,1,1)]),
  ("kingdom_1_reinforcements_c", "{!}Gothic Reinforcements", 0, 0, fac_commoners, 0, [(trp_gothic_footman,1,3),(trp_gothic_horseman,3,7)]),

  ("kingdom_2_reinforcements_a", "{!}E. Germanic Reinforcements", 0, 0, fac_commoners, 0, [(trp_eastern_germanic_skirmisher,2,10),(trp_eastern_germanic_spearman,2,10)]),
  ("kingdom_2_reinforcements_b", "{!}E. Germanic Reinforcements", 0, 0, fac_commoners, 0, [(trp_eastern_germanic_spearman,3,8),(trp_eastern_germanic_mounted_skirmisher,3,5),(trp_standard_bearer,1,1)]),
  ("kingdom_2_reinforcements_c", "{!}E. Germanic Reinforcements", 0, 0, fac_commoners, 0, [(trp_eastern_germanic_retainer,1,3),(trp_eastern_germanic_mounted_warrior,3,7)]),

  ("kingdom_3_reinforcements_a", "{!}Briton Reinforcements", 0, 0, fac_commoners, 0, [(trp_briton_skirmisher,3,9),(trp_briton_footman,3,9)]),
  ("kingdom_3_reinforcements_b", "{!}Briton Reinforcements", 0, 0, fac_commoners, 0, [(trp_briton_footman,2,6),(trp_abulci,2,4),(trp_angle_mercenary,1,3),(trp_imperial_signifer,1,1)]),
  ("kingdom_3_reinforcements_c", "{!}Briton Reinforcements", 0, 0, fac_commoners, 0, [(trp_briton_infantry,2,4),(trp_briton_horseman,2,4)]),

  ("kingdom_4_reinforcements_a", "{!}N. Germanic Reinforcements", 0, 0, fac_commoners, 0, [(trp_northern_germanic_skirmisher,2,10),(trp_northern_germanic_freeman,2,10)]),
  ("kingdom_4_reinforcements_b", "{!}N. Germanic Reinforcements", 0, 0, fac_commoners, 0, [(trp_northern_germanic_freeman,6,15),(trp_standard_bearer,1,1)]),
  ("kingdom_4_reinforcements_c", "{!}N. Germanic Reinforcements", 0, 0, fac_commoners, 0, [(trp_northern_germanic_warrior,2,5),(trp_northern_germanic_horseman,2,5)]),

  ("kingdom_5_reinforcements_a", "{!}Pictish Reinforcements", 0, 0, fac_commoners, 0, [(trp_pictish_skirmisher,4,10),(trp_verturiones_horse_whisperers,2,5),(trp_pictish_warrior,2,5)]),
  ("kingdom_5_reinforcements_b", "{!}Pictish Reinforcements", 0, 0, fac_commoners, 0, [(trp_pictish_warrior,4,10),(trp_attecotti_raider,2,5),(trp_standard_bearer,1,1)]),
  ("kingdom_5_reinforcements_c", "{!}Pictish Reinforcements", 0, 0, fac_commoners, 0, [(trp_dycalidones_fanatic,2,5),(trp_pictish_companion,2,5)]),

  ("kingdom_6_reinforcements_a", "{!}Sassanid Reinforcements", 0, 0, fac_commoners, 0, [(trp_sassanid_skirmisher,3,8),(trp_sassanid_levy,5,12)]),
  ("kingdom_6_reinforcements_b", "{!}Sassanid Reinforcements", 0, 0, fac_commoners, 0, [(trp_sassanid_footman,2,6),(trp_sassanid_archer,2,4),(trp_kurdish_javelinman,1,3),(trp_kurdish_slinger,1,3),(trp_sassanid_standard_bearer,1,1)]),
  ("kingdom_6_reinforcements_c", "{!}Sassanid Reinforcements", 0, 0, fac_commoners, 0, [(trp_sassanid_armored_footman,1,3),(trp_sassanid_cavalry,1,3),(trp_daylamite_hillman,1,2),(trp_sassanid_horse_archer,1,2),(trp_sassanid_officer,1,1)]),

  ("kingdom_7_reinforcements_a", "{!}W. Germanic Reinforcements", 0, 0, fac_commoners, 0, [(trp_western_germanic_skirmisher,4,10),(trp_western_germanic_freeman,4,10)]),
  ("kingdom_7_reinforcements_b", "{!}W. Germanic Reinforcements", 0, 0, fac_commoners, 0, [(trp_western_germanic_freeman,6,15),(trp_standard_bearer,1,1)]),
  ("kingdom_7_reinforcements_c", "{!}W. Germanic Reinforcements", 0, 0, fac_commoners, 0, [(trp_western_germanic_retainer,3,8),(trp_western_germanic_companion,1,2)]),

  ("kingdom_8_reinforcements_a", "{!}Caucasian Reinforcements", 0, 0, fac_commoners, 0, [(trp_caucasian_skirmisher,4,10),(trp_caucasian_levy,4,10)]),
  ("kingdom_8_reinforcements_b", "{!}Caucasian Reinforcements", 0, 0, fac_commoners, 0, [(trp_caucasian_levy,3,10),(trp_caucasian_archer,3,5),(trp_caucasian_standard_bearer,1,1)]),
  ("kingdom_8_reinforcements_c", "{!}Caucasian Reinforcements", 0, 0, fac_commoners, 0, [(trp_caucasian_footman,1,3),(trp_caucasian_nobleman,3,7)]),

  ("kingdom_11_reinforcements_a", "{!}Mauri Reinforcements", 0, 0, fac_commoners, 0, [(trp_ferentarius_indiginae_africani,4,10),(trp_civis_armatura_mauri,4,10)]),
  ("kingdom_11_reinforcements_b", "{!}Mauri Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_limitis_mauri,2,6),(trp_sagittarius,1,4),(trp_eques_indiginae_africani,3,5),(trp_imperial_signifer,1,1)]),
  ("kingdom_11_reinforcements_c", "{!}Mauri Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_limitis_mauri,2,5),(trp_eques_romano_mauri,2,5)]),

  ("kingdom_12_reinforcements_a", "{!}Hunnic Reinforcements", 0, 0, fac_commoners, 0, [(trp_crimean_gothic_skirmisher,2,6),(trp_hunnic_horse_archer,3,8),(trp_crimean_gothic_freeman,3,6)]), #mix of huns, goths, and other AOREs
  ("kingdom_12_reinforcements_b", "{!}Hunnic Reinforcements", 0, 0, fac_commoners, 0, [(trp_hunnic_horse_archer,2,6),(trp_akatziri_tribesman,2,6),(trp_meotian_horseman,2,5),(trp_draco_bearer,1,1)]),
  ("kingdom_12_reinforcements_c", "{!}Hunnic Reinforcements", 0, 0, fac_commoners, 0, [(trp_hunnic_retainer,2,6),(trp_crimean_gothic_horseman,1,2),(trp_akatziri_retainer,1,2)]),

  ("kingdom_15_reinforcements_a", "{!}Nubian Reinforcements", 0, 0, fac_commoners, 0, [(trp_nubian_bowman,4,10),(trp_nubian_tribesman,4,10)]), 
  ("kingdom_15_reinforcements_b", "{!}Nubian Reinforcements", 0, 0, fac_commoners, 0, [(trp_nubian_tribesman,3,8),(trp_nubian_archer,3,7)]),
  ("kingdom_15_reinforcements_c", "{!}Nubian Reinforcements", 0, 0, fac_commoners, 0, [(trp_nubian_warrior,2,5),(trp_nubian_horseman,2,5)]), 

  ("kingdom_16_reinforcements_a", "{!}Alan Reinforcements", 0, 0, fac_commoners, 0, [(trp_caucasian_alan_skirmisher,3,7),(trp_caucasian_alan_tribesman,3,7),(trp_caucasian_alan_footman,2,6)]),
  ("kingdom_16_reinforcements_b", "{!}Alan Reinforcements", 0, 0, fac_commoners, 0, [(trp_caucasian_alan_footman,2,5),(trp_caucasian_alan_tribesman,3,6),(trp_barsil_horse_archer,1,4),(trp_draco_bearer,1,1)]),
  ("kingdom_16_reinforcements_c", "{!}Alan Reinforcements", 0, 0, fac_commoners, 0, [(trp_aursa_rider,1,4),(trp_caucasian_alan_retainer,3,6)]),  

  ("kingdom_empire_reinforcements_a", "{!}Roman Reinforcements", 0, 0, fac_commoners, 0, [(trp_tiro,4,10),(trp_exculator,2,4),(trp_eques_mauri,2,6)]),
  ("kingdom_empire_reinforcements_b", "{!}Roman Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes,4,10),(trp_sagittarius,3,6),(trp_eques_ala,2,7),(trp_imperial_signifer,1,1)]),
  ("kingdom_empire_reinforcements_c", "{!}Roman Reinforcements", 0, 0, fac_commoners, 0, [(trp_eques_scutarii,2,6),(trp_eques_cataphractarii,1,3),(trp_centenarius,1,1)]),

  #minor cultures - could potentially be adopted by the player?
  ("culture_minor_1_reinforcements_a", "{!}Cantabrian Reinforcements", 0, 0, fac_commoners, 0, [(trp_latro_vasconius,8,20)]),
  ("culture_minor_1_reinforcements_b", "{!}Cantabrian Reinforcements", 0, 0, fac_commoners, 0, [(trp_hibero_roman_rusticus,6,15),(trp_imperial_signifer,1,1)]),
  ("culture_minor_1_reinforcements_c", "{!}Cantabrian Reinforcements", 0, 0, fac_commoners, 0, [(trp_eques_cantabri,1,5),(trp_bagaudae_footman,2,3),(trp_hibero_roman_defensor,1,2)]),

  ("culture_minor_2_reinforcements_a", "{!}Slavic Reinforcements", 0, 0, fac_commoners, 0, [(trp_slav_skirmisher,4,10),(trp_slav_archer, 4,10)]),
  ("culture_minor_2_reinforcements_b", "{!}Slavic Reinforcements", 0, 0, fac_commoners, 0, [(trp_slav_footman,6,15),(trp_standard_bearer,1,1)]),
  ("culture_minor_2_reinforcements_c", "{!}Slavic Reinforcements", 0, 0, fac_commoners, 0, [(trp_slav_horseman,2,5),(trp_slav_horsearcher,2,5)]),

  ("culture_minor_3_reinforcements_a", "{!}Coptic Reinforcements", 0, 0, fac_commoners, 0, [(trp_coptic_youth,4,10),(trp_coptic_footman,4,10)]),
  ("culture_minor_3_reinforcements_b", "{!}Coptic Reinforcements", 0, 0, fac_commoners, 0, [(trp_coptic_footman,3,8),(trp_coptic_watchman,3,7),(trp_standard_bearer,1,1)]),
  ("culture_minor_3_reinforcements_c", "{!}Coptic Reinforcements", 0, 0, fac_commoners, 0, [(trp_coptic_guard,2,5),(trp_eques_sexto_dalmatae,2,5)]),

  ("culture_minor_4_reinforcements_a", "{!}Frisian Reinforcements", 0, 0, fac_commoners, 0, [(trp_frisian_freeman,8,20)]),
  ("culture_minor_4_reinforcements_b", "{!}Frisian Reinforcements", 0, 0, fac_commoners, 0, [(trp_frisian_freeman,6,15),(trp_standard_bearer,1,1)]),
  ("culture_minor_4_reinforcements_c", "{!}Frisian Reinforcements", 0, 0, fac_commoners, 0, [(trp_frisian_companion,4,10)]),

  ("culture_minor_5_reinforcements_a", "{!}Aestii Reinforcements", 0, 0, fac_commoners, 0, [(trp_aestii_skirmisher,8,20)]),
  ("culture_minor_5_reinforcements_b", "{!}Aestii Reinforcements", 0, 0, fac_commoners, 0, [(trp_aestii_tribesman,6,15),(trp_standard_bearer,1,1)]),
  ("culture_minor_5_reinforcements_c", "{!}Aestii Reinforcements", 0, 0, fac_commoners, 0, [(trp_aestii_companion,4,10)]),

  ("culture_minor_6_reinforcements_a", "{!}Morden Reinforcements", 0, 0, fac_commoners, 0, [(trp_mordvin_skirmisher,8,20)]),
  ("culture_minor_6_reinforcements_b", "{!}Morden Reinforcements", 0, 0, fac_commoners, 0, [(trp_mordvin_footman,3,8),(trp_mordvin_mounted_skirmisher,3,7),(trp_standard_bearer,1,1)]),
  ("culture_minor_6_reinforcements_c", "{!}Morden Reinforcements", 0, 0, fac_commoners, 0, [(trp_mordvin_companion,4,10)]),

  ("culture_minor_7_reinforcements_a", "{!}Scandzae Reinforcements", 0, 0, fac_commoners, 0, [(trp_scandinavian_freeman,8,20)]),
  ("culture_minor_7_reinforcements_b", "{!}Scandzae Reinforcements", 0, 0, fac_commoners, 0, [(trp_scandinavian_retainer,6,15),(trp_standard_bearer,1,1)]),
  ("culture_minor_7_reinforcements_c", "{!}Scandzae Reinforcements", 0, 0, fac_commoners, 0, [(trp_scandinavian_comes,4,10)]),

  ("culture_minor_8_reinforcements_a", "{!}Tetraxitae Reinforcements", 0, 0, fac_commoners, 0, [(trp_crimean_gothic_skirmisher,4,10),(trp_crimean_gothic_freeman,4,10)]), #stronger than most
  ("culture_minor_8_reinforcements_b", "{!}Tetraxitae Reinforcements", 0, 0, fac_commoners, 0, [(trp_crimean_gothic_freeman,3,8),(trp_crimean_gothic_mounted_skirmisher,2,7),(trp_standard_bearer,1,1)]),
  ("culture_minor_8_reinforcements_c", "{!}Tetraxitae Reinforcements", 0, 0, fac_commoners, 0, [(trp_crimean_gothic_warrior,2,5),(trp_crimean_gothic_horseman,2,5)]),

  ("culture_minor_9_reinforcements_a", "{!}Western Alan Reinforcements", 0, 0, fac_commoners, 0, [(trp_western_alan_rider,8,20)]),
  ("culture_minor_9_reinforcements_b", "{!}Western Alan Reinforcements", 0, 0, fac_commoners, 0, [(trp_western_alan_lancer,6,15)]),
  ("culture_minor_9_reinforcements_c", "{!}Western Alan Reinforcements", 0, 0, fac_commoners, 0, [(trp_western_alan_cataphract,4,10)]),
  #special party templates for specific lords
  #Majorian - will be stronger than most party templates
  ("kingdom_1_lord_reinforcements_a", "{!}majorian_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_miles_foederatus_gothorum,3,7),(trp_exculator,1,3),(trp_western_alan_rider,2,4),(trp_eques_mauri,1,3),(trp_eques_ala,1,3)]), #greater amount of federate troops
  ("kingdom_1_lord_reinforcements_b", "{!}majorian_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_miles_iuniorum_italicorum,4,8),(trp_eques_symmachi_hunnorum,2,5),(trp_miles_foederatus_germani,2,5),(trp_imperial_signifer,1,1)]), #huns
  ("kingdom_1_lord_reinforcements_c", "{!}majorian_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_pedes_domestici,2,4),(trp_schola_gentilium_west,2,4),(trp_schola_scutariorum_west,2,4),(trp_centenarius,1,1)]), #has schola
  #For Leo I
  ("kingdom_2_lord_reinforcements_a", "{!}leo reinforcements", 0, 0, fac_commoners, 0, [(trp_tiro,4,11),(trp_exculator,3,5),(trp_miles_foederatus_gothorum,1,4)]), #east less reliant on foederati, limitanei troops, has horse archers
  ("kingdom_2_lord_reinforcements_b", "{!}leo reinforcements", 0, 0, fac_commoners, 0, [(trp_eques_sagittarii,2,5),(trp_sagittarius,2,6),(trp_pedes_matiarii_iuniores,4,9),(trp_imperial_signifer,1,1)]),
  ("kingdom_2_lord_reinforcements_c", "{!}leo reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_domestici,2,4),(trp_schola_scutariorum_east,2,4),(trp_schola_gentilium_east,2,4),(trp_centenarius,1,1)]), #has schola

  ("kingdom_2_lord_reinforcements_excubuitors", "{!}leo reinforcements", 0, 0, fac_commoners, 0, [(trp_excubitor,2,6),(trp_schola_scutariorum_east,1,3),(trp_schola_gentilium_east,1,3),(trp_centenarius,1,1)]), #additional bucellarii? maybe will be used for scholae?
  #Zeno / Tarasikodissa - isaurian troops
  ("knight_2_7_reinforcements_c", "{!}Tarasikodissa reinforcements", 0, 0, fac_commoners, 0, [(trp_isaurian_infantry,2,5),(trp_miles_prima_isaura_sagitarria,1,5),(trp_centenarius,1,1)]),
  #theoderic strabo
  ("knight_2_11_reinforcements_a", "{!}Theoderic Strabo Reinforcements", 0, 0, fac_commoners, 0, [(trp_miles_foederatus_gothorum,5,16),(trp_gothic_skirmisher,3,4)]), #foederati
  ("knight_2_11_reinforcements_b", "{!}Theoderic Strabo Reinforcements", 0, 0, fac_commoners, 0, [(trp_miles_foederatus_gothorum,3,8),(trp_eques_symmachi_hunnorum,2,6),(trp_imperial_signifer,1,1)]),
  ("knight_2_11_reinforcements_c", "{!}Theoderic Strabo Reinforcements", 0, 0, fac_commoners, 0, [(trp_eques_scutarii,2,5),(trp_bucellarius,2,6)]),
  #cantabrians
  ("knight_3_4_reinforcements_a", "{!}cantabrian_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_latro_vasconius,3,6),(trp_forest_bandit_recruit,3,9),(trp_gothic_freeman,3,5)]), #mix of roman + frankish infantry, skirmishers
  ("knight_3_4_reinforcements_b", "{!}cantabrian_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_forest_bandit,2,5),(trp_hibero_roman_venator,2,5),(trp_hibero_roman_rusticus,2,5),(trp_standard_bearer,1,1),(trp_gothic_mounted_skirmisher,1,3)]), #mix of roman infantry, archers, frankish infantry
  ("knight_3_4_reinforcements_c", "{!}cantabrian_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_hibero_roman_defensor,1,5),(trp_bagaudae_footman,2,3),(trp_eques_cantabri,1,2)]),
  #shah
  ("kingdom_6_lord_reinforcements_a", "{!}shah Reinforcements", 0, 0, fac_commoners, 0, [(trp_kurdish_javelinman,3,8),(trp_daylamite_hillman,5,12)]), 
  ("kingdom_6_lord_reinforcements_b", "{!}shah Reinforcements", 0, 0, fac_commoners, 0, [(trp_sassanid_footman,2,6),(trp_armenian_bowman,2,4),(trp_chionite_horse_archer,1,3),(trp_gilan_horseman,1,3),(trp_sassanid_standard_bearer,1,1)]),
  ("kingdom_6_lord_reinforcements_c", "{!}shah Reinforcements", 0, 0, fac_commoners, 0, [(trp_sassanid_guard_spearman,1,2),(trp_albanian_cavalry,1,3),(trp_sassanid_bodyguard,1,3),(trp_sassanid_cavalry,1,2),(trp_sassanid_officer,1,1)]),
  #lahkmids
  ("knight_6_6_reinforcements_a", "{!}lahkmid_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_arab_skirmisher,5,10),(trp_arab_tribesman,5,10)]), #Mix of mainly arab troops
  ("knight_6_6_reinforcements_b", "{!}lahkmid_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_arab_tribesman,5,11),(trp_arab_light_cavalry,2,4),(trp_sassanid_standard_bearer,1,1),(trp_sassanid_cavalry,1,3)]),
  ("knight_6_6_reinforcements_c", "{!}lahkmid_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_arab_heavy_cavalry,2,6),(trp_sassanid_armored_footman,2,4),(trp_sassanid_officer,1,1)]),
  #armenians
  ("knight_6_7_reinforcements_a", "{!}armenian_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_kurdish_javelinman,5,10),(trp_armenian_footman,5,10)]), #Mix of mainly armenian troops
  ("knight_6_7_reinforcements_b", "{!}armenian_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_armenian_footman,4,8),(trp_armenian_bowman,1,3),(trp_kurdish_slinger,2,4),(trp_sassanid_standard_bearer,1,1),(trp_sassanid_cavalry,1,3)]), #mix of mostly armenian infantry, sassanid cavalry
  ("knight_6_7_reinforcements_c", "{!}armenian_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sassanid_horse_archer,2,6),(trp_armenian_cataphract,1,2),(trp_sassanid_armored_footman,1,2),(trp_sassanid_officer,1,1)]), #Armenian cavalry, sassanid horse archers - primarily cavalry army
  #mauri king
  ("kingdom_11_lord_reinforcements_a", "{!}Mauri Reinforcements", 0, 0, fac_commoners, 0, [(trp_ferentarius_indiginae_africani,4,10),(trp_civis_armatura_mauri,4,10)]),
  ("kingdom_11_lord_reinforcements_b", "{!}Mauri Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_fortenses,2,5),(trp_pedes_tertio_augustani,2,5),(trp_sagittarius,1,3),(trp_eques_romano_mauri,1,3),(trp_imperial_signifer,1,1)]),
  ("kingdom_11_lord_reinforcements_c", "{!}Mauri Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_mauri_tonantes_seniores,2,5),(trp_eques_cataphractarii_mauri,2,5)]),

  #ambrosius aurelianus - stronger than the other lords
  ("kingdom_13_lord_reinforcements_a", "{!}arthur Reinforcements", 0, 0, fac_commoners, 0, [(trp_briton_skirmisher,4,10),(trp_briton_footman,4,10)]),
  ("kingdom_13_lord_reinforcements_b", "{!}arthur Reinforcements", 0, 0, fac_commoners, 0, [(trp_briton_footman,3,5),(trp_abulci,2,5),(trp_briton_horseman,1,5),(trp_imperial_signifer,1,1)]),
  ("kingdom_13_lord_reinforcements_c", "{!}arthur Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_secunda_britannica,2,5),(trp_briton_knight,2,5)]),
  #cunedda
  ("knight_13_1_reinforcements_a", "{!}cunedda_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_briton_skirmisher,4,10),(trp_briton_footman,4,10)]), 
  ("knight_13_1_reinforcements_b", "{!}cunedda_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_briton_footman,2,5),(trp_abulci,2,5),(trp_imperial_signifer,1,1),(trp_pedes_votadini,4,7)]),
  ("knight_13_1_reinforcements_c", "{!}cunedda_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_briton_infantry,1,3),(trp_pedes_votadini,1,3),(trp_briton_horseman,1,3),(trp_eques_votadini,1,4)]), 
  #riothamus
  ("knight_13_5_reinforcements_a", "{!}riothamus Reinforcements", 0, 0, fac_commoners, 0, [(trp_briton_skirmisher,2,5),(trp_forest_bandit_recruit,2,5),(trp_briton_footman,2,5),(trp_forest_bandit,2,5)]),
  ("knight_13_5_reinforcements_b", "{!}riothamus Reinforcements", 0, 0, fac_commoners, 0, [(trp_briton_footman,3,8),(trp_bagaudae_footman,3,7),(trp_imperial_signifer,1,1)]),
  ("knight_13_5_reinforcements_c", "{!}riothamus Reinforcements", 0, 0, fac_commoners, 0, [(trp_briton_infantry,2,4),(trp_briton_horseman,1,3),(trp_armorican_horseman,1,3)]), #just a little OP with these guys, but hey, he inspired king arthur!
  #Madakos - alan lord under hunnic service
  ("knight_23_6_reinforcements_a", "{!}Alan Reinforcements", 0, 0, fac_commoners, 0, [(trp_caucasian_alan_tribesman,4,10),(trp_meotian_horseman,4,10)]),
  ("knight_23_6_reinforcements_b", "{!}Alan Reinforcements", 0, 0, fac_commoners, 0, [(trp_caucasian_alan_tribesman,3,7),(trp_meotian_horseman,3,6),(trp_draco_bearer,1,1)]),
  ("knight_23_6_reinforcements_c", "{!}Alan Reinforcements", 0, 0, fac_commoners, 0, [(trp_caucasian_alan_retainer,2,4),(trp_caucasian_alan_companion,1,2)]),  

  #western roman empire reinforcements
  ("wre_lord_reinforcements_a", "{!}western roman empire reinforcements", 0, 0, fac_commoners, 0, [(trp_tiro,3,6),(trp_exculator,2,4),(trp_miles_foederatus_germani,1,4),(trp_miles_foederatus_gothorum,1,4),(trp_eques_mauri,1,2)]), #west more reliant on foederati
  ("wre_lord_reinforcements_b", "{!}western roman empire reinforcements", 0, 0, fac_commoners, 0, [(trp_eques_ala,2,5),(trp_sagittarius,2,6),(trp_pedes,4,9),(trp_imperial_signifer,1,1)]),
  ("wre_lord_reinforcements_c", "{!}western roman empire reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes,1,3),(trp_eques_promoti,2,4),(trp_eques_scutarii,1,4),(trp_centenarius,1,1)]),
  #eastern roman empire reinforcements
  ("ere_lord_reinforcements_a", "{!}eastern roman empire reinforcements", 0, 0, fac_commoners, 0, [(trp_tiro,4,11),(trp_exculator,3,5),(trp_eques_mauri,1,4)]), 
  ("ere_lord_reinforcements_b", "{!}eastern roman empire reinforcements", 0, 0, fac_commoners, 0, [(trp_eques_ala,2,5),(trp_sagittarius,2,6),(trp_pedes,4,9),(trp_imperial_signifer,1,1)]),
  ("ere_lord_reinforcements_c", "{!}eastern roman empire reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes,1,3),(trp_eques_scutarii,1,4),(trp_eques_cataphractarii,1,3),(trp_centenarius,1,1)]),
  #garrison reinforcements
  ("roman_garrison_reinforcements_a", "{!}Roman Garrison Reinforcements", 0, 0, fac_commoners, 0, [(trp_tiro,4,10),(trp_exculator,4,10)]),
  ("roman_garrison_reinforcements_b", "{!}Roman Garrison Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes,3,8),(trp_sagittarius,3,7)]),
  ("roman_garrison_reinforcements_c", "{!}Roman Garrison Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes,4,10)]),

  #unique garrison
  ("ravenna_garrison_reinforcements_a", "{!}Ravenna Garrison Reinforcements", 0, 0, fac_commoners, 0, [(trp_miles_iuniorum_italicorum,4,10),(trp_exculator,4,10)]),
  ("ravenna_garrison_reinforcements_b", "{!}Ravenna Garrison Reinforcements", 0, 0, fac_commoners, 0, [(trp_miles_iuniorum_italicorum,2,5),(trp_pedes_domestici,1,3),(trp_sagittarius,3,7)]),
  ("ravenna_garrison_reinforcements_c", "{!}Ravenna Garrison Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_domestici,4,10)]),

  ("massalia_garrison_reinforcements_a", "{!}Massalia Garrison Reinforcements", 0, 0, fac_commoners, 0, [(trp_miles_musculariorum,4,10),(trp_exculator,4,10)]),
  ("massalia_garrison_reinforcements_b", "{!}Massalia Garrison Reinforcements", 0, 0, fac_commoners, 0, [(trp_miles_musculariorum,3,8),(trp_sagittarius,3,7)]),
  ("massalia_garrison_reinforcements_c", "{!}Massalia Garrison Reinforcements", 0, 0, fac_commoners, 0, [(trp_miles_musculariorum,4,10)]),

  ("regina_garrison_reinforcements_a", "{!}castra regina Garrison Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_tertiani,4,10),(trp_exculator,4,10)]),
  ("regina_garrison_reinforcements_b", "{!}castra regina Garrison Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_tertiani,3,8),(trp_sagittarius,3,7)]),
  ("regina_garrison_reinforcements_c", "{!}castra regina Garrison Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_tertiani,4,10)]),

  ("batavis_garrison_reinforcements_a", "{!}batavis Garrison Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_cohortis_batavorum,4,10),(trp_exculator,4,10)]),
  ("batavis_garrison_reinforcements_b", "{!}batavis Garrison Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_cohortis_batavorum,3,8),(trp_sagittarius,3,7)]),
  ("batavis_garrison_reinforcements_c", "{!}batavis Garrison Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_cohortis_batavorum,4,10)]),

  ("constantinople_1_garrison_reinforcements_a", "{!}Constantinople Garrison Reinforcements", 0, 0, fac_commoners, 0, [(trp_tiro,4,10),(trp_exculator,4,10)]),
  ("constantinople_1_garrison_reinforcements_b", "{!}Constantinople Garrison Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes,2,5),(trp_pedes_domestici,1,3),(trp_sagittarius,3,7)]),
  ("constantinople_1_garrison_reinforcements_c", "{!}Constantinople Garrison Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_domestici,4,10)]),

  ("constantinople_2_garrison_reinforcements_a", "{!}Constantinople Garrison Reinforcements", 0, 0, fac_commoners, 0, [(trp_tiro,2,6),(trp_isaurian_warrior,2,6),(trp_exculator,4,8)]), #isaurians stationed in cnople
  ("constantinople_2_garrison_reinforcements_b", "{!}Constantinople Garrison Reinforcements", 0, 0, fac_commoners, 0, [(trp_isaurian_infantry,2,5),(trp_excubitor,1,3),(trp_sagittarius,3,7)]),
  ("constantinople_2_garrison_reinforcements_c", "{!}Constantinople Garrison Reinforcements", 0, 0, fac_commoners, 0, [(trp_excubitor,4,10)]),

  #vandals - technically eastern germans, have access to some alan troops
  ("kingdom_vandal_reinforcements_a", "{!}Vandal Reinforcements", 0, 0, fac_commoners, 0, [(trp_eastern_germanic_skirmisher,2,5),(trp_eastern_germanic_spearman,4,10),(trp_gaetuli_warrior,2,5)]),
  ("kingdom_vandal_reinforcements_b", "{!}Vandal Reinforcements", 0, 0, fac_commoners, 0, [(trp_eastern_germanic_spearman,3,7),(trp_eastern_germanic_mounted_skirmisher,0,2),(trp_western_alan_rider,2,4),(trp_gaetuli_horseman,1,2),(trp_standard_bearer,1,1)]),
  ("kingdom_vandal_reinforcements_c", "{!}Vandal Reinforcements", 0, 0, fac_commoners, 0, [(trp_eastern_germanic_retainer,2,4),(trp_eastern_germanic_mounted_warrior,1,3),(trp_western_alan_lancer,1,3)]),

  ("kingdom_alaman_reinforcements_a", "{!}Alammani Reinforcements", 0, 0, fac_commoners, 0, [(trp_western_germanic_skirmisher,4,10),(trp_western_germanic_freeman,2,5),(trp_lentienses_foederati,2,5)]),
  ("kingdom_alaman_reinforcements_b", "{!}Alammani Reinforcements", 0, 0, fac_commoners, 0, [(trp_western_germanic_freeman,4,9),(trp_brisgavi_retainer,2,6),(trp_standard_bearer,1,1)]),
  ("kingdom_alaman_reinforcements_c", "{!}Alammani Reinforcements", 0, 0, fac_commoners, 0, [(trp_western_germanic_retainer,3,5),(trp_bucinobantes_oathgiver,1,3),(trp_western_germanic_horseman,0,2)]),

  ("kingdom_suebi_reinforcements_a", "{!}Suebi Reinforcements", 0, 0, fac_commoners, 0, [(trp_western_germanic_skirmisher,2,6),(trp_western_germanic_freeman,4,7),(trp_miles_romani,2,7)]),
  ("kingdom_suebi_reinforcements_b", "{!}Suebi Reinforcements", 0, 0, fac_commoners, 0, [(trp_western_germanic_freeman,4,9),(trp_quadi_spearman,2,6),(trp_standard_bearer,1,1)]),
  ("kingdom_suebi_reinforcements_c", "{!}Suebi Reinforcements", 0, 0, fac_commoners, 0, [(trp_western_germanic_retainer,3,5),(trp_burii_retainer,1,3),(trp_western_germanic_horseman,0,2)]),

  ("kingdom_burgundian_reinforcements_a", "{!}Burgundian Reinforcements", 0, 0, fac_commoners, 0, [(trp_western_germanic_skirmisher,2,6),(trp_western_germanic_freeman,2,4),(trp_miles_romani,6,10)]), #majority roman population, small germanic pop, mostly post-roman troops
  ("kingdom_burgundian_reinforcements_b", "{!}Burgundian Reinforcements", 0, 0, fac_commoners, 0, [(trp_western_germanic_freeman,1,3),(trp_eques_romani,2,6),(trp_burgundian_tracker,3,6),(trp_standard_bearer,1,1)]),
  ("kingdom_burgundian_reinforcements_c", "{!}Burgundian Reinforcements", 0, 0, fac_commoners, 0, [(trp_burgundian_oathtaker,4,8),(trp_bucellarius,0,2)]),

  ("kingdom_frank_reinforcements_a", "{!}Frankish Reinforcements", 0, 0, fac_commoners, 0, [(trp_bructeri_skirmisher,4,8),(trp_miles_foederatus_germani,2,6),(trp_tiro,2,6)]),
  ("kingdom_frank_reinforcements_b", "{!}Frankish Reinforcements", 0, 0, fac_commoners, 0, [(trp_eques_ala,2,5),(trp_miles_foederatus_germani,2,5),(trp_chauci_archer,2,5),(trp_imperial_signifer,1,1)]),
  ("kingdom_frank_reinforcements_c", "{!}Frankish Reinforcements", 0, 0, fac_commoners, 0, [(trp_chamavi_footman,4,10)]),

  ("kingdom_frank_king_reinforcements_c", "{!}Frankish King Reinforcements", 0, 0, fac_commoners, 0, [(trp_chamavi_footman,3,6),(trp_antrustion,1,4)]),

  ("kingdom_gepid_reinforcements_a", "{!}Gepid Reinforcements", 0, 0, fac_commoners, 0, [(trp_gothic_skirmisher,2,5),(trp_gothic_freeman,2,5),(trp_daco_roman_militia,2,4),(trp_sadages_horse_archer,2,6)]),
  ("kingdom_gepid_reinforcements_b", "{!}Gepid Reinforcements", 0, 0, fac_commoners, 0, [(trp_gothic_freeman,3,6),(trp_gothic_mounted_skirmisher,1,4),(trp_iuthungi_scout,1,3),(trp_sadagarii_horseman,1,2),(trp_standard_bearer,1,1)]),
  ("kingdom_gepid_reinforcements_c", "{!}Gepid Reinforcements", 0, 0, fac_commoners, 0, [(trp_gothic_footman,2,5),(trp_gothic_horseman,1,3),(trp_victufali_mounted_warrior,1,3)]), #+1 to help resist against the huns

  ("kingdom_rugii_reinforcements_a", "{!}Rugii Reinforcements", 0, 0, fac_commoners, 0, [(trp_gothic_skirmisher,2,8),(trp_gothic_freeman,4,6),(trp_baiuvari_armati,2,6)]), #mix of bavarii, noricum troops
  ("kingdom_rugii_reinforcements_b", "{!}Rugii Reinforcements", 0, 0, fac_commoners, 0, [(trp_gothic_freeman,2,5),(trp_miles_romani,1,3),(trp_gothic_mounted_skirmisher,3,5),(trp_standard_bearer,1,1)]),
  ("kingdom_rugii_reinforcements_c", "{!}Rugii Reinforcements", 0, 0, fac_commoners, 0, [(trp_gothic_footman,1,3),(trp_gothic_horseman,1,4),(trp_eques_romani,1,3)]),

  ("kingdom_lombard_reinforcements_a", "{!}Lombard Reinforcements", 0, 0, fac_commoners, 0, [(trp_eastern_germanic_skirmisher,4,10),(trp_eastern_germanic_spearman,4,10)]),
  ("kingdom_lombard_reinforcements_b", "{!}Lombard Reinforcements", 0, 0, fac_commoners, 0, [(trp_eastern_germanic_spearman,3,8),(trp_eastern_germanic_mounted_skirmisher,3,5),(trp_standard_bearer,1,1)]),
  ("kingdom_lombard_reinforcements_c", "{!}Lombard Reinforcements", 0, 0, fac_commoners, 0, [(trp_eastern_germanic_retainer,0,2),(trp_langobard_retainer,2,3),(trp_charudes_retainer,1,3),(trp_cynocephalus,1,3)]),

  ("kingdom_thuringian_reinforcements_a", "{!}Thuringian Reinforcements", 0, 0, fac_commoners, 0, [(trp_eastern_germanic_skirmisher,3,8),(trp_eastern_germanic_spearman,4,8),(trp_hunnic_horse_archer,1,4)]),
  ("kingdom_thuringian_reinforcements_b", "{!}Thuringian Reinforcements", 0, 0, fac_commoners, 0, [(trp_warenae_armatus,3,8),(trp_eastern_germanic_mounted_skirmisher,3,5),(trp_standard_bearer,1,1)]),
  ("kingdom_thuringian_reinforcements_c", "{!}Thuringian Reinforcements", 0, 0, fac_commoners, 0, [(trp_eastern_germanic_retainer,1,2),(trp_eastern_germanic_mounted_warrior,1,3),(trp_thuringian_horseman,1,3),(trp_warenae_optimas,1,3)]),

  ("kingdom_saxon_reinforcements_a", "{!}Saxon Reinforcements", 0, 0, fac_commoners, 0, [(trp_northern_germanic_skirmisher,4,10),(trp_northern_germanic_freeman,4,10)]), #mix of kouadoi, frisians, angles
  ("kingdom_saxon_reinforcements_b", "{!}Saxon Reinforcements", 0, 0, fac_commoners, 0, [(trp_northern_germanic_freeman,2,5),(trp_kouadoi_warrior,2,5),(trp_frisian_freeman,2,5),(trp_standard_bearer,1,1)]),
  ("kingdom_saxon_reinforcements_c", "{!}Saxon Reinforcements", 0, 0, fac_commoners, 0, [(trp_northern_germanic_warrior,2,5),(trp_saxon_companion,1,2),(trp_northern_germanic_horseman,1,3)]),

  ("kingdom_amali_reinforcements_a", "{!}ostrogothic Reinforcements", 0, 0, fac_commoners, 0, [(trp_gothic_skirmisher,4,10),(trp_gothic_freeman,4,10)]),
  ("kingdom_amali_reinforcements_b", "{!}ostrogothic Reinforcements", 0, 0, fac_commoners, 0, [(trp_gothic_freeman,2,6),(trp_gothic_mounted_skirmisher,2,3),(trp_alpidzuri_rider,1,3),(trp_tuncarsi_mounted_skirmisher,1,3),(trp_standard_bearer,1,1)]),
  ("kingdom_amali_reinforcements_c", "{!}ostrogothic Reinforcements", 0, 0, fac_commoners, 0, [(trp_gothic_footman,1,3),(trp_gothic_horseman,2,5),(trp_boisci_lancer,1,3),(trp_gothic_centurion,1,1)]),

  ("kingdom_balthi_reinforcements_a", "{!}visigoth Reinforcements", 0, 0, fac_commoners, 0, [(trp_gothic_skirmisher,2,6),(trp_gothic_freeman,4,7),(trp_miles_romani,2,7)]),
  ("kingdom_balthi_reinforcements_b", "{!}visigoth Reinforcements", 0, 0, fac_commoners, 0, [(trp_gothic_freeman,3,8),(trp_gothic_mounted_skirmisher,3,5),(trp_standard_bearer,1,1)]),
  ("kingdom_balthi_reinforcements_c", "{!}visigoth Reinforcements", 0, 0, fac_commoners, 0, [(trp_gothic_footman,1,3),(trp_gothic_horseman,2,4),(trp_roxolani_horseman,1,4),(trp_gothic_centurion,1,1)]),

  ("kingdom_amali_king_reinforcements_c", "{!}ostrogothic king Reinforcements", 0, 0, fac_commoners, 0, [(trp_gothic_footman,1,3),(trp_gothic_horseman,1,3),(trp_boisci_lancer,1,3),(trp_ostrogoth_guard,2,3),(trp_gothic_centurion,1,1)]),
  ("kingdom_balthi_king_reinforcements_c", "{!}visigoth king Reinforcements", 0, 0, fac_commoners, 0, [(trp_gothic_footman,1,3),(trp_gothic_horseman,1,3),(trp_roxolani_horseman,1,3),(trp_visigoth_guard,2,3),(trp_gothic_centurion,1,1)]),

  ("kingdom_gallaeci_reinforcements_a", "{!}Gallaeci Reinforcements", 0, 0, fac_commoners, 0, [(trp_hibero_roman_venator,4,10),(trp_hibero_roman_rusticus,4,10)]), #mix of gallaeci, germans, romans + limited bagadua
  ("kingdom_gallaeci_reinforcements_b", "{!}Gallaeci Reinforcements", 0, 0, fac_commoners, 0, [(trp_miles_romani,3,9),(trp_sagittarius,3,6),(trp_standard_bearer,1,1)]),
  ("kingdom_gallaeci_reinforcements_c", "{!}Gallaeci Reinforcements", 0, 0, fac_commoners, 0, [(trp_hibero_roman_defensor,3,7),(trp_bucellarius,1,3)]),

  #caucasian factions
  ("kingdom_kartli_reinforcements_a", "{!}Kartli Reinforcements", 0, 0, fac_commoners, 0, [(trp_caucasian_skirmisher,4,10),(trp_caucasian_levy,4,10)]),
  ("kingdom_kartli_reinforcements_b", "{!}Kartli Reinforcements", 0, 0, fac_commoners, 0, [(trp_caucasian_levy,3,9),(trp_adyghe_warrior,2,3),(trp_caucasian_archer,1,4),(trp_caucasian_standard_bearer,1,1)]),
  ("kingdom_kartli_reinforcements_c", "{!}Kartli Reinforcements", 0, 0, fac_commoners, 0, [(trp_caucasian_footman,1,3),(trp_caucasian_nobleman,1,4),(trp_sarir_horseman,2,3)]),

  ("kingdom_lazika_reinforcements_a", "{!}Lazika Reinforcements", 0, 0, fac_commoners, 0, [(trp_caucasian_skirmisher,4,10),(trp_caucasian_levy,4,10)]),
  ("kingdom_lazika_reinforcements_b", "{!}Lazika Reinforcements", 0, 0, fac_commoners, 0, [(trp_caucasian_levy,2,5),(trp_tzanni_footman,2,5),(trp_suanian_archer,1,3),(trp_caucasian_archer,1,2),(trp_caucasian_standard_bearer,1,1)]),
  ("kingdom_lazika_reinforcements_c", "{!}Lazika Reinforcements", 0, 0, fac_commoners, 0, [(trp_caucasian_footman,1,3),(trp_caucasian_nobleman,3,7)]),

  ("kingdom_arran_reinforcements_a", "{!}Caucasian Albania Reinforcements", 0, 0, fac_commoners, 0, [(trp_aghwan_warrior,6,16),(trp_lekh_warrior,2,4)]), #caucasians, lekhs, aghwan
  ("kingdom_arran_reinforcements_b", "{!}Caucasian Albania Reinforcements", 0, 0, fac_commoners, 0, [(trp_sarir_horseman,2,6),(trp_aghwan_archer,2,4),(trp_lekh_retainer,2,6),(trp_caucasian_standard_bearer,1,1)]),
  ("kingdom_arran_reinforcements_c", "{!}Caucasian Albania Reinforcements", 0, 0, fac_commoners, 0, [(trp_albanian_cavalry,2,4),(trp_aghwan_nobleman,1,3),(trp_lekh_horseman,1,3),(trp_sassanid_officer,1,1)]),

  ("kingdom_bagadua_reinforcements_a", "{!}bagadua Reinforcements", 0, 0, fac_commoners, 0, [(trp_miles_romani,4,10),(trp_forest_bandit_recruit,4,10)]),
  ("kingdom_bagadua_reinforcements_b", "{!}bagadua Reinforcements", 0, 0, fac_commoners, 0, [(trp_bagaudae_footman,4,10),(trp_forest_bandit,3,6),(trp_eques_romani,2,7),(trp_imperial_signifer,1,1)]),
  ("kingdom_bagadua_reinforcements_c", "{!}bagadua Reinforcements", 0, 0, fac_commoners, 0, [(trp_bucellarius,3,9),(trp_centenarius,1,1)]),

#Max temp 1 : 10-22 - mainly limitanei + foederati, p. com
#Max temp 2: 8-18 - unique legions of com. aux palatina if needed
#Max temp 3: 6-12 - aux palatina, palatina, anything else
#Each template gets a standard bearer at tier 2
#Each template gets a centenarius at tier 3
  #for specific lords/positions in WRE
  #Magister Militum per Gallia - based off of the Magiter Equitum's Gallic command
  ("gallia_a", "{!}Per Gallia Reinforcements", 0, 0, fac_commoners, 0, [(trp_tiro,4,8),(trp_exculator,2,4),(trp_miles_foederatus_germani,2,6),(trp_western_alan_rider,2,4)]),
  ("gallia_b", "{!}Per Gallia Reinforcements", 0, 0, fac_commoners, 0, [(trp_eques_honoriani_taifali_iuniores,3,8),(trp_pedes_cortoriacenses,5,10),(trp_imperial_signifer,1,1)]),
  ("gallia_c", "{!}Per Gallia Reinforcements", 0, 0, fac_commoners, 0, [(trp_bucellarius,2,4),(trp_eques_batavi_seniores,2,8),(trp_centenarius,1,1)]),
  #Magister Militum per Dalmatia - based off of Comes Illyricum's command - known to be well equipped, have scythians (huns + goths)
  ("dalmatia_a", "{!}Per Dalmatia Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_tertiani,5,12),(trp_exculator,3,6),(trp_eques_symmachi_hunnorum,2,4)]),
  ("dalmatia_b", "{!}Per Dalmatia Reinforcements", 0, 0, fac_commoners, 0, [(trp_miles_foederatus_gothorum,4,9),(trp_miles_sagittarii_venatores,4,9),(trp_imperial_signifer,1,1)]),
  ("dalmatia_c", "{!}Per Dalmatia Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_felices_valentinianenses,3,6),(trp_bucellarius,3,6),(trp_centenarius,1,1)]),
  #Magister Utriusque Militiae - based off of Magister Pedium's italian command
  ("utriusque_a", "{!}Magister Utriusque Militiae Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_defensores_seniores,3,8),(trp_exculator,3,4),(trp_miles_foederatus_germani,2,6),(trp_western_alan_rider,2,4)]),
  ("utriusque_b", "{!}Magister Utriusque Militiae Reinforcements", 0, 0, fac_commoners, 0, [(trp_eques_stablesiani_italiciani,2,6),(trp_pedes_invicti_seniores,6,12),(trp_imperial_signifer,1,1)]),
  ("utriusque_c", "{!}Magister Utriusque Militiae Reinforcements", 0, 0, fac_commoners, 0, [(trp_comites_alani,3,6),(trp_pedes_ioviani_seniores,3,6),(trp_centenarius,1,1)]),
  #Comes hispenias - gothic foederati, hispano-roman troops
  ("hispenias_a", "{!}comes hispenias reinforcements", 0, 0, fac_commoners, 0, [(trp_hibero_roman_rusticus,3,6),(trp_hibero_roman_venator,2,4),(trp_miles_foederatus_gothorum,2,8),(trp_eques_mauri,1,2)]), #west more reliant on foederati
  ("hispenias_b", "{!}comes hispenias reinforcements", 0, 0, fac_commoners, 0, [(trp_hibero_roman_defensor,2,5),(trp_hibero_roman_venator,2,6),(trp_pedes_invicti_seniores,4,9),(trp_imperial_signifer,1,1)]),
  ("hispenias_c", "{!}comes hispenias reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_invicti_seniores,1,3),(trp_eques_promoti,2,4),(trp_eques_scutarii,1,4),(trp_centenarius,1,1)]),
  #Comes Africae
  ("africae_a", "{!}comes africae Reinforcements", 0, 0, fac_commoners, 0, [(trp_exculator,2,6),(trp_tiro,4,10),(trp_eques_sagittarii,2,4),]),
  ("africae_b", "{!}comes africae Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_fortenses,2,5),(trp_pedes_tertio_augustani,2,5),(trp_sagittarius,1,3),(trp_eques_sagittarii,1,3),(trp_imperial_signifer,1,1)]),
  ("africae_c", "{!}comes africae Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_mauri_tonantes_seniores,2,4),(trp_eques_stablesiani_italiciani,2,4),(trp_eques_cataphractarii,1,3),(trp_centenarius,1,1)]),
  #for specific lords/positions in ERE
  #Praesentalis will be stronger than the other positions
  #Magister Militum Praesentalis I
  ("presentalis_1_a", "{!}Presentalis I Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_primi_theodosiani,3,8),(trp_eques_dalmatae,2,4),(trp_exculator,2,6),(trp_sagittarius,2,4)]),
  ("presentalis_1_b", "{!}Presentalis I Reinforcements", 0, 0, fac_commoners, 0, [(trp_eques_sagittarii,2,4),(trp_eques_scutarii,2,3),(trp_eques_cataphractarii,1,3),(trp_pedes_victores,3,8),(trp_imperial_signifer,1,1)]),
  ("presentalis_1_c", "{!}Presentalis I Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_lanciarii_seniores,2,4),(trp_pedes_matiarii_iuniores,1,4),(trp_eques_clibanarii,1,4),(trp_centenarius,1,1)]),
  #Magister Militum Praesentalis II
  ("presentalis_2_a", "{!}Presentalis II Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_thraces,3,7),(trp_eques_sexto_dalmatae,2,5),(trp_exculator,2,6),(trp_sagittarius,2,4)]),
  ("presentalis_2_b", "{!}Presentalis II Reinforcements", 0, 0, fac_commoners, 0, [(trp_eques_scutarii,2,6),(trp_pedes_regii_east,4,8),(trp_eques_cataphractarii,2,4),(trp_imperial_signifer,1,1)]),
  ("presentalis_2_c", "{!}Presentalis II Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_scythae,2,4),(trp_pedes_daci,2,4),(trp_comites_sagittarius_armeni,2,4),(trp_centenarius,1,1)]),
  #Magister Militum per Orientem
  ("orientem_a", "{!}Per Orientem Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_transtigritani,6,11),(trp_miles_prima_isaura_sagitarria,2,4),(trp_roman_slinger,1,3),(trp_pedes_theodosiaci,1,4)]),
  ("orientem_b", "{!}Per Orientem Reinforcements", 0, 0, fac_commoners, 0, [(trp_eques_sagittarii,2,4),(trp_pedes_quinta_macedonica,2,5),(trp_pedes_decima_gemina,2,5),(trp_eques_scutarii,2,4),(trp_imperial_signifer,1,1)]),
  ("orientem_c", "{!}Per Orientem Reinforcements", 0, 0, fac_commoners, 0, [(trp_bucellarius,2,4),(trp_eques_tertii_stablesiani,2,4),(trp_eques_armigeri_seniores_orientales,2,4),(trp_centenarius,1,1)]),
  #Comes Limitis Aegypti
  ("aegypti_a", "{!}Comes Limitis Aegypti Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_quinta_macedonica,5,12),(trp_exculator,3,6),(trp_sagittarius,2,4)]),
  ("aegypti_b", "{!}Comes Limitis Aegypti Reinforcements", 0, 0, fac_commoners, 0, [(trp_eques_indiginae,2,6),(trp_eques_ala,3,6),(trp_pedes_quinta_macedonica,3,6),(trp_imperial_signifer,1,1)]),
  ("aegypti_c", "{!}Comes Limitis Aegypti Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_quinta_macedonica,4,8),(trp_eques_stablesiani,2,4),(trp_centenarius,1,1)]),
  #Spahbed
  ("spahbed_a", "{!}eran-spahbed Reinforcements", 0, 0, fac_commoners, 0, [(trp_kurdish_javelinman,2,5),(trp_kurdish_slinger,1,5),(trp_sassanid_levy,4,7),(trp_daylamite_hillman,1,3)]),
  ("spahbed_b", "{!}eran-spahbed Reinforcements", 0, 0, fac_commoners, 0, [(trp_sassanid_footman,2,6),(trp_armenian_bowman,2,4),(trp_gilan_horseman,1,3),(trp_chionite_horse_archer,1,3),(trp_sassanid_standard_bearer,1,1)]),
  ("spahbed_c", "{!}eran-spahbed Reinforcements", 0, 0, fac_commoners, 0, [(trp_parizi_warrior,1,2),(trp_sassanid_cavalry,1,4),(trp_sassanid_roman_deserter,1,2),(trp_albanian_cavalry,1,2),(trp_sassanid_officer,1,1)]),
  #Comes Domesticorum
  ("domesticus_c", "{!}Domesticus Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_domestici,3,6),(trp_eques_domestici,3,6),(trp_centenarius,1,1)]), #for the domestici
  #Magister Officiorum - west
  ("officiorum_west_c", "{!}Magister Officiorum Reinforcements", 0, 0, fac_commoners, 0, [(trp_schola_scutariorum_west,3,6),(trp_schola_gentilium_west,3,6),(trp_centenarius,1,1)]),
  #Magister Officiorum - east
  ("officiorum_east_c", "{!}Magister Officiorum Reinforcements", 0, 0, fac_commoners, 0, [(trp_schola_scutariorum_east,3,6),(trp_schola_gentilium_east,3,6),(trp_centenarius,1,1)]),
  #Magister Militum per Thracias
  ("thracias_a", "{!}Per Thracias Reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_augustenses,3,6),(trp_pedes_tzaanni,3,6),(trp_exculator,2,5),(trp_sagittarius,2,5)]),
  ("thracias_b", "{!}Per Thracias Reinforcements", 0, 0, fac_commoners, 0, [(trp_eques_sagittarii,2,6),(trp_pedes_tzaanni,3,6),(trp_pedes_augustenses,3,6),(trp_imperial_signifer,1,1)]),
  ("thracias_c", "{!}Per Thracias Reinforcements", 0, 0, fac_commoners, 0, [(trp_eques_stablesiani,3,6),(trp_eques_cataphractarii,3,6),(trp_centenarius,1,1)]),
  #Magister Militum per Illyricum
  ("illyricum_a", "{!}per Illyricum reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_lanciarii_iuniores,6,11),(trp_exculator,3,5),(trp_eques_sagittarii,1,6)]), 
  ("illyricum_b", "{!}per Illyricum reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_ascarii_iuniores,2,5),(trp_miles_sagittarii_lecti,2,6),(trp_pedes_lanciarii_iuniores,4,7),(trp_imperial_signifer,1,1)]),
  ("illyricum_c", "{!}per Illyricum reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_ascarii_iuniores,2,6),(trp_eques_scutarii,1,4),(trp_centenarius,1,1)]),
  #dux foenicis
  ("dux_foenicis_a", "{!}Dux Foenicis reinforcements", 0, 0, fac_commoners, 0, [(trp_miles_primae_illyriciorum,4,11),(trp_exculator,3,5),(trp_eques_sagittarii,1,4)]), 
  ("dux_foenicis_b", "{!}Dux Foenicis reinforcements", 0, 0, fac_commoners, 0, [(trp_eques_indiginae,2,5),(trp_sagittarius,2,6),(trp_miles_primae_illyriciorum,4,7),(trp_imperial_signifer,1,1)]),
  ("dux_foenicis_c", "{!}Dux Foenicis reinforcements", 0, 0, fac_commoners, 0, [(trp_miles_primae_illyriciorum,1,3),(trp_eques_scutarii,1,4),(trp_eques_promoti,1,3),(trp_centenarius,1,1)]),
  #dux armeniae
  ("dux_armeniae_a", "{!}Dux Armeniae reinforcements", 0, 0, fac_commoners, 0, [(trp_tiro,4,11),(trp_exculator,3,5),(trp_eques_sagittarii,1,4)]), 
  ("dux_armeniae_b", "{!}Dux Armeniae reinforcements", 0, 0, fac_commoners, 0, [(trp_eques_ala,2,5),(trp_sagittarius,2,6),(trp_pedes_tzaanni,4,9),(trp_imperial_signifer,1,1)]),
  ("dux_armeniae_c", "{!}Dux Armeniae reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_tzaanni,1,3),(trp_eques_cataphractarii,2,7),(trp_centenarius,1,1)]),
  #Dux Daciae ripensis
  ("dux_daciae_a", "{!}Dux Daciae ripensis reinforcements", 0, 0, fac_commoners, 0, [(trp_tiro,4,11),(trp_exculator,3,5),(trp_eques_dalmatae,1,4)]), 
  ("dux_daciae_b", "{!}Dux Daciae ripensis reinforcements", 0, 0, fac_commoners, 0, [(trp_eques_dalmatae,2,5),(trp_sagittarius,2,6),(trp_pedes_quinta_macedonica,4,9),(trp_imperial_signifer,1,1)]),
  ("dux_daciae_c", "{!}Dux Daciae ripensis reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes_quinta_macedonica,2,5),(trp_eques_scutarii,1,5),(trp_centenarius,1,1)]),
  #Dux Palaestinae
  ("dux_palaestinae_a", "{!}Dux Palaestinae reinforcements", 0, 0, fac_commoners, 0, [(trp_tiro,2,6),(trp_exculator,2,5),(trp_dromodarius,3,5),(trp_eques_sagittarii,3,6)]), 
  ("dux_palaestinae_b", "{!}Dux Palaestinae reinforcements", 0, 0, fac_commoners, 0, [(trp_eques_dalmatae,2,5),(trp_sagittarius,2,6),(trp_pedes,4,9),(trp_imperial_signifer,1,1)]),
  ("dux_palaestinae_c", "{!}Dux Palaestinae reinforcements", 0, 0, fac_commoners, 0, [(trp_pedes,1,3),(trp_eques_scutarii,1,4),(trp_eques_promoti,1,3),(trp_centenarius,1,1)]),
  #Isuarian Numeri
  ("numeri_isaurorum_a", "{!}numeri isaurorum reinforcements", 0, 0, fac_commoners, 0, [(trp_mountain_bandit,8,18)]), 
  ("numeri_isaurorum_b", "{!}numeri isaurorum reinforcements", 0, 0, fac_commoners, 0, [(trp_isaurian_warrior,5,12),(trp_sagittarius,3,8),(trp_imperial_signifer,1,1)]),
  ("numeri_isaurorum_c", "{!}numeri isaurorum reinforcements", 0, 0, fac_commoners, 0, [(trp_isaurian_infantry,3,10),(trp_centenarius,1,1)]),

  #eventually with have Magister Militum per Illyricum
  #lanciarii iuniores (comitatenses)
  #sagitarii lecti (auxilia palatina)
  #ascarii iuniores (auxilia palatina)
  #britones seniores (palatina)
  #germaniciani seniores (comitatenses) - had both "equites" and another listing, probably shared the same pattern?

  ("steppe_bandit_lair" ,"Iazyges Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_steppe_bandit,5,20)]),
  ("taiga_bandit_lair","Germanic Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_taiga_bandit,5,20)]),
  ("desert_bandit_lair" ,"Austuriani Rebel Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_desert_bandit,5,20)]),
  ("forest_bandit_lair" ,"Bagaudae Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_forest_bandit,5,20),(trp_bagaudae_footman,1,8)]),
  ("mountain_bandit_lair" ,"Isaurian Bandit Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_mountain_bandit,5,20)]),
  ("sea_raider_lair","Saxon Raider Landing",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_sea_raider,5,20)]),
  ("sea_raider_lair_2","Saxon Raider Landing",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_sea_raider,5,20)]),
  ("sabir_bandit_lair" ,"Sabir Bandit Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_sabir_bandit,5,20)]),
  ("armenian_bandit_lair" ,"Armenian Rebel Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_armenian_bandit,5,20)]),
  ("coptic_bandit_lair" ,"Coptic Rebel Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_coptic_youth,3,10),(trp_coptic_footman,2,10)]),
  ("arab_bandit_lair" ,"Saraceni Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_arab_bandit,5,20)]),
  ("looter_lair","Kidnappers' Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,5,20)]),
  
  ("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,50)]),

  ("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),
  
   ##diplomacy begin
  ("dplmc_spouse","Your spouse",icon_woman_b|pf_civilian|pf_show_faction,0,fac_neutral,merchant_personality,[]),

  ("dplmc_gift_caravan","Your Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
#recruiter kit begin
  ("dplmc_recruiter","Recruiter",icon_flagbearer_b|pf_show_faction,0,fac_neutral,merchant_personality,[(trp_dplmc_recruiter,1,1)]),
#recruiter kit end
   ##diplomacy end

   #new party templates
  ("coptic_rebellion","Coptic Rebel Army",icon_roman_army|carries_goods(20)|pf_show_faction,0,fac_coptic_rebels,bandit_personality,[(trp_coptic_youth,20,30),(trp_coptic_footman,40,80),(trp_coptic_watchman,10,30),(trp_coptic_guard,15,30)]),

  ("scirii_horde","Danubian Suebi Horde",icon_flagbearer_b|carries_goods(20)|pf_show_faction,0,fac_hunimund_suebi,soldier_personality,[(trp_western_germanic_freeman,105,250),(trp_western_germanic_skirmisher,30,60),(trp_steppe_bandit,10,40),(trp_steppe_cataphract,5,15)]),

  ("heruli_horde","Heruli Horde",icon_flagbearer_b|carries_goods(20)|pf_show_faction,0,fac_heruli,soldier_personality,[(trp_heruli_slave,150,250),(trp_heruli_warrior,100,160),(trp_scandinavian_freeman,40,80),(trp_scandinavian_retainer,15,30),(trp_heruli_king,1,1)]),

  ("mauri_rebel_horde","Austuriani Rebel Horde",icon_khergit|carries_goods(20)|pf_show_faction,0,fac_berber_rebels,bandit_personality,[(trp_eques_indiginae_africani,80,160),(trp_desert_bandit,20,60),(trp_ferentarius_indiginae_africani,40,80),(trp_civis_armatura_mauri,30,50)]),

  ("ostrogothic_army","Ostrogothic Army",icon_germanic_army|carries_goods(20)|pf_show_faction,0,fac_kingdom_4,soldier_personality,[(trp_gothic_freeman,40,75),(trp_gothic_skirmisher,10,30),(trp_gothic_mounted_skirmisher,10,20),(trp_gothic_horseman,5,10),(trp_gothic_companion,1,1)]), #balance out so that ostrogoths do not get completely destroyed

  ("arran_army","Arran Rebels",icon_axeman|carries_goods(20)|pf_show_faction,0,fac_kingdom_28,soldier_personality,[(trp_aghwan_warrior,60,100),(trp_aghwan_archer,20,40),(trp_aghwan_nobleman,10,20),(trp_albanian_cavalry,1,5)]),

  #minor factions 30 - 60
  ("aestii_party","Aestii Warriors",icon_axeman|carries_goods(30)|pf_show_faction,0,fac_minor_aestii,bandit_personality,[(trp_aestii_skirmisher,10,25),(trp_aestii_tribesman,15,25),(trp_aestii_companion,5,10)]), #for patrols
  ("aestii_party_1","Aestii Warriors",icon_axeman|carries_goods(30)|pf_show_faction,0,fac_minor_aestii,bandit_personality,[(trp_aestii_skirmisher,10,25),(trp_aestii_tribesman,15,25),(trp_suiones_guard,5,10),(trp_aestii_companion,5,10)]), #before quest is completed
  ("aestii_party_2","Aestii Warriors",icon_axeman|carries_goods(30)|pf_show_faction,0,fac_minor_aestii,bandit_personality,[(trp_aestii_skirmisher,10,25),(trp_aestii_tribesman,15,25),(trp_sitones_retainer,5,10),(trp_aestii_companion,5,10)]), #after quest is completed
  ("irish_party","Scoti Warriors",icon_axeman|carries_goods(30)|pf_show_faction,0,fac_minor_irish,bandit_personality,[(trp_irish_skirmisher,10,25),(trp_irish_warrior,15,25),(trp_irish_follower,5,10)]),
  ("garamantian_party","Garamantian Warriors",icon_axeman|carries_goods(30)|pf_show_faction,0,fac_minor_garamantians,bandit_personality,[(trp_garamantian_warrior,14,30),(trp_garamantian_horseman,14,25),(trp_african_mercenary,2,5)]),
  ("dani_party","Dani Warriors",icon_axeman|carries_goods(30)|pf_show_faction,0,fac_minor_dani,bandit_personality,[(trp_scandinavian_freeman,10,25),(trp_scandinavian_retainer,5,10),(trp_dane_vanguard,5,15),(trp_scandinavian_comes,5,10)]),
  ("morden_party","Morden Warriors",icon_axeman|carries_goods(30)|pf_show_faction,0,fac_minor_mordens,bandit_personality,[(trp_mordvin_skirmisher,10,15),(trp_mordvin_footman,10,25),(trp_mordvin_mounted_skirmisher,5,10),(trp_mordvin_companion,3,6),(trp_komi_warrior,2,4)]),
  ("sporoi_party","Sporoi Warriors",icon_axeman|carries_goods(30)|pf_show_faction,0,fac_minor_sporoi,bandit_personality,[(trp_slav_archer,5,14),(trp_slav_skirmisher,5,14),(trp_slav_footman,10,25),(trp_slav_horseman,3,5),(trp_slav_horsearcher,3,5)]), #slavs
  ("bosphoran_party","Bosphoran Patrol",icon_axeman|carries_goods(30)|pf_show_faction,0,fac_minor_bosphoran,soldier_personality,[(trp_bosphor_recruit,10,15),(trp_bosphor_infantry,10,25),(trp_bosphor_archer,5,10),(trp_bosphor_horseman,3,6),(trp_meotian_horseman,2,4)]),
  ("abagasian_party","Abagasian Warriors",icon_axeman|carries_goods(30)|pf_show_faction,0,fac_minor_abagasians,bandit_personality,[(trp_abasgian_skirmisher,10,15),(trp_abasgian_footman,10,25),(trp_abasgian_horse_archer,7,12),(trp_abasgian_nobleman,3,8)]),
  ("tauri_party","Tauri Raiders",icon_axeman|carries_goods(30)|pf_show_faction,0,fac_minor_tauri,bandit_personality,[(trp_tauri_axeman,15,30),(trp_tauri_horseman,15,30)]),
  ("augundzi_party","Augundzi Warriors",icon_axeman|carries_goods(30)|pf_show_faction,0,fac_minor_augundzi,bandit_personality,[(trp_scandinavian_freeman,5,15),(trp_saami_hunter,5,15),(trp_scandinavian_retainer,10,20),(trp_scandinavian_comes,5,10)]),
  ("vidivarii_party","Vidivarii Warriors",icon_axeman|carries_goods(30)|pf_show_faction,0,fac_minor_vidivarii,bandit_personality,[(trp_aestii_skirmisher,10,25),(trp_gothic_freeman,15,25),(trp_scandinavian_comes,5,10)]),
  ("frisian_party","Frisii Warriors",icon_axeman|carries_goods(30)|pf_show_faction,0,fac_minor_frisians,bandit_personality,[(trp_frisian_freeman,20,40),(trp_frisian_companion,5,10),(trp_saxon_companion,5,10)]),
  ("vascones_party","Vascones Raiders",icon_axeman|carries_goods(30)|pf_show_faction,0,fac_minor_vascones,bandit_personality,[(trp_latro_vasconius,10,15),(trp_hibero_roman_venator,5,10),(trp_hibero_roman_rusticus,10,25),(trp_hibero_roman_defensor,5,10)]),
  ("gallaeci_party","Gallaeci Raiders",icon_axeman|carries_goods(30)|pf_show_faction,0,fac_minor_gallaeci,bandit_personality,[(trp_hibero_roman_venator,10,20),(trp_hibero_roman_rusticus,10,20),(trp_hibero_roman_defensor,5,10),(trp_eques_cantabri,5,10)]),
  ("venedi_party","Venedi Warriors",icon_axeman|carries_goods(30)|pf_show_faction,0,fac_minor_venedi,bandit_personality,[(trp_venedi_skirmisher,10,20),(trp_venedi_warrior,10,20),(trp_venedi_nobleman,5,10),(trp_slav_horsearcher,5,10)]),
  ("saraguroi_party","Saraguroi Warriors",icon_axeman|carries_goods(30)|pf_show_faction,0,fac_minor_saraguroi,bandit_personality,[(trp_hunnic_horse_archer,10,20),(trp_hunnic_retainer,10,20),(trp_hunnic_skirmisher,5,10),(trp_hunnic_veteran,5,10)]),
  ("onoguroi_party","Onoguroi Warriors",icon_axeman|carries_goods(30)|pf_show_faction,0,fac_minor_onoguroi,bandit_personality,[(trp_hunnic_horse_archer,10,20),(trp_hunnic_retainer,10,20),(trp_hunnic_skirmisher,5,10),(trp_hunnic_veteran,5,10)]),
  ("kutriguroi_party","Kutriguroi Warriors",icon_axeman|carries_goods(30)|pf_show_faction,0,fac_minor_kutriguroi,bandit_personality,[(trp_hunnic_horse_archer,10,20),(trp_hunnic_retainer,10,20),(trp_hunnic_skirmisher,5,10),(trp_hunnic_veteran,5,10)]),
  ("sabiroi_party","Sabiroi Warriors",icon_axeman|carries_goods(30)|pf_show_faction,0,fac_minor_sabiroi,bandit_personality,[(trp_sabir_horse_archer,20,40),(trp_sabir_cataphract,10,20)]),


  ("minor_faction_levies", "Levies", icon_axeman|pf_show_faction|pf_always_visible, soldier_personality, fac_commoners, 0, []),

]
