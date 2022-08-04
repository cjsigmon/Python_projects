"""A Choose Your Own Adventure Game."""

__author__ = "730396796"

player: str
points: int = 0
NO: str = "No"
YES: str = "Yes"
HATMAN: str = "\U0001F574"
WITCH: str = "\U0001F9D9"
OLDMAN: str = "\U0001F474"
TREE: str = "\U0001F333"
DOOR: str = "\U0001F6AA"
EXPLOSION: str = "\U0001F4A5"
met_witch_twice: bool = False
bridge_wrong: str = "\nYou guessed incorrect! Your body is flung at sonic speed down into the lake and your quest comes to a sudden unfortunate end."


def main() -> None:
    """The entrypoint."""
    global points
    points = 0
    greet()
    choice: str = input("Where do you want to go? (Type A for \"Mountains,\" B for \"Lake,\" or C to end the game.) ")
    while choice != "A" and choice != "B" and choice != "C":
        choice = input("Sorry, you'll have to type in as exactly \"A\" or \"B\" or \"C\" (not inlcuding the quotation marks). ")
    if choice == "C":
        game_over()
        replay()
    elif choice == "A":
        mountains()
    elif choice == "B":
        lake()


def greet() -> None:
    """This opens the game."""
    global player
    print("\n Welcome to ADVENTURE STORY where your obejctive is to survive, recover your memory, discover treasure, and earn ADVENTURE POINTS. By making more adventurous choices, you can earn more points. But watch out! some choices can mean GAME OVER, so don't be too reckless. Now, allow me to set the scene...\n")
    input("... (press enter to continue.) \n")
    print(f"{TREE}{TREE}{TREE}{TREE}{TREE}{TREE}{TREE}{TREE}{TREE}{TREE}")
    print("You are alone in a dark forest.")
    print("You are afraid, hungry, and have no memory of how you got there.")
    input("... (press enter to continue.)\n")
    print("Suddenly, you see a tall man wearing a black coat and big black hat come out from behind a tree.")
    print(f"{HATMAN}")
    input("(enter)\n")
    print("The man comes up to you and begins speaking. \"So, what name do you go by, brave stranger?\" he asks.")
    player = input("Please type your name in here, then press enter:\n ")
    print(f"The man in black continues, \"Well, {player}, I think I may be able to help you. 'Course, you'll have to help me, too. You see, I'm looking for some treasure. It's said to be around these parts but I lost my map and I don't remember if it's up in the mountains or down by the lake.\"")
    input("(enter)")
      

def replay() -> None:
    """This restarts the game."""
    replay: str = input("Wanna start over? Type \"Yes\" to restart: ")
    while replay != YES:
        replay = input("If you want to play more you'll have to type \"Yes\" (but without the quotation marks) Type here: ")
    if replay == YES:
        main()
    elif replay == NO:
        print("OK. See ya later then.")


def point_increase() -> None:
    """This is used to add points every time the player makes a good choice."""
    global points
    print("\nGood choice! You earned 10 ADVENTURE POINTS!")
    points = points + 10
    print(f"You now have {points} total ADVENTURE POINTS.")


def small_point_increase() -> None:
    """This is used to add points every time the player makes a conservative choice."""
    global points
    print("\nMeh. That action only earned you 1 ADVENTURE POINT.")
    points = points + 1
    print(f"You now have {points} total ADVENTURE POINTS.")   


def bad_point_increase() -> None:
    """This is used to add points when the player takes a risky choice."""
    global points
    print("\nThat choice was adventurous. Perhaps a bit too much.")
    points = points + 5
    print(f"You now have {points} total ADVENTURE POINTS.")  
    

def game_over() -> None:
    """Run this every time a player's choice ends their path."""
    print("\nGAME OVER")
    print(f"YOUR EARNED ADVENTURE POINTS: {points}")


def mountains() -> None:
    """This leads through the mountain journey."""
    global met_witch_twice
    print()
    point_increase()
    print("The Hatman nods his head. \"I was thinking the same thing,\" he says. \"But I'll have to warn you, this way will be very dangerous...")
    input("(enter) \n")
    print("The man takes you through the woods for several hours. Over time, the walk becomes more strenuous and you notice that in addition to the fact you are out of breath, you are also very very hungry. You ask Hatman if he has anything to eat.")
    input("(enter) \n")
    print("\"Hmm, no, I don't believe that I do.\" He replies.\" \"But I can think of a couple of options.\"")
    input("(enter) \n")
    print("\"One thing is we could go around and forage for berries and what-not; I'm sure we'd find somethin,' whether it'd be poisonous or not is a different question. OR, we could summon the dinner witch--but watch out: she's been known to have a cruel sense of humor. So what do you think? Foraging or witch-summoning?\"\n")
    dinner_choice: str = input("Type A for \"Foraging,\" or B for \"Witch-summoning.\" ")
    while dinner_choice != "A" and dinner_choice != "B":
        dinner_choice = input("\nSorry, you'll have to type in as exactly \"A\" or \"B\" (not inlcuding the quotation marks). ")
    if dinner_choice == "A":
        small_point_increase()
        print("\nThe Hatman sighs and nods. \"Yep. That's probably the wise option,\" he says. The two of you split up to look for berries and whatever else you can find.")
        input("(enter) \n")
        print("Luckily, within moments you find some wild grapes. Just as you are reaching to grab some, a giant snake pops out of the brush and bites your arm off. You have only a few moments to cleverly think, \'I guess now I'm a lefty\' before succumbing to faintness and pass out.")
        input("(enter) \n")
        print("The Hatman tries to save you but unfortunately the blood loss is too bad and to top it all off, the snake was venemous.\n")
        game_over()
        replay()
    elif dinner_choice == "B":
        met_witch_twice = True
        point_increase()
        print("\nThe Hatman looks at you with a smirk. \"You're a risk-taker, eh?\" He grunts, \"I like that.\"")
        input("(enter) \n")
        print("Then Hatman begins chanting the lyrics to what he assures you is a very ancient song...")
        print("\t\"OHHHH dear dinner witch-ey, witch-ey,")
        print("\tWe find ourselves in quite the hitch-ey, hitch-ey.")
        print("\tSo please lend us your great favor,")
        print("\tIn something that has a nice flavor")
        print("\tA dooby doo-doo dee dah")
        print("\tI'll take anything but hog maw.\"")
        print("Right as Hatman finishes singing, a flurry of leaves, a chilling cackle, and a pleasant aroma fills the air around you. It's the dinner witch!")
        print(f"{WITCH}")
        input("(enter) \n")
        print("The witch materializes from a shadow and approaches you \"My, my, don't you look hungry,\" she says. \"Well, not to worry, I've got just the thing. But first you need to tell me...How old are you?\"")
        age: str = input("\nType your age here: ")
        portion: float = float(age) / 4
        print(f"\nThe witch cackles with delight. \"Oh, just a {age}-year old? I don't know if you can handle much more than {portion} helpings of my special potion--er, I mean food.\"")
        print("\tShe removes a flask from her gown filled with a gooey brown sludge and produces a bowl in her other hand out of thin air. She adds a couple dollops of sludge into the bowl and suddenly a slice of bread appears in it.")
        input("(enter) \n")
        print("\"Here,\" the witch says, \"Eat this piece of bread. Not only will it FILL YOU UP, but it will guide you to the treasure I know you seek.\"")
        print("\tYou take the slice of bread and begin eating. Then you begin to feel concerned about the safety of the pastry. Do you finish eating it or leave it half-eaten?")
        bread_choice: str = input("\nType \"A\" to finish the bread, or \"B\" to discretely toss it away ")
        while bread_choice != "A" and bread_choice != "B":
            bread_choice = input("\nSorry, you'll have to type in as exactly \"A\" or \"B\" (not inlcuding the quotation marks). ")
        if bread_choice == "A":
            point_increase()
            print("\nYou gulp down the last bite of bread and notice you DO feel quite full. Satisfied, you thank the witch.")
            input("(enter) \n")
            print(f"\"Oh, it was nothing really,\" she says. \"Now I guess I shall be seeing you later, {player}.\"")
            input("(enter) \n")
            print("You become confused when after a few moments the witch makes no attempt to move. She just stands there and smiles at you. Meanwhile you are feeling more and more full. Almost TOO full. Almost as if...\n")
            print("...\n")
            input("(enter) ")
            print(f"\nBOOOOOMMM!!! {EXPLOSION} The biggest gas explosion you've ever heard or felt erupts from your tail-end and you launch into the sky at hair-graying speed.")
            print("You look down on the world below you in wonder as you fly not only above and past the great dark forest, but past the mountain it was leading to.")
            input("(enter) ")
            print("\nYou begin to lose momentum and start to fall as you reach the opposite side of the mountain. Only now do you begin to wonder how you might stick the landing.")
            print("Quick! You've only got a few seconds before hitting the ground. Do you try to gently let another one loose or hold it in for good manners?")
            gas_choice: str = input("\nType \"Yes\" to let off some hot air or \"No\" to tough it out for the landing: ")
            while gas_choice != YES and gas_choice != NO:
                gas_choice = input("\nSorry, you'll have to type in as exactly \"Yes\" or \"No\" (not inlcuding the quotation marks). ")
            if gas_choice == NO:
                bad_point_increase()
                print("\nLet's see how this goes...")
                input("\n(enter) ")
                print("\nSPLAT! Yeesh, that does not look good. Maybe next time it'd be better to pass gas than to pass away.")
                replay()
            elif gas_choice == YES:
                point_increase()
                print("\nKablooey! Fwooosh! SKKKSH! You land softly and safe, thinking it's time to ditch your dream of a Tesla because gas is still a viable way to get around.")
                print("You take in your surroundings. You're situated at the end of a bridge that crosses from the forest over a lake to the side of the mountain. You wonder if you might have ended up here just as fast if you'd chosen the lake route. Either way, might as well get on with it and see if you can find the treasure or whatever. ")
                input("(enter) \n ")
                ending()
                
        else:
            bad_point_increase()
            print("\nOh noes! As you try to be discrete in throwing the rest of your bread away you realize this is impossible with the witch standing right in front of you. \"WHAT DO YOU THINK YOU'RE DOING?!?!\" she screams. \"I wasn't gonna tell you this, but since you have angered me, I will: It was I who erased your memory and left you in these woods to die. It was I who kidnapped your pet sloth and made you forget his name and very nearly your own. And it is I who will now erase your memory again and eliminate any chance you have of defeating me! MWAHAHA!\"\n")
            game_over()
            replay()


def math(a: int) -> int:
    """This function randomly chooses an amount of adventure points."""
    from random import randint
    point_increase: int = 0
    door: int = randint(1, 3)
    if a > 3 or a < 1:
        return point_increase
    elif a <= door:
        point_increase = point_increase + 100
    return point_increase


def ending() -> None:
    """This leads through the game ending."""
    global points
    global met_witch_twice
    global player
    print("\nYou see a cave on the side of the mountain in front of you. If there's going to be hidden treasure anyhwere around, it's gotta be here, you think. You walk into the cave and everything goes dark. You feel around the walls of the cave to keep yourself oriented. Your hand brushes past something fuzzy. Should you grab it, or keep walking?")
    sloth_choice: str = input("\nType \"Yes\" to grab or \"No\" to keep walking: ")
    while sloth_choice != YES and sloth_choice != NO:
        sloth_choice = input("\nSorry, you'll have to type in as exactly \"Yes\" or \"No\" (not inlcuding the quotation marks). ")
    if sloth_choice == YES:
        point_increase()
        print("\nYou reach back to the fuzzy item and suddenly IT grabs YOU. It wraps a little hand around your finger and instantly you remember: This is Siddhartha, your magical pet sloth. But what was he doing in some cave and how did he get there? You decide you may soon find the answer as you put Siddhartha into the open pouch of your backpack where he can continually give you neck massages and replenish your stamina.")
        input("(enter) ")
    else:
        small_point_increase()
    print("\nYou keep walking until you see a small lit fire on the ground a little ways ahead. You approach and there you see an old woman sitting, her back to you. You also see three wooden doors abruptly situated in the natural stone of the chamber's back wall.")
    print(f"\tThe old lady cackles and says, \"So, {player}, you've come at last. It was about time we met again.\"")
    input("(enter) ")
    print("\nShe turns around and faces you, and instantly your memory returns. THIS is the witch that you encountered while searching for treasure. It was she who erased your memory, kidnapped your magical sloth, and left you in the woods to die.") 
    if met_witch_twice is True:
        print("Not only that, she appears to be the very same witch who tricked you into eating the noxious bread that very likely could have killed you.")    
    input("(enter) ")
    print("\n\"What do you want from me?\" you ask the witch.")
    print("\t\"Oh, that's really quite simple,\" she says. I want to get rid of you and use your magical sloth for potion ingredients. But not to worry my dear; I can see those are not the goals you have in mind for your little adventure. You're after my treasure, aren't ya?\"")
    input("(enter) ")
    print("\nYou agree.")
    print("\t\"Good, good,\" the witch says. Then I propose a little compromise. If you can guess which one of these doors behind me has the treasure, I'll let you have some. If you guess wrong...I'll turn you into a demon--er, I think it's pronounced, \'chihuahua.\' Sound good?")
    input("(enter) ")
    print("\nYou nod.")
    print("\t\"Excellent!\" the witch exclaims. Let's begin...")
    print("\"Before you are three doors.\"")
    print(f"{DOOR}{DOOR}{DOOR}\n")
    door_choice: int = int(input("\"Which door do you choose?\" Type \"1\" for the one on the left, \"2\" for the one in the middle, or \"3\" for the one on the right: "))
    while door_choice != 1 and door_choice != 2 and door_choice != 3:
        door_choice = int(input("\nSorry, you'll have to type in as exactly \"1\" or \"2\" or \"3\" (not inlcuding the quotation marks). "))
    if points + math(door_choice) > points:
        points = points + math(door_choice)
        print("\nYou guessed correctly and earned 100 adventure points!")
        print("The witch hands you the treasure from behind the door and sends you on your way. You travel back home, now able to remember the way and live happily ever after.")
        print("\nYOU WON!")
        print(f"YOUR EARNED ADVENTURE POINTS: {points}")
        replay()
    else:
        bad_point_increase()
        print("\nIt seems you've made the wrong choice. With a flick of her fingers, the witch casts a spell on you and turns you into a troublesome and powerless canine. Your adventure has come to an end.")
        game_over()
        replay()


def lake() -> None:
    """This function goes through the lake path."""
    quest: str = "Treasure"
    swallow_first_option: str = "What do you mean? An African or European swallow?"
    swallow_second_option: str = "about 24 miles per hour"
    swallow_third_option: str = "24 miles per hour"
    global player
    global bridge_wrong
    point_increase()
    print("\n\"Yeah, that's probably the wise choice,\" the Hatman says. \"Let's start heading that way.\"")
    print("Hatman takes you down to a nearby stream and the two of you follow it down together for perhaps an hour before reaching a large clearing: You've arrived at the lake.")
    input("(enter) ")
    print("\nFortunately, there is a bridge right in front of you which Hatman assures is pretty dang likely to lead to the treasure.")
    print("\t\"Alright, before we cross, there's a few things you should know.\" ")
    input("(enter) ")
    print("\n\"There's going to be an enchanter guarding the bridge and making sure only those who are worthy can cross. He is going to ask you a series of three questions. First, he'll ask your name. Make sure you tell him the same one you told me. Second he'll ask your quest. You'll need to just say \'Treasure\' exactly as I have just done now, minus the quotation marks of course. And third, he'll ask you a pretty tricksy question that references a movie. It's best you just Google that one and copy/paste the top answer. And don't get confused why I know about such things. You ready? Let's go.")
    input("(enter) ")
    print("\nThe two of you approach the bridge and see a wizened old enchanter standing there. He looks you straight in the eye and seems to pierce into your soul.")
    print(f"{OLDMAN}")
    print("\tHe begins to speak: \"Stop, who would cross the Bridge of Death: Must answer me these questions three, 'ere the other side he see.\"")
    input("(enter) ")
    print("\n\"Okie-dokie,\" you say, \"Ask away.\"")
    your_name: str = input("\t\"What is your name?\" the man asks. [TYPE HERE]: ")
    if your_name != player:
        print(bridge_wrong)
        game_over()
        replay()
    elif your_name == player:
        point_increase()
        print(f"\n\"Correct, {player}.\"")
        your_quest: str = input("\n\t\"What is your quest?\" [TYPE HERE]: ")
        if your_quest != quest:
            print(bridge_wrong)
            game_over()
            replay()
        elif your_quest == quest:
            point_increase()
            print("\n\"Indeed.\"")
            swallow_answer: str = input("\n\"What is the air-speed velocity of an unladen swallow?\" [TYPE HERE]: ")
            if swallow_answer != swallow_first_option and swallow_answer != swallow_second_option:
                print(bridge_wrong)
                game_over()
                replay()
            elif swallow_answer == swallow_second_option or swallow_answer == swallow_first_option or swallow_answer == swallow_third_option:
                point_increase()
                print("\n\"Very good. You may pass.\" The enchanter steps aside and lets you onto the bridge. Unfortunately Hatman is unable to join you since when asked his own set of questions, he got stumped on the third one, which was \'What is your favorite color?\' You continue across the bridge alone. When you reach the other side, there is a mountainside surrounded by forest right in front of you.")
                input("(enter) ")
                ending()


if __name__ == "__main__":
    main()