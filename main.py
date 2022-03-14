import pgzrun
import time
import random

# screen dimensions
WIDTH = 1275
HEIGHT = 763
rect_screen = Rect((0, 0), (1275, 763))

#Starting Screen
boxes = []
for i in range(0,150):
    x = random.randint(0, 1275)
    y = random.randint(0, 763)
    boxes.append(Rect((x, y), (10, 10)))

# Buttons
main_screen_start_button = Rect((400, 325), (75, 60))

# Colors RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# In game or not
playing = False


"""Player images and coords"""

# Player Walking Animation
player_right = "player_right 1"
player_left = "player_left 1"
player_up = "player_back"
player_down = "player_front"
player = player_right
player_current = 0
player_images_right = [
    "player_right 1",
    "player_right 2",
    "player_right 3",
    "player_right 4",
    "player_right 5",
]
player_images_left = [
    "player_left 1",
    "player_left 2",
    "player_left 3",
    "player_left 4",
    "player_left 5",
]

# Player coordinates
player_x = 1
player_y = 20
player_x2 = 0
player_y2 = 0

"""Player Worth"""
correct_answers = 0
coins = 0
cosmetics = []
perks = []
skins = []

# Player Movement
moveable = True

"""Shop"""
shop_icon = "shop_icon"
rect_shop_icon = Rect((1225, 713), (50, 50))
shop = "shop"
shop_open = False
shop_display = True

"""Shop contents"""

perks_open = False
cosmetics_open = False
skins_open = False

rect_perks = Rect((744, 588), (186, 63))
rect_cosmetics = Rect((174, 629), (298, 64))
rect_skins = Rect((977, 351), (175, 56))
rect_exit = Rect((0, 0), (73, 43))

perks_mouse_click = (5000, 5000)
cosmetics_mouse_click = (5000, 5000)
skins_mouse_click = (5000, 5000)

# Cosmetics Shop
shop_cosmetics = "shop_cosmetics"
rect_halo = Rect((288, 151), (191, 84))

# Perks Shop
shop_perks = "shop_perks"
rect_speed_boost = Rect((978, 80), (206, 176))

# Skins Shop
shop_skins = "shop_skins"
rect_butter_alien = Rect((39, 422), (141, 189))

"""NPC Images"""


"""Maps"""

starting_map = "starting_map"
tutorial_map = "tutorial_map"
christian_map = "christian_map"
islam_map = "islam_map"

# Current map that will be changed
current_map = starting_map


"""Landing numbers on array"""
# 0 — Unrestricted block that can be walked on
# 1 — Restricted block that cannot be walked on
# 2 — Starting map --> Tutorial map


"""Restrictions for certain locations"""

# Christian (unlocked after tutorial)
christian = 0

# Christian Boss
christian_boss = 1

# Islam Boss
islam = 1



"""List of NPC's"""

# Starting Map

# Tutorial Map
# Guide
# Chris
# Bobby
# Jason
# Jing

# Christian Map
# Abdi
# Abilene
# Appolos
# Carmel
# Elon

"""Dialogue"""
# Regular Dialogue
dialogue = False
dialogue_box = "dialogue_box"
dialogue_box_rect = Rect((0, 638), (1275, 763))

# Boss Dialogue
boss_dialogue_box = "boss_dialogue_box"

# Boss Test
boss_test = False

# Counter for the order of dialogue for npcs
counter = 0

# Counter for the order of boss questions


# Click variable for dialogue continuation
mouse_click_pos = (5000, 5000)

# First message counted
first_msg_visited = False

"""Boss Test"""

# Boss Test Box
christian_boss_test_box = "boss_test_box1"

# Counter for the order of questions
boss_counter = 0

# Multiple Choice options
option_a = "option_a"
option_b = "option_b"
option_c = "option_c"
option_d = "option_d"
rect_option_a = Rect((0, 443), (638, 160))
rect_option_b = Rect((638, 443), (638, 160))
rect_option_c = Rect((0, 603), (638, 160))
rect_option_d = Rect((638, 603), (638, 160))


"""Interaction Messages List"""

# Tutorial Map
guide = [
    "Hi! Welcome to <Game Name>",
    "In this game you will explore many maps and learn about different religions",
    "The whole point of this game is to be more religiously aware, which will lead to religious acceptance",
]
chris = [
    "There are <number> of religions you can explore:",
    "Christianity",
    "Islam",
    "No religion",
    "Hinduism",
    "Buddhism",
    "Folk Religion",
    "Each religion has its own unique map with its own uniqe people and traditions",
]

jing = [
    "You will get to learn about the various aspects of a religion like",
    "Influence in the world",
]
jason = [
    "There will be tests at the end of each religion at the boss npc",
    "Each boss beat will give you money",
    "Money can be used to buy perks character including",
    "Teleportation, increased speed, and cosmetics",
]
bobby = [""]

# Christianity Map
abdi = [
    "Christianity has helped change cultures and civilizations for the better over its years of existence",
    "Christians recognize that every person is created in the image of God and, thus, equal beings",
    "They led the abolition of slavery in England and America",
    "Christians built churches, schools, orphanages,",
    "hospitals, homeless shelters, and soup kitchens",
    "As a result, Christianity has truly had a positive impact in this world",
]
abilene = [
    "There are many Christian holidays that people may not know are Christian",
    "Walk around to learn about some!"
]
appolos = [
    "Christmas Day, December 25 is a day of celebration (mainly for Western Christians)",
    "This special day is all about cherishing the birth of Jesus who Christians believes is the Christ",
    "and the divine son of God",
]
carmel = [
    "Easter Day or Easter Sunday is a day that commermorates the resurrection of Jesus as the Christ after Good Friday",
    "Easter eggs are distributed, they symbolize the new life which Christians experience and see at the heart of God's world",
]
elon = [
    "Hello there",
    "I am the Christian Boss",
    "Call me Elon",
    "I will be testing you on your knowledge of Christianity",
    "You will be rewarded if you succeed and punished if you fail",
    "Click anywhere to begin the test, and best of luck",
]

#Islamic Map
saeed = [
    "Welcome to the Islam Map. Walk around to interact with Muslims "
]
aaban = [
    "Islam influenced society and altered the course of history and today's world",
    "The rise of Islam influenced civil rights, education, and basis of life for millions of people",
    "Walk around to learn about some of Islam's impacts on society, holidays, and traditions"
]
aabid = [
    "Islam accelarated the evolution of civil rights while it was transmitted to other lands",
    "Before Islam, people lived in the el-ghaliya time period, meaning ignorance."
    "It was a time where people took advantage of power and treated others poorly"
    "However, with Islam's help, the el-ghaliya time period quickly diminished",
]
aayan = [
    "The word Islam means submission",
    "Islam advocates for peace, justice, and unity amongst mankind"
    "At the same time, it downplays violence, terrorism, and injustice.",
    "This Islamic principle has guided MILLIONS of muslims across the globe throughout history"
]
zara = [
    "Islam also has various holidays",
    "Walk around to learn about some!"
]
gamal = [
    "Muharram, otherwise known as The Islamic New Year, is a month that begins the Islamic year.",
    "It is celebrated quietly, with simple prayers, readings, and reflections"
]
oaghavanth = [
    "Eid al-Fitr, or the celebration concluding Ramadan, is a festival celebrating the end of the month of fasting, or Ramadan",
    "During this festival, people tend to dress in fine clothes, decorate their homes, gift children with treats, and visit friends and family",
    "The main theme of Eid al-Fitr if geneoristy and gratitude",
    "When the festival concludes, Muslims must share their blessings by feeding the poor and helping out in mosques (where they pray)"
]
oanez = [
    "Within Islam, there are five pillars that make up someone's faith to Islam",
    "The first is profession of faith, or shahada, which is the belief that God if the only god and Muhammad is the Messenger of God",
    "The second is prayer, or salat. Muslims pray 5 times a day at dawn, noon, mid-afternoon, sunset, and after dark.",
    "Next is Alms, or zakat, which means that Muslims donate a fixed portion of their income to people in need.",
    "Wealthy Muslims even build mosques, drinking fountains, schools, hospitals, and other related institutions for the sake of duty and blessings"
    "Second to last is Fasting, or swam, which is when adult Muslims have to abstain from food and drink. The whole point is to renew their awareness of Fod's blessings and to understand the less fortunate",
    "Pilgrimage, or haji, is the rule that every Muslim must visit the Ka'ba in the holy city of Mecca which muslims believe is the house built for God. They pray in the direction of the Ka'ba"
]

#Hindu Map
raahi = [
    "Hinduism is one of the oldest religions in the world.",
    "Walk around to explore the wonders of Hinduism!"
]
rusheek = [
    "Believe it or not, many aethiests in this world follow Hindu practices",
    "Yoga and meditation, for example, originated from Hindu faith",
    "Although it is not well-known, Lord Shiva Ganesha and Guatama Buddha are the Gods most often associated with yoga",
    "Yet, millions of people do yoga everyday, so people actually do something that comes from Hindu"
]
aachal = [
    "Ahimsa, or non-violence, is a common Hindu teaching.",
    "It applies to not only humans but animals as well",
    "This is why there are more and more vegetarians and vegans in the world: they were influenced by these Hindu teachings",
    ""
]
avikam = [
    ""
]
qumudini = [
    ""
]
ichacha = [
    ""
]
indravathi = [
    ""
]

# ALL BOSSES TEST QUESTIONS AND ANSWERS

elon_questions = [
    "Whhich of the following was introduced by Christians",
    "Who is the 'Christ' in Christianity",
    "Which of the following best describes the meaning of Easter eggs",
    "In what two locations did the Christians lead slavery abolition?",
]
elon_answers = ["a", "d", "a", "b"]

elon_answers_a = ["Homeless shelters", "Christians", "The new life of Christians", "North and South America" ]
elon_answers_b = ["Airports", "Moses", "Eggs that people eat as celebratory food", "America and England"]
elon_answers_c = ["Mosques", "God", "Resurrection of Jesus", "England and Canada"]
elon_answers_d = ["Food banks", "Jesus", "Christian's holy object", "England and Canada" ]

player_answers = ["e", "e", "e", "e"]

answer_counter = 0

"""Interaction Counter"""
boss_iteration = 0

# Christianity Map
christian_counter = ["abdi", "abilene", "appolos", "carmel"]

#Islam Map
islam_counter = []

"""Religions in the game"""
# Christianity (31.2%)
# Islam (24.1%)
# No religion (16%)
# Hinduism (15.1%)
# Buddhism (6.9%)
# Folk religions (5.7%)

"""Bot location generator"""
while True:
    print("Welcome to this religious awareness game!")
    try:
        player_name = str(input("Enter player name: "))
        if len(player_name) >= 10:
            print("Name cannot exceed 10 characters. Try again.")
        else:
            break
    except:
        print("Error. Try again")


def update():
    global player, player_x, player_y, player_x2, player_y2, player_current, moveable
    global current_map
    global dialogue, boss_test
    global npc, boss, boss_answers
    global christian_counter
    global christian, christian_boss
    global islam
    global boss_iteration
    global starting_map_array, tutorial_map_array, christian_map_array, islam_map_array

    walking_left = False
    walking_right = False
    walking_down = False
    walking_up = False

    player_x2 = player_x
    player_y2 = player_y

    if playing == True:
        if moveable == True:
            if keyboard.d:
                player_x2 += 0.5
                player = player_right
                walking_right = True
                walking_steps = 5
            if keyboard.a:
                player_x2 -= 0.5
                player = player_left
                walking_left = True
                walking_steps = 5
            if keyboard.w:
                player_y2 -= 0.5
                player = player_up
            if keyboard.s:
                player_y2 += 0.5
                player = player_down

        if walking_right == True:
            # here you need to check some counter
            # if it is time for next step to walk slower
            # but don't use `time.sleep()`
            if walking_steps > 0:
                player_current = (player_current + 1) % len(player_images_right)
                player = player_images_right[player_current]
                walking_steps -= 1
            else:
                walking_right = False

        if walking_left == True:
            # here you need to check some counter
            # if it is time for next step to walk slower
            # but don't use `time.sleep()`
            if walking_steps > 0:
                player_current = (player_current + 1) % len(player_images_left)
                player = player_images_left[player_current]
                walking_steps -= 1
            else:
                walking_left = False

        """
        ALL 2D MAP ARRAYS
        """

        #STARTING MAP ARRAY
        starting_map_array = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,christian,christian,christian,christian,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        [1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

        tutorial_map_array = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,0,0,4,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1],
        [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,1,1],
        [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [2,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1],
        [1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1],
        [1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1],
        [1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1],
        [1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1],
        [1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1],
        [1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1],
        [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1],
        [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1],
        [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
        [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
        [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
        [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
        [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
        [1,1,1,1,0,0,0,0,0,7,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,6,0,0,0,0,0,0,0,1,1,1,1],
        [1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

        christian_map_array = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,0,0,0,0,0,0,1,1,1,7,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
        [1,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,8],
        [1,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,8],
        [1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1],
        [1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1],
        [1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1],
        [1,1,0,0,0,0,0,0,0,3,1,1,1,0,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1],
        [1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1],
        [1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1],
        [1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,0,0,1,1],
        [1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,5,0,1,1,0,0,1,1],
        [1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,0,0,1,1],
        [1,1,0,0,0,0,0,0,1,1,1,1,1,christian_boss,christian_boss,christian_boss,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1],
        [1,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,1,1,1,0,4,0,1,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,1,1,1,1,1,1,0,0,1,1],
        [1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,0,0,1,1],
        [1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,0,0,1,1],
        [1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,0,0,1,1],
        [1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

        islam_map_array = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
        [1,0,3,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,4,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
        [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,islam,islam,islam,islam,islam,islam,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,islam,islam,islam,islam,islam,islam,islam,islam,islam,islam,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,islam,islam,islam,islam,islam,10,islam,islam,islam,islam,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,islam,islam,islam,islam,islam,islam,islam,islam,islam,islam,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,islam,islam,islam,islam,islam,islam,islam,islam,islam,islam,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,islam,islam,islam,islam,islam,islam,islam,islam,islam,islam,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [2,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,islam,islam,islam,islam,islam,islam,islam,islam,islam,islam,0,0,9,0,0,0,0,0,0,0,0,0,0,1],
        [2,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,islam,islam,islam,islam,islam,islam,islam,islam,islam,islam,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [2,0,0,7,0,0,0,0,0,0,1,0,0,0,0,0,islam,islam,islam,islam,islam,islam,islam,islam,islam,islam,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [2,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,islam,islam,islam,islam,islam,islam,islam,islam,islam,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [2,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,islam,islam,islam,islam,islam,islam,islam,islam,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [2,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,islam,islam,islam,islam,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
        [1,0,6,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,5,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

        # Determine which map is the player currently on
        if current_map == starting_map:

            # Conditions in starting map array

            # 0 — Safe space
            if starting_map_array[round(player_y2)][round(player_x2)] == 0:
                player_x = player_x2
                player_y = player_y2

            # 1 Solid space

            # 2 Starting map --> Tutorial map
            if starting_map_array[round(player_y2)][round(player_x2)] == 2:
                christian = 0
                current_map = tutorial_map
                player_x = 1
                player_y = 19

            # 3 Starting map --> Western map
            if starting_map_array[round(player_y2)][round(player_x2)] == 3:
                current_map = christian_map
                player_x = 25
                player_y = 38

        if current_map == tutorial_map:

            # Conditions in tutorial map array

            # 0 — Safe space
            if tutorial_map_array[round(player_y2)][round(player_x2)] == 0:
                player_x = player_x2
                player_y = player_y2

            # 1 Solid Space

            # 2 Tutorial map --> Starting map
            if tutorial_map_array[round(player_y2)][round(player_x2)] == 2:
                current_map = starting_map
                player_x = 38
                player_y = 20

            # 3 Interaction with Guide
            if tutorial_map_array[round(player_y2)][round(player_x2)] == 3:
                dialogue = True
                npc = guide

            # 4 Interaction with Chris
            if tutorial_map_array[round(player_y2)][round(player_x2)] == 4:
                dialogue = True
                npc = chris

            # 5 Interaction with Jing
            if tutorial_map_array[round(player_y2)][round(player_x2)] == 5:
                dialogue = True
                npc = jing

            # 6 Interaction with Jason
            if tutorial_map_array[round(player_y2)][round(player_x2)] == 6:
                dialogue = True
                npc = jason

            # 7 Interaction with Bobby
            if tutorial_map_array[round(player_y2)][round(player_x2)] == 7:
                dialogue = True
                npc = bobby

        if current_map == christian_map:

            if christian_map_array[round(player_y2)][round(player_x2)] == 0:
                player_x = player_x2
                player_y = player_y2

            if christian_map_array[round(player_y2)][round(player_x2)] == 2:
                current_map = starting_map
                player_x = 23
                player_y = 1

            # 3 Interaction with Abdi
            if christian_map_array[round(player_y2)][round(player_x2)] == 3:
                dialogue = True
                christian_counter.append("abdi")
                npc = abdi

            # 4 Interaction with Abilene
            if christian_map_array[round(player_y2)][round(player_x2)] == 4:
                dialogue = True
                christian_counter.append("abilene")
                npc = abilene

            # 5 Interaction with Appolos
            if christian_map_array[round(player_y2)][round(player_x2)] == 5:
                dialogue = True
                christian_counter.append("appolos")
                npc = appolos

            # 6 Interaction with Carmel
            if christian_map_array[round(player_y2)][round(player_x2)] == 6:
                dialogue = True
                christian_counter.append("carmel")
                npc = carmel

            # 7 Interaction with Elon
            if christian_map_array[round(player_y2)][round(player_x2)] == 7:
                dialogue = True
                boss_test = True
                npc = elon
                boss = elon_questions
                boss_answers = elon_answers

            if christian_map_array[round(player_y2)][round(player_x2)] == 8:
                current_map = islam_map
                player_x = 1
                player_y = 19

        if current_map == islam_map:

            if islam_map_array[round(player_y2)][round(player_x2)] == 0:
                player_x = player_x2
                player_y = player_y2

            if islam_map_array[round(player_y2)][round(player_x2)] == 2:
                current_map = christian_map
                player_x = 38
                player_y = 15

            if islam_map_array[round(player_y2)][round(player_x2)] == 3:
                dialogue = True
                islam_counter.append("aayan")
                npc = aayan

            if islam_map_array[round(player_y2)][round(player_x2)] == 4:
                dialogue = True
                islam_counter.append("oaghavanth")
                npc = oaghavanth

            if islam_map_array[round(player_y2)][round(player_x2)] == 5:
                dialogue = True
                islam_counter.append("gamal")
                npc = gamal

            if islam_map_array[round(player_y2)][round(player_x2)] == 6:
                dialogue = True
                islam_counter.append("zara")
                npc = zara

            if islam_map_array[round(player_y2)][round(player_x2)] == 7:
                dialogue = True
                islam_counter.append("saeed")
                npc = saeed

            if islam_map_array[round(player_y2)][round(player_x2)] == 8:
                dialogue = True
                islam_counter.append("aaban")
                npc = aaban

            if islam_map_array[round(player_y2)][round(player_x2)] == 9:
                dialogue = True
                islam_counter.append("aabid")
                npc = aabid

            if islam_map_array[round(player_y2)][round(player_x2)] == 10:
                dialogue = True
                islam_counter.append("oanez")
                npc = oanez


        #Conditions needed to unlock christian boss
        if (
            christian_counter.count("abdi") >= 1
            and christian_counter.count("abilene") >= 1
            and christian_counter.count("appolos") >= 1
            and christian_counter.count("carmel") >= 1
        ):
            christian_boss = 0

        #Conditions needed to unlock islam boss
        if (
            islam_counter.count("aayan") >= 1
            and islam_counter.count("oaghavanth") >= 1
            and islam_counter.count("gamal") >= 1
            and islam_counter.count("zara") >= 1
            and islam_counter.count("saeed") >= 1
            and islam_counter.count("aaban") >= 1
            and islam_counter.count("aabid") >= 1
        ):
            islam = 0

    #Animation for home screen
    if playing == False:
        for i in boxes:
            i.x += 2
            i.y += 2

            if i.x > WIDTH:
              i.x = 0

            if i.y > HEIGHT:
              i.y = 0


#Finding the location of each mouse click
def on_mouse_down(pos):
    global mouse_click_pos, shop_mouse_click
    global perks_mouse_click, cosmetics_mouse_click, skins_mouse_click
    global playing
    global dialogue
    global counter
    global npc

    #Assigning a variable to mouse click pos when player is in dialogue
    if dialogue == True:
        mouse_click_pos = pos
    #Assigning a variable to mouse click pos when player is in test
    if boss_test == True and dialogue == False:
        mouse_click_pos = pos
    #Start of game button
    if main_screen_start_button.collidepoint(pos):
        playing = True
    #Assign a variable to shop menu if main shop is open
    if (
        shop_display == True
        and perks_open == False
        and cosmetics_open == False
        and skins_open == False
    ):
        shop_mouse_click = pos
    #Assigning a variable to each sub shop
    if shop_open == True:
        if perks_open == True:
            perks_mouse_click = pos
        elif cosmetics_open == True:
            cosmetics_mouse_click = pos
        elif skins_open == True:
            skins_mouse_click = pos

#Checks answers of player answer
def check_answers(b_counter, b_answers, p_answers):
    global correct_answers

    #Answer correct adds to correct answer count and advances one in question
    if b_answers[b_counter] == p_answers[b_counter]:
        b_counter += 1
        correct_answers += 1
    #Answer wrong simply adds to one in question
    else:
        print("Wrong")
        b_counter += 1
    return b_counter, correct_answers

def mouse_adjustment(shoptype_click_pos):
    global shop_mouse_click, perks_mouse_click, skins_mouse_click, cosmetics_mouse_click
    global perks_open, skins_open, cosmetics_open

    if shoptype_click_pos == perks_mouse_click:
        shop_mouse_click = (5000, 5000)
        perks_mouse_click = (5000, 5000)
        perks_open = False
    elif shoptype_click_pos == skins_mouse_click:
        shop_mouse_click = (5000, 5000)
        skins_mouse_click = (5000, 5000)
        skins_open = False
    elif shoptype_click_pos == cosmetics_mouse_click:
        shop_mouse_click = (5000, 5000)
        cosmetics_mouse_click = (5000, 5000)
        cosmetics_open = False

def draw():

    global player_x, player_x2, player_y, player_y2
    global counter, boss_counter, boss_iteration
    global elon
    global dialogue, boss_test
    global mouse_click_pos
    global shop_mouse_click, perks_mouse_click, cosmetics_mouse_click, skins_mouse_click
    global moveable
    global player_answers, correct_answers, answer_counter
    global coins, cosmetics, skins, perks
    global shop_display, shop_open
    global perks_open, cosmetics_open, skins_open

    if playing:  # in game
        clock.tick(60)
        screen.clear()
        screen.fill(BLACK)
        screen.blit(
            current_map, ((WIDTH / 2) - (player_x * 32), (HEIGHT / 2) - (player_y * 32))
        )
        screen.blit(player, (WIDTH / 2, HEIGHT / 2))

        # Dialogue draws based on map and npc
        if dialogue == True:
            moveable = False

            if counter < len(npc):
                screen.blit(dialogue_box, (0, 588))
                screen.draw.text(npc[counter], (50, 662.5), color="white", fontsize=25)
                if rect_screen.collidepoint(mouse_click_pos):
                    mouse_click_pos = (5000, 5000)
                    counter += 1
            else:
                dialogue = False
                moveable = True
                counter = 0

        if boss_test == True and dialogue == False and boss_iteration == 0:
            moveable = False

            if boss_counter < len(boss):
                screen.blit(christian_boss_test_box, (0, 0))
                screen.draw.text(
                boss[boss_counter], (50, 140), color="red", fontsize=50
                )
                #Draws questions and multiple choice outlines
                screen.blit(option_a, (0, 443))
                screen.blit(option_b, (638, 443))
                screen.blit(option_c, (0, 603))
                screen.blit(option_d, (638, 603))
                screen.draw.text(elon_answers_a[answer_counter], (100,520), color="black", fontsize=35)
                screen.draw.text(elon_answers_b[answer_counter], (738,520), color="black", fontsize=35)
                screen.draw.text(elon_answers_c[answer_counter], (100,680), color="black", fontsize=35)
                screen.draw.text(elon_answers_d[answer_counter], (738,680), color="black", fontsize=35)

                #Tracks which option the player clicks and calculates whether it got it wrong or right
                if rect_option_a.collidepoint(mouse_click_pos):
                    mouse_click_pos = (5000, 5000)
                    player_answers[boss_counter] = "a"
                    boss_counter, correct_answers = check_answers(
                        boss_counter, boss_answers, player_answers
                    )
                    answer_counter += 1

                elif rect_option_b.collidepoint(mouse_click_pos):
                    mouse_click_pos = (5000, 5000)
                    player_answers[boss_counter] = "b"
                    boss_counter, correct_answers = check_answers(
                        boss_counter, boss_answers, player_answers
                    )
                    answer_counter += 1

                elif rect_option_c.collidepoint(mouse_click_pos):
                    mouse_click_pos = (5000, 5000)
                    player_answers[boss_counter] = "c"
                    boss_counter, correct_answers = check_answers(
                        boss_counter, boss_answers, player_answers
                    )
                    answer_counter += 1

                elif rect_option_d.collidepoint(mouse_click_pos):
                    mouse_click_pos = (5000, 5000)
                    player_answers[boss_counter] = "d"
                    boss_counter, correct_answers = check_answers(
                        boss_counter, boss_answers, player_answers
                    )
                    answer_counter += 1
            #End of test — quick summary of player's performance
            else:
                screen.clear()
                screen.draw.text(
                    "You got "
                    + str(correct_answers)
                    + " correct answer(s) out of "
                    + str(len(elon_questions))
                    + " questions",
                    (30, 400),
                    color="green",
                    fontsize=50,
                )
                screen.draw.text(
                    "+ " + str(50 * correct_answers) + " coins",
                    (30, 435),
                    color="green",
                    fontsize=50,
                )
                screen.draw.text(
                    "Click anywhere to exit", (30, 600), color="white", fontsize=25
                )
                #Prevents boss to be accessed again
                if npc == elon:
                    elon = ["You can only face Elon once"]
                #When user clicks the result screen
                if rect_screen.collidepoint(mouse_click_pos):
                    boss_iteration = 1
                    coins += 50 * correct_answers
                    moveable = True
                    boss_test = False
                    boss_counter = 0
                    correct_answers = 0
                    player_answers = ["e", "e", "e", "e"]

        #Shop icon drawing in the bottom right
        if shop_display == True:
            screen.blit(shop_icon, (1225, 713))
            if rect_shop_icon.collidepoint(shop_mouse_click):
                shop_open = True
        #Shop menus — open or not
        if shop_open == True:
            moveable = False
            screen.clear()
            screen.blit(shop, (0, 0))
            if rect_perks.collidepoint(shop_mouse_click):
                perks_open = True
            elif rect_cosmetics.collidepoint(shop_mouse_click):
                cosmetics_open = True
            elif rect_skins.collidepoint(shop_mouse_click):
                skins_open = True
            elif rect_exit.collidepoint(shop_mouse_click):
                moveable = True
                shop_open = False
            #If a sub shop is open, draw the according shop image and items to screen
            if perks_open == True:
                screen.clear()
                screen.blit(shop_perks, (0, 0))
                if rect_exit.collidepoint(perks_mouse_click):
                    mouse_adjustment(perks_mouse_click)
            elif skins_open == True:
                screen.clear()
                screen.blit(shop_skins, (0, 0))
                if rect_exit.collidepoint(skins_mouse_click):
                    mouse_adjustment(skins_mouse_click)
            elif cosmetics_open == True:
                screen.clear()
                screen.blit(shop_cosmetics, (0, 0))
                if rect_exit.collidepoint(cosmetics_mouse_click):
                    mouse_adjustment(cosmetics_mouse_click)
    #Home screen
    else:  # title screen
        screen.fill(WHITE)
        screen.draw.text("MEET DIFFERENT PEOPLE ", (300, 0), color="green", fontsize=40)
        screen.draw.text("Start", (425, 350), color="black", fontsize=20)
        screen.draw.rect(main_screen_start_button, "black")
        for i in range(len(boxes)):
            screen.draw.filled_rect(boxes[i], "red")

#Execute all code above
pgzrun.go()
