from tkinter import *
import tkinter.font
import math
import random
import numpy as np


WIDTH = 1065
HEIGHT = 615
INIT_X = 50
INIT_Y = 200
INIT_X_DOUBLE_1 = 50
INIT_Y_DOUBLE_1= 100
INIT_X_DOUBLE_2 = 50
INIT_Y_DOUBLE_2= 415
GRAVITY = 1
JUMP_ACCEL = 15
GROUND_WIDTH_MIN_MODE1 = 100
GROUND_WIDTH_MAX_MODE1 = 200
GROUND_HEIGHT_MIN_MODE1 = 10
GROUND_HEIGHT_MAX_MODE1 = 200
GROUND_MERGIN_MIN_MODE1= 10
GROUND_MERGIN_MAX_MODE1 = 40
GROUND_WIDTH_MIN_MODE2 = 50
GROUND_WIDTH_MAX_MODE2 = 90
GROUND_HEIGHT_MIN_MODE2 = 10
GROUND_HEIGHT_MAX_MODE2 = 200
GROUND_MERGIN_MIN_MODE2= 30
GROUND_MERGIN_MAX_MODE2 = 50
GROUND_WIDTH_MIN_MODE3 = 50
GROUND_WIDTH_MAX_MODE3 = 80
GROUND_HEIGHT_MIN_MODE3 = 10
GROUND_HEIGHT_MAX_MODE3 = 200
GROUND_MERGIN_MIN_MODE3= 40
GROUND_MERGIN_MAX_MODE3 = 50
SCROLL_SPEED = 10
MAX_JUMP_COUNT = 2
CHOICE_HEIGHT = 60


class BicycleMan:
    def __init__(self):
        self.manAngle = 0
        self.scrollX = 0
        self.groundList = []
        self.groundList2 = []
        self.manCX = INIT_X
        self.manCY = INIT_Y
        
        self.manWidth =  WIDTH/100 * math.cos(math.pi*1.83+self.manAngle) + WIDTH/200  -(WIDTH/100 * math.cos(math.pi*1.16+self.manAngle) + WIDTH/200)
        self.manHeight =  - WIDTH/100 * math.sin(math.pi*1.83+self.manAngle) + WIDTH/200 -(- WIDTH/75 *  math.sin(math.pi/3+self.manAngle) + WIDTH/200)
        self.gameState = "START_SCREEN"
        self.isUpperGameOver = False
        self.isLowerGameOver = False
        self.enableGravity = False
        self.enableGravity2 = False

        self.gStart = self.manCX - 50
        self.gStart2 = self.manCX - 100
        self.gStart3 = self.manCX - 100

        self.speedY = 0
        self.speedY2 = 0

        self.isNewHighScore = False

        self.meterCount = 0
        self.meterCount2 = 0
        self.bestMeter = 0

        # back ground
        self.sunCX = WIDTH/2
        self.sunCY = HEIGHT/2
        self.sunR = WIDTH/10
        self.lightStart = 30
        self.lightR = self.sunR * 10
        self.fujiUB = WIDTH/10
        self.fujiLB = WIDTH/5
        self.moveCloud1 = 0.25
        self.moveCloud2 = 0.35
        self.moveCloud3 = 0.4
        self.c1Return = False
        self.c2Return = False
        self.c3Return = False
        self.c1x = WIDTH * 1/5
        self.c2x = WIDTH * 1/2
        self.c3x = WIDTH * 3/4
        self.cherryList = []
        self.time = 0
        self.jumpCount = 0
        self.jumpCount2 = 0

        #Settings
        self.isLevelOptionOpen = False
        self.isLevelSelected =  True
        self.isModeOptionOpen = False
        self.isModeSelected = True
        self.isHelpWindowOpen = False

        self.level = 1 #[1, 2, 3]
        self.playMode = "Single Play"
        if self.playMode == "Double Play":
            self.manCX = INIT_X_DOUBLE_1
            self.manCY = INIT_Y_DOUBLE_1
        self.manCX2 = INIT_X_DOUBLE_2
        self.manCY2 = INIT_Y_DOUBLE_2
        self.startCount = 4

    
        pass

    def prepare(self):
        self.manAngle = 0
        self.scrollX = 0
        self.groundList = []
        self.groundList2 = []
        self.manCX = INIT_X
        self.manCY = INIT_Y
        self.manWidth =  WIDTH/100 * math.cos(math.pi*1.83+self.manAngle) + WIDTH/200  -(WIDTH/100 * math.cos(math.pi*1.16+self.manAngle) + WIDTH/200)
        self.manHeight = - WIDTH/100 * math.sin(math.pi*1.83+self.manAngle) + WIDTH/200 -(- WIDTH/75 *  math.sin(math.pi/3+self.manAngle) + WIDTH/200)
        self.gameState = "READY"
        self.isUpperGameOver = False
        self.isLowerGameOver = False

        self.enableGravity = False
        self.enableGravity2 = False

        self.gStart = self.manCX - 50
        self.gStart2 = self.manCX - 50
        self.meterCount = 0
        self.meterCount2 = 0

        self.speedY = 0
        self.speedY2 = 0

        self.jumpCount = 0
        self.jumpCount2 = 0

        if self.playMode == "Double Play":
            self.manCX = INIT_X_DOUBLE_1
            self.manCY = INIT_Y_DOUBLE_1
        self.manCX2 = INIT_X_DOUBLE_2
        self.manCY2 = INIT_Y_DOUBLE_2



    def mousePressed(self, event ,canvas):
        #start screen
        if self.gameState == "START_SCREEN":
            if self.isHelpWindowOpen == False:
                #if user clicks "Press to start" button
                if(event.x >= WIDTH/2-150 and event.x <= WIDTH/2+150) and (event.y >= HEIGHT/2+150 and event.y <= HEIGHT/2+200):
                    self.prepare()
                    self.gameState = "READY"
                    self.enableGravity = True
                #if user clicks "Setting" button
                elif(event.x >= WIDTH*6/7-75 and event.x <= WIDTH*6/7+75) and (event.y >= HEIGHT/7-15 and event.y <= HEIGHT/7+15):
                    self.gameState = "SETTING"
                #if user clicks "Help" button
                elif(event.x >= WIDTH/7-40 and event.x <= WIDTH/7+43) and (event.y >= HEIGHT/7-15 and event.y <= HEIGHT/7+15):
                    # canvas.create_rectangle(WIDTH/7-24, HEIGHT/7-8, WIDTH/7+24, HEIGHT/7+8,fill ="blue",activefill="#c06762", width = 0)
                    self.isHelpWindowOpen = True
            #help window
            else:
                #if user clicks close button 
                if(event.x >= WIDTH/2-285 and event.x <= WIDTH/2-265) and (event.y >= HEIGHT/7+20 and event.y <= HEIGHT/7+40):
                    self.isHelpWindowOpen = False   

        #setting screen
        if self.gameState == "SETTING":
            if self.isLevelSelected:
                #if user clicks level button 
                if(event.x >= WIDTH/4+150 and event.x <= WIDTH/4+450) and (event.y >= HEIGHT/3-20 and event.y <= HEIGHT/3+20):
                    self.isLevelOptionOpen = True
                    self.isLevelSelected = False

            else:
            #if user clicks "level1" button 
                if(event.x >= WIDTH/4+150 and event.x <= WIDTH/4+450) and (event.y >= HEIGHT/3-20 and event.y <= HEIGHT/3+20):
                    self.level = 1
                    self.isLevelSelected = True

                #if user clicks "level2" button 
                elif(event.x >= WIDTH/4+150 and event.x <= WIDTH/4+450) and (event.y >= HEIGHT/3+20 and event.y <= HEIGHT/3+60):
                    self.level = 2
                    self.isLevelSelected = True

                #if user clicks "level3" button
                elif(event.x >= WIDTH/4+150 and event.x <= WIDTH/4+450) and (event.y >= HEIGHT/3+60 and event.y <= HEIGHT/3+100):
                    self.level = 3
                    self.isLevelSelected = True

            #if user clicks mode button 
            if self.isModeSelected :
                if(event.x >= WIDTH/4+150 and event.x <= WIDTH/4+450) and (event.y >= HEIGHT*2/3-20 and event.y <= HEIGHT*2/3+20):
                    self.isModeOptionOpen = True
                    self.isModeSelected = False
   
            else:
                #if user clicks "Single play" button 
                if(event.x >= WIDTH/4+150 and event.x <= WIDTH/4+450) and (event.y >= HEIGHT*2/3-20 and event.y <= HEIGHT*2/3+20):
                    self.playMode = "Single Play"
                    self.isModeSelected = True
                
                #if user clicks "Double play" button
                elif(event.x >= WIDTH/4+150 and event.x <= WIDTH/4+450) and (event.y >= HEIGHT*2/3+20 and event.y <= HEIGHT*2/3+60):
                    self.playMode = "Double Play"
                    self.isModeSelected = True

            #if user clicks "HOME" button
            if(event.x >= WIDTH/2-73 and event.x <= WIDTH/2+72) and (event.y >= HEIGHT*9/10-18 and event.y <= HEIGHT*9/10+18):
                self.gameState = "START_SCREEN"

        #Game over screen
        if self.gameState == "GameOver":
            #if user clicks "Start again" button
            if (event.x >= WIDTH/2-150 and event.x <= WIDTH/2+150) and (event.y >= HEIGHT*3.5/5-30 and event.y <= HEIGHT*3.5/5+30):
                self.prepare()
                self.gameState = "READY"
                self.enableGravity = True
            #if user clicks "Home" button              
            if (event.x >= WIDTH/6-43 and event.x <= WIDTH/6+40) and (event.y >= HEIGHT/6-15 and event.y <= HEIGHT/6+13):
                self.gameState = "START_SCREEN"
            pass


    def keyPressed(self, event):
        if (event.keysym == "y"):
            self.manAngle += math.pi/18

        if (event.keysym == "s") and self.gameState == "READY":
            self.gameState = "PLAYING"

        if self.playMode == "Single Play":
            if (self.enableGravity == False  or self.jumpCount > 0) and (event.keysym == "Up"):
                self.jump()
        elif self.playMode == "Double Play":
            if (self.enableGravity == False  or self.jumpCount > 0) and (event.keysym == "e"):
                self.jump()
            if (self.enableGravity2 == False  or self.jumpCount2 > 0) and (event.keysym == "Up"):
                self.jump2()

        pass


    def timerFired(self, canvas):
        if self.playMode == "Single Play":
            if self.enableGravity:
                self.speedY += GRAVITY
            else:
                self.jumpCount = MAX_JUMP_COUNT

            self.manCY += self.speedY
            
            if self.gameState == "PLAYING":
                self.meterCount += 1
                self.manCX += SCROLL_SPEED

            self.lightStart += 0.25


        elif self.playMode == "Double Play":
            if self.enableGravity:
                self.speedY += GRAVITY
            else:
                self.jumpCount = MAX_JUMP_COUNT

            if self.enableGravity2:
                self.speedY2 += GRAVITY   
            else:
                self.jumpCount2 = MAX_JUMP_COUNT

            self.manCY += self.speedY
            self.manCY2 += self.speedY2

            if self.gameState == "PLAYING":
                self.manCX += SCROLL_SPEED
                self.manCX2 += SCROLL_SPEED
            
            if self.gameState == "PLAYING" and self.isUpperGameOver == False:
                self.meterCount += 1
            if self.gameState == "PLAYING" and self.isLowerGameOver == False:
                self.meterCount2 += 1

        if self.gameState == "PLAYING":
            self.scrollX += SCROLL_SPEED

        self.time += self.timerDelay
        if not self.c1Return:
            self.c1x += self.moveCloud1
        if self.c1Return:
            self.c1x -= self.moveCloud1

        if not self.c2Return:
            self.c2x += self.moveCloud2
        if self.c2Return:
            self.c2x -= self.moveCloud2

        if not self.c3Return:
            self.c3x -= self.moveCloud3
        if self.c3Return:
            self.c3x += self.moveCloud3

        if self.manCX - self.scrollX < 50:
                self.manCX += 1

        if self.manCX2 - self.scrollX < 50:
                self.manCX2 += 1

        if self.manCX2 - self.scrollX > 50:
                self.manCX2 -= 1

    def redrawAll(self, canvas):
        self.drawBackground(canvas)
        self.drawLight(canvas)
        self.drawBackgroundMountain(canvas)
        self.drawSun(canvas)
        self.drawFuji(canvas)
        self.drawCloud(canvas)
        self.drawBamboo(canvas)
        self.drawGround(canvas)
        self.isGameOver()
        self.drawGameOver(canvas)
        self.drawMeterCount(canvas)
        self.createGround()
        self.drawStartScreen(canvas)
        self.drawSettingScreen(canvas)
        self.drawHelpWindow(canvas)
        self.drawSeparator(canvas)
        self.startTriger()
        self.collision()
        self.collision2()
        self.drawMan(canvas)
        # print(self.enableGravity)
        # print(self.jumpCount)
        # print(self.enableGravity)
        print(self.gameState)


    def startTriger(self):
        if self.gameState == "READY" and self.enableGravity == False:
            self.gameState = "PLAYING"

        
    def man(self, canvas, cx, cy):

        headCX = cx + WIDTH/75 * math.cos(math.pi/3+self.manAngle)
        headCY = cy - WIDTH/75 * math.sin(math.pi/3+self.manAngle)
        headR = WIDTH/200
        canvas.create_oval(headCX - headR, headCY - headR, headCX + headR, headCY + headR, fill = "black",outline="black", width=WIDTH/1000)

        fwheelCX = cx + WIDTH/100 * math.cos(math.pi*1.83+self.manAngle)
        fwheelCY = cy - WIDTH/100 * math.sin(math.pi*1.83+self.manAngle)
        fwheelR = WIDTH/200
        canvas.create_oval(fwheelCX - fwheelR, fwheelCY - fwheelR, fwheelCX + fwheelR, fwheelCY + fwheelR, fill = "white", outline="black", width=WIDTH/1000)

        bwheelCX = cx + WIDTH/100 * math.cos(math.pi*1.16+self.manAngle)
        bwheelCY = cy - WIDTH/100 * math.sin(math.pi*1.16+self.manAngle)
        bwheelR = WIDTH/200
        canvas.create_oval(bwheelCX - bwheelR, bwheelCY - bwheelR, bwheelCX + bwheelR, bwheelCY + bwheelR, fill = "white", outline="black", width=WIDTH/1000)

        bodyX1 = cx + WIDTH/150 * math.cos(math.pi+self.manAngle)
        bodyX2 = headCX
        bodyY1 = cy
        bodyY2 = headCY
        canvas.create_line(bodyX1, bodyY1, bodyX2, bodyY2, fill="black", width=WIDTH/300)

        bbodyX1 = cx + WIDTH/100 * math.cos(math.pi*1.1+self.manAngle)
        bbodyX2 = cx + WIDTH/100 * math.cos(math.pi/18+self.manAngle)
        bbodyY1 = cy - WIDTH/100 * math.sin(math.pi*1.1+self.manAngle)
        bbodyY2 = cy - WIDTH/100 * math.sin(math.pi/18+self.manAngle)
        canvas.create_line(bbodyX1, bbodyY1, bbodyX2, bbodyY2, fill="red", width=WIDTH/300)


        legX1 = bodyX1
        legX2 = cx
        legY1 = bodyY1
        legY2 = cy - WIDTH/75 * math.sin(math.pi*1.8 + self.manAngle)
        canvas.create_line(legX1, legY1, legX2, legY2, fill="black", width=WIDTH/300)

        armX1 = cx + WIDTH/150 * math.cos(math.pi/3+self.manAngle)
        armX2 = cx + WIDTH/100 * math.cos(math.pi*1.94+self.manAngle)
        armY1 = cy - WIDTH/150 * math.sin(math.pi/3+self.manAngle)
        armY2 = cy - WIDTH/100 * math.sin(math.pi*1.94+self.manAngle)
        canvas.create_line(armX1, armY1, armX2, armY2, fill="black", width=WIDTH/300)



    def drawMan(self, canvas):
        if self.gameState == "READY" or self.gameState == "PLAYING":
                if self.playMode == "Single Play":
                    self.man(canvas, self.manCX-self.scrollX, self.manCY)
                elif self.playMode == "Double Play":
                    if not self.isUpperGameOver:
                        self.man(canvas, self.manCX-self.scrollX, self.manCY)
                    if not self.isLowerGameOver:
                        self.man(canvas, self.manCX2-self.scrollX, self.manCY2)
        elif self.gameState == "START_SCREEN":
            self.man(canvas, self.sunCX, self.sunCY-self.sunR-10)


    def jump(self):
        self.jumpCount -= 1
        self.speedY = -JUMP_ACCEL
       

    def jump2(self):
        self.jumpCount2 -=1
        self.speedY2 = -JUMP_ACCEL
        

    def drawStartScreen(self,canvas):
        if self.gameState == "START_SCREEN":
            titleFont = tkinter.font.Font(family = "Optima Extrablack", size = 150)
            headingFont = tkinter.font.Font(family = "Optima Bold", size = 37)
            buttonFont = tkinter.font.Font(family = "Optima Bold", size = 30)
            canvas.create_text(WIDTH/2, HEIGHT/2-30, text="BIKE MAN", font=titleFont, fill="black")
            canvas.create_rectangle(WIDTH/2-150, HEIGHT/2+150, WIDTH/2+150, HEIGHT/2+200,fill ="#273622",activefill="#32462c", width = 0)
            canvas.create_text(WIDTH/2,HEIGHT/2+175, text="PRESS TO START",fill = "white", font=buttonFont)
            # canvas.create_rectangle(WIDTH/7-40, HEIGHT/7-15, WIDTH/7+43, HEIGHT/7+15,fill ="blue",activefill="#c06762", width = 0)
            canvas.create_text(WIDTH/7,HEIGHT/7, text="HELP",fill = "#e03753", font=headingFont,activefill="#e86a7f")
            # canvas.create_rectangle(WIDTH*6/7-75, HEIGHT/7-15, WIDTH*6/7+75, HEIGHT/7+15,fill ="blue",activefill="#c06762", width = 0)
            canvas.create_text(WIDTH*6/7,HEIGHT/7, text="SETTING",fill = "#e03753", font=headingFont,activefill="#e86a7f")

    def drawSettingScreen(self, canvas):
        if self.gameState == "SETTING":
            headingFont = tkinter.font.Font(family = "Optima Extrablack", size = 45)
            paragraphFont = tkinter.font.Font(family = "Optima Bold", size = 30)
            optionFont = tkinter.font.Font(family = "Optima Bold", size = 30)
            canvas.create_rectangle(0,0,WIDTH, HEIGHT, fill="#B8B694")
            canvas.create_text(WIDTH/2, HEIGHT/10, text="Settings", font=headingFont)
            canvas.create_rectangle(WIDTH/4+120, HEIGHT/3-20, WIDTH/4+150, HEIGHT/3+20, fill ="#e7d541", width = 0)
            canvas.create_text(WIDTH/4, HEIGHT/3, text="Choose level : ", font=paragraphFont)
            canvas.create_polygon(WIDTH/4+125, HEIGHT/3-8, WIDTH/4+145, HEIGHT/3-8, WIDTH/4+135, HEIGHT/3+8, fill="white")
            canvas.create_rectangle(WIDTH/4+120, HEIGHT*2/3-20, WIDTH/4+150, HEIGHT*2/3+20, fill ="#527248", width = 0)
            canvas.create_text(WIDTH/4, HEIGHT*2/3, text="Choose mode : ", font=paragraphFont)
            canvas.create_polygon(WIDTH/4+125, HEIGHT*2/3-8, WIDTH/4+145, HEIGHT*2/3-8, WIDTH/4+135, HEIGHT*2/3+8, fill="white")
            # canvas.create_rectangle(WIDTH/2-73, HEIGHT*9/10-18,  WIDTH/2+72, HEIGHT*9/10+18, fill = "blue")
            
            canvas.create_text(WIDTH/2, HEIGHT*9/10, text="HOME",fill ="#273622",activefill="#32462c", font =headingFont)
            

            if self.isLevelOptionOpen:
                canvas.create_rectangle(WIDTH/4+150, HEIGHT/3-20, WIDTH/4+450, HEIGHT/3+20, fill ="#f0e486", width=0, activefill ="#f6f0ba")
                canvas.create_text(WIDTH/4+300, HEIGHT/3, text ="level1",font=optionFont)
                canvas.create_rectangle(WIDTH/4+150, HEIGHT/3+20, WIDTH/4+450, HEIGHT/3+60, fill ="#e9d952", width=0, activefill ="#f6f0ba")
                canvas.create_text(WIDTH/4+300, HEIGHT/3+40, text ="level2",font=optionFont)
                canvas.create_rectangle(WIDTH/4+150, HEIGHT/3+60, WIDTH/4+450, HEIGHT/3+100, fill ="#e2ce1e", width=0, activefill ="#f6f0ba")
                canvas.create_text(WIDTH/4+300, HEIGHT/3+80, text ="level3",font=optionFont)

            if self.isLevelSelected:
                self.isLevelOptionOpen = False
                canvas.create_rectangle(WIDTH/4+150, HEIGHT/3-20, WIDTH/4+450, HEIGHT/3+20, fill ="#f0e486", width=0, activefill ="#f6f0ba")
                canvas.create_text(WIDTH/4+300, HEIGHT/3, text ="level%d" % (self.level),font=optionFont)

            if self.isModeOptionOpen:
                canvas.create_rectangle(WIDTH/4+150, HEIGHT*2/3-20, WIDTH/4+450, HEIGHT*2/3+20, fill ="#b8ceb1", width=0, activefill ="#d9e5d5")
                canvas.create_text(WIDTH/4+300, HEIGHT*2/3, text ="Single Play",font=optionFont)
                canvas.create_rectangle(WIDTH/4+150, HEIGHT*2/3+20, WIDTH/4+450, HEIGHT*2/3+60, fill ="#8cb081", width=0, activefill ="#d9e5d5")
                canvas.create_text(WIDTH/4+300, HEIGHT*2/3+40, text ="Double Play",font=optionFont)


            if self.isModeSelected:
                self.isModeOptionOpen = False
                canvas.create_rectangle(WIDTH/4+150, HEIGHT*2/3-20, WIDTH/4+450, HEIGHT*2/3+20, fill ="#b8ceb1", width=0, activefill ="#d9e5d5")
                canvas.create_text(WIDTH/4+300, HEIGHT*2/3, text ="%s" % (self.playMode),font=optionFont)

    

    def drawHelpWindow(self, canvas):
        if self.isHelpWindowOpen:
            headingFont = tkinter.font.Font(family = "Optima Extrablack", size = 30)
            paragraphFont = tkinter.font.Font(family = "Optima Extrablack", size = 25)
            sentenceFont = tkinter.font.Font(family = "Optima Bold", size = 25)
            self.round_rectangle(canvas, WIDTH/5, HEIGHT/7, WIDTH*4/5, HEIGHT*6/7, radius=25, fill="#c29297", outline="#a65f67", width=7)
            canvas.create_text(WIDTH/2, HEIGHT/7+25, text ="User Guide", font = headingFont)
            canvas.create_text(WIDTH/2-100, HEIGHT/7+75, text ="Single Play mode:", font = paragraphFont)
            canvas.create_text(WIDTH/2-85, HEIGHT/7+115, text ="Press “Up” key to jump", font = sentenceFont)
            canvas.create_text(WIDTH/2-100, HEIGHT/7+200, text ="Double Play mode:", font = paragraphFont)
            canvas.create_text(WIDTH/2+5, HEIGHT/7+240, text ="Player1(upper) - Press “Up” key to jump", font = sentenceFont)
            canvas.create_text(WIDTH/2-4, HEIGHT/7+280, text ="Player2(lower) - Press “E” key to jump", font = sentenceFont)
            self.drawCloseButton(canvas, WIDTH/2-275, HEIGHT/7+30, 10, "#e5d1d3","#f3eaeb","#aea5a8")

    def drawCloseButton(self, canvas, x, y, size, backColor, activeColor, xColor):
        canvas.create_rectangle(x-size, y-size, x+size, y+size, fill=backColor, activefill=activeColor, width=0)
        left_x1 =x-size+1
        left_x2 =x+size-1
        left_y1 = y-size+1
        left_y2 = y+size-1
        right_x1 = x+size-1
        right_x2 = x-size+1
        right_y1 = y-size+1
        right_y2 = y+size-1
        canvas.create_line(left_x1, left_y1, left_x2, left_y2, fill=xColor, width=4)
        canvas.create_line(right_x1, right_y1, right_x2, right_y2, fill=xColor, width=4)

        
    # def drawStart(self,canvas):
    #     paragraphFont = tkinter.font.Font(family = "Optima Bold", size = 30)
    #     if self.playMode == "Single Play":
    #         print(self.gameState)
    #         if self.gameState == "READY":
    #             # canvas.create_text(WIDTH/2, HEIGHT/2-50, text="BIKE MAN", font="Times 56", fill="black")
    #             if self.startCount == 3:
    #                 canvas.create_text(WIDTH/2, HEIGHT/2, text="3", font=paragraphFont, fill="black")
    #             elif self.startCount == 2:
    #                 canvas.create_text(WIDTH/2, HEIGHT/2, text="2", font=paragraphFont, fill="black")
    #             elif self.startCount == 1:
    #                 canvas.create_text(WIDTH/2, HEIGHT/2, text="1", font=paragraphFont, fill="black")
    #             elif self.startCount == 0:
    #                 canvas.create_text(WIDTH/2, HEIGHT/2, text="GO!", font=paragraphFont, fill="black")

        # elif self.playMode == "Double Play":
        #     if self.gameState == "READY":
        #         # canvas.create_text(WIDTH/2, HEIGHT/2-50, text="BIKE MAN", font="Times 56", fill="black")
        #         canvas.create_text(WIDTH/2, HEIGHT/2+10, text="press s to start", font="Times 35", fill="black")
        #     pass

    def startCounter(self, canvas):
        if self.startCount <= -2:
            return 
        else:
            if self.gameState == "READY":
                self.startCount -= 1
                print(self.startCount)
                canvas.after(1000, self.startCounter(canvas))
            

    def drawMeterCount(self, canvas):
        if self.playMode == "Single Play":
              if self.gameState == "PLAYING":
                    canvas.create_text(WIDTH * 1/10, HEIGHT * 1/10, text = "%dm" % (self.meterCount), fill = "black", font="Times 20")
        elif self.playMode == "Double Play":
            if self.gameState == "PLAYING" and self.isUpperGameOver == False:
                canvas.create_text(WIDTH * 1/10, HEIGHT * 1/10, text = "%dm" % (self.meterCount), fill = "black", font="Times 20")
            if self.gameState == "PLAYING" and self.isLowerGameOver == False:
                canvas.create_text(WIDTH * 1/10, HEIGHT * 6/10, text = "%dm" % (self.meterCount2), fill = "black", font="Times 20")
            pass

    #CITATION algorithm from http://tokibito.hatenablog.com/entry/20121227/1356581559
    def collisionRectRect(self, rect, rect2):
        if rect[2] < rect2[0]:
            return ""
        if rect2[2] < rect[0]:
            return ""
        if rect[3] < rect2[1]:
            return ""
        if rect2[3] < rect[1]:
            return ""

        dy = rect2[3] - rect[1] #Upper
        dx1 = rect2[2] - rect[0] #Left
        dx2 = rect[2] - rect2[0] #Right

        if dy < dx1 and dy < dx2:
            return "Upper"
        elif dx1 < dy and dx1 < dx2:
            return "Left"
        else:
            return "Right"
    
    def collision(self):
            if self.gameState == "READY" or self.gameState == "PLAYING":
                self.enableGravity = True
                for rect in self.groundList:
                    ret = self.collisionRectRect(rect,
                     [self.manCX -self.manWidth/2, self.manCY - self.manHeight/2, 
                     self.manCX +self.manWidth/2, self.manCY + self.manHeight/2])

                    if ret == "Upper":
                        self.manCY = rect[1] - self.manHeight/2
                        if self.speedY > 0:
                            self.speedY = 0
                        self.enableGravity = False
                        return
                    elif ret == "Left":
                        self.manCX = rect[0] - self.manWidth/2
                        return
                    elif ret == "Right":
                        self.manCX = rect[2] - self.manWidth/2
                        return 

    def collision2(self):
        if self.gameState == "READY" or self.gameState == "PLAYING":
            if self.playMode == "Double Play":
                self.enableGravity2 = True
                for rect2 in self.groundList2:
                    ret2 = self.collisionRectRect(rect2,
                     [self.manCX2 -self.manWidth/2, self.manCY2 - self.manHeight/2, 
                     self.manCX2 +self.manWidth/2, self.manCY2 + self.manHeight/2])
                    if ret2 == "Upper":
                        self.manCY2 = rect2[1] - self.manHeight/2
                        if self.speedY2 > 0:
                            self.speedY2 = 0
                        self.enableGravity2 = False
                        return
                    elif ret2 == "Left":
                        self.manCX2 = rect2[0] - self.manWidth/2
                        return
                    elif ret2 == "Right":
                        self.manCX2 = rect2[2] - self.manWidth/2
                        return 
        

    def createGround(self):
        if self.playMode == "Single Play":
            if self.gameState == "READY" or self.gameState == "PLAYING":

                if self.level == 1:
                    while(self.gStart < self.scrollX + WIDTH):
                        gWidth = random.randint(GROUND_WIDTH_MIN_MODE1, GROUND_WIDTH_MAX_MODE1)
                        gHeight = random.randint(GROUND_HEIGHT_MIN_MODE1, GROUND_HEIGHT_MAX_MODE1)
                        colors = ["#273622"]
                        color = random.choice(colors)
                        self.groundList.append([self.gStart, HEIGHT-gHeight, self.gStart+gWidth, HEIGHT, color])
                        self.gStart += gWidth + random.randint(GROUND_MERGIN_MIN_MODE1, GROUND_MERGIN_MAX_MODE1)

                
                elif self.level == 2:
                    while(self.gStart2 < self.scrollX + WIDTH):
                        gWidth = random.randint(GROUND_WIDTH_MIN_MODE2, GROUND_WIDTH_MAX_MODE2)
                        gHeight = random.randint(GROUND_HEIGHT_MIN_MODE2, GROUND_HEIGHT_MAX_MODE2)
                        colors = ["#bf7a4a"]
                        color = random.choice(colors)
                        self.groundList.append([self.gStart2, HEIGHT-gHeight, self.gStart2+gWidth, HEIGHT, color])
                        self.gStart2 += gWidth + random.randint(GROUND_MERGIN_MIN_MODE2, GROUND_MERGIN_MAX_MODE2)

                elif self.level == 3:
                    while(self.gStart3 < self.scrollX + WIDTH):    
                        gWidth = random.randint(GROUND_WIDTH_MIN_MODE3, GROUND_WIDTH_MAX_MODE3)
                        gHeight = random.randint(GROUND_HEIGHT_MIN_MODE3, GROUND_HEIGHT_MAX_MODE3)
                        colors = ["#bf4a55"]
                        color = random.choice(colors)
                        self.groundList.append([self.gStart, HEIGHT-gHeight, self.gStart+gWidth, HEIGHT, color])
                        self.gStart += gWidth + random.randint(GROUND_MERGIN_MIN_MODE3, GROUND_MERGIN_MAX_MODE3)

                while self.groundList[0][2] < 0:
                    self.groundList.pop(0)

        elif self.playMode == "Double Play":
            if self.gameState == "READY" or self.gameState == "PLAYING":

                while(self.gStart < self.scrollX + WIDTH):
                    if self.level == 1:
                        gWidth = random.randint(GROUND_WIDTH_MIN_MODE1, GROUND_WIDTH_MAX_MODE1)
                        gHeight = random.randint(GROUND_HEIGHT_MIN_MODE1/2, GROUND_HEIGHT_MAX_MODE1/2)
                        colors = ["#273622"]
                        color = random.choice(colors)
                        self.groundList.append([self.gStart, HEIGHT/2-gHeight, self.gStart+gWidth, HEIGHT/2, color])
                        self.gStart += gWidth + random.randint(GROUND_MERGIN_MIN_MODE1, GROUND_MERGIN_MAX_MODE1)

                    elif self.level == 2:
                        self.gStart
                        gWidth = random.randint(GROUND_WIDTH_MIN_MODE2, GROUND_WIDTH_MAX_MODE2)
                        gHeight = random.randint(GROUND_HEIGHT_MIN_MODE2/2, GROUND_HEIGHT_MAX_MODE2/2)
                        colors = ["#bf7a4a"]
                        color = random.choice(colors)
                        self.groundList.append([self.gStart, HEIGHT/2-gHeight, self.gStart+gWidth, HEIGHT/2, color])
                        self.gStart += gWidth + random.randint(GROUND_MERGIN_MIN_MODE2, GROUND_MERGIN_MAX_MODE2)

                    elif self.level == 3:
                        self.gStart
                        gWidth = random.randint(GROUND_WIDTH_MIN_MODE3, GROUND_WIDTH_MAX_MODE3)
                        gHeight = random.randint(GROUND_HEIGHT_MIN_MODE3/2, GROUND_HEIGHT_MAX_MODE3/2)
                        colors = ["#bf4a55"]
                        color = random.choice(colors)
                        self.groundList.append([self.gStart, HEIGHT/2-gHeight, self.gStart+gWidth, HEIGHT/2, color])
                        self.gStart += gWidth + random.randint(GROUND_MERGIN_MIN_MODE3, GROUND_MERGIN_MAX_MODE3)

                while self.groundList[0][2] < 0:
                    self.groundList.pop(0)

                while(self.gStart2 < self.scrollX + WIDTH):
                    if self.level == 1:
                        gWidth = random.randint(GROUND_WIDTH_MIN_MODE1, GROUND_WIDTH_MAX_MODE1)
                        gHeight = random.randint(GROUND_HEIGHT_MIN_MODE1/2, GROUND_HEIGHT_MAX_MODE1/2)
                        colors = ["#273622"]
                        color = random.choice(colors)
                        self.groundList2.append([self.gStart2, HEIGHT-gHeight, self.gStart2+gWidth, HEIGHT, color])
                        self.gStart2 += gWidth + random.randint(GROUND_MERGIN_MIN_MODE1, GROUND_MERGIN_MAX_MODE1)

                    elif self.level == 2:
                        self.gStart2
                        gWidth = random.randint(GROUND_WIDTH_MIN_MODE2, GROUND_WIDTH_MAX_MODE2)
                        gHeight = random.randint(GROUND_HEIGHT_MIN_MODE2/2, GROUND_HEIGHT_MAX_MODE2/2)
                        colors = ["#bf7a4a"]
                        color = random.choice(colors)
                        self.groundList2.append([self.drawStartScreen, HEIGHT-gHeight, self.gStart2+gWidth, HEIGHT, color])
                        self.gStart2 += gWidth + random.randint(GROUND_MERGIN_MIN_MODE2, GROUND_MERGIN_MAX_MODE2)

                    elif self.level == 3:
                        self.gStart2
                        gWidth = random.randint(GROUND_WIDTH_MIN_MODE3, GROUND_WIDTH_MAX_MODE3)
                        gHeight = random.randint(GROUND_HEIGHT_MIN_MODE3/2, GROUND_HEIGHT_MAX_MODE3/2)
                        colors = ["#bf4a55"]
                        color = random.choice(colors)
                        self.groundList2.append([self.gStart2, HEIGHT-gHeight, self.gStart2+gWidth, HEIGHT, color])

                        self.gStart2 += gWidth + random.randint(GROUND_MERGIN_MIN_MODE3, GROUND_MERGIN_MAX_MODE3)

                while self.groundList2[0][2] < 0:
                    self.groundList2.pop(0)
            pass


    def drawGround(self, canvas):
        if self.playMode == "Single Play":
            if self.gameState == "READY" or self.gameState == "PLAYING":
                for coord in self.groundList:
                    canvas.create_rectangle(coord[0]-self.scrollX, coord[1], coord[2]-self.scrollX, coord[3], fill=coord[4], outline =coord[4])
        elif self.playMode == "Double Play":
            if self.gameState == "READY" or self.gameState == "PLAYING":
                for coord in self.groundList:
                    canvas.create_rectangle(coord[0]-self.scrollX, coord[1], coord[2]-self.scrollX, coord[3], fill=coord[4], outline =coord[4])
                for coord in self.groundList2:
                    canvas.create_rectangle(coord[0]-self.scrollX, coord[1], coord[2]-self.scrollX, coord[3], fill=coord[4], outline =coord[4])
            pass

 

    def isGameOver(self):
        if self.playMode == "Single Play":
            if self.gameState != "PLAYING":
                return 
            if self.manCY > HEIGHT or self.manCX - self.scrollX< 0:
                self.gameState = "GameOver"
                if self.bestMeter < self.meterCount:
                    self.bestMeter = self.meterCount
                    self.isNewHighScore = True
                else:
                    self.isNewHighScore = False

        elif self.playMode == "Double Play":
            if self.gameState != "PLAYING":
                return 
            if self.manCY > HEIGHT/2 or self.manCX - self.scrollX< 0:
                self.isUpperGameOver = True
                if self.bestMeter < self.meterCount:
                    self.bestMeter = self.meterCount
                    self.isNewHighScore = True
                else:
                    self.isNewHighScore = False

            if self.manCY2 > HEIGHT or self.manCX2 - self.scrollX<0:
                self.isLowerGameOver = True

                if self.bestMeter < self.meterCount:
                    self.bestMeter = self.meterCount
                    self.isNewHighScore = True
                else:
                    self.isNewHighScore = False

            if self.isUpperGameOver == True and self.isLowerGameOver == True:
                self.gameState = "GameOver"

            pass

    def drawGameOver(self, canvas):
        headingFont = tkinter.font.Font(family = "Optima Extrablack", size = 60)
        paragraphFont = tkinter.font.Font(family = "Optima Bold", size = 30)
        homeFont = tkinter.font.Font(family = "Optima Bold", size = 35)
        if self.playMode == "Single Play":
            if self.gameState == "GameOver":
                canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill = "#F22547", width = 0)
                canvas.create_text(WIDTH/2, HEIGHT/2-10, text="Game over...", fill = "white", font=headingFont)
                canvas.create_rectangle(WIDTH/2-150,HEIGHT*3.5/5-30, WIDTH/2+150,HEIGHT*3.5/5+30, fill ="#8c836a",outline ="white", activefill ="#a79f8a",width = 3)
                canvas.create_text(WIDTH/2, HEIGHT*3.5/5, text="press to start again", fill = "white", font=paragraphFont)
                canvas.create_text(WIDTH/6, HEIGHT/6, text="home",fill = "#c9c4b7", activefill ="white", font=homeFont)
                if self.isNewHighScore:
                    canvas.create_text(WIDTH/2, HEIGHT/2-120, text="NEW HIGH SCORE!", fill = "white", font=paragraphFont)
                else:
                    canvas.create_text(WIDTH/2, HEIGHT/2-120, text="score", fill = "white", font=paragraphFont)
                canvas.create_text(WIDTH/2, HEIGHT/2-80, text="%dm" % self.meterCount, fill = "white", font=paragraphFont)

        elif self.playMode == "Double Play":
            if self.isUpperGameOver == True and self.isLowerGameOver  == False:
                print()
                canvas.create_rectangle(0, 0, WIDTH, HEIGHT/2, fill = "#F22547", width = 0)
                canvas.create_text(WIDTH/2, HEIGHT/10, text="%dm" % self.meterCount, fill = "white", font="Times 30 italic")
                canvas.create_text(WIDTH/2, HEIGHT/5+20, text="Game over", fill = "white", font="Times 50 italic")
                # canvas.create_text(WIDTH/2, HEIGHT/2-20, text="press r to start again", fill = "white", font="Times 30 italic")
                
                # if self.isNewHighScore:
                #     canvas.create_text(WIDTH/2, HEIGHT/2-120, text="NEW HIGH SCORE!", fill = "white", font="Times 30 italic")
                # else:
                #     canvas.create_text(WIDTH/2, HEIGHT/2-120, text="score", fill = "white", font="Times 40 italic")
            if self.isLowerGameOver == True and self.isUpperGameOver == False:
                canvas.create_rectangle(0, HEIGHT/2, WIDTH, HEIGHT, fill = "#F22547", width = 0)
                canvas.create_text(WIDTH/2, HEIGHT/2+45, text="%dm" % self.meterCount2, fill = "white", font="Times 30 italic")
                canvas.create_text(WIDTH/2, HEIGHT*4/5-30, text="Game over", fill = "white", font="Times 50 italic")
                # canvas.create_text(WIDTH/2, HEIGHT*3/2+30, text="press r to start again", fill = "white", font="Times 30 italic")
                # if self.isNewHighScore:
                #     canvas.create_text(WIDTH/2, HEIGHT/2-120, text="NEW HIGH SCORE!", fill = "white", font="Times 30 italic")
                # else:
                #     canvas.create_text(WIDTH/2, HEIGHT/2-120, text="score", fill = "white", font="Times 40 italic")

            if self.isLowerGameOver and self.isUpperGameOver:
                canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill = "#F22547", width = 0)

            pass

    #CITATION: I got the tkinter drawing funtions from https://stackoverflow.com/questions/44099594/how-to-make-a-tkinter-canvas-rectangle-with-rounded-corners
    def round_rectangle(self, canvas, x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]
        return canvas.create_polygon(points, **kwargs, smooth=True)

    def drawSun(self,canvas):
        if self.playMode == "Single Play":
            canvas.create_oval(self.sunCX-self.sunR, self.sunCY-self.sunR,self.sunCX+self.sunR, self.sunCY+self.sunR, fill="#F22547",width=0)
        elif self.playMode == "Double Play":
            canvas.create_oval(self.sunCX-self.sunR/2, self.sunCY/2-self.sunR/2,self.sunCX+self.sunR/2, self.sunCY/2+self.sunR/2, fill="#F22547",width=0)
            canvas.create_oval(self.sunCX-self.sunR/2, self.sunCY*3/2-self.sunR/2,self.sunCX+self.sunR/2, self.sunCY*3/2+self.sunR/2, fill="#F22547",width=0)
            pass
    
    def drawBackground(self, canvas):
        canvas.create_rectangle(0, 0, WIDTH, HEIGHT,fill="#EDEACC", width=0)
    
    def drawFuji(self, canvas):
        if self.playMode == "Single Play":
            g1 = (self.sunCX-WIDTH/3, HEIGHT)
            g2 = (self.sunCX+WIDTH*2/10, HEIGHT)
            g3 = (self.sunCX-WIDTH/10, self.sunCY)
            g4 = (self.sunCX-WIDTH/7, self.sunCY)
            w1 = (g4[0]-abs(g1[0]-g4[0])*1/4*1.195, g4[1]+(g1[1]+g4[1])*1/10)
            w2 = (g3[0]+abs(g2[0]-g3[0])*1/2*0.75, g3[1]+abs(g2[1]+g3[1])*5/40)
            w3 = g3
            w4 = g4
            canvas.create_polygon(g1, g2, g3, g4, fill="#727176",width=0)
            canvas.create_polygon(w1, w2, w3, w4, fill="#FFFFFF",width=0)
        elif self.playMode == "Double Play":
            g1 = (self.sunCX-WIDTH/3, HEIGHT/2)
            g2 = (self.sunCX+WIDTH*2/10, HEIGHT/2)
            g3 = (self.sunCX-WIDTH/10, self.sunCY/2)
            g4 = (self.sunCX-WIDTH/7, self.sunCY/2)
            w1 = (g4[0]-abs(g1[0]-g4[0])*1/4*1.195, g4[1]+(g1[1]+g4[1])*1/10)
            w2 = (g3[0]+abs(g2[0]-g3[0])*1/2*0.75, g3[1]+abs(g2[1]+g3[1])*5/40)
            w3 = g3
            w4 = g4
            canvas.create_polygon(g1, g2, g3, g4, fill="#727176",width=0)
            canvas.create_polygon(w1, w2, w3, w4, fill="#FFFFFF",width=0)
            g1 = (self.sunCX-WIDTH/3, HEIGHT)
            g2 = (self.sunCX+WIDTH*2/10, HEIGHT)
            g3 = (self.sunCX-WIDTH/10, self.sunCY*3/2)
            g4 = (self.sunCX-WIDTH/7, self.sunCY*3/2)
            w1 = (g4[0]-abs(g1[0]-g4[0])*1/4*1.4, g4[1]+((g1[1]+g4[1])*1/10)*(1/2))
            w2 = (g3[0]+abs(g2[0]-g3[0])*1/2*0.9, g3[1]+(abs(g2[1]+g3[1])*5/40)*(1/2))
            w3 = g3
            w4 = g4
            canvas.create_polygon(g1, g2, g3, g4, fill="#727176",width=0)
            canvas.create_polygon(w1, w2, w3, w4, fill="#FFFFFF",width=0)
            pass

    
    def drawLight(self, canvas):
        if self.gameState == "READY" or self.gameState == "PLAYING":
            if self.playMode == "Single Play":
                cx = self.sunCX
                cy = self.sunCY
                r = self.lightR
                color = "#F0E68C"
                canvas.create_arc(cx-r, cy-r, cx+r, cy+r,start=self.lightStart, extent=15, style="pieslice",fill=color, outline="#EDEACC")
                canvas.create_arc(cx-r, cy-r, cx+r, cy+r,start=self.lightStart+60, extent=15, style="pieslice",fill=color, outline="#EDEACC")
                canvas.create_arc(cx-r, cy-r, cx+r, cy+r,start=self.lightStart+120, extent=15, style="pieslice",fill=color, outline="#EDEACC")
                canvas.create_arc(cx-r, cy-r, cx+r, cy+r,start=self.lightStart+180, extent=15, style="pieslice",fill=color, outline="#EDEACC")
                canvas.create_arc(cx-r, cy-r, cx+r, cy+r,start=self.lightStart+240, extent=15, style="pieslice",fill=color, outline="#EDEACC")
                canvas.create_arc(cx-r, cy-r, cx+r, cy+r,start=self.lightStart+300, extent=15, style="pieslice",fill=color, outline="#EDEACC")
                
        

    def cloud(self, canvas, x, y):
        self.round_rectangle(canvas, x-(WIDTH/25)*2, y-(HEIGHT/350)*5/3, x+(WIDTH/60)*5/3, y+(HEIGHT/50)*5/3, radius=25, fill="#FFFFFF", width = 0)
        self.round_rectangle(canvas, x-(WIDTH/60)*5/3, y-(HEIGHT/50)*5/3, x+(WIDTH/25)*2, y+(HEIGHT/350)*5/3, radius=25, fill="#FFFFFF", width = 0)

   

    def drawCloud(self, canvas):
        if self.playMode == "Single Play":
            self.cloud(canvas, self.c1x, HEIGHT * 2/5)
            self.cloud(canvas, self.c2x, HEIGHT * 1/7)
            self.cloud(canvas, self.c3x, HEIGHT * 4/7)
        elif self.playMode == "Double Play":
            self.cloud(canvas, self.c1x, HEIGHT * 2/5 + HEIGHT/2)
            self.cloud(canvas, self.c2x, HEIGHT * 1/7 + HEIGHT/2)
            self.cloud(canvas, self.c3x, HEIGHT * 2/7 + HEIGHT/2)
            self.cloud(canvas, self.c1x, HEIGHT * 2/5)
            self.cloud(canvas, self.c2x, HEIGHT * 1/7)
            self.cloud(canvas, self.c3x, HEIGHT * 2/7)
            pass

    def bamboo(self, canvas, cx, cy, r, angle, n):
        space = WIDTH/200
        color = "#5A5239"
        if self.playMode == "Single Play":
            bambooWidth = 75
        if self.playMode == "Double Play":
            bambooWidth = 100
        for i in range(n):
            if i == 0:
                p0 = (cx, cy) 
            bamX1 = cx + (i+1)* r * math.cos(angle)
            bamY1 = cy - (i+1)* r * math.sin(angle)
            p1 = (bamX1, bamY1)
            canvas.create_line(p0, p1, fill=color, width=WIDTH/bambooWidth)
            bamX1S = cx + ((i+1) * r+space) * math.cos(angle)
            bamY1S = cy - ((i+1) * r+space) * math.sin(angle)
            p1S = (bamX1S, bamY1S)
            p0 = p1S


    def drawBamboo(self, canvas):
        if self.playMode == "Single Play":
            if self.gameState == "READY" or self.gameState == "PLAYING":
                self.bamboo(canvas, WIDTH*38/40, HEIGHT, HEIGHT*(2/3)*(1/4) ,math.pi/2*7/6, 5)
                self.bamboo(canvas, WIDTH*34/40, HEIGHT, HEIGHT*(2/3)*(1/4) ,math.pi/2*11/10, 7)
        elif self.playMode == "Double Play":
            if self.gameState == "READY" or self.gameState == "PLAYING":
                self.bamboo(canvas, WIDTH*38/40, HEIGHT/2, (HEIGHT/2)*(2/3)*(1/4) ,math.pi/2*7/6, 5)
                self.bamboo(canvas, WIDTH*34/40, HEIGHT/2, (HEIGHT/2)*(2/3)*(1/4) ,math.pi/2*11/10, 7)
                self.bamboo(canvas, WIDTH*38/40, HEIGHT, (HEIGHT/2)*(2/3)*(1/4) ,math.pi/2*7/6, 5)
                self.bamboo(canvas, WIDTH*34/40, HEIGHT, (HEIGHT/2)*(2/3)*(1/4) ,math.pi/2*11/10, 6)

                
    def cherry(self, canvas, x, y):
        color = "#FCD3DC"
        r = WIDTH/30
        canvas.create_oval(x-r*4/10, y-r/6, x+r*4/10, y+r/6, fill = color, width=0)

    def createCherry(self):
        x = random.randint(1, WIDTH)
        self.cherryList.append([x, 0])


    def drawCherry(self, canvas):
        for coord in self.cherryList:
            self.cherry(canvas, coord[0], coord[1])


    def drawBackgroundMountain(self, canvas):
        if self.playMode == "Single Play":
            p1 = (-WIDTH*1/7, HEIGHT)
            p2 = (WIDTH*1/2, HEIGHT)
            p3 = (WIDTH*1/10, HEIGHT*8/10)
            p4 = (WIDTH*2/10, HEIGHT*8/10)
            canvas.create_polygon(p1, p2, p4, p3,fill="#B8B694", width=0)
            q1 = (WIDTH*4/10, HEIGHT)
            q2 = (WIDTH*11/10, HEIGHT)
            q3 = (WIDTH*6/10, HEIGHT*9/10)
            q4 = (WIDTH*8/10, HEIGHT*9/10)
            canvas.create_polygon(q1, q2, q4, q3,fill="#B8B694", width=0)

        elif self.playMode == "Double Play":
            p1 = (-WIDTH*1/7, HEIGHT/2)
            p2 = (WIDTH*1/2, HEIGHT/2)
            p3 = (WIDTH*1/10, HEIGHT*3/10)
            p4 = (WIDTH*2/10, HEIGHT*3/10)
            canvas.create_polygon(p1, p2, p4, p3,fill="#B8B694", width=0)
            q1 = (WIDTH*4/10, HEIGHT/2)
            q2 = (WIDTH*11/10, HEIGHT/2)
            q3 = (WIDTH*6/10, HEIGHT*4/10)
            q4 = (WIDTH*8/10, HEIGHT*4/10)
            canvas.create_polygon(q1, q2, q4, q3,fill="#B8B694", width=0)

            r1 = (-WIDTH*1/7, HEIGHT)
            r2 = (WIDTH*1/2, HEIGHT)
            r3 = (WIDTH*1/10, HEIGHT*8/10)
            r4 = (WIDTH*2/10, HEIGHT*8/10)
            canvas.create_polygon(r1, r2, r4, r3,fill="#B8B694", width=0)
            s1 = (WIDTH*4/10, HEIGHT)
            s2 = (WIDTH*11/10, HEIGHT)
            s3 = (WIDTH*6/10, HEIGHT*9/10)
            s4 = (WIDTH*8/10, HEIGHT*9/10)
            canvas.create_polygon(s1, s2, s4, s3,fill="#B8B694", width=0)

            pass

    def drawSeparator(self, canvas):
        if self.playMode == "Double Play" and not (self.isLowerGameOver == True and self.isUpperGameOver == True) and (self.gameState != "SETTING"):
            canvas.create_line(0, HEIGHT/2, WIDTH, HEIGHT/2, width = 3)


    # CITATION: I got the tkinter drawing funtions from https://www.cs.cmu.edu/~112/notes/notes-graphics.html
    def run(self):
        def redrawAllWrapper(self, canvas):
            canvas.delete(ALL)
            canvas.create_rectangle(0, 0, WIDTH, HEIGHT,
                                    fill='white', width=0)
            self.redrawAll(canvas)
            canvas.update()
    
        def mousePressedWrapper(self, event, canvas):
            self.mousePressed(event,canvas)
            redrawAllWrapper(self, canvas)
    
        def keyPressedWrapper(self, event, canvas):
            self.keyPressed(event)
            redrawAllWrapper(self, canvas)
    
        def timerFiredWrapper(self, canvas):
            self.timerFired(canvas)
            redrawAllWrapper(self, canvas)
            # pause, then call timerFired again
            canvas.after(self.timerDelay, timerFiredWrapper, self, canvas)
        # Set up data and call init
        class Struct(object): pass
        data = Struct()
        self.timerDelay = 10 # milliseconds
        #initiate visualizer
        bicycleman = BicycleMan()
        # create the root and the canvas
        root = Tk()
        canvas = Canvas(root, width=WIDTH, height=HEIGHT)
        canvas.pack()
        # set up events
        root.bind("<Button-1>", lambda event:
                                mousePressedWrapper(self, event, canvas))
        root.bind("<Key>", lambda event:
                                keyPressedWrapper(self, event, canvas))
        timerFiredWrapper(self, canvas)
        # and launch the app
        root.mainloop()  # blocks until window is closed
        print("bye!")
    
    def play(self):
        self.run()
        
    def main(self):
        self.play()

b = BicycleMan()
b.main()
