# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character("Narrator", color="#00ff00")
define dragon = Character("Dragon")
define villager = Character("Villager")
define village_girl = Character("Village girl")
define blacksmith = Character("Blacksmith")
define thief = Character("Thief")
define dragon = Character("Dragon")


label start:
  # Define initial variables
  $ has_dragon = False
  $ took_gold = False
  $ talked_to_girl = False
  $ talked_to_blacksmith = False
  
  scene forest
  narrator "You are hiking around mountains, on your way to the next adventure."
  scene forest dragon
  menu:
    "Oh no, is that a dragon?!":
      $ ignored = True
  
  menu:
    "I'll fight it, show it who's boss!":
      jump forest_fight_dragon
    "Maybe if I feed him my leftovers from lunch, he'll become my friend...":
      jump forest_befriend_dragon
    "It's probably best if I just go back the other way...":
      jump first_go_to_village
  return

label forest_fight_dragon:
  scene forest fight
  dragon "{i}dragon noises{/i}"
  scene black
  narrator "Unsurprisingly, an unarmed human was no match for a fierce dragon."
  narrator "Better luck next time, adventurer."
  return
  
label forest_befriend_dragon:
  scene forest food
  dragon "{i}intrigued dragon noises{/i}"
  scene forest
  show dragon
  $ has_dragon = True
  dragon "{i}happy dragon noises{/i}"
  
  menu:
    "Hey, that worked! I guess I have a new friend now.":
      $ ignored = True
  
  menu:
    "Let's continue further towards the mountains!":
      show dragon-small onlayer screens:
        xalign 0.0
        yalign 1.0
      jump mountainside_trail
    "Let's turn around and go the other way anyway.":
      show dragon-small onlayer screens:
        xalign 0.0
        yalign 1.0
      jump first_go_to_village
  return
  
label mountainside_trail:
  scene mountainside
  menu:
    "The mountains sure are pretty! Let's continue.":
      $ ignored = True

  scene cave entrance
  menu:
    "Huh, I didn't know there was a cave hiding here.":
      $ ignored = True

  menu:
    "Let's go explore it!":
      jump first_cave_appearance
    "It's probably best if we just continue.":
      jump first_go_to_village
  return
  
label first_cave_appearance:
  scene cave gold
  narrator "You find some bags of gold in the cave."
  narrator "They do not appear to belong to anyone, but it might not be a wise decision to just take them either."

  menu:
    "We should leave the bags alone and get out of here!":
      jump leave_first_cave
    "Finders keepers! This is my gold now!":
      $ took_gold = True
      scene cave
      show gold onlayer screens:
        xalign 1.0
        yalign 1.0
      menu:
        "Let's get going before somebody finds us!":
          jump leave_first_cave
  return
  
label leave_first_cave:
  scene mountainside
  narrator "The trail leads you further away from the cave, towards the village."
  jump first_go_to_village

label first_go_to_village:
  scene village
  narrator "You've arrived at the village."
  scene village villager
  show villager
  villager "Oh adventurer! Can you please help us?"
  villager "Thieves raided our village earlier and have taken most of the village's gold!"
  villager "We will not be able to continue our way of life without our incomes or savings and really need your help in recovering the gold!"
  if has_dragon:
    villager "I'm sure this dragon of yours could help you retrieve the gold!"
  
  if took_gold:
    menu:
      "Oh, I actually just found all this gold in a cave! Is this yours?":
        jump return_gold
      "Sorry, I can't help you.":
        jump disagree
  menu:
    "Oh my, I'll do whatever I can to help!":
      jump agree
    "Sorry, I can't help you.":
      jump disagree
  return
  
label agree:
  villager "We really appreciate you willing to aid us in this time of need."
  villager "We will be willing to provide you with whatever you need to take on those awful thieves!"
  jump ask_around_village
  
label ask_around_village:
  scene village
  if talked_to_girl and talked_to_blacksmith:
    jump talked_to_everyone

  menu:
    "Let's go talk to the girl over there." if not talked_to_girl:
        jump village_girl_chat
    "Let's see if the blacksmith can help us." if not talked_to_blacksmith:
      jump blacksmith_chat
  return
  
label village_girl_chat:
  scene village girl
  show girl
  village_girl "Hiya Adventurer!"
  village_girl "Are you here to help us get our gold back from the mean thieves?"
      
  menu: 
    "Yes! Do you have any more information about them?":
      # this is the only option so we'll just continue here, but it wants to have something in here, so let's just set a variable
      $ ignored = True
    
  village_girl "Absolutely!"
  village_girl "While out in the forest I've spotted them sneaking around by the mountains mutliple times!"
  village_girl "I'm just too scared to go after them so I don't know what they're doing there."
  village_girl "I hope this helps though!"
      
  menu:
    "That's very helpful, thanks!":
      $ ignored = True
  
  $ talked_to_girl = True
  jump ask_around_village
  
label blacksmith_chat:
  scene village blacksmith
  show blacksmith
  blacksmith "Why hello there Adventurer, what brings you here?"
  
  menu: 
    "I'm looking for some equipment to get your gold back from the thieves.":
      $ ignored = True
  blacksmith "Oh really? That is wonderful news! Thank you so much for your assistance!"
  blacksmith "I have a spare sword and some armor I would be happy to lend you."
  menu:
    "That would be very helpful, thank you!":
      $ ignored = True
  
  $ talked_to_blacksmith = True
  jump ask_around_village
  
label talked_to_everyone:
  menu:
    "Now that we are all geared up, let's go find the gold!":
      jump head_to_cave
  return
  
label head_to_cave:
  scene mountainside
  narrator "You continue towards the cave entrance."
  scene cave entrance
  show thief-angry
  thief "Hey you there!"
  thief "What do you think you are doing in these parts? This is my mountain!"
  menu:
    "I'm here looking for gold that was stolen from the villagers!":
       $ ignored = True
  thief "Well well well, you tried to retrieve some stolen items..."
  hide thief-angry
  show thief
  if has_dragon:
    thief "only for your items and your little pet to end up stolen as well!"
  else:
    thief "only for your items to end up stolen as well!"
  menu:
    "Over my dead body!":
      $ignored = True
  
  scene black
  pause(3)
  scene cave entrance
  show thief-injured
  thief "Fine, fine, you win! Please don't hurt me any more!"
  hide thief-injured
  pause(2)
  jump cave_after_fight

label cave_after_fight:
  scene cave gold
  narrator "You have found the missing bags of gold!"
  scene cave
  show gold onlayer screens:
    xalign 1.0
    yalign 1.0
  pause(3)
  jump village_return_from_mountain
  
label village_return_from_mountain:
  scene village
  pause(2)
  scene village villager
  show villager
  villager "You have returned Adventurer! Where you able to find any of our missing gold?"
  menu:
    "Yes, I did! Here you go!":
      $ignored = True
  hide gold onlayer screens
  villager "Oh thank you so much, Adventurer!"
  villager "On behalf of the whole village, thank you so much for getting our gold back!"
  scene village
  pause(2)
  narrator "With their gold back, the village was able to continue their day to day life."
  narrator "The thief was never seen near the village again."
  narrator "After helping the villagers get their gold back, you feel very accomplished with the good deed."
  narrator "Throughout the rest of your travels, whenever someone else asks for help you go and try to aid them if you can."
  scene black
  pause(5)
  return
  
label disagree:
  villager "Oh that's perfectly understandable. Sorry to bother you!"
  jump disagree_left_village
  return

label disagree_left_village:
  scene mountainside
  pause(5)
  if took_gold:
    show thief-angry
    thief "Hey! What do you think you're doing?!"
    thief "That's my bags of gold! I stole them myself!"
    thief "You're going to pay for that!"
    scene black
    narrator "Your adventure has come to an unfortunate end."
  else:
    show thief
    thief "Well well well, what do we have here?"
    thief "An adventurer?"
    thief "You probably shouldn't be here on your own, there are dangers lurking in the mountains..."
    thief "Especially thieves like myself!"
    #gets knocked out and taken to the cave
    scene black
    if has_dragon:
      jump disagree_cave
    else:
      jump disagree_cave_end
  return
  
label disagree_cave_end:  
  scene black
  pause(2)
  narrator "You slowly wake up."
  scene cave gold
  menu:
    "I better escape before the thief returns!":
      $ ignore = True
  "" "{i}You are unable to break free.{/i}"
  show thief
  thief "Oh ho think we can escape do we?"
  thief "You are not going anywhere!"
  scene black
  narrator "And so your adventure has unfortunately come to an end."
  return 
  
  
label disagree_cave:
  scene black
  narrator "You slowly wake up."
  scene cave gold
  menu:
    "We need to try to escape!":
      $ ignore = True
  "After a moment of struggling, your dragon comes over and bites through the ropes, allowing you both to escape."
  menu: 
    "Those bags look like they contain the villagers' gold!":
       $ ignore = True
  menu:
    "I'll take them for myself, just to show the thief who's boss!":
      jump disagree_steal_gold
    "We don't have time for that, we need to get out of here immediately!":
      jump disagree_leave_gold
    "Let's take them to the village.":
      jump disagree_change_heart
  return
  
label disagree_steal_gold:
  scene forest
  show gold onlayer screens:
    xalign 1.0
    yalign 1.0
  narrator "After taking the gold and escaping from the cave, the village is never able to recover the stolen gold."
  narrator "Without their life savings, they struggle to keep the village running."
  narrator "Since you and your dragon now have quite some wealth to your names, you are able to travel and live without worries..."
  narrator "but you always have to keep watch because your wealth has made {b}you{/b} the target of many a thief."
  return
  
label disagree_leave_gold:
  scene forest
  narrator "You and your dragon escaped without running into the thief."
  narrator "Another Adventurer later came along and recovered the village's stolen gold."
  narrator "The village was eventually able to fully recover and get back to normal."
  narrator "You and your dragon friend go off and explore many new areas together, glad you have each other."
  return
  
label disagree_change_heart:
  show gold onlayer screens:
    xalign 1.0
    yalign 1.0
  scene village
  pause(2)
  scene village villager
  show villager
  villager "Adventurer? What are you doing back here?"
  villager "I thought you said you were just passing through and had already left this place!"
  menu:
    "I was going to leave, but I think I stumbled upon your lost gold.":
       $ ignore = True
  villager "The missing gold!"
  hide gold onlayer screens
  villager "I do not know how you found this, but you have no idea how much this means to all of us!"
  villager "Thank you so much for returning this to us!"
  menu:
    "Oh don't mention it, it was no problem at all!":
      $ ignore = True
  scene village
  pause(2)
  narrator "With their gold back, the village was able to continue their day to day life."
  narrator "The thief was never seen near the village again."
  narrator "After helping the villagers get their gold back, you feel very accomplished with the good deed."
  narrator "Throughout the rest of your travels, whenever someone else asks for help you go and try to aid them if you can."
  return
  
label return_gold:
  villager "Oh my! Yes, that is our gold! Thank you so much!"
  menu:
    "Here you go!":
      hide gold onlayer screens
  villager "Thank you again so much!"
  narrator "Everyone lived happily ever after. The end."
  return