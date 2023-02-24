# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character("Narrator")
define dragon = Character("Dragon")
define villager = Character("Villager")
define blacksmith = Character("Blacksmith")
define thief = Character("Thief")

label start:
    scene black
    #show eileen happy
    narrator "You wake up."
    scene forest dragon
    narrator "What's that? A dragon?!"
    
    menu:
      "Fight it":
        jump forest_fight_dragon
      "Befriend it":
        jump forest_befriend_dragon
      "Go the other way":
        jump forest_go_to_village

    return

label forest_fight_dragon:
  scene black
  narrator "You're fighting the dragon"
  narrator "You lose the fight. Game Over."
  return
  
label forest_befriend_dragon:
  scene black
  narrator "You're befriending the dragon"
  scene forest 
  show dragon
  narrator "You now have a new friend! Where shall you both start adventuring to together?"
  
  menu:
    "Head deeper into the forest":
      jump mountainside_trail
    "Go the other way":
      jump forest_go_to_village_with_dragon
    
  return
  
label mountainside_trail
  scene mountainside
  narrator "as you both explore the scenery, you stumble upon a cave entrance that your new dragon friend seems curious about. What should you both do?
  
  menu:
    "Follow the dragon into the cave."
      jump first_cave_appearance
    "Tell the dragon not now and continue down the path"
      jump mountainside_go_to_village
  return
  
label forest_go_to_village_with_dragon
  return
  
  
  
label forest_go_to_village:
  narrator "You're going to the village"
  scene village
  "Villager" "Oh adventurer! Can you please help us? Thieves raided our village earlier and have taken most of the villages gold! We will not be able to continue our way of life without our incomes or savings and really need your help in recovering the gold!
  
  menu:
    "Agree to help retrieve the gold"
      jump agree
    "Tell them sorry you are not able to help"
      jump disagree
  return
  