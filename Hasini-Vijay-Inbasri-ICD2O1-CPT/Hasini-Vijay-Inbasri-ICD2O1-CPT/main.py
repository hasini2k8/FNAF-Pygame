"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
pygame.mixer.init()

# Defining some important colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_RED = (82, 15, 28)
GREY = (61, 56, 57)
BLACK = (0, 0, 0)
BROWN = (79, 56, 26)
PEACH = (245, 202, 157)
BLUE = (34, 46, 133)
DARK_GREEN = (29, 94, 47)

#Adding the sleep time variable depending on the script and the number of questions played in each round
SLEEP_TIME = 2
Q_IN_EACH_ROUND = 3

#Importing sys, random and time libraries
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#Heading of game
pygame.display.set_caption("Evan's Quest")

#All the Audio files
click_sound = pygame.mixer.Sound("five-nights-at-freddys-6-am.ogg")
jumpscare_audio = pygame.mixer.Sound("jumpscare-sound-fnaf-4.ogg")
bite_sound = pygame.mixer.Sound("bite_audio.mpeg.ogg")
ballora_sound = pygame.mixer.Sound("ballora-music-box.mp3")
music_box_sound = pygame.mixer.Sound("puppet-music-box.mp3")
static_sound = pygame.mixer.Sound("fnaf-1-music-box.mp3")
button_sound = pygame.mixer.Sound("button-click.mp3")
light_sound = pygame.mixer.Sound("light-flicker.mp3")
begin_sound = pygame.mixer.Sound("voice_button.mp3")
night_3_sound = pygame.mixer.Sound("night-3-theme.ogg")
sad_sound = pygame.mixer.Sound("sad_audio.ogg")
night_5_sound = pygame.mixer.Sound("night-5-audio.mp3")
voicelines = pygame.mixer.Sound("evan_voicelines.mp3")
end_scene = pygame.mixer.Sound("freddy-beatbox.mp3")
# Fonts
font = pygame.font.Font(None, 36)

#Some variables defined like:
done = False #starting the game
current_screen = "start" #prevent the mouse button play from playing again
bg_screen_loaded = False
play_clicked = False#prevent the play button from getting activated again after being clicked
life_count = 3 #number of lives
night_level = 1 #night levels
questions_list = [] #questions file reading

#Reading the questions from the questions.txt and reading them
#Extra out of syllabus code from Udemy course: Dict
def read_questions_from_file(file):
  global questions_list
  list = []

  input_file = open(file, "r")
  file_text = input_file.readlines()

  for line in file_text:
    dict = {}
    a = line[:-1].split(',')
    dict.update({"question": a[0]})
    dict.update({"answers": a[1:5]})
    dict.update({"correct_answer": a[5]})
    list.append(dict)

  questions_list = list

#initializing variables for the actual game
def initialize_game():
  global bg_screen_loaded
  global play_clicked
  global life_count
  global night_level
  read_questions_from_file("questions.txt")

  bg_screen_loaded = False
  play_clicked = False
  life_count = 3
  night_level = 1

#drawing the play game button on start screen
def draw_button():
  pygame.draw.rect(screen, (130, 22, 42), (350, 200, 100, 50))
  pygame.draw.rect(screen, BLACK, (350, 200, 100, 50), 3)
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('Play', True, WHITE)
  screen.blit(text_surface, (370, 215))

#Drawing the cry evan picture for the start screen
def cry_evan():
  pygame.draw.rect(screen, (245, 202, 157), (50, 120, 150, 90))  #face
  pygame.draw.rect(screen, BLACK, (70, 150, 30, 30))  # Evan's 1st eye
  pygame.draw.rect(screen, BLACK, (150, 150, 30, 30))  # Evan's 2nd eye
  pygame.draw.rect(screen, (3, 255, 251), (70, 180, 30, 30))  #tear
  pygame.draw.rect(screen, (3, 255, 251), (150, 180, 30, 30))  #tear 2
  pygame.draw.rect(screen, (79, 56, 26), (50, 80, 150, 40))  #hair
  pygame.draw.rect(screen, BROWN, (30, 100, 20, 60))  #hair
  pygame.draw.rect(screen, BROWN, (200, 100, 20, 60))  #hair
  pygame.draw.rect(screen, BROWN, (110, 120, 30, 10))  #hair
  pygame.draw.rect(screen, BROWN, (130, 120, 15, 30))  #hair
  pygame.draw.rect(screen, (245, 202, 157), (100, 210, 50, 10))  #neck
  pygame.draw.rect(screen, BLACK, (50, 220, 150, 150))  #shirt
  pygame.draw.rect(screen, (138, 138, 138), (50, 250, 150, 20))  #shirt stripe
  pygame.draw.rect(screen, (138, 138, 138), (50, 280, 150, 20))  #shirt stripe
  pygame.draw.rect(screen, BLUE, (50, 330, 150, 40))  #pant base
  pygame.draw.polygon(screen, BLUE, ((50, 330), (150, 330), (110, 400),
                                     (50, 400)))  #pant leg one
  pygame.draw.polygon(screen, BLUE, ((110, 330), (200, 330), (200, 400),
                                     (140, 400)))  #pant 2
  pygame.draw.rect(screen, BLACK, (30, 220, 50, 50))  #hand
  pygame.draw.rect(screen, PEACH, (40, 270, 30, 50))  #hand
  fredbear_image = pygame.image.load('fredbear.png')
  # Resize the image
  fredbear_image = pygame.transform.scale(fredbear_image, (80, 80))
  screen.blit(fredbear_image, (80, 250))
  pygame.draw.rect(screen, PEACH, (40, 310, 100, 20))
  pygame.draw.rect(screen, BLACK, (180, 220, 50, 50))  #hand
  pygame.draw.rect(screen, PEACH, (200, 270, 20, 50))  #hand
  pygame.draw.rect(screen, PEACH, (190, 310, 40, 30))  #hand
  flashlight_image = pygame.image.load('flashlight.png')
  flashlight_image = pygame.transform.scale(flashlight_image, (150, 150))
  screen.blit(flashlight_image, (200, 250))#Flshlight

#Drawing the non-cry-evan for the start screen
def non_cry_evan():
  pygame.draw.rect(screen, (245, 202, 157), (50, 120, 150, 90))  #face
  pygame.draw.rect(screen, BLACK, (70, 150, 30, 30))  # Evan's 1st eye
  pygame.draw.rect(screen, BLACK, (150, 150, 30, 30))  # Evan's 2nd eye
  pygame.draw.rect(screen, (79, 56, 26), (50, 80, 150, 40))  #hair
  pygame.draw.rect(screen, BROWN, (30, 100, 20, 60))  #hair
  pygame.draw.rect(screen, BROWN, (200, 100, 20, 60))  #hair
  pygame.draw.rect(screen, BROWN, (110, 120, 30, 10))  #hair
  pygame.draw.rect(screen, BROWN, (130, 120, 15, 30))  #hair
  pygame.draw.rect(screen, (245, 202, 157), (100, 210, 50, 10))  #neck
  pygame.draw.rect(screen, BLACK, (50, 220, 150, 150))  #shirt
  pygame.draw.rect(screen, (138, 138, 138), (50, 250, 150, 20))  #shirt stripe
  pygame.draw.rect(screen, (138, 138, 138), (50, 280, 150, 20))  #shirt stripe
  pygame.draw.rect(screen, BLUE, (50, 330, 150, 40))  #pant base
  pygame.draw.polygon(screen, BLUE, ((50, 330), (150, 330), (110, 400),
                                     (50, 400)))  #pant leg one
  pygame.draw.polygon(screen, BLUE, ((110, 330), (200, 330), (200, 400),
                                     (140, 400)))  #pant 2
  pygame.draw.rect(screen, BLACK, (30, 220, 50, 50))  #hand
  pygame.draw.rect(screen, PEACH, (40, 270, 30, 50))  #hand
  fredbear_image = pygame.image.load('fredbear.png')
  # Resize the image
  fredbear_image = pygame.transform.scale(fredbear_image, (80, 80))
  screen.blit(fredbear_image, (80, 250))
  pygame.draw.rect(screen, PEACH, (40, 310, 100, 20))
  pygame.draw.rect(screen, BLACK, (180, 220, 50, 50))  #hand
  pygame.draw.rect(screen, PEACH, (190, 310, 40, 30))  #hand
  flashlight_image = pygame.image.load('flashlight.png')
  flashlight_image = pygame.transform.scale(flashlight_image, (150, 150))
  screen.blit(flashlight_image, (200, 250))#flashlight


# Introduction Screen - Drawing the TV static glitch animation
def draw_static():
  for y in range(0, HEIGHT, 5):
    for x in range(0, WIDTH, 5):
      color = random.choice([DARK_RED, GREY
                             ])  # Randomly choose between dark red and grey
      pygame.draw.rect(screen, color, (x, y, 5, 5))

#Introduction Screen - fredbears lines for the introduction
def fredbears_lines():

  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('Tommorow is another day..', True,
                                    (252, 205, 76))
  screen.blit(text_surface, (400, 200))
  pygame.display.flip()
  fredbear_image = pygame.image.load('fredbear.png')
  # Resize the image
  fredbear_image = pygame.transform.scale(fredbear_image, (300, 350))
  screen.blit(fredbear_image, (100, 200))
  pygame.display.flip()

#3 Night 4 - bullies arriving scene
bullies_arrive = True
def three_bullies_arrive():
  speed = 5
  image = pygame.image.load('fnaf_bullies.png')
   # Resize the image
  image = pygame.transform.scale(image, (200, 200))
  image_rect = image.get_rect()
  x, y = 0, 180
  global bullies_arrive
  if bullies_arrive == True:
      for i in range(50):
        x += speed
        bite_interaction_bg()
        new_image = pygame.image.load('8_bit_evan_cry_hide.png')
         # Resize the image
        new_image = pygame.transform.scale(new_image, (100, 50))
        screen.blit(new_image, (550, 320))
        screen.blit(image, (x, y))
        pygame.display.flip()
        clock.tick(60)

  bullies_arive = False

#Night 5 - background
def bite_interaction_bg():
  screen.fill(GREY)
  x = 100
  for i in range(5):
    pygame.draw.line(screen, (84, 89, 85),(x,0),(x,400),50)
    pygame.draw.line(screen, (84, 89, 85),(x+20,0),(x+20,400),20)
    x += 200
  pygame.draw.rect(screen, (158, 44, 63), (300, 100, 300, 300))
  pygame.draw.line(screen, (74, 57, 37), (450, 100), (450, 400), 10)
  pygame.draw.rect(screen, (74, 57, 37), (300, 100, 300, 300), 10)
  pygame.draw.line(screen, BLACK, (650, 200), (630, 307), 3)
  pygame.draw.line(screen, BLACK, (630, 190), (630, 307), 3)
  pygame.draw.line(screen, BLACK, (600, 190), (620, 307), 3)
  pygame.draw.line(screen, BLACK, (650, 200), (630, 307), 3)
  pygame.draw.line(screen, BLACK, (650, 200), (630, 307), 3)
  pygame.draw.circle(screen, GREEN, (660, 180), 25)
  pygame.draw.circle(screen, RED, (630, 200), 25)
  pygame.draw.circle(screen, (181, 177, 45), (620, 150), 25)
  pygame.draw.circle(screen, (84, 32, 97), (600, 190), 25)
  pygame.draw.circle(screen, (70, 142, 184), (630, 170), 25)

  pygame.draw.line(screen, RED, (400, 300), (700, 300),6)
  pygame.draw.line(screen, (105, 39, 47), (400, 307), (700, 307), 10)#table
  pygame.draw.line(screen, (105, 39, 47), (405, 310), (405, 400), 10)#table
  pygame.draw.line(screen, (105, 39, 47), (695, 310), (695, 400), 10)#table
  pygame.draw.rect(screen, (64, 45, 24), (50, 50, 200, 200))
  pygame.draw.rect(screen, (201, 54, 59), (60, 60, 180, 180))
  image = pygame.image.load('photo.png')
   # Resize the image
  image = pygame.transform.scale(image, (170, 170))
  screen.blit(image, (50, 70))
  pygame.draw.rect(screen, (48, 58, 105), (0, 370, 800, 30))

#Night 5 - animation for when evan hides under the table
evan_hide = True
def evan_hides_under_table():
  speed = 5
  image = pygame.image.load('8_bit_evan_.png')
   # Resize the image
  image = pygame.transform.scale(image, (50, 100))
  image_rect = image.get_rect()
  x, y = 0, 280
  global evan_hide
  if evan_hide == True:
      for i in range(100):
        x += speed
        bite_interaction_bg()
        screen.blit(image, (x, y))
        pygame.display.flip()
        clock.tick(60)

  evan_hide = False
bullies_take_evan = True

#Night 5 - bullies carry evan towards fredbear
def carry_him_away():
  speed = 5
  image = pygame.image.load('fnaf_bullies_carry_evan.png')
   # Resize the image
  image = pygame.transform.scale(image, (300, 200))
  image_rect = image.get_rect()
  x, y = 400, 200
  global bullies_take_evan
  if bullies_take_evan == True:
      for i in range(100):
        x -= speed
        bite_interaction_bg()
        screen.blit(image, (x, y))
        pygame.display.flip()
        clock.tick(60)
  bullies_take_evan = False

#Night 5 - bite of 83 taking place
def bite_of_83():
  night_5_sound.play()
  bite_interaction_bg()
  evan_hides_under_table()
  time.sleep(1)
  pygame.draw.rect(screen, BLACK, (0,0, 800, 100))
  button_font = pygame.font.Font(None, 29)
  text_surface = button_font.render("It's too late! Hide under the table! You know what happens if he finds you! ", True, (196, 178, 35))
  screen.blit(text_surface, (50, 40))
  pygame.display.flip()
  time.sleep(2)
  bite_interaction_bg()
  image = pygame.image.load('8_bit_evan_cry_hide.png')
   # Resize the image
  image = pygame.transform.scale(image, (100, 50))
  screen.blit(image, (550, 320))
  three_bullies_arrive()
  pygame.display.flip()
  time.sleep(2)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  image = pygame.image.load('frederick.png')
   # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  button_font = pygame.font.Font(None, 26)
  text_surface = button_font.render("FINALLY! The day has come!", True, (124, 186, 110))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  image = pygame.image.load('jeremy.png')
   # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  button_font = pygame.font.Font(None, 26)
  text_surface = button_font.render("I can't wait to see the look on his face!", True, (124, 64, 245))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  image = pygame.image.load('simon_talk.png')
   # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  button_font = pygame.font.Font(None, 26)
  text_surface = button_font.render("Before that, where is that crybaby?", True, (124, 64, 245))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  image = pygame.image.load('jeremy.png')
   # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  button_font = pygame.font.Font(None, 26)
  text_surface = button_font.render("Better question. Where's Mike?", True, (124, 64, 245))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  image = pygame.image.load('foxybro_smirking_smile.png')
   # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  button_font = pygame.font.Font(None, 26)
  text_surface = button_font.render("I'm here, dummies. Look in front of you.", True, RED)
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  bite_interaction_bg()
  image = pygame.image.load('fnaf_bullies.png')
   # Resize the image
  image = pygame.transform.scale(image, (200, 200))
  screen.blit(image, (250, 180))
  new_image = pygame.image.load('8_bit_evan_cry_hide.png')
  # Resize the image
  new_image = pygame.transform.scale(new_image, (100, 50))
  screen.blit(new_image, (550, 320))
  new_image = pygame.image.load('8_bit_foxy_bro.png')
   # Resize the image
  new_image = pygame.transform.scale(new_image, (150, 200))
  screen.blit(new_image, (600, 220))
  pygame.display.flip()
  time.sleep(4)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  image = pygame.image.load('simon_talk.png')
   # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  button_font = pygame.font.Font(None, 26)
  text_surface = button_font.render("Hey man! Have you seen the crybaby?", True, (124, 64, 245))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  image = pygame.image.load('foxybro_smirking_smile.png')
   # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  button_font = pygame.font.Font(None, 26)
  text_surface = button_font.render("Are you stupid or dumb, you idiots?", True, RED)
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  image = pygame.image.load('foxybro_smirking_smile.png')
   # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  button_font = pygame.font.Font(None, 26)
  text_surface = button_font.render("He's literally hiding under the table.", True, RED)
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  image = pygame.image.load('frederick.png')
   # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  button_font = pygame.font.Font(None, 26)
  text_surface = button_font.render("Well then, let's drag him out!", True, (124, 64, 245))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  image = pygame.image.load('Caught you Crybaby.png')
   # Resize the image
  image = pygame.transform.scale(image, (800, 400))
  screen.blit(image, (0, 0))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(GREY)
  squaresize = 50
  for x in range(0, 800, squaresize):
      for y in range(0, 400, squaresize):
          if (x // squaresize + y // squaresize) % 2 == 0:
              pygame.draw.rect(screen, (19, 27, 69), (x, y, squaresize, squaresize))
          else:
              pygame.draw.rect(screen, (0,0,0), (x, y, squaresize, squaresize))
  pygame.draw.polygon(screen, GREY, ((0, 0), (800, 0),(800, 400), (600, 200), (200, 200),(0, 400)))
  image = pygame.image.load('evan_crouch.png')
   # Resize the image
  image = pygame.transform.scale(image, (400, 400))
  screen.blit(image, (200, 50))
  time.sleep(3)
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render("N-No... p-please!", True, (RED))
  screen.blit(text_surface, (280, 30))
  pygame.draw.rect(screen, (161, 71, 72), (0,0, 20, 400))
  pygame.draw.rect(screen, (161, 71, 72), (780 ,0, 20, 400))
  pygame.draw.rect(screen, (161, 71, 72), (580, 0, 20, 200))
  pygame.draw.rect(screen, (161, 71, 72), (200, 0, 20, 200))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  image = pygame.image.load('fredbear.png')
   # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (50, 100))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render("Stay strong, Evan... ", True, (196, 178, 35))
  screen.blit(text_surface, (400, 200))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  bite_interaction_bg()
  image = pygame.image.load('8_bit_frederick.png')
   # Resize the image
  image = pygame.transform.scale(image, (150, 200))
  screen.blit(image, (200, 200))
  image = pygame.image.load('8_bit_simon.png')
   # Resize the image
  image = pygame.transform.scale(image, (150, 200))
  screen.blit(image, (300, 200))
  image = pygame.image.load('8_bit_jeremy.png')
   # Resize the image
  image = pygame.transform.scale(image, (150, 200))
  screen.blit(image, (500, 200))
  image = pygame.image.load('8_bit_foxy_bro.png')
   # Resize the image
  image = pygame.transform.scale(image, (120, 180))
  screen.blit(image, (580, 200))
  image = pygame.image.load('8_bit_evan_caught.png')
   # Resize the image
  image = pygame.transform.scale(image, (100, 100))
  screen.blit(image, (400, 200))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  image = pygame.image.load('simon_talk.png')
   # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  button_font = pygame.font.Font(None, 26)
  text_surface = button_font.render("Your brother's a big baby, isnt't he?", True, (124, 64, 245))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  image = pygame.image.load('frederick.png')
   # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  button_font = pygame.font.Font(None, 26)
  text_surface = button_font.render("I wonder when he is going to 'man up' !", True, (124, 64, 245))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  image = pygame.image.load('simon_talk.png')
   # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  button_font = pygame.font.Font(None, 26)
  text_surface = button_font.render("No wonder why he cries all the time", True, (124, 64, 245))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  image = pygame.image.load('frederick.png')
   # Resize the image
  night_5_sound.play()
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  button_font = pygame.font.Font(None, 26)
  text_surface = button_font.render("Hey guys! Did you hear that?", True, (124, 64, 245))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  image = pygame.image.load('foxybro_smirking_smile.png')
   # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  button_font = pygame.font.Font(None, 26)
  text_surface = button_font.render("The little man wants to give fredbear a big kiss!", True, RED)
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  image = pygame.image.load('evan_scared.png')
   # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (5, 100))
  button_font = pygame.font.Font(None, 30)
  text_surface = button_font.render("M-mikey! p-please don't!", True, RED)
  screen.blit(text_surface, (300, 330))
  pygame.display.flip()
  time.sleep(3)
  bite_interaction_bg()
  image = pygame.image.load('8_bit_frederick.png')
   # Resize the image
  image = pygame.transform.scale(image, (150, 200))
  screen.blit(image, (200, 200))
  image = pygame.image.load('8_bit_simon.png')
   # Resize the image
  image = pygame.transform.scale(image, (150, 200))
  screen.blit(image, (300, 200))
  image = pygame.image.load('8_bit_jeremy.png')
   # Resize the image
  image = pygame.transform.scale(image, (150, 200))
  screen.blit(image, (500, 200))
  image = pygame.image.load('8_bit_foxy_bro.png')
   # Resize the image
  image = pygame.transform.scale(image, (120, 180))
  screen.blit(image, (580, 200))
  image = pygame.image.load('8_bit_evan_caught.png')
   # Resize the image
  image = pygame.transform.scale(image, (100, 100))
  screen.blit(image, (400, 200))
  pygame.display.flip()
  time.sleep(2)
  bite_interaction_bg()
  image = pygame.image.load('fnaf_bullies_carry_evan.png')
   # Resize the image
  image = pygame.transform.scale(image, (300, 200))
  screen.blit(image, (400, 200))
  time.sleep(1)
  carry_him_away()

# Start Screen with Play Button - Function to display the starting screen
def start_screen():
  global current_screen
  i = 5
  current_screen = "start"
  initialize_game()
  screen.fill(BLACK)

  while i < 10:
    static_sound.play()
    draw_static()
    draw_button()
    cry_evan()
    image = pygame.image.load('topic_title.png')
    # Resize the image
    image = pygame.transform.scale(image, (400, 50))
    screen.blit(image, (350, 50))
    image = pygame.image.load('title.png')
    # Resize the image
    image = pygame.transform.scale(image, (400, 100))
    screen.blit(image, (350, 100))
    pygame.display.flip()
    time.sleep(0.005)
    non_cry_evan()
    pygame.display.flip()
    time.sleep(0.005)
    i += 1
  pygame.display.flip()

#Introduction Screen - crying child animation for introduction
def crying_child():
  crying_image = pygame.image.load('8_bit_evan_.png')
  # Resize the image
  crying_image = pygame.transform.scale(crying_image, (100, 150))
  screen.blit(crying_image, (300, 100))
  crying_image = pygame.image.load('8_bit_evan_cry.png')
  pygame.display.flip()
  time.sleep(1)
  # Resize the image
  crying_image = pygame.transform.scale(crying_image, (100, 150))
  screen.blit(crying_image, (300, 100))
  pygame.display.flip()
  time.sleep(1)

#all 4 night's backgrounds
def night_one_bg():
  pygame.draw.rect(screen, (161, 81, 71), (0, 0, 800, 400))
  pygame.draw.rect(screen, (82, 52, 48), (0, 150, 800, 30))
  pygame.draw.rect(screen, (212, 182, 178), (0, 180, 800, 220))
  x = 0
  for i in range(400):
    pygame.draw.rect(screen, (138, 97, 84), (x, 180, 10, 220))
    x += 20
  pygame.draw.rect(screen, (77, 38, 25), (50, 50, 150, 150))
  pygame.draw.rect(screen, (17, 58, 97), (60, 60, 130, 130))
  pygame.draw.rect(screen, (77, 38, 25), (120, 60, 10, 130))
  pygame.draw.rect(screen, (77, 38, 25), (60, 120, 130, 10))
  pygame.draw.rect(screen, (77, 38, 25), (110, 50, 150, 150))
  pygame.draw.rect(screen, (17, 58, 97), (120, 60, 130, 130))
  pygame.draw.rect(screen, (77, 38, 25), (180, 60, 10, 130))
  pygame.draw.rect(screen, (77, 38, 25), (120, 120, 130, 10))
  pygame.draw.rect(screen, (77, 38, 25), (350, 50, 150, 150))
  pygame.draw.rect(screen, (17, 58, 97), (360, 60, 130, 130))
  pygame.draw.rect(screen, (77, 38, 25), (420, 60, 10, 130))
  pygame.draw.rect(screen, (77, 38, 25), (360, 120, 130, 10))
  x = 0
  evan_non_flash()

#drawing the door
def door():
  pygame.draw.rect(screen, (0, 0, 0), (550, 50, 220, 350))
  pygame.draw.rect(screen, BROWN, (560, 60, 200, 350))
  pygame.draw.circle(screen, WHITE, (580, 240), 5)
  x = 100
  for i in range(4):
    pygame.draw.line(screen, (117, 19, 40), (600, x), (720, x + 30), 5)
    x += 20

#drawing the life bar
def life_bar():
  x = 20
  for i in range(3):
    pygame.draw.circle(screen, RED, (x, 20), 10)
    pygame.draw.circle(screen, RED, (x + 12, 20), 10)
    pygame.draw.polygon(screen, RED, ((x - 10, 20), (x + 23, 20), (x + 5, 40)))
    x += 40
    button_font = pygame.font.Font(None, 25)
    text_surface = button_font.render("Night " + str(night_level), True, WHITE)
    screen.blit(text_surface, (150, 15))

#night 1 - Intro animation
def night1_play():
  ballora_sound.stop()
  begin_sound.play()
  screen.fill(BLACK)
  button_font = pygame.font.Font(None, 30)
  text_surface = button_font.render(
      "Night " + str(night_level), True, WHITE)
  screen.blit(text_surface, (350, 200))
  pygame.display.flip()
  time.sleep(3)
  light_sound.play()
  for i in range(40):
    screen.fill(BLACK)
    evan_non_flash()
    life_bar()
    pygame.display.flip()
    pygame.time.delay(10)  # Adjust delay for flickering speed
    night_one_bg()
    evan_non_flash()
    life_bar()
    door()
    pygame.display.flip()
    pygame.time.delay(10)

  screen.fill(BLACK)
  life_bar()
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  evan_image = pygame.image.load('evan_scared.png')
  # Resize the image
  evan_image = pygame.transform.scale(evan_image, (250, 250))
  screen.blit(evan_image, (5, 150))
  pygame.display.flip()
  time.sleep(SLEEP_TIME)
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render(
      'well... thats t-the sign o-of the n-nightmares...', True, RED)
  screen.blit(text_surface, (200, 330))
  pygame.display.flip()
  time.sleep(SLEEP_TIME)
  pygame.draw.rect(screen, GREY, (200, 310, 700, 50))
  evan_image = pygame.image.load('evan_smile.png')
  # Resize the image
  evan_image = pygame.transform.scale(evan_image, (250, 250))
  screen.blit(evan_image, (5, 150))
  pygame.display.flip()
  time.sleep(SLEEP_TIME)
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render(
      'b-but.. I-I am s-sure w-we can b-beat them...', True, RED)
  screen.blit(text_surface, (200, 330))
  pygame.display.flip()
  time.sleep(SLEEP_TIME)
  pygame.draw.rect(screen, GREY, (200, 310, 700, 50))
  evan_image = pygame.image.load('evan_scared.png')
  # Resize the image
  evan_image = pygame.transform.scale(evan_image, (250, 250))
  screen.blit(evan_image, (5, 150))
  pygame.display.flip()
  time.sleep(SLEEP_TIME)
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('r-right..?', True, RED)
  screen.blit(text_surface, (200, 330))
  pygame.display.flip()
  time.sleep(SLEEP_TIME)
  screen.fill(BLACK)
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('I-m sure you can... Do not worry...',
                                    True, (252, 205, 76))
  screen.blit(text_surface, (400, 200))
  pygame.display.flip()
  fredbear_image = pygame.image.load('fredbear.png')
  # Resize the image
  fredbear_image = pygame.transform.scale(fredbear_image, (300, 350))
  screen.blit(fredbear_image, (100, 200))
  pygame.display.flip()
  time.sleep(SLEEP_TIME)
  play_questions()

#Night 2 - animation background
def interaction_bg():
  screen.fill(BLACK)
  squaresize = 50
  for x in range(0, 800, squaresize):
    for y in range(0, 400, squaresize):
      if (x // squaresize + y // squaresize) % 2 == 0:
        pygame.draw.rect(screen, (19, 27, 69), (x, y, squaresize, squaresize))
      else:
        pygame.draw.rect(screen, (0, 0, 0), (x, y, squaresize, squaresize))
  pygame.draw.polygon(screen, (35, 56, 89), ((0, 0), (800, 0), (800, 400),
                                             (600, 200), (200, 200), (0, 400)))
  sofa_image = pygame.image.load('sofa.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (300, 300))
  screen.blit(sofa_image, (400, 70))
  sofa_image = pygame.image.load('TV.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (200, 200))
  screen.blit(sofa_image, (100, 100))


do_animation = True

#Night 2 animation
def slide_image_to_middle(image, final_x, speed):
  image_rect = image.get_rect()
  x, y = 0, 200
  global do_animation
  if do_animation == True:
    for i in range(60):
      interaction_bg()
      x += speed
      screen.blit(image, (x, y))
      pygame.display.flip()
      clock.tick(60)

  do_animation = False

#nightmare jumpscare list
nightmare_list = [
    "nightmare_freddy.png", "nightmare_bonnie.png", "nightmare_chica.png",
    "nightmare_foxy.png", "nightmare_fredbear.png"
]

#Display the question and answer options on screen
def display_question_and_answers(question, answers):
  question_font = pygame.font.Font(None, 30)
  answer_font = pygame.font.Font(None, 24)
  question_text = question_font.render(question, True, WHITE)
  question_rect = question_text.get_rect(center=(400, 100))

  answer1_text = answer_font.render(answers[0], True, WHITE)
  answer1_rect = answer1_text.get_rect(center=(200, 320))

  answer2_text = answer_font.render(answers[1], True, WHITE)
  answer2_rect = answer2_text.get_rect(center=(200, 370))

  answer3_text = answer_font.render(answers[2], True, WHITE)
  answer3_rect = answer3_text.get_rect(center=(620, 320))

  answer4_text = answer_font.render(answers[3], True, WHITE)
  answer4_rect = answer4_text.get_rect(center=(620, 370))

  night_one_bg()
  evan_non_flash()
  life_bar()
  door()
  hide_life(life_count)
  screen.blit(question_text, question_rect)
  pygame.draw.rect(screen, (145, 59, 44), (50, 300, 300, 40))
  pygame.draw.rect(screen, (BLACK), (50, 300, 300, 40), 2)
  screen.blit(answer1_text, answer1_rect)
  pygame.draw.rect(screen, (145, 59, 44), (50, 350, 300, 40))
  pygame.draw.rect(screen, (BLACK), (50, 350, 300, 40), 2)
  screen.blit(answer2_text, answer2_rect)
  pygame.draw.rect(screen, (145, 59, 44), (500, 300, 250, 40))
  pygame.draw.rect(screen, (BLACK), (500, 300, 250, 40), 2)
  screen.blit(answer3_text, answer3_rect)
  pygame.draw.rect(screen, (145, 59, 44), (500, 350, 250, 40))
  pygame.draw.rect(screen, (BLACK), (500, 350, 250, 40), 2)
  screen.blit(answer4_text, answer4_rect)

  pygame.display.flip()

#Function for playing the questions
def play_questions():
  global life_count
  global current_screen
  global night_level
  global questions_list

  night_one_bg()
  evan_non_flash()
  life_bar()
  door()
  hide_life(life_count)
  correct_answers = 0
  while correct_answers < Q_IN_EACH_ROUND:
      answer_selected = False
      user_answer = None
      choice = random.randrange(0, len(questions_list) - 2)
      question = questions_list[choice]
      display_question_and_answers(question["question"], question["answers"])
      correct_answer = question["correct_answer"]
      done = False
      while not done:
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 < x < 350 and 300 < y < 340:
                    button_sound.play()
                    user_answer = "1"
                elif 50 < x < 350 and 350 < y < 390:
                    button_sound.play()
                    user_answer = "2"
                elif 500 < x < 750 and 300 < y < 340:
                    button_sound.play()
                    user_answer = "3"
                elif 500 < x < 750 and 350 < y < 390:
                    button_sound.play()
                    user_answer = "4"
                else:
                    continue

                if user_answer == correct_answer:
                  print("Great! Let's go on")
                  questions_list.pop(choice)
                  correct_answers += 1
                else:
                  print("U-uh oh... OUCH!")
                  life_count -= 1
                  nchica_image = pygame.image.load(random.choice(nightmare_list))
                  # Resize the image
                  nchica_image = pygame.transform.scale(nchica_image, (800, 400))
                  screen.blit(nchica_image, (0, 0))
                  pygame.display.flip()
                  jumpscare_audio.play()
                  time.sleep(4)
                  questions_list.pop(choice)

                answer_selected = True
                break

        if answer_selected == True:
           break
      #while not done loop ends here

      night_one_bg()
      evan_non_flash()
      life_bar()
      door()

      if life_count > 0:
        hide_life(life_count)

      else:
        screen.fill(BLACK)
        time.sleep(SLEEP_TIME)
        start_screen()
        break
  #if life count is greater than 0, then play the next night
  if  life_count > 0:
    night_level += 1
    current_screen = "play_questions"
    button_font = pygame.font.Font(None, 36)
    text_surface = button_font.render('Press SPACE to pass the night...', True, BLACK)
    screen.blit(text_surface, (400, 20))
    pygame.display.flip()



#Night 3 - Simon's background
def simon_interaction_bg():
  screen.fill(DARK_GREEN)
  x = 10
  for i in range(50):  #grass
    pygame.draw.circle(screen, (78, 138, 101), (x, 20), 5)
    pygame.draw.circle(screen, (78, 138, 101), (x, 180), 5)
    pygame.draw.circle(screen, (78, 138, 101), (x, 340), 5)
    x += 50
  x = 40
  for i in range(50):  #grass
    pygame.draw.circle(screen, (78, 138, 101), (x, 100), 5)
    x += 50
  x = 40
  for i in range(50):  #grass
    pygame.draw.circle(screen, (78, 138, 101), (x, 260), 5)
    x += 50

  y = 0
  for i in range(3):  #pathway
    pygame.draw.rect(screen, (117, 125, 120), (550, y, 120, 100))
    pygame.draw.rect(screen, BLACK, (550, x, 120, 100), 3)
    y += 110

  x_new = 550
  for i in range(6):  #pathway
    pygame.draw.rect(screen, (117, 125, 120), (x_new, 220, 120, 100))
    pygame.draw.rect(screen, BLACK, (550, x, 120, 100), 3)
    x_new -= 130
  pygame.draw.rect(screen, (194, 170, 103), (50, 0, 450, 200))  #sandbox
  pygame.draw.rect(screen, GREY, (50, 0, 450, 200), 15)
  nchica_image = pygame.image.load('simon.png')
  # Resize the image
  nchica_image = pygame.transform.scale(nchica_image, (150, 150))
  screen.blit(nchica_image, (50, 100))
  pygame.display.flip()


simon_meet = True

#Night 3 - second animation
def evan_slides_down_part_2():
  speed = 5
  image = pygame.image.load('8_bit_evan.png')
  # Resize the image
  image = pygame.transform.scale(image, (50, 100))
  image_rect = image.get_rect()
  x, y = 560, 0
  global simon_meet
  if simon_meet == True:
    for i in range(40):
      y += speed
      simon_interaction_bg()
      screen.blit(image, (x, y))
      pygame.display.flip()
      clock.tick(60)
    for i in range(80):
      x -= speed
      simon_interaction_bg()
      screen.blit(image, (x, y))
      pygame.display.flip()
      clock.tick(60)
  print(x, y)
  simon_meet = False


evan_leave = True

#Night 3 - Evan leaving the screen - part 2 interaction with simon
def leave_out():
  speed = 5
  image = pygame.image.load('8_bit_evan.png')
  # Resize the image
  image = pygame.transform.scale(image, (50, 100))
  image_rect = image.get_rect()
  x, y = 160, 200
  global evan_leave
  if evan_leave == True:
    for i in range(80):
      x -= speed
      simon_interaction_bg()
      screen.blit(image, (x, y))
      pygame.display.flip()
      clock.tick(60)

  evan_leave = False

#Night 3 - short story interaction with Simon
def interaction_with_Simon():
  screen.fill(DARK_GREEN)
  x = 10
  for i in range(50):
    pygame.draw.circle(screen, (78, 138, 101), (x, 20), 5)
    x += 50
  x = 40
  for i in range(50):
    pygame.draw.circle(screen, (78, 138, 101), (x, 100), 5)
    x += 50
  x = 10
  for i in range(50):
    pygame.draw.circle(screen, (78, 138, 101), (x, 180), 5)
    x += 50
  x = 40
  for i in range(50):
    pygame.draw.circle(screen, (78, 138, 101), (x, 260), 5)
    x += 50
  x = 10
  for i in range(50):
    pygame.draw.circle(screen, (78, 138, 101), (x, 340), 5)
    x += 50
  y = 0
  for i in range(3):
    pygame.draw.rect(screen, (117, 125, 120), (550, y, 120, 100))
    pygame.draw.rect(screen, BLACK, (550, x, 120, 100), 3)
    y += 110

  x_new = 550
  for i in range(6):
    pygame.draw.rect(screen, (117, 125, 120), (x_new, 220, 120, 100))
    pygame.draw.rect(screen, BLACK, (550, x, 120, 100), 3)
    x_new -= 130

  pygame.draw.rect(screen, (194, 170, 103), (50, 0, 450, 200))  #sandbox
  pygame.draw.rect(screen, GREY, (50, 0, 450, 200), 15)
  nchica_image = pygame.image.load('simon.png')
  # Resize the image
  nchica_image = pygame.transform.scale(nchica_image, (150, 150))
  screen.blit(nchica_image, (50, 100))
  pygame.display.flip()
  time.sleep(1)
  evan_slides_down_part_2()
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  time.sleep(1)
  image = pygame.image.load('simon_talk.png')
  # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  button_font = pygame.font.Font(None, 26)
  text_surface = button_font.render(
      "Aren't you the kid who always hides under the table and cries?", True,
      (237, 82, 9))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  time.sleep(1)
  image = pygame.image.load('bully_meet_evan.png')
  # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (5, 100))
  button_font = pygame.font.Font(None, 30)
  text_surface = button_font.render("...I-I'm s-sorry...", True, RED)
  screen.blit(text_surface, (250, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  image = pygame.image.load('simon_talk.png')
  # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  button_font = pygame.font.Font(None, 30)
  text_surface = button_font.render(
      "Ha Ha! No one else is scared! Why are you?", True, (237, 82, 9))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  image = pygame.image.load('simon_talk.png')
  # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  button_font = pygame.font.Font(None, 30)
  text_surface = button_font.render("Mike's right! you're such a crybaby!",
                                    True, (237, 82, 9))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  simon_interaction_bg()
  leave_out()
  time.sleep(3)

#Night 3 - interaction background  - part 1 - interaction with cindy - short story
def new_interaction_bg():
  screen.fill(DARK_GREEN)

  x = 10
  for i in range(50):
    pygame.draw.circle(screen, (78, 138, 101), (x, 20), 5)
    x += 50
  x = 40
  for i in range(50):
    pygame.draw.circle(screen, (78, 138, 101), (x, 100), 5)
    x += 50
  x = 10
  for i in range(50):
    pygame.draw.circle(screen, (78, 138, 101), (x, 180), 5)
    x += 50
  x = 40
  for i in range(50):
    pygame.draw.circle(screen, (78, 138, 101), (x, 260), 5)
    x += 50
  x = 10
  for i in range(50):
    pygame.draw.circle(screen, (78, 138, 101), (x, 340), 5)
    x += 50
  x = 0
  for i in range(4):
    pygame.draw.rect(screen, (117, 125, 120), (550, x, 120, 100))
    pygame.draw.rect(screen, BLACK, (550, x, 120, 100), 3)
    x += 110
  nchica_image = pygame.image.load('grass.png')
  # Resize the image
  nchica_image = pygame.transform.scale(nchica_image, (70, 70))
  screen.blit(nchica_image, (400, 100))
  screen.blit(nchica_image, (100, 300))
  nchica_image = pygame.image.load('Cindy.png')
  # Resize the image
  nchica_image = pygame.transform.scale(nchica_image, (100, 100))
  screen.blit(nchica_image, (200, 200))
  nchica_image = pygame.image.load('flower.png')
  # Resize the image
  nchica_image = pygame.transform.scale(nchica_image, (50, 50))
  screen.blit(nchica_image, (100, 100))
  nchica_image = pygame.image.load('flower.png')
  # Resize the image
  nchica_image = pygame.transform.scale(nchica_image, (50, 50))
  screen.blit(nchica_image, (400, 300))

#Night 3 - Evan animation meeting cindy
def slide_image_to_middle_night_3(image, final_x, speed):
  image_rect = image.get_rect()
  x, y = 560, 0

  for i in range(40):
    y += speed
    new_interaction_bg()
    screen.blit(image, (x, y))
    pygame.display.flip()
    clock.tick(60)
  for i in range(50):
    x -= speed
    new_interaction_bg()
    screen.blit(image, (x, y))
    pygame.display.flip()
    clock.tick(60)



do_new_animation = True

#Night 3 - evan exiting the interaction with cindy - animation
def new_slide_image_to_middle():
  image = pygame.image.load('8_bit_evan.png')
  # Resize the image
  image = pygame.transform.scale(image, (50, 100))
  image_rect = image.get_rect()
  speed = 5
  x, y = 310, 200
  global do_new_animation
  if do_new_animation == True:
    for i in range(50):
      x += speed
      new_interaction_bg()
      screen.blit(image, (x, y))
      pygame.display.flip()
      clock.tick(60)
    for i in range(40):
      y += speed
      new_interaction_bg()
      screen.blit(image, (x, y))
      pygame.display.flip()
      clock.tick(60)
  do_new_animation = False

#Night 4 - background
def william_interaction_bg():
  music_box_sound.play()
  screen.fill(GREY)
  x = 100
  for i in range(5):
    pygame.draw.line(screen, (84, 89, 85), (x, 0), (x, 400), 50)
    pygame.draw.line(screen, (84, 89, 85), (x + 20, 0), (x + 20, 400), 20)
    x += 200
  pygame.draw.rect(screen, BLACK, (300, 100, 300, 300))
  pygame.draw.rect(screen, (74, 57, 37), (300, 100, 300, 300), 10)
  image = pygame.image.load('suit_on.png')
  # Resize the image
  image = pygame.transform.scale(image, (350, 300))
  screen.blit(image, (250, 110))
  pygame.draw.line(screen, BLACK, (650, 200), (630, 307), 3)
  pygame.draw.line(screen, BLACK, (630, 190), (630, 307), 3)
  pygame.draw.line(screen, BLACK, (600, 190), (620, 307), 3)
  pygame.draw.line(screen, BLACK, (650, 200), (630, 307), 3)
  pygame.draw.line(screen, BLACK, (650, 200), (630, 307), 3)
  pygame.draw.circle(screen, GREEN, (660, 180), 25)
  pygame.draw.circle(screen, RED, (630, 200), 25)
  pygame.draw.circle(screen, (181, 177, 45), (620, 150), 25)
  pygame.draw.circle(screen, (84, 32, 97), (600, 190), 25)
  pygame.draw.circle(screen, (70, 142, 184), (630, 170), 25)

  pygame.draw.line(screen, RED, (400, 300), (700, 300), 6)
  pygame.draw.line(screen, (105, 39, 47), (400, 307), (700, 307), 10)  #table
  pygame.draw.line(screen, (105, 39, 47), (405, 310), (405, 400), 10)  #table
  pygame.draw.line(screen, (105, 39, 47), (695, 310), (695, 400), 10)  #table
  pygame.draw.rect(screen, (64, 45, 24), (50, 50, 200, 200))
  pygame.draw.rect(screen, (201, 54, 59), (60, 60, 180, 180))
  image = pygame.image.load('photo.png')
  # Resize the image
  image = pygame.transform.scale(image, (170, 170))
  screen.blit(image, (50, 70))
  pygame.draw.rect(screen, (48, 58, 105), (0, 370, 800, 30))


evan_meet_william = True

#Night 4 - Evan animation - entering the pizzeria
def join_in_night_four():
  speed = 5
  image = pygame.image.load('8_bit_evan_.png')
  # Resize the image
  image = pygame.transform.scale(image, (50, 100))
  image_rect = image.get_rect()
  x, y = 0, 280
  global evan_meet_william
  if evan_meet_william == True:
    for i in range(50):
      x += speed
      william_interaction_bg()
      screen.blit(image, (x, y))
      pygame.display.flip()
      clock.tick(60)

  evan_meet_william = False


evan_exiting = True

#Night 4 - Evan animation - exiting the pizzeria
def evan_now_exiting():
  speed = 5
  image = pygame.image.load('8_bit_evan_cry.png')
  # Resize the image
  image = pygame.transform.scale(image, (50, 100))
  image_rect = image.get_rect()
  x, y = 200, 280
  global evan_exiting
  if evan_exiting == True:
    for i in range(100):
      x += speed
      william_interaction_bg()
      screen.blit(image, (x, y))
      pygame.display.flip()
      clock.tick(60)

  evan_exiting = False

#Night 4 Short Story - interaction with william afton
def night4_willian_interaction():
  screen.fill(GREY)
  x = 100
  for i in range(5):
    pygame.draw.line(screen, (84, 89, 85), (x, 0), (x, 400), 50)
    pygame.draw.line(screen, (84, 89, 85), (x + 20, 0), (x + 20, 400), 20)
    x += 200
  pygame.draw.rect(screen, BLACK, (300, 100, 300, 300))
  pygame.draw.rect(screen, (74, 57, 37), (300, 100, 300, 300), 10)
  image = pygame.image.load('suit_on.png')
  # Resize the image
  image = pygame.transform.scale(image, (350, 300))
  screen.blit(image, (250, 110))
  pygame.draw.line(screen, BLACK, (650, 200), (630, 307), 3)
  pygame.draw.line(screen, BLACK, (630, 190), (630, 307), 3)
  pygame.draw.line(screen, BLACK, (600, 190), (620, 307), 3)
  pygame.draw.line(screen, BLACK, (650, 200), (630, 307), 3)
  pygame.draw.line(screen, BLACK, (650, 200), (630, 307), 3)
  pygame.draw.circle(screen, GREEN, (660, 180), 25)
  pygame.draw.circle(screen, RED, (630, 200), 25)
  pygame.draw.circle(screen, (181, 177, 45), (620, 150), 25)
  pygame.draw.circle(screen, (84, 32, 97), (600, 190), 25)
  pygame.draw.circle(screen, (70, 142, 184), (630, 170), 25)

  pygame.draw.line(screen, RED, (400, 300), (700, 300), 6)
  pygame.draw.line(screen, (105, 39, 47), (400, 307), (700, 307), 10)  #table
  pygame.draw.line(screen, (105, 39, 47), (405, 310), (405, 400), 10)  #table
  pygame.draw.line(screen, (105, 39, 47), (695, 310), (695, 400), 10)  #table
  pygame.draw.rect(screen, (64, 45, 24), (50, 50, 200, 200))
  pygame.draw.rect(screen, (201, 54, 59), (60, 60, 180, 180))
  image = pygame.image.load('photo.png')
  # Resize the image
  image = pygame.transform.scale(image, (170, 170))
  screen.blit(image, (50, 70))
  pygame.draw.rect(screen, (48, 58, 105), (0, 370, 800, 30))
  join_in_night_four()
  time.sleep(2)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  time.sleep(1)
  image = pygame.image.load('william_smile.png')
  # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  button_font = pygame.font.Font(None, 26)
  text_surface = button_font.render(
      "Such a masterpiece don't you think? Perfect for your birthday!", True,
      (163, 48, 186))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  time.sleep(1)
  image = pygame.image.load('William_happy.png')
  # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  music_box_sound.play()
  button_font = pygame.font.Font(None, 26)
  text_surface = button_font.render(
      "I have invited both Mike's and your friends for your party!", True,
      (163, 48, 186))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  time.sleep(1)
  image = pygame.image.load('evan_sad.png')
  # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (5, 100))
  button_font = pygame.font.Font(None, 28)
  text_surface = button_font.render(
      "B-but.. y-you k-know a-about them... t-they're mean!", True, RED)
  screen.blit(text_surface, (230, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  time.sleep(1)
  image = pygame.image.load('william_upset.png')
  # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  button_font = pygame.font.Font(None, 26)
  text_surface = button_font.render(
      "I told you that they're just teasing you. ", True, (163, 48, 186))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  time.sleep(1)
  image = pygame.image.load('william_upset.png')
  # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  button_font = pygame.font.Font(None, 26)
  text_surface = button_font.render("It's not like you're gonna die kiddo.",
                                    True, (163, 48, 186))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  william_interaction_bg()
  evan_now_exiting()
  time.sleep(4)
  screen.fill(BLACK)
  time.sleep(3)
  screen.fill(BLACK)
  sofa_image = pygame.image.load('fredbear.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (350, 350))
  screen.blit(sofa_image, (5, 50))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('No one listens to you... but I can', True,
                                    (252, 205, 76))
  screen.blit(text_surface, (400, 200))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  sofa_image = pygame.image.load('fredbear.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (350, 350))
  screen.blit(sofa_image, (5, 50))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('M-more l-like n-no one l-likes m-me',
                                    True, (RED))
  screen.blit(text_surface, (390, 200))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  sofa_image = pygame.image.load('fredbear.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (350, 350))
  screen.blit(sofa_image, (5, 50))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('One day to go...', True, (252, 205, 76))
  screen.blit(text_surface, (400, 200))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  sofa_image = pygame.image.load('fredbear.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (350, 350))
  screen.blit(sofa_image, (5, 50))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('Tommorow is another day...', True,
                                    (252, 205, 76))
  screen.blit(text_surface, (400, 200))
  pygame.display.flip()
  time.sleep(3)
  begin_sound.play()
  screen.fill(BLACK)
  button_font = pygame.font.Font(None, 30)
  text_surface = button_font.render('Night 4', True, WHITE)
  screen.blit(text_surface, (350, 200))
  pygame.display.flip()
  time.sleep(4)
  play_questions()

#Night 3 Short Story - interaction with Cindy
def interaction_with_Cindy():
  night_3_sound.play()
  screen.fill(DARK_GREEN)

  x = 10
  for i in range(50):
    pygame.draw.circle(screen, (78, 138, 101), (x, 20), 5)
    x += 50
  x = 40
  for i in range(50):
    pygame.draw.circle(screen, (78, 138, 101), (x, 100), 5)
    x += 50
  x = 10
  for i in range(50):
    pygame.draw.circle(screen, (78, 138, 101), (x, 180), 5)
    x += 50
  x = 40
  for i in range(50):
    pygame.draw.circle(screen, (78, 138, 101), (x, 260), 5)
    x += 50
  x = 10
  for i in range(50):
    pygame.draw.circle(screen, (78, 138, 101), (x, 340), 5)
    x += 50
  x = 0
  for i in range(4):
    pygame.draw.rect(screen, (117, 125, 120), (550, x, 120, 100))
    x += 110
  nchica_image = pygame.image.load('grass.png')
  # Resize the image
  nchica_image = pygame.transform.scale(nchica_image, (70, 70))
  screen.blit(nchica_image, (400, 100))
  screen.blit(nchica_image, (100, 300))
  nchica_image = pygame.image.load('Cindy.png')
  # Resize the image
  nchica_image = pygame.transform.scale(nchica_image, (100, 100))
  screen.blit(nchica_image, (200, 200))
  nchica_image = pygame.image.load('flower.png')
  # Resize the image
  nchica_image = pygame.transform.scale(nchica_image, (100, 100))
  screen.blit(nchica_image, (200, 200))
  image = pygame.image.load('8_bit_evan.png')
  # Resize the image
  image = pygame.transform.scale(image, (50, 100))
  slide_image_to_middle_night_3(image, 400, 5)
  time.sleep(2)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  time.sleep(1)
  image = pygame.image.load('Cindy_sad.png')
  # Resize the image
  image = pygame.transform.scale(image, (150, 250))
  screen.blit(image, (600, 150))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('Hey Ev! Look at what daddy got for me!',
                                    True, (237, 82, 9))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  time.sleep(1)
  image = pygame.image.load('evan_smile.png')
  # Resize the image
  image = pygame.transform.scale(image, (250, 250))
  screen.blit(image, (5, 150))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render(('...? I-Is t-that-'), True, RED)
  screen.blit(text_surface, (200, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  image = pygame.image.load('cindy_happy.png')
  # Resize the image
  image = pygame.transform.scale(image, (150, 250))
  screen.blit(image, (600, 150))
  button_font = pygame.font.Font(None, 30)
  text_surface = button_font.render(('An ultra rare springbonnie plushie!'),
                                    True, (237, 82, 9))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  image = pygame.image.load('Cindy_sad.png')
  # Resize the image
  image = pygame.transform.scale(image, (150, 250))
  screen.blit(image, (600, 150))
  button_font = pygame.font.Font(None, 30)
  text_surface = button_font.render(('Wait.. why are you crying?'), True,
                                    (237, 82, 9))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  image = pygame.image.load('close_eyes_evan.png')
  # Resize the image
  image = pygame.transform.scale(image, (250, 250))
  screen.blit(image, (5, 150))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render(('n-nightmares... a-again... '), True, RED)
  screen.blit(text_surface, (200, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  image = pygame.image.load('Cindy_sad.png')
  # Resize the image
  image = pygame.transform.scale(image, (150, 250))
  screen.blit(image, (600, 150))
  button_font = pygame.font.Font(None, 30)
  text_surface = button_font.render(
      ('Nightmares are not real. Wanna hear something?'), True, (237, 82, 9))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  image = pygame.image.load('Cindy_talk.png')
  # Resize the image
  image = pygame.transform.scale(image, (150, 250))
  screen.blit(image, (600, 150))
  button_font = pygame.font.Font(None, 30)
  text_surface = button_font.render(('I heard that kids died at the pizzeria'),
                                    True, (237, 82, 9))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  image = pygame.image.load('Cindy_talk.png')
  # Resize the image
  image = pygame.transform.scale(image, (150, 250))
  screen.blit(image, (600, 150))
  button_font = pygame.font.Font(None, 28)
  text_surface = button_font.render(
      ('Once they died, they were stuffed in... animatronics'), True,
      (237, 82, 9))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  image = pygame.image.load('cindy_smile.png')
  # Resize the image
  image = pygame.transform.scale(image, (150, 250))
  screen.blit(image, (600, 150))
  button_font = pygame.font.Font(None, 30)
  text_surface = button_font.render(('But I am sure that is just a myth!'),
                                    True, (237, 82, 9))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  image = pygame.image.load('cindy_smile.png')
  # Resize the image
  image = pygame.transform.scale(image, (150, 250))
  screen.blit(image, (600, 150))
  button_font = pygame.font.Font(None, 30)
  text_surface = button_font.render(
      ('Cannot wait to come to your party! Bye Ev!'), True, (237, 82, 9))
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  new_interaction_bg()
  new_slide_image_to_middle()
  time.sleep(2)
  interaction_with_Simon()
  time.sleep(3)
  screen.fill(BLACK)
  sad_sound.play()
  sofa_image = pygame.image.load('fredbear.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (350, 350))
  screen.blit(sofa_image, (5, 50))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('No-one still b-believes me...', True, (RED))
  screen.blit(text_surface, (400, 200))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  sofa_image = pygame.image.load('fredbear.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (350, 350))
  screen.blit(sofa_image, (5, 50))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('Not even that pigtailed girl?', True,
                                    (252, 205, 76))
  screen.blit(text_surface, (400, 200))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  sofa_image = pygame.image.load('fredbear.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (350, 350))
  screen.blit(sofa_image, (5, 50))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('Do not worry.. I will be there', True,
                                    (252, 205, 76))
  screen.blit(text_surface, (400, 200))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  sofa_image = pygame.image.load('fredbear.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (350, 350))
  screen.blit(sofa_image, (5, 50))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('Till the end', True, (252, 205, 76))
  screen.blit(text_surface, (400, 200))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  sofa_image = pygame.image.load('fredbear.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (350, 350))
  screen.blit(sofa_image, (5, 50))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('3 days left...', True, (252, 205, 76))
  screen.blit(text_surface, (400, 200))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  sofa_image = pygame.image.load('fredbear.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (350, 350))
  screen.blit(sofa_image, (5, 50))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('Tommorow is another day...', True, (252, 205, 76))
  screen.blit(text_surface, (400, 200))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  begin_sound.play()
  time.sleep(1)
  button_font = pygame.font.Font(None, 30)
  text_surface = button_font.render('Night 3', True, WHITE)
  screen.blit(text_surface, (350, 200))
  pygame.display.flip()
  time.sleep(4)
  play_questions()

#Night 2 - interaction with michael short story
def night2_michael_interaction():
  ballora_sound.stop()
  music_box_sound.play()
  screen.fill(BLACK)

  squaresize = 50
  for x in range(0, 800, squaresize):
    for y in range(0, 400, squaresize):
      if (x // squaresize + y // squaresize) % 2 == 0:
        pygame.draw.rect(screen, (19, 27, 69), (x, y, squaresize, squaresize))
      else:
        pygame.draw.rect(screen, (0, 0, 0), (x, y, squaresize, squaresize))
  pygame.draw.polygon(screen, (35, 56, 89), ((0, 0), (800, 0), (800, 400),
                                             (600, 200), (200, 200), (0, 400)))

  sofa_image = pygame.image.load('sofa.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (300, 300))
  screen.blit(sofa_image, (400, 70))
  sofa_image = pygame.image.load('TV.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (200, 200))
  screen.blit(sofa_image, (100, 100))
  image = pygame.image.load('evan.png')
  # Resize the image
  image = pygame.transform.scale(image, (70, 130))
  slide_image_to_middle(image, 400, 5)
  sofa_image = pygame.image.load('evan.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (70, 130))
  screen.blit(sofa_image, (300, 200))
  print("1st sleep")
  pygame.display.flip()
  time.sleep(1)
  sofa_image = pygame.image.load('foxybro.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (200, 200))
  screen.blit(sofa_image, (150, 50))
  sofa_image = pygame.image.load('TV.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (200, 200))
  screen.blit(sofa_image, (100, 100))
  print("2nd sleep")
  pygame.display.flip()
  time.sleep(1)
  sofa_image = pygame.image.load('cry_evan.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (70, 130))
  screen.blit(sofa_image, (300, 200))
  pygame.display.flip()
  time.sleep(1)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  sofa_image = pygame.image.load('foxy_bro_laughing.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (250, 300))
  screen.blit(sofa_image, (600, 100))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('Ha ha! Got you, crybaby!', True, RED)
  screen.blit(text_surface, (200, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  sofa_image = pygame.image.load('evan_scared.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (250, 250))
  screen.blit(sofa_image, (5, 150))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render(
      'T-That w-was n-not f-funny.. M-mikey... *sniffles*', True, RED)
  screen.blit(text_surface, (200, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  sofa_image = pygame.image.load('foxybro_mouth_open.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (250, 300))
  screen.blit(sofa_image, (600, 100))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render(
      'Aww... What you gonna do about it crybaby? Cry?', True, RED)
  screen.blit(text_surface, (50, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  sofa_image = pygame.image.load('foxybro_smirking.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (250, 300))
  screen.blit(sofa_image, (600, 100))
  button_font = pygame.font.Font(None, 24)
  text_surface = button_font.render(
      'Maybe locking you in your room again might teach you on how to act like a man',
      True, RED)
  screen.blit(text_surface, (20, 330))
  pygame.display.flip()
  time.sleep(3)
  music_box_sound.play()
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  sofa_image = pygame.image.load('evan_scared.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (250, 250))
  screen.blit(sofa_image, (5, 150))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('N-No.. p-please d-dont...', True, RED)
  screen.blit(text_surface, (200, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  sofa_image = pygame.image.load('foxy_bro_laughing.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (250, 300))
  screen.blit(sofa_image, (600, 100))
  button_font = pygame.font.Font(None, 28)
  text_surface = button_font.render(
      'Nah... I have other plans for you. Well... happy early dumb birthday',
      True, RED)
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  sofa_image = pygame.image.load('fredbear.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (350, 350))
  screen.blit(sofa_image, (5, 50))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('Did he hurt you again?', True,
                                    (252, 205, 76))
  screen.blit(text_surface, (400, 200))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  sofa_image = pygame.image.load('fredbear.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (350, 350))
  screen.blit(sofa_image, (5, 50))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('Y-Yes.. h-he d-did', True, (RED))
  screen.blit(text_surface, (400, 200))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  sofa_image = pygame.image.load('fredbear.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (350, 350))
  screen.blit(sofa_image, (5, 50))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('I am sure this will all end..', True,
                                    (252, 205, 76))
  screen.blit(text_surface, (400, 200))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  sofa_image = pygame.image.load('fredbear.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (350, 350))
  screen.blit(sofa_image, (5, 50))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('On the day of your 9th birthday..', True,
                                    (252, 205, 76))
  screen.blit(text_surface, (400, 200))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  sofa_image = pygame.image.load('fredbear.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (350, 350))
  screen.blit(sofa_image, (5, 50))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('A-Are y-you s-sure..?', True, RED)
  screen.blit(text_surface, (400, 200))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  sofa_image = pygame.image.load('fredbear.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (350, 350))
  screen.blit(sofa_image, (5, 50))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('4 days left...', True, (252, 205, 76))
  screen.blit(text_surface, (400, 200))
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  sofa_image = pygame.image.load('fredbear.png')
  # Resize the image
  sofa_image = pygame.transform.scale(sofa_image, (350, 350))
  screen.blit(sofa_image, (5, 50))
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render('Tommorow is another day...', True,
                                    (252, 205, 76))
  screen.blit(text_surface, (400, 200))
  pygame.display.flip()
  time.sleep(4)
  screen.fill(BLACK)
  begin_sound.play()
  time.sleep(1)
  button_font = pygame.font.Font(None, 30)
  text_surface = button_font.render('Night 2', True, WHITE)
  screen.blit(text_surface, (350, 200))
  pygame.display.flip()
  time.sleep(4)
  play_questions()


font = pygame.font.Font(None, 20)

#Alter the life count according to the number of questions got wrong
def hide_life(count):

  if (count == 1 or count == 2):
    pygame.draw.circle(screen, BLACK, (20, 20), 10)
    pygame.draw.circle(screen, BLACK, (20 + 12, 20), 10)
    pygame.draw.polygon(screen, BLACK,
                        ((20 - 10, 20), (20 + 23, 20), (20 + 5, 40)))

  if (count == 1):
    pygame.draw.circle(screen, BLACK, (60, 20), 10)
    pygame.draw.circle(screen, BLACK, (60 + 12, 20), 10)
    pygame.draw.polygon(screen, BLACK,
                        ((60 - 10, 20), (60 + 23, 20), (60 + 5, 40)))

#GamePlay Screen - Evan image
def evan_non_flash():
  evan_non_flash_image = pygame.image.load('evan_non_flash.png')
  # Resize the image
  evan_non_flash_image = pygame.transform.scale(evan_non_flash_image,
                                                (200, 300))
  screen.blit(evan_non_flash_image, (50, 100))
  #time.sleep(SLEEP_TIME)

#introduction screen - draw background
def draw_intro_bg():
  screen.fill(WHITE)

  squaresize = 50
  for x in range(0, WIDTH, squaresize):
    for y in range(0, HEIGHT, squaresize):
      if (x // squaresize + y // squaresize) % 2 == 0:
        pygame.draw.rect(screen, (19, 27, 69), (x, y, squaresize, squaresize))
      else:
        pygame.draw.rect(screen, (0, 0, 0), (x, y, squaresize, squaresize))
  pygame.draw.rect(screen, (77, 52, 12), (550, 44, 200, 300))
  pygame.draw.rect(screen, BLUE, (550, 50, 200, 300))  #bed
  pygame.draw.rect(screen, (10, 158, 168), (600, 70, 100, 52))  #bed
  pygame.draw.rect(screen, (86, 137, 140), (550, 200, 200, 150))  #bed
  fredbear_image = pygame.image.load('fredbear.png')
  chica_image = pygame.image.load('chica.png')
  # Resize the image
  chica_image = pygame.transform.scale(chica_image, (500, 400))
  screen.blit(chica_image, (10, 50))
  freddy_image = pygame.image.load('freddy.png')
  # Resize the image
  freddy_image = pygame.transform.scale(freddy_image, (500, 400))
  screen.blit(freddy_image, (70, 50))
  bonnie_image = pygame.image.load('bonnie.png')
  # Resize the image
  bonnie_image = pygame.transform.scale(bonnie_image, (500, 400))
  screen.blit(bonnie_image, (70, 50))
  # Resize the image
  fredbear_image = pygame.transform.scale(fredbear_image, (80, 80))
  screen.blit(fredbear_image, (600, 100))
  wardrobe_image = pygame.image.load('wardrobe.png')
  # Resize the image
  wardrobe_image = pygame.transform.scale(wardrobe_image, (300, 300))
  screen.blit(wardrobe_image, (0, 0))
  pygame.display.flip()

#rules screen after introduction
def draw_rules_screen():
  screen.fill(BLACK)
  button_font = pygame.font.Font(None, 30)
  text_surface = button_font.render('RULES', True, WHITE)
  screen.blit(text_surface, (400, 50))
  pygame.font.Font(None, 100)
  text_surface = button_font.render('You have 3 lives in the whole game!',
                                    True, WHITE)
  screen.blit(text_surface, (250, 100))
  text_surface = button_font.render(
      'You, as Evan Afton have to beat the nightmares', True, WHITE)
  screen.blit(text_surface, (200, 150))
  text_surface = button_font.render(
      'Solve the puzzles to pass through each door!', True, WHITE)
  screen.blit(text_surface, (210, 200))
  text_surface = button_font.render('A wrong answer leads to losing a life',
                                    True, WHITE)
  screen.blit(text_surface, (250, 250))
  text_surface = button_font.render(
      'If you get atleast 3 questions right, you can pass the night!', True,
      WHITE)
  screen.blit(text_surface, (150, 300))
  text_surface = button_font.render(
      'Hit SPACE to continue to the next level', True, WHITE)
  screen.blit(text_surface, (250, 350))
  pygame.display.flip()

#introduction short story
def draw_checkered_bg():

  global current_screen
  global bg_screen_loaded

  if bg_screen_loaded == True:
    return

  bg_screen_loaded = True
  current_screen = "backstory"

  draw_intro_bg()
  ballora_sound.play()
  time.sleep(SLEEP_TIME)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  evan_image = pygame.image.load('evan_scared.png')
  # Resize the image
  evan_image = pygame.transform.scale(evan_image, (250, 250))
  screen.blit(evan_image, (5, 150))
  pygame.display.flip()
  time.sleep(SLEEP_TIME)
  button_font = pygame.font.Font(None, 36)
  text_surface = button_font.render(
      'H-Hi.... m-my name i-is.. Evan.. Evan A-Afton..', True, RED)
  screen.blit(text_surface, (200, 330))
  pygame.display.flip()
  time.sleep(SLEEP_TIME)
  pygame.draw.rect(screen, GREY, (200, 310, 550, 50))
  evan_image = pygame.image.load('evan_sad.png')
  # Resize the image
  evan_image = pygame.transform.scale(evan_image, (250, 250))
  screen.blit(evan_image, (5, 150))
  text_surface = button_font.render(
      'I-I am 8 years old... I-I am t-turning 9.. yay I guess..', True, RED)
  screen.blit(text_surface, (200, 330))
  pygame.display.flip()
  time.sleep(SLEEP_TIME)
  pygame.draw.rect(screen, GREY, (200, 310, 700, 50))
  evan_image = pygame.image.load('evan_sad.png')
  # Resize the image
  evan_image = pygame.transform.scale(evan_image, (250, 250))
  screen.blit(evan_image, (5, 150))
  text_surface = button_font.render('T-This is m-my plushy F-Fredbear..', True,
                                    RED)
  screen.blit(text_surface, (200, 330))
  pygame.display.flip()
  time.sleep(SLEEP_TIME)
  pygame.draw.rect(screen, GREY, (200, 310, 550, 50))
  evan_image = pygame.image.load('close_eyes_evan.png')
  # Resize the image
  evan_image = pygame.transform.scale(evan_image, (250, 250))
  screen.blit(evan_image, (5, 150))
  text_surface = button_font.render(
      'I h-have a l-lot o-of s-scary nightmares...', True, RED)
  screen.blit(text_surface, (200, 330))
  pygame.display.flip()
  time.sleep(SLEEP_TIME)
  pygame.draw.rect(screen, GREY, (200, 310, 550, 50))
  evan_image = pygame.image.load('evan_scared.png')
  # Resize the image
  evan_image = pygame.transform.scale(evan_image, (250, 250))
  button_font = pygame.font.Font(None, 30)
  screen.blit(evan_image, (5, 150))
  text_surface = button_font.render(
      'B-but.. m-my older b-brother always laughs a-about it..', True, RED)
  screen.blit(text_surface, (200, 330))
  pygame.display.flip()
  time.sleep(SLEEP_TIME)
  pygame.draw.rect(screen, GREY, (200, 310, 550, 50))
  evan_image = pygame.image.load('evan_sad_2.png')
  # Resize the image
  evan_image = pygame.transform.scale(evan_image, (250, 250))
  screen.blit(evan_image, (5, 150))
  text_surface = button_font.render(
      'C-could y-you h-help me f-face m-my nightmares..?', True, RED)
  screen.blit(text_surface, (200, 330))
  pygame.display.flip()
  time.sleep(SLEEP_TIME)

  draw_intro_bg()
  for i in range(2):
    crying_child()
  pygame.display.flip()
  time.sleep(SLEEP_TIME)

  screen.fill(BLACK)
  #time.sleep(SLEEP_TIME)
  button_font = pygame.font.Font(None, 30)
  text_surface = button_font.render(
      'Warning: This game contains Jumpscares and Loud Noises!!', True, WHITE)
  screen.blit(text_surface, (100, 200))
  pygame.display.flip()
  time.sleep(SLEEP_TIME)

  draw_rules_screen()
  time.sleep(SLEEP_TIME + 6)

  screen.fill(BLACK)
  pygame.display.flip()
  time.sleep(SLEEP_TIME)
  fredbears_lines()
  pygame.display.flip()
  time.sleep(SLEEP_TIME)

  night1_play()
  pygame.display.flip()

#night 5 - bite_interaction - part 2 background
def bite_interaction_bg_part_2():
  screen.fill(GREY)
  x = 100
  for i in range(5):
    pygame.draw.line(screen, (84, 89, 85),(x,0),(x,400),50)
    pygame.draw.line(screen, (84, 89, 85),(x+20,0),(x+20,400),20)
    x += 200
  pygame.draw.rect(screen, (130, 55,18), (0, 320, 300, 60))
  pygame.draw.rect(screen, (64, 27, 9), (0, 300, 310, 20))
  image = pygame.image.load('springbonnie.png')
   # Resize the image
  image = pygame.transform.scale(image, (170, 280))
  screen.blit(image, (10, 40))
  image = pygame.image.load('fredbear_animatronic.png')
   # Resize the image
  image = pygame.transform.scale(image, (170, 280))
  screen.blit(image, (130, 40))
  pygame.draw.line(screen, BLACK, (650, 200), (630, 307), 3)
  pygame.draw.line(screen, BLACK, (630, 190), (630, 307), 3)
  pygame.draw.line(screen, BLACK, (600, 190), (620, 307), 3)
  pygame.draw.line(screen, BLACK, (650, 200), (630, 307), 3)
  pygame.draw.line(screen, BLACK, (650, 200), (630, 307), 3)
  pygame.draw.circle(screen, GREEN, (660, 180), 25)
  pygame.draw.circle(screen, RED, (630, 200), 25)
  pygame.draw.circle(screen, (181, 177, 45), (620, 150), 25)
  pygame.draw.circle(screen, (84, 32, 97), (600, 190), 25)
  pygame.draw.circle(screen, (70, 142, 184), (630, 170), 25)

  pygame.draw.line(screen, RED, (400, 300), (700, 300),6)
  pygame.draw.line(screen, (105, 39, 47), (400, 307), (700, 307), 10)#table
  pygame.draw.line(screen, (105, 39, 47), (405, 310), (405, 400), 10)#table
  pygame.draw.line(screen, (105, 39, 47), (695, 310), (695, 400), 10)#table
  pygame.draw.rect(screen, (48, 70, 107), (0, 370, 800, 30))
  x = 400
  for i in range(4):
    pygame.draw.rect(screen, (41, 40, 38), (x, 0, 20, 50))
    pygame.draw.circle(screen, (41, 40, 38), (x+10, 60), 25)
    x += 80
  pygame.draw.circle(screen, (255, 251, 13), (405, 60), 15)
  pygame.draw.circle(screen, (255, 13, 21), (485, 60), 15)
  pygame.draw.circle(screen, (12, 179, 0), (565, 60), 15)
  pygame.draw.circle(screen, (255, 154, 3), (645, 60), 15)

#night 5 - carry evan to fredbear animation
def carry_him_towards():
  speed = 5
  image = pygame.image.load('fnaf_bullies_carry_evan.png')
   # Resize the image
  image = pygame.transform.scale(image, (300, 200))
  image_rect = image.get_rect()
  x, y = 800, 200
  for i in range(50):
        x -= speed
        bite_interaction_bg_part_2()
        screen.blit(image, (x, y))
        pygame.display.flip()
        clock.tick(60)

#night 5 - bite takes place
def bite_of_83_takes_place():
  bite_interaction_bg_part_2()
  pygame.display.flip()
  carry_him_towards()
  pygame.display.flip()
  time.sleep(3)
  screen.fill(BLACK)
  pygame.draw.rect(screen, GREY, (0, 300, 800, 100))
  pygame.display.flip()
  image = pygame.image.load('foxybro_laughing.png')
   # Resize the image
  image = pygame.transform.scale(image, (300, 300))
  screen.blit(image, (500, 100))
  button_font = pygame.font.Font(None, 26)
  text_surface = button_font.render("Hey guys! Looks like the little man wants to give him a big kiss!", True, RED)
  screen.blit(text_surface, (10, 330))
  pygame.display.flip()
  time.sleep(3)
  bite_interaction_bg_part_2()
  image = pygame.image.load('fnaf_4_bullies_stand.png')
   # Resize the image
  image = pygame.transform.scale(image, (250, 200))
  screen.blit(image, (400, 200))
  image = pygame.image.load('foxy_bro_8_bit_stand.png')
   # Resize the image
  image = pygame.transform.scale(image, (120, 200))
  screen.blit(image, (350, 200))
  image = pygame.image.load('evan_trapped.png')
   # Resize the image
  image = pygame.transform.scale(image, (150, 40))
  screen.blit(image, (200, 120))
  pygame.display.flip()
  time.sleep(3)
  bite_sound.play()
  bite_interaction_bg_part_2()
  image = pygame.image.load('evan_dead.png')
   # Resize the image
  image = pygame.transform.scale(image, (130, 40))
  screen.blit(image, (200, 120))
  image = pygame.image.load('fnaf_4_bullies_stand.png')
   # Resize the image
  image = pygame.transform.scale(image, (250, 200))
  screen.blit(image, (400, 200))
  image = pygame.image.load('foxy_bro_8_bit_stand.png')
   # Resize the image
  image = pygame.transform.scale(image, (120, 200))
  screen.blit(image, (350, 200))
  image = pygame.image.load('blood.png')
  # Resize the image
  image = pygame.transform.scale(image, (800, 400))
  screen.blit(image, (0, 0))
  pygame.display.flip()

  time.sleep(3)
  screen.fill(BLACK)
  button_font = pygame.font.Font(None, 40)
  text_surface = button_font.render("EVAN!!", True, RED)
  screen.blit(text_surface, (350, 200))
  pygame.display.flip()
  time.sleep(3)
  night_5_sound.stop()
  screen.fill(BLACK)
  image = pygame.image.load('evan_angel.jpeg')
  # Resize the image
  image = pygame.transform.scale(image, (400, 400))
  screen.blit(image, (200, 0))
  pygame.display.flip()
  ballora_sound.stop()
  voicelines.play()
  time.sleep(60)
  image = pygame.image.load('game_over.png')
  # Resize the image
  image = pygame.transform.scale(image, (200, 100))
  screen.blit(image, (350, 200))
  pygame.display.flip()
  time.sleep(3)
  end_scene.play()
  screen.fill(BLACK)
  button_font = pygame.font.Font(None, 40)
  text_surface = button_font.render("Credits:", True, RED)
  screen.blit(text_surface, (350, 50))
  button_font = pygame.font.Font(None, 30)
  text_surface = button_font.render("Drawing Credits: Hasini", True, WHITE)
  screen.blit(text_surface, (300, 150))
  button_font = pygame.font.Font(None, 30)
  text_surface = button_font.render("8-bit Credits: Media", True, WHITE)
  screen.blit(text_surface, (300, 250))
  button_font = pygame.font.Font(None, 30)
  text_surface = button_font.render("Song Credits: Media and Natsu", True, WHITE)
  screen.blit(text_surface, (300, 350))
  button_font = pygame.font.Font(None, 30)
  global night_level
  night_level += 1

#night play function to move to next night/level

def play_next_night():
  print("reached play next night method", night_level)
  screen.fill(BLACK)
  time.sleep(4)
  button_font = pygame.font.Font(None, 30)
  text_surface = button_font.render(
      "Night " + str(night_level - 1) + " complete", True, WHITE)
  screen.blit(text_surface, (350, 200))
  click_sound.play()
  pygame.display.flip()
  time.sleep(12)
  if night_level == 2:
    print("Level 2")
    night2_michael_interaction()
  elif night_level == 3:
    print("Level 3")
    interaction_with_Cindy()
  elif night_level == 4:
    print("Level 4")
    night4_willian_interaction()
  else:
    print("final screen")
    bite_of_83()
    time.sleep(1)
    bite_of_83_takes_place()
    #call finish screen


# Loop until the user clicks the close button.

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
  # --- Main event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    elif event.type == pygame.MOUSEBUTTONDOWN:
      # Check if the mouse click is within the play button area
      mouse_x, mouse_y = pygame.mouse.get_pos()
      if 350 <= mouse_x <= 450 and 200 <= mouse_y <= 250 and current_screen == "start":
        button_sound.play()
        print("reached mouse button click")
        play_clicked = True
        static_sound.stop()
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and current_screen == "play_questions":
      ballora_sound.stop()
      print("reached space key")
      play_next_night()

  # --- Game logic should go here
  if play_clicked:
    draw_checkered_bg()

    # Your other game logic and drawing code here...

  # If play is not clicked, show the start screen
  else:
    start_screen()

  # --- Go ahead and update the screen with what we've drawn.
  pygame.display.flip()

  # --- Limit to 60 frames per second
  clock.tick(60)

# Close the window and quit.
pygame.quit()
