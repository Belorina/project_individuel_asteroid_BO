from random import randint

WIDTH = 800
HEIGHT = 600
lines = 7
power_up_apparition = 40 

power_up_glitch_apparition = 80 

stick_on = False

time_bigger_player = 0
time_glitch = 0


player = Actor("player-neon")
player.pos = [400, 550]

ball = Actor("ball-pero")
ball.pos = [400, 500]
ball_speed = [3, -3]

power_up_speed = [0, 3]

ball_fall_count = 0

all_bricks = []
all_super_bricks = []

all_bricks_blue = []
all_super_bricks_blue = []

all_power_up_bigger_player = []
all_power_up_health = []

all_power_up_glitch = []

three_heart = Actor("3-hearts", anchor=["left", "bottom"])
two_heart = Actor("2-hearts", anchor=["left", "bottom"])
one_heart = Actor("1-hearts", anchor=["left", "bottom"])

three_heart.pos = [1, 599]
two_heart.pos = [1, 599]
one_heart.pos = [1, 599]

heart = None

score = 0

music.play("loop_chill")

    # placing blue bricks 
def setup_bricks_blue():
    global all_bricks_blue

    all_bricks_blue = []
    
    for x in range (0, 800, 100):
        for y in range(0, 30 * lines, 30):
            brick_blue = Actor("brick-perso-blue", anchor=["left", "top"]) 
            brick_blue.pos = [x, y ]
            all_bricks_blue.append(brick_blue)
setup_bricks_blue()

def setup_super_bricks_blue():
    global all_super_bricks_blue
    
    all_super_bricks_blue = []
    
    for x in range (0, 800, 100):
        super_brick_blue = Actor("super-brick-perso-blue", anchor=["left", "top"]) 
        super_brick_blue.pos = [x, 30 * lines + 1]
        all_super_bricks_blue.append(super_brick_blue)
setup_super_bricks_blue()

   # placing bricks 
def setup_bricks():
    global all_bricks
    
    all_bricks = []

    for x in range (0, 800, 100):
        for y in range(0, 30 * lines, 30):
            brick = Actor("brick-perso", anchor=["left", "top"]) 
            brick.pos = [x, y]
            all_bricks.append(brick)
setup_bricks()

    # placing super_bricks 
def setup_super_bricks():
    global all_super_bricks

    all_super_bricks = []

    for x in range(0, 800, 100):
        super_brick = Actor("super-brick-perso", anchor=["left", "top"])
        super_brick.pos = [x, 30 * lines + 1]
        all_super_bricks.append(super_brick)
setup_super_bricks()


def draw():
    global all_bricks_blue
    global all_super_bricks_blue


    screen.clear()
    screen.fill((9,2,50))

    game_bg = Actor("game-bg")
    game_bg.pos = [400, 300]
    game_bg.draw()


    for brick in all_bricks:
        brick.draw()
        
    for super_brick in all_super_bricks:
        super_brick.draw()

    if time_glitch > 0:
        for brick_blue in all_bricks_blue:
            brick_blue.draw()
            
        for super_brick_blue in all_super_bricks_blue:
            super_brick_blue.draw()
            
    
    for power_up_bigger_player in all_power_up_bigger_player:
        power_up_bigger_player.draw()

    for power_up_health in all_power_up_health:
        power_up_health.draw()

    for power_up_glich in all_power_up_glitch:
        power_up_glich.draw()

    player.draw()
    ball.draw()
    health()
    
    game_over_screen()
  
    showing_score()

def showing_score():
    global ball_fall_count

    if ball_fall_count == 3:
        screen.draw.text("score: " + str(score), midtop=(400, 350), owidth=1.5, ocolor=("purple"), color="pink")

        all_bricks = []

    else:
        screen.draw.text("score: " + str(score), bottomright=(790, 599), owidth=1.5, ocolor=("purple"), color="pink")

def on_mouse_move(pos):
    player.pos = [pos[0], player.pos[1]]

    if stick_on:
        ball.pos = player.pos
        ball.bottom = player.top

def on_mouse_down():
    global ball_speed
    global stick_on

    if stick_on:
        ball_speed = [3, -3]
        stick_on = False


def invert_horizontal_speed():
    ball_speed[0] = ball_speed[0] * -1
    
def invert_vertical_speed():
    ball_speed[1] = ball_speed[1] * -1

def upgrade_ball_speed(upgrade):
    if ball_speed[0] > 0:
        ball_speed[0] = ball_speed[0] + upgrade
    else:
        ball_speed[0] = ball_speed[0] - upgrade

    if ball_speed[1] > 0:
        ball_speed[1] = ball_speed[1] + upgrade
    else:
        ball_speed[1] = ball_speed[1] - upgrade

def health():
    global ball_fall_count
    global three_heart
    global two_heart
    global one_heart
    global heart
            
    if ball_fall_count == 0:
        heart = three_heart
        heart.draw()

    if ball_fall_count == 1:
        heart = two_heart
        heart.draw()

    if ball_fall_count == 2:
        heart = one_heart
        heart.draw()
    
def extra_health():
    global ball_fall_count
    global three_heart
    global two_heart
    global heart
        
    if heart == two_heart:
        ball_fall_count = ball_fall_count - 1
        heart.draw()
        
    if heart == one_heart:
        ball_fall_count = ball_fall_count - 1
        heart.draw()
        
# GAME OVER SCREEN: game_over_screen.draw() when game_over is true ? 
def game_over_screen():
    global ball_fall_count
    global ball_speed

    if ball_fall_count == 3:
        screen.clear()
        screen.fill((9,2,50))
    # si enlever ca ^^^^   screen du jeux reste avec game over dessus
    # tester avec dimmed background filter after game over, before screen play (also freez player.mouse thing)
        
        ball_speed = [0, 0]
        
        game_bg = Actor("game-bg")
        game_bg.pos = [400, 300]
        game_bg.draw()

        game_over_pic = Actor("game-over", anchor=["left", "top"])
        game_over_pic.pos = [0, 0]
        game_over_pic.draw()

        screen.draw.text("Press SPACE to restart. ", midtop=(400, 400), owidth=1.5, ocolor=("purple"), color="pink")
        reboot()

            

def reboot():
    global ball_speed
    global ball_fall_count
    global score
    
    
    keyboard[keys.SPACE]  # True if the space bar is pressed
    if keyboard[keys.SPACE] == True:

        ball_fall_count = 0 
        ball_speed = [3, -3]
        score = 0

        setup_bricks()
        setup_super_bricks()

def update(dt):
    global time_bigger_player
    global player
    global score 
    global time_glitch
    global stick_on
    global ball_speed
    global ball_fall_count
       
    # temps plus grand que zero quand powerup active (creation de chrono)
    if time_bigger_player > 0:
        time_bigger_player = time_bigger_player - dt

        if time_bigger_player <= 0:
            player = Actor("player-neon", player.pos)

    if time_glitch > 0:
        time_glitch = time_glitch - dt
        
        if time_glitch <= 0:
            pass
            

    # move ball
    new_x = ball.pos[0] + ball_speed[0]
    new_y = ball.pos[1] + ball_speed[1]

    ball.pos = [new_x, new_y]

    # move power up bigger_player 
    for power_up_bigger_player in all_power_up_bigger_player:
        new_x = power_up_bigger_player.pos[0] + power_up_speed[0]
        new_y = power_up_bigger_player.pos[1] + power_up_speed[1]

        power_up_bigger_player.pos = [new_x, new_y]

    # move power up health
    for power_up_health in all_power_up_health:
        new_x = power_up_health.pos[0] + power_up_speed[0]
        new_y = power_up_health.pos[1] + power_up_speed[1]

        power_up_health.pos = [new_x, new_y]
    
     # move power up glitch 
    for power_up_glitch in all_power_up_glitch:
        new_x = power_up_glitch.pos[0] + power_up_speed[0]
        new_y = power_up_glitch.pos[1] + power_up_speed[1]

        power_up_glitch.pos = [new_x, new_y]


    # check boundries
    if ball.right >= WIDTH or ball.left <= 0:  # ball.right, donne la 
                                            # position a droit de la ball
        invert_horizontal_speed()

    if ball.top <= 0:
        invert_vertical_speed()

    if ball.bottom > HEIGHT + 30:
        ball_fall_count = ball_fall_count + 1
        ball.pos = player.pos
        ball.bottom = player.top

        sounds.ball_fall.play()

        stick_on = True
        ball_speed = [0, 0]  

    if ball.colliderect(player):
        if ball.pos[0] >= player.left and ball.pos[0] <= player.right:
            invert_vertical_speed()
            upgrade_ball_speed(0.25)
            sounds.pop.play()
        else:
            invert_horizontal_speed()
            upgrade_ball_speed(0.25)
            sounds.pop.play()
        

    for brick in all_bricks:
        if ball.colliderect(brick):
            sounds.pop.play()
            all_bricks.remove(brick)

            if ball.pos[0] >= player.left and ball.pos[0] <= player.right:
                invert_vertical_speed()
            else:
                invert_horizontal_speed()


            score =  score + 10
            rnd = randint(0, 100)

            if rnd <= power_up_apparition:
                power_up_1 = Actor("powerup1", anchor=["left", "top"])
                power_up_1.pos = brick.pos
                all_power_up_bigger_player.append(power_up_1)

            if rnd >= power_up_apparition: 
                power_up_2 = Actor("power-up-heart", anchor=["left", "top"])
                power_up_2.pos = brick.pos
                all_power_up_health.append(power_up_2)

            if rnd <= power_up_glitch_apparition:
                power_up_3 = Actor("trans", anchor=["left", "top"])
                power_up_3.pos = brick.pos
                all_power_up_glitch.append(power_up_3)

    for super_brick in all_super_bricks: 
        if ball.colliderect(super_brick):
            
            sounds.walkie_talkie.play()

            brick = Actor("super-brick-perso-2", anchor=["left", "top"])
            brick.pos = super_brick.pos
            all_bricks.append(brick)

            invert_vertical_speed()
            all_super_bricks.remove(super_brick)



    for brick_blue in all_bricks_blue:
        if ball.colliderect(brick_blue):
            all_bricks_blue.remove(brick_blue)
            

    for super_brick_blue in all_super_bricks_blue: 
        if ball.colliderect(super_brick_blue):
            all_super_bricks_blue.remove(super_brick_blue)

    for power_up_bigger_player in all_power_up_bigger_player:
        if player.colliderect(power_up_bigger_player):
            sounds.power_up_sound.play()
            all_power_up_bigger_player.remove(power_up_bigger_player)
            time_bigger_player = 3
            player = Actor("bigger-player-neon", player.pos)
            

    for power_up_health in all_power_up_health:
        if player.colliderect(power_up_health):
            sounds.power_up_sound.play()
            all_power_up_health.remove(power_up_health)
            extra_health()

    for power_up_glitch in all_power_up_glitch:
            if player.colliderect(power_up_glitch):
                sounds.glitch.play()
                all_power_up_glitch.remove(power_up_glitch)
                time_glitch= 0.5

