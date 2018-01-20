#Xie Shawn
#Dec 16 2014

import pygame
import random
from pygame.locals import *
from pygame.color import THECOLORS
pygame.init()
import os, time
import platform
if platform.system()=="Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

size=(400,400)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Pipes Game")
#screen.fill((200,200,200))
pygame.display.flip()
clock=pygame.time.Clock()
keepGoing= True

tfont=pygame.font.SysFont("New Times Roman",22)
x=0
state="menu"
btnNew=pygame.image.load("new.png").convert()
btnInrtuct=pygame.image.load("ins.png").convert()

bg=pygame.image.load("bg.jpg").convert()
bird=pygame.image.load("bird2 copy.gif").convert()
retry=pygame.image.load("retry.png").convert()
menu=pygame.image.load("menu.png").convert()
back=pygame.image.load("back.png").convert()

#Generting the pipes
ran=random.randint(1,5)
ran=str(ran)
up=pygame.image.load ("up"+ran+".png").convert()
down=pygame.image.load ("down"+ran+".png").convert()
ran2=random.randint(1,5)
ran2=str(ran2)
up2=pygame.image.load ("up"+ran2+".png").convert()
down2=pygame.image.load ("down"+ran2+".png").convert()

#background
screen.blit(bg, (0, 0),(x,0,400,400) )

#Intructions
instruct = tfont.render(('How to play:'), True, (0,0,0))
instruct2 = tfont.render(('Press key "w" to '), True, (0,0,0))
instruct3 = tfont.render(('enable your bird to jump or '), True, (0,0,0))
instruct4 = tfont.render(('increase in height lattitude. '), True, (0,0,0))
instruct5 =tfont.render(('Try to avoid as many pipes '),True,(0,0,0))
instruct6 =tfont.render(('as possible.'),True,(0,0,0))
error = tfont.render(('Error!!!!!!!!!'), True, (200,0,10))



try:
    p=400
    p2=p+250
    y=200
    y2=200
    direction="down"
    score=0
    hs=0
    while keepGoing:
        

        clock.tick(60)
        x=x+1
        x=x%401

        screen.blit(bg, (0, 0),(x,0,400,400) )
        
        
        
        if state=="menu":
            bn=screen.blit(btnNew,(125,80))    
            bi=screen.blit(btnInrtuct,(110,170))   
           

        elif state=="again":
#High score and score
 
           
            score=int(score)
            high=open("high.txt")
            lis=""
            for r in high:
                lis=lis+r
            high.close()
            slis=lis.split("\n")

                    
            for y in slis:
                y=int(y)
                if y<score:
                   
                    slis[0]=str(score)
                   

            hs=slis[0]
            high2=open("high.txt","w").close()
            high2=open("high.txt","a")
            high2.write(hs)
            high2.close()
           
        
            hic =tfont.render(('Highest Score: '+hs),True,(0,0,0))
            screen.blit(hic,(140,10))

            score=str(score)
            sc =tfont.render(('Your Score: '+score),True,(0,0,0))
            screen.blit(sc,(140,30))
#Bliting the Retry and Main Menu
            re=screen.blit(retry,(140,100))
            me=screen.blit(menu,(140,250))
            
        elif state=="game":
#The y coordinate of each pipe
            if ran=="1":
                n=320
            elif ran=="2":
                n=260
            elif ran=="3":
                n=240
            elif ran=="4":
                n=200
            else:
                n=280
                
            if ran2=="1":
                n2=320
            elif ran2=="2":
                n2=260
            elif ran2=="3":
                n2=240
            elif ran2=="4":
                n2=200
            else:
                n2=280
            
            screen.blit(up,(p,0))
            screen.blit(down,(p,n))
            
            screen.blit(up2,(p2,0))
            screen.blit(down2,(p2,n2))

#Score counter
            if p==67:
                score=score+1
            if p2==71:
                score=score+1
            
#Generating the pipes
            if p<=-75:
                ran=random.randint(1,5)
                ran=str(ran)
                up=pygame.image.load ("up"+ran+".png").convert()
                down=pygame.image.load ("down"+ran+".png").convert()
                p=400
            if p2<=-75:
                ran2=random.randint(1,5)
                ran2=str(ran2)
                up2=pygame.image.load ("up"+ran2+".png").convert()
                down2=pygame.image.load ("down"+ran2+".png").convert()
                p2=401

            p=p-3
            p2=p2-3
            
            

#Controling the bird            
            if direction=="up":
                y=y-9
            else:
                y=y+3
#Bliting the bird             
            screen.blit(bird,(150,y))

#Checking if the bird hits the pipes
            if 75<p<200:

                if y<=n-140 or y>=n-50:
                    state="again"
            if 75<p2<200:

                if y<=n2-140 or y>=n2-50:
                    state="again"
            if y==350:
                state="again"
#Instruction Screen
        elif state=="instructions":
            screen.blit(instruct,(20,70))
            screen.blit(instruct2,(20,90))
            screen.blit(instruct3,(20,110))
            screen.blit(instruct4,(20,130))
            screen.blit(instruct5,(20,150))
            screen.blit(instruct6,(20,170))
            ba=screen.blit(back,(20,250))

        else:
            screen.blit(error,(20,60))

        pygame.display.flip()


# key and mouse events
        for ev in pygame.event.get(): 
            
            if ev.type == pygame.QUIT: 
                keepGoing = False
            elif ev.type == KEYDOWN:
                if ev.key == K_w:
                    direction="up"
           
            elif ev.type == KEYUP:
                direction="down"  
            elif ev.type == MOUSEBUTTONDOWN:
#Checking collision in "instruction" screen
                if state=="instructions":
                    pos3=pygame.mouse.get_pos()
                    if ba.collidepoint(pos3):
                        state="menu"
#Checking collsion in "again" screen                  
                if state=="again":
                    pos2=pygame.mouse.get_pos()
                    if re.collidepoint(pos2):
                        state="game"
                        p=400
                        p2=p+250
                        y=200
                        y2=200
                        score=0
                    elif me.collidepoint(pos2):
                        p=400
                        p2=p+250
                        y=200
                        y2=200
                        score=0
                        state="menu"
#Checking collision in the "menu" screen
                if state!="game" and state !="instructions" and state !="again":
                    pos=pygame.mouse.get_pos()
                    if bn.collidepoint(pos):
                        state="game"
                    elif bi.collidepoint(pos):
                        state="instructions"
                   


finally:
    pygame.quit()
