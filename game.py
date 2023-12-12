import pygame, random
from car import Car
from powerup import Powerup

def car_racing(multiplayer):
    pygame.init()

    GREEN = (20, 255, 140)
    GREY = (210, 210 ,210)
    WHITE = (255, 255, 255)
    NICEGREY = (65,64,66)

    #POWERUP LIST AND ATTRIBUTES : POWERUP_TYPE : [POWERUP_PATH, STATUS, LAST_TIME_ACTIVATED]
    powerupList = ["INVINCIBLE", "SCOREMULTIPLIER", "SLOWDOWN", "SPEEDBOOST"]
    powerupDictionary = {
        "INVINCIBLE": ["assets/powerups/INVICIBILITY.png", False, 0],
        "SCOREMULTIPLIER": ["assets/powerups/SCOREMULTIPLIER.png", False, 0],
        "SLOWDOWN": ["assets/powerups/SLOWDOWN.png", False, 0],
        "SPEEDBOOST": ["assets/powerups/SPEEDBOOST.png", False, 0]
    }
    powerupDuration = 5000 #milliseconds

    score = 0

    # Default x values for each lane 
    lanesValuesX = [60, 160, 260, 360]

    speed = 1

    SCREENWIDTH=800
    SCREENHEIGHT=600

    size = (SCREENWIDTH, SCREENHEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Car Racing")

    font = pygame.font.Font(None, 36)

    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()
    
    #initiating each car : 1 for player and 4 types of incoming cars that the player should dodge
    playerCar = Car("assets/cars/car_player_1.png", 60, 80, 1)
    playerCar.rect.x = 160
    playerCar.rect.y = SCREENHEIGHT - 100
    print("playerCar position:", playerCar.rect.x, playerCar.rect.y)

    car1 = Car("assets/cars/car_npc_1.png", 60, 80, random.randint(50,100))
    car1.rect.x = 60
    car1.rect.y = -100

    car2 = Car("assets/cars/car_npc_2.png", 60, 80, random.randint(50,100))
    car2.rect.x = 160
    car2.rect.y = -600

    car3 = Car("assets/cars/car_npc_3.png", 60, 80, random.randint(50,100))
    car3.rect.x = 260
    car3.rect.y = -300

    car4 = Car("assets/cars/car_npc_4.png", 60, 80, random.randint(50,100))
    car4.rect.x = 360 
    car4.rect.y = -900 

    # Add the cars to the list of objects
    all_sprites_list.add(playerCar)
    all_sprites_list.add(car1)
    all_sprites_list.add(car2)
    all_sprites_list.add(car3)
    all_sprites_list.add(car4)

    all_coming_cars = pygame.sprite.Group()
    all_coming_cars.add(car1)
    all_coming_cars.add(car2)
    all_coming_cars.add(car3)
    all_coming_cars.add(car4)

    all_powerups = pygame.sprite.Group()

    # If is multiplayer add an extra player car
    if(multiplayer):
        secondPlayerCar = Car("assets/cars/car_player_1.png", 60, 80, 1)
        secondPlayerCar.rect.x = 360
        secondPlayerCar.rect.y = SCREENHEIGHT - 100
        all_sprites_list.add(secondPlayerCar)
        print("secondPlayerCar position:", secondPlayerCar.rect.x, secondPlayerCar.rect.y)

    # Load background image
    background_image = pygame.image.load("assets/interface/interfacetres.png")
    background_image = pygame.transform.scale(background_image, (SCREENWIDTH, SCREENHEIGHT))

    #Allowing the user to close the window...
    carryOn = True
    clock=pygame.time.Clock()
    last_time = pygame.time.get_ticks()

    while carryOn:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    carryOn=False
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x:
                         playerCar.moveRight(10)

            # Default single player car controls arrow up down left right
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                playerCar.moveLeft(5)
            if keys[pygame.K_d]:
                playerCar.moveRight(5)
            if keys[pygame.K_w]:
                playerCar.moveUp(5)
            if keys[pygame.K_s]:
                playerCar.moveDown(5)


            # If there is a second player control it by W S A D
            if(multiplayer):
                if keys[pygame.K_LEFT]:
                    secondPlayerCar.moveLeft(5)
                if keys[pygame.K_RIGHT]:
                    secondPlayerCar.moveRight(5)
                if keys[pygame.K_UP]:
                    secondPlayerCar.moveUp(5)
                if keys[pygame.K_DOWN]:
                    secondPlayerCar.moveDown(5)

            
            # CHECKING IF POWERUPS ARE ACTIVATED 
            # IF YES , DO THE RESPECTIVE POWER UP
            # IF IT HAS PASSED MORE THEN THE POWER UP DURATION, TURN IT OFF
            if(powerupDictionary["SCOREMULTIPLIER"][1]):
                timePassed = (pygame.time.get_ticks() - powerupDictionary["SCOREMULTIPLIER"][2])
                if(timePassed >= powerupDuration):
                    powerupDictionary["SCOREMULTIPLIER"][1] = False
                    powerupDictionary["SCOREMULTIPLIER"][2] = 0
                score += pygame.time.get_ticks() * 0.0001 * 4
            score += pygame.time.get_ticks() * 0.0001

            if(powerupDictionary["SLOWDOWN"][1]):
                timePassed = (pygame.time.get_ticks() - powerupDictionary["SLOWDOWN"][2])
                if(timePassed >= powerupDuration):
                    powerupDictionary["SLOWDOWN"][1] = False
                    powerupDictionary["SLOWDOWN"][2] = 0
                speed -= 0.05
            
            if(powerupDictionary["SPEEDBOOST"][1]):
                playerCar.speed = playerCar.speed * 1.5
                timePassed = (pygame.time.get_ticks() - powerupDictionary["SPEEDBOOST"][2])
                if(timePassed >= powerupDuration):
                    powerupDictionary["SPEEDBOOST"][1] = False
                    powerupDictionary["SPEEDBOOST"][2] = 0
                    playerCar.speed = playerCar.speed / 1.5
            
            # RANDOM POWER UP GENERATOR
            # EVERY 5 TO 10 SECONDS GENERATE A NEW POWER UP AT A RANDOM POSITION
            this_time = pygame.time.get_ticks()
            if this_time - last_time >= random.randint(5000, 10000):
                newPowerupType = powerupList[random.randint( 0 , len(powerupList)-1 )]
                newPowerup = Powerup(powerupDictionary[newPowerupType][0], newPowerupType)
                newPowerup.rect.x = lanesValuesX[random.randint(0, 3)]
                newPowerup.rect.y = random.randint(0, 800)
                all_sprites_list.add(newPowerup)
                all_powerups.add(newPowerup)
                last_time = this_time 

            #CHECK IF THERE IS ANY POWERUP THAT HAS SURPASSED THE INTENDED DURATION
            #IF YES , TURN IT OFF 
            for powerup in powerupDictionary:
                timePassed = (pygame.time.get_ticks() - powerupDictionary[powerup][2])
                if(powerupDictionary[powerup][1] == True and timePassed >= powerupDuration):
                    powerupDictionary[powerup][1] = False
                    powerupDictionary[powerup][2] = 0
 
            # STAR = POWER UP
            # MOVING THE STARS DOWN THE LANE, AND KILLING THEM WHEN THEY REACH END OF SCREEN
            for star in all_powerups:
                star.moveForward()
                if star.rect.y > SCREENHEIGHT:
                    all_powerups.remove(star)
                    all_sprites_list.remove(star)
                    star.kill()

            #CHECK IF THERE IS ANY COLLISION BETWEEN A STAR AND THE PLAYER CAR
            #IF YES ACTIVATE THE POWER UP CONDITION
            star_collision_list = pygame.sprite.spritecollide(playerCar, all_powerups, False)
            for star in star_collision_list:
                powerupDictionary[star.type][1] = True
                powerupDictionary[star.type][2] = pygame.time.get_ticks()
                all_powerups.remove(star)
                all_sprites_list.remove(star)
                star.kill()

            #MAKING THE INCOMING CAR MOVE, IF THEY REACH END OF SCREEN 
            #SEND THEM BACK TO THE START OF THE LANE 
            for car in all_coming_cars:
                car.moveForward(speed)
                if car.rect.y > SCREENHEIGHT:
                    car.changeSpeed(random.randint(50,100))
                    car.rect.y = -200

                # Check if there is a car collision
                car_collision_list = pygame.sprite.spritecollide(playerCar, all_coming_cars, False)
                for car in car_collision_list:
                    if(powerupDictionary["INVINCIBLE"][1] == False):
                        print("Car crash!")
                        # End Of Game
                        carryOn = False

            all_sprites_list.update()

            #Drawing on Screen
            screen.blit(background_image, (0, 0))  # Draw the background image
            #Draw The Road
            pygame.draw.rect(screen, NICEGREY, [40,0, 400,SCREENHEIGHT])
            #Draw Line painting on the road
            pygame.draw.line(screen, WHITE, [140,0],[140,SCREENHEIGHT],5)
            #Draw Line painting on the road
            pygame.draw.line(screen, WHITE, [240,0],[240,SCREENHEIGHT],5)
            #Draw Line painting on the road
            pygame.draw.line(screen, WHITE, [340,0],[340,SCREENHEIGHT],5)

            #WRITE SCORE IN THE RIGHT PART OF THE SCREEN
            score_text = font.render("score: {}".format(int(score)), True, NICEGREY)
            screen.blit(score_text, [500, 400])

            #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
            all_sprites_list.draw(screen)

            #Refresh Screen
            pygame.display.flip()

            #Number of frames per secong e.g. 60
            clock.tick(60)

    pygame.quit()

