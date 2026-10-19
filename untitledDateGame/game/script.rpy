# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define nr = Character("Noor")

define pm = Character("Dr. Palm")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # !!! show noor happy

    # These display lines of dialogue.

    "Location: Moroccan Airspace, 2,000 m above sea level"

    "Captain" "Good evening, passengers. This is your captain speaking aboard flight D8 from Boston Logan to Casablanca Mohamed V International Airport. We are about to begin landing, please return your seat backs to the upright position, and stow away your tray tables."

    nr "Already landing? Guess that’s what I get for sleeping on the airplane… I was hoping to brush up on recent research, though."

    nr "Blech, still have the taste of the croissants they gave out after take-off. I should probably freshen up before the seatbelt sign goes on."

    # EFFECT fade

    # SOUND door open

    # LOCATION // Bathroom: customization, choose character style.

    # SOUND door close

    # EFFECT fade

    # SOUND seatbelt sign

    "Captain" "Hello, once again! We’ve begun our descent, and you’ll notice that the seatbelt sign is now on. Please keep your seatbelts fastened and refrain from getting up for the remainder of the flight. On behalf of the airline, we would like to thank you all for for flying with us today, and hope to see you again soon!"

    # SOUND plane landing

    # EFFECT fade to black

    # EFFECT fade \\ note, maybe wipe or other scene transition

    # SOUND bags rustling

    "Location: Casablanca Mohamed V Airport"


    nr "Whew, gotta love that Moroccan air! So warm, especially after that freezing flight. The temperature really messed with my sleep, not gonna lie."

    nr "I’m so glad I didn’t check any bags. Instead of having to wait in another line after customs, I can check straight into my —"

    "!! Alert !! 1 New Message"

    nr "Shoot, forgot to check my phone. Hope I didn’t miss anything important."

    # // Phone: Message (top, clickable) — Dr. Palm / Good evening (unless it happens to be —
    #     Onclick: message history, message
    #     Here are the details of your flight ticket:
    #     [image]
    #     Good evening (unless it happens to be morning where you are)!
    #     Call me when you land. I have something important to discuss.


    """

    "Noor presses “Call,” and waits."

    pm "Well, hello there! I presume you landed safely, heh."

    nr "Yup. All in one piece, ready to get to researching as soon as possible!"

    pm "Oh, you are? I have a bit of bad news, I’m afraid."

    pm "The grant funding the research program in Morocco fell out. We’ll get you back to the States soon on a return flight, but the university can’t provide accommodations, unfortunately."

    nr "…"

    # THINKING !!!
    nr "I thought they were just going to say something like there were budget cuts. I wasn’t expecting this! I’m barely out of freshman year, too, and now I’ve got to navigate Morocco on my own for, uh, for —"

    nr "When’s the return flight?"

    pm "[sharply inhales]"

    pm "We’ll see what we can do, and get back to you."

    pm "Sorry for the bad news. I know it probably wasn’t what you were hoping to hear after landing in a new country, ready to do some rrrrresearch!"

    # THINKING !!
    nr "Classic Dr. Palm. Him and his enthusiasm for learning! If only the university staff shared his passion ..."

    nr "... Or the government? I really should have looked into where the grant came from."

    nr "Speaking of the grant… I guess he softened the blow a little. Still, I don’t really like how avoidant his answer — no matter how enthusiastic – was."

    nr "Well, he’s the only professor I know. I can’t afford to ruin my relationship with him over a fluke like this. How am I ever going to get another opportunity, then? That settles it."

    "..."

    pm "Hello... You still there?"

    nr "Oh! Yes, I was just about to say that there was no problem, sir! You know, in research it’s important to be able to pivot, and that’s what I’ll do."

    pm "Ha, ha, indeed. Alright, goodbye for now."

    # This ends the game.

    return
