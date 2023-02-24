# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character("Narrator")
define dragon = Character("Dragon")
define villager = Character("Villager")
define blacksmith = Character("Blacksmith")
define thief = Character("Thief")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    narrator "You wake up."

    #e "Once you add a story, pictures, and music, you can release it to the world!"
    
    scene forest dragon
    
    narrator "What's that? A dragon?!"

    # This ends the game.

    return
