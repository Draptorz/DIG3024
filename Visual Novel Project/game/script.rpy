# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character("Narrator", color="#00ff00")
define dragon = Character("Dragon")
define villager = Character("Villager")
define village_girl = Character("Village girl")
define blacksmith = Character("Blacksmith")
define thief = Character("Thief")


label start:
  # Define initial variables
  $ has_dragon = False
  $ stole_gold = False
  $ talked_to_girl = False
  $ talked_to_blacksmith = False
  
  scene black
  narrator "You wake up."
  scene forest dragon
  narrator "What's that? A dragon?!"
  
  menu:
    "Fight it":
      jump forest_fight_dragon
    "Befriend it":
      jump forest_befriend_dragon
    "Go the other way":
      jump first_go_to_village
  return

label forest_fight_dragon:
  scene black
  narrator "You're fighting the dragon"
  narrator "You lose the fight. Game Over."
  return
  
label forest_befriend_dragon:
  narrator "You're befriending the dragon"
  scene forest
  show dragon
  $ has_dragon = True
  narrator "You now have a new friend! Where shall you both start adventuring to together?"
  
  menu:
    "Head deeper into the forest":
      jump mountainside_trail
    "Go the other way":
      jump first_go_to_village
    
  return
  
label mountainside_trail:
  scene mountainside
  narrator "as you both explore the scenery, you stumble upon a cave entrance that your new dragon friend seems curious about. What should you both do?"
  
  menu:
    "Follow the dragon into the cave.":
      jump first_cave_appearance
    "Tell the dragon not now and continue down the path":
      jump first_go_to_village
  return
  
label first_cave_appearance:
  scene cave
  narrator "There's some hidden bags of gold in here! They do not appear to belong to anyone, but it might not be a wise decision to just take them either."

  menu:
    "We should leave the bags alone and get out of here!":
      jump leave_first_cave
    "This gold belongs to someone and that someone is me now!":
      jump leave_first_cave_with_gold
  return
  
label leave_first_cave:
  scene mountainside
  narrator "after leaving the cave, you and the dragon decide to continue heading down the trail."
  jump first_go_to_village

label first_go_to_village:
  narrator "You're going to the village"
  scene village
  villager "Oh adventurer! Can you please help us? Thieves raided our village earlier and have taken most of the villages gold! We will not be able to continue our way of life without our incomes or savings and really need your help in recovering the gold!"
  if has_dragon:
    villager "Also, nice dragon!"
  
  menu:
    "Agree to help retrieve the gold":
      jump agree
    "Tell them sorry you are not able to help":
      jump disagree
  return
  
label agree:
  villager "We really appreciate you willing to aid us in this time of need. We will be willing to provide you with whatever you need to take on those awful thieves!"
  jump ask_around_village
  
label ask_around_village:
  if talked_to_girl and talked_to_blacksmith:
    jump talked_to_everyone

  menu:
    "Let's go talk to the girl over there and see if she has any information for us." if not talked_to_girl:
        jump village_girl_chat
    "Let's see if we can get anything to aid us should we have to fight the thieves at the blacksmith." if not talked_to_blacksmith:
      jump blacksmith_chat
  return
  
label village_girl_chat:
  village_girl "Hiya Adventurer! Are you here to help us get our gold back from the mean thieves?"
      
  menu: 
    "yes, do you by chance have any information that could help me find them?":
      # this is the only option so we'll just continue here, but it wants to have something in here, so let's just set a variable
      $ ignored = True
    
  village_girl "Absolutely! While out in the forest I've spotted them sneaking around by the mountains mutliple times! I am however way too young to be going after them so I am not sure exactly why they are always over in that area. Hope I could help though!"
      
  menu:
    "Yes that should help me out a lot thank you!":
      $ ignored = True
  
  $ talked_to_girl = True
  jump ask_around_village
  
label blacksmith_chat:
  blacksmith "Why hello there Adventurer, what brings you here?"
  
  menu: 
    "I am looking for some equipment, I have offered to go after the thieves and get your vilages gold back.":
      $ ignored = True
  blacksmith "Oh really? That is wonderful news! Thank you so much for your assistance! I have a spare sword and some armor I would be happy to extend to you to help keep you safe from those awful thieves."
  menu:
    "The armor and sword would be very much appreciated! I shall return soon with the gold!":
      $ ignored = True
  
  $ talked_to_blacksmith = True
  jump ask_around_village
  
label talked_to_everyone:
  narrator "Now that we are all geared up let's head over to the mountainside and find the missing gold!"
  jump head_to_cave
  return
  
label head_to_cave:
  scene mountainside
  narrator "While on the path through the forest that sticks to the mountainside, you come across a cave that two people emerge from." 
  thief "Hey you there! What do you think you are doing in these parts? This is our mountain!"
  menu:
    "I am here looking for some fools that thought it was a good idea to steal from the nearby village, I guess assuming you are the culprits would be correct.":
       $ ignored = True
  thief "Hey who you calling a fool? Hand over your goods they belong to us now!"
    #fight ensues and you win 
    #dragon you are uninjured, without dragon you get injured
  menu:
    "Now that they are gone, let us see what is hidden within this cave.":
      $ ignored = True
  jump cave_after_fight

label cave_after_fight:
  scene cave
  narrator "Here are the three missing bags of gold! Now that we have found them we can bring them back to the village, the villagers will be so excited!"
  jump village_return_from_mountain
  
label village_return_from_mountain:
  villager "You have returned Adventurer! Where you able to find any of our missing gold?"
  menu:
    "Yes here are the three missing bags of gold! Those pesky thieves should not bother you for some time but be more careful about the gold in the future.":
      $ignored = True    
  villager "Oh we will do not worry, we all have definitely learned from this lesson! Regardless, on behalf of the whole village, thank you so much for aiding us and recovering the gold."
  narrator "With their gold back, the village was able to hire help in watching their finances and continue supporting themselves. With more time the area was able to prosper due to a variety of factors including the lack of thefts that occured near the village since then and others moving to the area."
  narrator "The end."