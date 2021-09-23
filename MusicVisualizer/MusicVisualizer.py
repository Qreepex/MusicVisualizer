import pygame, sys, os, pyautogui, pyaudio, wave, audioop, time
from random import randint as ri
from termcolor import colored as col
pygame.init()

ParticleProperties = [] # dont change anything


# Append helper
# ParticleProperties.append({'sx': 0, 'sy': 0, 'size': 0, 'col': (255, 255, 255), 'life': 0, 'redubounce': 0, 'grav': 0, 'AirFric': 0,  'move': True, 'rect': pygame.Rect(0, 0, 0, 0)})
#                                             speedx |                        |                                  |              |                        |              |                                           |
#                                                        speedy               |                                  |              |                       |               |                                            |
#                                                                                   color                          |             |                        |               |                                            |
#                                                                                                                     lifetime  |                       |               |                                            |
#                                                                                                                                   reducespeed     |               |                                            |
#                                                                                                                                   on bounce        |                |                                           |
#                                                                                                                                   (division)         |                |                                           |
#                                                                                                                                                          gravitation |                                           |
#                                                                                                                                                                           Air Friction                          |
#                                                                                                                                                                                                                       Rectangle

realpath = str(os.path.realpath("./") + "/").replace("\\", "/") # dont change anything


font = pygame.font.SysFont('comicsans', 20)
background = pygame.image.load(f"{realpath}Background.png")

width, height = pyautogui.size() 

Simheight = height
Simwidth = width

Gravitation = 1 # Normal 1
SimSpeed = 1 # Normal 1 || When Higher the Sim is slower || Not go under 1
AirFriction = 0.05 # Normal 0.05
Size = 10 # Normal 10
redubounce = 1.5 # Normal 1.5
lifeTime = 34 # Normal 34
maxThrowSpeed = 150 # Normal 150

cursor = pygame.Rect(0, 0, Size, Size) # dont change anything

Delete = False # dont change anything

Locked = False # dont change anything
Lockpos = [0, 0] # dont change anything

def checkPath():
    while True: 
        path = input(col("Enter the Path to your music. NEED TO BE A '.WAV' FILE!!!\n>>>   ", "cyan"))
        if not path.split("/")[-1].__contains__("."): print(col("-- Path need to be an file --", "green")); continue
        if not path.endswith(".wav"): print(col("-- File not an wave file --", "yellow")); continue
        if not os.path.exists(path): print(col("-- path does not exists --", "red")); continue
        print(col("Loading... Pleas stand by a bit.", "cyan")); return path
songpath = checkPath()

wf = wave.open(songpath)



WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption('ParticleSim')
pygame.mouse.set_visible(False)

def Spawn_Green():
    x, y = 0, 0
    x1 = Simwidth
    for _ in range(0, 5):
        ParticleProperties.append({'sx': ri(5, 15), 'sy': ri(5, 15), 'size': Size, 'col': (0+ri(0, 90), 255-ri(0, 90), 0+ri(0, 90)), 'life': lifeTime-ri(0, 20), 'redubounce': redubounce, 'grav': Gravitation, 'AirFric': AirFriction, 'move': True, 'rect': pygame.Rect(x, y, Size, Size), 'border': True})
        ParticleProperties.append({'sx': ri(-15, -5), 'sy': ri(5, 15), 'size': Size, 'col': (0+ri(0, 90), 255-ri(0, 90), 0+ri(0, 90)), 'life': lifeTime-ri(0, 20), 'redubounce': redubounce, 'grav': Gravitation, 'AirFric': AirFriction, 'move': True, 'rect': pygame.Rect(x1, y, Size, Size), 'border': True})

def Spawn_Blue():
    x, y = 0, Simheight
    x1 = Simwidth
    ParticleProperties.append({'sx': ri(28, 30), 'sy': ri(-40, -38), 'size': Size, 'col': (0+ri(0, 90), 0+ri(0, 90), 255-ri(0, 90)), 'life': lifeTime+lifeTime-ri(0, 20), 'redubounce': redubounce, 'grav': Gravitation, 'AirFric': AirFriction, 'move': True, 'rect': pygame.Rect(x, y, Size, Size), 'border': True})
    ParticleProperties.append({'sx': ri(-30, -28), 'sy': ri(-40, -38), 'size': Size, 'col': (0+ri(0, 90), 0+ri(0, 90), 255-ri(0, 90)), 'life': lifeTime+lifeTime-ri(0, 20), 'redubounce': redubounce, 'grav': Gravitation, 'AirFric': AirFriction, 'move': True, 'rect': pygame.Rect(x1, y, Size, Size), 'border': True})

def Spawn_Red():
    for _ in range(0, 10):
        ParticleProperties.append({'sx': ri(-20, 20), 'sy': ri(-13, -5), 'size': Size, 'col': (255-ri(0, 100), 0+ri(0, 90), 0+ri(0, 90)), 'life': lifeTime-ri(0, 10), 'redubounce': redubounce, 'grav': 0, 'AirFric': AirFriction//2, 'move': True, 'rect': pygame.Rect(ri(0, Simwidth), Simheight, Size, Size), 'border': True})

def Spawn_Violet():
    x, y = ri(0, Simwidth), ri(0, Simheight)
    for _ in range(0, 8):
        ParticleProperties.append({'sx':0, 'sy': ri(-3, 0), 'size': Size, 'col': (135-ri(0, 40), 47+ri(0, 40), 186-ri(0, 40)), 'life': lifeTime-ri(0, 10), 'redubounce': redubounce, 'grav': -1, 'AirFric': 0, 'move': True, 'rect': pygame.Rect(x, y, Size, Size), 'border': False})

def Spawn_Pink():
    half = Simwidth//2
    y, x1, x2 = 0,  half-half//2, half+half//2
    ParticleProperties.append({'sx': ri(-4, 4), 'sy': ri(2, 5), 'size': Size, 'col': (245-ri(0, 40), 81-ri(0, 40), 217-ri(0, 40)), 'life': lifeTime+ri(0, 10), 'redubounce': redubounce, 'grav': 1, 'AirFric': 0, 'move': True, 'rect': pygame.Rect(x1, y, Size, Size), 'border': False})
    ParticleProperties.append({'sx': ri(-4, 4), 'sy': ri(2, 5), 'size': Size, 'col': (245-ri(0, 40), 81-ri(0, 40), 217-ri(0, 40)), 'life': lifeTime+ri(0, 10), 'redubounce': redubounce, 'grav': 1, 'AirFric': 0, 'move': True, 'rect': pygame.Rect(x2, y, Size, Size), 'border': False})

def Spawn_Gold():
    x, x1 = 0, Simwidth
    for _ in range(0, 5):
        ParticleProperties.append({'sx': ri(0, 10), 'sy': ri(1, 7), 'size': Size, 'col': (255-ri(0, 90), 217-ri(0, 90), 0+ri(0, 90)), 'life': lifeTime+ri(0, 10), 'redubounce': redubounce, 'grav': .4, 'AirFric': AirFriction, 'move': True, 'rect': pygame.Rect(x, ri(0, Simheight), Size, Size), 'border': True})
        ParticleProperties.append({'sx': ri(-10, 0), 'sy': ri(1, 7), 'size': Size, 'col': (255-ri(0, 90), 217-ri(0, 90), 0+ri(0, 90)), 'life': lifeTime+ri(0, 10), 'redubounce': redubounce, 'grav': .4, 'AirFric': AirFriction, 'move': True, 'rect': pygame.Rect(x1, ri(0, Simheight), Size, Size), 'border': True})

def Spawn_Cyan():
    x, y = Simwidth//2, Simheight//2
    ParticleProperties.append({'sx': ri(-30, 30), 'sy': ri(-30, 30), 'size': Size, 'col': (0+ri(0, 90), 255-ri(0, 90), 162-ri(0, 90)), 'life': lifeTime+ri(0, 10), 'redubounce': redubounce, 'grav': 0, 'AirFric': 0, 'move': True, 'rect': pygame.Rect(x, y, Size, Size), 'border': False})

def Spawn_VioletPink():
    halfx = Simwidth//2
    halfy = Simheight//2
    spawn = 3
    for _ in range(0, 40):
        ParticleProperties.append({'sx': ri(5, 50), 'sy': ri(-2, 2), 'size': Size, 'col': (255-ri(0, 110), 0+ri(0, 70), 102+ri(-55, 50)), 'life': lifeTime//ri(1, 10), 'redubounce': redubounce, 'grav': 0, 'AirFric': 0, 'move': True, 'rect': pygame.Rect(spawn, halfy, Size, Size), 'border': True})
        # Left
        ParticleProperties.append({'sx': ri(-50, -5), 'sy': ri(-2, 2), 'size': Size, 'col': (255-ri(0, 110), 0+ri(0, 70), 102+ri(-55, 50)), 'life': lifeTime//ri(1, 10), 'redubounce': redubounce, 'grav': 0, 'AirFric': 0, 'move': True, 'rect': pygame.Rect(Simwidth-spawn, halfy, Size, Size), 'border': True})
        # Right
        ParticleProperties.append({'sx': ri(-2, 2), 'sy': ri(5, 50), 'size': Size, 'col': (255-ri(0, 110), 0+ri(0, 70), 102+ri(-55, 50)), 'life': lifeTime//ri(1, 10), 'redubounce': redubounce, 'grav': 0, 'AirFric': 0, 'move': True, 'rect': pygame.Rect(halfx, spawn, Size, Size), 'border': True})
        # Top
        ParticleProperties.append({'sx': ri(-2, 2), 'sy': ri(-50, -5), 'size': Size, 'col': (255-ri(0, 110), 0+ri(0, 70), 102+ri(-55, 50)), 'life': lifeTime//ri(1, 10), 'redubounce': redubounce, 'grav': 0, 'AirFric': 0, 'move': True, 'rect': pygame.Rect(halfx, Simheight-spawn, Size, Size), 'border': True})
        # Buttom

def Spawn_Rainbow():
    halfx = Simwidth//2
    halfy = Simheight//2
    for _ in range(0, 20):
        ParticleProperties.append({'sx': ri(-20, 20), 'sy': ri(-20, 20), 'size': Size, 'col': (0+ri(0, 255), 0+ri(0, 255), 0+ri(0, 255)), 'life': lifeTime+ri(1, 10), 'redubounce': redubounce, 'grav': 0, 'AirFric': 0, 'move': True, 'rect': pygame.Rect(halfx, halfy, Size, Size), 'border': True})

def SimulatePartic():
    for part in ParticleProperties:

        if part['life'] != -1: part['life'] = part['life'] - 1
        if part['life'] == 0: ParticleProperties.remove(part)

        if part['move']:
            part['sy'] += part['grav']

            if part['border']:
                if part['rect'].x + Size > Simwidth and part['sx'] > 0: part['sx']= -part['sx'] // part['redubounce']
                elif part['rect'].x < 0 and part['sx'] < 0: part['sx']= -(part['sx'] // part['redubounce'])
                if part['rect'].x > Simwidth +Size+Size: part['rect'].x = Simwidth-Size

                if part['rect'].y + Size > Simheight and part['sy'] > 0: part['sy'] = -(part['sy'] // part['redubounce'])
                elif part['rect'].y < 0 and part['sy'] < 0: part['sy'] = -(part['sy'] // part['redubounce'])
                if part['rect'].y > Simheight +Size+Size: part['rect'].y = Simheight-Size

            if part['sx'] < 0: part['sx'] += part['AirFric']
            elif part['sx'] > 0: part['sx'] -= part['AirFric']
            if int(part['sx']) == 0: part['sx'] = 0

            if part['rect'].y == Simheight-Size+1 and part['sy'] == 0 and part['sx'] == 0: part['move'] = False

            part['rect'].x += part['sx']
            part['rect'].y += part['sy']


        if Delete:
            cursor.width = Size*2
            cursor.height = Size*2
            if cursor.colliderect(part['rect']):
                try: ParticleProperties.remove(part)
                except: continue
        else:
            cursor.width = Size
            cursor.height = Size



################################################################################
maxValue = 2**15
bars = 35
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 # change when needed
RATE = 44100
p = pyaudio.PyAudio()
stream = p.open(format =
                p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)
##############################################################################

trigger_Violet = .05
trigger_Pink = .1
trigger_Gold = .15
trigger_Green = .2
trigger_Blue = .25
trigger_Red = .3
trigger_Green2 = .4
trigger_VioletPink = .5
trigger_Rainbow = .6
trigger_ALL = .7

###############################################################################
FPS = 0
volume = 0
clock = pygame.time.Clock()
ticks = 0
data = wf.readframes(chunk)
Song = pygame.mixer.Sound(songpath)
Song.play()

while True:
    start = time.time()
    clock.tick(60)

    WIN.blit(pygame.transform.scale(background, (int(width*(volume+1)), int(height*(volume+1)))), (int(width-(width*(volume+1)))//2, int(height-(height*(volume+1)))//2))
    # WIN.fill((50, 50, 50))

    x,y  = pygame.mouse.get_pos()
    cursor.x, cursor.y, cursor.width, cursor.height = x, y, Size, Size
    keys = pygame.key.get_pressed()


    if keys[pygame.K_SPACE]:
        Delete = True

    if keys[pygame.K_0]:
        Spawn_Blue()
        Spawn_Cyan()
        Spawn_Gold()
        Spawn_Green()
        Spawn_Pink()
        Spawn_Rainbow()
        Spawn_Red()
        Spawn_Violet()
        Spawn_VioletPink()
    if keys[pygame.K_1]:
        Spawn_Green()
    if keys[pygame.K_2]:
        Spawn_Blue()
    if keys[pygame.K_3]:
        Spawn_Red()
    if keys[pygame.K_4]:
        Spawn_Violet()
    if keys[pygame.K_5]:
        Spawn_Pink()
    if keys[pygame.K_6]:
        Spawn_Gold()
    if keys[pygame.K_7]:
        Spawn_Cyan()
    if keys[pygame.K_8]:
        Spawn_VioletPink()
    if keys[pygame.K_9]:
        Spawn_Rainbow()
    if keys[pygame.K_ESCAPE]:
        break
    if keys[pygame.K_p]:
        pygame.mixer.pause()
        time.sleep(1)
        while True:
            WIN.fill((50, 50, 50))
            k = pygame.key.get_pressed()
            if k[pygame.K_p] and k[pygame.K_LSHIFT] or k[pygame.K_RSHIFT]:
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(1)

            pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(Simwidth//2-20, Simheight//2-60, 20, 60))
            pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(Simwidth//2+20, Simheight//2-60, 20, 60))
            for p in ParticleProperties:
                pygame.draw.rect(WIN, p['col'], p['rect'])

            x,y  = pygame.mouse.get_pos()
            cursor.x, cursor.y, cursor.width, cursor.height = x, y, Size, Size
            pygame.draw.rect(WIN, (255, 0, 0), cursor)
            pygame.display.update()

        time.sleep(.01)
        pygame.mixer.unpause()

    if ticks % SimSpeed == 0:
        SimulatePartic()

    for p in ParticleProperties:
        pygame.draw.rect(WIN, p['col'], p['rect'])

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            break

        elif event.type == pygame.MOUSEBUTTONDOWN and not Locked:
            Locked = True
            Lockpos = [x, y]

        elif event.type == pygame.MOUSEBUTTONUP and Locked:
            Locked = False
            speedx = -(x - Lockpos[0])
            speedy = -(y - Lockpos[1])

            mTS = maxThrowSpeed//10

            if speedx > 0 and speedx < 1: speedx = speedx*mTS
            elif speedx > 0 and speedx > 1: speedx = speedx//mTS
            elif speedx < 0 and speedx < -1: speedx = speedx//mTS
            elif speedx < 0 and speedx > -1: speedx = speedx*mTS

            if speedy > 0 and speedy < 1: speedy = speedy*mTS
            elif speedy > 0 and speedy > 1: speedy = speedy//mTS
            elif speedy < 0 and speedy < -1: speedy = speedy//mTS
            elif speedy < 0 and speedy > -1: speedy = speedy*mTS

            if speedx > maxThrowSpeed: speedx = maxThrowSpeed
            elif speedx < -maxThrowSpeed: speedx = -maxThrowSpeed
            if speedy > maxThrowSpeed: speedy = maxThrowSpeed
            elif speedy < -maxThrowSpeed: speedy = -maxThrowSpeed

            for _ in range(0, 10):
                ParticleProperties.append({'sx': speedx+ri(-5, 5), 'sy': speedy+ri(-5, 5), 'size': Size, 'col': (255-ri(0, 100), 255-ri(0, 100), 255-ri(0, 100)), 'life': lifeTime*3, 'redubounce': redubounce, 'grav': Gravitation, 'AirFric': AirFriction, 'colide': True, 'move': True, 'rect': pygame.Rect(x, y, Size, Size), 'border': True})


    if Locked:
        pygame.draw.line(WIN, (0, 0, 0), (x+(Size//2), y+(Size//2)), (Lockpos[0]+(Size//2), Lockpos[1]+(Size//2)), width=2)
        pygame.draw.rect(WIN, (255, 0, 0), pygame.Rect(Lockpos[0], Lockpos[1], Size, Size))
        speedx = -(x - Lockpos[0])
        speedy = -(y - Lockpos[1])

        mTS = maxThrowSpeed//10

        if speedx > 0 and speedx < 1: speedx = speedx*mTS
        elif speedx > 0 and speedx > 1: speedx = speedx//mTS
        elif speedx < 0 and speedx < -1: speedx = speedx//mTS
        elif speedx < 0 and speedx > -1: speedx = speedx*mTS

        if speedy > 0 and speedy < 1: speedy = speedy*mTS
        elif speedy > 0 and speedy > 1: speedy = speedy//mTS
        elif speedy < 0 and speedy < -1: speedy = speedy//mTS
        elif speedy < 0 and speedy > -1: speedy = speedy*mTS

        if speedx > maxThrowSpeed: speedx = maxThrowSpeed
        elif speedx < -maxThrowSpeed: speedx = -maxThrowSpeed
        if speedy > maxThrowSpeed: speedy = maxThrowSpeed
        elif speedy < -maxThrowSpeed: speedy = -maxThrowSpeed

        WIN.blit(font.render(f"x{speedx}", 1, (255, 255, 255)), (x-Size-5, y+Size+5))
        WIN.blit(font.render(f"y{speedy}", 1, (255, 255, 255)), (x-Size-5, y+Size+Size+10))
    
        # for _ in range(0, 1):
                # ParticleProperties.append({'sx': randint(-20, 20), 'sy': randint(-20, 20), 'size': Size, 'col': (255, 255, 255), 'life': lifeTime, 'redubounce': redubounce, 'grav': Gravitation, 'AirFric': AirFriction, 'colide': True, 'move': True, 'rect': pygame.Rect(x, y, Size, Size)})

    stream.write(data)
    DATA = wf.readframes(chunk)
    volume = round(audioop.rms(DATA, 2), 2)

    if len(DATA) == 0: break
    if volume != 0: volume = float(volume)/float(maxValue)


    if volume >= trigger_ALL:
        Spawn_Blue()
        Spawn_Cyan()
        Spawn_Gold()
        Spawn_Green()
        Spawn_Pink()
        Spawn_Rainbow()
        Spawn_Red()
        Spawn_Violet()
        Spawn_VioletPink()
    elif volume >= trigger_Rainbow:
        Spawn_Rainbow()
    elif volume >= trigger_VioletPink:
        Spawn_VioletPink()
    elif volume >= trigger_Green2:
        Spawn_Cyan
    elif volume >= trigger_Red:
        Spawn_Red()
    elif volume >= trigger_Blue:
        Spawn_Blue()
    elif volume >= trigger_Green:
        Spawn_Green()
    elif volume >= trigger_Gold:
        Spawn_Gold()
    elif volume >= trigger_Pink:
        Spawn_Pink()
    elif volume >= trigger_Violet:
        Spawn_Violet()


    volumebar = f"[{'|'*(int(volume*30))}{' '*(int(30-volume*30))}]"

    WIN.blit(font.render(f"Volume: {volumebar}", 1, (255, 255, 255)), (10, 10))
    WIN.blit(font.render(f"Volume: {round(volume*30, 2)}", 1, (255, 255, 255)), (10, 30))
    WIN.blit(font.render(f"Particels: {len(ParticleProperties)}", 1, (255, 255, 255)), (10, 50))
    if FPS >= 40:
        WIN.blit(font.render(f"FPS: {FPS}", 1, (63, 232, 108)), (10, 70))
    elif FPS >= 30:
        WIN.blit(font.render(f"FPS: {FPS}", 1, (217, 214, 56)), (10, 70))
    elif FPS >= 10:
        WIN.blit(font.render(f"FPS: {FPS}", 1, (230, 64, 46)), (10, 70))

    if ticks % 8 == 0:
        FPS = round(1.0/(time.time()-start+.000000000000001), 1)
        # print(f"Volume:{volumebar}\t   Fps: {FPS}\t   Particels: {len(ParticleProperties)}")
        

    if not Delete: pygame.draw.rect(WIN, (255, 0, 0), cursor)
    else: pygame.draw.rect(WIN, (255, 0, 0), pygame.Rect(x-(Size//2), y-(Size//2), Size*2, Size*2))

    Delete = False
    ticks += 1

    pygame.display.update()

pygame.quit()
stream.close()

print("\n\n\n\n\n\n\n")
print(col("-- Thanks for using this Music Visualizer --", "red"))
print("\n\n\n")
