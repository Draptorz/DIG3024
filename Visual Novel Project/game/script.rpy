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
  return
label forest_befriend_dragon:
  scene black
  narrator "You're befriending the dragon"
  return
label forest_go_to_village:
  narrator "You're going to the village"
  return