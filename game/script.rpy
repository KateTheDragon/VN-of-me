# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kate")
define c = Character("Celine")

# The game starts here.

label start:

    "???" "...Hello?"

    scene bg room

    show kate happy

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


label work:
    c "Tell me about your work history."
    show kate thinking
    k """I've had four internships.
    
    The most recent one was with other Ocean Interactive, a game studio.
    
    Before that, I worked with Wind River Systems building cloud server operating systems.
    
    My first two internships were with Altera, who were bought out by Intel while I worked there, testing FPGA chips for telecom."""

    show kate happy
    menu:
        k "Which one do you wanna hear more about?"
        "Other Ocean":
            jump otherOcean
        "Wind River":
            jump windRiver
        "Altera/Intel":
            jump altera
        "Let's talk about something else":
            jump somethingElse

label otherOcean:
    c "What did you do at Other Ocean?"
    show kate happy
    k """I worked on a mobile game called Super Samurai Rampage, which we designed for both Android and iOS.

    I also helped port it to {a=https://store.steampowered.com/app/675030/Super_Samurai_Rampage/}Steam!{/a}

    As it was a small team, I got to experience a lot of different facets of game development, from design and prototyping to building the product, to testing and debugging, to porting it to different platforms."""
    
    show kate thinking
    k "I primarily used C# and Unity at Other Ocean. \nI also worked with the Steam and Google Play APIs to build the achievement and leaderboard systems."
    k "I was really proud of my work here.{nw}"
    show kate happy
    k "I was really proud of my work here.{fast} It was awesome to be able to put my name on a finished, user-focused product!"
    menu:
        "What should I ask them about next?"
        "Wind River":
            jump windRiver
        "Altera/Intel":
            jump altera
        "I want to talk about something else.":
            jump somethingElse

label windRiver:
    c "What was your work with Wind River like?"
    show kate happy
    k """At Wind River, I worked with a team building Linux operating system for cloud servers.

    Personally, I worked on automated testing, and integrating an older, stagnate system into their upgraded primary system.

    I wrote test cases in C++, debugged automation scripts in Python and Bash, and did integration work in C++ and Python."""
    show kate thinking
    k """Unfortunately, when it came to the integration job, the new system had been upgraded so far and gotten so complex that I wasn't able to successfully integrate them in my short time there.

    But it was a really fun challenge and I feel like I got it a lot closer than when it started."""

    menu:
        "What should I ask them about next?"
        "Other Ocean":
            jump otherOcean
        "Altera/Intel":
            jump altera
        "I want to talk about something else.":
            jump somethingElse

label altera:
    c "What was working at Intel like? And... Altera?"

    show kate happy
    k """Altera got bought out by Intel during my first term work term with them and they were in the process of integration during my second one.

    So my first internship was at Altera. I was super green, didn't know much about anything just yet!

    I mostly took the daily automated test results, fixed what I could, ran a few additional test when necessary, and passed it on to the more experienced programmers.

    By the time my second internship rolled around, they were officially called Intel and I was more experienced. 

    I worked in simulation this time. I built a data frame that the full-timers could use to test FPGA embedded software."""
    menu:
        "What should I ask them about next?"
        "Other Ocean":
            jump otherOcean
        "Wind River":
            jump windRiver
        "I want to talk about something else.":
            jump somethingElse


return

