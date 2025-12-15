from header_common import *
from header_operations import *
from header_triggers import *
from header_scenes import *
from module_constants import *

from compiler import *
####################################################################################################################
#  Each scene record contains the following fields:
#  1) Scene id {string}: used for referencing scenes in other files. The prefix scn_ is automatically added before each scene-id.
#  2) Scene flags {int}. See header_scenes.py for a list of available flags
#  3) Mesh name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  4) Body name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  5) Min-pos {(float,float)}: minimum (x,y) coordinate. Player can't move beyond this limit.
#  6) Max-pos {(float,float)}: maximum (x,y) coordinate. Player can't move beyond this limit.
#  7) Water-level {float}.
#  8) Terrain code {string}: You can obtain the terrain code by copying it from the terrain generator screen
#  9) List of other scenes accessible from this scene {list of strings}.
#     (deprecated. This will probably be removed in future versions of the module system)
#     (In the new system passages are used to travel between scenes and
#     the passage's variation-no is used to select the game menu item that the passage leads to.)
# 10) List of chest-troops used in this scene {list of strings}. You can access chests by placing them in edit mode.
#     The chest's variation-no is used with this list for selecting which troop's inventory it will access.

####################################################################################################################

scenes = [
  ("random_scene",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000133e00907000d234800004364000070f200007f8f",
    [],[]),
  ("conversation_scene",0,"encounter_spot", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("water",0,"none", "none", (-1000,-1000),(1000,1000),-0.5,"0",
    [],[]),

  ("scene_sea",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x0000000350114b8000098a5d0000358380001fde0000108b",
    [],[], "sea_outer_terrain_2"),

  ("random_scene_steppe",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(100,100),-0.5,"0x0000000229602800000691a400003efe00004b34000059be",
    [],[], "outer_terrain_steppe"),
  ("random_scene_plain",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(100,100),-0.5,"0x0000000229602800000691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(100,100),-0.5,"0x0000000229602800000691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("random_scene_desert",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(100,100),-0.5,"0x0000000229602800000691a400003efe00004b34000059be",
    [],[], "outer_terrain_desert_b"),
  ("random_scene_steppe_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(100,100),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(100,100),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(100,100),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("random_scene_desert_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(100,100),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_desert"),
  ("camp_scene",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(100,100),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("camp_scene_horse_track",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(100,100),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  #new battle scenes begin
  ### We divide the map into regions:
  # # 1) Spain
  # # 2) North Africa,
  # # 3) South Italy and Greece
  # # 4) Nile
  # # 5) Syria and Palestine
  # # 6) Anatolia central
  # # 7) Anatolia coastal
  # # 8) Mesopotamia
  # # 9) Persian hill lands (green)
  # # 10) Persian hill lands (desert)
  # # 11) Caucasus

  ("battle_scene_snow_1",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x0000000048e00980000705c100004a17000017c400007b30",
    [],[], "outer_terrain_plain"),
  ("battle_scene_snow_2",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x000000004c600980000705c1000030e3000002bc000068f5",
    [],[], "outer_terrain_plain"),

  ("random_scene_snow_custom_1",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x00000000468005e3000d234800004470000067d500004470",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow_custom_2",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x0000000041c005e3000d234800004470000067d500002885",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow_custom_3",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x00000000426005e3000d234800004470000067d5000055c9",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow_custom_4",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x00000000426005e3000d23480000057f000067d500007ecc",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow_custom_5",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x0000000043e005e3000d23480000057f000067d50000660b",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow_custom_6",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x000000004c6005e3800d23480000057f0000403d00004af3",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow_custom_7",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x0000000044e005e3800d23480000057f000000db00005e1b",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow_custom_8",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x0000000044e005e3000d23480000590a000000db0000455e",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow_custom_9",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x00000000482005e3000d23480000590a000000db0000229b",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow_custom_10",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x000000004c600563000d23480000590a000000db00006bd5",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow_custom_11",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x000000004c600ae3000d23480000590a000000db00006e4b",
    [],[], "outer_terrain_plain"),

  ("random_scene_snow_forest_custom_1",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x00000000cc600ae3000d23480000590a000000db00006e4b",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow_forest_custom_2",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x00000000cc600563000d2348000037cc000000db000045f6",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow_forest_custom_3",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x00000000cc600563000d234800001ea3000000db000027bb",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow_forest_custom_4",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x00000000cc600563000d234800005cfa000000db000017fb",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow_forest_custom_5",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x00000000cc600563000d234800007432000000db00002d7c",
    [],[], "outer_terrain_plain"),

  #new custom battle maps
 ("custom_battle_plains_1",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x00000000300012e30007c5f1000036660000112a00006486", [],[], "outer_terrain_plain"), #valley 1 forest/plains
 ("custom_battle_plains_2",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x0000000030000763000785e300004b920000090a0000418d", [],[], "outer_terrain_plain"), #river 1 plains
 ("custom_battle_plains_3",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x00000000300007630007bdf1000020360000064a00007b83", [],[], "outer_terrain_plain"), #hills 1 forest/plains
 ("custom_battle_plains_4",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x0000000130000d6300093e4f00006024000006620000100a", [],[], "outer_terrain_plain"), #hills 2 forest/plains
 ("custom_battle_plains_5",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x00000000300005000007b5ed0000750f000056d900005a07", [],[], "outer_terrain_plain"), #river 2 plains
 ("custom_battle_plains_6",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x000000023c604780000b72df00000b7c00003503000067fc", [],[], "outer_terrain_plain"), #hills 3 forest/plains
 ("custom_battle_plains_7",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x0000000231000580000c0b0500006b520000720600007ff0", [],[], "outer_terrain_plain"), #plains

 ("custom_battle_forest_1",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x00000001bc61cee200093e53000056430000221c0000208f", [],[], "outer_terrain_plain"), #hills 1 forest
 ("custom_battle_forest_2",sf_generate,"none", "none", (0,0),(250,250),-0.5,"0x00000000300005800007c9f4000040a10000421300000192", [],[], "outer_terrain_plain"), #flat forest
 ("custom_battle_forest_3",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x00000000300005800007c9f4000040a10000421300000192", [],[], "outer_terrain_plain"), #river - plains/forest
 ("custom_battle_forest_4",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x00000002bc6088e28009be7900000a740000455f00003f08", [],[], "outer_terrain_plain"), #river - forest

 ("custom_battle_swamp_1",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-0.5,"0x00000000300005000007bdef0000750f000056d900005a07", [],[], "outer_terrain_plain"), #plains
 ("custom_battle_swamp_2",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-0.5,"0x00000000300005000007bdef0000750f000056d900005a07", [],[], "outer_terrain_forest"), #forest

#from maxi
  ("random_scene_new_steppe_custom_1", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220200500000afebf0000381400001e040000112d",[], [], "outer_terrain_steppe"),
  ("random_scene_new_steppe_custom_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220600500000afebf00004d66000013330000593c",[], [], "outer_terrain_steppe"),
  ("random_scene_new_steppe_custom_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220000500000afebf000074e00000524c00002aec",[], [], "outer_terrain_steppe"),
  ("random_scene_new_steppe_custom_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220800500000afebf00001e120000059000005a37",[], [], "outer_terrain_steppe"),
  ("random_scene_new_steppe_custom_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220400500000afebf00002440000051c60000229d",[], [], "outer_terrain_steppe"),
  ("random_scene_new_steppe_custom_6", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220000500000afebf0000376a00002c26000018f6",[], [], "outer_terrain_steppe"),
  ("random_scene_new_steppe_custom_7", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220600500000afebf000002bc000075c0000003db",[], [], "outer_terrain_steppe"),
  ("random_scene_new_steppe_custom_8", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220600500000afebf00006bc9000047da000060aa",[], [], "outer_terrain_steppe"),
  ("random_scene_new_steppe_custom_9", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220200500000afebf000058250000326800001a29",[], [], "outer_terrain_steppe"),
  ("random_scene_new_steppe_custom_10", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220000500000afebf00005f9600004b2f000073b3",[], [], "outer_terrain_steppe"),

  ("random_scene_plain_custom_1", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000023a00096300098a63000005d6000038400000015e",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000023240096300098a63000008610000085300002096",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002324007e300098a63000026700000795a000021ad",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002324007e300098a6300002742000011ff00007b9a",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002324007e300098a6300006db90000329e000074ed",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_6", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000023280086300098a6300001e9000000b2000006c18",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_7", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000233a0086300098a63000025b70000051200007f9d",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_8", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000233a0056300098a6300002c0c00003cd00000025e",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_9", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000235c008e300098a6300003d0900001f2600000f9c",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_10", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002314008e300098a6300005d7100001aac00005cb6",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_11", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002314008e300098a63000023c700000cd500007908",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_12", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002314008e300098a630000278100006dbb00004d39",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_13", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000232e00ae300098a63000014c000005c3f000011dc",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_14", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000232e00ae300098a6300002d1d0000753e0000502d",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_15", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000232e00ae300098a630000218a0000064900001c8c",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_16", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000231c0086300098a6300004b690000757300007722",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_17", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000231c0086300098a63000048b200000f2000003774",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_18", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000231c0086300098a630000177d00000e2d00002165",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_19", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000231c0086300098a630000647f0000005f00004d32",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_20", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000231c0086300098a63000007fd0000723c000032c7",[], [], "outer_terrain_plain"),

  ("random_scene_desert_custom_1", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000025559050000098a630000260a0000532f00003eb5",[], [], "outer_terrain_desert"),
  ("random_scene_desert_custom_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000025559050000098a63000039ba000048ae00002407",[], [], "outer_terrain_desert"),
  ("random_scene_desert_custom_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000025559050000098a63000019d60000425e00002a7e",[], [], "outer_terrain_desert"),
  ("random_scene_desert_custom_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000251d9050000098a6300003dfc000009af00003990",[], [], "outer_terrain_desert"),
  ("random_scene_desert_custom_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000251d9050000098a630000436f000048c500000caf",[], [], "outer_terrain_desert"),
  ("random_scene_desert_custom_6", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000251d9068000098a63000027a4000032c000007042",[], [], "outer_terrain_desert"),
  ("random_scene_desert_custom_7", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000251d9068000098a630000097a00001c900000259e",[], [], "outer_terrain_desert"),
  ("random_scene_desert_custom_8", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000025019058000098a63000066fc0000756500004946",[], [], "outer_terrain_desert"),
  ("random_scene_desert_custom_9", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000025019058000098a63000073c200002f6c000013be",[], [], "outer_terrain_desert"),
  ("random_scene_desert_custom_10", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000025019058000098a630000730b0000759600006b12",[], [], "outer_terrain_desert"),

  ("random_scene_plain_forest_custom_1", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b5e0056300098a63000064670000419400003ab1",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b5e0056300098a630000635e0000473800004cd3",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b5e0056300098a630000517600007b16000039a4",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b82006e300098a6300007d63000067ce00004a61",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b82006e300098a6300005ef9000041f300002200",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_6", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b82006e300098a630000250600003c4c00004ac9",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_7", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b820086300098a6300006d46000067fb00007796",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_8", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b820086300098a630000104b00003e0f00002ef9",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_9", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b820086300098a630000717a000052e200007d13",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_10", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b820086300098a63000009d60000490000005972",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_11", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b680086300098a630000243900001253000003d5",[], [], "outer_terrain_forest"),

  ("random_scene_desert_forest_custom_1", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002da0005000009ca720000504d000006e5000020d8",[], [], "outer_terrain_desert"),
  ("random_scene_desert_forest_custom_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002da0005000009ca7200006f4b000068770000566d",[], [], "outer_terrain_desert"),
  ("random_scene_desert_forest_custom_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002da0005000009ca720000209a0000793200003452",[], [], "outer_terrain_desert"),
  ("random_scene_desert_forest_custom_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002dc6005000009ca720000345800000507000022b7",[], [], "outer_terrain_desert"),
  ("random_scene_desert_forest_custom_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002dc6005000009ca720000073180007cf700005e67",[], [], "outer_terrain_desert"),

#REGIONAL MAPS

 ("sea_battle_mediterranean", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000001300000000005194a000041ef00005ae800003c55",[], [], "outer_terrain_beach_rotated"),
 ("sea_battle_north_europe", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000001300000000005194a000041ef00005ae800003c55",[], [], "outer_terrain_beach_rotated"),

 ("forest_battle_plain_roman", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000001300000000005194a000041ef00005ae800003c55",[], [], "outer_terrain_forest"),

# done
 ("battle_persian_hills_desert", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002d4a0098000092a4a00007ee00000704600005611",[], [], "outer_terrain_desert"),
 ("battle_persian_hills_desert_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002d8c005000009926300000dbc000049c400005816",[], [], "outer_terrain_desert"),
 ("battle_persian_hills_desert_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002d8c0050000099263000045140000011d000072c7",[], [], "outer_terrain_desert"),
 ("battle_persian_hills_desert_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002d8c00500000992630000794800007da900001d87",[], [], "outer_terrain_desert"),
 ("battle_persian_hills_desert_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002d8c005000009926300000ace00007da900000096",[], [], "outer_terrain_desert"),

 #done
 ("battle_spain", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000022000098000092a4a00007aec000020060000135c",[], [], "outer_terrain_plain"),
 ("battle_spain_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000241200f000009aa6c00005b9f0000010e00001f4c",[], [], "outer_terrain_steppe_2"),
 ("battle_spain_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220000f000009aa6c0000717a0000541600005727",[], [], "outer_terrain_steppe"),
 ("battle_spain_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002200005000009aa6c00006b7b00007984000029cb",[], [], "outer_terrain_steppe"),
 ("battle_spain_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002200009800009aa6c000011f900007984000029cb",[], [], "outer_terrain_steppe_2"),

 #done
 ("battle_mesopotamia", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000024560050000092a4a00005d5f00004f6000006eed",[], [], "outer_terrain_beach_desert"),
 ("battle_mesopotamia_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002200008e300095a5900005a7c000009d100001667",[], [], "outer_terrain_beach_desert"),
 ("battle_mesopotamia_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002432008e300095a5900006d970000621600006a47",[], [], "outer_terrain_desert"),
 ("battle_mesopotamia_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000024320056300095a590000384e00005d9500001ead",[], [], "outer_terrain_desert"),
 ("battle_mesopotamia_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000022000056300095a59000075ba0000694f00001fc2",[], [], "outer_terrain_desert_b"),

 #done
 ("battle_syria", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000245c00b0000092a4a0000707100004fa700002266",[], [], "outer_terrain_steppe_2"),
 ("battle_syria_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000024a000f810008fe4200004bc200006e8000000586",[], [], "outer_terrain_steppe_3"),
 ("battle_syria_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000024a000f810008fe42000027970000714600000586",[], [], "outer_terrain_steppe_3"),
 ("battle_syria_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000230000f810008fe420000724200006717000034ca",[], [], "outer_terrain_steppe_3"),
 ("battle_syria_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000230000f810008fe4200002ae1000002cb00006f0c",[], [], "outer_terrain_steppe_3"),

 #done
 ("battle_nile", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000024000050000092a4a000073b600002e1d00006385",[], [], "outer_terrain_beach_desert_flat"),
 ("battle_nile_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002300005010009124400006d24000064da000056e5",[], [], "outer_terrain_beach_desert_flat"),
 ("battle_nile_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002300009810009124400004c390000765d00007454",[], [], "outer_terrain_beach_desert_flat"),
 ("battle_nile_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002400005010009124400006d24000064da000056e5",[], [], "outer_terrain_beach_desert_flat"),
 ("battle_nile_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000240000501000912440000389c000069c200003811",[], [], "outer_terrain_beach_desert_flat"),
 #done
 ("battle_nile_delta", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000024000050000092a4a00002048000027c400006e2f",[], [], "outer_terrain_beach_desert_flat"),
 ("battle_nile_delta_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002400005000009124400001d78000046ec00005b45",[], [], "outer_terrain_beach_desert_flat"),
 ("battle_nile_delta_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002300005000009124400001d78000046ec00005b45",[], [], "outer_terrain_beach_desert_flat"),
 ("battle_nile_delta_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002300005000009124400005e5c0000147800000d0c",[], [], "outer_terrain_beach_desert_flat"),
 ("battle_nile_delta_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000023000050000091244000023850000152c00001670",[], [], "outer_terrain_beach_desert_flat"),

#done
 ("battle_anatolia_coastal", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000024a1909e30008aa2b00005ac600004cf300000143",[], [], "outer_terrain_beach_med"),
 ("battle_anatolia_coastal_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002c4c01a800009a66a00006a2400000c8000007f4f",[], [], "outer_terrain_beach_med"),
 ("battle_anatolia_coastal_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000024b000e000009e2780000253e000027db00007fd1",[], [], "outer_terrain_steppe_2"),
 ("battle_anatolia_coastal_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000244c014000009a66a0000690a0000787200005016",[], [], "outer_terrain_steppe_2"),
 ("battle_anatolia_coastal_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000244c014000009a66a00006aca00001f7b000016ee",[], [], "outer_terrain_steppe_2"),

 ("battle_caucasian_mountains", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002a520108000091e470000627b0000786a00007f58",[], [], "outer_terrain_mountain"),
 ("battle_caucasian_mountains_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000233a788b20009364e00002ebf000067560000174d",[], [], "outer_terrain_mountain"),
 ("battle_caucasian_mountains_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000233a789630009364e000060510000724400003221",[], [], "outer_terrain_mountain"),
 ("battle_caucasian_mountains_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000233a789630009364e00000a5f0000475a00002ea3",[], [], "outer_terrain_mountain"),
 ("battle_caucasian_mountains_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b3a789630009364e0000697200005efa00003e36",[], [], "outer_terrain_mountain"),
 ("battle_caucasian_mountains_6", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000230000500000329e400005cce00003f9200002e90",[], [], "outer_terrain_mountain"),

 ("battle_central_anatolia", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002206006e30008be27000060d50000026e000003de",[], [], "outer_terrain_steppe_3"),
 ("battle_central_anatolia_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000000200012e30009725e000024bc000066590000127e",[], [], "outer_terrain_steppe_3"),
 ("battle_central_anatolia_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000000200012e30009725e00007f1a0000629a00001b19",[], [], "outer_terrain_steppe_3"),
 ("battle_central_anatolia_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000020000ce30009725e00007f1a0000629a00004017",[], [], "outer_terrain_steppe_3"),
 ("battle_central_anatolia_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000020000ce30009725e000053370000024c00000ada",[], [], "outer_terrain_steppe_3"),

 ("battle_europe_mountains", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000023c0151e30008160200005d1e0000559000000edb",[], [], "outer_terrain_plain_2"),
 ("battle_europe_mountains_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002bc60158000087a1e00001d6d00003ee8000008cb",[], [], "outer_terrain_plain_2"),
 ("battle_europe_mountains_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000238c005000009926300003fed0000064d00006e9d",[], [], "outer_terrain_mountain"),
 ("battle_europe_mountains_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000238c00500000992630000763b000033b800000501",[], [], "outer_terrain_mountain"),
 ("battle_europe_mountains_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000238c00500000992630000267800006700000071b3",[], [], "outer_terrain_mountain"),

 ("battle_persian_hills_green", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000022000160000089e2b00006f7200002a3400003b51",[], [], "outer_terrain_steppe_3"),
 ("battle_persian_hills_green_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000012201907e300599a64000009bd00002031000076c1",[], [], "outer_terrain_steppe_3"),
 ("battle_persian_hills_green_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000012201907e300599a6400000175000056a60000146c",[], [], "outer_terrain_steppe_3"),
 ("battle_persian_hills_green_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000012201907e300599a64000067d400001d0d000014bc",[], [], "outer_terrain_steppe_3"),
 ("battle_persian_hills_green_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000012201907e300599a64000001eb000014bc0000411e",[], [], "outer_terrain_steppe_3"),
 ("bridge_battle_iran_green", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000001300000000005194a000041ef00005ae800003c55",[], [], "outer_terrain_steppe"),

 ("battle_italian_greek", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000247c4caa3000982610000689f00000bda00002412",[], [], "outer_terrain_plain_2"),
 ("battle_italian_greek_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000124a1907e300599a6400001dc2000050d600002850",[], [], "outer_terrain_plain_2"),
 ("battle_italian_greek_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000124a1907e300599a6400002ee9000074da0000423d",[], [], "outer_terrain_plain_2"),
 ("battle_italian_greek_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000012401907e300599a64000061ae00006617000033aa",[], [], "outer_terrain_plain_2"),
 ("battle_italian_greek_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000012400007e300599a6400007ec300000ad900006f54",[], [], "outer_terrain_plain_2"),
 ("bridge_battle_mediterranean", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000001300000000005194a000041ef00005ae800003c55",[], [], "outer_terrain_steppe"),

  #NORTH AFRICA
 ("river_battle_north_africa", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000248600500000b0ac6000016a200000dff00007268",[], [], "outer_terrain_steppe"),
 ("random_scene_north_africa_1", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000145800863000abaae0000274a00004eb700003ff9",[], [], "outer_terrain_steppe"), #hills/valley 1
 ("random_scene_north_africa_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000146e00563000d2348000073b90000447500000f05",[], [], "outer_terrain_steppe"), #flatlands 1
 ("random_scene_north_africa_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000014c601163000d234800007a2d00006ac200005744",[], [], "outer_terrain_steppe"), #hills/valley 2
 ("random_scene_north_africa_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000014c600d63000d23480000267d0000754c00006fca",[], [], "outer_terrain_steppe"), #hills 2


  ("battle_scene_custom_1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000003c64120080025896000014d90000058a00000d06",
    [],[], "outer_terrain_plain"),
  ("battle_scene_custom_2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000420000500000231cf0000075e0000723200001a43",
    [],[], "outer_terrain_steppe"),

  ("four_ways_inn",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af",
    [],[], "outer_terrain_town_thir_1"),
  ("test_scene",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0230817a00028ca300007f4a0000479400161992",
    [],[], "outer_terrain_plain"),
  ("quick_battle_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x30401ee300059966000001bf0000299a0000638f",
    [],[], "outer_terrain_plain"),
  ("quick_battle_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0xa0425ccf0004a92a000063d600005a8a00003d9a",
    [],[], "outer_terrain_steppe"),
  ("quick_battle_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x4c6024e3000691a400001b7c0000591500007b52",
    [],[], "outer_terrain_plain"),
  ("quick_battle_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00001d63c005114300006228000053bf00004eb9",
    [],[], "outer_terrain_plain"),
  ("quick_battle_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x3a078bb2000589630000667200002fb90000179c",
    [],[], "outer_terrain_plain"),
  ("quick_battle_6",sf_generate,"none", "none", (0,0),(120,120),-100,"0xa0425ccf0004a92a000063d600005a8a00003d9a",
    [],[], "outer_terrain_steppe"),
  ("quick_battle_7",sf_generate,"none", "none", (0,0),(100,100),-100,"0x314d060900036cd70000295300002ec9000025f3",
    [],[],"outer_terrain_plain"),
  ("salt_mine",sf_generate,"none", "none", (-200,-200),(200,200),-100,"0x2a07b23200025896000023ee00007f9c000022a8",
    [],[], "outer_terrain_steppe"),
  ("novice_ground",sf_indoors,"training_house_a", "bo_training_house_a", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("zendar_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[], "outer_terrain_plain"),
  ("dhorak_keep",sf_generate,"none", "none", (0,0),(120,120),-100,"0x33a7946000028ca300007f4a0000479400161992",
    ["exit"],[]),
  ("reserved4",sf_generate,"none", "none", (0,0),(120,120),-100,"28791",
    [],[]),
  ("reserved5",sf_generate,"none", "none", (0,0),(120,120),-100,"117828",
    [],[]),
  ("reserved6",sf_generate,"none", "none", (0,0),(100,100),-100,"6849",
    [],[]),
  ("reserved7",sf_generate,"none", "none", (0,0),(100,100),-100,"6849",
    [],[]),
  ("reserved8",sf_generate,"none", "none", (0,0),(100,100),-100,"13278",
    [],[]),
  ("reserved9",sf_indoors,"thirsty_lion", "bo_thirsty_lion", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("reserved10",0,"none", "none", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("reserved11",0,"none", "none", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("reserved12",sf_indoors,"thirsty_lion", "bo_thirsty_lion", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("training_ground",sf_generate,"none", "none", (0,0),(120,120),-100,"0x30000500400360d80000189f00002a8380006d91",
    [],["tutorial_chest_1", "tutorial_chest_2"], "outer_terrain_plain_2"),
  ("tutorial_1",sf_indoors,"tutorial_1_scene", "bo_tutorial_1_scene", (-100,-100),(100,100),-100,"0",
    [],[]),
##  ("tutorial_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003a04ce140005e17a000030030000780e00006979",
##    [],[], "outer_terrain_plain"),
  ("tutorial_2",sf_indoors,"tutorial_2_scene", "bo_tutorial_2_scene", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("tutorial_3",sf_indoors,"tutorial_3_scene", "bo_tutorial_3_scene", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("tutorial_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x30000500400360d80000189f00002a8380006d91",
    [],[], "outer_terrain_plain"),
  ("tutorial_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x3a06dca80005715c0000537400001377000011fe",
    [],[], "outer_terrain_plain"),


  ("training_ground_horse_track_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000337553240004d53700000c0500002a0f80006267",
    [],[], "outer_terrain_plain"),
  ("training_ground_horse_track_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000301553240004d5370000466000002a0f800073f1",
    [],[], "outer_terrain_plain"),
  #Kar
  ("training_ground_horse_track_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000400c12b2000515470000216b0000485e00006928",
    [],[], "outer_terrain_plain"),
  #Steppe
  ("training_ground_horse_track_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000200b60320004a5290000180d0000452f00000e90",
    [],[], "outer_terrain_steppe"),
  #Plain
  ("training_ground_horse_track_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003008208e0006419000000f730000440f00003c86",
    [],[], "outer_terrain_plain"),

  ("training_ground_ranged_melee_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001350455c20005194a000041cb00005ae800000ff5",
    [],[], "outer_terrain_plain"),
  ("training_ground_ranged_melee_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0000000532c8dccb0005194a000041cb00005ae800001bdd",
    [],[], "outer_terrain_plain"),
  #Kar
  ("training_ground_ranged_melee_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000054327dcba0005194a00001b1d00005ae800004d63",
    [],[], "outer_terrain_plain"),
  #Steppe
  ("training_ground_ranged_melee_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000012247dcba0005194a000041ef00005ae8000050af",
    [],[], "outer_terrain_steppe"),
  #Plain
  ("training_ground_ranged_melee_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001324a9cba0005194a000041ef00005ae800003c55",
    [],[], "outer_terrain_plain"),

  ("zendar_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    ["the_happy_boar","","zendar_merchant"],[], "outer_terrain_plain_2"),
#  ("zendar_center",0,"sargoth_square", "bo_sargoth_square", (-24,-22),(21,13),-100,"0",
#    ["the_happy_boar","","zendar_merchant"],[]),
  ("the_happy_boar",sf_indoors,"interior_town_house_f", "bo_interior_town_house_f", (-100,-100),(100,100),-100,"0",
    ["zendar_center"],["zendar_chest"]),
  ("zendar_merchant",sf_indoors,"interior_town_house_i", "bo_interior_town_house_i", (-100,-100),(100,100),-100,"0",
    [],[]),

# Tvern names:
  #the shy monkey
  #the singing pumpkin
  #three swords
  #red stag
  #the bard's corner

#interior_tavern_a
#  town_1   Sargoth     #plain
#  town_2   Tihr        #plain
#  town_3   Veluca      #steppe
#  town_4   Suno        #plain
#  town_5   Jelkala     #plain
#  town_6   Praven      #plain
#  town_7   Uxkhal      #plain
#  town_8   Reyvadin    #plain
#  town_9   Khudan      #snow
#  town_10  Tulga       #steppe
#  town_11  Curaw       #snow
#  town_12  Wercheg     #plain
#  town_13  Rivacheg    #plain
#  town_14  Halmar      #steppe
  ("town_1_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x3002cd340002b4ac00002ccd800026dc00000c1d",
    [],[],"outer_terrain_plain"),
  ("town_2_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x3002cd340002b4ac00002ccd800026dc00000c1d",
    [],[],"sea_outer_terrain_1"),
  ("town_3_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000300005000005b56d00000e1a00007c7d00007c7d",
    [],[],"outer_terrain_plain"),
  ("town_4_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000a000050000091e4b0000683a00006fbb0000640c",
    [],[],"outer_terrain_steppe"),
  ("town_5_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000300005000005b56d00000e1a00007c7d00007c7d",
    [],[],"outer_terrain_plain"),
  ("town_6_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130000500000911a900002d4000004bb200004d2a",
    [],[],"sea_outer_terrain_2"),
  ("town_7_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),
  ("town_8_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x0000000130000000000edbb600000e1a00007c7d00007c7d",
    [],[],"outer_terrain_plain"),
  ("town_9_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),
  ("town_10_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x0000000130000100000af2bc00000b5c00003ad100005795",
    [],["bonus_chest_4"],"outer_terrain_plain"),
  ("town_11_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),
  ("town_12_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013007b2630005695c00001ebe0000028e00007e37",
    [],[],"outer_terrain_forest"),
  ("town_13_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000300005000006f1bc00003217000045ed00004139",
    [],["bonus_chest_8"],"outer_terrain_plain"),
  ("town_14_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af",
    [],[],"outer_terrain_forest"),
  ("town_15_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000300005000005b56d00000e1a00007c7d00007c7d",
    [],[],"outer_terrain_plain"),
  ("town_16_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000300005000005695d00007fbc00005de100006275",
    [],["bonus_chest_3"],"outer_terrain_plain"),
  ("town_17_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000013a01c85000057ddf700072a70000240a00001e090",
    [],[],"sea_outer_terrain_2"),
  ("town_18_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x3002cd340002b4ac00002ccd800026dc00000c1d",
    [],[],"outer_terrain_town_thir_1"),
  ("town_19_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x0000000050000000000e13840000076300004ce100002de9",
    [],[],"outer_terrain_desert"),
  ("town_20_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000a000050000091e4b0000683a00006fbb0000640c",
    [],[],"outer_terrain_steppe"),
  ("town_21_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000005054100002d0b00003a0200002ca5",
    [],[],"outer_terrain_beach"),
  ("town_22_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_desert"),
## New Cities
  ("town_23_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x3002cd340002b4ac00002ccd800026dc00000c1d",
    [],[],"outer_terrain_plain"),
  ("town_24_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af",
    [],[],"outer_terrain_plain"),
  ("town_25_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000300005000007a1e800000b5400003ad100005795",
    [],[],"outer_terrain_plain"),
  ("town_26_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000a000050000091e4b0000683a00006fbb0000640c",
    [],[],"outer_terrain_steppe"),
  ("town_27_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x000000003000050000054150000045e10000331000005af7",
    [],[],"outer_terrain_plain"),
  ("town_28_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x000000005a024714000d23480000076300004ce100002de9",
    [],[],"outer_terrain_desert_b"),

  ("town_29_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_plain"),
  ("town_30_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030024e108003fd0100007bd300006c31000061aa",
    [],[],"outer_terrain_plain"),

  ("town_31_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130000500000b5f1600000aac000021cc000077c2",
    [],[],"outer_terrain_forest"),
  ("town_32_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300000000005194a000041ef00005ae800003c55",
    [],[],"outer_terrain_forest"),

  ("town_33_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000300005000007a1e800000b5400003ad100005795",
    [],[],"outer_terrain_plain"),

  ("town_34_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000001300000000005194a000041ef00005ae800003c55",
    [],[],"outer_terrain_plain_2"),

  ("town_35_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),

  ("town_36_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000a00005000005715c00000935000076e80000443a",
    [],[],"outer_terrain_beach"),

  ("town_37_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000001a0000500000d2348000008df00004ce100002de9",
    [],[],"TLD_outer_terrain_river_west"),
  ("town_38_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x000000003000050000090240000017ed0000346f0000649d",
    [],[],"outer_terrain_steppe"),
  ("town_39_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000300005000005b56d00000e1a00007c7d00007c7d",
    [],[],"outer_terrain_plain"),

  ("town_40_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),
  ("town_41_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98d0005b56d000072a70000240a00001e09",
    [],[],"outer_terrain_beach"),

  ("town_42_center",sf_generate|sf_muddy_water,"none", "none",(0,0),(100,100),-100,"0x000000005a024714000d23480000076300004ce100002de9",
    [],[],"outer_terrain_desert"),

  ("town_43_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000715c5000057cd000035390000272c",
    [],[],"outer_terrain_plain"),

  ("town_44_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98d0005b56d000072a70000240a00001e09",
    [],[],"outer_terrain_beach"),
  ("town_45_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000a000050000091e4b0000683a00006fbb0000640c",
    [],[],"outer_terrain_mountain"),

  ("town_46_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000001300000000005194a000041ef00005ae800003c55",
    [],[],"outer_terrain_plain_2"),

  ("town_47_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000007a1e800000b5400003ad100005795",
    [],[],"outer_terrain_forest"),

  ("town_48_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000007a1e800000b5400003ad100005795",
    [],[],"outer_terrain_forest"),

  ("town_49_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),

  ("town_1_castle",sf_indoors,"viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_1_seneschal"]),
  ("town_2_castle",sf_indoors,"interior_castle_n", "bo_interior_castle_n", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_2_seneschal"]),
  ("town_3_castle",sf_indoors,"byzantine_interior", "bo_brewery_interior", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_3_seneschal"]),
  ("town_4_castle",sf_indoors, "interior_castle_q", "bo_interior_castle_q", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_4_seneschal"]),
  ("town_5_castle",sf_indoors,"byzantine_interior", "bo_brewery_interior", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_5_seneschal"]),
  ("town_6_castle",sf_indoors, "constantinople_interior", "bo_brewery_interior", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_6_seneschal"]),
  ("town_7_castle",sf_indoors, "byzantine_interior", "bo_brewery_interior", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_7_seneschal"]),
  ("town_8_castle",sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_8_seneschal"]),
  ("town_9_castle",sf_indoors, "byzantine_interior", "bo_brewery_interior", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_9_seneschal"]),
  ("town_10_castle",sf_indoors, "interior_castle_d_roman", "bo_interior_castle_d", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_10_seneschal"]),
  ("town_11_castle",sf_indoors, "byzantine_interior", "bo_brewery_interior", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_11_seneschal"]),
  ("town_12_castle",sf_indoors, "castle_h_interior_b", "bo_castle_h_interior_b", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_12_seneschal"]),
#  ("town_12_castle",sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",
#    ["exit"],["town_12_seneschal"]),
  ("town_13_castle",sf_indoors, "interior_castle_m2", "bo_interior_castle_m", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_13_seneschal"]),
  ("town_14_castle",sf_indoors,"viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_14_seneschal"]),
  ("town_15_castle",sf_indoors, "byzantine_interior", "bo_brewery_interior", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_15_seneschal"]),
  ("town_16_castle",sf_indoors,"byzantine_interior", "bo_brewery_interior", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_16_seneschal"]),
  ("town_17_castle",sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_17_seneschal"]),
  ("town_18_castle",sf_indoors,"viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_18_seneschal"]),
  ("town_19_castle",sf_indoors, "arabian_interior_keep_a", "bo_arabian_interior_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_19_seneschal"]),
  ("town_20_castle",sf_indoors, "arabian_interior_keep_a", "bo_arabian_interior_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_20_seneschal"]),
  ("town_21_castle",sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_21_seneschal"]),
  ("town_22_castle",sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_22_seneschal"]),
## New Cities
  ("town_23_castle",sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_23_seneschal"]),
  ("town_24_castle",sf_indoors,"viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_24_seneschal"]),
  ("town_25_castle",sf_indoors, "interior_castle_d_roman", "bo_interior_castle_d", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_25_seneschal"]),
  ("town_26_castle",sf_indoors, "arabian_interior_keep_a", "bo_arabian_interior_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_26_seneschal"]),
  ("town_27_castle",sf_indoors, "interior_castle_g_square_keep", "bo_interior_castle_g_square_keep", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_27_seneschal"]),
  ("town_28_castle",sf_indoors, "arabian_interior_keep_a", "bo_arabian_interior_keep_a", (-100,-100),(100,100),-100,"0x00000007300005000002308c00004a840000624700004fda",
    ["exit"],["town_28_seneschal"]),

  ("town_29_castle",sf_indoors,"viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_29_seneschal"]),
  ("town_30_castle",sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_30_seneschal"]),

  ("town_31_castle",sf_indoors,"viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_31_seneschal"]),
  ("town_32_castle",sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100, -100), (100, 100), -100, "0",
    ["exit"], ["town_32_seneschal"]),

  ("town_33_castle",sf_indoors, "interior_castle_d_roman", "bo_interior_castle_d", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_33_seneschal"]),

  ("town_34_castle",sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_34_seneschal"]),

  ("town_35_castle",sf_indoors, "byzantine_interior", "bo_brewery_interior", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_35_seneschal"]),

  ("town_36_castle",sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_36_seneschal"]),

  ("town_37_castle",sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_37_seneschal"]),
  ("town_38_castle",sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_38_seneschal"]),
  ("town_39_castle",sf_indoors, "byzantine_interior", "bo_brewery_interior", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_39_seneschal"]),

  ("town_40_castle",sf_indoors, "byzantine_interior", "bo_brewery_interior", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_40_seneschal"]),
  ("town_41_castle",sf_indoors, "byzantine_interior", "bo_brewery_interior", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_41_seneschal"]),

  ("town_42_castle",sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_42_seneschal"]),

  ("town_43_castle",sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_43_seneschal"]),

  ("town_44_castle",sf_indoors, "interior_castle_d_roman", "bo_interior_castle_d", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_44_seneschal"]),
  ("town_45_castle",sf_indoors, "arabian_interior_keep_a", "bo_arabian_interior_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_45_seneschal"]),

  ("town_46_castle",sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_46_seneschal"]),

  ("town_47_castle",sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100, -100), (100, 100), -100, "0",
    ["exit"], ["town_47_seneschal"]),

  ("town_48_castle",sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100, -100), (100, 100), -100, "0",
    ["exit"], ["town_47_seneschal"]),

  ("town_49_castle",sf_indoors, "byzantine_interior", "bo_brewery_interior", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_35_seneschal"]),


  ("town_1_tavern",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_2_tavern",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_3_tavern",sf_indoors, "interior_castle_d_roman", "bo_interior_castle_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_4_tavern",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_5_tavern",sf_indoors, "interior_castle_d_roman", "bo_interior_castle_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_6_tavern",sf_indoors, "interior_castle_d_roman", "bo_interior_castle_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_7_tavern",sf_indoors, "roman_tavern", "bo_roman_tavern", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_8_tavern",sf_indoors, "interior_castle_d_roman", "bo_interior_castle_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_9_tavern",sf_indoors, "roman_tavern", "bo_roman_tavern", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_10_tavern",sf_indoors, "interior_castle_d_roman", "bo_interior_castle_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_11_tavern",sf_indoors, "roman_tavern", "bo_roman_tavern", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_12_tavern",sf_indoors, "interior_rhodok_houses_d", "bo_interior_rhodok_houses_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_13_tavern",sf_indoors, "interior_castle_d_roman", "bo_interior_castle_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_14_tavern",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_15_tavern",sf_indoors, "interior_castle_d_roman", "bo_interior_castle_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_16_tavern",sf_indoors, "interior_castle_d_roman", "bo_interior_castle_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_17_tavern",sf_indoors, "roman_tavern", "bo_roman_tavern", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_18_tavern",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_19_tavern",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_20_tavern",sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_21_tavern",sf_indoors, "roman_tavern", "bo_roman_tavern", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_22_tavern",sf_indoors, "roman_tavern", "bo_roman_tavern", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
## New Cities
  ("town_23_tavern",sf_indoors, "interior_tavern_b", "bo_interior_tavern_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_24_tavern",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_25_tavern",sf_indoors, "interior_castle_d_roman", "bo_interior_castle_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_26_tavern",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_27_tavern",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_28_tavern",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_29_tavern",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_30_tavern",sf_indoors, "interior_tavern_b", "bo_interior_tavern_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  #("town_31_tavern",sf_indoors, "interior_rhodok_houses_d", "bo_interior_rhodok_houses_d", (-100,-100),(100,100),-100,"0",
  #  ["exit"],[]),
  ("town_31_tavern",sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_32_tavern",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_33_tavern",sf_indoors, "interior_castle_d_roman", "bo_interior_castle_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_34_tavern",sf_indoors, "viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_35_tavern",sf_indoors, "roman_tavern", "bo_roman_tavern", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  #("town_36_tavern",sf_indoors, "interior_castle_d_roman", "bo_interior_castle_d", (-100,-100),(100,100),-100,"0",
  #  ["exit"],[]),
  ("town_36_tavern",sf_indoors, "interior_rhodok_houses_d", "bo_interior_rhodok_houses_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


  ("town_37_tavern",sf_indoors, "interior_castle_d_roman", "bo_interior_castle_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_38_tavern",sf_indoors, "viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_39_tavern",sf_indoors, "interior_castle_d_roman", "bo_interior_castle_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_40_tavern",sf_indoors, "roman_tavern", "bo_roman_tavern", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_41_tavern",sf_indoors, "roman_tavern", "bo_roman_tavern", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_42_tavern",sf_indoors, "interior_castle_d_roman", "bo_interior_castle_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_43_tavern",sf_indoors, "interior_tavern_b", "bo_interior_tavern_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_44_tavern",sf_indoors, "interior_castle_d_roman", "bo_interior_castle_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_45_tavern",sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_46_tavern",sf_indoors, "viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_47_tavern",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_48_tavern",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_49_tavern",sf_indoors, "roman_tavern", "bo_roman_tavern", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


  ("town_1_store",sf_indoors,"viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_2_store",sf_indoors,"viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_3_store",sf_indoors,"interior_rhodok_houses_d", "bo_interior_rhodok_houses_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_4_store",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_5_store",sf_indoors,"interior_rhodok_houses_d", "bo_interior_rhodok_houses_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_6_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_7_store",sf_indoors, "interior_house_a", "bo_interior_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_8_store",sf_indoors, "interior_house_b", "bo_interior_house_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_9_store",sf_indoors, "interior_tavern_a", "bo_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_10_store",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_11_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_12_store",sf_indoors, "viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_13_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_14_store",sf_indoors, "interior_rhodok_houses_b", "bo_interior_rhodok_houses_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_15_store",sf_indoors, "interior_rhodok_houses_b", "bo_interior_rhodok_houses_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_16_store",sf_indoors,"interior_rhodok_houses_d", "bo_interior_rhodok_houses_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_17_store",sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_18_store",sf_indoors, "viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_19_store",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_20_store",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_21_store",sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_22_store",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
## New Cities
  ("town_23_store",sf_indoors, "viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_24_store",sf_indoors, "interior_rhodok_houses_b", "bo_interior_rhodok_houses_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_25_store",sf_indoors,"interior_rhodok_houses_d", "bo_interior_rhodok_houses_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_26_store",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_27_store",sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_28_store",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_29_store",sf_indoors, "interior_rhodok_houses_b", "bo_interior_rhodok_houses_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_30_store",sf_indoors, "interior_town_house_i", "bo_interior_town_house_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_31_store",sf_indoors, "viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_32_store",sf_indoors, "viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_33_store",sf_indoors,"interior_rhodok_houses_d", "bo_interior_rhodok_houses_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_34_store",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_35_store",sf_indoors, "interior_house_a", "bo_interior_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_36_store",sf_indoors, "viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_37_store",sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_38_store",sf_indoors, "interior_house_b", "bo_interior_house_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_39_store",sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_40_store",sf_indoors, "interior_house_a", "bo_interior_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_41_store",sf_indoors, "viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_42_store",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_43_store",sf_indoors,"interior_town_house_e", "bo_interior_town_house_e", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_44_store",sf_indoors, "viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_45_store",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_46_store",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_47_store",sf_indoors, "viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_48_store",sf_indoors, "viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_49_store",sf_indoors, "interior_house_a", "bo_interior_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_1_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_2_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_3_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_4_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_desert"),
  ("town_5_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_6_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_plain"),
  ("town_7_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_plain"),
  ("town_8_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af",
    [],[],"outer_terrain_plain"),
  ("town_9_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_10_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_forest"),
  ("town_11_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_12_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_13_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_plain"),
  ("town_14_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_forest"),
  ("town_15_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_16_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_17_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_desert"),
  ("town_18_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_town_thir_1"),
  ("town_19_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_desert"),
  ("town_20_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_desert"),
  ("town_21_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_plain"),
  ("town_22_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_desert"),
## New Cities
  ("town_23_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_24_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_25_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_26_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_desert"),
  ("town_27_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_steppe"),
  ("town_28_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_desert"),

  ("town_29_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af",
    [],[],"outer_terrain_plain"),
  ("town_30_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

  ("town_31_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_forest"),
  ("town_32_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

  ("town_33_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

  ("town_34_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_desert"),

  ("town_35_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

  ("town_36_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

  ("town_37_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_steppe"),
  ("town_38_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_plain"),
  ("town_39_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

  ("town_40_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_41_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

  ("town_42_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_desert"),

  ("town_43_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_44_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_45_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_mountain"),
  ("town_46_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_desert"),

  ("town_47_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_48_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_49_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),

("town_1_prison",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_2_prison",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",#"interior_prison_n", "bo_interior_prison_n",
    ["exit"],[]),
  ("town_3_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_4_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_5_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_6_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_7_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_8_prison",sf_indoors,"dungeon_cell_b", "bo_dungeon_cell_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_9_prison",sf_indoors,"interior_prison_j", "bo_interior_prison_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_10_prison",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_11_prison",sf_indoors,"dungeon_a", "bo_dungeon_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_12_prison",sf_indoors,"interior_prison_h", "bo_interior_prison_h", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_13_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_14_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_15_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_16_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_17_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_18_prison",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_19_prison",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_20_prison",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_21_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_22_prison",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
## New Cities
  ("town_23_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_24_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_25_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_26_prison",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_27_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_28_prison",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_29_prison",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",#"interior_prison_j", "bo_interior_prison_j",
    ["exit"],[]),
  ("town_30_prison",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",#"interior_prison_o", "bo_interior_prison_o",
    ["exit"],[]),
  ("town_31_prison",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_32_prison",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_33_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_34_prison",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_35_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_36_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("town_37_prison",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_38_prison",sf_indoors,"dungeon_cell_b", "bo_dungeon_cell_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_39_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_40_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_41_prison",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_42_prison",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_43_prison",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_44_prison",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_45_prison",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_46_prison",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_47_prison",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_48_prison",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_49_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_1_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_plain"),
  ("town_2_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_plain"),
  ("town_3_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000005b56d00000e1a00007c7d00007c7d",
    [],[],"outer_terrain_plain"),
  ("town_4_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000a000050000091e4b0000683a00006fbb0000640c",
    [],[],"outer_terrain_steppe"),
  ("town_5_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000005b56d00000e1a00007c7d00007c7d",
    [],[],"outer_terrain_plain"),
  ("town_6_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000003f0fc000046ee00004ec900002751",
    [],[],"sea_outer_terrain_2"),
  ("town_7_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),
  ("town_8_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000013301c85000059224800072a70000240a00001e090",
    [],[],"outer_terrain_plain"),
  ("town_9_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),
  ("town_10_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130000100000af2bc00000b5c00003ad100005795",
    [],[],"outer_terrain_forest"),
  ("town_11_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),
  ("town_12_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013007b2630005695c00001ebe0000028e00007e37",
    [],[],"outer_terrain_forest"),
  ("town_13_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000006f1bc00003217000045ed00004139",
    [],[],"outer_terrain_plain"),
  ("town_14_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_forest"),
  ("town_15_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000005b56d00000e1a00007c7d00007c7d",
    [],[],"outer_terrain_plain"),
  ("town_16_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000005695d00007fbc00005de100006275",
    [],[],"outer_terrain_plain"),
  ("town_17_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000013a01c85000057ddf700072a70000240a00001e090",
    [],[],"sea_outer_terrain_2"),
  ("town_18_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_plain"),
  ("town_19_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000005a024714000d23480000076300004ce100002de9",
    [],[],"outer_terrain_desert"),
  ("town_20_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000a000050000091e4b0000683a00006fbb0000640c",
    [],[],"outer_terrain_steppe"),
  ("town_21_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98d0005b56d000072a70000240a00001e09",
    [],[],"outer_terrain_beach"),
  ("town_22_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_desert"),
# New Cities
  ("town_23_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_plain"),
  ("town_24_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_plain"),
  ("town_25_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000007a1e800000b5400003ad100005795",
    [],[],"outer_terrain_plain"),
  ("town_26_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000a000050000091e4b0000683a00006fbb0000640c",
    [],[],"outer_terrain_steppe"),

  ("town_27_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000050000054150000045e10000331000005af7",
    [],[],"outer_terrain_plain"),

  ("town_28_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000005a024714000d23480000076300004ce100002de9",
    [],[],"outer_terrain_desert_b"),
  ("town_29_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_plain"),
  ("town_30_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030024e108003fd0100007bd300006c31000061aa",
    [],[],"outer_terrain_plain"),
  ("town_31_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130000500000b5f1600000aac000021cc000077c2",
    [],[],"outer_terrain_forest"),
  ("town_32_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300000000005194a000041ef00005ae800003c55",
    [],[],"outer_terrain_forest"),
  ("town_33_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000007a1e800000b5400003ad100005795",
    [],[],"outer_terrain_plain"),
  ("town_34_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300000000005194a000041ef00005ae800003c55",
    [],[],"outer_terrain_plain_2"),
  ("town_35_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),

  ("town_36_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000a00005000005715c00000935000076e80000443a",
    [],[],"outer_terrain_beach"),

  ("town_37_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001a0000500000d2348000008df00004ce100002de9",
    [],[],"TLD_outer_terrain_river_west"),
  ("town_38_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000050000090240000017ed0000346f0000649d",
    [],[],"outer_terrain_steppe"),
  ("town_39_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000005b56d00000e1a00007c7d00007c7d",
    [],[],"outer_terrain_plain"),

  ("town_40_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),
  ("town_41_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98d0005b56d000072a70000240a00001e09",
    [],[],"outer_terrain_beach"),
  ("town_42_walls",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x000000005a024714000d23480000076300004ce100002de9",
    [],[],"outer_terrain_desert"),

  ("town_43_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000715c5000057cd000035390000272c",
    [],[],"outer_terrain_plain"),

  ("town_44_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98d0005b56d000072a70000240a00001e09",
    [],[],"outer_terrain_beach"),
  ("town_45_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000a000050000091e4b0000683a00006fbb0000640c",
    [],[],"outer_terrain_mountain"),
  ("town_46_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300000000005194a000041ef00005ae800003c55",
    [],[],"outer_terrain_plain_2"),
  ("town_47_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000007a1e800000b5400003ad100005795",
    [],[],"outer_terrain_forest"),
  ("town_48_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000007a1e800000b5400003ad100005795",
    [],[],"outer_terrain_forest"),
  ("town_49_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),

  ("town_1_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_2_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_3_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000050000500400370e000002236000043df0000369c",
    [],[],"outer_terrain_plain"),
  ("town_4_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000a000050000091e4b0000683a00006fbb0000640c",
    [],[],"outer_terrain_steppe"),
  ("town_5_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000050000500400370e000002236000043df0000369c",
    [],[],"outer_terrain_plain"),
  ("town_6_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130000500000911a900002d4000004bb200004d2a",
    [],[],"outer_terrain_plain"),
  ("town_7_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),
  ("town_8_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000005b56d00000e1a00007c7d00007c7d",
    [],[],"outer_terrain_plain"),
  ("town_9_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),
  ("town_10_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130000100000af2bc00000b5c00003ad100005795",
    [],[],"outer_terrain_plain"),
  ("town_11_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),
  ("town_12_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_13_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000006f1bc00003217000045ed00004139",
    [],[]),
  ("town_14_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_forest"),
  ("town_15_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000005b56d00000e1a00007c7d00007c7d",
    [],[],"outer_terrain_plain"),
  ("town_16_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000005695d00007fbc00005de100006275",
    [],[],"outer_terrain_plain"),
  ("town_17_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),
  ("town_18_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_town_thir_1"),
  ("town_19_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000005a024714000d23480000076300004ce100002de9",
    [],[],"outer_terrain_desert"),
  ("town_20_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000a000050000091e4b0000683a00006fbb0000640c",
    [],[],"outer_terrain_steppe"),
  ("town_21_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),
  ("town_22_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000005a024714000d23480000076300004ce100002de9",
    [],[],"outer_terrain_desert"),
#New Cities
  ("town_23_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_24_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_25_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000007a1e800000b5400003ad100005795",
    [],[]),
  ("town_26_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000a000050000091e4b0000683a00006fbb0000640c",
    [],[],"outer_terrain_steppe"),

  ("town_27_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000050000054150000045e10000331000005af7",
    [],[],"outer_terrain_plain"),

  ("town_28_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000005a024714000d23480000076300004ce100002de9",
    [],[],"outer_terrain_desert_b"),
  ("town_29_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_town_thir_1"),
  ("town_30_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_31_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_32_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_33_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_34_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300000000005194a000041ef00005ae800003c55",
    [],[],"outer_terrain_plain_2"),
  ("town_35_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),

  ("town_36_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),

  ("town_37_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000050000054150000045e10000331000005af7",
    [],[],"outer_terrain_plain"),
  ("town_38_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000050000090240000017ed0000346f0000649d",
    [],[],"outer_terrain_plain"),
  ("town_39_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000005b56d00000e1a00007c7d00007c7d",
    [],[],"outer_terrain_plain"),

  ("town_40_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),
  ("town_41_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),
  ("town_42_alley",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x000000005a024714000d23480000076300004ce100002de9",
    [],[],"outer_terrain_desert"),
  ("town_43_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000715c5000057cd000035390000272c",
    [],[],"outer_terrain_plain"),
  ("town_44_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),
  ("town_45_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000a000050000091e4b0000683a00006fbb0000640c",
    [],[],"outer_terrain_mountain"),
  ("town_46_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300000000005194a000041ef00005ae800003c55",
    [],[],"outer_terrain_plain_2"),

  ("town_47_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000007a1e800000b5400003ad100005795",
    [],[],"outer_terrain_forest"),
  ("town_48_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000007a1e800000b5400003ad100005795",
    [],[],"outer_terrain_forest"),
  ("town_49_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",
    [],[],"outer_terrain_beach"),


#0x30054d228004050000005a768000688400002e3b
#0x30054da28004050000005a76800022aa00002e3b
#Castles:
  ("castle_1_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005630007d1f800006aba0000574f00001099", #comagena
    [],[],"TLD_outer_terrain_river_east"),

  ("castle_2_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007a3b20005795e0000706d0000381800000bbc", #bry briton hillfort
    [],[],"outer_terrain_plain"),
  ("castle_2_interior",sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("castle_2_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("castle_8_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500005000004fd3f0000315e0000201a0000697b", #roman desert port castle
    [],[],"outer_terrain_beach_desert"),
  ("castle_8_interior",sf_indoors, "arabian_interior_keep_b2", "bo_arabian_interior_keep_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("castle_8_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("castle_11_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130025cb20006097f00005b1400000e2f00005fd9", #brytenwalda hillfort
    [],[],"outer_terrain_plain"),
  ("castle_11_interior",sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("castle_11_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("castle_12_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0", #bry old roman castrum
    [],[],"outer_terrain_plain"),
  ("castle_12_interior",sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("castle_12_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_34_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000500000d234800003d64000017f800003012", #ettenrocal roman castle
    [],[],"outer_terrain_plain"),

  #castle 34 variants - base scene by ettenrocal, improved by InVain
  #high tower variants
  ("castle_34_exterior_gate",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000500000d234800003d64000017f800003012", 
    [],[],"outer_terrain_plain"), #unused
  ("castle_34_exterior_ladder",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000500000d234800003d64000017f800003012", 
    [],[],"outer_terrain_plain"),  #Brigetio

  ("castle_34_exterior_var1_ladder_medi",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000500000d234800003d64000017f800003012", 
    [],[],"sea_outer_terrain_3"), #seaside west, Pollentia
  ("castle_34_exterior_var1_ladders",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000500000d234800003d64000017f800003012", 
    [],[],"outer_terrain_plain"), #unused

  ("castle_34_exterior_var2_gate",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003a0000500000d234800003d64000017f800003012", 
    [],[],"outer_terrain_castle_9"), #Theodosiopolis = Erzurum
  ("castle_34_exterior_var2_gate_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000500000d234800003d64000017f800003012", 
    [],[],"outer_terrain_plain"), #Avaricum

  #low tower variants from here
  ("castle_34_exterior_var3_2gates",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000500000d234800003d64000017f800003012", 
    [],[],"outer_terrain_plain"), #brigetio

    #ladder attack from the side
  ("castle_34_exterior_var4_ladders",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000500000d234800003d64000017f800003012", 
    [],[],"outer_terrain_castle_9"), #unused
  ("castle_34_exterior_var4_ladders_desert",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000350000500000d234800003d64000017f800003012", 
    [],[],"outer_terrain_desert"), #Castellum_Dimmidi
  ("castle_34_exterior_var4_ladders_medi",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000500000d23480000365e000017f800003012", 
    [],[],"outer_terrain_plain"), #unused
  ("castle_34_exterior_var4_ladders_medi_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000500000d234800003d64000017f800003012", 
    [],[],"outer_terrain_plain"), #unused
  ("castle_34_exterior_var4_ladders_medi_city",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000500000d234800003d64000017f800003012", 
    [],[],"outer_terrain_plain"), #unused

  ("castle_34_exterior_var5_gate",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000500000d234800003d64000017f800003012", 
    [],[],"outer_terrain_plain"), #unused
  ("castle_34_exterior_var5_gate_medi",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000500000d234800003d64000017f800003012", 
    [],[],"outer_terrain_castle_9"), #Dariunk, Armenia
  ("castle_34_exterior_var5_gate_medi_city_harbour",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003a0000500000d234800003d64000017f800003012",
    [],[],"outer_terrain_beach"),
  ("castle_34_exterior_var5_gate_medi_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000500000d234800003d64000017f800003012",
    [],[],"outer_terrain_plain"), #Scallabis
  ("castle_34_exterior_var5_gate_medi_town_harbour",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000500000d234800003d64000017f800003012", 
    [],[],"outer_terrain_beach"),
  ("castle_34_exterior_var5_gate_medi_town_seaside",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000500000d234800003d64000017f800003012",
    [],[],"outer_terrain_beach"),
  ("castle_34_exterior_var5_gate_desert_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000350000500000d234800003d64000017f800003012", 
    [],[],"outer_terrain_desert"), #Emesa
  ("castle_34_exterior_var5_gate_desert",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000350000500000d234800003d64000017f800003012", 
    [],[],"outer_terrain_desert"), #unused


  ("castle_34_exterior_var6_ladders_barbarian",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000500000d234800003d64000017f800003012", 
    [],[],"outer_terrain_plain"), #Civitas_Riedonum
  ("castle_34_exterior_var6_ladders_barbarian_village",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000500000d234800003d64000017f800003012", 
    [],[],"outer_terrain_plain"), #Petuaria
  ("castle_34_exterior_var7_ladders_ruined_barbarian",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000500000d234800003d64000017f800003012", 
    [],[],"outer_terrain_plain"), #Savaria
  ("castle_34_exterior_var7_ladders_ruined_barbarian_village",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000500000d234800003d64000017f800003012", 
    [],[],"outer_terrain_plain"), #Bagacum; Segontium
  ("castle_34_exterior_var8_gate_barbarian",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003a0000500000d234800003d64000017f800003012", 
    [],[],"outer_terrain_beach_rotated"), #olbia
  ("castle_34_exterior_var8_gate_barbarian_village",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000330000500000d234800003d64000017f800003012", 
    [],[],"outer_terrain_plain"), #Colonia_Ulpia_Traiana

  ("castle_34_interior",sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("castle_34_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("castle_40_exterior_var1_gate",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000370e000002236000043df0000369c", #roman desert castle by me (sorta shitty) #InVain: not shitty it all, use as a generic fort instead
    [],[],"outer_terrain_plain"), #unused
    #InVain: Variants
  ("castle_40_exterior_var1_ladders",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000370e000002236000043df0000369c", 
    [],[],"outer_terrain_plain"), #unused
  ("castle_40_exterior_var2_gate_medi_town_harbour",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000370e000002236000043df0000369c", 
    [],[],"outer_terrain_beach_med"), #Icosium, Kydonia
  ("castle_40_exterior_var2_gate_village",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000370e000002236000043df0000369c", 
    [],[],"outer_terrain_plain"), #Castra_Regina
  ("castle_40_exterior_var2_gate_village_medi",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000370e000002236000043df0000369c", 
    [],[],"outer_terrain_plain"), #Scupi
  ("castle_40_exterior_var3_ladders",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000370e000002236000043df0000369c", 
    [],[],"outer_terrain_plain"), #unused
  ("castle_40_exterior_var3_ladders_sinope",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000a0000500000370e000002236000043df0000369c", 
    [],[],"sea_outer_terrain_2"), #Sinope
  ("castle_40_exterior_var3_ladders_village_medi",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000a0000500000370e000002236000043df0000369c", 
    [],[],"outer_terrain_plain"), #unused
  ("castle_40_exterior_var4_ladders",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000370e000002236000043df0000369c", 
    [],[],"outer_terrain_plain"), #unused
  ("castle_40_exterior_var5_ladders_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000370e000002236000043df0000369c", 
    [],[],"outer_terrain_plain"), #Genava, Augusta_Treverorum
  ("castle_40_exterior_var5_ladders_town_medi",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000a0000500000370e000002236000043df0000369c", 
    [],[],"outer_terrain_plain"), #Siscia, Nicaea
  ("castle_40_exterior_var6_gate_town_medi",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000370e000002236000043df0000369c", 
    [],[],"outer_terrain_desert"), #Edessa, Ptolemais
  ("castle_40_exterior_var7_gate_city_medi_harbour",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000370e000002236000043df0000369c", 
    [],[],"outer_terrain_beach_rotated"), #harbour city south

  ("castle_40_interior",sf_indoors, "arabian_interior_keep_b2", "bo_arabian_interior_keep_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("castle_40_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("castle_42_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001a00005000005695c00001ebe0000028e00007e37", #levente's donated persian fortress
    [],[],"outer_terrain_desert"),
  ("castle_42_interior",sf_indoors, "arabian_interior_keep_b2", "bo_arabian_interior_keep_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("castle_42_prison",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("castle_48_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000a000050000086a1a000077300000250a00005b03", #my sassanid castle
    [],[],"outer_terrain_steppe"),
  ("castle_48_interior",sf_indoors, "arabian_interior_keep_b2", "bo_arabian_interior_keep_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("castle_48_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    [],[]),
    #variants by InVain
  ("castle_59_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000004c13100001d3100006d4100001edd", #roman danube fort, edited by Invain
    [],[],"TLD_outer_terrain_river_middle"), #roman village with bridge; Eburodunum
  ("castle_59_exterior_var0_noriver_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000004c13100001d3100006d4100001edd", 
    [],[],"outer_terrain_plain"), #roman town; Augusta_Suessionum
  ("castle_59_exterior_var0_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000a00005000004c131000073e500006d4100001edd", 
    [],[],"TLD_outer_terrain_river_middle"), #roman town, steppe ground, hilly outer terrain; unused
  ("castle_59_exterior_var0_town_barbarian",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000004c13100001d3100006d4100001edd", 
    [],[],"TLD_outer_terrain_river_middle"), ##Dierna, Durovernum_Cantiacorum
  ("castle_59_exterior_var1_bridge",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000004c13100001d3100006d4100001edd", 
    [],[],"TLD_outer_terrain_river_middle"), #Ioviaco #attack via pontoon bridge

  ("castle_59_exterior_var2_barbarian",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000004c13100001d3100006d4100001edd", 
    [],[],"TLD_outer_terrain_river_middle"), # Avaricum
  ("castle_59_exterior_var2_barbarian_noriver",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000004c13100001d3100006d4100001edd", 
    [],[],"outer_terrain_plain"), #unused
  ("castle_59_exterior_var3_barbarian_steppe_ruined_gate",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000a00005000004c13100001d3100006d4100001edd", 
    [],[],"sea_outer_terrain_2"), #Tanais
  ("castle_59_exterior_var3_barbarian_ruined_gate_noriver",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000004c13100001d3100006d4100001edd", 
    [],[],"outer_terrain_plain"), #Bagacum
  ("castle_59_exterior_var3_barbarian_ruined_ladder",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000004c13100001d3100006d4100001edd", 
    [],[],"TLD_outer_terrain_river_middle"), #Castrum_Rauracense
  ("castle_59_exterior_var3_barbarian_ruined_ladder_noriver",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000004c13100001d3100006d4100001edd", 
    [],[],"outer_terrain_mountain"), #Carredunum   
  ("castle_59_exterior_var4_town_barbarian_noriver",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000004c13100001d3100006d4100001edd", 
    [],[],"outer_terrain_mountain"), #Caranicum
  ("castle_59_exterior_var5_gate",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000004c13100001d3100006d4100001edd", 
    [],[],"TLD_outer_terrain_river_west"), #ex-roman/ barbarian village; Isca_Dumnoniarum
  ("castle_59_exterior_var6_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000004c13100001d3100006d4100001edd", 
    [],[],"TLD_outer_terrain_river_middle"), #roman/barbarian; #Batavis
  ("castle_59_exterior_var7_desert",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500005000004c13100001d3100006d4100001edd", 
    [],[],"outer_terrain_desert"), #Jabiya
    
  ("castle_59_interior",sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("castle_59_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("castle_67_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130025cb20006097f00005b1400000e2f00005fd9", #n. germanic castle thing from brytenwalda
    [],[],"outer_terrain_forest"),
  ("castle_67_interior",sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("castle_67_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("castle_70_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x3189dc1a000429090000619700007cbd00005ab7", #germanic town fort thing from brytenwalda
    [],[],"outer_terrain_plain"),
  ("castle_70_interior",sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("castle_70_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("castle_73_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007b23200049d2a00003c37000040ef000037cd", #bry old roman coastal fort
    [],[],"sea_outer_terrain_1"),
  ("castle_73_interior",sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("castle_73_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_79_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300000000005c577000041ef00005ae800003c55", #from wlod
    [],[],"outer_terrain_plain"), #Tingartia
    #InVain: Desert variants
  ("castle_79_exterior_var1_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500000000005c577000041ef00005ae800003c55",
    [],[],"outer_terrain_desert"), #Gafsa
  ("castle_79_exterior_var1_village",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500000000005c577000041ef00005ae800003c55", 
    [],[],"outer_terrain_desert"), #Cydamus
  ("castle_79_exterior_var2_ladder",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500000000005c577000041ef00005ae800003c55", 
    [],[],"outer_terrain_desert"), #unused
  ("castle_79_exterior_var3_gate",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500000000005c577000041ef00005ae800003c55",
    [],[],"outer_terrain_desert"), #unused
  ("castle_79_exterior_var4_gate_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300000000005c577000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"), ##Volubilis
  ("castle_79_exterior_var4_gate_village",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500000000005c577000041ef00005ae800003c55", 
    [],[],"outer_terrain_desert"), #unused
  ("castle_79_exterior_var4_ladder",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500000000005c577000041ef00005ae800003c55", 
    [],[],"outer_terrain_desert"), #unused
  ("castle_79_exterior_var4_ladder_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500000000005c577000041ef00005ae800003c55", 
    [],[],"outer_terrain_desert"), #Nova_Trajana_Bostra

  ("roman_fortress_exterior_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007858000049d2a00003c37000040ef000037cd", #from levente - river roman fort
    [],[],"outer_terrain_forest"), #Roman river fort by Levente; #Mogontiacum, Bassania

  ("dumatha_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000050044e900003dd02000077b20000400100005697", #from levente - dumatha
    [],[],"outer_terrain_desert"),

  ("tingis_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300000000007f5f7000041ef00005ae800003c55", #from wlod
    [],[],"sea_outer_terrain_3"),

  ("castle_28_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000005f97c00006b860000752a00006d22", #from a dream of eagles - antonis
    [],[],"sea_outer_terrain_1"),

  ("castle_33_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300000000005194a000041ef00005ae800003c55", #from wlod
    [],[],"outer_terrain_plain"),

 # uniques

  ("castle_15_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230029cb2000709c200003c9500004b9b00002f4d", #dun at
    [],[], "outer_terrain_plain"),
  ("castle_15_interior",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_15_seneschal"]),
  ("castle_15_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_60_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130000500000aa2a8000035b600002c1b00002af9", #Asturica_Augusta - Viladonga castrum
    [],[],"outer_terrain_forest"),

  ("castle_63_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000007a2600c0000054150000075280000575900001853", #ujarma
    [],[],"outer_terrain_steppe"),
  ("castle_63_interior",sf_indoors, "dungeon_entry_a", "bo_dungeon_entry_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_63_seneschal"]),
  ("castle_63_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_64_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000ad340004d537000024650000253c00000461", #phasis
    [],[],"outer_terrain_plain"),
  ("castle_64_interior",sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_64_seneschal"]),
  ("castle_64_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_66_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230000500000759d600000529000064e800003cb9", #ubrzis - by maxi
    [],[],"outer_terrain_plain"),
  ("castle_66_interior",sf_indoors, "interior_castle_j", "bo_interior_castle_j" , (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_66_seneschal"]),
  ("castle_66_prison",sf_indoors,"interior_prison_m", "bo_interior_prison_m", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_71_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b0000500000775df000051b80000280800001434",
    [],[],"outer_terrain_forest"),
  ("castle_71_interior",sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_71_seneschal"]),
  ("castle_71_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_80_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500000000004b12c000041ef00005ae800003c55", #will replace with levente's african castle
    [],[],"outer_terrain_desert"),
  ("castle_80_interior",sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_80_seneschal"]),
  ("castle_80_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_84_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98d0005b56d000072a70000240a00001e09",
    [],[],"outer_terrain_forest"),


  ("castle_27_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002541c00062d8b00000a01000068cb00006d9b",
    [],[],"outer_terrain_plain"),
  ("castle_27_interior",sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("castle_27_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_41_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013005213200077dda0000733300002edf000052ba",
    [],[],"outer_terrain_plain"),
  ("castle_41_interior",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("castle_41_prison",sf_indoors,"interior_prison_h", "bo_interior_prison_h", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("venedi_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000220000500000d23480000540b000076c900003f3f", #dunepru scene, now reused for castle
    [],[],"outer_terrain_forest"),

  # == Villages ==
  #Roman village templates:
  ("village_roman_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000003a8ea00006acd0000637600004d7f", #village_125
    [],[], "outer_terrain_plain"),
  ("village_roman_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000003ccf300005ffe0000621800003824", #village_196
    [],[],"outer_terrain_plain"),
  ("village_roman_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000004c13100001d3100006d4100001edd", #village_18
    [],[],"outer_terrain_plain"),

  ("village_roman_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300000000005194a000041ef00005ae800003c55", #coastal
    [],[],"outer_terrain_beach"),
  ("village_roman_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300000000005194a000041ef00005ae800003c55", #northern african village?
    [],[],"outer_terrain_plain"),
  ("village_roman_6",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300000000005194a000041ef00005ae800003c55", #city like village
    [],[],"outer_terrain_plain"),
  # germanic/generic village templates
  ("village_generic_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023009629a0005615800005564000023590000579e", #village_192
    [],[],"outer_terrain_plain"),
  ("village_generic_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023009629a0005615800005564000023590000579e", #village_175, has small fort
    [],[],"outer_terrain_plain"),
  ("village_generic_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300022a60005314c0000428100007e0100002e97", #village_49
    [],[],"outer_terrain_plain"),
  ("village_generic_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300410320005a96800006b5300004edc00000d11", #village_20
    [],[],"outer_terrain_plain"),
  ("village_generic_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300621b100051d47000034e300007926000048d3", #village_164
    [],[],"outer_terrain_plain"),
  ("village_generic_6",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013005dad40005f57b0000543e0000279d000052b4", #village_10
    [],[],"outer_terrain_plain"),
  # brytenwalda
  ("village_generic_7",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002541c00062d8b00000a01000068cb00006d9b", #village_74
    [],[],"outer_terrain_plain"),
  ("village_generic_8",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b", #village_10
    [],[],"outer_terrain_plain"),
  ("village_generic_9",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000004300005008005b57000004e31800017d80000754b", #village_112
    [],[],"outer_terrain_plain"),
  ("village_generic_10",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230020a008005294c000063fc0000771c0000216f", #village_149
    [],[],"outer_terrain_plain"),
  # rafa's maps -- thank you!
  ("village_generic_11",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000006218900004315000047030000587e",
    [],[],"outer_terrain_forest"),
  ("village_generic_12",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300005000007f9fc0000207400004aa000005d32", #saxon village
    [],[],"outer_terrain_forest"),

  # dacian borbor/Romanius scene
  ("village_generic_13",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300000000001a86b000041ef00005ae800003c55", #saxon village
    [],[],"outer_terrain_forest"),

  #Eastern steppe/plains - caucasia, sassanid
  ("village_eastern_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000022007a7b200045d19000004920000076d00003b0a", #village_76
    [],[],"outer_terrain_steppe"),
  ("village_eastern_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012007a3df0004e52b0000167700005180000051ea", #village_45
    [],[],"outer_terrain_steppe"),
  #Desert villages - Mauri, Arabs, Sassanids, Vandals (ish)
  ("village_desert_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11", #village_113
    [],[],"outer_terrain_desert"),
  ("village_desert_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11", #village_252
    [],[],"outer_terrain_desert"),
  #saved for specific locations
  ("village_desert_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11", #village_102
    [],[],"outer_terrain_desert"),
  ("village_desert_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11", #village_101
    [],[],"outer_terrain_desert"),

  ("village_garamantian",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002562005000008da3800006e27000071660000587a", #from maxi
    [],[],"outer_terrain_desert"),
  # steppe villages
  ("village_steppe_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200213e300077ddf000019d3000034520000626e", #village_168
    [],[],"outer_terrain_steppe"),
  # special/specific villages
  ("village_13",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000004c13100001d3100006d4100001edd",
    [],[], "outer_terrain_plain"),
  ("village_14",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230029ce30004912400002acc000040d7000077db",
    [],[], "outer_terrain_plain"),
  ("village_60",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000004c13100001d3100006d4100001edd",
    [],[],"outer_terrain_plain"),
  ("village_65",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013004d8320006358b00006d2b000005d5000023e5",
    [],[],"outer_terrain_plain"),
  ("village_87",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98a0004dd3000001a5e00005c6200001ec9",
    [],[],"outer_terrain_plain"),
  ("village_91",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_desert"),
  ("village_94",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_desert"),
  ("village_97",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_desert"),
  ("village_100", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000220000500000811ff000072770000522d00001d47",
    [],[], "outer_terrain_steppe"),
  ("village_109",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_desert"),
  ("village_110",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_desert"),
  ("village_150",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000003ccf300005ffe0000621800003824",
    [],[],"outer_terrain_plain"),

  ("memphis",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000002019098000046917000041010000386000003a38",
    [],[], "outer_terrain_desert"),

  ("field_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033a059a5a0009525600002005000060e300001175",
    [],[],"outer_terrain_plain"),
  ("field_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033a079a3f000a3a8000006dfd000030a100006522",
    [],[],"outer_terrain_steppe"),
  ("field_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30054da28004050000005a76800022aa00002e3b",
    [],[],"outer_terrain_steppe"),
  ("field_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30054da28004050000005a76800022aa00002e3b",
    [],[],"outer_terrain_steppe"),
  ("field_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30054da28004050000005a76800022aa00002e3b",
    [],[],"outer_terrain_steppe"),

  ("test2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b0078cb20003fd0000005e480000288c0000286f",
    [],[],"outer_terrain_steppe"),

  ("test3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b00511d98004b12e0000039f00004e6300005c7d",
    [],[],"outer_terrain_plain"),

  # multiplayer
  ("multi_scene_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000050000056d5b00004fb4000069ed00003150",
    [],[],"outer_terrain_plain"),
  ("multi_scene_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005630007d1f800006aba0000574f00001099",
    [],[],"outer_terrain_plain"),
  ("multi_scene_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002e0b20005154500006e540000235600007b55",
    [],[],"outer_terrain_plain"),
  ("multi_scene_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300659630003c8f300003ca000006a8900003c89",
    [],[],"outer_terrain_plain"),
  ("multi_scene_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_6",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300494b200048524000059e80000453300001d32",
    [],[],"outer_terrain_plain"),
  ("multi_scene_7",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130010e0e0005fd84000011c60000285b00005cbe",
    [],[],"outer_terrain_plain"),
  ("multi_scene_8",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000020004db18004611400005c918000397b00004c2e",
    [],[],"outer_terrain_plain"),
  ("multi_scene_9",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000400032320003c0f300001f9e000011180000031c",
    [],[],"outer_terrain_plain"),
  ("multi_scene_10",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003009cde1000599630000423b00005756000000af",
    [],[],"outer_terrain_plain"),
  ("multi_scene_11",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af",
    [],[],"outer_terrain_plain"),
  ("multi_scene_12",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003d7e30005053f00003b4e0000146300006e84",
    [],[],"outer_terrain_beach"),
  ("multi_scene_13",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_14",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000040000c910003e8fa0000538900003e9e00005301",
    [],[],"outer_terrain_plain"),
  ("multi_scene_15",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500b1d158005394c00001230800072880000018f",
    [],[],"outer_terrain_desert"),
  ("multi_scene_16",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000d007abd20002c8b1000050c50000752a0000788c",
    [],[],"outer_terrain_desert"),
  ("multi_scene_17",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_plain"),
  ("multi_scene_18",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x00000000b00037630002308c00000c9400005d4c00000f3a",
    [],[],"outer_terrain_plain"),
  ("multi_scene_19",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_20",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002ab630004651800000d7a00007f3100002701",
    [],[],"outer_terrain_plain"),
  ("multi_scene_21",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000040000c910003e8fa0000538900003e9e00005301",
    [],[],"outer_terrain_beach_snowy"),

  ("random_multi_plain_medium",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000001394018dd000649920004406900002920000056d7",
    [],[], "outer_terrain_plain"),
  ("random_multi_plain_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000013a001853000aa6a40004406900002920001e4f81",
    [],[], "outer_terrain_plain"),
  ("random_multi_steppe_medium", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x0000000128601ae300063d8f0004406900002920001e4f81",
    [],[], "outer_terrain_steppe"),
  ("random_multi_steppe_large", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x000000012a00d8630009fe7f0004406900002920001e4f81",
    [],[], "outer_terrain_steppe"),

  ("multiplayer_maps_end",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),

  ("wedding",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0", [],[]),
  ("lair_steppe_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000200c69ac80043d0d0000556b0000768400003ea9",
    [],[],"outer_terrain_steppe"), #a box canyon with a spring? -tents...
  ("lair_taiga_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300000000005194a000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"), #a box canyon with a spring? -tents... - replaced old one with snow with steppe bandit lair
  ("lair_desert_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000200000000005194a000041ef00005ae800003c55",
    [],[],"outer_terrain_desert"), #an encampment in the woods
  ("lair_forest_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b00326d90003ecfb0000657e0000213500002461",
    [],[],"outer_terrain_plain"), #a cliffside ledge or cave overlooking a valley
  ("lair_mountain_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000200434070004450c000022bf00006ad6000060ed",
    [],[],"outer_terrain_steppe"),
  ("lair_sea_raiders",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b00562e200040900000063f40000679f00006cda",
    [],[],"sea_outer_terrain_1"), #the longships beached on a hidden cove
  ("lair_arab_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000005024cd120005595400003882000037a90000673e",
    [],[],"outer_terrain_desert"),


  ("quick_battle_scene_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000023002dee300045d1d000001bf0000299a0000638f",
    [],[], "outer_terrain_plain"),
  ("quick_battle_scene_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0000000250001d630005114300006228000053bf00004eb9",
    [],[], "outer_terrain_desert_b"),
  ("quick_battle_scene_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000023002b76300046d2400000190000076300000692a",
    [],[], "outer_terrain_plain"),
  ("quick_battle_scene_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000025a00f23700057d5f00006d6a000050ba000036df",
    [],[], "outer_terrain_desert_b"),
  ("quick_battle_scene_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012007985300055550000064d500005c060000759e",
    [],[],"outer_terrain_plain"),
  ("quick_battle_maps_end",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),

  ("tutorial_training_ground",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003000050000046d1b0000189f00002a8380006d91",
    [],[], "outer_terrain_plain"),

  ("town_1_room",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_5_room",sf_indoors, "interior_town_house_d", "bo_interior_town_house_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_6_room",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_8_room",sf_indoors, "interior_house_b", "bo_interior_house_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_10_room",sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_19_room",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("meeting_scene_steppe",0,"ch_meet_steppe_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_plain",0,"ch_meet_plain_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_snow",0,"ch_meet_plain_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_desert",0,"ch_meet_desert_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_steppe_forest",0,"ch_meet_steppe_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_plain_forest",0,"ch_meet_plain_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_snow_forest",0,"ch_meet_plain_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_desert_forest",0,"ch_meet_desert_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),

  ("meeting_scene_water",sf_generate|sf_no_horses,"none", "none", (-1000,-1000),(1000,1000), 0,"0x0000000730000500000d23480000035180006c8200004a21",
   [],[],"sea_battle_terrain"),

  ("enterprise_tannery",sf_generate,"ch_meet_steppe_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0x000000012004480500040902000041cb00005ae800000ff5",
    [],[]),
  ("enterprise_winery",sf_indoors,"winery_interior", "bo_winery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_mill",sf_indoors,"mill_interior", "bo_mill_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_smithy",sf_indoors,"smithy_interior", "bo_smithy_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_dyeworks",sf_indoors,"weavery_interior", "bo_weavery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_linen_weavery",sf_indoors,"weavery_interior", "bo_weavery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_wool_weavery",sf_indoors,"weavery_interior", "bo_weavery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_brewery",sf_indoors,"brewery_interior", "bo_brewery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_oil_press",sf_indoors,"oil_press_interior", "bo_oil_press_interior", (-40,-40),(40,40),-100,"0",
    [],[]),


  # == MINOR FACTION SETTLEMENTS ==
  ("aestii_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300000000005194a000041ef00005ae800003c55",
    [],[],"outer_terrain_forest"),
  ("irish_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013005213200077dda0000733300002edf000052ba",
    [],[],"outer_terrain_plain"),
  ("garamantian_town_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001200000000005194a000041ef00005ae800003c55",
    [],[],"outer_terrain_desert"),
  ("dani_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130000100000af2bc00000b5c00003ad100005795",
    [],[],"outer_terrain_plain"),
  ("morden_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300000000005194a000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"),
  ("sporoi_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000007a1e800000b5400003ad100005795",
    [],[],"outer_terrain_forest"),
  ("panticapaeum",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130000500000d2348000078ee00001f09000071c6",
    [],[],"outer_terrain_beach"),
  ("abagasian_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300000000005194a000041ef00005ae800003c55",
    [],[],"sea_outer_terrain_1"),
  ("tauri_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000000000036cd5000041ef00005ae800003c55",
    [],[],"outer_terrain_beach"),
  ("frisian_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300000000005194a000041ef00005ae800003c55",
    [],[],"outer_terrain_beach"),
  ("augundzi_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300000000005194a000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"),
  ("vidivarii_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002a0000500000d234800007d8e00006aca00005ad8",
    [],[],"outer_terrain_plain"),
  ("iberian_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130000500000aa2a8000035b600002c1b00002af9", #shared by both vascones + gallacians for now
    [],[],"outer_terrain_forest"),
  ("saraguroi_town", sf_generate, "none", "none", (0, 0), (220, 220), -100, "0x0000000220000500000811ff00007c1000000733000040f4",
    [], [], "outer_terrain_steppe"),
  ("onoguroi_town", sf_generate, "none", "none", (0, 0), (220, 220), -100, "0x0000000220000500000811ff00007c1000000733000040f4",
    [], [], "outer_terrain_steppe"),
  ("kutriguroi_town", sf_generate, "none", "none", (0, 0), (220, 220), -100, "0x0000000220000500000811ff00007c1000000733000040f4",
    [], [], "outer_terrain_steppe"),
  ("sabiroi_town", sf_generate, "none", "none", (0, 0), (220, 220), -100, "0x0000000220000500000811ff00007c1000000733000040f4",
    [], [], "outer_terrain_steppe"),
  ("minor_roman_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005630007d1f800006aba0000574f00001099",
    [],[],"outer_terrain_plain"),
  ("heruli_town",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030044e900003dd02000077b20000400100005697",
    [],[],"outer_terrain_plain"),

  ("ruins_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000003ccf300007c9a00004ca90000122f",
   [],["bonus_chest_5"], "outer_terrain_plain"),
  ("hidden_forest",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013005dad40005f57b0000543e0000279d000052b4",
    [],[], "outer_terrain_plain"), #chief sot acaba
  ("hidden_fort",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b0000500000380e0000027b5000023b900001596",
   [],[], "outer_terrain_plain"),
  ("holy_lance_cave",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500007630005a56b00006e200000319300002f0b",
   [],["bonus_chest_11"], "outer_terrain_desert"),
  ("court_of_attila",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000005ad6b000063be00001b7300005721",
    [],["bonus_chest_6"], "outer_terrain_plain"),
  ("attila_sword_location",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000002acab0000094d0000144a00003cc5",
    [],[],"outer_terrain_plain"),
  ("waylands_smithy",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000002acab0000094d0000144a00003cc5",
    [],[],"outer_terrain_plain"),
  ("circle_mystic",sf_generate,"none", "none", (0,0),(240,240),-100,"0x00000004300005008005b57000004e31800017d80000754b",
    [],[],"outer_terrain_plain"),
  ("roman_villa",sf_generate,"none", "none", (0,0),(240,240),-100,"0x000000005000050000057d5f0000746000002d2600002d3d", #alexandria roman villa scene
    [],[],"outer_terrain_beach_desert"),
  ("roman_villa_attack",sf_generate,"none", "none", (0,0),(240,240),-100,"0x000000005000050000057d5f0000746000002d2600002d3d", #roman villa under attack for roman pagan quest
    [],[],"outer_terrain_beach_desert"),
  ("mithraeum",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000003f0fc00003b8500005bae00007494", #Mithraeum for roman pagan quest
    [],[],"outer_terrain_plain"),
  ("roman_villa_generic",sf_generate,"none", "none", (0,0),(240,240),-100,"0x00000000300005000003f0fc00003b8500005bae00007494", #generic roman villa scene
    [],[],"outer_terrain_plain"),
  ("abandoned_mithraic_temple",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000003f0fc00003b8500005bae00007494", #abandoned Mithraeum for roman pagan quest
    [],[],"outer_terrain_plain"),
  ("roman_fort",sf_generate,"none", "none", (0,0),(240,240),-100,"0x000000013001b2320004a52900004d390000518c00001ab1",
    [],[],"outer_terrain_plain"),
  ("nubian_bandit_camp",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500005000002e4bd00007bd8000051d300003037",
   [],[], "outer_terrain_desert"),
  ("diocletians_palace",sf_generate,"none", "none", (0,0),(240,240),-100,"0x00000000300005000007d9f600002df30000228200001296",
    [],["bonus_chest_1"],"outer_terrain_beach"),
  ("vidigoias_grave",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000002acab0000094d0000144a00003cc5",
    [],["bonus_chest_2"],"outer_terrain_plain"),
  ("sarmatian_fort",sf_generate,"none", "none", (0,0),(240,240),-100,"0x000000013001b2320004a52900004d390000518c00001ab1",
    [],[],"outer_terrain_plain"),
  ("maxi_roman_villa", sf_generate, "none", "none", (0,0),(100,100),-100,"0x0000000234a01c3c0005e97900002ad30000589000000c2b",
    [],[], "outer_terrain_plain"),
  ("dragons_lair",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003002d0630005a56d00007bbb0000223c00007de0",
    [],[], "outer_terrain_forest"),
  ("roman_villa_city", sf_generate, "none", "none", (0,0),(100,100),-100,"0x00000000300005000003f0fc00003b8500005bae00007494",
    [],[], "outer_terrain_plain"),
  #ambush scene
  ("ambush_plains_forest",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(180,180),-0.5,"0x00000001300410320005a96800006b5300004edc00000d11",
    [],[], "outer_terrain_forest"),
  ("grove_of_nymphs", sf_generate, "none", "none", (0,0),(100,100),-100,"0x00000002300005000005755b000016cc00004d020000497c",
    [],[], "outer_terrain_forest"),
  ("roman_village_battle", sf_generate, "none", "none", (0,0),(100,100),-100,"0x000000003000050080062589000045da00001a300000123f",
    [],[], "outer_terrain_forest"),
  ("silingi_village",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000006218900004315000047030000587e",
    [],[],"outer_terrain_forest"),
  ("venedi_outpost",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000007a1e800000b5400003ad100005795",
    [],[],"outer_terrain_forest"),
  ("noricum_refugee_camp",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000004c13100001d3100006d4100001edd",
    [],[],"outer_terrain_forest"),
  ("abandoned_silver_mine",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b00005000005e5790000371500000e3500000f71",
    [],["silver_mine_chest_1","silver_mine_chest_2"], "outer_terrain_mountain"),
  #cynocephali
  ("wolfmen_lair",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000bc60cbb68005ad6800000a2400005f5c00007f21",
    [],[],"outer_terrain_forest"),
  ("wolfmen_ambush",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000bc66cbe30005d9760000438d00007aec00002978",
    [],[],"outer_terrain_forest"),
  ("wolfmen_raid",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b000056300050d450000700900007d720000684a",
    [],[],"outer_terrain_forest"),
  #black river
  ("black_river_ambush",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000056300053d4f00002f210000542d0000774e", #0x000000003000056380053d4f00002f210000542d0000774e
    [],[],"outer_terrain_river_1"),
  ("black_river_fort",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000563000729cd00006123000057a1000024c8",
    [],[],"outer_terrain_forest"),
  ("black_river_villa",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000715c5000057cd000035390000272c",
    [],[],"outer_terrain_forest"),
  #severinus quest
  ("asturis_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005630007d1f800006aba0000574f00001099", #initial scene
    [],[],"outer_terrain_forest"),
  ("asturis_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005630007d1f800006aba0000574f00001099", #ruins
    [],["bonus_chest_7"],"outer_terrain_forest"),
  ("comagena_church",sf_indoors,"interior_castle_j", "bo_interior_castle_j", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("favianis",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005630007d1f800006aba0000574f00001099",
    [],[],"outer_terrain_forest"),
  ("tiguntia",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000bc6006638005dd770000654f00000c4e0000672b",
    [],[],"outer_terrain_forest"), #severinus quest

  ("christian_monastery",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007a3b20005795e0000706d0000381800000bbc",
    [],[],"outer_terrain_plain"),
  ("fortified_monastery",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000004190600005e5c00000ad3000018b3",
    [],[],"outer_terrain_plain"), #villa for batavis
  ("pagan_grove",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000002acab0000094d0000144a00003cc5",
    [],[],"outer_terrain_plain"),
  ("roman_pagan_temple",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000050000040d030000138400003ec000005815", #unique
    [],[],"outer_terrain_plain"),
  ("fire_temple",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000a000050000048d260000248b00007aa200007107", #unqiue
    [],[],"outer_terrain_steppe"),
  ("christian_monastery_desert",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000005000050000048d260000248b00007aa200007107",
    [],[],"outer_terrain_desert"),
  ("arian_monastery",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007a3b20005795e0000706d0000381800000bbc",
    [],[],"outer_terrain_plain"),
  ("celtic_stone_circle",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000006300654ac00062d910000635800007c9600005d35",
    [],[], "outer_terrain_plain"),
  ("steppe_shrine",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000020000663000521480000559b00006178000063e2",
    [],[], "outer_terrain_steppe"),
  ("siwa",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000025c600606000926470000240d0000747200007110",
    [],[],"outer_terrain_desert"),

  # butters/maxi scenes
  ("german_temple_1", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x00000000bc634eb20003d0f20000135000004cf100002af3",[], [], "outer_terrain_plain"),
  ("german_temple_2", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x00000001bc6170b68003d0f2000062e900007b2500006111",[], [], "outer_terrain_plain"),
  ("german_temple_3", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x000000033a0797428005614e000023608000708d00007a0d",[], [], "outer_terrain_plain"),


  ("duel_plain_forest", sf_generate, "none", "none", (0, 0), (200, 200), -0.5, "0x00000000300005000005495000002ee4000032f600000753",
    [],[], "outer_terrain_plain"),
  ("finnquest_dani_camp", sf_generate, "none", "none", (0, 0), (200, 200), -0.5, "0x00000000300005000005495000002ee4000032f600000753",
    [],[], "outer_terrain_beach"),
  ("cutscene_longboat", sf_generate, "none", "none", (0, 0), (200, 200), -0.5, "0x00000000300005000005495000002ee4000032f600000753",
    [],[], "sea_outer_terrain_1"),
  ("cutscene_longboat_2", sf_generate, "none", "none", (0, 0), (200, 200), -0.5, "0x00000000300005000005495000002ee4000032f600000753",
    [],[], "sea_outer_terrain_2"),
  ("cutscene_longboat_fleet", sf_generate, "none", "none", (0, 0), (200, 200), -0.5, "0x0000000330000500000d23480000766b00001c13000046e9",
    [],[], "sea_outer_terrain_2"),
  ("finns_hall_interior",sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


  ("church", sf_indoors, "interior_prison_cell_a", "bo_interior_prison_cell_a", (-100, -100), (100, 100), -100, "0",
    [], ["bonus_chest_9"]),
  ("imperial_palace", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x00000002300000000004fd4a000041ef00005ae800003c55",
    [], ["bonus_chest_10"], "outer_terrain_plain"),

  ## ernak quest
  ("village_of_lekhs", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x00000000300005000005695d00007fbc00005de100006275",
    [], [], "outer_terrain_mountain"),
  ("ruins_of_olpia_pontica", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x00000000300005000003ccf300007c9a00004ca90000122f",
    [], [], "outer_terrain_plain"),
  ("the_oath", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x000000022000050000049d2a00003c37000040ef000037cd",
    [], [], "outer_terrain_steppe"),
  ("final_battle", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x00000000300005000003ccf300007c9a00004ca90000122f",
    [], [], "outer_terrain_steppe"),

  #madsci VC sea battles
  ("sea_battle",sf_generate|sf_no_horses,"none", "none", (-1000,-1000),(1000,1000), 0,"0x0000000730000500000d23480000035180006c8200004a21",
   [],[],"sea_battle_terrain"),
  ("sea_battle_coast",sf_generate|sf_no_horses,"none", "none", (-1000,-1000),(1000,1000), 0,"0x0000000730000500000d23480000035180006c8200004a21",
   [],[],"sea_outer_terrain_3"),


  ("haddingrs_revenge_beach_battle",sf_generate|sf_no_horses,"none", "none", (-1000,-1000),(1000,1000), 0,"0x00000002b1e005000007a1e800001570000016b500000561",
    [],[],"outer_terrain_beach"),
  ("haddingrs_revenge_forest_hideout",sf_generate|sf_no_horses,"none", "none", (-1000,-1000),(1000,1000), 0,"0x00000000bc6005000004190900007f0a00003c1800001ab3",
    [],[],"outer_terrain_plain_2"),
  ("haddingrs_revenge_sedgean",sf_generate,"none", "none", (-1000,-1000),(1000,1000), 0,"0x00000000300000000005194a000041ef00005ae800003c55",
    [],[],"outer_terrain_plain_2"),
  ("haddingrs_revenge_wangofthus_hall",sf_generate,"none", "none", (-1000,-1000),(1000,1000), 0,"0x000000023000050000076ddb000029ba000027660000651a",
    [],[],"outer_terrain_plain_2"),
  ("haddingrs_revenge_travel_cutscene", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000003c600563000d2348000052d4000067d5000029c1",
    [], [], "outer_terrain_forest"),
  ("haddingrs_aesti_village", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002a0000500000d234800007d8e00006aca00005ad8",
    [], [], "outer_terrain_beach"),
  ("haddingrs_aesti_grove", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000033a0797428005614e000023608000708d00007a0d",
    [], [], "outer_terrain_forest"),
  ("haddingrs_aesti_ambush", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000000300005000007bdef0000750f000056d900005a07",
    [], [], "outer_terrain_forest"),
  ("haddingrs_aesti_trade_post", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000023000050000076ddb000029ba000027660000651a",
    [], [], "outer_terrain_forest"),
  ("haddingrs_final_battle",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-0.5,"0x00000000300005000007bdef0000750f000056d900005a07",
    [],[], "outer_terrain_plain"), #plains
  ("haddingrs_final_battle_duel",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-0.5,"0x00000000300005000007bdef0000750f000056d900005a07",
    [],[], "outer_terrain_plain"), #plains

  # ("haddingrs_aesti_final_battle", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000023000050000076ddb000029ba000027660000651a",
  #   [], [], "outer_terrain_forest"),
]
