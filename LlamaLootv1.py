import pygame, sys, time, random # IMPORTS
from pygame.locals import * # LOCAL IMPORT
import pygame.freetype # FREETYPE IMPORT

pygame.init() # INITIALIZE THE GAME
pygame.mixer.init()
# GAME RESOLUTION
width = 1100 # WINDOW WIDTH !IMPORTANT!
height = 700 # WINDOW HEIGHT !IMPORTANT!
window = pygame.display.set_mode((width, height)) # WINDOW ASPECT RATIO
pygame.display.set_caption('Test') # MAIN WINDOW TITLE
pygame.display.set_icon(pygame.image.load('Assets/vbucklogo.png'))

# TEXT RENDER ENGINE
def textformat(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText

# COLORS
Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
LightBlue = (0,125,255)

# FONTS
MainFont = 'Assets/gamefont.otf'

#MUSIC
Menu_music = pygame.mixer.music.load('Assets/menuscreenmusic.mp3')

# GAME FRAMERATE
clock = pygame.time.Clock()
FPS=59.94 # FPS !IMPORTANT!

# MOUSE 
mouse = pygame.mouse.get_pos() # MOUSE VARIABLE !IMPORTANT!


# ASSETS
homebutton = pygame.image.load('Assets/homebutton.png')
homebuttonwhite = pygame.image.load('Assets/homebuttonwhite.png')
lockerbutton = pygame.image.load('Assets/lockerbutton.png')
lockerbuttonwhite = pygame.image.load('Assets/lockerbuttonwhite.png')
storebutton = pygame.image.load('Assets/storebutton.png')
storebuttonwhite = pygame.image.load('Assets/storebuttonwhite.png')
exitbutton = pygame.image.load('Assets/exitbutton.png')
exitbuttonwhite = pygame.image.load('Assets/exitbuttonwhite.png')
comingsoonwhite = pygame.image.load('Assets/comingsoonsmall.png')
battlepasswhite = pygame.image.load('Assets/Battlepass.png')
vbuckswhite = pygame.image.load('Assets/bbuckswhite.png')
fullscreen = pygame.image.load('Assets/fullscreenicon.png')
smallscreen = pygame.image.load('Assets/smallscreenicon.png')
fullscreentext = pygame.image.load('Assets/fullscreentesting.png')
llamatext = pygame.image.load('Assets/llamaword.png')
open_packs = pygame.image.load('Assets/openpackstext.png')
newsbutton = pygame.image.load('Assets/newsbutton.png')
tradingbuttonimage = pygame.image.load('Assets/tradingbutton.png')

# FADE THE SCREEN ( DELAY = 20 )
def fade(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0,300):
        fade.set_alpha(alpha)
        window.blit(fade,(0,0))
        pygame.display.update()
        pygame.time.delay(20)
        
def shortfade(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0,300):
        fade.set_alpha(alpha)
        window.blit(fade,(0,0))
        pygame.display.update()
        pygame.time.delay(5)

def homebutton1(x,y):
    window.blit(homebutton, (x,y))

def storebutton1(x,y):
    window.blit(storebutton, (x,y))

def lockerbutton1(x,y):
    window.blit(lockerbutton, (x,y))

def comingsoonbutton1(x,y):
    window.blit(comingsoonwhite, (x,y))

def battlepassbutton1(x,y):
    window.blit(battlepasswhite, (x,y))

def vbucksbutton(x,y):
    window.blit(vbuckswhite, (x,y))

def resourceload3(x,y):
    window.blit(loading3, (x,y))

def fullscreenbutton(x,y):
    window.blit(fullscreenicon, (x,y))

def smallscreenbutton(x,y):
    window.blit(smallscreenicon, (x,y))

def fullscreenword(x,y):
    window.blit(fullscreentext, (x,y))

def llamawordtext(x,y):
    window.blit(llamatext, (x,y))

def openpackstext(x,y):
    window.blit (open_packs, (x,y))

def tradingbuttonword(x,y):
    window.blit(tradingbuttonimage, (x,y))

# LOADING SCREEN
def Preload():

    Preload = True
    while Preload:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    selected =  fade(width, height)
                if event.key==pygame.K_RETURN:
                    selected = menu()
                elif event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                    
        window.fill(LightBlue)
        GameInfo = textformat("Llama Loot! (Version 0.1 - Alpha)", MainFont, 55, White) #preload Version info
        BugAlert = textformat("This game is in its very early testing stages.",MainFont, 25, White)
        BugAlert2 = textformat("Please Expect bugs, lags, glitches and some other aspects of the game to not work as intended.", MainFont, 25, White)    
        BugAlert3 = textformat("We update Llama Loot EVERY WEEK! Join our discord and let us know what YOU would like to see in future updates!", MainFont, 25, White)
        loadPrompt = textformat("Press ENTER To Continue.", MainFont, 60, White)
        Devs = textformat("Created By the LlamaLoot Development Team.",MainFont, 28, White)

        GameInfoRect = GameInfo.get_rect()
        BugAlertRect = BugAlert.get_rect()
        BugAlert2Rect = BugAlert2.get_rect()
        BugAlert3Rect = BugAlert3.get_rect()
        loadPromptRect = loadPrompt.get_rect()
        DevsRect = Devs.get_rect()

        window.blit(GameInfo, (width/2 - (GameInfoRect[2]/2), 65))
        window.blit(BugAlert, (width/2 - (BugAlertRect[2]/2), 150))
        window.blit(BugAlert2, (width/2 - (BugAlert2Rect[2]/2), 173))
        window.blit(BugAlert3, (width/2 -(BugAlert3Rect[2]/2), 198))
        window.blit(loadPrompt, (width/2 - (loadPromptRect[2]/2), 375))
        window.blit(Devs, (width/2 - (DevsRect[2]/2), 650))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Loading...")

        
        mouse = pygame.mouse.get_pos()
                    


# MAIN MENU
class mixerWrapper():

    def __init__(self):
        self.IsPaused = False

    def toggleMusic(self):
        if self.IsPaused:
            pygame.mixer.music.unpause()
            self.IsPaused = False
        else:
            pygame.mixer.music.pause()
            self.IsPaused = True


def menu():


    pygame.mixer.music.load('Assets/menuscreenmusic.mp3')
    pygame.mixer.music.play(0)

    
    menu = True
    selected = "start"


    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    if selected=="quit":
                        selected="Patch Notes"
                    elif selected=="Patch Notes":
                        selected="start"
                if event.key==pygame.K_DOWN:
                    if selected=="start":
                        selected= "Patch Notes"
                    elif selected=="Patch Notes":
                        selected="quit"
                elif event.key==pygame.K_ESCAPE:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        pygame.mixer.music.fadeout(500)
                        fade(width, height)
                        selected=homescreen()
                    elif selected=="Patch Notes":
                        fade(width, height)
                        selected = patchnotes()
                    if selected=="quit":
                        selected = quitconfirm()
                if event.key==pygame.K_m:
                    pygame.mixer.music.pause()


                    
        window.fill(LightBlue) # WINDOW COLOR
        version = textformat("0.1 (Alpha)", MainFont, 30, White) # VERSION INFO !IMPORTANT!
        title = textformat("Llama Loot!", MainFont, 90, White) # GAME TITLE COLOR
        if selected=="start":
            textstart = textformat("START", MainFont, 85, Black)# START BUTTON WHEN HOVERED
        else:
            textstart = textformat("START", MainFont, 70, White) # DORMANT START BUTTON
        if selected=="Patch Notes":
            textpatchnotes = textformat("PATCH NOTES (0.1.0)", MainFont, 85, Black) # PATCH NOTES BUTTON WHEN HOVERED ON
        else:
            textpatchnotes = textformat("PATCH NOTES (0.1.0)", MainFont, 70, White) # DORMANT PATCH NOTES BUTTON
        if selected=="quit":
            textquit = textformat("QUIT (Enter)", MainFont, 70, Black) # QUIT BUTTON WHEN HOVERED ON
        else:
            textquit = textformat("QUIT (Escape)", MainFont, 50, Red) # DORMANT QUIT BUTTON
        
        versionrect = version.get_rect()
        titlerect = title.get_rect()
        startrect = textstart.get_rect()
        patchrect = textpatchnotes.get_rect()
        quitrect = textquit.get_rect()

        window.blit(version, (width/2 - (versionrect[2]/2), 50)) # VERSION INFO !IMPORTANT!
        window.blit(title, (width/2 - (titlerect[2]/2), 80)) # GAME TITLE
        window.blit(textstart, (width/2 - (startrect[2]/2), 300)) # BUTTON THAT STARTS THE GAME
        window.blit(textpatchnotes, (width/2 -(patchrect[2]/2), 385)) # BUTTON DIRECTING YOU TO PATCH NOTES SCREEN
        window.blit(textquit, (width/2 - (quitrect[2]/2), 470)) # QUIT GAME BUTTON
        window.blit(fullscreentext, (820,30))
        window.blit(fullscreen, (1040,25))
        

        pygame.display.update()
        clock.tick(FPS) # MAIN MENU FPS !IMPORTANT!
        pygame.display.set_caption("Llama Loot (Alpha)") # WINDOW TITLE

        

# PATCH NOTES
def patchnotes():

    patchnotes = True

    while patchnotes:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    selected = shortfade(width, height)
                if event.key==pygame.K_RETURN:
                    selected = menu()
                if event.key==pygame.K_ESCAPE:
                    selected = shortfade(width, height)
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                
        window.fill(Black)
        patchversion = textformat("0.1 (Alpha)", MainFont, 40, White)
        patchtitle = textformat("Llama Loot", MainFont, 90, White)
        patchnote_1 = textformat("-Game Launch!", MainFont, 30, White)


        patchversionRect = patchversion.get_rect()
        patchtitleRect = patchtitle.get_rect()
        patchnote_1Rect = patchnote_1.get_rect()

        window.blit(patchversion, (width/2 - (patchversionRect[2]/2), 50))
        window.blit(patchtitle, (width/2 - (patchtitleRect[2]/2), 80))
        window.blit(patchnote_1, (width/2 - (patchnote_1Rect[2]/2), 250))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Llama Loot Patch Notes")


# CONFIRM QUIT 
def quitconfirm():

    quitconfirm = True
    selected = "Yes"

    while quitconfirm:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_DOWN:
                    selected = "No"
                if event.key==pygame.K_UP:
                    selected = "Yes"
                if event.key==pygame.K_RETURN:
                    if selected =="Yes":
                        pygame.quit()
                        quit()
                    if selected == "No":
                        selected = shortfade(width, height)
                        menu()
                        
        window.fill(LightBlue)
        quitprompt = textformat("Are You Sure You Want To Quit?", MainFont, 70, White)
        if selected == "Yes":
            confirm_yes = textformat("Yes", MainFont, 75, Black)
        else:
            confirm_yes = textformat("Yes", MainFont, 60, White)
        if selected == "No":
            confirm_no = textformat("No", MainFont, 75, Black)
        else:
            confirm_no = textformat("No", MainFont, 60, White)

        quitpromptRect = quitprompt.get_rect()
        confirmyesRect = confirm_yes.get_rect()
        confirmnoRect = confirm_no.get_rect()

        window.blit(quitprompt, (width/2 - (quitpromptRect[2]/2), 75))
        window.blit(confirm_yes, (width/2 - (confirmyesRect[2]/2), 250))
        window.blit(confirm_no, (width/2 - (confirmnoRect[2]/2), 320))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Quit ?")





def testingscreen():

    testingscreen = True

    while testingscreen:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event == pygame.k_RETURN:
                    selected = homescreen()

    window.fill(LightBlue)

    sentence1 = textformat("This part of the game is currently in testing.", MainFont, 40, White)
    sentence2 = textformat("Please check back in the next update!", MainFont, 40, White)

    sen1rect = sentence1.get_rect()
    sen2rect = sentence2.get_rect()

    window.blit(sentence1, (width/2 - (sen1rect[2]/2), 90))
    window.blit(sentence2, (width/2 - (sen2rect[2]/2), 120))


    pygame.display.update()
    clock.tick(FPS)




    




# HOME SCREEN
def homescreen():
    
    pygame.mixer.music.fadeout(-1)
    
    homescreen = True
    

    while homescreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        window.fill(LightBlue)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        selected = (click)

        if 100+75 > mouse[0] > 100 and 60+45 > mouse[1] > 60:
           window.blit(homebuttonwhite,(100,75))
           if click[0] == 1:
               print("youre already home!")
           
        else:
           window.blit(homebuttonwhite,(100,75))

        if 528+75 > mouse[0] > 500 and 60+45 > mouse[1] > 60:
           window.blit(lockerbuttonwhite,(500,75))
           if click[0] ==1:
               selected = lockerscreen()
        else:
            window.blit(lockerbutton,(500,70))
            
        if 903+85 > mouse[0] > 895 and 25+75 > mouse[1] > 60:
            window.blit(storebuttonwhite,(900,75))
            print("This Feature is coming soon!")            
        else:
            window.blit(storebutton,(900,70))
        if 23+60 > mouse[0] > 8 and 23+650 > mouse[1] > 645:
            window.blit(exitbuttonwhite,(20,650))
            if click[0] == 1:
                selected = menu()
        else:
            window.blit(exitbutton,(20,650))
            




        pygame.draw.rect(window, True, (50,200,200,225))
        pygame.draw.rect(window, True, (450,200,200,225))
        pygame.draw.rect(window, True, (450,475,200,50))
        pygame.draw.rect(window, True, (850,200,200,225))

        pygame.draw.rect(window, True, (900,15,110,23))
        pygame.draw.rect(window, True, (100,110,75,3))
        pygame.draw.rect(window, True, (500,110,100,3))
        pygame.draw.rect(window, True, (900,110,88,3))
   

    
        window.blit(comingsoonwhite, (485, 465))
        window.blit(vbuckswhite, (902,19))

        if 73+150 > mouse[0] > 70 and 73+240 > mouse[1] > 280:
            window.blit(battlepasswhite, (73,290))
            pygame.draw.rect(window, True, (40,190,220,3))
            pygame.draw.rect(window, True, (40,190,3,244))
            pygame.draw.rect(window, True, (40,433,220,3))
            pygame.draw.rect(window, True, (258,190,3,244))
            window.blit(comingsoonwhite, (85,205))
            if click[0] == 1:
                selected = testingscreen()
        else:
            window.blit(battlepasswhite, (73,300))
            window.blit(comingsoonwhite, (85,190))
        if 480+145 > mouse[0] > 475 and 90+230 > mouse[1] > 285:
            window.blit(open_packs, (480,290))
            pygame.draw.rect(window, True, (440,190,220,3))
            pygame.draw.rect(window, True, (440,190,3,244))
            pygame.draw.rect(window, True, (440,433,220,3))
            pygame.draw.rect(window, True, (658,190,3,244))
            window.blit(comingsoonwhite, (485,205))
            if click[0] == 1:
                selected = testingscreen()
        else:
            window.blit(open_packs, (480,300))
            window.blit(comingsoonwhite, (485,190))
        if 900+145 > mouse[0] > 895 and 90+230 > mouse[1] > 285:
            window.blit(tradingbuttonimage, (900,290))
            window.blit(comingsoonwhite, (885,205))
            pygame.draw.rect(window, True, (840,190,220,3))
            pygame.draw.rect(window, True, (840,190,3,244))
            pygame.draw.rect(window, True, (840,433,220,3))
            pygame.draw.rect(window, True, (1058,190,3,244))
            if click[0] == 1:
                selected = testingscreen()
           
        else:
            window.blit(tradingbuttonimage, (900,300))
            window.blit(comingsoonwhite, (885,190))

            
        
        

        pygame.display.update()
        clock.tick(FPS)


def testingscreen():

    testingscreen = True

    while testingscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                   homescreen()

    
        window.fill(LightBlue)

        sentence1 = textformat("This part of the game is currently in testing.", MainFont, 40, White)
        sentence2 = textformat("Please check back in the next update!", MainFont, 40, White)
        gobacktip = textformat("Press ENTER to go back", MainFont, 50, White)
    

        sen1rect = sentence1.get_rect()
        sen2rect = sentence2.get_rect()
        gobackrect= gobacktip.get_rect()

        window.blit(sentence1, (width/2 - (sen1rect[2]/2), 90))
        window.blit(sentence2, (width/2 - (sen2rect[2]/2), 120))
        window.blit(gobacktip, (width/2 - (gobackrect[2]/2), 200))


        pygame.display.update()
        clock.tick(FPS)


def lockerscreen():

     lockerscreen = True

     while lockerscreen:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()

                 window.fill(LightBlue)

                 pygame.display.update()
                 clock.tick(FPS)
        


lockerscreen()



    
            
        
        










