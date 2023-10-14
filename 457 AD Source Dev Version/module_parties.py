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
pf_minor_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium|pf_hide_defenders
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small


parties = [
  ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(-157.94, 19.77),[(trp_player,1,0)]),
  ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(1,1),[(trp_temp_troop,3,0)]),
  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_killed", "{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),   
  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), 
  ("zendar","Zendar",pf_disabled|icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(300,300),[]),

 ("town_1", "Colonia Agrippina", icon_town_old|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-159.88, 112.82), [], 170),
 ("town_2", "Apurnethige", icon_town_snow|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-218.75, 181.29), [], 99), 
 ("town_3", "Tolosa", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-200.27, 41.43), [], 80),       
 ("town_4", "Sepahan", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (234.94, 1.89), [], 279), 
 ("town_5", "Burdigala", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-218.5, 61.87), [], 93),
 ("town_6", "Constantinopolis", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (6.27, 27.68), [], 178), 
 ("town_7", "Thessaloniki", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-35.52, 15.19), [], 260),  
 ("town_8", "Roma", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-116.82, 19.37), [], 213), 
 ("town_9", "Salonae", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-81.8,38.29), [], 90),      
 ("town_10", "Sirmium", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-69.39,59.68), [], 310),  
 ("town_11", "Neapolis", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-104.72, 11.56), [], 150),      
 ("town_12", "Napoca", icon_town_old|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-34.91, 76.97), [], 25),         
 ("town_13", "Ravenna", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-121.45, 47.16), [], 47),               
 ("town_14", "Argentoratum", icon_town_old|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-157.85, 91.45), [], 135),      
 ("town_15", "Lutetia", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-192.92, 95.04), [], 45),     
 ("town_16", "Lugdunum", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-174.31, 62.13), [], 24),  
 ("town_17", "Carthago", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-136.69, -32.42), [], 90), 
 ("town_18", "Deva Victrix", icon_town_old|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-223.9, 144.94), [], 135),        
 ("town_19", "Ctesiphon", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (148.84, -3.58), [], 45), 
 ("town_20", "Nasibin", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (117.71, 20.31), [], 269),   
 ("town_21", "Alexandria", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (44.66, -70.33), [], 288),                
 ("town_22", "Jerusalem", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (86.07, -58.99), [], 190),                

#New Cities
 ("town_23","Bracara", icon_town_old|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-281.59,29.48),[], 170), 
 ("town_24","Londinium", icon_town_old|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-204.49,126.64),[], 170),                    
 ("town_25","Emerita Augusta", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-263.46,4.16),[], 170),             
 ("town_26","Amol", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(212.94, 43.63),[], 45),                   
 #edited 10/27
 ("town_27", "Archaeopolis", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (106.55, 66.14), [], 190),      
 ####
 ("town_28", "Estakhr", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (241.01, -22.64), [], 45), 
 #new towns 5/22/20
 ("town_29", "Tornacum", icon_town_old|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-178.94, 118.18), [], 170), 
 ("town_30", "Aregalia", icon_town_snow|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-123.31, 120.3), [], 170), 
 ("town_31", "Eburodunum", icon_town_snow|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-79.54, 112.21), [], 170), 
 ("town_32", "Tulifurdunum", icon_town_snow|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-146.15, 130.59), [], 170),
 ("town_33", "Vindobona", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-93.11, 88.14), [], 170),         
 ("town_34", "Altava", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-240.12, -51.92), [], 170),
 ("town_35", "Hippo Regius", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-162, -32.38), [], 170), 
 #new towns 8/12/20
 ("town_36", "Chersonesus", icon_town_old|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (38.43, 76.15), [], 170), 
 #new towns 10/27/20
 ("town_37", "Mtskheta", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (135.55, 66.79), [], 170),         
 ("town_38", "Antiochea", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (80.18, -12.12), [], 170),                 
 ("town_39", "Ancyra", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (41.43,14.31), [], 170),                       
 ("town_40", "Tarraco", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-208.99, 13.8), [], 170),                  
 ("town_41", "Ephesus", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-1.42,-6.21), [], 170),                   
 ("town_42", "Pachoras", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (84.73, -146.49), [], 170), 
 #new town 8/23/21
 ("town_43", "Usupa", icon_town_snow|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (100.21, 113.85), [], 170),
 ("town_44", "Phanagoria", icon_town_old|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (61.14, 83.77), [], 170), 



 ("castle_1", "Genua", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-146.84, 47.99), [], 50),      #genoa    #[swycartographr] prev. coords: (-173, 41.75)
 ("castle_2", "Venta_Silurum", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-227.58, 128.32), [], 83),       #[swycartographr] prev. coords: (-230.05, 124.45)
 ("castle_3", "Aquincum", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-76.61,82.7), [], 100),              #[swycartographr] prev. coords: (-116.81, 75.23) #[swycartographr] prev. coords: (-76.19, 83.89)
 ("castle_4", "Caesaraugusta", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-226.61, 26.7), [], 180),
 ("castle_5", "Morisena", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-59.7, 75.29), [], 90),               #[swycartographr] prev. coords: (-100.73, 65)
 ("castle_6", "Kydonia", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-20.07, -38.62), [], 55), #moved to crete #[swycartographr] prev. coords: (-74.4, -41.8)
 ("castle_7", "Civitas_Riedonum", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-215.38, 94.01), [], 45),     #[swycartographr] prev. coords: (-227.97, 89.72)
 ("castle_8", "Sabratha", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-122.56,-72.17), [], 30),             #[swycartographr] prev. coords: (-157.75, -71.84)
 #("castle_9", "Malaca", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-268.3, -14.5), [], 100),
 ("castle_9", "Ptolemais", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (66.69, -117.45), [], 100),           #[swycartographr] prev. coords: (-7.92, -109)
 ("castle_10", "Veh-Ardashir", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (295.45, -4.27), [], 110),        #[swycartographr] prev. coords: (182, -23.2)
 ("castle_11", "Asciburgium", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-161.64, 127.35), [], 75),        #[swycartographr] prev. coords: (-178.52, 121.03)
 ("castle_12", "Augusta_Suessionum", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-182.58, 96.86), [], 95),  #[swycartographr] prev. coords: (-195.91, 95.37)
 ("castle_13", "Tomis", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-0.3, 65.58), [], 115),                 #[swycartographr] prev. coords: (-54.6, 53.6)
 ("castle_14", "Genava", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-163.7, 66.61), [], 90),
 ("castle_15", "Dun_At", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-226.16, 176.17), [], 235),            #[swycartographr] prev. coords: (-228.67, 175.54)
 ("castle_16", "Pola", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-109.47,55.71), [], 45), #was aquilea, -144.56, 52.82 #[swycartographr] prev. coords: (-144.35, 45.9)
 ("castle_17", "Caralis", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-142.28,-5.41), [], 15), #now moved to sardinia #[swycartographr] prev. coords: (-178.1, -9.4)
 ("castle_18", "Massalia", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-174.36, 38.41), [], 300),           #[swycartographr] prev. coords: (-193.85, 32.3)
 ("castle_19", "Savaria", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-90.38,74.06), [], 280), #Claudium Virunum #[swycartographr] prev. coords: (-130.55, 69.02)
 ("castle_20", "Syracuse", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-95.45, -30.18), [], 260),           #[swycartographr] prev. coords: (-135.02, -25.97)
 ("castle_21", "Avaricum", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-193.39, 74.26), [], 260),           #[swycartographr] prev. coords: (-208.02, 75.56) #[swycartographr] prev. coords: (-192.09, 77.87)
 ("castle_22", "Icosium", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-187.89, -31.09), [], 260), # replaced caesarea #[swycartographr] prev. coords: (-216.9, -26.5)
 ("castle_23", "Theodosiopolis", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (114.85, 30.13), [], 80), #Theodosiopolis in Armenia, Erzurum #[swycartographr] prev. coords: (42.64, 30.82)
 ("castle_24", "Nicaea", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (26.34, 9.76), [], 226),                #[swycartographr] prev. coords: (-33.48, 14.29)
 ("castle_25", "Aesmos", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-22.24, 46.53), [], 260), #was novae, however was abandoned bc of Attila. Aesemos was able to stand and win against the huns #[swycartographr] prev. coords: (-76.84, 41.27)
 #("castle_26", "Ulpianum", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-103.21, 29.94), [], 260),
 ("castle_26", "Dyrrhachium", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-61.26, 8.26), [], 260),          #[swycartographr] prev. coords: (-106.6, 8.6)
 ("castle_27", "Melitene", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (89.09, 20.07), [], 260),             #[swycartographr] prev. coords: (19.9508, 12.8957)
 ("castle_28", "Bagacum", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-174.43, 112.53), [], 260),           #[swycartographr] prev. coords: (-189.42, 107.36)
 ("castle_29", "Brigetio", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-79.77,84), [], 280),             #[swycartographr] prev. coords: (-120.97, 78.91)
 ("castle_30", "Mogontiacum", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-153.36, 103.64), [], 260),       #[swycartographr] prev. coords: (-169.83, 104.52)
 ("castle_31", "Trapezus", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (90.46,43.87), [], 260),              #[swycartographr] prev. coords: (15.3, 39.27)
 ("castle_32", "Sinope", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (44.78, 40.93), [], 260),               #[swycartographr] prev. coords: (-11.55, 38.48)
 ("castle_33", "Lapurdum", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-223.05, 42.7), [], 80),            #[swycartographr] prev. coords: (-234.83, 47.51)
 ("castle_34", "Augusta_Treverorum", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-163.31, 104.96), [], 260), #[swycartographr] prev. coords: (-178.29, 102.04) #[swycartographr] prev. coords: (-160.6, 102.95)
 ("castle_35", "Corinth", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-30.95, -16.48), [], 188),            #[swycartographr] prev. coords: (-84.81, -20.4)
# ("castle_35", "Thessaloniki", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-83.18, 10.68), [], 260),
 ("castle_36", "Kapalak", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (158.97, 66), [], 260),             #[swycartographr] prev. coords: (83.5, 52.02)
 ("castle_37", "Mediolanum", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-136.79, 55.24), [], 260),         #[swycartographr] prev. coords: (-169.68, 53.93) #[swycartographr] prev. coords: (-136.38, 55.55)
 ("castle_38", "Gesoscribate", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-238.69, 94.87), [], 260),       #[swycartographr] prev. coords: (-245.16, 94.31)
 ("castle_39", "Tingartia", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-200.78,-43.74), [], 280),          #[swycartographr] prev. coords: (-232.9, -36.2)
 ("castle_40", "Gafsa", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-150.99, -65.96), [], 260),             #[swycartographr] prev. coords: (-179, -59.39)
 ("castle_41", "Damascus", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (98.41, -32.67), [], 260),            #[swycartographr] prev. coords: (24.02, -33.51)
 ("castle_42", "Hamadan", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (185.21, 21.81), [], 80),             #[swycartographr] prev. coords: (95.85, 22.31) #[swycartographr] prev. coords: (166.38, 22.49) #[swycartographr] prev. coords: (177.75, 19.5)
 ("castle_43", "Bishapur", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (223.56, -25.3), [], 260),              #[swycartographr] prev. coords: (129.97, -43.87)
 ("castle_44", "Al_Hirah", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (158.57, -28.86), [], 260),                #[swycartographr] prev. coords: (70.62, -34.48)
 ("castle_45", "Shad_Peroz", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (170.34, 10.77), [], 260),                #[swycartographr] prev. coords: (78.77, 7.11)
 ("castle_46", "Nova_Trajana_Bostra", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (96.57, -64.91), [], 260), #[swycartographr] prev. coords: (25.1, -54.5)
 ("castle_47", "Edessa", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (106.35, 7.45), [], 260),                 #[swycartographr] prev. coords: (42.75, 5.26) #[swycartographr] prev. coords: (37.17, 1.8)
 ("castle_48", "Dariunk", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (137.61, 32.57), [], 260), 
#New Castles
  ("castle_49","Mazun",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(299.33, -56.38),[],260),                     #[swycartographr] prev. coords: (182.13, -77.32)
  ("castle_50","Cair_Brithon",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-227.73, 161.82),[],260),             #[swycartographr] prev. coords: (-229.8, 159)
  ("castle_51","Castra_Regina",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-113.25, 92.87),[],75),              #[swycartographr] prev. coords: (-145.61, 79.23) #[swycartographr] prev. coords: (-100.14, 88.31)
  #("castle_52","Toletum",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-258.37, 14.7),[],75), 
  ("castle_52","Scupi",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-53.74, 39.77),[],75),                       #[swycartographr] prev. coords: (-97.5, 26.5)
  ("castle_53","Scallabis",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-289.2, 10.61),[],75),                   #[swycartographr] prev. coords: (-291.89, 21.69)
  ("castle_54","Dvin",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(138.91, 40.46),[],75),                        #[swycartographr] prev. coords: (67.15, 39.3) #[swycartographr] prev. coords: (144.05, 45.84)
  ("castle_55","Carthago_Nova",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-227.35, -15.81),[],75),             #[swycartographr] prev. coords: (-237.35, -10.8)
  ("castle_56","Augusta_Rauricorum",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-144.02, 83.39),[],75),         #[swycartographr] prev. coords: (-171.52, 76)
  ("castle_57","Durovernum_Cantiacorum",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-198.27, 121.87),[],75),    #[swycartographr] prev. coords: (-207.36, 116.16)
  ("castle_58","Isca_Dumnoniarum",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-236.85, 119.05),[],75),          #[swycartographr] prev. coords: (-236.04, 115.44)
  ("castle_59","Colonia_Ulpia_Traiana",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-166.11, 123.67),[],75),     #[swycartographr] prev. coords: (-181.91, 116.62)
  ("castle_60","Asturica_Augusta",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-250.67, 28.46),[],75),           #[swycartographr] prev. coords: (-262.13, 42.91)
  ("castle_61","Pollentia",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-192.44,1.19),[],260),                   #[swycartographr] prev. coords: (-214.87, 4.04)
  ("castle_62","Siscia",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-82.41,54.61),[],260),                      #[swycartographr] prev. coords: (-119.4, 46)
  ("castle_63","Ujarma", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (143, 67.66), [], 260),              #[swycartographr] prev. coords: (67.6, 55.75)
  ("castle_64","Phasis", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (105.24, 59.99), [], 260),              #[swycartographr] prev. coords: (29.1, 51.58)
  ("castle_65","Ray", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (212.7,29.78), [], 260), 
  ("castle_66", "Uburzis", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-133.65, 100.81), [], 180), #alemmani castle/fort #[swycartographr] prev. coords: (-154.76, 99)

  #new castles 5/22/20
  ("castle_67", "Amisia", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-161.08, 141.2), [], 180),            #[swycartographr] prev. coords: (-178.41, 130.24)
  ("castle_68", "Angulus", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-145.36, 157.46), [], 180),          #[swycartographr] prev. coords: (-164, 139) #[swycartographr] prev. coords: (-165.35, 141.77)
  ("castle_69", "Lupfurdunum", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-100.82, 119.44), [], 180),      #[swycartographr] prev. coords: (-131, 102)

  ("castle_70", "Alabu", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-140.14, 177.12), [], 180),            #[swycartographr] prev. coords: (-161.99, 166.27)

  ("castle_71", "Usbium", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-99.52, 98.16), [], 180),             #[swycartographr] prev. coords: (-137.5, 88.5) #[swycartographr] prev. coords: (-89.75, 97.99)
  ("castle_72", "Bogadium", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-150.62, 123.95), [], 180),         #[swycartographr] prev. coords: (-165.89, 120.23)
  ("castle_73", "Camulodunum", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-194.87, 131.08), [], 180),      #[swycartographr] prev. coords: (-205.88, 122.62)
  ("castle_74", "Eboracum", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-210.2, 157.85), [], 180),          #[swycartographr] prev. coords: (-213.928, 150.319)
  ("castle_75", "Polondava", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-8.41,77.31), [], 180),            #[swycartographr] prev. coords: (-62.57, 64.05)
  #new castles 8/12/20
  ("castle_76", "Tanais", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (65.79, 107.61), [], 180),             #[swycartographr] prev. coords: (-2.73, 89.26)
  ("castle_77", "Olbia", icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (16.35, 89.5), [], 180),                #[swycartographr] prev. coords: (-39.51, 77.98)
  #new castles 1/11/21
  ("castle_78", "Tingis", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-271.71, -36.84), [], 260),           #[swycartographr] prev. coords: (-281.95, -22.7)
  ("castle_79", "Volubilis", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-270.26, -49.61), [], 260),        #[swycartographr] prev. coords: (-281.5, -36.2)

  ("castle_80", "Ptolemais Theron", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (110.89, -135.38), [], 260),  #[swycartographr] prev. coords: (31.11, -133.23)
  ("castle_81", "Kalabhsa", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (86.05, -132.02), [], 260),  #-3.26, -124.214 #[swycartographr] prev. coords: (-5.1, -122)
  #new castles 8/23/21
  ("castle_82", "Siracena", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (95.76, 86.28), [], 260),            #[swycartographr] prev. coords: (26.24, 74.5)
  ("castle_83", "Seraca", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (122.53, 82.1), [], 260),              #[swycartographr] prev. coords: (52.3, 68.5)
  ("castle_84", "Ulpia_Traiana_Sarmizegetusa", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-37.56, 69.21), [], 260), #unique scene 
  ("castle_85", "Dierna", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-51.41, 57.85), [], 260),  
  ("castle_86", "Bassiana", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-63.13,57.92), [], 260),  

  ("castle_87", "Chora", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (153.29,77.98), [], 260),  
  ("castle_88", "Shamakha", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (165.83,65.07), [], 260),  
  ("castle_89", "Vahman_Ardasir", icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (201.68,-27.33), [], 260),  

 ("village_1", "Olisipo", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-292.93, 5.89), [], 100),           #[swycartographr] prev. coords: (-85.1181, -28.2196) #[swycartographr] prev. coords: (-293.74, 18.35)
 ("village_2", "Smyrna", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (2.38, 0.99), [], 110),               #[swycartographr] prev. coords: (-50.9496, -8.74263)
 ("village_3", "Vindinum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-202.81, 93.22), [], 120), #Heraclea Pontica #[swycartographr] prev. coords: (-32.5367, 24.7948) #[swycartographr] prev. coords: (-218.7, 87)
 ("village_4", "Larissa", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-36.53, -0.7), [], 130),            #[swycartographr] prev. coords: (-83.3282, -4.26458)
 ("village_5", "Cataractonium", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-212.54, 164.98), [], 170),   #[swycartographr] prev. coords: (-217.35, 156.3)
 ("village_6", "Cambidano", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-129.59,83.64), [], 100), #was Briciana, -156.84,84.85 #[swycartographr] prev. coords: (-158.13, 80.46)
 ("village_7", "Amisus", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (64.07, 41.98), [], 110),             #[swycartographr] prev. coords: (-1.5998, 33.8451)
 ("village_8", "Astuia", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-113.78, 144.22), [], 120),          #[swycartographr] prev. coords: (-148.24, 129.43)
 ("village_9", "Duriorigum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-226.66, 84.5), [], 130),        #[swycartographr] prev. coords: (-236.64, 84.7051)
 ("village_10", "Dunnichen", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-219.92, 187.76), [], 170),      #[swycartographr] prev. coords: (-217.99, 177.55)
 ("village_11", "Carnuntum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-86.68, 86.06), [], 100),        #[swycartographr] prev. coords: (-128.66, 78.6) #[swycartographr] prev. coords: (-85.09, 85.74)
 ("village_12", "Iader", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-90.73,41.58), [], 110),             #[swycartographr] prev. coords: (-131.9, 39)
 ("village_13", "Athenae", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-24.79, -11.64), [], 120),         #[swycartographr] prev. coords: (-76.6, -18.36)
 ("village_14", "Tarsatica", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-100, 54.01), [], 130),          #[swycartographr] prev. coords: (-137.19, 48.78)
 ("village_15", "Philippopolis", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-24.72, 32.7), [], 170),     #[swycartographr] prev. coords: (-77.29, 25.23)
 ("village_16", "Dianium", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-218.86, -7.17), [], 170),         #[swycartographr] prev. coords: (-233.65, -3.09)
 ("village_17", "Tarentum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-84.5, 4.45), [], 35),            #[swycartographr] prev. coords: (-119.4, 0.98)
 ("village_18", "Placentia", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-136.55, 50.43), [], 170),       #[swycartographr] prev. coords: (-167.81, 49.29)
 ("village_19", "Crotona", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-80.51, -6.47), [], 170),          #[swycartographr] prev. coords: (-121.82, -10.28)
 ("village_20", "Samshuilde",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(145.8,55.85),[], 40),              #[swycartographr] prev. coords: (68.88, 45.7)
 ("village_21", "Valarshapat", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (133.55, 43.18), [], 100),      #[swycartographr] prev. coords: (63.64, 41.48) #[swycartographr] prev. coords: (140.01, 41.86)
 ("village_22", "Florentia", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-126.27, 38.3), [], 110), #      #[swycartographr] prev. coords: (-161.704, 37.2467)
 ("village_23", "Rotomagus", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-197.42, 104.14), [], 120),      #[swycartographr] prev. coords: (-210.084, 99.7676)
 ("village_24", "Constantia", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-217.07, 100.23), [], 130), #now Brest #[swycartographr] prev. coords: (-244.695, 92.4219) #[swycartographr] prev. coords: (-226.92, 97.65)
 ("village_25", "Mamucium", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-220.13, 150.07), [], 170),       #[swycartographr] prev. coords: (-221.58, 144.65)
 #("village_26", "Romula Malva", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-82.2,49.6), [], 170), 
 ("village_26", "Naissus", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-49.5,43.13), [], 170),            #[swycartographr] prev. coords: (-93.23, 31.4)
 ("village_27", "Augustodunum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-181.26, 69.82), [], 170),    #[swycartographr] prev. coords: (-197.98, 70.07) #[swycartographr] prev. coords: (-180.78, 67.04)
 ("village_28", "Pictavis", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-214.29, 68.88), [], 170), #taifals #[swycartographr] prev. coords: (-227, 72.8) #[swycartographr] prev. coords: (-215.87, 67.87)
 ("village_29", "Gesoriacum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-185.5, 118.42), [], 170),      #[swycartographr] prev. coords: (-201.38, 111.31)
 ("village_30", "Letocetum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-217.74, 139.08), [], 170),      #[swycartographr] prev. coords: (-219.7, 136.18)
 ("village_31", "Barium", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-90.24, 16.93), [], 100),            #[swycartographr] prev. coords: (-124.65, 7)
 ("village_32", "Aventicum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-158.68, 72.97), [], 110),       #[swycartographr] prev. coords: (-185, 64.87)
 ("village_33", "Dionysiopolis", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (1.54, 51.51), [], 120),      #[swycartographr] prev. coords: (-53.24, 42.45)
 ("village_34","Vani",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(117.16,52.66),[], 40),                    #[swycartographr] prev. coords: (35.34, 50)
 ("village_35", "Tullum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-162.39, 87.36), [], 170),          #[swycartographr] prev. coords: (-183.56, 87.23)
 ("village_36", "Dorostorum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-9.12, 52.54), [], 170),        #[swycartographr] prev. coords: (-65.58, 46.22)
 ("village_37", "Borbetomagus", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-153.56, 98.46), [], 170),      #[swycartographr] prev. coords: (-166.612, 102.367) #[swycartographr] prev. coords: (-170.7, 90.13) #[swycartographr] prev. coords: (-171.26, 100.22)
 ("village_38", "Stobi", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-37.88, 27.53), [], 170),            #[swycartographr] prev. coords: (-82.4766, 14.0508) #[swycartographr] prev. coords: (-76.64, 14.48) #[swycartographr] prev. coords: (-93.07, 17.06) #[swycartographr] prev. coords: (-99.95, 33.69)
 ("village_39", "Oiasso", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-228.7, 39.58), [], 170),
 ("village_40", "Pons_Abbatis", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-35.01, 82.32), [], 170),     #[swycartographr] prev. coords: (-82.4, 69.95)
 ("village_41", "Bonna", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-157.89, 110.91), [], 100),          #[swycartographr] prev. coords: (-170.81, 109.41)
 ("village_42", "Vienna", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-174.44, 56.61), [], 110),            #[swycartographr] prev. coords: (-93.2404, 118.683) #[swycartographr] prev. coords: (-190.58, 59.7) #[swycartographr] prev. coords: (-191.58, 57.43)
 ("village_43", "Augusta Vindelicum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-117.06, 89.13), [], 120),  #[swycartographr] prev. coords: (-152.55, 81.81)
 ("village_44", "Turris", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-146.5,10.6), [], 130),             #[swycartographr] prev. coords: (-183.4, 4.7)
 ("village_45","Tsunda",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(129.58,57.05),[], 40),                  #[swycartographr] prev. coords: (53.31, 49.39)
 ("village_46","Mokvi",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.82,68.68),[], 40),                   #[swycartographr] prev. coords: (26.68, 60.31)
 ("village_47", "Nemetacum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-184, 111.66), [], 170), 
 ("village_48", "Samosata", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (92.85, 1.85), [], 170),           #[swycartographr] prev. coords: (26, -4.8)
 ("village_49","Urbnisi",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(130.27,67.38),[], 40),                 #[swycartographr] prev. coords: (53, 55.8)
 ("village_50", "Barcino", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-198.05, 19.79), [], 170),         #[swycartographr] prev. coords: (-213.4, 21.25)
 ("village_51", "Lilybaeum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-115.56, -20.15), [], 100),      #[swycartographr] prev. coords: (-150.59, -20.96)
 ("village_52", "Porolissum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-41.02, 87.15), [], 110),      #[swycartographr] prev. coords: (-89.3, 74.3) #[swycartographr] prev. coords: (-110.78, 44.92)
 ("village_53", "Adramyttium", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-2.02, 11.03), [], 120),            #[swycartographr] prev. coords: (-54.5434, 5.68571) #[swycartographr] prev. coords: (-54.8, 0.73)
 ("village_54", "Poetovio", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-95.54, 66.03), [], 130),         #[swycartographr] prev. coords: (-128.8, 60.13) #[swycartographr] prev. coords: (-96.55, 65.87)
 ("village_55", "Iconium", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (54.32, -4.06), [], 170),         #[swycartographr] prev. coords: (-24.7383, 7.21991) #[swycartographr] prev. coords: (-19.7205, -3.72606)
 ("village_56", "Atuatuca_Tongrorum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-166.4, 113.69), [], 170), #[swycartographr] prev. coords: (-182.76, 111.09)
 ("village_57", "Nahavand", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (181.65, -4.18), [], 170),         #[swycartographr] prev. coords: (95.77, -1.68) #[swycartographr] prev. coords: (174.74, -3.96)
 ("village_58", "Cotais",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120.32,63.45),[], 40),                 #[swycartographr] prev. coords: (41.3, 56.7)
 ("village_59", "Portus Namnetum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-223.83, 79.92), [], 170),  #[swycartographr] prev. coords: (-233.76, 81.34)
 ("village_60", "Hadrianopolis", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-11.26, 32.33), [], 170),    #[swycartographr] prev. coords: (-63.6, 24.58)
 ("village_61", "Segontium", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-231.27, 142.91), [], 100),      #[swycartographr] prev. coords: (-232.11, 141.65)
 ("village_62", "Lissus", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-61.72, 12.83), [], 100),           #[swycartographr] prev. coords: (-107.75, 12.5)
 ("village_63", "Arsamosata", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (32.83, 24.17), [], 100),        #[swycartographr] prev. coords: (28.4829, 21.2656)
 ("village_64", "Cemenelum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-155.51, 41.69), [], 100),       #[swycartographr] prev. coords: (-181.9, 37.2)
 ("village_65", "Saldae", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-172.9, -35.15), [], 100),         #[swycartographr] prev. coords: (-175.119, 20.8238) #[swycartographr] prev. coords: (-175.119, 20.8238) #[swycartographr] prev. coords: (-174.41, -39.05) #[swycartographr] prev. coords: (-207.88, -26.75)
 ("village_66", "Mursa", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-76.44, 61.52), [], 100),            #[swycartographr] prev. coords: (-116.8, 56.3) #[swycartographr] prev. coords: (-106.93, 40.7)
 ("village_67", "Narbo", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-191.75, 34.96), [], 100), #Arelate  #[swycartographr] prev. coords: (-207.94, 35.44)
 ("village_68", "Vesunna", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-204.24, 54.16), [], 100),         #[swycartographr] prev. coords: (-220.209, 58.2107)
 ("village_69", "Samarobriva", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-177.5, 107.53), [], 100),     #[swycartographr] prev. coords: (-200.5, 104.24)
 ("village_70", "Durocortorum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-181.09, 102.79), [], 100),    #[swycartographr] prev. coords: (-190.38, 98.35) #[swycartographr] prev. coords: (-212.61, 95.99)
 #("village_71", "Derbenz", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (90.31, 63.66), [], 35), 
 ("village_71", "Partav", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (159.72, 59.31), [], 35),            #[swycartographr] prev. coords: (82.5, 46.7)
 ("village_72", "Spoletum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-117.88, 30.6), [], 60),          #[swycartographr] prev. coords: (-152.361, 29.2445)
 ("village_73", "Dunadd", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-234.3, 182.59), [], 55),       #[swycartographr] prev. coords: (50.6437, 132.341) #[swycartographr] prev. coords: (-229.26, 172.82) #[swycartographr] prev. coords: (-231.47, 170.81)
 ("village_74", "Andematunum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-173.21,77.44), [], 15),            #[swycartographr] prev. coords: (-128.477, 11.0678) #[swycartographr] prev. coords: (-118.73, 4.33) #[swycartographr] prev. coords: (-191.14, 74.74)
 ("village_75", "Segobriga", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-238.27, 10.13), [], 10),        #[swycartographr] prev. coords: (-248.6, 14)
 ("village_76", "Sebastopolis", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (95.25, 70.93), [], 35),       #[swycartographr] prev. coords: (22.16, 62.13)
 ("village_77", "Myra", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (24.31, -21.04), [], 160),             #[swycartographr] prev. coords: (-34.6, -25.8)
#("village_77", "Leontopolis", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (44.6, 28.2), [], 160),
 ("village_78","Rustavi",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(144.04,62.74),[], 40),                 #[swycartographr] prev. coords: (70.7, 51.86)
 ("village_79", "Aginnum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-217.689987, 49.985104), []),
 ("village_80", "Portus Blendium", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-253.31, 46.1), [], 40),          #[swycartographr] prev. coords: (-105.964, 149.087) #[swycartographr] prev. coords: (-249.31, 50.56)
 ("village_81", "Singidunum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-63.44, 52.51), [], 20),        #[swycartographr] prev. coords: (-104.23, 50.4) #[swycartographr] prev. coords: (-78.47, 61.99)
 ("village_82","Asparos",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(103.79,52.43),[], 40),                 #[swycartographr] prev. coords: (26.51, 46.95)
 ("village_83", "Nicopolis", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-47.3, -8.37), [], 55),         #[swycartographr] prev. coords: (-94.6068, -10.2971) #[swycartographr] prev. coords: (-99.12, -8.16) #[swycartographr] prev. coords: (-95, -11.51)
 ("village_84", "Vesontio", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-164.45, 80.7), [], 15), 
 ("village_85", "Valentia", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-176.5, 49.18), [], 10),          #[swycartographr] prev. coords: (-196.9, 49.4)
 ("village_86", "Apulum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-30.01, 73.52), [], 35),            #[swycartographr] prev. coords: (-84.6, 62.9)
 ("village_87", "Thagaste", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-155.45, -44.53), [], 160),        #[swycartographr] prev. coords: (-197.207, -30.2992) #[swycartographr] prev. coords: (-189.15, -33.84)
 ("village_88", "Limonum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-197.33, 64.38), [], 180),        #[swycartographr] prev. coords: (-105.923, 131.182) #[swycartographr] prev. coords: (-217.66, 69.88) #[swycartographr] prev. coords: (-228.95, 73.88)
 ("village_89", "Flevum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-176.57, 129.66), []),              #[swycartographr] prev. coords: (-190.71, 124.15)
 #("village_90", "Naissus", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-93.23,31.4), [], 40),
 ("village_90", "Deultum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-2.21,42.58), [], 40), #was ratiara, -87.33,43.2 #[swycartographr] prev. coords: (-56.44, 33.14)
 ("village_91", "Tyrus", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (83.23, -36.09), [], 20),             #[swycartographr] prev. coords: (12.0936, -39.4521) #[swycartographr] prev. coords: (12.05, -41.89)
 ("village_92", "Paraetonium", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (8.31, -76.73), [], 60),        #[swycartographr] prev. coords: (-46.7, -76.24)
 ("village_93", "Macomades", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-152.21, -51.91), [], 67),         #[swycartographr] prev. coords: (10.7035, -49.859) #[swycartographr] prev. coords: (-187.9, -39)
 ("village_94", "Palmyra", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (107.04, -31.87), [], 15),          #[swycartographr] prev. coords: (36.3, -33.08)
 ("village_95", "Gerrha", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (237.86, -71.3), [], 10),             #[swycartographr] prev. coords: (98.53, -35.35) #[swycartographr] prev. coords: (122.01, -75.92) #[swycartographr] prev. coords: (125.44, -81.73)
 ("village_96", "Tripoli", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (84.27, -28.5), [], 35),            #[swycartographr] prev. coords: (12.4885, -28.3669)
 ("village_97", "Pelusium", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (65.32, -68.54), [], 160),       #[swycartographr] prev. coords: (6.16186, -69.2138) #[swycartographr] prev. coords: (0.25, -70.16)
 ("village_98", "Amida", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (103.94, 17.47), [], 180),              #[swycartographr] prev. coords: (45.3, 12.6) #[swycartographr] prev. coords: (41.81, 9.95) #[swycartographr] prev. coords: (101.48, -17.43)
 ("village_99", "Sisauranon", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (125.18,21.52), []),
 ("village_100", "Sari", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (218, 47.99), [], 40),                #[swycartographr] prev. coords: (130.46, 42.45)
 ("village_101", "Susa", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (195.84, -12.13), [], 20),             #[swycartographr] prev. coords: (113.25, -20.39) #[swycartographr] prev. coords: (192.55, -7.91) #[swycartographr] prev. coords: (193.18, -10.62)
 ("village_102", "Niniveh", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (138.35, 9.95), [], 170),          #[swycartographr] prev. coords: (61.5, 1)
 ("village_103", "Ganzak", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (163.17, 24.5), [], 55),           #[swycartographr] prev. coords: (77.7175, 20.5276) #[swycartographr] prev. coords: (162.32, 20.21)
 ("village_104", "Oxyrhynchus", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (55.47, -110.91), [], 15),
 ("village_105", "Singara", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (123.21, 9.12), [], 10),            #[swycartographr] prev. coords: (50.13, -4.13) #[swycartographr] prev. coords: (52.9, -5.26)
 ("village_106", "Tarsus", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (66.27, -7.34), [], 20),            #[swycartographr] prev. coords: (2.35, -10.5)
 ("village_107", "Tabriz", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (156.78, 32.1), [], 160),           
 ("village_108", "Peroz_Shapur", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (137.18, 3.28), [], 180),            #[swycartographr] prev. coords: (59.3069, -11.7166)
 ("village_109", "Diospolis", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (50.51, -68.66), []),            #[swycartographr] prev. coords: (-14.9103, -70.3516)
 ("village_110", "Gaza", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (78.03, -64.45), [], 40),             #[swycartographr] prev. coords: (10.23, -60.26)
#New Villages in Mod
  ("village_111","Nishapur",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(262.01,43.62),[], 40),              #[swycartographr] prev. coords: (157.84, 32.19)
  ("village_112","Royan",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(186.14,39.44),[], 40),                 #[swycartographr] prev. coords: (99.75, 40.13)
  ("village_113", "Hormirzad", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (289.1,-27.78), [], 180),       #[swycartographr] prev. coords: (173.2, -50)
  ("village_114","Daba",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(288.34,-46.06),[], 40),                 #[swycartographr] prev. coords: (177.83, -68.95)
  ("village_115","Pax Julia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-284.2,-5.85),[], 40),             #[swycartographr] prev. coords: (-289.07, 3.14)
  ("village_116","Iuvavum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-89.9,81.43),[], 40),                #[swycartographr] prev. coords: (-137.3, 73)
  ("village_117","Venonis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-217.02,132.18),[], 40),             #[swycartographr] prev. coords: (-221.95, 129.46)
  ("village_118","Huensis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-234.22,191.39),[], 40),             #[swycartographr] prev. coords: (-235.17, 179.66)
  ("village_119","Noviomagnus_Reginorum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-210.14,119.73),[], 40),  #[swycartographr] prev. coords: (-214.88, 112.96)
  ("village_120","Delminium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-69.38,35.73),[], 40),             #[swycartographr] prev. coords: (-118.68, 30.24)
  ("village_121","Moray",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-222.08,197.87),[], 40),               #[swycartographr] prev. coords: (-218.81, 187.47)
  ("village_122","Salamatica",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-251.85, 17.22),[], 40),          #[swycartographr] prev. coords: (-264.88, 28.38)
  ("village_123","Forum_Limicorum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-269.22,34.6),[], 40),
  ("village_124","Aquae_Flaviae",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-267.5,28.59),[], 40),         #[swycartographr] prev. coords: (-277.5, 37.83)
  ("village_125","Patavium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-122.84,56.72),[], 40),             #[swycartographr] prev. coords: (-153.49, 49.38)
  ("village_126","Gorsium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-77.15,79.31),[], 40),               #[swycartographr] prev. coords: (-118, 71.7)
  ("village_127","Durobrivae",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-204.38,138.1),[], 40),           #[swycartographr] prev. coords: (-207.13, 134.97)
  ("village_128","Brigantium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-272.66,51.58),[], 40),           #[swycartographr] prev. coords: (-275.58, 58.24)
  ("village_129","Goyman",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(227.29,12.41),[], 40),                #[swycartographr] prev. coords: (126.83, 6.43)
  ("village_130","Corduba",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-264.45,-6.77),[], 40),              #[swycartographr] prev. coords: (-273.34, -1.18)
  ("village_131","Golshan",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(294.65, 16.56),[], 40),              #[swycartographr] prev. coords: (170, 18)
  ("village_132","Hispalis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-267.11,-16.25),[], 40),            #[swycartographr] prev. coords: (-277.71, -6.85)
  ("village_133","Mariana",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-244.53,-10.07),[], 40),             #[swycartographr] prev. coords: (-258.36, -0.1)
  ("village_134", "Hadrumetum", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-132.54, -45.65), [], 10),    #[swycartographr] prev. coords: (-167.531, -39.6997)
  ("village_135","Ardestan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(251.55,4.91),[], 40),               #[swycartographr] prev. coords: (146.34, 4.63)
  #("village_136","Zamb",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(200,63.31),[], 40),
  ("village_136", "Vahshatabad_Ardashir", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (198.54, -33.87), [], 130),         #[swycartographr] prev. coords: (105, -42)
  #("village_137","Khobi",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.15,54.84),[], 40),    
  ("village_137", "Aila", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (90.23, -76.89), [], 170),           #[swycartographr] prev. coords: (18.8, -89.4)
  ("village_138","Gorgan",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(219.24,54.64),[], 40),                #[swycartographr] prev. coords: (134.25, 48.6)
  #("village_139","Mihrdatkart",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(163,67.2),[], 40),  
  ("village_139", "Argan", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (214.33, -23.75), [], 170),           #[swycartographr] prev. coords: (116.6, -38)
  ("village_140", "Hormoz_Ardashir", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (173.45, -23.27), [], 60),        #[swycartographr] prev. coords: (83.49, -24.11)
  ("village_141", "Sitifis", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-172.57, -45.22), [], 170),      #[swycartographr] prev. coords: (-205.78, -35.16)
  ("village_142", "Leptis Magna", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-91.26, -79.77), [], 170),          #[swycartographr] prev. coords: (-143.54, -73.67)
  ("village_143","Thevestis",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-147.43,-41.34),[], 40),           #[swycartographr] prev. coords: (-178.96, -39.84)
  ("village_144","Tipasa",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-132.08, -66.38),[], 40),             #[swycartographr] prev. coords: (-166.91, -62.51)
  ("village_145","Tucca",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.98,-36.86),[], 40),               #[swycartographr] prev. coords: (-175.48, -31.9)
  ("village_146","Mogentiana",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-86.05,76.16),[], 40),            #[swycartographr] prev. coords: (-126.47, 71.02)
  ("village_147","Tricciana",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-80.35,73.15),[], 40),             #[swycartographr] prev. coords: (-120.4, 67.4)
  ("village_148","Segestica",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-86.89,60.29),[], 40),             #[swycartographr] prev. coords: (-125, 52)
  ("village_149","Sopinae",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-80.89,67.88),[], 40),                #[swycartographr] prev. coords: (-120, 61) #[swycartographr] prev. coords: (-80.09, 71.8)
  ("village_150","Aurelianorum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-193.3,87.67),[], 40),          #[swycartographr] prev. coords: (-208.3, 85.55)
  #new villages 5/22/20
  ("village_151","Navalia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-157.36,120.98),[], 40),             #[swycartographr] prev. coords: (-175.51, 117.25)
  ("village_152","Siatutanda",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-165.05,130.46),[], 40),          #[swycartographr] prev. coords: (-182.87, 123.92)
  ("village_153","Manarmanis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-172.58,138.87),[], 40),          #[swycartographr] prev. coords: (-184.83, 132.55)
  ("village_154","Alisum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-155.09,116.31),[], 40),              #[swycartographr] prev. coords: (-171.03, 115.56)
  ("village_155","Bezabde",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(128.15,26.32),[], 40),
  ("village_156","Treva",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-137.62,143.49),[], 40),               #[swycartographr] prev. coords: (-162.71, 132.96)
  ("village_157","Arus",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-147.09,170.67),[], 40),                #[swycartographr] prev. coords: (-160, 154.45)
  ("village_158","Lauriacum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-101.38,87.85),[], 40),             #[swycartographr] prev. coords: (-139.07, 79.33)
  ("village_159","Chalusus",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-140.9,153.35),[], 40),             #[swycartographr] prev. coords: (-160, 140.3)
  ("village_160","Marionis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-120.37,150.17),[], 40),            #[swycartographr] prev. coords: (-150.95, 135)
  ("village_161","Menosgada",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-111.66,101.82),[], 40),           #[swycartographr] prev. coords: (-144.4, 96.4)
  ("village_162","Bicurgium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-114.74,116.08),[], 40),           #[swycartographr] prev. coords: (-143, 104)
  ("village_163","Celegia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-105.14,123.45),[], 40),             #[swycartographr] prev. coords: (-136.84, 112.7)
  ("village_164","Semnon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-123.89,137.43),[], 40),              #[swycartographr] prev. coords: (-122.59, 135.74) #[swycartographr] prev. coords: (-146.8, 121)
  ("village_165","Dastagerd",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(153.93,5.74),[], 40),            
  ("village_166","Candunum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-131.36,120.55),[], 40),            #[swycartographr] prev. coords: (-151, 111)
  ("village_167","Ascalingium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-143.92,124.76),[], 40),         #[swycartographr] prev. coords: (-162.25, 125.07)
  ("village_168","Caolanconum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-105.97,130.76),[], 40),           #[swycartographr] prev. coords: (-126, 105)
  ("village_169","Stragona",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-82.04,116.83),[], 40),             #[swycartographr] prev. coords: (-120, 101.7)
  ("village_170","Abieta",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.64,95.46),[], 40),                 #[swycartographr] prev. coords: (-107.84, 87.26) #[swycartographr] prev. coords: (-61.7, 99.76)
  ("village_171","Bagavan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(132.41,31.71),[], 40),           
  ("village_172","Tergeste",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-109.99,61.16),[], 40), 
  ("village_173","Settuia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.32,107.16),[], 40),              #[swycartographr] prev. coords: (-110.69, 97.42)
  ("village_174","Arsicua",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.58,96.61),[], 40),               #[swycartographr] prev. coords: (-122.7, 86) #[swycartographr] prev. coords: (-76.67, 93.42)

  ("village_175","Divodurum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-158.58,95.48),[], 40),           #[swycartographr] prev. coords: (-178.09, 93.58) #[swycartographr] prev. coords: (-179.62, 101.76)
  ("village_176","Fabiranum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-149.27,143.35),[], 40),           #[swycartographr] prev. coords: (-170.18, 133.88)
  ("village_177","Corinium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-220.71,128.02),[], 40),            #[swycartographr] prev. coords: (-220.84, 123.8)
  ("village_178","Calleva",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-218.26,123.05),[], 40),             #[swycartographr] prev. coords: (-218.6, 117.3)
  ("village_179","Venta",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-197.77,138.02),[], 40),               #[swycartographr] prev. coords: (-204.26, 126.13)
  ("village_180","Moridunum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-234.82,133.05),[], 40),           #[swycartographr] prev. coords: (-235.5, 126.6)
  ("village_181","Tulisurgium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-137.46,129.85),[], 40),
  ("village_182","Munitium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-145.5,116.64),[], 40),             #[swycartographr] prev. coords: (-161.25, 110.78)
  ("village_183","Gravionarium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-133.73,107.23),[], 40),         #[swycartographr] prev. coords: (-157, 104.9)
  ("village_184","Segodunum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-140.61,97.88),[], 40),            #[swycartographr] prev. coords: (-162.3, 95.28)
  ("village_185","Arrabona",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-82.85,82.87),[], 40),              #[swycartographr] prev. coords: (-123.04, 76.7)

  ("village_186","Uscenum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-75.03,92.19),[], 40),               #[swycartographr] prev. coords: (-112.25, 82.85) #[swycartographr] prev. coords: (-68.81, 93.04)
  ("village_187","Tbilisi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(149.93,64.26),[], 40),               #[swycartographr] prev. coords: (65.5, 50.11)
  ("village_188","Tibiscum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.42,67.12),[], 40),              #[swycartographr] prev. coords: (-96.3, 57.3)
  ("village_189","Athribis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.3,-76.51),[], 40),              #[swycartographr] prev. coords: (-13.3, -82.7)

  ("village_190","Toronum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-199.33,80.66),[], 40),              #[swycartographr] prev. coords: (-213, 81.9)
  ("village_191","Augusta Ausciorum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-206.52,40.51),[], 40),    #[swycartographr] prev. coords: (-220.7, 39)
  ("village_192","Elusa",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-206.42,45.27),[], 40),                #[swycartographr] prev. coords: (-222.62, 44.4)
  ("village_193","Augustonemetum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-184.43,60.86),[], 40),       #[swycartographr] prev. coords: (-204, 56)
  #new villages 6/14/20
  #start off with new roman villages - wre first
  ("village_194","Rhegium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-90.24,-16.97),[], 40),              #[swycartographr] prev. coords: (-128.85, -19.1)
  ("village_195","Amiternum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-110.26,23.55),[], 40),            #[swycartographr] prev. coords: (-146.6, 20.62)
  ("village_196","Pisae",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-132.77,40.63),[], 40),                #[swycartographr] prev. coords: (-167.2, 34.4)
  ("village_197","Verona",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-129.36,58.9),[], 40),                #[swycartographr] prev. coords: (-159.34, 53.53)
  ("village_198","Domavium",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-74.85,47.36),[], 40),              #[swycartographr] prev. coords: (-110.5, 40.3)
  ("village_199","Narona",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-69.25,27.7),[], 40),                 #[swycartographr] prev. coords: (-117.9, 25.5)
  ("village_200","Alalie",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-143.37,18.17),[], 40),               #[swycartographr] prev. coords: (-175, 16.76)
  ("village_201","Philippi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.29,23.04),[], 40),              #[swycartographr] prev. coords: (-74.2, 14.5)
  ("village_202","Synnada",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39.66,4.76),[], 40), #taifals        #[swycartographr] prev. coords: (-26.3, 4)
  ("village_203","Attalia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33.22,-15.43),[], 40),               #[swycartographr] prev. coords: (-28, -22)
  ("village_204","Gortyna",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11.6,-39.21),[], 40),               #[swycartographr] prev. coords: (-66.3, -44.6)
  ("village_205","Nicomedia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.39,21.95),[], 40),              #[swycartographr] prev. coords: (-37.3, 19)
  ("village_206","Caesarea Eusebia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.45,16.2),[], 40),      #[swycartographr] prev. coords: (-2.36, 8.83) #[swycartographr] prev. coords: (-0.08, -30.24)
  ("village_207","Nicosia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(60.41,-25.45),[], 40),               #[swycartographr] prev. coords: (-8.45, -30.1)
  ("village_208","Palma",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-193.62,-1.82),[], 40),                #[swycartographr] prev. coords: (-217.4, 1.8)
  #frankish villages
  ("village_209","Levefanum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-176.02,124.43),[], 40),           #[swycartographr] prev. coords: (-186.82, 119.55)
  ("village_210","Virodunum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-164.47,98.43),[], 40),           #[swycartographr] prev. coords: (-184.2, 96.85) #[swycartographr] prev. coords: (-165.83, 101.59)
  ("village_211","Arae Flaviae",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-152.22,89.07),[], 40),         #[swycartographr] prev. coords: (-170.4, 85.3)
  #new desert villages - ere - vandals - mauri
  ("village_212","Memphis",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52.38,-85.43),[], 40),               #[swycartographr] prev. coords: (-15.7, -90.8)
  ("village_213","Cyrene",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.76,-72.71),[], 40),               #[swycartographr] prev. coords: (-82.2, -66.3)
  ("village_214","Augila",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.3,-99.45),[], 40),                #[swycartographr] prev. coords: (-87, -98.7)
  ("village_215","Syrorum",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-210.29,-50.53),[], 40),             #[swycartographr] prev. coords: (-240.6, -39.8)
  ("village_216","Cartena",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-206.79,-34.41),[], 40),             #[swycartographr] prev. coords: (-234.4, -26.2)
  ("village_217","Cesarea",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-195.15,-31.88),[], 40),             #[swycartographr] prev. coords: (-225.25, -26)
  ("village_218","Siga",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-231.09,-40.87),[], 40),                #[swycartographr] prev. coords: (-251.1, -32.7)
  ("village_219","Cirta",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-162.65,-40.04),[], 40),               #[swycartographr] prev. coords: (-197.01, -31.43)
  ("village_220","Rusaddir",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-247.91,-42.63),[], 40),            #[swycartographr] prev. coords: (-261.8, -30.7)
  ("village_221","Columnata",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-212.31,-41.15),[], 40),           #[swycartographr] prev. coords: (-237.6, -33.65)
  ("village_222","Arsennaria",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-214.29,-34.81),[], 40),          #[swycartographr] prev. coords: (-239, -28.6)
  ("village_223","Bararus",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-132.8,-51.85),[], 40),              #[swycartographr] prev. coords: (-166, -46.85)
  ("village_224","Thabrasa",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-146.48,-30.67),[], 40),            #[swycartographr] prev. coords: (-182.3, -29)
  #sad! no more desert villages!
  ("village_225","Arelate",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-177.92,41.23),[], 40),              #[swycartographr] prev. coords: (-197.5, 37.1)
  ("village_226","Asculum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-108.11,30.85),[], 40),              #[swycartographr] prev. coords: (-142.53, 27.13)
  ("village_227","Virunum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-98.28, 76.69),[], 40),              #[swycartographr] prev. coords: (-139.51, 63.27)
  #("village_228","Augustomagnus",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-202, 96),[], 40),
  ("village_228","Lindum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-205.47, 151.98),[], 40),             #[swycartographr] prev. coords: (-211.91, 143.4)
  #new villages 8/12/20 - huns in crimea and ukraine
  ("village_229","Theodosia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.88, 79.98),[], 342),            #[swycartographr] prev. coords: (-17.21, 70.05)
  ("village_230","Argedava",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18.39, 54.59),[], 40),             #[swycartographr] prev. coords: (-70.7, 50.63)
  ("village_231","Charax",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(38.06, 69.86),[], 40),                #[swycartographr] prev. coords: (-24.6, 64.08)
  ("village_232","Kalos Limen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.45, 78.56),[], 40), #was Naubarum (-20.5, 101.5) #[swycartographr] prev. coords: (-30.3, 69.65)
  ("village_233","Hermonassa",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(66.67, 80.73),[], 40),            #[swycartographr] prev. coords: (-5.16, 71.76)
  ("village_234","Tyras",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.18, 80.25),[], 40),                 #[swycartographr] prev. coords: (-48, 68.5) #[swycartographr] prev. coords: (11.55, 62.86)
  ("village_235","Tracana",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.77, 98.19),[], 40),               #[swycartographr] prev. coords: (-22.4, 85.2)
  ("village_236","Arargus",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(55.2, 105.99),[], 40),               #[swycartographr] prev. coords: (-12.72, 91)
  ("village_237","Ionopolis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.13, 35.7),[], 40),              #[swycartographr] prev. coords: (-21.15, 36)
  ("village_238","Gargaza",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.44, 88.23),[], 40),               #[swycartographr] prev. coords: (0.04, 76.77)
  ("village_239","Patria Onoguria",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.48, 108.14),[], 40),      #[swycartographr] prev. coords: (5, 93.6)
  #new villages 1/11/21
  ("village_240","Sala",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-283.45, -51.36),[], 40),               #[swycartographr] prev. coords: (-291.7, -34.1)
  ("village_241","Lixus",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-274.8, -42.1),[], 40),                #[swycartographr] prev. coords: (-284.4, -26.25)
  #new villages 3/12/21 - hispania
  ("village_242","Calagurris",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-238.43, 33.58),[], 40), 
  ("village_243","Saguntum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-220.41, 4.17),[], 40),             #[swycartographr] prev. coords: (-231.11, 10.44)
  ("village_244","Ilerda",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-215.74, 20.25),[], 40),              #[swycartographr] prev. coords: (-227.9, 26.45)
  ("village_245","Conimbriga",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-282.81, 22.01),[], 40),          #[swycartographr] prev. coords: (-287, 31.3)
  #anatolia
  ("village_246","Gangra",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(47.51, 19.97),[], 40),                #[swycartographr] prev. coords: (-14.07, 20.77)
  ("village_247","Cyzicus",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.27, 18.53),[], 40),                #[swycartographr] prev. coords: (-51, 9.4)
  ("village_248","Satala",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.82, 32.42),[], 40),              
  ("village_249","Sabastea",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(77.62, 23.33),[], 40),              #[swycartographr] prev. coords: (7, 18.6) #[swycartographr] prev. coords: (0.77, -27.52)
  ("village_250","Traianopolis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.2, 21.06),[], 40),           #[swycartographr] prev. coords: (-63.92, 15.25)

  ("village_251","Luxor",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.99, -126.66),[], 40),               #[swycartographr] prev. coords: (-4.84, -118.06)
  ("village_252","Aswan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(83.13, -138.56),[], 40),               #[swycartographr] prev. coords: (-7.3, -127.7)
  ("village_253","Silimi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89.1, -150.84),[], 40),               #[swycartographr] prev. coords: (-4.75, -141.3)
  #("village_254","Berenice",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.32, -104.72),[], 40),
  ("village_254","Oosook",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(113, -141.67),[], 40),                #[swycartographr] prev. coords: (36.4, -139)
  ("village_255","Ballana",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84.43, -142.87),[], 40),             #[swycartographr] prev. coords: (-7.5, -134.86)
  ("village_256","Philae",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89.73, -141.18),[], 40),              #[swycartographr] prev. coords: (-1.41, -130.2)
  #new villages 8/23/21
  ("village_257","Marubius",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(108.14,111.3),[], 40),              #[swycartographr] prev. coords: (38.2, 89.6)
  ("village_258","Suruba",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(92.3,102.59),[], 40),                 #[swycartographr] prev. coords: (15.61, 87)
  ("village_259","Udon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(116.99,100.8),[], 40),                  #[swycartographr] prev. coords: (47.26, 83.37)
  ("village_260","Ebriapa",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.3,89.79),[], 40),                #[swycartographr] prev. coords: (49, 74.29)
  ("village_261","Corusia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.3,92.62),[], 40),                 #[swycartographr] prev. coords: (28.7, 79.2)

  ("village_262","Resculum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.75, 82.1),[], 40), 
  ("village_263","Romula",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.13, 51.95),[], 40), 
  #new villages 11/13/22 - albania stronk
  ("village_264","Shaporan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(159.76, 75.11),[], 40), 
  ("village_265","Khorsan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(170.3, 63.12),[], 40), 



  ("salt_mine","Salt_Mine",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.2, -31),[]), #special locations
  ("diocletians_palace","Old Palace",icon_village_snow_a|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79.14, 34.56),[]), #[swycartographr] prev. coords: (-123.14, 29.53)

  ("four_ways_inn","Four_Ways_Inn",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.8, -39.6),[]),
  ("test_scene","test_scene",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  ("battlefields","battlefields",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -16.6),[]),
  ("dhorak_keep","Dhorak_Keep",icon_town|pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50,-58),[]),

  ("ruins_1","Ruins_of_Vimiacium",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50.72, 53.33),[]), 
  ("hidden_forest","Zamb",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(310.7,74.28),[]), 
  ("hidden_fort","Ruins",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_hunimund_suebi,0,ai_bhvr_hold,0,(-86.41,91.35),[]), 
  ("holy_lance_cave","Cave",pf_disabled|icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(78.77, -77.54),[]), 
  ("attila_sword_location","Grove",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.23, 70.09),[]), 
  ("waylands_smithy","Wayland's Smithy",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-224.17, 121.57),[]), 
  ("donar_forest","Forest",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.23,142.24),[]), 
  ("abandoned_mithraic_temple","Abandoned Antrum",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-136.05,60.09),[]), 
  ("nubian_bandit_camp","Bandit Encampment",pf_disabled|icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(96.18,-160.01),[]),
  ("vidigoias_grave","Vidigoia's Grave",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.84,68.9),[]), 
  ("bagadua_fort","Ruins of Iuliobriga",pf_disabled|pf_always_visible|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-227.66,29.15),[(trp_bagaudae_footman, 30, 0),(trp_forest_bandit, 20, 0),(trp_forest_bandit_recruit, 30, 0)]), 
  ("grove_of_nymphs","Grove of Nymphs",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.65,-19.97),[]), 
  ("sinuessa","Sinuessa",pf_disabled|icon_village_snow_burnt_a|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-107.04,14.81),[]), #roman_village_battle map 
  ("silingi_village","Vicus Silingorum",pf_disabled|icon_village_a|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.33,123.08),[]), 
  ("venedi_village_quest","Venedi Village",pf_disabled|icon_village_a|pf_always_visible|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-69.66,133.01),[]),  #for the quest
  ("agrippinus_quest_villa","Agrippinus's Villa",pf_disabled|pf_always_visible|icon_village_snow_a|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-182.33,88.54),[]), 
  ("court_of_attila","Attila's Court",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62.33, 88.26),[]), #sword of attila quest 
  ("noricum_refugee_camp","Refugee Camp",pf_disabled|icon_village_a|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-92.53, 83.47),[]), #severinus quest 
  ("sarmatian_camp","Campus_Sarmaticum",pf_disabled|icon_village_a|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-72.17, 84.19),[]), #hunimund quest 
  #ernak quest
  ("village_of_the_lekhs", "Village of the Lekhs", pf_disabled|icon_village_a|pf_is_static, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (138, 79.07), [(trp_lekh_warrior,150,0),(trp_lekh_retainer,50,0)]), #[swycartographr] prev. coords: (-6.56, 158.21) #[swycartographr] prev. coords: (159.15, 168.09)
  ("ruins_of_oplia_pontica", "Ruins of Olpia Pontica", pf_disabled|icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (13.93, 87.64), []), #[swycartographr] prev. coords: (-6.56, 158.21) #[swycartographr] prev. coords: (159.15, 168.09)
  ("camp_of_tatra", "Camp of Tatra", pf_disabled|icon_bandit_lair|pf_is_static, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (133.96, 156.33), [(trp_sabir_tatra, 1, 0),(trp_sabir_horse_archer,100,0),(trp_sabir_cataphract,50,0)]), #[swycartographr] prev. coords: (-6.56, 158.21) #[swycartographr] prev. coords: (159.15, 168.09)
  ("wolfmen_lair","Forest",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-80.6,127.09),[]),
  ("abandoned_silver_mine","Abandoned_Silver_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-253.03,38.97),[]), #hidden

  #("champion_lair","Forest_Hideout",pf_disabled|icon_castle_snow_b|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.58,-3.78),[]), #not used just yet

  # ("training_ground","Training Ground",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3, -7),[]),
  ("training_ground_1", "Training Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-103.4,17.24),[], 100), #roman, will be in italy?
  ("training_ground_2", "Training Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.79, 10.08),[], 100),
  ("training_ground_3", "Training Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-230.62, 72.0),[], 100), 
  ("training_ground_4", "Training Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.92, -85.79),[], 100),
  ("training_ground_5", "Training Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-146.43, 20.1),[], 100),


#  bridge_a
  # ("Bridge_1","{!}1",pf_disabled|icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-194.17, 65.10),[], 13),
  # ("Bridge_2","{!}2",pf_disabled|icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-158.5, 50.3),[], 85),
  # ("Bridge_3","{!}3",pf_disabled|icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-237.07, 31.02),[], 91),
  # ("Bridge_4","{!}4",pf_disabled|icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-161.16, 49.12),[], 353),
  # ("Bridge_5","{!}5",pf_disabled|icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-133.18, -83.02),[], 247),
  # ("Bridge_6","{!}6",pf_disabled|icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-94.23, 39.28),[], 257),
  # ("Bridge_7","{!}7",pf_disabled|icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-218.92, 80.25),[], 182),
  # ("Bridge_8","{!}8",pf_disabled|icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-195.15, 93.17),[], 114),
  # ("Bridge_9","{!}9",pf_disabled|icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-193.06, -9.60),[], 100),
  # ("Bridge_10","{!}10",pf_disabled|icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-116.6, 44.33),[], 267),
  # ("Bridge_11","{!}11",pf_disabled|icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.43, -81.26),[], 295),
  # ("Bridge_12","{!}12",pf_disabled|icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-154.13, 18.84),[], -35.5),
  # ("Bridge_13","{!}13",pf_disabled|icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-196.3, 39.45),[], 87),
  # ("Bridge_14","{!}14",pf_disabled|icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-273.26, 10.11),[], 88),

  ("looter_spawn_point"   ,"{!}looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(26, 77),[(trp_looter,15,0)]),
  ("steppe_bandit_spawn_point"  ,"the danube",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-76.42, 76.85),[(trp_looter,15,0)]), 
  ("taiga_bandit_spawn_point"   ,"germania",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-139.87, 126.39),[(trp_looter,15,0)]), 
  ("forest_bandit_spawn_point"  ,"gaul and hispania",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-232.77, 21.13),[(trp_looter,15,0)]), 
  ("mountain_bandit_spawn_point","the mountains",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(48.81,10.46),[(trp_looter,15,0)]), 
  ("desert_bandit_spawn_point"  ,"the desert",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-147.98, -59.72),[(trp_looter,15,0)]), 
  ("sea_raider_spawn_point_1"   ,"frisia",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-177.40, 128.56),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_2"   ,"britannia",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-206.12, 145.24),[(trp_looter,15,0)]), 
  ("sabir_bandit_spawn_point","the steppe",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(70.83,92.39),[(trp_looter,15,0)]),  
  ("armenian_rebel_spawn_point","armenia",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(128.46,50.49),[(trp_looter,15,0)]),  
  ("coptic_spawn_point"  ,"egypt",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(57.36, -80.69),[(trp_looter,15,0)]),         
  ("arab_bandit_spawn_point"  ,"the desert",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(118.23, -33.87),[(trp_looter,15,0)]), 
 # add extra towns before this point 
  ("spawn_points_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),

  ("pirate_spawn_point"  ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-87.38, -1.83),[(trp_looter,15,0)]),     
  ("scirii_spawn_point"  ,"the danube",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-93.86, 92.58),[(trp_looter,15,0)]),    
  ("heruli_spawn_point"  ,"germania",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-118.47, 103.51),[(trp_looter,15,0)]),    

  ("reserved_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_2"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),

  ("freelancer_party_backup","{!}",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  #minor faction villages
  ("aestii_village", "Fort_of_the_Bull", icon_castle_b|pf_minor_town, no_menu, pt_none, fac_minor_aestii, 0, ai_bhvr_hold, 0, (-51.63, 186.34), []),
  ("irish_village", "Rath_Celtchair", icon_village_a|pf_minor_town, no_menu, pt_none, fac_minor_irish, 0, ai_bhvr_hold, 0, (-242.78, 155.39), []), 
  ("garamantian_village_1", "Garama", icon_village_c|pf_minor_town, no_menu, pt_none, fac_minor_garamantians, 0, ai_bhvr_hold, 0, (-108.72, -112.92), []), 
  ("dani_village", "Heorot", icon_village_a|pf_minor_town, no_menu, pt_none, fac_minor_dani, 0, ai_bhvr_hold, 0, (-126.88, 167.08), []),  
  ("morden_village", "Terekh's_Hall", icon_castle_b|pf_minor_town, no_menu, pt_none, fac_minor_mordens, 0, ai_bhvr_hold, 0, (36.85, 160.96), []), 
  ("sporoi_village", "Niossus", icon_village_a|pf_minor_town, no_menu, pt_none, fac_minor_sporoi, 0, ai_bhvr_hold, 0, (3.06, 121.46), []),  
  ("bosphoran_village", "Panticapaeum", icon_castle_a|pf_minor_town, no_menu, pt_none, fac_minor_bosphoran, 0, ai_bhvr_hold, 0, (54.96, 84.42), []),
  ("abagasian_village", "Anakopia", icon_castle_a|pf_minor_town, no_menu, pt_none, fac_minor_abagasians, 0, ai_bhvr_hold, 0, (85.78,73.74), []),  
  ("tauri_village", "Vicus_Taurorum", icon_village_a|pf_minor_town, no_menu, pt_none, fac_minor_tauri, 0, ai_bhvr_hold, 0, (45.09, 77.36), []),
  ("augundzi_village", "Vicus_Augandzorum", icon_village_a|pf_minor_town, no_menu, pt_none, fac_minor_augundzi, 0, ai_bhvr_hold, 0, (-163.96, 198.3), []), 
  ("vidivarii_village", "Truso", icon_village_a|pf_minor_town, no_menu, pt_none, fac_minor_vidivarii, 0, ai_bhvr_hold, 0, (-79.94, 152), []), 
  ("frisian_village", "Finn's Hall", icon_village_a|pf_minor_town, no_menu, pt_none, fac_minor_frisians, 0, ai_bhvr_hold, 0, (-174.68, 135.89), []), 
  ("vascones_village", "Flaviobriga", icon_castle_a|pf_minor_town, no_menu, pt_none, fac_minor_vascones, 0, ai_bhvr_hold, 0, (-243.57, 43.55), []),
  ("gallaeci_village", "Lucus_Augusti", icon_castle_a|pf_minor_town, no_menu, pt_none, fac_minor_gallaeci, 0, ai_bhvr_hold, 0, (-267.49,42.04), []),
  ("venedi_village", "Dunepru", icon_village_a|pf_minor_town, no_menu, pt_none, fac_minor_venedi, 0, ai_bhvr_hold, 0, (-6.4, 159.72), []),   #[swycartographr] prev. coords: (-6.56, 158.21)
  ("onoguroi_village", "Campus Onogurorum", icon_village_a|pf_minor_town, no_menu, pt_none, fac_minor_onoguroi, 0, ai_bhvr_hold, 0, (111.7, 126.6), []), #[swycartographr] prev. coords: (-6.56, 158.21)
  ("saraguroi_village", "Campus Saragurorum", icon_village_a|pf_minor_town, no_menu, pt_none, fac_minor_saraguroi, 0, ai_bhvr_hold, 0, (98.2, 154.34), []), #[swycartographr] prev. coords: (-6.56, 158.21)
  ("kutriguroi_village", "Campus Kutrigurorum", icon_village_a|pf_minor_town, no_menu, pt_none, fac_minor_kutriguroi, 0, ai_bhvr_hold, 0, (55.04, 132.01), []), #[swycartographr] prev. coords: (-6.56, 158.21)
  ("sabiroi_village", "Campus Sabirorum", icon_village_a|pf_minor_town, no_menu, pt_none, fac_minor_sabiroi, 0, ai_bhvr_hold, 0, (159.15, 168.09), []), #[swycartographr] prev. coords: (-6.56, 158.21)
  #minor faction villages

  ("religious_site_1","Batavis",icon_castle_snow_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-107.97, 87.93),[]), #roman 
  ("religious_site_2","Monastery_of_Stavrovouni",icon_castle_snow_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.4,-32.38),[]), #roman 
  ("religious_site_3","Monastery_of_Mor_Gabriel",icon_castle_snow_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(91.22,9.02),[]), #roman 
  ("religious_site_4","Monastery_of_Saint_Anthony",icon_castle_snow_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(60.98,-97.53),[]), #coptic 
  ("religious_site_5","Arian_Monastery",icon_castle_snow_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-212.02,49.17),[]), #arian 
  ("religious_site_6","Arian_Monastery",icon_castle_snow_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-137.79,-40.93),[]), #arian 
  ("religious_site_7","Grove_of_Nerthus",icon_castle_snow_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-128.07,163.56),[]), #germanic pagan 
  ("religious_site_8","Donar's_Oak",icon_castle_snow_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-138.54,105.63),[]), #germanic pagan 
  ("religious_site_9","Aphrodisias",icon_castle_snow_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.25,-3.84),[]), #greco-roman paganism 
  ("religious_site_10","Great_Fire_of_Adur_Farnbag",icon_castle_snow_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(236.84,-39.66),[]), #zoroastrian 
  ("religious_site_11","Great_Fire_of_Adur_Gushnap",icon_castle_snow_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(138.16,51.05),[]), #zoroastrian 
  ("religious_site_12","Monastery_of_Saint_Athanasius",icon_castle_snow_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11.7, 47.01),[]), #roman 
  ("religious_site_13","Paromeos_Monastary",icon_castle_snow_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.91, -77.41),[]), #coptic 
  ("religious_site_14","Irminsul",icon_castle_snow_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-156.34,132.32),[]), #pagan 
  ("religious_site_15","Monastery_of_Lerina",icon_castle_snow_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-165.82,36.74),[]), #roman 
  ("religious_site_16","Monastery_of_Saint_Martin",icon_castle_snow_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-210.1,72.77),[]), #roman 
  ("religious_site_17","Stone_Circle",icon_castle_snow_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-222.81,139.23),[]), #celtic pagan 
  ("religious_site_18","Altar_to_the_Skyfather",icon_castle_snow_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(45.91, 112),[]), #shamanism
  ("religious_site_19","Siwa",icon_castle_snow_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.77, -104.82),[]), #egyptian paganism

  #siwa - for roman pagans (egyptian)
  #?? for pagans in the steppes
  
  #animal spawns
  ("deer_spawn_point" ,"the wilderness",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-143.69,109.36),[]), 
  ("boar_spawn_point" ,"the wilderness",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-185.14,75.49),[]), 

  ]
