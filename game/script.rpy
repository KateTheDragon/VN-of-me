# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kate")
define K = Character('Kate', kind=nvl)
define c = Character("You")

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
            jump jonar


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
    show kate thinking
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

label spareTime:
    c "What do you do in your spare time?"
    show kate happy
    k """I'm so glad you asked!

    As you might guess from, uh, this, I enjoy gaming and dabbling in various creative hobbies like music and drawing.

    I also like to volunteer. I spent several years volunteering with Sandbox Gaming, raising money for children's charities in St. John's, Newfoundland. I was the treasurer by the end of it! 

    I've also participated in a few game jams and other programming competitions."""
    menu:
        "What should I ask them about next?"
        "Their hobbies":
            jump hobbies
        "Sandbox Gaming":
            jump sandbox
        "Programming competitions":
            jump gameJams
        "I want to talk about something else":
            jump somethingElse

label hobbies:
    c "Tell me more about your hobbies."
    show kate happy
    k """I'm pretty big into gaming. 

    When it comes to video games I like puzzle games like Portal and casual games like Pokemon Go. 

    I enjoy a good board game too, like Catan or Ticket to Ride. 

    And of course, I play a lot of Dungeons and Dragons and other social roleplaying games. 

    {cps=*2}(Please don't ask me about my D&D characters, we'll be here all day.){/cps}

    I also dabble in creative hobbies. I draw and paint, and I play guitar, bass, and ukulele. I'm not particularly good at any of it, but I have fun anyway."""
label hobbyMenu:
    menu:
        "What should I ask them about next?"
        "Their D&D characters":
            jump dndWarn
        "Sandbox Gaming":
            jump sandbox
        "Programming competitions":
            jump gameJams
        "I want to talk about something else":
            jump somethingElse

label dndWarn:
    c "Ok... now I have to ask about your D&D characters."
    show kate thinking
    k """I'm warning you, don't do it.

    There are a lot of them and I am very attached to all of their stories."""
    menu:
        "Should they really tell me about their dnd characters?"
        "Yes":
            jump dnd
        "No":
            c "Never mind."
            jump hobbyMenu

label dnd:
    c "Lay it on me."
    # TODO: make this auto-go and extra fast
    show kate happy
    k """Ok so right now I'm in three games. 

    The character I'm most excited about is named Lady Mara Banefort. 

    In that campaign, we're all Lords and Ladies doing political intrigue type things. 

    Mara is from a real respectable old family, but she has a major secret: she's actually a tiefling and a bastard. 

    She was hidden away as a child, and sent off to the Mages' Tower in the hopes that the world would forget about it. 

    Her family refers to her being a tiefling as her \"illness\" or her \"affliction\". 

    Anywayy when her mother, the previous Lady Banefort, died unexpectedly, everyone expected Mara's younger brother Robin to take up the lordship but he was too noble for his own good and sought out Mara from her travels as a bard. 

    A couple of the party members have figured it out, but if the world at large learns about it, not just Mara's political career, but her entire family's reputation could be at stake.

    I've also got this adorable little witch girl named Evie Evergreen. 

    That game is technically Savage Worlds, not Dungeons and Dragons, so it's a lot more flexible in character creation. My friends and I all decided to be silly and play a party full of children. So Evie is the elf equivalent of a pre-teen. 

    She ran away from home and was really precocious at the adventurer's guild and gathered herself a band of other unaccompanied minors, and they run around getting themselves into trouble they shouldn't be in.

    The last character I'm currently playing is a Loxodon Warlock named Lieutenant Pom Brighttusk. 

    Loxodons are normally rather large elephant people, but because this campaign is set on a world that's entirely islands, the Loxodons are actually like Dwarf-sized. 

    Anyway, this character, Pom, found a dragon egg at a rather sketchy market. 

    The baby in the egg called out to him, so he bought the egg and now he's on leave from the army to raise the dragon as his daughter. 

    Tanwen, the dragon, is a very powerful creature even within her egg. She grants Pom all sorts of magical powers - spells, incantations, and most recently, A GIANT SWORD WITH FLAMES ON IT!!!

    I just left a campaign where I was playing a Tabaxi rogue named Fog-on-the-Water, or Foggy for short.

    This frisky feline fellow is an ex-pirate. he only gave it up because his face is incredibly recognizable on wanted posters and nobody wants to hire him for the more discreet type of job any more, which is where his skillset really lies. 

    So he's looking to fix up his reputation, doing a few jobs on the right side of the law while satisfying his curiousity for adventure and loot.

    I've played a few other characters over time, like a standard half-orc barbarian named Vola the Skull-Cleaver, a pacifist healer elf who the dice gods once favoured to kick in a door over the real strong guy, and a centaur bard. 

    But my favourite character of all time was the party's grumpy grandma, Sabina the ranger. 

    Over the course of two campaigns, Sabina gained a wolf companion named Fayah after the godess of the hunt, met all the kings and governments on her continent, watched her friend Mort die, saved the world, gained the title Lichslayer, became the leader of her ranger corps, got tired of the bureaucracy and went on a new adventure to another continent, found a spaceship at the bottom of a lake, was on the spaceship as her friend Svala raised it to the surface, travelled to another dimension, watched Svala get trapped there and presumably killed by the enemy army, and saved the world again. 

    (Svala, a cleric, used her last moments of connection with her home plane to teleport out of there, a spell the party didn't know she had. She also had a large diamond from her home plane which she was going to use to revive anyone who died but is now using as a focus of a sort to get herself back home.)"""

    show kate thinking
    c "{w=1.0}.{w=1.0}.{w=1.0}."
    k "... I told you not to ask."
    c "...Anyway..."
    jump hobbyMenu

label sandbox:
    c "What was volunteering with Sandbox Gaming like?"
    show kate happy
    k """I had a lot of fun with Sandbox Gaming. 

    I started as a simple volunteer, baking cookies for bake sales and hauling TVs. 

    Eventually I became a committee member, a board member, and then the Treasurer."""
    show kate thinking
    k """We had weekly meetings where I met a lot of wonderful people. We held events for the local gaming community in St. John's, which I helped to run. 

    I played in and hosted tournaments for games like MarioKart and Overcooked. 

    We started up a drop-in Dungeons and Dragons league. 

    Our biggest events, though, were our online gaming marathons. Twice a year, we'd live stream games for 80 hours straight, taking shifts to play games and host and run the tech.""" 
    show kate happy
    k """We'd raise thousands of dollars every year, and it all went straight to various charities in the city.

    Seeing the positive impact I had had on my community was really special. 

    I got to see exactly where the money went each year, and meet some of the kids we had helped support. 

    It feels good to do good, ya know?"""
    menu:
        "What should I ask them about next?"
        "Their hobbies":
            jump hobbies
        "Programming competitions":
            jump gameJams
        "I want to talk about something else":
            jump somethingElse

label gameJams:
    c "What did you do for the programming competitions?"
    show kate thinking
    k """In early 2018, I was part of the Atlantic Engineering Competition. 

    A small group of us were given a problem in the morning, and we had to build a solution in one day. I think we were given about 8 hours.  

    My team decided to build a web app because it was the best fit for the challenge.""" 
    show kate happy
    k """At that time, I had had very little experience in web development so I went online, took a quick crash course in Javascript, and used it for the rest of the day!

    Twice now, I've taken part in the GMTK Game Jam, and I plan to participate again this year.
    
    The first time, me and my friend Garrett made a game about herding cats. 

    The second year, I tried it solo and made a game about a mother finding her lost egg."""
    show kate thinking
    k "For both game jams, I used C# and built the games in Unity 3D."
    menu:
        "What should I ask them about next?"
        "Their hobbies":
            jump hobbies
        "Sandbox Gaming":
            jump sandbox
        "I want to talk about something else":
            jump somethingElse

label jonar:
    c "Why do you want to work with Jonar?"
    show kate happy
    k """The fact that this is an acceptable way to apply is certainly a pro. 

    Like seriously, lots of employers like to say they're a {i}\"fun place to work\"{/i} but with you guys it actually seems true.

    Also basically everyone wants 3 or 5 or 10 years of experience in this economy, so I count myself lucky to have found a place like you that knows the value of a fast learner with a fresh brain!"""
    show kate thinking
    k """On top of that, I'm all about the user experience.

    My main goal at the end of the day is to make software that's easy and enjoyable to use."""
    show kate happy
    k "I want to be proud of the work I've done and if people don't like using it, how can I claim I've helped make something good?"

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
            jump jonar
        "I'm done":
            jump end

label end:
    menu:
        "Contact info":
            jump contact
        "Credits":
            jump credits
        "Quit":
            jump thankYou

label credits:
    scene black
    with dissolve
    show text ("{color=#fff}{size=80}Credits\n\n{size=40}Directed by\n{size=60}Kate Peterson\n\n{size=40}Music by\n{size=60}Erik Peterson\n\n{size=40}Produced by\n{size=60}Kate Peterson\n\n{size=40}Character Artist\n{size=60}Ashley Quirke\n\n{size=40}Written by\n{size=60}Kate Peterson\n\n{size=40}Background Artist\n{size=60}Undetermined\n\n{size=40}Programmed by\n{size=60}Kate Peterson\n\n{size=40}Moral support\n{size=60}Erik Peterson"):
        anchor (0.5, 0.0)
        pos (0.5, 1.0)
        linear 30.0 yanchor 1.0 ypos 0.0
    with Pause(30.0)
    show text ("{color=#fff}{size=80}Based on a true story: the life of Kate Peterson") at truecenter with dissolve
    with Pause(3.5)
    menu:
        "Contact info":
            jump contact
        "Quit":
            jump thankYou

label contact:
    scene bg room

    show kate happy at left

    K "You can reach me by phone at (709) 763 1266"
    K "By email at petersonkatec@gmail.com"
    K "Or by carrier pigeon at -"
    K "Wait, do people still use those?"
    nvl clear
    menu:
        "Credits":
            jump credits
        "Quit":
            jump thankYou

label thankYou:
    c "Thank you for your time."
    show kate happy at center with move
    k """No, thank you! 

    I'm glad we got this opportunity to chat! I hope to see you again soon. 

    Bye!"""
    c "Bye!"
return