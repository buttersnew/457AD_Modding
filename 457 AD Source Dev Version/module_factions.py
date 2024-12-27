from header_factions import *

from compiler import *
####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.02),("forest_bandits", -0.02)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0x888888),
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),

  #("dark_knights","Slavic Invasion", 0, 0.5,[("innocents",-0.9),("player_faction",-0.4)], []),

  ("culture_1",  "Gothic", 0, 0.9, [], []),
  ("culture_2",  "Eastern Germanic", 0, 0.9, [], []),
  ("culture_3",  "Romano-Briton", 0, 0.9, [], []),
  ("culture_4",  "Northern Germanic", 0, 0.9, [], []),
  ("culture_5",  "Pictish", 0, 0.9, [], []),
  ("culture_6",  "Persian", 0, 0.9, [], []),
  ("culture_empire",  "Roman", 0, 0.9, [], []),
  ("culture_7",  "Western Germanic", 0, 0.9, [], []),
  ("culture_8",  "Caucasian", 0, 0.9, [], []),
  ("culture_11",  "Romano-Mauri", 0, 0.9, [], []),
  ("culture_12",  "Hunnic", 0, 0.9, [], []),
  ("culture_15",  "Nubian", 0, 0.9, [], []),
  ("culture_16",  "Caucasian Alan", 0, 0.9, [], []),
  #minor cultures
  ("culture_minor_1",  "Hispano-Roman", 0, 0.9, [], []),
  ("culture_minor_2",  "Slavic", 0, 0.9, [], []),
  ("culture_minor_3",  "Coptic", 0, 0.9, [], []),
  ("culture_minor_4",  "Frisian", 0, 0.9, [], []),
  ("culture_minor_5",  "Baltic", 0, 0.9, [], []),
  ("culture_minor_6",  "Morden", 0, 0.9, [], []),
  ("culture_minor_7",  "Scandzae", 0, 0.9, [], []),
  ("culture_minor_8",  "Tetraxitae Gothic", 0, 0.9, [], []),
  ("culture_minor_9",  "Western Alan", 0, 0.9, [], []),
  ("culture_minor_10",  "Iazyg", 0, 0.9, [], []),

  ("player_faction","Player Faction",0, 0.9, [], []),
  ("player_supporters_faction","Player's Supporters",0, 0.9, [("player_faction",1.00),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("coptic_rebels", -0.05),("berber_rebels", -0.05),("armenian_rebels", -0.05)], [], 0xFF4433), #changed name so that can tell difference if shows up on map

  ("kingdom_1",  "Imperium Romanum Pars Occidentalis", 0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.75),("coptic_rebels", -0.05),("minor_vascones", 0.5),("minor_gallaeci", 0.5)], [], 0x8E0D0D), #Western Roman Empire / Imperium Romanum Pars Occidentalis // Friendly with ERE and Salian franks to start
  ("kingdom_2",  "Imperium Romanum Pars Orientalis",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.75),("coptic_rebels", -0.75)], [], 0x9B3CDB), #Eastern Roman Empire / Imperium Romanum Pars Orientalis // Friendly to WRE and Lazika to start
  ("kingdom_3",  "Regnum Balthorum", 0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0x3b4192), #Kingdom of the Visigoths / Regnum Visigothorum 65563F
  ("kingdom_4",  "Regnum Amalorum",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0x6ea6ce), #Kingdom of the Ostrogoths / Regnum Ostrogothi - changed to Regnum Amalorum, Kingdom of the Amali (dynasty) goths
  ("kingdom_5",  "Regnum Picti",  0, 0.9, [("saxons", 0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0x667FFF), #Kingdom of the Picts / Regnum Picti
  ("kingdom_6",  "Eranshahr",  0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0xfe6f20), #Sassanid Empire / Eranshahr
  ("kingdom_7",  "Regnum Salii",  0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0x2A8000), #Kingdom of the Salian Franks / Regnum Salii
  ("kingdom_8",  "Regnum Suevorum",  0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("minor_gallaeci", -0.5)], [], 0x65cd65), #Kingdom of the Suebi / Regnum Suevorum
  ("kingdom_9",  "Regnum Burgundionum",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0xb3636e), #Kingdom of the Burgundians / Regnum Burgundionum
  ("kingdom_10",  "Regnum Alemmani",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0xbd832f), #Kingdom of the Alemmani / Regnum Alemmani
  ("kingdom_11",  "Regnum Gepidae",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0x904659), #Kingdom of the Gepids / Regnum Gepidae 904659
  ("kingdom_12",  "Regnum Saxones",    0, 0.9, [("saxons", 0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0x4f6e45), #Kingdom of the Saxons / Regnum Saxones 0xf93504
  ("kingdom_13",  "Regnum Britannorum",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("minor_irish", -0.7)], [], 0xab4343), #Romano-Britons / Regnum Britannorum
  ("kingdom_14",  "Regnum Rugurum",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0x4e5f89), #Kingdom of the Rugii / Regnum Rugurum 65cd65
  ("kingdom_15",  "Regnum Vandalorum et Alanorum",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.75),("coptic_rebels", -0.05)], [], 0xd5d6b4), #Kingdom of the Vandals / Regnum Vandalorum et Alanorum
  ("kingdom_16",  "Kartli",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0x0c42c4), #Kartli / Kingdom of Iberia
  ("kingdom_17",  "Regnum Langobardi",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0x5f252e), #Kingdom of the Langobards / Regnum Langobardi 910c21
  ("kingdom_18",  "Regnum Thuringii",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0x5b4d4f), #Kingdom of the Thuringians / Regnum Thuringii
  ("kingdom_19",  "Regnum Iuti",    0, 0.9, [("saxons", 0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0x353c4c), #Kingdom of the Jutes / Regnum Iuti
  ("kingdom_20",  "Regnum Ripuarii",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0x587f95), #Kingdom of the Ripuarian Franks / Regnum Ripuarii
  ("kingdom_21",  "Regnum Scirii",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0x265626), #Kingdom of the Scirii / Regnum Scirii # was 0x103210
  ("kingdom_22",  "Provincia Mauretania",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", 0.05)], [], 0xd33434), #Kingdom of the Mauri and the Romans / Regnum Maurorum Et Romanorum 0x80FF00
  ("kingdom_23",  "Hunni",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0xCC9966), #Hunni / Huns
  ("kingdom_24",  "Lazika-Egrisi",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0x2d7b34), #Kingdom of Lazika / Lazika-Egrisi
  ("kingdom_25",  "Nobadia",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("coptic_rebels", 0.05)], [], 0x1b3159), #Kingdom of Nobatia / Nobadia
  ("kingdom_26",  "Blemmyae",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("coptic_rebels", 0.05)], [], 0xae5b14), #Kingdom of the Blemmyes / Blemmyae #0x947b15
  ("kingdom_27",  "Alania",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x947b15), #Kingdom of the Alans / Alania #0xae5b14
  ("kingdom_28",  "Arran",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0x1e817f),
  ("kingdom_29",  "Regnum Anglii",    0, 0.9, [("saxons", 0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0x583b37), #Kingdom of the Jutes / Regnum Iuti
  ("kingdom_30",  "Framta's Suebi",  0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("minor_gallaeci", -0.5)], [], 0xDECB4F),

#madsci Spanish rebel factions, will be renamed automatically by a script depending on where they start
  ("rebel_kingdom_1",  "Rebels",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0x7d2439), #7d2439
  ("rebel_kingdom_2",  "Rebels",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0x622228),
  ("rebel_kingdom_3",  "Rebels",    0, 0.9, [("saxons", -0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05)], [], 0x741f1a),

  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),

  ("robber_knights",  "{!}robber_knights", 0, 0.1, [], []),
  #("khergits","{!}Khergits", 0, 0.5,[("player_faction",0.0)], []),
  #("black_khergits","Hunnic Rebels", 0, 0.5,[("player_faction",-0.3),("kingdom_1",-0.05),("kingdom_2",-0.05),("kingdom_4",-0.05),("kingdom_11",-0.05)], []),
  #("rebel_peasants","Rebel Peasants", 0, 0.5,[("vaegirs",-0.5),("player_faction",0.0)], []),

  ("manhunters","Slavers", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1)], []),
  ("deserters","Deserters", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0x888888),
  ("mountain_bandits","Isaurians", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.05),("kingdom_2",-0.01)], [], 0x888888), #updated faction color 0x033677
  ("forest_bandits","Bagaudae", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15),("kingdom_1",-0.75),("kingdom_3",-0.75),("kingdom_8",0.5)], [], 0x888888),
  ("undeads","{!}Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","{!}Slavers", 0, 0.1, [], []),
  ("peasant_rebels","Rebels", 0, 1.0,[("kingdom_1",-0.4),("kingdom_2",-0.4)], [], 0x5c2222), #used for roman rebels
  ("noble_refugees","{!}Noble Refugees", 0, 0.5,[], []),
  #new bandit faction, based on berber rebels (laguatan) who fought against the Romans + Vandals in the 4th - 6th centuries. Went under the label of Austuriani
  ("berber_rebels","Austuriani", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15),("kingdom_1",-0.5),("kingdom_2",-0.5),("kingdom_15",-1),("kingdom_22",0.75)], [], 0x888888), #0x3db8ca
  #coptic rebels
  ("coptic_rebels","Coptic Rebels", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15),("kingdom_1",-0.75),("kingdom_2",-0.75),("kingdom_6",-0.5),("coptic_christians",0.75),("armenian_rebels",0.75)], [], 0x888888), #0x2f3968
  #armenian rebels
  ("armenian_rebels","Armenian Rebels", 0, 0.5,[("commoners",-0.05),("merchants",-0.5),("player_faction",-0.05),("kingdom_6",-0.75),("kingdom_2",0.75),("kingdom_16",0.5),("coptic_christians",0.75),("coptic_christians",0.75)], [], 0x888888),
  #Samaritan rebels - revolted in 484 under Zeno, may add them as a small rebel faction?
  ("samaritan_rebels","Samaritan Rebels", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15),("kingdom_1",-0.75),("kingdom_2",-0.75),("kingdom_6",-0.5),("jews",0.75)], [], 0x888888),
  #saxon raider
  ("saxons","Saxon Raiders", 0, 0.5,[("commoners",0.1),("merchants",0.1),("manhunters",-0.2),("player_faction",-0.05),("player_supporters_faction",-0.05)], [], 0x888888),
  #suebi civil war
  #starts at war with the ostrogothic kingdom, will be spawned in an event war with scirii, rugii, heruli + suebi vs ostrogoths
  ("hunimund_suebi","Danubian Suebi", 0, 0.5,[("kingdom_4",-0.75),("kingdom_11",0.99),("kingdom_14",0.99),("kingdom_21",0.99)], [], 0x3c5a1b), #lead by hunimund, at war with ostrogoths, will make color orange
  ("faltras_suebi","Faltras's Loyalists", 0, 0.5,[("kingdom_8",-0.75)], [], 0x3c5a1b),

  #Minor faction features
  #Unique merchant with unique goods
  #Player can give gifts (of gold) to increase relation to unique hire troops
  #Player can attack settlement to get access to troops, minor faction becomes tributary of player
  #Unique quests?
  #Unique flavor dialogue about the minor faction/culture
  #minor factions start
  ("minor_aestii","Aestii", 0, 0.9,[("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6),("minor_vidivarii",-0.5)], [], 0x713735),
  ("minor_irish","Scoti", 0, 0.9,[("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6),("kingdom_13", -0.7),("kingdom_5",-0.75),("kingdom_19",-0.75),("kingdom_29",-0.75),("kingdom_12",-0.75),("kingdom_1",-0.75)], [], 0x395035),
  ("minor_garamantians","Garamantians", 0, 0.9,[("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", 0.5),("coptic_rebels", -0.05),("manhunters",0.6),("kingdom_15",-0.75),("kingdom_1",-0.75)], [], 0xc87b50),
  ("minor_dani","Danir", 0, 0.9,[("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6),("kingdom_19",-0.75),("minor_augundzi",-0.75)], [], 0x993322),
  ("minor_mordens","Mordens", 0, 0.9,[("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6)], [], 0x65563F),
  ("minor_sporoi","Sporoi", 0, 0.9,[("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6),("minor_saraguroi",-0.75),("minor_kutriguroi",-0.75),("minor_sabiroi",-0.75),("minor_onoguroi",-0.75),("minor_iazyges",-0.75),("kingdom_23",-0.75),("kingdom_11",-0.75)], [], 0xFFFFFF),
  ("minor_bosphoran","Basileion tou Bosporou", 0, 0.9,[("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6),("kingdom_23", 0.9)], [], 0x3852B0),
  ("minor_abagasians","Abasgoi", 0, 0.9,[("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6),("kingdom_24", 0.9)], [], 0x20553D),
  ("minor_tauri","Tauri", 0, 0.9,[("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6),("kingdom_2", 0.9)], [], 0xABD4FF),
  ("minor_augundzi","Augandzi", 0, 0.9,[("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6),("minor_dani",-0.75)], [], 0x2c2c2c),
  ("minor_vidivarii","Vidivarii", 0, 0.9,[("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6),("minor_aestii",-0.75)], [], 0x7ed2da),
  ("minor_frisians","Frisii", 0, 0.9,[("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6),("kingdom_13",-0.75)], [], 0xc26a3a),
  ("minor_vascones","Vascones", 0, 0.9,[("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", 0.5),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6),("kingdom_3",-0.75),("kingdom_8",-0.75)], [], 0x2f0a0a),
  ("minor_gallaeci","Gallaeci", 0, 0.9,[("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", 0.5),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6),("kingdom_3",-0.75),("kingdom_8",-0.75)], [], 0x009acd),
  ("minor_venedi","Venedi", 0, 0.9,[("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6),("kingdom_23",-0.75),("minor_saraguroi",-0.75),("minor_onoguroi",-0.75),("minor_kutriguroi",-0.75),("minor_sabiroi",-0.75)], [], 0xc19135),
  ("minor_saraguroi","Saraguroi", 0, 0.9,[("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6),("kingdom_23",-0.75),("kingdom_27",-0.75)], [], 0xc19135),
  ("minor_onoguroi","Onoguroi", 0, 0.9,[("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6)], [], 0xc19135),
  ("minor_kutriguroi","Kutriguroi", 0, 0.9,[("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6)], [], 0xc19135),
  ("minor_sabiroi","Sabiroi", 0, 0.9,[("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6),("minor_kutriguroi",-0.75),("minor_onoguroi",-0.75),("minor_saraguroi",-0.75),], [], 0xc19135),
  ("minor_valentia","Valentia Alanorum", 0, 0.9,[("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6),("kingdom_1", 0.5)], [], 0x71253c),
  ("minor_aurelianorum","Aurelianorum Alanorum", 0, 0.9,[("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6),("kingdom_1", 0.5),("kingdom_3",-0.75),], [], 0x7d2828),
  ("minor_iazyges","Iazyges", 0, 0.9,[("kingdom_4",-0.75),("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6)], [], 0xc19135),
  ("minor_heruli","Heruli", 0, 0.5,[("kingdom_4",-0.75),("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6)], [], 0x993322), #lead by Visilaus, at war with ostrogoths
  ("adovacrius_host","Adovacrius_Host", 0, 0.9,[("kingdom_1",-0.75),("kingdom_3",-0.75),("kingdom_7",-0.75),("outlaws",-0.75),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("berber_rebels", -0.05),("coptic_rebels", -0.05),("manhunters",0.6)], [], 0xc19135),
  ("minor_factions_end",  "{!}minor_factions_end", 0, 0.9, [], []),

  #religions
  ("roman_christians","Chalcedonian Christians", 0, 0.5,[("arian_christians",-0.05),("coptic_christians",-0.05),("nestorian_christians",-0.05),("donatist_christians",-0.05),("kingdom_1", 0.9),("kingdom_2", 0.9)], [], 0xFFFFFF), #very friendly with the romans
  ("arian_christians","Arian Christians", 0, 0.5,[("roman_christians",-0.05),("coptic_christians",-0.05),("nestorian_christians",-0.05),("donatist_christians",-0.05)], [], 0xFFFFFF),
  ("coptic_christians","Miaphysite Christians", 0, 0.5,[("arian_christians",-0.05),("roman_christians",-0.05),("nestorian_christians",-0.05),("donatist_christians",-0.05)], [], 0xFFFFFF),
  ("nestorian_christians","Nestorian Christians", 0, 0.5,[("arian_christians",-0.05),("roman_christians",-0.05),("coptic_christians",-0.05),("donatist_christians",-0.05)], [], 0xFFFFFF),
  ("donatist_christians","Donatist Christians", 0, 0.5,[("arian_christians",-0.05),("roman_christians",-0.05),("nestorian_christians",-0.05),("coptic_christians",-0.05)], [], 0xFFFFFF),
  ("pagans","Pagans", 0, 0.5,[], [], 0xFFFFFF), #neutral on other religions
  ("roman_pagans","Greco-Roman Pagans", 0, 0.5,[("roman_christians",-0.05),("kingdom_1", 0.1),("kingdom_2", -0.01)], [], 0xFFFFFF), #likes wre, dislikes ere
  ("zoroastrians","Mazdaist Zoroastrians", 0, 0.5,[("kingdom_6", 0.9)], [], 0xFFFFFF), #very friendly with the sassanids
  ("zurvanism","Zurvanite Zoroastrians", 0, 0.5,[("kingdom_6", 0.9)], [], 0xFFFFFF), #very friendly with the sassanids
  ("jews","Jews", 0, 0.5,[("arian_christians",-0.05),("coptic_christians",-0.05),("roman_christians",-0.05),("nestorian_christians",-0.05),("donatist_christians",-0.05),("pagans",-0.05),("roman_pagans",-0.05),("zoroastrians",-0.05)], [], 0xFFFFFF), #used for later
  ("religion_end","Religions End", 0, 0.5,[], [], 0xFFFFFF), 

  #chariot racing teams
  ("blue_team","Blues",0, 0.1,[("player_faction",0.0),("kingdom_1",0.5),("kingdom_2",0.5)], [],0x0c42c4),
  ("green_team","Greens",0, 0.1,[("player_faction",0.0),("kingdom_1",0.5),("kingdom_2",0.5)], [],0x2d7b34),
  ("red_team","Reds",0, 0.1,[("player_faction",0.0),("kingdom_1",0.5),("kingdom_2",0.5)], [],0x8E0D0D),
  ("white_team","Whites",0, 0.1,[("player_faction",0.0),("kingdom_1",0.5),("kingdom_2",0.5)], [],0xFFFFFF),

]

##diplomacy start+ Define these for convenience
dplmc_factions_begin = 1 #As mentioned in the notes above, this is hardcoded and shouldn't be altered.  Deliberately excludes "no faction".
dplmc_non_generic_factions_begin = [x[0] for x in enumerate(factions) if x[1][0] == "merchants"][0] + 1
dplmc_factions_end   = len(factions)
##diplomacy end+
