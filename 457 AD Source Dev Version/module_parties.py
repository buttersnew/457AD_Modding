from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

from compiler import *
####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0
#pf_town = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small


parties = [
  ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(-157.94, 19.77),[(trp_player,1,0)]),
  ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(1,1),[(trp_temp_troop,3,0)]),
#parties before this point are hardwired. Their order should not be changed.

  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#Used for calculating casulties.
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_killed", "{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  #TODO: remove this and move all to collective ally
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
   
  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #ganimet hesaplari icin #new:
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #new:  

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

###############################################################  
  ("zendar","Zendar",pf_disabled|icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18,60),[]),

 ("town_1", "Colonia Agrippina", icon_town_old|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-175.54, 111.49), [], 170), 
 ("town_2", "Apurnethige", icon_town_snow|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-222, 174.5), [], 99), 
 ("town_3", "Tolosa", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-218.04, 41.76), [], 80),                      
 ("town_4", "Sepahan", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (140.5, -2), [], 279),                   
 ("town_5", "Burdigala", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-230.2, 63), [], 93), #Formerly pictavis                 
 ("town_6", "Constantinopolis", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-47.95, 21.99), [], 178),
 ("town_7", "Thessaloniki", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-81.77, 7.86), [], 260),
 ("town_8", "Roma", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-153.72, 15.82), [], 213),
 ("town_9", "Salonae", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-126.61,31.89), [], 90),            
 ("town_10", "Sirmium", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-111.93,54.3), [], 310),         
 ("town_11", "Neapolis", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-139.029449, 6.742909), [], 150),
 ("town_12", "Napoca", icon_town_old|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-85.75, 67.84), [], 25),      
 ("town_13", "Ravenna", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-154.35, 43.99), [], 47), 
 ("town_14", "Argentoratum", icon_town_old|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-177.2, 88.88), [], 135), 
 ("town_15", "Lutetia", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-205.74, 91.46), [], 45),        #Lutetia  
 ("town_16", "Lugdunum", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-191.89, 63.69), [], 24),  
 ("town_17", "Carthago", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-166.61, -30.27), [], 90), #or Magna Germania?
 ("town_18", "Deva Victrix", icon_town_old|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-226.92, 142.78), [], 135),
 ("town_19", "Ctesiphon", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (73.51, -13.55), [], 45),
 ("town_20", "Nasibin", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (51.07, 2.94), [], 269),  
 ("town_21", "Alexandria", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-22.729939, -78.47226), [], 288),
 ("town_22", "Jerusalem", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (15.445934, -59.968212), [], 190),

#New Cities
 ("town_23","Bracara", icon_town_old|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-284.56,40.22),[], 170), #Capital of Suebi 
 ("town_24","Londinium", icon_town_old|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-212.88,120.05),[], 170),  
 ("town_25","Emerita Augusta", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-275.56,12.19),[], 170),  
 ("town_26","Amol", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.05, 38.15),[], 45), 
 #edited 10/27
 ("town_27", "Archaeopolis", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (33.63, 56.47), [], 190),
 ####
 ("town_28", "Estakhr", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (142.46, -33.13), [], 45),
 #new towns 5/22/20
 ("town_29", "Tornacum", icon_town_old|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-193.21, 112.01), [], 170), #new capital of franks
 ("town_30", "Aregalia", icon_town_snow|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-139, 108), [], 170), #capital of thuringians
 ("town_31", "Eburodunum", icon_town_snow|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-118.12, 97.89), [], 170), #capital of lombards
 ("town_32", "Tulifurdunum", icon_town_snow|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-166.07, 127.74), [], 170), #new capital of saxons
 ("town_33", "Vindobona", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-135.05, 79.7), [], 170),
 ("town_34", "Altava", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-255.5, -38.5), [], 170), #capital of romano-berbers
 ("town_35", "Hippo Regius", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-194.18, -27), [], 170), #important vandal city
 #new towns 8/12/20
 ("town_36", "Chersonesus", icon_town_old|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-27.25, 66.85), [], 170), #captured by the huns in 370 - now under roman rule
 #new towns 10/27/20
 ("town_37", "Mtskheta", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (61, 54.72), [], 170),
 ("town_38", "Antiochea", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (8.961354, -19.447083), [], 170),
 ("town_39", "Ancyra", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-19.8,13.3), [], 170),
 ("town_40", "Tarraco", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-223.76, 19.25), [], 170),
 ("town_41", "Ephesus", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-53.9,-15.4), [], 170),
 ("town_42", "Pachoras", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-10.9, -139.7), [], 170), #capital of nobatia
 #new town 8/23/21
 ("town_43", "Usupa", icon_town_snow|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (32, 91), [], 170), #capital of alans
 ("town_44", "Phanagoria", icon_town_old|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-6.06, 75), [], 170), #capital of huns



 ("castle_1", "Genua", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-173, 41.75), [], 50),      #genoa
 ("castle_2", "Venta_Silurum", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-230.05, 124.45), [], 83),
 ("castle_3", "Aquincum", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-116.81,75.23), [], 100),
 ("castle_4", "Caesaraugusta", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-240.11, 30.97), [], 180),
 ("castle_5", "Morisena", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-100.73, 65), [], 90),  
 ("castle_6", "Kydonia", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-74.4, -41.8), [], 55), #moved to crete
 ("castle_7", "Civitas_Riedonum", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-227.97, 89.72), [], 45),
 ("castle_8", "Sabratha", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-157.75,-71.84), [], 30),
 #("castle_9", "Malaca", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-268.3, -14.5), [], 100),
 ("castle_9", "Ptolemais", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-7.92, -109), [], 100),
 ("castle_10", "Veh-Ardashir", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (182, -23.2), [], 110),
 ("castle_11", "Asciburgium", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-178.52, 121.03), [], 75), 
 ("castle_12", "Augusta_Suessionum", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-195.91, 95.37), [], 95),
 ("castle_13", "Tomis", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-54.6, 53.6), [], 115),
 ("castle_14", "Vesontio", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-183.89, 76.98), [], 90), #Nemausus  
 ("castle_15", "Dun_At", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-228.67, 175.54), [], 235), 
 ("castle_16", "Pola", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-144.35,45.9), [], 45), #was aquilea, -144.56, 52.82
 ("castle_17", "Caralis", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-178.1,-9.4), [], 15), #now moved to sardinia
 ("castle_18", "Massalia", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-193.85, 32.3), [], 300), 
 ("castle_19", "Savaria", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-130.55,69.02), [], 280), #Claudium Virunum
 ("castle_20", "Syracuse", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-135.02, -25.97), [], 260),
 ("castle_21", "Avaricum", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-208.02, 75.56), [], 260),
 ("castle_22", "Icosium", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-216.9, -26.5), [], 260), # replaced caesarea
 ("castle_23", "Theodosiopolis", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (42.64, 30.82), [], 80), #Theodosiopolis in Armenia, Erzurum
 ("castle_24", "Nicaea", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-33.48, 14.29), [], 226),
 ("castle_25", "Aesmos", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-76.84, 41.27), [], 260), #was novae, however was abandoned bc of Attila. Aesemos was able to stand and win against the huns
 #("castle_26", "Ulpianum", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-103.21, 29.94), [], 260),
 ("castle_26", "Dyrrhachium", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-106.6, 8.6), [], 260),
 ("castle_27", "Melitene", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (19.950827, 12.895659), [], 260),
 ("castle_28", "Bagacum", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-189.42, 107.36), [], 260),
 ("castle_29", "Brigetio", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-120.97,78.91), [], 280),
 ("castle_30", "Mogontiacum", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-169.83, 104.52), [], 260),
 ("castle_31", "Trapezus", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (15.3,39.27), [], 260),
 ("castle_32", "Sinope", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-11.55, 38.48), [], 260), 
 ("castle_33", "Lapurdum", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-234.83, 47.51), [], 80),
 ("castle_34", "Augusta_Treverorum", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-178.29, 102.04), [], 260),
 ("castle_35", "Corinth", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-84.81, -20.4), [], 188),    
# ("castle_35", "Thessaloniki", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-83.18, 10.68), [], 260),
 ("castle_36", "Kapalak", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (83.5, 52.02), [], 260),
 ("castle_37", "Mediolanum", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-169.68, 53.93), [], 260),
 ("castle_38", "Gesoscribate", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-245.16, 94.31), [], 260), 
 ("castle_39", "Tingartia", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-232.9,-36.2), [], 280),
 ("castle_40", "Gafsa", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-179, -59.39), [], 260), 
 ("castle_41", "Damascus", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (24.02, -33.51), [], 260),
 ("castle_42", "Ecbatana", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (95.85, 22.31), [], 80), 
 ("castle_43", "Bishapur", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (129.97, -43.87), [], 260),             
 ("castle_44", "Al_Hirah", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (70.62, -34.48), [], 260),               
 ("castle_45", "Sahrestan_Yazdegerd", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (78.77, 7.11), [], 260),               
 ("castle_46", "Nova_Trajana_Bostra", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (25.1, -54.5), [], 260),
 ("castle_47", "Edessa", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (37.17, 1.8), [], 260),                 #[swycartographr] prev. coords: (42.75, 5.26)
 ("castle_48", "Chlomaron", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (58.676208, 17.043514), [], 260), #Tigranocerta's name in antiquity
 
#New Castles
  ("castle_49","Mazun",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(182.13, -77.32),[],260), 
  ("castle_50","Cair_Brithon",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-229.8, 159),[],260), 
  ("castle_51","Castra_Regina",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-145.61, 79.23),[],75), 
  #("castle_52","Toletum",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-258.37, 14.7),[],75), 
  ("castle_52","Scupi",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-97.5, 26.5),[],75), 
  ("castle_53","Scallabis",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-291.89, 21.69),[],75), 
  ("castle_54","Dvin",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(67.15, 39.3),[],75),
  ("castle_55","Carthago_Nova",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-237.35, -10.8),[],75),
  ("castle_56","Augusta_Rauricorum",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-171.52, 76),[],75),
  ("castle_57","Durovernum_Cantiacorum",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-207.36, 116.16),[],75),
  ("castle_58","Isca_Dumnoniarum",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-236.04, 115.44),[],75),
  ("castle_59","Colonia_Ulpia_Traiana",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-181.91, 116.62),[],75), 
  ("castle_60","Asturica_Augusta",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-262.13, 42.91),[],75),
  ("castle_61","Pollentia",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-214.87,4.04),[],260),
  ("castle_62","Siscia",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-119.4,46),[],260),
  ("castle_63","Ujarma", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (67.6, 55.75), [], 260),        
  ("castle_64","Phasis", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (29.1, 51.58), [], 260),
  ("castle_65","Rhagae", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (116.64,28.89), [], 260), #67.81,28.2 for tushpa
  ("castle_66", "Uburzis", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-154.76, 99), [], 180), #alemmani castle/fort

  #new castles 5/22/20
  ("castle_67", "Amisia", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-178.41, 130.24), [], 180),
  ("castle_68", "Angulus", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-165.35, 141.77), [], 180),          #[swycartographr] prev. coords: (-164, 139)
  ("castle_69", "Lupfurdunum", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-131, 102), [], 180),

  ("castle_70", "Alabu", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-161.99, 166.27), [], 180),

  ("castle_71", "Usbium", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-137.5, 88.5), [], 180),
  ("castle_72", "Bogadium", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-165.89, 120.23), [], 180),
  ("castle_73", "Camulodunum", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-205.88, 122.62), [], 180),
  ("castle_74", "Eboracum", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-213.927994, 150.319168), [], 180),
  ("castle_75", "Polondava", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-62.57,64.05), [], 180),
  #new castles 8/12/20
  ("castle_76", "Tanais", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-2.73, 89.26), [], 180),
  ("castle_77", "Olbia", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-39.51, 77.98), [], 180),
  #new castles 1/11/21
  ("castle_78", "Tingis", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-281.95, -22.7), [], 260), 
  ("castle_79", "Volubilis", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-281.5, -36.2), [], 260), 

  ("castle_80", "Ptolemais Theron", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (31.11, -133.23), [], 260), 
  ("castle_81", "Kalabhsa", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-5.1, -122), [], 260),  #-3.26, -124.214
  #new castles 8/23/21
  ("castle_82", "Siracena", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (26.24, 74.5), [], 260), 
  ("castle_83", "Seraca", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (52.3, 68.5), [], 260), 
  ("castle_84", "Ulpia_Triana_Sarmizegetusa", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-90.96, 60.22), [], 260), #unique scene
  ("castle_85", "Dierna", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-92.12, 47.93), [], 260),
  ("castle_86", "Bassiana", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-105.1,53.92), [], 260),


 ("village_1", "Olisipo", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-293.74, 18.35), [], 100),           #[swycartographr] prev. coords: (-85.1181, -28.2196)
 ("village_2", "Smyrna", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-50.94965, -8.742628), [], 110),
 ("village_3", "Vindinum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-218.7, 87), [], 120), #Heraclea Pontica #[swycartographr] prev. coords: (-32.5367, 24.7948)
 ("village_4", "Larissa", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-83.328163, -4.264576), [], 130), 
 ("village_5", "Cataractonium", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-217.35, 156.3), [], 170),
 ("village_6", "Cambidano", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-158.13,80.46), [], 100), #was Briciana, -156.84,84.85
 ("village_7", "Amisus", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-1.599802, 33.845119), [], 110),
 ("village_8", "Astuia", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-148.24, 129.43), [], 120),
 ("village_9", "Duriorigum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-236.639862, 84.705055), [], 130),
 ("village_10", "Dunnichen", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-217.99, 177.55), [], 170),  
 ("village_11", "Carnuntum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-128.66, 78.6), [], 100),
 ("village_12", "Iader", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-131.9,39), [], 110),      
 ("village_13", "Athenae", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-76.6, -18.36), [], 120),  
 ("village_14", "Tarsatica", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-137.19, 48.78), [], 130),  
 ("village_15", "Philippopolis", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-77.29, 25.23), [], 170),  
 ("village_16", "Dianium", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-233.65, -3.09), [], 170), 
 ("village_17", "Tarentum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-119.4, 0.98), [], 35),
 ("village_18", "Placentia", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-167.81, 49.29), [], 170),
 ("village_19", "Crotona", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-121.82, -10.28), [], 170),
 ("village_20", "Samshuilde",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.88,45.7),[], 40),   
 ("village_21", "Valarshapat", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (63.64, 41.48), [], 100),
 ("village_22", "Florentia", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-161.704163, 37.246693), [], 110), #
 ("village_23", "Rotomagus", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-210.083817, 99.767563), [], 120),
 ("village_24", "Constantia", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-226.92, 97.65), [], 130), #now Brest #[swycartographr] prev. coords: (-244.695, 92.4219)
 ("village_25", "Mamucium", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-221.58, 144.65), [], 170),
 #("village_26", "Romula Malva", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-82.2,49.6), [], 170), 
 ("village_26", "Naissus", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-93.23,31.4), [], 170), 
 ("village_27", "Augustodunum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-197.98, 70.07), [], 170), 
 ("village_28", "Pictavis", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-227, 72.8), [], 170), #taifals
 ("village_29", "Gesoriacum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-201.38, 111.31), [], 170), 
 ("village_30", "Letocetum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-219.7, 136.18), [], 170),   
 ("village_31", "Barium", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-124.65, 7), [], 100),           
 ("village_32", "Aventicum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-185, 64.87), [], 110),
 ("village_33", "Dionysiopolis", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-53.24, 42.45), [], 120),
 ("village_34","Vani",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.34,50),[], 40),
 ("village_35", "Tullum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-183.56, 87.23), [], 170), 
 ("village_36", "Dorostorum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-65.58, 46.22), [], 170), 
 ("village_37", "Borbetomagus", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-171.26, 100.22), [], 170),      #[swycartographr] prev. coords: (-166.612, 102.367) #[swycartographr] prev. coords: (-170.7, 90.13)
 ("village_38", "Stobi", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-93.07, 17.06), [], 170),            #[swycartographr] prev. coords: (-82.4766, 14.0508) #[swycartographr] prev. coords: (-76.64, 14.48)
 ("village_39", "Flaviobriga", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-243.34, 48.4), [], 170), 
 ("village_40", "Pons_Abbatis", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-82.4, 69.95), [], 170), 
 ("village_41", "Bonna", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-170.81, 109.41), [], 100),
 ("village_42", "Vienna", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-191.58, 57.43), [], 110),            #[swycartographr] prev. coords: (-93.2404, 118.683) #[swycartographr] prev. coords: (-190.58, 59.7)
 ("village_43", "Augusta Vindelicum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-152.55, 81.81), [], 120), 
 ("village_44", "Turris", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-183.4,4.7), [], 130),
 ("village_45","Tsunda",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.31,49.39),[], 40),                 
 ("village_46","Mokvi",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.68,60.31),[], 40),  
 ("village_47", "Augustobona", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-195.75, 81.93), [], 170), #now Orleans #[swycartographr] prev. coords: (-203.614, 85.2365)
 ("village_48", "Samosata", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (26, -4.8), [], 170),
 ("village_49","Urbnisi",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53,55.8),[], 40), 
 ("village_50", "Barcino", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-213.4, 21.25), [], 170),  
 ("village_51", "Lilybaeum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-150.59, -20.96), [], 100),
 ("village_52", "Porolissum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-89.3, 74.3), [], 110),
 ("village_53", "Adramyttium", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-54.8, 0.73), [], 120),            #[swycartographr] prev. coords: (-54.5434, 5.68571)
 ("village_54", "Poetovio", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-128.8, 60.13), [], 130),
 ("village_55", "Iconium", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-19.720499, -3.726059), [], 170),         #[swycartographr] prev. coords: (-24.7383, 7.21991)
 ("village_56", "Atuatuca_Tongrorum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-182.76, 111.09), [], 170),
 ("village_57", "Nahavand", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (95.77, -1.68), [], 170),
 ("village_58", "Cotais",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.3,56.7),[], 40),   
 ("village_59", "Portus Namnetum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-233.76, 81.34), [], 170), 
 ("village_60", "Hadrianopolis", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-63.6, 24.58), [], 170), 
 ("village_61", "Segontium", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-232.11, 141.65), [], 100),
 ("village_62", "Lissus", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-107.75, 12.5), [], 100), 
 ("village_63", "Arsamosata", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (32.83, 24.17), [], 100),        #[swycartographr] prev. coords: (28.4829, 21.2656)
 ("village_64", "Cemenelum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-181.9, 37.2), [], 100), 
 ("village_65", "Saldae", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-207.88, -26.75), [], 100),         #[swycartographr] prev. coords: (-175.119, 20.8238) #[swycartographr] prev. coords: (-175.119, 20.8238) #[swycartographr] prev. coords: (-174.41, -39.05)
 ("village_66", "Mursa", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-116.8, 56.3), [], 100), 
 ("village_67", "Narbo", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-207.94, 35.44), [], 100), #Arelate
 ("village_68", "Vesunna", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-220.208939, 58.210735), [], 100),
 ("village_69", "Samarobriva", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-200.5, 104.24), [], 100),
 ("village_70", "Durocortorum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-190.38, 98.35), [], 100),
 #("village_71", "Derbenz", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (90.31, 63.66), [], 35), 
 ("village_71", "Partav", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (82.5, 46.7), [], 35), 
 ("village_72", "Spoletum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-152.361191, 29.244488), [], 60),
 ("village_73", "Dunadd", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-231.47, 170.81), [], 55),       #[swycartographr] prev. coords: (50.6437, 132.341) #[swycartographr] prev. coords: (-229.26, 172.82)
 ("village_74", "Andematunum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-191.14,74.74), [], 15),            #[swycartographr] prev. coords: (-128.477, 11.0678) #[swycartographr] prev. coords: (-118.73, 4.33)
 ("village_75", "Segobriga", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-248.6, 14), [], 10),
 ("village_76", "Sebastopolis", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (22.16, 62.13), [], 35),
 ("village_77", "Myra", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-34.6, -25.8), [], 160),
#("village_77", "Leontopolis", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (44.6, 28.2), [], 160),
 ("village_78","Rustavi",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.7,51.86),[], 40),
 ("village_79", "Aginnum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-217.689987, 49.985104), []),
 ("village_80", "Portus Blendium", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-249.31, 50.56), [], 40),          #[swycartographr] prev. coords: (-105.964, 149.087)
 ("village_81", "Singidunum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-104.23, 50.4), [], 20),
 ("village_82","Asparos",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.51,46.95),[], 40),
 ("village_83", "Nicopolis", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-95, -11.51), [], 55),         #[swycartographr] prev. coords: (-94.6068, -10.2971) #[swycartographr] prev. coords: (-99.12, -8.16)
 ("village_84", "Caesarodunum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-179.4, 69.6), [], 15),      #[swycartographr] prev. coords: (-222.915, 77.8036) #[swycartographr] prev. coords: (-182.9, 76.44)
 ("village_85", "Valentia", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-196.9, 49.4), [], 10),
 ("village_86", "Apulum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-84.6, 62.9), [], 35),
 ("village_87", "Thagaste", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-189.15, -33.84), [], 160),        #[swycartographr] prev. coords: (-197.207, -30.2992)
 ("village_88", "Limonum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-217.66, 69.88), [], 180),        #[swycartographr] prev. coords: (-105.923, 131.182)
 ("village_89", "Flevum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-190.71, 124.15), []), 
 #("village_90", "Naissus", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-93.23,31.4), [], 40),
 ("village_90", "Deultum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-56.44,33.14), [], 40), #was ratiara, -87.33,43.2
 ("village_91", "Tyrus", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (12.05, -41.89), [], 20),             #[swycartographr] prev. coords: (12.0936, -39.4521)
 ("village_92", "Paraetonium", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-46.7, -76.24), [], 60),
 ("village_93", "Macomades", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-187.9, -39), [], 67),         #[swycartographr] prev. coords: (10.7035, -49.859)
 ("village_94", "Palmyra", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (36.3, -33.08), [], 15),
 ("village_95", "Gerrha", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (125.44, -81.73), [], 10),             #[swycartographr] prev. coords: (98.53, -35.35) #[swycartographr] prev. coords: (122.01, -75.92)
 ("village_96", "Tripoli", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (12.488498, -28.366917), [], 35),
 ("village_97", "Pelusium", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (0.25, -70.16), [], 160),       #[swycartographr] prev. coords: (6.16186, -69.2138)
 ("village_98", "Amida", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (41.81, 9.95), [], 180),              #[swycartographr] prev. coords: (45.3, 12.6)
 ("village_99", "Tushpa", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (67.81,28.2), []), #67.81,28.2 for tushpa
 ("village_100", "Sari", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (130.46, 42.45), [], 40), 
 ("village_101", "Susa", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (113.25, -20.39), [], 20),
 ("village_102", "Niniveh", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (61.5, 1), [], 170),
 ("village_103", "Ganzak", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (77.717484, 20.527571), [], 55),
 ("village_104", "Oxyrhynchus", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-16.5, -105), [], 15),
 ("village_105", "Singara", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (52.9, -5.26), [], 10),            #[swycartographr] prev. coords: (50.13, -4.13)
 ("village_106", "Tarsus", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (2.35, -10.5), [], 20), 
 ("village_107", "Tabriz", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (86.46489, 33.293297), [], 160),
 ("village_108", "Ashur", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (59.306915, -11.71656), [], 180),
 ("village_109", "Diospolis", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-14.910334, -70.351624), []),
 ("village_110", "Gaza", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (10.23, -60.26), [], 40), 
#New Villages in Mod
  ("village_111","Nishapur",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(157.84,32.19),[], 40),
  ("village_112","Rasht",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.75,40.13),[], 40),
  ("village_113", "Hormirzad", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (173.2,-50), [], 180),
  ("village_114","Daba",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(177.83,-68.95),[], 40),
  ("village_115","Pax Julia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-289.07,3.14),[], 40),
  ("village_116","Iuvavum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-137.3,73),[], 40),
  ("village_117","Venonis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-221.95,129.46),[], 40),
  ("village_118","Huensis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-235.17,179.66),[], 40), 
  ("village_119","Noviomagnus_Reginorum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-214.88,112.96),[], 40), 
  ("village_120","Delminium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-118.68,30.24),[], 40),
  ("village_121","Moray",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-218.81,187.47),[], 40),
  ("village_122","Salamatica",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-264.88, 28.38),[], 40),
  ("village_123","Lucus",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-271.83,52.53),[], 40),
  ("village_124","Aquae_Flaviae",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-277.5,37.83),[], 40),
  ("village_125","Patavium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-153.49,49.38),[], 40),
  ("village_126","Gorsium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-118,71.7),[], 40),
  ("village_127","Durobrivae",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-207.13,134.97),[], 40),
  ("village_128","Brigantium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-275.58,58.24),[], 40),
  ("village_129","Goyman",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(126.83,6.43),[], 40), 
  ("village_130","Corduba",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-273.34,-1.18),[], 40),
  ("village_131","Golshan",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(170, 18),[], 40),
  ("village_132","Hispalis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-277.71,-6.85),[], 40),
  ("village_133","Mariana",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-258.36,-0.1),[], 40), 
  ("village_134", "Hadrumetum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-167.530579, -39.699673), [], 10),
  ("village_135","Ardestan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(146.34,4.63),[], 40),
  #("village_136","Zamb",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(200,63.31),[], 40),
  ("village_136", "Basra", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (105, -42), [], 130),
  #("village_137","Khobi",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.15,54.84),[], 40),    
  ("village_137", "Aila", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (18.8, -89.4), [], 170),
  ("village_138","Gorgan",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(134.25,48.6),[], 40),
  #("village_139","Mihrdatkart",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(163,67.2),[], 40),  
  ("village_139", "Abadan", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (116.6, -38), [], 170),
  ("village_140", "Kashkar", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (83.49, -24.11), [], 60),
  ("village_141", "Sitifis", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-205.78, -35.16), [], 170),  
  ("village_142", "Leptis Magna", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-143.54, -73.67), [], 170),         
  ("village_143","Thevestis",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-178.96,-39.84),[], 40),
  ("village_144","Tipasa",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-166.91, -62.51),[], 40),
  ("village_145","Tucca",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-175.48,-31.9),[], 40),
  ("village_146","Mogentiana",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-126.47,71.02),[], 40),
  ("village_147","Tricciana",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-120.4,67.4),[], 40),
  ("village_148","Segestica",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-125,52),[], 40),
  ("village_149","Sopinae",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-120,61),[], 40),
  ("village_150","Aurelianorum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-208.3,85.55),[], 40),
  #new villages 5/22/20
  ("village_151","Navalia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-175.51,117.25),[], 40),
  ("village_152","Siatutanda",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-182.87,123.92),[], 40),
  ("village_153","Manarmanis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-184.83,132.55),[], 40),
  ("village_154","Alisum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-171.03,115.56),[], 40),
  ("village_155","Susudata",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-141,122),[], 40),
  ("village_156","Treva",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-162.71,132.96),[], 40),
  ("village_157","Arus",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-160,154.45),[], 40),
  ("village_158","Lauriacum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.07,79.33),[], 40),
  ("village_159","Chalusus",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-160,140.3),[], 40),
  ("village_160","Marionis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-150.95,135),[], 40),
  ("village_161","Menosgada",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-144.4,96.4),[], 40),
  ("village_162","Bicurgium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-143,104),[], 40),
  ("village_163","Celegia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-136.84,112.7),[], 40),
  ("village_164","Semnon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-146.8,121),[], 40),
  ("village_165","Mosovium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-145.5,114),[], 40),
  ("village_166","Candunum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-151,111),[], 40),
  ("village_167","Ascalingium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-162.25,125.07),[], 40),
  ("village_168","Caolanconum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-126,105),[], 40),
  ("village_169","Stragona",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-120,101.7),[], 40),
  ("village_170","Abieta",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-107.84,87.26),[], 40),
  ("village_171","Meliodunum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-124,95.5),[], 40),
  ("village_172","Abilurm",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-135.5,91.5),[], 40),
  ("village_173","Settuia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-110.69,97.42),[], 40),
  ("village_174","Arsicua",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-122.7,86),[], 40),

  ("village_175","Divodurum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-178.09,93.58),[], 40),
  ("village_176","Fabiranum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-170.18,133.88),[], 40),
  ("village_177","Corinium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-220.84,123.8),[], 40),
  ("village_178","Calleva",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-218.6,117.3),[], 40),
  ("village_179","Venta",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-204.26,126.13),[], 40),
  ("village_180","Moridunum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-235.5,126.6),[], 40),
  ("village_181","Tecelia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-170.12,129.33),[], 40),
  ("village_182","Munitium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-161.25,110.78),[], 40),
  ("village_183","Gravionarium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-157,104.9),[], 40),
  ("village_184","Segodunum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-162.3,95.28),[], 40),
  ("village_185","Arrabona",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-123.04,76.7),[], 40),

  ("village_186","Uscenum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-112.25,82.85),[], 40),
  ("village_187","Tbilisi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.5,50.11),[], 40),
  ("village_188","Tibiscum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-96.3,57.3),[], 40),
  ("village_189","Athribis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13.3,-82.7),[], 40),

  ("village_190","Toronum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-213,81.9),[], 40),
  ("village_191","Augusta Ausciorum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-220.7,39),[], 40),
  ("village_192","Elusa",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-222.62,44.4),[], 40),
  ("village_193","Augustonemetum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-204,56),[], 40),
  #new villages 6/14/20
  #start off with new roman villages - wre first
  ("village_194","Rhegium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-128.85,-19.1),[], 40),
  ("village_195","Amiternum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-146.6,20.62),[], 40),
  ("village_196","Pisae",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-167.2,34.4),[], 40),
  ("village_197","Verona",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-159.34,53.53),[], 40),
  ("village_198","Domavium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-110.5,40.3),[], 40),
  ("village_199","Narona",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-117.9,25.5),[], 40),
  ("village_200","Alalie",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-175,16.76),[], 40),
  ("village_201","Philippi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-74.2,14.5),[], 40),
  ("village_202","Synnada",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.3,4),[], 40), #taifals
  ("village_203","Attalia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28,-22),[], 40),
  ("village_204","Gortyna",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-66.3,-44.6),[], 40),
  ("village_205","Nicomedia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.3,19),[], 40),
  ("village_206","Caesarea Eusebia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.36,8.83),[], 40),
  ("village_207","Nicosia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.45,-30.1),[], 40),
  ("village_208","Palma",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-217.4,1.8),[], 40),
  #frankish villages
  ("village_209","Levefanum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-186.82,119.55),[], 40),
  ("village_210","Virodunum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-184.2,96.85),[], 40),
  ("village_211","Arae Flaviae",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-170.4,85.3),[], 40),
  #new desert villages - ere - vandals - mauri
  ("village_212","Memphis",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.7,-90.8),[], 40),
  ("village_213","Cyrene",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-82.2,-66.3),[], 40),
  ("village_214","Augila",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-87,-98.7),[], 40),
  ("village_215","Syrorum",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-240.6,-39.8),[], 40),
  ("village_216","Cartena",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-234.4,-26.2),[], 40),
  ("village_217","Cesarea",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-225.25,-26),[], 40),
  ("village_218","Siga",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-251.1,-32.7),[], 40),
  ("village_219","Cirta",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-197.01,-31.43),[], 40),
  ("village_220","Rusaddir",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-261.8,-30.7),[], 40),
  ("village_221","Columnata",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-237.6,-33.65),[], 40),
  ("village_222","Arsennaria",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-239,-28.6),[], 40),
  ("village_223","Bararus",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-166,-46.85),[], 40),
  ("village_224","Thabrasa",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-182.3,-29),[], 40),
  #sad! no more desert villages!
  ("village_225","Arelate",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-197.5,37.1),[], 40),
  ("village_226","Asculum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-142.53,27.13),[], 40), 
  ("village_227","Virunum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.51, 63.27),[], 40),
  #("village_228","Augustomagnus",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-202, 96),[], 40),
  ("village_228","Lindum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-211.91, 143.4),[], 40),
  #new villages 8/12/20 - huns in crimea and ukraine
  ("village_229","Theodosia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.21, 70.05),[], 342),  
  ("village_230","Argedava",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-70.7, 50.63),[], 40),
  ("village_231","Charax",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.6, 64.08),[], 40),
  ("village_232","Kalos Limen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.3, 69.65),[], 40), #was Naubarum (-20.5, 101.5)
  ("village_233","Hermonassa",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.16, 71.76),[], 40),
  ("village_234","Tyras",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48, 68.5),[], 40),
  ("village_235","Tracana",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-22.4, 85.2),[], 40),
  ("village_236","Arargus",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.72, 91),[], 40),
  ("village_237","Ionopolis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.15, 36),[], 40),
  ("village_238","Gargaza",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.04, 76.77),[], 40),
  ("village_239","Patria Onoguria",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5, 93.6),[], 40),
  #new villages 1/11/21
  ("village_240","Sala",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-291.7, -34.1),[], 40),
  ("village_241","Lixus",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-284.4, -26.25),[], 40),
  #new villages 3/12/21 - hispania
  ("village_242","Calagurris",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-244.71, 37.93),[], 40), 
  ("village_243","Saguntum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-231.11, 10.44),[], 40),
  ("village_244","Ilerda",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-227.9, 26.45),[], 40),
  ("village_245","Conimbriga",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-287, 31.3),[], 40),
  #anatolia
  ("village_246","Gangra",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.07, 20.77),[], 40),
  ("village_247","Cyzicus",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51, 9.4),[], 40),
  ("village_248","Satala",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.3, 30.2),[], 40),
  ("village_249","Sabastea",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7, 18.6),[], 40),
  ("village_250","Traianopolis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.92, 15.25),[], 40), 

  ("village_251","Luxor",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.84, -118.06),[], 40),
  ("village_252","Aswan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.3, -127.7),[], 40),
  ("village_253","Silimi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.75, -141.3),[], 40),
  #("village_254","Berenice",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.32, -104.72),[], 40),
  ("village_254","Oosook",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(36.4, -139),[], 40),
  ("village_255","Ballana",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.5, -134.86),[], 40),
  ("village_256","Philae",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.41, -130.2),[], 40),
  #new villages 8/23/21
  ("village_257","Marubius",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(38.2,89.6),[], 40),
  ("village_258","Suruba",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.61,87),[], 40),
  ("village_259","Udon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(47.26,83.37),[], 40),
  ("village_260","Ebriapa",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49,74.29),[], 40),
  ("village_261","Corusia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.7,79.2),[], 40),

  ("village_262","Resculum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-97.05, 69.5),[], 40),
  ("village_263","Romula",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-81.75, 48.57),[], 40),

  ("salt_mine","Salt_Mine",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.2, -31),[]), #special locations
  ("diocletians_palace","Old Palace",icon_village_snow_a|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-123.14, 29.53),[]),

  ("four_ways_inn","Four_Ways_Inn",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.8, -39.6),[]),
  ("test_scene","test_scene",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  #("test_scene","test_scene",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  ("battlefields","battlefields",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -16.6),[]),
  ("dhorak_keep","Dhorak_Keep",icon_town|pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50,-58),[]),

  ("ruins_1","Ruins_of_Vimiacium",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-98.3, 45),[]),
  ("hidden_forest","Zamb",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(200,63.31),[]),
  ("hidden_fort","Ruins",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_hunimund_suebi,0,ai_bhvr_hold,0,(-126,83),[]), #-110,76
  ("holy_lance_cave","Cave",pf_disabled|icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(20.8, -74.58),[]),
  ("attila_sword_location","Grove",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-110, 60),[]),
  ("waylands_smithy","Wayland's Smithy",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-225.32, 119.42),[]),
  ("donar_forest","Forest",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-133.59,130.93),[]),
  ("abandoned_mithraic_temple","Abandoned Antrum",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-166.3,57.57),[]),
  ("nubian_bandit_camp","Bandit Encampment",pf_disabled|icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2,-139),[]),
  ("vidigoias_grave","Vidigoia's Grave",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62,60),[]),
  ("bagadua_fort","Ruins of Iuliobriga",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-244.5,43.6),[]),
  ("quest_villa","Villa",pf_disabled|pf_always_visible|icon_village_snow_a|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-220,19),[]),
  ("dragons_lair","Dragon's Lair",pf_disabled|icon_bandit_lair|pf_always_visible|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-163,158.17),[]),
  ("grove_of_nymphs","Grove of Nymphs",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79,-26.4),[]),
  ("sinuessa","Sinuessa",pf_disabled|icon_village_snow_burnt_a|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-143.13,7.16),[]), #roman_village_battle map
  ("silingi_village","Vicus Silingorum",pf_disabled|icon_village_a|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-111,109),[]),
  ("venedi_village","Venedi Village",pf_disabled|icon_village_a|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-99,113),[]),
  ("agrippinus_quest_villa","Agrippinus's Villa",pf_disabled|pf_always_visible|icon_village_snow_a|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-212.5,85.4),[]),
  ("court_of_attila","Attila's Court",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-106.6, 75.9),[]), #sword of attila quest
  ("noricum_refugee_camp","Refugee Camp",pf_disabled|icon_village_a|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-140.2, 75.86),[]), #severinus quest
  ("sarmatian_camp","Campus_Sarmaticum",pf_disabled|icon_village_a|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-111.12, 74.82),[]), #hunimund quest

  #("champion_lair","Forest_Hideout",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.58,-3.78),[]), #not used just yet

  ("training_ground","Training Ground",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3, -7),[]),
  ("training_ground_1", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-144.86,8.32),[], 100), #roman, will be in italy?
  ("training_ground_2", "Training Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.79, 10.08),[], 100),
  ("training_ground_3", "Training Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-230.62, 72.0),[], 100), 
  ("training_ground_4", "Training Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.92, -85.79),[], 100),
  ("training_ground_5", "Training Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-146.43, 20.1),[], 100),


#  bridge_a
  ("Bridge_1","{!}1",pf_disabled|icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-194.17, 65.10),[], 13),
  ("Bridge_2","{!}2",pf_disabled|icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-158.5, 50.3),[], 85),
  ("Bridge_3","{!}3",pf_disabled|icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-237.07, 31.02),[], 91),
  ("Bridge_4","{!}4",pf_disabled|icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-161.16, 49.12),[], 353),
  ("Bridge_5","{!}5",pf_disabled|icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-133.18, -83.02),[], 247),
  ("Bridge_6","{!}6",pf_disabled|icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-94.23, 39.28),[], 257),
  ("Bridge_7","{!}7",pf_disabled|icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-218.92, 80.25),[], 182),
  ("Bridge_8","{!}8",pf_disabled|icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-195.15, 93.17),[], 114),
  ("Bridge_9","{!}9",pf_disabled|icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-193.06, -9.60),[], 100),
  ("Bridge_10","{!}10",pf_disabled|icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-116.6, 44.33),[], 267),
  ("Bridge_11","{!}11",pf_disabled|icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.43, -81.26),[], 295),
  ("Bridge_12","{!}12",pf_disabled|icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-154.13, 18.84),[], -35.5),
  ("Bridge_13","{!}13",pf_disabled|icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-196.3, 39.45),[], 87),
  ("Bridge_14","{!}14",pf_disabled|icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-273.26, 10.11),[], 88),

  ("looter_spawn_point"   ,"{!}looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(26, 77),[(trp_looter,15,0)]),
  ("steppe_bandit_spawn_point"  ,"the danube",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-109, 67),[(trp_looter,15,0)]),
  ("taiga_bandit_spawn_point"   ,"germania",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-154, 115),[(trp_looter,15,0)]),
  ("forest_bandit_spawn_point"  ,"gaul and hispania",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-244.52, 30.87),[(trp_looter,15,0)]),
  ("mountain_bandit_spawn_point","the mountains",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-18,-8),[(trp_looter,15,0)]),
  ("desert_bandit_spawn_point"  ,"the desert",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-189.3, -47.1),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_1"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-188.40, 125.36),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_2"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-210.7, 140.7),[(trp_looter,15,0)]),
  ("sabir_bandit_spawn_point","the steppe",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(10.72,90.59),[(trp_looter,15,0)]),
  ("armenian_rebel_spawn_point","armenia",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(65,26),[(trp_looter,15,0)]),
  ("coptic_spawn_point"  ,"egypt",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-15, -91),[(trp_looter,15,0)]),
  ("arab_bandit_spawn_point"  ,"the desert",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(50, -25),[(trp_looter,15,0)]),
 # add extra towns before this point 
  ("spawn_points_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),

  ("pirate_spawn_point"  ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-128, -11),[(trp_looter,15,0)]),
  ("scirii_spawn_point"  ,"the danube",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-109.3, 77.3),[(trp_looter,15,0)]),
  ("heruli_spawn_point"  ,"germania",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-131.5, 91.3),[(trp_looter,15,0)]),

  ("reserved_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_2"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),

  ("freelancer_party_backup","{!}",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  #minor faction villages
  ("aestii_village", "Fort_of_the_Bull", icon_castle_b|pf_town, no_menu, pt_none, fac_minor_aestii, 0, ai_bhvr_hold, 0, (-81.51, 163.4), []),
  ("irish_village", "Rath_Celtchair", icon_village_a|pf_town, no_menu, pt_none, fac_minor_irish, 0, ai_bhvr_hold, 0, (-238.26, 152.56), []),
  ("garamantian_village_1", "Garama", icon_village_c|pf_town, no_menu, pt_none, fac_minor_garamantians, 0, ai_bhvr_hold, 0, (-179.62, -100.36), []),
  ("dani_village", "Heorot", icon_village_a|pf_town, no_menu, pt_none, fac_minor_dani, 0, ai_bhvr_hold, 0, (-151.87, 149.4), []),
  ("morden_village", "Terekh's_Hall", icon_castle_b|pf_town, no_menu, pt_none, fac_minor_mordens, 0, ai_bhvr_hold, 0, (-24.79, 148.02), []), 
  ("sporoi_village", "Danaprstadr", icon_village_a|pf_town, no_menu, pt_none, fac_minor_sporoi, 0, ai_bhvr_hold, 0, (-52.67, 121.78), []),
  ("bosphoran_village", "Panticapaeum", icon_castle_a|pf_town, no_menu, pt_none, fac_minor_bosphoran, 0, ai_bhvr_hold, 0, (-15, 72.86), []),
  ("abagasian_village", "Anakopia", icon_castle_a|pf_town, no_menu, pt_none, fac_minor_abagasians, 0, ai_bhvr_hold, 0, (17.6,64.2), []),
  ("tauri_village", "Vicus_Taurorum", icon_village_a|pf_town, no_menu, pt_none, fac_minor_tauri, 0, ai_bhvr_hold, 0, (-22.66, 65.02), []),

  #minor faction villages

  ("religious_site_1","Batavis",icon_castle_snow_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-142.06, 79.02),[]), #roman
  ("religious_site_2","Monastery_of_Stavrovouni",icon_castle_snow_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.95,-33.7),[]), #roman
  ("religious_site_3","Monastery_of_Mor_Gabriel",icon_castle_snow_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.5,0.1),[]), #roman
  ("religious_site_4","Monastery_of_Saint_Anthony",icon_castle_snow_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.1,-90.8),[]), #coptic
  ("religious_site_5","Arian_Monastery",icon_castle_snow_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-224.8,50.7),[]), #arian
  ("religious_site_6","Arian_Monastery",icon_castle_snow_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-168.5,-33.9),[]), #arian
  ("religious_site_7","Grove_of_Nerthus",icon_castle_snow_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-151.9,145.7),[]), #pagan
  ("religious_site_8","Donar's_Oak",icon_castle_snow_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-151.7,102.6),[]), #pagan
  ("religious_site_9","Aphrodisias",icon_castle_snow_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.1,-13.7),[]), #greco-roman paganism
  ("religious_site_10","Great_Fire_of_Adur_Farnbag",icon_castle_snow_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(142.6,-54.3),[]), #zoroastrian
  ("religious_site_11","Great_Fire_of_Adur_Gushnap",icon_castle_snow_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.94,34.37),[]), #zoroastrian
  ("religious_site_12","Monastery_of_Saint_Athanasius",icon_castle_snow_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-67.38, 38.56),[]), #roman
  ("religious_site_13","Paromeos_Monastary",icon_castle_snow_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25, -82.8),[]), #coptic
  ("religious_site_14","Irminsul",icon_castle_snow_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-172.6,126.24),[]), #pagan
  ("religious_site_15","Monastery_of_Lerina",icon_castle_snow_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-187.7,33.9),[]), #roman
  ("religious_site_16","Monastery_of_Saint_Martin",icon_castle_snow_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-223.25,70.12),[]), #roman
  #animal spawns
  ("deer_spawn_point" ,"the wilderness",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-154,104),[]),
  ("boar_spawn_point" ,"the wilderness",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-201,72),[]),

  ]
