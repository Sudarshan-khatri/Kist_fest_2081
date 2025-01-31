# import the module pygame for create the game
import pygame
from pygame import mixer
import math

# import the module random to generate the random value of enenmy
import random

# initialize the system for game
pygame.init()

#create teh window of game 
screen=pygame.display.set_mode((800,650))

#background sound
# mixer.music.load('Alian Invasion/hi.wav')
# mixer.music.play(-1)

# set the game name 
pygame.display.set_caption("Alian Invasion")
# set the image on window 
w_img=pygame.image.load('Alian Invasion/alian.png')
pygame.display.set_icon(w_img)

# set the background image 
bg_img=pygame.image.load('Alian Invasion/back.jpg')
bg_img=pygame.transform.scale(bg_img, (800,650))

# initialize the background color
bg_color=(230,167,255)

#set the  rocket in window
player_img=pygame.image.load('Alian Invasion/rocket.png')
playerX=365
playerY=575
player_change=0

#set the bullet to sut out the enemy:
player_bullet=pygame.image.load('Alian Invasion/bull1.png')
bullet_X=0
bullet_Y=570
bullet_change=0.1
bullet_state="Ready"   #ready :can't fire ,fire:fire the bullet
#display the score in the window
score_values=0
font=pygame.font.Font('freesansbold.ttf',32)

textX=10
textY=10
def show_score(x,y):
    score=font.render("Score:"+str(score_values),True,(255,255,255))
    screen.blit(score,(x,y))
over_font=pygame.font.Font('freesansbold.ttf',32)
def game_over_text():
    over_txt=font.render("Game_over",True,(255,255,255))
    screen.blit(over_txt,(200,250))

# set the enemy in the window 
enemy_img=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
no_of_enemy=50
for i in range(no_of_enemy):
    enemy_img.append(pygame.image.load('Alian Invasion/enemy.png'))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(10,50))
    enemyX_change.append(0.3)
    enemyY_change.append(20)
# rocket function 
def f_player(x,y):
    screen.blit(player_img,(x,y))

# enemy function 
def e_enemy(x,y):
    screen.blit(enemy_img[i],(x, y))

#bullet function
def bullet_hit(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(player_bullet,(x,y))

#collision between bullet and enemy
def iscollision(bullet_X,bullet_Y,enemyX,enemyY):
    distance=math.sqrt((math.pow(bullet_X-bullet_Y,2))+(math.pow(enemyX-enemyY,2)))
    if distance<27:
       return True
    else:
        return False
    
def is_collision_re(playerX,playerY,enemyX,enemyY):
    dist=math.sqrt((math.pow(playerX-playerY,2))+(math.pow(enemyX-enemyY,2)))
    if dist<27:
       return True
    else:
        return False


# use while loop for run the game untill quit the game 
running=True 
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    # set the keystroke to control the rocket with the help of keyboard button
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player_change-=0.6
            if event.key==pygame.K_RIGHT:
                player_change+=0.6
        
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                player_change=0
            if event.key==pygame.K_SPACE:
                bullet_X=playerX
                bullet_hit(bullet_X,bullet_Y)
    # display the background image
    screen.blit(bg_img,(0,0))
  
    # set the boundaries for the rocket
    playerX+=player_change
    if playerX>=736:
        playerX=736
    elif playerX<=0:
        playerX=0  
    
    # set the boundaries for the enemy
    for i in range(no_of_enemy):
        #game over 
        if enemyY[i]>800:
            for j in range(no_of_enemy):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i]+=enemyX_change[i]
        if enemyX[i]>=776:
            enemyX_change[i]=-0.6
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]<=0:
            enemyX_change[i]=0.6
            enemyY[i]+=enemyY_change[i]

        #bullet movement
        if bullet_Y<=0:
            bullet_Y=570
            bullet_state="fire"
        if bullet_state is "fire":
            bullet_hit(playerX,bullet_Y)
            bullet_Y-=bullet_change

        #collision of bullet and enemy:
        collision=iscollision(bullet_X,bullet_Y,enemyX[i],enemyY[i])
        if collision:
            bullet_Y=570
            bullet_state="ready"
            score_values+=1
            enemyX[i]=random.randint(0,400)
            enemyY[i]=random.randint(10,50)
        e_enemy(enemyX[i],enemyY[i])

    # call the function
    f_player(playerX,playerY)
    show_score(textX,textY)
    #update the display
    pygame.display.flip()
pygame.display.update()

