# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Tutorial")

define unknown = Character("???")

define commentary = Character("")

define player = Character("[playerName]")

define mom = Character("Mom")

define tadashi = Character("Tadashi")

define yuka = Character("Yuka")

define teacher = Character("Teacher")

define studentA = Character("Student A")

define studentB = Character("Student B")

define anon = Character("???")

transform small:
    zoom 1.25

transform middle:
    zoom 1.5

transform large: 
    zoom 3.75 #adjust as required

transform largest:
    zoom 2.5


# The game starts here.

    
label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show anon

    # These display lines of dialogue.

    e "Welcome to Time Loop Academy"

    e "Before we begin, we’d like to give a quick warning regarding the context of this game – if you are uncomfortable with themes of murder, do not continue this game!"

    e "This game is purely fictional – any resemblance to real life places or people is coincidental"

    e "Now enjoy the game!"

    $ playerName = renpy.input("What is your name?: ", length=20)

    $ playerName.strip()

    if not playerName:
        $ playerName = "Charles the III"

    player "My name is [playerName]"

    scene black
    with fade

    unknown "... [playerName]!"

    unknown "[playerName!u]!!!"

    commentary "{i}Sheets rustling{/i}"

    play audio "alarm.ogg"

    scene bedroom at large
    with dissolve

    mom  "[playerName]! Wake up! You're going to be late!"

    player "Nnnn..."

    player "Crap..."

    player "{i}Slept in again... you think I would've learned after being late so many times already.{/i}"

    player "{i}Oh well, guess I better get ready and go{/i}"

    scene black
    with fade

    play audio "sheets.mp3"

    pause (4)

    play audio "Toast.ogg"
    pause (3)

    play audio "Door.ogg"

    pause(2)
    
    scene school at large
    with dissolve

    player "{i}Jikan High... it’s your perfectly average Japanese high school. Almost too average. {/i}"
    
    player "{i}I’ve been here for a while, and nothing exciting has ever happened. Every day has consisted of waking up, going to school, going home, and going to bed. It’s like a damn time loop!{/i}"
            
    player "{i}But that’s life I guess. It’s my own fault for looking for some excitement from some normal high school. Hopefully once I graduate, things will change.{/i}"

    play audio "footsteps.ogg"
    
    scene hallway at small
    with dissolve

    pause(2)

    scene classroom at small
    with dissolve

    show tadashi smile
    with dissolve

    tadashi "Yo! [playerName]!"

    show tadashi idle

    player "{i}My best friend Tadashi, he has been with me since grade school. He can be an idiot sometimes, but you can’t find someone more loyal than him.{/i}"

    show tadashi smile

    tadashi "You're cutting it pretty close. Sleep in again?"

    player "Yeah yeah, cut me some slack. I was up all night studying for today’s test..."

    show tadashi worry

    tadashi "Wait- we have a test today?"

    player "..."

    player "{i}Like i said... an idiot"

    player "Alright, we got a few minutes before class... I’ll help you cram-study."

    show tadashi smile

    tadashi "You're the best!"

    show black
    with fade

    pause (0.5)

    scene hallway at small
    with dissolve

    player "{i}That test was a lot easier than I thought. Maybe studying with Tadashi helped me out a bit too...{/i}"

    player "Anyway, I need to head to my next class-"

    play audio "Bump.mp3"

    pause(1.5)

    player "Oof!"

    show yuka worry
    with dissolve

    yuka "Ah!"

    yuka "Oh! [playerName]! I'm so sorry! Are you okay?"

    player "Oh... Yuka."

    player "{i}Crap... of course I end up bumping into the most beautiful girl at our school!{/i}"

    player "{i}If her armada of fans were here... they’d jump me for potentially hurting their muse...{/i}"

    player "{i}But I can’t blame them, she really is pretty...{/i}"

    yuka "[playerName]?"

    player "Oh! Sorry- yeah I’m- I’m fine..."

    show yuka happy

    yuka "I see. That's a relief."

    yuka "So how did your test go today?"

    player "Huh? How did you know about my test?"

    yuka "I have the same test tomorrow. They always have your class take it the day before ours."

    player "Oh really? I had no idea."

    yuka "Yup. I was actually hoping you’d help me study today after school... at my place."

    yuka "..."

    player "{i}Huh?{/i}"

    player "{i}Wait a minute. Yuka isn’t only popular for our looks. She’s also the smartest girl in our grade.{/i}"

    player "{i}Does she really need help studying?{/i}"

    player "{i}Or...{/i}"

    player "{i}Is she... flirting with me?!{/i}"

    menu:
        "What should I do?"

        "Accept Yuka's invite":
            $ acceptedInvite = True

            player "Sure! Though I don’t know how much help I’ll be..."

            yuka "Thank you, [playerName]! Then I’ll be waiting for you at the gate after school."

            hide yuka happy
            with fade

            player "{i}Alright [playerName], calm down. You’re just helping her study. That’s it. Nothing more.{/i}"

            player "{i}...Right?{/i}"


        "Turn her down":
            $ acceptedInvite = False

            player "{i}No, I must be mistaken. There’s no way she’d be interested in me.{/i}"

            player "Sorry Yuka, I don’t think I’d be much help. Maybe you should ask someone else."

            show yuka worry

            yuka "Oh... I see. I’m sorry for asking."

            player "No it’s-"

            play audio "footsteps.ogg"

            hide yuka worry
            with fade

            player "{i}Crap... did I upset her?{/i}"
    
    player "{i}Whatever, I can worry about that later. I have to get to class.{/i}"

    scene classroom at small
    with fade

    teacher "And for today’s cleaning duty we’ll have Mikoto and... [playerName]"

    studentA "Uh oh, getting paired up with Mikoto?"

    studentB "Ugh, for real, I got paired with him last time. He didn’t even show up! I had to do all the cleaning myself."

    player "{i}Just my luck... looks like I’ll be staying late...{/i}"

    if(acceptedInvite):
        player"{i}Hopefully I can still make it in time to study with Yuka{/i}"

    play audio "Bell.mp3"
    
    scene classroom night at small
    with fade

    player "{i}He really didn’t show up. I had to do the cleaning all by myself.{/i}"
    
    player "{i}Gah... my arms hurt...{/i}"

    player "{i}Oh well, I should pack up and get out of here.{/i}"

    play audio "footsteps.ogg"

    scene hallway night at small
    with fade

    player "{i}I never realized how creepy school can be when it’s late. I can practically hear my own heartbeat.{/i}"

    play audio "Heartbeat.wav"

    player "{i}Anyway, why do I feel so uneasy?{/i}"

    player "{i}Like someone is... watching me...{/i}"

    scene hallway person at small
    with dissolve

    player "{i}...{/i}"

    player "{i}...Huh?{/i}"

    scene hallway night at small
    with dissolve

    show anon
    with dissolve

    anon "{color=#f00}...{/color}"

    player "{i}Who is that?{/i}"

    player "{i}Whoever they are, I don’t have a good feeling about this.{/i}"

    player "{i}I should get out of here.{/i}"

    menu:
        "How do I get away"

        "Run":
            pause(0.5)

        "Quietly leave":
            pause(0.5)

    player "{i}But as soon as I turn around-{/i}"

    play audio "Stab.mp3"

    show black

    player "{i}...{/i}"

    play audio "alarm.ogg"

    scene bedroom at large
    with dissolve

    player "Gah!"

    mom "[playerName]? Are you up?"

    player "Uh... yeah! Sorry mom!"

    player "{i}What... was that?{/i}"

    player "{i}A dream?{/i}"

    mom "Well come down and eat your breakfast! You need a full stomach for that test today!"

    player "Okay, sure-"
    
    player "{i}Wait. Test?{/i}"

    player "{i}I took the test yesterday, didn’t I?{/i}"

    player "{i}Let’s see... I have to have my calendar somewhere.{/i}"

    play audio "sheets.mp3"

    pause(3)

    player "{i}Yesterday was Monday, the 12th, so today should be...{/i}"

    player "{i}Monday the 12th?!{/i}"

    show black
    with fade

    scene black

    show anon

    e "Thank you for playing our demo [playerName]!"

    e "Stay tuned for updates. Until then, see ya!"

    # This ends the game. 

    return
