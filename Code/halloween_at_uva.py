""" short choose-your-own adventure game for a school project - AR """

the_story_continues = True

print('\t', "It’s the night of Hallow’s Eve, and instead of having fun, you’re at the ground floor of Brown", '\n',
      "library last-minute studying for the exam your professor decided to schedule for Monday, the 31st.", '\n',
      "You’ve found yourself the most isolated and quiet corner of grounds to be able to focus while everyone", '\n',
      "else enjoys the end of their Halloween weekend. All of a sudden, the lights go out, and you’re plunged", '\n',
      "into darkness. You look down at your phone and see it’s 12:00 AM – finally Halloween.")
print()

while ( the_story_continues == True ):
    reply = input("Choose to - Investigate the cause or Ignore it & keep studying: ")
    reply = reply.strip().lower().split()

    if ( reply[0] == "investigate" ):
        print()
        print('\t', "Using your phone as a flashlight, you look around the walls for a light switch, noting", '\n',
              "that it seems as though everyone else has vanished. Your phone’s light begins to flicker,", '\n',
              "and you try to exit to your home screen before trying to bring up the control center again. But", '\n',
              "instead, your phone locks, and you’re greeted by the smiling faces of your friends and", '\n',
              "family on the lock screen. Their faces begin to distort and glitch until they’re left", '\n',
              "glaring at you with glowing red eyes. The screen then blacks out, and you feel a jolt of", '\n',
              "electricity in your hand.")
        print()
        reply2 = input("Choose to - Try to fix your phone or Drop it and run: ")
        reply2 = reply2.strip().lower().split()

        if ( reply2[0] in ["try", "fix", "phone"] ):
            the_story_continues = False
            print()
            print('\t', "You desperately try to elicit some response from your phone, tapping the screen and", '\n',
                        "mashing buttons, but to no avail. Suddenly, you hear fast and heavy footsteps getting", '\n',
                        "closer and closer. Before you can even react, you see a flash of blue, and then nothingness.")
            print()
            print("Try Again? (death 1)")

        elif ( reply2[0] in ["drop", "run"] ):
            print()
            print('\t', "You run out the nearest door and out into the cool night, hoping to run into crowds of", '\n',
                        "people who’ll snap you out of it and allow you to conclude that you’ve just been", '\n',
                        "studying for way too long. But as you make your way towards McCormick, you realize that", '\n',
                        "there’s no one – not one sign of life – on grounds. It’s deadly silent – no people, no", '\n',
                        "parties, no music, no cars, no bugs, no birds. There’s no indication that anyone has", '\n',
                        "ever been in your location, aside from the man-made signs and structures near the road." )
            print()
            reply3 = input("Choose to - Explore further or Close your eyes: ")
            reply3 = reply3.strip().lower().split()

            if ( reply3[0] == "explore" ):
                the_story_continues = False
                print()
                print('\t', "You keep walking forward, hoping to find any sign of life or at least any hint", '\n',
                            "about what is going on. You walk and walk until you somehow ended up on the Lawn.", '\n',
                            "There’s still no sign of anything, until you get to the Rotunda steps, where a ", '\n',
                            "mangled body lies. You’re repelled, but it’s the only thing you’ve seen so far, so", '\n',
                            "you go closer. You notice a piece of paper with scribbles of writing lying near the", '\n',
                            "body, so you pick it up. It reads, “If you’re reading this, it’s probably already", '\n',
                            "too late, but the only way out of this is to close your eyes.” You immediately", '\n',
                            "shut your eyes, placing blind faith in the author of these words, but nothing", '\n',
                            "happens. You continue reading. “If that doesn’t work, you’re already dead, but you", '\n',
                            "at least deserve some answers. I still don’t understand everything myself, but I", '\n',
                            "know it found you through one of your devices. Once it does, every piece of ", '\n',
                            "technology around you stops working, and you end up here. I think it’s almost here", '\n',
                            "so that’s all I can say but I’m sorr” The last word is smudged and barely", '\n',
                            "readable, but you know what they meant. You feel dread build up inside of you, and", '\n',
                            "at the last second of your life, you realize that it’s right behind you.")
                print()
                print("Ending 1 (knowledge)")

            elif ( reply3[0] in ["close", "eyes"] ):
                the_story_continues = False
                print()
                print('\t', "You shut your eyes tight, hoping that once you reopen them, you’ll wake up from", '\n',
                            "this nightmare. Surprisingly, the longer you keep your eyes closed, the more it", '\n',
                            "sounds like there are others nearby. You can no longer stand the apprehension, and", '\n',
                            "when you open your eyes, it feels like you’ve been teleported back to reality.", '\n',
                            "Students’ chatter, laughing, and faint music fills the air as you look around and", '\n',
                            "see everything has returned to normal. Somehow, closing your eyes was the right", '\n',
                            "things to do. You’ll never really know what happened to you that day, but hey,", '\n',
                            "at least you survived.")
                print()
                print("Ending 2 (escape)")

            else:
                print("unknown answer")

        else:
            print("unknown answer")

    elif ( reply[0] == "ignore" ):
        print()
        print('\t', "You decide that the light emanating from your laptop is enough illumination for you, and", '\n',
                    "nothing will get in the way of you finishing your studying ASAP. Unfortunately for you,", '\n',
                    "it’s not long after that you stop getting a signal. Your opened tabs stop responding, and", '\n',
                    "they suddenly begin closing on their own. All of your open windows begin to close out, and", '\n',
                    "you’re left staring at your desktop, at the smiling faces of your friends and family. Their", '\n',
                    "faces begin to distort and glitch until they’re left glaring at you with glowing red eyes.", '\n',
                    "The screen then blacks out, and you hear heavy footsteps making their towards you.")
        print()
        reply4 = input("Choose to - Run or Hide: ")
        reply4 = reply4.strip().lower()

        if ( reply4 == "run" ):
            print()
            print('\t', "You run out the nearest door and into the cool night, hoping to run into crowds of", '\n',
                        "people who’ll snap you out of it and allow you to conclude that you’ve just been", '\n',
                        "studying for way too long. But as you make your way towards McCormick, you realize that", '\n',
                        "there’s no one – not one sign of life – on grounds. It’s deadly silent – no people, no", '\n',
                        "parties, no music, no cars, no bugs, no birds. There’s no indication that anyone has", '\n',
                        "ever been in your location, aside from the man-made signs and structures near the road.")
            print()
            reply5 = input("Choose to - Look at your phone or Explore further: ")
            reply5 = reply5.strip().lower().split()

            if ( reply5[0] in ["look", "phone"] ):
                the_story_continues = False
                print()
                print('\t', "You pull out your phone, hoping to find answers, or even just the ability to", '\n',
                            "contact someone. As soon as you unlock it though, a jolt of electricity runs", '\n',
                            "through your hand and throughout your body, and you drop the phone. You look down", '\n',
                            "at the phone, the screen glitching uncontrollably, as colors, images, and text", '\n',
                            "appear every millisecond. It slows down enough to let you see three words. “Look", '\n',
                            "behind you.” You do, and the last thing you ever see is a flash of red.")
                print()
                print("Try Again? (death 3)")

            elif ( reply5[0] == "explore" ):
                the_story_continues = False
                print()
                print('\t', "You keep walking forward, hoping to find any sign of life or at least any hint", '\n',
                            "about what is going on. You walk and walk until you somehow ended up on the Lawn.", '\n',
                            "There’s still no sign of anything, until you get to the Rotunda steps, where a ", '\n',
                            "mangled body lies. You’re repelled, but it’s the only thing you’ve seen so far, so", '\n',
                            "you go closer. You notice a piece of paper with scribbles of writing lying near the", '\n',
                            "body, so you pick it up. It reads, “If you’re reading this, it’s probably already", '\n',
                            "too late, but the only way out of this is to close your eyes.” You immediately", '\n',
                            "shut your eyes, placing blind faith in the author of these words, but nothing", '\n',
                            "happens. You continue reading. “If that doesn’t work, you’re already dead, but you", '\n',
                            "at least deserve some answers. I still don’t understand everything myself, but I", '\n',
                            "know it found you through one of your devices. Once it does, every piece of ", '\n',
                            "technology around you stops working, and you end up here. I think it’s almost here", '\n',
                            "so that’s all I can say but I’m sorr” The last word is smudged and barely", '\n',
                            "readable, but you know what they meant. You feel dread build up inside of you, and", '\n',
                            "at the last second of your life, you realize that it’s right behind you.")
                print()
                print("Ending 1 (knowledge)")

            else:
                print("unknown answer")

        elif ( reply4 == "hide" ):
            the_story_continues = False
            print()
            print('\t', "You look around and decide to squeeze into a small corner behind some bookshelves. You", '\n',
                        "hold your breath and make yourself seem as small as possible as the footsteps make", '\n',
                        "their way towards you. They stop, and you wonder if they’re going to leave. Suddenly,", '\n',
                        "you feel a large force push against you, a flash of green, and then darkness.")
            print()
            print("Try Again? (death 2)")

        else:
            print("unknown answer")
    else:
        print("unknown answer")
