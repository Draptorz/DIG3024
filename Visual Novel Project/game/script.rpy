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
  narrator "While on your way to the next village on your journey through the mountains, you encounter something quite strange."
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
  narrator "While on the path through the forest that sticks to the mountainside." 
  show thief
  thief "Hey you there! What do you think you are doing in these parts? This is our mountain!"
  menu:
    "I am here looking for some fools that thought it was a good idea to steal from the nearby village, I guess assuming you are the culprits would be correct.":
       $ ignored = True
  if has_dragon:
    thief "Hey who you calling a fool? Hand over your goods and your dragon, they belong to us now!"
  else:
    thief "Hey who you calling a fool? Hand over your goods, they belong to us now!"
    # TODO Raise sword and shield
    menu:
      "Over my dead body!":
        $ignored = True
    
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
  narrator "After helping the villagers get their gold back, you feel very accomplished with the good deed. Throughout the rest of your travels, whenever someone else asks for help you go and try to aid them if you can."
  narrator "The end."
  
label disagree:
  villager "Oh ok, sorry for bothering you about our dilema. I was careless in asking someone just passing through, please accept my appologies! If you need anything just let us know."
    menu:
      "I am all set but thank you for the offer, I will be on my way.":
      $ ignore = True
    jump disagree_left_village
  return

label disagree_left_village
  thief "Not too smart to be out here on your own buddy, your items are mine now!"
  #gets knocked out and taken to the cave
  scene black
  if has_dragon:
  jump disagree_cave
  else:
  jump disagree_cave_end
  return
  
label disagree_cave_end  
  scene black
  narrator "You slowly come to in a new location tied up."
  scene cave
  menu:
    "Huh? Where am I? This appears to be a cave of some sorts, I need to escape before that theif comes back!":
    $ ignore = True
  "struggles but to no avail are you able to break out of the restraints"
  show theif
  theif "Oh ho think we can escape do we? You are not going anywhere."
  scene black
  narrator "Game over"
  return 
  
  
label disagree_cave
  scene black
  narrator "You slowly come to in a new location tied up with your dragon friend next to you."
  menu:
    "Huh? Where am I? Dragon are you ok? This looks like a cave we have been taken to, we need to get out of here before that guy comes back!":
    $ ignore = True
  "after a moment of struggling your dragon comes over and bites through the ropes, allowing you both to escape"
  menu: 
    "Thanks buddy! Hey what's over there? Those look likes bags of something... Oh! Those must be the bags of gold that were stolen from the village! With them being just right here, what should I do with them?":
  menu:
    "Take the bags of gold and keep them, the theif deserves to lose them after daring kidnap you and your friend!":
      jump disagree_steal_gold
    "Leave them! That theif could be back any moment and then you both will be done for!":
      jump disagree_leave_gold
    "Since they are right here, might as well help the villagers and bring the bags back to them. The theif should learn better than hiding people and treasure together.":
      jump disagree_change_heart
  return
  
label disagree_steal_gold
  scene black
  narrator "After taking the gold and escaping from the cave, the village is never able to recover the stolen gold. With the gold lost, they struggle to keep the village running and suffer for many years because of having to rebuild from nothing.
  narrator "Since you and your dragon now have quite some wealth to your names, you are able to travel and live without worries, but always have to keep watch because many others have tried to take that wealth from you."
  narrator "The end."
  return
  
label disagree_leave_gold
  scene black
  narrator "After you both escape with your lives leaving the gold behind you, another Adventurer comes along and is successful in recovering the villages stolen gold. The village did struggle for some time while being without the funds for many daily needs, but with the returned gold they could pick themselves up quickly and began to prosper with time."
  narrator "You and your dragon friend go off and explore many new areas together just glad you both have each other."
  narrator "The end."
  return
  
label disagree_change_heart
  scene village
  narrator "After you both emerge safely from the cave with the stolen gold, you return to the village to give it back to its rightful owners."
  villager "Adventurer? What are you doing back here? I thought you said you were just passing through and had already left this place!"
  menu:
    "I had left, but got caught up with something and managed to find these. Is this by chance what your village has lost?":
       $ ignore = True
  villager "The missing gold! I do not know how you found this, but you have no idea how much this means to all of us! Thank you so much for returning this to us!"
  menu:
    "It was no problem, I hope you all take better care at keeping this safe from now on though!":
      $ ignore = True
  villager "Oh we will we can promise you that! Once again, thank you both."
  scene black
  narrator "After recieving their gold back, the village was able to hire help in watching their finances and continue supporting themselves. The theif was scared off by those hired to protect the place, and the village along with the surrounding area grew more populous and prospered."
  narrator "Once leaving the village and having gone through the change of heart, you and your dragon friend continued to help out whenever asked throughout the rest of your journey."
  narrator "The end."