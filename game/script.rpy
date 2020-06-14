# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kate")
defint c = Character("Celine")

# The game starts here.

label start:

    "???" "...Hello?"

    scene bg room

    show Kate happy

    k "Hi! You must be Celine. I'm Kate."
    k "It's nice to meet you!"
    k "I'm so glad you could chat with me today."

    menu:
        "I should ask them about..."
        "Their work history":
            jump work
        "Their education":
            jump education
        "How they spend their spare time":
            jump spareTime
        "Why they're interested in Jonar":
            jump Jonar

    return

label work:
    c "Tell me about your work history."
    show Kate thinking
    k "I've had four internships."
    k "The most recent one was with other Ocean Interactive, a game studio."
    k "Before that, I worked with Wind River Systems building cloud server operating systems."
    k "My first two internships were with Altera, who were bought out by Intel while I worked there, testing FPGA chips for telecom."
    show Kate happy
    k "Which one do you wanna hear more about?"
    menu:
        "Other Ocean":
            jump OtherOcean
        "Wind River":