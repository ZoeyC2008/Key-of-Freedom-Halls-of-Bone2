# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define totum = Character("Totum", color="#ed820e")
define tian = Character("Tian de'Meng", color="#005cb8")

#variables
default silver = 0
default agate = 0
default bone = 0

default buying = ""
default selling =""

default inventory = []

default min_buy = 0
default max_buy = 0
default buy_money = 0

default max_sell = 0
default sell_money = 0

default eyes_num = 2
default lungs_num = 2
default ribs_num = 24
default nerves_num = 1
default liver_num = 3
default skin_num = 1
default limbs_num = 4
default injury = ""

#opening
image op 1 = "images/opening/op1.png"
image op 2 = "images/opening/op2.png"
image op 3 = "images/opening/op3.png"
image op 4 = "images/opening/op4.png"
image op 5 = "images/opening/op5.png"

#person
image person = "images/person/person.png"
image person arm = "images/person/personnoarm.png"
image person eye = "images/person/personnoeye.png"
image person stomach = "images/person/personnokidney.png"
image person lung = "images/person/personnolung.png"
image person skin = "images/person/personnoskin.png"

#characters
image totum = "images/characters/totum.png"
image tian = "images/characters/lgneutral.png"
image tian happy = "images/characters/lghappy.png"

#backgrounds
image bg blue = "#add8e6"
image bg totum store = "images/bgs/totum_shop.png"

#cutscene
image cutscene death = "images/cutscenes/death.png"

#position
#define lg_ypos = 
define pos_lg_slightly_left = Position(xalign=0.15, ypos=850)
define pos_person = Position(xalign=0.35, yalign=0.5)
# The game starts here.


label start:
    jump opening_sequence

    return

label opening_sequence:
    scene op 1
    pause

    scene op 2
    pause

    scene op 3
    pause

    scene op 4
    pause

    scene op 5
    pause

    jump totum_store

label totum_store:
    scene bg totum store
    show totum at center
    show tian at pos_lg_slightly_left

    tian "Alright, Totum is generally a fair person."
    tian "Let's practive by buying some nightmare flowers."
    totum "They don't have money."
    tian "That's fine!"
    tian "I've given them some coinage, in silver of course."
    $ silver += 100
    tian "Totum doesn't like dealing in anything else, but in these isles agate and bone are more than common currencies."
    tian "But if that's not enough..."
    tian "Well, Totum, you still have the ceremonial knife don't you?"
    tian "We can always pay in blood!"
    tian "What you need to do is go to the 'behold yourself' tab. Since humans are made of so many useles parts, I'm sure you can spare some to pay for the nightmare flowers."

    jump totum_menu

label totum_menu:
    scene bg totum store
    show totum at center
    show tian at pos_lg_slightly_left

    menu:
        "(Look at the items on sale.)":
            jump totum_buy
        "(Check money)":
            jump money
        "(Behold yourself.)":
            jump behold_self


label totum_buy:
    scene bg totum store
    show totum at center
    show tian at pos_lg_slightly_left
    "Totum has many different products."
    menu:
        "A Silver Blade":
            $ buying = "silver_blde"
        "A Agate Blade":
            $ buying = "agate_blade"
        "A Bone Blade":
            $ buying = "bone_blade"
        "A Paper Boat":
            $ buying = "paper_boat"
        "A Feathered Boat":
            $ buying = "feathered_boat"
        "A Singular Nightmare Flower":
            $ buying = "nightmare_flower"
    jump totum_buying

label money:
    "You have [silver] silver, [agate] agate, and [bone] bone."

label behold_self:
    scene bg blue

    if injury == "chest":
        show person lung at pos_person
    elif injury == "middle":
        show person stomach at pos_person
    elif injury == "flayed":
        show person skin at pos_person
    elif injury == "eye":
        show person eye at pos_person
    elif injury == "limb":
        show person arm at pos_person
    else:
        show person at pos_person

    "You're in Totum's shop, he'd be happy to lend you a knife."
    menu:
        "Heart":
            $ selling = "heart"
            jump no_heart
        "Lungs":
            $ selling = "lung"
            $ injury = "chest"
            $ lungs_num -= 1
            if (lungs_num < 0):
                jump no_organ
        "Liver":
            $ selling = "liver"
            $ injury = "middle"
            $ liver_num -= 1
            if (liver_num < 0):
                jump no_organ
        "Nerves":
            $ selling = "nerve"
            $ injury = "flayed"
            $ nerves_num -= 1
            if (nerves_num < 0):
                jump no_organ
        "Skin":
            $ selling = "skin"
            $ injury = "flayed"
            $ skin_num -= 1
            if (skin_num < 0):
                jump no_organ
        "Eyes":
            $ selling = "eye"
            $ injury = "eye"
            $ eyes_num -= 1
            if (eyes_num < 0):
                jump no_organ
        "Ribs":
            $ selling = "rib"
            $ injury = "chest"
            $ ribs_num -= 1
            if (ribs_num < 0):
                jump no_organ
        "Limb":
            $ selling = "limb"
            $ injury = "limb"
            $ limbs_num -= 1
            if (limbs_num < 0):
                jump no_organ
    jump totum_selling

label no_heart:
    show cutscene death

    tian "You are an idiot."
    tian "Humans can't live without their heart."
    return

label no_organ:
    show cutscene death

    tian "You are an idiot."
    tian "Huamns don't have that many organs."
    return

label totum_selling:
    if selling == "lung":
        $ max_sell = 200
        tian "A lung, necessary for breathing."
    elif selling == "liver":
        $ max_sell = 150
        tian "Part of a liver, can detoxify blood."
    elif selling == "nerves":
        $ max_sell = 160
        tian "Nerves, the information highway for the brain."
    elif selling == "skin":
        $ max_sell = 440
        tian "Skin, something that keeps everything together."
    elif selling == "eye":
        $ max_sell = 125
        tian "Eyes, a way to process the world."
    elif selling == "rib":
        $ max_sell = 35
        tian "Ribs protect your squishy innards."
    elif selling == "limb":
        $ max_sell = 335
        tian "Limbs, something that moves, I think, it's not like I have limbs."

    scene bg totum store
    show totum at center
    show tian at pos_lg_slightly_left

    #bargin time
    $ sell_money = renpy.input("Enter a number (0-1000):")

    # Convert to integer safely
    $ sell_money = int(sell_money.strip() or 0)

    # Clamp value between 0 and 1000
    $ sell_money = max(0, min(1000, sell_money))

    if (sell_money < max_sell):
        totum "Yes...A good deal."
        $ silver += sell_money
    else:
        totum "Sorry, I'm not willing to pay that much."
        tian "You are an idiot."
        tian "Why would you let Totum cut out your organ before agreeing on a price??"
    jump totum_menu


label totum_buying:
    
    if buying == "silver_blade":
        $ min_buy = 150
        $ max_buy = 300
        totum "Purified silver, more or less. Cuts through flesh perfectly and the wound won't even be infected, probably. Can be used for organs and sacrificial blood, so long as you don't min_buyd the somewhat imprecise wound."
    elif buying == "agate_blade":
        $ min_buy = 300
        $ max_buy = 400
        totum "Freshly quartered agate, good at quartering flesh. Will be able to carefully cut at any organ, so long as you know where it is. You most certainly don't want to cut your aorta while trying to get a lung."
    elif buying == "bone_blade":
        $ min_buy = 450
        $ max_buy = 600
        totum "Not as good as a blade from your own bone, but a stranger will have to do. You don't want to give up a limb just yet, do you? This blade shall find its way through your flesh, and it shall obtain exactly what is needed, no more, no less."
    elif buying == "paper_boat":
        $ min_buy = 180
        $ max_buy = 350
        totum "Cheap, but reliable. This boat will get you between islands just fine, as long as you're light, that is."
    elif buying == "feathered_boat":
        $ min_buy = 600
        $ max_buy = 750
        totum "Made from the plucked feathers of a thousand swans, this boat will keep you afloat even through the worst of storms."
    elif buying == "nightmare_flower":
        $ min_buy = 110
        $ max_buy = 150
        totum "Pretty, but cheap, and maybe just fine enough of a gift."
    
    totum "It'll cost [max_buy] silver."

    #bargin time
    $ buy_money = renpy.input("Enter a number (0-1000):")

    # Convert to integer safely
    $ buy_money = int(buy_money.strip() or 0)

    # Clamp value between 0 and 1000
    $ buy_money = max(0, min(1000, buy_money))

    if (buy_money > min_buy):
        if (silver < buy_money):
            totum "Ah, but you don't have enough money to pay."
            tian "Better, use some of your body."
            tian "Totum's being very generous, letting you use his knifes for free."
        else:
            totum "We have a deal!"
            $ inventory.append(buying)
            $ silver -= buy_money
    else:
        totum "Sorry, but I refuse that price."
    jump totum_menu

