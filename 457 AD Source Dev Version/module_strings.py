#-*-coding:utf-8-*-
from module_skills import *
from compiler import *
#SB : skill strings from CC, see bottom
strings = [
  ("no_string", "NO STRING!"),
  ("empty_string", " "),
  ("yes", "Yes."),
  ("no", "No."),
# Strings before this point are hardwired.
  ("blank_string", " "),
  ("ERROR_string", "{!}ERROR!!!ERROR!!!!ERROR!!!ERROR!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!!"),
##  ("none", "none"),
  ("noone", "no one"),
##  ("nothing", "nothing"),
  ("s0", "{!}{s0}"),
  ("blank_s1", "{!} {s1}"),
  ("reg1", "{!}{reg1}"),
  ("s50_comma_s51", "{!}{s50}, {s51}"),
  ("s50_and_s51", "{s50} and {s51}"),
  ("s52_comma_s51", "{!}{s52}, {s51}"),
  ("s52_and_s51", "{s52} and {s51}"),
  ("s5_s_party", "{s5}'s Warband"),
  ("s5_l_party", "{s5}'s Legio"),

  ("given_by_s1_at_s2", "Given by {s1} at {s2}"),
  ("given_by_s1_in_wilderness", "Given by {s1} whilst in the field"),
  ("s7_raiders", "{s7} Raiders"),

  ("bandits_eliminated_by_another", "The troublesome bandits have been eliminated by another party."),
  ("msg_battle_won","Battle won! Press tab key to leave..."),
  ("tutorial_map1","You are now viewing the overland map. Left-click on the map to move your party to that location, enter the selected town, or pursue the selected party. Time will pause on the overland map if your party is not moving, waiting or resting. To wait anywhere simply press and hold down the space bar."),


  ("change_color_1", "{!}Change Color 1"),
  ("change_color_2", "{!}Change Color 2"),
  ("change_background", "{!}Change Background Pattern"),
  ("change_flag_type", "{!}Change Flag Type"),
  ("change_map_flag_type", "{!}Change Map Flag Type"),
  ("randomize", "Randomize"),
  ("sample_banner", "{!}Sample banner:"),
  ("sample_map_banner", "{!}Sample map banner:"),
  ("number_of_charges", "{!}Number of charges:"),
  ("change_charge_1",       "{!}Change Charge 1"),
  ("change_charge_1_color", "{!}Change Charge 1 Color"),
  ("change_charge_2",       "{!}Change Charge 2"),
  ("change_charge_2_color", "{!}Change Charge 2 Color"),
  ("change_charge_3",       "{!}Change Charge 3"),
  ("change_charge_3_color", "{!}Change Charge 3 Color"),
  ("change_charge_4",       "{!}Change Charge 4"),
  ("change_charge_4_color", "{!}Change Charge 4 Color"),
  ("change_charge_position", "{!}Change Charge Position"),
  ("choose_position", "{!}Choose position:"),
  ("choose_charge", "{!}Choose a charge:"),
  ("choose_background", "{!}Choose background pattern:"),
  ("choose_flag_type", "{!}Choose flag type:"),
  ("choose_map_flag_type", "{!}Choose map flag type:"),
  ("choose_color", "{!}Choose color:"),
  ("accept", "{!}Accept"),
  ("charge_no_1", "{!}Charge #1:"),
  ("charge_no_2", "{!}Charge #2:"),
  ("charge_no_3", "{!}Charge #3:"),
  ("charge_no_4", "{!}Charge #4:"),
  ("change", "{!}Change"),
  ("color_no_1", "{!}Color #1:"),
  ("color_no_2", "{!}Color #2:"),
  ("charge", "Charge"),
  ("color", "Color"),
  ("flip_horizontal", "Flip Horizontal"),
  ("flip_vertical", "Flip Vertical"),
  ("hold_fire", "Hold Fire"),
  ("blunt_hold_fire", "Blunt / Hold Fire"),

  ("tutorial_ammo_refilled", "Ammo refilled."),
  ("tutorial_failed", "You have been beaten this time, but don't worry. Follow the instructions carefully and you'll do better next time.\
 Press the Tab key to return to to the menu where you can retry this tutorial."),

  ("tutorial_1_msg_1","{!}In this tutorial you will learn the basics of movement and combat.\
 In Mount&Blade: Warband, you use the mouse to control where you are looking, and W, A, S, and D keys of your keyboard to move.\
 Your first task in the training is to locate the yellow flag in the room and move over it.\
 You can press the Tab key at any time to quit this tutorial or to exit any other area in the game.\
 Go to the yellow flag now."),
  ("tutorial_1_msg_2","{!}Well done. Next we will cover attacking with weapons.\
 For the purposes of this tutorial you have been equipped with bow and arrows, a sword and a shield.\
 You can draw different weapons from your weapon slots by using the scroll wheel of your mouse.\
 In the default configuration, scrolling up pulls out your next weapon, and scrolling down pulls out your shield.\
 If you are already holding a shield, scrolling down will put your shield away instead.\
 Try changing your wielded equipment with the scroll wheel now. When you are ready,\
 go to the yellow flag to move on to your next task."),
  ("tutorial_1_msg_3","{!}Excellent. The next part of this tutorial covers attacking with melee weapons.\
 You attack with your currently wielded weapon by using your left mouse button.\
 Press and hold the button to ready an attack, then release the button to strike.\
 If you hold down the left mouse button for a while before releasing, your attack will be more powerful.\
 Now draw your sword and destroy the four dummies in the room."),
  ("tutorial_1_msg_4","{!}Nice work! You've destroyed all four dummies. You can now move on to the next room."),
  ("tutorial_1_msg_5","{!}As you see, there is an archery target on the far side of the room.\
 Your next task is to use your bow to put three arrows into that target. Press and hold down the left mouse button to notch an arrow.\
 You can then fire the arrow by releasing the left mouse button. Note the targeting reticule in the centre of your screen,\
 which shows you the accuracy of your shot.\
 In order to achieve optimal accuracy, let fly your arrow when the reticule is at its smallest.\
 Try to shoot the target now."),
  ("tutorial_1_msg_6","{!}Well done! You've learned the basics of moving and attacking.\
 With a little bit of practice you will soon master them.\
 In the second tutorial you can learn more advanced combat skills and face armed opponents.\
 You can press the Tab key at any time to return to the tutorial menu."),

  ("tutorial_2_msg_1","{!}This tutorial will teach you how to defend yourself with a shield and how to battle armed opponents.\
 For the moment you are armed with nothing but a shield.\
 Your task is not to attack, but to successfully protect yourself from harm with your shield.\
 There is an armed opponent waiting for you in the next room.\
 He will try his best to knock you unconscious, while you must protect yourself with your shield\
 by pressing and holding the right mouse button.\
 Go into the next room now to face your opponent.\
 Remember that you can press the Tab key at any time to quit this tutorial or to exit any other area in the game."),
  ("tutorial_2_msg_2","{!}Press and hold down the right mouse button to raise your shield. Try to remain standing for twenty seconds. You have {reg3} seconds to go."),
  ("tutorial_2_msg_3","{!}Well done, you've succeeded in defending against an armed opponent.\
 The next phase of this tutorial will pit you and your shield against a force of enemy archers.\
 Move on to the next room when you're ready to face an archer."),
  ("tutorial_2_msg_4","{!}Defend yourself from arrows by raising your shield with the right mouse button. Try to remain standing for twenty seconds. You have {reg3} seconds to go."),
  ("tutorial_2_msg_5","{!}Excellent, you've put up a succesful defence against the archer.\
 There is a reward waiting for you in the next room."),
  ("tutorial_2_msg_6","{!}In the default configuration,\
 the F key on your keyboard is used for non-violent interaction with objects and humans in the gameworld.\
 To pick up the sword on the altar, look at it and press F when you see the word 'Equip'."),
  ("tutorial_2_msg_7","{!}A fine weapon! Now you can use it to deliver a bit of payback.\
 Go back through the door and dispose of the archer you faced earlier."),
  ("tutorial_2_msg_8","{!}Very good. Your last task before finishing this tutorial is to face the maceman.\
 Go through the door now and show him your steel!"),
  ("tutorial_2_msg_9","{!}Congratulations! You have now learned how to defend yourself with a shield and even had your first taste of combat with armed opponents.\
 Give it a bit more practice and you'll soon be a renowned swordsman.\
 The next tutorial covers directional defence, which is one of the most important elements of Mount&Blade: Warband combat.\
 You can press the Tab key at any time to return to the tutorial menu."),

  ("tutorial_3_msg_1","{!}This tutorial is intended to give you an overview of parrying and defence without a shield.\
 Parrying attacks with your weapon is a little bit more difficult than blocking them with a shield.\
 When you are defending with a weapon, you are only protected from one direction, the direction in which your weapon is set.\
 If you are blocking upwards, you will parry any overhead swings coming against you, but you will not stop thrusts or attacks to your sides.\
 Either of these attacks would still be able to hit you.\
 That's why, in order to survive without a shield, you must learn directional defence.\
 Go pick up the quarterstaff by pressing the F key now to begin practice."),
  ("tutorial_3_msg_2","{!}By default, the direction in which you defend (by clicking and holding your right mouse button) is determined by the attack direction of your closest opponent.\
 For example, if your opponent is readying a thrust attack, pressing and holding the right mouse button will parry thrust attacks, but not side or overhead attacks.\
 You must watch your opponent carefully and only initiate your parry AFTER the enemy starts to attack.\
 If you start BEFORE he readies an attack, you may parry the wrong way altogether!\
 Now it's time for you to move on to the next room, where you'll have to defend yourself against an armed opponent.\
 Your task is to defend yourself successfully for twenty seconds with no equipment other than a simple quarterstaff.\
 Your quarterstaff's attacks are disabled for this tutorial, so don't worry about attacking and focus on your defence instead.\
 Move on to the next room when you are ready to initiate the fight."),
  ("tutorial_3_msg_3","{!}Press and hold down the right mouse button to defend yourself with your staff after your opponent starts his attack.\
 Try to remain standing for twenty seconds. You have {reg3} seconds to go."),
  ("tutorial_3_msg_4","{!}Well done, you've succeeded this trial!\
 Now you will be pitted against a more challenging opponent that will make things more difficult for you.\
 Move on to the next room when you're ready to face him."),
  ("tutorial_3_msg_5","{!}Press and hold down the right mouse button to defend yourself with your staff after your opponent starts his attack.\
 Try to remain standing for twentys seconds. You have {reg3} seconds to go."),
  ("tutorial_3_msg_6","{!}Congratulations, you still stand despite the enemy's best efforts.\
 The time has now come to attack as well as defend.\
 Approach the door and press the F key when you see the text 'Next level'."),

  ("tutorial_3_2_msg_1","{!}Your staff's attacks have been enabled again. Your first opponent is waiting in the next room.\
 Defeat him by a combination of attack and defence."),
  ("tutorial_3_2_msg_2","{!}Defeat your opponent with your quarterstaff."),
  ("tutorial_3_2_msg_3","{!}Excellent. Now the only thing standing in your way is one last opponent.\
 He is in the next room. Move in and knock him down."),
  ("tutorial_3_2_msg_4","{!}Defeat your opponent with your quarterstaff."),
  ("tutorial_3_2_msg_5","{!}Well done! In this tutorial you have learned how to fight ably without a shield.\
 Train hard and train well, and no one shall be able to lay a stroke on you.\
 In the next tutorial you may learn horseback riding and cavalry combat.\
 You can press the Tab key at any time to return to the tutorial menu."),

  ("tutorial_4_msg_1","{!}Welcome to the fourth tutorial.\
 In this sequence you'll learn about riding a horse and how to perform various martial exercises on horseback.\
 We'll start by getting you mounted up.\
 Approach the horse, and press the 'F' key when you see the word 'Mount'."),
  ("tutorial_4_msg_2","{!}While on horseback, W, A, S, and D keys control your horse's movement, not your own.\
 Ride your horse and try to follow the yellow flag around the course.\
 When you reach the flag, it will move to the next waypoint on the course until you reach the finish."),
  ("tutorial_4_msg_3","{!}Very good. Next we'll cover attacking enemies from horseback. Approach the yellow flag now."),
  ("tutorial_4_msg_4","{!}Draw your sword (using the mouse wheel) and destroy the two targets.\
 Try hitting the dummies as you pass them at full gallop -- this provides an extra challenge,\
 but the additional speed added to your blow will allow you to do more damage.\
 The easiest way of doing this is by pressing and holding the left mouse button until the right moment,\
 releasing it just before you pass the target."),
  ("tutorial_4_msg_5","{!}Excellent work. Now let us try some target shooting from horseback. Go near the yellow flag now."),
  ("tutorial_4_msg_6","{!}Locate the archery target beside the riding course and shoot it three times with your bow.\
 Although you are not required to ride while shooting, it's recommended that you try to hit the target at various speeds and angles\
 to get a feel for how your horse's speed and course affects your aim."),
  ("tutorial_4_msg_7","{!}Congratulations, you have finished this tutorial.\
 You can press the Tab key at any time to return to the tutorial menu."),
# Ryan END

  ("tutorial_5_msg_1","{!}TODO: Follow order to the flag"),
  ("tutorial_5_msg_2","{!}TODO: Move to the flag, keep your units at this position"),
  ("tutorial_5_msg_3","{!}TODO: Move to the flag to get the archers"),
  ("tutorial_5_msg_4","{!}TODO: Move archers to flag1, infantry to flag2"),
  ("tutorial_5_msg_5","{!}TODO: Enemy is charging. Fight!"),
  ("tutorial_5_msg_6","{!}TODO: End of battle."),

  ("trainer_help_1", "{!}This is a training ground where you can learn the basics of the game. Use W, A, S, and D keys to move and the mouse to look around."),
  ("trainer_help_2", "{!}To speak with the trainer, go near him, look at him and press the 'F' key when you see the word 'Talk' under his name.\
 When you wish to leave this or any other area or retreat from a battle, you can press the TAB key."),

  ("custom_battle_1", "{!}Lord Haringoth of Swadia is travelling with his household knights when he spots a group of raiders preparing to attack a small hamlet.\
 Shouting out his warcry, he spurs his horse forward, and leads his loyal men to a fierce battle."),
  ("custom_battle_2", "{!}Lord Mleza is leading a patrol of horsemen and archers\
 in search of a group of bandits who plundered a caravan and ran away to the hills.\
 Unfortunately the bandits have recently met two other large groups who want a share of their booty,\
 and spotting the new threat, they decide to combine their forces."),
  ("custom_battle_3", "{!}Lady Brina is leading the defense of her castle against a Swadian army.\
 Now, as the besiegers prepare for a final assault on the walls, she must make sure the attack does not succeed."),
  ("custom_battle_4", "{!}When the scouts inform Lord Grainwad of the presence of an enemy war band,\
 he decides to act quickly and use the element of surprise against superior numbers."),
  ("custom_battle_5", "{!}Lord Haeda has brought his fierce huscarls into the south with the promise of plunder.\
 If he can make this castle fall to him today, he will settle in these lands and become the ruler of this valley."),

  ("finished", "(Finished)"),

  ("delivered_damage", "Delivered {reg60} damage."),
  ("archery_target_hit", "Distance: {reg61} yards. Score: {reg60}"),

  ("use_baggage_for_inventory","Use your baggage to access your inventory during battle (it's at your starting position)."),
##  ("cant_leave_now","Can't leave the area now."),
  ("cant_use_inventory_now","Can't access inventory now."),
  ("cant_use_inventory_arena","Can't access inventory in the arena."),
  ("cant_use_inventory_disguised","Can't access inventory while you're disguised."),
  ("cant_use_inventory_tutorial","Can't access inventory in the training camp."),
  ("1_denar", "1 siliqua"),
  ("reg1_denars", "{reg1} siliquae"),
  ("january_reg1_reg2", "January {reg1}, {reg2}"),
  ("february_reg1_reg2", "February {reg1}, {reg2}"),
  ("march_reg1_reg2", "March {reg1}, {reg2}"),
  ("april_reg1_reg2", "April {reg1}, {reg2}"),
  ("may_reg1_reg2", "May {reg1}, {reg2}"),
  ("june_reg1_reg2", "June {reg1}, {reg2}"),
  ("july_reg1_reg2", "July {reg1}, {reg2}"),
  ("august_reg1_reg2", "August {reg1}, {reg2}"),
  ("september_reg1_reg2", "September {reg1}, {reg2}"),
  ("october_reg1_reg2", "October {reg1}, {reg2}"),
  ("november_reg1_reg2", "November {reg1}, {reg2}"),
  ("december_reg1_reg2", "December {reg1}, {reg2}"),

##  ("you_approach_town","You approach the town of "),
##  ("you_are_in_town","You are in the town of "),
##  ("you_are_in_castle","You are at the castle of "),
##  ("you_sneaked_into_town","You have sneaked into the town of "),

  ("town_nighttime"," It is late at night and honest folk have abandoned the streets."),
  ("door_locked","The door is locked."),
  ("castle_is_abondened","The castle seems to be unoccupied."),
  ("town_is_abondened","The town has no garrison defending it."),
  ("place_is_occupied_by_player","The place is held by your own troops."),
  ("place_is_occupied_by_enemy", "The place is held by hostile troops."),
  ("place_is_occupied_by_friendly", "The place is held by friendly troops."),

  ("do_you_want_to_retreat", "Are you sure you want to retreat?"),
  ("give_up_fight", "Give up the fight?"),
  ("do_you_wish_to_leave_tutorial", "Do you wish to leave the tutorial?"),
  ("do_you_wish_to_surrender", "Do you wish to surrender?"),
  ("can_not_retreat", "Can't retreat, there are enemies nearby!"),
##  ("can_not_leave", "Can't leave. There are enemies nearby!"),

  ("s1_joined_battle_enemy", "{s1} has joined the battle on the enemy side."),
  ("s1_joined_battle_friend", "{s1} has joined the battle on your side."),

#  ("entrance_to_town_forbidden","It seems that the town guards have been warned of your presence and you won't be able to enter the town unchallenged."),
  ("entrance_to_town_forbidden","The town guards are on the lookout for intruders and it seems that you won't be able to pass through the gates unchallenged."),
  ("sneaking_to_town_impossible","The town guards are alarmed. You wouldn't be able to sneak through that gate no matter how well you disguised yourself."),

  ("battle_won", "You have won the battle!"),
  ("battle_lost", "You have lost the battle!"),

  ("attack_walls_success", "After a bloody fight, your brave soldiers manage to claim the walls from the enemy."),
  ("attack_walls_failure", "Your soldiers fall in waves as they charge the walls, and the few who remain alive soon rout and run away, never to be seen again."),
  ("attack_walls_continue", "A bloody battle ensues and both sides fight with equal valour. Despite the efforts of your troops, the castle remains in enemy hands."),

  ("order_attack_success", "Your men fight bravely and defeat the enemy."),
  ("order_attack_failure", "You watch the battle in despair as the enemy cuts your soldiers down, then easily drives off the few ragged survivors."),
  ("order_attack_continue", "Despite an extended skirmish, your troops were unable to win a decisive victory."),

  ("join_order_attack_success", "Your men fight well alongside your allies, sharing in the glory as your enemies are beaten."),
  ("join_order_attack_failure", "You watch the battle in despair as the enemy cuts your soldiers down, then easily drives off the few ragged survivors."),
  ("join_order_attack_continue", "Despite an extended skirmish, neither your troops nor your allies were able to win a decisive victory over the enemy."),

  ("siege_defender_order_attack_success", "The men of the garrison hold their walls with skill and courage, breaking the enemy assault and skillfully turning the defeat into a full-fledged rout."),
  ("siege_defender_order_attack_failure", "The assault quickly turns into a bloodbath. Valiant efforts are for naught; the overmatched garrison cannot hold the walls, and the enemy puts every last defender to the sword."),
  ("siege_defender_order_attack_continue", "Repeated, bloody attempts on the walls fail to gain any ground, but too many enemies remain for the defenders to claim a true victory. The siege continues."),


  ("hero_taken_prisoner", "{s1} of {s3} has been taken prisoner by {s2}."),
  ("hero_freed", "{s1} of {s3} has been freed from captivity by {s2}."),
  ("center_captured", "{s2} have taken {s1} from {s3}."),

  ("troop_relation_increased", "Your relation with {s1} has increased from {reg1} to {reg2}."),
  ("troop_relation_detoriated", "Your relation with {s1} has deteriorated from {reg1} to {reg2}."),
  ("faction_relation_increased", "Your relation with {s1} has increased from {reg1} to {reg2}."),
  ("faction_relation_detoriated", "Your relation with {s1} has deteriorated from {reg1} to {reg2}."),
  ("troop_relation_increased_s35", "Your relation with your {s35} has increased from {reg1} to {reg2}."),
  ("troop_relation_detoriated_s35", "Your relation with your {s35} has deteriorated from {reg1} to {reg2}."),

  ("party_gained_morale", "Your party gains {reg1} morale."),
  ("party_lost_morale",   "Your party loses {reg1} morale."),
  ("other_party_gained_morale", "{s1} gains {reg1} morale."),
  ("other_party_lost_morale",   "{s1} loses {reg1} morale."),

  ("qst_follow_spy_noticed_you", "The spy has spotted you! He's making a run for it!"),
#  ("father", "father"),
#  ("husband", "husband"),
#  ("wife", "wife"),
#  ("daughter", "daughter"),
#  ("mother", "mother"),
#  ("son", "son"),
#  ("brother", "brother"),
#  ("sister", "sister"),
#  ("he", "He"),
#  ("she", "She"),
  ("s3s_s2", "{s3}'s {s2}"),
  ("s5_is_s51", "{s5} is {s51}."),
  ("s5_is_the_ruler_of_s51", "{s5} is the ruler of {s51}. "),
##diplomacy start+ make gender correct using reg4
  ("s5_is_a_nobleman_of_s6", "{s5} is a {reg4?noblewoman:nobleman} of {s6}. "),#-- update fix 2011-04-08, ternary was messed up
##diplomacy end+
##  ("your_debt_to_s1_is_changed_from_reg1_to_reg2", "Your debt to {s1} is changed from {reg1} to {reg2}."),

  ("relation_mnus_100", "Vengeful"), # -100..-94
  ("relation_mnus_90",  "Vengeful"),  # -95..-84
  ("relation_mnus_80",  "Vengeful"),
  ("relation_mnus_70",  "Hateful"),
  ("relation_mnus_60",  "Hateful"),
  ##diplomacy start+
  # What the hell?!  These stupid spaces make otherwise-useful constants unusable.
  # Changing them to strip out the space padding.
#  ("relation_mnus_50",  " Hostile"),
#  ("relation_mnus_40",  "  Angry"),
#  ("relation_mnus_30",  "    Resentful"),
#  ("relation_mnus_20",  "      Grumbling"),
#  ("relation_mnus_10",  "        Suspicious"),
#  ("relation_plus_0",   "         Indifferent"),# -5...4
#  ("relation_plus_10",  "          Cooperative"), # 5..14
#  ("relation_plus_20",  "           Welcoming"),
#  ("relation_plus_30",  "            Favorable"),
#  ("relation_plus_40",  "             Supportive"),
#  ("relation_plus_50",  "              Friendly"),
#  ("relation_plus_60",  "               Gracious"),
#  ("relation_plus_70",  "                 Fond"),
#  ("relation_plus_80",  "                  Loyal"),
#  ("relation_plus_90",  "                   Devoted"),
  ("relation_mnus_50",  " Hostile".strip()),
  ("relation_mnus_40",  "  Angry".strip()),
  ("relation_mnus_30",  "    Resentful".strip()),
  ("relation_mnus_20",  "      Grumbling".strip()),
  ("relation_mnus_10",  "        Suspicious".strip()),
  ("relation_plus_0",   "         Indifferent".strip()),# -5...4
  ("relation_plus_10",  "          Cooperative".strip()), # 5..14
  ("relation_plus_20",  "           Welcoming".strip()),
  ("relation_plus_30",  "            Favorable".strip()),
  ("relation_plus_40",  "             Supportive".strip()),
  ("relation_plus_50",  "              Friendly".strip()),
  ("relation_plus_60",  "               Gracious".strip()),
  ("relation_plus_70",  "                 Fond".strip()),
  ("relation_plus_80",  "                  Loyal".strip()),
  ("relation_plus_90",  "                   Devoted".strip()),
  ##diplomacy end+
  ("relation_mnus_100_ns", "{s60} is vengeful towards you."), # -100..-94
  ("relation_mnus_90_ns",  "{s60} is vengeful towards you."),  # -95..-84
  ("relation_mnus_80_ns",  "{s60} is vengeful towards you."),
  ("relation_mnus_70_ns",  "{s60} is hateful towards you."),
  ("relation_mnus_60_ns",  "{s60} is hateful towards you."),
  ("relation_mnus_50_ns",  "{s60} is hostile towards you."),
  ("relation_mnus_40_ns",  "{s60} is angry towards you."),
  ##diplomacy start+ fix preposition
  #("relation_mnus_30_ns",  "{s60} is resentful against you."),
  ("relation_mnus_30_ns",  "{s60} is resentful towards you."),
  ##diplomacy end+
  ("relation_mnus_20_ns",  "{s60} is grumbling against you."),
  ("relation_mnus_10_ns",  "{s60} is suspicious towards you."),
  ##diplomacy start+ fix preposition
  #("relation_plus_0_ns",   "{s60} is indifferent against you."),# -5...4
  ("relation_plus_0_ns",   "{s60} is indifferent towards you."),# -5...4
  ##diplomacy end+
  ("relation_plus_10_ns",  "{s60} is cooperative towards you."), # 5..14
  ("relation_plus_20_ns",  "{s60} is welcoming towards you."),
  ("relation_plus_30_ns",  "{s60} is favorable to you."),
  ("relation_plus_40_ns",  "{s60} is supportive to you."),
  ("relation_plus_50_ns",  "{s60} is friendly to you."),
  ("relation_plus_60_ns",  "{s60} is gracious to you."),
  ("relation_plus_70_ns",  "{s60} is fond of you."),
  ("relation_plus_80_ns",  "{s60} is loyal to you."),
  ("relation_plus_90_ns",  "{s60} is devoted to you."),

  ("relation_reg1", " Relation: {reg1}"),

  ("center_relation_mnus_100", "The populace hates you with a passion"), # -100..-94
  ("center_relation_mnus_90",  "The populace hates you intensely"), # -95..-84
  ("center_relation_mnus_80",  "The populace hates you strongly"),
  ("center_relation_mnus_70",  "The populace hates you"),
  ("center_relation_mnus_60",  "The populace is hateful to you"),
  ("center_relation_mnus_50",  "The populace is extremely hostile to you"),
  ("center_relation_mnus_40",  "The populace is very hostile to you"),
  ("center_relation_mnus_30",  "The populace is hostile to you"),
  ("center_relation_mnus_20",  "The populace is against you"),
  ("center_relation_mnus_10",  "The populace is opposed to you"),
  ("center_relation_plus_0",   "The populace is indifferent to you"),
  ("center_relation_plus_10",  "The populace is acceptive of you"),
  ("center_relation_plus_20",  "The populace is cooperative to you"),
  ("center_relation_plus_30",  "The populace is somewhat supportive of you"),
  ("center_relation_plus_40",  "The populace is supportive of you"),
  ("center_relation_plus_50",  "The populace is very supportive of you"),
  ("center_relation_plus_60",  "The populace is loyal to you"),
  ("center_relation_plus_70",  "The populace is highly loyal to you"),
  ("center_relation_plus_80",  "The populace is devoted to you"),
  ("center_relation_plus_90",  "The populace is fiercely devoted to you"),

  ("town_prosperity_0",   "The poverty of the town of {s60} is unbearable"),
  ("town_prosperity_10",   "The squalorous town of {s60} is all but deserted."),
  ("town_prosperity_20",   "The town of {s60} looks a wretched, desolate place."),
  ("town_prosperity_30",   "The town of {s60} looks poor and neglected."),
  ("town_prosperity_40",   "The town of {s60} appears to be struggling."),
  ("town_prosperity_50",   "The town of {s60} seems unremarkable."),
  ("town_prosperity_60",   "The town of {s60} seems to be flourishing."),
  ("town_prosperity_70",   "The prosperous town of {s60} is bustling with activity."),
  ("town_prosperity_80",   "The town of {s60} looks rich and well-maintained."),
  ("town_prosperity_90",   "The town of {s60} is opulent and crowded with well-to-do people."),
  ("town_prosperity_100",  "The glittering town of {s60} openly flaunts its great wealth."),

  ("village_prosperity_0",   "The poverty of the village of {s60} is unbearable."),
  ("village_prosperity_10",  "The village of {s60} looks wretchedly poor and miserable."),
  ("village_prosperity_20",  "The village of {s60} looks very poor and desolate."),
  ("village_prosperity_30",  "The village of {s60} looks poor and neglected."),
  ("village_prosperity_40",  "The village of {s60} appears to be somewhat poor and struggling."),
  ("village_prosperity_50",  "The village of {s60} seems unremarkable."),
  ("village_prosperity_60",  "The village of {s60} seems to be flourishing."),
  ("village_prosperity_70",  "The village of {s60} appears to be thriving."),
  ("village_prosperity_80",  "The village of {s60} looks rich and well-maintained."),
  ("village_prosperity_90",  "The village of {s60} looks very rich and prosperous."),
  ("village_prosperity_100", "The village of {s60}, surrounded by vast, fertile fields, looks immensely rich."),

  #Alternatives
  ("town_alt_prosperity_0",   "Those few items sold in the market appear to be priced well out of the range of the inhabitants. The people are malnourished, their animals are sick or dying, and the tools of their trade appear to be broken. The back alleys have been abandoned to flies and mangy dogs."),
  ("town_alt_prosperity_20",   "You hear grumbling in the marketplace about the price of everyday items and the shops are half empty. You see the signs of malnourishment on both people and animals, and both buildings and tools suffer from lack of repair. Many may already have migrated to seek work elsewhere."),
  ("town_alt_prosperity_40",   "You hear the occasional grumble in the marketplace about the price of everyday items, but there appear to be a reasonable amount of goods for sale. You see the occasional abandoned building, shop, or cart, but nothing more than the ordinary."),
  ("town_alt_prosperity_60",   "The people look well-fed and relatively content. Craftsmen do a thriving business, and some migrants appear to be coming here from other regions to seek their luck."),
  ("town_alt_prosperity_80",   "The walls, streets, and homes are well-maintained. The markets are thronged with migrants from the nearby regions drawn here by the availability of both goods and work. The rhythm of hammers and looms speak to the business of the artisans' workshops."),

  ("village_alt_prosperity_0",   "Only a handful of people are strong enough to work in the fields, many of which are becoming overgrown with weeds. The rest are weak and malnourished, or have already fled elsewhere. The draft animals have long since starved or were eaten, although a few carcasses still lie on the outskirts, their bones knawed by wild beasts."),
  ("village_alt_prosperity_20",   "Some farmers and animals are out in the fields, but their small numbers suggest that some villagers may be emigrating in search of food. Farm implements look rusty and broken. Brush and weeds seem to be reclaiming some of the outermost fields."),
  ("village_alt_prosperity_40",   "The fields and orchards are busy, with villagers engaged in the tasks of the seasons. Humans and animals alike look relatively healthy and well-fed. However, a small number of the outermost fields are left unsewn, and some walls are in ill repair, suggesting that there are still not quite enough hands to do all the work which needs to be done."),
  ("village_alt_prosperity_60",   "The fields and orchards are humming with activity, with filled sacks of grain and drying meat testifying to the productivity of the village's cropland and pastureland."),
  ("village_alt_prosperity_80",   "The fields and orchards are humming with activity, with freshly dug irrigation ditches suggest that the farmers have enough spare time and energy to expand area under cultivation. Seasonal laborers appear to be flocking here to help with the work and join in the general prosperity."),

  ("oasis_village_alt_prosperity_0",   "The palm groves are virtually abandoned, and the canals which irrigate them are clogged with silt. The handful of villagers you see look malnourished and restless. The draft animals have long since starved or were eaten, although a few carcasses still lie on the outskirts, their bones knawed by the wild jackals of the desert."),
  ("oasis_village_alt_prosperity_20",   "Few villagers can be seen tending to the palm groves, and in places, the desert dunes appear to be encroaching on the gardens. Many of the canals are clogged with silt, and the wells and cisterns are filled with sand."),
  ("oasis_village_alt_prosperity_40",   "Men and women are busy tending the palm groves, climbing to the tops of trees to pollinate the fruit. Healthy animals draw the pumps and wheels that bring water to the fields. Some of the irrigation canals and cisterns, however, could use some maintenance."),
  ("oasis_village_alt_prosperity_60",   "The palm groves and orchards are humming with activity. Farmers call to each other cheerfully from the tops of the trees, where they pollinate the date fruit. The creak of wooden pumps, the bellowing of draft animals, and the rush of flowing water speak of an irrigation system that is thriving under the villagers' attention."),
  ("oasis_village_alt_prosperity_80",   "The palm groves are humming with activity, as farmers load up a bumper crop of dates for sale to the market. Men and women are hard at work digging new wells and canals, to bring additional land under irrigation."),



  ("acres_grain",       "acres of grainfields"),
  ("acres_orchard",     "acres of orchards and vineyards"),
  ("acres_oasis",       "acres of irrigated oasis gardens"),


  ("looms",     		"looms"),
  ("silver_smiths",     "silver smiths"),
  ("boats",     		"boats"),
  ("head_cattle",       "head of cattle"),
  ("head_sheep",        "head of sheep"),

  ("mills",     "mills"),
  ("kilns",     "kilns"),
  ("pans",      "pans"),
  ("deposits",  "deposits"),
  ("hives",     "hives"),
  ("breweries", "breweries"),
  ("presses",   "presses"),
  ("smithies",  "smithies"),
  ("caravans",  "overland caravans"),
  ("traps",     "traps"),
  ("gardens",   "small gardens"),
  ("tanneries", "tanning vats"),

  ("master_miller",  "Master miller"),
  ("master_brewer",  "Master brewer"),
  ("master_presser", "Master presser"),
  ("master_smith",   "Master smith"),
  ("master_tanner",  "Master tanner"),
  ("master_weaver",  "Master weaver"),
  ("master_dyer",    "Master dyer"),



  ("war_report_minus_4",   "we are about to lose the war"),
  ("war_report_minus_3",   "the situation looks bleak"),
  ("war_report_minus_2",   "things aren't going too well for us"),
  ("war_report_minus_1",   "we can still win the war if we rally"),
  ("war_report_0",   "we are evenly matched with the enemy"),
  ("war_report_plus_1",   "we have a fair chance of winning the war"),
  ("war_report_plus_2",   "things are going quite well"),
  ("war_report_plus_3",   "we should have no difficulty defeating them"),
  ("war_report_plus_4",   "we are about to win the war"),


  ("persuasion_summary_very_bad", "You try your best to persuade {s50},\
 but none of your arguments seem to come out right. Every time you start to make sense,\
 you seem to say something entirely wrong that puts you off track.\
 By the time you finish speaking you've failed to form a single coherent point in your own favor,\
 and you realise that all you've done was dig yourself deeper into a hole.\
 Unsurprisingly, {s50} does not look impressed."),
  ("persuasion_summary_bad",      "You try to persuade {s50}, but {reg51?she:he} outmanoeuvres you from the very start.\
 Even your best arguments sound hollow to your own ears. {s50}, likewise,\
 has not formed a very high opinion of what you had to say."),
  ("persuasion_summary_average",  "{s50} turns out to be a skilled speaker with a keen mind,\
 and you can't seem to bring forth anything concrete that {reg51?she:he} cannot counter with a rational point.\
 In the end, neither of you manage to gain any ground in this discussion."),
  ("persuasion_summary_good",     "Through quick thinking and smooth argumentation, you manage to state your case well,\
 forcing {s50} to concede on several points. However, {reg51?she:he} still expresses doubts about your request."),
  ("persuasion_summary_very_good","You deliver an impassioned speech that echoes through all listening ears like poetry.\
 The world itself seems to quiet down in order to hear you better .\
 The inspiring words have moved {s50} deeply, and {reg51?she:he} looks much more well-disposed towards helping you."),


# meet_spy_in_enemy_town quest secret sentences
  ("secret_sign_1",  "The armoire dances at midnight..."),
  ("secret_sign_2",  "I am selling these fine Persian tapestries. Would you like to buy some?"),
  ("secret_sign_3",  "The friend of a friend sent me..."),
  ("secret_sign_4",  "The wind blows hard from the east and the river runs red..."),

  ("countersign_1",  "But does he dance for the dresser or the candlestick?"),
  ("countersign_2",  "Yes I would, do you have any in blue?"),
  ("countersign_3",  "But, my friend, your friend's friend will never have a friend like me."),
  ("countersign_4",  "Have you been sick?"),

# Names
  ("name_1",  "Albard"),
  ("name_2",  "Euscarl"),
  ("name_3",  "Sigmar"),
  ("name_4",  "Talesqe"),
  ("name_5",  "Ritmand"),
  ("name_6",  "Aels"),
  ("name_7",  "Raurqe"),
  ("name_8",  "Bragamus"),
  ("name_9",  "Taarl"),
  ("name_10", "Ramin"),
  ("name_11", "Shulk"),
  ("name_12", "Putar"),
  ("name_13", "Tamus"),
  ("name_14", "Reichad"),
  ("name_15", "Walcheas"),
  ("name_16", "Rulkh"),
  ("name_17", "Marlund"),
  ("name_18", "Auguryn"),
  ("name_19", "Daynad"),
  ("name_20", "Joayah"),
  ("name_21", "Ramar"),
  ("name_22", "Caldaran"),
  ("name_23", "Brabas"),
  ("name_24", "Kundrin"),
  ("name_25", "Pechnak"),

# Surname
  ("surname_1",  "{s50} of Noricum"),
  ("surname_2",  "{s50} of Illyria"),
  ("surname_3",  "{s50} of Hispania"),
  ("surname_4",  "{s50} of Germania"),
  ("surname_5",  "{s50} of Italia"),
  ("surname_6",  "{s50} of the North"),
  ("surname_7",  "{s50} of the South"),
  ("surname_8",  "{s50} of the East"),
  ("surname_9",  "{s50} of the West"),
  ("surname_10", "{s50} of Persia"),
  ("surname_11", "{s50} of Africa"),
  ("surname_12", "{s50} of Rome"),
  ("surname_13", "{s50} of Gaul"),
  ("surname_14", "{s50} of Thrace"),
  ("surname_15", "{s50} of Dacia"),
  ("surname_16", "{s50} the Simpleton"),
  ("surname_17", "{s50} the Short"),
  ("surname_18", "{s50} the Weak"),
  ("surname_19", "{s50} the Strong"),
  ("surname_20", "{s50} Longbeard"),
  ("surname_21", "{s50} the Long"),
  ("surname_22", "{s50} the Gaunt"),
  ("surname_23", "{s50} Silkybeard"),
  ("surname_24", "{s50} the Sparrow"),
  ("surname_25", "{s50} the Pauper"),
  ("surname_26", "{s50} the Scarred"),
  ("surname_27", "{s50} the Fair"),
  ("surname_28", "{s50} the Grim"),
  ("surname_29", "{s50} the Red"),
  ("surname_30", "{s50} the Black"),
  ("surname_31", "{s50} the Tall"),
  ("surname_32", "{s50} Star-Eyed"),
  ("surname_33", "{s50} the Fearless"),
  ("surname_34", "{s50} the Valorous"),
  ("surname_35", "{s50} the Cunning"),
  ("surname_36", "{s50} the Coward"),
  ("surname_37", "{s50} the Bright"),
  ("surname_38", "{s50} the Quick"),
  ("surname_39", "{s50} the Minstrel"),
  ("surname_40", "{s50} the Bold"),
  ("surname_41", "{s50} Hot-Head"),

  ("surnames_end", "surnames_end"),


  ("number_of_troops_killed_reg1", "Number of troops killed: {reg1}"),
  ("number_of_troops_wounded_reg1", "Number of troops wounded: {reg1}"),
  ("number_of_own_troops_killed_reg1", "Number of friendly troops killed: {reg1}"),
  ("number_of_own_troops_wounded_reg1", "Number of friendly troops wounded: {reg1}"),

  ("retreat", "Retreat!"),
  ("siege_continues", "Fighting Continues..."),
  ("casualty_display", "Your casualties: {s10}^Enemy casualties: {s11}{s12}"),
  ("casualty_display_hp", "^You were wounded for {reg1} hit points."),

# Quest log texts
  ("quest_log_updated", "Quest log has been updated..."),

  ("banner_selection_text", "You have been awarded the right to carry a banner.\
 Your banner will signify your status and bring you honour. Which banner do you want to choose?"),


# Retirement Texts: s7=village name; s8=castle name; s9=town name
  ("retirement_text_1", "Only too late do you realise that your money won't last.\
 It doesn't take you long to fritter away what little you bothered to save,\
 and you fare poorly in several desperate attempts to start adventuring again.\
 You end up a beggar in {s9}, living on alms and the charity of the church."),
  ("retirement_text_2", "Only too late do you realise that your money won't last.\
 It doesn't take you long to fritter away what little you bothered to save.\
 Once every siliqua has evaporated in your hands you are forced to start a life of crime in the backstreets of {s9},\
 using your skills to eke out a living robbing coppers from women and poor townsmen."),
  ("retirement_text_3", "Only too late do you realise that your money won't last.\
 It doesn't take you long to fritter away what little you bothered to save,\
 and you end up a penniless drifter, going from tavern to tavern\
 blagging drinks from indulgent patrons by regaling them with war stories that no one ever believes."),
  ("retirement_text_4", "The silver you've saved doesn't last long,\
 but you manage to put together enough to buy some land near the village of {s7}.\
 There you become a free farmer, and you soon begin to attract potential {wives/husbands}.\
 In time the villagers come to treat you as their local hero.\
 You always receive a place of honour at feasts, and your exploits are told and retold in the pubs and taverns\
 so that the children may keep a memory of you for ever and ever."),
  ("retirement_text_5", "The silver you've saved doesn't last long,\
 but it's enough to buy a small tavern in {s9}. Although the locals are wary of you at first,\
 they soon accept you into their midst. In time your growing tavern becomes a popular feasthall and meeting place.\
 People come for miles to eat or stay there due to your sheer renown and the epic stories you tell of your adventuring days."),
  ("retirement_text_6", "You've saved wisely throughout your career,\
 and now your silver and your intelligence allow you to make some excellent investments to cement your future.\
 After buying several shops and warehouses in {s9}, your shrewdness turns you into one of the most prominent merchants in town,\
 and you soon become a wealthy {man/woman} known as much for your trading empire as your exploits in battle."),
  ("retirement_text_7", "As a landed noble, however minor, your future is all but assured.\
 You settle in your holdfast at {s7}, administrating the village and fields,\
 adjudicating the local courts and fulfilling your obligations to your liege lord.\
 Occasionally your liege calls you to muster and command in his campaigns, but these stints are brief,\
 and you never truly return to the adventuring of your younger days. You have already made your fortune.\
 With your own hall and holdings, you've few wants that your personal wealth and the income of your lands cannot afford you."),
  ("retirement_text_8", "There is no question that you've done very well for yourself.\
 Your extensive holdings and adventuring wealth are enough to guarantee you a rich and easy life for the rest of your days.\
 Retiring to your noble seat in {s8}, you exchange adventure for politics,\
 and you soon establish yourself as a considerable power in your liege lord's kingdom.\
 With intrigue to busy yourself with, your own forests to hunt, a hall to feast in and a hundred fine war stories to tell,\
 you have little trouble making the best of the years that follow."),
  ("retirement_text_9", "As a reward for your competent and loyal service,\
 your liege lord decrees that you be given a hereditary title, joining the major nobility of the realm.\
 Soon you complete your investitute as baron of {s7}, and you become one of your liege's close advisors\
 and adjutants. Your renown garners you much subtle pull and influence as well as overt political power.\
 Now you spend your days playing the games of power, administering your great fiefs,\
 and recounting the old times of adventure and glory."),
  ("retirement_text_10", "Though you started from humble beginnings, your liege lord holds you in high esteem,\
 and a ripple of shock passes through the realm when he names you to the hereditary title of {count/countess} of {s9}.\
 Vast fiefs and fortunes are now yours to rule. You quickly become your liege's most trusted advisor,\
 almost his equal and charged with much of the running of his realm,\
 and you sit a throne in your own splendourous palace as one of the most powerful figures in Europe."),


#NPC companion changes begin


# Objectionable actions

# humanitarian
  ("loot_village", "attack innocent villagers"),
  ("steal_from_villagers", "steal from poor villagers"),
  ("rob_caravan", "rob a merchant caravan"), # possibly remove
  ("sell_slavery", "sell people into slavery"),

# egalitarian
  ("men_hungry", "run out of food"), ##Done - simple triggers
  ("men_unpaid", "not be able to pay the men"),
#  ("party_crushed", "get ourselves slaughtered"), ##Done - game menus
  ("excessive_casualties", "turn every battle into a bloodbath for our side"),

# chivalric
  ("surrender", "surrender to the enemy"), ##Done - game menus
  ("flee_battle", "run from battle"), ##Done - game menus
  ("pay_bandits", "pay off common bandits"),

# honest
  ("fail_quest", "fail a quest which we undertook on word of honour"),

# quest-related strings
  ("squander_money", "squander money given to us in trust"),
  ("murder_merchant", "involve ourselves in cold-blooded murder"),
  ("round_up_serfs", "round up serfs on behalf of some noble"),


# Fates suffered by companions in battle
  ("battle_fate_1", "We were separated in the heat of battle"),
  ("battle_fate_2", "I was wounded and left for dead"),
  ("battle_fate_3", "I was knocked senseless by the enemy"),
  ("battle_fate_4", "I was taken and held for ransom"),
  ("battle_fate_5", "I got captured, but later managed to escape"),


# strings for opinion
  ("npc_morale_report", "I'm {s6} your choice of companions, {s7} your style of leadership, and {s8} the general state of affairs"),
  ("happy", "happy about"),
  ("content", "content with"),
  ("concerned", "concerned about"),
  ("not_happy", "not at all happy about"),
  ("miserable", "downright appalled at"),


  ("morale_reg1",    " Morale: {reg1}"),
  ("bar_enthusiastic", "                   Enthusiastic"),
  ("bar_content",      "              Content"),
  ("bar_weary",        "          Weary"),
  ("bar_disgruntled",  "     Disgruntled"),
  ("bar_miserable",    "  Miserable"),


#other strings
  ("here_plus_space", "here "),


#NPC strings
#npc1 = Shimon Ben Mattityahu
#npc2 = Narseh - finished
#npc3 = valentia - done -wlod
#npc4 = Amasten Ou Hiader - done -wlod
#npc5 = sunicas - done -wlod
#npc6 = Wadomar - done -wlod
#npc7 = Ingrid - done -wlod
#npc8 =
#npc9 = Thalassius
#npc10 = Aistulf - finished
#npc11 = Alodia - done -wlod
#npc12 = Artemios - finished
#npc13 = Eirpanome
#npc14 = Comminus - finished
#npc15 = Marcus Lincinus Poscas - done
#npc16 = Shapurdukhtak - needs work and rename
#npc17 = Alachis - done -wlod
#npc18 = Khaetag - done -wlod
#npc25 - Iohannes - oliver
#npc25 - Babai - done wlod
#npc26 - amasten - done discord member
#npc27 - rabia - done discord member
#npc28 - ladislaus - done adrian
#npc29 - alexius - done discord member

  ("npc1_intro", "Shalom and may your road always be prosperous, besiyata dishmaya!. Are you looking for an experienced sailor and a man who is blessed by Yahweh? If you are you have found your man, I also have some knowledge about trading and exchanging of goods, prices, spices and so on. Once you are a sailor for long enough you start to learn about all and of course I as an educated man wishing to learn more, and as I said I can also administer spiritual help to your men."),
  ("npc2_intro", "Hello. Would you be so kind as to have a cup with me?"),
  ("npc3_intro", "Salve!"),
  ("npc4_intro", "Tell me stranger, are you a friend of those strawhead Vandals and Germanic thieves? Are you a kisser of the boots that trample around my homeland and cause distress to my people? Answer me before I impale you with my spear!"),
  ("npc5_intro", "Ayoi! Hail from the steppes to you, warrior! What do you seek?"),
  ("npc6_intro", "Hail to you, oh valorous one! Let me steal you few seconds of your time, I am Wadomar, son of Visimar, son of Radagaisus! Yes, that Radagaisus!"),
  ("npc7_intro", "I'm selling hides, need any?"),
  ("npc8_intro", "Ahlan wa sahlan! You seem to be an adventurer, I am a bit of that too, but my story is much sadder than you may think, don't be fooled by my clothing, I am not that well-off right now. The jinns have cursed me and so have many men too for my early life was too much for those around me. Care to hear how I ended up here after walking the deserts for many moons?"),
  ("npc9_intro", "You there, good {man/woman}, be so kind as to fetch me another drink, eh?"),
  ("npc10_intro", "Greetings, {brother/sister}! Let's drink!"),
  ("npc11_intro", "Greetings, what brings you here?"),
  ("npc12_intro", "Greetings, fellow traveller. I noticed your wounded arm, let me look at it."),
  #("npc13_intro", "Greetings, traveller. I am Justin. No doubt you will have heard of me, especially in Constantinople."),
  ("npc13_intro", "Greetings! My bow and my eyes are for hire. Hire me!"),
  ("npc14_intro", "Yes? What is it you wish?"),
  ("npc15_intro", "Oh! Say, friend, are you by chance heading out of town anytime soon?"),
  ("npc16_intro", "Hello there. From the look of you, I'd say you're expecting to get into some fights in the near future. Are you by any chance looking for some help?"),
  ("npc17_intro", "Wes thu hailaz, frawjon! You look sturdy. I was a warrior, like you... Once!"),
  ("npc18_intro", "Greetings to you, traveller. Mind offering me some mead?"),
  ("npc19_intro", "Bo'g z wami!!"),
  ("npc20_intro", "Hello there."),
  ("npc21_intro", "Maska agro!"),
  ("npc22_intro", "Vanity... all is vanity, all is lost, so hopelessly lost, there is no hope for any of us..."),
  ("npc23_intro", "Me mou tous kuklous taratte! I am about to find out a mathematical solution to this problem that has pestered me and I'm trying to read this philosophical text by the great Proclus! I'd appreciate that a plebian and a barbarian like you does not bother me..."),
  ("npc24_intro", "If you are another priest or a beggar come to ask me for blessings or coins, leave before I run you through with my sword, I want to be left in peace when I am drinking my mead!"),
("npc25_intro",
 "Greetings, traveler. I am Babai, son of Benga, leader of the Iazyges. My father commands our people between the Tissus and the Danubius, but I seek to see the world and prove myself worthy of leading one day."),

("npc26_intro", "Christ's blessing on you if you are a righteous and right-thinking Christian, endless curses if you are one of those vile pagans or infidels who shall soon die by the wrath brought on by God!"),
("npc27_intro", "Hail, traveller. I am Harva, of the Phinnoi, kinsman to Valta of Järvi. I have fought the Swehanaz along the icy rivers and bled beneath the cold stars. Might you be in need of a loyal spear?"),
("npc28_intro", "Peace be upon you, stranger. I am Malzam of the Baquates, rider of the Maure plains, son of the red dust and the burning wind. Might you have need of a strong arm and a loyal heart?"),
  ("npc29_intro", "Greetings, traveler. I am Sultana, daughter of no renown, born and raised in the streets of Ctesiphon. Might I have a word with you?"),
("npc30_intro", "Greetings, traveler. I am Barzabod, once an officer of the Shah's cavalry, now a free man seeking worthy employment."),

  ("npc1_intro_response_1", "So you are a rabbi, aspiring merchant and a sailor, hmm useful traits, spirituality may not help against swords, but I could still think I might have use for you. Anything more you can tell me about yourself?"),
  ("npc2_intro_response_1", "It'd be impolite to refuse such polite request."),
  ("npc3_intro_response_1", "Salve. What's a young woman like you doing in a place like this?"),
  ("npc4_intro_response_1", "Easy there! I'm not a comrade to them and I am more interested in fighting against them than being their friend, lower your spear, man."),
  ("npc5_intro_response_1", "My name is {playername}, and what is yours?"),
  ("npc6_intro_response_1", "The Radagaisus who invaded Italy, fifty years ago?"),
  ("npc7_intro_response_1", "No, not really. What does a lone woman do here? And why are you armed? This is indeed a strange sight."),
  ("npc8_intro_response_1", "Yes! I am always ready to hear a good story even if it is not a happy one, please continue."),
  ("npc9_intro_response_1", "You must have me confused with the tavernkeep."),
  ("npc10_intro_response_1", "That's something I'll never refuse."),
  ("npc11_intro_response_1", "Hunger, mainly. Plus, there's always some interesting fella to meet in the taverns."),
  ("npc12_intro_response_1", "What, are you a medicus? Very well then, take a look."),
  ("npc13_intro_response_1", "What's your name, warrior? You're clearly not from here."),
  ("npc14_intro_response_1", "To pass the time of day with a fellow traveller, if you permit."),
  ("npc15_intro_response_1", "I am. What concern is it of your, may I ask?"),
  ("npc16_intro_response_1", "I could be. What's your story?"),
  ("npc17_intro_response_1", "I am. I fare well with the weapons... And you?"),
  ("npc18_intro_response_1", "I have some spare coins... But you might as well share some tales to repay me."),
  ("npc19_intro_response_1", "Excuse me?"),
  ("npc20_intro_response_1", "Hello!"), #I don't need anything special for her intro, she's recieved via quest
  ("npc21_intro_response_1", "Excuse me?"),
  ("npc22_intro_response_1", "Are you reciting poetry or why the melancholy, my good man, you seem well dressed and rich."),
  ("npc23_intro_response_1", "Geia sou! You are a learned man I see, I too am interested about the works of old masters, Hippocrates, Aristofanes... and others, may I know a bit more about you?"),
  ("npc24_intro_response_1", "I am neither. I am looking for warriors and companions."),
("npc25_intro_response_1", "A noble ambition, Babai. You sound like a young man with much to learn but plenty of potential. Tell me more about yourself."),
("npc26_intro_response_1", "You are a bit radical, aren't you? Well, I can listen to your reasoning at least. "),
("npc27_intro_response_1", "You sound like a man who's seen his share of war. Tell me more about yourself."),
("npc28_intro_response_1", "You seem well-spoken for a desert warrior. Tell me more of yourself, Malzam."),
  ("npc29_intro_response_1", "A woman, alone? That is rare... what brings you here?"),
("npc30_intro_response_1", "An officer of the Shah? What brings you so far west?"),

  ("npc1_intro_response_2", "I've heard that merchants and sailors are sly and ought not to be trusted, what are you then? a Jew, sailor and a thrifty merchant. I believe I will take my leave now before I get any more cheated, good day."),
  ("npc2_intro_response_2", "I have better things to do."),
  ("npc3_intro_response_2", "Run along now, girl. I have work to do."),
  ("npc4_intro_response_2", "I indeed believe that Genseric is the rightful king of Africa and that he did no wrong when he crushed your people, it is as simple as the strong ruling and the weak serving. If you wish to test your mettle we can step outside and I will leave you bloody."),
  ("npc5_intro_response_2", "Just mistook you for someone else, nevermind."),
  ("npc6_intro_response_2", "Get lost barbarian, Stilicho should have exterminated all your grandfather's offspring!"),
  ("npc7_intro_response_2", "No, farewell."),
  ("npc8_intro_response_2", "I know this one, you had too much drink, you jumped into the wrong bed, you angered the wrong man and so on. I am not interested, you are of no use to me and you seem like a noble brat and I can't stand them."),
  ("npc9_intro_response_2", "Fetch it yourself!"),
  ("npc10_intro_response_2", "Oh, I'll drink a lot today, but not with you. Get lost."),
  ("npc11_intro_response_2", "I' just hungry. Sorry woman, I need to eat now."),
  ("npc12_intro_response_2", "It's just a flesh wound, no need to bother about it. Mind your own business."),
  ("npc13_intro_response_2", "No, I really don't like you folk from the southern Nile."),
  ("npc14_intro_response_2", "Nothing at all. My apologies."),
  ("npc15_intro_response_2", "I'd be obliged if you minded your own business, sir."),
  ("npc16_intro_response_2", "Mind your own business, lass."),
  ("npc17_intro_response_2", "Sorry, I probably mistook you for someone else."),
  ("npc18_intro_response_2", "Pah, piss off drunkard."),
  ("npc19_intro_response_2", "(telling to yourself) Just a barbarian, let it pass..."),
  ("npc20_intro_response_2", "Not now, maybe later"),
  ("npc21_intro_response_2", "(telling to yourself) What is he even saying?!"),
  ("npc22_intro_response_2", "I have seen enough doomsday prophets to know they are cowards who try to lead people astray and even more, you are annoying me, begone!"),
  ("npc23_intro_response_2", "What an insufferable man you are. The Roman emperors did right when they destroyed the library in Alexandria, who knows how much more annoying you would be if you had fancy scrolls too to spout your rubbish with!"),
  ("npc24_intro_response_2", "We can go outside and test whether your mettle is only good for talking for that's all I am hearing."),
("npc25_intro_response_2", "Another young warrior dreaming of glory. I think I'll pass on this one. Farewell, Babai."),
("npc26_intro_response_2", "You talk a lot, yet I can bet your actions are few. Same with all of you damn fanatics so leave me alone, unless you wish to see God."),
("npc27_intro_response_2", "Keep your spear and your northern frost. I'm not looking for company."),
("npc28_intro_response_2", "I have no use for desert raiders. Be gone, before I set my dogs on you."),
  ("npc29_intro_response_2", "Be gone, woman. This is no place for your kind."),
("npc30_intro_response_2", "I don't trust Persians. Go serve your king somewhere else."),

#backstory intro
  ("npc1_backstory_a", "I am from Cyrenaica, and I am a son of a rabbi and a healer. My father was also a sword-carrying man who had a dream of independent Judea, like in the days of David, Saul and Eshbaal. We have been ruled over by Romans and their pagan ways and now by Christians who I consider to be followers of a false prophet. Their 'leader' Yeshua was just an ordinary man who wanted to bask in the glory of his own making, he was not pious, or a good man and I say the elders were right to condemn him. My father is still alive but forced to live in exile somewhere since he has too many enemies but the dream lives on. My mother was killed while she was outside Alexandria by a Christian mob who had deemed her a witch and 'bad luck' they carved her to pieces, the savages, can you hear from my voice that I am a bit bitter about the fates of my parents? Well wouldn't you be?"),
  ("npc2_backstory_a", "It's always good to meet a friendly face in an unfriendly place."),
  ("npc3_backstory_a", "It's not like I enjoy staying in this place alone... But I have my reasons!"),
  ("npc4_backstory_a", "Hmh... I don't know whether to believe you but I guess I can at least tell you who I am and why I hate the invaders in my dear Africa. I am a son of a Berber tribal chieftain, my dear father fought bravely against the Vandals. He died by treachery, he had issued a challenge to the Vandal rabble warband that he and their leader would duel and if he wins, they would leave. During the night before the duel day, the Vandals snuck near his house and set it ablaze, he perished in the flames, a death not worthy of a warrior. I am trying to find this Vandal leader since my tribe has told me that I am not welcome before the man responsible for my father's fate is dead and his body flayed to feed the crows."),
  ("npc5_backstory_a", "I am Sunicas, a Hunni from the Akatziri tribes. I was born and raised on the steppes as a horseman and a warrior."),
  ("npc6_backstory_a", "That is true! I am grandson to the glorious Radagaisus, who caused much grief to the Romans. My father told me many tales about him, I dream to become as daring and blessed by God as my ancestor was."),
  ("npc7_backstory_a", "I sell hides, meat... That's what I do! And why am I here alone? That is not your businness!"),
  ("npc8_backstory_a", "Very well. My name is Rabi'a ibn Samaw'a. I am the grandson of an Arab king who fell from grace. Since I was just a little habibi I remember very well of being fascinated by the poetry of our storytellers and poets, my uncle introduced me to that school of thought, and I was a great poet by 16. My father Samaw'a was a very strict man and deemed that honor and courtly behavior are vital for a man and that without them you are no man. I was young and foolish, I used to be out for long times, drinking and in general being a nuisance, my father berated me for being a drunk, it was a disgrace to him. In addition my poetry was a bit... uhhmm how do you say? Brave! yes. I wrote about things few would write and that earned my father's anger and he shouted to me that I should write 'more decent' at least. The final straw was that I always appreciated the beauty of the fairer sex and my father was perfectly fine with the idea of trying to find a wife but I was a young man and so I wasn't interested in that. He drove me out after that and declared 'as long as you act like a filthy chelb, I would not be welcome back' So here I am wondering."),
  ("npc9_backstory_a", "My most humble apologies. It is sometimes hard to recognize folk amid the smoke and gloom here. I still cannot believe that I must make my home in such a place."),
  ("npc10_backstory_a", "Haha! That's the spirit! I knew you are someone worthy of my time since I saw you. I'm Aistulf, son of Gaidoald, and I see a warrior in front of me - I mean a true warrior not like those meek limitanei. Someone I was looking for. Give me gold, and I'll kill, burn and steal for you."),
  ("npc11_backstory_a", "That's very true! I myself am an interestin' fella, don't you think?"),
  ("npc12_backstory_a", "Indeed, I was trained how to heal various diseases and wounds. I'm Artemios, son of Agathocles. I'm proud to say I received the best education in Alexandreia and Antiocheia. Let me look at your arm while I tell you more about me..."),
  ("npc13_backstory_a", "Name's is Eirpanome, finest offspring of the Nubian nobility!"),
  ("npc14_backstory_a", "Very well. I do not mind. My name is Rufinius."),
  ("npc15_backstory_a", "I'm an engineer, specialized in the art of fortification. If you need a wall knocked down, I can do that, given enough time. If you need a wall built back up, I can do that too, although it will take longer and cost you more. And you can't cut costs, either, unless you want your new edifice coming down underneath you, as someone around here has just found out."),
  ("npc16_backstory_a", "Well you know, as long as I can remember I've had a weakness for pretty things, and it's gotten me into trouble, you see."),
  ("npc17_backstory_a", "Let me be clear. I'm a warrior, a gasind, I was sworn to a Lord, one of his best men! My name is Alachis, son of Sigmar. Do you want to live? Hire me."),
  ("npc18_backstory_a", "I can give you all the tales you need. I'll take the chance to tell you who I am... My name is Khaetag, son of Ouziagos... Great and noble man among the Alans!"),
  ("npc19_backstory_a", "Well, I... gave you a blessing, I suppose. I wished you to have God on your side."),
  ("npc20_backstory_a", "I am a woman of the Goths. I was raised while our people were ruled over by the Huns. My father was a warrior, following our rulers to conquest and battle."),
  ("npc21_backstory_a", "Worry not, {brother/sister}, I'm simply greeting a fellow traveler, and perhaps I am hoping to steal some of your time."),
  ("npc22_backstory_a", "I am weeping for Rome, for all those who have fallen defending her: Stilicho, Aetius and so many more and even more I weep for I know we Romans no longer have warriors and heroes worthy of Aeneas of old."),
  ("npc23_backstory_a", "Oh! I did not expect to see an educated man in this cesspool of ignorance and all that is vile for a good Greek, such as myself! My name is Helladios, I am a philosopher, merchant and a mathematician and I am trying to bring light to all these savages you see around you, but as of yet I'm having little luck, they do not care, some of them have even been very rude with me, but my intellect is surely greater than theirs combined. Squares, rhombuses, pentagrams... I know these all and I use them to create art and superior structures that are the marvel of the whole world!"),
  ("npc24_backstory_a", "This is not a whorehouse so you won't find company here and judging by the looks of the locals I doubt you will find a warrior from here either, except me. I was born for battle and battle is what I live for, the name is Ladislaus."),
("npc25_backstory_a", "The Iazyges were once the masters of these lands. My ancestors rode with pride, feared by Romans and respected by the steppe tribes. But now, our strength has faded. My father struggles to defend our people against the growing power of the Ostrogoths, and the Huns have weakened us further. ^He hopes I will take his place one day, but I do not wish to lead without proving myself worthy. That is why I am here - to fight, to learn, and to earn the right to rule."),
("npc26_backstory_a", "Radical is the only way to go, Christ drove the swindlers and merchants from the temple, he said he comes with the sword and does not come in peace. I only follow him. My name is Alexius, and I am awoken priest, reborn you could say. For I was not always like this."),
("npc27_backstory_a", "My people live far from the lands of kings and emperors. In Järvi, life is harsh - the wind bites, and the wolves prowl even in daylight. The Swehanaz come from the sea with their long boats, burning homes and taking what little we have. I've met them at the riverbank more times than I can count."),
("npc28_backstory_a", "After the Romans left our lands, they left us no maps, no coin, and no kings - only empty fortresses and broken statues. My tribe, the Baquates, learned to fend for ourselves, trading when we could, fighting when we must."),
  ("npc29_backstory_a", "Yes, I know what I am and where I stand. I am no warrior, and I do not claim to be. But I can serve in other ways. I've cooked for soldiers, tended wounds, managed camps when others fled. That is worth something."),
("npc30_backstory_a", "My days in the army are behind me, but I have not forgotten the art of war. Sword, bow, lance... I have wielded them all in the name of my people. I rode in the plains of Mesopotamia and through the high passes of the Zagros."),

#backstory main body
  ("npc1_backstory_b", "I am no warrior, but I know how to swing a staff and how to defend myself. My staff and faith will keep me safe; don't you worry. Know that if you hire me, I won't stand Christians much. May all their teeth fall out but one so that they may still get a toothache!"),
  ("npc2_backstory_b", "I'm Narseh, from Cteziphon. You've surely heard of this city. I was in charge of a great caravan heading to Constantinopolis. Many goods - silk from far east, ivory from India, olibanum from Arabia... We heard of the bandits preying on our usual route, so this time we tried to outsmart them and use the longer, but safer one, through the wilderness of the desert. A safer one... While trying to avoid few bands of bandits we marched straight into lands of the wild nomads. They killed almost half of the guards and took away a third of the goods. We barely reached the civilized areas of the mediterranean shore."),
  ("npc3_backstory_b", "It's because of my father. He wanted to marry me to a Christian. No one worships the Gods anymore, not along the warm shores of our sea in Mare Nostrum... Which isn't Nostrum anymore, anyway."),
  ("npc4_backstory_b", "Naturally I live by raiding and hunting, I will not take prisoners, my brothers in arms have captured Vandal women as spoils, they marry them and rape them, men are sometimes taken as slaves too. I say all of that is a waste of time, they need to be fed. We ought to just murder every single one of them, make our land like it was before these Vandal bastards."),
  ("npc5_backstory_b", "My people reached these lands from far East with the rest of the Hunni few generations before I was born. I followed Attila in battle, I was one of his retainers and now I am looking for someone as ambitious as the Little Father."),
  ("npc6_backstory_b", "I grew up at Alaric's court of Rex Theodoric in Toulose. He is a great king, and offered many of us, fellow Goths, shelter when my grandfather was killed! My father grew up as Visigoth and so do I, but we do not regret our origins as Eastern Goths that once dwelled the Steppes alongside Alan and Sarmatians, long before the Huns came!"),
  ("npc7_backstory_b", "I'm sorry, I don't even know you yet I spoke harshly. Well, I am here because I am a wretched woman... A dead one. I am merely trying to live day by day, hunting, as my husband taught me... Well, during another life."),
  ("npc8_backstory_b", "I was actually glad to have been freed from the chains of my father and continued my degenerate, uncaring lifestyle, but then about 6 months after my banishment I received a word that my father had been murdered by a rival tribe. Something in me hit that day, I realized that there was more to life than my pursuits of earthly pleasures and that I would need to exact revenge on these donkeys. I swore an oath that I would not drink any wine, would not seduce a single woman or sleep in the same bed for two nights before my father's killers would lie dead."),
  ("npc9_backstory_b", "I was born in Britannia, as son of one of the patricians there. During the troubles over 10 years ago, both my father and I took up arms to defend our home from the pictish invaders. We thought we were to receive aid and soldiers from the Emperor, and be able to defend our homes. We were wrong, and my father was killed in battle, right by my side..."),
  #SB : removed space after s19
  ("npc10_backstory_b", "My tribe lives north of the Alps. We are the Langobardi. They call us savages, but that's because they fear us. Because there's no greater warriors than us! We were forced out of our ancestral lands because of the famine and with every generation we go more and more south. The land we're living now is good, but... who knows where our sons and grandsons will live? I'm young and strong. I wander here and there, learning about other lands, learning about its inhabitants and their strength. I've heard that Italia is rich and I would like to learn more about it, see it for myself."),
  ("npc11_backstory_b", "Maybe you don't know me, but I know you! I saw you and your followers entering the city earlier, this day. Maybe you're looking for someone to manage your stuff in your warband! I have been a merchant most of my life."),
  ("npc12_backstory_b", "Let me see... Just as I thought, it heals well, but it'll heal faster when I apply the maggots. Don't worry, it's a common way to treat wounds like these. I've done it many times when I served as additional medicus in Legio X. They say war is the best school for a physician and I agree with it. I've never seen so many cuts and broken bones before or after. Unfortunately one day the primus pilus became sick. I did everything I could - I poured wax on his belly button, I gave him mercury mixed with lead to swallow, I even secretly sacrificed white hare to the goddess Spes, like all open-minded physicians would do... unfortunately, nothing worked. There's simply nothing more I could've done in his case."),
  #("npc13_backstory_b", "I was a peasant swineherder from Dardania. However, not long ago when I was just a teenager, I and a few companions fled from my home from a barbarian invasion. We came to Constantinople and joined the Excubitors, Emperor Leo's palace guards."),
  ("npc13_backstory_b", "You barbarians from the north don't know us well, but we've been here since the dawn of times, guarding the southern gates of the Niles from you and the Greeks before you! We are hardy warriors, famous for our skills with the bow. Test me on the battlefield, I won't disappoint you."),
  ("npc14_backstory_b", "I am a former Roman Officer. After serving in the wars against Attila, I retired. However, my heart itches to go back into the field of battle."),
  #SB : replace cash with silver
  ("npc15_backstory_b", "The Comes Civitas {s19} in {s20} wanted a new tower added to the wall. Trouble is, he ran out of silver halfway through the process, before I could complete the supports. I told him that it would collapse, and it did. Unfortunately he was standing on it, at the time. The new Comes Civitas didn't feel like honouring his predecessor's debts and implied that I might find myself charged with murder if I push the point."),
  ("npc16_backstory_b", "I grew up in Istakhr, Sasanid Empire, as a bonded servant, working alongside my mother in the kitchens. I would amuse myself by hunting mice through the pantries and sculleries. I was so good at it that I put the castle cats out of a job, and eventually the Argbed realized that I might also be employed to track down bigger game, on certain errands of a type perhaps better left unsaid. Needless to say, I found a number of opportunities to avail myself of trinkets that had formerly belonged to my lord's enemies. So I was able to buy myself out of bondage, and find hire as a free agent. My last job was {s19}in {s20}."),
  ("npc17_backstory_b", "My story? I'm a Lombard, therefore a warrior. I was raised to be one since I was a toddler! My kin was chosen by Godan himself which granted us victory against the Vandals. You wont find better warriors than the Lombards among all the free people of this world... And I do not lie! I never lie."),
  ("npc18_backstory_b", "The steppes are a sea of grass and we, nomads, are particularly good in living there. That harsh land gives us all we need... And when we lacked of something, we simply stole it from someone else! Yes... Stole it, it's the past. Now the Huns, devil creatures, kicked us out of our land, kidnapped our women and destroyed our homes. Can you believe it? We ruled the steppes for centuries before they came. We're now a wretched people... Some of us stayed in the steppes, others... Like the tribe of my father, were forced to move."),
  ("npc19_backstory_b", "My name is Siestrzewit. I know, it sounds terribly to you, it merely means someone who rules over his sister. Regardless of that however, I felt kinda not on great terms with my own one - she definetely took character after our mother, sadly - so I decided to enlist, first in Hunnic horde and then after the leader got his horde destroyed by a Roman patrol, also in Roman service."),
  ("npc20_backstory_b", "While I travelled with my family, I learned how to fight and defend myself, however I have rarely used those skills. I saw the horrors which the huns had released upon the world, and my own people. However, my father was still loyal to them, despite what they had done."),
  ("npc21_backstory_b", "My name is Biankhii, my father named me after one of the Kings of Old Medewi. My father has long since passed, and my mother raised me and my siblings to the best of my abilities. Luckily for me, an old friend of my father took my under his wing and taught me the ways of the Bow. Noobii marksmanship is renown throughout the world, and we have been the bane of empires far older than Rome."),
  ("npc22_backstory_b", "My parents named me Decimus and my soldiers in arms agreed it is a name I deserve. I was born in Rome a long time ago during times when all started to crumble, oh so fast. My parents were rich patricians, my father was a respected veteran from wars against all manner of barbarians. My mother was a healer and tried to keep the old beliefs of Rome alive even during these times when Christ is the ruler. I remember only little of them, a shame. Both died when Alaric and his horde ravaged Rome. I was young and they didn't wish to kill me, perhaps out of pity or out of spite and wanted to leave me to my misery. I was saved by a friendly merchant who was fleeing the city and we managed to avoid the Visigoth patrols and I lived with him until I came to age."),
  ("npc23_backstory_b", "I am originally from Athens. That city has seen better days, where philosophers once debated and great decisions for my dear Hellas were once made. Now it is a city with only boors and uncultured swine and even worse  my brother said that he had seen a... a-a Goth walking down the Tripodon! If Pericles had seen this, oh how much he would've wept. I swore when I finished my studies that I would once again reignite the fire of civilization that would illuminate this darkened world."),
  ("npc24_backstory_b", "I and my family lived far in the east in the tundra, my father was a tribal leader and my mother his concubine, I guess there's no other way to say it. Our village elder told that my father went to even further to the east to fight an evil dragon who had taken up residence in some mountain, I doubt it has any truth, more than likely he got drunk and got killed, like my mother said how he was most of the time. My mother... I have no idea, where she is now, the Huns attacked my village and I only remember that she ran to a forest, and I was separated. There is not a lot of hope of her being alive either, if those cowards didn't get her, the wolves or the weather did."),
("npc25_backstory_b", "I am no stranger to battle. The Iazyges are riders and warriors by tradition, and I have trained with our finest. Yet, I know I lack the experience of true conflict. My father tells me that leadership is more than strength - it is wisdom and courage. I hope to gain those by traveling with a warband such as yours."),
("npc26_backstory_b", "My father I do not know, he left when he was serving in Valentinian's army. I remember only my mother crying that he would never come back, he didn't. My mother yet lives... somewhere but he had to flee because my father's enemies wanted her dead too."),
("npc27_backstory_b", "I learned to fight young. The snow and ice make you tough. But there's only so much glory to win in defending your own. I want to see the world, test myself against foes beyond the north, and make a name worthy of the sagas."),
("npc28_backstory_b", "I was born in Volubilis, though it is no longer a city of marble but of sand and goats. Still, I was raised among warriors - we ride swift horses and throw our javelins truer than any man from the north. I fought against Vandal raiders, and once hunted a Roman deserter across the salt flats."),
  ("npc29_backstory_b", "My brothers wanted me married off to a dull merchant. But I said no. I left. I chose the road, the dust, the campfire smoke. I may not wield a sword, but I've never run from hardship."),
("npc30_backstory_b", "I served honorably, but war does not last forever. I left service to chase a simpler dream: a piece of land in Persis, a good wife, and a house full of children. But dreams need silver... and silver flows in the footsteps of brave men."),

#backstory recruit pitch
  ("npc1_backstory_c", "Know also that any action you take against my people I will not stand for or accept, my people have suffered enough so no need for you to add to that suffering."),
  ("npc2_backstory_c", "And if it were not enough - Ahriman, the evil spirit, sent a storm upon us when our ships left the Antiocheia. All three vessels sank and all our precious cargo was lost. I spent two days drifting until a passing fishermen rescued me. I won't dare to return to Cteziphon. The man who sent me on this voyage would kill me because my life is the only precious thing I have right now and that's the price I'd have to pay. My only chance is to return to him with chests full of gold."),
  ("npc3_backstory_c", "I shall not marry a Christian. Never! I was raised as a Roman woman, loyal to the old Gods. I won't return to my father, I thought his values weren't on sale."),
  ("npc4_backstory_c", "And so no I am travelling between the cities and vistas searching Vandals to kill. But lately the spoils and money has been tight, maybe you could assist me in my mission for revenge!"),
  ("npc5_backstory_c", "In the meantime, any opportunities to earn a living with my sword would be most welcome."),
  ("npc6_backstory_c", "However, I grew tired of staying in Tolosa. There's glory awaiting for me, and my father's name needs to be avenged! I am looking for a daring warlord to serve. Are you the right man, with the right temper?"),
  ("npc7_backstory_c", "I lost everything when a group of Burgundians burned down my village... Sorry, I do not wish to talk about that."),
  ("npc8_backstory_c", "So far I have managed to live my life as I described but it is agony, the sweetness of wine and woman are immense and to forbid these is... it's torture. But if an Arab breaks an oath, he loses all respect and he is like a dog after that, despicable and only worthy of kicks. Maybe you could help me bring the felons to justice, you seem like a well-traveled {man/woman}."),
  ("npc9_backstory_c", "At that point, I knew the battle had been lost, and fled the battlefield. My family's land was ravaged and destroyed by the savages. I have nothing left but my sword... Not even my honor... I have been wandering tavern to tavern, looking for ways I can make a living. I hope to offer my sword to someone worthy, but in the meantime I am condemned to make my bed among thieves, vagabonds, merchants, and the other riff-raff of the road"),
  ("npc10_backstory_c", "I see that you are an adventurer. That you travel and fight a lot. Take me with you and I swear I'll fight for you fiercely as long as you promise me a fair share of loot."),
  ("npc11_backstory_c", "I had my share of fighting in my life, even if I am a woman! Trading is not an easy businness surely not a safe one. Bandits plague these lands and and daring warriors are always looking for caravans without many guards to defend them. So you can trust me when I say I know my share of things!"),
  ("npc12_backstory_c", "He died and all those ignorants suddenly started to blame me for this. And when few hundred men with sharp swords start to blame you for the death of their beloved commander - you know it's time to move elsewhere. I tried to treat wounds in this town, but I'm a bit sick of treating warts on genitals, especially when all those patients scream so loud when I apply glowing-hot iron there. Allow me to join your party and I promise you'll always be treated by a professional."),
  #("npc13_backstory_c", "However, despite all my hardships I have yet to gain any glory; to go out into the chaotic world and prove my worth."),
  ("npc13_backstory_c", "And if you won't... Then to hell you go! You won't find a better archer around, not even among the peoples of the steppes that you so much fear"),
  ("npc14_backstory_c", "So, if you are in need of a good officer and man willing to train your soldiers, you have found him"),
  ("npc15_backstory_c", "More fool me for having taken the contract without an advance, I suppose, but the end of it all is that I'm in a difficult spot, with the roads full of bandits and no money to pay for an escort. So I'd be much obliged if a well-armed party heading out in the next few days could take me along."),
  ("npc16_backstory_c", "Unfortunately, my last employer's wife had a lovely amulet, of a kind I simply could not resist. She doesn't know it's missing, yet, but she might soon. So tell me, are you looking for helpers?"),
  ("npc17_backstory_c", "I can fight with sword and spear, both in formation or challenge our enemy into a deadly duel, you will never see me defeated... Ah! Especially from these very weaklings that live south."),
  ("npc18_backstory_c", "Here I am then... My people is scattered and weak, I can only wish to make a name for myself to clear my family name by the shame of our current conditions. I'm a good tracker, and I fare well with my bow on horse... Have you heard of someone looking for a man like me? You, perhaps?"),
  ("npc19_backstory_c", "There I took a note about Christianity. And converted. Really, teaching of Christus should be spread in my lands more. People should really be more altruistic, honest and good-natured."),
  ("npc20_backstory_c", "However, my father died while following Attila's expedition to gaul, and soon enough Attila took me as his wife. After our wedding night, Attila died in his sleep, from what I saw, a nosebleed. Many of the Hunnic nobles placed the blame on me, so I ran away and took his sword with me. I've been running ever since."),
  ("npc21_backstory_c", "Regardless, I've recently decided to venture into the world in hopes of make a name for myself, and to bring more income to my family back in our village."),
  ("npc22_backstory_c", "Dulce et decorum est pro patria mori, that was what my father taught me, it is a noble phrase, but I must admit our rulers were not noble or very concerned about the state Rome was in. Do you know what Emperor Honorius did? He was shocked because he thought his pet cock had died! That much that bastard cared! We need to rid ourselves of these kinds of useless rulers and restore Rome to her rightful place!"),
  ("npc23_backstory_c", "As I said I am also a travelling merchant, I have been trying to sell my hand-made mathematical instruments and decorative items I have bought to people but imagine this I was selling my wares in Judea when a local came to me furious that I had sold him an abascus which he apparently did not know how to use and next thing I know I'm fleeing the city with an angry mob at my heels. I tell you it is an injustice!"),
  ("npc24_backstory_c", "My father always told me to take faith in the higher powers, that they would save us all if we just had faith. Hmmh didn't seem to save either even though my mother frequently made sacrifices to the forest gods. After the supposed passing of my parents, I decided to teach myself how to fight, a wandering wizard taught me some techniques and told me some hard truths about life, such as 'There is none who defend you in the end except you by yourself' His teachings did not fail me."),
("npc25_backstory_c", "If you choose to take me, I ask for nothing but the chance to prove myself. You will find me loyal and eager to learn. Together, we can face the challenges ahead and emerge stronger."),
("npc26_backstory_c", "I served in a militia before I was given the vision, the vision of a Rome that rules all of this world, where Christ's kingdom stretches from Hibernia to the godless lands of the Persians. This vision was shown to me by Mary herself after I had been in a battle that we had lost, I was knocked unconscious and during that slumber I saw what will happen, I only need an army dedicated to God to make this an effective reality. The Virgin spoke to me that it is MY duty, and I will do it!"),
("npc27_backstory_c", "If you are a bold warlord with honor in your heart and steel in your hands, then I will gladly stand by you. I offer you my spear, my shield, and the loyalty of a northern heart. What say you?"),
("npc28_backstory_c", "Now I seek a warlord who is just but bold. I will ride beside him, as long as he leads with strength. If you are that man, then I offer you my spear - for a modest price."),
("npc29_backstory_c", "I am looking for a warband that values loyalty and hard work. If you are a just leader, I will carry your burdens, feed your men, and keep the camp whole. Just don't ask me to die in a shield wall, and we will get along."),
("npc30_backstory_c", "So here I am, offering my arm once more. I seek a leader of courage and vision - not a butcher, but a man with a cause. If you are that man, then I am ready to follow."),

### use these if there is a short period of time between the last meeting
  ("npc1_backstory_later", "Finally understood that I am not asking much or did you just came to say more curses to me?"),
  ("npc2_backstory_later", "I sold my boots and have managed to make a few siliquae peddling goods from town to town, but it's a hard living."),
  ("npc3_backstory_later", "Since I left my domus I have travelled the world and saw many great things! Who would have guessed a lone woman like me would have managed without a tutor? Regardless, I miss having a family. Friends. People you love. Maybe one day I will find a group for me..."),
  ("npc4_backstory_later", "So... came back after you saw that your men are not good enough and that you need Berbers to actually protect you?"),
  ("npc5_backstory_later", "I've been wandering through this war-torn land, looking for a leader who is worth following."),
  ("npc6_backstory_later", "Ah! You again! Are you here to insult my family name once again? In that case I will duel you to death!"),
  ("npc7_backstory_later", "I'm still here, selling my products, trying to survive. Not much to add to this."),
  ("npc8_backstory_later", "If you came to insult me, leave, if you came to reconsider taking me in, speak."),
  ("npc9_backstory_later", "I've offered my sword to a few people in these parts. But I find as often as not they'll ask me to run messages, or train peasants, or some other job not fit for a gentleman."),
  ("npc10_backstory_later", "You're still here? Still looking for someone better than me? Bah, good luck with that!"),
  ("npc11_backstory_later", "Oh, nothing much you see... I just stick to my caravan, try to protect my merchants to the best of my abilities. That's all."),
  ("npc12_backstory_later", "Ugh, I've just had to pull another rotten tooth and apply the mixture of olives and dung there. It's not a job for a renowned physician like me."),
  #("npc13_backstory_later", "I have been waiting for my chance to gain power and glory, and have yet to find it."),
  ("npc13_backstory_later", "Do what I do best, killing, commander. But here we are again. Do you need my bow now?"),
  ("npc14_backstory_later", "I have gone from court to court, but I have not yet found a noble in need of my services."),
  ("npc15_backstory_later", "I've been going from city to city, looking to see if any walls need repair. But either the lord's away, or he's got other things on his mind, or I run into his creditors on the street, begging for change, and I realize that here's one job not to take. So if you hear of anything, let me know."),
  ("npc16_backstory_later", "I do the odd job from time to time. But there's naught like steady employment, and a regular run of corpses to loot."),
  ("npc17_backstory_later", "Ah, you! The sturdy warrior. Are you still looking for blades?"),
  ("npc18_backstory_later", "Oh, you... The wanderer... Did you find what you were looking for?"),
  ("npc19_backstory_later", "Hello, friend. Could you consider enlisting a Slavic sword-for-hire again?"),
  ("npc20_backstory_later", "Hello there, I hope you still have that sword? Regardless, I'm still travelling if you need me..."),
  ("npc21_backstory_later", "Hello friend, changed your mind and decided you need my services?"),
  ("npc22_backstory_later", "Do you still need me or did you come here to mock me some more?"),
  ("npc23_backstory_later", "Is the barbarian back, you wish to take me with you, after those words you said? all right lucky for you that I am a forgiving man."),
  ("npc24_backstory_later", "Still here, why exactly? Quit wasting my time if you have nothing worthwhile to say."),
("npc25_backstory_later", "Have you decided to give me a chance, or are you still weighing your options? I am ready to ride whenever you are."),
("npc26_backstory_later", "Seen God's light or does evil still control your actions? Speak."),
("npc27_backstory_later", "You're back. Have you reconsidered, or are you here to mock the ways of the north once more?"),
("npc28_backstory_later", "You again. Have you come to mock the sons of the desert, or do you finally see the worth of a Baquates warrior?"),
("npc29_backstory_later", "Ah, you return. Have you reconsidered my offer, or do you only wish to mock a woman for daring to live free?"),
("npc30_backstory_later", "General. We meet again. Have you thought about my offer? I will not linger here forever."),

  ("npc1_backstory_response_1", "If I have Christians in my party I will make sure that they hold their tongue, you are most welcome wise rabbi, son of the most wise Salomon."),
  ("npc2_backstory_response_1", "Well, perhaps I could offer you work. Can you fight?"),
  ("npc3_backstory_response_1", "I am the leader of a warband. We don't often hire women but... If you want you can share our fire in our camp. Beware though, this is no easy life. Not a life for a woman."),
  ("npc4_backstory_response_1", "I agree that it's high time these defilers of Mauri lands are driven back to where they came from, I will assist you!"),
  ("npc5_backstory_response_1", "That's the spirit! I might be able to offer you something."),
  ("npc6_backstory_response_1", "No. I am here to offer you work. Join my warband, Wadomar son of Visimar. Many adventures await us and much loot to be shared!"),
  ("npc7_backstory_response_1", "Hmm... I could offer you something better than this, if you're interested."),
  ("npc8_backstory_response_1", "What a magical story and I do believe that murderers like that need to be punished, I am sure we can find them if we work together. So feel welcome to my band."),
  ("npc9_backstory_response_1", "Perhaps you would like to join my company for a while."),
  ("npc10_backstory_response_1", "I need people like you indeed."),
  ("npc11_backstory_response_1", "What will you do now?"),
  ("npc12_backstory_response_1", "Your medical knowledge is impressive. We will surely need a skilled medicus."),
  ("npc13_backstory_response_1", "Perhaps, but for the moments these are just words... At the end you're lost here in {s20}, you don't seem so engaged in fights of any kind. What brought you here?"),
  ("npc14_backstory_response_1", "I might be able to use you in my company."),
  ("npc15_backstory_response_1", "Where do you need to go?"),
  ("npc16_backstory_response_1", "I might be. What can you do?"),
  ("npc17_backstory_response_1", "I do, I do. It is time for you to show me if you're really worthy."),
  ("npc18_backstory_response_1", "I see. A tragic tale, but men seeking to avenge their fallen relatives and to clear their names are always very motivated and untamed. Yes, I might need someone like you... Indeed."),
  ("npc19_backstory_response_1", "Och, certainly. You know, you are quite a nice discutant for a barbarian from faraway north, I must admit."),
  ("npc20_backstory_response_1", "Great! You can join again."),
  ("npc21_backstory_response_1", "You are an enthusiastic young man, I must admit I would need more reasons than your enthusiasm to lead a young barbarian on my party."),
  ("npc22_backstory_response_1", "I too am longing for the days when Rome commanded and others obeyed, when Imperator was the law, people had faith in him, when the Eagle was respected."),
  ("npc23_backstory_response_1", "You are like the wise men of old, are you perhaps interested travelling with us, I'm sure my troops could use some deep thoughts and a calming logic from time to time..."),
  ("npc24_backstory_response_1", "So... if you are looking for employment, my offer still stands"),
#("npc25_backstory_response_1", "A wise choice, {playername}. I may be young, but I am eager to prove myself. I will not let you down, and one day you will speak of my loyalty with pride."),
("npc25_backstory_response_1", "I need people like you indeed."),
("npc26_backstory_response_1", "Well, you've had a rough life indeed, you could try finding this destiny with my warband, how do you plead? "),
("npc27_backstory_response_1", "No mockery. I need warriors who do not fear the cold or the sword. Join me, Harva of the Phinnoi."),
("npc28_backstory_response_1", "Malzam, Join my warband. There is silver to earn and glory to win."),
("npc29_backstory_response_1", "No mockery. I have work for you, if you're still willing. My warband could use a steady hand and a sharp mind."),
("npc30_backstory_response_1", "I have. Barzabod, I need a man like you. Join my warband, and glory will follow."),

  ("npc1_backstory_response_2", "Frankly I kill anyone I wish and I won't let some Jewish sentimentality or make-belief stop me. Second: why should I hire a man who is only armed with a wooden staff? one stroke from a sword and it would be cut in half. I wish you luck, you will need it"),
  ("npc2_backstory_response_2", "Hard luck, friend. Good day to you."),
  ("npc3_backstory_response_2", "Go back to your family, lass. Fathers must always be obeyed."),
  ("npc4_backstory_response_2", "Vandals seem to be doing well. I imagine you are jealous that they have a functioning society. I have no interest in attacking them and to you my only advice is: hang up your spear and live a peaceful life, no use fighting a war you can't win."),
  ("npc5_backstory_response_2", "Sigh.. So long as you hill clans fight tribe against tribe, you will remain a silly, weak people."),
  ("npc6_backstory_response_2", "Of course! Meet me outside the city. I'll make you eat my steel."),
  ("npc7_backstory_response_2", "I see. Well, good luck."),
  ("npc8_backstory_response_2", "Another folk tale from Arabia and most likely a load of rubbish too and to be fair if you really were that much of a loose loudmouth, I don't think you have changed that much, taking you into my party would be too dangerous."),
  ("npc9_backstory_response_2", "I don't need some sob in my company. Farewell."),
  ("npc10_backstory_response_2", "I don't like what you're saying."),
  ("npc11_backstory_response_2", "Very interesting, woman, but I have work to do."),
  ("npc12_backstory_response_2", "On the other hand who needs a doctor when you can just fast and pray."),
  ("npc13_backstory_response_2", "You indeed seem valiant, but I am not looking for archers. Farewell."),
  ("npc14_backstory_response_2", "I'll let you know if I hear of anything. Good day."),
  ("npc15_backstory_response_2", "Sorry. I've got all the men that I can manage right now."),
  ("npc16_backstory_response_2", "Sorry, lass. You sound like you might be trouble."),
  ("npc17_backstory_response_2", "You're just a drunkard and I have no need of you."),
  ("npc18_backstory_response_2", "That was a very sad tale... Sorry nomad, I wish to hear no more of them and I have no time to loose... I'm looking for something. Good luck."),
  ("npc19_backstory_response_2", "A loser who couldn't even have his sister under control and then had failed foederatus service? Begone, stinky Venedus!"),
  ("npc20_backstory_response_2", "I'm sorry but I'm hesitant. We will definitely meet again."),
  ("npc21_backstory_response_2", "Go back to your mother, boy, war is no place for children."),
  ("npc22_backstory_response_2", "What a pathetic, sad sob story, washed-up son of a soldier who has seen better days and now has delusional dreams of grand Rome, keep drinking wine, it is all you can do and all you ever will be good for."),
  ("npc23_backstory_response_2", "It is an injustice! Your complaining. To my ears. Go back to that symposium of yours or wherever the hell you have talked garbage to other gullible people. I've heard enough, these people are smart when they do not listen to you."),
  ("npc24_backstory_response_2", "Did that wizard also teach you the meaning of 'no, I am not interested in hiring you.'"),
#("npc25_backstory_response_2", "If you think I am unworthy, then so be it. But remember, even the greatest warriors started somewhere. Perhaps we will meet again when I have more scars to show."),
("npc25_backstory_response_2", "Sorry. I've got all the men that I can manage right now."),
("npc26_backstory_response_2", "Would be messiahs come and go, I only pray your passing happens soon. You are insane."),
("npc27_backstory_response_2", "Still not interested. Go back to your snows and ghosts, northerner."),
("npc28_backstory_response_2", "I came to see if you were still wasting time talking. I see nothing's changed."),
("npc29_backstory_response_2", "Your place is at home, not on the road. Stay away from me."),
("npc30_backstory_response_2", "No. I've thought better of it. You'd be more use back in your orchard."),

  ("npc1_signup", "Good to hear, they can be so annoying sometimes."),
  ("npc2_signup", "Well, I will confess that I am not a warrior by trade."),
  ("npc3_signup", "Oh... Really? I have never joined a warband... I guess I could help cleaning your horses, the stables... But I am no fighter. Even though maybe you could teach me a thing or two... A fighting woman! Ah! If only my father could see this..."),
  ("npc4_signup", "We should get along just fine, I actually seem to have taken a liking to you and that will remain AS long as you won't consort with the Vandalic scum or hire them, I will I swear by Ifri that I don't care even if they are on my side..."),
  ("npc5_signup", "Why, that is a most generous offer."),
  ("npc6_signup", "Ah! This is talking! Good, good. I will join you, Warlord. With me at your side, your Comitatus will never bend to someone else's knees."),
  ("npc7_signup", "I might be. I could certainly use the money."),
  ("npc8_signup", "We must find them, I cannot find peace before this task has been completed, my father's spirit demands me to act!"),
  ("npc9_signup", "I would very much like that, mister!"),
  ("npc10_signup", "I said I knew you are worthy of my time! A warrior knows who's a bear and who's a mouse. And you definitely knows the feeling of piercing your enemy and seeing his life go away."),
  ("npc11_signup", "Why, I'll be a soldier myself! Help my hands to a bit of loot to comfort me in my retirement. Two boys I bore, both soldiers' brats, and they became soldiers themselves. One had his head split by a Hunnic war club, the other died of the pox, but at least they didn't die hungry."),
  ("npc12_signup", "I'm but a humble servant doing my best to help those who suffer."),
  ("npc13_signup", "Commander, I am here because my party was disbanded. I finished my contract and thus I thought to spend my coins on here, hoping to find a woman to please me."),
  ("npc14_signup", "I would be pleased to ride with you, at least for a little while, for pay and a share of any loot."),
  ("npc15_signup", "Eventually I'd like to go to Constantinople and help work on the walls there, but I'd welcome the opportunity to get a few siliquae in my pocket, first, so I don't come home empty handed. So if you promise me food and a share of the loot, I'd be happy to fight with you for a while."),
  ("npc16_signup", "Well, Captain, let me tell you. I may not know how to read and write, but I know the quickest way to a man's heart is between his fourth and fifth rib, if you understand me. "),
  ("npc17_signup", "Are you making fun of me?! I - AM - worthy. Surely more than all those sissy eunuchs that follow you around and that you call warriors. I'll show you what a - TRUE - warrior can do. Just lead me to the battlefield!"),
  ("npc18_signup", "Very well. As I told you, I'm a tracker, but a warrior too. We Alans were the ruler of the steppes once... Our bows might not be as good as those that the Huns use, but our skills on horses have no equals. You can trust my word."),
  ("npc19_signup", "I am honored to hear so. Back in my tribe I was the son of witez', that is, a chief. I felt that staying in hall of my father was certainly not what I want to have for myself, even if we all share things with each other, a youngest son of minor chief doesn't have big perspectives in a tribe, so I decided to become a warrior. Trained hardly, I think I mastered bow, shield and axe quite well."),
  ("npc20_signup", "Very well, I am a warrior at heart, so I will serve well in your company."),
  ("npc21_signup", "Oh certainly, {sir/madame}, even amongst the Noobii my skill with the bow is unparalleled. Once, drove back 10 raiders which seek to plunder and enslave my village with only my bow and arrows. The situation back home is complicated you see, the Kings of Old Medewi are no more, and the tribes are in constant conflict. Being the son of a humble hunter, I might also be able to track and spot our enemies long before they have a chance to realize we are there."),
  ("npc22_signup", "Ah, someone who is after my own heart. If all Romans believed in our might like you do, we would still be rulers, leaders, powerful figures! instead now we have treacherous generals, traders and merchants who care only about lining their own pockets, soldiers who no longer care about the Res Publica and fight only for money, thank Jupiter that the Praetorian Guard was at least abolished. I too volunteered into the army, but I never fought only for pay, I fought for an idea and for my ideals. When I was in the army I learned about leading men and of the tactics needed to win the day."),
  ("npc23_signup", "Hmm... your troops are barbarians, I doubt I can teach much to them but I can at least try. You should probably know that I consider Romans to be as barbaric and moronic as the Iberian farmers so don't expect me to bow my head to them, all they know is how to fight each other, drink wine, lie and cheat. That's why their dear Empire is falling so fast, but since they do not even know *proper* geometry or math. Ageometretos medeis eisito as I say."),
  ("npc24_signup", "Eh, why not I enjoy the sound of battle and the clash of weapons, it's what I live for."),
("npc25_signup", "Excellent! I've been looking for a leader who values ambition and potential. I will follow you without hesitation."),
  ("npc26_signup", "Yes! I believe I could, your army... I hope it is only servants of True God, right? "),
("npc27_signup", "Then I shall follow you, warleader. My spear is yours, and my word is bond. Together, we shall bring fear even to the Swehanaz."),
("npc28_signup", "Wise choice, warlord. You won't regret having me by your side - swift in the saddle, sharp with the spear."),
("npc29_signup", "Then I am yours to serve. I'll keep the camp in order, mend what's broken, and keep the pot full. You won't regret this."),
("npc30_signup", "A wise choice. I will ride with you. Just remember, I bring skill, not blind obedience."),

  ("npc1_signup_2", "However, before I come with you there is a... monetary matter that must be talked about... My father always told me that you should never work for free and I'll be the firstborn of Satan if I start now, so I require a humble payment of 700 siliquae."),
  ("npc2_signup_2", "I'm a fast learner. I can ride, and know a fair bit about trade, prices and such."),
  ("npc3_signup_2", "I can help keep your camp in check, hire servants to have everything in order. I can also manage your finances if you will let me. After all, I am still a merchant's daughter! I know a thing or two."),
  ("npc4_signup_2", "I have been trained to war from a young age, my spear has taken the lives of countless lesser men who took on me."),
  ("npc5_signup_2", "I shall not betray you -- so long, of course, as you do your duty to me by feeding me, paying me, and not dragging my miserable hide into a battle where there is no chance of winning. Hand me some salt, if you will -- it is the custom of our people to take salt from our captains, as a token of their concern for our well-being."),
  ("npc6_signup_2", "I was told by the best fencing masters in Tolosa how to deal a deadly blow, and learned from our Alanic subjects how to properly ride good steeds. I am a good warrior, you won't regret this."),
  ("npc7_signup_2", "But let your followers know that I do not suffer louts and brutes. Anyone who misbehaves around me will quickly find an arrow in their gullet."),
  ("npc8_signup_2", "I do not even require money from you, I just need someone who will stay loyal and won't betray me. If you hold true to me, I will do the same to you."),
  ("npc9_signup_2", "I am a nobleman, and prefer to fight with sword and lance. I recognize that you are of lower birth than I, there is no shame for me to serve under an experienced captain -- presuming, of course, that your followers do not become too familiar with me. I assume that will not be a problem?"),
  ("npc10_signup_2", "Bring me with you and I'll stand by your side in the heat of battle. I'll shield you with my shield and kill your enemies with my axe, sword, spear or my bare fists if I'll have to!"),
  ("npc11_signup_2", "I know how to swing a blade, staunch a wound, and feed an army on the march. It would be a foolish captain who passed up the opportunity to hire an experienced campaigner like me! Say, Dux, don't you need someone like me in your warparty?"),
  ("npc12_signup_2", "I can recognize any illness by smelling your wounds, observing the omens or interpreting your dreams. You'll find no better professional than me."),
  ("npc13_signup_2", "I was employed here in {s20}, a local magnate asked us to get rid of a group of bandits near the town. I personally found out the bandit leader was building a net of smugglers and robbers in town in order to weaken the local authorities. I get rid of the problem myself, that's all you need to know."),
  ("npc14_signup_2", "I am a skilled swordsman, and I can also instruct your men in fighting. But I warn you that I do not care to fight for a leader who is lax in discipline with {his/her} men, for in the long run they will not respect a soft hand. "),
  ("npc15_signup_2", "Siegework is my speciality, although I reckon can handle myself well enough in an open battle, if need be."),
  ("npc16_signup_2", "I can throw knives, in addition to stabbing with them, and I'm slippery as quicksilver. You'll find me useful in a fight, I'll warrant."),
  ("npc17_signup_2", "I'll be your loyal retainer and with - ME - at your side no one will ever touch you nor they will dare to come closer. Together, me and you, we will pour the war into the bowels of the lands!"),
  ("npc18_signup_2", "One thing though, I have to tell you. I dont want Huns around me, I dont like them, I hate them to say the truth. They destroyed my kin and stole a life full of wealth and glory from me."),
  ("npc19_signup_2", "While I was fighting for Huns, I was lucky to serve mounted. Perhaps I earned their respect during that archery contest, though I never truly understood their speech. Maybe it's better, considering that I ended up in Roman auxilia after such Hunnic band got destroyed by them. Nevetherless, even considering my bad luck in finding reliable commanders, I still earned a bit of loot enough to buy myself proper helmet and shield, aswell as sword and better mount, so that I can fight along cavalry too. Fairly enough, although the service is now over, I still look for an employer who could enlist me for a coin. Afterall, I am a warrior now and never felt used to doing a civilian life."),
  ("npc20_signup_2", "I won't let you down!"),
  ("npc21_signup_2", "Unfortunately, I have only been able to bring my bow and arrows, my spear and shield, and the robes I am wearing. Oh! And an old Iron helmet my father's friend gave me as a farewell gift."),
  ("npc22_signup_2", "I still have my sword, my plumbatae and rusted but trusty shield and I still have strength in me. I will follow you if you stay loyal to the Roman way and to you keep your morals with you."),
  ("npc23_signup_2", "My wits and sharp tongue will keep me safe and if those do not then I have my dagger, I was quite the fighter when I was younger, killed many who insulted me can do it still if needed, so what you say?"),
  ("npc24_signup_2", "But blood and guts do not bring food to the table, as such I require a modest sum of 800 siliquae as a signup cost. A thin man is either a sick man or a poor man as they say."),
("npc25_signup_2", "I ask for no payment - only the opportunity to fight and learn by your side. Wealth does not concern me; experience is what I seek."),
  ("npc26_signup_2", "I do not fight for money like some mercenary or some boor so if you only promise to stay on the godly path, I will follow you in that path."),
("npc27_signup_2", "I have fought in blizzards and stood alone at river crossings. I've tracked raiders through night and snow. I do not boast - I endure. And I will endure for your cause."),
("npc28_signup_2", "I have hunted lions in the wastes and outpaced Vandal scouts. My people live hard, and only the strong survive. You'll find no coward in me."),
("npc29_signup_2", "Just don't expect me to fight with sword and shield. But I'll run with the carts, keep the wounded fed, and help your men stay alive."),
("npc30_signup_2", "Let others shout and boast - I strike where it matters. You'll see what a real soldier can do."),


  ("npc1_signup_response_1", "By the twelve tribes that is some cost, but I guess you must be worth it, I certainly hope so for your and my sake, here."),
  ("npc2_signup_response_1", "That will do."),
  ("npc3_signup_response_1", "It will do lass! You will be helpful. Time to pack your bags now."),
  ("npc4_signup_response_1", "The downfall of Genseric and his cowardly advisors begins today, Onwards to victory!"),
  ("npc5_signup_response_1", "Certainly. Here, have some salt."),
  ("npc6_signup_response_1", "Good! Fetch your stuff, we will leave soon."),
  ("npc7_signup_response_1", "I will hire you. Try not to shoot anyone on your first day."),
  ("npc8_signup_response_1", "Even if we have to search all of Rub'al-Khali we will find them, I'm sure."),
  ("npc9_signup_response_1", "Well, it shouldn't be. I'll have a talk with them."),
  ("npc10_signup_response_1", "How can I refuse such impressive warrior? Very well, join us."),
  ("npc11_signup_response_1", "It sounds like you'll be useful. You are hired."),
  ("npc12_signup_response_1", "Then welcome to our company, medicus!"),
  ("npc13_signup_response_1", "I'm willing to give you a chance. I'll provide you with a pay, food and equipment, but you will always have to watch my back."),
  ("npc14_signup_response_1", "Good. I'll be happy to hire someone like you."),
  ("npc15_signup_response_1", "That works for me. I will be pleased to hire you."),
  ("npc16_signup_response_1", "It sounds like you can do the job. I will hire you."),
  ("npc17_signup_response_1", "That's the spirit. I like you, Alachis son of Sigmar. Let's go."),
  ("npc18_signup_response_1", "There are no many Huns around these places today anymore... From what I heard they're all around the Pontos Aexinos. Welcome to my host, Khaetag."),
  ("npc19_signup_response_1", "Good. You can be useful to us."),
  ("npc20_signup_response_1", "Very well, welcome to my company!"),
  ("npc21_signup_response_1", "Alright, you have convinced me, young man, do not disappoint me!"),
  ("npc22_signup_response_1", "May Juno light our way and guide us and may Mars give us victory and faith to win and conquer all obstacles!"),
  ("npc23_signup_response_1", "Fortune favors the smart. Let us get on the road, we have a great task ahead of us and we will be happy to have you with us!"),
  ("npc24_signup_response_1", "Done, welcome to our warband!"),
  ("npc25_signup_response_1", "Good. Your determination pleases me, Babai. Let us set out together and see what the world has in store."),
  ("npc26_signup_response_1", "I will make sure my men understand and give you proper respect, o enlightened one!"),
("npc27_signup_response_1", "Gather your gear. We march with the rising sun."),
("npc28_signup_response_1", "Fetch your arms and your horse, Malzam. We ride soon."),
("npc29_signup_response_1", "Good! Gather your things, we march soon."),
("npc30_signup_response_1", "Good. Fetch your saddle and meet us at the gate."),

#11
  ("npc1_signup_response_2", "You are either a fool or drunk if you think I will pay you that much, even 500 seems too much. Begone before you make me mad!."),
  ("npc2_signup_response_2", "I'm afraid I'm only looking for men with some experience. Good day to you."),
  ("npc3_signup_response_2", "Ah well... No, I am sorry. I was looking for... Well... Women that offer different kind of services you know! No offense meant."),
  ("npc4_signup_response_2", "AI am not going to sack any of my men just because they happen to be Vandals, you can try to debate me on this, with swords or spears, however you wish."),
  ("npc5_signup_response_2", "Actually, on second thought, I prefer to keep more civilized company."),
  ("npc6_signup_response_2", "Ahahah, I was just joking! Get lost, barbarian. Your kin is the reason of my people's disgraces!"),
  ("npc7_signup_response_2", "Actually, on second thought, you sound like you might be trouble. Good day to you. "),
  ("npc8_signup_response_2", "Now when I think about it, that's the problem with you Arabs, you are all too concerned about revenge and paying back insults that you will never be united or live in peace, I would be a fool to hire you, you'd probably create more enemies to me too."),
  ("npc9_signup_response_2", "You assume wrong, sir. In my company we respect courage and skill, rather than noble birth."),
  ("npc10_signup_response_2", "On second thought... maybe taking such bloodthirsty person is not a good idea."),
  ("npc11_signup_response_2", "Sorry, woman. We've already got as many in our company as we can handle."),
  ("npc12_signup_response_2", "I'm not sure I could afford the services of such great mind... I'll look for someone cheaper."),
  ("npc13_signup_response_2", "You really haven't convinced me. Farewell."),
  ("npc14_signup_response_2", "Actually, I have no wish to provoke a mutiny in my ranks. Good day, sir."),
  ("npc15_signup_response_2", "Actually, I need a different kind of expertise. My apologies."),
  ("npc16_signup_response_2", "To be honest, I'd prefer someone who was a little less tempted to larceny."),
  ("npc17_signup_response_2", "You may be right, but I think I'll look for someone else."),
  ("npc18_signup_response_2", "Mmmh... I understand this, but my host is not a place where to get your revenge. Find someone else for this, Khaetag."),
  ("npc19_signup_response_2", "A barbarian warrior in full panoply? It's insultful to see such precious gear wasted on such lowly being."),
  ("npc20_signup_response_2", "Sorry but not today... maybe later."),
  ("npc21_signup_response_2", "I would be a fool to hire a boy to fight my battles, go back to your filthy village before your poor mother whores herself."),
  ("npc22_signup_response_2", "By Sol Invictus man, with all that whining and wailing you would do better in this life as a Vestal virgin, I doubt you ever even were a soldier, either way I suggest you fall to your sword now."),
  ("npc23_signup_response_2", "Will you shut the hell up before I run you through with my sword. I truly hope that your sharp tongue and your constant provocations ends up getting you the reward Socrates got after people got tired of him."),
  ("npc24_signup_response_2", "Why should I hire you, the only thing I see is a boorish, Eastern pampered noble, what use would you be to us?"),
  ("npc25_signup_response_2", "If you think I have nothing to offer, I will not force your hand. But know this: one day you may regret passing on a chance to shape a future leader."),
  ("npc26_signup_response_2", "You are not in charge of who I hire or won't hire. And frankly your voice is beginning to annoy me, go find someone else to spout your nonsense to."),
("npc27_signup_response_2", "I changed my mind. Your spear would snap like pine in real war. Farewell."),
("npc28_signup_response_2", "You desert folk love your words. Go brag to someone else."),
("npc29_signup_response_2", "On second thought, I don't need a camp wench. Find someone else to carry pots and pans."),
("npc30_signup_response_2", "Hah. Forget it. You're not the kind of man I'd follow."),

  ("npc1_payment", "Excellent! I will be taking the {reg3} siliquae now, I have a few payments to make before we leave..."),
  ("npc2_payment", "I just need a payment of {reg3} siliquae."),
  ("npc3_payment", "I just need a payment of {reg3} siliquae."),
  ("npc4_payment", "I just need a payment of {reg3} siliquae."),
  ("npc5_payment", "Thank you. Now, to seal off our agreement, I ask for {reg3} siliquae from you. It's an advice my father gave me. He told me 'Sunicas, never fight for a barbarian before {he/she} pays you your worth of gold first'."),
  ("npc6_payment", "I just need a payment of {reg3} siliquae."),
  ("npc7_payment", "All right then. I will come with you. But I want a payment of {reg3} siliquae first. You aren't expecting me to work for free, do you?"),
  ("npc8_payment", "All right, friend I will follow you. However, I need a payment of {reg3} siliquae first, to cover my lodging."),
  ("npc9_payment", "That's very good of you. And before I join, can you lend me {reg3} siliquae, so that I can buy some proper clothing that befits a gentleman of noble birth such as myself. The coat on me has been worn down badly due to my recent bad fortune, and I cannot let common soldiers mistake me as one of their own."),
  ("npc10_payment", "You won't be disappointed! But before we go I have to visit the local smith. I had a quarrel with one of the idiots here and thanks to his bloody bones my weapon isn't as sharp as it used to be. Give me {reg3} siliquae and it'll be like new!"),
  ("npc11_payment", "Hey thank you Dux. But before joining up with you, I would ask for a payment of {reg3} siliquae. I know that in war parties soldiers can go on for weeks without seeing any wages. I am wise enough not to sign anywhere without having myself covered."),
  ("npc12_payment", "I just need a payment of {reg3} siliquae."),
  ("npc13_payment", "My cost is {reg3}, pay me now and I'll join you."),
  ("npc14_payment", "Ah, one last thing. I would ask for an initial payment of {reg3} siliquae before I join your command. My 20 years of service under the empire and the skills I have gained does not come for free."),
  ("npc15_payment", "Good. By the way, as a skilled engineer I would expect a payment for my services. A signing bonus of {reg3} siliquae would be fair, I think."),
  ("npc16_payment", "Now, that's good news, captain. So, how about paying me a little something to seal off our agreement? A mere {reg3} would be enough. Please don't take this the wrong way, but I've had some bad luck with employers in the past. "),
  ("npc17_payment", "Well... Before we leave, I drank too much in this tavern since the end of my last employment and I dont have a single panningaz left... But I still need to pay unless I slaughter them and then run away from this wretched city!"),
  ("npc18_payment", "You wont be disappointed, believe me. However, I'd like to at least purchase some decent horse before we move, mine died along the road. Can you lend me {reg3} for this? Consider it my payment."),
  ("npc19_payment", "I just need a payment of {reg3} siliquae."),
  ("npc20_payment", "I just need a payment of {reg3} siliquae."),
  ("npc21_payment", "Praise Mandulis! I promise I will not disappoint you, sir/madame! Regarding payment, do not worry, I do not intend to take too much from you, just enough to send money back to my family. Does {reg3} sound fair?"),
  ("npc22_payment", "I just need a payment of {reg3} siliquae."),
  ("npc23_payment", "I just need a payment of {reg3} siliquae."),
  ("npc24_payment", "All right then. I will come with you, however I do need that payment of {reg3} siliquae... I have built quite the debt here, and need to pay it off..."),
  ("npc25_payment", "There is no payment to discuss - I fight for the experience, not for coin. Let us ride without delay."),
  ("npc26_payment", "I just need a payment of {reg3} siliquae."),
("npc27_payment", "For a man of the north, gold is less important than honor. I ask no coin - only worthy deeds."),
("npc28_payment", "Before I ride, there is a small matter of {reg3} siliquae. That's what my service is worth - fair and square."), #500 siliquae
("npc29_payment", "I ask only for {reg3} siliquae. A modest price for honest work."),
("npc30_payment", "For my skills, I ask {reg3} siliquae. Not a coin less. Quality has its price."),

  ("npc1_payment_response", "Very well, here's the money."),
  ("npc2_payment_response", "Very well, here's the money."),
  ("npc3_payment_response", "Very well, here's the money."),
  ("npc4_payment_response", "Very well, here's the money."),
  ("npc5_payment_response", "Well... here's {reg3} siliquae, then. Your first payment."),
  ("npc6_payment_response", "Very well, here's the money."),
  ("npc7_payment_response", "No, of course not. Here's {reg3} siliquae."),
  ("npc8_payment_response", "Very well, here's the money."),
  ("npc9_payment_response", "Very well, here's the money."),
  ("npc10_payment_response", "Of course. Here, {reg3} siliquae."),
  ("npc11_payment_response", "Very well, here's {reg3} siliquae. Make yourself ready. We leave soon."),
  ("npc12_payment_response", "Of course. Here, {reg3} siliquae."),
  ("npc13_payment_response", "Of course, here's {reg3} siliquae. Make ready to leave soon."),
  ("npc14_payment_response", "All right, here's {reg3} siliquae. You are most welcome in our company."),
  ("npc15_payment_response", "All right, here's {reg3} siliquae. Glad to have you with us."),
  ("npc16_payment_response", "All right, here's {reg3} siliquae for you. Make yourself ready."),
  ("npc17_payment_response", "Very well, here's the money. Just try to save your strength for the trip."),
  ("npc18_payment_response", "Understandable for a nomad. Here horses cost a bit more than in the steppes. Have your coins."),
  ("npc19_payment_response", "All right, here's {reg3} siliquae for you. Make yourself ready."),
  ("npc20_payment_response", "Of course. Here, {reg3} siliquae."),
  ("npc21_payment_response", "{reg3} sounds fair. Now, fall in with the rest."),
  ("npc22_payment_response", "Of course. Here, {reg3} siliquae."),
  ("npc23_payment_response", "Of course. Here, {reg3} siliquae."),
  ("npc24_payment_response", "Very well, here's {reg3} siliquae. Now, fall in with the rest."),
  ("npc25_payment_response", "Good. Wealth may fade, but strength and wisdom endure. Let us make the most of our time together."),
  ("npc26_payment_response", "Of course. Here, {reg3} siliquae."),
("npc27_payment_response", "So be it. Walk with me then, Harva."),
("npc28_payment_response", "Very well, here's the money."),
("npc29_payment_response", "Very well, here's the money."),
("npc30_payment_response", "Very well. You've earned it."),


  ("npc1_morality_speech", "Captain, I am an honorable man and I too have a reputation to uphold as such I cannot stand that you would bring me and this group dishonor by failing a quest, do better next time, I can feel the anger of Yahweh on my neck."),
  ("npc2_morality_speech", "I hope you don't mind my saying so, but it's a bit hard for me to see us {s21}. Maybe I ought to try to be more of a hardened soldier, but if we could try to exercise a little mercy from time to time, I'd sleep better."),
  ("npc3_morality_speech", "Hey! HEY! What did you do?! I didnt join you to slaughter peasants, merchants, harm innocent people! Stop! Maybe this is not the right place for me after all..."),
  ("npc4_morality_speech", "Comes, you really managed to lose many good men, soldiers are not like trees, they cannot be easily replaced, I advise better tactical planning next time..."),
  ("npc5_morality_speech", "Pardon me, captain. It is not good to {s21}. Your first duty is to the men who have taken your salt. The least they can expect is food, pay, the opportunity to loot, and that you not waste their lives needlessly."),
  ("npc6_morality_speech", "Warlord! You must be daring... And be more ambitious! Robbing caravans is not enough. We should invade one of these fertile lands, settle in it and demand tributes from our new subjects."),
  ("npc7_morality_speech", "Captain -- I do not like to see us {s21}. Such are the actions of a common bandit chief, with no regard for his followers."),
  ("npc8_morality_speech", "I never shy away from battle, my father fought against the Romans and the Persians too, he once told me that someday we will live free of them both, but I fear I or my children will not see that day..."),
  ("npc9_morality_speech", "Dux -- it is not my way to {s21}. Men of my house will accept death but not dishonour. Please do not make me ashamed to serve under you."),
  ("npc10_morality_speech", "I don't mind to butcher from time to time but I don't like to {s21}. We should just take the loot and go."),
  ("npc11_morality_speech", "Excuse me, captain. It's not good that we {s21}. I've followed armies and warbands for 30 years, and the least the soldiers expect of a leader is to feed them, pay them, and do {his/her} best to keep their sorry skins intact as best {he/she} can."),
  ("npc12_morality_speech", "Captain -- I do not like to see us {s21}. I am prepared to be a warrior, but not a brigand. Pray let us try to show a little more compassion."),
  ("npc13_morality_speech", "Commander! Did we just {s21} ? This is dishonorable and I wish we won't repeat this kind of behavior."),
  ("npc14_morality_speech", "I do not care to {s21}. No one with a reputation for cowardice will be properly feared by his men."),
  ("npc15_morality_speech", "{Sir/Madame} -- just so you know my opinion, any commander with sense will not let his company {s21}.I hope you don't mind me speaking so bluntly."),
  ("npc16_morality_speech", "Captain. I don't like to {s21}. So many throats left uncut, and so many purses left unexplored..."),
  ("npc17_morality_speech", "Warlord! What the hell?! Did we really {s21}? I do not approve it, you're the chief, you give us order but beware... If you will stick to this dishonorable behavior I will leave... Not to return again!"),
  ("npc18_morality_speech", "Why do we {s21} ? That's not what I signed up, chief. Please, let's not do it again."),
  ("npc19_morality_speech", "Poor people. Did we really have to raid their village? These times saw many people getting raided and killed over the steppe. We could have spared at least few rather than ruining this village for good."),
  ("npc20_morality_speech", "I was not pleased that you decided to {s21}. To fall in battle leading your men is an honour, but living as a coward is a disgrace."),
  ("npc21_morality_speech", "{Sir/Madame}, I stopped some of your men from raping a mother that was fleeing with her children. I understand that war is terrible, but perhaps we can make more loot from battles rather than brutalizing the innocent?"),
  ("npc22_morality_speech", "I trust in your judgement and when we are fighting the enemies of Rome, I believe our conduct should be merciless. Take no prisoners and send every one of them to Pluto and fear will keep the rest of them in line."),
  ("npc23_morality_speech", "You'll get no objections from me if you kill a few innocents, if they are not Greeks I could not care less. Though you might wish to spare some, we need servants and slaves as well and you know that work is the greatest joy and value of a slave."),
  ("npc24_morality_speech", "We are living an unpeaceful era, I have fought in more battles than my father at my age, I wonder what's the root cause of all this, not that I'd really care for battle is where I am at home."),
("npc25_morality_speech", "Captain, I must speak my mind. A leader's strength is measured not just by their victories, but by their honor. I urge you to do better - for your sake and for those who follow you."),
  ("npc26_morality_speech", "Battles where the blood of filthy pagans is spilled is always a sacred work. We still have a long way to go before we have cleansed all that needs to be purged... "),
("npc27_morality_speech", "Warlord! That was a bold choice. You lead like the reindeer leads the herd - strong and without fear. I am proud to follow such a path."),
("npc28_morality_speech", "Warlord, you have the look of someone who knows when to strike and when to wait. Keep to this path, and the desert itself will envy your cunning."),
("npc29_morality_speech", "I was not pleased that you decided to {s21}."),
("npc30_morality_speech", "General, I commend your foresight. Strategy and boldness will lead us to prosperity. A man must do more than just survive - he must build a future worth guarding."),

  ("npc1_2ary_morality_speech", "I am not a soldier, but I know how dishonorable it is to run from battle, the ancient tribes of Israel did not run away from challenges, and neither should you. You are making me question my choices, let's go back and reduce those men to heap of bones!"),
  ("npc2_2ary_morality_speech", "{Sir/Madame} -- I'm not altogether happy that we {s21}. I'm a merchant, and in our business one is bonded by one's word. I don't want a reputation for dishonesty -- that would spell my end as a trader, {sir/madame}."),
  ("npc3_2ary_morality_speech", "Hey... I know it can be hard to do the right thing sometimes but you had no other choice. No regrets, look forward and don't blame yourself. You did well."),
  ("npc4_2ary_morality_speech", "It is true that my mission is one where only blood and dead Vandals interest me, but I too must eat so pay me in time Comes, otherwise I might have to rethink my loyalties"),
  ("npc5_2ary_morality_speech", "What we have done is dishonorable."),
  ("npc6_2ary_morality_speech", "Warlord -- you may choose to {s21}, but would prefer to have no part in it. Such is not the path to glory!"),
  ("npc7_2ary_morality_speech", "What we have done is dishonorable."),
  ("npc8_2ary_morality_speech", "What we have done is dishonorable."),
  ("npc9_2ary_morality_speech", "Dux, I am dismayed that you {s21}. A {gentleman/gentlewoman} such as yourself should exhibit the highest standards of honour at all times."),
  ("npc10_2ary_morality_speech", "{Brother/Sister} -- I can't say I like to see us {s21}. You should treat your men well, and they'll repay with interest."),
  ("npc11_2ary_morality_speech", "What we have done is dishonorable."),
  ("npc12_2ary_morality_speech", "What we have done is dishonorable."),
  ("npc13_2ary_morality_speech", "What we have done is dishonorable."),
  ("npc14_2ary_morality_speech", "Captain -- you should not let it bother you that you {s21}. Armies are made to do their leaders' bidding, and hardships are part of a soldier's life."),
  ("npc15_2ary_morality_speech", "You know, friend {playername}, it's none too reassuring to see how you just {s21}. If you can break your word to them, you can break your word to me, is how I figure it."),
  ("npc16_2ary_morality_speech", "Captain -- just so you know, it's no problem by me that we {s21}. We do what we need to do to live, and they'd do the same to us if they were in our shoes."),
  ("npc17_2ary_morality_speech", "Warlord! I approve that we {s21}. Our enemies are crushed, we saw them fleeing in front of us and heard the lamentations of their women. That's the best in life a man could dream of."),
  ("npc18_2ary_morality_speech", "Very well, I didnt expect that we {s21}. It makes me feel good, even if the others might not agree."),
  ("npc19_2ary_morality_speech", "Chief, it's okay that you had to retreat from this battle. Enemy had an upper hand and it's definetely better to retreat one day to fight another than get massacred, looted and left to crows."),
  ("npc20_2ary_morality_speech", "What we have done is dishonorable."),
  ("npc21_2ary_morality_speech", "I do not think retreating was cowardly, sir/madame, we all value our lives after all. We can always come back and avenge our honor."),
  ("npc22_2ary_morality_speech", "Fleeing from battle is unforgiveable and and an insult to all Romans. In the old days it could be punished with decimatio, that kept soldiers from thinking about running most times."),
  ("npc23_2ary_morality_speech", "Grave mistake of planning and dishonorable as well. My ancestors did not flee at Thermopylae, we fought till the last man, you too should follow their example, it is better to die than live after a lost battle."),
  ("npc24_2ary_morality_speech", "I have honor code too, however {s21} violates this. Those who do so are nothing but scum in my eyes."),
  ("npc25_2ary_morality_speech", "Running from battle? Iazyges do not flee, Captain. We face death with pride and swords drawn. I hope this was an exception, not the rule."),
  ("npc26_2ary_morality_speech", "What we have done is dishonorable."),
("npc27_2ary_morality_speech", "Warlord... you may choose to {s21}, but I will speak plainly - I would rather not be part of such a path. That is not how we earn respect among the Phinnoi."),
("npc28_2ary_morality_speech", "Warlord -- you may choose to {s21}, but I was not raised to follow such ways. The men speak of honor - they must see it in their leader."),
  ("npc29_2ary_morality_speech", "What we have done is dishonorable."),
("npc30_2ary_morality_speech", "General - you may choose to {s21}, but that is not the path of an honorable soldier. I have fought many battles... and I know when a choice brings shame."),

  ("npc1_personalityclash_speech", "{s11} is an ahabal! a damn sheretz! Yimach shmo! He claims he is a healer and a learned man too; I debated him about the effects of Roman medicine on people I told him that one Roman medicus kills more men than a well-armed legion with their ineptitude. He called me a 'Jewish bastard' and that I speak when I should be quiet and I am quiet when I should talk."),
  ("npc2_personalityclash_speech", "{Sir/Madame} -- as you recall I was a merchant before I signed on with you. I respect men who make their living peacefully, risking all to bring goods for far away lands."),
  ("npc3_personalityclash_speech", "Captain, is this the way you want your men to be treated? I'm a mere camp follower, but look at how Beorhtric and Rufinius treat the others. They're merely barbarians! Both of them! Even if Rufinius is a roman like me. About the other, that barbarian from the dark forests of Germania... Dont let me talk about him!"),
  ("npc4_personalityclash_speech", "{s11}, that son of a mule Alanic mother humper! He is getting on my nerves and last battle we were in, he remarked how he has fought against Berbers before and that he even has the teeth of one as trophy! If I find this to be true I will disembowel him."),
  ("npc5_personalityclash_speech", "A moment of your time, captain. {s11} seems to think me a common bandit, just because I have rewarded myself in the past to the legitimate spoils of war from caravans passing through my family's lands."),
  ("npc6_personalityclash_speech", "A moment of your time, Warlord!, but I cannot keep my tongue stilled any longer. That harlot, {s11} -- every time she sees me she points the five fingers of her hand at me -- a peasant's sign to ward off evil."),
  ("npc7_personalityclash_speech", "Captain -- I have been searching my mind trying to remember where I have heard about {s11}, the one who calls himself a liberator, and friend of yours. As I watched him in action during that last battle, I suddenly remembered. He is nothing more than a violent bandit..."),
  ("npc8_personalityclash_speech", "{s11} is not the kind of a man this band needs, he can't fight, he is cowardly, he cannot do a task when given and he is a Persian, I have fought against his ilk for far too long. If that storm that wrecked his ships was sent by a god then I give my praises to that deity and my curses that it didn't kill him."),
  ("npc9_personalityclash_speech", "Dux -- {s11} is a base braggart, a man with no respect for the honour of women. I am tired of hearing how he conquered this or that damsel."),
  ("npc10_personalityclash_speech", "Excuse me, captain. I hate to trouble you with such things, but I just wanted to let you know that I can't abide that fellow {s11}."),
  ("npc11_personalityclash_speech", "Begging your pardon, captain, but I can't keep silent. That man, {s11} -- did terrible things in his past."),
  ("npc12_personalityclash_speech", "My lord. The arab, {s11}, complained of headaches -- a possible symptom of excess of sanguinity. I thought to apply my leeches."),
  #("npc13_personalityclash_speech", "Captain, I weary of {s11}, who curses the Lord my God."),
  ("npc13_personalityclash_speech", "Commander, that small-eyed barbarian from the Skythia that plague this party with his sickening presence: he doesn't know his place."),
  ("npc14_personalityclash_speech", "Excuse me, captain. A few minutes ago, I had expressed the opinion that liberal use of the lash and occasional use of the gallows is essential to keep soldiers in line. Men without a healthy fear of their commanders are more likely to run from battle."),
  ("npc15_personalityclash_speech", "Excuse me. I hope you don't mind me telling you that in my opinion, that girl {s11} is a danger to the party. She's a feral brat, disrespectful of authority and the basic principles of the military art."),
  ("npc16_personalityclash_speech", "Oy, captain. Just so you know -- there's something funny about {s11}. He makes strange scrawlings in the dirt, and mutters to himself."),
  ("npc17_personalityclash_speech", "Warlord! That eunuch man... {s11} I think he likes other men... I mean, I can't be sure but my manly insticts tell me to not trust greeks and their feminine behavior."),
  ("npc18_personalityclash_speech", "Chief, when I joined you I told you I didnt want Huns around me. That {s11} must go. His mere presence is an insult to me, I should cut him down like a dog."),
  ("npc19_personalityclash_speech", "Chief, I really do not like {s11}. He seems to enjoy killing innocents, raiding people and harassing caravans. Quite reminds me of this Hunnic chief which led ous to that defeat at the Roman border. Please, reconsider if he is really worthy your wage."),
  ("npc20_personalityclash_speech", "{!}."),
  ("npc21_personalityclash_speech", "{Sir/Madame}, I have to admit I find Sunicas to be a disgusting man. He often retells with delight the pain he has inflicted to others, particularly on maidens. He whispers that he wishes to raid more villages and attack more caravans."),
  ("npc22_personalityclash_speech", "General, I will not sugarcoat this. Next time I see {s11} I will kill him myself, I don't know why I haven't done it yet. He is Judean scum, I've met some of his ilk before farther in the East and not one I have seen has been worth any trust, I'd rather trust a Pict!"),
  ("npc23_personalityclash_speech", "Captain. I'd like to point out that having {s11} in this party is an affront to me and everything I stand for as it should be for you."),
  ("npc24_personalityclash_speech", "{s11} annoys me, he speaks of his Hebrew God but I don't see how he's supposed to be better than mine. Also I do not trust a man who does not eat meat or wine and makes excuses that it needs to be ko...gosh... whatever he said."),
("npc25_personalityclash_speech", "{s11} is insufferable. They speak as if their way is the only way, ignoring the wisdom of others. If they were on the Danubian plains, they would not last a week."),
  ("npc26_personalityclash_speech", "{s11} is a false prophet and a follower of false ways. I know very well that ages ago we did break away from their beliefs and we did it to create something better, something that truly was from God, not the corrupted faith of Pharisee or the degraded words of high priests, those bastards killed Christ because they were afraid of his righteousness and influence."),
("npc27_personalityclash_speech", "Warlord, allow me a word. That woman, {s11}, walks among hardened warriors as if the campfire were her weaving hall. It unsettles the men - and it unsettles me."),
("npc28_personalityclash_speech", "Warlord, I do not like the look of {s11}. She reminds me too much of the northern raiders who struck our camps - wild eyes, and too bold with her tongue."),
  ("npc29_personalityclash_speech", "I'd like to point out that having {s11} in this party is an affront to me and everything I stand for as it should be for you."),
("npc30_personalityclash_speech", "General, I must speak plainly. This man, {s11}, is a disgrace. Undisciplined, wild... He brings shame upon your banner."),

  ("npc1_personalityclash_speech_b", "He will be the one who will be quiet if he keeps annoying me, his kind are a cancer, a blight on this world. Good for nothing Romans and their pompous ways, what have they ever done to us?"),
  ("npc2_personalityclash_speech_b", "I don't much care to hear {s11} gloat about the caravans he has looted, or he plans to loot, like he has no respect for good honest trade."),
  ("npc3_personalityclash_speech_b", "I saw them flogging and punishing the others harshly... I am not a warrior, I already said this, but I disagree! My heart aches for them. They're friends!"),
  ("npc4_personalityclash_speech_b", "I said to him that we should just fight to the death but he said I'm not worth the effort. ME!? NOT WORTH IT!?!? just you wait, one day you look the other way and then my spear will be in your neck..."),
  ("npc5_personalityclash_speech_b", "I told him that if the warrior's way bothers him so much, that he become a priest or a beggar and so not have to worry about such things. I hope you do not mind that I said such things."),
  ("npc6_personalityclash_speech_b", "I am telling you, warlord. Next time she tries ward off evil I'll grab my belt and leash her. Women should learn their places, but this warband looks like a circus nowadays!"),
  ("npc7_personalityclash_speech_b", "I do not care for how he stares at me around the campfire after a meal, as he picks his teeth. This berber is no more than a brigand, masking his villianry with a guise of 'freedom' for his people. I do not care to travel with such people."),
  ("npc8_personalityclash_speech_b", "He also called me an 'ignorant shrew' questioned the size of my manhood and the worst of all he insulted my father. You know, among the Arab tribes, men have killed for insults directed against their parents and elders. It was only because of you I abstained from ending him right then and there but I have my limits so I advise you to tell him to be quiet when he talks to his superiors."),
  ("npc9_personalityclash_speech_b", "If he persists, I shall tell him that he is a base varlot, and if it comes to blows I will not apologize. That is all, Dux."),
  ("npc10_personalityclash_speech_b", "He's just a simple brigand, as far as I can tell. Genuine blue-bloods are bad enough, but those who pretend to be blue-bloods are bloody intolerable. Anyway, I might have said something a bit sharp to him a minute ago. He seemed to take offense, anyway. I just thought you should know."),
  ("npc11_personalityclash_speech_b", "He's a kinslayer, cursed by heaven, and he'll bring misfortune and sorrow upon us, that's for certain. I don't like being around him and I don't think he should be with us. That's all. Sorry for troubling you."),
  ("npc12_personalityclash_speech_b", "But when I tried to afix them, he recoiled and struck me, and accused me of witchcraft. Captain, I am deeply tired of attending to the complaints of such an ungrateful and ignorant lot."),
  #("npc13_personalityclash_speech_b", "My faith is an important part of my life, I do not take kindly to those insults."),
  ("npc13_personalityclash_speech_b", "His cruelty on the battlefield knows no bounds and his elongated skull makes me question his human nature in the first place. I think we would be better if we were to get rid of him. What do you think? ."),
  ("npc14_personalityclash_speech_b", "That chit {s11} saw fit to admonish me for this. I will not have my methods questioned in front of the men, and I will not serve any commander who tolerates such insubordination in his company. Thank you for allowing me to speak my peace."),
  ("npc15_personalityclash_speech_b", "What's more, I suspect she's a thief. I found her going through my baggage and pawing some of my schematics, and she pulled a knife on me when I thought fit to object. A wise captain would not allow her in his company."),
  ("npc16_personalityclash_speech_b", "Fearing witchcraft, I asked him about it, and he told me that a chit of a girl like myself should mind her own business. So I had a look in his baggage, and found strange plans and diagrams. I think he's a sorceror, Captain, and if I catch him trying to hex me he'll have a knife in his throat."),
  ("npc17_personalityclash_speech_b", "Well warlord, you know what they say about Greeks, people from the East... I will keep my arse well tight when I see him, and my seax well placed so he can notice it!... Come on, warlord!, let me cut that dog's throat, we dont need him!"),
  ("npc18_personalityclash_speech_b", "He may be a good warrior, but he's still a savage. One day or another I will lay my hands on him and throw him out of our tents."),
  ("npc19_personalityclash_speech_b", "He's just a steppe raider without any morals and I regret having served under those of his kind."),
  ("npc20_personalityclash_speech_b", "I am disappointed."),
  ("npc21_personalityclash_speech_b", "He has also questioned my manhood in repeated occasions because I refuse to partake on his barbaric stories. I things continue the way they are, I am afraid I will have to duel him for my honor."),
  ("npc22_personalityclash_speech_b", "What an absolute repugnant piece of work, I'd suggest you sack him or better yet let me open him and be done with it, we might save some Romans at the same time, who knows what crimes he will do if you let him ago."),
  ("npc23_personalityclash_speech_b", "My dear brother once said, If you haggle or trade with a Punic, you lose, if you race a Scythian on a horse, you lose and if you trust a barbarian, you lose your life."),
  ("npc24_personalityclash_speech_b", "Some of the stories he has told about his time sailing in the seas are lies, they must be. He told me that he once killed a huge sea serpent that was the length of a house. No such thing exists and even if it would, he'd be fish food by now."),
("npc25_personalityclash_speech_b", "The arrogance of {s11} grates on me. Perhaps they need to be reminded that respect is earned, not given freely. A sparring match might do them some good."),
  ("npc26_personalityclash_speech_b", "{s11} also said that I only speak and babble about concepts but don't even understand any deeper meanings of what I say. Some nerve he has, he's a sailor... they are the least deep and philosophical people on this earth!"),
("npc27_personalityclash_speech_b", "The north teaches us that men hunt, fight, and die - women stay home and keep the hearth. Letting her march beside us is folly. One day it will cost us dearly."),
("npc28_personalityclash_speech_b", "Women belong by the fire, not among spears and blood. And this one? She draws too many stares. Sooner or later, she'll bring trouble."),
("npc29_personalityclash_speech_b", "The arrogance of {s11} grates on me. Perhaps they need to be reminded that respect is earned, not given freely."),
("npc30_personalityclash_speech_b", "I have served alongside brave men, loyal men. But this one? He belongs to the pasture, not the war camp. I will not share the fire with him."),

### set off by behavior after victorious battle
  ("npc1_personalityclash2_speech", "If you don't mind, I'd prefer not to be deployed anywhere near {s11}."),
  ("npc2_personalityclash2_speech", "{Sir/Madame}. If you don't mind, I'd prefer not to be deployed anywhere near {s11}, after what he said to me during that last battle."),
  ("npc3_personalityclash2_speech", "Captain! Captain! I wasnt sure we would have gotten away this time...  But you did it! Thank you! Thank you! You are indeed a great leader."),
  ("npc4_personalityclash2_speech", "Sunicas is not much better than a Vandal, I've seen and heard of the Huns and they are in my opinion just as worthless as those who occupy us. Attila was a weak man, if we Berbers had fought against him, he would have lost a lot much sooner, Sunicas looks up to him? Shows the kind of man he is!"),
  ("npc5_personalityclash2_speech", "Captain. {s11} needs to have her tongue cut out."),
  ("npc6_personalityclash2_speech", "Warlord. Did you see {s11} during that last battle? A shameful display, let me tell you. We shouldnt hire these men in our group!"),
  ("npc7_personalityclash2_speech", "Captain, I have done my best to put up with your followers' rude talk and filthy habits. But that one who calls himself {s11} is beyond tolerance."),
  ("npc8_personalityclash2_speech", "Captain. {s11} is a most insolent girl. I have tried to be polite, even friendly, only to have her rebuff me."),
  ("npc9_personalityclash2_speech", "Dux, I hope you do not mind me telling you this, but in my opinion {s11}, the merchant, does not know his place. During that last battle, he cut in front of me to engage a foe whom I had marked for my own."),
  ("npc10_personalityclash2_speech", "{Brother/Sister} -- a question for you. Are you in charge of this company, or is it {s11}?"),
  ("npc11_personalityclash2_speech", "Captain. I don't much care for that {s11}. After that last battle, he went around muttering some heathen incantation, as he went through the slain looking for loot."),
  ("npc12_personalityclash2_speech", "Captain. I can no longer abide the rank ignorance of {s11}. As I was treating the wounded during our last battle, he saw fit to disparage my use of laudanum in relieving the pain while I conducted surgery, and of treating wounds with a poultice of honey."),
  ("npc13_personalityclash2_speech", "Oy -- master, I don't fancy myself a sensitive soul, but I don't particularly like how {s11} went about cutting the throats of the enemy wounded, back there."),
  ("npc14_personalityclash2_speech", "Sir. {s11} is incorrigibly indisciplined. During that skirmish, I called out to him that he should hold ranks with the rest of our battle array. He called back to me that I should 'get stuffed.'"),
  ("npc15_personalityclash2_speech", "Captain -- I must tell you that I question {s11}'s medical credentials. As he was tending to our wounded after that last battle, I saw fit to remind him that the peerless Galerian often advocated administering a distillation of beetroot, to restore the humor imbalance brought by loss of sanguinity."),
  ("npc16_personalityclash2_speech", "Beg your pardon, Captain. {s11} might have been a very good sailor, but he's not got the stomach to be a warrior, if you ask me."),
  ("npc17_personalityclash2_speech", "Mighty warlord, may the Gods guide your sword through the flesh of our enemies! I came here to tell you that I cannot stand that man, he thinks he's the best, he's the bravest... Pah! {s11} is but a rascal. Do not trust him!"),
  ("npc18_personalityclash2_speech", "That man of the forest, {s11} can't really wield a lance properly. My kin spent his life subjugating those weaklings in the forest-steppes north. I dont think he's such a great addition to our party."),
  ("npc19_personalityclash2_speech", "If you don't mind, I'd prefer not to be deployed anywhere near {s11}."),
  ("npc20_personalityclash2_speech", "If you don't mind, I'd prefer not to be deployed anywhere near {s11}."),
  ("npc21_personalityclash2_speech", "If you don't mind, I'd prefer not to be deployed anywhere near {s11}."),
  ("npc22_personalityclash2_speech", "General. I have something to talk with you. {s11} deserves to be hung from the nearest tree or crucified like in the good old days. We have no need for a young girl who thinks she's so much better than everyone else, and think about it a woman huntress, we Romans truly are superior, we do not strive to endanger our women by telling them to go hunting with bows and spears."),
  ("npc23_personalityclash2_speech", "{s11} is not the kind of man I'd like to keep close. I had a Nubian servant once, my brother bought him from Alexandria and he did fine, he could read, somewhat and calculate the diameter of a round table, after a few hours of course. But he was also arrogant, vain and tried to always show of his physical strength, my brother killed him after he had rode his horse without a permission, what a waste of labor."),
  ("npc24_personalityclash2_speech", "{s11} is nothing more than a man trapped in the past, some refuse to see what I already see crystal clear: Rome is falling and with it will fall their rule and grip of the the people they subjugated. The Eagle is tearing itself apart with the internal wars and disputes."),
("npc25_personalityclash2_speech", "{s11} is insufferable. They speak as if their way is the only way, ignoring the wisdom of others. If they were on the Danubian plains, they would not last a week."),
  ("npc26_personalityclash2_speech", "{s11} is a danger to true faith, he is a pagan, he follows the bloodthirsty words and deeds of the outdated, degenerate Roman gods! Great shame of mine that my ancestors too believed in them during the ancient times. But now we are awake, and we know the word and glory of the only God."),
("npc27_personalityclash2_speech", "Warlord. That northener, {s11}, he behaves like a barbarian from Scandza. A shameful sight. Men like that have no place in our shield-wall."),
("npc28_personalityclash2_speech", "I saw {s11} in the last fight. The way he flailed about - I'd trust a drunk with a blade more than that one."),
("npc29_personalityclash2_speech", "{s11} is insufferable. They speak as if their way is the only way, ignoring the wisdom of others."),
("npc30_personalityclash2_speech", "General. During our last fight, {s11} behaved like a fool. He lacked control, ignored your orders, and nearly cost us victory."),

  ("npc1_personalityclash2_speech_b", "{s11} is dishonorable."), #madsci generic response
  ("npc2_personalityclash2_speech_b", "The enemy was bearing down on us, and he says, 'Step aside, merchant, this is a warrior's work.' Next time I will step aside, and let him take a spear in the gut."), #marnid - alayen
  ("npc3_personalityclash2_speech_b", "After our last victory I was picking through the slain, and availed myself of one of our foe's purses. No sooner had I done so then {s11} came up behind me and struck it from my hands, saying that it was he who had made the kill, and thus he deserved the spoils. My lord, I could not tell in the heat of battle who had struck whom. If {s11} had simply told me that he deserved the purse, I would gladly have given it to him."),#Ymira - matheld
  ("npc4_personalityclash2_speech_b", "Vandals have employed some Huns so I have a reason to look at them with disdain, but I will for now tolerate that man, but only if he leaves me alone, I do not wish to interact with him, I have better things to do."),
  ("npc5_personalityclash2_speech_b", "When the loot was piled up after the last battle, I found among the enemy's baggage a very decent cooking pot. Often I had wished to find such a pot, so I could boil some of the stews that my people use to warm their bellies during the winter months. But {s11} grabs the pot, and tells me that I will not be allowed to 'taint' it with heathen food, and that it should properly belong to her. I yielded the pot to her, but I will not tolerate such disrespect in the future."), #beheshtur- katrin
  ("npc6_personalityclash2_speech_b", "Does he think he is a dangerous man? I will show him that feeble roman what a - TRUE - warrior does."), #firentis - nizar
  ("npc7_personalityclash2_speech_b", "He claims to be an educated man of his faith, yet he is no more than a filthy sailor; which speaks to his true nature..."),
  ("npc8_personalityclash2_speech_b",  "As we were cleaning our weapons after that last battle, I remarked that I thought her a handsome girl, and after I regained my lands I would happily find her a match with one of my warriors. I thought it was a very generous offer, as a woman disinherited by her father is hardly going to find herself awash in prospects. But rather than thank me, she simply turned her back without a word. It was only out of respect for your leadership that I did not immediately try to teach her some manners."),  #matheld - ymira
  ("npc9_personalityclash2_speech_b", "I appreciate that he is willing to risk his life in battle, but that alone does not make a gentleman. He is not of noble birth, and his family's wealth comes from commerce and usury. He may fight with us as an auxiliary, but should not attempt to steal glory from his betters."),# alayen - marnid
  ("npc10_personalityclash2_speech_b", "In that last battle he was shouting at me: 'Go forward, go back, hold the line.' When I told him to mind his own trimming he said he'd have the entire warband decimated.  Captain, that man is looking for an axe in his chest, begging your pardon."),
  ("npc11_personalityclash2_speech_b", "He said it was a prayer of thanksgiving for victory, but it didn't sound like that to me. Captain, I don't want him raising up the ghosts of the dead to make trouble for us on our travels. I think you had best be rid of him"),
  ("npc12_personalityclash2_speech_b", "Captain, if that man knew the slightest thing about medical matters, he would know that one should never undermine a patient's confidence in his doctor, particularly not during a complicated operation. If you would be kind enough to dismiss him from this company, you would be doing all of us a great service."), # jeremenus - artimenner
  ("npc13_personalityclash2_speech_b", "The way she whistles cheerfully as she does it -- it puts a chill down my spine, it does?"), #nizar - firentis
  ("npc14_personalityclash2_speech_b", "{Sir/Madame}, such defiance of proper authority is a corrosive influence on our company, and I shall have him flogged if he does so again."), #lazalit - bunduk
  ("npc15_personalityclash2_speech_b", "{s11} responded that Galenian was an 'antiquated know-nothing.' Captain, no true doctor would have such disrespect for the great masters of the past. I do not believe you should employ such an obvious impostor."), #artimenner - Artemios
  ("npc16_personalityclash2_speech_b", "After our last scrap, I was slicing open the guts of some our foes to check for hidden gold, as a girl who counts her pennies ought. He gagged and muttered that I was an 'animal.' I'll inspect his innards for contraband if he doesn't keep a civil tongue in his head."),
  ("npc17_personalityclash2_speech_b", "If he keeps strutting like that I'll end his life with my seax one of these nights."),#alachis - aistulf
  ("npc18_personalityclash2_speech_b", "We're fighting, open field battles, not skirmishing in some swampy forests. He needs to learn how to fight properly."),#khaetag - bogdan
  ("npc19_personalityclash2_speech_b", "{s11} is dishonorable."),#khaetag - bogdan
  ("npc20_personalityclash2_speech_b", "{s11} is dishonorable."),
  ("npc21_personalityclash2_speech_b", "{s11} is dishonorable."),
  ("npc22_personalityclash2_speech_b", "It shows you that Germanic tribes are either short on manpower or that their men are such effeminate weaklings that women need to hunt in their stead. Either way it should be easy for us to hunt them down and finish them like the dogs they are like you should deal with {s11}."),
  ("npc23_personalityclash2_speech_b", "{s11} reminds me of him quite a bit, he has said that people in his homeland are engaged in a conflict, is that a surprise when you look at him?, an extraordinary bowman? It is a coward's weapon fit for a black bastard like him, if you give me a pass I will duel him and we will see if he's a man. I do not wish to kill him, merely cut him a bit to teach him a lesson."),
  ("npc24_personalityclash2_speech_b", "He asked me a few days back that which side am I, on the side of civilization or barbarity. I said that I am on the side of my folk which he took as an offense, though I could care less if I offend him, he's a relic of a bygone era that the west and east will soon crush and once his dream is shattered, I'll be there to laugh at him."),
  ("npc25_personalityclash2_speech_b", "The arrogance of {s11} grates on me. Perhaps they need to be reminded that respect is earned, not given freely. A sparring match might do them some good."),
  ("npc26_personalityclash2_speech_b", "{s11} and I talked a while back and he said to my face that he intends to wipe out all 'cross-lovers' one day and that crucifixion is a great punishment to all followers of the cross. He even dared to say, 'Who cares if you worship Christ or a donkey, both are only mortals unlike Mars, Pluto and Jupiter who are divine' That is the very essence of blasphemy and the next time he dares to slander me like this I will use my staff and fists. He's pitiful band is almost stamped out, he should know when to give up."),
("npc27_personalityclash2_speech_b", "Does he think his strong arm and voice will save him? Let him step into the cold and prove his worth, or be gone."),
("npc28_personalityclash2_speech_b", "Let me ride ahead next time, and I'll show that soft-skinned fool what true warriors do on horseback."),
("npc29_personalityclash2_speech_b", "You should show that soft-skinned fool what true warriors do on horseback."),
("npc30_personalityclash2_speech_b", "A warrior without discipline is no warrior at all. I will make sure he learns what duty and precision mean - if he lasts that long."),

  ("npc1_personalitymatch_speech", "Captain, {s11} back there didn't do badly in that last fight at all. He's a good egg, too."),
  ("npc2_personalitymatch_speech", "{Sir/Madame}. I just wanted to tell you that {s11} may be a rough sort, but I'm proud to call him my companion."),
  ("npc3_personalitymatch_speech", "Captain... {s11} is such a great man... I might sound like a silly girl, but he truly is! He's honorable, brave.... Ooohh.... You should really take him into consideration! Just saying!"),
  ("npc4_personalitymatch_speech", "{!}."),
  ("npc5_personalitymatch_speech", "That was a fine battle, Khagan {playername} ! {s11} is a good man to have by our side in a fight."),
  ("npc6_personalitymatch_speech", "Warlord! We lost too many men in these last few days. I beg you, keep your men's lives in regard. We won't go nowhere without them!"),
  ("npc7_personalitymatch_speech", "Captain. I was just talking to {s11}. She may be a bit savage, but I believe that she is a faithful friend."),
  ("npc8_personalitymatch_speech", "{s11} is a most alluring and beautiful woman, that hair is like a gold wheat, those eyes like a jewel and the body a wonder to behold. You can't even understand how hard I have to fight against myself to not try seducing her, I think you should keep her away but not too far away so that I may bask in her radiance and look her in those eyes..."),
  ("npc9_personalitymatch_speech", "Dux. {s11} acquitted herself well in that fight back there. A fine, modest maiden she is, if I dare say so myself."),
  ("npc10_personalitymatch_speech", "Ahoy, Brother! I wish you joy of your victory! Say, old Mother {s11}'s not bad in a scrap, is she, for a woman of her years? Although I'm getting to be a bit of an old dog myself, now."),
  ("npc11_personalitymatch_speech", "Ach, captain! A fight like that one sets my old joints a-creaking. Still, we licked them pretty good, didn't we?"),
  ("npc12_personalitymatch_speech", "A bloody business, captain, a bloody business -- although a necessary one, of course. {s11}, I believe, shares my ambivalence about this constant fighting."),
  ("npc13_personalitymatch_speech", "Commander, {s11} might be haughty and selfish sometimes, but he is a true warrior."),
  ("npc14_personalitymatch_speech", "Captain. It is a pleasure going into battle with men like {s11} by my side."),
  ("npc15_personalitymatch_speech", "Captain. I was just having a word with {s11} after our last battle, and it strikes me that the man has got a good head on his shoulders."),
  ("npc16_personalitymatch_speech", "Oy -- captain. I was just having a chat with {s11}, as we picked through the bodies after our last little scrap."),
  ("npc17_personalitymatch_speech", "Oh powerful warlord! Your humble gasind, {s11}, is here to congratulate with you for your recent victories. Also, me and {s11} decided to bring you six scalps each to honor you! I like him, he's a great warrior... It is no coincidence he's a kinsman!"),
  ("npc18_personalitymatch_speech", "Chief, that Gutonez... {s11}. He's a good warrior and I respect his kin. He's of blue blood and his ancestors were all great warriors."),
  ("npc19_personalitymatch_speech", "Chief, I really like to serve with Marcus Lincinus Posca. Skilled engineer, modest in living, ambitious and yet honest. I appreciate that."),
  ("npc20_personalitymatch_speech", "It is a pleasure going into battle with {s11} by my side."),
  ("npc21_personalitymatch_speech", "{Sir/Madame}, {s11} is an exceptional man. I have often find myself in his company and he has even taken upon himself to teach me the way the Huns use their bows. Not that I would need it, but it has been very helpful in understanding the enemy"),
  ("npc22_personalitymatch_speech", "General. I want to tell you something. {s11} is truly and outstanding individual, a Roman, a great fighter and an officer. I like to think that my father was something like him. Keep him close and let him help you and we may achieve great things, I know it!"),
  ("npc23_personalitymatch_speech", "Captain, you remember when I said that I consider Romans to be barabarians too? Well I still do but {s11} I could tolerate at least for a while. He has a right idea how to deal with scum from outlands and that brutality is a virtue."),
  ("npc24_personalitymatch_speech", "Captain, I am glad you have brought a fellow kinsman, {s11} into our company. One who can relate to me both in culture and faith."),
("npc25_personalitymatch_speech", "{s11} handled themselves well in that last fight. It's good to see someone with both skill and humility. I think we'll get along just fine."),
  ("npc26_personalitymatch_speech", "Just like him, I've always been a fan of Romans, and I wouldn't trade my homeland for anything. Now, I understand that I might not be able to do that right away, but I'm sure I'll find a way to help my fellow Romans."),
("npc27_personalitymatch_speech", "Warlord, your shield-brother {s11} - he fights like a man born of storm and ice. That one, I trust with my back in battle."),
("npc28_personalitymatch_speech", "Warlord - keep men like {s11} close. He is quiet, but his arrows never miss. That is a man who earns his share."),
("npc29_personalitymatch_speech", "It is a pleasure to travel with {s11} by my side."),
("npc30_personalitymatch_speech", "General, your warband holds strong hearts. I ask you to keep men like {s11} close - their steadiness steadies us all."),

  ("npc1_personalitymatch_speech_b", "Just like him, we both with for our homelands to be free from their occupiers; in his case the Vandals, and in mine, the Romans."),
  ("npc2_personalitymatch_speech_b", "Based on how he did in that last fight, I'd say that I'd trust my back to him any day, not only in battle, but as a fellow trader."),
  ("npc3_personalitymatch_speech_b", "I also confess that I find him a truly delightful companion, a man of both wit and manners. Perhaps, perhaps... Ah, but I say too much. Good day, {sir/madame}."),
  ("npc4_personalitymatch_speech_b", "I approve of {s11}."), #madsci generic response
  ("npc5_personalitymatch_speech_b", "As for his other attributes, I doubt that he is any more a noble than I am, but I have to admire the brazen way he makes that claim."),
  ("npc6_personalitymatch_speech_b", "I must say that {s11} is a source of great comfort to me. I have told him of my sin, and he said to me that Heaven will forgive my transgression, if I truly repent and truly desire such forgiveness. He is wise, and I am glad that he is with us."),
  ("npc7_personalitymatch_speech_b", "At some point in the future, if you have no need of our services, she has promised to go back to the ravines with me and find the bandits who murdered my lover, and help me take my revenge. It was a kind offer. I am glad that she is with us."),
  ("npc8_personalitymatch_speech_b", "I do not know what about her makes me feel so... anxious or stricken but she has some kind of a hidden charm. She hunts and is actually a good hunter, that is one thing I can respect as well, she would be a good home maker, but I must contain myself, I made a vow and it is more important and stronger than any one woman, I would not forgive myself If I would surrender to her."),
  ("npc9_personalitymatch_speech_b", "Were she of noble blood, I might ask for her hand. It is a pity that she is a merchant's daughter. But speaking with her is a pleasant way to pass time on the march."),
  ("npc10_personalitymatch_speech_b", "Heh. It just goes to show that youth ain't everything, that experience also wins battles. I reckon she and I could teach the young puppies of the world a thing or two, couldn't we?"),
  ("npc11_personalitymatch_speech_b", "Old {s11} in particular showed them a thing or two, I thought. Not bad for the pair of us, I thought, given that between us we've probably seen close to a hundred winters."),
  ("npc12_personalitymatch_speech_b", "It saddens him deeply to take the lives of his fellow men, however just the cause. He and I have talked together of a brighter future, of the need to unite these petty warring kingdoms, so that we may bring this time of troubles to an end."),
  ("npc13_personalitymatch_speech_b", "Either on horseback or on foot he is impetuous and undisciplined in charging, as if he is the only man in the world who is not coward."),
  ("npc14_personalitymatch_speech_b", "He is a professional soldier, and though he may not be as fast on his feet as some others, he knows the wisdom of holding together in a disciplined battle-line. You showed good sense in bringing him into this company."),
  ("npc15_personalitymatch_speech_b", "War, like any other affair, requires careful planning and preparation, and a firm grasp of strategic principals. All other things being equal, the best trained army will win the battle, an observation that I think our last fight bears out. The men may curse him now, but they'll learn to thank him, I'll warrant."),
  ("npc16_personalitymatch_speech_b", "Have you heard her story? Can you believe the wrongs done to her? I tell you, it makes my blood boil. I want to cut off all the little bits of those bastards who mistreated her -- and I'll do it, too, if we ever run into them in our travels."),
  ("npc17_personalitymatch_speech_b", "He's a warrior by heart, skilled, tempered, bloodthirsty... I wish all your soldiers were like him!"),
  ("npc18_personalitymatch_speech_b", "After today's battle I'm glad I can call him my friend and brother, even if not by blood. Warriors do not need to be in the same family if we all shed our blood together."),
  ("npc19_personalitymatch_speech_b", "Although he is an engineer from Roman schola and I am mere barbarian, we got along preety well, and listening to his monologues about masonry and siege machines was very intriguing for me."),
  ("npc20_personalitymatch_speech_b", "I approve of {s11}."),
  ("npc21_personalitymatch_speech_b", "Even though he keeps the Roman God and follow the Old Ways of my people, he is a good man and the world would be a better place if there were more men like him."),
  ("npc22_personalitymatch_speech_b", "We need more experienced and hardened Romans if we are to drag Rome from its low point to the light of true Gods, we need those who dare and who can hold a shield and sword, those who can fight to bring order to this land. Men like I and {s11}."),
  ("npc23_personalitymatch_speech_b", "Don't get me wrong he is still a filthy barbarian and I didn't like his remark when he said that 'Merchants are worse than murderers, they steal your coins and so your life' But I've grown to tolerate him, at least. I wonder if I'm becoming sick, I'm usually more stoic."),
  ("npc24_personalitymatch_speech_b", "A reliable warrior, and what I could consider a friend of mine. We ought to look for more men like him."),
("npc25_personalitymatch_speech_b", "I appreciate {s11}'s perspective. They understand what it means to fight for something greater than themselves, just as I hope to do for my people."),
  ("npc26_personalitymatch_speech_b", "I'm glad you found me, {playername}. I hope that we will meet again soon."),
("npc27_personalitymatch_speech_b", "He reminds me of the warriors of the old tales. Strong in arm, and silent in pride. With him in our company, we shall go far."),
("npc28_personalitymatch_speech_b", "He reminds me of my kin, the hunters of the mountain passes. Sharp eyes, steady hands. I respect him - truly."),
("npc29_personalitymatch_speech_b", "You could say that I approve of {s11}."), #madsci generic response
("npc30_personalitymatch_speech_b", "He reminds me of comrades from my old regiment. Reliable. Brave. A man with such character makes this chaos bearable."),


  ("npc1_retirement_speech", "Captain, to be honest I have grown tired of you and wish to return to the seas, I am never happy on land I must be riding the waves, that is what I was born to do, so I will be leaving, I hope you understand."),
  ("npc2_retirement_speech", "I'm getting a bit tired of the warrior's life. I think I have enough gold to quench my former trade master's wrath and who knows - maybe I'll return to simple trading. I would like to thank you again for taking me on, and wish you the best of luck."),
  ("npc3_retirement_speech", "Captain... I cannot live this life anymore. The lives we took, the pain we caused... I know you will tell me I knew what joining a warband meant, but it's simply false. I wasn't aware. Not completely at least! I beg you, leave me be. Maybe one day we will meet again."),
  ("npc4_retirement_speech", "When I met you I thought that by staying on your side I could reclaim the lost glory and drive the Vandals out of Africa. I now think that both of these are not realist and I think maybe I should leave for the cities of Mauri, leave a more quiet life there."),
  ("npc5_retirement_speech", "Khagan -- since I have taken your salt, I have fought for you fiercely, and loyally. But you have not always repayed my service with the kind of leadership that I deserve. So I am going home, in the hope that the Khan's men have forgotten me, to see my father and brothers again."),
  ("npc6_retirement_speech", "Warlord! Take no offense but we're not going anywhere here. I believe I will be on my path, alone, or maybe I will fetch a group of warriors and carve my own name into the old men's tales. Forgive me, Warlord, for I love you truly as you're my companion. But I can't stay any longer."),
  ("npc7_retirement_speech", "Captain, I shed my blood for you and this woman would have never thought about becoming a warrior. However, now I have some money in my purse and I have to do a thing. I have one last quest to do. It's now or never. I will find those Burgundians who sentenced me to live as a fugitive my whole life and I will give them a long and painful death. Do not come with me, this is something I have to do alone."),
  ("npc8_retirement_speech", "I have thought about things lately and I think it is time I try to return back to my tribe, who knows maybe they have forgiven me already, I can still continue my quest but I'd like to see them after all these years, so I'd like to leave if that's okay."),
  ("npc9_retirement_speech", "We have fought well together, and earned ourselves much glory. But I have some reservations about your leadership, and at any rate have my patrimony to reclaim. I will be leaving you. Perhaps we will meet again."),
  ("npc10_retirement_speech", "It's time for me to return home and tell my people about everything I've seen. I'll tell them that Italia is a wealthy place, its soil is rich and its sun is warm. And what's most important - the people who live there became fat and lazy. Farewell, maybe we'll meet again one day, as friends, or foes. You know what choice would be better for you, haha!"),
  ("npc11_retirement_speech", "You did an old woman a great service by taking her into your company. But I'm afraid I'm finding this life no more to my liking than driving a wagon. Too much cold, too much hunger, and at the end all I see in front of me is a hole in the ground. So I'll be off, although I don't know where."),
  ("npc12_retirement_speech", "Forgive me, but I have to tell you something. In the last town we visited I spotted a sick man - his symptoms were unlike anything I've seen before. You told us to gather our things and move out, so I had no time to examine him closer. And right now I think that my duty, as a trained medicus, is to go back and do my best to help him. No one in your party is sick or seriously injured, so my services are not necessary here. I'll try to help him and then return to you, if possible. Farewell!"),
  ("npc13_retirement_speech", "Commander!, I joined this warband because you looked influential and respected, and you are. However, things are not going as I expected. I might take some time for myself now and I'll look for opportunities elsewhere. I hope we meet again, commander."),
  ("npc14_retirement_speech", "I would like to inform you that I wish to sever our relationship. I intend to seek alternative employment."),
  ("npc15_retirement_speech", "I appreciate that you took me on, but I'm not altogether happy about how things have worked out. I'm going to head off elsewhere -- maybe go home, maybe find another job, I haven't quite decided yet."),
  ("npc16_retirement_speech", "I've had good times in this company, and I've found myself a pretty trinket or two on the battlefield, but right now it isn't working out. I'm leaving you to go offer my talents to someone else."),
  ("npc17_retirement_speech", "So what, you leave me here!? I wont stay idle while you and your eunuch boys roam around pillaging... I'll find another warlord to serve! Say what, warlord? Fuck you!"),
  ("npc18_retirement_speech", "I know I may have been annoying some time, but I did not expect to be left like this. I'll go to the Romans of the East, I heard they may need men fighting the Huns in Crimea. That might finally be my chance to clear the name of my family. If I survive... Well, I hope to see you around."),
  ("npc19_retirement_speech", "I have to take rest. Too much fighting, too many quarrels, I... just need to take a leave."),
  ("npc20_retirement_speech", "I'm getting quite tired of travelling now. Never thought I would do this much. Maybe I should just settle down somewhere... Thank you for taking me on, I hope to see you again."),
  ("npc21_retirement_speech", "I think I see what you meant back when you hired me. War is hell, it is even more terrible than what I ever imagined. I have made enough gold and I wish to take my leave. Do not worry, I am not foolish enough to ask for Valentina's hand."),
  ("npc22_retirement_speech", "I have grown very doubtful about the possibilities we have. I see now that I am not worthy of the old Roman officers, I don't think Majorian would want me into his army. Henceforth I have decided to retire somewhere far away and die there in peace, Rome is doomed and with her, the world."),
  ("npc23_retirement_speech", "I've travelled with you and lived in this society for long enough to see that there is no saving or educating the plebeians or the Goths, Vandals and what else, I've decided to go somewhere where I can live in peace, I'm tired of men, I'm tired of war, I'm tired of politics, and I'm tired of life so I will be going and you cannot stop me."),
  ("npc24_retirement_speech", "Captain... to be frank, I wish to go back to my homeland, I wish to see the large forests and open taiga, I've grown tired of just walking around, even if I've had good experiences travelling with you."),
("npc25_retirement_speech", "Captain, my time with you has been invaluable, but the road calls me back to my people. My father grows older, and I must take up the mantle of leadership. Farewell, and may your path be filled with victory."),
  ("npc26_retirement_speech", "The word of God must be spread, but my strength wains and my willpower erodes, I think I will retire for a while... maybe to Hispania, I have friends there."),
("npc27_retirement_speech", "I have to take rest. Too much fighting, too many quarrels, I... just need to take a leave."),
("npc28_retirement_speech", "Warlord! I have given you my arm and my loyalty, but the wind calls me back to my people. I must return to my tribe and ride once more with my kin. This life has taught me much, and I will speak of it around the campfires of my homeland."),
("npc29_retirement_speech", "Warlord... This path we walk is bloodier than I imagined. I joined seeking purpose, but I fear this life of war may not be mine to live. I shall leave your warband, with respect and gratitude."),
("npc30_retirement_speech", "General, with due respect... this path leads nowhere. I have served with dignity, but now I must follow my own road. Perhaps, if the winds favor me, I will build a quiet life back in Persis. Until then, may your sword strike true."),

  ("npc1_rehire_speech", "Well did not get to a ship, the port master here said that he won't hire me because I look too gruffy and risky, so can you hire me back, you at least trust me, unlike these shabbaz."),
  ("npc2_rehire_speech", "{Sir/Madame}! It's good to see you again. I took my gold and embarked on a ship going east but Ahriman, evil spirit, cursed me again! Ship sank again and I nearly drowned as well trying to grab my sack. I had to choose - either die as a rich man or let it go and live as a poor man. And here I am, so it's obvious what choice I made. I'd be honored and grateful if you let me join you once more."),
  ("npc3_rehire_speech", "Look who's here! Captain! I am so happy to meet you again. I see you're alive and well, that is good! How are the others? You know, things here aren't going that well... I would be very happy if you were to give me a second chance in your group. I miss the others!"),
  ("npc4_rehire_speech", "So you must think, why I am here? Well the Gaetuli robbers took almost all I had and now I have lost my will to live, do you wish to help me regain my honor and my wealth?"),
  ("npc5_rehire_speech", "{playername} , my Khagan! Your fame grows ever greater -- even as far as my homeland, beyond the Pontos. I'd returned there, hoping that the Khan's men had forgotten. Well, they had not -- even before I set foot in my valley, I had word from my family that both the Khan and the Humyan were looking for me. So I came back again, hoping you might forget any harsh words I had spoken, to see if I could fight with you once again."),
  ("npc6_rehire_speech", "Oh, Warlord! Brother! It is me, Wadomar. Your humble servant. Long time has passed since we last met and I had my share of adventures and deeds in the meantime... But nothing gives me the same feelings I had in your warband. I am here to ask you for forgiveness. I want to rejoin the group!"),
  ("npc7_rehire_speech", "Captain! Captain! It's me, Ingrid! I... I am back. I did what I had to do and I feel relieved now. My husband is avenged, as well as my daughters. I am ready to rejoin you, if you will let me."),
  ("npc8_rehire_speech", "Well, they didn't wish to see me, the elder cried that if I step one more time to their camp I'd be killed, so I guess it's back to the road, willing to take me back?"),
  ("npc9_rehire_speech", "My dear, dear Dux which I love truly! So good it is to see you! I have sought service with the lords of this land, but have been most grieviously disappointed. Half of them ask me to collect debts from fellow lords, as though I were a banker's errand boy, or chase down his serfs, as though I were a farm overseer. One even asked me to murder one of his creditors! I have looked for you, to see if you would wish me to join you again."), #Alayen
  ("npc10_rehire_speech", "Is that you again? I've decided to work for someone like you again, but now when I see you I can't imagine joining any of those fools. We had a good time together. It seems the gods want us to fight side by side again. What say you?"),
  ("npc11_rehire_speech", "Captain! So good to see you! People say that you've been making gold hand over foot. I'm a fidgety old bag of bones, I'll admit. I left you because I wasn't satisfied with the warrior's life, but I spend a bit of time in town and I realize that there are worse things in life than a full belly, honest companions, and the joy of seeing the enemy run before you. So, would you be hiring again"),
  ("npc12_rehire_speech", "Welcome again! What an auspiciuos meeting! Do you remember that sick man I mentioned to you? It turned out his illness was very serious. The fever and coughing resisted everything I did, even the most scientific treatment. Plucking hair from his nose, flogging his back with copper rods, bathing his feet in boiling urine... And the patient was more miserable with every new method I applied. Unfortunately all my efforts were for nothing, I couldn't save him. At least his family was very grateful that I cared for him in his last days. I did what I promised to do - to help others in need. Now I'm ready to join you again. Do you need my help?"),
  ("npc13_rehire_speech", "Commander! It's me, Eirpamone! I'm so glad to see you. How are the things going in the warband? How many enemies did you slain? I found myself without an occupation again, for the moment. So if you need an extra hand, I would be willing to come back... If you let me."),
  ("npc14_rehire_speech", "Captain. It is good to see you. When last we parted, I was ready to swear that I would not serve you again, but perhaps I judged you too harshly. All over, men sing your praises. I have tried serving in other lords' armies, and believe me, what I have seen of them restores my opinion of your leadership. If you would have me in your company, I would fight for you again."),
  ("npc15_rehire_speech", "Why hello, {playername}. I can't say I'm entirely displeased to see you. You see, I took on another contract before I left, and sure enough, when it came time to collect the pay, the lord had nothing but talk and excuses and petty little complaints about my handiwork. I can't say I was always happy in your company, but at least I put gold directly into my purse after every battle. You still offering work?"),
  ("npc16_rehire_speech", "Captain! They say that you've done well for yourself since we last met. I'll come out and admit that I cursed your name when we parted ways, but thinking back on it you weren't all that bad. All these lords, they're glad enough to send me on little side errands, but they don't much care to have me in their main battle-line. Apparently I spook the men. I've heard it muttered that I'm a witch, or that I eat men's hearts after killing them, or other rot. Not that I mind stabbing a man while he's asleep, but it's a lot more gratifying when he's awake and kicking. So I thought I'd try to find you again, see if you'll take me on."),
  ("npc17_rehire_speech", "Hoi! Hoi! Warlord! It's me! Do you remember me? It's your loyal, humble servant Alachis, the best of your host! I know last time we left us with some grudges... But please, I'm a lost man without your guidance! I killed my last employer because he wasnt like you... Please... Take me back with you, warlord!"),
  ("npc18_rehire_speech", "Chief! Is that you? It is! I'm glad to see you alive and well, let me hug you with my very own arms. I have many good things to tell you, I served the Romans of the East for a while. Fought in Crimea and then against the Sassanids of the East. But if you seek my services, I'm willing to lend you my sword again."),
  ("npc19_rehire_speech", "Chief, I am glad to see you again. I feel kind of in debt with you since you recruited me in the past, armed, fed, and pay me and yet you are still here. I decided to reenlist at your service. Would you welcome me back?"),
  ("npc20_rehire_speech", "Ah, {playername}, it is good to see you once again. Do you need another warrior in your company still?"),
  ("npc21_rehire_speech", "{Sir/Madame}, is good to see you again! I may have underestimated how much money I need to make it back to my village safely and although my family is better than they had ever been, I would not like to return empty-handed. I know I disappointed you by leaving, but perhaps would you consider hiring me again?"),
  ("npc22_rehire_speech", "Oh General! What luck to see you here! I was going to retire into the island of Hibernia but some Goths robbed me of my coins, my luck and so I'm again forced to seek solace from a tavern, no one here cares about me and I'm not sure how long I can fool the tavernkeeper by saying I'm rich and I will pay him soon, so...can I come with you, we could begin again!"),
  ("npc23_rehire_speech", "Seems like we meet again, last time we met I said that I am tired of it all and still am but I realized that without coins it is hard to retire or be without a care so I'm forced to offer myself to you again, I feel disgust but I do not wish to wither away in some Roman gutter, Will you take me back?"),
  ("npc24_rehire_speech", "I could not make it, too many Iazyge bands and other dangers, I think I'll gather a personal retinue... then I'll go back, unless you wish to hire me again right now?"),
("npc25_rehire_speech", "Captain, it seems my return to the Danubian plains was premature. My people are not yet ready for my leadership, and I find myself missing the road. If you will have me back, I will ride with you once more."),
  ("npc26_rehire_speech", "God's light only carries so far, I took a carriage to Hispania but we were ambushed by Goths and most of my belongings were taken, what little I own. Please take me back to your group so that I can continue my mission."),
("npc27_rehire_speech", "{playername}, I am glad to see you again. I feel kind of in debt with you since you recruited me in the past, armed, fed, and pay me and yet you are still here. I decided to reenlist at your service. Would you welcome me back?"),
("npc28_rehire_speech", "Warlord! The gods smile - it is you! I thought I had found my path, but I was wrong. Your warband gave me purpose, and I wish to ride at your side once more, if you'll have me."),
("npc29_rehire_speech", "Warlord! What fortune to see you again. My time away was filled with chores and wandering, but none gave me the sense of belonging your company did. If you'll have me, I would return to your side."),
("npc30_rehire_speech", "General! It is good to see you again. The road has taught me many things, but none so valuable as the strength of discipline and purpose I found under your banner. If you'll have me, I am ready to serve once more."),

#local color strings
  ("npc1_home_intro", "Jerusalem. The holy city of many religions and a source of endless bloodletting and disputes, I almost died here some years back, it was a terrible affair which included jealousy and love, I also lost my brave friend Ishmael here?"), #Jerusalem
  ("npc2_home_intro", "We're approaching the pass where the cursed bandits attacked us."),
  ("npc3_home_intro", "Can you smell that? Lemon trees, apples and crocus flowers, it's the scent of Italia, where I was born. I spent many a happy summer in Rome when I was a girl, playing in the gardens of my mother's family while my father was away trading."), #triggered around ravenna
  ("npc4_home_intro", "Tingis is a beautiful city and well-fortified enough that not just anyone walks over that city, I admire it in a way even though it has been decades since it was taken by Vandals."), #triggered around tingis
  ("npc5_home_intro", "Khagan! What Gods do you pray to? I pray to the Four Winds. Christians here in the warband believe they're God is stronger and powerful... Pah! Bollocks. My Gods live in the everlasting skies... And we're all beneath them!"), #triggered around olbia
  ("npc6_home_intro", "We keep passing by the ashes of this Empire, Warlord... "), #triggered around narbo
  ("npc7_home_intro", "Before joining your warband I was a lost soul, captain. I owe you much."),
  ("npc8_home_intro", "Nova Trajana Bostra that name makes me so angry... my hear burns with fire every time I see that cursed town and that theater."), #unused
  ("npc9_home_intro", "Britannia! My lost home. Rome has been here shortly, but left a good mark on these lands. Now that the Empire is gone, many crave for its return."), #corinum
  ("npc10_home_intro", "Watch out, we're approaching the lands of the Langobardi."),
  ("npc11_home_intro", "I see the the forests. We must be getting near home."),
  ("npc12_home_intro", "We're passing by the site of one of my greatest medical triumphs, if that interests you."),
  ("npc13_home_intro", "Commander, this is my land. Nubia. I was born in a hamlet along the Nile and therefore I enjoyed the pleasures of a good life when I was a kid. Although, the desert has been my companion since I was a little boy. The Nile is the guardian of life, but you just need to take few steps towards the horizon to find out that life is a precious but feeble gift, to be protected to the death."),
  ("npc14_home_intro", "Do you see that city over there? Rome -- the former capital of the Empire."),
  ("npc15_home_intro", "You see that city over there? Constantinople, the eastern empire's capital."),
  ("npc16_home_intro", "Aye, captain, do you see those? Those are hare tracks on the ground. We must be getting near to my birthplace."),
  ("npc17_home_intro", "Warlord!, What gods do you pray to? I have many Gods, but the greatest is Godan... The one-eyed Allfather!"),
  ("npc18_home_intro", "I was talking with the men the other day..."),
  ("npc19_home_intro", "Ach yes, the endless forests, some scattered gords... I feel we're are next to home."),
  ("npc20_home_intro", "Unfinished - you shouldn't see this"), #might use
  ("npc21_home_intro", "Ages ago, my ancestors called this land Medewi, in honor to the city where the Old Kingdom had its center. Now its nothing more than a collection of nomadic tribes and petty lords who deign to call themselves Kings. The one in the lands you call 'Nobatia' is the most powerful, but it is not the only one."),
  ("npc22_home_intro", "Eternal City, Rome the city with seven hills, where our story began, where my ancestors lived in peace and from where civilization was brought to all and the light of knowledge was lit.My home, oh how terrible fate you have suffered!"),
  ("npc23_home_intro", "Athens! My dear home and the site where I made my first political debates and where I met my first Spartan, not a pleasant experience, they are brutish uncouth warriors but dumb as mules!"),
  ("npc24_home_intro", "That is {s21}, I have some bad memories of this rotten city."),
("npc25_home_intro", "My home lies between the Danubius and the Tissus, where the Iazyges have lived for centuries. It is a land of open skies, swift horses, and proud traditions."),
  ("npc26_home_intro", "{s21}! My home and the home of so many great saints."),
  ("npc27_home_intro", "{s21}! My home and the home of so many great heroes."),
("npc28_home_intro", "Warlord, the dust in the air, the smell of olives and salt... this reminds me of Volubilis."),
("npc29_home_intro", "Look around, Warlord... So many lands once part of mighty empires, now left to dust and stories."),
("npc30_home_intro", "General... do you smell that? Dates and river clay. We're nearing the lands of the south, near my homeland."),

  ("npc1_home_description", "I was on a holy mission to Jerusalem and to my delight and misfortune I fell in love with a Christian woman, a wife of a Roman officer, my comrade Ishmael was with me and he told me that I should try to get this woman for myself, well we ended up having a fairly hot night but her husband came back early and he was so enraged that he almost killed me but I jumped out of a window before he could swing his sword at me. This caused a riot in the Christian quarter since he told people that I had raped her and... all right I was rough with her but nothing like that happened, I swear on my mother's grave!"),
  ("npc2_home_description", "At first we only saw a lone rider observing us from afar. He followed us for a day or two, never approaching too close. Then he disappeared, much to our relief. Unfortunately, as it turned out, it wasn't a good sign."),
  ("npc3_home_description", "Italy has wet winters and hot summers, but the people here build great cisterns to water their crops. They grow grapes -- Italian wine is famous, {sir/madame} -- and those who can afford it make walled gardens, where fruit trees grow in abundance, and we sit at night listening to music, or playing chess, or merely sniff the night air."),
  ("npc4_home_description", "My grandfather won much glory in the fights they used to held there, it was no rules and to the death. It was from him my father learned the art of battle and war..."),
  ("npc5_home_description", "Next time I hear one of them talking like that... I'm going to challenge them to a duel! Pah! And we'll see who the Gods favour for real."),
  ("npc6_home_description", "Many men died to conquer all these lands, defeat all these enemies and yet... It is all vanishing now. God has sense of humour!"),
  ("npc7_home_description", "With you I found a loyal friend, and many other good people along the way. You're family now and I am thankful for that."),
  ("npc8_home_description", "I and my father have tried to take Busrana many times from the Romans but they have always had a strong garrison here and they even used to mint their own coinage here, I even heard from my father that once the Romans had an Arab emperor who respected Busrana but I think that's just my father telling tall tales or trying to impress us."),
  ("npc9_home_description", "My family was born here, by my mother's side, my roots trace back to Hispania but my father's... My father's family was from here long before Rome arrived."),
  ("npc10_home_description", "These are the land we claimed from the pitiful fools who lived there before us. We came from the north like a storm. I tell you - when the whole tribe marches - nothing can stop it. We both travelled far and wide and I've seen many tribes and cities. And mark my words - if I say that nothing can stop us - then I know what I'm saying."),
  ("npc11_home_description", "I'm from Frankia. You know the saying, Dux -- 'Barley grown in Frankia is made into ale in Augusta Treverorum, and we're all the better for it.' Not sure what that means, Dux, but it's true about the barley. And wheat, and oats. We grow more grain here in Gaul then all the rest of the Empire put together, and our ale is the best, too. You can see it in the soil here -- rich and black, and smells of good harvests and full bellies."),
  ("npc12_home_description", "It was no more than five years ago. I was still living in this town when local bishop's servant came to my house begging for my help. As a renowned medicus I immediately went with him to the bishop's palace. There I saw the bishop - he had a high fever and was clutching his stomach. He vomited all day yet illness did not go away. I observed him closely and touched his ears with the copper rods repeatedly. It didn't help him though and on the next day he was still very ill."),
  #("npc13_home_description", "I had been raised by a my rather poor family during the rather turbulent times in the Empire. Eventually in my early teenage years, a barbarian army raided our village, and me and a few of my close friends were able to escape to Constantinople."),
  ("npc13_home_description", "The Nile for us means everything. We are its wardens and we know its course since the source, way more south. You know, you barbarians from the North believe that the world ends there, and south of Nubia only animals live: but I can tell you, it's not true. Plenty of land and other tribes lie south! We call them the southern barbarians and their land truly is endless."),
  ("npc14_home_description", "Once the great imperial capital, The eternal city was sacked in 410 by the Gothic barbarians, and again in 455. Dark times during the Empire. However, we've endured."),
  ("npc15_home_description", "There's no greater city than Constantinople today. Rome is nothing but a provincial town nowadays... Sad, that's true, but still. If you want to see a real capital you should come here, there's nothing greater than this city."),
  ("npc16_home_description", "We Persians are a noble kin. Romans despise us, and that's only because they cannot stand someone can actually put a fight against them."),
  ("npc17_home_description", "However, I seldom pray to him... He doesnt listen..."),
  ("npc18_home_description", "Some of them are good men, honest, brave... A shame no one will remember them after their death. You, maybe you and me... Someone will tell tales about us but most of these names will be lost in the sands forever. Time is cruel, and in hundreds of years just the great men will be remembered, while the common soldiers will have no names..."),
  ("npc19_home_description", "You know we are a simple people. Most of us can't even afford proper clothing, let alone armour. Most go in the field with large shield, spear and rarely axes. Some chieftains might don clothing or even chainmail. And a sword, as sign of authority."),
  ("npc20_home_description", "{s21}..."),
  ("npc21_home_description", "You must know, our people are not a single entity. Many have come from afar and have called this place home, adopting our customs and Gods as their own. The differences are still there, however, please do not expect me to intercede for some of these men are my enemies as much as they are yours."),
  ("npc22_home_description", "You may not know this, but Rome used to be a capital of the world, all roads led here and everyone who had the luck of calling themselves Roman were well-off. Now it has been ravaged by war, by disease, by poverty and no longer it is a significant town."),
  ("npc23_home_description", "I was debating with a certain patrician man about the prices of rye and fruits and demanded that if we are not able to provide for our citizens then we should just take from neighboring polises. He called me a warmonger and a bloodthirsty demagogue. Me! a supporter of demoskratos! people's rule! Spartan visitor happened to hear our debate..."),
  ("npc24_home_description", "I was once visiting this town and I was wearing an amulet that I was given by my mother, it brings health and luck to a person. One day I lost it, while staying in this town, I still believe it was stolen by some sticky-fingered thief."),
("npc25_home_description", "The Danubian plains were once the domain of the Iazyges, masters of horse and spear. We were feared by Rome and respected by the steppe tribes. But those days are gone. The Huns have weakened us, and the Ostrogoths press from the east. Yet, it is still my home, and I will one day return to lead my people."),
  ("npc26_home_description", "The Greeks called the city Hierosolyma and those who came before me, our priests named it Urislem. Nevertheless it is the most sacred of sacred amongst my people, I vowed that I'd spread the glory of this city anywhere I went and so I have done."),
  ("npc27_home_description", "{s21}..."),
("npc28_home_description", "Once a mighty Roman city, now crumbled and overgrown. But we, the Baquates, roam its bones freely, making our own laws beneath the open sky."),
("npc29_home_description", "In Ctesiphon, where I was born, we spoke many tongues and shared many meals - Persians, Romans, even Armenians. But the winds of war carried most away. I miss it, still."),
("npc30_home_description", "Persis is a land of fire and memory. Our hills bear the weight of empires, our villages still speak the name of Darius. I left to seek gold... but my heart remains there."),

  ("npc1_home_description_2", "The Christians started hunting down Jews soon enough, my friend Ishmael was caught by them early on one morning and the last thing I could hear was 'Shimon, run, run!', I have no idea what happened to him, but he is dead for sure. I heard the mob chanting 'Behead Jews' and 'Death to the Israelites' I run out and run like I have never run before, after I am out of the gates I 'borrowed' a horse and vowed that I would never enter this city again, I much more prefer the open seas anyway than the confines of a town, still I would not mind seeing her again..."),
  ("npc2_home_description_2", "The lone rider disappeared, but the horde appeared. He must've informed his kin of the easy prey heading to the valley. They blocked both entrances and trapped us inside. Then stones and arrows fell on us like a hailstorm... We fought fiercely but it was the captain of our guard who saved us. He realised we'd be doomed if we stayed there and led the charge which broke through the nomads' ranks and allowed us to escape with some of our goods. He died of his wounds, slain by the spear, but so did the chief of the nomads."),
  ("npc3_home_description_2", "However, now this land is just a shadow of it's former self. I am afraid Italia will never recover from this, Rome is dying and there is no other hope for us."),
  ("npc4_home_description_2", "The streets of Mauri controlled cities are not very safe and the ability to beat a man in dishonest fight is as an important skill here as is cooking in some more peaceful lands. I have been in many street brawls and have never lost one, I haven't been very brutal against my attackers except the one who insulted my mother, he ended up into the sea in bits."),
  ("npc5_home_description_2", "They're all afraid of us, Hunni! And even now that our nation is in shambles, they keep paying our Khagans not to raid their clay!"),
  ("npc6_home_description_2", "Not that I dislike this! It leaves - us - the space to find a place for our kin! We're the new that advances."),
  ("npc7_home_description_2", "Maybe you don't like to talk, but I wanted to express you my gratitude regardless. I will always be at your side."),
  ("npc8_home_description_2", "Busrana even has baths and other entertainment. Can you imagine those fat cats in there taking baths when we sieged that place, they mocked us and didn't even consider us real threats, but mark my words, that place will one day belong to us."),
  ("npc9_home_description_2", "They benefitted much from Rome, as the Empire gave his citizens much to rejoice, but now that Rome abandoned these lands and the barbarians are at the gates I don't know what future lies for Britannia."),
  ("npc10_home_description_2", "All those fools are just lucky our king Aldihoc is satisfied by his lands so far. It's good, I admit. Full of streams and fields, and there's plenty of game in the forests covering the valleys. But, as your people say, all good things come to an end and one day we'll march again. I don't know where, but I would build higher walls if I were one of those Romans living in Italia..."),
  ("npc11_home_description_2", "My ancestors weren't from these places. Once Frankia was in Germania, a greater land far West. I'm sure you've been there plenty of times. But in Germania wheat and barley do not grow as strong as here. Gaul is our new home, and this is where we will build our own empire one day."),
  ("npc12_home_description_2", "During night he had a nightmare - he saw a rotten bush which grew out of the spoiled seed. I immediately recognized that the source of his illness is his own spoiled seed lingering in his body, so I immediately castrated him to save his life. He resisted fiercely, not thinking clearly because of the fever, but in the end the illness vanished on the third day and his life was saved. All young boy servants living in his palace seemed very grateful for what I did, for saving their mentor's life."),
  #("npc13_home_description_2", "While my friends and I were in Constantinople, with little to nothing we decided to join the Emperor's newly formed imperial guards, the excuibitors. Ever since then I have not been able to visit my former home."),
  ("npc13_home_description_2", "You could march along the shore of the Great Sea for months and still not being able to find the end of this huge land. There are so many things that you barbarians don't know, but still, you claim yourselves to be the rulers of the known world. Pah!"),
  ("npc14_home_description_2", "Eventually we'll be able to retake the lands we have lost, and build the Empire to its height once more."),
  ("npc15_home_description_2", "If I will ever retire I'll come here, buy myself a good house, find a good wife and have a bunch of kids. In this changing world, with barbarians at every corner, this is one of the few places that will survive the test of time."),
  ("npc16_home_description_2", "However, here we are. My homeland, my kinsmen, are fighting against the Empire in the West, that you call East, but they can't manage win. In time, my glorious Emperor will breach the walls of Constantinople and conquer all those lands that lie beyond."),
  ("npc17_home_description_2", "But he's strong! If I die, I have to go before him and he will ask: what's the rule of steel? If I dont know it, he will cast me away. That's Godan, powerful in the Valhall!"),
  ("npc18_home_description_2", "... But all those that shed their blood for you? They're like dead already, if your name cannot live after your death, you're dead already. Am I annoying you with these things? I'm sorry, after some time together you probably understood I'm not the most positive person you can meet."),
  ("npc19_home_description_2", "People are poor, we certainly do not feel great future in this God forsaken land. And yet something keeps us there. I expect that if we ever move out, it would be some event of history note!"),
  ("npc20_home_description_2", "People are poor, we certainly do not feel great future in this forsaken land. And yet something keeps us there. I expect that if we ever move out, it would be some event of history note!"),
  ("npc21_home_description_2", "I have but one advice, {Sir/Madame}, we must avoid their archers no matter who we are fighting whilst we are here. Some of my kin dipped their arrows in poison whilst others, even if not poisoned, are so precise they might take an eye, perhaps both."),
  ("npc22_home_description_2", "The countryside around Rome is not safe, all manner of criminals walk these hills and sometimes barbarian hordes penetrate almost to the city itself. What an insufferable injustice, there was a time when it was unthinkable that Rome could fall or be sacked."),
  ("npc23_home_description_2", "I said that if Sparta had adopted our ways sooner it would have soared much higher and that I believe Spartans should be educated more. He answered 'If' and 'you believe' and walked away with a grin on his face. I swear if I had had my dagger I'd have used it. It was a humiliating situation, yet I still feel warmly about my home, the Acropolis is a magnificent place."),
  ("npc24_home_description_2", "After that, I have lost every single gamble I have ever taken and all games of luck are hazardous to my purse. I have been sick a lot more than I was when I still had that amulet, what I would give to be able to have it still."),
("npc25_home_description_2", "Despite its challenges, I love my homeland. The rivers, the plains, the herds of horses - it is in my blood. My father's hope, and mine, is that the Iazyges can rise again to reclaim their strength."),
  ("npc26_home_description_2", "{s21} has great walls but it's internal problems with traditional believers, Christians, Jews and more has lead it to be a hotbed of disputes. What is there to dispute? {s21} is rightful Christian clay."),
  ("npc27_home_description_2", "People are poor, we certainly do not feel great future in this forsaken land. And yet something keeps us there. I expect that if we ever move out, it would be some event of history note!"),
("npc28_home_description_2", "It was not the sword that gave us these lands, but the collapse of those who came before us. Let us hope we fare better when our time comes."),
("npc29_home_description_2", "That said... I would not return. I've chosen my own road, and this road - with you - gives me more freedom than a house ever did."),
("npc30_home_description_2", "One day, I hope to return, not as a wandering blade - but as a man with land, wife, and peace."),

  ("npc1_home_recap", "Cyrenaica is my dear home but It's been a long time since I have been there and I feel that I should visit it someday."),
  ("npc2_home_recap", "I was born over the mountains.  I'm a merchant, the son of a merchant, and the grandson of a merchant."),
  ("npc3_home_recap", "Ah, do you again want to hear that story? I though I was being annoying... Well, not much to be said. Italia is my land! Rome is my home. I am a roman woman and will always be."),
  ("npc4_home_recap", "My home is the desert of Africa, one day I will return there victorious with an army of Vandals skulls!"),
  ("npc5_home_recap", "Nothing much, Khagan! I was born North of the Pontos, which some may call Black Sea, in the neverending steppes. Grew up like warriors, served Attila, here I am now!"),
  ("npc6_home_recap", "Eh? What do you want to know? Pah, sorry Warlord I'm on duty. We'll talk later!"),
  ("npc7_home_recap", "My story? It's not an happy one, captain. I'd rather not talk about it."),
  ("npc8_home_recap", "Desert is my home, every dune is my home, every palm tree my roof and I wouldn't want it any other way."),
  ("npc9_home_recap", "I am from a noble family from Britannia and even though my family is ancient and respected I am a roman and proud to be one."),
  ("npc10_home_recap", "Proud Langobardi warrior, at your service."),
  ("npc11_home_recap", "I was born in the train of an army, and lived all my days in the train of an army. My folk are from Frankia, in northern Gaul, however, so I guess that's as much home to me as anywhere."),
  ("npc12_home_recap", "I am a medicus. I travel the world in search of medical knowledge."),
  #("npc13_home_recap", "I am from Roman Dardania."),
  ("npc13_home_recap", "I come from Nubia, a most ancient land south of Egypt."),
  ("npc14_home_recap", "I am a former Roman Officer."),
  ("npc15_home_recap", "I'm from the Eastern Roman Empire, specifically Greece."),
  ("npc16_home_recap", "There's not much to be said. I am a persian, born in the Empire... However, as you know, I am also a thief and an assassin! That's probably why you hired me."),
  ("npc17_home_recap", "I'm a Lombard, our ancient home was the nordic Scandza! But now we live in Anthaib."),
  ("npc18_home_recap", "What? Ah, well... Not sure exactly. My father was from the steppes, I was born somewhere in Dacia. We moved immediatly after."),
  ("npc19_home_recap", "I'm from the high steppes of Cimmeria, near {s21}."),
  ("npc20_home_recap", "I am a Gothic woman, and last wife of Attila."),
  ("npc21_home_recap", "I am from {s21}."),
  ("npc22_home_recap", "I am from {s21}."),
  ("npc23_home_recap", "I come from the bastion of learning and civilization, {s21}."),
  ("npc24_home_recap", "My home is far in the east, I could take you there one day."),
("npc25_home_recap", "The Danubian plains are calling to me, Captain. It is my home, and I hope to one day make it as strong as it was in the days of my ancestors."),
  ("npc26_home_recap", "God has made the earth my abode and I wish to bring light to all of it's corners."),
  ("npc27_home_recap", "I am from {s21}."),
("npc28_home_recap", "Volubilis? Ah, a ghost of stone and olive trees. We herd our flocks through its ruins and whisper stories of when Rome still ruled the sands."),
("npc29_home_recap", "Ctesiphon? Ah, a jewel once. Now... a cracked gem in a dusty crown. But its spirit lives in people like me."),
("npc30_home_recap", "Ah, Persis. Dry lands, proud people. My father's olive grove is probably still standing, unless the goats ate it."),

  ("npc1_honorific", "Captain"), #Borcha
  ("npc2_honorific", "{Sir/Madame}"), #marnid
  ("npc3_honorific", "{playername}"), #ymira
  ("npc4_honorific", "Comes"), #rolf
  ("npc5_honorific", "{playername} Khagan"), #beheshtur
  ("npc6_honorific", "warlord"), #firentis
  ("npc7_honorific", "Captain"), #deshavi
  ("npc8_honorific", "Captain"),
  ("npc9_honorific", "{My good sir/My good lady}"), #Alayen
  ("npc10_honorific", "{Brother/Sister}"), #Bunduk
  ("npc11_honorific", "{Laddie/Lassie} -- I mean Captain"), #katrin
  ("npc12_honorific", "Captain"),
  ("npc13_honorific", "Commander"), #nizar
  ("npc14_honorific", "Comes"), #lazalit
  ("npc15_honorific", "Captain"), #artimenner
  ("npc16_honorific", "Captain"), #klethi
  ("npc17_honorific", "Warlord"),
  ("npc18_honorific", "Chief"), #khaetag
  ("npc19_honorific", "Chief"),
  ("npc20_honorific", "Reiks"), #ildico
  ("npc21_honorific", "Lord"),
  ("npc22_honorific", "General"),
  ("npc23_honorific", "Captain"),
  ("npc24_honorific", "Captain"),
  ("npc25_honorific", "Rider"),
  ("npc26_honorific", "Valorous one"),
("npc27_honorific", "Warlord"),
("npc28_honorific", "Warlord"),
("npc29_honorific", "Warlord"),
("npc30_honorific", "General"),

  ("npc1_kingsupport_1", "I believe only a true follower of one true God can become a just king, but you are a just man enough, you have my support."), #Borcha
  ("npc2_kingsupport_1", "Well, captain -- I'd support you. I think you'd give the world the kind of enlightened rule which it has long needed."), #marnid
  ("npc3_kingsupport_1", "Are you being serious captain? How do you even think that... Well, wait. Nevermind. Forget about what I  said. I am your friend, Captain. I will always support you."), #ymira
  ("npc4_kingsupport_1", "If you promise to help my cause to banish the Vandals of course I'll support..."), #rolf
  ("npc5_kingsupport_1", "A fine idea, Khagan - you have shown that you know how to govern men. Mind that you govern them justly, though..."), #beheshtur
  ("npc6_kingsupport_1", "You are strong, Warlord. And I honor strenght! I will support you in this quest."), #firentis
  ("npc7_kingsupport_1", "Oh... I didn't expect this, to be honest, captain. But if you seek to take some land for you and your warriors why would I object? I myself am without a place to call home and, to be honest, I miss having a place to return at night."), #deshavi
  ("npc8_kingsupport_1", "I can indeed help you with that."),
  ("npc9_kingsupport_1", "Very good, my lord. I'm a roman by blood, but the Empire never stood for me when the Picts burned down my villa. So I don't owe Rome anything, and I say, 'Let Italia go to the most valiant!' Which would be you, Dux."), #Alayen
  ("npc10_kingsupport_1", "Well, {Brother/Sister}, I suppose there must be {kings/kings and queens}, and if there must be {kings/kings and queens}, then you would be as good a {king/queen} as any..."),#Bunduk
  ("npc11_kingsupport_1", "Why, that's a fine idea, Dux! I suppose I shall have to learn to call you 'Regulus', or 'Rex', then..."), #katrin
  ("npc12_kingsupport_1", "I am sure that you would make a fine king, captain. I flatter myself that I am a good judge of character, and you have demonstrated a capacity for compassion that far exceeds that of these others who call themselves monarchs."), #Artemios
  ("npc13_kingsupport_1", "I've been at your side long enough to get to know you, Commander. I am at your side, regardless of your future decisions. The men respect you, and that is enough for me to say that you would be an excellent leader of peoples."), #nizar
  ("npc14_kingsupport_1", "Well, sir, the heavens have instituted a hierarchy in this world, and normally I would have no truck with usurpation. But I also think that the kings of this land are a weak and sorry lot, not worthy of the name of king, and that leaves the crown free to be taken by a better {man/ruler}, such as yourself."), #lezalit
  ("npc15_kingsupport_1", "Well, you pay your men on time, when you can, generally speaking. That's the best qualification for kingship there is, in my book. You show some respect for the rights of others."), #artimenner
  ("npc16_kingsupport_1", "Why not, captain? I'm sure you'd make a fine {king/queen} -- and of course I'd hope you remember the little people like myself who did you a pretty turn on your scramble to the throne."), #klethi
  ("npc17_kingsupport_1", "Warlord... YES! That's what Godan wants for us. We will forge our imperium through fire and steel and conquer whoever will try to fight us. I'm with you, Warlord.... Warlord? No! Rex! You're my Rex now."),
  ("npc18_kingsupport_1", "You're ambitious, chief, I like this and I will help you. You will, however, need men, horses, arrows and spears... This land wont be conquered alone. But yes, for what matters I'm with you. Always and forever, you gave me a purpose, I owe you my life."),
  ("npc19_kingsupport_1", "Your own chiefdom? With a hall and loyal druzhyna, I suppose? Well, it will require finding of loyal men, ready to serve, and riches to provide to them, to stay loyal. People paying tribute to you and whole other things a chiefdom needs. With power comes both wealth and responsibility, but also a threat."),
  ("npc20_kingsupport_1", "You've got quite the guts, {playername}. Strong warriors tend to get a lot of fame, and loyal followers."),
  ("npc21_kingsupport_1", "A ruler such as you might save Rome, even if some might snicker at the idea. You are strong and capable, it is the only thing I can offer."),
  ("npc22_kingsupport_1", "You have shown to be a capable leader of men, maybe even worthy of Caesar of old, I'd be honored to support your cause."),
  ("npc23_kingsupport_1", "I'd rather nominate some Greek man to this but you are not the worst barbarian there is so I'l give you my support... for now."),
  ("npc24_kingsupport_1", "My trust in rulers is not exactly great but I think you could do fine."),
  ("npc25_kingsupport_1", "Captain, you have proven yourself to be a leader of strength and honor. The Iazyges respect such traits, and I will speak of your deeds to those who will listen."),
  ("npc26_kingsupport_1", "God's rule comes first but we need earthly support too."),
("npc27_kingsupport_1", "Aye, Warlord. You have the bearing of one born to lead. I will support your claim, with shield and steel."),
("npc28_kingsupport_1", "You are a bold leader, warlord. And boldness deserves loyalty. I will ride for your cause."),
("npc29_kingsupport_1", "You are kind, Warlord, and fair to those beneath you. I will support your claim."),
("npc30_kingsupport_1", "You have shown command, General. The kind that binds men to loyalty. I will support your claim."),

  ("npc1_kingsupport_2", "You can help us reclaim our homeland too, I think."), #Borcha
  ("npc2_kingsupport_2", "Most of the lords of this land -- well, let's just say that they never held a siliqua that they didn't collect as rent or take as pillage. You, on the other hand, have some experience of commerce and trade, of the effort and risk involved in making sure that men don't go hungry in Rome while there's a glut of grain in Alexandria, to give an example.... If you like, captain, I reckon I could find some support for you among the merchants and burghers of this realm."), #marnid
  ("npc3_kingsupport_2", "If you will ever manage to conquer your plot of land please, consider hiring some roman quartermasters, scribes, lawyers... whatever you will need to rule justly."), #ymira
  ("npc4_kingsupport_2", "Well, why not, you may give us assistance with our war against the Vandals"), #rolf
  ("npc5_kingsupport_2", "Ay, Khagan, I would. But there is something I should say, on behalf of the men of the steppes such as myself. It would bring great joy to us, to hear from the lips of one who would be khan, that you would restore an anicent right. From the days of the old emperors, the men of the steppes have enjoyed the right to bring their flocks to new pastures or to market, which necessarily involves the crossing of lands owned by the great lords of this realm."), #beheshtur
  ("npc6_kingsupport_2", "We need a tactic! And a strategy! I think we need allies first... We won't build our kingdom alone. My people, the Goths, are divided and many seek to serve a powerful lord. I think you can be that man!"), #firentis
  ("npc7_kingsupport_2", "Yes, I will support you. You're a good man, captain and I will help you in your quest with the hope you will treat everyone with the respect they deserve."), #deshavi
  ("npc8_kingsupport_2", "I believe the tribes of the desert will listen to me if I talk, I have some influence and I am not completely unknown!"), #matheld
  ("npc9_kingsupport_2", "I would, Dux, and others would too. But here's what I think -- you need to show the patricians and other influential people of this land that you're capable of defending their rights. They've been abandoned by the Empire long time ago, they mourn for someone who can defend them now."), #Alayen
  ("npc10_kingsupport_2", "Certainly, {Brother/Sister}. But I'd ask that you consider a thought of mine. If you became {king/queen}, then I'd ask you open your court to the common folks, and not just to the lords and blue-bloods. I'd ask you to let it be known that should any man be judged and sentenced, that he have the right to appeal to you directly. Right now, the lords have the right -- I say every man should have it, too."), #Bunduk
  ("npc11_kingsupport_2", "Of course, I would! Let me see your hand, there... Aha! You've got the 'Mark of Kings.' That's what we call it in Frankia, anyway. I hear in Rome it's the 'Emperor's Line,' but they call everything differently, over there. Anyway, yours is very long -- I'd say that it means that you're meant to rule! It's your destiny! In fact, I think I can even recall a prophecy to that effect. Hmm, how did it go..."), #katrin
  ("npc12_kingsupport_2", "Of course, captain.  But if I have learned anything in my travels in this land, it is that Romans are sticklers for precedent. Everything must be done as it was done in the Empire. Many, even the barbarians subject themselves and continue Roman Law. And of course, every king must be crowned according to 'Roman' law."), #Artemios
  ("npc13_kingsupport_2", "Although, we can't do much alone. You have to gather supporters, god more strength and be merciful with your enemies so they will be convinced to join our side. I can do my part, and tell of your strength to my fellow countrymen in Nubia, as well as Egypt, where many of my kinsmen live today and serve in the army."), #nizar
  ("npc14_kingsupport_2", "I would indeed, sir. I think you can unite this land, and then we'll be able to raise an army that has not seen for many generations, and conquer just as the great Emperors of the past had done."), #lazalit
  ("npc15_kingsupport_2", "I would. People might say that you don't have royal blood in your veins. But as far as I've seen, royal blood makes you a skinflint. Kings and nobles will take out loans or commission building projects without half a thought to how they're ever going to pay back all those commoners who expect to eat after an honest day's work. If you ask me, an honest tongue makes a {man/woman} a {king/queen}, not a fancy pedigree."), #artimenner
  ("npc16_kingsupport_2", "Of course, my {lord/lady}. And what's more, I figure a girl like me could do you a bit of a service raising support with the lords of this land. I may have only had a small part in their schemes and intrigues over the years, but I think I know what they want. And given what I know of their secrets, they'd not want to be denying me admission to their halls, now would they?"), #klethi
  ("npc17_kingsupport_2", "I told you I'm with you... Rex! But if you want more warriors to flock to your banner you will have to be ruthless... Merciless... A brave warrior! Friendships are not formed with us, as with you, over the wine-cups, nor are they determined by considerations of age or neighborhood. We wait till we see a brave man, capable of valiant deeds, and to him we all turn."),
  ("npc18_kingsupport_2", "If you want my advice, however, you will need friends. You cannot rule alone, you will need other chiefs to give you legitimacy and prestige. Otherwise, hungry wolves will storm your tent and steal all you have."), #Borcha
  ("npc19_kingsupport_2", "I certainly would, Chief. I will go back to lands of my forefathers, tell them that new witez' forms his warband and will bring honour and glory to those serving under him. That's certain that you are such witez' worth of note."),
  ("npc20_kingsupport_2", "If there is anything I've learned is that you must have loyal supporters if you're going to rule. Look at the Romans, always fighting civil wars due to a lack of loyalty for their emperor. Pathetic!"),
  ("npc21_kingsupport_2", "Sure would, best to have you as a ruler."),
  ("npc22_kingsupport_2", "I will follow you to the steps of underworld if need be."),
  ("npc23_kingsupport_2", "There are worse fates I guess..."),
  ("npc24_kingsupport_2", "I do know a few ways how we can enhance our support!"),
("npc25_kingsupport_2", "If you ever help my people reclaim our place in the Danubian plains, I will stand by your claim without question."),
  ("npc26_kingsupport_2", "We will gain support if I speak to the faithful, trust me!"),
("npc27_kingsupport_2", "But remember - one cannot carve a crown alone. You'll need loyal men and wise counsel. My people, the Phinnoi, respect courage above all. If you keep showing it, I'll make sure word spreads."),
("npc28_kingsupport_2", "But strength alone is not enough. We will need allies - clever ones, loyal ones. The desert teaches patience. Move with wisdom, and your kingdom shall rise."),
("npc29_kingsupport_2", "But promise me one thing - that in your court, there will be room for those of humble birth and silent strength. A just throne requires more than steel."),
("npc30_kingsupport_2", "But know this - a kingdom is not won by strength alone. You must be wise, and surround yourself with those who speak truth, even when it's hard to hear."),

  ("npc1_kingsupport_2a", "I will if I can..."), #Borcha
  ("npc2_kingsupport_2a", "Please continue..."), #marnid
  ("npc3_kingsupport_2a", "Please continue..."), #ymira
  ("npc4_kingsupport_2a", "I will if I can..."),
  ("npc5_kingsupport_2a", "Please go on..."), #beheshtur
  ("npc6_kingsupport_2a", "Splendid"), #firentis
  ("npc7_kingsupport_2a", "Well, yes, I will try to keep order..."), #deshavi
  ("npc8_kingsupport_2a", "Great."), #matheld
  ("npc9_kingsupport_2a", "That seems sensible enough..."), #Alayen
  ("npc10_kingsupport_2a", "Of course - I would give my subjects that right"), #Bunduk
  ("npc11_kingsupport_2a", "See if you can recall that prophesy."), #katrin
  ("npc12_kingsupport_2a", "Interesting. Please go on..."), #Artemios
  ("npc13_kingsupport_2a", "Please go on..."), #nizar
  ("npc14_kingsupport_2a", "Please go on..."), #lazalit
  ("npc15_kingsupport_2a", "Well-spoken, my good man"), #artimenner
  ("npc16_kingsupport_2a", "Interesting... Please continue"), #klethi
  ("npc17_kingsupport_2a", "Please go on..."),
  ("npc18_kingsupport_2a", "Not sure where this is leading but please, can you explain?"), #Borcha
  ("npc19_kingsupport_2a", "Please continue..."),
  ("npc20_kingsupport_2a", "Please continue..."),
  ("npc21_kingsupport_2a", "Please go on..."),
  ("npc22_kingsupport_2a", "Keep talking..."),
  ("npc23_kingsupport_2a", "Keep talking..."),
  ("npc24_kingsupport_2a", "Keep talking..."),
("npc25_kingsupport_2a", "I will do what I can to help. You have my loyalty."),
  ("npc26_kingsupport_2a", "I will do my best to help. You have my loyalty."),
("npc27_kingsupport_2a", "Then let it be so."),
("npc28_kingsupport_2a", "Then I am with you."),
("npc29_kingsupport_2a", "Then may the stars guide you."),
("npc30_kingsupport_2a", "You have my allegiance."),

  ("npc1_kingsupport_2b", "Well. We saw how that turned out..."), #Borcha
  ("npc2_kingsupport_2b", "I do not ask for their support, as they would no doubt wish to make a profit on the transaction."), #marnid
  ("npc3_kingsupport_2b", "I have no intention of hobbling myself in that way."), #ymira
  ("npc4_kingsupport_2b", "I will see what I can do..."), #rolf
  ("npc5_kingsupport_2b", "I said that I wished to be {king/queen}, not that I wished to involve myself in the minutiae of nomadism"), #beheshtur
  ("npc6_kingsupport_2b", "I'm not sure that I can quite deliver all that"), #firentis
  ("npc7_kingsupport_2b", "I think you're maybe taking the idea of the king's peace a bit too far, there"), #deshavi
  ("npc8_kingsupport_2b", "That's a pretty tall condition"), #matheld
  ("npc9_kingsupport_2b", "I'm not sure that implementing your idea would be as 'simple' as you think"), #Alayen
  ("npc10_kingsupport_2b", "Hmm. Let me think it over."), #Bunduk
  ("npc11_kingsupport_2b", "Ah... I'll have my hand back, please."), #katrin
  ("npc12_kingsupport_2b", "Enough, sir. I will not have you mock our traditions"), #Artemios
  ("npc13_kingsupport_2b", "Well. We saw how that turned out..."), #nizar
  ("npc14_kingsupport_2b", "Actually, I was looking forward to a bit of rest after becoming {king/queen}..."), #lazalit
  ("npc15_kingsupport_2b", "{King/Queen} of the Clerks, maybe, Enough of such talk"), #artimenner
  ("npc16_kingsupport_2b", "No offense, but I'm not sure that's the approach I'd take"), #klethi
  ("npc17_kingsupport_2b", "Well. We saw how that turned out..."),
  ("npc18_kingsupport_2b", "No offense, but are you really sure of this?"),
  ("npc19_kingsupport_2b", "On another, I don't think it's yet a time to do that."),
  ("npc20_kingsupport_2b", "No offense, but I'm not sure that's the approach I'd take"),
  ("npc21_kingsupport_2b", "Well. We saw how that turned out..."),
  ("npc22_kingsupport_2b", "Hmm. Let me think it over."),
  ("npc23_kingsupport_2b", "Hmm. Let me think it over."),
  ("npc24_kingsupport_2b", "Hmm. Let me think it over."),
("npc25_kingsupport_2b", "That depends on how well things go. Leadership is earned, not given."),
  ("npc26_kingsupport_2b", "That depends on how well things go. Leadership is earned, not given."),
("npc27_kingsupport_2b", "You seek to rule much, but your deeds must speak louder still."),
("npc28_kingsupport_2b", "I do not yet see the fire of kingship in you... not fully."),
("npc29_kingsupport_2b", "Forgive me... but I am not ready to believe in such lofty dreams."),
("npc30_kingsupport_2b", "Forgive me, General, but I do not believe the stars favor such an ambition - yet."),

  ("npc1_kingsupport_3", "I can talk to the sailors and my people about your claim, I am sure they will support me if I give them enough reason to do so."), #Borcha
  ("npc2_kingsupport_3", "If you like, captain, I can take a few weeks to visit the guildhalls and caravanseries where I have contacts, and explain to them that, in you, they will have a {king/ruler} who will check the rapacious nobles, who, with their tariffs and taxes, would strangle commerce for the sake of a few extra siliquae to spend on their wars and their feasts. What do you say to that, captain?"), #marnid
  ("npc3_kingsupport_3", "If you were to make such a pledge, Captain, I think that it would help many of the lords of this land overcome any reluctance that they might have. If your aim is to restore the old Roman system, then arguably you are a more legitimate {king/ruler} then any of these come-lately usurpers. Give me leave for several weeks, {sir/madame}, and I will let it be known in the noble courts and merchant houses of this land that you intend to restore their ancient rights."), #ymira
  ("npc4_kingsupport_3", "The Berbers and desert tribes will listen when I talk, you want me to gain more support for your claim? I can do that easily!"),
  ("npc5_kingsupport_3", "Anyway, Khagan, in these sorry times the men of the great estates have taken to blocking our passage, charging us huge fees to cross. It is a great burden on my people, Khagan. If I could take a few weeks to let the men of the steppes know that you would support the restoration of our ancient rights, well, then, I think you would find many who would support you as khan, And when men speak of you as khan, that's the first step to becoming one."), #beheshtur
  ("npc6_kingsupport_3", "Very well. Although I am now a stranger to my family, I have entered many a noble's hall in your train, and I reckon I would be welcome again. I shall go about this land and tell the nobles that when you are {king/queen}, you will strive your hardest to inspire strenght and show wisdom."), #firentis
  ("npc7_kingsupport_3", "I'll tell you what, captain. Give me a few weeks and I'll go to some of these villages -- stinking hovels that they are, but I reckon I can take care of myself these days. I'll tell the people there that once you unify this land, you'll wipe it clean of banditry. You'll erect gallows along the roads and keep them well-stocked with broken-necked thieves, so that every passerby knows that the wages of indecency is death."), #deshavi
  ("npc8_kingsupport_3", "I can go ask a couple of friendly tribes for their support, I will report how it goes."), #matheld
  ("npc9_kingsupport_3", "Absolutely Dux. Give me a group of men and I'll do anything in my power to help you in this quest. We will ride vilage after vilage holding meetings with the locals in order to talk with them and bring them on our side. This will be very useful."), #Alayen
  ("npc10_kingsupport_3", "Well then, {Brother/Sister}, give me leave for a few weeks and I can go about this land, letting the common folk know that you will rule justly and equitably, and that lord and common alike should be one before your law. Men will speak of you as {king/queen}, and that's a good start to becoming one..."), #Bunduk
  ("npc11_kingsupport_3", "I can't recall now, but if you let me go back to my home, I could find an old greybeard who remembers it in full. And, I could put it around that you've got the mark of kings on your hand! There's many where I come from who are waiting for a just ruler, and a man's hands tell all that's worth knowing about him. Give me a few weeks, and I'll reckon I can have quite a few expecting you to be their next {king/queen}."), #katrin
  ("npc12_kingsupport_3", "But you know what? There was no 'imperial' law when it came to the crown. Sometimes one emperor handed the empire to his son. Sometimes he split it between his generals. Sometimes one emperor murdered the last. There's no right 'Roman' way to crown a {king/king or queen}, and thus it makes sense that the crown should go to the one most fit to govern -- which would be you, naturally. Give me a couple of weeks, and I'll write a tract which proves it and find a copyist to post a version in every town tavern in the land. What do you say to that idea, captain?"),
  ("npc13_kingsupport_3", "If you let me, I'll ride there, to my homeland and see what I can do to gather more support from my kinsmen. It won't do no harm, commander. You can only benefit from this."), #nizar
  ("npc14_kingsupport_3", "Give me leave for a few weeks, {sir/madame}, and I will let all the worthy men of this land know that you are the one to unite not just the Empire, but all the other dominions. For according to my thinking, no one should be {king/king or queen} here unless they have the capacity to rule the entirety of the realm -- and you alone have demonstrated such a capacity, {sir/madame}."), #lazalit
  ("npc15_kingsupport_3", "I'm glad you think so. Here's what I suggest. I know men in the guilds here, men like me, who've been shafted and shaken down until they can take no more. Here's what I'll tell them -- you're honest. You respect the burghers. You'll pay your debts. You won't beggar your subjects."), #artimenner
  ("npc16_kingsupport_3", "Give me leave for a few weeks, and I'll do a little tour of my former employers' castles. I'll sing them a pretty song about what you'll do as {king/queen}, about all the ancient freedoms you'll restore -- let them rob their tenants and tax the merchants and fight their wars and spend themselves silly without a thought to tomorrow, as a noble ought! What do you say to that, captain?"), #klethi
  ("npc17_kingsupport_3", "Listen, Rex... What I can do for you is this: let me go to my kinsmen, the Lombards. A weak, old man rules them now. Let me do my part and they will hear stories of your deeds and glory. Many will join you and leave the old king because you're strong... And he is not."),
  ("npc18_kingsupport_3", "To rule you will need warriors, and I'm gonna give you warriors... The best of them! Let me leave to speak with what's left of my tribe. I'm sure that if I speak with them, they will spread the word and you will become even more popular and prestigious."), #khaetag
  ("npc19_kingsupport_3", "A proper witez' needs his druzhyna. Not just a small warband, but a unit of note, even in hundreds of wariors. And you need faithful officers ready to serve you. That's where I come, hehe. I will thus come along and tell that such druzhyna is in creation and that many riches will come to those serving in them. This will help you in forging your own chiefdom, that's for certain."),
  ("npc20_kingsupport_3", "If you give me a few weeks I can travel the lands, speaking highly of you to both rich and poor. People love a good story, and a good leader."),
  ("npc21_kingsupport_3", "If I could go about this land for a few weeks, telling the common folk that you were going to amnesty their kinfolk -- well, they would start talking of you as the Emperor, and that would pave your way to the throne. Shall I do that, {Sir/Madame}."),
  ("npc22_kingsupport_3", "I could contact my old comrades and ask them to spread the word that you are seeking to become an Emperor, I'm sure some of them would be interested, though I know many support Majorian, shall I contact them, General?"),
  ("npc23_kingsupport_3", "I have connections to my old classmates, should I ask them to support you, I can be persuasive you know?"),
  ("npc24_kingsupport_3", "I know some people from the tundras and they will listen if I speak."),
("npc25_kingsupport_3", "I will ride to our allies and speak of your strength. The Iazyges value loyalty, and I will make sure they know you are a leader to trust."),
  ("npc26_kingsupport_3", "I have contacts in Judea and now's the time to use them. I will return victorious!"),
("npc27_kingsupport_3", "Very well. Among the northern tribes, my name is known. I'll carry your word from hearth to hearth, that you are a warlord worth following - bold, just, and strong."),
("npc28_kingsupport_3", "Very well. I know many who still respect the name of my people. I shall ride to them and speak of your strength, your justice. They will listen - some will follow."),
("npc29_kingsupport_3", "I know little of thrones, but I've served many lords. If you ask me, I'll travel to the courts and camps, and whisper your name where it matters most."),
("npc30_kingsupport_3", "Very well. I once served nobles and officers in distant provinces. Let me ride once more through those halls and whisper your name to those with ears to listen. I will return with news and pledges."),

  ("npc1_kingsupport_objection", "Artemios is not the kind of man you should place your trust on, he is a know-it-all Roman noble who thinks he is so much better than others. Why would a Roman want someone like you to rule? In the worst case he will go to gather support for himself and I would not be surprised at all. You have made a mistake here."), #Borcha
  ("npc2_kingsupport_objection", "Um, captain. Beorhtric has ridden off to tell the lords of this land that you'll let them settle their quarrels by force and violence. You know they rarely actually fight each other, right? Most of the time, it's the traders and travellers on the roads between their castles that get clobbered in their petty disputes. Any excuse to shake down a caravan, they'll take. I really hope that he misunderstood you, sir."), #marnid
  ("npc3_kingsupport_objection", "Captain! Are you really relying on Beorhtric and Rufinius for this task? They will not ensure you a new flow of good warriors... But rather cutthroats and criminals alike! Stop them! There must be another way."),
  ("npc4_kingsupport_objection", "Sending Khaetag to gather for support is your most foolish decision bar none. I am ashamed and angry to call you a 'Captain' when he is the one who sends a fucking strawhead to gather support from all manner of Germanics no doubt. I should go after him and leave his body in a ditch."),
  ("npc5_kingsupport_objection", "{playername} , my Khagan -- I overhead what you told the other warrior. But I wonder -- if the lords who live from farming, and the merchants who earn from trade, are allowed to determine what taxes will be leveed, then who will be taxed? Those who live from flocks, of course -- my people, the people of the steppes. I would have nothing to do with these councils, Khagan -- all free men should be one, under the khan, and that is the end of it."), #beheshtur
  ("npc6_kingsupport_objection", "I understand that you have dispatched Mastigas to fabricate a claim of royal descent. I have to tell you, {sir/madame} -- I do not think that the heavens will smile on such an attempt to take the throne by fraud."), #firentis
  ("npc7_kingsupport_objection", "I have heard what you told Aistulf, about giving every common criminal the right of appeal to the {king/ruler}. I do not approve. Bandits should be hanged when caught. Give them a trial or an appeal, and they will talk their way out of the noose. Aistulf is a good man, but no man can fully understand what these wolves in human form do to women"), #deshavi
  ("npc8_kingsupport_objection", "Coward will bring cowardly company. Narseh has the wits of a blind half-insane donkey. What do you think he can achieve that I can't, anything he can do, I can do better. Send me next time and leave Narseh to trim the horses even though that is too good of a job for a bastard like him."), #matheld
  ("npc9_kingsupport_objection", "Dux -- it is with great regret that I have learned that you have told Sunicas to let his people know that you will allow them to lead their flocks over the lands of their betters. I hope that I am mistaken about this, sir. The money we demand is but small compensation for the damage they cause to our flocks and the pollution of our water sources. Dux, if your future kingdom is to be some nomads' paradise, then I for one do not look forward to it."), #alayen
  ("npc10_kingsupport_objection", "I hear that you've got Nizar spinning poems to justify your ascent to the throne. I can't say I approve, {Brother/Sister}. If men fight for a {king/sovereign}, it should be because they know they're going to get something good out of it, not because they've taken a liking to a silly song."), #Bunduk
  ("npc11_kingsupport_objection", "I hear that Rufinius is off and about telling folks that you're going to make yourself {king/queen} and then lead an army over the mountains. Shall there be no end to these wars, Dux? I was thinking that if you made yourself {king/queen}, then maybe you'd give us a bit of peace. But I guess the heavens have made blood to be spilt, and bones to be broken, and there's no getting round their decree."), #katrin
  ("npc12_kingsupport_objection", "Captain. I hear that you've gone and made Klethi, of all people, some sort of ambassador to the aristocracy. I shudder to think of what that amoral girl might be promising them on your behalf -- and dignifying all these gross indulgences by calling them 'ancient freedoms.' By doing this, you mock those of us who who had hoped that you would have helped the world escape its bloody past, and move towards a new age of peace and learning. Enough, I have said my peace."), #Artemios
  ("npc13_kingsupport_objection", "Commander, you know I don't like Sunicas. He's a treacherous man from a treacherous folk. You don't want the Huns to support you, you can't trust them. Not even a decade ago, that folk were ravaging these lands killing, destroying everything on their path. Think wisely, commander, think wisely."), #nizar
  ("npc14_kingsupport_objection", "I understand that you've sent your man, {s14}, to proclaim to all the entire world that you intend to free all the miscreants of this land upon your accession to the throne. What a foul idea... Men must be governed, {sir/madame} -- with whips and chains and the noose, if necessary. You'll find that out the hard way if you become {king/queen}, I'll warrant."), #lezalit
  ("npc15_kingsupport_objection", "I understand that you've given leave to that lass to spread some nonsense about marks on your hands. I just want to say that, as an educated man, I find it disturbing that you would resort to old women's superstitions to back your claim. Village women will believe one thing one day, another thing the next. Now a horoscope, properly cast by an astrologer at a royal university with a reputation to uphold, might tell you something worth knowing, but those have not been performed in the Empire for some time."), #artimenner
  ("npc16_kingsupport_objection", "Oy -- Captain! I hear that Narseh's gone off to sing a pretty song to the merchants, on how you'll hand them the kingdom on a silver platter for them to feast upon, smack their lips, and suck the marrow from the bones. I hope that's just a tale you're telling. A noble lord will at least toss a few coppers to the poor when he holds his feasts, and will make sure that the servants go home with full bellies. A merchant marries his daughter, and you'd be lucky to get a few crusts and scraps of gristle from the table. That's my experience, anyway."), #klethi
  ("npc17_kingsupport_objection", "Rex! I heard you sent one of your eunuchs to spread word about the arrival of a new, just king that will uphold the rights of the common and blablabla... What the hell is this? You seem to me like one of those silly Franks pretending to be romans! Pah! Men will follow you if you're strong! No one cares about the rights of the commoners."), #Alachis
  ("npc18_kingsupport_objection", "Boss -- you've given leave to Shimon to tell the nobles that they will have rights over pasture, market, and forest? I can't say I like that. Give him his way, and he'll set up gibbets in every village in the land, where there will dangle some poor sod who has a distaste for him... You've seen how he talks about the Christians in our company."), #khaetag
  ("npc19_kingsupport_objection", "Sending Sunicas to gather support for you? I do not admire this choice. He is greedy, ruthless, brutal and simpleton in nature. I do not think if sending someone like him will say anything good about you, Chief."),
  ("npc20_kingsupport_objection", "Unfished - you shouldn't see this."),
  ("npc21_kingsupport_objection", "{Sir/Madame} you've given leave to the berber to go tell the nobles that they will have rights over pasture, market, and forest? I can't say I like that. You will only have more enemies than friends if you continue enlisting him as your emissary."),
  ("npc22_kingsupport_objection", "General have you lost your mind? You asked Ingrid to help you gather support? What do you think that whore can do? Ask the rabbits or maybe the little birds to aid you in your fight for legitimacy? How do you think a young girl like that can convince anyone: if she says your name, you will be the laughingstock of the whole land and my honor will be stained too."),
  ("npc23_kingsupport_objection", "Captain! You asked that Siestrewiz to help you gather support for the claim? Why? What do you think he can do? He is a barbarian and of so low intellect that if a rat and he would compete he would lose, hard. Not to mention that he's not even loyal to you, truly, I've seen men lusting over coin like he is, the second you cannot pay him he will show you his true colors."),
  ("npc24_kingsupport_objection", "I don't see a point in sending Decimus to gather support, he's a broken man who will bring us only as broken support as he is. This is meaningless."),
("npc25_kingsupport_objection", "Sending Wadomar to represent you? A Goth speaking on your behalf? That will only sow distrust among the Iazyges. I urge you to choose someone else."),
  ("npc26_kingsupport_objection", "Why send Decimus to gather support, he may gather support, for a Pagan rebellion and revival, that's what he would do. You may have just done a great disservice for the cross... I do not like it at all."),
("npc27_kingsupport_objection", "You sent {s14}? That one is like spring ice - thin and full of cracks. A poor choice if you're building trust among warriors."),
("npc28_kingsupport_objection", "You sent {s14} to plead your right? That one? I cannot stand behind this. It reeks of desperation, not destiny."),
("npc29_kingsupport_objection", "Warlord - I heard you sent {s14} to spin a tale of false ancestry. That path is crooked and clouds your cause with shadows. Please reconsider."),
("npc30_kingsupport_objection", "General, I must object. Sending {s14} to forge claims dishonors all you have built. Ambition is no excuse for deceit."),


  ("npc1_intel_mission", "Information gathering is something I can do, we Jews are encouraged to be knowledgeable so you have chosen the right man, sailors will open their mouth after some beer."), #Borcha
  ("npc2_intel_mission", "{Sir/My lady}, if you're interested in events in {s18}, I can still make contact with my old trading partners in {s17}. They're usually well-informed about political events."), #marnid
  ("npc3_intel_mission", "Captain, although I cannot return to my father's house in {s17}, I still may make contact with my sister. She will be privy to the councils of the great merchant houses, and may tell us much about the state of the {s18}."), #ymira
  ("npc4_intel_mission", "Good Berber can easily find out any information he wants, we are talented in espionage too, so just point and I'll star gathering."),
  ("npc5_intel_mission", "If you like, Khagan {playername} , I can take a few days to visit my mother's sister's people. They work in a caravanserie in {s17}, and hear the news from all across the {s18}. They may have some gossip about the feuds and rivaries of the great lords, if that is of interest to you."), #beheshtur
  ("npc6_intel_mission", "Warlord -- while I am not strictly welcome in {s17}, I would be able to make contact with some former tenants of an estate of mine nearby. I granted them ownership after my abrupt departure, and they are now well-placed in society, and also less inclined than most to hold my crime against me. If you give me a few days, I may be able to collect some interesting information about the {s18}."), #firentis
  ("npc7_intel_mission", "Captain. When I left my former home in Alemannia, I had promised myself that I would never return, except for the purposes of taking out vengeance on those who wronged me. Perhaps I was rash. I am occasionally curious as to how my relatives are going there, those that are still alive, at least. Perhaps I can bring them some gifts, to let them know what I have made of myself! Any rate, they are wretched people, but just as a cringing dog keeps its ear to the wind, so do they. They may have useful information about the {s18}, if you would give me a few days to pay them a visit."), #deshavi
  ("npc8_intel_mission", "I will ask the bazaars and the desert dwellings of the latest news, I'm sure you will find something that will interest you."), #matheld
  ("npc9_intel_mission", "Dux -- it has been some time since I sampled the delights of {s17}, where gentlefolk such as myself are wont to partake of the hospitality of the most puissant and generous lord. If you wish, I could perhaps go there, and let you know something about the concerns that weigh on the minds of the great peers of the {s18}."), #Alayen
  ("npc10_intel_mission", "Captain -- I was thinking that some of my old mates in the garrison at {s17} would be glad to see me. They are good lads, and would never betray the city, but like me they have no particular affection for the bluebloods that command them, and may be willing to slip a little political gossip our way. The gentry are always falling out over one little thing or the other, but the lads might be able to know if there's real dissent brewing."), #Bunduk
  ("npc11_intel_mission", "Dux -- I was thinking that it's been a while since I visited my kinfolk in {s17}. They've been kind enough to me over the years, helping me out during the lean times, so I feel I'd like to share some of my newfound fortune with them. I've also bought wholesale enough times from the {s17} grain merchants for them to trust me. I'd reckon they might be persuaded to spill a few tidbits about events in the {s18}, if that would interest you."), #katrin
  ("npc12_intel_mission", "If you wish, Captain, I would not mind taking the time to pay a visit to a pupil of mine, now employed by the lord of {s17}. I had great hopes for him, but I have heard that he has lately endorsed the use of muskmelon for the treatment of palsy, on the grounds that its cold essence offsets an abundance of yellow bile. This is a travesty of medicine, and I must journey there swiftly to correct him. While I am there, if you wish, I could question him on the latest trends within the {s18}, a matter which may interest you."), #Artemios
#  ("npc13_intel_mission", "Oh valiant one! With your permission, I was thinking that I might pay a visit to the dales near {s17}. I try not to revisit old pastures, but I must confess a certain curiosity as to how a comely shepherdess of my former acquaintance is getting along. On the way, I may attempt to stop in at the castle. I suspect that it would not be terribly difficult for me to charm my way into the lord's hall, and I may be able to provide you with the latest news from the {s18}."), #nizar
  ("npc13_intel_mission", "As I told you, commander. I would be more than willing to help you. I'll leave tomorrow morning for my homeland, Nubia, and I'll spread the word of your noble name."), #nizar
  ("npc14_intel_mission", "Captain... As you may know, I helped train the garrison of {s17}. One of their number has lately been in touch with me, and suggests that if I were to visit him, he could pass me information on events within the {s18}. I am willing to do this, if you can spare me. While it is a great disgrace to be a traitor, there is no dishonor in making use of one."), #lazalit
  ("npc15_intel_mission", "Captain. As you may know, I have for some time harbored a wish to go to {s17}, and study the masonry -- one of the finest examples of the old Imperial style. As it happens, one of my colleagues is currently engaged there doing repair work on the curtain wall. While his sense of professional obligation I think would prevent him, rightfully, from disclosing to me any weaknesses in its defenses, I suspect that he would not be averse to offering up his opinion on the general state of the {s18}, if that is of interest to you."), #artimenner
  ("npc16_intel_mission", "Oy, Captain! I had a mind to pay a visit to my old haunts at {s17}. Let's just say that the lord and lady of the place had commissioned a certain service from me, and had been a bit lax about payment. However, a certain sparkly bauble in the lady's possession will fit the bill nicely. I see no need to trouble them by letting them know about my visit, but I could have a wee chat with my old friend the castle steward, who'll be letting me into the place, about goings-on in the {s18}."), #klethi
  ("npc17_intel_mission", "Warlord, you're strong and wise and I wish to help you in your struggle. I have still many friends in {s17}, the land of the Lombards, if you let me I will visit {s18} and make sure to know what they think of you and what they plan to do. They will never recognise me, you can trust Alachis!"), #Alachis
  ("npc18_intel_mission", "I have an idea, let me go to {s17} in disguise, they wont recognise me. In the tavern or in the streets I may find valuable information about {s18}, does it seem to you like a good deal? If they capture me I will die there without giving them a single information, mark my words."), #khaetag
  ("npc19_intel_mission", "Hm, I recall that under Hunnic service, we did a tour or two in lands of Eastern Germania, along where Eburodunum is. I think I could pay locals a visit to ask how they are going and how is their tribe doing. Something worth of note if you ever wanted to pay a visit to that area."),
  ("npc20_intel_mission", "Well, I will go to {s17}, land occupied by my kin. They will hear your stories and flock to you, Reiks."),
  ("npc21_intel_mission", "I'm afraid I cannot help you there. I am simply a young barbarian, as the Romans would say, I lack any big contact to help you cement your claim. I am terribly sorry."),
  ("npc22_intel_mission", "I've yet to manage to contact my old brothers and others who might help you, I need more time and a strategy to better help you, I will when the time is right!"),
  ("npc23_intel_mission", "I am talented in gathering any information, mathematical or otherwise, since I am a trader I know all the latest words and rumors that go around. Wish to send me find out how our situation could be improved?"),
  ("npc24_intel_mission", "I learned how to listen when I hunted game, I'm sure I can do the same with people."),
("npc25_intel_mission", "Scouting is a skill we riders of the plains know well. I will find the information you need and return swiftly."),
  ("npc26_intel_mission", "A good priest always finds gossip and can find out what's the latest word."),
("npc27_intel_mission", "I can travel north, along the lakes and rivers, and speak to the old chiefs and warriors. They'll not turn away a man of the Phinnoi. I'll bring back news - if any stirs."),
("npc28_intel_mission", "Warlord - I know the markets and caravan routes around {s17}. Some of the traders still remember me from Volubilis. I can slip in, ask the right questions, and return with something useful on the {s18}."),
("npc29_intel_mission", "If you wish it, I can head to {s17}. A woman like me is easily overlooked, and I may learn much in kitchens and courtyards that others would miss."),
("npc30_intel_mission", "General - I still know a few men from my old company near {s17}. They're retired now, settled down, but they owe me a favor or two. I believe I can draw some valuable information about the {s18}."),

  ("npc1_fief_acceptance", "The people of Israel have now a home, a TRUE home to live in, soon we can gather an army to drive out those who stain the land of David with their unclean foots, I give you my warmest thanks, I won't let you down now, you will soon have an army that even the Romans will fear!"), #Borcha
  ("npc2_fief_acceptance", "{s17} as a fief? Well, I've always thought in terms of buying and selling goods, not in terms of governing anything. But now that you mention it, I bet I could make that place turn a fair bit of revenue. I thank you, {my Lord/my lady} -- this is a very kind turn that you have done me."), #marnid
  ("npc3_fief_acceptance", "Why? Really? Oh... Valentina the governor of a settlement! Who whould have taught? Father... I am speaking of you now! Captain, it is a great honour. I am a mere merchant's daughter but I will do my best."), #ymira
  ("npc4_fief_acceptance", "This is it! the beginning of a more organized resistance against the Vandals it does not matter where my fief is, I will use it to launch campaigns against my people's oppressors, I thank you immensely, you are a good friend and I promise that I won't let you down."), #rolf
  ("npc5_fief_acceptance", "Khagan -- I would be most pleased to hold {s17}. I will send word to the hills, to my kinsmen, and let them know that there is honorable gold to be earned serving under me in your armies -- and they will come flocking to fight for you!"), #beheshtur
  ("npc6_fief_acceptance", "Warlord -- I am surprised that you find me worthy to govern men, as I am just beginning to learn to govern myself. But if you indeed wish it, I would be most honored to hold {s17} in your name, and dedicate myself to the protection of those who live there."), #firentis
  ("npc7_fief_acceptance", "Aye, I'll hold {s17} -- and give it a reputation that strikes fear in the hearts of thieves and brigands across Germania. Thank you, Rex, for this opportunity."), #deshavi
  ("npc8_fief_acceptance", "I am happy when I am travelling I do not require a house or a farm but I thank you for this show of generosity, I am no longer a homeless wanderer, but know that I will not settle down, my quest is yet to be finished."), #matheld
  ("npc9_fief_acceptance", "Dux, I was cheated of my inheritance -- but now, with this offer of this estate, you make right what was wrong. It would give me the greatest honor to serve you, to fight for you, and to hold this land in fief to you."), #alayen
  ("npc10_fief_acceptance", "You'd make me a lord? Well, no thank you -- but if you would call me 'tribune' -- the tribunes being the people's servants in the old times -- then I suppose I could bring myself to run {s17} for you. I'd put food in the bellies of the hungry, and raise a fine force of Romans foot to fight on your behalf, {Brother/Sister}. But I can't promise that the real blue-bloods will enjoy rubbing shoulders with me in your councils."), #bunduk
  ("npc11_fief_acceptance", "Ay! You'd grant old Alodia a title of nobility? Well, I'd be daft to turn you down, now wouldn't I? My, the strange turns that life takes... Fancy this old bag of bones becoming a great peer of the realm of these lands."), #katrin
  ("npc12_fief_acceptance", "Well, {sire/my lady}, I'd have you know that don't believe in the holding of land in fief to the king. Farmers and landholders should govern their own affairs, under the distant watch of the sovereign. That being said, the Empire has seen far too much bloodshed for us to turn the social order on its head right now. Give me that land, and I'll endeavor to prepare it for a brighter future -- if not in this generation, than perhaps in the next."), #Artemios
  ("npc13_fief_acceptance", "I am grateful you acknowledged my importance in your party and gifted me with land. I shall not forget this, commander. The first thing I will do, will be to build a temple for Isis, our supreme goddess and will hold a feast in your name."), #nizar
  ("npc14_fief_acceptance", "You do me a great honor, captain. Where I'm from, a youngest son such as myself has few opportunities to earn a fief of his own. But here, in the Empire, there is still the chance for a man to win with his sword what was denied him by his birth! I shall hold {s17} as your vassal, and raise an army to fight for your glory and for mine."), #lazalit
  ("npc15_fief_acceptance", "Well, {sir/my lady}, that's a gracious act, and marks you as the kind of monarch who can save this sorry land from the incompetence of the current batch. I suspect a lot of the noble lords around here will think that a commoner like me isn't fit to hold a fief. Well, when they see what I do with it, and what revenues I can bring in, they'll change their tune!"), #artimenner
  ("npc16_fief_acceptance", "Oh, that's most generous of you, my king. I've been in and out of many a great hall or manor -- not always with the master's permission, I should add -- but I never thought I'd own one myself. Let me think... When I collect my first year's rents, what baubles shall I buy myself?"), #klethi
  ("npc17_fief_acceptance", "I was raised to fight and that's what I did my entire life... I cannot believe you're now giving me land, Rex! You're doing me great honor and I swear, I will never, never betray your trust. Maybe it is time for a man of war like me to find some peace and settle down."), #Alachis
  ("npc18_fief_acceptance", "What? Really?! Chief, you are fulfilling my wish and quench the thirst for revenge I always had. Finally, being the owner of a land and of a proper host I will finally be able to clean my family name entirely. Thank you chief, I bow to your magnanimity."), #khaetag
  ("npc19_fief_acceptance", "A fief? For myself? I am thankful, Chief, very much. Never expected to inherit my own after my father and here I get one. I will try to keep things in order so that the people are happy and peace in land settled."),
  ("npc20_fief_acceptance", "You're giving me {s17} to rule over, Reiks? I never thought I'd ever have my own land. Thank you my Reiks!"),
  ("npc21_fief_acceptance", "You'd make me lord of {s17}, {Sir/Madame}? I never expected to receive a lordship, I am the son of a huntsman after all and I know very little of stewardship. I accept this honor however; my family could move to this new land and our lives would be better. I will govern them to the best of my capabilities, and I swear I will not disappoint you!"),
  ("npc22_fief_acceptance", "I will be a lord? a lord of {s17}, General? If only my father was here to see this and my dear mother, too. Look! Gaze upon me! I am now a landowner. I will do everything in my power to raise you Roman legionaries worthy of being called just that. {s18} will be a center of Roman power from where we will take back what belongs to us!"),
  ("npc23_fief_acceptance", "Finally! I can start my own philosophical school, one that is dedicated to turning young boys into erudite speakers and thinkers who can move the minds and hearts of thousands, of course I will raise troops to protect us and to civilize the marauding hordes by force, if necessary, I thank you, I might even consider you my friend and that is a lot coming from me."),
  ("npc24_fief_acceptance", "I like to be on the move so a permanent fief is maybe not what I require but I thank you for the gesture."),
("npc25_fief_acceptance", "You honor me with this land, Captain. The Iazyges will see it as a sign of trust, and I will work tirelessly to ensure it prospers under your name."),
  ("npc26_fief_acceptance", "This will be a new house of God, one where I train the future generation of faithful novices, I thank you for this trust, soon you will see God's might in action."),
("npc27_fief_acceptance", "A hall of my own? I never dreamed it. But if it pleases you, Warlord, I'll hold {s17} in your name and protect it as I would my own kin."),
("npc28_fief_acceptance", "Warlord - to govern land is no small thing. But I've seen leaders rise from nothing among my people, and I will not shrink from the task. I will rule {s17} wisely in your name."),
("npc29_fief_acceptance", "Warlord - I never thought I'd be asked to govern, but I accept your trust. I'll bring order, warmth, and care to {s17}, as any good steward should."),
("npc30_fief_acceptance", "General - I did not expect such an honor. But I swear this: I will keep {s17} safe and just, as a man who served many lords and finally found one worth serving."),

  ("npc1_woman_to_woman", "{!}."), #Borcha
  ("npc2_woman_to_woman", "{!}."), #marnid
  ("npc3_woman_to_woman", "My lady, if you don't mind me saying -- I think by now you have proven yourself to be one of the great warriors of this realm. Yet strangely, no king has come forward to offer you a fief. Perhaps it is because you are a woman. No matter -- I personally believe that you will take your place among the great lords of this realm, even if you have to fight twice as long and twice as hard to receive your due!"), #ymira
  ("npc4_woman_to_woman", "{!}."), #rolf
  ("npc5_woman_to_woman", "{!}."), #beheshtur
  ("npc6_woman_to_woman", "{!}."), #firentis
  ("npc7_woman_to_woman", "Captain. If you don't mind me saying, you have fought long and hard against the scum of the world, and with their defeat, you make this land a better place. You are well deserving of a fief of your own -- and I suspect that if you were not a woman, a king would have offered you one by now. That is the way of the men in this sorry land: they let us stand in the front of the battleline to take the enemy's blows, but when it comes to a division of the spoils, they expect us to head to the rear."), #deshavi
  ("npc8_woman_to_woman", "{!}"), #matheld
  ("npc9_woman_to_woman", "{!}."), #alayen
  ("npc10_woman_to_woman", "{!}."), #bunduk
  ("npc11_woman_to_woman", "Aye, Dux, I just can't help thinking to myself -- you've made quite a name for yourself, haven't you? Fighting and marching up and down the length of the land. Why, I suspect if you were a man, some king would have offered you a fief by now. Well, you may still get what you deserve -- you'll just have to prove yourself a bit more."), #katrin
  ("npc12_woman_to_woman", "{!}."), #Artemios
  ("npc13_woman_to_woman", "{!}."), #nizar
  ("npc14_woman_to_woman", "{!}."), #lazalit
  ("npc15_woman_to_woman", "{!}."), #artimenner
  ("npc16_woman_to_woman", "Oy, Captain -- if you don't mind me saying, you've made quite a name for yourself in these parts. I suspect that if you were a man, a king would have offered you a fief by now. But we ladies should come to expect things like that. Men will find any excuse not to reward us for our work, so if we take a fancy to a bit of land somewhere, maybe we should just reach out and take it. That's the way I look at the world, anyway."), #klethi
  ("npc17_woman_to_woman", "{!}."), #Alachis
  ("npc18_woman_to_woman", "{!}."),
  ("npc19_woman_to_woman", "{!}."),
  ("npc20_woman_to_woman", "{!}."),
  ("npc21_woman_to_woman", "{!}."),
  ("npc22_woman_to_woman", "{!}."),
  ("npc23_woman_to_woman", "{!}."),
  ("npc24_woman_to_woman", "{!}."),
("npc25_woman_to_woman",
 "My lady, you lead with the strength and wisdom of the greatest Iazyg chieftains. Even in a world where women are underestimated, you have earned the respect of warriors like me."),
  ("npc26_woman_to_woman", "{!}."), #alayen
("npc27_woman_to_woman", "{!}."),
("npc28_woman_to_woman", "{!}."),
("npc29_woman_to_woman", "Strange, isn't it? They say the world belongs to men, yet here we are, marching at its edge. I won't shrink back - and I see you won't either."),
("npc30_woman_to_woman", "{!}."),


  ("npc1_turn_against", "I am a servant too like we all are, you were my master and a friend once but now I have a new leader who order me to fight against you, my honor does not allow me to go against this order even if I'd want to, I'm so sorry, but I must do battle with you,  I hope you can forgive me in the next life."), #Borcha
  ("npc2_turn_against", "This is a sad day. I never thought that I might meet my old captain on the field of battle. Even if I triumph, it will bring me no joy."), #marnid
  ("npc3_turn_against", "Oh {playername} -- what a tragic turn our lives have taken! I can only hope that the tides of war that have made us enemies, will one day allow us to be friends."), #ymira
  ("npc4_turn_against", "Fate or destiny, whatever it is has brought us to opposing sides, I respect you as my friend and one who brought me up from my low point but a Berber is loyal to his commander so I have no choice other than to kill you. Draw your sword and let's get this over with!"), #rolf
  ("npc5_turn_against", "My Khagan, {playername} ! I took your salt, and was well rewarded for it! However, I will remind you of an old truth -- that while a Hun may be an ardent follower, and a devoted friend, he will never be your slave.... Anyway, today I come against you with my sword raised. But I hope that one day we raise a glass together, to a friendship renewed."), #beheshtur
  ("npc6_turn_against", "The time has come, {playername}. Our swords will clash and many men will die today! Let us do it quickly, without lingering even further."), #firentis
  ("npc7_turn_against", "Well, captain. You made of me a powerful woman, and for that I am grateful. However, you did not buy me, and now the circumstances have caused us our interests to clash, I can meet you in battle with a clear conscience. Still, I hope some day that circumstances may change again, and we may meet as friends."), #deshavi
  ("npc8_turn_against", "I am sorry, my friend that we have been put up to this situation, I have only ever wanted to avenge my father. You are dear to me and the reason why I am here but an Arab is loyal to the one he serves and I must be too, do not take this personally for I really do not want to do this."), #matheld
  ("npc9_turn_against", "I will not accept fault for the circumstances which have led us to become enemies. I want you to know that my conscience is clear, although my heart is heavy."), #alayen
  ("npc10_turn_against", "Well, it looks like the tides of fate have led me to make war on my old captain. Maybe things started to go wrong when you became my liege -- I suppose I was never much suited to vassalage. Anyway, here we are now. Maybe, when the world is changed and there are no more masters and servants, or lords and vassals, then we can meet together as friends."), #bunduk
  ("npc11_turn_against", "Great heaven, Rex. So now it looks like you and I are enemies. Didn't I say that life takes us on some very strange turns? Destiny sometimes has a cruel sense of humor -- I'll say that much."), #katrin
  ("npc12_turn_against", "So, it seems we must fight. I would have you know, {sir/my lady}, that I have not betrayed you. I had never served you as a man, but served the principles which I believed you upheld. As you no longer uphold them, I must do my best to thwart you. But I bear you no ill will, and I hope that we can meet again some day as friends"), #Artemios
  ("npc13_turn_against", "Commander, I would have never imagined it had to go this way. Now we are enemies, our armies will clash and death will follow... And then silence. If death was to claim me on the battlefield, I hope I'll be able to leave this world with your forgiveness..."), #nizar
  ("npc14_turn_against", "Well, {playername}. We meet as enemies. I confess that I have mixed feelings. It grieves me to make war on you, but if we meet in battle and I prevail, I will have defeated the worthiest foe in the entire world, and I will know that my mastery of the military art is complete!"), #lazalit
  ("npc15_turn_against", "Ah... I have not been looking forward to this day. I just want to say that in my sight, if you'd kept your faith in me, things would never have come to this. But no doubt you see it differently."), #artimenner
  ("npc16_turn_against", "Hello, Captain! So, I guess we're enemies! One small word of warning if we end up fighting each other -- once the rage of battle hits me, I can't always account for my actions. Just know that whatever I do, it's not personal. Maybe if we both walk away from this, we can meet once more as friends?"), #klethi
  ("npc17_turn_against", "Rex... Warlord... It was never meant to end like this. If I win, I will make sure to jump on my very same sword and die. If you win, please, grant me the funerals of a proper warrior. Now prepare."), #Alachis
  ("npc18_turn_against", "I'm sorry that we meet like this, Chief. There's no question that I owe my rise in life to you. You doubtless think me ungrateful. However, one has to follow one's destiny -- isn't that correct?"), #khaetag
  ("npc19_turn_against", "That's with great regret that we have to take swords against each other, Chief. However, I have my obligations to my new liege and have to follow them."),
  ("npc20_turn_against", "This is a sad day, {playername}. I never would have thought I would be against you when I was in your company, but it seems times have changed..."),
  ("npc21_turn_against", "I owe everything to you, this much is true, but I had to decide what was best for my family and myself. I'm sorry, Sir/Madame, but duty demands we fight."),
  ("npc22_turn_against", "I see we are now at opposite sides. I believed in you, and I trusted you, but you have forsaken reason and the Roman way of which I told you about, I will always follow it, no matter who is my liege! I will never give up! Now draw steel, wretch!"),
  ("npc23_turn_against", "You have strayed far enough from the way I have deemed good and which should be followed by those I consider to be good men. I must kill you for Hellas, for all that is sacred and as a punishment for your missteps. Andron gar epiphanon pasa ge taphos!"),
  ("npc24_turn_against", "Sometimes our sides are not chosen but given to us, by some of fate's turns I've become your enemy, I am sorry but my honor requires me to follow my current liege. Do not take this amiss but this is what I must do!"),
("npc25_turn_against", "Captain, I owe you much, but my loyalty now belongs elsewhere. My honor binds me to fight for my new leader, even if it means standing against you. I hope one day you will understand."),
  ("npc26_turn_against", "Sometimes our sides are not chosen but given to us, by some of fate's turns I've become your enemy, I am sorry but my honor requires me to follow my current liege. Do not take this amiss but this is what I must do!"),
("npc27_turn_against", "This is a hard path, {playername}. I never wished to cross blades with you. But now we stand as foes, and so - let steel decide."),
("npc28_turn_against", "So it comes to this, {playername}. Steel must decide between us. I bear no grudge, but I will not hold back. May the best warrior live."),
("npc29_turn_against", "So it comes to this, {playername}. I once followed your banner with hope. Now I raise my own. May this end swiftly, and with mercy."),
("npc30_turn_against", "It seems fate has twisted our paths, General. I regret this day, but I will not waver. Ready your blade."),

#NPC companion changes end





#Troop Commentaries begin
#Tags for comments are = allied/enemy, friendly/unfriendly, and then those related to specific reputations
#Also, there are four other tags which refer to groups of two or more reputations (spiteful, benevolent, chivalrous, and coldblooded)
#The game will select the first comment in each block which meets all the tag requirements

#Beginning of game comments
("comment_intro_liege_affiliated", "I am told that you are pledged to one of the pretenders who disputes my claim to my rulership. But we may still talk."),
##diplomacy start+ (documentation only)
#NOTE:
#  The comment_* strings below are used with script_lord_comment_to_s43
#  Some of the suffixes differ from the ones used in the personality codes.  The equivalencies are:
#     liege       = lrep_none
#     martial     = lrep_martial
#     badtempered = lrep_quarrelsome
#     pitiless    = lrep_selfrighteous
#     cunning     = lrep_cunning
#     sadistic    = lrep_debauched
#     goodnatured = lrep_goodnatured
#     upstanding  = lrep_upstanding
##diplomacy end+ (documentation only)
("comment_intro_famous_liege", "Your fame runs before you! Perhaps it is time that you sought a liege worthy of your valor."),
("comment_intro_famous_martial", "Your fame runs before you! Perhaps we shall test each other's valor in a tournament, or on the battlefield!"),
("comment_intro_famous_badtempered", "I've heard of you. Well, I'm not one for bandying words, so if you have anything to say, out with it."),
("comment_intro_famous_pitiless", "I know your name. It strikes fear in men's hearts. That is good. Perhaps we should speak together, some time."),
("comment_intro_famous_cunning", "Ah, yes. At last we meet. You sound like a good {man/woman} to know. Let us speak together, from time to time."),
("comment_intro_famous_sadistic", "I know your name -- and from what I hear, I'll warrant that many a grieving widow knows too. But that is no concern of mine."),
("comment_intro_famous_goodnatured", "I've heard of you! It's very good to finally make your acquaintance."),
("comment_intro_famous_upstanding", "I know your name. They say you are a most valiant warrior. I can only hope that your honour and mercy matches your valor."),

("comment_intro_noble_liege", "I see that you carry a {nobleman's/noble's} banner, although I do not recognize the device. Know that I am always looking for good {men/warriors} to fight for me, once they prove themselves to be worthy of my trust."),
("comment_intro_noble_martial", "I see that you carry a nobleman's banner, but I do not recognize the device. No matter -- a brave {man's/warrior's} home is all the world, or so they say!"),
("comment_intro_noble_badtempered", "I don't recognize the device on your banner. No doubt another foreigner come to our lands, as if we didn't have so many here already."),
("comment_intro_noble_pitiless", "I see that you carry a nobleman's banner, but I do not recognize the device. Another vulture come to grow fat on the leftovers of war, no doubt!"),
("comment_intro_noble_cunning", "I see that you carry a nobleman's banner, but I do not recognize the device. Still, it is always worthwhile to make the acquaintance of {men/women} who may one day prove themselves to be great warriors."),
("comment_intro_noble_sadistic", "I see that you carry a nobleman's banner, but I do not recognize the device. Perhaps you are the bastard {son/daughter} of a puffed-up cattle thief? Or perhaps you stole it?"),
("comment_intro_noble_goodnatured", "I see that you carry a nobleman's banner, but I do not recognize the device. Forgive my ignorance, {sir/my lady}! It is good to make your acquaintance."),
("comment_intro_noble_upstanding", "I see that you carry a nobleman's banner, but I do not recognize the device. No doubt you have come to Europe in search of wealth and glory. If this indeed is the case, then I only ask that you show mercy to those poor souls caught in the path of war."),


("comment_intro_common_liege", "You may be of common birth, but know that I am always looking for good men to fight for me, if they can prove themselves to be worthy of my trust."),
("comment_intro_common_martial", "Perhaps you are not of gentle birth, but even a commoner, be {he/she} of sufficient valor, may make something of {himself/herself} some day."),
("comment_intro_common_badtempered", "Speak quickly, if you have anything to say, for I have no time to be bandying words with common soldiers of fortune."),
("comment_intro_common_pitiless", "You have the look of a mercenary, another vulture come to grow fat on the misery of this land."),
("comment_intro_common_cunning", "Well... I have not heard of you, but you have the look of a {man/woman} who might make something of {himself/herself}, some day."),
("comment_intro_common_sadistic", "Normally I cut the throats of impudent commoners who barge into my presence uninvited, but I am in a good mood today."),
("comment_intro_common_goodnatured", "Well, you look like a good enough sort."),
("comment_intro_common_upstanding", "Peace to you, and always remember to temper your valor with mercy, your courage with honour."),


##diplomacy start+
#Change female intros and rejoiners to be prejudiced against whatever sex the player happens to be
#(This will be invisible to the player by default, since ordinarily these are never spoken to
#make players, but it allows a reversal of the convention.  TODO: add documentation of xxx

#famous
##dplmc+ changes to include female-to-male versions
("comment_intro_female_famous_liege", "I have heard much about you. Some {women/men} may fear a {man/woman} who is versed in the art of war, but I for one will not turn away hands that can grip a sword, should their owner be brave and loyal."),
("comment_intro_female_famous_martial", "I have heard much about you. They say that you are the equal of even the bravest of {women/men} in your prowess at arms. Perhaps one day I shall try my valor against yours, either in a tournament or on the battlefield!"),
("comment_intro_female_famous_badtempered", "I've heard of talk of you -- the {man/woman} who knows how to fight like a {woman/man}."),
("comment_intro_female_famous_pitiless", "I know your name. It strikes fear in {women/men}'s hearts. That is good. Perhaps we should speak together, some time."),
("comment_intro_female_famous_cunning", "Ah, yes. At last we meet. You sound like a good {man/woman} to know. Let us speak together, from time to time."),
("comment_intro_female_famous_sadistic", "I know your name -- and from what I hear, I'll warrant that many a grieving widow knows too. But that is no concern of mine."),
("comment_intro_female_famous_goodnatured", "I've heard of you! It's very good to finally make your acquaintance."),
("comment_intro_female_famous_upstanding", "I know your name. They say you are a most valiant warrior. I can only hope that your honour and mercy matches your valor."),


#aristocratic
##(... continuing dplmc+ changes to include female-to-male versions ...)
("comment_intro_female_noble_liege", "It is not often that I meet a {male/woman} who aspires to lead {warriors/men} into battle. But these are dark and troubled times, and I for one will not turn away hands that can grip a sword, should their owner be brave and loyal."),
("comment_intro_female_noble_martial", "I do not recognize the device on your banner, but clearly you are a {boy/lady} of rank. Please consider me your most humble servant."),
("comment_intro_female_noble_badtempered", "I don't recognize the device on that banner. Clearly another foreigner come to our lands, bringing their strange ways."),
("comment_intro_female_noble_pitiless", "I see that you carry a noble's banner, but I do not recognize the device... You should know, {boy/lady}, that in times of war it is the {women/men} who ride to war, and if you seek to overturn the natural order of things, you will find your fair head stuck on a pike -- like that of any other rebel!"),
("comment_intro_female_noble_cunning", "It is not unheard-of for a {male/woman} to seek {his/her} fortune on the battlefields, but neither is it usual. I shall be most interested in your progress."),
("comment_intro_female_noble_sadistic", "You appear to be of noble rank, but I don't recognize your banner. Clearly, another foreigner come to our shores -- no doubt from a land where {women/men} are weak, and the {men/women} ride to war in their place!"),
("comment_intro_female_noble_goodnatured", "I see that you carry a {noblewoman/nobleman}'s banner, but I do not recognize the device. Forgive my ignorance, {dear boy/my lady}! It is good to make your acquaintance."),
("comment_intro_female_noble_upstanding", "It is not every day that we see a {male/woman} caparisoned for war. Please do not take this amiss, {dear boy/my lady}, for you have every right to protect yourself, but I cannot pretend to be fully comfortable with your decision to fight in battle. I would prefer that {males/women} be untouched by these wars, as I believe the {male/female} to be the custodian of what little gentility and tenderness remains to us."),


#admiring
##(... continuing dplmc+ changes to include female-to-male versions ...)
("comment_intro_female_admiring_liege", "It is not often that I meet a {male/woman} who aspires to lead {warriors/men} into battle. But these are dark and troubled times, and I for one will not turn away hands that can grip a sword, should their owner be brave and loyal."),
("comment_intro_female_admiring_martial", "Greetings, {dear boy/my lady}. Although I see from your demeanor that you are not a conventional {boy/maiden}, I hope that you are not averse to a declaration of admiration from me, your most humble servant."),
("comment_intro_female_badtempered_admiring", "Heh. Fancy this -- a {pretty boy/maiden}, all equipped for war. Well, it's a strange sight, but in your case, I can imagine that it might grow on me."),
("comment_intro_female_pitiless_admiring", "It is unusual to see a {male/woman} girt for war. Be careful, {dear boy/my lady} -- it is a harsh world, and it would be a shame to see such beauty marred by a sword-blow."),
#Next line deliberately doesn't switch the gender of daughter in the female-to-male version (the implication is that the amazon wants her warrior daughters to have similar bravery)
("comment_intro_female_cunning_admiring", "Greetings, {dear boy/my lady}. Please do not think it forward, if I say that it is unusual to see a {male/woman} caparisoned for war. I hope that one day I may be the {mother/father} of a daughter possessed of such bravery and spirit."),
("comment_intro_female_sadistic_admiring", "What have we here! A {pretty boy/woman}, caparisoned for war! Well, I dare say that one as fair as you could lend a touch of {delicacy/femininity} even to a mail hauberk."),
("comment_intro_female_admiring_goodnatured", "{Dear boy/My lady}, if you are skilled as arms as you are fair in countenance, then your enemies should indeed fear you!"),
("comment_intro_female_admiring_upstanding", "Greetings, {dear boy/my lady}. Even with the dust of the march upon your clothes and gear, I can see that you are not lacking in the graces of your noble sex."),

#common
##(... continuing dplmc+ changes to include female-to-male versions ...)
("comment_intro_female_common_liege", "It is not often that I meet a {male/woman} who aspires to lead {warriors/men} into battle. But these are dark and troubled times, and I for one will not turn away hands that can grip a sword, should their owner be brave and loyal."),
("comment_intro_female_common_martial", "I must say, {dear boy/my lady} -- do be careful, riding about this dangerous land. If you ever wished to seek a more... em... settled life, I'm sure I could find you a worthy {wife/husband} from among my {warriors/men}."),
("comment_intro_female_common_badtempered", "By the way, {boy/girl} -- does your {mistress/husband} know that you nicked {her/his} weapons and armor? I'll bet you're in for a right old beating when you get home!"),
("comment_intro_female_common_pitiless", "These are fallen times indeed, when even {males/women} turn brigand, to pick the leavings from the wreckage of war."),
("comment_intro_female_common_cunning", "It is not unheard-of for a {male/woman} to seek {his/her} fortune on the battlefields, but neither is it usual. I shall be most interested in your progress."),
("comment_intro_female_common_sadistic", "A {male/woman}, caparisoned for war! Well, I suppose that you're {not much less/no more} womanly than most of those in my service who call themselves warriors."),
("comment_intro_female_common_goodnatured", "From the look of you, I suppose you can handle yourself, but do be careful out there, {dear boy/my lady}."),
("comment_intro_female_common_upstanding", "It is not every day that we see a {male/woman} caparisoned for war. Please do not take this amiss, {dear boy/my lady}, for you have every right to protect yourself, but I cannot pretend to be fully comfortable with your decision to fight in battle. I would prefer that {males/women} be untouched by these wars, as I believe the {male/female} to be the custodian of what little gentility and tenderness remains to us."),

#Rejoinder
##(... continuing dplmc+ changes to include female-to-male versions ...)
("rejoinder_intro_female_common_badtempered", "I won my weapons in battle. Would you care to test their edge?"),
("rejoinder_intro_female_noble_sadistic", "Never mind my country. Here, it seems, dogs lead {soldiers/men} to war."),
("rejoinder_intro_female_common_sadistic", "And you, {madam/sir}, are no more bestial than my horse."),
("rejoinder_intro_female_noble_pitiless", "I would restore the natural order, so that you no longer speak from your arse."),
("rejoinder_intro_female_common_pitiless", "Indeed, these are fallen times, when brigands call themselves 'Lord'."),

("rejoinder_intro_noble_sadistic", "Maybe now I'll take your banner. And your cattle. And your life."),


("rejoinder_intro_female_pitiless_admiring", "I would be delighted to mar your {pretty face/handsome nose}, {madam/sir}."),
("rejoinder_intro_female_common_upstanding", "Would you like to feel the tenderness of my steel?"),
("rejoinder_intro_female_noble_upstanding", "Would you like to feel the tenderness of my steel?"),
("rejoinder_intro_female_common_martial", "I could find worthier {wives/husbands} than those in a kennel."),
("rejoinder_intro_female_sadistic_admiring", "You could add a touch of humanity to a horse's harness, but just a touch."),
("rejoinder_intro_female_badtempered_admiring", "If you're disturbed by the sight of me, I'd be pleased to put out your eyes."),
##(end dplmc+ changes to include female-to-male versions)
##diplomacy end+

#("comment_defer_fief_to_woman", "Were you a man, I would gladly have granted you land, and counted you as one of my bravest vassals. But you see, this has never before happened in calradia. We have had women serve in our armies, and sometimes, a woman who is the inheritor of her husband or father will lead her retainers into battle to uphold her family obligation. But to enfief a woman for having proved herself in battle? I, for one, have not heard of this."),

#("comment_defer_fief_to_woman_2", "Do not think that I am slave to tradition, if it comes between me and the crown which is rightully mine. But a monarch also cannot appear weak..."),






#Actions vis-a-vis civilians
  ("comment_you_raided_my_village_enemy_benevolent",    "You have attacked innocent farmers under my protection in the village of {s51}. I will punish you for your misdeeds!"),
  ("comment_you_raided_my_village_enemy_spiteful",      "You have raided my village of {s51}, destroying my property and killing the tenants. I will take my compensation in blood!"),
  ("comment_you_raided_my_village_enemy_coldblooded",   "You have raided my village of {s51}, destroying my property and killing the tenants. I will make you think twice before you disrupt my revenues like that again."),
  ("comment_you_raided_my_village_enemy",               "You have raided my village of {s51}, destroying my property and killing tenants under my protection. You will pay the price for your crime!"),
  ("comment_you_raided_my_village_unfriendly_spiteful", "You have raided my village of {s51}. Do it again and I'll gut you like a fish."),
  ("comment_you_raided_my_village_friendly",            "You have raided my village of {s51}. This will place a grave strain on our friendship."),
  ("comment_you_raided_my_village_default",             "You have raided my village of {s51}. If you continue to behave this way, we may soon come to blows."),

  #SB : remove "stolen from my property", cattles -> cattle
  ("comment_you_stole_cattles_from_my_village_enemy_benevolent",    "I have heard that you have stolen cattle from innocent farmers under my protection in the village of {s51}. I will punish you for your misdeeds!"),
  ("comment_you_stole_cattles_from_my_village_enemy_spiteful",      "I have heard that you have stolen cattle from my villagers living at {s51}. You will pay results of this dishonorable act!"),
  ("comment_you_stole_cattles_from_my_village_enemy_coldblooded",   "I have heard that you have stolen cattle from my villagers living at {s51}. I will make you think twice before you disrupt my revenues like that again."),
  ("comment_you_stole_cattles_from_my_village_enemy",               "I have heard that you have stolen cattle from my villagers living at {s51}. You will pay results of this dishonorable act!"),
  ("comment_you_stole_cattles_from_my_village_unfriendly_spiteful", "I have heard that you have stolen cattle from my villagers living at {s51}. Do it again and I'll gut you like a fish."),
  ("comment_you_stole_cattles_from_my_village_friendly",            "I have heard that you have stolen cattle from my villagers living at {s51}. This will place a grave strain on our friendship."),
  ("comment_you_stole_cattles_from_my_village_default",             "I have heard that you have stolen cattle from my villagers living at {s51}. If you continue to behave this way, we may soon come to blows."),

  ("comment_you_robbed_my_village_enemy_coldblooded", "You have robbed my tenants in the village of {s51}. I take that as a personal insult."),
  ("comment_you_robbed_my_village_enemy",             "You have robbed innocent farmers under my protection in the village of {s51}. I will punish you for your misdeeds!"),
  ("comment_you_robbed_my_village_friendly_spiteful", "I have heard that you pinched some food from my tenants at {s51}. Well, I'll not begrudge you a scrap or two, but keep in mind that I'm the one who must listen to their whining afterward."),
  ("comment_you_robbed_my_village_friendly",          "I have heard that you requisitioned supplies from my tenants at {s51}. I am sure that you would not have done so were you not desperately in need."),
  ("comment_you_robbed_my_village_default",           "You have robbed my tenants in the village of {s51}. If you continue to behave this way, we may soon come to blows."),

  ("comment_you_accosted_my_caravan_enemy",          "You have been accosting caravans under my protection. But your trail of brigandage will soon come to an end."),
  ("comment_you_accosted_my_caravan_default",        "You have been accosting caravans under my protection. This sort of behavior must stop."),

  ("comment_you_helped_villagers_benevolent",                "I heard that you gave charity to my tenants in the village of {s51}. I had been neglectful in my duties as lord and protector, and I appreciate what you have done."),
  ("comment_you_helped_villagers_friendly_cruel",            "I heard that you gave charity to my tenants in the village of {s51}. I appreciate that you meant well, but I'd rather you not undercut my authority like that."),
  ("comment_you_helped_villagers_friendly",                  "I heard that you gave charity to my tenants in the village of {s51}. Times are hard, and I know that you mean well, so I will not object to you providing them with assistance."),
  ("comment_you_helped_villagers_unfriendly_spiteful",       "I heard that you gave charity to my tenants in the village of {s51}. As amusing as it is to see you grubbing for favor among my vassals, I would ask you to mind your own business."),
  ("comment_you_helped_villagers_cruel",                     "I heard that you gave charity to my tenants in the village of {s51}. As the peasants' lord and protector, it is most properly my duty to assist them in times of hardship. You may mean well, but your actions still undercut my authority. I would thank you to leave them alone."),
  ("comment_you_helped_villagers_default",                   "I heard that you gave charity to my tenants in the village of {s51}. Times are hard, and I know that you mean well, but try not to make a habit of it. I am their lord and protector, and I would rather not have them go looking to strangers for assistance."),

#Awarding fief-related events
  ("comment_you_give_castle_in_my_control",                    "You won't regret your decision to give {s51} to me. You can count on me to protect it."),
  #can be added some more here acc. characteristic.

#Combat-related events
  ("comment_you_captured_a_castle_allied_friendly",            "I heard that you have besieged and taken {s51}. That was a great dead, and I am proud to call you my friend!"),
  ("comment_you_captured_a_castle_allied_spiteful",            "I heard that you have besieged and taken {s51}. Good work! Soon, we will have all their fortresses to despoil, their treasuries to ransack, their grieving widows to serve us our wine."),
  ("comment_you_captured_a_castle_allied_unfriendly_spiteful", "I heard that you have besieged and taken {s51}. Well, every dog has his day, or so they say. Enjoy it while you can, until your betters kick you back out in the cold where you belong."),
  ("comment_you_captured_a_castle_allied_unfriendly",          "I heard that you have besieged and taken {s51}. Whatever our differences in the past, I must offer you my congratulations."),
  ("comment_you_captured_a_castle_allied",                     "I heard that you have besieged and taken {s51}. We have them on the run!"),

  ("comment_you_captured_my_castle_enemy_spiteful",            "I hear that you have broken into my home at {s51}. I hope the dungeon is to your liking, as you will be spending much time there in the years to come."),
  ("comment_you_captured_my_castle_enemy_chivalrous",          "You hold {s51}, my rightful fief. I hope you will give me the chance to win it back!"),
  ("comment_you_captured_my_castle_enemy",                     "You have something that belongs to me -- {s51}. I will make you relinquish it."),

###Add some variation to these
  ("comment_we_defeated_a_lord_unfriendly_spiteful",           "I suppose you will want to drink to the memory of our victory over {s54}. Well, save your wine -- it will take more than that to wipe out the stain of your earlier disgraces."),
  ("comment_we_defeated_a_lord_unfriendly",                    "I will not forget how we fought together against {s54}, but I can also not forget the other matters that lie between us."),
  ("comment_we_defeated_a_lord_cruel",                         "That was a great victory over {s54}, wasn't it? We made of his army a feast for the crows!"),
  ("comment_we_defeated_a_lord_quarrelsome",                   "I won't forget how we whipped {s54}? I enjoyed that."),
  ("comment_we_defeated_a_lord_upstanding",                    "I will not forget our victory over {s54}. Let us once again give thanks to heaven, and pray that we not grow too proud."),
  ("comment_we_defeated_a_lord_default",                       "That was a great victory over {s54}, wasn't it? I am honoured to have fought by your side."),

  ("comment_we_fought_in_siege_unfriendly_spiteful",           "I suppose you will want to drink to the memory of our capture of {s51}. Well, save your wine -- it will take more than that to wipe out the stain of your earlier disgraces."),
  ("comment_we_fought_in_siege_unfriendly",                    "I will not forget how we together we stormed {s51}, but I can also not forget the other matters that lie between us."),
  ("comment_we_fought_in_siege_cruel",                         "I won't forget how we broke through the walls of {s51} and put its defenders to the sword. It is a sweet memory."),
  ("comment_we_fought_in_siege_quarrelsome",                   "Remember how the enemy squealed when we came over the walls of {s51}? They had thought they were safe! We wiped the smug smiles of their faces!"),
  ("comment_we_fought_in_siege_upstanding",                    "I will not forget our capture of {s51}. Let us once again give thanks to heaven, and pray that we not grow too proud."),
  ("comment_we_fought_in_siege_default",                       "I will not forget how together we captured {s51}. I am honoured to have fought by your side."),

  ("comment_we_fought_in_major_battle_unfriendly_spiteful",    "I suppose you will want to drink to the memory of our great victory near {s51}. Well, save your wine -- it will take more than that to wipe out the stain of your earlier disgraces."),
  ("comment_we_fought_in_major_battle_unfriendly",             "I will not forget how we fought together in the great battle near {s51}, but I can also not forget the other matters that lie between us."),
  ("comment_we_fought_in_major_battle_cruel",                  "I won't forget the great battle near {s51}, when we broke through the enemy lines and they ran screaming before us. It is a sweet memory."),
  ("comment_we_fought_in_major_battle_quarrelsome",            "That was a fine fight near {s51}, when we made those bastards run!"),
  ("comment_we_fought_in_major_battle_upstanding",             "I will not forget how we fought side by side at the great battle near {s51}. Let us once again give thanks to heaven, and pray that we not grow too proud."),
  ("comment_we_fought_in_major_battle_default",                "I will not forget how we fought side by side at the great battle near {s51}. I am honoured to have fought by your side."),



  ##diplomacy start+
  #Make gender correct, using reg4 for the gender of s54.  Making this work required altering script_get_relevant_comment_to_s42
  ("comment_you_defeated_a_lord_allied_liege",                   "So, you crossed swords with that rascal they call {s54}, and emerged victorious. I am very happy to hear that."),
  ("comment_you_defeated_a_lord_allied_unfriendly_spiteful",     "I heard that you fought and defeated {s54}. Every dog has its day, I suppose."),
  ("comment_you_defeated_a_lord_allied_spiteful",                "I heard that you fought and defeated that dog {s54}. Ah, if only I could have heard {reg4?her:him} whimpering for mercy."),
  ("comment_you_defeated_a_lord_allied_unfriendly_chivalrous",   "I heard that you fought and defeated {s54}. I hope that you did not use dishonourable means to do so."),
  ("comment_you_defeated_a_lord_allied",                         "I heard that you fought and defeated {s54}. I wish you joy of your victory."),
  ##diplomacy end+

  ("comment_you_defeated_me_enemy_chivalrous", "I will not begrudge you your victory the last time that we met, but I am anxious for another round!"),
  ("comment_you_defeated_me_enemy_spiteful",   "I have been looking forward to meeting you again. Your tricks will not deceive me a second time, and I will relish hearing your cries for mercy."),
  ("comment_you_defeated_me_enemy",            "When last we met, {playername}, you had the better of me. But I assure you that it will not happen again!"),

  ("comment_I_defeated_you_enemy_spiteful",          "Back for more? Make me fight you again, and I'll feed your bowels to my hounds."),
  ("comment_I_defeated_you_enemy_chivalrous",        "Come to test your valor against me again, {playername}?"),
  ("comment_I_defeated_you_enemy_benevolent",        "So once again you come at me? Will you ever learn?"),
  ("comment_I_defeated_you_enemy_coldblooded",       "You are persistent, but a nuisance."),
  ("comment_I_defeated_you_enemy",                   "How many times must I chastise you before you learn to keep your distance?"),

  ##diplomacy start+
  #Make gender correct, using reg4 for the gender of s54.  Making this work required altering script_get_relevant_comment_to_s42
  #Replacing "men" with "warriors" when the enemy leader was female in case it was an all-female band.
  ("comment_we_were_defeated_unfriendly_spiteful",   "Last I saw you, you had been struck down by the {reg4?warriors:men} of {s54}. I blame you for that disaster. What a pity to see that you survived."),
  ("comment_we_were_defeated_unfriendly",            "Last I saw you, you had been struck down by the {reg4?warriors:men} of {s54}. Well, I see that you survived."),
  ("comment_we_were_defeated_cruel",                 "Last I saw you, you had been struck down by the {reg4?warriors:men} of {s54}. Don't worry -- we'll find {reg4?her:him}, and make {reg4?her:him} choke on {reg4?her:her} victory."),
  ("comment_we_were_defeated_default",               "Last I saw you, you had been struck down by the {reg4?warriors:men} of {s54}. It is good to see you alive and well."),
  ##diplomacy end+

  ##diplomacy start+
  #Make gender correct, using reg4 for the gender of s54.  Making this work required altering script_get_relevant_comment_to_s42
  ("comment_you_were_defeated_allied_friendly_spiteful",      "I heard that {s54} gave you a hard time. Don't worry, friend -- I'll find {reg4?her:him} for you, and make you a gift of {reg4?her:his} head."),
  ("comment_you_were_defeated_allied_unfriendly_cruel",       "I had heard that {s54} slaughtered your men like sheep. But here you are, alive. Such a disappointment!"),
  ("comment_you_were_defeated_allied_spiteful",               "I heard that {s54} crushed you underfoot like an ant. Hah! Children should not play games made for grown-ups, little {boy/girl}!"),
  ("comment_you_were_defeated_allied_pitiless",               "I heard that {s54} defeated you, and scattered your forces. That is most disappointing..."),
  ("comment_you_were_defeated_allied_unfriendly_upstanding",  "I heard that {s54} defeated you. Perhaps you should consider if you have considered any misdeeds, that might cause heaven to rebuke you in this way."),
  ("comment_you_were_defeated_allied_unfriendly",             "I heard that {s54} defeated you. Look, try not to get too many of our men killed, will you?"),
  ("comment_you_were_defeated_allied",                        "I heard that {s54} defeated you. But take heart -- the tables will soon be turned!"),
  ##diplomacy end+

  ##diplomacy start+
  #Make gender correct, using reg4 for the gender of s54.  Making this work required altering script_get_relevant_comment_to_s42
  ("comment_you_helped_my_ally_unfriendly_chivalrous",        "I heard that you saved {s54} from likely defeat. Whatever else I may think of you, I must at least commend you for that."),
  ("comment_you_helped_my_ally_unfriendly",                   "{!}[revelance should be zero, and this message should not appear]"),
  ("comment_you_helped_my_ally_liege",                        "I heard that you saved my vassal {s54} from likely defeat. "),
  ("comment_you_helped_my_ally_unfriendly_spiteful",          "I heard that you rode to the rescue of our poor {s54}. Did you think {reg4?her:him} a damsel in distress? No matter -- it's a common mistake."),
  ("comment_you_helped_my_ally_spiteful",                     "I heard that you saved {s54} from a whipping. You should have let {reg4?her:him} learn {reg4?her:his} lesson, in my opinion."),
  ("comment_you_helped_my_ally_chivalrous",                   "I heard that you got {s54} out of a tight spot. That was a noble deed."),
  ("comment_you_helped_my_ally_default",                   "I heard that you got {s54} out of a tight spot. Good work!"),
  ##diplomacy end+

  #SB : duplicate strings
  ("comment_you_were_defeated_allied_unfriendly_dupe", "I heard that {s54} defeated you. Look, try not to get too many of our men killed, will you?"),
  ("comment_you_were_defeated_allied_dupe", "I heard that {s54} defeated you. But take heart -- the tables will soon be turned!"),

  ("comment_you_abandoned_us_unfriendly_spiteful",     "You worm! You left us alone to face {s54}, didn't you? I spit at you."),
  ("comment_you_abandoned_us_unfriendly_pitiless",     "Well... You abandoned me in the middle of a battle with {s54}, didn't you? I'll see you buried in a traitor's grave."),
  ("comment_you_abandoned_us_spiteful",                "You disappeared in the middle of that battle with {s54}... I hope you have a good explanation. Did your bowels give out? Were you shaking too hard with fear to hold your weapon?"),
  ("comment_you_abandoned_us_chivalrous",              "What happened? You disappeared in the middle of that battle against {s54}. I can only hope that you were too badly wounded to stand, for I would be ashamed to have gone into battle alongside a coward."),
  ("comment_you_abandoned_us_benefitofdoubt",          "What happened? You disappeared in the middle of that battle against {s54}. I assume that you must have been wounded, but it did look suspicious."),
  ("comment_you_abandoned_us_default",                 "What happened? One moment you were fighting with us against {s54}, the next moment you were nowhere to be found?"),

  ("comment_you_ran_from_me_enemy_spiteful",          "Last time we met, you ran from me like a whipped dog. Have you come back to bark at me again, or to whine for mercy?"),
  ("comment_you_ran_from_me_enemy_chivalrous",        "Last time we met, you fled from me. Learn to stand and fight like a gentleman!"),
  ("comment_you_ran_from_me_enemy_benevolent",        "When I saw you flee the last time that we met, I had hoped that I would not have to fight you again."),
  ("comment_you_ran_from_me_enemy_coldblooded",       "Last time we met, you fled from me. That was a wise decision"),
  ("comment_you_ran_from_me_enemy",                   "You may have been able to escape the last time we crossed paths, but the next time I doubt that you be so lucky."),

  ("comment_you_ran_from_foe_allied_chivalrous",      "They say that you fled from {s54}, leaving your men behind. I pray that this is not true, for such conduct does dishonour to us all."),
  ("comment_you_ran_from_foe_allied_upstanding",      "They say that you fled from {s54}, leaving your men behind. I do not always believe such rumors, and I also know that desperate straits call for desperate measures. But I beg you to take more care of your good name, for men will not fight in our armies if they hear that we abandon them on the field of battle."),
  ("comment_you_ran_from_foe_allied_spiteful",        "By the way, they said that you ran away from {s54} like a quaking little rabbit, leaving your men behind to be butchered. Ha! What a sight that would have been to see!"),


  ("comment_you_defeated_my_friend_enemy_pragmatic",  "You may have bested {s54}, but you cannot defeat us all."),
  ("comment_you_defeated_my_friend_enemy_chivalrous", "I have heard that you defeated {s54}, and ever since have been anxious to cross swords with you."),
  ("comment_you_defeated_my_friend_enemy_spiteful",   "Your fame runs before you, {playername}. {s54} may have fallen for your tricks, but if you fight me, you'll find a me a much more slippery foe."),
  ("comment_you_defeated_my_friend_enemy",            "They say that you have defeated {s54}. But I will be a truer test of your skill at arms."),

  ##diplomacy start+
  #Make gender correct, using reg4 for the gender of s54.  Making this work required altering script_get_relevant_comment_to_s42
  ("comment_you_captured_a_lord_allied_friendly_spiteful",   "I heard that you captured {s54}. I hope that you squeezed {reg4?her:him} for every siliqua."),
  ("comment_you_captured_a_lord_allied_unfriendly_spiteful", "I heard that you captured {s54}. Your coffers must be well-bloated with ransom by now. Such a pity that money cannot transform a low-born cur into a {gentleman/gentlewoman}!"),#also gentleman -> {gentleman/gentlewoman}
  ("comment_you_captured_a_lord_allied_chivalrous",          "I heard that you captured {s54}. Well done. I assume, of course, that {reg4?she:he} has been been treated with the honours due {reg4?her:his} rank."),
  ("comment_you_captured_a_lord_allied",                     "I heard that you captured {s54}. Well done. {reg4?Her:His} ransom must be worth quite something."),
  ##diplomacy end+

  ##diplomacy start+
  #Make gender correct, using reg4 for the gender of s54.  Making this work required altering script_get_relevant_comment_to_s42
  ("comment_you_let_go_a_lord_allied_chivalrous",            "I heard that you captured {s54}, but then let {reg4?her:him} go. Such chivalry does a credit to our cause."),
  ("comment_you_let_go_a_lord_allied_upstanding",            "I heard that you captured {s54}, but then let {reg4?her:him} go. Well, that was an honourable course of action, if possibly also a dangerous one."),
  ("comment_you_let_go_a_lord_allied_coldblooded",           "I heard that you captured {s54}, but then let {reg4?her:him} go. That was most chivalrous of you, but chivalry does not win wars."),
  ("comment_you_let_go_a_lord_allied_unfriendly_spiteful",   "I heard that you captured {s54}, but then let {reg4?her:him} go. How very chivalrous of you! No doubt the widows and orphans {reg4?she:he} leaves in {reg4?her:his} wake will want to commend you in person."),
  ("comment_you_let_go_a_lord_allied",                       "I heard that you captured {s54}, but then let {reg4?her:him} go. Well, I will not tell you what to do with your own prisoners."),
  ##diplomacy end+

  ("comment_you_let_me_go_spiteful",                    "When last we met, you had me at your mercy and allowed me to go free. I hope you enjoyed toying with me, like a cat with a mouse, because soon I will have you at my mercy, to slay or humiliate according to my fancy."),
  ("comment_you_let_me_go_enemy_chivalrous",            "When last we met, you had me at your mercy and allowed me to go free. That was most chivalrous of you, and I will not forget. But I also must remember my oath to my liege, and our kingdoms are still at war."),
  ("comment_you_let_me_go_enemy_coldblooded",           "When last we met, you had me at your mercy and allowed me to go free. But we are still enemies, and I cannot promise to repay your mercy in kind."),
  ("comment_you_let_me_go_enemy",                       "When last we met, you had me at your mercy and allowed me to go free. That was kind of you. But we are still at war."),
  ("comment_you_let_me_go_default",                     "When last we met, you had me at your mercy and allowed me to go free. That was kind of you, and I am glad that our kingdoms are no longer at war."),


#Internal faction events
  ("comment_pledged_allegiance_allied_martial_unfriendly",             "I heard that you have pledged allegiance to our lord, {s54}. Pray do not disgrace us by behaving in a cowardly fashion."),
  ("comment_pledged_allegiance_allied_martial",                        "I heard that you have pledged allegiance to our lord, {s54}. I look forward to fighting alongside you against our foes."),
  ("comment_pledged_allegiance_allied_quarrelsome_unfriendly",         "I heard that you have pledged allegiance to our lord, {s54}. Bah. Do yourself a favor, and stay out of my way."),
  ("comment_pledged_allegiance_allied_quarrelsome",                    "I heard that you have pledged allegiance to our lord, {s54}. Fight hard against our foes, respect your betters, and don't cross me, and we'll get along fine."),
  ("comment_pledged_allegiance_allied_selfrighteous_unfriendly",       "I heard that you have pledged allegiance to our lord, {s54}. If I were he, I would not trust you to clean the sculleries."),
  ("comment_pledged_allegiance_allied_selfrighteous",                  "I heard that you have pledged allegiance to our lord, {s54}. Fight bravely and you will be well-rewarded. Betray us, and we shall make of you the kind of example that will not soon be forgotten."),
  ("comment_pledged_allegiance_allied_cunning_unfriendly",             "I heard that you have pledged allegiance to our lord, {s54}. I do not pretend to be happy about his decision, but perhaps it is better to have you inside our tent pissing out, than the other way around."),
  ("comment_pledged_allegiance_allied_cunning",                        "I heard that you have pledged allegiance to our lord, {s54}. That is good. The more skilled fighters we have with us in these troubled times, the better. I shall be watching your progress."),
  ("comment_pledged_allegiance_allied_debauched_unfriendly",           "I heard that you have pledged allegiance to our lord, {s54}. No doubt you will soon betray him, and I will have the pleasure of watching you die a traitor's death."),
  ("comment_pledged_allegiance_allied_debauched",                      "I heard that you have pledged allegiance to our lord, {s54}. Excellent... I am sure that you and I will become very good friends. But remember -- if you betray us, it will be the biggest mistake you will ever make."),
  ("comment_pledged_allegiance_allied_goodnatured_unfriendly",         "I heard that you have pledged allegiance to our lord, {s54}. Well, I can't say that I would have trusted you, but perhaps you deserve the benefit of the doubt."),
  ("comment_pledged_allegiance_allied_goodnatured",                    "I heard that you have pledged allegiance to our lord, {s54}. Good {man/woman}! Our lord is a noble soul, and rewards loyalty and valor with kindness and generosity."),
  ("comment_pledged_allegiance_allied_upstanding_unfriendly",          "I heard that you have pledged allegiance to our lord, {s54}. Alas, from what I know of you I fear that you will disgrace us, but I will be happy if you prove me wrong."),
  ("comment_pledged_allegiance_allied_upstanding",                     "I heard that you have pledged allegiance to our lord, {s54}. Fight against our foes with valor, but also with honour and compassion. A good name is as valuable as a sharp sword or a swift horse in affairs of arms."),


  ("comment_our_king_granted_you_a_fief_allied_friendly_cruel",     "I heard that {s54} granted you {s51} as a fief. Don't forget -- spare the whip and spoil the peasant!"),
  ("comment_our_king_granted_you_a_fief_allied_friendly_cynical",   "I heard that {s54} granted you {s51} as a fief. I am glad to see you prosper -- but be careful. Men are vipers, envious and covetous of their neighbours' wealth. Stay close to me, and I'll watch your back."),

  ("comment_our_king_granted_you_a_fief_allied_friendly",              "I heard that {s54} granted you {s51} as a fief. May your new lands prosper."),
  ("comment_our_king_granted_you_a_fief_allied_unfriendly_upstanding", "I heard that {s54} granted you {s51} as a fief. But keep in mind that pride goes before a fall."),
  ("comment_our_king_granted_you_a_fief_allied_unfriendly_spiteful",   "I heard that {s54} granted you {s51} as a fief. I suspect, however, that fortune is only raising you up so as to humble you even more, when it casts you back into the dung from whence you came."),
  ("comment_our_king_granted_you_a_fief_allied_spiteful",              "I heard that {s54} granted you {s51} as a fief. Let's hope you are indeed deserving of our lord's favor."),

  ("comment_our_king_granted_you_a_fief_allied",                       "I heard that {s54} granted you {s51} as a fief. You seem to be doing very well for yourself."),

  ("comment_you_renounced_your_alliegance_enemy_friendly",             "I heard that you renounced your allegiance to our lord, {s54}. It grieves me that we must now meet on the field of battle."),
  ("comment_you_renounced_your_alliegance_friendly",                   "I heard that you renounced your allegiance to our lord, {s54}. Let us pray that we may not come to blows."),
  ("comment_you_renounced_your_alliegance_unfriendly_spiteful",        "I always had you figured for a traitor to {s54}, and now it seems I was proven right. I hope you are prepared to die a traitor's death!"),
  ("comment_you_renounced_your_alliegance_unfriendly_moralizing",      "I heard that you renounced your allegiance to our lord, {s54}. I am forced to consider you a traitor."),
  ("comment_you_renounced_your_alliegance_enemy",                      "I heard that you renounced your allegiance to our lord, {s54}. Well, it is the way of the world for old comrades to become enemies."),
  ("comment_you_renounced_your_alliegance_default",                    "I heard that you renounced your allegiance to our lord, {s54}. Well, that is your decision, but do not expect me to go easy on you when we meet on the battlefield."),

#player claim throne statements
  ("comment_you_claimed_the_throne_1_player_liege",             "My informants tell me that some people in this realm are speaking of you as the next king. I assume that you will quickly put a stop to such idle and dangerous talk."),
  ("comment_you_claimed_the_throne_2_player_liege",             "My informants tell me that some of your companions have telling the peasants that you have a claim to the throne. I sincerely hope that they have been acting without your orders."),

#new political comments
##diplomacy start+
#Note that the following are not called from the conversation-starting invocation of script_get_relevant_comment_to_s42
##diplomacy end+
  ("comment_lord_intervened_against_me", "It is well known that I had quarreled with {s54}, and {s50} ruled in my rival's favor."),
  ("comment_i_protested_marshall_appointment", "It is well known that I had protested {s54}'s decision to appoint {s51} as marshal."),
  ("comment_i_blamed_defeat", "It is well known that I am dissatisfied with {s54} for the favor shown to {s51}, who led us to defeat against the {s56}."),
  ("comment_i_was_entitled_to_fief", "It is well known that I am disappointed that {s54} received the fief of {s51}, which should have gone to me."),

##diplomacy start+
#Altered to use reg3 for gender of s51, reg4 for gender of s54, and reg65 for gender of speaker
#Note that some of these are not called from the conversation-starting invocation of script_get_relevant_comment_to_s42
  ("comment_i_quarreled_with_troop_over_woman", "It is well known that {s51} paid suit to {s54}, while I was also courting {reg4?her:him}. {reg3?She:He} is unworthy of {reg4?her:his} attentions, and I intend to teach {reg3?her:him} to keep {reg3?her:his} distance from {reg4?her:him}."),

  ("comment_i_quarreled_with_you_over_woman_default", "I hear that you have been paying suit to {s54}. I do not believe that you are worthy of a fair {reg4?lady:lad} such as {reg4?her:him}, and would strongly encourage you to cease pursuing {reg4?her:him}."),

  ("comment_i_quarreled_with_you_over_woman_derisive", "I hear that you have been paying suit to {s54}. Let me tell you something -- I've had my eye on that one ever since I was a {reg65?lass:lad}, and {reg4?she:he} was a {reg4?lass:lad}. {reg4?She:he}'s a high-born {reg4?lady:scion} of this realm, and should not be demeaned by a foreigner's crude attentions. Keep away from {reg4?her:him}, or expect to pay the price!"),
##diplomacy end+

  ("comment_player_suggestion_succeeded", "I followed your suggestion, and profited much by your advice."),
  ("comment_player_suggestion_failed", "I followed your suggestion and met with disaster, and I hold you responsible."),

  ##diplomacy start+
  #Make gender correct, using reg4 for the gender of s54.  Making this work required altering script_get_relevant_comment_to_s42
  ("comment_you_enfiefed_a_commoner_hesitant",  "I understand that you have given {s51} to a commoner who calls {reg4?herself:himself} {s54}. Be careful. To learn the art of governance is no easy task, and perhaps it is best that fathers pass it on to their sons. I advise you against tampering with the institution of lordship."),
  ("comment_you_enfiefed_a_commoner_derisive",   "I understand that you have given {s51} to a commoner who calls {reg4?herself:himself} {s54}. Do not the ancients warn us against making royal robes out of the hides of pigs?"),
  ("comment_you_enfiefed_a_commoner_nasty",      "I understand that you have given {s51} to a commoner who has taken the name of {s54}. Have a care! A dog may turn on its master."),
  ##diplomacy end+

  ##diplomacy start+
  #Make gender correct, using reg4 for the gender of s50.  Making this work required altering script_get_relevant_comment_to_s42
  #Don't change the order of the following strings!  (Refer to script_get_relevant_comment_to_s42 if you must)
  ("comment_marriage_normal_family",  "Congratulations on your marriage to my {s11} {s50}. You may now consider yourself part of the family!"),
  ("comment_marriage_normal",         "Congratulations on your marriage to {s50}. The news does credit to you both."),
  ("comment_marriage_normal_nasty",   "Well -- I see that you have married {s50}. (reg4?She:He} was always a silly {reg4?girl:boy}, with appalling judgment."),

  ("comment_marriage_elopement_family",  "Well... You somehow persuaded my {s11} {s50} to marry you. I don't know what you did to make {reg4?her:him} accept you, but our family will not forget this humiliation."),
  ("comment_marriage_elopement_liege",   "I hear that you have eloped with {s50}, against {reg4?her:his} family's wishes. I am not pleased. {reg4?Her:His} family are among the great lords of my realm, and I do not like to see them made to look like fools."),
  ##diplomacy end+

  ("comment_you_broke_truce_as_my_vassal",  		"I hear that you have broken my truce by attacking {s55}. Do you know how this makes me look? If you were acting under my orders, I appear dishonorable. If you were not, I look weak. I have half a mind to indict you for treason here and now."),
  ("comment_you_attacked_neutral_as_my_vassal", "I hear that you have attacked subjects of the {s55}. You have given them an excuse to attack me, if they want... We shall see what comes of this. A fine day's work you have done!"),



  ("personality_archetypes",   "liege"),
  ("martial",                  "martial"),
  ("quarrelsome",              "bad-tempered"),
  ("selfrighteous",            "pitiless"),
  ("cunning",                  "cunning"),
  ("debauched",                "sadistic"),
  ("goodnatured",              "good-natured"),
  ("upstanding",               "upstanding"),
  ("roguish",                  "roguish"),
  ("benevolent",               "benevolent"),
  ("mercantile",               "mercantile"),

  ("surrender_demand_default",        "Yield or die!"),
  ("surrender_demand_martial",        "The odds are not in your favor today. You may fight us, but there is also no shame if you yield now."),
  ("surrender_demand_quarrelsome",    "I've got you cornered. Give up, or I'll ride you down like a dog."),
  ("surrender_demand_pitiless",       "You cannot defeat me, and I'll teach you a painful lesson if you try. Yield!"),
  ("surrender_demand_cunning",        "You are outmatched today. Give up -- if not for your own sake, then think of your men!"),
  ("surrender_demand_sadistic",       "Surrender or I'll gut you like a fish!"),
  ("surrender_demand_goodnatured",    "We have the advantage of you. Yield, and you will be well-treated."),
  ("surrender_demand_upstanding",     "You may fight us, but many of your men will be killed, and you will probably lose. Yield, and spare us both the unnecessary bloodshed."),

  ("surrender_offer_default",        "Stop! I yield!"),
  ("surrender_offer_martial",        "Stop! I yield!"),
  ("surrender_offer_quarrelsome",    "Enough! You win today, you dog! Ach, the shame of it!"),
  ("surrender_offer_pitiless",       "I yield! You have won. Cursed be this day!"),
  ("surrender_offer_cunning",        "Stop! I yield to you!"),
  ("surrender_offer_sadistic",       "I give up! I give up! Call back your dogs!"),
  ("surrender_offer_goodnatured",    "I yield! Congratulations on your victory, {sir/madame}!"),
  ("surrender_offer_upstanding",     "I yield! Grant me the honours of war, and do yourself credit!"),


  ("lord_declines_negotiation_offer_default",     "That may be, but I wish to fight with you"),
  ("lord_declines_negotiation_offer_martial",     "That may be, but it is my duty to fight with you"),
  ("lord_declines_negotiation_offer_quarrelsome", "Hah! I want to fight with you"),
  ("lord_declines_negotiation_offer_pitiless",    "Why should I care? I wish to fight with you"),
  ("lord_declines_negotiation_offer_cunning",     "Ah. Unfortunately, you see, I wish to fight with you"),
  ("lord_declines_negotiation_offer_sadistic",    "Still your tongue! You will have need of it shortly, while begging for mercy"),
  ("lord_declines_negotiation_offer_goodnatured", "I'm sorry -- I can't just let you ride away. No hard feelings?"),
  ("lord_declines_negotiation_offer_upstanding",  "That may be, but my duty to my liege requires me to fight with you"),


  ("prisoner_released_default",       "You have my gratitude, {sir/madame}. I shall not forget your kindness."),
  ("prisoner_released_martial",       "You are indeed a {man/woman} of honour, {sir/madame}. I shall not forget this!"),
  ("prisoner_released_quarrelsome",   "I'm free? Well... Good bye, then."),
  ("prisoner_released_pitiless",      "Thank you. When you are finally defeated, I will request for your death to be swift and merciful. Unless, that is, you care to join us... Good bye, for now."),
  ("prisoner_released_cunning",       "Am I? You are a good {man/woman}. I will try to find a way to repay you."),
  ("prisoner_released_sadistic",      "Am I? So refined is your cruelty, that you would rather see me free and humiliated, than in chains. Enjoy your triumph!"),
  ("prisoner_released_goodnatured",   "You are indeed a {man/woman} of honour, {sir/madame}. I shall not forget this!"),
  ("prisoner_released_upstanding",    "You are indeed a {man/woman} of honour, {sir/madame}. I shall not forget this!"),

#Post 0907 changes begin
  ("enemy_meet_default",              "Who are you, that comes in arms against me?"),
  ("enemy_meet_martial",              "What is your name, {sir/madame}? If we come to blows, I would know whom I fight."),
  ("enemy_meet_quarrelsome",          "Who the hell are you?"),
  ("enemy_meet_pitiless",             "Who are you? Speak, so that I may know whom I slay."),
  ("enemy_meet_cunning",              "Tell me your name. It is always good to know your enemy."),
  ("enemy_meet_sadistic",             "Who are you? Speak quick, before I cut your tongue out."),
  ("enemy_meet_goodnatured",          "What is your name, {sir/madame}? If we come to blows, I would know whom I fight."),
  ("enemy_meet_upstanding",           "Who are you, who would come in arms to dispute our righteous cause?"),

  ("battle_won_default",              "You have proven yourself a most valued ally, today."),
  ("battle_won_martial",              "There is no greater fortune than the chance to show one's valor on the field of arms!"),
  ("battle_won_quarrelsome",          "Hah! We showed those bastards a thing or two, there, didn't we?"),
  ("battle_won_pitiless",             "Together, we will make the foe learn to fear our names, and to quail at our coming!"),
  ("battle_won_cunning",              "Now, we must be sure to press our advantage, so that the blood shed today is not wasted."),
  ("battle_won_sadistic",             "Now let us strip their dead and leave them for the crows, so that all will know the fate of those who come against us."),
  ("battle_won_goodnatured",          "That was a good scrap! No joy like the joy of victory, eh?"),
  ("battle_won_upstanding",           "Now, let us give thanks to the heavens for our victory, and mourn the many fine men who have fallen today."),

  ("battle_won_grudging_default",     "You helped turn the tide on the field, today. Whatever I may think of you, I cannot fault you for your valor."),
  ("battle_won_grudging_martial",     "{playername} -- you have shown yourself a worthy {man/woman} today, whatever your misdeeds in the past."),
  ("battle_won_grudging_quarrelsome", "Hmf. Yours is not a face which I normally like to see, but I suppose today I should thank you for your help."),
  ("battle_won_grudging_pitiless",    "Your help was most valuable today. I would not imagine that you came to help me out of kindness, but I nonetheless thank you."),
  ("battle_won_grudging_cunning",     "It would be unwise of me not to thank you for coming to help me in my hour of need. So... You have my gratitude."),
  ("battle_won_grudging_sadistic",    "Well! How touching! {playername} has come to rescue me."),
  ("battle_won_grudging_goodnatured", "{playername}! I can't say that we've always gotten along in the past, but you fought well today. My thanks to you!"),
  ("battle_won_grudging_upstanding",  "Perhaps I was wrong about you. Your arrival was most timely. You have my gratitude."),

  ("battle_won_unfriendly_default",         "So you're here. Well, better late than never, I suppose."),
  ("battle_won_unfriendly_martial",         "We have hard harsh words in the past, but for now let us simply enjoy our victory."),
  ("battle_won_unfriendly_quarrelsome",     "If you're standing there waiting for thanks, you can keep waiting. Your help wasn't really needed, but I guess you had nothing better to do, right?"),
  ("battle_won_unfriendly_pitiless",        "You have come here, like a jackal to a lion's kill. Very well then, help yourself to the spoils. I shall not stop you."),
  ("battle_won_unfriendly_cunning",         "{playername}... Well, I suppose your arrival didn't hurt, although I won't pretend that I'm happy to see you."),
  ("battle_won_unfriendly_sadistic",        "Back off, carrion fowl! This was my victory, however hard you try to steal the glory for yourself."),
  ("battle_won_unfriendly_goodnatured",     "Oh, it's you. Well, I suppose I should thank you for your help."),
  ("battle_won_unfriendly_upstanding",      "Thank you for coming to my support. Now I will be off, before I say something that I regret."),

  ("troop_train_request_default",               "I need someone like you to knock them into shape."),
  ("troop_train_request_martial",               "They need someone to show them the meaning of valor."),
  ("troop_train_request_quarrelsome",           "Fat lazy bastards. They make me puke."),
  ("troop_train_request_pitiless",              "They are more afraid of the enemy than they are of me, and this will not do."),
  ("troop_train_request_cunning",               "But men, like swords, are tempered and hardened by fire."),
  ("troop_train_request_sadistic",              "They need someone with steel in his back to flog some courage into them, or kill them trying."),
  ("troop_train_request_goodnatured",           "They're good enough lads, but I am afraid that they are not quite ready for a battle just yet."),
  ("troop_train_request_upstanding",            "It would be tantamount to murder for me to lead them into combat in their current state."),

  ("unprovoked_attack_default",               "What? Why do you attack us? Speak, you rascal!"),
  ("unprovoked_attack_martial",               "I have no objection to a trial of arms, but I would ask you for what reason you attack us?"),
  ("unprovoked_attack_quarrelsome",           "You're making a big mistake, {boy/girl}. What do you think you're doing?"),
  ("unprovoked_attack_pitiless",              "Indeed? If you really want to die today, I'd be more than happy to oblige you, but I am curious as to what you hope to accomplish."),
  ("unprovoked_attack_cunning",               "Really? I think that you are acting most unwisely. What do you hope to gain by this?"),
  ("unprovoked_attack_sadistic",              "What's this? Do you enjoy having your eyes put out?"),
  ("unprovoked_attack_goodnatured",           "Why do you do this? We've got no quarrel, {sir/madame}."),
  ("unprovoked_attack_upstanding",            "I consider this an unprovoked assault, and will protest to your king. Why do you do this?"),

  ("unnecessary_attack_default",               "I will not hesitate to cut you down if pressed, but I will offer you the chance to ride away from this."),
  ("unnecessary_attack_martial",               "I am eager to take you up on your challenge, {sir/madame}, although I will give you a minute to reconsider."),
  ("unnecessary_attack_quarrelsome",           "Bah! I'm in no mood for this nonsense today. Get out of my way."),
  ("unnecessary_attack_pitiless",              "I am in a merciful mood today. I will pretend that I did not hear you."),
  ("unnecessary_attack_cunning",               "I don't see what you have to gain by making an enemy of me. Maybe you should just ride away."),
  ("unnecessary_attack_sadistic",              "I have no time to waste on a worm like you. Get out of my way."),
  ("unnecessary_attack_goodnatured",           "I don't see what you have to gain by picking a fight, {sir/madame}. You can still ride away."),
  ("unnecessary_attack_upstanding",            "If a fight is what you wish, {sir/madame}, then you will have one, but I will yet offer you the chance to back down."),

  ("lord_challenged_default",                   "As you wish. Prepare to die!"),
  ("lord_challenged_martial",                   "So be it. Defend yourself!"),
  ("lord_challenged_quarrelsome",               "You impudent whelp! I'll crush you!"),
  ("lord_challenged_pitiless",                  "If you so badly wish to die, then I have no choice but to oblige you."),
  ("lord_challenged_cunning",                   "Well, if you leave me no choice..."),
  ("lord_challenged_sadistic",                  "You heap of filth! I'll make you wish you'd never been born."),
  ("lord_challenged_goodnatured",               "Very well. I had hoped that we might avoid coming to blows, but I see that have no choice."),
  ("lord_challenged_upstanding",                "So be it. It saddens me that you cannot be made to see reason."),

  ("lord_mission_failed_default",               "Well, I am disappointed, but I am sure that you will have many chances to redeem yourself."),
  ("lord_mission_failed_martial",               "There is no honour in failing a quest which you endeavoured to take, but I will accept your word on it."),
  ("lord_mission_failed_quarrelsome",           "You failed? Bah. I should have expected as much from the likes of you."),
  ("lord_mission_failed_pitiless",              "You failed? Well. You disappoint me. That is a most unwise thing to do."),
  ("lord_mission_failed_cunning",               "Well, I am disappointed, but no one can guarantee that the winds of fortune will always blow their way."),
  ("lord_mission_failed_sadistic",              "Indeed? Those who fail me do not always live to regret it."),
  ("lord_mission_failed_goodnatured",           "Oh well. It was a long shot, anyway. Thank you for making an effort."),
  ("lord_mission_failed_upstanding",            "Very well. I am sure that you gave it your best effort."),

  ("lord_follow_refusal_default",       "Follow you? You forget your station, {sir/madame}."),
  ("lord_follow_refusal_martial",       "Perhaps if you one day prove yourself a valorous and honourable warrior, then I would follow you. But not today."),
  ("lord_follow_refusal_quarrelsome",   "Follow someone like you? I don't think so."),
  ("lord_follow_refusal_pitiless",      "Lords like me do not follow people like you, {sir/madame}."),
  ("lord_follow_refusal_cunning",       "First show me that you are the type of {man/woman} who will not lead me into disaster, and then perhaps I will follow you."),
  ("lord_follow_refusal_sadistic",      "I think not! Rather, you should follow me, as a whipped cur follows {his/her} master."),
  ("lord_follow_refusal_goodnatured",   "Um, I am a bit pressed with errands right now. Perhaps at a later date."),
  ("lord_follow_refusal_upstanding",    "First show me that you are worthy to lead, and then perhaps I will follow."),



  ("lord_insult_default",               "base varlot"),
  ("lord_insult_martial",               "dishonourable knave"),
  ("lord_insult_quarrelsome",           "filth-swilling bastard"),
  ("lord_insult_pitiless",              "low-born worm"),
  ("lord_insult_cunning",               "careless oaf"),
  ("lord_insult_sadistic",              "sniveling cur"),
  ("lord_insult_goodnatured",           "unpleasant fellow"),
  ("lord_insult_upstanding",            "disgraceful scoundrel"),


  ("lord_derogatory_default",               "base and vile"),
  ("lord_derogatory_martial",               "bullheaded"),
  ("lord_derogatory_quarrelsome",           "quarrelsome and divisive"),
  ("lord_derogatory_pitiless",              "cruel, tyrannical"),
  ("lord_derogatory_cunning",               "unscrupulous and manipulative"),
  ("lord_derogatory_sadistic",              "vile and dishonorable"),
  ("lord_derogatory_goodnatured",           "hopelessly naive"),
  ("lord_derogatory_upstanding",            "stiffnecked and sanctimonious"),

  ("lord_derogatory_result",                "bring us to ruin"),
  ("lord_derogatory_martial_action",        "attack the enemy without thought or plan, and throw away the lives of your men"),
  ("lord_derogatory_quarrelsome_action",    "pick fights with other lords, leaving us divided and weak"),
  ("lord_derogatory_pitiles_action",        "alienate the commons, provoking revolt and mutiny"),
  ("lord_derogatory_cunning_action",        "cut a deal with the enemy behind our back"),
  ("lord_derogatory_sadistic_action",       "bring shame upon our cause and our realm"),
  ("lord_derogatory_goodnatured_action",    "take pity on our enemies, rather than fight them"),
  ("lord_derogatory_upstanding_action",     "place your own exaggerated sense of honor above the needs of the realm"),



  #SB : gender strings - reg4 as current liege, reg3 as proposed liege
  ("rebellion_dilemma_default",                 "{!}[liege]"),
  ("rebellion_dilemma_martial",                 "{s45} was clearly wronged. Although I gave an oath to {s46}, it does not bind me to support {reg4?her:him} if {reg4?she:he} usurped the throne illegally."),
  ("rebellion_dilemma_quarrelsome",             "Hmm. {s46} has never given me my due, so I don't figure I owe him much. However, maybe {s45} will be no better, and {s46} has at least shown {reg4?her:him}self."),
  ("rebellion_dilemma_pitiless",                "Hmm. {s45} says {reg3?she:he} is the rightful heir to the throne. That is good -- it absolves me of my oath to {s46}. But still I must weight my decision carefully."),
  ("rebellion_dilemma_cunning",                 "Hmm. I gave an oath of homage to {s46}, yet the powerful are not bound by their oaths as our ordinary people. Our duty is to our own ability to rule, to impose order and prevent the war of all against all."),
  ("rebellion_dilemma_sadistic",                "Hmm. In this vile world, a wise {reg65?woman:man} must think of {reg65?her:him}self, for no one else will. So -- what's in it for me?"),
  ("rebellion_dilemma_goodnatured",             "I do not know what to say. I gave an oath to {s46} as the lawful ruler, but if he is not the lawful ruler, I don't know if I am still bound."),
  ("rebellion_dilemma_upstanding",              "This is troublesome. It is a grave thing to declare my homage to {s46} to be null and void, and dissolve the bonds which keep our land from sinking into anarchy. Yet I am also pledged to support the legitimacy of the succession, and {s45} also has a valid claim to the throne."),

  ("rebellion_dilemma_2_default",               "{!}[liege]"),
  ("rebellion_dilemma_2_martial",               "On the other hand, {s46} has led us in war and peace, and I am loathe to renounce my allegiance."),
  ("rebellion_dilemma_2_quarrelsome",           "So tell me, why should I turn my back on the {reg4?bitch:bastard} I know, in favor of {reg3?a woman:the bastard} I don't know?"),
  ("rebellion_dilemma_2_pitiless",              "It is a most perilous position to be in, to be asked whom I would make {reg3?ruler:king} of this land. Yet it is also a time of opportunity, for me to reap the rewards that have always been my due!"),
  ("rebellion_dilemma_2_cunning",               "{s46} has been challenged, and thus {reg4?she:he} will never be able to rule as strongly as one whose claim has never been questioned. Yet if {s45} takes the throne by force, {reg3?she:he} will not be as strong as one who succeeded peacefully."),
  ("rebellion_dilemma_2_sadistic",              "Perhaps if I join {s45} while {reg3?she:he} is still weak {reg3?she:he} will enrich me, but perhaps if I bring {s46} your head {reg4?she:he} will give me an even greater reward."),
  ("rebellion_dilemma_2_goodnatured",           "{s46} has always treated me decently, yet it's true that {reg4?she:he} did wrong to {s45}. I hesitate to renounce my homage to {s46}, yet I also don't think it's right to support injustice."),
  ("rebellion_dilemma_2_upstanding",            "I feel that I must do whatever is best for the realm, to avoid it being laid waste by civil war and ravaged by its enemies."),


  ("political_philosophy_default",               "{!}[liege]"),
  ("political_philosophy_martial",               "My sword is at the disposal of my rightful liege, so long as he upholds his duty to me."),
  ("political_philosophy_quarrelsome",           "Bah. They're all a bunch of bastards. I try to make sure that the ones who wrong me learn to regret it."),
  ("political_philosophy_pitiless",              "Men will always try to cheat others of their rightful due. In this faithless world, each must remain vigilant of his own rights."),
  ("political_philosophy_cunning",               "Well, it's a harsh world, and it is our lot to face harsh choices. Sometimes one must serve a tyrant to keep the peace, but sometimes a bit of rebellion keeps the kings honest. Circumstance is all."),
  ("political_philosophy_sadistic",              "My philosophy is simple: it is better to be the wolf than the lamb."),
  ("political_philosophy_goodnatured",           "Well, you should keep faith with your promises, and not do injustice to others. Sometimes it's hard to balance those. Stick with people you trust, I think, and it's hard to go far wrong."),
  ("political_philosophy_upstanding",            "Kingship and lordship have been instituted to keep the peace and prevent the war of all against all, yet that must not blind us to the possibility of injustice."),
  ("political_philosophy_roguish",               "Hmm.. I guess I'm thinking that it's good to be a lord."),
  ("political_philosophy_benefactor",            "A good ruler makes sure all are treated justly. Personally, I intend to use my authority to better the lot of those who live in my demesne."),
  ("political_philosophy_custodian",             "A good ruler creates the proper conditions for people to prosper. Personally, I intend to use my wealth to create more wealth, for myself and for the common benefit."),



  ("rebellion_prior_argument_very_favorable",   "I have already heard some arguments for supporting your candidate for the throne, and I tend to agree with them."),
  ("rebellion_prior_argument_favorable",        "I have already heard some arguments for supporting your candidate for the throne, and I tend to agree with them."),
  ("rebellion_prior_argument_unfavorable",      "I have already heard some arguments for supporting your candidate for the throne, but I do not find them convincing."),
  ("rebellion_prior_argument_very_unfavorable", "I have already heard some arguments for supporting your candidate for the throne, but I disagree with most of them."),

  ("rebellion_rival_default",                   "{!}[liege]"),
  ("rebellion_rival_martial",                   "{s49} your ally {s44} once questioned my honour and my bravery. It's not often I get the chance to face him in battle, and make him retract his statement."),
  ("rebellion_rival_quarrelsome",               "{s49} you're working with {s44}. He's a crafty weasel, and I don't trust him one bit."),
  ("rebellion_rival_pitiless",                  "{s49} you seem to have enlisted the support of {s44} -- who is soft, and weak, and not fit to govern a fief, and whom I have always detested."),
  ("rebellion_rival_cunning",                   "{s49} {s44}, who has already joined you, is headstrong and quarrelsome, and a bit of liability."),
  ("rebellion_rival_sadistic",                  "{s49} I have no desire to fight alongside your ally {s44}, who puts on such a nauseating display of virtue."),
  ("rebellion_rival_goodnatured",               "{s49} I'd be reluctant to be on the same side as {s44}, who has quite a reputation for cruelty."),
  ("rebellion_rival_upstanding",                "{s49} your ally {s44} is in my opinion a dangerous, unreliable, and highly unprincipled man."),

  ("rebellion_argument_favorable",              "I respect your line of argument"),
  ("rebellion_argument_neutral",                "I find your line of argument only moderately compelling"),
  ("rebellion_argument_unfavorable",            "I do not find your line of argument compelling"),

  ("rebellion_persuasion_favorable",            "you state your case eloquently"),
  ("rebellion_persuasion_neutral",              "you make a reasonable case"),
  ("rebellion_persuasion_unfavorable",          "you make an unconvincing case"),

  ("rebellion_relation_very_favorable",         "I have the greatest respect for you personally."),
  ("rebellion_relation_favorable",              "I know and respect you personally."),
  ("rebellion_relation_neutral",                "I do not know you as well as I might like."),
  ("rebellion_relation_unfavorable",            "I do not trust you."),

  ("and_comma_3", "Furthermore, "),
  ("but_comma_3", "However,"),

  ("and_comma_1", ", and "),
  ("but_comma_1", ", but "),

  ("and_comma_2", ". Moreover, "),
  ("but_comma_2", ". Nonetheless, "),

  ("rebellion_agree_default",               "Very well -- I am ready to pledge myself to {s45} as my {reg3?queen:king}."),
  ("rebellion_agree_martial",               "I have decided. I will back {s45} as the rightful heir."),
  ("rebellion_agree_quarrelsome",           "Ahh, I've thought long enough. I never did like {s46} much anyway. Let's go take his throne away from {reg4?her:him}."),
  ("rebellion_agree_pitiless",              "You are fortunate. I have decided to join your cause. Pray do not give me cause to regret this decision."),
  ("rebellion_agree_cunning",               "This is a most dangerous decision, but after careful consideration, I have decided that I will join you. Let's hope it is for the best."),
  ("rebellion_agree_sadistic",              "Well then. I will back {reg5?you:your {reg3?woman:man} {s45}}. But you'd best make sure that {reg5?I'm rewarded:{reg3?she:he} rewards me} well!"),
  ("rebellion_agree_goodnatured",           "All right. I think {reg5?you:your {reg3?woman:man}} will be a good ruler. I'll be part of your cause."),
  #SB : remove "so be it" since it's used in subsequent strings to avoid awkwardness
  ("rebellion_agree_upstanding",            "May the Heavens forgive me if I do wrong. My first duty is to this realm, and to save it from lawlessness I will back {s45} and renounce my homage to {s46}."),


  #SB : fix some identifiers
  ("rebellion_refuse_default",              "{!}[liege]"),
  ("rebellion_refuse_martial",              "I am sorry. {s45} has a good claim, but it's not enough for me to turn my back on {s46}. I will remain loyal to my liege."),
  ("rebellion_refuse_quarrelsome",          "Nah. Your whelp {s45} doesn't have what it takes to rule this realm. I'm sticking with {s46}."),
  ("rebellion_refuse_pitiless",              "No. I will not join your rebellion. I count it little more than the tantrum of a child, denied a bauble which {reg3?she:he} thinks should be {reg3?hers:his}. I will stick with {s46}, whose ability to rule is well-tested."),
  ("rebellion_refuse_cunning",               "I am sorry. You do not give me reason for confidence that you will win. Many will die, but I do not wish to be among them. I will continue to back {s46}."),
  ("rebellion_refuse_sadistic",              "No. I won't play your little game. You grasp at a crown, but I think instead you'll get a quick trip to the scaffold, and I'll be there by {s46}'s side to watch the headsman's axe drop."),
  ("rebellion_refuse_goodnatured",           "I am sorry. I don't feel right turning my back on {s46}. No hard feelings when me meet on the battlefield."),
  ("rebellion_refuse_upstanding",            "I am sorry. {s45}'s claim is not strong enough for me to inflict the curse of civil disorder on the poor wretches of this land. I will continue to back {s46}. May the Heavens forgive me if I do wrong."),

  ("talk_later_default",                    "{!}[liege]"),
  ("talk_later_martial",                    "Now is not the time to talk politics! I am here today with my fellow lords, armed for battle. You'd better prepare to fight."),
  ("talk_later_quarrelsome",                "Do you expect me to discuss betraying my liege with you, while we are surrounded by his army? What do you take me for, a bloody idiot?"),
  ("talk_later_pitiless",                   "Still your tongue! Whatever I have to say on this matter, I will not say it here and now, while we are in the midst of our army."),
  ("talk_later_cunning",                    "This is hardly the time or the place for such a discussion. Perhaps we can discuss it at a later time and a different place, but for now we're still foes."),
  ("talk_later_sadistic",                   "You should have your mouth sewn shut! Can you imagine what would happen if the other vassals see me talking to you of treason?"),
  ("talk_later_goodnatured",                "So you wish to discuss your rebellion with me? Try that again when we aren't surrounded by my liege's army, and I will hear what you have to say."),
  ("talk_later_upstanding",                 "Whatever my thoughts on the legitimacy of the succession, I am not about to discuss them here and now. If we meet again when we can talk in privacy, I will hear what you have to say on the matter. But for now, consider me your enemy."),

  ("npc_claim_throne_liege",                    "{!}[placeholder - i am already king]"),
  ("npc_claim_throne_liege_martial",            "{!}[it is my right by birth]."),
  ("npc_claim_throne_liege_quarrelsome",        "{!}[in this life, you take power when you can get it]"),
  ("npc_claim_throne_liege_pitiless",           "{!}[it is my right by birth]."),
  ("npc_claim_throne_liege_cunning",            "{!}[i suppose there comes a time in a man's life when you should grasp at a crown, as you'll always regret not doing it]."),
  ("npc_claim_throne_liege_sadistic",           "{!}[i will show those who despise me]."),
  ("npc_claim_throne_liege_goodnatured",        "{!}[if you really think that i have the best claim]."),
  ("npc_claim_throne_liege_upstanding",         "{!}[i could do much good]."),
#


##diplomacy start+ Change the next line
#  ("gossip_about_character_default",        "They say that {s6} doesn't possess any interesting character traits."),
  ("gossip_about_character_default",        "There aren't many recent rumors about {s6}'s personal life."),
##diplomacy end+
  ("gossip_about_character_martial",        "They say that {s6} loves nothing more than war."),
  ##diplomacy start+ make pronouns gender-correct (reg4)
  ("gossip_about_character_quarrelsome",    "They say that {s6} almost came to blows with another lord lately, because the man made a joke about {reg4?her:his} nose."),
  ("gossip_about_character_selfrighteous",  "I heard that {s6} had a retainer executed because the unfortunate man killed a deer in {reg4?her:his} forest."),
  ("gossip_about_character_cunning",        "They say that {s6} is a cunning opponent."),
  ("gossip_about_character_sadistic",       "They say that {s6} likes to torture {reg4?her:his} enemies. I wouldn't want to get on the bad side of that {reg4?woman:man}."),
  ("gossip_about_character_goodnatured",    "They say that {s6} is a good {reg4?woman:man} and treats people living in {reg4?her:his} lands decently. That is more than what can be said for most of the nobles."),
  ("gossip_about_character_upstanding",     "People say that it is good to be in the service of {s6}. {reg4?She:He} is good to {reg4?her:his} followers, and rewards them if they work well."),
  ##diplomacy end+
  ("latest_rumor",        "The latest rumor you heard about {s6} was:"),





#steve lord recruitment changes begin
  ("changed_my_mind_default",                   "{!}[liege]"),
  ("changed_my_mind_martial",                   "However, your stirring words make me reconsider my position."),
  ("changed_my_mind_quarrelsome",               "But I think you've talked me into it anyway, you bastard. I'm still listening"),
  ("changed_my_mind_pitiless",                  "But when you plea like that, I will deign to reconsider."),
  ("changed_my_mind_cunning",                   "But you know, you're a well-spoken bastard. That impresses me. I'm still listening."),
  ("changed_my_mind_sadistic",                  "But as your silver tongue sings so pretty a song on your behalf, I will not dismiss the idea just yet."),
  ("changed_my_mind_goodnatured",               "But you make a good case, so I'll try to keep an open mind."),
  ("changed_my_mind_upstanding",                "However, you make an eloquent case. I am still listening."),
#steve lord recruitment changes end

#steve post 0912 changes begin

  ("swadian_rebellion_pretender_intro",    "I am Libius Severus, rightful ruler of the Western Roman Empire."),
  ("vaegir_rebellion_pretender_intro",     "My name is My name is Iulius Patricius, son of the renowned Aspar, Magister Militum of the Eastern Roman Empire, true ruler of the Romans of the east."),
  ("khergit_rebellion_pretender_intro",    "I am Euric, rightful king of the Visigoths"),
  ("nord_rebellion_pretender_intro",       "I am Odoin, rightful ruler of the Ostrogoths."),
  ("rhodok_rebellion_pretender_intro",     "I am Lord Kastor, the rightful King of the Rhodoks, who will free them from tyranny."),
  ("sarranid_rebellion_pretender_intro",   "I am Peroz, brother of Hormizd and rightful Shahanshah of Eranshahr."),



  ("swadian_rebellion_pretender_story_1",  "I am a senator from Lucania and patrician of Rome."),
  ("vaegir_rebellion_pretender_story_1",   "I am of Alanic-Gothic descent, like my father, Aspar, who is the most powerful patrician in the Eastern empire! He gave me this roman name so I may become Emperor!"),
  ("khergit_rebellion_pretender_story_1",  "Theodoric II and I are brothers, some of the few sons of the great Theodoric I. We all fought along side him against Attila at the battle of the Catalaunian Plains, where he died in battle."),
  ("nord_rebellion_pretender_story_1",     "I am called the Odoin because I have travelled great distances, even by the standards of us, migrating folks, in search of knowledge. Before I came of age, my father sent me abroad on a tour of study at the courts and universities in the lands overseas. If the Germans are to call themselves the heirs of the Empire, then they must act the part, and know something of law and letters, and not call themselves content merely to fight, plunder, and drink."),
  ("rhodok_rebellion_pretender_story_1",   "The Rhodoks are a free people, and not slaves to any hereditary monarch. The king must be chosen from one of the leading noble families of the land, by a council drawn by lot from the patricians of the cities of Jelkala, Veluca, and Yalen. The council meets on a field before Jelkala, and no man is allowed to appear in arms during their deliberations, on pain of death."),
  ("sarranid_rebellion_pretender_story_1", "I am one of the sons of former Shahanshah, Yazdegerd II. I was always considered my father's favorite, and was the next in line for the throne."),

  ("swadian_rebellion_pretender_story_2",  "The current emperor is a result of the murder of the previous, Eparchius Avitus and was only given power by the military."),
  ("vaegir_rebellion_pretender_story_2",   "The current Emperor was placed on the throne by my father, due to his faith. As Arians, we are not allowed to reign as emperor, due to the church and the zealous people of Constantinople..."),
  ("khergit_rebellion_pretender_story_2",  "According to our ancient customs, the eldest son takes the throne, and after the death of our Father, my eldest brother, Thorismund took the throne. However, Theodoric murdered him in cold blood, taking the throne for himself like a tyrant!"),
  ("nord_rebellion_pretender_story_2",     "My father died however before I completed my course of study, and as I hurried home to claim his throne my ship was wrecked by a storm. One of my father's thanes, Valamir, seized this opportunity and spread rumors that I had died abroad. He summoned a gathering of his supporters to have himself proclaimed king, and has taken the past few years to consolidate his power."),
  ("rhodok_rebellion_pretender_story_2",   "During the last selection, there were but two candidates, myself, and Lord Graveth. While the council was deliberating, Graveth appeared, sword in hand, telling them that a Swadian raiding party was about to descend on the field of deliberation -- which was true, by the way -- and if he were not elected king, then he would leave them to their fate."),
  ("sarranid_rebellion_pretender_story_2", "After our father's death my older brother, Hormizd took the throne for himself at Rhagae while I was away on the frontier with the Hephthalites organizing peace, despite me being in line for the throne."),

  ("swadian_rebellion_pretender_story_3",  "The Western Empire ought to be ruled by someone with the support of the aristocracy and the people, not a military dictator."),
  ("vaegir_rebellion_pretender_story_3",   "However, unlike my father, I will convert to become Emperor, and take my place as emperor, over that lowly former tribune!"),
  ("khergit_rebellion_pretender_story_3",  "My brother thinks that us Visigoths will be Rome's puppets; Respecting their alliances and treaties and imperial titles, bah! We goths are strong warriors, and we should be independent of their rule, look, the Romans are weak, and fledgling. A perfect time to strike back! I promise to bring us to victory over the Romans again, like we did at Adrianople and Rome!"),
  ("nord_rebellion_pretender_story_3",     "So I remain in exile -- except now I am not looking for sages to tutor me in the wisdom of faraway lands, but warriors, to come with me back to the land of the Romans and regain my throne. If Valamir doubts my ability to rule, then let him say so face to face, as we stare at each other over the rims of our shields. For a warrior can be a scholar, and a scholar a warrior, and to my mind, only one who combines the two is fit to be king!"),
  ("rhodok_rebellion_pretender_story_3",   "Well, Graveth defeated the Swadians, and for that, as a Rhodok, I am grateful. When I am king, I will myself place the wreath of victory on his head. But after that I will have it separated from his shoulders, for by his actions he has shown himself a traitor to the Rhodok confederacy and its sacred custom."),
  ("sarranid_rebellion_pretender_story_3", "My brother is known to be unjust and a tyrant among the nobles. Not only do I have the support of the power Mihran family, but I also have the support of the Hephthalite king. But most important, I have the support of the people who do not wish to be ruled by an unjust tyrant. All I need is someone to help me take the throne."),

  ("swadian_rebellion_monarch_response_1", "Libius Severus believes he should be emperor?. He is right that I was placed into power by the military, but it was after I won a victory against the invading Alemmani, in which I initially refused."),
  ("vaegir_rebellion_monarch_response_1",  "Ah, Iulius Patricius, son of my most influential general and rival, Aspar... It is true that I was placed on the throne by Aspar, just as the previous emperor, Marcian was."),
  ("khergit_rebellion_monarch_response_1", "My brother Euric has perhaps told you of his insistence upon taking the throne from me, and accuses me of patricide. As if he would not be a hypocrite himself for killing me! I killed Thorismund for he violated our treaties with the Romans, who we are loyal allies for! Our father died fighting along side the Romans against those Hunnic beasts, and to think we should violate our alliances?"),
  ("nord_rebellion_monarch_response_1",    "Odoin? Bastard, is more like it. Perhaps you have heard the expression, 'Unhappy is the land whose king is a child.' Unhappy too is the land whose king is a student. You want the Goths to be ruled by a beardless youth, whose hand bears no callouses left by a sword's grip, who has never stood in a shield wall? If Odoin were king, his retainers would laugh at him to his face!"),
  ("rhodok_rebellion_monarch_response_1",  "No doubt Lord Kastor told you that I defiled the hallowed Rhodok custom by interfering with the patricians' election of a king. Well, let me tell you something. The patricians of the towns make longwinded speeches about our ancient liberties, but then choose as their king whichever noble last sat in their villa and sipped a fine wine and promised to overlook their unpaid taxes."),
  ("sarranid_rebellion_monarch_response_1", "Our scholars have long agreed that there is one overriding principle in politics, tyranny, whatever you may believe it is, is better than civil war. It was for that reason that I took the throne from my brother, whom is much more of a scholar than a warrior, and for most a ruler."),

  ("swadian_rebellion_monarch_response_2", "A corrupt senator like him would easily fall prey to the demands of the Vandals. Not only is he corrupt, but also an ally and pawn of Ricimer, the man who contests power with me, but cannot become emperor due to his barbarian heritage and arian beliefs. Now enough of this, I wish not to speak about it again."),
  ("vaegir_rebellion_monarch_response_2",  "Aspar granting me the throne does not matter. I have gained it, and that is final. If every old claim were to be brought up anew, if every man's inheritance could be called into question at any time, then it would be the end of the institution of kingship, and we would live in a state of constant civil war like the crises of old."),
  ("khergit_rebellion_monarch_response_2", "Look what our alliance has done for us. Our loyalty has given us land, power and respect. If Euric believes he will lead the kingdom as an independent ruler, he will face the consiquences of the might of the Roman army!"),
  ("nord_rebellion_monarch_response_2",    "The slavers may have had fancy ideas about how to dispose of his kingdom, but it is not just royal blood that makes a King of the Goths. I am king by acclamation of the thanes, and by right of being the strongest. That counts for more than blood, and woe to any man in this land who says otherwise."),
  ("rhodok_rebellion_monarch_response_2",  "The only liberty that concerns them is their liberty to grow fat. Meanwhile, my men sleep out on the steppe, and eat dry bread and salt fish, and scan the horizon for burning villages, and shed our blood to keep the caravan routes open. Here's an idea -- if I ever meet a merchant who limps from a Khergit arrow-wound or a Swadian sword-stroke, then I'll say, 'Here's a man whose counsel is worth taking.'"),
  ("sarranid_rebellion_monarch_response_2", "You should know, however, that supporting my brother shall lead to a civil war not only in the empire, but our family as well. This would weaken our empire, and make it vulnerable to the Romans in our west and the Hephthalites in the East. A stable empire is better than a weakened one."),

#steve post 0912 changes end

#courtship
  ("courtship_comment_conventional_generic",  "is a very well-bred sort"),
  ("courtship_comment_adventurous_generic",   "seems decent enough"),
  ("courtship_comment_otherworldly_generic",  "is most polite and attentive"),
  ("courtship_comment_ambitious_generic",     "lacks drive -- but perhaps that may be remedied"),
  ("courtship_comment_moralist_generic",      "seems to be a man of good character"),

  ("feast_description", 					  "scant"),
  ("feast_description_2", 					  "meager"),
  ("feast_description_3", 					  "barely adequate"),
  ("feast_description_4", 					  "sufficient"),
  ("feast_description_5", 					  "bountiful"),
  ("feast_description_6", 					  "magnificent"),

  ("feast_lengthy_description_1", 			  "The food you provided was insufficient for your guests and their retinues, forcing them to purchase their sustenance from the surrounding countryside at grossly inflated prices. The consensus among those who attended was that you failed to do your duty as a host, diminishing both their trust in you and your overall reputation."),
  ("feast_lengthy_description_2", 			  "The food and drink you provided eventually ran out, forcing some guests to either buy their own from passing peddlars, or send some of their retinue home early. The more charitable attributed the shortfall to poor planning rather than meanness, but either way, it did your reputation no good."),
  ("feast_lengthy_description_3", 			  "The food and drink you provided was adequate for your noble guests, although some of the commoners in their retinues went without. You are establishing a reputation as one who has at least a grasp of your social obligations as a noble."),
  ("feast_lengthy_description_4", 		      "You have provided enough food and drink, and with sufficient varieties, to do yourself credit. The food, drink, and merriment have loosened your guests tongues, allowing them to converse candidly about the matters of the realm, and deepening their trust in you."),
  ("feast_lengthy_description_5", 			  "You have provided a bountiful table not just for your noble guests but for their retinues, with food left over to be distributed to the poor. Your guests lavish praise upon you for your generosity, and for your understanding of the social obligations of your rank. The conversation, fueled by the food and drink, has been merry, strengthening the bonds between those who attended."),
  ("feast_lengthy_description_6", 			  "The realm will be speaking of the bounty of your table for months to come, and it will become the standard to which all other feasts will aspire. You have filled the bellies not just of your noble guests and their retinues, but also of the poor who flocked to the gates. "),


  ("kingdom_1_adjective",                     "Roman"),
  ("kingdom_2_adjective",                     "Roman"),
  ("kingdom_3_adjective",                     "Visigothic"),
  ("kingdom_4_adjective",                     "Ostrogothic"),
  ("kingdom_5_adjective",                     "Pictish"),
  ("kingdom_6_adjective",                     "Sassanid"),
  ("kingdom_7_adjective",                     "Salian"),
  ("kingdom_8_adjective",                     "Suebian"),
  ("kingdom_9_adjective",                     "Burgundian"),
  ("kingdom_10_adjective",                     "Alemanni"),
  ("kingdom_11_adjective",                     "Gepid"),
  ("kingdom_12_adjective",                     "Saxon"),
  ("kingdom_13_adjective",                     "Romano-British"),
  ("kingdom_14_adjective",                     "Roman"),
  ("kingdom_15_adjective",                     "Vandal"),
  ("kingdom_16_adjective",                     "Iberian"),
  ("kingdom_17_adjective",                     "Langobard"),
  ("kingdom_18_adjective",                     "Thuringian"),
  ("kingdom_19_adjective",                     "Jute"),
  ("kingdom_20_adjective",                     "Ripaurian"),
  ("kingdom_21_adjective",                     "Scirian"),
  ("kingdom_22_adjective",                     "Romano-Mauri"),
  ("kingdom_23_adjective",                     "Hunnic"),
  ("kingdom_24_adjective",                     "Lazikan"),
  ("kingdom_25_adjective",                     "Nubian"),
  ("kingdom_26_adjective",                     "Nubian"),
  ("kingdom_27_adjective",                     "Alan"),
  ("kingdom_28_adjective",                     "Aghwan"),
  ("kingdom_29_adjective",                     "Angle"),
  ("kingdom_31_adjective",                     "Armenian"),
  ("kingdom_32_adjective",                     "Irish"),
  ("kingdom_33_adjective",                     "Sporoi"),
  ("kingdom_34_adjective",                     "Venedi"),

  ("credits_1", "Mount&Blade: Warband Copyright 2008-2015 Taleworlds Entertainment"),
  ("credits_2", "Game design:^Armagan Yavuz^Steve Negus^Cem Cimenbicer"),
  ("credits_3", "Programming:^Armagan Yavuz^Cem Cimenbicer^Serdar Kocdemir^Ozan Gumus^Mustafa Korkmaz^^Additional Programming:^Gokhan Uras^M. Furkan Yilmaz"),
  ("credits_4", "CG Artists:^Ozgur Saral^Mustafa Ozturk^Pinar Cekic^Ozan Unlu^Yigit Savtur^Umit Singil"),
  ("credits_5", "Concept Artist:^Ganbat Badamkhand"),
  ("credits_6", "Writing:^Steve Negus^Armagan Yavuz^Ryan A. Span"),
  ("credits_7", "Original Music:^Jesse Hopkins"),
  ("credits_8", "Voice Talent:^Tassilo Egloffstein"),
  ("credits_9", "This game has been supported by The Scientific and Technological Research Council of Turkey.^^\
Tutorial written by:^Steve Negus^Armagan Yavuz^Edward Spoerl^^\
Horse Motion Capture Animation Supplied by:^Richard Widgery & Kinetic Impulse^^\
Physics:^Havok^^\
Sound and Music Program Library:^FMODex Sound System by Firelight Technologies^^\
Skybox Textures:^Jay Weston^^\
Chinese Translation:^Hetairoi; Gaodatailang; silentjealousy; Ginn; fallout13; James; D.Kaede; Kan2; alixyang; muyiboy^^\
TaleWorlds Director of Communications:^Ali Erkin^^\
TaleWorlds Forum Programming:^Brett Flannigan ^^^\
TaleWorlds.com Forum Administrators and Moderators:^\
Janus^\
Archonsod^\
Narcissus^\
Nairagorn^\
Lost Lamb^\
Deus Ex^\
Merentha^\
Volkier^\
Instag0^\
Ativan^\
ego^\
Guspav^\
Hallequin^\
Invictus^\
okiN^\
Raz^\
rejenorst^\
Skyrage^\
ThVaz^^^\
Mount&Blade Community Suggestions and Feedback:^\
A_Mustang^\
adamlug^\
Adorno^\
alden^\
Alhanalem^\
amade^\
Anthallas^\
Alkhadias Master^\
Arch3r^\
Archevious^\
Arcas Nebun^\
Arcon^\
Arcturus^\
ares007^\
Arjihad^\
BadabombadaBang^\
Badun^\
BaronAsh^\
Berserker Pride^\
bgfan^\
bierdopjeee^\
Big_Mac^\
Binboy^\
blink180heights^\
BlodsHammar^\
Bloid^\
Brandon^\
Brego^\
chenjielian^\
cifre^\
COGlory^\
Corinthian Hoplite^\
Crazed Rabbit^\
CryptoCactus^\
CtrlAltDe1337^\
Cuther^\
Da-V-Man^\
dimitrischris^\
dstemmer^\
EasyCo506^\
Egbert^\
ethneldryt^\
eudaimondaimon^\
Faranox^\
Fawzia dokhtar-i-Sanjar^\
Fei Dao^\
Gabeed^\
GeN76^\
General_Hospital^\
GhosTR^\
glustrod^\
Gubbo^\
guspav^\
Halcyon^\
Harn^\
Hethwill^\
Highelfwarrior^\
HULKSMASH^\
Iberon^\
ignoble^\
Jack_Merchantson^\
JoG^\
Jov^\
Kazzan^\
King Jonathan the Great^\
Kleidophoros^\
knight^\
Kong Burger^\
Kristiania^\
l3asu^\
Larkraxm^\
Leandro1021DX^\
lighthaze^\
Llew2^\
Lord Rich^\
lordum_ediz^\
Lucke189^\
Mabons^\
MacPharlan^\
Madnes5^\
MagicMaster^\
Makh^\
ManiK^\
Manitas^\
Marin Peace Bringer^\
Martinet^\
MAXHARDMAN^\
Merlkir^\
miguel8500^\
Mithras^\
Moddan^\
Nate^\
Nemeo^\
Nite/m4re^\
noobalicous^\
Nord Champion^\
okiN^\
Orion^\
OTuphlos^\
Papa Lazarou^\
Phallas^\
Plazek^\
Prcin^\
PSYCHO78^\
PsykoOps^\
Reapy^\
Red River^\
Rhizobium^\
Riggea^\
Rongar^\
Ros^\
sadnhappy^\
Sarejo^\
ScientiaExcelsa^\
Scorch!^\
Seawied86^\
sebal87^\
shikamaru 1993^\
Shun^\
silentdawn^\
Sir Gowe^\
Skyrage^\
Slawomir of Aaarrghh^\
SoloSebo^\
SovietSoldier^\
Stabbing Hobo^\
Stratigos001^\
Styo^\
TalonAquila^\
test^\
The Yogi^\
Thundertrod^\
Thyr^\
Tim^\
Titanshoe^\
tmos^\
Toffey^\
Tonttu^\
Trenalok^\
Tronde^\
UberWiggett^\
Urist^\
Ursca^\
urtzi^\
Vermin^\
Viajero^\
Vincenzo^\
Vulkan^\
Warcat92^\
Welcome_To_Hell^\
Wheem^\
Wu-long^\
Yellonet^\
Yobbo^\
Yoshi Murasaki^\
Yoshiboy^\
Zyconnic^^^\
Special Thanks to Toby Lee for his ideas and in depth feedback on the combat system.^\
...and many many other wonderful Mount&Blade players!^^\
(This is only a small sample of all the players who have contributed to the game by providing suggestions and feedback.^\
This list has been compiled by sampling only a few threads in the Taleworlds Forums.^\
Unfortunately compiling an exhaustive list is almost impossible.^\
We apologize sincerely if you contributed your suggestions and feedback but were not listed here, and please know that we are grateful to you all the same...)\
"),
  ("credits_10", "Paradox Interactive^^President and CEO:^Theodore Bergqvist^^Executive Vice President:^Fredrik Wester\
^^Chief Financial Officer:^Lena Eriksson^^Finance & Accounting:^Annlouise Larsson^^VP Sales & Marketing US:^Reena M. Miranda\
^^VP Sales & Marketing EU:^Martin Sirc^^Distribution Manager Nordic:^Erik Helmfridsson^^Director of PR & Marketing:^Susana Meza\
^^PR & Marketing:^Sofia Forsgren^^Product Manager:^Boel Bermann\
"),
  ("credits_11", "Logotype:^Jason Brown^^Cover Art:^Piotr Fox Wysocki\
^^Layout:^Christian Sabe^Melina Grundel^^Poster:^Piotr Fox Wysocki^^Map & Concept Art:^Ganbat Badamkhand\
^^Manual Editing:^Digital Wordsmithing: Ryan Newman, Nick Stewart^^Web:^Martin Ericsson^^Marketing Assets:^2Coats\
^^Localization:^S&H Entertainment Localization^^GamersGate:^Ulf Hedblom^Andreas Pousette^Martin Ericson^Christoffer Lindberg\
"),
  ("credits_12", "Thanks to all of our partners worldwide, in particular long-term partners:\
^Koch Media (Germany & UK)^Blue Label (Italy & France)^Friendware (Spain)^New Era Interactive Media Co. Ltd. (Asia)\
^Snowball (Russia)^Pinnacle (UK)^Porto Editora (Portugal)^Hell-Tech (Greece)^CD Projekt (Poland, Czech Republic, Slovakia & Hungary)\
^Paradox Scandinavian Distribution (Scandinavia)\
"),

#### Warband added texts

#multiplayer scene names
  ("multi_scene_1", "Ruins"),
  ("multi_scene_2", "Village"),
  ("multi_scene_3", "Hailes Castle"), #Castle 1
  ("multi_scene_4", "Ruined Fort"),
  ("multi_scene_5", "Scene 5"), #not ready yet
  ("multi_scene_6", "Scene 6"), #not ready yet
  ("multi_scene_7", "Field by the River"),
  ("multi_scene_8", "Rudkhan Castle"), #Castle 2
  ("multi_scene_9", "Snowy Village"),
  ("multi_scene_10", "Turin Castle"), #Castle 3
  ("multi_scene_11", "Nord Town"),
  ("multi_scene_16", "Port Assault"),
  ("multi_scene_17", "Brunwud Castle"), #Castle 4
  ("multi_scene_18", "Battle on Ice"),
  ("multi_scene_19", "Mahdaar Castle"), #Castle 5
  ("multi_scene_20", "Jameyyed Castle"), #Castle 6
  ("multi_scene_21", "The Arena"),
  ("multi_scene_22", "Forest Hideout"),
  ("multi_scene_23", "Canyon"),
  ("multi_scene_24", "Desert Town"),
  #INVASION MODE START
  # ("multi_scene_25", "Cold Coast"),
  #INVASION MODE END
  ("multi_scene_12", "Random Plains (Medium)"),
  ("multi_scene_13", "Random Plains (Large)"),
  ("multi_scene_14", "Random Steppe (Medium)"),
  ("multi_scene_15", "Random Steppe (Large)"),
  ("multi_scene_end", "multi_scene_end"),

#multiplayer game type names
  ("multi_game_type_1", "Deathmatch"),
  ("multi_game_type_2", "Team Deathmatch"),
  ("multi_game_type_3", "Battle"),
  ("multi_game_type_4", "Fight and Destroy"),
  ("multi_game_type_5", "Capture the Flag"),
  ("multi_game_type_6", "Conquest"),
  ("multi_game_type_7", "Siege"),
  ("multi_game_type_8", "Duel"),
  ("multi_game_types_end", "Invasion"),

  ("poll_kick_player_s1_by_s0", "{s0} started a poll to kick player {s1}."),
  ("poll_ban_player_s1_by_s0", "{s0} started a poll to ban player {s1}."),
  ("poll_change_map_to_s1_by_s0", "{s0} started a poll to change map to {s1}."),
  ("poll_change_map_to_s1_and_factions_to_s2_and_s3_by_s0", "{s0} started a poll to change map to {s1} and factions to {s2} and {s3}."),
  ("poll_change_number_of_bots_to_reg0_and_reg1_by_s0", "{s0} started a poll to change bot counts to {reg0} and {reg1}."),

  ("poll_kick_player", "Poll to kick player {s0}: 1 = Accept, 2 = Decline"),
  ("poll_ban_player", "Poll to ban player {s0}: 1 = Accept, 2 = Decline"),
  ("poll_change_map", "Poll to change map to {s0}: 1 = Accept, 2 = Decline"),
  ("poll_change_map_with_faction", "Poll to change map to {s0} and factions to {s1} versus {s2}: 1 = Accept, 2 = Decline"),
  ("poll_change_number_of_bots", "Poll to change number of bots to {reg0} for {s0} and {reg1} for {s1}: 1 = Accept, 2 = Decline"),
  ("poll_time_left", "({reg0} seconds left)"),
  ("poll_result_yes", "The poll is accepted by the majority."),
  ("poll_result_no", "The poll is rejected by the majority."),

  ("total_item_cost_reg0", "Total cost: {reg0}"),

  ("server_name", "Server name:"),
  ("game_password", "Game password:"),
  ("map", "Map:"),
  ("game_type", "Game type:"),
  ("max_number_of_players", "Maximum number of players:"),
  ("number_of_bots_in_team_reg1", "Number of bots in team {reg1}:"),
  ("team_reg1_faction", "Team {reg1} faction:"),
  ("enable_valve_anti_cheat", "Enable Valve Anti-cheat (Requires valid Steam account)"),
  ("allow_friendly_fire", "Allow ranged friendly fire"),
  ("allow_melee_friendly_fire", "Allow melee friendly fire"),
  ("friendly_fire_damage_self_ratio", "Friendly fire damage self (%):"),
  ("friendly_fire_damage_friend_ratio", "Friendly fire damage friend (%):"),
  ("spectator_camera", "Spectator camera:"),
  ("control_block_direction", "Control block direction:"),
  ("map_time_limit", "Map time limit (minutes):"),
  ("round_time_limit", "Round time limit (seconds):"),
  ("players_take_control_of_a_bot_after_death", "Switch to bot on death:"),
  ("team_points_limit", "Team point limit:"),
  ("point_gained_from_flags", "Team points gained for flags (%):"),
  ("point_gained_from_capturing_flag", "Points gained for capturing flags:"),
  ("respawn_period", "Respawn period (seconds):"),
  ("add_to_official_game_servers_list", "Add to official game servers list"),
  ("combat_speed", "Combat_speed:"),
  ("combat_speed_0", "Slowest"),
  ("combat_speed_1", "Slower"),
  ("combat_speed_2", "Medium"),
  ("combat_speed_3", "Faster"),
  ("combat_speed_4", "Fastest"),
  ("off", "Off"),
  ("on", "On"),
  ("defender_spawn_count_limit", "Defender spawn count:"),
  ("unlimited", "Unlimited"),
  ("automatic", "Automatic"),
  ("by_mouse_movement", "By mouse movement"),
  ("free", "Free"),
  ("stick_to_any_player", "Lock to any player"),
  ("stick_to_team_members", "Lock to team members"),
  ("stick_to_team_members_view", "Lock to team members' view"),
  ("make_factions_voteable", "Allow polls to change factions"),
  ("make_kick_voteable", "Allow polls to kick players"),
  ("make_ban_voteable", "Allow polls to ban players"),
  ("bots_upper_limit_for_votes", "Bot count limit for polls:"),
  ("make_maps_voteable", "Allow polls to change maps"),
  ("valid_vote_ratio", "Poll accept threshold (%):"),
  ("auto_team_balance_limit", "Auto team balance threshold (diff.):"),
  ("welcome_message", "Welcome message:"),
  ("initial_gold_multiplier", "Starting gold (%):"),
  ("battle_earnings_multiplier", "Combat gold bonus (%):"),
  ("round_earnings_multiplier", "Round gold bonus (%):"),
  ("allow_player_banners", "Allow individual banners"),
  ("force_default_armor", "Force minimum armor"),

  ("reg0", "{!}{reg0}"),
  ("s0_reg0", "{!}{s0} {reg0}"),
  ("s0_s1", "{!}{s0} {s1}"),
  ("reg0_dd_reg1reg2", "{!}{reg0}:{reg1}{reg2}"),
  ("s0_dd_reg0", "{!}{s0}: {reg0}"),
  ("respawning_in_reg0_seconds", "Respawning in {reg0} seconds..."),
  ("no_more_respawns_remained_this_round", "No lives left for this round"),
  ("reg0_respawns_remained", "({reg0} lives remaining)"),
  ("this_is_your_last_respawn", "(This is your last life)"),
  ("wait_next_round", "(Wait for the next round)"),

  ("yes_wo_dot", "Yes"),
  ("no_wo_dot", "No"),

  ("we_resign", "We have no strength left to put up a fight. We surrender to you, {playername}."),
  ("i_resign", "I don't want to die today. I surrender."),

  ("s1_returned_flag", "{s1} has returned their flag to their base!"),
  ("s1_auto_returned_flag", "{s1} flag automatically returned to their base!"),
  ("s1_captured_flag", "{s1} has captured the enemy flag!"),
  ("s1_taken_flag", "{s1} has taken the enemy flag!"),
  ("s1_neutralized_flag_reg0", "{s1} has neutralized flag {reg0}."),
  ("s1_captured_flag_reg0", "{s1} has captured flag {reg0}!"),
  ("s1_pulling_flag_reg0", "{s1} has started pulling flag {reg0}."),

  ("s1_destroyed_target_0", "{s1} destroyed target A!"),
  ("s1_destroyed_target_1", "{s1} destroyed target B!"),
  ("s1_destroyed_catapult", "{s1} destroyed the catapult!"),
  ("s1_destroyed_trebuchet", "{s1} destroyed the trebuchet!"),
  ("s1_destroyed_all_targets", "{s1} destroyed all targets!"),
  ("s1_saved_1_target", "{s1} saved one target."),
  ("s1_saved_2_targets", "{s1} saved all targets."),

  ("s1_defended_castle", "{s1} defended their castle!"),
  ("s1_captured_castle", "{s1} captured the castle!"),

  ("auto_team_balance_in_20_seconds", "Auto-balance will be done in 20 seconds."),
  ("auto_team_balance_next_round", "Auto-balance will be done next round."),
  ("auto_team_balance_done", "Teams have been auto-balanced."),
  ("s1_won_round", "{s1} has won the round!"),
  ("round_draw", "Time is up. Round draw."),
  ("round_draw_no_one_remained", "No one left. Round draw."),
  ("death_mode_started", "Hurry! Become master of the field!"),

  ("reset_to_default", "Reset to Default"),
  ("done", "Done"),
  ("player_name", "Player Name"),
  ("kills", "Kills"),
  ("deaths", "Deaths"),
  ("ping", "Ping"),
  ("dead", "Dead"),
  ("reg0_dead", "{reg0} Dead"),
  ("bots_reg0_agents", "Bots ({reg0} agents)"),
  ("bot_1_agent", "Bot (1 agent)"),
  ("score", "Score"),
  ("score_reg0", "Score: {reg0}"),
  ("flags_reg0", "(Flags: {reg0})"),
  ("reg0_players", "({reg0} players)"),
  ("reg0_player", "({reg0} player)"),

  ("open_gate", "Open Gate"),
  ("close_gate", "Close Gate"),
  ("open_door", "Open Door"),
  ("close_door", "Close Door"),
  ("raise_ladder", "Raise Ladder"),
  ("drop_ladder", "Drop Ladder"),

  ("cancel", "Cancel"),
  ("continue", "Continue"),
  ("back", "Back"),
  ("start_map", "Start Map"),

  ("choose_an_option", "Choose an option:"),
  ("choose_a_poll_type", "Choose a poll type:"),
  ("choose_faction", "Choose Faction"),
  ("choose_a_faction", "Choose a faction:"),
  ("choose_troop", "Choose Troop"),
  ("choose_a_troop", "Choose a troop class:"),
  ("choose_items", "Choose Equipment"),
  ("options", "Options"),
  ("redefine_keys", "Redefine Keys"),
  ("submit_a_poll", "Submit a Poll"),
  ("administrator_panel", "Administrator Panel"),
  ("kick_player", "Kick Player"),
  ("ban_player", "Ban Player"),
  ("mute_player", "Mute Player"),
  ("unmute_player", "Unmute Player"),
  ("quit", "Quit"),
  ("poll_for_changing_the_map", "Change the map"),
  ("poll_for_changing_the_map_and_factions", "Change the map and factions"),
  ("poll_for_changing_number_of_bots", "Change number of bots in teams"),
  ("poll_for_kicking_a_player", "Kick a player"),
  ("poll_for_banning_a_player", "Ban a player"),
  ("choose_a_player", "Choose a player:"),
  ("choose_a_map", "Choose a map:"),
  ("choose_a_faction_for_team_reg0", "Choose a faction for team {reg0}:"),
  ("choose_number_of_bots_for_team_reg0", "Choose number of bots for team {reg0}:"),
  ("spectator", "Spectator"),
  ("spectators", "Spectators"),
  #("score", "Score"),
  ("command", "Command:"),
  ("profile_banner_selection_text", "Choose a banner for your profile:"),
  ("use_default_banner", "Use Faction's Banner"),

  ("party_morale_is_low", "Morale of some troops are low!"),
  ("weekly_report", "Weekly Report"),
  ("has_deserted_the_party", "has deserted the party."),
  ("have_deserted_the_party", "have deserted the party."),

  ("space", " "),
  #new auto generated strings which taken from quick strings.
  ("us_", "Us "),
  ("allies_", "Allies "),
  ("enemies_", "Enemies "),
  ("routed", "Routed"),
  ("weekly_budget", "Weekly Budget"),
  ("income_from_s0", "Income from {s0}:"),
  ("mercenary_payment_from_s0", "Mercenary payment from {s0}:"),
  ("s0s_party", "{s0}'s Warband"),
  ("loss_due_to_tax_inefficiency", "Loss due to tax inefficiency:"),
  ("wages_for_s0", "Wages for {s0}:"),
  ("earlier_debts", "Earlier debts:"),
  ("net_change", "Net change:"),
  ("earlier_wealth", "Earlier wealth:"),
  ("new_wealth", "New wealth:"),
  ("new_debts", "New debts:"),
  ("completed_faction_troop_assignments_cheat_mode_reg3", "{!}Completed faction troop assignments, cheat mode: {reg3}"),
  ("completed_political_events_cheat_mode_reg3", "{!}Completed political events, cheat mode: {reg3}"),
  ("assigned_love_interests_attraction_seed_reg3", "{!}Assigned love interests. Attraction seed: {reg3}"),
  ("located_kingdom_ladies_cheat_mode_reg3", "{!}Located kingdom ladies, cheat mode: {reg3}"),
  ("team_reg0_bot_count_is_reg1", "{!}Team {reg0} bot count is {reg1}."),
  ("input_is_not_correct_for_the_command_type_help_for_more_information", "{!}Input is not correct for the command. Type 'help' for more information."),
  ("maximum_seconds_for_round_is_reg0", "Maximum seconds for round is {reg0}."),
  ("respawn_period_is_reg0_seconds", "Respawn period is {reg0} seconds."),
  ("bots_upper_limit_for_votes_is_reg0", "Bots upper limit for votes is {reg0}."),
  ("map_is_voteable", "Map is voteable."),
  ("map_is_not_voteable", "Map is not voteable."),
  ("factions_are_voteable", "Factions are voteable."),
  ("factions_are_not_voteable", "Factions are not voteable."),
  ("players_respawn_as_bot", "Players respawn as bot."),
  ("players_do_not_respawn_as_bot", "Players do not respawn as bot."),
  ("kicking_a_player_is_voteable", "Kicking a player is voteable."),
  ("kicking_a_player_is_not_voteable", "Kicking a player is not voteable."),
  ("banning_a_player_is_voteable", "Banning a player is voteable."),
  ("banning_a_player_is_not_voteable", "Banning a player is not voteable."),
  ("player_banners_are_allowed", "Player banners are allowed."),
  ("player_banners_are_not_allowed", "Player banners are not allowed."),
  ("default_armor_is_forced", "Default armor is forced."),
  ("default_armor_is_not_forced", "Default armor is not forced."),
  ("percentage_of_yes_votes_required_for_a_poll_to_get_accepted_is_reg0", "Percentage of yes votes required for a poll to get accepted is {reg0}%."),
  ("auto_team_balance_threshold_is_reg0", "Auto team balance threshold is {reg0}."),
  ("starting_gold_ratio_is_reg0", "Starting gold ratio is {reg0}%."),
  ("combat_gold_bonus_ratio_is_reg0", "Combat gold bonus ratio is {reg0}%."),
  ("round_gold_bonus_ratio_is_reg0", "Round gold bonus ratio is {reg0}%."),
  ("point_gained_from_flags_is_reg0", "Team points gained for flags is {reg0}%."),
  ("point_gained_from_capturing_flag_is_reg0", "Points gained for capturing flags is {reg0}%."),
  ("map_time_limit_is_reg0", "Map time limit is {reg0} minutes."),
  ("team_points_limit_is_reg0", "Team point limit is {reg0}."),
  ("defender_spawn_count_limit_is_s1", "Defender spawn count is {s1}."),
  ("system_error", "SYSTEM ERROR!"),
  ("prisoner_granted_parole", "Prisoner granted parole"),
  ("prisoner_not_offered_parole", "Prisoner not offered parole"),
  #("_age_reg1_family_", "^Age: {reg1}^Family:"),
  ("_age_reg1_family_", "Age: {reg1}^Family:"),
  ("s49_s12_s11_rel_reg0", "{s49} {s12} ({s11}, rel: {reg0}),"),
  ("s49_s12_s11", "{s49} {s12} ({s11}),"),
  #SB : add wealth, remove later, also add marshal indicator
  #("lord_info_string", "{reg6?:{reg4?{s54} is the ruler of {s56}.^:{s54} is {reg5?the marshal for:a vassal of} {s55} of {s56}.^}}Renown: {reg15}. Controversy: {reg16}. Wealth: {reg17}.^Religion: {s29}.^{reg9?{reg3?She:He} is the {reg3?lady:lord} of {s58}.:{reg3?She:He} has no fiefs.}{s27}{s26}^{s59}^{s49}"),
  ("lord_info_string", "{reg6?:{reg4?{s54} is the ruler of {s56}.^:{s54} is {reg5?the marshal for:a vassal of} {s55} of {s56}.^}}Renown: {reg15}. Controversy: {reg16}. Wealth: {reg17}.^Religion: {s29} ^{reg9?{reg3?She:He} is the {reg3?lady:lord} of {s58}.:{reg3?She:He} has no fiefs.}{s27}{s26}^{s59}^{s49}"),
  ("updating_faction_notes_for_s14_temp_=_reg4", "{!}Updating faction notes for {s14}, temp = {reg4}"),
  ("foreign_relations__", "{s20}^Foreign relations: ^"), #SB : insert domestic policy string
  ("s21__the_s5_is_at_war_with_the_s14", "{s21}^* The {s5} is at war with the {s14}."),
  ("s21_the_s5_has_had_the_upper_hand_in_the_fighting", "{s21} The {s5} has had the upper hand in the fighting."),
  ("s21_the_s5_has_gotten_the_worst_of_the_fighting", "{s21} The {s5} has gotten the worst of the fighting."),
  ("s21_the_fighting_has_gone_on_for_some_time_and_the_war_may_end_soon_with_a_truce", "{s21} The fighting has gone on for some time, and the war may end soon with a truce."),
  ("s21_the_fighting_has_begun_relatively_recently_and_the_war_may_continue_for_some_time", "{s21} The fighting has begun relatively recently, and the war may continue for some time."),
  ("s21_reg4reg5", "{!}{s21} ({reg4}/{reg5})"),
  ("_however_the_truce_is_no_longer_binding_on_the_s14", " However, the truce is no longer binding on the {s14}"),
  ("s21__the_s5_is_bound_by_truce_not_to_attack_the_s14s18_the_truce_will_expire_in_reg1_days", "{s21}^* The {s5} is bound by truce not to attack the {s14}.{s18} The truce will expire in {reg1} days."),
  ("s21__the_s5_has_recently_suffered_provocation_by_subjects_of_the_s14_and_there_is_a_risk_of_war", "{s21}^* The {s5} has recently suffered provocation by subjects of the {s14}, and there is a risk of war."),
  # ("s21__the_s5_has_no_outstanding_issues_with_the_s14", "{s21}^* The {s5} has no outstanding issues with the {s14}."),
  ("s21_the_s14_was_recently_provoked_by_subjects_of_the_s5_and_there_is_a_risk_of_war_", "{s21} The {s14} was recently provoked by subjects of the {s5}, and there is a risk of war.^"),
  ("s21_cheat_mode_assessment_s14_", "{!}{s21}^CHEAT MODE ASSESSMENT: {s14}^"),
  #("the_s5_is_ruled_by_s6_it_occupies_s8_its_vassals_are_s10__s21", "The {s5} is ruled by {s6}.^It occupies {s8}.^Its vassals are {s10}.^^{s21}"),
  ("the_s5_is_ruled_by_s6_it_occupies_s8_its_vassals_are_s10__s21", "The {s5} is ruled by {s6} ^It occupies {s8}.^Its vassals are {s10}.^^{s21}"),
  ("assigned_lord_reputation_and_relations_cheat_mode_reg3", "{!}Assigned lord reputation and relations, cheat mode: {reg3}"),
  ("caravan_trades_in_s5_originally_from_s4_", "{!}Caravan trades in {s5}, originally from {s4} "),
  ("your_hero_prisoned_at_s1", "{!}your hero prisoned at {s1}."),
  ("old_morale_is_reg0_new_morale_is_reg1", "{!}old morale is {reg0}, new morale is {reg1}"),
  ("our_per_person__reg0_num_people__reg1_total_gain__reg2", "{!}[our] per person : {reg0}, num people : {reg1}, total gain : {reg2}"),
  ("ene_per_person__reg0_num_people__reg1_total_gain__reg2", "{!}[ene] per person : {reg0}, num people : {reg1}, total gain : {reg2}"),
  ("all_per_person__reg0_num_people__reg1_total_gain__reg2", "{!}[all] per person : {reg0}, num people : {reg1}, total gain : {reg2}"),
  ("loss_ratio_is_reg1", "{!}loss ratio is {reg1}"),
  ("total_enemy_morale_gain__reg6_last_total_enemy_morale_gain__reg7_remaining_enemy_population__reg5", "{!}total enemy morale gain : {reg6}, last total enemy morale gain : {reg7}, remaining enemy population : {reg5}"),
  ("reg4_killed_reg5_wounded_reg6_routed", "{reg4} killed, {reg5} wounded, {reg6} routed"),
  ("reg4_killed_reg5_routed", "{reg4} killed, {reg5} routed"),
  ("reg4_killed_reg5_wounded", "{reg4} killed, {reg5} wounded"),
  ("reg4_wounded_reg5_routed", "{reg4} wounded, {reg5} routed"),
  #("routed", "routed"),
  ("caravan_in_s10_considers_s11_total_price_dif_=_reg3", "{!}Caravan in {s10} considers {s11}, total price dif = {reg3}"),
  ("test__caravan_in_s3_selects_for_s4_trade_score_reg3", "{!}TEST - Caravan in {s3} selects for {s4}, trade score: {reg3}"),
  ("prisoner_relative_is_reg0", "{!}prisoner relative is {reg0}"),
  ("test_diagnosis__traveller_attacks_for_s4", "{!}Test diagnosis -- traveller attacks for {s4}"),
  ("traveller_attack_found", "{!}Traveller attack found"),
  ("s42", "{s42}"),
  ("test_diagnostic_quest_found_for_s4", "{!}Test diagnostic: Quest found for {s4}"),
  ("s4_changing_sides_aborts_quest", "{!}{s4} changing sides aborts quest"),
  ("s4_awarded_to_s5", "{s4} awarded to {s5}"),
  ("s11_reacts_to_granting_of_s12_to_s10", "{!}{s11} reacts to granting of {s12} to {s10}"),
  ("debug__hiring_men_to_s7_ideal_size__reg6_ideal_top_size__reg7_hiring_budget__reg8", "{!}DEBUG : hiring men to {s7} ideal size : {reg6}, ideal top size : {reg7}, hiring budget : {reg8}"),
  ("debug__hiring_men_to_party_for_s0", "{!}DEBUG : hiring men to party for {s0}"),
  ("calculating_sortie_for_s4_strength_of_reg3_vs_reg4_enemies", "Calculating sortie for {s4}, strength of {reg3} vs {reg4} enemies"),
  ("s4_sorties", "{!}{s4} sorties"),
  ("current_wealth_reg1_taxes_last_collected_from_s4", "Current wealth: {reg1}. Taxes last collected from {s4}"),
  ("s4_considers_going_to_s5_to_pay_court_to_s6", "{!}{s4} considers going to {s5} to pay court to {s6}"),
  ("relation_with_1_bug_found_here__probably_because_s5_has_just_been_captured", "{!}Relation with -1 bug found here - probably because {s5} has just been captured"),
  ("s4_has_reg4_chance_of_going_to_home_center", "{!}{s4} has {reg4} chance of going to home center"),
  ("s4_has_reg4_chance_of_recruiting_troops", "{s4} has {reg4} chance of recruiting troops"),
  ("s4_has_reg4_chance_of_going_to_s5", "{s4} has {reg4} chance of going to {s5}"),
  ("s4_has_reg5_chance_of_patrolling_s6", "{s4} has {reg5} chance of patrolling {s6}"),
  ("s4_has_reg5_chance_of_raiding_s6", "{s4} has {reg5} chance of raiding {s6}"),
  ("s4_has_reg5_chance_of_besieging_s6", "{s4} has {reg5} chance of besieging {s6}"),
  ("sum_chances_reg6", "Sum chances: {reg6}"),
  ("deciding_faction_ai_for_s3", "Deciding faction AI for {s3}"),
  ("s5_decides_s14", "{!}{s5} decides: {s14}"),
  ("lords_of_the_s1_gather_for_a_feast_at_s2", "Lords of the {s1} gather for a feast at {s2}."),
  ("s5_begins_offensive", "{!}{s5} begins offensive"),
  ("renown_change_of_reg4_reduced_to_reg5_because_of_high_existing_renown", "{!}Renown change of {reg4} reduced to {reg5}, because of high existing renown"),
  ("s14", "{!}{s14}"),
  ("players_kingdom_has_had_reg3_days_of_peace", "Player's kingdom has had {reg3} days of peace"),
  ("s4_is_present_at_the_center_and_in_place_of_honor", "{!}{s4} is present at the center and in place of honor"),
  ("s4_is_present_at_the_center_as_a_refugee", "{!}{s4} is present at the center as a refugee"),
  ("s4_is_present_at_the_center_and_not_attending_the_feast", "{!}{s4} is present at the center and not attending the feast"),
  ("s4_is_present_at_the_center_and_is_married", "{!}{s4} is present at the center and is married"),
  ("s4_is_present_at_the_center_and_is_attending_the_feast", "{s4} is present at the center and is attending the feast"),
  ("s4_is_present_at_the_center_and_is_awaiting_the_player_in_private", "{s4} is present at the center and is awaiting the player in private"),
  ("s4_is_present_at_the_center_and_is_allowed_to_meet_the_player", "{s4} is present at the center and is allowed to meet the player"),
  ("s4_is_present_at_the_center_and_is_not_allowed_to_meet_the_player", "{s4} is present at the center and is not allowed to meet the player"),

  #Relative types
  ("no_relation", "no relation"),
  ("wife", "wife"),
  ("husband", "husband"),
  ("father", "father"),
  ("mother", "mother"),
  ("daughter", "daughter"),
  ("son", "son"),
  ("sister", "sister"),
  ("brother", "brother"),
  ("niece", "niece"),
  ("nephew", "nephew"),
  ("aunt", "aunt"),
  ("uncle", "uncle"),
  ("cousin", "cousin"),
  ("daughterinlaw", "daughter-in-law"),
  ("soninlaw", "son-in-law"),
  ("motherinlaw", "mother-in-law"),
  ("fatherinlaw", "father-in-law"),
  ("sisterinlaw", "sister-in-law"),
  ("brotherinlaw", "brother-in-law"),
  ("print_party_members_entered", "print party members entered"),
  ("num_companion_stacks_=_reg10", "num companion stacks = {reg10}"),
  ("someone", "someone"),

  #Trade explanations
##diplomacy start+ replace {sir/madame} with {s0} so it can be "my lord" or "your highness"
  ("i_take_what_work_i_can_sirmadame_i_carry_water_or_help_the_merchants_with_their_loads_or_help_build_things_if_theres_things_to_be_built", "I take what work I can, {s0}. I carry water, or help the merchants with their loads, or help build things, if there are things to be built."),
##diplomacy end+
  ("dna_reg4_total_production_reg5_modula_reg7", "{!}DNA: {reg4}, total production: {reg5}, modula: {reg7}"),
  ("agent_produces_s9", "{!}Agent produces {s9}"),
##diplomacy start+ replace {sir/madame} with {s0} so it can be "my lord" or "your highness"
  ("im_not_doing_anything_sirmadame_theres_no_work_to_be_had_around_here_these_days", "I'm not doing anything, {s0}. There's no work to be had around here these days."),
  ("im_not_doing_anything_sirmadame_i_have_no_land_of_my_own_and_theres_no_work_to_be_had_around_here_these_days", "I'm not doing anything, {s0}. I have no land of my own, and there's no work to be had around here these days."),
  ("why_im_still_living_off_of_your_kindness_and_goodness_sirmadame_hopefully_there_will_be_work_shortly", "Why, I'm still living off of your kindness and goodness, {s0}. Hopefully there will be work, shortly."),
##diplomacy end+
  ("i_work_in_the_fields_just_outside_the_walls_where_they_grow_grain_we_dont_quite_grow_enough_to_meet_our_needs_though_and_have_to_import_grain_from_the_surrounding_countryside", "I work in the fields, just outside the walls, where they grow grain. We don't quite grow enough to meet our needs, though, and have to import grain from the surrounding countryside."),
  ("i_work_mostly_in_the_fields_growing_grain_in_the_town_they_grind_it_to_make_bread_or_ale_and_we_can_also_boil_it_as_a_porridge", "I work mostly in the fields, growing grain. In the town they grind it to make bread or ale, and we can also boil it as a porridge."),
  ("i_work_in_the_breweries_making_ale_the_poor_folk_drink_a_lot_of_it_as_its_cheaper_than_wine_we_make_it_with_grain_brought_in_from_the_countryside", "I work in the breweries, making ale. The poor folk drink a lot of it, as it's cheaper than wine. We make it with grain brought in from the countryside."),
  ("i_work_in_a_mill_grinding_flour_to_make_bread_bread_is_cheap_keeps_well_and_fills_the_stomach", "I work in a mill, grinding flour to make bread. Bread is cheap, keeps well, and fills the stomach."),
  ("i_tend_cattle_we_dry_and_salt_meat_to_preserve_it_and_make_cheese_from_the_milk", "I tend cattle. We dry and salt meat to preserve it, and send the hides to the towns to be made into leather. We also make cheese from the milk."),
  ("i_tend_cattle_we_dry_and_salt_meat_to_preserve_it_and_make_cheese_from_the_milk_so_it_doesnt_spoil", "I tend cattle. We dry and salt meat to preserve it, and send the hides to the towns to be made into leather. We also make cheese from the milk."),
  ("i_tend_sheep_we_send_the_wool_to_the_cities_to_be_woven_into_cloth_and_make_mutton_sausage_when_we_cull_the_herds", "I tend sheep. We send the wool to the cities to be woven into cloth, and make mutton sausage when we cull the herds."),
  ("i_work_at_a_loom_spinning_cloth_from_wool_wool_is_some_of_the_cheapest_cloth_you_can_buy_but_it_will_still_keep_you_warm", "I work at a loom, spinning cloth from wool. Wool is some of the cheapest cloth you can buy, but it will still keep you warm."),
  ("i_crew_a_fishing_boat_we_salt_and_smoke_the_flesh_to_sell_it_far_inland", "I crew a fishing boat. We salt and smoke the flesh, to sell it far inland."),
  ("i_sift_salt_from_a_nearby_flat_they_need_salt_everywhere_to_preserve_meat_and_fish", "I sift salt from a nearby flat. They need salt everywhere, to preserve meat and fish."),
  ("i_mine_iron_from_a_vein_in_a_nearby_cliffside_they_use_it_to_make_tools_arms_and_other_goods", "I mine iron from a vein in a nearby cliffside. They use it to make tools, arms, and other goods."),
  ("i_make_pottery_which_people_use_to_store_grain_and_carry_water", "I make pottery, which people use to store grain and carry water."),

##diplomacy start+ replace {sir/madame} with {s0} so it can be "my lord" or "your highness"
  ("trade_explanation_tools", "I work in a smithy, {s0}, making all sorts of ironware -- knives, axes, pots, plough-blades, scythes, hammers, anvils, tongs, adzes, saws, nails, horseshoes, firesteel, braziers, and of course arms and armor for your excellencies."),
##diplomacy end+
  ("trade_explanation_oil", "I work in an oil press, making oil from olives brought in from the countryside. If you can afford it, our oil has a hundred uses -- in cooking, lamps, even for easing childbirth."),
##diplomacy start+ replace {sir/madame} with {s0} so it can be "my lord" or "your highness"
  ("trade_explanation_linen", "I weave linen, using flax brought in from the surrounding countryside. It's makes a tough, light fabric, {s0} -- good for summer clothing, sails for boats, and the like."),
##diplomacy end+
  ("trade_explanation_velvet", "I work in one of this town's great weaveries, carefully making the velvet for which we are known. We use silks brought from across the mountains, and dyes from the far corners of the earth, and make of it the finest and most expensive fabric that can be found in the land."),
  ("trade_explanation_spice", "I work in the caravanserie, helping the merchants unload the spice they bring from across the mountains. Pepper, cinnamon, cloves, saffron... The rich mark their wealth by the amount of spices in their food, and they say that for every ailment, there's a spice which cures it."),
  ("trade_explanation_apples", "I'm just coming in from the orchards, where we grow apples. We dry them for storage, or they can also be made into cider or vinegar."),

  ("trade_explanation_grapes", "I work in the vineyards on the hillsides, growing grapes to be made into fine wines for the tables of the lords, ladies, and merchants, and cheap wine to be mixed with water to quench the thirst of the commons."),
  ("trade_explanation_dyes", "I work in the caravanseries, unloading dyes brought in from the lands far away -- the crimson of oak beetles and the red roots of madder, the blue of indigo and woad shrubs, the yellow of weld root and greenweed. The weavers use it to color the silks and velvets of the great lords of the realm."),
##diplomacy start+ replace {sir/my lady} with {s0} so it can be "my lord" or "your highness"
  ("trade_explanation_leatherwork", "I work in the tanneries outside the walls, turning cured hides from the countryside into good, supple leather. It's foul work, and I come home stinking of urine, dung, and lime -- but that's where your boots, saddles, and bridles come from, {s0}."),
  ("trade_explanation_flax", "I sew and harvest linseed, and rot the stems to make flax fibers. That's the source of your fine linens, {s0} -- a rotting pit on the edge of a field."),
##diplomacy end+
  #SB : differentiate between two sources of dates
  ("trade_explanation_dates_village", "I tend to a grove of date palms. I hope you don't mind me saying so, {s0}, but it takes great skill to tend them, as we must climb to the tops of the palms to ensure that the trees will flower. We export the fruit far and wide, as they keep for many months when properly dried. As sweet as honey, and they grant the eater health and strength."),
  ("trade_explanation_dates_town", "I tend to a grove of date palms. We grow them using well-water, and export the fruit far and wide, as they keep for many months when properly dried. As sweet as honey, and they grant the eater health and vigor."),
  ("trade_explanation_olives", "I tend to a grove of olive trees. You can eat the fruit or preserve it in brine, but we end up sending most of it to be pressed, to be made into oil."),
  #new trade good
  ("trade_explanation_jewelry", "I work in one of this town's jewelries, carefully making the jewelry for which we are known. We use the precious metals brought from all over, such as gold and silver as well as many beautiful gemstones, to make of it the finest and most expensive ornaments that can be found in the land."),




  ("s10_has_reg4_needs_reg5", "{!}{s10} has {reg4}, needs {reg5}"),
  ("s14_i_hear_that_you_can_find_a_good_price_for_it_in_s15", "{s14}. I hear that you can find a good price for it in {s15}."),
  ("s1_reg1", "{!}{s1} ({reg1})"),
  ("s1_reg2", "{!}{s1} ({reg2})"),
  ("s1_reg3", "{!}{s1} ({reg3})"),
  ("s1_reg4", "{!}{s1} ({reg4})"),
  ("s1_reg5", "{!}{s1} ({reg5})"),
  ("s1_reg6", "{!}{s1} ({reg6})"),
  ("s1_reg7", "{!}{s1} ({reg7})"),
  ("s1_reg8", "{!}{s1} ({reg8})"),
  ("s1_reg9", "{!}{s1} ({reg9})"),
  ("reg13", "{!}{reg13}"),
  ("reg14", "{!}{reg14}"),
  ("reg15", "{!}{reg15}"),
  ("reg16", "{!}{reg16}"),
  ("reg17", "{!}{reg17}"),
  ("reg18", "{!}{reg18}"),
  ("reg19", "{!}{reg19}"),
  ("reg20", "{!}{reg20}"),
  ("reg21", "{!}{reg21}"),
  ("assigning_lords_to_empty_centers", "{!}ASSIGNING LORDS TO EMPTY CENTERS"),
  ("assign_lords_to_empty_centers_just_happened", "{!}Assign lords to empty centers just happened"),
  ("s4_of_the_s5_is_unassigned", "{!}{s4} of the {s5} is unassigned"),
  ("s4_of_the_s5_is_reserved_for_player", "{!}{s4} of the {s5} is reserved for player"),
  ("s4_of_the_s5_has_no_fiefs", "{!}{s4} of the {s5} has no fiefs"),
  ("s4_unassigned_centers_plus_landless_lords_=_reg4", "{!}{s4}: unassigned centers plus landless lords = {reg4}"),
  ("s4_holds_s5_in_reserve", "{!}{s4} holds {s5} in reserve"),
  ("s2s_rebellion", "{s2}'s Rebellion"),
  ("political_suggestion", "Political suggestion"),
  ("updating_volunteers_for_s4_faction_is_s5", "{!}Updating volunteers for {s4}, faction is {s5}"),
  ("shuffling_companion_locations", "{!}Shuffling companion locations"),
  ("s4_is_at_s5", "{s4} is at {s5}"), #SB : translate string
  ("instability_reg0_of_lords_are_disgruntled_reg1_are_restless", "Instability: {reg0}% of lords are disgruntled, {reg1}% are restless"),
  ("reg1shehe_is_prisoner_of_s1", "{reg1?She:He} is prisoner of {s1}."),
  ("s39_rival", "{s39} (rival)"),
  ("s40", "{!}{s40}"),
  ("s41_s39_rival", "{s41}, {s39} (rival)"),
  ("reputation_cheat_mode_only_martial_", "{!}Reputation (cheat mode only): Martial^"),
  ("reputation_cheat_mode_only_debauched_", "{!}Reputation (cheat mode only): Debauched^"),
  ("reputation_cheat_mode_only_pitiless_", "{!}Reputation (cheat mode only): Pitiless^"),
  ("reputation_cheat_mode_only_calculating_", "{!}Reputation (cheat mode only): Calculating^"),
  ("reputation_cheat_mode_only_quarrelsome_", "{!}Reputation (cheat mode only): Quarrelsome^"),
  ("reputation_cheat_mode_only_goodnatured_", "{!}Reputation (cheat mode only): Good-natured^"),
  ("reputation_cheat_mode_only_upstanding_", "{!}Reputation (cheat mode only): Upstanding^"),
  ("reputation_cheat_mode_only_conventional_", "{!}Reputation (cheat mode only): Conventional^"),
  ("reputation_cheat_mode_only_adventurous_", "{!}Reputation (cheat mode only): Adventurous^"),
  ("reputation_cheat_mode_only_romantic_", "{!}Reputation (cheat mode only): Romantic^"),
  ("reputation_cheat_mode_only_moralist_", "{!}Reputation (cheat mode only): Moralist^"),
  ("reputation_cheat_mode_only_ambitious_", "{!}Reputation (cheat mode only): Ambitious^"),
  ("reputation_cheat_mode_only_reg11_", "{!}Reputation (cheat mode only): {reg11}^"),
  ("love_interest", "love interest"),
  ("betrothed", "betrothed"),
  ("s40_s39_s2_reg0", "{!}{s40}, {s39} ({s2}, {reg0})"),
  ("other_relations_s40_", "Other relations: {s40}^"),
  ("relation_with_liege_reg0_", "Relation with liege: {reg0}^"),
  ("sense_of_security_military_reg1_court_position_reg3_", "Sense of security: military {reg1}, court position {reg3}^"),
  ("s46s45s44s48", "{!}{s46}{s45}{s44}{s48}"),
  ("political_details_s47_", "Political details:^{s47}^"),
  ("checking_volunteer_availability_script", "{!}Checking volunteer availability script"),
  ("center_relation_at_least_zero", "{!}Center relation at least zero"),
  ("relationfaction_conditions_met", "{!}Relation/faction conditions met"),
  ("troops_available", "{!}Troops available"),
  ("party_has_capacity", "{!}Party has capacity"),
  ("personality_clash_conversation_begins", "{!}Personality clash conversation begins"),
  ("personality_match_conversation_begins", "{!}Personality match conversation begins"),
  ("the_s55", "the {s55}"),

  ("travellers_on_the_road", "travellers on the road"),
  ("attack_on_travellers_found_reg3_hours_ago", "{!}Attack on travellers found, {reg3} hours ago"),
  ("trade_event_found_reg3_hours_ago", "{!}Trade event found, {reg3} hours ago"),
  ("a_short_while_ago", "a short while ago"),
  ("one_day_ago", "one day ago"),
  ("two_days_day_ago", "two days day ago"),
  ("earlier_this_week", "earlier this week"),
  ("about_a_week_ago", "about a week ago"),
  ("about_two_weeks_ago", "about two weeks ago"),
  ("several_weeks_ago", "several weeks ago"),
  ("unknown_assailants", "unknown assailants"),

  #Faction descriptors
  ("swadians", "Goths"),
  ("vaegirs", "Vandals"),
  ("khergits", "Huns"),
  ("nords", "Germans"),
  ("rhodoks", "Picts"),
  ("sarranids", "Sassanids"),
  ("west_imperials", "Western Romans"),
  ("east_imperials", "Eastern Romans"),
  ("jumnes", "Germans"),
  ("romans", "Romans"),
  ("franks", "Franks"),
  ("saxons", "Saxons"),
  ("britons", "Romano-Britons"),
  ("mauri", "Romano-Mauri"),
  ("lombards", "Langobardi"),
  ("bandits", "bandits"),
  ("deserters", "deserters"),
  ("your_followers", "your followers"),
  ("armenians", "Armenians"),
  ("jews", "Jews"),
  ("irish", "Irish"),
  ("sporoi", "Sporoi"),
  ("venedi", "Venedi"),

  ("we_have_heard_that_travellers_heading_to_s40_were_attacked_on_the_road_s46_by_s39", "We have heard that travellers heading to {s40} were attacked on the road {s46} by {s39}"),
  ("s43_s44", "{!}{s43}^{s44}"),
  ("we_have_heard_that_travellers_coming_from_s40_were_attacked_on_the_road_s46_by_s39", "We have heard that travellers coming from {s40} were attacked on the road {s46} by {s39}"),
  ("travellers_coming_from_s40_traded_here_s46", "Travellers coming from {s40} traded here {s46}"),
  ("s44", "{!}{s44}"),
  ("it_is_still_early_in_the_caravan_season_so_we_have_seen_little_tradings42", "It is still early in the caravan season, so we have seen little trading.{s42}"),
  ("there_has_been_very_little_trading_activity_here_recentlys42", "There has been very little trading activity here recently.{s42}"),
  ("there_has_some_trading_activity_here_recently_but_not_enoughs42", "There has some trading activity here recently, but not enough.{s42}"),
  ("there_has_some_trading_activity_here_recently_but_the_roads_are_dangerouss42", "There has some trading activity here recently, but the roads are dangerous.{s42}"),
  ("the_roads_around_here_are_very_dangerouss42", "The roads around here are very dangerous.{s42}"),
  ("we_have_received_many_traders_in_town_here_although_there_is_some_danger_on_the_roadss42", "We have received many traders in town here, although there is some danger on the roads.{s42}"),
  ("we_have_received_many_traders_in_town_heres42", "We have received many traders in town here.{s42}"),
  ("s44_s41", "{!}{s44}, {s41}"),
  ("s41", "{!}{s41}"),
  ("there_is_little_news_about_the_caravan_routes_to_the_towns_of_s44_and_nearby_parts_but_no_news_is_good_news_and_those_are_therefore_considered_safe", "There is little news about the caravan routes to the towns of {s44} and nearby parts. But no news is good news, and those are therefore considered safe."),
  ("s47_also_the_roads_to_the_villages_of_s44_and_other_outlying_hamlets_are_considered_safe", "{s47} Also, the roads to the villages of {s44} and other outlying hamlets are considered safe."),
  ("however_the_roads_to_the_villages_of_s44_and_other_outlying_hamlets_are_considered_safe", "However, the roads to the villages of {s44} and other outlying hamlets are considered safe."),
  ("we_have_shortages_of", "We have shortages of"),
  ("s33_s34_reg1", "{!}{s33} {s34} ({reg1}),"),
  ("we_have_adequate_stores_of_all_commodities", "We have adequate stores of all commodities"),
  ("s33_and_some_other_commodities", "{s33} and some other commodities"),
  ("the_roads_are_full_of_brigands_friend_but_that_name_in_particular_does_not_sound_familiar_good_hunting_to_you_nonetheless", "The roads are full of brigands, friend, but that name in particular does not sound familiar. Good hunting to you, nonetheless."),
  ("less_than_an_hour_ago", "less than an hour ago"),
  ("maybe_reg3_hours_ago", "maybe {reg3} hours ago"),
  ("reg3_days_ago", "{reg3} days ago"),
  ("youre_in_luck_we_sighted_those_bastards_s16_near_s17_hurry_and_you_might_be_able_to_pick_up_their_trail_while_its_still_hot", "You're in luck. We sighted those bastards {s16} near {s17}. Hurry, and you might be able to pick up their trail while it's still hot."),
  ("you_speak_of_claims_to_the_throne_good_there_is_nothing_id_rather_do_than_fight_for_a_good_cause", "You speak of claims to the throne. Good. There is nothing I'd rather do than fight for a good cause."),
  ("you_speak_of_claims_to_the_throne_well_there_is_nothing_id_rather_do_than_fight_for_a_good_cause_but_the_claim_you_make_seems_somewhat_weak", "You speak of claims to the throne. Well, there is nothing I'd rather do than fight for a good cause, but the claim you make seems somewhat weak."),
  ("i_am_pleased_that_you_speak_of_upholding_my_ancient_rights_which_are_sometimes_trod_upon_in_these_sorry_days", "I am pleased that you speak of upholding my ancient rights, which are sometimes trod upon in these sorry days."),
##diplomacy start+: change "king" to "{s14}" #("i_am_pleased_that_you_speak_of_upholding_my_ancient_rights_but_sometimes_men_make_pledges_before_they_are_king_which_they_cannot_keep_once_they_take_the_throne", "I am pleased that you speak of upholding my ancient rights. But sometimes men make pledges before they are king, which they cannot keep once they take the throne."),
  ("i_am_pleased_that_you_speak_of_upholding_my_ancient_rights_but_sometimes_men_make_pledges_before_they_are_king_which_they_cannot_keep_once_they_take_the_throne", "I am pleased that you speak of upholding my ancient rights. But sometimes men make pledges before they are {s14}, which they cannot keep once they take the throne."),
##Change "swing my sword" to "{s14}"
#  ("you_speak_of_protecting_the_commons_well_i_supposed_thats_good_but_sometimes_the_commons_overstep_their_boundaries_im_more_concerned_that_your_claim_be_legal_so_i_can_swing_my_sword_with_a_good_conscience", "You speak of protecting the commons. Well, I supposed that's good, but sometimes the commons overstep their boundaries. I'm more concerned that your claim be legal, so I can swing my sword with a good conscience."),
  ("you_speak_of_protecting_the_commons_well_i_supposed_thats_good_but_sometimes_the_commons_overstep_their_boundaries_im_more_concerned_that_your_claim_be_legal_so_i_can_swing_my_sword_with_a_good_conscience", "You speak of protecting the commons. Well, I supposed that's good, but sometimes the commons overstep their boundaries. I'm more concerned that your claim be legal, so I can {s14} with a good conscience."),
##diplomacy end+
  ("you_speak_of_giving_me_land_good_i_ask_for_no_more_than_my_due", "You speak of giving me land. Good. I ask for no more than my due."),
  ("you_speak_of_giving_me_land_unfortunately_you_are_not_wellknown_for_rewarding_those_to_whom_you_have_made_such_offers", "You speak of giving me land. Unfortunately, you are not well-known for rewarding those to whom you have made such offers."),
  ("you_speak_of_unifying_calradia_well_i_believe_that_well_always_be_fighting__its_important_that_we_fight_for_a_rightful_cause", "You speak of unifying Europe. Well, I believe that we'll always be fighting - it's important that we fight for a rightful cause."),
  ("you_talk_of_claims_to_the_throne_but_i_leave_bickering_about_legalities_to_the_lawyers_and_clerks", "You talk of claims to the throne, but I leave bickering about legalities to the lawyers and clerks."),
##diplomacy start+: change "king" to "{s14}"
#  ("you_speak_of_ruling_justly_hah_ill_believe_theres_such_a_thing_as_a_just_king_when_i_see_one", "You speak of ruling justly. Hah! I'll believe there's such a thing as a just king when I see one."),
  ("you_speak_of_ruling_justly_hah_ill_believe_theres_such_a_thing_as_a_just_king_when_i_see_one", "You speak of ruling justly. Hah! I'll believe there's such a thing as a just {s14} when I see one."),
#  ("you_spoke_of_protecting_the_rights_of_the_nobles_if_you_did_youd_be_the_first_king_to_do_so_in_a_very_long_time", "You spoke of protecting the rights of the nobles. If you did, you'd be the first king to do so in a very long time."),
  ("you_spoke_of_protecting_the_rights_of_the_nobles_if_you_did_youd_be_the_first_king_to_do_so_in_a_very_long_time", "You spoke of protecting the rights of the nobles. If you did, you'd be the first {s14} to do so in a very long time."),
##diplomacy end+
  ("you_speak_of_giving_me_land_ay_well_lets_see_if_you_deliver", "You speak of giving me land. Ay, well, let's see if you deliver."),
  ("you_speak_of_giving_me_land_bah_youre_not_known_for_delivering_on_your_pledges", "You speak of giving me land. Bah. You're not known for delivering on your pledges."),
  ("you_speak_of_unifying_calradia_well_youve_done_a_good_job_at_making_calradia_bend_its_knee_to_you_so_maybe_thats_not_just_talk", "You speak of unifying Europe. Well, you've done a good job at making Europe bend its knee to you, so maybe that's not just talk."),
  ("you_speak_of_unifying_calradia_id_be_impressed_if_i_thought_you_could_do_it_but_unfortunately_you_dont", "You speak of unifying Europe. I'd be impressed if I thought you could do it. But unfortunately, you don't."),
  ("you_speak_of_claims_to_the_throne_well_any_peasant_can_claim_to_be_a_kings_bastard", "You speak of claims to the throne. Well, any peasant can claim to be a king's bastard"),
  ("well_its_a_fine_thing_to_court_the_commons_with_promises_but_what_do_you_have_to_offer_me", "Well, it's a fine thing to court the commons with promises, but what do you have to offer me?"),
##diplomacy start+: change "lords" to "{s15}", and "lord" to "{s14}"
#  ("you_speak_of_protecting_the_rights_of_lords_that_would_make_a_fine_change_if_my_rights_as_lord_would_be_respected", "You speak of protecting the rights of lords. That would make a fine change, if my rights as lord would be respected."),
  ("you_speak_of_protecting_the_rights_of_lords_that_would_make_a_fine_change_if_my_rights_as_lord_would_be_respected", "You speak of protecting the rights of {s15}. That would make a fine change, if my rights as {s14} would be respected."),
#  ("you_speak_of_protecting_the_rights_of_lords_that_would_make_a_fine_change_if_my_rights_as_lord_would_be_respected_however_it_is_easy_for_you_to_make_promises_while_you_are_weak_that_you_have_no_intention_of_keeping_when_you_are_strong", "You speak of protecting the rights of lords. That would make a fine change, if my rights as lord would be respected. However, it is easy for you to make promises while you are weak, that you have no intention of keeping when you are strong."),
  ("you_speak_of_protecting_the_rights_of_lords_that_would_make_a_fine_change_if_my_rights_as_lord_would_be_respected_however_it_is_easy_for_you_to_make_promises_while_you_are_weak_that_you_have_no_intention_of_keeping_when_you_are_strong", "You speak of protecting the rights of {s15}. That would make a fine change, if my rights as {s14} would be respected. However, it is easy for you to make promises while you are weak, that you have no intention of keeping when you are strong."),
##diplomacy end+
  ("you_speak_of_giving_me_land_well_my_family_is_of_ancient_and_noble_lineage_so_you_promise_me_no_more_than_my_due_still_your_gesture_is_appreciated", "You speak of giving me land. Well, my family is of ancient and noble lineage, so you promise me no more than my due. Still, your gesture is appreciated."),
  ("you_speak_of_giving_me_land_well_you_make_that_pledge_but_i_am_not_impressed", "You speak of giving me land. Well, you make that pledge, but I am not impressed."),
  ("you_speak_of_unifying_calradia_well_much_of_this_land_now_bends_its_knee_to_you_so_perhaps_that_is_not_just_talk", "You speak of unifying Europe. Well, much of this land now bends its knee to you, so perhaps that is not just talk."),
  ("you_speak_of_unifying_calradia_but_right_now_yours_is_just_one_squabbling_faction_among_many", "You speak of unifying Europe, but right now yours is just one squabbling faction among many."),
  ("you_speak_of_claims_well_no_offense_but_a_claim_unsupported_by_might_rarely_prospers", "You speak of claims. Well, no offense, but a claim unsupported by might rarely prospers."),
  ("you_speak_of_protecting_the_commons_well_i_suppose_that_will_make_for_a_more_prosperous_realm_ive_always_tried_to_treat_my_peasants_decently_saves_going_to_bed_worrying_about_whether_youll_wake_up_with_the_roof_on_fire", "You speak of protecting the commons. Well, I suppose that will make for a more prosperous realm. I've always tried to treat my peasants decently. Saves going to bed worrying about whether you'll wake up with the roof on fire."),
  ("you_speak_of_protecting_the_commons_very_well_but_remember_that_peasants_are_more_likely_to_cause_trouble_if_you_make_promises_then_dont_deliver_than_if_you_never_made_the_promise_in_the_first_place", "You speak of protecting the commons. Very well. But remember that peasants are more likely to cause trouble if you make promises then don't deliver, than if you never made the promise in the first place."),
##diplomacy start+: change "lords" to "{s14}", and "king" to "{s15}"
#  ("you_speak_of_protecting_the_rights_of_lords_good_youd_be_well_advised_to_do_that__men_fight_better_for_a_king_wholl_respect_their_rights", "You speak of protecting the rights of lords. Good. You'd be well advised to do that -- men fight better for a king who'll respect their rights."),
  ("you_speak_of_protecting_the_rights_of_lords_good_youd_be_well_advised_to_do_that__men_fight_better_for_a_king_wholl_respect_their_rights", "You speak of protecting the rights of {s14}. Good. You'd be well advised to do that -- men fight better for a {s15} who'll respect their rights."),
#  ("you_speak_of_protecting_the_rights_of_lords_very_well_but_remember__failing_to_keep_promises_which_you_made_while_scrambling_up_the_throne_is_the_quickest_way_to_topple_off_of_it_once_you_get_there", "You speak of protecting the rights of lords. Very well. But remember -- failing to keep promises which you made while scrambling up the throne is the quickest way to topple off of it once you get there."),
  ("you_speak_of_protecting_the_rights_of_lords_very_well_but_remember__failing_to_keep_promises_which_you_made_while_scrambling_up_the_throne_is_the_quickest_way_to_topple_off_of_it_once_you_get_there", "You speak of protecting the rights of {s14}. Very well. But remember -- failing to keep promises which you made while scrambling up the throne is the quickest way to topple off of it once you get there."),
##diplomacy end+
  ("you_speak_of_giving_me_land_very_good_but_often_i_find_that_when_a_man_makes_too_many_promises_trying_to_get_to_the_top_he_has_trouble_keeping_them_once_he_reaches_it", "You speak of giving me land. Very good, but often I find that when a man makes too many promises trying to get to the top, he has trouble keeping them once he reaches it."),
  ("you_speak_of_unifying_calradia_well_many_have_said_that_you_might_very_well_be_the_one_to_do_it", "You speak of unifying Europe. Well, many have said that, you might very well be the one to do it."),
  ("you_speak_of_unifying_calradia_well_all_the_kings_say_that_im_not_sure_that_you_will_succeed_while_they_fail", "You speak of unifying Europe. Well, all the kings say that. I'm not sure that you will succeed while they fail."),
  ("you_speak_of_claims_do_you_think_i_care_for_the_nattering_of_lawyers", "You speak of claims. Do you think I care for the nattering of lawyers?"),
##diplomacy start+
##Replace "swineherd" with "{s14}"
#  ("you_speak_of_protecting_the_commons_how_kind_of_you_i_shall_tell_my_swineherd_all_about_your_sweet_promises_no_doubt_he_will_become_your_most_faithful_vassal", "You speak of protecting the commons. How kind of you! I shall tell my swineherd all about your sweet promises. No doubt he will become your most faithful vassal."),
  ("you_speak_of_protecting_the_commons_how_kind_of_you_i_shall_tell_my_swineherd_all_about_your_sweet_promises_no_doubt_he_will_become_your_most_faithful_vassal", "You speak of protecting the commons. How kind of you! I shall tell my {s14} all about your sweet promises. No doubt he will become your most faithful vassal."),
##Replace "lords" with "{s14}"
#  ("you_speak_of_protecing_the_rights_of_lords_such_sweet_words_but_ill_tell_you_this__the_only_rights_that_are_respected_in_this_world_are_the_rights_to_dominate_whoever_is_weaker_and_to_submit_to_whoever_is_stronger", "You speak of protecing the rights of lords. Such sweet words! But I'll tell you this -- the only rights that are respected in this world are the rights to dominate whoever is weaker, and to submit to whoever is stronger."),
  ("you_speak_of_protecing_the_rights_of_lords_such_sweet_words_but_ill_tell_you_this__the_only_rights_that_are_respected_in_this_world_are_the_rights_to_dominate_whoever_is_weaker_and_to_submit_to_whoever_is_stronger", "You speak of protecing the rights of {s14}. Such sweet words! But I'll tell you this -- the only rights that are respected in this world are the rights to dominate whoever is weaker, and to submit to whoever is stronger."),
##diplomacy end+
  ("you_speak_of_giving_me_land_yes_very_good__but_you_had_best_deliver", "You speak of giving me land. Yes, very good -- but you had best deliver."),
  ("you_speak_of_giving_me_land_hah_perhaps_all_those_others_to_whom_you_promised_lands_will_simply_step_aside", "You speak of giving me land. Hah! Perhaps all those others to whom you promised lands will simply step aside?"),
  ("you_speak_of_unifying_calradia_you_may_indeed_humble_the_other_kings_of_this_land_and_in_that_case_i_would_hope_that_you_would_remember_me_as_your_faithful_servant", "You speak of unifying Europe. You may indeed humble the other kings of this land, and in that case I would hope that you would remember me as your faithful servant."),
  ("you_speak_of_unifying_calradia_but_you_are_weak_and_i_think_that_you_will_remain_weak", "You speak of unifying Europe But you are weak, and I think that you will remain weak."),
##diplomacy start+: replace "king" with "{s14}", and remove extraneous space
#  ("you_speak_of_claims_its_good_for_a_king_to_have_a_strong_claim_although_admittedly_im_more_concerned_that_he_rules_just_ly_than_with_legalities_anyway_your_claim_seems_wellfounded_to_me", "You speak of claims. It's good for a king to have a strong claim, although admittedly I'm more concerned that he rules just ly than with legalities. Anyway, your claim seems well-founded to me."),
  ("you_speak_of_claims_its_good_for_a_king_to_have_a_strong_claim_although_admittedly_im_more_concerned_that_he_rules_just_ly_than_with_legalities_anyway_your_claim_seems_wellfounded_to_me", "You speak of claims. It's good for a {s14} to have a strong claim, although admittedly I'm more concerned that he rules justly than with legalities. Anyway, your claim seems well-founded to me."),
##diplomacy end+
  ("you_speak_of_claims_but_your_claim_seems_a_bit_weak_to_me", "You speak of claims, but your claim seems a bit weak to me."),
  ("you_speak_of_protecting_the_commons_i_like_that_my_tenants_are_a_happy_lot_i_think_but_i_hear_of_others_in_other_estates_that_arent_so_fortunate", "You speak of protecting the commons. I like that. My tenants are a happy lot, I think, but I hear of others in other estates that aren't so fortunate."),
  ("you_speak_of_protecting_the_commons_im_glad_to_hear_you_say_that_but_do_me_a_favor__dont_promise_the_commons_anything_you_cant_deliver_thats_a_sure_way_to_get_them_to_rebel_and_it_breaks_my_heart_to_have_to_put_them_down", "You speak of protecting the commons. I'm glad to hear you say that. But do me a favor -- don't promise the commons anything you can't deliver. That's a sure way to get them to rebel, and it breaks my heart to have to put them down."),
##diplomacy start+: replace "lords" with "{s14}", and "king" with "{s15}"
#  ("you_speak_of_protecting_the_rights_of_lords_well_very_good_i_suppose_but_you_know__we_lords_can_take_of_ourselves_its_the_common_folk_who_need_a_strong_king_to_look_out_for_them_to_my_mind", "You speak of protecting the rights of lords. Well, very good, I suppose. But you know -- we lords can take of ourselves. It's the common folk who need a strong king to look out for them, to my mind."),
  ("you_speak_of_protecting_the_rights_of_lords_well_very_good_i_suppose_but_you_know__we_lords_can_take_of_ourselves_its_the_common_folk_who_need_a_strong_king_to_look_out_for_them_to_my_mind", "You speak of protecting the rights of {s14}. Well, very good, I suppose. But you know -- we {s14} can take of ourselves. It's the common folk who need a strong {s15} to look out for them, to my mind."),
##diplomacy end+
  ("you_speak_of_giving_me_land_its_kind_of_you_really_though_that_is_not_necessary", "You speak of giving me land. It's kind of you. Really, though, that is not necessary."),
##diplomacy start+: replace "by the sword" with "by the {s14}"
#  ("you_speak_of_unifying_calradia_well_maybe_you_can_unite_this_land_by_the_sword_but_im_not_sure_that_this_will_make_you_a_good_ruler", "You speak of unifying calradia. Well, maybe you can unite this land by the sword. But I'm not sure that this will make you a good ruler."),
  ("you_speak_of_unifying_calradia_well_maybe_you_can_unite_this_land_by_the_sword_but_im_not_sure_that_this_will_make_you_a_good_ruler", "You speak of unifying Europe. Well, maybe you can unite this land by the {s14}. But I'm not sure that this will make you a good ruler."),
##Replace "king" with "{s14}"
#  ("you_speak_of_claims_a_king_must_have_a_strong_legal_claim_for_there_not_to_be_chaos_in_the_realm_and_yours_is_wellestablished", "You speak of claims. A king must have a strong legal claim for there not to be chaos in the realm, and yours is well-established."),
  ("you_speak_of_claims_a_king_must_have_a_strong_legal_claim_for_there_not_to_be_chaos_in_the_realm_and_yours_is_wellestablished", "You speak of claims. A {s14} must have a strong legal claim for there not to be chaos in the realm, and yours is well-established."),
#  ("you_speak_of_claims_a_king_must_have_a_strong_legal_claim_for_there_not_to_be_chaos_in_the_realm_but_your_claim_is_not_so_strong", "You speak of claims. A king must have a strong legal claim for there not to be chaos in the realm, but your claim is not so strong."),
  ("you_speak_of_claims_a_king_must_have_a_strong_legal_claim_for_there_not_to_be_chaos_in_the_realm_but_your_claim_is_not_so_strong", "You speak of claims. A {s14} must have a strong legal claim for there not to be chaos in the realm, but your claim is not so strong."),
##Replace "king" with "{s14}", and "lords" with "{s15}"
#  ("you_speak_of_protecting_the_rights_of_lords_it_is_of_course_important_that_a_king_respect_the_rights_of_his_vassals_although_i_worry_that_a_king_who_took_a_throne_without_proper_cause_would_not_rule_with_justice", "You speak of protecting the rights of lords. It is of course important that a king respect the rights of his vassals, although I worry that a king who took a throne without proper cause would not rule with justice."),
  ("you_speak_of_protecting_the_rights_of_lords_it_is_of_course_important_that_a_king_respect_the_rights_of_his_vassals_although_i_worry_that_a_king_who_took_a_throne_without_proper_cause_would_not_rule_with_justice", "You speak of protecting the rights of lords. It is of course important that a {s14} respect the rights of his vassals, although I worry that a {s14} who took a throne without proper cause would not rule with justice."),
#  ("you_speak_of_protecting_the_rights_of_lords_it_is_of_course_important_that_a_king_respect_the_rights_of_his_vassals_however_i_would_like_to_know_that_you_would_indeed_deliver_on_your_promises", "You speak of protecting the rights of lords. It is of course important that a king respect the rights of his vassals. However, I would like to know that you would indeed deliver on your promises."),
  ("you_speak_of_protecting_the_rights_of_lords_it_is_of_course_important_that_a_king_respect_the_rights_of_his_vassals_however_i_would_like_to_know_that_you_would_indeed_deliver_on_your_promises", "You speak of protecting the rights of {s15}. It is of course important that a {s14} respect the rights of his vassals. However, I would like to know that you would indeed deliver on your promises."),

#  ("you_speak_of_protecting_the_commons_i_would_be_pleased_to_serve_a_king_who_respected_the_rights_of_his_subjects_although_i_worry_that_a_king_who_took_a_throne_without_proper_cause_would_not_rule_with_justice", "You speak of protecting the commons. I would be pleased to serve a king who respected the rights of his subjects, although I worry that a king who took a throne without proper cause would not rule with justice."),
  ("you_speak_of_protecting_the_commons_i_would_be_pleased_to_serve_a_king_who_respected_the_rights_of_his_subjects_although_i_worry_that_a_king_who_took_a_throne_without_proper_cause_would_not_rule_with_justice", "You speak of protecting the commons. I would be pleased to serve a {s14} who respected the rights of his subjects, although I worry that a {s14} who took a throne without proper cause would not rule with justice."),

#  ("you_speak_of_protecting_the_commons_i_would_be_pleased_to_serve_a_king_who_respected_the_rights_of_his_subjects_however_i_would_like_to_know_that_you_would_indeed_deliver_on_your_promises", "You speak of protecting the commons. I would be pleased to serve a king who respected the rights of his subjects. However, I would like to know that you would indeed deliver on your promises."),
  ("you_speak_of_protecting_the_commons_i_would_be_pleased_to_serve_a_king_who_respected_the_rights_of_his_subjects_however_i_would_like_to_know_that_you_would_indeed_deliver_on_your_promises", "You speak of protecting the commons. I would be pleased to serve a {s14} who respected the rights of his subjects. However, I would like to know that you would indeed deliver on your promises."),
##diplomacy end+ (finish adding alternate cultural terms)
  ("i_am_not_swayed_by_promises_of_reward", "I am not swayed by promises of reward"),
  ("you_speak_of_unifying_calradia_it_would_be_good_to_bring_peace_to_the_realm_and_i_believe_that_you_are_strong_enough_to_do_so", "You speak of unifying Europe. It would be good to bring peace to the realm, and I believe that you are strong enough to do so."),
  ("you_speak_of_unifying_calradia_it_would_be_good_to_bring_peace_the_realm_but_with_your_kingdom_in_its_current_state_i_worry_that_you_are_just_bringing_more_discord", "You speak of unifying Europe. It would be good to bring peace the realm, but with your kingdom in its current state, I worry that you are just bringing more discord."),
##diplomacy start+ duplicate definition of s15...
#at the very least, fix its defects
#  ("s15", "{!}{s15"),
  ("s15", "{!}{s15}"),
##diplomacy end+
  ("my_s11_s15", "my {s11} {s15}"),
  ("stop_gap__s15_is_the_rival_of_s16", "{!}STOP GAP - {s15} is the rival of {s16}"),
  ("my_s11_s18", "My {s11} {s18}"),
  ("the_socalled_s11_s18", "The so-called {s11} {s18}"),
##diplomacy start+ make pronouns gender-correct
#reg3 refers to the gender of the lord being spoken about, reg65 is the speaker's
  ("s18_would_cheat_me_of_my_inheritance_by_heaven_i_know_my_rights_and_im_not_going_to_back_down", "{s18} would cheat me of my inheritance. By heaven, I know my rights, and I'm not going to back down."),
  ("s18_once_questioned_my_honour_and_my_bravery_i_long_for_the_day_when_i_can_meet_him_in_battle_and_make_him_retract_his_statement", "{s18} once questioned my honour and my bravery. I long for the day when I can meet {reg3?her:him} in battle, and make {reg3?her:him} retract {reg3?her:his} statement."),
  ("s18_once_questioned_my_judgment_in_battle_by_heaven_would_he_have_us_shirk_our_duty_to_smite_our_sovereigns_foes", "{s18} once questioned my judgment in battle. By heaven, would {reg3?she:he} have us shirk our duty to smite our sovereign's foes?"),
  ("s18_seems_to_think_he_has_the_right_to_some_of_my_property_well_he_does_not", "{s18} seems to think {reg3?she:he} has the right to some of my property. Well, {reg3?she:he} does not."),
  ("s18_once_took_something_i_said_amiss_stubborn_bastard_wont_give_it_up_and_keeps_trying_to_get_me_to_recant_my_words", "{s18} once took something I said amiss. Stubborn {reg3?bitch:bastard} won't give it up, and keeps trying to get me to recant my words."),
  ("s18_is_a_crafty_weasel_and_i_dont_trust_him_one_bit", "{s18} is a crafty weasel, and I don't trust {reg3?her:him} one bit."),
  ("s18_i_despite_him_he_puts_on_such_a_nauseating_display_of_virtue_and_thinks_nothing_of_insulting_his_betters", "{s18}? I despise {reg3?her:him}. {reg3?She:He} puts on such a nauseating display of virtue, and thinks nothing of insulting {reg3?her:his} betters."),
  ("s18_entered_into_a_little_deal_with_me_and_is_now_trying_to_wriggle_out_of_it", "{s18} entered into a little deal with me and is now trying to wriggle out of it."),
  ("s18_once_ran_an_errand_for_me_and_now_thinks_i_owe_him_something_i_owe_his_ilk_nothing", "{s18} once ran an errand for me, and now thinks I owe {reg3?her:him} something. I owe {reg3?her:his} ilk nothing."),
  ("s18_is_soft_and_weak_and_not_fit_to_govern_a_fief_and_i_have_always_detested_him", "{s18} is soft, and weak, and not fit to govern a fief, and I have always detested {reg3?her:him}."),
  ("s18_is_a_quarrelsome_oaf_and_a_liability_in_my_opinion_and_ive_let_him_know_as_much", "{s18} is a quarrelsome oaf and a liability, in my opinion, and I've let {reg3?her:him} know as much."),
  ("s18_i_am_sorry_to_say_is_far_too_softhearted_a_man_to_be_given_any_kind_of_responsibility_his_chivalry_will_allow_the_enemy_to_flee_to_fight_another_day_and_will_cost_the_lives_of_my_own_faithful_men", "{s18}, I am sorry to say, is far too softhearted a {reg3?woman:man} to be given any kind of responsibility. {reg3?Her:His} chivalry will allow the enemy to flee to fight another day, and will cost the lives of my own faithful {reg65?soldiers:men}."),
  ("s18_seems_to_have_something_against_me_for_some_reason_i_dont_like_to_talk_ill_of_people_but_i_think_hes_can_be_a_bit_of_a_cad_sometimes", "{s18} seems to have something against me, for some reason. I don't like to talk ill of people, but I think {reg3?she:he} can be a bit of a cad, sometimes."),#also removed improper "'s"
  ("s18_has_always_treated_me_contemptuously_although_i_have_done_him_no_wrong", "{s18} has always treated me contemptuously, although I have done {reg3?her:him} no wrong."),
  ("s18_is_thoroughly_dishonorable_and_a_compulsive_spinner_of_intrigues_which_i_fear_will_drag_us_into_wars_or_incite_rebellions", "{s18} is thoroughly dishonorable, and a compulsive spinner of intrigues which I fear will drag us into wars or incite rebellions."),
  ("s18_disappoints_me_i_once_scolded_for_his_rashness_in_battle_and_he_took_offense_i_do_not_care_to_apologize_for_my_efforts_to_save_his_life_and_the_lives_of_his_men", "{s18} disappoints me. I once scolded {reg3?her:him} for {reg3?her:his} rashness in battle, and {reg3?she:he} took offense. I do not care to apologize for my efforts to save {reg3?her:his} life, and the lives of {reg3?her:his} {reg3?soldiers:men}."),#also added missing pronoun
  ("s18_squanders_money_and_carouses_in_a_way_most_unbefitting_a_noble_by_doing_so_he_disgraces_us_all", "{s18} squanders money and carouses in a way most unbefitting a noble. By doing so, {reg3?she:he} disgraces us all."),
  ("s18_has_been_speaking_ill_of_me_behind_my_back_or_so_they_say", "{s18} has been speaking ill of me behind my back, or so they say."),
  ("s18_is_a_disgrace_reg3shehe_consorts_with_merchants_lends_money_at_interest_uses_coarse_language_and_shows_no_attempt_to_uphold_the_dignity_of_the_honor_bestowed_upon_reg3herhim", "{s18} is a disgrace. {reg3?She:He} consorts with merchants, lends money at interest, uses coarse language, and shows no attempt to uphold the dignity of the honor bestowed upon {reg3?her:him}."),
  ("s18_has_condemned_me_for_engaging_in_commerce_what_could_possibly_be_wrong_with_that", "{s18} has condemned me for engaging in commerce. What could possibly be wrong with that?"),
  ("s18_i_have_heard_has_been_encouraging_seditious_ideas_among_the_peasantry__a_foolish_move_which_endangers_us_all", "{s18}, I have heard, has been encouraging seditious ideas among the peasantry -- a foolish move which endangers us all."),
  ("s18_has_called_me_out_for_the_way_i_deal_with_my_tenants_well_so_be_it_if_i_teach_them_that_they_are_the_equal_of_anyone_with_socalled_gentle_blood_what_is_it_to_reg3herhim", "{s18} has called me out for the way I deal with my tenants. Well, so be it. If I teach them that they are the equal of anyone with so-called 'gentle' blood, what is it to {reg3?her:him}?"),
  ("a_most_gallant_gentleman_who_knows_how_to_treat_a_lady", "a most gallant {reg3?gentlewoman:gentleman}, who knows how to treat a {reg65?lady:young man}"),
  ("a_base_cad", "a base cad"),
  ("a_man_who_treats_me_as_his_equal_which_is_rare", "{reg3?{reg65?someone:a woman}:a man} who treats me as {reg3?her:his} equal, which is rare"),
  ("appears_to_value_me_with_his_estate_and_his_horse_as_prizes_worth_having", "appears to value me with {reg3?her:his} estate and {reg3?her:his} horse as prizes worth having"),
  ("a_bit_dull_but_what_can_you_expect", "a bit dull, but what can you expect..."),
  ("the_man_whom_destiny_intends_for_me", "the {reg3?one:man} whom destiny intends for me"),
  ("is_not_right_for_me__i_cannot_say_why_but_he_makes_my_skin_crawl", "is not right for me - I cannot say why, but {reg3?she:he} makes my skin crawl"),
  ("is_a_man_who_clearly_intends_to_make_his_mark_in_the_world", "is a {reg3?woman:man} who clearly intends to make {reg3?her:his} mark in the world"),
  ("is_a_layabout_a_naif_prey_for_others_who_are_cleverer_than_he", "is a lay-about, a naif, prey for others who are cleverer than {reg3?she:he}"),
  ("is_a_man_of_stalwart_character", "is a {reg3?woman:man} of stalwart character"),
  ("appears_to_be_a_man_of_low_morals", "appears to be a {reg3?woman:man} of low morals"),
  ("appears_to_be_a_man_who_lacks_selfdiscipline", "appears to be a {reg3?woman:man} who lacks self-discipline"),
##diplomacy end+
  ("check_reg8_s4_reconciles_s5_and_s6_", "{!}Check #{reg8}: {s4} reconciles {s5} and {s6} "),
  ("diagnostic__player_should_receive_consultation_quest_here_if_not_already_active", "{!}Diagnostic -- Player should receive consultation quest here, if not already active"),
  ("check_reg8_s4_rules_in_s5s_favor_in_quarrel_with_s6_", "{!}Check #{reg8}: {s4} rules in {s5}'s favor in quarrel with {s6} "),
  ("check_reg8_new_rivalry_generated_between_s5_and_s6", "{!}Check #{reg8}: New rivalry generated between {s5} and {s6}"),
  ("check_reg8_s5_attempts_to_win_over_s6", "{!}Check #{reg8}: {s5} attempts to win over {s6}"),
  ("s1_has_no_lords", "{!}{s1} has no lords"),
  ("do_political_consequences_for_s4_victory_over_s5", "{!}Do political consequences for {s4} victory over {s5}"),
  ("bandits_attacked_a_party_on_the_roads_so_a_bounty_is_probably_available", "Bandits attacked a party on the roads, so a bounty is probably available"),
  ("travellers_attacked_on_road_from_s15_to_s16", "{!}Travellers attacked on road from {s15} to {s16}"),
  ("s15_shares_joy_of_victory_with_s16", "{!}{s15} shares joy of victory with {s16}"),
  ("faction_marshall_s15_involved_in_defeat", "{!}Faction marshall {s15} involved in defeat"),
  ("player_faction_marshall_involved_in_defeat", "{!}Player faction marshall involved in defeat"),
  ("s14_of_s15_defeated_in_battle_loses_one_point_relation_with_liege", "{!}{s14} of {s15} defeated in battle, loses one point relation with liege"),
  ("s14_defeated_in_battle_by_s15_loses_one_point_relation", "{!}{s14} defeated in battle by {s15}, loses one point relation"),
  ("s14_blames_s15_for_defeat", "{!}{s14} blames {s15} for defeat"),
  ("s32_is_undeclared_rebel", "{!}{s32} is undeclared rebel"),
  ("small_bonus_for_no_base", "{!}Small bonus for no base"),
  ("s15_considered_member_of_faction_s20_weight_of_reg15", "{!}{s15} considered member of faction {s20}, weight of {reg15}"),
  ("checking_for_recruitment_argument_reg24", "{!}Checking for recruitment argument #{reg24}"),
  ("g_talk_troop_s20_evaluates_being_vassal_to_s22_of_s21", "{!} G talk troop {s20} evaluates being vassal to {s22} of {s21}"),
  ("base_result_for_security_reg1", "{!}Base result for security: {reg1}"),
  ("result_for_security_weighted_by_personality_reg2", "{!}Result for security weighted by personality: {reg2}"),
  ("base_result_for_political_connections_reg3", "{!}Base result for political connections: {reg3}"),
  ("result_for_political_connections_weighted_by_personality_reg4", "{!}Result for political connections weighted by personality: {reg4}"),
  ("result_for_argument_strength_reg7", "{!}Result for argument strength: {reg7}"),
  ("result_for_argument_appeal_reg17", "{!}Result for argument appeal: {reg17}"),
  ("combined_result_for_argument_modified_by_persuasion_reg8", "{!}Combined result for argument modified by persuasion: {reg8}"),
  ("base_changing_sides_penalty_reg9", "{!}Base changing sides penalty: {reg9}"),
  ("changing_sides_penalty_weighted_by_personality_reg10", "{!}Changing sides penalty weighted by personality: {reg10}"),
  ("combined_bonuses_and_penalties_=_reg0", "{!}Combined bonuses and penalties = {reg0}"),
  ("intrigue_test_troop_party_is_active", "{!}Intrigue test: Troop party is active"),
  ("intrigue_test_troop_party_is_not_in_battle", "{!}Intrigue test: Troop party is not in battle"),
  ("intrigue_test_troop_is_not_prisoner", "{!}Intrigue test: Troop is not prisoner"),
  ("intrigue_test_troop_is_nearby", "{!}Intrigue test: Troop is nearby"),
  ("s20_relation_with_s15_changed_by_reg4_to_reg14", "{!}{s20} relation with {s15} changed by {reg4} to {reg14}"),
  ("total_additions_reg4", "Total additions: {reg4}"),
  ("total_subtractions_reg4", "Total subtractions: {reg4}"),
  ("checking_lord_reactions_in_s15", "{!}Checking lord reactions in {s15}"),
  ("s14_protests_the_appointment_of_s15_as_marshall", "{!}{s14} protests the appointment of {s15} as marshall"),
  ("s11_relocates_to_s10", "{s11} relocates to {s10}."),
  ("checking_s3_at_s5_with_s11_relationship_with_s4_score_reg0", "{!}Checking {s3} at {s5} with {s11} relationship with {s4} (score {reg0})"),
  ("s3_feast_concludes_at_s4", "{!}{s3} feast concludes at {s4}"),
  ("attendance_reg3_nobles_out_of_reg4", "{!}Attendance: {reg3} nobles out of {reg4}"),
  ("romantic_chemistry_reg0", "{!}DEBUG : Romantic chemistry: {reg0}"),
  ("personality_modifier_reg2", "{!}Personality modifier: {reg2}"),
  ("renown_modifier_reg3", "{!}Renown modifier: {reg3}"),
  ("final_score_reg0", "{!}Final score: {reg0}"),
  ("s4_pursues_suit_with_s5_in_s7", "{!}{s4} pursues suit with {s5} in {s7}"),
  ("note__favor_event_logged", "{!}NOTE - Favor event logged"),
  ("result_lady_forced_to_agree_to_engagement", "{!}Result: lady forced to agree to engagement"),
  ("result_lady_rejects_suitor", "{!}Result: lady rejects suitor"),
  ("result_happy_engagement_between_s4_and_s5", "{!}Result: happy engagement between {s4} and {s5}"),
  ("result_s4_elopes_with_s5", "{!}Result: {s4} elopes with {s5}"),
  ("result_s4_reluctantly_agrees_to_engagement_with_s5", "{!}Result: {s4} reluctantly agrees to engagement with {s5}"),
  ("result_stalemate_patience_roll_=_reg3", "{!}Result: stalemate, patience roll = {reg3}"),
  ("s3_marries_s4_at_s5", "{s3} marries {s4} at {s5}"),
  ("_i_must_attend_to_this_matter_before_i_worry_about_the_affairs_of_the_realm", " I must attend to this matter before I worry about the affairs of the realm."),
  ("the_other_matter_took_precedence", "The other matter took precedence."),
  ("i_cannot_leave_this_fortress_now_as_it_is_under_siege", "I cannot leave this fortress now, as it is under siege."),
  ("after_all_we_are_under_siege", "After all, we are under siege."),
  ("we_are_not_strong_enough_to_face_the_enemy_out_in_the_open", "We are not strong enough to face the enemy out in the open."),
  ("i_should_probably_seek_shelter_behind_some_stout_walls", "I should probably seek shelter behind some stout walls."),
  ("enemies_are_reported_to_be_nearby_and_we_should_stand_ready_to_either_man_the_walls_or_sortie_out_to_do_battle", "Enemies are reported to be nearby, and we should stand ready to either man the walls or sortie out to do battle."),
  ("the_enemy_is_nearby", "The enemy is nearby."),
  ("as_the_marshall_i_am_assembling_the_army_of_the_realm", "As the marshal, I am assembling the army of the realm."),
  ("as_the_marshall_i_am_assembling_the_army_of_the_realm_and_travel_to_lands_near_s10_to_inform_more_vassals", "As the marshal, I am assembling the army of the realm. We are travelling to the region of {s10} to inform more vassals."),
  ("i_intend_to_assemble_the_army_of_the_realm", "I intend to assemble the army of the realm."),
  ("as_the_marshall_i_am_leading_the_siege", "As the marshal, I am leading the siege."),
  ("i_intend_to_begin_the_siege", "I intend to begin the siege."),
  ("as_the_marshall_i_am_leading_our_raid", "As the marshal, I am leading our raid."),
  ("i_intend_to_start_our_raid", "I intend to start our raid."),
  ("as_the_marshall_i_am_leading_our_forces_in_search_of_the_enemy", "As the marshal, I am leading our forces in search of the enemy."),
  ("i_intend_to_lead_our_forces_out_to_find_the_enemy", "I intend to lead our forces out to find the enemy."),
  ("as_the_marshall_i_am_leading_our_forces_to_engage_the_enemy_in_battle", "As the marshal, I am leading our forces to engage the enemy in battle."),
  ("i_intend_to_lead_our_forces_out_to_engage_the_enemy", "I intend to lead our forces out to engage the enemy."),
  ("i_dont_have_enough_troops_and_i_need_to_get_some_more", "I don't have enough troops, and I need to get some more."),
  ("i_am_running_low_on_troops", "I am running low on troops."),
  ("we_are_following_your_direction", "We are following your direction."),
  ("i_need_to_make_preparations_for_your_wedding", "I need to make preparations for your wedding."),
  ("after_all_i_need_to_make_preparations_for_your_wedding", "After all, I need to make preparations for your wedding."),
  ("i_am_heading_to_the_site_of_our_wedding", "I am heading to the site of our wedding."),
  ("after_all_we_are_soon_to_be_wed", "After all, we are soon to be wed!"),
  ("i_am_hosting_a_feast_there", "I am hosting a feast there."),
  ("i_have_a_feast_to_host", "I have a feast to host."),
  ("i_am_to_be_the_bridegroom_there", "I am to be the bridegroom there."),
  ("my_wedding_day_draws_near", "My wedding day draws near."),
  ("i_have_too_much_loot_and_too_many_prisoners_and_need_to_secure_them", "I have too much loot and too many prisoners, and need to secure them."),
  ("i_should_think_of_dropping_off_some_of_my_prisoners", "I should think of dropping off some of my prisoners."),
  ("i_need_to_reinforce_it_as_it_is_poorly_garrisoned", "I need to reinforce it, as it is poorly garrisoned."),
  ("there_is_a_hole_in_our_defenses", "There is a hole in our defenses."),
  ("i_am_following_the_marshals_orders", "I am following the marshal's orders."),
  ("the_marshal_has_given_me_this_command", "The marshal has given me this command."),
  ("i_am_answering_the_marshals_summons", "I am answering the marshal's summons."),
  ("our_realm_needs_my_support_there_is_enemy_raiding_one_of_our_villages_which_is_not_to_far_from_here_i_am_going_there", "Our realm needs my support. There is enemy raiding one of our villages which is not to far from here. I am going there."),
  ("the_marshal_has_issued_a_summons", "The marshal has issued a summons."),
  ("comradeinarms", "comrade-in-arms."),
  ("i_am_supporting_my_s11_s10", "I am supporting my {s11} {s10}."),
  ("i_believe_that_one_of_my_comrades_is_in_need", "I believe that one of my comrades is in need."),
  ("s20_decided_to_attack_s21", "{!}{s20} decided to attack {s21}."),
  ("a_fortress_is_vulnerable", "A fortress is vulnerable."),
  ("i_believe_that_the_enemy_may_be_vulnerable", "I believe that the enemy may be vulnerable."),
  ("i_need_to_inspect_my_properties_and_collect_my_dues", "I need to inspect my properties and collect my dues."),
  ("it_has_been_too_long_since_i_have_inspected_my_estates", "It has been too long since I have inspected my estates."),
  ("my_men_are_weary_so_we_are_returning_home", "My men are weary, so we are returning home."),
  ("my_men_are_becoming_weary", "My men are becoming weary."),
  ("i_have_a_score_to_settle_with_the_lord_there", "I have a score to settle with the lord there."),
  ("i_am_thinking_of_settling_an_old_score", "I am thinking of settling an old score."),
  ("i_am_short_of_money_and_i_hear_that_there_is_much_wealth_there", "I am short of money, and I hear that there is much wealth there."),
  ("i_need_to_refill_my_purse_preferably_with_the_enemys_money", "I need to refill my purse, preferably with the enemy's money."),
  ("by_striking_at_the_enemys_richest_lands_perhaps_i_can_draw_them_out_to_battle", "By striking at the enemy's richest lands, perhaps I can draw them out to battle!"),
  ("i_am_thinking_of_going_on_the_attack", "I am thinking of going on the attack."),
  ("perhaps_if_i_strike_one_more_blow_we_may_end_this_war_on_our_terms_", "Perhaps, if I strike one more blow, we may end this war on our terms. "),
  ("we_may_be_able_to_bring_this_war_to_a_close_with_a_few_more_blows", "We may be able to bring this war to a close with a few more blows."),
  ("i_wish_to_attend_the_feast_there", "I wish to attend the feast there."),
  ("there_is_a_feast_which_i_wish_to_attend", "There is a feast which I wish to attend."),
  ("there_is_a_fair_lady_there_whom_i_wish_to_court", "There is a fair lady there, whom I wish to court."),
  ("i_have_the_inclination_to_pay_court_to_a_fair_lady", "I have the inclination to pay court to a fair lady."),
  ("we_have_heard_reports_that_the_enemy_is_in_the_area", "We have heard reports that the enemy is in the area."),
  ("i_have_heard_reports_of_enemy_incursions_into_our_territory", "I have heard reports of enemy incursions into our territory."),
  ("i_need_to_spend_some_time_with_my_household", "I need to spend some time with my household."),
  ("it_has_been_a_long_time_since_i_have_been_able_to_spend_time_with_my_household", "It has been a long time since I have been able to spend time with my household."),
  ("i_am_watching_the_borders", "I am watching the borders."),
  ("i_may_be_needed_to_watch_the_borders", "I may be needed to watch the borders."),
  ("i_will_guard_the_areas_near_my_home", "I will guard the areas near my home..."),
  ("i_am_perhaps_needed_most_at_home", "I am perhaps needed most at home."),
  ("i_cant_think_of_anything_better_to_do", "I can't think of anything better to do..."),
  ("i_am_completing_what_i_have_already_begun", "I am completing what I have already begun."),
  ("i_dont_even_have_a_home_to_which_to_return", "I don't even have a home to which to return."),
  ("debug__s10_decides_s14_faction_ai_s15", "{!}DEBUG : {s10} decides: {s14} (faction AI: {s15})"),
  ("_i_am_acting_independently_because_no_marshal_is_appointed", " I am acting independently, because no marshal is appointed."),
  ("_i_am_acting_independently_because_our_marshal_is_currently_indisposed", " I am acting independently, because our marshal is currently indisposed."),
  ("_i_am_acting_independently_because_our_realm_is_currently_not_on_campaign", " I am acting independently, because our realm is currently not on campaign."),
  ("_i_am_not_accompanying_the_marshal_because_i_fear_that_he_may_lead_us_into_disaster", " I am not accompanying the marshal, because I fear that he may lead us into disaster."),
  ("i_am_not_accompanying_the_marshal_because_i_question_his_judgment", " I am not accompanying the marshal, because I question his judgment."),
  ("i_am_not_accompanying_the_marshal_because_i_can_do_greater_deeds", " I am not accompanying the marshal, because I can do greater deeds."),
  ("_s16_has_kept_us_on_campaign_on_far_too_long_and_there_are_other_pressing_matters_to_which_i_must_attend", " {s16} has kept us on campaign on far too long, and there are other pressing matters to which I must attend."),
  ("_i_am_not_participating_in_the_marshals_campaign_because_i_do_not_know_where_to_find_our_main_army", " I am not participating in the marshal's campaign, because I do not know where to find our main army."),
  ("_i_am_acting_independently_although_some_enemies_have_been_spotted_within_our_borders_they_havent_come_in_force_and_the_local_troops_should_be_able_to_dispatch_them", " I am acting independently. Although some enemies have been spotted within our borders, they haven't come in force and the local troops should be able to dispatch them."),
  ("_the_needs_of_the_realm_must_come_first", " The needs of the realm must come first."),
  ("we_are_likely_to_be_overwhelmed_by_the_s9_let_each_defend_their_own", "We are likely to be overwhelmed by the {s9}. Let each defend their own."),
  ("we_should_see_this_siege_through", "We should see this siege through."),
  ("we_should_prepare_to_defend_s21_but_we_should_gather_our_forces_until_we_are_strong_enough_to_engage_them", "We should prepare to defend {s21}, but we should gather our forces until we are strong enough to engage them."),
  ("we_should_prepare_to_defend_s21_but_first_we_have_to_gather", "We should prepare to defend {s21}. But first we have to gather our army."),
  ("we_should_ride_to_break_the_siege_of_s21", "We should ride to break the siege of {s21}."),
  ("we_should_ride_to_defeat_the_enemy_gathered_near_s21", "We should ride to defeat the enemy gathered near {s21}."),
  ("we_have_located_s21s_army_and_we_should_engage_it", "We have located {s21}'s army, and we should engage it."),
  ("this_offensive_needs_to_wind_down_soon_so_the_vassals_can_attend_to_their_own_business", "This offensive needs to wind down soon, so the vassals can attend to their own business."),
  ("the_vassals_are_tired_we_let_them_rest_for_some_time", "The vassals are tired of campaigning. We should let them rest for some time."),
  ("the_vassals_still_need_time_to_attend_to_their_own_business", "The vassals still need time to attend to their own business."),
  ("it_is_time_to_go_on_the_offensive_and_we_must_first_assemble_the_army", "It is time to go on the offensive, and we must first assemble the army."),
  ("we_must_continue_to_gather_the_army_before_we_ride_forth_on_an_offensive_operation", "We have only assembled a few vassals, but we must continue to gather the army before we ride forth on an offensive operation."),
  #("there_is_no_need_to_beat_around_the_borders__we_can_take_them_out_with_a_strike_to_the_heart", "There is no need to beat around the borders, we can take them out with a strike to the heart!"),
  ("there_is_no_need_to_beat_around_the_borders__we_can_take_one_of_their_important_towns", "There is no need to beat around the borders, we can take one of their important towns."),
  ("we_should_exploit_our_success_over_s21_by_seizing_one_of_their_fortresses", "We should exploit our success over {s21} by seizing one of their fortresses."),
  ("we_shall_leave_a_fiery_trail_through_the_heart_of_the_enemys_lands_targeting_the_wealthy_settlements_if_we_can", "We shall leave a fiery trail through the heart of the enemy's lands, targeting the wealthy settlements if we can."),
  ("the_army_will_be_disbanded_because_we_have_been_waiting_too_long_without_a_target", "The army will be disbanded, because we have been waiting too long without a target."),
  ("it_is_time_for_the_feast_to_conclude", "It is time for the feast to conclude."),
  ("we_should_continue_the_feast_unless_there_is_an_emergency", "We should continue the feast, unless there is an emergency."),
  ("you_had_wished_to_hold_a_feast", "You had wished to hold a feast."),
  ("your_wedding_day_approaches_my_lady", "Your wedding day approaches, my lady."),
  ("your_wedding_day_approaches", "Your wedding day approaches."),
  ("s22_and_s23_wish_to_marry", "{s22} and {s23} wish to marry."),
  ("it_has_been_a_long_time_since_the_lords_of_the_realm_gathered_for_a_feast", "It has been a long time since the lords of the realm gathered for a feast."),
  ("the_circumstances_which_led_to_this_decision_no_longer_apply_so_we_should_stop_and_reconsider_shortly", "The circumstances which led to this decision no longer apply, so we should stop and reconsider shortly."),
  ("we_cant_think_of_anything_to_do", "{!}ERROR -- We can't think of anything to do."),
  ("s15_is_at_war_with_s16_", "{s15} is at war with {s16}. "),
  ("in_the_short_term_s15_has_a_truce_with_s16_as_a_matter_of_general_policy_", "In the short term, {s15} has a truce with {s16}. As a matter of general policy, "),
  ("in_the_short_term_s15_was_recently_provoked_by_s16_and_is_under_pressure_to_declare_war_as_a_matter_of_general_policy_", "In the short term, {s15} was recently provoked by {s16}, and is under pressure to declare war. As a matter of general policy, "),
  ("envoymodified_diplomacy_score_honor_plus_relation_plus_envoy_persuasion_=_reg4", "{!}Envoy-modified diplomacy score (honor plus relation plus envoy persuasion) = {reg4}"),
  ("s12s15_cannot_negotiate_with_s16_as_to_do_so_would_undermine_reg4herhis_own_claim_to_the_throne_this_civil_war_must_almost_certainly_end_with_the_defeat_of_one_side_or_another", "{s12}{s15} cannot negotiate with {s16}, as to do so would undermine {reg4?her:his} own claim to the throne. This civil war must almost certainly end with the defeat of one side or another."),
  ("s12s15_considers_s16_to_be_dangerous_and_untrustworthy_and_shehe_wants_to_bring_s16_down", "{s12}{s15} considers {s16} to be dangerous and untrustworthy, and {reg4?she:he} wants to bring {s16} down."),
  ("s12s15_is_anxious_to_reclaim_old_lands_such_as_s18_now_held_by_s16", "{s12}{s15} is anxious to reclaim old lands such as {s18}, now held by {s16}."),
  ("s12s15_feels_that_reg4shehe_is_winning_the_war_against_s16_and_sees_no_reason_not_to_continue", "{s12}{s15} feels that {reg4?she:he} is winning the war against {s16}, and sees no reason not to continue."),
  ("s12s15_faces_too_much_internal_discontent_to_feel_comfortable_ignoring_recent_provocations_by_s16s_subjects", "{s12}{s15} faces too much internal discontent to feel comfortable ignoring recent provocations by {s16}'s subjects."),
  ("s12even_though_reg4shehe_is_fighting_on_two_fronts_s15_is_inclined_to_continue_the_war_against_s16_for_a_little_while_longer_for_the_sake_of_honor", "{s12}Even though {reg4?she:he} is fighting on two fronts, {s15} is inclined to continue the war against {s16} for a little while longer, for the sake of honor."),
  ("s12s15_feels_that_reg4shehe_must_pursue_the_war_against_s16_for_a_little_while_longer_for_the_sake_of_honor", "{s12}{s15} feels that {reg4?she:he} must pursue the war against {s16} for a little while longer, for the sake of honor."),
  ("s12s15_is_currently_on_the_offensive_against_s17_now_held_by_s16_and_reluctant_to_negotiate", "{s12}{s15} is currently on the offensive against {s17}, now held by {s16}, and reluctant to negotiate."),
  ("s12s15_is_alarmed_by_the_growing_power_of_s16", "{s12}{s15} is alarmed by the growing power of {s16}."),
  ("s12s15_distrusts_s16_and_fears_that_any_deals_struck_between_the_two_realms_will_not_be_kept", "{s12}{s15} distrusts {s16}, and fears that any deals struck between the two realms will not be kept."),
  ("s12s15_is_at_war_on_too_many_fronts_and_eager_to_make_peace_with_s16", "{s12}{s15} is at war on too many fronts, and eager to make peace with {s16}."),
  ("s12s15_seems_to_think_that_s16_and_reg4shehe_have_a_common_enemy_in_the_s17", "{s12}{s15} seems to think that {s16} and {reg4?she:he} have a common enemy in the {s17}."),
  ("s12s15_feels_frustrated_by_reg4herhis_inability_to_strike_a_decisive_blow_against_s16", "{s12}{s15} feels frustrated by {reg4?her:his} inability to strike a decisive blow against {s16}."),

  ("s12s15_has_suffered_enough_in_the_war_with_s16_for_too_little_gain_and_is_ready_to_pursue_a_peace", "{s12}{s15} has suffered enough in the war with {s16}, for too little gain, and is ready to pursue a peace."),
  ("s12s15_has_suffered_enough_in_the_war_with_s16_for_too_little_gain_and_is_ready_to_pursue_a_peace_2", "{s12}{s15} has suffered too much in the war with {s16}, for no gain, and is ready to pursue a peace."),
  ("s12s15_has_suffered_enough_in_the_war_with_s16_for_too_little_gain_and_is_ready_to_pursue_a_peace_3", "{s12}{s15} has suffered too much in the war with {s16} and is ready to pursue a peace."),
#
#new wargoal:
  ("s12s15_dominates_its_weaker_neighbor_s16", "{s12}{s15} attempts to dominate his weaker neighbor {s16}."),	#MOTO for new diplomatic result
  ("s12s15_acts_to_drive_the_people_of_s16_and_their_like_out_of_the_Isles", "{s12}{s15} acts to kill the people of {s16}!"),	#MOTO for new diplomatic result


  ("s12s15_would_like_to_firm_up_a_truce_with_s16_to_respond_to_the_threat_from_the_s17", "{s12}{s15} would like to firm up a truce with {s16} to respond to the threat from the {s17}."),
  ("s12s15_wishes_to_be_at_peace_with_s16_so_as_to_pursue_the_war_against_the_s17", "{s12}{s15} wishes to be at peace with {s16} so as to pursue the war against the {s17}."),
  ("s12s15_seems_to_be_intimidated_by_s16_and_would_like_to_avoid_hostilities", "{s12}{s15} seems to be intimidated by {s16}, and would like to avoid hostilities."),
  ("s12s15_has_no_particular_reason_to_continue_the_war_with_s16_and_would_probably_make_peace_if_given_the_opportunity", "{s12}{s15} has no particular reason to continue the war with {s16}, and would probably make peace if given the opportunity."),
  ("s12s15_seems_to_be_willing_to_improve_relations_with_s16", "{s12}{s15} seems to be willing to improve relations with {s16}."),
  ("excuse_me_how_can_you_possibly_imagine_yourself_worthy_to_marry_into_our_family", "Excuse me? How can you possibly imagine yourself worthy to marry into our family?"),
    ("em_with_regard_to_her_ladyship_we_were_looking_specifically_for_a_groom_of_some_distinction_fight_hard_count_your_dinars_and_perhaps_some_day_in_the_future_we_may_speak_of_such_things_my_good_man", "Em... With regard to her ladyship, we were looking specifically for a {groom/bride} of some distinction. Fight hard, count your siliquae, and perhaps some day in the future we may speak of such things, my good {man/woman}!"), #dckplmc start+
  ("em_with_regard_to_her_ladyship_we_were_looking_specifically_for_a_groom_of_some_distinction", "Em... With regard to her ladyship, we were looking specifically for a {groom/bride} of some distinction."),
  ("it_is_too_early_for_you_to_be_speaking_of_such_things_you_are_still_making_your_mark_in_the_world", "It is too early for you to be speaking of such things. You are still making your mark in the world."),
  ("you_dont_serve_the_s4_so_id_say_no_one_day_we_may_be_at_war_and_i_prefer_not_to_have_to_kill_my_inlaws_if_at_all_possible", "You don't serve the {s4}, so I'd say no. One day we may be at war, and I prefer not to have to kill my in-laws, if at all possible."),
  ("as_you_are_not_a_vassal_of_the_s4_i_must_decline_your_request_the_twists_of_fate_may_mean_that_we_will_one_day_cross_swords_and_i_would_hope_not_to_make_a_widow_of_a_lady_whom_i_am_obligated_to_protect", "As you are not a vassal of the {s4}, I must decline your request. The twists of fate may mean that we will one day cross swords, and I would hope not to make a widow of a lady whom I am obligated to protect."),
  ("as_you_are_not_a_pledged_vassal_of_our_liege_with_the_right_to_hold_land_i_must_refuse_your_request_to_marry_into_our_family", "As you are not a pledged vassal of our liege, with the right to hold land, I must refuse your request to marry into our family."),
  ("look_here_lad__the_young_s14_has_been_paying_court_to_s16_and_youll_have_to_admit__hes_a_finer_catch_for_her_than_you_so_lets_have_no_more_of_this_talk_shall_we", "Look here, {lad/lass} -- the young {s14} has been paying court to {s16}, and you'll have to admit -- he's a finer catch for her than you. So let's have no more of this talk, shall we?"),
  ("i_do_not_care_for_you_sir_and_i_consider_it_my_duty_to_protect_the_ladies_of_my_household_from_undesirable_suitors", "I do not care for you, {sir/madam}, and I consider it my duty to protect the ladies of my household from undesirable suitors..."),
  ("hmm_young_girls_may_easily_be_led_astray_so_out_of_a_sense_of_duty_to_the_ladies_of_my_household_i_think_i_would_like_to_get_to_know_you_a_bit_better_we_may_speak_of_this_at_a_later_date", "Hmm. Young girls may easily be led astray, so out of a sense of duty to the ladies of my household, I think I would like to get to know you a bit better. We may speak of this at a later date."), #dckplmc end+
  ("you_may_indeed_make_a_fine_match_for_the_young_mistress", "You may indeed make a fine match for the young mistress."),
#diplomacy start+ (players of either gender may marry opposite-gender lords)
  ("madame__given_our_relations_in_the_past_this_proposal_is_most_surprising_i_do_not_think_that_you_are_the_kind_of_woman_who_can_be_bent_to_a_hushands_will_and_i_would_prefer_not_to_have_our_married_life_be_a_source_of_constant_acrimony", "{Sir/Madame} -- given our relations in the past, this proposal is most surprising. I do not think that you are the kind of {man/woman} who can be bent to a {wife/husband}'s will, and I would prefer not to have our married life be a source of constant acrimony."),
  ("i_would_prefer_to_marry_a_proper_maiden_who_will_obey_her_husband_and_is_not_likely_to_split_his_head_with_a_sword", "I would prefer to marry a proper {lord/maiden} who will {cherish/obey} {his/her} {wife/husband}, and is not likely to split {her/his} head with a sword."),
  ("my_lady_while_i_admire_your_valor_you_will_forgive_me_if_i_tell_you_that_a_woman_like_you_does_not_uphold_to_my_ideal_of_the_feminine_of_the_delicate_and_of_the_pure", "My {lord/lady}, while I admire your valor and your beauty, you will forgive me if I tell you that a {man/woman} like you does not uphold to my ideal of a {husband/wife}: {masculine/feminine}, delicate, and pure."),#this sounds ridiculous -- don't use the male version
  ("nah_i_want_a_woman_wholl_keep_quiet_and_do_what_shes_told_i_dont_think_thats_you", "Nah. I want a {man/woman} who'll keep quiet and do what {he/she}'s told. I don't think that's you."),
  ("my_lady_you_are_possessed_of_great_charms_but_no_properties_until_you_obtain_some_to_marry_you_would_be_an_act_of_ingratitude_towards_my_ancestors_and_my_lineage", "My {lord/lady}, you are possessed of great charms, but no properties. Until you obtain some, to marry you would be an act of ingratitude towards my ancestors and my lineage."),
  ("my_lady_you_are_a_woman_of_no_known_family_of_no_possessions__in_short_a_nobody_do_you_think_that_you_are_fit_to_marry_into_may_family", "My {lord/lady}, you are a {man/woman} of no known family, of no possessions -- in short, a nobody. Do you think that you are fit to marry into may family?"),
  ("my_lady__forgive_me__the_quality_of_our_bond_is_not_of_the_sort_which_the_poets_tell_us_is_necessary_to_sustain_a_happy_marriage", "My {lord/lady} -- forgive me -- the quality of our bond is not of the sort which the poets tell us is necessary to sustain a happy marriage."),
  ("um_i_think_that_if_i_want_to_stay_on_s4s_good_side_id_best_not_marry_you", "Um, I think that if I want to stay on {s4}'s good side, I'd best not marry you."),
  ("you_serve_another_realm_i_dont_see_s4_granting_reg4herhis_blessing_to_our_union", "You serve another realm. I don't see {s4} granting {reg4?her:his} blessing to our union."),
  ("madame_my_heart_currently_belongs_to_s4", "{Sir/Madame}, my heart currently belongs to {s4}."),
  ("my_lady_you_are_a_woman_of_great_spirit_and_bravery_possessed_of_beauty_grace_and_wit_i_shall_give_your_proposal_consideration", "My {lord/lady}, you are a {man/woman} of great spirit and bravery, possessed of {strength/beauty}, {courage/grace}, and wit. I shall give your proposal consideration."),
  ("my_lady_you_are_a_woman_of_great_spirit_and_bravery_possessed_of_beauty_grace_and_wit_i_would_be_most_honored_were_you_to_become_my_wife", "My {lord/lady}, you are a {man/woman} of great spirit and bravery, possessed of {strength/beauty}, {courage/grace}, and wit. I would be most honored were you to become my {husband/wife}."),
#diplomacy end+
  ("poem_choice_reg4_lady_rep_reg5", "{!}Poem choice: {reg4}, lady rep: {reg5}"),
  ("ah__kais_and_layali__such_a_sad_tale_many_a_time_has_it_been_recounted_for_my_family_by_the_wandering_poets_who_come_to_our_home_and_it_has_never_failed_to_bring_tears_to_our_eyes", "Ah -- 'Kais and Layali' -- such a sad tale. Many a time has it been recounted for my family by the wandering poets who come to our home, and it has never failed to bring tears to our eyes."),
  ("kais_and_layali_three_hundred_stanzas_of_pathetic_sniveling_if_you_ask_me_if_kais_wanted_to_escape_heartbreak_he_should_have_learned_to_live_within_his_station_and_not_yearn_for_what_he_cannot_have", "'Kais and Layali'? Three hundred stanzas of pathetic sniveling, if you ask me. If Kais wanted to escape heartbreak, he should have learned to live within his station, and not yearn for what he cannot have."),
  ("kais_and_layali_no_one_should_ever_have_written_such_a_sad_poem_if_it_was_the_destiny_of_kais_and_layali_to_be_together_than_their_love_should_have_conquered_all_obstacles", "'Kais and Layali'? No one should ever have written such a sad poem! If it was the destiny of Kais and Layali to be together, than their love should have conquered all obstacles!"),
  ("ah_kais_and_layali_a_very_old_standby_but_moving_in_its_way", "Ah, 'Kais and Layali.' A very old stand-by, but moving, in its way."),
  ("the_saga_of_helgered_and_kara_such_happy_times_in_which_our_ancestors_lived_women_like_kara_could_venture_out_into_the_world_like_men_win_a_name_for_themselves_and_not_linger_in_their_husbands_shadow", "The saga of 'Helgered and Kara'? Such happy times in which our ancestors lived! Women like Kara could venture out into the world like men, win a name for themselves, and not linger in their husbands' shadow."),
  ("ah_the_saga_of_helgered_and_kara_now_there_was_a_lady_who_knew_what_she_wanted_and_was_not_afraid_to_obtain_it", "Ah, the saga of 'Helgered and Kara'. Now there was a lady who knew what she wanted, and was not afraid to obtain it."),
  ("the_saga_of_helgered_and_kara_a_terrible_tale__but_it_speaks_of_a_very_great_love_if_she_were_willing_to_make_war_on_her_own_family", "The saga of 'Helgered and Kara'? A terrible tale - but it speaks of a very great love, if she were willing to make war on her own family."),
  ("the_saga_of_helgered_and_kara_as_i_recall_kara_valued_her_own_base_passions_over_duty_to_her_family_that_she_made_war_on_her_own_father_i_have_no_time_for_a_poem_which_praises_such_a_woman", "The saga of 'Helgered and Kara'? As I recall, Kara valued her own base passions over duty to her family that she made war on her own father. I have no time for a poem which praises such a woman!"),
  ("the_saga_of_helgered_and_kara_how_could_a_woman_don_armor_and_carry_a_sword_how_could_a_man_love_so_ungentle_a_creature", "The saga of 'Helgered and Kara'? How could a woman don armor and carry a sword! How could a man love so ungentle a creature!"),
  ("a_conversation_in_the_garden_i_cannot_understand_the_lady_in_that_poem_if_she_loves_the_man_why_does_she_tease_him_so", "'A Conversation in the Garden'? I cannot understand the lady in that poem. If she loves the man, why does she tease him so?"),
  ("a_conversation_in_the_garden_let_us_see__it_is_morally_unedifying_it_exalts_deception_it_ends_with_a_maiden_surrendering_to_her_base_passions_and_yet_i_cannot_help_but_find_it_charming_perhaps_because_it_tells_us_that_love_need_not_be_tragic_to_be_memorable", "'A Conversation in the Garden'? Let us see -- it is morally unedifying, it exalts deception, it ends with a maiden surrendering to her base passions... And yet I cannot help but find it charming, perhaps because it tells us that love need not be tragic to be memorable."),
  ("a_conversation_in_the_garden_now_that_is_a_tale_every_lady_should_know_by_heart_to_learn_the_subtleties_of_the_politics_she_must_practice", "'A Conversation in the Garden'? Now that is a tale every lady should know by heart, to learn the subtleties of the politics she must practice!"),
  ("a_conversation_in_the_garden_it_is_droll_i_suppose__although_there_is_nothing_there_that_truly_stirs_my_soul", "'A Conversation in the Garden'? It is droll, I suppose -- although there is nothing there that truly stirs my soul."),
  ("storming_the_fortress_of_love_ah_yes_the_lady_sits_within_doing_nothing_while_the_man_is_the_one_who_strives_and_achieves_i_have_enough_of_that_in_my_daily_life_why_listen_to_poems_about_it", "'Storming the Fortress of Love'? Ah, yes. The lady sits within doing nothing, while the man is the one who strives and achieves. I have enough of that in my daily life. Why listen to poems about it?"),
  ("storming_the_fortress_of_love_ah_yes_an_uplifting_tribute_to_the_separate_virtues_of_man_and_woman", "'Storming the Fortress of Love'? Ah, yes. An uplifting tribute to the separate virtues of man and woman."),
  ("storming_the_fortress_of_love_ah_yes_but_although_it_is_a_fine_tale_of_virtues_it_speaks_nothing_of_passion", "'Storming the Fortress of Love'? Ah, yes. But although it is a fine tale of virtues, it speaks nothing of passion!"),
  ("storming_the_fortress_of_love_ah_a_sermon_dressed_up_as_a_love_poem_if_you_ask_me", "'Storming the Fortress of Love'? Ah... A sermon dressed up as a love poem, if you ask me."),
  ("a_hearts_desire_ah_such_a_beautiful_account_of_the_perfect_perfect_love_to_love_like_that_must_be_to_truly_know_rapture", "'A Heart's Desire'? Ah, such a beautiful account of the perfect, perfect love! To love like that must be to truly know rapture!"),
  ("a_hearts_desire_silly_if_you_ask_me_if_the_poet_desires_a_lady_then_he_should_endeavor_to_win_her__and_not_dress_up_his_desire_with_a_pretense_of_piety", "'A Heart's Desire'? Silly, if you ask me. If the poet desires a lady, then he should endeavor to win her -- and not dress up his desire with a pretense of piety!"),
  ("a_hearts_desire_hmm__it_is_an_interesting_exploration_of_earthly_and_divine_love_it_does_speak_of_the_spiritual_quest_which_brings_out_the_best_in_man_but_i_wonder_if_the_poet_has_not_confused_his_yearning_for_higher_things_with_his_baser_passions", "'A Heart's Desire'? Hmm -- it is an interesting exploration of earthly and divine love. It does speak of the spiritual quest which brings out the best in man, but I wonder if the poet has not confused his yearning for higher things with his baser passions."),
  ("a_hearts_desire_oh_yes__it_is_very_worthy_and_philosophical_but_if_i_am_to_listen_to_a_bard_strum_a_lute_for_three_hours_i_personally_prefer_there_to_be_a_bit_of_a_story", "'A Heart's Desire'? Oh, yes -- it is very worthy and philosophical. But if I am to listen to a bard strum a lute for three hours, I personally prefer there to be a bit of a story."),
  ("result_reg4_string_s11", "{!}Result: {reg4}. String: {s11}"),
  ("calculating_effect_for_policy_for_s3", "{!}Calculating effect for policy for {s3}"),
  ("reg3_units_of_s4_for_reg5_guests_and_retinue", "{reg3} units of {s4} for {reg5} guests and retinue"),
  ("reg3_units_of_spice_of_reg5_to_be_consumed", "{reg3} units of spice of {reg5} to be consumed"),
  ("reg3_units_of_oil_of_reg5_to_be_consumed", "{reg3} units of oil of {reg5} to be consumed"),
  ("of_food_which_must_come_before_everything_else_the_amount_is_s8", "Of food, which must come before everything else, the amount is {s8}"),
  ("s9_and_the_variety_is_s8_", "{s9} and the variety is {s8}. "),
  ("s9_of_drink_which_guests_will_expect_in_great_abundance_the_amount_is_s8", "{s9} Of drink, which guests will expect in great abundance, the amount is {s8}"),
  ("s9_of_spice_which_is_essential_to_demonstrate_that_we_spare_no_expense_as_hosts_the_amount_is_s8_", "{s9} Of spice, which is essential to demonstrate that we spare no expense as hosts, the amount is {s8}. "),
  ("s9_of_oil_which_we_shall_require_to_light_the_lamps_the_amount_is_s8", "{s9} Of oil, which we shall require to light the lamps, the amount is {s8}."),
  ("s9_overall_our_table_will_be_considered_s8", "{s9} Overall, our table will be considered {s8}."),
  ("rebel", "rebel"),
  ("bandit", "bandit"),
  ("relation_of_prisoner_with_captor_is_reg0", "relation of prisoner with captor is {reg0}"),
  ("s5_suffers_attrition_reg3_x_s4", "{s5} suffers attrition: {reg3} x {s4}"),
  ("s65", "{!}{s65}"),
  ("s10_said_on_s1_s11__", "{s10} said on {s1}: {s11}^^"),
  ("rumor_note_to_s3s_slot_reg4_s5", "{!}Rumor note to {s3}'s slot {reg4}: {s5}"),
  ("totalling_casualties_caused_during_mission", "Totalling casualties caused during mission..."),
  ("removing_s4_from_s5", "Removing {s4} from {s5}"),
  ("s4_joins_prison_break", "{s4} joins prison break"),
  ("helper_is_spawned", "helper is spawned."),
  ("leaving_area_during_prison_break", "Leaving area during prison break"),
  ("talk_to_the_trainer", "Talk to the trainer."),
  ("woman", "woman"),
  ("man", "man"),
  ("noble", "noble"),
  ("common", "common"),
  ("may_find_that_you_are_able_to_take_your_place_among_calradias_great_lords_relatively_quickly", "may find that you are able to take your place among Europe's great generals relatively quickly"),
  ("may_face_some_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords", "may face some difficulties establishing yourself as an equal among Europe's great generals"),
  ("may_face_great_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords", "may face great difficulties establishing yourself as an equal among Europe's great generals"),
  ("current_party_morale_is_reg5_current_party_morale_modifiers_are__base_morale__50_party_size_s2reg1_leadership_s3reg2_food_variety_s4reg3s5s6_recent_events_s7reg4_total__reg5___", "Current party morale is {reg5}.^Current party morale modifiers are:^^Base morale:  +{reg6}^Party size: {s2}{reg1}^Leadership: {s3}{reg2}^Food variety: {s4}{reg3}{s5}{s6}^Recent events: {s7}{reg4}^TOTAL:  {reg5}^^^"),
  ("s1extra_morale_for_s9_troops__reg6_", "{s1}Extra morale for {s9} troops : {reg6}.{reg7}^"), #SB : decimal
  ("courtships_in_progress_", "Courtships in progress:^"),
  ("s1_s2_relation_reg3_last_visit_reg4_days_ago", "{s1}^{s2}, relation {reg3}, last visit {reg4} days ago"),
  ("s1__poems_known", "{s1}^^Poems known:"),
  ("s1_storming_the_castle_of_love_allegoric", "{s1}^Storming the Castle of Love (Allegoric)"),
  ("s1_kais_and_layali_tragic", "{s1}^Kais and Layali (Tragic)"),
  ("s1_a_conversation_in_the_garden_comic", "{s1}^A Conversation in the Garden (Comic)"),
  ("s1_helgered_and_kara_epic", "{s1}^Helgered and Kara (Epic)"),
  ("s1_a_hearts_desire_mystic", "{s1}^A Heart's Desire (Mystic)"),
  ("no_companions_in_service", "No companions in service"),
  ("gathering_support", "Gathering support"),
  ("expected_back_imminently", "Expected back imminently"),
  ("expected_back_in_approximately_reg3_days", "Expected back in approximately {reg3} days"),
  ("gathering_intelligence", "Gathering intelligence in {s9}"), #SB : in {s9}
  ("diplomatic_embassy_to_s9", "Diplomatic embassy to {s9}"),
  ("serving_as_minister", "Serving as minister"),
  ("in_your_court_at_s9", "In your court at {s9}"),
  ("under_arms", "Under arms"),
  ("in_your_party", "In your party"),
  ("s4_s8_s5", "{!}{s4}: {s8} ({s5})"),
  ("s2_s3", "{!}{s2}^{s3}"),
  ("attacking_enemy_army_near_s11", "Attacking enemy army near {s11}"),
  ("holding_feast_at_s11", "Holding feast at {s11}"),
  ("sfai_reg4", "{!}SFAI: {reg4}"),
  ("s9s10_current_state_s11_hours_at_current_state_reg3_current_strategic_thinking_s14_marshall_s12_since_the_last_offensive_ended_reg4_hours_since_the_decisive_event_reg10_hours_since_the_last_rest_reg9_hours_since_the_last_feast_ended_reg5_hours_percent_disgruntled_lords_reg7_percent_restless_lords_reg8__", "{s9}{s10}^Current state: {s11}^Hours at current state: {reg3}^Current strategic thinking: {s14}^Marshall: {s12}^Since the last offensive ended: {reg4} hours^Since the decisive event: {reg10} hours^Since the last 18+ hour rest: {reg9} hours^Since the last feast ended: {reg5} hours^Percent disgruntled lords: {reg7}%^Percent restless lords: {reg8}%^^"),
  ("_right_to_rule_reg12", "^Right to rule: {reg12}."),
  ("political_arguments_made_legality_reg3_rights_of_lords_reg4_unificationpeace_reg5_rights_of_commons_reg6_fief_pledges_reg7", "Political arguments made:^Legality: {reg3}^Rights of lords: {reg4}^Unification/peace: {reg5}^Rights of commons: {reg6}^Fief pledges: {reg7}"),
  ("renown_reg2_honour_rating_reg3s12_friends_s8_enemies_s6_s9", "Renown: {reg2}.^Honour rating: {reg3}.{s12}^Friends: {s8}.^Enemies: {s6}.^{s9}"),
  #SB : gender string, correct "your"
  ("you_lie_stunned_for_several_minutes_then_stagger_to_your_feet_to_find_your_s10_standing_over_you_you_have_lost_the_duel", "You lie stunned for several minutes, then stagger to your feet, to find {s10} standing over you. You have lost the duel."),
  ("s10_lies_in_the_arenas_dust_for_several_minutes_then_staggers_to_his_feet_you_have_won_the_duel", "{s10} lies in the arena's dust for several minutes, then staggers to {reg65?her:his} feet. You have won the duel."),
  ("debug__you_fought_with_a_center_so_no_change_in_morale", "{!}DEBUG : You fought with a center so no change in morale."),
  ("_this_castle_is_temporarily_under_royal_control", " This castle is temporarily under royal control."),
  ("_this_castle_does_not_seem_to_be_under_anyones_control", " This castle does not seem to be under anyone's control."),
  ("_this_town_is_temporarily_under_royal_control", " This town is temporarily under royal control."),
  ("_the_townspeople_seem_to_have_declared_their_independence", " The townspeople seem to have declared their independence."),
  ("to_your_husband_s11", "to your husband, {s11}."),
  ("_you_see_the_banner_of_your_wifehusband_s7_over_the_castle_gate", " You see the banner of your {wife/husband}, {s7}, over the castle gate."),
  ("_the_banner_of_your_wifehusband_s7_flies_over_the_town_gates", " The banner of your {wife/husband}, {s7}, flies over the town gates."),
  ("_the_lord_is_currently_holding_a_feast_in_his_hall", "^The lord is currently holding a feast in his hall."),
  ("_join_the_feast", " (join the feast)"),
  ("belligerent_drunk_in_s4", "Belligerent drunk in {s4}"),
  ("belligerent_drunk_not_found", "Belligerent drunk not found"),
  ("roughlooking_character_in_s4", "Rough-looking character in {s4}"),
  ("roughlooking_character_not_found", "Rough-looking character not found"),
  ("_however_you_have_sufficiently_distinguished_yourself_to_be_invited_to_attend_the_ongoing_feast_in_the_lords_castle", ". However, you have sufficiently distinguished yourself to be invited to attend the ongoing feast in the lord's castle."),
  ("s8_you_are_also_invited_to_attend_the_ongoing_feast_in_the_castle", "{s8}. You are also invited to attend the ongoing feast in the castle."),
  ("__hardship_index_reg0_avg_towns_reg1_avg_villages_reg2__", "{!}^^Hardship index: {reg0}, avg towns: {reg1}, avg villages: {reg2}^^"),
  ("__s3_price_=_reg4_calradian_average_reg6_capital_reg11_s4_base_reg1modified_by_raw_material_reg2modified_by_prosperity_reg3_calradian_average_production_base_reg5_total_reg12_consumed_reg7used_as_raw_material_reg8modified_total_reg9_calradian_consumption_base_reg10_total_reg13s1_", "{!}^^{s3}^Price = {reg4} (average {reg6})^Capital: {reg11} {s4}^Base {reg1}/modified by raw material {reg2}/modified by prosperity {reg3}^(average production, base {reg5}, total {reg12}).^Consumed {reg7}/used as raw material {reg8}/modified total {reg9}^(consumption, base: {reg10}, total: {reg13}){s1}^"),
  ("s11_unfortunately_s12_was_wounded_and_had_to_be_left_behind", "{s11} Unfortunately, {s12} was wounded and had to be left behind."),
  ("s11_also_s12_was_wounded_and_had_to_be_left_behind", "{s11} Also, {s12} was wounded and had to be left behind."),
  ("trial_influences_s17s_relation_with_s18_by_reg3", "{!}Trial influences {s17}'s relation with {s18} by {reg3}"),
  ("with_the_s10", "with the {s10}"),
  ("outside_calradia", "outside Europe."),
  ("you_have_been_indicted_for_treason_to_s7_your_properties_have_been_confiscated_and_you_would_be_well_advised_to_flee_for_your_life", "You have been indicted for treason to {s7}. Your properties have been confiscated, and you would be well advised to flee for your life."),
##diplomacy start+ replaced "He" with "{reg4?She:He}"
  ("by_order_of_s6_s4_of_the_s5_has_been_indicted_for_treason_the_lord_has_been_stripped_of_all_reg4herhis_properties_and_has_fled_for_reg4herhis_life_he_is_rumored_to_have_gone_into_exile_s11", "By order of {s6}, {s4} of the {s5} has been indicted for treason. The {reg4?lady:lord} has been stripped of all {reg4?her:his} properties, and has fled for {reg4?her:his} life. {reg4?She:He} is rumored to have gone into exile {s11}."),
##diplomacy end+
  ("local_notables_from_s1_a_village_claimed_by_the_s4_have_been_mistreated_by_their_overlords_from_the_s3_and_petition_s5_for_protection", "local notables from {s1}, a village claimed by the {s4}, have been mistreated by their overlords from the {s3} and petition {s5} for protection"),
  ("villagers_from_s1_stole_some_cattle_from_s2", "villagers from {s1} stole some cattle from {s2}"),
  ("villagers_from_s1_abducted_a_woman_from_a_prominent_family_in_s2_to_marry_one_of_their_boys", "villagers from {s1} abducted a woman from a prominent family in {s2} to marry one of their boys"),
  ("villagers_from_s1_killed_some_farmers_from_s2_in_a_fight_over_the_diversion_of_a_stream", "villagers from {s1} killed some farmers from {s2} in a fight over the diversion of a stream"),
  ("your_new_minister_", "Your new minister "),
  ("s10_is_your_new_minister_and_", "{s10} is your new minister, and "),
  ("due_to_the_fall_of_s10_your_court_has_been_relocated_to_s12", "Due to the loss of {s10}, your court has been relocated to {s11}"),
  ("after_to_the_fall_of_s10_your_faithful_vassal_s9_has_invited_your_court_to_s11_", "After to the loss of {s10}, your faithful vassal {s9} has invited your court to {s11} "),
  ("after_to_the_fall_of_s11_your_court_has_nowhere_to_go", "After the loss of {s11}, your court has nowhere to go"),
  ("s8_wishes_to_inform_you_that_the_lords_of_s9_will_be_gathering_for_a_feast_at_his_great_hall_in_s10_and_invites_you_to_be_part_of_this_august_assembly", "{s8} wishes to inform you that the lords of {s9} will be gathering for a feast at his great hall in {s10}, and invites you to be part of this exalted assembly."),
  ("consult_with_s11_at_your_court_in_s12", "Consult with {s11} at your court in {s12}"),
  ("as_brief_as_our_separation_has_been_the_longing_in_my_heart_to_see_you_has_made_it_seem_as_many_years", "As brief as our separation has been, the longing in my heart to see you has made it seem as many years."),
  ("although_it_has_only_been_a_short_time_since_your_departure_but_i_would_be_most_pleased_to_see_you_again", "Although it has only been a short time since your departure, I would be most pleased to see you again."),
  ("although_i_have_received_no_word_from_you_for_quite_some_time_i_am_sure_that_you_must_have_been_very_busy_and_that_your_failure_to_come_see_me_in_no_way_indicates_that_your_attentions_to_me_were_insincere_", "Although I have received no word from you for quite some time, I am sure that you must have been very busy, and that your failure to come see me in no way indicates that your attentions to me were insincere."),
  ##diplomacy start+
  #Correct the gender of the below
  ("i_trust_that_you_have_comported_yourself_in_a_manner_becoming_a_gentleman_during_our_long_separation_", "I trust that you have comported yourself in a manner becoming a {gentleman/lady} during our long separation."),#gentleman -> {gentleman/lady}
  ("it_has_been_many_days_since_you_came_and_i_would_very_much_like_to_see_you_again", "It has been many days since you came, and I would very much like to see you again."),
  ("_you_should_ask_my_s11_s16s_permission_but_i_have_no_reason_to_believe_that_he_will_prevent_you_from_coming_to_see_me", " You should ask my {s11} {s16}'s permission, but I have no reason to believe that he will prevent you from coming to see me."),
  ("_you_should_first_ask_her_s11_s16s_permission", ". You should first ask her {s11} {s16}'s permission"),
  ("_alas_as_we_know_my_s11_s16_will_not_permit_me_to_see_you_however_i_believe_that_i_can_arrange_away_for_you_to_enter_undetected", " Alas, as we know, my {s11} {s16} will not permit me to see you. However, I believe that I can arrange a way for you to enter undetected."),
  ("_as_my_s11_s16_has_already_granted_permission_for_you_to_see_me_i_shall_expect_your_imminent_arrival", " As my {s11} {s16} has already granted permission for you to see me, I shall expect your imminent arrival."),
  ("visit_s3_who_was_last_at_s4s18", "Visit {s3}, who was last at {s4}{s18}"),
  ("giver_troop_=_s2", "{!}Giver troop = {s2}"),
  ("the_guards_at_the_gate_have_been_ordered_to_allow_you_through_you_might_be_imagining_things_but_you_think_one_of_them_may_have_given_you_a_wink", "The guards at the gate have been ordered to allow you through. You might be imagining things, but you think one of them may have given you a wink"),
  ("the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter_however_as_you_walk_back_towards_your_lodgings_an_elderly_lady_dressed_in_black_approaches_you_i_am_s11s_nurse_she_whispers_urgently_don_this_dress_and_throw_the_hood_over_your_face_i_will_smuggle_you_inside_the_castle_to_meet_her_in_the_guise_of_a_skullery_maid__the_guards_will_not_look_too_carefully_but_i_beg_you_for_all_of_our_sakes_be_discrete", "The guards glare at you, and you know better than to ask permission to enter. However, as you walk back towards your lodgings, an elderly lady dressed in black approaches you. 'I am {s11}'s nurse,' she whispers urgently. 'Don this dress, and throw the hood over your face. I will smuggle you inside the castle to meet her in the guise of a scullery maid -- the guards will not look too carefully. But I beg you, for all of our sakes, be discreet!"),
  ("the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter_however_as_you_walk_back_towards_your_lodgings_an_elderly_lady_dressed_in_black_approaches_you_i_am_s11s_nurse_she_whispers_urgently_wait_for_a_while_by_the_spring_outside_the_walls_i_will_smuggle_her_ladyship_out_to_meet_you_dressed_in_the_guise_of_a_shepherdess_but_i_beg_you_for_all_of_our_sakes_be_discrete", "The guards glare at you, and you know better than to ask permission to enter. However, as you walk back towards your lodgings, an elderly lady dressed in black approaches you. 'I am {s11}'s nurse,' she whispers urgently. 'Wait for a while by the spring outside the walls. I will smuggle her ladyship out to meet you, dressed in the guise of a shepherdess. But I beg you, for all of our sakes, be discreet!"),
  ("the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter_however_as_you_walk_back_towards_your_lodgings_an_elderly_lady_dressed_in_black_approaches_you_i_am_s11s_nurse_she_whispers_urgently_her_ladyship_asks_me_to_say_that_yearns_to_see_you_but_that_you_should_bide_your_time_a_bit_her_ladyship_says_that_to_arrange_a_clandestine_meeting_so_soon_after_your_last_encounter_would_be_too_dangerous", "The guards glare at you, and you know better than to ask permission to enter. However, as you walk back towards your lodgings, an elderly lady dressed in black approaches you.^'I am {s11}'s nurse,' she whispers urgently. 'Her ladyship asks me to say that she yearns to see you, but that you should bide your time a bit. Her ladyship says that to arrange a clandestine meeting so soon after your last encounter would be too dangerous.'"),
  ##diplomacy end+
  ("the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter", "The guards glare at you, and you know better than to ask permission to enter."),
  ("s3_commander_of_party_reg4_which_is_not_his_troop_leaded_party_reg5", "{!}{s3} commander of party #{reg4} which is not his troop leaded party {reg5}"),
  ("party_with_commander_mismatch__check_log_for_details_", "Party with commander mismatch - check log for details "),
  ("s4_adds_wealth_has_reg4_wealth_accumulated", "{!}{s4} adds wealth, has {reg4} wealth accumulated"),
  ("doing_political_calculations_for_s9", "Doing political calculations for {s9}"),
  ("s9_does_not_have_a_fief", "{!}{s9} does not have a fief"),
  ("current_wealth_reg1", "Current wealth: {reg1}"),
  ("debug__attempting_to_spawn_s4", "{!}DEBUG : Attempting to spawn {s4}"),
  ("debug__s0_is_spawning_around_party__s7", "{!}DEBUG : {s0} is spawning around party : {s7}"),
  ("no_trigger_noted", "{!}(No trigger noted"),
  ("triggered_by_npc_is_quitting", "{!}(Triggered by NPC is quitting"),
  ("triggered_by_npc_has_grievance", "{!}(Triggered by NPC has grievance"),
  ("triggered_by_npc_has_personality_clash", "{!}(Triggered by NPC has personality clash"),
  ("triggered_by_npc_has_political_grievance", "{!}(Triggered by NPC has political grievance"),
  ("triggered_by_npc_to_rejoin_party", "{!}(Triggered by NPC to rejoin party"),
  ("triggered_by_npc_has_sisterly_advice", "{!}(Triggered by NPC has sisterly advice)"),
  ("triggered_by_local_histories", "{!}(Triggered by local histories)"),
  ("s1_reg0_s2", "{!}{s1}, {reg0} {s2}"),
  ("s3_reg0_s2", "{!}{s3} {reg0} {s2}"),
  ("s1_s2", "{!}{s1} {s2}"),
  ("wanted_bandits_spotted_by_s4", "Wanted bandits spotted by {s4}"),
  ("s4_ready_to_voice_objection_to_s3s_mission_if_in_party", "{s4} ready to voice objection to {s3}'s mission, if in party"),
  ("test_effective_relation_=_reg3", "{!}DEBUG : Effective relation = {reg3}"),
  ("g_talk_troop_=_reg0__g_encountered_party_=_reg1__slot_value_=_reg2", "{!}g talk troop = {reg0} , g encountered party = {reg1} , slot value = {reg2}"),
  ("strange_that_one_didnt_seem_like_your_ordenary_troublemaker_he_didnt_drink_all_that_much__he_just_stood_there_quietly_and_watched_the_door_you_may_wish_to_consider_whether_you_have_any_enemies_who_know_you_are_in_town_a_pity_that_blood_had_to_be_spilled_in_my_establishment", "Strange. That one didn't seem like your ordinary troublemaker. He didn't drink all that much -- he just stood there, quietly, and watched the door. You may wish to consider whether you have any enemies who know you are in town... A pity that blood had to be spilled in my establishment..."),
  ("wielded_item_reg3", "{!}Wielded item: {reg3}"),
  ("you_never_let_him_draw_his_weapon_still_it_looked_like_he_was_going_to_kill_you_take_his_sword_and_purse_i_suppose_he_was_trouble_but_its_not_good_for_an_establishment_to_get_a_name_as_a_place_where_men_are_killed", "You never let him draw his weapon.... Still, it looked like he was going to kill you. Take his sword and purse, I suppose. He was trouble, but it's not good for an establishment to get a name as a place where men are killed."),
  ("well_id_say_that_he_started_it_that_entitles_you_to_his_sword_and_purse_i_suppose_have_a_drink_on_the_house_as_i_daresay_youve_saved_a_patron_or_two_a_broken_skull_still_i_hope_he_still_has_a_pulse_its_not_good_for_an_establishment_to_get_a_name_as_a_place_where_men_are_killed", "Well... I'd say that he started it. That entitles you to his sword and purse, I suppose. Have a drink on the house, as I daresay you've saved a patron or two a broken skull. Still, I hope he still has a pulse. It's not good for an establishment to get a name as a place where men are killed."),
  ("stop_no_shooting_no_shooting", "Stop! No shooting! No shooting!"),
  ("em_ill_stay_out_of_this", "Em... I'll stay out of this."),
  ("the_s12_is_a_labyrinth_of_rivalries_and_grudges_lords_ignore_their_lieges_summons_and_many_are_ripe_to_defect", "The {s12} is a labyrinth of rivalries and grudges. Lords ignore their liege's summons, and many are ripe to defect."),
  ("the_s12_is_shaky_many_lords_do_not_cooperate_with_each_other_and_some_might_be_tempted_to_defect_to_a_liege_that_they_consider_more_worthy", "The {s12} is shaky. Many lords do not cooperate with each other, and some might be tempted to defect to a liege that they consider more worthy."),
  ("the_s12_is_fairly_solid_some_lords_bear_enmities_for_each_other_but_they_tend_to_stand_together_against_outside_enemies", "The {s12} is fairly solid. Some lords bear enmities for each other, but they tend to stand together against outside enemies."),
  ("the_s12_is_a_rock_of_stability_politically_speaking_whatever_the_lords_may_think_of_each_other_they_fight_as_one_against_the_common_foe", "The {s12} is a rock of stability, politically speaking. Whatever the lords may think of each other, they fight as one against the common foe."),
  ("tribune_s12", "Tribune {s12}"),
  ("lady_s12", "Lady {s12}"),
  ("lord_s12", "Lord {s12}"),
  ("resolve_the_dispute_between_s11_and_s12", "Resolve the dispute between {s11} and {s12}"),
  ("in_doing_so_you_will_be_in_violation_of_your_truce_is_that_what_you_want", "In doing so, you will be in violation of your truce. Is that what you want?"),
  ("if_you_attack_without_provocation_some_of_your_vassals_may_consider_you_to_be_too_warlike_is_that_what_you_want", "If you attack without provocation, some of your vassals may consider you to be too warlike. Is that what you want?"),
  ("our_men_are_ready_to_ride_forth_at_your_bidding_are_you_sure_this_is_what_you_want", "Our men are ready to ride forth at your bidding... Are you sure this is what you want?"),
  ("seek_recognition", "seek recognition"),
  ("seek_vassalhood", "seek vassalhood"),
  ("seek_a_truce", "seek a truce"),
  ("_promised_fief", " (promised fief)"),
  ("no_fiefss12", "(no fiefs){s12}"),
  ("fiefs_s0s12", "(fiefs: {s0}{s12})"),
  ("please_s65_", "Please {s65}, "),
  ("_s15_is_also_being_held_here_and_you_may_wish_to_see_if_reg4shehe_will_join_us", " {s15} is also being held here, and you may wish to see if {reg4?she:he} will join us."),
  ("one_thing_in_our_favor_is_that_s12s_grip_is_very_shaky_he_rules_over_a_labyrinth_of_rivalries_and_grudges_lords_often_fail_to_cooperate_and_many_would_happily_seek_a_better_liege", "One thing in our favor is that {s12}'s grip is very shaky. He rules over a labyrinth of rivalries and grudges. Lords often fail to cooperate, and many would happily seek a better liege."),
  ("thankfully_s12s_grip_is_fairly_shaky_many_lords_do_not_cooperate_with_each_other_and_some_might_be_tempted_to_seek_a_better_liege", "Thankfully, {s12}'s grip is fairly shaky. Many lords do not cooperate with each other, and some might be tempted to seek a better liege."),
  ("unfortunately_s12s_grip_is_fairly_strong_until_we_can_shake_it_we_may_have_to_look_long_and_hard_for_allies", "Unfortunately, {s12}'s grip is fairly strong. Until we can shake it, we may have to look long and hard for allies."),
  ("unfortunately_s12s_grip_is_very_strong_unless_we_can_loosen_it_it_may_be_difficult_to_find_allies", "Unfortunately, {s12}'s grip is very strong. Unless we can loosen it, it may be difficult to find allies."),
  ("playername_come_to_plague_me_some_more_have_you", "{playername}... Come to plague me some more, have you?"),
  ("ah_it_is_you_again", "Ah. It is you again..."),
  ("well_playername", "Well, {playername}"),
  ("comment_found_s1", "{!}Comment found: {s1}"),
  ("rejoinder_noted", "{!}Rejoinder noted"),
  ("s11", "{!}{s11}"),
  ("flagon_of_mead", "flagon of mead"),
  ("skin_of_kumis", "skin of kumis"),
  ("mug_of_kvass", "mug of kvass"),
  ("cup_of_wine", "cup of wine"),
##diplomacy start+ Make gender-correct using reg4
  ("you_intend_to_challenge_s13_to_force_him_to_retract_an_insult", "You intend to challenge {s13} to force {reg4?her:him} to retract an insult."),
##diplomacy end+
  ("intrigue_impatience=_reg3_must_be_less_than_100", "{!}Intrigue impatience= {reg3}, must be less than 100"),
  ("youll_have_to_speak_to_me_at_some_other_time_then", "You'll have to speak to me at some other time, then."),
  ("this_is_no_time_for_words", "This is no time for words!"),
  ("lord_not_alone", "{!}Lord not alone"),
##diplomacy start+ (players of either gender may marry opposite-gender lords)
  ("of_course_my_wife", "Of course, my {husband/wife}."),
  ("perhaps_not_our_marriage_has_become_a_bit_strained_dont_you_think", "Perhaps not. Our marriage has become a bit strained, don't you think?"),
  ("why_is_that_my_wife_actually_our_marriage_has_become_such_that_i_prefer_to_have_a_witness_for_all_of_our_converations", "Why is that, my {husband/wife}? Actually, our marriage has become such that I prefer to have a witness for all of our converations."),
##diplomacy end+
  ("all_right_then_what_do_you_have_to_say_out_with_it", "All right then. What do you have to say? Out with it."),
  ("bah__im_in_no_mood_for_whispering_in_the_corner", "Bah -- I'm in no mood for whispering in the corner."),
  ("bah_i_dont_like_you_that_much_im_not_going_to_go_plot_with_you_in_some_corner", "Bah. I don't like you that much. I'm not going to go plot with you in some corner."),
  ("well__now_what_do_you_have_to_propose", "Well -- now what do you have to propose?"),
  ("trying_our_hand_at_intrigue_are_we_i_think_not", "Trying our hand at intrigue, are we? I think not"),
  ("hah_i_trust_you_as_a_i_would_a_serpent_i_think_not", "Hah! I trust you as a I would a serpent. I think not."),
  ("i_do_not_like_to_conduct_my_business_in_the_shadows_but_sometimes_it_must_be_done_what_do_you_have_to_say", "I do not like to conduct my business in the shadows, but sometimes it must be done. What do you have to say?"),
  ("i_would_prefer_to_conduct_our_affairs_out_in_the_open", "I would prefer to conduct our affairs out in the open."),
  ("do_not_take_this_amiss_but_with_you_i_would_prefer_to_conduct_our_affairs_out_in_the_open", "Do not take this amiss, but with you, I would prefer to conduct our affairs out in the open."),
  ("hmm_you_have_piqued_my_interest_what_do_you_have_to_say", "Hmm. You have piqued my interest. What do you have to say?"),
  ("em_lets_keep_our_affairs_out_in_the_open_for_the_time_being", "Em... Let's keep our affairs out in the open, for the time being."),
  ("thats_sensible__the_world_is_full_of_churls_who_poke_their_noses_into_their_betters_business_now_tell_me_what_it_is_that_you_have_to_say", "That's sensible -- the world is full of churls who poke their noses into their betters' business. Now tell me what it is that you have to say."),
  ("what_do_you_take_me_for_a_plotter", "What do you take me for? A plotter?"),
  ("well_i_normally_like_to_keep_things_out_in_the_open_but_im_sure_someone_like_you_would_not_want_to_talk_in_private_unless_heshe_had_a_good_reason_what_is_it", "Well, I normally like to keep things out in the open, but I'm sure someone like you would not want to talk in private unless {he/she} had a good reason. What is it?"),
  ("surely_we_can_discuss_whatever_you_want_to_discuss_out_here_in_the_open_cant_we", "Surely we can discuss whatever you want to discuss out here in the open, can't we?"),
  ##diplomacy start+ make gender-correct using reg65
  ("im_a_simple__man_not_one_for_intrigue_but_id_guess_that_you_have_something_worthwhile_to_say_what_is_it", "I'm a simple {reg65?woman:man}, not one for intrigue, but I'd guess that you have something worthwhile to say. What is it?"),
  ##diplomacy end+
  ("forgive_me_but_im_not_one_for_going_off_in_corners_to_plot", "Forgive me, but I'm not one for going off in corners to plot."),
  ("please_do_not_take_this_amiss_but_i_do_not_trust_you", "Please do not take this amiss, but I do not trust you."),
  ("certainly_playername_what_is_it", "Certainly, {playername}. What is it?"),
  ("forgive_me_but_id_prefer_to_keep_our_conversations_in_the_open", "Forgive me, but I'd prefer to keep our conversations in the open."),
  ("please_do_not_take_this_amiss_but_im_not_sure_you_and_i_are_still_on_those_terms", "Please do not take this amiss, but I'm not sure you and I are still on those terms."),
  ("persuasion__relation_less_than_5", "{!}Persuasion + relation less than -5)"),
  ("s15_dupe", "{!}{s15}"), #SB : duplicate
  ("persuasion__2__lord_reputation_modifier__relation_less_than_10", "{!}Persuasion * 2 + lord reputation modifier + relation less than 10)"),
  ("s13", "{!}{s13}"),
  ("placeholder", "{!}[placeholder]..."),
  ##diplomacy start+ Replace "queen" with "{s0}"
  ("really_well_this_is_the_first_i_have_heard_of_it_unless_you_build_up_support_for_that_claim_you_may_find_it_difficult_to_find_allies_however_whenever_you_see_fit_to_declare_yourself_publically_as_queen_i_should_be_honored_to_be_your_consort", "Really? Well, this is the first I have heard of it. Unless you build up support for that claim, you may find it difficult to find allies. However, whenever you see fit to declare yourself publically as {s0}, I should be honored to be your consort."),
  ##diplomacy end+
  ("yes_i_have_heard_such_talk_while_it_is_good_that_you_are_building_up_your_support_i_do_not_think_that_you_are_quite_ready_to_proclaim_yourself_yet_however_i_will_let_you_be_the_judge_of_that_and_when_you_decide_i_should_be_honored_to_be_your_consort", "Yes... I have heard such talk. While it is good that you are building up your support, I do not think that you are quite ready to proclaim yourself yet. However, I will let you be the judge of that, and when you decide, I should be honored to be your consort."),
  ("yes_and_many_others_in_calradia_think_so_as_well_perhaps_it_is_time_that_you_declared_yourself_and_we_shall_ride_forth_together_to_claim_your_throne_i_should_be_honored_to_be_your_consort", "Yes... and many others think so as well. Perhaps it is time that you declared yourself, and we shall ride forth together to claim your throne. I should be honored to be your consort."),
  ("i_am_disturbed_about_my_lord_s15s_choice_of_companions", "I am disturbed about my lord {s15}'s choice of companions."),
  ("well_ill_be_honest_i_feel_that_sometimes_s15_overlooks_my_rights_and_extends_his_protection_to_the_unworthy", "Well, I'll be honest. I feel that sometimes {s15} overlooks my rights, and extends {reg15?her:his} protection to the unworthy."),
  ("heh_one_thing_that_ill_say_about_s15_is_that_he_has_a_ripe_batch_of_bastards_in_his_court", "Heh. One thing that I'll say about {s15} is that {reg15?she:he} has a ripe batch of bastards in {reg15?her:his} court."),
  ("well_sometimes_i_have_to_say_that_i_question_s15s_judgment_regarding_those_who_he_keeps_in_his_court", "Well, sometimes I have to say that I question {s15}'s judgment regarding those whom {reg15?she:he} keeps in his court."),
  ("s15_is_a_weak_man_who_too_easily_lends_his_ear_to_evil_council_and_gives_his_protection_to_some_who_have_done_me_wrong", "{s15} is a weak ruler, who too easily lends an ear to evil council, and gives protection to some who have done me wrong."),
  ("i_will_confess_that_sometimes_i_worry_about_s15s_judgment_particularly_in_the_matter_of_the_counsel_that_he_keeps", "I will confess that sometimes I worry about {s15}'s judgment, particularly in the matter of the counsel that {reg15?she:he} keeps.."),
  ("what_do_i_think_i_think_that_s15_is_a_vile_pretender_a_friend_to_the_flatterer_and_the_hypocrite", "What do I think? I think that {s15} is a vile pretender, a friend to the flatterer and the hypocrite."),
  ("well_s15_is_not_like_you_ill_say_that_much", "Well, {s15} is not like you. I'll say that much."),
  ("s15_long_may_he_live", "{s15}? Long may {reg15?she:he} live!"),
  ("he_is_my_liege_that_is_all_that_i_will_say_on_this_matter", "{s15} is my liege. That is all that I will say on this matter."),
  ("that_you_are_the_rightful_heir_to_the_throne_of_calradia", "That you are the rightful heir to the throne of Europe?"),
  ("that_s14_is_the_rightful_ruler_of_calradia", "That {s14} is the rightful ruler of Europe?"),
  ("that_s14_will_rule_this_land_justly", "That {s14} will rule this land justly?"),
  ("that_s14_will_protect_our_rights_as_nobles", "That {s14} will protect our rights as nobles?"),
  ("that_s14_will_unify_this_land_and_end_this_war", "That {s14} will unify this land and end this war?"),
  ("that_s14_will_reward_me_with_a_fief", "That {s14} will reward me with a fief?"),
  #("prior_arguments", "Prior arguments:"),
  #("legal_reg3", "Legal: {reg3}"),
  #("just_king_reg3", "Just king: {reg3}"),
  #("bring_peace_reg3", "Bring peace: {reg3}"),
  #("only_best_counsel_reg3", "Only best counsel: {reg3}"),
  #("reward_lords_reg3", "Reward lords: {reg3}"),
  ("he", "he"),
  ("king", "king"),
  ("she", "she"),
  ("queen", "queen"),
  ("khan", "khan"),
  ("i", "I"),
  ("according_to_the_ancient_law_and_custom_of_the_calradians_s45_should_be_s47", "According to the ancient law and customs, {s45} should be {s47}"),
  ("because_s44_is_the_rightful_s47_of_the_s46", "Because {s44} is the rightful {s47} of the {s46}"),
  ("you_speak_of_claims_and_legalities_yet_to_others_you_talk_of_bringing_peace_by_force", "You speak of claims and legalities, yet to others you talk of bringing peace by force"),
  ("you_speak_of_bringing_peace_by_force_yet_to_others_you_make_legal_claims", "You speak of bringing peace by force, yet to others you make legal claims."),
  ("you_speak_to_some_of_upholding_the_rights_of_the_commons_yet_you_speak_to_others_of_uphold_the_rights_of_nobles_what_if_those_rights_are_in_conflict", "You speak to some of upholding the rights of the commons, yet you speak to others of uphold the rights of nobles. What if those rights are in conflict?"),
##diplomacy start+
#Replace "lord" with {s12}
#  ("you_speak_to_me_of_upholding_my_rights_as_a_lord_but_to_others_you_talk_of_upholding_the_rights_of_all_commons_what_if_those_rights_come_into_conflict", "You speak to me of upholding my rights as a lord, but to others you talk of upholding the rights of all commons. What if those rights come into conflict?"),
  ("you_speak_to_me_of_upholding_my_rights_as_a_lord_but_to_others_you_talk_of_upholding_the_rights_of_all_commons_what_if_those_rights_come_into_conflict", "You speak to me of upholding my rights as a {s12}, but to others you talk of upholding the rights of all commons. What if those rights come into conflict?"),
##diplomacy end+
  ("a_claim_should_be_strong_indeed_before_one_starts_talking_about_it", "A claim should be strong indeed before one starts talking about it."),
##diplomacy start+: Replace "king" with {s12}, and "pigherd" with {s14}
##OLD:
#  ("a_king_should_prove_his_valor_beyond_any_doubt_before_he_starts_talking_about_a_claim_to_the_throne", "A king should prove his valor beyond any doubt before he starts talking about a claim to the throne."),
#  ("you_must_prove_yourself_a_great_warrior_before_men_will_follow_you_as_king", "You must prove yourself a great warrior before men will follow you as king."),
#  ("a_claim_to_the_throne_should_be_strong_indeed_before_one_presses_it", "A claim to the throne should be strong indeed before one presses it."),
#  ("indeed_but_a_man_must_also_prove_himself_a_great_warrior_before_men_will_follow_you_as_king", "Indeed. But a man must also prove himself a great warrior before men will follow you as king."),
#  ("my_pigherd_can_declare_himself_king_if_he_takes_he_fancy_i_think_you_need_to_break_a_few_more_heads_on_tbe_battlefield_before_men_will_follow_you", "My pigherd can declare himself king, if he takes he fancy. I think you need to break a few more heads on tbe battlefield before men will follow you."),
##NEW: Replace "king" with {s12}, and "pigherd" with {s14}
  ("a_king_should_prove_his_valor_beyond_any_doubt_before_he_starts_talking_about_a_claim_to_the_throne", "A {s12} should prove his valor beyond any doubt before he starts talking about a claim to the throne."),
  ("you_must_prove_yourself_a_great_warrior_before_men_will_follow_you_as_king", "You must prove yourself a great warrior before men will follow you as {s12}."),
  ("a_claim_to_the_throne_should_be_strong_indeed_before_one_presses_it", "A claim to the throne should be strong indeed before one presses it."),
  ("indeed_but_a_man_must_also_prove_himself_a_great_warrior_before_men_will_follow_you_as_king", "Indeed. But a man must also prove himself a great warrior before men will follow you as {s12}."),
  ("my_pigherd_can_declare_himself_king_if_he_takes_he_fancy_i_think_you_need_to_break_a_few_more_heads_on_tbe_battlefield_before_men_will_follow_you", "My {s14} can declare himself {s12}, if he takes he fancy. I think you need to break a few more heads on tbe battlefield before men will follow you."),
##diplomacy end+
  ("if_you_do_not_wish_to_die_on_a_scaffold_like_so_many_failed_pretenders_before_you_i_would_suggest_that_you_to_build_your_claim_on_stronger_foundations_so_that_men_will_follow_you", "If you do not wish to die on a scaffold, like so many failed pretenders before you, I would suggest that you to build your claim on stronger foundations, so that men will follow you."),
  ("if_you_do_not_wish_to_die_on_a_scaffold_like_so_many_failed_pretenders_before_you_i_would_advise_you_prove_yourself_on_the_field_of_battle_so_that_men_will_follow_you", "If you do not wish to die on a scaffold, like so many failed pretenders before you, I would advise you prove yourself on the field of battle, so that men will follow you."),
  ##diplomacy start+ replace "with their swords" with "with their {s12}", and "Real kings" with "Real {s14}"
#  ("talk_is_for_heralds_and_lawyers_real_kings_prove_themselves_with_their_swords", "Talk is for heralds and lawyers. Real kings prove themselves with their swords."),
  ("talk_is_for_heralds_and_lawyers_real_kings_prove_themselves_with_their_swords", "Talk is for heralds and lawyers. Real {s14} prove themselves with their {s12}."),
  ##diplomacy end+
  ("i_were_you_i_would_try_to_prove_myself_a_bit_more_before_i_went_about_pressing_my_claim", "If I were you, I would try to prove myself a bit more before I went about pressing my claim."),
  ("trump_check_random_reg4_skill_reg3", "{!}DEBUG : Trump check: random {reg4}, skill {reg3}"),
  ("s12_s43", "{!}{s12} {s43}"),
  ("indeed_please_continue", "Indeed. Please continue."),
  ("me", "me"),
  ("preliminary_result_for_political_=_reg4", "{!}DEBUG : Preliminary result for political = {reg4}"),
  ("i_worry_about_those_with_whom_you_have_chosen_to_surround_yourself", "I worry about those with whom you have chosen to surround yourself."),
  ("there_are_some_outstanding_matters_between_me_and_some_of_your_vassals_", "There are some outstanding matters between me and some of your vassals. "),
  ("result_for_political_=_reg41", "{!}DEBUG : Result for political = {reg41}"),
  ("my_liege_has_his_faults_but_i_dont_care_for_your_toadies", "My liege has his faults but I don't care for your toadies."),
  ("i_think_youre_a_good_man_but_im_worried_that_you_might_be_pushed_in_the_wrong_direction_by_some_of_those_around_you", "I think you're a good man, but I'm worried that you might be pushed in the wrong direction by some of those around you."),
  ("i_am_loathe_to_fight_alongside_you_so_long_as_you_take_under_your_wing_varlots_and_base_men", "I am loathe to fight alongside you, so long as you take under your wing varlots and base men."),
  ("ill_be_honest__with_some_of_those_who_follow_you_i_think_id_be_more_comfortable_fighting_against_you_than_with_you", "I'll be honest -- with some of those who follow you, I think I'd be more comfortable fighting against you than with you."),
  ("i_say_that_you_can_judge_a_man_by_the_company_he_keeps_and_you_have_surrounded_yourself_with_vipers_and_vultures", "I say that you can judge a man by the company he keeps, and you have surrounded yourself with vipers and vultures."),
  ("you_know_that_i_have_always_had_a_problem_with_some_of_our_companions", "You know that I have always had a problem with some of our companions."),
  ("politically_i_would_be_a_better_position_in_the_court_of_my_current_liege_than_in_yours", "Politically, I would be a better position in the court of my current liege, than in yours."),
  ("i_am_more_comfortable_with_you_and_your_companions_than_with_my_current_liege", "I am more comfortable with you and your companions than with my current liege"),
  ("militarily_youre_in_no_position_to_protect_me_should_i_be_attacked_id_be_reluctant_to_join_you_until_you_could", "Militarily, you're in no position to protect me, should I be attacked. I'd be reluctant to join you until you could."),
  ("militarily_when_i_consider_the_lay_of_the_land_i_realize_that_to_pledge_myself_to_you_now_would_endanger_my_faithful_retainers_and_my_family", "Militarily, when I consider the lay of the land, I realize that to pledge myself to you now would endanger my faithful retainers and my family."),
  ("militarily_youre_in_no_position_to_come_to_my_help_if_someone_attacked_me_i_dont_mind_a_good_fight_but_i_like_to_have_a_chance_of_winning", "Militarily, you're in no position to come to my help, if someone attacked me. I don't mind a good fight, but I like to have a chance of winning."),
  ("militarily_you_would_have_me_join_you_only_to_find_myself_isolated_amid_a_sea_of_enemies", "Militarily, you would have me join you, only to find myself isolated amid a sea of enemies."),
  ("militarily_youre_in_no_position_to_come_to_my_help_if_someone_attacked_me_youd_let_me_be_cut_down_like_a_dog_id_bet", "Militarily, you're in no position to come to my help, if someone attacked me. You'd let me be cut down like a dog, I'd bet."),
  ("militarily_i_wouldnt_be_any_safer_if_i_joined_you", "Militarily, I wouldn't be any safer if I joined you."),
  ("militarily_i_might_be_safer_if_i_joined_you", "Militarily, I might be safer if I joined you."),
  ("finally_there_is_a_cost_to_ones_reputation_to_change_sides_in_this_case_the_cost_would_be_very_high", "Finally, one should always think carefully about retracting one's allegiance, even if there is good reason, as it is not good to get a name as one who changes lieges easily. In this case, the cost to my reputation would be very high."),
  ("finally_there_is_a_cost_to_ones_reputation_to_change_sides_in_this_case_the_cost_would_be_significant", "Finally, one should always think carefully about retracting one's allegiance, even if there is good reason, as it is not good to get a name as one who changes lieges easily. In this case, the cost to my reputation would be significant."),
  ("finally_there_is_a_cost_to_ones_reputation_to_change_sides_in_this_case_however_many_men_would_understand", "Finally, one should always think carefully about retracting one's allegiance, even if there is good reason, as it is not good to get a name as one who changes lieges easily. In this case, however, many men would understand."),
  ("chance_of_success_=_reg1", "{!}DEBUG : Chance of success = {reg1}%"),
  ("random_=_reg3", "{!}DEBUG : Random = {reg3}"),
  ("i_will_not_have_it_be_said_about_me_that_i_am_a_traitor_that_is_my_final_decision_i_have_nothing_more_to_say_on_this_matter", "I will not have it be said about me that I am a traitor. That is my final decision. I have nothing more to say on this matter."),
  ("i_am_pledged_to_defend_s14_i_am_sorry_though_we_may_meet_on_the_battlefield_i_hope_that_we_will_still_be_friends", "I am pledged to defend {s14}. I am sorry. Though we may meet on the battlefield, I hope that we will still be friends."),
  ("i_really_cannot_bring_myself_to_renounce_s14_i_am_sorry_please_lets_not_talk_about_this_any_more", "I really cannot bring myself to renounce {s14}. I am sorry. Please, let's not talk about this any more."),
  ("however_i_have_decided_that_i_must_remain_loyal_to_s14_i_am_sorry", "However, I have decided that I must remain loyal to {s14}. I am sorry."),
  ("however_i_will_not_let_you_lead_me_into_treason_do_not_talk_to_me_of_this_again", "However, I will not let you lead me into treason. Do not talk to me of this again."),
  ("its_not_good_to_get_a_reputation_as_one_who_abandons_his_liege_that_is_my_decision_let_us_speak_no_more_of_this_matter", "It's not good to get a reputation as one who abandons his liege. That is my decision. Let us speak no more of this matter."),
  ("ive_decided_to_stick_with_s14_i_dont_want_to_talk_about_this_matter_any_more", "I've decided to stick with {s14}. I don't want to talk about this matter any more."),
  ("lord_pledges_to_s4", "{!}DEBUG : Lord pledges to {s4}"),
  ("lord_recruitment_provokes_home_faction", "{!}DEBUG : Lord recruitment provokes home faction"),
  ("ERROR__wrong_quest_type", "{!}ERROR - Wrong quest type"),
  ("you_are_challenging_me_to_a_duel_how_droll_as_you_wish_playername_it_will_be_good_sport_to_bash_your_head_in", "You are challenging me to a duel? How droll! As you wish, {playername}, it will be good sport to bash your head in."),
  ("call_me_coward_very_well_you_leave_me_no_choice", "Call me coward? Very well, you leave me no choice."),
  ("reg3_hours", "{reg3} hours."),
  ("hour", "hour."),
  ("however_circumstances_have_changed_since_we_made_that_decision_and_i_may_reconsider_shortly_s16", "However, circumstances have changed since we made that decision, and I may reconsider shortly. {s16}"),
  ("i_wish_to_marry_your_s11_s10_i_ask_for_your_blessing", "I wish to marry your {s11}, {s10}. I ask for your blessing."),
  ("i_wish_to_marry_your_s11_s10_i_ask_for_your_help", "I wish to marry your {s11}, {s10}. I ask for your help."),
  ("you_plan_to_marry_s3_at_a_feast_hosted_by_s4_in_s5_you_should_be_notifed_of_the_feast_as_soon_as_it_is_held", "You plan to marry {s3} at a feast hosted by {s4} in {s5}. You should be notifed of the feast as soon as it is held."),
  ("your_s11_", "your {s11}, "),
  ("i_ask_again_may", "I ask again: may"),
  ("may", "May"),
  ("very_well_as_far_as_im_concerned_i_suppose_she_can_see_most_anyone_she_likes__within_reason_of_course", "Very well. As far as I'm concerned, I suppose she can see most anyone she likes - within reason, of course."),
  ("very_well_an_alliance_with_you_could_be_valuable_go_chat_with_her_and_see_if_you_can_get_her_to_take_a_fancy_to_you_if_she_doesnt_and_if_we_still_want_to_conclude_this_business_then_i_can_make_her_see_reason", "Very well. An alliance with you could be valuable. Go chat with her, and see if you can get her to take a fancy to you. If she doesn't, and if we still want to conclude this business, then I can make her see reason."),
  ("you_have_my_blessing_to_pay_suit_to_her__so_long_as_your_intentions_are_honorable_of_course_depending_on_how_things_proceed_between_you_two_we_may_have_more_to_discuss_at_a_later_date", "You have my blessing to pay suit to her -- so long as your intentions are honorable, of course. Depending on how things proceed between you two, we may have more to discuss at a later date."),
  ("war_damage_inflicted_reg3_suffered_reg4_ratio_reg5", "{!}DEBUG : War damage inflicted: {reg3}, suffered: {reg4}, ratio: {reg5}"),
  ("ERROR__did_not_calculate_war_progress_string_properly", "{!}ERROR - did not calculate war progress string properly"),
  ("the_war_has_barely_begun_so_and_it_is_too_early_to_say_who_is_winning_and_who_is_losing", "The war has barely begun, so and it is too early to say who is winning and who is losing."),
  ("we_have_been_hitting_them_very_hard_and_giving_them_little_chance_to_recover", "We have been hitting them very hard, and giving them little chance to recover."),
  ("the_fighting_has_been_hard_but_we_have_definitely_been_getting_the_better_of_them", "The fighting has been hard, but we have definitely been getting the better of them."),
  ("they_have_been_hitting_us_very_hard_and_causing_great_suffering", "They have been hitting us very hard, and causing great suffering."),
  ("the_fighting_has_been_hard_and_i_am_afraid_that_we_have_been_having_the_worst_of_it", "The fighting has been hard, and I am afraid that we have been having the worst of it."),
  ("both_sides_have_suffered_in_the_fighting", "Both sides have suffered in the fighting."),
  ("no_clear_winner_has_yet_emerged_in_the_fighting_but_i_think_we_are_getting_the_better_of_them", "No clear winner has yet emerged in the fighting, but I think we are getting the better of them."),
  ("no_clear_winner_has_yet_emerged_in_the_fighting_but_i_fear_they_may_be_getting_the_better_of_us", "No clear winner has yet emerged in the fighting, but I fear they may be getting the better of us."),
  ("no_clear_winner_has_yet_emerged_in_the_fighting", "No clear winner has yet emerged in the fighting."),
  ("s9_s14", "{!}{s9} {s14}"),
  ("there_is_no_campaign_currently_in_progress", "There is no campaign currently in progress."),
  ("we_are_assembling_the_army", "We are assembling the army."),
  ("we_aim_to_take_the_fortress_of_s8", "We aim to take the fortress of {s8}."),
  ("we_are_on_a_raid_and_are_now_targeting_s8", "We are on a raid, and are now targeting {s8}."),
  ("we_are_trying_to_seek_out_and_defeat_s8", "We are trying to seek out and defeat {s8}."),
  ("we_are_riding_to_the_defense_of_s8", "We are riding to the defense of {s8}."),
  ("we_are_gathering_for_a_feast_at_s8", "We are gathering for a feast at {s8}."),
  ("_however_that_may_change_shortly_s14", " However, that may change shortly. {s14}"),
  ("it_is_our_custom_to_seal_any_such_alliances_with_marriage_and_in_fact_we_have_been_looking_for_a_suitable_groom_for_my_s11_s14", "It is our custom to seal any such alliances with marriage, and in fact, we have been looking for a suitable {groom/bride} for my {s11}, {s14}."), #dckplmc
  ("once_again_", "once again "),
  ("cheat__marriage_proposal", "Cheat - marriage proposal"),
##diplomacy start+ gender correction
  ("you_plan_to_marry_s4_as_you_have_no_family_in_calradia_he_will_organize_the_wedding_feast", "You plan to marry {s4}. As you have no family in Europe, {she/he} will organize the wedding feast."),
##diplomacy end+
  ("s43_just_so_you_know_if_you_attack_me_you_will_be_in_violation_of_the_truce_you_signed_with_the_s34", "{s43} Just so you know, if you attack me, you will be in violation of the truce you signed with the {s34}"),
##diplomacy start+ gender correction
  ("very_well__you_are_now_my_liege_as_well_as_my_husband", "We can keep this short: you are now my liege, as well as my {wife/husband}, with all the mutual obligations which that entails."),
  ("i_thank_you_reg39my_ladylord", "I thank you, {reg39?my lady:lord}."),
  ("now_some_might_say_that_women_have_no_business_leading_mercenary_companies_but_i_suspect_that_you_would_prove_them_wrong_what_do_you_say", "Now, some might say that {males/women} have no business leading mercenary companies, but I suspect that you would prove them wrong. What do you say?"),
##diplomacy end+
  ("what_do_you_say_to_entering_the_service_of_s9_as_a_mercenary_captain_i_have_no_doubt_that_you_would_be_up_to_the_task", "What do you say to entering the service of {s9} as a mercenary captain? I have no doubt that you would be up to the task."),
  ("s9_asked_you_to_rescue_s13_who_is_prisoner_at_s24", "{s9} asked you to rescue {s13}, who is prisoner at {s24}."),
  ("s9_asked_you_to_attack_a_village_or_some_caravans_as_to_provoke_a_war_with_s13", "{s9} asked you to attack a village or some caravans as to provoke a war with {s13}."),
  ("s9_asked_you_to_catch_the_three_groups_of_runaway_serfs_and_bring_them_back_to_s4_alive_and_breathing_he_said_that_all_three_groups_are_heading_towards_s3", "{s9} asked you to catch the three groups of runaway serfs and bring them back to {s4}, alive and breathing. He said that all three groups are heading towards {s3}."),
  ("ERROR__player_not_logged_as_groom", "{!}ERROR - Player not logged as groom"),
  ("you_intend_to_bring_goods_to_s9_in_preparation_for_the_feast_which_will_be_held_as_soon_as_conditions_permit", "You intend to bring goods to {s9} in preparation for the feast, which will be held as soon as conditions permit."),
  ("hello_playername", "Hello, {playername}"),
  ("ah_my_gentle_playername_how_much_good_it_does_my_heart_to_see_you_again", " How much good it does my heart to see you again! Sometimes, I feel that there is a mystic bond between us that transcends the distance."),
  ("playername__i_am_so_glad_to_see_you_again_i_must_say_i_do_envy_your_freedom_to_ride_out_and_experience_the_world", " I must say, I do envy your freedom to ride out and experience the world."),
  ("playername__i_am_so_glad_to_see_you_i_trust_that_you_have_been_behaving_honorably_since_last_we_met", " I trust that you have been behaving honorably since last we met."),
  ("playername__i_am_so_glad_that_you_were_able_to_come", " I am so glad that you were able to come."),
##diplomacy start+ make both-gender versions (reg65 is speaker's gender)
  ("i_do_enjoy_speaking_to_you_but_i_am_sure_you_understand_that_our_people_cluck_their_tongues_at_a_woman_to_spend_too_long_conversing_with_a_man_outside_her_family__although_the_heavens_know_its_never_the_man_who_is_held_to_blame_", "I do enjoy speaking to you. But I am sure you understand that our people cluck their tongues at a {reg65?woman:boy} to spend too long conversing with a {man/woman} outside {reg65?her:his} family -- although the heavens know it's never the {man/woman} who is held to blame. "),
  ("as_much_as_i_enjoy_speaking_to_you_i_do_not_care_to_be_gossiped_about_by_others_who_might_lack_my_grace_and_beauty_", "As much as I enjoy speaking to you, I do not care to be gossiped about by others who might lack my grace and beauty. "),
  ("i_do_so_enjoy_speaking_to_you_but_as_a_daughter_of_one_of_the_great_families_of_this_land_i_must_set_an_example_of_propriety_", "I do so enjoy speaking to you. But as a {reg65?daughter:scion} of one of the great families of this land, I must set an example of propriety. "),
  ("i_do_so_enjoy_speaking_to_you_but_as_a_daughter_of_good_family_i_must_protect_my_reputation_", "I do so enjoy speaking to you. But as a {reg65?daughter:son} of good family, I must protect my reputation. "),
  ("although_it_is_kind_of_you_to_pay_me_such_attentions_i_suspect_that_you_might_find_other_ladies_who_may_be_more_inclined_to_return_your_affection", "Although it is kind of you to pay me such attentions, I suspect that you might find other {reg65?ladies:young men} who may be more inclined to return your affection."),
  ("as_flattered_as_i_am_by_your_attentions_perhaps_you_should_seek_out_another_lady_of_somewhat_shall_we_say_different_tastes", "As flattered as I am by your attentions, perhaps you should seek out another {reg65?lady:boy} of somewhat... shall we say... different tastes."),
  ("as_flattered_as_i_am_by_your_attentions_i_am_a_daughter_of_good_family_and_must_be_aware_of_my_reputation_it_is_not_seemly_that_i_converse_too_much_at_one_time_with_one_man_i_am_sure_you_understand_now_if_you_will_excuse_me", "As flattered as I am by your attentions, I am a {reg65?daughter:scion} of good family and must be aware of my reputation. It is not seemly that I converse too much at one time with one {man/woman}. I am sure you understand. Now, if you will excuse me..."),
##diplomacy end+ (making both-gender version)
  ("very_well__i_will_let_you_choose_the_time", "Very well -- I will let you choose the time."),
  ("good_i_am_glad_that_you_have_abandoned_the_notion_of_pushing_me_into_marriage_before_i_was_ready", "Good! I am glad that you have abandoned the notion of pushing me into marriage before I was ready."),
  ("rival_found_s4_reg0_relation", "{!}DEBUG : Rival found: {s4} ({reg0} relation)"),
  ("i_am", "I am"),
  ("s12_comma", "{!}{s12},"),
  ("s12_s11_to_s14", "{s12} {s11} to {s14}"),
  ("s12_period", "{!}{s12}."),
  ("s12_i_am_here_for_the_feast", "{s12}. I am here for the feast."),
  ("another_tournament_dedication_oh_i_suppose_it_is_always_flattering", "Another tournament dedication? Oh, I suppose it is always flattering..."),
  ("do_you_why_what_a_most_gallant_thing_to_say", "Do you? Why, what a most gallant thing to say."),
  ("hmm_i_cannot_say_that_i_altogether_approve_of_such_frivolity_but_i_must_confess_myself_a_bit_flattered", "Hmm.. I cannot say that I altogether approve of such frivolity, but I must confess myself a bit flattered."),
  ("why_thank_you_you_are_most_kind_to_do_so", "Why, thank you. You are most kind to do so."),
  ("you_are_most_courteous_and_courtesy_is_a_fine_virtue_", "You are most courteous, and courtesy is a fine virtue. "),
  ("hmm_youre_a_bold_one_but_i_like_that_", "Hmm. You're a bold one, but I like that. "),
  ("ah_well_they_all_say_that_but_no_matter_a_compliment_well_delivered_is_at_least_a_good_start_", "Ah, well, they all say that. But no matter. A compliment well delivered is at least a good start. "),
  ("oh_do_you_mean_that_such_a_kind_thing_to_say", "Oh! Do you mean that? Such a kind thing to say!"),
##diplomacy start+ make gender correct
  ("you_are_a_most_gallant_young_man_", "You are a most gallant young {man/woman}. "),
##diplomacy end+
  ("_do_come_and_see_me_again_soon", " Do come and see me again soon."),
  ("you_intend_to_ask_s12_for_permission_to_marry_s15", "You intend to ask {s12} for permission to marry {s15}."),
  ("you_intend_to_ask_s12_to_pressure_s10_to_marry_you", "You intend to ask {s12} to pressure {s10} to marry you."),
  ("do_be_careful_i_am_so_much_endebted_to_you_for_this", "Do be careful! I am so much endebted to you for this..."),
  ("go_then__we_shall_see_which_of_you_triumphs", "Go, then -- we shall see which of you triumphs..."),
##diplomacy start+ make gender correct
  ("sigh_i_will_never_truly_understand_men_and_their_rash_actions", "Sigh... I will never truly understand {men/women}, and their rash actions..."),
  ("you_intend_to_challenge_s13_to_force_him_to_relinquish_his_suit_of_s11", "You intend to challenge {s13} to force {reg4?her:him} to relinquish his suit of {s11}."),
##diplomacy end+
  ("farewell", "Farewell."),
  ("farewell_playername", "Farewell, {playername}."),
  ("__we_believe_that_there_is_money_to_be_made_selling_", "  We believe that there is money to be made selling "),
  ("s14s15_", "{!}{s14}{s15}, "),
  ("_we_carry_a_selection_of_goods_although_the_difference_in_prices_for_each_is_not_so_great_we_hope_to_make_a_profit_off_of_the_whole", " We carry a selection of goods. Although the difference in prices for each is not so great, we hope to make a profit off of the whole."),
  ("s14and_other_goods", "{s14}and other goods."),
  ("_have_you_not_signed_a_truce_with_our_lord", " Have you not signed a truce with our lord?"),
  ("parole", "parole"),
  ("normal", "normal"),
  ("s51", "{!}{s51}"),
  ("_meanwhile_s51_reg2areis_being_held_in_the_castle_but_reg2havehas_made_pledges_not_to_escape_and_reg2areis_being_held_in_more_comfortable_quarters", " Meanwhile, {s51} {reg2?are:is} being held in the castle, but {reg2?have:has} made pledges not to escape, and {reg2?are:is} being held in more comfortable quarters."),
  ("you_may_be_aware_my_lord_of_the_quarrel_between_s4_and_s5_which_is_damaging_the_unity_of_this_realm_and_sapping_your_authority_if_you_could_persuade_the_lords_to_reconcile_it_would_boost_your_own_standing_however_in_taking_this_on_you_run_the_risk_of_one_the_lords_deciding_that_you_have_taken_the_rivals_side", "You may be aware, {sire/my lady}, of the quarrel between {s4} and {s5} which is damaging the unity of this realm and sapping your authority. If you could persuade the lords to reconcile, it would boost your own standing. However, in taking this on, you run the risk of one the lords deciding that you have taken the rival's side."),
  ("you_may_be_aware_my_lord_of_the_quarrel_between_s4_and_s5_which_is_damaging_the_unity_of_this_realm_and_sapping_your_authority_if_you_could_persuade_the_lords_to_reconcile_i_imagine_that_s7_would_be_most_pleased_however_in_taking_this_on_you_run_the_risk_of_one_the_lords_deciding_that_you_have_taken_the_rivals_side", "You may be aware, {my lord/my lady}, of the quarrel between {s4} and {s5} which is damaging the unity of this realm. If you could persuade the lords to reconcile, I imagine that {s7} would be most pleased. However, in taking this on, you run the risk of one the lords deciding that you have taken the rival's side."),
  ("_of_course_the_land_is_currently_at_peace_so_you_may_have_better_luck_in_other_realms", " Of course, the land is currently at peace, so you may have better luck in other realms."),
  ("here", "here"),
  ("over", "over"),
  ("s8_in_s12", "{s8} in {s12}"),
  ("_has_put_together_a_bounty_on_some_bandits_who_have_been_attacking_travellers_in_the_area", " has put together a bounty on some bandits who have been attacking travellers in the area."),
  ("_is_looking_for_a_way_to_avoid_an_impending_war", " is looking for a way to avoid an impending war."),
  ("_may_need_help_rescuing_an_imprisoned_family_member", " may need help rescuing an imprisoned family member."),
##diplomacy start+ fix pronoun with reg4
  ("_has_been_asking_around_for_someone_who_might_want_work_id_watch_yourself_with_him_though", " has been asking around for someone who might want work. I'd watch yourself with {reg4?her:him}, though."),
##diplomacy end+
  ("town", "town"),
  ("castle", "castle"),
  ("_but_he_is_holding_there_as_a_prisoner_at_dungeon_of_s13", " But {reg4?she:he} is being held there as a prisoner in the {s13}'s dungeon."), #SB : the town/castle
  ("log_entry_type_reg4_for_s4_total_entries_reg5", "{!}DEBUG : Log entry type: {reg4} for {s4}, total entries: {reg5}"),
  ("ERROR__reputation_type_for_s9_not_within_range", "{!}ERROR - reputation type for {s9} not within range"),
##diplomacy start+ make gender-flipped versions, using reg4 for gender of s9
#xxx yyy zzz TODO: make sure you set reg4 before calling this!
  ("they_say_that_s9_is_a_most_conventional_maiden__devoted_to_her_family_of_a_kind_and_gentle_temperament_a_lady_in_all_her_way", "They say that {s9} is a most conventional {reg4?maiden:lad} - devoted to {reg4?her:his} family, of a kind and gentle temperament, a {reg4?lady:young gentleman} in all {reg4?her:his} way."),
  ("they_say_that_s9_is_a_bit_of_a_romantic_a_dreamer__of_a_gentle_temperament_yet_unpredictable_she_is_likely_to_be_led_by_her_passions_and_will_be_trouble_for_her_family_ill_wager", "They say that {s9} is a bit of a romantic, a dreamer -- of a gentle temperament, yet unpredictable. {reg4?She:He} is likely to be led by {reg4?her:his} passions, and will be trouble for {reg4?her:his} family, I'll wager."),
  ("they_say_that_s9_is_determined_to_marry_well_and_make_her_mark_in_the_world_she_may_be_a_tremendous_asset_for_her_husband__provided_he_can_satisfy_her_ambition", "They say that {s9} is determined to marry well and make {reg4?her:his} mark in the world. {reg4?She:He} may be a tremendous asset for {reg4?her husband:his wife} -- provided {reg4?he:she} can satisfy {reg4?her:his} ambition!"),
  ("they_say_that_s9_loves_to_hunt_and_ride_maybe_she_wishes_she_were_a_man_whoever_she_marries_will_have_a_tough_job_keeping_the_upper_hand_i_would_say", "They say that {s9} loves to hunt and ride. Maybe {reg4?she:he} wishes {reg4?she:he} were a {reg4?man:woman}! Whoever {reg4?she:he} marries will have a tough job keeping the upper hand, I would say."),
  ("they_say_that_s9_is_a_lady_of_the_highest_moral_standards_very_admirable_very_admirable__and_very_hard_to_please_ill_warrant", "They say that {s9} is a {reg4?lady:young gentleman} of the highest moral standards. Very admirable, very admirable -- and very hard to please, I'll warrant."),
  ("s9_is_now_betrothed_to_s11_soon_we_believe_there_shall_be_a_wedding", "{s9} is now betrothed to {s11}. Soon, we believe, there shall be a wedding!"),
  ("i_have_not_heard_any_news_about_her", "I have not heard any news about {reg4?her:him}."),
  ("searching_for_rumors_for_s9", "{!}DEBUG : Searching for rumors for {s9}"),
  ("they_say_that_s9_has_shown_favor_to_s11_perhaps_it_will_not_be_long_until_they_are_betrothed__if_her_family_permits", "They say that {s9} has shown favor to {s11}. Perhaps it will not be long until they are betrothed -- if {reg4?her:his} family permits."),
  ("they_say_that_s9_has_been_forced_by_her_family_into_betrothal_with_s11", "They say that {s9} has been forced by {reg4?her:his} family into betrothal with {s11}."),
  ("they_say_that_s9_has_agreed_to_s11s_suit_and_the_two_are_now_betrothed", "They say that {s9} has agreed to {s11}'s suit, and the two are now betrothed."),
  ("they_say_that_s9_under_pressure_from_her_family_has_agreed_to_betrothal_with_s11", "They say that {s9}, under pressure from {reg4?her:his} family, has agreed to betrothal with {s11}."),
  ("they_say_that_s9_has_refused_s11s_suit", "They say that {s9} has refused {s11}'s suit."),
  ("they_say_that_s11_has_tired_of_pursuing_s9", "They say that {s11} has tired of pursuing {s9}."),
  ("they_say_that_s9s_family_has_forced_her_to_renounce_s11_whom_she_much_loved", "They say that {s9}'s family has forced {reg4?her:him} to renounce {s11}, whom {reg4?she:he} much loved."),
  ("they_say_that_s9_has_run_away_with_s11_causing_her_family_much_grievance", "They say that {s9} has run away with {s11}, causing {reg4?her:his} family much grievance."),
##Finished with gender-flipped versions
##diplomacy end+
  ("they_say_that_s9_and_s11_have_wed", "They say that {s9} and {s11} have wed."),
  ("they_say_that_s9_was_recently_visited_by_s11_who_knows_where_that_might_lead", "They say that {s9} was recently visited by {s11}. Who knows where that might lead!"),
  ("there_is_not_much_to_tell_but_it_is_still_early_in_the_season", "There is not much to tell, but it is still early in the season"),
  ("ERROR_lady_selected_=_s9", "{!}ERROR: lady selected = {s9}"),
  ("s12there_is_a_feast_of_the_s3_in_progress_at_s4_but_it_has_been_going_on_for_a_couple_of_days_and_is_about_to_end_", "{s12}There is a feast of the {s3} in progress at {s4}, but it has been going on for a couple of days and is about to end. "),
  ("s12there_is_a_feast_of_the_s3_in_progress_at_s4_which_should_last_for_at_least_another_day_", "{s12}There is a feast of the {s3} in progress at {s4}, which should last for at least another day. "),
  ("s12there_is_a_feast_of_the_s3_in_progress_at_s4_which_has_only_just_begun_", "{s12}There is a feast of the {s3} in progress at {s4}, which has only just begun. "),
  ("not_at_this_time_no", "Not at this time, no."),
  ("s12the_great_lords_bring_their_daughters_and_sisters_to_these_occasions_to_see_and_be_seen_so_they_represent_an_excellent_opportunity_to_make_a_ladys_acquaintance", "{s12}The great lords bring their daughters and sisters to these occasions to see and be seen, so they represent an excellent opportunity to make a lady's acquaintance."),
  ("you_will_not_be_disappointed_sirmadam_you_will_not_find_better_warriors_in_all_calradia", "You will not be disappointed {sir/madam}. You will not find better warriors in all the world."),
  ("your_excellency", "your excellency"),
  ("s10_and_s11", "{s10} and {s11}"),
  ("your_loyal_subjects", "your loyal subjects"),
  ("loyal_subjects_of_s10", "loyal subjects of {s10}"),
  ("the", "the"),
  ("we", "we"),
  ("track_down_s7_and_defeat_him_defusing_calls_for_war_within_the_s11", "Track down {s7} and defeat him, defusing calls for war within the {s11}."),
  ("track_down_the_s9_who_attacked_travellers_near_s8_then_report_back_to_the_town", "Track down the {s9} who attacked travellers near {s8}, then report back to the town."),
  ("fire_time__reg0_cur_time__reg1", "{!}DEBUG : fire time : {reg0}, cur time : {reg1}"),
  ("fire_set_up_time_at_city_reg0_is_reg1", "{!}fire set up time at city {reg0} is {reg1}"),
  ("our_power__reg3__enemy_power__reg4", "{!}our power : {reg3}, enemy power : {reg4}"),
  #end new auto generated strings

  ("do_you_wish_to_award_it_to_one_of_your_vassals", "Do you wish to award it to one of your vassals?"),
  ("who_do_you_wish_to_give_it_to", "Who do you wish to give it to?"),
  ("sire_my_lady_we_have_taken_s1_s2", "{Sire/My lady}, we have taken {s1}. {s2}"),
  ("s12i_want_to_have_s1_for_myself", "{s12}I want to have {s1} for myself. {s2}"),
  ("fiefs_s0", "(fiefs: {s0})"),

  #reserved strigs
  ("reserved_001", "{!}Reserved 001"),
  #reserved strings end

  ("production_setting_buy_from_market",      "We are buying raw materials from the market."),
  ("production_setting_buy_from_inventory",   "We are only using the raw materials in our inventory."),
  ("production_setting_produce_to_inventory", "We are putting our output into the inventory."),
  ("production_setting_produce_to_market",    "We are selling our output directly into the inventory."),



  #Strings to add...
  #Strings for political quest outcomes

  #Notes on companions
  #Pretender and companion strings
  #Redo map color strings


#STRINGS ADDED AFTER THE FREEZE
  ("feast_quest_expired", "You were unable to hold a feast as planned. Most likely, major faction campaigns or other events intervened. You may attempt to hold the feast again, if you wish."),
  ("whereabouts_unknown", "Whereabouts unknown."),
  ("mulberry_groves", "acres of mulberry groves"),
  ("olive_groves", "acres of olive groves"),
  ("acres_flax", "acres of flax fields"),
  ("enterprise_enemy_realm", "{Sir/Madame}, you are an enemy of this realm. We cannot allow you to buy land here."),
  ("intrigue_success_chance", "{!}Your modified relation: {reg5}, {s4}'s relation: {reg4}"),

  ("you_intend_to_denounce_s14_to_s13_on_behalf_of_s12", "You intend to privately denounce {s14} to {s13} on behalf of {s12}"),
  ("you_intend_to_denounce_s14_to_his_face_on_behalf_of_s14", "You intend to openly denounce {s14} to his face, on behalf of {s12}"),
  ("you_intend_to_bring_gift_for_s14", "You intend to bring velvet and furs to {s12}. Then, speak to {s14}, to see if {s12} was able to arrange a reconciliation."),

  #Strategy AI string
  ("we_will_gather_the_army_but_not_ride_until_we_have_an_objective", "We will gather the army, but not ride forth until we have an objective."),
  ("we_shall_lay_siege_to_an_easy_fortress_to_capture", "We are concentrating out forces on their most vulnerable fortress."),
  ("we_shall_strike_at_the_heart_of_our_foe_and_seize_the_fortress_of_s14", "We intend to strike a blow which will do them the greatest damage."),
  ("we_shall_take_the_fortress_of_s14_which_appears_easily_defensible", "We aim to take a fortress which is easy for us to defend."),
  ("we_shall_cut_a_fiery_trail_through_their_richest_lands_to_draw_them_out_to_battle", "We leave a fiery trail through their richest lands to draw them out to battle."),

  #Strategy AI string
  ("strategy_criticism_rash",     "I believe that this strategy is rash, and needlessly exposes our forces to danger."),
  ("strategy_criticism_cautious", "I believe that this strategy is overly cautious, and will see our army melt away from boredom without us achieving any successes."),


  ("tavernkeeper_invalid_quest", " had some sort of business going on, but I'm having trouble remembering the details."),

  ("faction_title_male_player", "Comes {s0}"),
  ("faction_title_male_1", "Comes Rei Militaris {s0}"),
  ("faction_title_male_2", "Comes Rei Militaris {s0}"),
  ("faction_title_male_3", "Harjatuga {s0}"),
  ("faction_title_male_4", "Harjatuga {s0}"),
  ("faction_title_male_5", "Mael {s0}"),
  ("faction_title_male_6", "Argbed {s0}"),
  ("faction_title_male_7", "Harjatogo {s0}"),
  ("faction_title_male_8", "Harjatogo {s0}"),
  ("faction_title_male_9", "Harjatogo {s0}"),
  ("faction_title_male_10", "Harjatogo {s0}"),
  ("faction_title_male_11", "Harjatuga {s0}"),
  ("faction_title_male_12", "Harjatogo {s0}"),
  ("faction_title_male_13", "Dux {s0}"),
  ("faction_title_male_14", "Harjatogo {s0}"),
  ("faction_title_male_15", "Harjatuga {s0}"),
  ("faction_title_male_16", "Saspet {s0}"),
  ("faction_title_male_17", "Harjatogo {s0}"),
  ("faction_title_male_18", "Harjatogo {s0}"),
  ("faction_title_male_19", "Harjatogo {s0}"),
  ("faction_title_male_20", "Comes {s0}"),
  ("faction_title_male_21", "Harjatuga {s0}"),
  ("faction_title_male_22", "Comes {s0}"),
  ("faction_title_male_23", "Chief {s0}"),
  ("faction_title_male_24", "Saspet {s0}"),
  ("faction_title_male_25", "Phylarch {s0}"),
  ("faction_title_male_26", "Phylarch {s0}"),
  ("faction_title_male_27", "Chief {s0}"),
  ("faction_title_male_28", "Saspet {s0}"),
  ("faction_title_male_29", "Harjatogo {s0}"),
  ("faction_title_male_30", "Harjatogo {s0}"),
  ("faction_title_male_31", "Sparapet {s0}"),
  ("faction_title_male_32", "Tovisaci {s0}"),
  ("faction_title_male_33", "Chief {s0}"),
  ("faction_title_male_34", "Chief {s0}"),
  ("faction_title_male_rebel_1", "Dominus {s0}"),
  ("faction_title_male_rebel_2", "Dominus {s0}"),
  ("faction_title_male_rebel_3", "Dominus {s0}"),

  ("faction_title_female_player", "Comitessa {s0}"),
  ("faction_title_female_1", "Comitessa {s0}"),
  ("faction_title_female_2", "Comitessa {s0}"),
  ("faction_title_female_3", "Frauja {s0}"),
  ("faction_title_female_4", "Frauja {s0}"),
  ("faction_title_female_5", "{s0}"),
  ("faction_title_female_6", "{s0}"),
  ("faction_title_female_7", "Comitessa {s0}"),
  ("faction_title_female_8", "Frao {s0}"),
  ("faction_title_female_9", "Frao {s0}"),
  ("faction_title_female_10", "Frao {s0}"),
  ("faction_title_female_11", "Frauja {s0}"),
  ("faction_title_female_12", "Frao {s0}"),
  ("faction_title_female_13", "Comitessa {s0}"),
  ("faction_title_female_14", "Comitessa {s0}"),
  ("faction_title_female_15", "Frao {s0}"),
  ("faction_title_female_16", "{s0}"),
  ("faction_title_female_17", "Frao {s0}"),
  ("faction_title_female_18", "Frao {s0}"),
  ("faction_title_female_19", "Frao {s0}"),
  ("faction_title_female_20", "Comitessa {s0}"),
  ("faction_title_female_21", "Frao {s0}"),
  ("faction_title_female_22", "Comitessa {s0}"),
  ("faction_title_female_23", "Comitessa {s0}"),
  ("faction_title_female_24", "{s0}"),
  ("faction_title_female_25", "{s0}"),
  ("faction_title_female_26", "{s0}"),
  ("faction_title_female_27", "{s0}"),
  ("faction_title_female_28", "{s0}"),
  ("faction_title_female_29", "Frao {s0}"),
  ("faction_title_female_30", "{s0}"),
  ("faction_title_female_31", "{s0}"),
  ("faction_title_female_32", "{s0}"),
  ("faction_title_female_33", "{s0}"),
  ("faction_title_female_34", "{s0}"),
  ("faction_title_female_rebel_1", "{s0}"),
  ("faction_title_female_rebel_2", "{s0}"),
  ("faction_title_female_rebel_3", "{s0}"),

  ("faction_leader_title_male_player", "{s0} Augustus"),
  ("faction_leader_title_male_1", "{s0} Augustus"),
  ("faction_leader_title_male_2", "{s0} Augustus"),
  ("faction_leader_title_male_3", "Rex {s0}"),
  ("faction_leader_title_male_4", "Reiks {s0}"),
  ("faction_leader_title_male_5", "Ris {s0}"),
  ("faction_leader_title_male_6", "Shahanshah {s0}"),
  ("faction_leader_title_male_7", "Rex {s0}"),
  ("faction_leader_title_male_8", "Rex {s0}"),
  ("faction_leader_title_male_9", "Rex {s0}"),
  ("faction_leader_title_male_10", "Rex {s0}"),
  ("faction_leader_title_male_11", "Reiks {s0}"),
  ("faction_leader_title_male_12", "Rex {s0}"),
  ("faction_leader_title_male_13", "Rex {s0}"),
  ("faction_leader_title_male_14", "Reiks {s0}"),
  ("faction_leader_title_male_15", "Vandalirice {s0}"),
  ("faction_leader_title_male_16", "Mepe {s0}"),
  ("faction_leader_title_male_17", "Rex {s0}"),
  ("faction_leader_title_male_18", "Rex {s0}"),
  ("faction_leader_title_male_19", "Rex {s0}"),
  ("faction_leader_title_male_20", "Regulus {s0}"),
  ("faction_leader_title_male_21", "Rex {s0}"),
  ("faction_leader_title_male_22", "Rex {s0}"),
  ("faction_leader_title_male_23", "Rex {s0}"),
  ("faction_leader_title_male_24", "Mepe {s0}"),
  ("faction_leader_title_male_25", "Basiliskos {s0}"),
  ("faction_leader_title_male_26", "Basiliskos {s0}"),
  ("faction_leader_title_male_27", "Rex {s0}"),
  ("faction_leader_title_male_28", "Shah {s0}"),
  ("faction_leader_title_male_29", "Rex {s0}"),
  ("faction_leader_title_male_30", "Rex {s0}"),
  ("faction_leader_title_male_31", "{s0}"),
  ("faction_leader_title_male_32", "Ris {s0}"),
  ("faction_leader_title_male_33", "Rex {s0}"),
  ("faction_leader_title_male_34", "Rex {s0}"),
  ("faction_leader_title_male_rebel_1", "Defensor Civitatis {s0}"),
  ("faction_leader_title_male_rebel_2", "Defensor Civitatis {s0}"),
  ("faction_leader_title_male_rebel_3", "Defensor Civitatis {s0}"),

  ("faction_leader_title_female_player", "Queen {s0}"),
  ("faction_leader_title_female_1", "Queen {s0}"),
  ("faction_leader_title_female_2", "Queen {s0}"),
  ("faction_leader_title_female_3", "Queen {s0}"),
  ("faction_leader_title_female_4", "Queen {s0}"),
  ("faction_leader_title_female_5", "Queen {s0}"),
  ("faction_leader_title_female_6", "Queen {s0}"),
  ("faction_leader_title_female_7", "Queen {s0}"),
  ("faction_leader_title_female_8", "Queen {s0}"),
  ("faction_leader_title_female_9", "Queen {s0}"),
  ("faction_leader_title_female_10", "Queen {s0}"),
  ("faction_leader_title_female_11", "Queen {s0}"),
  ("faction_leader_title_female_12", "Queen {s0}"),
  ("faction_leader_title_female_13", "Queen {s0}"),
  ("faction_leader_title_female_14", "Queen {s0}"),
  ("faction_leader_title_female_15", "Queen {s0}"),
  ("faction_leader_title_female_16", "Queen {s0}"),
  ("faction_leader_title_female_17", "Queen {s0}"),
  ("faction_leader_title_female_18", "Queen {s0}"),
  ("faction_leader_title_female_19", "Queen {s0}"),
  ("faction_leader_title_female_20", "Queen {s0}"),
  ("faction_leader_title_female_21", "Queen {s0}"),
  ("faction_leader_title_female_22", "Queen {s0}"),
  ("faction_leader_title_female_23", "Queen {s0}"),
  ("faction_leader_title_female_24", "Queen {s0}"),
  ("faction_leader_title_female_25", "Queen {s0}"),
  ("faction_leader_title_female_26", "Queen {s0}"),
  ("faction_leader_title_female_27", "Queen {s0}"),
  ("faction_leader_title_female_28", "Queen {s0}"),
  ("faction_leader_title_female_29", "Queen {s0}"),
  ("faction_leader_title_female_30", "Queen {s0}"),
  ("faction_leader_title_female_31", "Queen {s0}"),
  ("faction_leader_title_female_32", "Queen {s0}"),
  ("faction_leader_title_female_33", "Queen {s0}"),
  ("faction_leader_title_female_34", "Queen {s0}"),
  ("faction_leader_title_female_rebel_1", "{s0}"),
  ("faction_leader_title_female_rebel_2", "{s0}"),
  ("faction_leader_title_female_rebel_3", "{s0}"),


  ("name_kingdom_text", "What will be the name of your kingdom?"),
  ("default_kingdom_name", "{s0}'s Kingdom"),

  #Defector joining
  ("lord_defects_ordinary", "{s1} has renounced {reg4?her:his} allegiance to the {s3}, and joined the {s2}"),
##diplomacy start+ fix gender of pronouns
  ("lord_defects_player",   "{s1} has renounced {reg4?her:his} allegiance to the {s3}. {reg4?She:He} has tentatively joined your kingdom. You may go to your court to receive a pledge, if you wish."),
  ("lord_defects_player_faction",   "{s1} has renounced {reg4?her:his} allegiance to the {s3}. {reg4?She:He} has tentatively joined your kingdom. You may go to your court to receive a pledge, if you wish."),
  ("lord_indicted_player_faction", "By order of {s6}, {s4} of the {s5} has been indicted for treason. The lord has been stripped of all {reg4?her:his} properties, and has fled for {reg4?her:his} life. {reg4?She:He} wishes to join your kingdom. You may find {reg4?her:him} in your court to receive {reg?her:his} allegiance, if you wish it."),
##diplomacy end+
  ("lord_indicted_dialog_approach", "Greetings, {my lord/my lady}. You may have heard of my ill treatment at the hands of {s10}. You have a reputation as one who treats {his/her} vassals well, and if you will have me, I would be honored to pledge myself as your vassal."),
  ("lord_indicted_dialog_approach_yes", "And I would be honored to accept your pledge."),
  ("lord_indicted_dialog_approach_no", "I'm sorry. Your service is not required."),
  ("lord_indicted_dialog_rejected", "Indeed? Well, perhaps your reputation is misleading. Good day, {my lord/my lady} -- I go to see if another ruler is more appreciative of my talents."),

##diplomacy start+ fix gender of pronouns with reg4
  ("_has_been_worried_about_bandits_establishing_a_hideout_near_his_home", " has been worried about bandits establishing a hideout in {reg4?her:his} area."),
##diplomacy end+
  ("bandit_lair_quest_description", "Find and destroy the {s9}, and report back to {s11}."),

  ("bandit_hideout_preattack", "You approach the hideout. The {s4} don't appear to have spotted you yet, and you could still sneak away unnoticed. The difficult approach to the site -- {s5} -- means that only a handful of troops in your party will be able to join the attack, and they will be unable to bring their horses. If your initial attack fails, the {s4} will easily be able to make their escape and disperse. Do you wish to attack the hideout, or wait for another occasion?"),
  ("bandit_hideout_failure", "The {s4} beat back your attack. You regroup, and advance again to find that they have dispersed and vanished into the surrounding countryside, where no doubt they will continue to threaten travellers."),
  ("bandit_hideout_success", "With their retreat cut off, the {s4} fall one by one to your determined attack. Their hideout, and their ill-gotten gains, as now yours."),

  ("bandit_approach_defile", "down a narrow defile"),
  ("bandit_approach_swamp", "through a pine swamp"),
  ("bandit_approach_thickets", "through a series of dense thickets"),
  ("bandit_approach_cliffs", "up a path along the side of a cliff"),
  ("bandit_approach_cove", "down a stream bed cutting through the sea-cliffs"),

  ("political_explanation_lord_lacks_center", "In this case, the fief should go to a lord who has no land and no income."),
  ("political_explanation_lord_took_center", "In this case, the fortress should go to the one who captured it."),
  ("political_explanation_most_deserving_friend", "In this case, I looked to my close friends and companions, and decided to give the fief to the most deserving."),
  ("political_explanation_most_deserving_in_faction", "In this case, I looked to all the lords of the realm, and decided to give the fief to the most deserving."),
  ("political_explanation_self", "In the absence of any clear other candidate, I nominate myself."),
  ("political_explanation_marshal", "I chose the most valiant of our nobles, whom I trust, and whose name is not currently tainted by controversy."),

  ("prisoner_at_large", "large, after the captors were defeated in battle. I expect your friend will resurface shortly."),

  ("quick_battle_scene_1", "Farmhouse"),
  ("quick_battle_scene_2", "Oasis"),
  ("quick_battle_scene_3", "Tulbuk's Pass"),
  ("quick_battle_scene_4", "Haima Castle"),
  ("quick_battle_scene_5", "Ulbas Castle"),

  ("quick_battle_troop_1", "Majorian's career in the Roman military starting following the great Roman General, Aetius. Majorian distinguished himself in the defense of Turonensis, and in the a battle against the Franks in 448. Majorian would continue to interact with the military and Roman politics, until 457, where after a battle against invading Alemmani by Lake Maggiore, he was proclaimed emperor. Majorian would continue to lead conquests retaking land in Gaul in hispania, until the destrution of his fleet and eventual murder by Ricimer in 461."),
  ("quick_battle_troop_2", "King of the Gepids, Ardaric was one of Attila's most closest and loyal vassals. However, after Attila's death Ardaric would rebel against Attila's sons, defeating them at the Battle of Nedao in 454, securing independence of the Gepids and founding a kingdom in Dacia."),
  ("quick_battle_troop_3", "A man born to shake the world, and make many powerful men fall at his knees. Hailing from the Pontic Caspian Steppes, the Huns reached the Black Sea and from there launched several campaigns against the Alans, Goths (which they quickly subjugated) and then, especially with Attila, against the Roman Empire. Attila was the son of Rua and is widely remembered as one of the greatest foes that threatened the very existence of the Roman Empire, sich as Hannibal centuries before."),
  ("quick_battle_troop_4", "One of the most powerful men of the Western Roman Empire, he was of Vandal lineage by father and Roman by mother. Regarded as one of the pillars of the Western Roman Empire during the first years of the fifth century, Stilicho is indeed one of the greatest generals of the dominate. Not only he, de facto, ruled the Western Empire after the death of Theodosis I, but he managed to defeat the Visigoths of Alaric and the Ostrogoths of Radagaisus several times during his career."),
  ("quick_battle_troop_5", "The man who stopped Attila himself at the Battle of the Catalaunian Plains in the year 451. Flavius Aetius was a general and roman consul that served faithfully the Roman Empire during his last turbulent years. Aetius is today known as one of the men that saved the Empire from its demise but was then assassinated by the Emperor Valentinianus himself who, incited by an eunuch called Eraclius, ordered to kill the general sentencing this way the Roman Empire to fall a little more than a decade later."),
  ("quick_battle_troop_6", "King of the Ostrogoths who invaded Italy. Sources describe him as a raving madman, Radagaisus was instead a warlord who led the first invasion of Italy, which failed, defeated by Flavius Stilicho. Radagaisus spread chaos in Italy for half a year untill the Roman Empire decided to gather an impressive army composed by Romans, Germans and Huns to defeat him on open field. Would he have won, Italy would have become the first barbarian kingdom in post-Roman Europe."),
  ("quick_battle_troop_7", "King of the Danubian Suebi who did not pass the Rhine and settled in Galicia, fought against Attila in the Battle of Nedao. Hunimund was known as the man who tried to stop the growing influence and power of the Ostrogoths in Pannonia. Alongside a coalition formed by his people, the Suebi of the Danube, the Sciri, Rugi and Sarmatians faced the Ostrogoths led by King Valamir at the Battle of Bolia, where he ended up defeated the year 469. After the defeat, King Valamir of the Ostrogoths adopted him as a son, but Hunimund revolted again but was eventually defeated by Ardaric few years later."),
  ("quick_battle_troop_8", "Count of Trier. Arbogast was born into a Romanized Frankish family and was a Catholic Christian. His father Arigius (mentioned by Auspicius) was possibly a native of Trier, and one of his ancestors was the 4th century magister militum Arbogastes. Arbogast was obviously highly educated, and Sidonius Apollinaris (Epistulae 4.17) praises him as one of the last defenders of the collapsing Western Roman Empire and Roman culture during the years of the political disintegration of Gaul."),
  ("quick_battle_troop_9", "Beowulf, hero of the Geats and mythical germanic character. Famous for slaying the monster Grendel and becoming the King of the Geats, Beowulf is the protagonist of an homonymous poem written in England between the 8th and the 11th century although it tells the tales of the changing political landscape of Northern Europe at the end of the 5th and the beginning of the 6th century. Widely regarded as the archetypical germanic hero, Beowulf is probably the most famous germanic character of the poems, gifted by unparallel strength, courage and cunningness."),
  ("quick_battle_troop_10", "The King of Kartli who united Georgia and led his people against the Sasanids. Part of the georgian heroic pantheon, King Vakhtang struggled to gain more autonomy for his kingdom in the Caucasua and battled repeatedly against the Kingdom of Lazika, against the Alans, the Huns and the Sasanids. He was eventually defeated and then canonized by the Georgian Orthodox Church."),
  ("quick_battle_troop_11", "Sasanian King of Kings, Peroz I led his empire through many hardships, famine and several wars. He succesfully crushed a revolt in the Caucasus, defeated the Kidarites and expanded his Empire in Sakhastan. He was then defeated and captured several times by the Hephthalites that succesfully managed to bring the Sasanian Empire to its knees, leading these nomadic foes to gain more prominence and take a leading role in the easternmost provinces of the Sasanid Empire."),
  ("quick_battle_troops_end", "{!}quick_battle_troops_end"),

  ("tutorial_training_ground_intro_message", "Walk around the training field and speak with the fighters to practice various aspects of Mount&Blade combat. You can use ASDW keys to move around. To talk to a character, approach him until his name appears on your screen, and then press the F key. You can also use the F key to pick up items, open doors and interact with objects. Press the Tab key to exit the tutorial any time you like."),

  ("map_basic", "Map"),
  ("game_type_basic", "Game Type"),
  ("battle", "Battle"),
  ("siege_offense", "Siege (Offense)"),
  ("siege_defense", "Siege (Defense)"),
  ("character", "Character"),
  ("biography", "Background"),
  ("player", "Player"),
  ("enemy", "Enemy"),
  ("faction", "Faction"),
  ("army_composition", "Army Composition"),
  ("army_size", "Army Size"),
  ("reg0_percent", "{!}{reg0}%"),
  ("reg0_men", "{reg0} men"),
  ("start", "Start"),
  ("i_need_to_raise_some_men_before_attempting_anything_else", "I need to raise some men before attempting anything else"),
  ("we_are_currently_at_peace", "We are currently at peace."),
  ("the_marshalship", "the marshalship"),

  ("you", "you"),
  ("myself", "myself"),
  ("my_friend_s15", "my friend {s15}"),
  ("custom_battle", "Custom Battle"),

  ("comment_intro_liege_affiliated_to_player", "I am told that you would dispute my claim to the crown of europe. Needless to say, I am not pleased by this news. However, we may still talk."),

  ("s21_the_s8_declared_war_out_of_personal_enmity", "{s21} The {s8} declared war out of personal enmity"),
  ("s21_the_s8_declared_war_in_response_to_border_provocations", "{s21} The {s8} declared war in response to border provocations"),
  ("s21_the_s8_declared_war_to_curb_the_other_realms_power", "{s21} The {s8} declared war to curb the other realm's power"),
  ("s21_the_s8_declared_war_to_regain_lost_territory", "{s21} The {s8} declared war to regain lost territory"),

  ("_family_", "^Family: "),

  ("we_are_conducting_recce", "We will first scout the area, and then decide what to do."),

  ("_family_dupe", "^Family:"), #SB : duplicate string
  ("s49_s12_s11_end", "{s49} {s12} ({s11})."),

 ("center_party_to_far_away", "is not our target, because it is too far away from our main army."),
  ("center_party_not_active", "is not our target, because we don't have a leader who has taken the field."),
  ("center_is_friendly", "is not our enemy."),
  ("center_is_already_besieged", "is already under siege."),
  ("center_is_looted_or_raided_already", "is already been laid waste."),
  ("center_marshal_does_not_want_to_attack_innocents", "is inhabited by common folk, who would suffer the most if the land is laid waste."),
  ("center_we_have_already_committed_too_much_time_to_our_present_siege_to_move_elsewhere", "is already under siege, so it would be a mistake to move elsewhere."),
  ("center_we_are_already_here_we_should_at_least_loot_the_village", "is close at hand, we should take hold of its wealth and lay waste to the rest."),

  ("center_far_away_we_can_reconnoiter_but_will_delay_decision_until_we_get_close", "NOT USED"),
  ("center_far_away_our_cautious_marshal_does_not_wish_to_reconnoiter", "is too far away, even to reconnoiter."),
  ("center_far_away_even_for_our_aggressive_marshal_to_reconnoiter", "is too far away, even to reconnoiter."),

  ("center_far_away_reason", "{s6} is further than {s5} to our centers, therefore it will be harder for us to protect after taking it."),
  ("center_closer_but_this_is_not_enought", "{s6} is closer than {s5} to our borders, but because of other reasons we are not attacking {s6} for now."),

  ("center_protected_by_enemy_army_aggressive", "is protected by enemy forces, which we believe to be substantially stronger than our own."),
  ("center_protected_by_enemy_army_cautious", "is protected by an enemy army, which we believe to be too strong to engage with confidence of victory."),

  ("center_cautious_marshal_believes_center_too_difficult_to_capture", "would require a bloody and risky siege."),
  ("center_even_aggressive_marshal_believes_center_too_difficult_to_capture", "is too heavily defended to capture."),

  ("center_value_outweighed_by_difficulty_of_capture", "is not of sufficient value to justify the difficulty of attacking it"),
  ("center_value_justifies_the_difficulty_of_capture", "can be taken, and is of sufficient value to justify an attack."),

  ("center_is_indefensible", "is too far away from our other fortresses to be defended."),
  ("we_are_waiting_for_selection_of_marshal", "We are waiting for the selection of a marshal"),
  ("best_to_attack_the_enemy_lands", "Given the size of our forces, we believe the best approach is to attack the enemy's lands."),
  ("we_believe_the_fortress_will_be_worth_the_effort_to_take_it", "We believe the fortress will be worth the effort to take it."),
  ("we_will_gather_to_defend_the_beleaguered_fortress", "We will gather to defend the beleaguered fortress"),
  ("the_enemy_temporarily_has_the_field", "The enemy temporarily has the field, and we should seek refuge until the storm passes"),
  ("center_has_not_been_scouted", "has not been recently scouted by our forces, but we can go there, and decide what to do when we get close."),
  ("we_have_assembled_some_vassals", "We have assembled some of the vassals, but we will wait until we have more before venturing into enemy territory."),

  ("we_are_waiting_here_for_vassals", "We are waiting for the vassals to join us."),
  ("we_are_travelling_to_s11_for_vassals", "We are travelling to {s11}, so that the vassals may more easily join our host before we ride forth."),

  ("center_strength_not_scouted", "We have not scouted it recently, and do not know how strongly it is defended"),
  ("center_strength_strongly_defended", "We believe it to be strongly defended"),
  ("center_strength_moderately_defended", "We believe it to be moderately well defended"),
  ("center_strength_weakly_defended", "We believe it to be weakly defended"),

  ("center_distant_from_concentration", "is close to us than it is to the main enemy army, which we have located. It could be attacked and destroyed before they are able to respond"),

  ("plus", "+"),
  ("minus", "-"),

  ("tutorial_training_ground_warning_no_weapon", "Hey, don't you think you need some sort of weapon before we try that? There should be some spare weapons over there. Just go pick one up."),
  ("tutorial_training_ground_warning_shield", "You need to put down your shield first. Scroll down with the mouse scroll-wheel to put down your shield."),
  ("tutorial_training_ground_warning_melee_with_parry", "You need to wield a melee weapon for this exercise. "),
  ("tutorial_training_ground_warning_melee", "Scroll up with your mouse wheel to equip a weapon. Scrolling up will equip next weapon while scrollng down will equip next shield."),
  ("tutorial_training_ground_attack_training", "Number of successful attacks: {reg0} / 5^Number of unsuccessful attacks: {reg1}^{s0}"),
  ("tutorial_training_ground_attack_training_down", "Make a thrust attack! (Move your mouse down while pressing the left mouse button)"),
  ("tutorial_training_ground_attack_training_up", "Make an overhead attack! (Move your mouse up while pressing the left mouse button)"),
  ("tutorial_training_ground_attack_training_left", "Attack from left! (Move your mouse left while pressing the left mouse button)"),
  ("tutorial_training_ground_attack_training_right", "Attack from right! (Move your mouse right while pressing the left mouse button)"),
  ("tutorial_training_ground_parry_training", "Number of successful parries: {reg0} / 5"),
  ("tutorial_training_ground_chamber_training", "Number of successful chambering blocks: {reg0} / 5"),
  ("tutorial_training_ground_archer_training", "Number of nice shots: {reg0} / 3^{s0}"),
  ("tutorial_training_ground_ammo_refill", "Your missiles are refilled for the tutorial."),
  ("tutorial_training_ground_archer_text_1", "Approach the {s0} and press F to pick it up."),
  ("tutorial_training_ground_archer_text_2", "Shoot the targets now."),
  ("tutorial_training_ground_archer_text_3", "The size of the targeting reticule indicates your accuracy. Press and hold down the left mouse button until the reticule shrinks down to its minimum size. Release the left mouse button when the reticule is at its smallest. If you wait too long the reticule will expand again."),
  ("tutorial_training_ground_archer_text_4", "Press R to toggle first person view. First person view makes it easier to aim with ranged weapons."),
  ("tutorial_training_ground_archer_text_5", "You have shot all the targets. Now talk to the trainer again."),
  ("tutorial_training_ground_horseman_text_1", "Go near the {s0} and press F to pick it up."),
  ("tutorial_training_ground_horseman_text_2", "Approach the horse and press F to mount."),
  ("tutorial_training_ground_horseman_text_3", "Ride towards the next waypoint."),
  ("tutorial_training_ground_horseman_text_4", "Strike the next dummy that has an arrow on top of it!"),
  ("tutorial_training_ground_horseman_text_5", "Shoot at the archery target that has an arrow on top of it!"),
  ("tutorial_training_ground_horseman_text_6", "You have finished the exercise successfully. Now go back to the trainer and talk to him."),

  ("the_great_lords_of_your_kingdom_plan_to_gather_at_your_hall_in_s10_for_a_feast", "The great lords of your kingdom plan to gather at your hall in {s10} for a feast"),
  ("your_previous_court_some_time_ago", "your previous court some time ago,"),
  ("awaiting_the_capture_of_a_fortress_which_can_serve_as_your_court", "awaiting the recapture of a fortress which can serve as your court."),
  ("but_if_this_goes_badly", " I value your advice. But if this goes badly, I shall hold you responsible."),

  ("i_realize_that_you_are_on_good_terms_with_s4_but_we_ask_you_to_do_this_for_the_good_of_the_realm", " I realize that you are on good terms with {s4}, but this is all for the good of the realm"),
##diplomacy start+ todo xxx gender correct ##diplomacy end+
  ("i_realize_that_you_are_on_good_terms_with_s4_but_the_blow_will_hurt_him_more", "I realize that you are on good terms with {s4} -- but this only means that your blow will hit him even harder!"),

  ("killed_bandit_at_alley_fight", "The merchant takes you to his house. Once inside, he stands by the door for a while checking the street, and then, finally convinced you have not been followed, comes near you to speak..."),
  ("wounded_by_bandit_at_alley_fight", "You are struck down. However, before you lose consciousness, you hear shouts and a rush of footfalls... You awake to find yourself indoors, weak but alive."),

  ("cannot_leave_now", "Cannot leave now."),
  ("press_tab_to_exit_from_town", "Press Tab to leave now. You can press Tab key to quickly exit any location in the game."),
  ("find_the_lair_near_s9_and_free_the_brother_of_the_prominent_s10_merchant", "Find the bandit lair near {s9}, and free the brother of the {s10} merchant."),
  ("please_sir_my_lady_go_find_some_volunteers_i_do_not_know_how_much_time_we_have", "{Sir/My lady} -- if you want to justify the trust which I have placed in you, then make a bit of haste. Go find some volunteers. I'm not sure how much time we have."),
  ("you_need_more_men_sir_my_lady", "Look -- you need more men. Right now, you have only {reg0} in your party. If you attack them with too few men, you may find their hideout by getting yourself dragged up to it in fetters, and that's not the plan. Do not take that risk. Go out and visit some more villages to find more volunteers, and then you can start paying them back in their own coin."),
  ("good_you_have_enough_men", "Good, good. You did well. You have enough men. Now, go and knock some of those robbers over the head, and make them tell you how to find their hideout."),
  ("do_not_waste_time_go_and_learn_where_my_brother_is", "Look, {sir/my lady}. Time is at a bit of premium, here. Now, if you could go find out where they are hiding my brother, that would be appreciated."),

  ("start_up_quest_message_1", "{s9} wants you to collect at least five men from nearby villages. After you collect these men, find and speak with him. He is in the tavern at {s1}"),
  ("start_up_quest_message_2", "Find and defeat a group of bandits lurking near {s9}, and learn where your employer's brother has been taken."),
  ("start_up_quest_message_3", "Rescue the merchant's brother from the robber's hideout located near {s9}."),
  ("start_up_first_quest", "You have taken your first quest. You may view your quest log by pressing 'Q' anytime in the game."),

  ("reason_1", "Our current objective is of greater value."),
  ("reason_2", "An attack on {s8} poses a greater danger to our realm."),
  ("reason_3", "We believe that {s8} faces a more immediate threat"),
  ("reason_4", "It may be because of the size of the enemy forces in the area."),
  ("reason_5", "I'm not sure."),
  ("reason_6", "We do not know how strongly it is defended."),
  ("reason_7", "We believe it to be strongly defended."),
  ("reason_8", "We believe it to be moderately well defended."),
  ("reason_9", "We believe it to be weakly defended."),

  ("has_decided_that_an_attack_on_", "has decided to attack"),
  ("this_would_be_better_worth_the_effort", "This would be better worth the effort, taking into consideration its value, and its distance, and the likely number of defenders."),
  ("has_decided_to_defend_", "has decided to defend"),
  ("before_going_offensive_we_should_protect_our_lands_if_there_is_any_threat_so_this_can_be_reason_marshall_choosed_defending_s4", "Before going offensive we should protect our lands if there is any threat. So this can be reason marshall choosed defending {s4}."),

  ("are_you_all_right", "Now... Let me explain my proposition"),
  ("you_are_awake", "Ah -- you're awake. It's good to see that you can still walk. You're lucky that we came along. I had been speaking with the watch, when we heard the sounds of a fight and ran to see what was happening. We didn't arrive in time to prevent you getting knocked down, but we may have saved you from getting your throat cut... Now... Maybe you can help me..."),
  ("save_town_from_bandits", "Save {s9} from bandits."),

  ("you_fought_well_at_town_fight_survived", "Hah! Well done -- I saw at least three of the enemy go down before you. Keep fighting like that, and you'll make quite a name for yourself in this land. "),
  ("you_fought_normal_at_town_fight_survived", "Well done! I hear you accounted for one or two of the bastards, and you're still on your feet. You can't ask for a better outcome of a battle than that..."),
  ("you_fought_bad_at_town_fight_survived", "Well, the enemy is in flight, and it looks like you're still on your feet. At the end of the day, that's all that's important in a battle."),

  ("you_fought_well_at_town_fight", "Ah! You're awake. You took quite a blow, there. But good news! We defeated them -- and you did them some real damage before you went down. If you hadn't been here, it could have gone very baldy. I'm grateful to you..."),
  ("you_wounded_at_town_fight", "Ah! You're alive. That's a relief. You took quite a blow, there. I'm not sure that you got any of them yourself, but thankfully, the rest of us were able to beat them. We'll need to see about getting you some treatment.... "),

  ("you_fought_well_at_town_fight_survived_answer", "Let every villain learn to fear the name {playername}!"),
  ("you_fought_normal_at_town_fight_survived_answer", "Ah, well, I'm proud to have done my bit along with the rest..."),
  ("you_fought_bad_at_town_fight_survived_answer", "Well, I was about to strike one down, but I slipped in some blood, you see..."),
  ("you_fought_well_at_town_fight_answer", "Ah well. I guess I don't mind a blow taken in a good cause."),
  ("you_wounded_at_town_fight_answer", "Right. I suppose I should be more careful."),

  ("unfortunately_reg0_civilians_wounded_during_fight_more", " Unfortunately, about {reg0} of my lads got themselves wounded. I should go look on on them."),
  ("unfortunately_reg0_civilians_wounded_during_fight", " Unfortunately, one of my lads took a pretty nasty blow. I should go see how he is doing."),
  ("also_one_another_good_news_is_any_civilians_did_not_wounded_during_fight", " Also, no one on our side was hurt very seriously. That's good news"),

  ("merchant_and_you_call_some_townsmen_and_guards_to_get_ready_and_you_get_out_from_tavern", "You leave the tavern and go out to the streets. Nervous looking young men are waiting in every street corner. You can see they have daggers and clubs concealed under their clothes, and catch a mixture of fear, anticipation and pride in the quick looks they throw at you as you pass by. Praying that your enemies have not been alarmed by this all too obvious bunch of plotters, you check your weapons for one last time and prepare yourself for the action ahead."),
  ("town_fight_ended_you_and_citizens_cleaned_town_from_bandits", "The remaining few bandits scatter off to the town's narrow alleys, only to be hunted down one by one by the angry townsfolk. Making sure that your victory is complete and all the wounded have been taken care of, you and the merchant head to his house to review the day's events."),
  ("town_fight_ended_you_and_citizens_cleaned_town_from_bandits_you_wounded", "You fall down with that last blow, unable to move and trying hard not to pass out. Soon the sounds of fighting filling the street gives way to the cheers of the townsmen and you realize with relief that your side won the day. Soon, friendly arms pick you up from the ground and you let yourself drift off to a blissful sleep. Hours later, you wake up in the merchants house."),


  ("journey_to_reyvadin", "You arrived at Constantinople, capital of the Eastern Roman Empire"),
  ("journey_to_praven", "You came by ship to the administrative capital of the Western Roman Empire, Ravenna."),
  ("journey_to_jelkala", "You came by ship to the city of Londinium, in Britannia."),
  ("journey_to_sargoth", "You came by ship to the city of Cartago, former bread basket of the Roman Empire."),
  ("journey_to_tulga", "You came with a caravan to the city of Tournacum, under the Rule of the Franks."),
  ("journey_to_shariz", "You came with a caravan to the great city of Ctesiphon, capital of the Sassanid Persian Empire."),

  ("lost_tavern_duel_ordinary", "You slump to the floor, stunned by the drunk's last blow. Your attacker's rage immediately seems to slacken. He drops into a chair and sits there watching you, muttering under his breath, almost regretfully. A few of the other patrons manage to coax him to his feet and bundle him out the door. One of the others attends to your wounds, and soon you too are back on your feet, unsteady but alive."),
  ("lost_tavern_duel_assassin", "You slump to the floor, stunned by your attacker's last blow. Slowly and deliberately, he kneels down by your side, pulling a long knife from under his clothes. But before he can finish you off, the tavernkeeper, who seems to have regained his courage, comes up from behind and gives your attacker a clout behind the head. He loses his balance, and then, seeing that his chance to kill you has been lost, makes a dash for the door. He gets away. Meanwhile, the other tavern patrons bind your wounds and haul you to a back room to rest and recover."),
  ("lost_startup_hideout_attack", "You recover consciousness a short while later, and see that the kidnappers have celebrated their victory by breaking open a cask of wine, and have forgotten to take a few elementary precautions -- like binding your hands and feet. You manage to slip away. Based on the boisterous sounds coming from the hideout, you suspect that you may yet have some time to gather a few more followers and launch another attack."),
  ("reg1_blank_s3", "{!}{reg1} {s3}"),

  #SB : extra space
("as_you_no_longer_maintain_an_independent_kingdom_you_no_longer_maintain_a_court",  "As you no longer rule an independent kingdom, you no longer maintain a court"),

("rents_from_s0",  "Rents from {s0}:"),
("tariffs_from_s0",  "Tariffs from {s0}:"),
("general_quarrel",  " We've found ourselves on the opposite side of many arguments over the years, and bad blood has built up between us."),

#these are for resetting old {!} party names for the spawnpoints
("the_steppes", "the steppe"),
("the_deserts", "the desert"),
("the_tundra", "the tundra"),
("the_forests", "the forests"),
("the_highlands", "the highlands"),
("the_coast", "the coast"),
  ##diplomacy start+ make gender-correct
  ("my_lady_not_sufficient_chemistry", "My {lord/lady}, there are other {suitors/maidens} who have captured my heart."),
  ("my_lady_engaged_to_another", "My {lord/lady}, as I understand it, you are engaged to another."),
  ##diplomacy end+
  ("attempting_to_rejoin_party", "Attempting to rejoin party,"),
  ("separated_from_party", "Separated from party,"),
  #("whereabouts_unknown", "whereabouts unknown"),

  ("none_yet_gathered", "{!}None yet gathered"),

  ("betrothed_dupe", " Betrothed "), #SB : unused
  ("leading_party", "leading a party"),
  ("court_disbanded", "As you no longer rule an independent kingdom, your court has been disbanded"),
  ("i_am_not_accompanying_the_marshal_because_will_be_reappointment", " I am not accompanying the marshal, because I suspect that our ruler will shortly appoint another to that post."),

  ("persuasion_opportunity", "Persuasion opportunity.^Relation required for automatic success: {reg4}^Current relationship: {reg5}^Chance of success: {reg7}^Chance of losing {reg9} relation point(s): {reg8}"),

  ("marshal_warning", "You are not following {s1}. However, you will not suffer any penalty."),

  ("follow_army_quest_brief_2", "Your mission is complete. You may continue to follow {s9}'s army, if you wish further assignments."),

  ("greetings_playername__it_is_good_to_see_you_i_hope_that_you_have_had_success_in_your_efforts_to_make_your_name_in_the_world", " I am glad to see you. I trust you are having some success out there, making your name in the world"),

  ("minister_advice_select_fief", " Might I suggest that you select {s4}, as the vassals have been speculating about how you might assign it."),
  ("minister_advice_select_fief_wait", " Might I suggest that you wait until after you have appointed a marshal, as that will give time to the vassals to decide whom they wish to support."),
  ("minister_advice_fief_leading_vassal", " {s4}, by the way, has already received the support of {reg4} of your vassals."),
  ("unassigned_center", " (unassigned)"),
  ("s43_also_you_should_know_that_an_unprovoked_assault_is_declaration_of_war", "{s43} Also, as you are the ruler of your realm, you should know that this assault constitutes a declaration of war."),
  ("missing_after_battle", "Missing after battle"),
  ("retrieve_garrison_warning", " (Troops might not be retrievable if fortress awarded to another)"),

  ("s12s15_declared_war_to_control_calradia", "{s12}{s15} may attack {s16} without pretext, as a bid to extend control over all."),
  #SB : removed prepadding and period, s10 in dialogue already had these
  ("offer_gift_description", "improve my standing by offering a gift"),
  ("resolve_dispute_description", "improve my standing by resolving a dispute"),
#diplomacy start+ potential gender correction
  ("feast_wedding_opportunity", " If your betrothed and {her/his} family are present, then this may be an opportunity for you to celebrate the wedding."),
#diplomacy end+
  ("s21_the_s8_declared_war_as_part_of_a_bid_to_conquer_all_calradia", "{s21}. The {s8} declared war with very little pretext, as part of a bid to conquer all."),
  ("master_vinter", "Master vinter"),
  ("s54_has_left_the_realm", "{s54} has left the realm."),
  ("enterprise_s5_at_s0", "Net revenue from {s5} at {s0}"),

  ("bread_site", "mill"),
  ("ale_site", "brewery"),
  ("oil_site", "oil press"),
  ("wine_site", "wine press"),
  ("tool_site", "ironworks"),
  ("leather_site", "tannery"),
  ("linen_site", "linen weavery"),
  ("wool_cloth_site", "wool weavery"),
  ("velvet_site", "dyeworks"),

  ("under_sequestration", "Under sequestration"),
  ("describe_secondary_input", " In addition, you will also need to purchase {s11} worth {reg10} siliquae."),
  ("profit", "profit"),
  ("loss", "loss"),

  ("server_name_s0", "Server Name: {s0}"),
  ("map_name_s0", "Map Name: {s0}"),
  ("game_type_s0", "Game Type: {s0}"),
  ("remaining_time_s0reg0_s1reg1", "Remaining Time: {s0}{reg0}:{s1}{reg1}"),
  ("you_are_a_lord_lady_of_s8_s9", "You are a {lord/lady} of {s8}.^{s9}"),
  ("you_are_king_queen_of_s8_s9", "You are {king/queen} of {s8}.^{s9}"),
  ("for_s4", " for {s4}"),

  ("cancel_fiancee_quest", " Also, you should please consider that other matter I had asked of you to have been successfully completed. It is not fit for me to commission you with tasks."),
  ("a_duel_request_is_sent_to_s0", "A duel offer is sent to {s0}."),
  ("s0_offers_a_duel_with_you", "{s0} offers a duel with you."),
  ("your_duel_with_s0_is_cancelled", "Your duel with {s0} is cancelled."),
  ("a_duel_between_you_and_s0_will_start_in_3_seconds", "A duel between you and {s0} will start in 3 seconds."),
  ("you_have_lost_a_duel", "You have lost a duel."),
  ("you_have_won_a_duel", "You have won a duel!"),
  ("server_s0", "[!]: {s0}"),
  ("disallow_ranged_weapons", "Disallow ranged weapons"),
  ("ranged_weapons_are_disallowed", "Ranged weapons are disallowed."),
  ("ranged_weapons_are_allowed", "Ranged weapons are allowed."),
  ("duel_starts_in_reg0_seconds", "Duel starts in {reg0} seconds..."),

  ##diplomacy begin
###################################################################################
# Autoloot
###################################################################################
	("dplmc_none", "none"),

	("dplmc_item_pool_no_items", "There are currently no items in the item pool."),
	("dplmc_item_pool_one_item", "There is one item left in the item pool."),
	("dplmc_item_pool_many_items", "There are {reg20} items left in the item pool."),
	("dplmc_item_pool_abandon", "Leave the items in the item pool and continue."),
	("dplmc_item_pool_leave", "Done."),

	("dplmc_hero_not_upgrading_armor","not upgrading my armor"),
	("dplmc_hero_upgrading_armor","upgrading my own armor"),
	("dplmc_hero_not_upgrading_horse","not upgrading my horses"),
	("dplmc_hero_upgrading_horse","upgrading my own horses"),

	("dplmc_hero_wpn_slot_none","Keep current ({s10})"), #0
	("dplmc_hero_wpn_slot_horse","Horse"), #1 to maintain compatibility with header_items (item type 1 is horse)
	("dplmc_hero_wpn_slot_one_handed","One-handed Weapon"), #2
	("dplmc_hero_wpn_slot_two_handed","Two-handed Weapon"),  #3
	("dplmc_hero_wpn_slot_polearm_all","Polearms"), #4
	("dplmc_hero_wpn_slot_arrows","Arrows"), #5
	("dplmc_hero_wpn_slot_bolts","Bolts"), #6
	("dplmc_hero_wpn_slot_shield","Shield"), #7
	("dplmc_hero_wpn_slot_bow","Bow"), #8
	("dplmc_hero_wpn_slot_crossbow","Crossbow"), #9
	("dplmc_hero_wpn_slot_throwing","Throwing Weapon"), #10
  ##diplomacy start+ importing latest CC autoloot
	("dplmc_hero_wpn_slot_goods", "Goods "), #11
	("dplmc_hero_wpn_slot_head_armor", "Head armor "), #12
	("dplmc_hero_wpn_slot_body_armor", "Body armor "), #13
	("dplmc_hero_wpn_slot_foot_armor", "Foot armor "), #14
	("dplmc_hero_wpn_slot_hand_armor", "Hand armor "), #15
	("dplmc_hero_wpn_slot_pistol", "Pistol "), #16
	("dplmc_hero_wpn_slot_musket", "Musket "), #17
	("dplmc_hero_wpn_slot_bullets", "Bullets "), #18
	("dplmc_hero_wpn_slot_animal", "Animal "), #19
	("dplmc_hero_wpn_slot_book", "Book "), #20
  ##diplomacy end+
  #### Autoloot improved by rubik begin
	("dplmc_hero_wpn_slot_two_handed_one_handed","Two-handed/One-handed"), #11
  #### Autoloot improved by rubik end
###################################################################################
# End Autoloot
###################################################################################

  ("dplmc_gather_information", "gather information"),
  ("dplmc_conclude_non_agression", "conclude a non-aggression treaty"),
  ("dplmc_nearly_no", "nearly no"),
  ("dplmc_less_than_one_hundred", "less than one hundred"),
  ("dplmc_more_than_one_hundred", "more than one hundred"),
  ("dplmc_more_than_two_hundred", "more than two hundred"),
  ("dplmc_more_than_five_hundred", "more than five hundred"),
  ("dplmc_bring_gift", "bring the gift"),
  ("dplmc_exchange_prisoner","to exchange {s10} against {s11}"),
  ("dplmc_has_been_set_free", "{s7} has been set free."),
  ("dplmc_tax_very_low", "very low"),
  ("dplmc_tax_low", "low"),
  ("dplmc_tax_normal", "normal"),
  ("dplmc_tax_high", "high"),
  ("dplmc_tax_very_high", "very high"),
  ("dplmc_place_is_occupied_by_insurgents","The place is held by insurgents."),
  #nested diplomacy start+
  #Alter prepositions for dplmc_relation_****_**_ns
  #   indifferent against -> indifferent towards
  #   resentful against   -> resentful towards
  #Also changed pronouns to be gender-correct: "He" to {reg4?She:He}
  ("dplmc_relation_mnus_100_ns", "{reg4?She:He} seems to be vengeful towards {s59}."), # -100..-94
  ("dplmc_relation_mnus_90_ns",  "{reg4?She:He} seems to be vengeful towards {s59}."),  # -95..-84
  ("dplmc_relation_mnus_80_ns",  "{reg4?She:He} seems to be vengeful towards {s59}."),
  ("dplmc_relation_mnus_70_ns",  "{reg4?She:He} seems to be hateful towards {s59}."),
  ("dplmc_relation_mnus_60_ns",  "{reg4?She:He} seems to be hateful towards {s59}."),
  ("dplmc_relation_mnus_50_ns",  "{reg4?She:He} seems to be hostile towards {s59}."),
  ("dplmc_relation_mnus_40_ns",  "{reg4?She:He} seems to be angry towards {s59}."),
  ("dplmc_relation_mnus_30_ns",  "{reg4?She:He} seems to be resentful towards {s59}."),
  ("dplmc_relation_mnus_20_ns",  "{reg4?She:He} seems to be grumbling against {s59}."),
  ("dplmc_relation_mnus_10_ns",  "{reg4?She:He} seems to be suspicious towards {s59}."),
  ("dplmc_relation_plus_0_ns",   "{reg4?She:He} seems to be indifferent towards {s59}."),# -5...4
  ("dplmc_relation_plus_10_ns",  "{reg4?She:He} seems to be cooperative towards {s59}."), # 5..14
  ("dplmc_relation_plus_20_ns",  "{reg4?She:He} seems to be welcoming towards {s59}."),
  ("dplmc_relation_plus_30_ns",  "{reg4?She:He} seems to be favorable to {s59}."),
  ("dplmc_relation_plus_40_ns",  "{reg4?She:He} seems to be supportive to {s59}."),
  ("dplmc_relation_plus_50_ns",  "{reg4?She:He} seems to be friendly to {s59}."),
  ("dplmc_relation_plus_60_ns",  "{reg4?She:He} seems to be gracious to {s59}."),
  ("dplmc_relation_plus_70_ns",  "{reg4?She:He} seems to be fond of {s59}."),
  ("dplmc_relation_plus_80_ns",  "{reg4?She:He} seems to be loyal to {s59}."),
  ("dplmc_relation_plus_90_ns",  "{reg4?She:He} seems to be devoted to {s59}."),
  ("dplmc_s39_rival", " {reg4?She:He} scents rivals in {s39}"),
  ##nested diplomacy end+
  ("dplmc_s41_s39_rival", "{s41}, {s39}"),
  ##nested diplomacy start+
  #Changed pronouns to be gender-correct: "He" to {reg4?She:He}, etc.
  ("dplmc_s40_love_interest_s39", "{s40}. Aside from that {reg4?her:his} love interest is {s39}."),
  ("dplmc_s40_betrothed_s39", "{s40}. Aside from that {reg4?she:he} is betrothed to {s39}."),
  ("dplmc_reputation_martial", "It is said that {s46} is a martial person."),
  ("dplmc_reputation_debauched", "It is said that {s46} is a debauched person."),
  ("dplmc_reputation_pitiless", "It is said that {s46} is a pitiless person."),
  ("dplmc_reputation_calculating", "It is said that {s46} is a calculating person."),
  ("dplmc_reputation_quarrelsome", "It is said that {s46} is a quarrelsome person."),
  ("dplmc_reputation_goodnatured", "It is said that {s46} is a good-natured person."),
  ("dplmc_reputation_upstanding", "It is said that {s46} is a upstanding person."),
  ("dplmc_reputation_conventional", "It is said that {s46} is a conventional person."),
  ("dplmc_reputation_adventurous", "It is said that {s46} is a adventurous person."),
  ("dplmc_reputation_romantic", "It is said that {s46} is a romantic person."),
  ("dplmc_reputation_moralist", "It is said that {s46} is a moralist."),#Moralist -> moralist
  ("dplmc_reputation_ambitious", "It is said that {s46} is a ambitious person."),
  ("dplmc_reputation_unknown", "{s46}'s motivations are a closed book."),#Rewrote
  ##nested diplomacy end+
  ("dplmc_s21__the_s5_is_bound_by_alliance_not_to_attack_the_s14s18_it_will_expire_in_reg1_days", "{s21}^* The {s5} has formed an alliance with the {s14}.{s18} It will degrade into a defensive pact in {reg1} days."),
  ("dplmc_s21__the_s5_is_bound_by_defensive_not_to_attack_the_s14s18_it_will_expire_in_reg1_days", "{s21}^* The {s5} has agreed to a defensive pact with the {s14}.{s18} It will degrade into a trade agreement in {reg1} days."),
  ("dplmc_s21__the_s5_is_bound_by_trade_not_to_attack_the_s14s18_it_will_expire_in_reg1_days", "{s21}^* The {s5} has agreed to a trade agreement with the {s14}.{s18} It will degrade into a non-aggression pact in {reg1} days."),
  ("dplmc_small","small"),
  ("dplmc_medium","medium"),
  ("dplmc_big","big"),
  ("dplmc_elite","elite"),
  ("dplmc_very_decentralized", "very decentralized"),
  ("dplmc_quite_decentralized", "quite decentralized"),
  ("dplmc_little_decentralized", "a little decentralized"),
  ("dplmc_neither_centralize_nor_decentralized","neither too centralized nor decentralized"),
  ("dplmc_little_centralized", "a little centralized"),
  ("dplmc_quite_centralized", "quite centralized"),
  ("dplmc_very_centralized", "very centralized"),
  ("dplmc_very_plutocratic", "very plutocratic"),
  ("dplmc_quite_plutocratic", "quite plutocratic"),
  ("dplmc_little_plutocratic", "a little plutocratic"),
  ("dplmc_neither_aristocratic_nor_plutocratic","neither too aristocratic nor plutocratic"),
  ("dplmc_little_aristocratic", "a little aristocratic"),
  ("dplmc_quite_aristocratic", "quite aristocratic"),
  ("dplmc_very_aristocratic", "very aristocratic"),
  ("dplmc_all_free", "almost all free"),
  ("dplmc_mostly_free", "mostly free"),
  ("dplmc_usually_free", "usually free"),
  ("dplmc_mixture_serfs", "a mixture of serfs and freeman"),
  ("dplmc_usually_serfs", "usually serfs"),
  ("dplmc_mostly_serfs", "mostly serfs"),
  ("dplmc_all_serfs", "almost all serfs"),
  ("dplmc_very_quantity", "a vast number of soldiers"),
  ("dplmc_great_quantity", "very many soldiers"),
  ("dplmc_good_quantity", "many soldiers"),
  ("dplmc_mediocre_quality", "a mediocre quality"),
  ("dplmc_good_quality", "a good quality"),
  ("dplmc_great_quality", "a great quality"),
  ("dplmc_very_quality", "a very high quality"),
  ("dplmc_s21_the_s8_declared_war_to_fulfil_pact", "{s21}. The {s8} declared war to fulfil a pact"),
 ##diplomacy end
 ##diplomacy start+
 ("dplmc_very_laissez_faire", "very laissez-faire"),
 ("dplmc_quite_laissez_faire", "quite laissez-faire"),
 ("dplmc_little_laissez_faire", "a little laissez-faire"),
 ("dplmc_neither_mercantilist_nor_laissez_faire","neither particularly mercantilist nor entirely laissez-faire"),
 ("dplmc_little_mercantilist", "a little mercantilist"),
 ("dplmc_quite_mercantilist", "quite mercantilist"),
 ("dplmc_very_mercantilist", "very mercantilist"),

  ("dplmc_how_will_your_male_vassals_be_known","How will your male vassals be known?"),
  ("dplmc_how_will_your_female_vassals_be_known","How will your female vassals be known?"),
  ("dplmc_s40_married_s39", "{s40}. Aside from that {reg4?she:he} is married to {s39}."),
 #For fief exachange
 #TODO: customize responses by relation and/or personality
  ("dplmc_fief_exchange_ask_interest", "Would you be interested in exchanging fiefs?"),
  ("dplmc_fief_exchange_not_interested","No, I would not be interested in that."),

  ("dplmc_fief_exchange_listen", "This is somewhat unusual but not unprecendented.  I will listen.  Which fief of mine did you have in mind?"),
  ("dplmc_fief_exchange_listen_player_approval", "This is somewhat unusual, but since you're the {king/queen} there is no one to object.  Which fief of mine did you have in mind?"),
  ("dplmc_fief_exchange_listen_s10_approval", "This is somewhat unusual, but unless {s10} objects there is no reason we could not.  Which fief of mine did you have in mind?"),

  ("dplmc_fief_exchange_listen_2", "What fief do you offer in exchange?"),

  ("dplmc_fief_exchange_refuse_home", "I have no intention of giving up {s14}."),
  ("dplmc_fief_exchange_refuse_town", "I don't want to exchange a town for a castle or village."),
  ("dplmc_fief_exchange_refuse_castle", "I don't want to exchange a castle for a mere village."),
  ("dplmc_fief_exchange_refuse_rich", "I don't want to exchange a richer fief for one that much poorer."),
  ("dplmc_fief_exchange_refuse_s14_attack", "Speak of this to me later when {s14} is not under attack."),

  ("dplmc_fief_exchange_accept", "That exchange is acceptable to me."),
  ("dplmc_fief_exchange_accept_reg3_denars", "That exchange is acceptable to me, if you are willing to provide {reg3} siliquae to cover my expenses from the relocation."),

  ("dplmc_fief_exchange_confirm","It is settled then."),
  ("dplmc_fief_exchange_confirm_reg3_denars","It is settled then.  Here are your {reg3} siliquae."),
  #Other dialog
  ("dplmc_your_s11_s10", "Your {s11}, {s10}"),
  ("dplmc_reg6my_reg7spouse", "{reg6?M:m}y {reg7?love:{husband/wife}}"),
  #For trying to convince someone to support another candidate
  ("dplmc_refuse_support_s43_named_s4", "Support a {s43} like {s4}?  I think not."),
  #for political comments
  ("dplmc_comment_you_enfiefed_a_commoner_supportive",  "I understand that you have given {s51} to {s54}.  Others may find this controversial, but I believe that {s54} will be an able governor, and that {reg4?she:he} will not let you down."),
  #forms of address
  ("dplmc_sirmadame", "{sir/madame}"),
  ("dplmc_sirmadam",  "{sir/madam}"),
  ("dplmc_my_lordlady", "my {lord/lady}"),
  ("dplmc_your_highness", "your highness"),
  #expanded relation terms
  ("dplmc_grandfather", "grandfather"),
  ("dplmc_grandmother", "grandmother"),
  ("dplmc_grandson", "grandson"),
  ("dplmc_granddaughter", "granddaughter"),
  ("dplmc_half_brother", "half-brother"),#sharing a father or a mother, but not both
  ("dplmc_half_sister", "half-sister"),#sharing a father or a mother, but not both
  ("dplmc_sister_wife", "sister-wife"),#two women married to the same person
  ("dplmc_co_husband", "co-husband"),#two men married to the same person
  ("dplmc_co_spouse", "co-spouse"),#two people of different genders married to the same third person
  #not used in the relation scripts, but used elsewhere
  ("dplmc_friend", "friend"),
  ("dplmc_ally", "ally"),
  #status notifier
  ("s54_is_deceased", "{s54} is deceased."),
  ("dplmc_political_explanation_original_lord", "In this case, the fortress should go its original owner."),
  ##Utility: use these to avoid use of high-numbered string registers
 ("dplmc_s0_comma_s1",   "{!}{s0}, {s1}"),
 ("dplmc_s0_and_s1",     "{s0} and {s1}"),
 ("dplmc_s0_newline_s1", "{!}{s0}^{s1}"),
 ##diplomacy end+

 #morality objections
 ("hire_deserters", "take those scoundrels under our banner"),
 ("rotten_food", "consume those foul foodstuff and find insects with every bite we take"),
 ("repress_farmers", "repress those peasants and propagate the violence inherent in the system"),
 ("stop_cheating", "waste time playing around with 'consoles' when you can just change the damn thing under camp options"),

 #auxiliary item types
 ("dplmc_hero_wpn_slot_morningstar","Two-handed/One-handed"), #21
 ("dplmc_hero_wpn_slot_lance","Lances"), #22
 ("dplmc_hero_wpn_slot_pikes","Pikes"), #23
 ("dplmc_hero_wpn_slot_halberd","Bladed Polearms"), #23
 ("dplmc_hero_wpn_slot_no_metatype","No Preference"), #23

  ("camera_keyboard", "To watch the fight you can use direction keys to move horizontally, numpad +- to move vertically, and numpad keys to rotate."),
  ("camera_mouse", "Use the mouse or numpad to rotate the camera, direction keys to move (holding Zoom will move faster). Tilt to adjust sensitivity, numpad to rotate and move vertically."),
  ("camera_follow", "Use tilt keys or mouse wheel to follow friendly agents. Hold Ctrl while using numpad to change view angle."),

  #ai behaviour strings (probably correct)
  ("ai_bhvr_hold", "Holding"),
  ("ai_bhvr_travel_to_party", "Travelling to Party"),
  ("ai_bhvr_patrol_location", "Patrolling Point"),
  ("ai_bhvr_patrol_party", "Patrolling around Party"),
  ("ai_bhvr_track_party", "Tracking Party"),
  ("ai_bhvr_attack_party", "Attacking Party"),
  ("ai_bhvr_avoid_party", "Avoiding Party"),
  ("ai_bhvr_travel_to_point", "Travelling to Point"),
  ("ai_bhvr_negotiate_party", "Negotiate Party"),
  ("ai_bhvr_in_town", "In Town"),
  ("ai_bhvr_travel_to_ship", "Travelling to Ship"),
  ("ai_bhvr_escort_party", "Accompanying Party"),
  ("ai_bhvr_driven_by_party", "Being Driven"),

  #party template names
  ("s5_transfer", "Transfer to {s5}"),
  ("s5_reinf", "Reinforcements from {s5}"),
  ("s5_scout", "{s5} Scout"),
  ("s5_patrol", "{s5} Patrol"),

  #companion mission strings
  ("preparing_prison_break", "Preparing a prison break in {s9}"),
  ("on_loan", "On loan"),
  ("accompanying_s5", "Accompanying {s5}"),

  # ("damage_cut", "cut"),
  # ("damage_pierce", "pierce"),
  # ("damage_blunt", "blunt"),

 #utility for keys array

  ("key_0", "0"),
  ("key_1", "1"),
  ("key_2", "2"),
  ("key_3", "3"),
  ("key_4", "4"),
  ("key_5", "5"),
  ("key_6", "6"),
  ("key_7", "7"),
  ("key_8", "8"),
  ("key_9", "9"),
  ("key_a", "A"),
  ("key_b", "B"),
  ("key_c", "C"),
  ("key_d", "D"),
  ("key_e", "E"),
  ("key_f", "F"),
  ("key_g", "G"),
  ("key_h", "H"),
  ("key_i", "I"),
  ("key_j", "J"),
  ("key_k", "K"),
  ("key_l", "L"),
  ("key_m", "M"),
  ("key_n", "N"),
  ("key_o", "O"),
  ("key_p", "P"),
  ("key_q", "Q"),
  ("key_r", "R"),
  ("key_s", "S"),
  ("key_t", "T"),
  ("key_u", "U"),
  ("key_v", "V"),
  ("key_w", "W"),
  ("key_x", "X"),
  ("key_y", "Y"),
  ("key_z", "Z"),
  ("key_numpad_0", "Numpad 0"),
  ("key_numpad_1", "Numpad 1"),
  ("key_numpad_2", "Numpad 2"),
  ("key_numpad_3", "Numpad 3"),
  ("key_numpad_4", "Numpad 4"),
  ("key_numpad_5", "Numpad 5"),
  ("key_numpad_6", "Numpad 6"),
  ("key_numpad_7", "Numpad 7"),
  ("key_numpad_8", "Numpad 8"),
  ("key_numpad_9", "Numpad 9"),
  ("key_num_lock", "Num lock"),
  ("key_numpad_slash", "Numpad slash"),
  ("key_numpad_multiply", "Numpad multiply"),
  ("key_numpad_minus", "Numpad minus"),
  ("key_numpad_plus", "Numpad plus"),
  ("key_numpad_enter", "Numpad enter"),
  ("key_numpad_period", "Numpad period"),
  ("key_insert", "Insert"),
  ("key_delete", "Delete"),
  ("key_home", "Home"),
  ("key_end", "End"),
  ("key_page_up", "Page up"),
  ("key_page_down", "Page down"),
  ("key_up", "Up"),
  ("key_down", "Down"),
  ("key_left", "Left"),
  ("key_right", "Right"),
  ("key_f1", "F1"),
  ("key_f2", "F2"),
  ("key_f3", "F3"),
  ("key_f4", "F4"),
  ("key_f5", "F5"),
  ("key_f6", "F6"),
  ("key_f7", "F7"),
  ("key_f8", "F8"),
  ("key_f9", "F9"),
  ("key_f10", "F10"),
  ("key_f11", "F11"),
  ("key_f12", "F12"),
  ("key_space", "Space"),
  ("key_escape", "Escape"),
  ("key_enter", "Enter"),
  ("key_tab", "Tab"),
  ("key_back_space", "Back space"),
  ("key_open_braces", "Open braces"),
  ("key_close_braces", "Close braces"),
  ("key_comma", "Comma"),
  ("key_period", "Period"),
  ("key_slash", "Slash"),
  ("key_back_slash", "Back slash"),
  ("key_equals", "Equals"),
  ("key_minus", "Minus"),
  ("key_semicolon", "Semicolon"),
  ("key_apostrophe", "Apostrophe"),
  ("key_tilde", "Tilde"),
  ("key_caps_lock", "Caps lock"),
  ("key_left_shift", "Left shift"),
  ("key_right_shift", "Right shift"),
  ("key_left_control", "Left control"),
  ("key_right_control", "Right control"),
  ("key_left_alt", "Left alt"),
  ("key_right_alt", "Right alt"),


  ("story_parent_noble","You came into the world a {reg11?daughter:son} of declining nobility,\
 owning only the house in which they lived. However, despite your family's hardships,\
 they afforded you a good education and trained you from childhood for the rigors of aristocracy and life at court."),
  ("story_parent_merchant","You were born the {reg11?daughter:son} of travelling merchants,\
 always moving from place to place in search of a profit. Although your parents were wealthier than most\
 and educated you as well as they could, you found little opportunity to make friends on the road,\
 living mostly for the moments when you could sell something to somebody."),
  ("story_parent_guard","As a child, your family scrabbled out a meagre living from your father's wages\
 as a guardsman to the local lord. It was not an easy existence, and you were too poor to get much of an\
 education. You learned mainly how to defend yourself on the streets, with or without a weapon in hand."),
  ("story_parent_forester","You were the {reg11?daughter:son} of a family who lived off the woods,\
 doing whatever they needed to make ends meet. Hunting, woodcutting, making arrows,\
 even a spot of poaching whenever things got tight. Winter was never a good time for your family\
 as the cold took animals and people alike, but you always lived to see another dawn,\
 though your brothers and sisters might not be so fortunate."),
  ("story_parent_nomad","You were a child of the steppe, born to a tribe of wandering nomads who lived\
 in great camps throughout the arid grasslands.\
 Like the other tribesmen, your family revered horses above almost everything else, and they taught you\
 how to ride almost before you learned how to walk."),
  ("story_parent_thief","As the {reg11?daughter:son} of a thief, you had very little 'formal' education.\
 Instead you were out on the street, begging until you learned how to cut purses, cutting purses\
 until you learned how to pick locks, all the way through your childhood.\
 Still, these long years made you streetwise and sharp to the secrets of cities and shadowy backways."),
  ("story_parent_priest","A {reg11?daughter:son} that nobody wanted, you were left to the church as a baby,\
 a foundling raised by the priests and nuns to their own traditions.\
 You were only one of many other foundlings and orphans, but you nonetheless received a lot of attention\
 as well as many years of study in the church library and before the altar. They taught you many things.\
 Gradually, faith became such a part of your life that it was no different from the blood coursing through your veins."),

  ##   As a {reg11?girl:boy} growing out of childhood,\
  ("story_childhood_page","you were sent to live in the court of one of the nobles of the land.\
 There, your first lessons were in humility, as you waited upon the lords and ladies of the household.\
 But from their chess games, their gossip, even the poetry of great deeds and courtly love, you quickly began to learn about the adult world of conflict\
 and competition. You also learned from the rough games of the other children, who battered at each other with sticks in imitation of their elders' swords."),
  ("story_childhood_apprentice","you apprenticed with a local craftsman to learn a trade. After years of hard work and study under your\
 new master, he promoted you to journeyman and employed you as a fully paid craftsman for as long as\
 you wished to stay."),
  ("story_childhood_urchin","you took to the streets, doing whatever you must to survive.\
 Begging, thieving and working for gangs to earn your bread, you lived from day to day in this violent world,\
 always one step ahead of the law and those who wished you ill."),
 ("story_childhood_nomad","you rode the great steppes on a horse of your own, learning the ways of the grass and the desert.\
 Although you sometimes went hungry, you became a skillful hunter and pathfinder in this trackless country.\
 Your body too started to harden with muscle as you grew into the life of a nomad {reg11?woman:man}."),
  ("story_childhood_stockboy","you apprenticed to a wealthy merchant, picking up the trade over years of working shops and driving caravans.\
 You soon became adept at the art of buying low, selling high, and leaving the customer thinking they'd\
 got the better deal."),
  ("story_childhood_mummer","you attached yourself to a troupe of wandering entertainers, going from town to town setting up mummer's\
 shows. It was a life of hard work, selling, begging and stealing your living from the punters who flocked\
 to watch your antics. Over time you became a performer well capable of attracting a crowd."),
  ("story_childhood_courtier","you spent much of your life at court, inserting yourself into the tightly-knit circles of nobility.\
 With the years you became more and more involved with the politics and intrigue demanded of a high-born {reg11?woman:man}.\
 You could not afford to remain a stranger to backstabbing and political violence, even if you wanted to."),
  ("story_childhood_noble","{reg11?you were trained and educated to the duties of a noble woman. You learned much about the household arts,\
 but even more about diplomacy and decorum, and all the things that a future husband might choose to speak of.\
 Truly, you became every inch as shrewd as any lord, though it would be rude to admit it aloud:you were trained and educated to perform the duties and wield the rights of a noble landowner.\
 The managing of taxes and rents were equally important in your education as diplomacy and even\
 personal defence. You learned everything you needed to become a lord of your own hall}."),
  ("story_childhood_acolyte","you became an acolyte in the church, the lowest rank on the way to priesthood.\
 Years of rigorous learning and hard work followed. You were one of several acolytes,\
 performing most of the menial labour in the church in addition to being trained for more holy tasks.\
 On the night of your adulthood you were allowed to conduct your first service.\
 After that you were no longer an acolyte {reg11?girl:boy}, but a {reg11?girl:boy} waiting to take your vows into the service of God."),


##  Though the distinction felt sudden to you, somewhere along the way you had become a {reg11?woman:man}, and the whole world seemed to change around you.\
  ("story_job_bravo","You left your old life behind to travel the roads as a mercenary, a bravo, guarding caravans for coppers\
 or bashing in heads for silvers. You became a {reg11?daughter:man} of the open road, working with bandits as often as against.\
 Going from fight to fight, you grew experienced at battle, and you learned what it was to kill."),
  ("story_job_merc","You signed on with a mercenary company and travelled far from your home. The life you found was rough and\
 ready, marching to the beat of strange drums and learning unusual ways of fighting.\
 There were men who taught you how to wield any weapon you desired, and plenty of battles to hone your skills.\
 You were one of the charmed few who survived through every campaign in which you marched."),
("story_job_poacher","Dissatisfied with common men's desperate scrabble for coin, you took to your local lord's own forests\
 and decided to help yourself to its bounty, laws be damned. You hunted stags, boars and geese and sold\
 the precious meat under the table. You cut down trees right under the watchmen's noses and turned them into\
 firewood that warmed many freezing homes during winter. All for a few silvers, of course."),
("story_job_craftsman","You pursued a career as a smith, crafting items of function and beauty out of simple metal.\
 As time wore on you became a master of your trade, and fine work started to fetch fine prices.\
 With food in your belly and logs on your fire, you could take pride in your work and your growing reputation."),
  ("story_job_peddler","Heeding the call of the open road, you travelled from village to village buying and selling what you could.\
 It was not a rich existence, but you became a master at haggling even the most miserly elders into\
 giving you a good price. Soon, you knew, you would be well-placed to start your own trading empire..."),
  ("story_job_preacher","You packed your few belongings and went out into the world to spread the word of God. You preached to\
 anyone who would listen, and impressed many with the passion of your sermons. Though you had taken a vow\
 to remain in poverty through your itinerant years, you never lacked for food, drink or shelter; the\
 hospitality of the peasantry was always generous to a rising {reg11?woman:man} of God."),
("story_job_troubadour","You set out on your own with nothing except the instrument slung over your back and your own voice.\
 It was a poor existence, with many a hungry night when people failed to appreciate your play,\
 but you managed to survive on your music alone. As the years went by you became adept at playing the\
 drunken crowds in your taverns, and even better at talking anyone out of anything you wanted."),
  ("story_job_squire", "When you were named a retainer to a noble at court, you practiced long hours with weapons,\
 learning how to deal out hard knocks and how to take them, too.\
 You were instructed in your obligations to your lord, and of your duties to those who might one day be your vassals.\
 But in addition to learning the chivalric ideal, you also learned about the less uplifting side\
 -- old warriors' stories of ruthless power politics, of betrayals and usurpations,\
 of men who used guile as well as valor to achieve their aims."),
  ("story_job_lady","You joined the tightly-knit circle of women at court, ladies who all did proper ladylike things,\
 the wives and mistresses of noble men as well as maidens who had yet to find a husband.\
 However, even here you found politics at work as the ladies schemed for prominence and fought each other\
 bitterly to catch the eye of whatever unmarried man was in fashion at court.\
 You soon learned ways of turning these situations and goings-on to your advantage. With it came the\
 realisation that you yourself could wield great influence in the world, if only you applied yourself\
 with a little bit of subtlety."),
 ("story_job_student","You found yourself as a student in the university of one of the great cities,\
 where you studied theology, philosophy, and medicine.\
 But not all your lessons were learned in the lecture halls.\
 You may or may not have joined in with your fellows as they roamed the alleys in search of wine, women, and a good fight.\
 However, you certainly were able to observe how a broken jaw is set,\
 or how an angry townsman can be persuaded to set down his club and accept cash compensation for the destruction of his shop."),

   ##^Only you know exactly what caused you to give up your old life and become an adventurer.\
  ("story_reason_revenge","Still, it was not a difficult choice to leave, with the rage burning brightly in your heart.\
 You want vengeance. You want justice. What was done to you cannot be undone,\
 and these debts can only be paid in blood..."),
  ("story_reason_death","All you can say is that you couldn't bear to stay, not with the memories of those you loved so close and so\
 painful. Perhaps your new life will let you forget,\
 or honour the name that you can no longer bear to speak..."),
  ("story_reason_wanderlust","You're not even sure when your home became a prison, when the familiar became mundane, but your dreams of\
 wandering have taken over your life. Whether you yearn for some faraway place or merely for the open road and the\
 freedom to travel, you could no longer bear to stay in the same place. You simply went and never looked back..."),
  ("story_reason_fervor","Regardless, the intense faith burning in your soul would not let you find peace in any single place.\
 There were others in the world, souls to be washed in the light of God. Now you preach wherever you go,\
 seeking to bring salvation and revelation to the masses, be they faithful or pagan. They will all know the\
 glory of God by the time you're done..."),
  ("story_reason_disown","However, you know you cannot go back. There's nothing to go back to. Whatever home you may have had is gone\
 now, and you must face the fact that you're out in the wide wild world. Alone to sink or swim..."),
  ("story_reason_greed","To everyone else, it's clear that you're now motivated solely by personal gain.\
 You want to be rich, powerful, respected, feared.\
 You want to be the one whom others hurry to obey.\
 You want people to know your name, and tremble whenever it is spoken.\
 You want everything, and you won't let anyone stop you from having it..."),

  ("story_all", "{s10}^^You started to learn about the world almost as soon as you could walk and talk. As a {reg11?girl:boy} growing out of childhood, {s11}^^\
Though the distinction felt sudden to you, somewhere along the way you had become a {reg11?woman:man}, and the whole world seemed to change around you. {s12}^^\
Only you know exactly what caused you to give up your old life and become an adventurer. {s13}"),
  ("continue_dot", "Continue..."),
  ("chest_info", "Go near the chest and hold down the right mouse button for a while, then you can deposit or withdraw money from the chest. If you also have a chamberlain, you can access your treasury."),
#keep these string order relatively the same, because we're storing randomly within the range
#mercenary hiring, reg65 = gender, s0 = sir/madam, reg1 = plural/singular
  ("mercenary_intro_1", "You chose well, {s0}. {reg1?My {reg65?companions:lads}:I} know how to keep {reg1?their:my} word and earn {reg1?their:my} pay."),
  ("mercenary_intro_2", "Well done, {s0}. Keep the money and wine coming {reg1?my:our} way, and there's no foe in the world you need fear."),
  ("mercenary_intro_3", "{reg1?We are:I am} at your service, {s0}. Point {reg1?us:me} in the direction of those who need hurting, and {reg1?we:I}'ll do the rest."),
  ("mercenary_intro_4", "You will not be disappointed {s0}. You will not find {reg1?better warriors:a better fighter} in all the land."),
#bandit
  ("bandit_intro_1", "I can smell a fat purse a mile away. Methinks yours could do with some lightening, eh?"),
  ("bandit_intro_2", "Why, it be another traveller, chance met upon the road! I should warn you, country here's a mite dangerous for a good {fellow/woman} like you. But for a small donation my boys and I'll make sure you get rightways to your destination, eh?"),
  ("bandit_intro_3", "Well well, look at this! You'd best start coughing up some silver, friend, or me and my boys'll have to break you."),
  ("bandit_intro_4", "There's a toll for passin' through this land, payable to us, so if you don't mind we'll just be collectin' our due from your purse..."),
  ("bandit_outro_1", "Another fool come to throw {him/her}self on my weapon, eh? Fine, let's fight!"),
  ("bandit_outro_2", "We're not afraid of you, {sirrah/wench}. Time to bust some heads!"),
  ("bandit_outro_3", "That was a mistake. Now I'm going to have to make your death long and painful."),
  ("bandit_outro_4", "Brave words. Let's see you back them up with deeds, cur!"),
  ("bandit_outro_5", "I hope you die in a hole."),

#presentation names
  ("name_presentation_text", "What will be the name of {s1}?"),
  ("default_kingdom", "your realm"),
  ("default_town", "the capital"),
  ("default_party", "the party"),
  ("default_troop", "this companion"),
#training opponent descriptions
  ("tier_reg", "Good for you {lad/lass}. With this victory, you have advanced to the next training level. From now on your opponents will be regular fighters, not the riff-raff off the street, so be on your toes."),
  ("tier_vet", "Way to go {lad/lass}. Welcome to the third training level. From now on your opponents will be veteran fighters; soldiers and arena regulars and the like. These guys know some dirty tricks, so keep your defense up."),
  ("tier_champ", "You've got the heart of a champion, {lad/lass}, and the sword arm to match. From now on your opponents will be champion fighters. These are the cream of the crop, the finest warriors I have trained. If you can best three of them in a row, you will join their ranks."), # and they might join yours in return
  #("tier_finish", "It does my heart good to see such a promising talent. You have passed all tiers of training. You can now tell everyone that you have been trained by the master of the training field. If you have any recruits that need a lesson, don't hesitate to see me."),
#training ground strings
  ("ctm_melee", "Your opponent{reg0?s are: is} ready for the fight."),
  ("ctm_ranged", "Stay behind the line on the ground and shoot the targets. Try not to waste any shots."),
  ("ctm_mounted", "Try to destroy as many targets as you can. You have two and a half minutes to clear the track."),
#utility from CC for item modifiers
  ("imod_plain", "{!}"),
  ("imod_cracked", "Cracked "),
  ("imod_rusty", "Rusty "),
  ("imod_bent", "Bent "),
  ("imod_chipped", "Chipped "),
  ("imod_battered", "Battered "),
  ("imod_poor", "Poor "),
  ("imod_crude", "Crude "),
  ("imod_old", "Old "),
  ("imod_cheap", "Cheap "),
  ("imod_fine", "Fine "),
  ("imod_well_made", "Well Made "),
  ("imod_sharp", "Sharp "),
  ("imod_balanced", "Balanced "),
  ("imod_tempered", "Tempered "),
  ("imod_deadly", "Deadly "),
  ("imod_exquisite", "Exquisite "),
  ("imod_masterwork", "Masterwork "),
  ("imod_heavy", "Heavy "),
  ("imod_strong", "Strong "),
  ("imod_powerful", "Powerful "),
  ("imod_tattered", "Tattered "),
  ("imod_ragged", "Ragged "),
  ("imod_rough", "Rough "),
  ("imod_sturdy", "Sturdy "),
  ("imod_thick", "Thick "),
  ("imod_hardened", "Hardened "),
  ("imod_reinforced", "Reinforced "),
  ("imod_superb", "Superb "),
  ("imod_lordly", "Lordly "),
  ("imod_lame", "Lame "),
  ("imod_swaybacked", "Swaybacked "),
  ("imod_stubborn", "Stubborn "),
  ("imod_timid", "Timid "),
  ("imod_meek", "Meek "),
  ("imod_spirited", "Spirited "),
  ("imod_champion", "Champion "),
  ("imod_fresh", "Fresh "),
  ("imod_day_old", "Day Old "),
  ("imod_two_day_old", "Two Day Old "),
  ("imod_smelling", "Smelling "),
  ("imod_rotten", "Rotten "),
  ("imod_large_bag", "Large Bag "),

  #lowercase descriptions for disguises
  ("pilgrim_disguise", "pilgrim"),
  ("farmer_disguise", "farmer"),
  ("hunter_disguise", "hunter"),
  ("guard_disguise", "guard"),
  ("merchant_disguise", "merchant"),
  ("bard_disguise", "bard"),

  #recolor presentation strings
  ("html", "HTML Code: {s0}"),
  ("html_color", "{!}#{s11}{s12}{s13}{s14}{s15}{s16}"),
  ("color_of", "Color of {s0}:"),
  # ("color_kingdom", "your realm"),
  ("color_banner", "the back of your banner"),
  ("color_group", "the {s0} group on the minimap"),

  #update settings
  ("setting_of", "Current Setting: {s1}"),

  #SB : new strings from Invasion, moved down here to keep slot compatibility
  ("multi_scene_25", "Cold Coast"),
  # ("multi_game_type_9", "Invasion"),

  ("s1_team", "{s1} squad"),
  # ("warning_max_players_count_caption", "{!}NOT USED"),
  # ("warning_max_players_count_text", "{!}The recommended number of players for this mode is 16 players"),
  # ("warning_max_players_count_text2", "The recommended number of players for this mode is 16 players"),
  # ("command_info_text", "{!}Squad size: {reg1}, cost: {reg2}"),

  # ("morale_reason_faction_conflict", "{!}NOT USED"),
  # ("morale_reason_faction_common", "{!}NOT USED"),
  # ("multi_disable_granades", "Disable grenades"),
  # ("squad_size_s0", "Squad size: {s0}"),

  ("mp_add_troop", "Companions"),
  # ("mp_squad", "Squad"),
  # ("mp_squad_req_size_reg0", "Requested: {reg0}"),
  # ("mp_squad_active_size_reg0", "Active: {reg0}"),
  # ("squad_cost_reg0", "Squad cost: {reg0}"),
  # ("item_cost_reg0", "Item cost: {reg0}"),
  ("next_wave_in_reg0_mins", "Next wave in {reg0} mins..."),
  ("wave_info", "WAVE INFO"),
  ("wave_no_reg1", "Wave No: {reg1}"),
  ("veteran_wave_no_reg1", "Veteran Wave No: {reg1}"),
  ("elite_wave_no_reg1", "Elite Wave No: {reg1}"),
  ("time_left_reg2_mins_reg1_secs", "Time Left: {reg2} minutes and {reg1} seconds"),
  ("time_left_reg1_secs", "Time Left: {reg1} seconds"),
  ("enemies_reg1_total_reg2_arriving", "Enemies: {reg1} Alive, {reg2} Arriving"),
  ("ccoop_enemy_info", "   {reg4} {s0} ({reg3} arriving)"),

  #Suvorov add 01/06/2011
  # ("oim_black_hetman_failed", "You no longer control the capital, there is no chance of victory. All is lost!"),

  # ("squad_size_for_captains", "Squad size for captains:"),
  # ("captain_merc_ratio", "Captain / Mercenary ratio:"),
  # ("1_div", "1 / "),
  # ("zero", "{!}0"),
  # ("accompany", "Accompany"),

  # ("reg2_s1_s2_s2", "{reg2?{s1}, {s2}:{s2}}"),
  # ("reg2_s1_and_s2_s2", "{reg2?{s1} and {s2}:{s2}}"),
  # ("give_the_money_you_took_from_s9_to_s10", "Give the money you took from {s9} to {s10}."),

  # ("man", "man"),
  # ("men", "men"),

  # ("you_have_taken_all_infantry", "Haha! {Sir/Madam}, you've taken all my infantry already. Will there be anything else?"),
  # ("you_have_taken_all_musketeer", "Haha! {Sir/Madam}, you've taken all my musketeer already. Will there be anything else?"),
  # ("you_have_taken_all_cavalry", "Haha! {Sir/Madam}, you've taken all my cavalry already. Will there be anything else?"),

  # ("price_there_known", "{s1}, ({s2} is {reg1} thalers there)"),
  # ("price_there_unknown", "{s1}"),
  # ("s1_reg0_s2", "{!}{s1}, {reg0} {s2}"),
  # ("s3_reg0_s2", "{!}{s3} {reg0} {s2}"),
  # ("s1_s2", "{!}{s1} {s2}"),
  # ("your_troops_are_dying_because_of_illness", "Your troops are dying because of a disease!"),
  # ("has_died_because_of_illness", "has died of {s4}."),
  # ("have_died_because_of_illness", "have died of {s4}."),


  ("ccoop_wave_reg1_is_coming_in_reg0_seconds", "Wave {reg1} is coming in {reg0} seconds"),
  ("ccoop_veteran_wave_reg1_is_coming_in_reg0_seconds", "Veteran wave {reg1} is coming in {reg0} seconds"),
  ("ccoop_elite_wave_reg1_is_coming_in_reg0_seconds", "Elite wave {reg1} (Tier {reg2}) is coming in {reg0} seconds"),
  #("ccoop_next_wave_in_reg0_seconds_times_up", "Time is up, next wave is {reg2}. {reg1} new troops are coming in {reg0} seconds"),
  #("ccoop_next_wave_in_reg0_seconds_first_wave", "Enemy troops are coming in {reg0} seconds"),
  ("prison_cart_hint", "Destroy the prisoner cart or pass the round to rescue fallen comrades."),

  #Berk:
  ("wave_reg1", "Wave {reg1}"),
  ("veteran_wave_hint", "Beware: Veterans have increased numbers and health!"), #SB: veteran waves aren't used
  ("elite_wave_hint", "Beware: Elites have increased health and deliver more damage!"),
  ("ask_for_help_to_respawn_hint", "You'll respawn once your comrades destroy the prisoner cart or pass the current round."),
  ("wait_for_next_turn_to_respawn_hint", "You will respawn in the next round."),

  # ("mp_cbf_squad_auto_ratio", "Auto-balance captain squad ratio"),

  ("default", "Default"),

  #settings
  ("dplmc_setting_2", "High"),
  ("dplmc_setting_1", "Medium"),
  ("dplmc_setting_0", "Low"),
  ("dplmc_setting_off", "Disabled"),
  ("dplmc_setting_on", "Enabled"),
  ("dplmc_setting_freq", "Frequent"),
  ("dplmc_setting_tt0", "Mouse-over options for further information. More detailed description of mechanics can be found in the game concepts information pages."),
  ("dplmc_setting_tt1", "This option makes every horse in battle lose movement speed directly proportional to their lost Health Points."),
  ("dplmc_setting_tt1a", "This option causes riderless horses in battle to start running away after 1 minute and being culled 30 seconds later. The default tic rate is 10 seconds, and a rate of 0 means culling is disabled. Riding a horse will reset its timer and other horses within 5 meters of the player will not be subject to culling."),
  ("dplmc_setting_tt2", "This option let your troops continue fighting should you fall in battle."),
  ("dplmc_setting_tt2a", "This option orders all your troops to use any weapons, fire at will, and charge once you fall in battle."),
  ("dplmc_setting_tt3", "This option gives advantage in autocalculated battles to those units who are better in the current terrain.^Horsemen are bad in forest terrain, while archers are better."),
  ("dplmc_setting_tt4", "This option lets exiled lords return in order to serve a new liege and form warbands without a home center."),
  ("dplmc_setting_tt5", "This option lets you decide the AI strength level. The higher this level is, the better the AI. High level is experimental and may brings some bugs to your game."),
  ("dplmc_setting_tt6", "This option changes the economical and behavior values to be more realistic. High level is experimental and may brings some bugs to your game."),
  ("dplmc_setting_tt7", "This option lets you decide the level of sexism in the game."),
  ("dplmc_setting_tt8", "This option toggles whether companions suffer from incompatible moralities and grievance penalties."),
  ("dplmc_setting_tt9", "This option enables a more complex disguise system while entering hostile centers."),
  ("dplmc_setting_tt10", "This option enables various cheat menus and debug features."),
  # ("dplmc_setting_tt10", "This option toggles the camera modes."),

  #yet to be determined <-known to be {s4} -> here
  #we're not sure which could <- the town of {s4} is believed to -> we think ourselves to

  ("mayor_wealth_compare", "Here in {s3}, we {s4} than {reg4} towns{reg6?, and {s5} than {reg5}:}."),
  ("mayor_wealth_no_data", "All things considered, we are on par with all others towns."),
  ("mayor_wealth_rank_1", "yet to be reckoned"),
  ("mayor_wealth_rank_2", "known to be {s2}"),
  ("mayor_wealth_rank_3", "here"),
  ("mayor_wealth_rank_4", "we're not sure which could"),
  ("mayor_wealth_rank_5", "the town of {s2} is believed to"),
  ("mayor_wealth_rank_6", "we think ourselves to"),
  ("mayor_wealth_compare_less_1", "are poorer"),
  ("mayor_wealth_compare_less_2", "produce less"),
  ("mayor_wealth_compare_less_3", "have villages in the hinterlands producing less"), #rephrased to follow "we"
  ("mayor_wealth_compare_less_4", "are less visited"),
  ("mayor_wealth_compare_less_5", "are less afflicted by bandits"), #split up
  ("mayor_wealth_compare_more_1", "are richer"),
  ("mayor_wealth_compare_more_2", "produce more"),
  ("mayor_wealth_compare_more_3", "have villagers producing more"),
  ("mayor_wealth_compare_more_4", "are more visited"),
  ("mayor_wealth_compare_more_5", "are more afflicted by raiders"),

  ("mayor_wealth_comparison_1", "Overall, the wealthiest town is {s2}. {s1}"),
  ("mayor_wealth_comparison_2", "In terms of local industry, the most productive town is {s2}. {s1}\
 Production is of course affected by the supply of raw materials, as well as by the overall prosperity of the town."),
  ("mayor_wealth_comparison_3", "In terms of the output of the surrounding villages, {s2} be the richest in the world. {s1}\
 The wealth of a town's hinterland, of course, is heavily dependent on the tides of war. Looting and pillage, and shifts in territory, can make a major impact."),
  ("mayor_wealth_comparison_4", "In terms of trade, {s2} have received the most visits from caravans over the past few months. {s1}"),
  ("mayor_wealth_comparison_5", "In terms of attacks on travellers, {s2} be the most dangerous. {s1}"),

  ("npc_mission_delegate_quest", "Questing on your behalf"), #generic description "on an errand"
  #these are 3rd-person descriptions of objectives {x} for {y} since string registers are not always known
  ("dplmc_npc_qst_deliver_message", "Deliver a peaceful message"),
  ("dplmc_npc_qst_deliver_message_to_enemy_lord", "Dispatch a military message"),
  ("dplmc_npc_qst_raise_troops", "Raise some troops"),
  ("dplmc_npc_qst_escort_lady", "Escort a lady"),
  ("dplmc_npc_qst_deal_with_bandits_at_lords_village", "Save a village"),
  ("dplmc_npc_qst_collect_taxes", "Collect some taxes"),
  ("dplmc_npc_qst_hunt_down_fugitive", "Hunt down a fugitive"),
  ("dplmc_npc_qst_kill_local_merchant", "Rough up a merchant"),
  ("dplmc_npc_qst_bring_back_runaway_serfs", "Bring back serfs"),
  ("dplmc_npc_qst_follow_spy", "Follow a spy's meeting"),
  ("dplmc_npc_qst_capture_enemy_hero", "Hold a lord hostage"),
  ("dplmc_npc_qst_lend_companion", "Lend a companion"),
  ("dplmc_npc_qst_collect_debt", "Collect someone's debt"),
  ("dplmc_npc_qst_incriminate_loyal_commander", "Incriminate a commander"),
  ("dplmc_npc_qst_meet_spy_in_enemy_town", "Receive a spy's report"),
  #most of these shouldn't be enabled
  ("dplmc_npc_qst_capture_prisoners", "Capture some prisoners"),
  ("dplmc_npc_qst_lend_surgeon", "16"),
  ("dplmc_npc_qst_follow_army", "17"),
  ("dplmc_npc_qst_report_to_army", "18"),
  ("dplmc_npc_qst_deliver_cattle_to_army", "19"), #army_quests_begin
  ("dplmc_npc_qst_join_siege_with_army", "20"),
  ("dplmc_npc_qst_screen_army", "21"),
  ("dplmc_npc_qst_scout_waypoints", "22"),
  ("dplmc_npc_qst_rescue_lord_by_replace", "23"), #lady_quests_begin
  ("dplmc_npc_qst_deliver_message_to_prisoner_lord", "Deliver a secret message"),
  ("dplmc_npc_qst_duel_for_lady", "Challenge a lord"),
  ("dplmc_npc_qst_duel_courtship_rival", "Duel a lord"),
  ("dplmc_npc_qst_duel_avenge_insult", "Call out a lord"),
  ("dplmc_npc_qst_move_cattle_herd", "Drive some cattle"), #mayor_quests_begin
  ("dplmc_npc_qst_escort_merchant_caravan", "Escort caravan"),
  ("dplmc_npc_qst_deliver_wine", "Deliver merchandise"),
  ("dplmc_npc_qst_troublesome_bandits", "Hunt down bandits"),
  ("dplmc_npc_qst_kidnapped_girl", "Ransom a girl"),
  ("dplmc_npc_qst_persuade_lords_to_make_peace", "Make peace"),
  ("dplmc_npc_qst_deal_with_looters", "Deal with looters"),
  ("dplmc_npc_qst_deal_with_night_bandits", "Drive out bandits"),
  ("dplmc_npc_qst_deliver_grain", "Gather supplies"),
  ("dplmc_npc_qst_deliver_cattle", "Deliver cattle"),
  ("dplmc_npc_qst_train_peasants_against_bandits", "Train peasants"),
  #TODO add bonus description for various starting background
  #some strings for companion personality
  ("dplmc_reputation_roguish", "It is whispered that {s46} lives life to the full."),
  ("dplmc_reputation_benefactor", "It is widely known that {s46} is a friend of the commoners."),
  ("dplmc_reputation_custodian", "It is believed that {s46} is a wise investor."),

  ("s5_over_s14", "{s21}^* The {s5} is the overlord of {s14}.{s18} It will degrade into an alliance in {reg1} days."),
  ("s14_over_s5", "{s21}^* The {s5} is a tributary vassal of {s14}.{s18} It will degrade into an alliance in {reg1} days."),
  ("tributary_attack", "They are our tributary state. If you attack them you violate the treaty."),

  # Object Titles
  ("mcc_label_done", "Done"),
  ("mcc_label_back", "Back"),
  ("mcc_label_default", "Default"),
  ("mcc_label_random", "Randomize"),
  ("mcc_label_menus", "Character Background"),
  ("mcc_label_story", "Your Story"),
  ("mcc_label_gender", "Your gender:"),
  ("mcc_label_father", "Your father was:"),
  ("mcc_label_earlylife", "You spent your early life as:"),
  ("mcc_label_later", "Later you became:"),
  ("mcc_label_reason", "The reason for an adventure:"),
  ("mcc_label_gameplay_options", "Game Options"),
  # ("mcc_label_fog_of_war", "Fog of War"),
  # ("mcc_label_mtt", "Troop Tree"),
  # ("mcc_label_gather_npcs", "Gather Companions"),
  ("mcc_label_region", "Starting Region"),
  ("mcc_empty", "{s31}"),
  ("mcc_str", "STR"),
  ("mcc_agi", "AGI"),
  ("mcc_int", "INT"),
  ("mcc_cha", "CHA"),
  ("mcc_zero", "0"),
  ("mcc_skl_ironflesh", "Ironflesh"),
  ("mcc_skl_powerstrike", "Power Strike"),
  ("mcc_skl_powerthrow", "Power Throw"),
  ("mcc_skl_powerdraw", "Power Draw"),
  ("mcc_skl_weaponmaster", "Weapon Master"),
  ("mcc_skl_shield", "Shield"),
  ("mcc_skl_athletics", "Athletics"),
  ("mcc_skl_riding", "Riding"),
  ("mcc_skl_horsearchery", "Horse Archery"),
  ("mcc_skl_looting", "Looting"),
  # ("mcc_skl_foraging", "Foraging"),
  ("mcc_skl_trainer", "Trainer"),
  ("mcc_skl_tracking", "Tracking"),
  ("mcc_skl_tactics", "Tactics"),
  ("mcc_skl_pathfinding", "Path-finding"),
  ("mcc_skl_spotting", "Spotting"),
  ("mcc_skl_inventorymanagement", "Inventory Mgmt."),
  ("mcc_skl_woundtreatment", "Wound Treatment"),
  ("mcc_skl_surgery", "Surgery"),
  ("mcc_skl_firstaid", "First Aid"),
  ("mcc_skl_engineer", "Engineer"),
  ("mcc_skl_persuasion", "Persuasion"),
  ("mcc_skl_prisonermanagement", "Prisoner Mgmt."),
  ("mcc_skl_leadership", "Leadership"),
  ("mcc_skl_trade", "Trade"),

  #Formations and AI
    ("tactical_controls", "Use the keyboard NUMBERS to select a division. Press 0 to select your entire force.^^\
Use F1-F4 to order selected divisions. Keep the F1 key down to place selected divisions. One may target an enemy division through this mechanism.^^\
Pressing the ENTER key often initiates an overhead Strategy Camera.^^\
Pressing the BACKSPACE key often initiates a Battle Command Display with 'radar.'"),
  ("division_placement", "When ONE division is selected, the center of its front rank is placed at the spot indicated.^^\
When MANY divisions are selected, they are separated and spread out as if the player were standing at the spot indicated.^^\
One may memorize the placement of selected divisions relative to the player by pressing F2, F7. Default is infantry to the left, cavalry right, and ranged forward."),
  ("formations", "The Complex Formations on the Battle Menu are:^^\
- RANKS with best troops up front^\
- SHIELD WALL, ranks with shields in front and longer weapons in back^\
- WEDGE with best troops up front^\
- SQUARE in no particular order^\
- NO FORMATION^^\
Even in the last case, the player can make formations up to four lines by ordering Stand Closer enough times."),


  #Titles given for players/lords in the Roman Empire
  #Patrician
  #Vir Illustris
  #Vir Spectabilis
  #Vir Clarissimus

  #Vir Clarissimus - Spectabilis - Illustris - able to be granted rank of Magister Officum after player reaches title

  #Military Positions in the Roman Empire


  ("com_chalcedonian_christian", "{s1}^^Religion: Chalcedonian Christianity"),
  ("com_arian_christian", "{s1}^^Religion: Arian Christianity"),
  ("com_miaphysite_christian", "{s1}^^Religion: Miaphysite Christianity"),
  ("com_nestorian_christian", "{s1}^^Religion: Nestorian Christianity"),
  ("com_donatist_christian", "{s1}^^Religion: Donatist Christianity"),
  ("com_pagan", "{s1}^^Religion: Pagan"),
  ("com_roman_paganism", "{s1}^^Religion: Roman Paganism"),
  ("com_zoroastrianism", "{s1}^^Religion: Mazdaist Zoroastrianism"),
  ("com_zurvanism", "{s1}^^Religion: Zurvanite Zoroastrianism"),
  ("com_judaism", "{s1}^^Religion: Judaism"),

  ("monastery_night", "It is night, and the clergy is asleep. Return in the morning."),

  ("king_campaign_start", "Start your campaign as king..."),
  ("lord_campaign_start", "Start your campaign as a vassal..."),

  ("faction_troop_tree", "Troop Trees"),

  #Who's in the hall?
  ("s22_and_s19", "{s22} and {s19}"),
  ("s22_coma_s19", "{s22}, {s19}"),
  ("s23_and_s20", "{s23} and {s20}"),
  ("s23_coma_s20", "{s23}, {s20}"),
  ("s24_and_s21", "{s24} and {s21}"),
  ("s24_coma_s21", "{s24}, {s21}"),
  ("s17_and_s67", "{s17} and {s67}"),
  ("s17_coma_s67", "{s17}, {s67}"),
  ("nobles_at_hall", "{reg0?Nobles at hall {reg0}.{reg1? Commanders {reg1} ({s67}).:} {reg2?Ladies {reg2} ({s19}).:}:}{reg4? pretenders to the throne {reg4} ({s21}).:} {reg3?Heroes in the tavern {reg3} ({s20}).:}"),

#MODEL STRINGS
  ("roman_focale_1","roman_focale_red"),
  ("roman_focale_2","roman_focale_white"),
  ("roman_focale_3","roman_focale_blue"),
  ("roman_focale_4","roman_focale_green"),
  ("roman_focale_5","roman_focale_brown"),
  ("roman_focale_6","roman_focale_yellow"),
  ("roman_focale_end","roman_focale_white"),

#new roman accessories by fabio
  ("accessories_capsa","accessories_capsa"),
  ("accessories_satchel","accessories_satchel"),
  ("accessories_pouch","accessories_pouch"),
  ("accessories_canteen","accessories_canteen"),
  ("accessories_end","accessories_pouch"),

  #pictish accessories
  ("pictish_backpack","pictish_backpack"),
  ("pictish_satchel", "pictish_satchel"),
  ("pictish_horn",    "pictish_horn"),
  ("pictish_chain",   "pictish_chain"),
  ("pictish_end",   "pictish_backpack"),

  #germanic dresses
  ("germanic_f_clothes_germanic_brooch","germanic_f_clothes_germanic_brooch"),
  ("germanic_f_clothes_celtic_brooch","germanic_f_clothes_celtic_brooch"),
  ("germanic_f_clothes_berber_brooch","germanic_f_clothes_berber_brooch"),
  ("germanic_f_clothes_brooch_end","germanic_f_clothes_germanic_brooch"),

  ("germanic_f_cloak_brooch_1","germanic_f_cloak_brooch_1"),
  ("germanic_f_cloak_brooch_2","germanic_f_cloak_brooch_1"),
  ("germanic_f_cloak_brooch_end","germanic_f_cloak_brooch_1"),


#new cloaks by asher
  #a - to be used by thorsburg tunic
  #b - to be used by others

  ("TOAOE_cloak_1a","TOAOE_cloak_1a"),#brown
  ("TOAOE_cloak_2a","TOAOE_cloak_2a"),#brown
  ("TOAOE_cloak_3a","TOAOE_cloak_3a"),#brown
  ("TOAOE_cloak_4a","TOAOE_cloak_4a"),#brown
  ("TOAOE_cloak_5a","TOAOE_cloak_5a"),#red/roman
  ("TOAOE_cloak_6a","TOAOE_cloak_6a"),#red/roman
  ("TOAOE_cloak_7a","TOAOE_cloak_7a"),#yellow w/ red stripe (roman)
  ("TOAOE_cloak_8a","TOAOE_cloak_8a"),#yellow w/ decorations (roman)
  ("TOAOE_cloak_9a","TOAOE_cloak_9a"),#brown with decorations (roman)
  ("TOAOE_cloak_10a","TOAOE_cloak_10a"),#decorated (roman)
  ("TOAOE_cloak_11a","TOAOE_cloak_11a"),#decorated (roman)
  ("TOAOE_cloak_12a","TOAOE_cloak_12a"),#germanic (brown)
  ("TOAOE_cloak_13a","TOAOE_cloak_13a"),#germanic (red/orange)
  ("TOAOE_cloak_14a","TOAOE_cloak_14a"),#germanic (red w/ stripes)
  ("TOAOE_cloak_15a","TOAOE_cloak_15a"),#germanic (red w/ stripes)

  ("TOAOE_cloak_1b","TOAOE_cloak_1b"),#brown
  ("TOAOE_cloak_2b","TOAOE_cloak_2b"),#brown
  ("TOAOE_cloak_3b","TOAOE_cloak_3b"),#brown
  ("TOAOE_cloak_4b","TOAOE_cloak_4b"),#brown
  ("TOAOE_cloak_5b","TOAOE_cloak_5b"),#red/roman
  ("TOAOE_cloak_6b","TOAOE_cloak_6b"),#red/roman
  ("TOAOE_cloak_7b","TOAOE_cloak_7b"),#yellow w/ red stripe (roman)
  ("TOAOE_cloak_8b","TOAOE_cloak_8b"),#yellow w/ decorations (roman)
  ("TOAOE_cloak_9b","TOAOE_cloak_9b"),#brown with decorations (roman)
  ("TOAOE_cloak_10b","TOAOE_cloak_10b"),#decorated (roman)
  ("TOAOE_cloak_11b","TOAOE_cloak_11b"),#decorated (roman)
  ("TOAOE_cloak_12b","TOAOE_cloak_12b"),#germanic (brown)
  ("TOAOE_cloak_13b","TOAOE_cloak_13b"),#germanic (red/orange)
  ("TOAOE_cloak_14b","TOAOE_cloak_14b"),#germanic (red w/ stripes)
  ("TOAOE_cloak_15b","TOAOE_cloak_15b"),#germanic (red w/ stripes)
#TEXTURE STRINGS

#ROUND SHIELDS + CONCAVE SHIELDS - NEW
  ("round_shields_leather_1","round_shields_leather_1"),
  ("round_shields_leather_2","round_shields_leather_2"),
  ("round_shields_leather_3","round_shields_leather_3"),

  ("round_shields_wood_1","round_shields_wood_1"),
  ("round_shields_wood_2","round_shields_wood_2"),
  ("round_shields_wood_3","round_shields_wood_3"),

  ("round_shields_germanic_1","round_shields_germanic_1"),
  ("round_shields_germanic_2","round_shields_germanic_2"),
  ("round_shields_germanic_3","round_shields_germanic_3"),
  ("round_shields_germanic_4","round_shields_germanic_4"),
  ("round_shields_germanic_5","round_shields_germanic_5"),
  ("round_shields_germanic_6","round_shields_germanic_6"),
  ("round_shields_germanic_7","round_shields_germanic_7"),
  ("round_shields_germanic_8","round_shields_germanic_8"),
  ("round_shields_germanic_9","round_shields_germanic_9"),
  ("round_shields_germanic_10","round_shields_germanic_10"),
  ("round_shields_germanic_11","round_shields_germanic_11"),
  ("round_shields_germanic_12","round_shields_germanic_12"),
  ("round_shields_germanic_13","round_shields_germanic_13"),
  ("round_shields_germanic_14","round_shields_germanic_14"),
  ("round_shields_germanic_15","round_shields_germanic_15"),
  ("round_shields_germanic_16","round_shields_germanic_16"),
  ("round_shields_germanic_17","round_shields_germanic_17"),
  ("round_shields_germanic_18","round_shields_germanic_18"),
  ("round_shields_germanic_19","round_shields_germanic_19"),
  ("round_shields_germanic_20","round_shields_germanic_20"),
  ("round_shields_germanic_21","round_shields_germanic_21"),
  ("round_shields_germanic_22","round_shields_germanic_22"),
  ("round_shields_germanic_23","round_shields_germanic_23"),
  ("round_shields_germanic_24","round_shields_germanic_24"),
  ("round_shields_germanic_25","round_shields_germanic_25"),
  ("round_shields_germanic_26","round_shields_germanic_26"),

  #romans
  ("round_shields_roman_1","round_shields_roman_1"),
  ("round_shields_roman_2","round_shields_roman_2"),
  ("round_shields_roman_3","round_shields_roman_3"),
  ("round_shields_roman_4","round_shields_roman_4"),
  ("round_shields_roman_5","round_shields_roman_5"),
  ("round_shields_roman_6","round_shields_roman_6"),
  ("round_shields_roman_7","round_shields_roman_7"),
  ("round_shields_roman_8","round_shields_roman_8"),
  ("round_shields_roman_9","round_shields_roman_9"),
  ("round_shields_roman_10","round_shields_roman_10"),
  ("round_shields_roman_11","round_shields_roman_11"),
  ("round_shields_roman_12","round_shields_roman_12"),
  ("round_shields_roman_13","round_shields_roman_13"),
  ("round_shields_roman_14","round_shields_roman_14"),
  ("round_shields_roman_15","round_shields_roman_15"),
  ("round_shields_roman_16","round_shields_roman_16"),
  ("round_shields_roman_17","round_shields_roman_17"),
  ("round_shields_roman_18","round_shields_roman_18"),
  ("round_shields_roman_19","round_shields_roman_19"),
  ("round_shields_roman_20","round_shields_roman_20"),
  ("round_shields_roman_21","round_shields_roman_21"),
  ("round_shields_roman_22","round_shields_roman_22"),
  ("round_shields_roman_23","round_shields_roman_23"),
  ("round_shields_roman_24","round_shields_roman_24"),
  ("round_shields_roman_25","round_shields_roman_25"),
  ("round_shields_roman_26","round_shields_roman_26"),
  ("round_shields_roman_27","round_shields_roman_27"), #aetius shield
  ("round_shields_roman_28","round_shields_roman_28"),
  ("round_shields_roman_29","round_shields_roman_29"),

  ("round_shields_domestici","round_shields_domestici"),

  #Mauri + Cantaber
  ("round_shields_mauri_1","round_shields_mauri_1"),
  ("round_shields_mauri_2","round_shields_mauri_2"),
  ("round_shields_mauri_3","round_shields_mauri_3"),
  ("round_shields_mauri_4","round_shields_mauri_4"),
  #Just Mauri
  ("round_shields_mauri_5","round_shields_mauri_5"),
  #Britons + Cantaber
  ("round_shields_britons_1","round_shields_britons_1"),
  ("round_shields_britons_2","round_shields_britons_2"),
  ("round_shields_britons_3","round_shields_britons_3"),
  ("round_shields_britons_4","round_shields_britons_4"),

  #Colors
  ("round_shields_red_1","round_shields_red_1"),
  ("round_shields_red_2","round_shields_red_2"),
  ("round_shields_red_3","round_shields_red_3"),

  ("round_shields_blue_1","round_shields_blue_1"),
  ("round_shields_blue_2","round_shields_blue_2"),
  ("round_shields_blue_3","round_shields_blue_3"),

  ("round_shields_green_1","round_shields_green_1"),
  ("round_shields_green_2","round_shields_green_2"),

  ("round_shields_gray_1","round_shields_gray_1"),
  ("round_shields_gray_2","round_shields_gray_2"),

  ("round_shields_orange_1","round_shields_orange_1"),
  ("round_shields_yellow_1","round_shields_yellow_1"),
  ("round_shields_white_1","round_shields_white_1"),

  #for unique shields
  ("unique_round_shields_1","unique_round_shields_1"),

#WICKER SHIELDS
  ("wicker_shields_1","wicker_shields_1"),
  ("wicker_shields_2","wicker_shields_2"),
  ("wicker_shields_3","wicker_shields_3"),
#KERCH SHIELDS
  ("kerch_shield_1","kerch_shield_1"),
  ("kerch_shield_2","kerch_shield_2"),
  ("kerch_shield_3","kerch_shield_3"),
  ("kerch_shield_4","kerch_shield_4"),
  ("kerch_shield_5","kerch_shield_5"),
  ("kerch_shield_6","kerch_shield_6"),
  ("kerch_shield_7","kerch_shield_7"),
  ("kerch_shield_8","kerch_shield_8"),
  ("kerch_shield_9","kerch_shield_9"),
  ("kerch_shield_10","kerch_shield_10"),
  ("kerch_shield_11","kerch_shield_11"),
  ("kerch_shield_12","kerch_shield_12"),
  ("kerch_shield_13","kerch_shield_13"),
  ("kerch_shield_14","kerch_shield_14"),
  ("kerch_shield_15","kerch_shield_15"),
  ("kerch_shield_wood","kerch_shield_wood"),
#OVAL SHIELDS
  ("oval_shields_white_1","oval_shields_white_1"),
  ("oval_shields_red_1","oval_shields_red_1"),
  ("oval_shields_blue_1","oval_shields_blue_1"),
  ("oval_shields_green_1","oval_shields_green_1"),
  ("oval_shields_yellow_1","oval_shields_yellow_1"),
  ("oval_shields_leather_1","oval_shields_leather_1"),
  ("oval_shields_leather_2","oval_shields_leather_2"),
  #CHI RHO
  ("oval_shields_chi_rho_1","oval_shields_chi_rho_1"),
  ("oval_shields_chi_rho_2","oval_shields_chi_rho_2"),
  ("oval_shields_chi_rho_3","oval_shields_chi_rho_3"),
  #MISC ROMAN SHIELDS
  ("oval_shields_limitanei_1","oval_shields_limitanei_1"),
  ("oval_shields_limitanei_2","oval_shields_limitanei_2"),
  ("oval_shields_limitanei_3","oval_shields_limitanei_3"),
  ("oval_shields_limitanei_4","oval_shields_limitanei_4"),
  #ROMANO-BRITON
  ("oval_shields_briton_1","oval_shields_briton_1"),
  #ROMANO-MAURI
  ("oval_shields_african_1","oval_shields_african_1"),
  ("oval_shields_african_2","oval_shields_african_2"),
  #WRE
  ("oval_shields_west_1","oval_shields_west_1"),
  ("oval_shields_west_2","oval_shields_west_2"),
  ("oval_shields_west_3","oval_shields_west_3"),
  ("oval_shields_west_4","oval_shields_west_4"),
  #ERE
  ("oval_shields_east_1","oval_shields_east_1"),
  ("oval_shields_east_2","oval_shields_east_2"),
  ("oval_shields_east_3","oval_shields_east_3"),
  ("oval_shields_east_4","oval_shields_east_4"),
  ("oval_shields_east_5","oval_shields_east_5"),
  ("oval_shields_east_6","oval_shields_east_6"),
  ("oval_shields_east_7","oval_shields_east_7"),

  ("oval_shields_domestici_1","oval_shields_domestici_1"),
  #unique
  ("oval_shields_unique_1","oval_shields_unique_1"),


  #eastern germanic shields by fabio
  ("eastern_germanic_shield_1","eastern_germanic_shield_1"),
  ("eastern_germanic_shield_2","eastern_germanic_shield_2"),
  ("eastern_germanic_shield_3","eastern_germanic_shield_3"),
  ("eastern_germanic_shield_4","eastern_germanic_shield_4"),
  ("eastern_germanic_shield_5","eastern_germanic_shield_5"),
  ("eastern_germanic_shield_6","eastern_germanic_shield_6"),

  ("balt_shields_1_wood","balt_shields_1_wood"),
  ("balt_shields_white_1","balt_shields_white_1"),
  ("balt_shields_blue_1","balt_shields_blue_1"),
  ("balt_shields_green_1","balt_shields_green_1"),
  ("balt_shields_red_1","balt_shields_red_1"),

#Georgian Rectangular Shields
  ("georgian_rectangular_shield_wood_1","georgian_rectangular_shield_wood_1"),
  ("georgian_rectangular_shield_wood_2","georgian_rectangular_shield_wood_2"),
  ("georgian_rectangular_shield_wood_3","georgian_rectangular_shield_wood_3"),

  ("georgian_rectangular_shield_leather_1","georgian_rectangular_shield_leather_1"),
  ("georgian_rectangular_shield_leather_2","georgian_rectangular_shield_leather_2"),
  ("georgian_rectangular_shield_leather_3","georgian_rectangular_shield_leather_3"),

#Pictish/arab shields
  ("pict_shield_1","pict_shield_1"),
  ("pict_shield_2","pict_shield_2"),
  ("pict_shield_3","pict_shield_3"),
  ("pict_shield_4","pict_shield_4"),
  ("pict_shield_5","pict_shield_5"),
  ("pict_shield_6","pict_shield_6"),
  ("pict_shield_7","pict_shield_7"),

#skin colored arms!
  ("roman_dress_arms_white","roman_dress_arms_white"),
  ("roman_dress_arms_brown","roman_dress_arms_brown"),
  ("roman_dress_arms_light","roman_dress_arms_light"),

  ("short_tunic_arms_white","short_tunic_arms_white"),
  ("short_tunic_arms_black","short_tunic_arms_black"),
  ("short_tunic_arms_brown","short_tunic_arms_brown"),
  ("short_tunic_arms_light","short_tunic_arms_light"),
  ("short_tunic_arms_mid","short_tunic_arms_mid"),
  ("short_tunic_arms_brown2","short_tunic_arms_brown2"),

  ("tunic_legs_white","tunic_legs_white"),
  ("tunic_legs_light","tunic_legs_light"),
  ("tunic_legs_mid","tunic_legs_mid"),
  ("tunic_legs_brown","tunic_legs_brown"),
  ("tunic_legs_black","tunic_legs_black"),
  ("tunic_legs_brown2","tunic_legs_brown2"),

  ("male_arms_white","male_arms_white"),
  ("male_arms_black","male_arms_black"),
  ("male_arms_brown","male_arms_brown"),
  ("male_arms_mid","male_arms_mid"),
  ("male_arms_light","male_arms_light"),
  ("male_arms_brown2","male_arms_brown2"),

  ("african_kilt_body_white","african_kilt_body_white"),
  ("african_kilt_body_black","african_kilt_body_black"),
  ("african_kilt_body_brown","african_kilt_body_brown"),
  ("african_kilt_body_mid","african_kilt_body_mid"),
  ("african_kilt_body_light","african_kilt_body_light"),

  ("exomis_body_1_white","exomis_body_1_white"),
  ("exomis_body_1_black","exomis_body_1_black"),
  ("exomis_body_1_brown","exomis_body_1_brown"),
  ("exomis_body_1_mid","exomis_body_1_mid"),
  ("exomis_body_1_light","exomis_body_1_light"),

  ("pants_body_white","pants_body_white"),
  ("pants_body_black","pants_body_black"),
  ("pants_body_brown","pants_body_brown"),
  ("pants_body_mid",  "pants_body_mid"),
  ("pants_body_light","pants_body_light"),


  ("your_men_break_off_the_siege_of_s10_to_follow_you", "Your men break off the siege of {s10} to follow you."),
  ("if_you_get_too_far_from_s10_your_siege_will_end", "If you get too far from {s10}, your siege will end."),
  ("the_s0_in_s4_has_been_completed", "The {s0} in {s4} has been completed."),
  ("s5_sends_word_that_your_betrothal_is_ended", "{s5} sends word that your betrothal is ended!"),
  ("you_dont_have_enough_money_to_continue_training_troops_at_s10", "You don't have enough money to continue training troops at {s10}."),
  ("at_s10_has_promoted_reg5_reg6s8_to_s9s6_to_s7", "at {s10} has promoted {reg5} {reg6?{s8} to {s9}:{s6} to {s7}}."),
  ("good_news_our_foragers_found_much_meat", "Good news! Our foragers found much meat."),
  ("our_foragers_have_returned_after_getting_some_food", "Our foragers have returned after getting some food in nearby villages, but the villagers are upset with us."),
  ("bad_news_our_foragers_didnt_find_food_today", "Bad news! Our foragers didn't find food today."),
  ("very_bad_news_our_foragers_were_attacked", "Very bad news! Our foragers were attacked by angry villagers, and we lost two to four men."),
  ("your_scouts_are_exploring_enemy_territory", "Your scouts are exploring enemy territory."),
  ("very_bad_news_our_scouts_were_attacked", "Very bad news! Our scouts were attacked, and we lost two to four men."),
  ("you_hear_rumors_of_discontent_among_your_men", "You hear rumors of discontent among your men. You should do something to raise their flagging spirits."),
  ("i_dont_have_enough_money", "I don't have enough money."),
  ("forget_it", "Forget it."),
  ("you_need_to_improve_your_refuge_first", "Improve your refuge first."),
  ("you_have_suffered_a_serious_injury_to_your", "You have suffered a serious injury to your"),
  ("it_will_be_permanent_in_reg1_days", "It will become permanent in {reg1} days."),
  ("it_will_be_cured_in_reg1_days", "It will heal in {reg1} days."),
  ("go_to_the_lords_hall_s1", "Visit the lord's hall{s1}."),
#######SIEGE WARFARE
  ("circunvalation_none",">>There is no blockade. Men and supplies can enter and exit practically at will.^^"),
  ("water_poison_im","Your men could throw dead rats in the wells and other water sources. That would make the population and the garrison sick." ),
  ("cattle_kill_im","Your men could kill the cattle they have here and in nearby villages. That would drastically reduce their food reserves.^^Moreover, this would damage the prestige and income of the lord of this place."),
  ("people_morale_im","Your men could spread rumors, leave the dead bodies of some locals at night in the square, and sow dissension among the defenders. This could also bring some men from their garrison to us."),
  ("food_burn_im","Your men could burn their granaries. This would cause devastation in their food stocks."),
  ("give_order", "So Order"),
  ("no_money", "You don't have enough money!"),
##wrong religion:
("no_suit_religion", "You can't possibly think of marrying into my family since you do not even believe in the same gods! Convert first, then we may discuss this topic again."),


#explanation texts for buildings

("irigation_name_rome", "Irrigation"),
("irigation_description_rome", "Improving the irrigation of farms and pasture land will improve the fertility of the lands. It will also lower probability of droughts."),

("manor_name_rome", "Manor"),
("manor_description_rome", "A manor lets you rest at the village and pay your troops half wages while you rest. You can also garrison troops in your manor to protect the village from raiding. You won't have to pay for the upkeep of stationed troops, but you can only add up to maximal 150 men. Furthermore, you can add prisoners, who will work in your village and generate additional wealth. It will cost 500 siliquae a month to maintain (costs will be paid from rents)."),

("guard_posts_name_rome", "Guard Posts"),
("guard_posts_description_rome", "Additional guard posts will help fighting banditry. Bandits will no longer be able to infest the settlement at night and looter will no longer spawn near the settlement. It will cost 300 siliquae upkeep which will be taken directly from the rents."),

("sewers_name_rome", "Sewers"),
("sewers_description_rome", "Building sewers and keeping the poop out of the streets will improve the health of the population and decrease probability of diseases."),
("sewers_name_eastern", "Kariz"),
("sewers_description_eastern", "Kariz are tunnel networks to transport water. Supply of fresh water will improve the health of the population and decrease probability of diseases."),
("sewers_name_germanic", "Water collector"),
("sewers_description_germanic", "Organizing the water supply will improve the health of the population and decrease probability of diseases."),
("sewers_name_british", "Sacred Enclosure"),
("sewers_description_british", "Having a sacred grove in the middle of the settlement will appease the gods and improve the health of the population and decrease probability of diseases."),
("sewers_name_dacian", "Modest sewers"),
("sewers_description_dacian", "Sewers will improve the health of the population and decrease probability of diseases."),
("sewers_name_nomadic", "Camp of Vitality"),
("sewers_description_nomadic", "A quiet place where the people can rest will improve the health of the population and decrease probability of diseases."),

("mills_name_rome", "Industrial Mills"),
("mills_description_rome", "An industrial mill will increase production of bread and other goods and thus increase wealth and rents."),
("mills_name_eastern", "Royal Mills"),
("mills_description_eastern", "Building additional mills will increase production of bread and other goods and thus increase wealth and rents."),
("mills_name_germanic", "Mills and Bakery"),
("mills_description_germanic", "Building more mills and bakeries will increase production of bread and other goods and thus increase wealth and rents."),
("mills_name_british", "Mills of the Chieftain"),
("mills_description_british", "Having additional mills will increase production of bread and other goods and thus increase wealth and rents."),
("mills_name_dacian", "Royal Granary"),
("mills_description_dacian", "Additional mills and a place to store the grain will increase production of bread and other goods and thus increase wealth and rents."),
("mills_name_nomadic", "Tribal Granary"),
("mills_description_nomadic", "A granary to store grain will increase production of bread and other goods and thus increase wealth and rents."),

("looms_name_rome", "Industrial Looms"),
("looms_description_rome", "Industrial looms will increase production of linen and wool cloths and thus increase wealth and rents."),
("looms_name_eastern", "Royal Loom Workshops"),
("looms_description_eastern", "More looms will increase production of linen and wool cloths and thus increase wealth and rents."),
("looms_name_germanic", "Loom Workshops"),
("looms_description_germanic", "Building loom workshops looms will increase production of linen and wool cloths and thus increase wealth and rents."),
("looms_name_british", "Artisans"),
("looms_description_british", "Artisans producting additional linen and wool cloths will increase wealth and rents."),
("looms_name_dacian", "Royal Looms"),
("looms_description_dacian", "Investing into loom workshops will increase production of linen and wool cloths and thus increase wealth and rents."),
("looms_name_nomadic", "Weavery Camp"),
("looms_description_nomadic", "Weaveries will increase production of linen and wool cloths and thus increase wealth and rents."),

("smithies_name_rome", "Industrial Smithies"),
("smithies_description_rome", "Industrial smithies will increase production of tools and other metal goods and thus increase wealth and rents."),
("smithies_name_eastern", "Royal Smithies"),
("smithies_description_eastern", "More smithies will increase production of tools and other metal goods and thus increase wealth and rents."),
("smithies_name_germanic", "Blacksmith"),
("smithies_description_germanic", "A blacksmith will increase production of tools and other metal goods and thus increase wealth and rents."),
("smithies_name_british", "Toolmaker"),
("smithies_description_british", "A toolmaker will increase production of tools and other metal goods and thus increase wealth and rents."),
("smithies_name_dacian", "Royal Iron Smelt Works"),
("smithies_description_dacian", "Investing into iron smelt works will increase the production of iron and other metal goods and thus increase wealth and rents."),
("smithies_name_nomadic", "Tribal Smithies"),
("smithies_description_nomadic", "Smithies will increase production of tools and other metal goods and thus increase wealth and rents."),

("fishing_name_rome", "Fishing Port"),
("fishing_description_rome", "Building an own port for a fishing fleet will increase the production of fish and thus increase rents. It will also generate 500 siliquae which are added to the rents (tolls)."),

("roads_name_rome", "Paved Roads"),
("roads_description_rome", "Roads simplify transportation and will increase trade and prosperity. It will also generate 2,000 siliquae which are added to the rents (tolls)."),
("roads_name_eastern", "Royal Toll Roads"),
("roads_description_eastern", "Roads simplify transportation and will increase trade and prosperity. It will also generate 2,000 siliquae which are added to the rents (tolls)."),
("roads_name_germanic", "Meadhall"),
("roads_description_germanic", "Building a large meadhall will increase trade and prosperity as people from nearby villages will come to spend their time there. It will also generate 2,000 siliquae which are added to the rents."),
("roads_name_british", "Farmer's Market"),
("roads_description_british", "A large marketplace will increase trade and prosperity. It will also generate 2,000 siliquae which are added to the rents."),
("roads_name_dacian", "Royal Treasury"),
("roads_description_dacian", "Minting coins and additional tax collectors will increase your income from trade and it will also generate 2,000 siliquae which are added to the rents."),

("roads_name_nomadic", "Marketplace"),
("roads_description_nomadic", "A marketplace will increase trade and prosperity. It will also generate 2,000 siliquae which are added to the rents (tolls)."),

("hospital_name_rome", "Hospital"),
("hospital_description_rome", "A hospital will improve the health of the population and increase your relation with the settlement. It has a monthly upkeep of 1,000 siliquae which will be taken from the rents."),
("hospital_name_eastern", "Shabestans"),
("hospital_description_eastern", "Shabestans are an underground floor with windcatchers to provide a cool environment. Thus, they will improve the health of the population and increase your relation with the settlement. It has a monthly upkeep of 1,000 siliquae which will be taken from the rents."),
("hospital_name_germanic", "Healer"),
("hospital_description_germanic", "A healer will improve the health of the population by treating their illnesses and increase your relation with the settlement. It has a monthly upkeep of 1,000 siliquae which will be taken from the rents."),
("hospital_name_british", "Druid Healer"),
("hospital_description_british", "A druidic healer will improve the health of the population by treating their illnesses and increase your relation with the settlement. It has a monthly upkeep of 1,000 siliquae which will be taken from the rents."),
("hospital_name_dacian", "Hospital"),
("hospital_description_dacian", "A hospital will increase the health of the population and increase your relation with the settlement. It has a monthly upkeep of 1,000 siliquae which will be taken from the rents."),
("hospital_name_nomadic", "Shaman's Hut"),
("hospital_description_nomadic", "A shaman will improve the health of the population by treating their illnesses and increase your relation with the settlement. It has a monthly upkeep of 1,000 siliquae which will be taken from the rents."),

("habour_name_rome", "Great Harbour"),
("habour_description_rome", "Enlarging the port will increase tariffs from sea trade and will increase prosperity and generate additional 2,500 siliquae of rents (tolls). Building such a large project will give you renown and experience."),
("habour_name_eastern", "Grand Merchant Port"),
("habour_description_eastern", "Enlarging the port will increase tariffs from sea trade and will increase prosperity and generate additional 2,500 siliquae of rents (tolls). Building such a large project will give you renown and experience."),
("habour_name_germanic", "Docks"),
("habour_description_germanic", "Building docks and a proper port will increase tariffs from sea trade and will increase prosperity and generate additional 2,500 siliquae of rents (tolls). Building such a large project will give you renown and experience."),
("habour_name_british", "Port"),
("habour_description_british", "Building a port will increase tariffs from sea trade and will increase prosperity and generate additional 2,500 siliquae of rents (tolls). Building such a large project will give you renown and experience."),
("habour_name_dacian", "Harbour"),
("habour_description_dacian", "Enlarging the port will increase tariffs from sea trade and will increase prosperity and generate additional 2,500 siliquae of rents (tolls). Building such a large project will give you renown and experience."),
("habour_name_nomadic", "Basic Port"),
("habour_description_nomadic", "Building a basic port will increase tariffs from sea trade and will increase prosperity and generate additional 2,500 siliquae of rents (tolls). Building such a large project will give you renown and experience."),


("farming_name_rome", "Provincial Farming"),
("farming_description_rome", "Investing into provincial farming and irrigation will increase the production of grain and other goods and thus increase rents."),
("farming_name_eastern", "Uzbari"),
("farming_description_eastern", "Building royal estates with improved irrigation will increase the production of grain and other goods and thus increase rents."),
("farming_name_germanic", "Farmsteads"),
("farming_description_germanic", "Building more farmsteads will increase the production of grain and other goods and thus increase rents."),
("farming_name_british", "Oathsworn Hamlets"),
("farming_description_british", "Give lands to minor nobles to harvest grain and other goods will increase rents."),
("farming_name_dacian", "Aristocratic Hamlets"),
("farming_description_dacian", "Give lands to local aristocracy to harvest grain and other goods will increase rents."),
("farming_name_nomadic", "Tributary Farms"),
("farming_description_nomadic", "More farmers who pay tributes will mean an increase of rents."),


("pasture_name_rome", "Provincial pastureland"),
("pasture_description_rome", "Increasing the pastureland will allow more cattle, sheep and horses to graze, which will generate more rents over time."),
("pasture_name_eastern", "Patbaz pastureland"),
("pasture_description_eastern", "Increasing the pastureland will allow more cattle, sheep and horses to graze, which will generate more rents over time."),
("pasture_name_germanic", "Pasturelands"),
("pasture_description_germanic", "Increasing the pastureland will allow more cattle, sheep and horses to graze, which will generate more rents over time."),
("pasture_name_british", "Oathsworn pastureland"),
("pasture_description_british", "Giving lands to minor nobles to graze their cattle, sheep and horses, which will generate more rents over time."),
("pasture_name_dacian", "Aristocratic pastureland"),
("pasture_description_dacian", "Giving pastureland to local aristocracy will allow them to grow more cattle, sheep and horses, which will generate more rents over time."),
("pasture_name_nomadic", "Tribal Herds"),
("pasture_description_nomadic", "Enlarge the herds of the tribe with more cattle, sheep and horses, which will generate more rents over time."),


("trader_name_rome", "Provincial Trader"),
("trader_description_rome", "Investment into local trade will increase the tariffs generated by villagers when entering the market town and will increase its prosperity. Additionally you will get 1,000 siliquae per month added to your rents (tolls)."),
("trader_name_eastern", "Bazaar"),
("trader_description_eastern", "Investment into local trade will increase the tariffs generated by villagers when entering the market town and will increase its prosperity. Additionally you will get 1,000 siliquae per month added to your rents (tolls)."),
("trader_name_germanic", "Fair"),
("trader_description_germanic", "Greating a place for fairs and markets will increase local trade will increase the tariffs generated by villagers when entering the market town and will increase its prosperity. Additionally you will get 1,000 siliquae per month added to your rents (tolls)."),
("trader_name_british", "Tavern"),
("trader_description_british", "By building a tavern people from nearby villages will come and thus increases trade and wealth. Additionally you will get 1,000 siliquae per month added to your rents."),
("trader_name_dacian", "Public Markets"),
("trader_description_dacian", "Investment into regional trade will increase the tariffs generated by villagers when entering the market town and will increase its prosperity. Additionally you will get 1,000 siliquae per month added to your rents (tolls)."),
("trader_name_nomadic", "Trading Post"),
("trader_description_nomadic", "A trading post will increase the tariffs generated by villagers when entering the market town and will increase its prosperity. Additionally you will get 1,000 siliquae per month added to your rents (tolls)."),


("ironmine_name_rome", "Iron mine"),
("ironmine_description_rome", "Investing into local iron mines will increase the prosperity of the village every month. It will also increase your income generated by slaves working in the village."),
("quarry_name_rome", "Quarry"),
("quarry_description_rome", "A quarry will increase the production of stone and generates additional income from slaves working in the village."),
("slave_market_name_rome", "Slave Market"),
("slave_market_description_rome", "A slave market increases the prosperity and tariffs of the center. It will increase income of the town by 1,500 (fees)."),
("silvermine_name_rome", "Silver and gold mine"),
("silvermine_description_rome", "Investing into local silver and gold production will increasse the prosperity of the village every month and will generate an additional income directly paid into your pocket. It will also increase the income generarted by slaves working in the village."),

#house of strength - for easterns
("training_name_rome", "Training Ground"),
("training_description_rome", "A training ground allows your troops to train while garrisoned in the center. It will cost 1000 siliquae a month to maintain (costs will be paid from rents)."),

("mill_simple_name_rome", "Mill"),
("mill_simple_description_rome", "A mill increases village prosperity every month. And it will also add an additional income of 600 siliquae to the center rents (fees)."),

("firefighters_name_rome", "Fire Department"),
("firefighters_description_rome", "Organizing a professional fire department can decrease the chance of devastating fires. It will cost 500 siliquae a month to maintain (costs will be paid from rents)."),
("firefighters_name_eastern", "Windcatchers"),
("firefighters_description_eastern", "Windcatchers are special buildings designed to decrease temprature in the city. Hence they decreases the chance of devastating fires. It will cost 500 siliquae a month to maintain (costs will be paid from rents)."),
("firefighters_name_germanic", "Sanctuary of Wodanaz"),
("firefighters_description_germanic", "Creating a sacred grove for Wodanaz to honour him will decrease the chance of devastating events like fires. It will cost 500 siliquae a month to maintain (costs will be paid from rents)."),
("firefighters_name_british", "Sanctuary of Epona"),
("firefighters_description_british", "Creating a large sanctuary for Epona will appease her and decrease the chance of devastating events like fires. It will cost 500 siliquae a month to maintain (costs will be paid from rents)."),
("firefighters_name_dacian", "Basic Sanitations"),
("firefighters_description_dacian", "Make waster disposal more efficient to decrease chance of devastating events like fires. It will cost 500 siliquae a month to maintain (costs will be paid from rents)."),
("firefighters_name_nomadic", "Altar"),
("firefighters_description_nomadic", "Build an altar to honor the gods. This will decrease chance of devastating events like fires. It will cost 500 siliquae a month to maintain (costs will be paid from rents)."),

("watchtower_name_rome", "Watch Tower"),
("watchtower_description_rome", "A watch tower lets the villagers raise alarm earlier. The time it takes for enemies to loot the village increases by 50%."),

("school_name_rome", "School"),
("school_description_rome", "A shool increases the loyality of the villagers to you by +1 every month and also increases wealth. It will cost 500 siliquae a month to maintain (costs will be paid from rents)."),
("school_name_eastern", "Archery Games"),
("school_description_eastern", "Games will entertain the population and thus increase your relation by +1 every month and also increases wealth. It will cost 500 siliquae a month to maintain (costs will be paid from rents)."),
("school_name_germanic", "Storyteller"),
("school_description_germanic", "Building a house for a storyteller will entertain the population and thus increase the loyality of the villagers to you by +1 every month and also increases wealth. It will cost 500 siliquae a month to maintain (costs will be paid from rents)."),
("school_name_british", "Hall of the Elders"),
("school_description_british", "Building a hall where the elders can gather will increase your realtion by +1 each month and also increases wealth. It will cost 500 siliquae a month to maintain (costs will be paid from rents)."),
("school_name_dacian", "School of Nobles"),
("school_description_dacian", "A shool to teach the local aristocracy will increases the loyality by +1 every month and also increases wealth. It will cost 500 siliquae a month to maintain (costs will be paid from rents)."),
("school_name_nomadic", "Learning Grove"),
("school_description_nomadic", "A learning grove increases the loyality of the villagers to you by +1 every month and also increases wealth. It will cost 500 siliquae a month to maintain (costs will be paid from rents)."),

("messenger_post_name_rome", "Messenger Post"),
("messenger_post_description_rome", "A messenger post lets the inhabitants send you a message whenever enemies are nearby, even if you are far away from here. It will cost 250 siliquae a month to maintain (costs will be paid from rents)."),
("prison_tower_name_rome", "Prison"),
("prison_tower_description_rome", "A prison reduces the chance of captives held here running away successfully."),

("forum_name_rome", "Forum"),
("forum_description_rome", "Your own forum, the Forum {playername}, is a sign of power. It will increase your renown, your relation with this center and tariff income. It will also increase your reputation and gain you experience."),
("forum_name_eastern", "Grand Bazaar"),
("forum_description_eastern", "Building a great bazaar is a sign of prestige. It will increase your renown, your relation with this center and tariff income. It will also increase your reputation and gain you experience."),
("forum_name_germanic", "Great Thingstead"),
("forum_description_germanic", "Greating sever halls where for the thingstead is a sign of power. It will increase your renown and your relation with this center. It will also increase your reputation and gain you experience. Additionally the income from tariffs will be raised due to increased trade."),
("forum_name_british", "Coin Mint"),
("forum_description_british", "Building a smithy to mint your own coint is a sign of power. It will increase your renown and your relation with this center. It will also increase your reputation and gain you experience. Additionally the income from tariffs will be raised due to increased trade."),
("forum_name_dacian", "Agora"),
("forum_description_dacian", "A place to trade and also a sign of your power. It will increase your renown and your relation with this center. It will also increase your reputation and gain you experience. Additionally the income from tariffs will be increased due to pilgrims coming into the town."),
("forum_name_nomadic", "Sanctuary of Api"),
("forum_description_nomadic", "Honor the great goddess Api. It will increase your renown and your relation with this center. It will also increase your reputation and gain you experience. Additionally the tariffs income will be increased due to pilgrims entering town."),

("temple_name_rome", "Temple of {s38}"),
("temple_description_rome", "Your own temple to honor {s38} will allow you to make sacrifices at the town. It will for sure please {s38}."),

("theatre_name_rome", "Theatre"),
("theatre_description_rome", "A theatre, the Theatrum {playername}, gives the people another possibility to enjoy. It is also a sign of power and increase your renown and relation with this center. It will also increase your reputation and gain you experience."),
("theatre_name_eastern", "Field of Games"),
("theatre_description_eastern", "Holding great games in horse archery and horse racing gives the people another possibility to enjoy. It is also a sign of power and increase your renown and relation with this center. It will also increase your reputation and gain you experience."),
("theatre_name_germanic", "Loremaster's Hall"),
("theatre_description_germanic", "A great hall where a loremaster can talk about the tales of our people gives another possibility to enjoy. It is also a sign of power and increase your renown and relation with this center. It will also increase your reputation and gain you experience."),
("theatre_name_british", "Bards Hall"),
("theatre_description_british", "A great hall where bards gather to entertain the people with tales and plays. It is also a sign of power and increase your renown and relation with this center. It will also increase your reputation and gain you experience."),
("theatre_name_dacian", "Theatre"),
("theatre_description_dacian", "A theatre gives people a place to enjoy. It is also a sign of power and increase your renown and relation with this center. It will also increase your reputation and gain you experience."),
("theatre_name_nomadic", "Great Horce Racing Games"),
("theatre_description_nomadic", "Horse races give the people another possibility to enjoy. Holding such games regularly is a sign of power and increase your renown and relation with this center. It will also increase your reputation and gain you experience."),

("public_baths_name_rome", "Public Baths"),
("public_baths_description_rome", "Baths are a place for people to enjoy. It is another sign of power and increase your renown and relation with this center. It will also increase your reputation and gain you experience."),
("public_baths_name_eastern", "Dynastic Fire Altar"),
("public_baths_description_eastern", "Build a great fire altar for your dynasty. It is another sign of power and increase your renown and relation with this center. It will also increase your reputation and gain you experience."),
("public_baths_name_germanic", "Bathhouse"),
("public_baths_description_germanic", "The bathhouse is a place for people to enjoy. It will increase your renown and relation with this center. It will also increase your reputation and gain you experience."),
("public_baths_name_british", "Sacred place of the Druids"),
("public_baths_description_british", "Creating a place where druids gather will increase the loyality of the population. It is another sign of power and increase your renown and relation with this center. It will also increase your reputation and gain you experience."),
("public_baths_name_dacian", "Large arena"),
("public_baths_description_dacian", "A large arena to give people a place to enjoy. It is another sign of power and increase your renown and relation with this center. It will also increase your reputation and gain you experience."),
("public_baths_name_nomadic", "House of the Ancestors"),
("public_baths_description_nomadic", "A holy place to honor the dead and drink to their memory. It is another sign of power and increase your renown and relation with this center. It will also increase your reputation and gain you experience."),

("triumphal_arch_name_rome", "Triumphal Arch"),
("triumphal_arch_description_rome", "A triumphal arch show your most famous victories over your enemies. It will increase your renown. Even after your death people will talk about you. It will also increase your reputation and gain you experience."),
("triumphal_arch_name_eastern", "Pahlavi Scriptorium"),
("triumphal_arch_description_eastern", "By building a scriptorum most you can spread your most famous victories over your enemies. It will increase your renown. Even after your death people will talk about you. It will also increase your reputation and gain you experience."),
("triumphal_arch_name_germanic", "Bardic Circle"),
("triumphal_arch_description_germanic", "Build a great halls for bards to sing about your most famous victories. It will increase your renown. Even after your death people will talk about you. It will also increase your reputation and gain you experience."),
("triumphal_arch_name_british", "Nemeton"),
("triumphal_arch_description_british", "A special grove to honor the gods. It will increase your renown. Even after your death people will talk about you. It will also increase your reputation and gain you experience."),
("triumphal_arch_name_dacian", "Glorius Monument"),
("triumphal_arch_description_dacian", "Build a monument to spread your fame. It will increase your renown. Even after your death people will talk about you. It will also increase your reputation and gain you experience."),
("triumphal_arch_name_nomadic", "Kurgan Field"),
("triumphal_arch_description_nomadic", "Create a place to burry great nobles. It will increase your renown. Even after your death people will talk about you. It will also increase your reputation and gain you experience."),


("barracks_name_rome", "Barracks"),
("barracks_description_rome", "This building allows you to recruit troops from your faction culture. It also increases the number of recruits available."),
("barracks_name_eastern", "Royal Barracks"),
("barracks_description_eastern", "This building allows you to recruit troops of your kingdom in an organized way. It also increases the number of recruits available."),
("barracks_name_germanic", "Warrior Hall"),
("barracks_description_germanic", "Build a warrior hall to encourage warriors of your people to settle here. It will allow you to recruit troops of your kingdom. It also increases the number of recruits available."),
("barracks_name_british", "Oathsworn Hall"),
("barracks_description_british", "Build a great hall to encourage warriors of your people to settle here. It will allow you to recruit troops of your kingdom. It also increases the number of recruits available."),
("barracks_name_dacian", "Hall of Champions"),
("barracks_description_dacian", "Build a great hall to encourage warriors of your people to settle here. It will allow you to recruit troops of your kingdom. It also increases the number of recruits available."),
("barracks_name_nomadic", "Warrior Camp"),
("barracks_description_nomadic", "Build a camp to give warriors of your people a place to life. It will allow you to recruit troops of your kingdom. It also increases the number of recruits available."),

("culture_name_rome", "Romanize the population"),
("culture_description_rome", "By introducing your traditions, laws and rituals to the local population, you can change the culture of the settlement in a peaceful way."),
("culture_name_eastern", "Assimilate the population to your culture"),
("culture_description_eastern", "By introducing your traditions, laws and rituals to the local population, you can change the culture of the settlement in a peaceful way."),
("culture_name_germanic", "Settle people of your culture"),
("culture_description_germanic", "By settling warriors and people of your culture you can change the culture of the settlement in a peaceful way."),
("culture_name_british", "Settle people of your culture"),
("culture_description_british", "By settling warriors and people of your culture you can change the culture of the settlement in a peaceful way."),
("culture_name_dacian", "Settle people of your culture"),
("culture_description_dacian", "By settling warriors and people of your culture you can change the culture of the settlement in a peaceful way."),
("culture_name_nomadic", "Settle people of your culture"),
("culture_description_nomadic", "By settling warriors and people of your culture you can change the culture of the settlement in a peaceful way."),

("event_fire_rome_name", "great fire"),
("event_fire_rome_description", "great fire"),
("event_conquered_name", "recently conquered"),
("event_conquered_description", "The settlement has been recently conquered and its administration is still in turmoil."),
("event_earthquake_name", "earthquake"),
("event_earthquake_description", "The people where shocked when the earth shaked under their feet with such a strength that even the strongest building was damaged. They left their houses and run for their lives to escape death. It will take month to bury the dead and rebuild the houses."),
("event_fire_name", "fire"),
("event_fire_description", "It all started as a small fire near the market place. Nobody thought it would persist long. The gods had no mercy and the fire increased until it destroyed nearly a quarter of the settlement. It will take a months or two until the damage is repaired."),
("event_drought_name", "drought"),
("event_drought_description", "There lack of rain has strained the supply of water too much. Many wells have dried up and the rivers are on a low water level. If the gods show no mercy the drought will continue for months."),
("event_insects_name", "beetle invasion"),
("event_insects_description", "Suddenly the sky was black, not by a cloude but a large swarm of insects. Millions of insects have invaded the fields, are destroying the crops and breeding. It will hopefully be over soon."),

("disease_consumption_name", "consumption"),
("disease_consumption_description", "The first recorded case was the son of an important nobleman. He was wracked with a bloody cough caused by cold humors in the lungs. Then the disease infected most of the population, killing many. Hopefully the disease will end soon."),

("disease_slow_fever_name", "slow fever"),
("disease_slow_fever_description", "The first case was most likely a rich noblewoman. She suffered from fever, abdominal pain, headeaches and vomiting after she returned from an nearby estate. Soon her servants where infected and then the disease spread over the whole population bringing death and pain. May the gods have mercy!"),

("disease_camp_fever_name", "camp fever"),
("disease_camp_fever_description", "The outbreak began in the slums, with thousands being plagued by rashes, fever, and coughs. Now it spread through the population bringing death and suffering, The people pray that it is soon over, but there is yet no end in sight."),

("disease_plague_name", "malaria"),
("disease_plague_description", "The origin of the outbreak is the family of a rich merchant. After returning from a trade journey he and his wife suffered from fever, tiredness, vomiting, and headaches. The cursed disease spread over the whole population, killing thousands of people leaving behind hundreds of orphans. May the gods show mercy!"),

("disease_measles_name", "measles"),
("disease_measles_description", "The origian of the outbreak is unknown. It most likely started in the merchant quarters of the settlement. Then it spread over the population, terrorising the people with red, flat rashes and fever. Gods, show mercy to this place!"),

("disease_smallpox_name", "smallpox"),
("disease_smallpox_description", "It has begon with the daughter of a wealthy merchant being riddled by scars, rashes, and bumps. Now nearly half the population is suffering from rashes. Hopefully the gods will show mercy!"),

("disease_greatpoxpox_name", "great pox"),
("disease_greatpoxpox_description", "The origin of the outbreak is unknown. Some people claim it was the wicked son of a merchant others claim it was a daughter of some nobleman, known for a lush lifestyle. who had it first. However, it spread over the population. The people are plagued by sores and inflammation and are suffering from the venereal plague."),


("slot_center_head_cattle", "head of cattle"),
("slot_center_head_sheep", "head of sheep"),
("slot_center_head_horses", "head of horses"),
("slot_center_acres_pasture", "acres of pasture land"),
("slot_center_acres_grain", "acres of grain fields"),
("slot_center_acres_olives", "acres of olive groves"),
("slot_center_acres_vineyard", "acres of vineyards"),
("slot_center_acres_flax", "acres of flax fields"),
("slot_center_acres_dates", "acres of date groves"),
("slot_center_fishing_fleet", "number of fishing boats"),
("slot_center_salt_pans", "number of salt pans"),
("slot_center_apiaries", "number of apiaries"),
("slot_center_silk_farms", "number of silk traders"),
("slot_center_kirmiz_farms", "number of dye traders"),
("slot_center_iron_deposits", "number of iron deposits"),
("slot_center_fur_traps", "number of hunting lodges"),
("slot_center_silver_deposits", "number of silver smithies"),
("slot_center_mills", "number of mills"),
("slot_center_breweries", "number of breweries"),
("slot_center_wine_presses", "number of wine presses"),
("slot_center_olive_presses", "number of olive presses"),
("slot_center_linen_looms", "number of linen looms"),
("slot_center_silk_looms", "number of velvet traders"),
("slot_center_wool_looms", "number of wool looms"),
("slot_center_pottery_kilns", "number of pottery kilns"),
("slot_center_smithies", "number of smithies"),
("slot_center_tanneries", "number of tanneries"),
("slot_center_household_gardens", "number of household gardens"),

("default_material",  "default"),
("pic_settlement_silvermine",  "pic_settlement_silvermine"),

("pic_settlement_manor",  "pic_settlement_manor"),
("pic_settlement_manor_germanic",  "pic_settlement_manor_germanic"),
("pic_settlement_manor_celtic",  "pic_settlement_manor_celtic"),
("pic_settlement_manor_dacian",  "pic_settlement_manor_dacian"),
("pic_settlement_manor_eastern",  "pic_settlement_manor_eastern"),
("pic_settlement_manor_nomadic",  "pic_settlement_manor_nomadic"),

("pic_settlement_mill",  "pic_settlement_mill"),
("pic_settlement_watchtower",  "pic_settlement_watchtower"),

("pic_settlement_school",  "pic_settlement_school"),
("pic_settlement_school_eastern",  "pic_settlement_school_eastern"),
("pic_settlement_school_dacian",  "pic_settlement_school_dacian"),
("pic_settlement_school_germanic",  "pic_settlement_school_germanic"),
("pic_settlement_school_celtic",  "pic_settlement_school_celtic"),
("pic_settlement_school_nomadic",  "pic_settlement_school_nomadic"),

("pic_settlement_ironmine",  "pic_settlement_ironmine"),

("pic_settlement_changeculture",  "pic_settlement_changeculture"),
("pic_settlement_changeculture_germanic",  "pic_settlement_changeculture_germanic"),
("pic_settlement_changeculture_celtic",  "pic_settlement_changeculture_celtic"),
("pic_settlement_changeculture_armenian",  "pic_settlement_changeculture_armenian"),
("pic_settlement_changeculture_dacian",  "pic_settlement_changeculture_dacian"),
("pic_settlement_changeculture_nomadic",  "pic_settlement_changeculture_nomadic"),

("pic_settlement_farms",  "pic_settlement_farms"),
("pic_settlement_farms_eastern",  "pic_settlement_farms_eastern"),
("pic_settlement_farms_celtic",  "pic_settlement_farms_celtic"),
("pic_settlement_farms_germanic",  "pic_settlement_farms_germanic"),
("pic_settlement_farms_dacian",  "pic_settlement_farms_dacian"),

("pic_settlement_cattle",  "pic_settlement_cattle"),

("pic_settlement_trader",  "pic_settlement_trader"),
("pic_settlement_trader_eastern",  "pic_settlement_trader_eastern"),
("pic_settlement_trader_germanic",  "pic_settlement_trader_germanic"),
("pic_settlement_trader_nomadic",  "pic_settlement_trader_nomadic"),
("pic_settlement_trader_celtic",  "pic_settlement_trader_celtic"),
("pic_settlement_trader_dacian",  "pic_settlement_trader_dacian"),

("pic_settlement_quarry",  "pic_settlement_quarry"),
("pic_settlement_irigation",  "pic_settlement_irigation"),
("pic_settlement_messenger",  "pic_settlement_messenger"),
("pic_settlement_guard",  "pic_settlement_guard"),
("pic_settlement_fishport",  "pic_settlement_fishport"),

("pic_settlement_roads",  "pic_settlement_roads"),
("pic_settlement_roads_eastern",  "pic_settlement_roads_eastern"),
("pic_settlement_roads_germanic",  "pic_settlement_roads_germanic"),
("pic_settlement_roads_celtic",  "pic_settlement_roads_celtic"),
("pic_settlement_roads_dacian",  "pic_settlement_roads_dacian"),
("pic_settlement_roads_nomadic",  "pic_settlement_roads_nomadic"),

("pic_settlement_hospital",  "pic_settlement_hospital"),
("pic_settlement_hospital_eastern",  "pic_settlement_hospital_eastern"),
("pic_settlement_hospital_germanic",  "pic_settlement_hospital_germanic"),
("pic_settlement_hospital_celtic",  "pic_settlement_hospital_celtic"),
("pic_settlement_hospital_dacian",  "pic_settlement_hospital_dacian"),
("pic_settlement_hospital_nomadic",  "pic_settlement_hospital_nomadic"),

("pic_settlement_prison",  "pic_settlement_prison"),

("pic_settlement_fire",  "pic_settlement_fire"),
("pic_settlement_fire_eastern",  "pic_settlement_fire_eastern"),
("pic_settlement_fire_germanic",  "pic_settlement_fire_germanic"),
("pic_settlement_fire_nomadic",  "pic_settlement_fire_nomadic"),
("pic_settlement_fire_celtic",  "pic_settlement_fire_celtic"),
("pic_settlement_fire_dacian",  "pic_settlement_fire_dacian"),

("pic_settlement_training",  "pic_settlement_training"),
("pic_settlement_slavemarket",  "pic_settlement_slavemarket"),

("pic_settlement_barracks",  "pic_settlement_barracks"),
("pic_settlement_barracks_eastern",  "pic_settlement_barracks_eastern"),
("pic_settlement_barracks_celtic",  "pic_settlement_barracks_celtic"),
("pic_settlement_barracks_germanic",  "pic_settlement_barracks_germanic"),
("pic_settlement_barracks_dacian",  "pic_settlement_barracks_dacian"),
("pic_settlement_barracks_nomadic",  "pic_settlement_barracks_nomadic"),

("pic_settlement_sewers",  "pic_settlement_sewers"),
("pic_settlement_sewers_eastern",  "pic_settlement_sewers_eastern"),
("pic_settlement_sewers_nomadic",  "pic_settlement_sewers_nomadic"),
("pic_settlement_sewers_germanic",  "pic_settlement_sewers_germanic"),
("pic_settlement_sewers_barbarian",  "pic_settlement_sewers_barbarian"),

("pic_settlement_industry",  "pic_settlement_industry"),
("pic_settlement_industry_eastern",  "pic_settlement_industry_eastern"),
("pic_settlement_industry_barbarian",  "pic_settlement_industry_barbarian"),
("pic_settlement_industry_grain",  "pic_settlement_industry_grain"),

("pic_settlement_loom",  "pic_settlement_loom"),
("pic_settlement_loom_eastern",  "pic_settlement_loom_eastern"),
("pic_settlement_loom_germanic",  "pic_settlement_loom_germanic"),
("pic_settlement_loom_celtic",  "pic_settlement_loom_celtic"),
("pic_settlement_loom_dacian",  "pic_settlement_loom_dacian"),

("pic_settlement_smithy",  "pic_settlement_smithy"),
("pic_settlement_smithy_generic",  "pic_settlement_smithy_generic"),
("pic_settlement_smithy_barbarian",  "pic_settlement_smithy_barbarian"),


("pic_settlement_port",  "pic_settlement_port"),
("pic_settlement_port_eastern",  "pic_settlement_port_eastern"),
("pic_settlement_port_barbarian",  "pic_settlement_port_barbarian"),

("pic_settlement_forum",  "pic_settlement_forum"),
("pic_settlement_forum_celtic",  "pic_settlement_forum_celtic"),
("pic_settlement_forum_eastern",  "pic_settlement_forum_eastern"),
("pic_settlement_forum_dacian",  "pic_settlement_forum_dacian"),
("pic_settlement_forum_nomadic",  "pic_settlement_forum_nomadic"),
("pic_settlement_forum_germanic",  "pic_settlement_forum_germanic"),

("pic_settlement_theatre",  "pic_settlement_theatre"),
("pic_settlement_theatre_eastern",  "pic_settlement_theatre_eastern"),
("pic_settlement_theatre_celtic",  "pic_settlement_theatre_celtic"),
("pic_settlement_theatre_germanic",  "pic_settlement_theatre_germanic"),
("pic_settlement_theatre_dacian",  "pic_settlement_theatre_dacian"),
("pic_settlement_theatre_nomadic",  "pic_settlement_theatre_nomadic"),

("pic_settlement_triumph",  "pic_settlement_triumph"),
("pic_settlement_triumph_germanic",  "pic_settlement_triumph_germanic"),
("pic_settlement_triumph_eastern",  "pic_settlement_triumph_eastern"),
("pic_settlement_triumph_celtic",  "pic_settlement_triumph_celtic"),
("pic_settlement_triumph_dacian",  "pic_settlement_triumph_dacian"),
("pic_settlement_triumph_nomadic",  "pic_settlement_triumph_nomadic"),

("pic_settlement_water",  "pic_settlement_water"),
("pic_settlement_water_eastern",  "pic_settlement_water_eastern"),
("pic_settlement_water_germanic",  "pic_settlement_water_germanic"),
("pic_settlement_water_celtic",  "pic_settlement_water_celtic"),
("pic_settlement_water_dacian",  "pic_settlement_water_dacian"),
("pic_settlement_water_nomadic",  "pic_settlement_water_nomadic"),

("pic_settlement_temple",  "pic_settlement_temple"),
("pic_settlement_temple_barbarian",  "pic_settlement_temple_barbarian"),
("pic_settlement_temple_eastern",  "pic_settlement_temple_eastern"),

("none",  "none"),
("center_manage_denied", "You need to be either the governor of the town or increase faction centralization."),
("custom_reinforce", "{reg0} {s1} have arrived for {s2}"),
("extort_tax", "Raise special tax"),
("extort_toll", "Raise special tariffs"),
("extort_concile", "Raid the town counsel"),

("extort_tax_xp", "You can raise a special tax. As the party member with the highest trade skill ({reg2}), {reg3?you expect:{s1} expects} it would take {reg40} hours to collect this tax and would give you {reg30} siliquae: But it will upset the citizens of {s39}."),
("extort_toll_xp", "You can raise a special toll on goods which are traded today. This would upset the merchants of {s39} and the villagers of the surrounding villages, who come here to sell their goods. As the party member with the highest trade skill ({reg2}), {reg3?you expect:{s1} expects} it would take {reg40} hours to collect the toll and would give you {reg30} siliquae."),
("extort_concile_xp", "The town counsel has {reg31} in their treasury. You can force them to take over their funds. It would take you 2 hours and you would gain {reg31} siliquae."),

("region_strings_begin","ZAMB LAND"),
("region_spain","Spain"),
("region_north_africa","North Africa"),
("region_southitaly","South Italy"),
("region_nile","Nile"),
("region_syria_palestine","Syria and Palestine"),
("region_anatolia_central","Anatolia Central"),
("region_anatolia_coastal","Anatolia Coastal"),
("region_mesopotamia","Mesopotamia"),
("region_persianhill_green","Persian hills (green)"),
("region_persianhill_desert","Persian hills (desert)"),
("region_caucasus","Caucasus"),
("region_greece","Greece"),
("region_nile_delta","Nile Delta"),
("region_mountain_europe","Mountain Europe Alps"),
("region_mountain_europe_spain_france","Mountain Europe Spain France"),
("region_mountain_europe_romania","Mountain Europe Romania"),
("region_mountain_europe_bohemia","Mountain Europe Bohemia"),
("other","other region"),

("face_culture_gothic", "000000001e0c244a3daa8c987489496400000000000193390000000000000000"),
("face_culture_eastgermanic", "000000002a0064824ce376687472a55a00000000001d479b0000000000000000"),
("face_culture_romanobriton", "00000000330c120366ad8ca8dbb2c53e00000000001d58d40000000000000000"),
("face_culture_northgermanic", "000000000a10050846546dc695cdcafc00000000001e346b0000000000000000"),
("face_culture_pictish", "000000000b10614a36db6db6db6db6db00000000001db6db0000000000000000"),
("face_culture_sassanid", "000000002700f10736db6db6db6db6db00000000001db6db0000000000000000"),
("face_culture_roman", "000000000010700436db6db6db6db6db00000000001db6db0000000000000000"),
("face_culture_westerngermanic", "000000000c0404ca36db6db6db6db6db00000000000db6db0000000000000000"),
("face_culture_caucasian", "000000003d0c21c336db6db6db6db6db00000000001db6db0000000000000000"),
("face_culture_romanmauri", "000000002201504448d972d95c8636d400000000001cb8a20000000000000000"),
("face_culture_hunnic", "000000002404c08b36db6db6db6db6db00000000001db6db0000000000000000"),
("face_culture_nubian", "000000003f0164c536db6db6db6db6db00000000001db6db0000000000000000"),
("face_culture_caucasian_alan", "00000000320c214336db6db6db6db6db00000000001db6db0000000000000000"),
("face_culture_armenian", "000000000b10f1405614b1c89aad596900000000001ee30a0000000000000000"),
("face_culture_jewish", "000000003010c10745622fef5a84c6e800000000001e38ea0000000000000000"),
("face_culture_irish", "000000000b10614a36db6db6db6db6db00000000001db6db0000000000000000"),
("face_culture_slavic", "000000001e0c244a3daa8c987489496400000000000193390000000000000000"),

("face_culture_gothic_female", "00000000340c0005449a6b372d791d2300000000000db8920000000000000000"),
("face_culture_eastgermanic_female", "00000000230c300b5b5669bb1472392400000000000d42cb0000000000000000"),
("face_culture_romanobriton_female", "000000003204300b676b8e5a4cadbadc000000000011cb530000000000000000"),
("face_culture_northgermanic_female", "000000003204300b676b8e5a4cadbadc000000000011cb530000000000000000"),
("face_culture_pictish_female", "000000003204300b676b8e5a4cadbadc000000000011cb530000000000000000"),
("face_culture_sassanid_female", "000000003810601172c956934671eb630000000000059adc0000000000000000"),
("face_culture_roman_female", "000000003d0c2001349494c88a85375d000000000011a5530000000000000000"),
("face_culture_westerngermanic_female", "000000003f04300834d953d9637568cb00000000001d6d220000000000000000"),
("face_culture_caucasian_female", "00000000340c0005449a6b372d791d2300000000000db8920000000000000000"),
("face_culture_romanmauri_female", "000000001100600c46df4da8db46c45c000000000012bad40000000000000000"),
("face_culture_hunnic_female", "000000003f04600d495b96d6a52d37a100000000001daaeb0000000000000000"),
("face_culture_nubian_female", "000000000c08800225218dc92c51552500000000001db8960000000000000000"),
("face_culture_caucasian_alan_female", "000000003d0c2001349494c88a85375d000000000011a5530000000000000000"),
("face_culture_armenian_female", "000000003d0c2001349494c88a85375d000000000011a5530000000000000000"),
("face_culture_jewish_female", "000000003d08100324cc75c6f22f3bab000000000015a7340000000000000000"),
("face_culture_irish_female", "000000003204300b676b8e5a4cadbadc000000000011cb530000000000000000"),
("face_culture_slavic_female", "00000000340c0005449a6b372d791d2300000000000db8920000000000000000"),

("culture_gothic","You_are_a_Goth._Your_people_are_scions_of_Berig,_the_warrior-king_who_led_your_forefathers_from_their_ancestral_homes_in_Scandza._They_travelled_far,_through_the_dark_forests_and_swamps_of_eastern_Europa,_across_mountains_and_wide_rivers,_in_search_of_new_lands_to_settle._When_the_Huns_came,_some_fled_while_others_fought._Now,_to_east_and_west,_they_carve_out_kingdoms_by_their_strength_and_courage."),
("culture_eastgermanic","You_are_a_German_of_the_east._Long_your_ancestors_roamed_the_forests_and_steppes_of_Germania_Scythica,_hard,_cruel_lands_that_breed_stern,_doughty_folk._In_recent_times,_many_of_your_people_have_journeyed_south,_whether_in_search_of_wealth_and_warmer_climes,_or_fleeing_the_terror_from_the_east."),
("culture_romanobriton","You_are_a_Romanized_Briton._Since_the_time_of_Claudius,_your_people_have_been_proud_citizens_of_Provincia_Britannia._Now,_the_Empire_is_on_the_brink_of_collapse,_Rome's_legions_long_withdrawn_from_your_shores,_and_the_Britons_stand_alone._Enemies_abound:_savage_Picts_north_of_the_crumbling_Wall;_Scoti_slavers_from_Hibernia_in_the_west;_and_ruthless_Germanic_invaders_from_across_the_Mare_Britannicum."),
("culture_northgermanic","You_are_a_German_of_the_north._Sons_of_the_lowland_marshes_and_wetlands,_your_people_are_courageous_raiders_and_bold_seafarers._Many_make_ready_to_brave_land_or_ocean_in_search_of_new_territory_to_settle._The_Romans_in_Britannia,_far-travelled_men_report,_are_weak_and_wealthy_-_a_fine_target,_perhaps,_for_the_adventurous."),
("culture_pictish","You_are_a_Pict._Since_the_world_was_made,_your_people_have_ruled_the_chill,_beautiful_lands_of_the_far_north,_called_Caledonia_by_the_ironclad_newcomers._Wild_and_free,_you_look_with_contempt_on_your_weak_southern_neighbours_who_tremble_behind_their_great_walls_and_towers_of_stone,_which_now_stand_abandoned_and_silent."),
("culture_sassanid","You_are_a_Persian._It_is_your_people's_duty_to_serve_the_Shahanshah_and_their_destiny_to_lead_the_rest_of_the_world._This_is_the_way_of_things._Yet_still_there_are_the_Romans,_who_dare_to_claim_hegemony._Though_they_have_never_been_able_to_threaten_the_Persian_heartlands,_nor_yet_has_the_Eranshahr_destroyed_these_interlopers."),
("culture_roman","You_are_a_Roman._Your_people_are_descendants_of_Aeneas,_prince_of_Troy_and_son_of_Venus;_masters_of_the_world,_dutybound_to_carry_the_light_of_civilisation_to_all_its_corners._Scipio,_Caesar,_Agricola,_Marius,_Stilicho_-_the_great_heroes_of_the_Roman_annals_are_too_many_to_count._Yet_the_light_flickers_and_fades._Now,_like_never_before,_Rome_needs_new_heroes."),
("culture_westerngermanic","You_are_a_German_of_the_west._Some_claim_your_ancestors_came_from_distant_Pannonia;_others_that_they_were_once_subjects_of_Priam_himself_and_travelled_from_Troy_in_ancient_times._Whatever_their_origin,_your_longhaired_kings_settled_generations_ago_along_the_banks_of_the_great_river_Rhenus,_in_the_shadow_of_Rome."),
("culture_caucasian","You_are_a_Caucasian._Your_people_are_indigenous_to_the_Caucasus_Mountains,_the_great_range_that_divides_the_civilised_world_from_the_wild,_endless_northern_steppe._Your_home_is_green_and_lush_but_rugged,_your_folk_hardy_and_strong._Since_ancient_times,_your_ancestors_traded_with_the_Hellenes_or_the_Persians,_but_no_empire_has_ever_truly_conquered_your_lands."),
("culture_romanmauri","You_are_a_Romanized_Berber._For_centuries,_your_ancestors_were_faithful_subjects_of_Rome_in_Africa._Now,_the_Empire_is_on_the_brink_of_collapse_and_your_people_control_their_own_destiny_at_last._This_is_an_era_of_promise_and_of_danger,_for_the_straw-haired_barbarians_who_marched_through_your_ancestral_lands_have_settled_in_Carthage_and_agitate_for_war."),
("culture_hunnic","You_are_a_Hun._Your_nomadic_ancestors_came_on_horseback_from_the_distant_east,_migrating_across_the_great_plains_in_pursuit_of_the_herds._Then_they_found_a_new_quarry,_and_the_soft_nations_of_the_south_learned_to_tremble_at_their_name._Mighty_Attila_almost_forged_a_great_Hunnic_empire_in_this_new_world,_but_he_was_overcome_and_your_people_scattered."),
("culture_nubian","You_are_a_Nubian._Your_people_are_sons_of_royal_Mero._Once,_your_great_kings_were_lords_of_Kush_and_even_pharaohs_of_all_Egypt_for_a_time,_ruling_everything_from_the_Axumite_Highlands_to_the_Nile_Delta._Though_the_ancient_kingdom_is_no_more,_broken_by_war_and_internal_conflict,_your_kin_remember_well_your_glorious_past_-_and_the_wrongs_done_them_by_Rome_and_Axum."),
("culture_caucasian_alan","You_are_an_Alan._Your_people,_called_Scyths_by_the_settled_men_of_the_south,_have_ever_been_masters_of_the_great_steppe._But_the_Huns,_who_swept_in_from_the_east_with_arrow_and_fire,_have_brought_much_suffering,_stealing_your_herds_and_richest_hunting_grounds,_extorting_tribute,_taking_slaves_and_forcing_you_back_to_the_foothills_of_the_mountains_and_the_shores_of_the_ocean."),
("culture_armenian","You_are_an_Armenian._Your_people_are_the_descendants_of_the_ancient_kingdoms_of_Urartu_and_Armenia,_a_proud_nation_that_has_stood_at_the_crossroads_of_empires._Once_ruled_by_the_mighty_Arsacid_dynasty,_Armenia_was_divided_between_the_Eastern_Roman_and_Sasanian_Empires._Now,_as_a_vassal_of_the_Sasanians,_your_people_cling_to_their_Christian_faith,_which_was_first_adopted_in_301_AD,_and_to_their_unique_identity._Despite_persecution_and_geopolitical_turmoil,_Armenia_remains_a_land_of_fierce_warriors,_wise_clergy,_and_resilient_families._You_live_in_a_time_when_the_memories_of_Vardan_Mamikonian's_sacrifice_at_Avarayr_inspire_your_people_to_stand_strong_against_any_oppression."),
("culture_jew","You_are_a_Jew._Your_people_are_the_descendants_of_the_ancient_Israelites,_whose_kingdoms_of_Israel_and_Judah_once_flourished_in_the_hills_and_plains_of_the_Holy_Land._Centuries_of_exile,_displacement,_and_empires_have_scattered_your_community_across_the_Mediterranean,_but_their_identity_remains_unshaken._In_Palaestina,_your_people_suffer_under_Roman_rule,_facing_restrictions_and_persecutions._Despite_this,_your_tradition_endures_through_prayer,_study,_and a_tenacious_hope_for_redemption_and_freedom."),
("culture_irish","You_are_an_Irish._Since_the_world_was_made,_your_people_have_ruled_the_chill,_beautiful_island_of_Eriu._Wild_and_free,_you_look_with_contempt_on_your_weak_eastern_neighbours_who_tremble_behind_their_great_walls_and_towers_of_stone,_which_now_stand_abandoned_and_silent."),
("culture_slavic","You_are_a_Slavic."),

("background_slave","Your_parents_were_slaves_and_thus_you_were_born._Your_life_has_been_one_of_hardship_and_suffering._As_a_child,_you_watched_your_family_cruelly_punished_by_the_master_for_any_small_mistake_or_perceived_offense._Nor_did_you_receive_mercy_because_of_your_age._Your_parents_died_young,_as_slaves_usually_do._Determined_to_avoid_the_same_fate,_you_escaped,_leaving_the_place_far_behind."),
("background_freeman","Your_parents_were_freemen,_owners_of_a_smallholding_worked_by_serfs._As_soon_as_you_could_walk,_you_too_were_put_to_work._You_helped_gather_the_harvest,_fetched_water,_fed_the_animals._Though_life_could_be_hard,_it_was_happy:_you_played_and_fought_with_the_other_children,_made_fun_baiting_livestock_and_enjoyed_the_many_cultural_and_religious_festivities_of_your_people."),
("background_noble","Your_parents_were_lesser_nobles,_owners_of_a_small_estate._They_were_proud_of_their_lineage_and_so_you_were_raised._Your_life_was_comfortable,_at_least_compared_with_those_of_the_smallfolk._Once_you_came_of_age,_your_father's_retainers_taught_you_the_use_of_spear,_sword_and_shield._And_you_learned_the_arts_of_tactics,_leadership_and_the_hunt."),

("build_strong","You_are_naturally_sturdy_and_well-built._Your_imposing_physique_makes_you_both_strong_and_intimidating."),
("build_thin","You_are_naturally_lithe_and_agile._Quick_and_nimble_on_your_feet,_you_are_fast_and_graceful."),
("build_weak","Your_are_naturally_weak_and_small._Your_puny_stature_made_you_an_easy_target_for_bullies_growing_up."),
("mind_genius","You_are_blessed_with_rare_intellect._Your_ability_to_learn_and_analyse_gives_you_an_edge_over_others_in_understanding_complex_concepts."),
("mind_shrewd","You_are_sharp_and_shrewd._Life_has_already_taught_you_the_value_of_good_judgement_and_quick_wits."),
("mind_normal","You_are_neither_particularly_mentally_gifted_nor_lacking._You_are_as_ordinary_and_superstitious_as_most_other_people_around_you."),
("mind_dull","Your_mind_is_very_slow._While_you_may_not_be_a_great_thinker,_you_compensate_for_this_with_strength,_beauty_or_sheer_force_of_will."),

("background_religion_chalcedonian", "Your parents believed in Christos and in God, his powerful father. Christos preached equality and love. Yet, the Christians are quarreling about the correct understanging of Christos words and his nature. You and your parents follow the Chalcedonian interpretation that Christos was one hypostasis in two natures. You never understood what this means, but you know that whatever the other Christian sects preaches is wrong."),
("background_religion_arianism", "Your parents believed in Christos and in God, his powerful father. Christos preached equality and love. Yet, the Christians are quarreling about the correct understanging of Christos words and his nature. You and your parents follow the Arian interpretation, which says that Christos, the Son of God, did not always exist but was made before time by God the Father. You never understood what this means, but you know that whatever the other Christian sects preaches is wrong."),
("background_religion_coptic", "Your parents believed in Christos and in God, his powerful father. Christos preached equality and love. Yet, the Christians are quarreling about the correct understanging of Christos words and his nature. You and your parents reject the Chalcedonian interpretation, which says that Christos was one hypostasis in two natures. You never understood what this means, but you know that whatever the other Christian sects preaches is wrong."),
("background_religion_nestorian", "Your parents believed in Christos and in God, his powerful father. Christos preached equality and love. Yet, the Christians are quarreling about the correct understanging of Christos words and his nature. You and your parents follow the teachings of Nestorius, the Patriarch of Constantinople, who emphasized a distinction between Christ's divine and human natures. You never understood what this means, but you know that whatever the other Christian sects preaches is wrong."),
("background_religion_donatist", "Your parents believed in Christos and in God, his powerful father. Christos preached equality and love. You and you parents are rigorists, and hold the belief that the sacraments done by lapsed priests and bishops are invalid, in contrast with the other churches that do not believe the same. You never understood what this means, but you know that whatever the other Christian sects preaches is wrong."),
("background_religion_paganism", "Your parents worshipped the Old Gods, the Gods people worshipped long time ago, before Rome brought all those Eastern cults, first and foremost Christianity, into your home lands. You always listened with fear and excitment the old tales about the creation of the Gods and their tricks."),
("background_religion_roman_paganism", "Your parents believed in the old Roman Gods. You learned that the Gods are arbitrary and fallible as the humans are. Thus you need to make sacrifices to appease them and receive their favor. You always listen with excitement to the old tales of the Illias and the Aeneid."),
("background_religion_zoroastrianism", "Your parents were devout worshippers of Ahura Mazda. You learned about the importance of the four elements, from which the fire is the most important one. Fire and clean water are agents of ritual purity."),
("background_religion_zurvanism", "Your parents were devout worshippers of Zurvan. In contrast with your Mazdaist Zoroastrian brethren, you were taught that Zurvan is the primordial creator, who begot the two twin entities; that of Ahura Mazda, embodying goodness, and Angra Mainyu, embodying evil."),
("background_religion_judaism", "Your parents were devout followers of Yahweh, and maintain the rabbinic traditions and the Mosaic covenant. You and your faithfully wait for the coming Messiah and the restoration of the Temple in Jerusalem."),

("diplo_casus_expired_reparations_accepted","In order to avoid war they decide to accept the demand. A sum of {reg40} siliquae has been paid as tribute."),
("diplo_casus_expired_reparations_refused_war","They refuse the demand and declare war!"),


("wre_description", "Imperator Caesar Iulius Valerius Majorianus Augustus:\
  ^\
  ^You are Majorian, Emperor of the Pars Occidentalis, the western regions of the Roman Empire. Loyal friend of Flavius Aetius, the Roman general who saved the Empire at the Catalaunian Plains defeating Attila, you proclaimed yourself emperor after Burco, a loyal comes, defeated a group of Alamans who were raiding Liguria.\
  ^\
  ^With your power and your soldiers you have now the chance to reclaim the lost provinces in Gallia, Hiberia and Africa. Many lands were lost to the barbarians escaping the Huns: your predecessors failed in the quest, but now it's your turn to restore the glory of Rome. This is the last chance of the Empire, if you fail, there will be no one else to prevent some Germanic tribes, or treacherous foederatus generals, to take Ravenna, Milan or even Rome from you.\
  ^\
  ^\
  ^Majorian will start at war on mutiple fronts: the Burgundians, the Visigoths and the Vandals are all hostile to your power and they occupy some of your richest regions you ought to reconquer for them. Picking Majorian's start, you will have some of the most powerful units in the entire game available in Ravenna to recruit, as well as your ordinary and efficent regular roman soldiers.\
  ^\
  ^Make sure to have enough gold to fill your coffers to pay your troops and make sure your many generals are happy with the land and military promotions you give them. Proceed carefully, if the germanic invaders manage to weaken you, more barbarian states will declare war on you, trying to invade Italy.\
  ^\
  ^Your northern provinces, controlled by Syagrius, are cut off from the main body of your controlled territories, but the Franks could be useful allies in fighting the Burgundians and reconquer the biggest chunk of Gaul. The Visigoths are indeed your toughest adversaries as they recently mangled the small Kingdom of the Suebi in northern Spain: they have no other enemy but you and the rogue bands of bagaudae raiding the mountainous regions of Northern Spain.\
  ^\
  ^The Vandals instead are strong in Carthage and the large amount of cities orbitating around the north-African capital allow their kingdom to store immense amounts of wealth. Although, they are being harassed by the Mauri and other tribes and might become soon an easy target. Better if to pick one enemy at once and do not waste too much manpower and wealth trying to fight them all at the same time: if taken alone, most of those post-roman barbarian kingdoms will be no match for you.\
  ^\
  ^Difficulty: Easy\
  ^\
  ^Starting allies: Salian Franks (tributaries)\
  ^\
  ^Starting enemies: Kingdom of the Visigoths, Kingdom of the Burgundians, Kingdom of the Vandals"),

("ere_description","Imperator Caesar Flavius Valerius Leo Augustus:\
  ^\
  ^You are Leo the First, Emperor of the East and you rule from the mighty and new city of Constantinople, built by the old Emperor himself. The old Aspar believed himself to be the brightest, he was convinced he would have been your master once you became Emperor. Pah! You're better than that, you outsmart him and all the other generals in tactical thought and wisdom... And I do believe it's time to show him who is the true Emperor of the Pars Orientalis.\
  ^However, your internal threats aren't the only enemies you're going to face: the situation in your eastern provinces is worrisome. The King of Kings, the persian Shahanshah, is rallying his troops and is about to attack Edessa, Theodosiopolis or Damascus. Our long story of conflicts with the Persians is old and tormented, but it is finally time to put an end to this and secure our eastern borders and the Caucasus once and for all. Pay also attention to the West, Majorian might need your assistence.\
  ^\
  ^Unlike for the Western Roman Empire, you have one main opponent that, in turn, is way stronger than most of the barbarian kingdoms north of the Danube. Your fortresses in the East are poorly defended and your generals struggle to reach Constantinople from distant provinces such as Egypt. Plan your campaigns carefully and protect your allies, such as the Kingdom of Lazika, from the hordes of the steppes.\
  ^In Egypt, furthermore, the myaphisite subjects of the Empire are upset with your rule and might revolt soon, this might keep some of your generals busy in the south and draw part of your manpower away from the Levant and Armenia. The Sasanid Empire is your equal in terms of economy and size of your army so expect large scale engagements and a long and exhausting conflict for your Eastern borders. Make sure to defeat the Persians on open field and go straight to their capital, Ctesiphon. If you manage to conquer it, the way to the East will be open to you and their other cities will fall easier than expected.\
  ^\
  ^Difficulty: Medium\
  ^\
  ^Starting allies: Kingdom of Lazika (tributaries), Tauri (tributaries)\
  ^\
  ^Starting enemies: Eranshar, Kingdom of Kartli, Huns"),

("visigoth_description","Theodoric II, King of the Visigoths:\
  ^\
  ^You are Theodoric the Second, son of Theodoric the First, the great hero and martyr of the Catalaunian Plains, where he was killed by Attila's forces in battle. You do not forget the blood you shed for the Empire, nor how little they repaid your kin for your sacrifices. There isn't a single gothic male, within your domains, that do not have their knees swollen, their arms wounded and their heads damaged by spears, arrows and stones while serving Rome.\
  ^You remember how your father lost his life fighting for Aetius! And now... Now the new Emperor, Majorian, is coming to reclaim the lands rightfully given to you for your people to settle! You can't tolerate this injustice. You will break Majorian, as you just did with the Suebi in Iberia..\
  ^\
  ^Theodoric the Second benefits from one of the best starts among the barbarian kingdoms in Europe. He has a large domain, comprised of Aquitania and almost whole of Iberia and is at the head of a powerful army. In Tolosa you will have the chance to recruit the Gardingi, one of the strongest cavalry units in the game, as well as your regular gothic troops and indigenous iberian allies.\
  ^Beware Majorian, the Roman Empire is way stronger than you and their armies more professional and better armed: make sure to lay a trap for them and fight them only in tactical advantage or numerical superiority, such as near your cities.\
  ^Make sure to get all the support you can from the Burgundians: the Vandals will hardly help as they are far and already fighting the Mauri. Also, pay a closer look to the Suebi. If Majorian manages to weaken you, they might declare war on you to reclaim their lost land in Spain.\
  ^\
  ^Difficulty: Hard\
  ^\
  ^Starting allies: Kingdom of the Burgundians\
  ^\
  ^Starting enemies: Imperium Romanorum Pars Occidentalis"),

("ostrogoth_description","Valamir, King of the Ostrogoths:\
  ^\
  ^You are Valamir, king of the Eastern Goths, ruler of the Feld, the great plains of the Danube river. Your prowess is known far and wide as you helped your brothers Gepids in freeing your peoples from the yoke of the Huns, few years back. Now you are free, and with many opportunities in front.\
  ^First of all, secure your domains in the great plains of the Danube: the tribes of the Skirii, Heruli, Rugii and the Sarmatians fear you and might attack you soon as members of a newborn, anti-gothic, coalition. The two new emperors, Majorian and Leo, are far and busy with their own fights, but if they will ever stregthen their position be sure: they will come for you. King of the Eastern Goths, saddle your horses and grab your spear, there is much to be done.\
  ^\
  ^Valamis is at the head of the strongest faction in the Danube area, if we do not count the Eastern Roman Empire. This is an interesting start as it allows you to expand quickly against the smaller tribes of Eastern Germans living along the great river. However, beware: your many vassals serving you might soon turn unhappy if you don't grant them land so be quick, strike first, strike hard and force them into obedience.\
  ^You have acess to good quality horsemen and a good number of pannonian Huns that settled there during the time of Attila. This gives you a tactical advantage against your neighbours, make sure to use your army at the best of their possibilities and expand your realm to provide a large income for your tribe.\
  ^\
  ^Difficulty: Medium\
  ^\
  ^Starting allies: None\
  ^\
  ^Starting enemies: None"),

("franks_description","Childeric, King of the Salian Franks:\
  ^\
  ^You are Childeric, king of the Salian Franks. Your dinasty is destined to greatness: you arose from the dark forests of Germania and befriended the Romans that respect you and value you as great allies at the border of Gallia. Your kin valiantly helped against Attila, few years before at the battle of the Catalaunian plains, and now again are called to help the Romans in their struggle as the new emperor, Majorian, is in peril due to the many tribes that swathe through Gaul the years before.\
  ^Mayhaps, in this time of confusion, it will be the time to outshine your ancestors, unite the Frankish tribes and expand your domains at the expense of the other nations surrounding you. The Franks ought to rule, and so they shall.\
  ^\
  ^The Frankish start is, again, a good germanic start for those who seek an interesting challenge without exhausting confrontations against bigger enemies. You will start tied to Majorian's diplomatic stances, but you will soon be able to field a large army to conquer the Ripuarian Franks, subjugate the Frisians and confront both Saxons and Alamans in their own turf.\
  ^Use the first stages of the conflicts against the Burgundians and the Visigoths, while helping Rome, to forge your veteran army and amass spoil of wars as the campaigns you will be engaged in after are going to be wealth consuming. Your army is indeed balanced, as you have acess to a good western germanic roster and quality regional troops as well as the famous Antrustiones. \
  ^\
  ^Difficulty: Medium\
  ^\
  ^Starting allies: Imperium Romanorum Pars Occidentalis\
  ^\
  ^Starting enemies: Visigoths, Burgundians."),

("sassanid_description","Hormizd III, Shahanshah of the Sassanid Empire:\
 ^\
 ^Oh great Shahansha, Hormizd the Third, your power outshines all the other monarchs and your glory is known from Hrwm to Qin. There is no greater empire than yours and no braver warriors than your soldiers. Your many subjects acclaim your power while your enemies fear you, such as the 'Emperor' from Constantinople.\
 ^In the past, when your family was finally recognised as the supreme authority in the realm, the men from the West tried to crush your forces many times but at the end you always managed to prevail. Now, it is finally time to turn your glare West, towards their rich cities and wealthy lands.\
 ^At the same time, it is of outmost importance to regain the lost provinces in the East, captured by the Xun decades before, such as Sogdia or the lands of the Kusans. Your fate is to rule the Earth, oh King of Kings, and with your supreme authority lead our through struggles and victories.\
 ^\
 ^The Sasanid start mirrors the Eastern Roman one. You have one main enemy (untill we add the Iranian Huns next update) that has, more or less, your same power and wealth as well as a strong tributary kingdom in the Caucasus. Your strategy is, of course, to rule in the Levant and in Egypt, taking those lands from the Romans. To do that, you will need your vassals to help you as well the ability to make them support you on large scale campaigns.\
 ^You start with a good economy and with excellent troops recruitable in your cities. Make large use of your horsemen, as the Romans beat you in infantry engagement, and you will make sure to have a great advantage against them. Furthermore, by increasing your piety and relationship with the zoroastrian world, you will be rewarded with champions heavily armed and recruitable in zoroastrian temples.\
 ^\
 ^Difficulty: Easy\
 ^\
 ^Starting allies: Kingdom of Kartli (tributaries)\
 ^\
 ^Starting enemies: Imperium Romanorum Pars Orientalis, Kingdom of Lazika"),

("vandal_description","Gaiseric, King of the Vandals and Alans:\
 ^\
 ^Great King Gaiseric! You, that led us across the pillars of Hercules and gave us a new home: Carthage! The great city of these seas. Locals told us this city was once a great enemy of Rome. Ah, the irony! As now it belongs to us, for whom the eternal city should be turned into ashes. Gaiseric, your realm couldn't be more prosperous: our lands are rich and the other nations pay us well for the wheat our subjects produce! However, the new emperor, Majorian, eyes our golden shores with envy.\
 ^He wants to reconquer Africa and steal it from our very own hands! This cannot be. And what can we say about the Mauri from Altava? Those folks think they can have it all. No. They won't have nothing. The Vandals and the Alans will prevail once more and we will make the Mauri and the Romans bend to our knee. You have the power to do it, king Gaiseric.\
 ^\
 ^The Vandal start is challenging and not adviced for beginners. The Vandals begin with a strong faction and rich fiefs, they have a decent army and a large income that can support a good retinue. However, they immediatly start at war with two factions: the Romano-Mauri of the Kingdom of Altava, which are very close to your faction, and the Western Roman Empire led by Majorian.\
 ^They're both strong opponents, with the Romans being largely superior to you in wealth and power. There are also some minor tribes south of Libya and a rogue band of Austurian kidnapping your peasant parties in Numidia.\
 ^All these things make the Vandal start a quite challenging one. Your best tactic is to immediatly weaken the Romano-Mauri and hope Majorian will delay his campaign to focus on the Visigoths and the Burgundians north. If you manage to reunite North-Africa under a single banner or have the Romano-Mauri become your tributaries, you will  have a chance to resist against Majorian. However, it is no easy businness and will require a campaign of exhausting fights.\
 ^\
 ^Difficulty: Hard\
 ^\
 ^Starting allies: None\
 ^\
 ^Starting enemies: Imperium Romanorum Pars Occidentalis, Kingdom of Altava, Austuriani"),

("iberian_description","Vakhtang, King of the Iberians:\
 ^\
 ^You are King Vakhtang, the supreme ruler of Kartli, Iberia in western chronicles. Your family has come from Persia ages ago to rule over the vast lands at the feet of the Caucasus mountains... And they did wonders! Your realm is rich, but surrounded by daring wolves. The Sasanids claim they have authority over your realm and we, sadly, are not as strong to face them. But this will change soon.\
 ^They are too focused to fight the Romans to care about us... And when the time will come, we will strike. The Kingdom of Lazika, west, rules over lands that are rightfully ours. We have to rally our army and show them who's stronger.\
 ^North of our towns live the Alans and the barbarians of the mountains, as well as the Huns: we have to pay attention to those nations as they are used to raid our settlements at summer. In time, Kartli will rise and you, King Vakhtang, will be the uncontested ruler of the Caucasus.\
 ^\
 ^Kartli starts as a vassal state of the Sasanids. Your diplomacy is strictly tied to the Shahanshah's decision and therefore you will start at war with both the Romans and Lazika. It's your chance to expand west and claim the Kingdom of Lazika for your own.\
 ^However, beware: Lazika is in decline but they can still field a strong army and are defended by their barbarian clientes in the North, such as the Abasgoi, and of course the Romans who keep Lazika as their tributary state. Your roster is solid, but your economy is not.\
 ^Make sure to amass wealth and gold before assaulting the cities in the Colchis. Once secured the Kingdom of Lazika, you will get the chance to look North, in the lands of the Alans. They have been severely weakened by the arrival of the Huns one century before and now live at the feet of the mountains pressured by more hordes North.\
 ^One thing you have to avoid: do not anger the Sasanids as they are far stronger than you and you will need the whole Caucasus on your side to be able to resist them.\
 ^\
 ^Difficulty: Medium\
 ^\
 ^Starting allies: Eranshar (you are their tributaries)\
 ^\
 ^Starting enemies: Kingdom of Lazika, Imperium Romanorum Pars Orientalis"),

("hun_description","Dengizich, King of the Huns:\
 ^\
 ^Dengizich, son of the Great Attila. You are the king of the Huns... But what's left of us now? When your father died, many tribes revolted and left our Empire. Our subject nations of the Gepids, Ostrogoths, Skirii and Rugii too decided to turn against you and even killed your brother! This cannot be. The world will be ruled by us and no one else.\
 ^Dengizich, it's now or never: the time to reclaim your father's domains and to force your subjects into submission. First, the tribes that refuse to rejoin your empire need to be crushed: the Saragurs, Oghurs and Onogurs think you are weak and cannot protect them from the Sabirs. It's time to prove they're wrong.\
 ^After them, the Gepids, west, led the coalition that defeated your brother Ellak at the battle of Nedao, where he lost his life. It's time to avenge him. And when you will finally settle all these unresolved issues with your neighboring nations there will be one left unpaid bill to solve. One with Rome and Constantinople. You will continue what your father started.\
 ^\
 ^The Hunni start is indeed one of the most peculiar and fun starts in the game and mixes challenges with an interesting gameplay. You start with a medium-sized faction and few tributaries, one of which is quite powerful (Alania). Around you there will be several rebel hordes you have to defeat.\
 ^Once the rebellious hordes are dealth with you will have the chance to immediatly expand west and invade the Gepids and possibly the other small polities of the Danube basin. Once your imperium reached a certain extent, you will have the chance to engage with the Eastern Roman Empire and possibly even helps it collapse.\
 ^However, beware: your army is diverse and full of good units, but horse archers aren't easy to use on the battlefield. Their skirmishing behavior is excellent against infantry but makes them an easy target for the enemy cavalry. Make sure to have a composite army with good footmen and heavy horsemen to help your horse archers annihilate your enemy.\
 ^\
 ^Difficulty: Medium/Easy\
 ^\
 ^Starting allies: Alania (your tributaries), Bosporan Kingdom (tributaries)\
 ^\
 ^Starting enemies: Imperium Romanorum Pars Orientalis, Gepids, Sabirs."),

("arthus_description","Ambrosius Aurelianus, King of the Britons:\
 ^\
 ^Ambrosius Aurelianus, last hope of the Britons in this times of great peril. Lead us to victory against the invading forces of Saxons, Angles, Jutes and Frisians coming from the continent to burn our farms, destroy our city and settle with their most terrible kinsmen. We can't let this to happen: rally the men of Britannia and our allies and make them fight against the banner of Rome and Christ once more.\
 ^Terrible enemies are ramming our doors, not only the Germans from beyond the sea but also the Picts from the North aim to conquer our cities and the Scoti from Hibernia are eager to turn us into their slaves. Listen to our plea, Ambrosius, and save us from our enemies. Rome might have abandoned us, but we still hold her dearly in our hearts.\
 ^\
 ^The Romano-Briton start is challenging because you will start at war with several enemies at the same time. They are all weaker and smaller than you, but they can hurt you badly if you don't manage the conflict in the right way. To make things worse, the germanic holdings are still mostly beyond and sea and to reach them will require time and vassals willing to follow you in long distance conflicts.\
 ^Your army is organised according to roman fashion, but you don't have neither the infrastructures nor the wealth to arm and train them the same way Ravenna and Constantinople did. However, you won't lack elite units and good mounted troops as well as regional auxiliary units to support you and it is possible your economy will be good enough to sustain your army.\
 ^Make sure, however, to reconquer the settlements lost to the Germans on the coast: from there they will have hard times campaigning in Britannia and you will be finally safe.\
 ^\
 ^Difficulty: Medium\
 ^\
 ^Starting allies: None\
 ^\
 ^Starting enemies: Saxons, Jutes, Angles, Frisians, Picts, Scoti"),
("aioulf_description","Aioulf, King of the Suebi:\
 ^\
 ^Aioulf, last hope of the Suebi in this times of great peril. Lead us to victory against the traitorous Framta and the Visigoths!\
 ^\
 ^The Suebi start is challenging because you will start at war with several enemies at the same time.\
 ^\
 ^Difficulty: Medium\
 ^\
 ^Starting allies: None\
 ^\
 ^Starting enemies: Visigoths, Framta's Suebi"),

#madsci VC sea battle
  ("quick_battle_troop_cam", "Watch the AI play the battle out. The camera uses the standard movement and rotation controls, plus F for up and V for down, +/- for zoom, Q to toggle follow terrain, numpad for game speed, mouse wheel for camera speed, arrow key rotation, Y to toggle invert y-axis, and R to toggle rotate-before-pan."),
  ("strategy_cam", "This camera follows the player. One may increase distance with the F key and reduce it with the V key. +/- for zoom, numpad for game speed (when cheats are enabled), and mouse wheel for camera speed."),
  ("ship_tutorial_0", "In this tutorial, you will learn how to control a ship. Take your time to learn how to command your crew, so you will be able keep a cool head in fast-developing naval battles.^^(Click * K * to continue.)"),
  ("ship_tutorial_1", "In a naval battle, it often helps to get an overview.^^(Click * BACKSPACE * to get an overview.)"),
  ("ship_tutorial_2", "You can look around by moving the mouse or get your perspective back on your ship by clicking * BACKSPACE * again.^^(Click * K * if you want to continue.)"),
  ("ship_tutorial_3", "If you want to make your ship move, you can give the crew the command to row. The more crew you have, the more speed you will gain through rowing.^^You can give commands to row forward, to row fast forward, to stay or to row backwards. Click the * UP * or the * DOWN * arrow key to switch between these commands.^^Your current command is represented by the arrows above and below the representation of your ship in the upper right corner of your display. Try to give different rowing commands!"),
  ("ship_tutorial_4", "If you want to make your ship move, you can give the crew the command to row. The more crew you have, the more speed you will gain through rowing.^^You can give commands to row forward, to row fast forward, to stay or to row backwards. Click the * UP * or the * DOWN * arrow key to switch between these commands.^^Your current command is represented by the arrows above and below the representation of your ship in the upper right corner of your display. Try to give different rowing commands!^^(Click * K * if you want to continue.)"),
  ("ship_tutorial_5", "If you want to direct your ship, you can give a command to the helmsmen. You can give commands to row straight, starboard, hard starboard, port or hard port. Click the * LEFT * or the * RIGHT * arrow key to switch between these commands.^^Your current command is represented by the arrows to the right and left of the representation of your ship in the upper right corner of your display. Try to give different helmsman commands!"),
  ("ship_tutorial_6", "If you want to direct your ship, you can give a command to the helmsmen. You can give commands to row straight, starboard, hard starboard, port or hard port. Click the * LEFT * or the * RIGHT * arrow key to switch between these commands.^^Your current command is represented by the arrows to the right and left of the representation of your ship in the upper right corner of your display. Try to give different helmsman commands!^^(Click * K * if you want to continue.)"),
  ("ship_tutorial_7", "If there is favourable wind, you can give the command to set the sail, but if you are in a head wind, you should give the command to reef the sail. Click * ENTER * to toggle between these commands. Your current command is represented by the sail of the representation of your ship in the upper right corner of your display. Your current position to the wind is represented by the blue flag. Try to give the command to set or reef the sail!"),
  ("ship_tutorial_8", "If there is favourable wind, you can give the command to set the sail, but if you are in a head wind, you should give the command to reef the sail. Click * ENTER * to toggle between these commands. Your current command is represented by the sail of the representation of your ship in the upper right corner of your display. Your current position to the wind is represented by the blue flag. Try to give the command to set or reef the sail!^^(Click * K * if you want to continue.)"),
  ("ship_tutorial_9", "Now you know the basic commands you need to control a ship. If you want to board an enemy ship in a naval battle, just try to catch it, and your crew will do the rest.^^For now, take your time to try out your ship. When you are done, land your ship at the beach where you started!"),
  ### PHAIAK chief begin
  ("busse", "Busse"),
  ("skeid", "Skeid"),
  ("karvi", "Iusoria"),
  ("snekkja", "Snekkja"),
  ("knorr", "Knorr"),
  ("byrding", "Byrding"),

  ("ship_wood_1", "Oak"),
  ("ship_wood_2", "Pine"),
  ("ship_wood_3", "Ash"),

  ("ship_name_1", "Tranann"),
  ("ship_name_2", "Ormurin Skamma"),
  ("ship_name_3", "Ormurin Langi"),
  ("ship_name_4", "Visundur"),
  ("ship_name_5", "Ognabrandur"),
  ("ship_name_6", "Olavssud"),
  ("ship_name_7", "Langfredag"),
  ("ship_name_8", "Kross-Sud"),
  ("ship_name_9", "Mariusud"),
  ("ship_name_10", "Kristsud"),
  ("ship_name_11", "Barden"),
  ("ship_name_12", "Barufakr"),
  ("ship_name_13", "Ormen"),
  ("ship_name_14", "Bokesuden"),
  ("ship_name_15", "Reinen"),
  ("ship_name_16", "Unnblakkr"),
  ("ship_name_17", "Seglhundr"),
  ("ship_name_18", "Bortlvalr"),
  ("ship_name_19", "Fjardlinni"),
  ("ship_name_20", "Svalbardi"),
  ("ship_name_21", "Fiardakolla"),
  ("ship_name_22", "Alptr"),
  ("ship_name_23", "Saeulfr"),
  ("ship_names_end", "ship_names_end"),

  ("cant_set_sail", "You can't set sail. Your ships don't have room for {reg3} of your men."),
  ("regnum_suevorum", "Regnum Suevorum"),
  ("mercenary", "Mercenary"),
  ("im_angry", "{playername}, I am not happy about how things are going."),
  ("jewish_riot", "The Jews are rioting!"),
  ("armenian_riot", "The Armenians are rioting!"),
("after_to_the_fall_of_s10_your_faithful_vassal_s9_has_invited_your_court_to_s11_nolord", "After to the loss of {s10}, your court will relocate to {s11}."),
  ("as_the_marshal_i_am_assembling_the_army_of_the_realm", "As the marshal, I am assembling the army of the realm."),
  ("as_the_marshal_i_am_assembling_the_army_of_the_realm_and_travel_to_lands_near_s10_to_inform_more_vassals", "As the marshal, I am assembling the army of the realm. We are travelling to the region of {s10} to inform more vassals."),
  ("as_the_marshal_i_am_leading_the_siege", "As the marshal, I am leading the siege."),
  ("as_the_marshal_i_am_leading_our_raid", "As the marshal, I am leading our raid."),
  ("as_the_marshal_i_am_leading_our_forces_in_search_of_the_enemy", "As the marshal, I am leading our forces in search of the enemy."),
  ("as_the_marshal_i_am_leading_our_forces_to_engage_the_enemy_in_battle", "As the marshal, I am leading our forces to engage the enemy in battle."),

#description string start
("desc_kingdom_1", "the Western Roman Empire is in a state of severe decline, both politically and territorially. The once-mighty empire has fractured, beset by internal instability, barbarian invasions, and a loss of central authority. This period is marked by the rise of powerful military generals and external pressures that diminish the empire's influence over its remaining territories."),

("desc_kingdom_2", "The Eastern Roman Empire, also known as the Byzantine Empire, is relatively stable compared to the Western Roman Empire. While the West is rapidly disintegrating, the Eastern Empire is consolidating its power and resources under the leadership of a new emperor, Leo I."),

("desc_kingdom_3", "The Balthorum are the ruling dynasty of the Visigoths, one of the most prominent Germanic tribes of the Migration Period."),

("desc_kingdom_4", "The Amalorum are the ruling dynasty of the Ostrogoths, one of the most prominent Gothic groups of the Migration Period."),

("desc_kingdom_5", "The Picts trace their origins back to ancient Celtic tribes. They have a strong warrior culture and are organized into a confederation of tribes, each led by a king or tribal chieftain, with loose alliances between them."),

("desc_kingdom_6", "Empire of the Iranians face many threats and dangers. Hephthalites are raiding the Eastern parts of the empire frequently, the transition of power from Yazdegerd II to current ruler Hormizd III was not a smooth and open wounds yet exist, the disputes with Rome over Armenia are still fresh in memory, and droughts ravage the empire. Current ruler also has his brother Peroz to watch out. Zoroastrian faith is the ruling religion in the empire but particulary in the western portions the relationship between Christians is strained."),

("desc_kingdom_7", "The Salii are one of the many tribes that make up the Franks, a Germanic group that inhabits areas along the Lower Rhine and northern Gaul."),

("desc_kingdom_8", "The Suevi Kingdom is a Germanic kingdom established in the northwest of the Iberian Peninsula. The Suevi had originally been pagan, but they converted to Christianity earlier than many other Germanic peoples."),

("desc_kingdom_9", "The Kingdom of Burgundy is a Germanic kingdom established within the collapsing Western Roman Empire. The Burgundians have transitioned from being a migratory tribe to rulers of a stable kingdom, blending Roman and Germanic traditions."),

("desc_kingdom_10", "The Alemmani are a Germanic tribal confederation. They are primarily agrarian but also engage in raiding and warfare, which is central to their economy and society."),

("desc_kingdom_11", "The Gepids are a significant force in the post-Roman world, playing a key role in the shifting balance of power."),

("desc_kingdom_12", "The Saxons are one of the Germanic tribes migrating and settling in Britain. Like other Germanic tribes, they migrated westward following the decline of Roman influence in northern Europe, seeking fertile land and opportunities for settlement."),

("desc_kingdom_13", "The Roman-Britons are a people in transition, living in the power vacuum created by the Roman withdrawal from Britain in 410 AD."),

("desc_kingdom_14", "The Rugii are a tribe of East Germanic origin, closely related to other tribes like the Gepids and Goths. They are one of many Germanic peoples involved in the shifting power dynamics instigated by the decline of the Western Roman Empire."),

("desc_kingdom_15", "The Vandals are a prominent Germanic tribe with a reputation for warrior strength and seafaring expertise. Under Gaiseric, the Vandals have established a powerful kingdom in North Africa. Gaiseric is particularly infamous for sacking Rome in 455 AD, a blow to the Western Roman Empire that weakened its authority and prestige"),

("desc_kingdom_16", "Kartli is a small but strategically significant state caught between two powerful empires: the Eastern Roman Empire to the west and the Sasanian Empire to the east."),

("desc_kingdom_17", "The Langobardi are a Germanic tribe from the region of southern Scandinavia who began migrating southward in the 4th and 5th centuries, seeking more fertile lands and opportunities for expansion."),

("desc_kingdom_18", "The Thuringians are a Germanic tribe that migrated from regions to the north and settled in central and eastern Germania."),

("desc_kingdom_19", "The Jutes are a Germanic tribe known for their maritime skills, trade, and ongoing conflicts with both the native Britons and other Germanic tribes."),

("desc_kingdom_20", "The Ripurians are a Germanic tribe living in northeastern Gaul."),

("desc_kingdom_21", "The Scirii are a Germanic tribe closely associated with the Ostrogoths and other Germanic tribes, playing a role in the fragmentation and reshaping of power in the region following the fall of Roman dominance."),

("desc_kingdom_22", "Mauretania was Romanized during the early Imperial period but has retained a strong Berber cultural influence."),

("desc_kingdom_23", "Following Attila's death, the Hunni empire has rapidly fragmented due to internal rivalries, external pressures, and the inability of his successors to maintain unity."),
("desc_kingdom_24", "Lazica is a small but strategically significant state caught between two powerful empires: the Eastern Roman Empire to the west and the Sasanian Empire to the east."),

("desc_kingdom_25", "Nobadia is a Nubian kingdom. It has an important role in the region due to its strategic position along the Nile River."),

("desc_kingdom_26", "The Blemmyae are a desert-dwelling people from Nubia, an area south of ancient Egypt."),

("desc_kingdom_27", "Alania is the remnants of a larger Alan confederation that has not migrated westward into Europe. They have made North Caucasus region and neighboring areas their abode, where they maintain a semi-nomadic lifestyle."),

("desc_kingdom_28", "The king of Arran, Vache II, relative to the Shahanshah, raised his armies and is now challenging the Shahanshah in order to contest his authority."),

("desc_kingdom_29", "The Angles are a Germanic tribe originating from the Angeln region. Their trajectory during this time is closely tied to the broader migrations of Germanic tribes into Britain."),

("desc_kingdom_30", "The Suevi Kingdom is a Germanic kingdom established in the northwest of the Iberian Peninsula. The Suevi had originally been pagan, but they converted to Christianity earlier than many other Germanic peoples."),

("desc_kingdom_31", "The Armenians are an ancient people."),
("desc_kingdom_32", "'Scoti' is the name given to raiders and settlers coming from the Irish coast during Late Antiquity by Roman sources."),
("desc_kingdom_33", "The Sporoi are an obscure tribe that are considered the precursor of the Antes and Sklaveni. They live along the course of the Dnieper and for long time they have been subjects of Goths and Huns. Now free, the Sporoi's descendants are about to change the shape of Europe."),
("desc_kingdom_34", "The Vistula Venedi are a tribe, or confederacy of tribes and clans, of uncertain ethnic background living along the eastern shores of the Vistula."),

("desc_rebel_kingdom_1", "The rebels fight for their freedom."),
("desc_rebel_kingdom_2", "The rebels fight for their freedom."),
("desc_rebel_kingdom_3", "The rebels fight for their freedom."),

("desc_minor_aestii", "The Aestii are a group of tribes of likely Baltic language who live along the eastern shores of the Baltic Sea as well as part of Eastern Pomerania. The name 'Aestii' is widely reported since ancient times and during the Migration Era they consist of several tribes who were never united under one single ruler."),

("desc_minor_garamantians", "The Garamantes are a berber civilization living in southern Libya. Known by the Romans since their first expansion in North Africa, they represent a powerful polity. Their capital, Garama, is an important trading centre that connects North Africa, and therefore Europe, to the Subsaharan civilizations. The Garamantes are well known as farmers but occasionally wage war against the Roman Empire."),

("desc_minor_dani", "The Dani are a Germanic tribe living in the islands of Denmark and southern Sweden."),

("desc_minor_mordens", "The Mordens are a tribal union of uncertain origins."),

# ("desc_minor_sporoi", "Living in the forest-steppe area of Ukraine, the Sporoi (the many) live in their villages. Former subjects of the Goths, Sarmatians and Huns, they are now free from their yoke and about to change the cultural shape of Europe forever."),

("desc_minor_bosphoran", "The Bosporan Kingdom is an ancient polity formed by Greek milesian settlers in the 5th century BCE. During the centuries that separate its foundation from the decline, the Bosporan Kingdom was the northernmost Hellenistic state and the one that was more influenced by the peoples and tribes living in the steppes, in the Maeotian swamps and on the shores of the sea. The results were, since the beginning of the Common Era, of a material culture that went through a strong process of sarmatisation as it is clearly visible by the names of the rulers and the customs of the deceased displayed on their funerary stelae. The kingdom became client of the Roman Empire around the beginning of the 1st CE and continued its existence prospering and by being the gates of the Mediterranean world to the steppes and the Forest Belt. Able to exert a considerable influence over its neighbors, the Bosporan Kingdom begun its decline in the 3rd century, at the arrival of the Goths and the westward expansion of the Alans from the Caucasus and the Pontic Caspian steppes."),

("desc_minor_abagasians", "The Abasgians are an indigenous Caucasian tribe living south-west of the Caucasus. They have ties to the Georgian polity of Lazika to which they pay tribute. However, Lazika's control over the warlike tribes living between the Caucasus mountains and the Black Sea shore is always very feeble as Lazika has to face revolts and serious threats from mountain tribes such as the Suani, neighbours to the Abasgians."),

("desc_minor_tauri", "The Tauri, or Tauroscythae, are known since ancient times to have lived in the area called Taurica in southern Crimea. They are considered indigenous, heavily influenced by the Scythians in their customs. They are known as pirates and robbers and are currently a protectorate of the Imperium Romanorum Pars Orientalis."),

("desc_minor_augundzi", "The Augandzi are a Germanic tribe living in Norway, probably near today's Agder fylke. The Augandzi are ruled by Svipdagr, the nemesis of the Danir king Garmr."),

("desc_minor_vidivarii", "On the shore of Ocean, where the floods of the river Vistula empty from three mouths, the Vidivarii dwell, a people gathered out of various tribes."),

("desc_minor_frisians", "The Frisii are a Germanic tribe living along the coast of the low-lying marshlands. They are mentioned by Latin sources from the earliest Roman presence and contacts with the tribe of the area, and in the past they even managed to wage succesful wars against the Roman Empire. However, the gradual worsening of the conditions of the marshes and coasts where they live in has forced many of them to migrate to Britain or fall under the influence of the Franks."),

("desc_minor_vascones", "Defined by Latin sources as 'latrones' (brigands), the Vascones, similarly to the Gallaeci, are nothing but former disgruntled roman provincials who, after the loss of Hispania at the beginning of the 5th century, had no choice but to self-govern themselves. This has led in a slow but progressive abandonment of many Roman cities and the reappearance of castra built on top of the ruins of iron age fortifications."),

("desc_minor_gallaeci", "The loss of Hispania by the Roman authority has forced many former Roman provincials, especially in the harsh regions of northern Hispania, to take up arms and resist the Germanic invaders with their own forces, this is well recorded by the Christian bishop Hydatius in his chronicle. The aristocracy of the local provincials have started reoccupying iron age castrums by their own initiative, as a display of wealth and power, and this has led to a political and military problem for the Visigothic and Suebi monarchs."),

# ("desc_minor_venedi", "The Vistula Venedi are a tribe, or confederacy of tribes and clans, of uncertain ethnic background living along the eastern shores of the Vistula."),

("desc_minor_saraguroi", "The Saraguroi are a nomadic tribe. They originated from Central Asian steppes, later migrating to the Pontic–Caspian steppe. Priscus, a Byzantine historian, mentions that the Saraguroi, along with other tribes, sought protection from the Eastern Roman Empire after being driven from their homeland by the Sabiroi."),

("desc_minor_onoguroi", "The Onoguroi are a nomadic tribal confederation who live in the Pontic–Caspian steppe and the Volga region. Their name, 'Onogur,' is believed to mean 'ten tribes,' reflecting their tribal structure."),

("desc_minor_kutriguroi", "The Kutriguroi are a nomadic tribal confederation that emerged in the Eurasian steppes. As nomadic horsemen, the Kutriguroi were skilled warriors, particularly adept in mounted archery and steppe warfare. Their society was organized around tribal alliances, and their economy depended on a combination of animal husbandry, trade with sedentary peoples, and raiding."),

("desc_minor_sabiroi", "The Sabiroi are a nomadic tribal confederation mentioned by the Byzantine historian Priscus in the 5th century. Priscus describes them as a confederation of Huns who invaded the Eastern Roman Empire during the reign of Emperor Theodosius II."),

("desc_minor_valentia", "The Regnum Valentiae, ruled by Sambida, is a crucial defensive outpost of the Western Roman Empire. Appointed by Aetius in the mid-5th century, Sambida leads his people in guarding the Rhone Valley, a region of strategic importance for the Empire's communication and defense. The Alans settled in Valentia as loyal federates, receiving lands in exchange for their military service. Sambida's leadership is characterized by pragmatism and stability; he maintains a cooperative relationship with Roman officials while preparing his warriors to defend against external threats such as the Burgundians and Visigoths. Though tributary to the Western Roman Empire, Sambida's domain stands as a beacon of Alan resilience and adaptability, blending loyalty to the Empire with the preservation of their distinct cultural identity."),

("desc_minor_aurelianorum", "The Regnum Aurelianorum, led by King Sangiban, stands as a testament to the resilience of this ancient Sarmatian people. Probably descending from Goar, the renowned Alan warlord who crossed the Rhine during the great migrations of the early 5th century, Sangiban commands a proud and independent realm. The Alans were originally invited into Gaul by the Roman general Aetius and granted lands in Aurelianorum to bolster defenses against the Visigoths. Sangiban proved his loyalty and martial prowess at the Battle of the Catalaunian Plains, where he led his Alan cavalry against Attila the Hun. Despite this legacy, his position remains precarious, as Visigothic expansion threatens the stability of his domain."),

("desc_minor_iazyges", "The Iazyges are a Sauromatae tribe that migrated from the Pontic-Caspian steppes to the Danubian plains during the 1st century CE. Settling between the rivers Tissus and Danubius, they carved a reputation as skilled riders and fierce warriors, often clashing with the Roman Empire. However, centuries of conflict and economic stagnation due to the limited pastures of the Danubian plains has led the Iazyges to an inevitable decline. The arrival of the Huns in the region left the Iazyges weakened and reliant on their neighbors for survival. Now caught between the rising power of the Amal dynasty to the west and their alliances with the Rugii, Scirii, and Suebi, they struggle to maintain their independence and warrior traditions."),

("desc_minor_heruli", "The Heruli are a Germanic tribe, originally hailing from Scandinavia, who migrated southward. Initially referred to as 'Scythians' by the Romans, they were instead following the larger Gothic confederation during their migration. Renowned for their agility and prowess as light horsemen, the Heruli are often employed as skilled mercenaries by the Romans, serving in various military campaigns. Currently, under the leadership of their chieftain Visilaus, the Heruli strive to maintain their identity and warrior traditions amidst the shifting powers of the era."),

("desc_adovacrius_host", "Adovacrius, also known as Eadwacer, is the leader of a Saxon warband that has carved a domain for itself in the western reaches of Gaul. Adovacrius and his warriors likely arrived by sea, coming from Britain or northern Germania. With a mixture of pirate raids and opportunistic conquests, they seized lands along the lower Liger, even capturing the city of Juliomagus. ^The Saxon host under Adovacrius wields both fear and ambition, but their position remains precarious. The Franks, under Childeric I, eye their domain with growing concern, while the remnants of Roman authority in the region still attempt to assert control."),

("desc_roman_christians", "Chalcedonian Christians adhere to the doctrines established by the Council of Chalcedon in 451 AD. This council articulated that Jesus Christ exists in two distinct natures-divine and human-united in one person without confusion or division. They face opposition from Copts and from those who follow the Miaphysite branch. The Nestorians who demanded clear distinction of Christ's nature also oppose Chalcedonians."),

("desc_arian_christians", "Arian Christians follow the teachings of Arius, a priest from Alexandria, who asserted that Jesus Christ, the Son of God, was a created being and not co-eternal with God the Father. This belief diverged from the mainstream Christian doctrine of the Trinity, which holds that the Father, Son, and Holy Spirit are of the same substance and co-eternal. Visigoths and Germanic tribes especially follow this branch of Christianity. They are opposed by Nicene Christians, tensions sometimes run high."),

("desc_coptic_christians", "Miaphysite Christians adhere to the Christological position that Jesus Christ has one united nature (miaphysis), both fully divine and fully human. This perspective was heavily influenced by the teachings of Cyril of Alexandria, who emphasized the unity of Christ's nature. Miaphysitism is particularly prominent among certain Christian communities, notably the Coptic Church in Egypt. Following their bishop Cyril, they embrace the Miaphysite stance, especially in response to the controversies surrounding Nestorianism. The primary opposition to Miaphysite Christians comes from those who accepted the Chalcedonian Definition established by the Council of Chalcedon."),

("desc_nestorian_christians", "Nestorian Christians follow the teachings of Nestorius, the Patriarch of Constantinople, who emphasized a distinction between Christ's divine and human natures. Nestorius proposed that Mary should be called 'Christotokos' (Christ-bearer) rather than 'Theotokos' (God-bearer), reflecting his view that the divine and human aspects of Jesus were distinct. This was deemed heretical by the First Council at Ephesus in 431 AD. Following their condemnation, many Nestorian Christians moved eastward, establishing the Church of the East, which became prominent in Persia and later expanded into Asia."),

("desc_donatist_christians", "Donatist Christians are a rigorist sect in North Africa who believe that the sanctity of the church depends on the purity of its members and clergy. They hold that sacraments administered by priests or bishops who had lapsed in faith during persecution (known as 'traditores') are invalid. The primary opposition to Donatism comes from the broader Catholic Church, notably figures like Augustine of Hippo, who argue that the validity of sacraments was not dependent on the moral purity of the clergy administering them.  This schism has led to significant religious and social tensions in North Africa with the Roman authorities often siding against the Donatists. Despite this, the Donatist movement persists."),

("desc_pagans", "Various pagan beliefs and groups yet exist, even after the Christianization of much of Europe. Anglo-Saxon pagans practice a polytheistic belief system venerating deities such as Woden, Thunor, and Tiw. Their spirituality is deeply connected to nature and ancestral traditions. Germanic tribes engage in the worship of gods like Odin and Thor, with rituals centered around natural elements and warrior ethos. These practices could still be found among tribes such as the Goths and Vandals. These faiths often face persecution and mockery from mainstream beliefs and some would like to see them stamped out once and for all."),

("desc_roman_pagans", "Greco-Roman pagans adhere to traditional polytheistic religions of ancient Greece and Rome, worshipping deities such as Zeus (Jupiter), Hera (Juno), and Athena (Minerva). Their beliefs encompass a rich tapestry of myths, rituals, and festivals integral to cultural and civic life and who would wish for Rome to return to the old ways. Christian leaders and emperors have implemented policies to suppress paganism, including the removal of symbols like the Altar of Victory from the Roman Senate and the prohibition of public sacrifices. Despite these efforts, paganism persists, especially in rural areas, leading to a religious landscape where traditional beliefs coexist with the expanding Christian faith."),

("desc_zoroastrians", "Mazdaist Zoroastrians are followers of Zoroastrianism, a monotheistic religion founded by the prophet Zarathustra (Zoroaster) in ancient Persia. They worship Ahura Mazda, the 'Wise Lord,' as the supreme deity and believe in a cosmic dualism between the forces of good (Ahura Mazda) and evil (Angra Mainyu). Central to their faith is the emphasis on individual responsibility to choose righteousness (asha) over deceit (druj), promoting values of truth, order, and moral integrity.  During this period, Zoroastrianism is the state religion of the Sassanian Empire, which often leads to tensions with neighboring regions and emerging religious groups. In regions like Armenia and Caucasian Albania, efforts are made by Sassanian rulers to impose Zoroastrianism, leading to conflicts with Christian populations who resist conversion."),

("desc_zurvanism", "Zurvanite Zoroastrians are devout to a branch of Zoroastrianism known as Zurvanism, which posits Zurvan, the deity of infinite time and space, as the primordial creator. This belief system proposes that Zurvan begots twin entities: Ahura Mazda, representing good, and Angra Mainyu, embodying evil. This interpretation introduced a monist perspective, differing from the traditional Zoroastrian dualism that emphasizes a clear distinction between good and evil forces. It faces opposition from orthodox Zoroastrians who view the Zurvanite interpretation as a deviation from established teachings. The orthodox faction maintains the traditional dualistic framework, emphasizing the independent and opposing nature of Ahura Mazda and Angra Mainyu."),

("desc_jews", "Judaism is a monotheistic religion centered on the belief in one transcendent God who revealed Himself to figures like Abraham and Moses. Jewish religious life is guided by Scriptures and rabbinic traditions, emphasizing adherence to the Mosaic covenant. They hold to the belief in a coming Messiah, a future anointed king who would restore Israel, rebuild the Temple in Jerusalem, and bring peace and justice to the world. The majority of Jews are now living in diaspora, with significant populations in the east as well in places like Alexandria, Babylon and Persia."),
#description strings end

("generic_lord_intro", "I am {s10}."),
#utility for skill names
]+[
("skl_"+skills[x][0], skills[x][1]) for x in range(0, len(skills))]
