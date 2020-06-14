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

label education:
    show kate happy
    k """I started at Memorial University of Newfoundland in the fall of 2014. 

    I was originally in the Computer Engineering program, which is why I was able to do the internships. 

    After a while I found out that it wasn't for me. It wasn't teaching me the software skills I needed to move my career in the direction I wanted. So, I switched to Computer Science."""
    menu:
        "What should I ask them about next?"
        "Their favourite class":
            jump faveClass
        "If they did any projects":
            jump project
        "I want to talk about something else.":
            jump somethingElse

label faveClass:
    c "What was your favourite class?"
    show kate thinking
    k """My favourite class was probably the swarm robotics class.

    There were too many students and not enough funding to work with {i}actual robots{/i}, so we worked in simulation instead."""
    show kate happy
    k """But it was still really cool.

    Basically, we'd program a bunch of little \"robots\" with simple behaviours, and when a whole bunch of them were set loose with the same program, there were emergent behaviours that let them complete tasks as a group!

    One robot might only be able to pick up an object and wander aimlessly until it found another object of the same colour, but a swarm of robots doing that could tidy up and sort a whole field of objects."""
    menu:
        "What should I ask them about next?"
        "If they did any projects":
            jump project
        "I want to talk about something else":
            jump somethingElse

label project:
    c "Did you do any interesting class projects?"
    show kate happy
    k """Oh yeah!

    I'd say the coolest one was for a game programming class, where me and my friend Garrett got to build a basic game engine from scratch over the course of the semester.

    By the end, we had a fully-functioning platformer, kind of like Super Mario. It had a level editor and everything!"""
    menu:
        "What should I ask them about next?"
        "Their favourite class":
            jump faveClass
        "I want to talk about something else":
            jump somethingElse

label somethingElse:
    c "Let's talk about something else."
    k "Ok, what do you wanna talk about?"
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
        "I'm done chatting":
            jump thankYou

return

