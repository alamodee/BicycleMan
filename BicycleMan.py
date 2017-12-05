from tkinter import *
import tkinter.font
import math
import random
import numpy as np


WIDTH = 710 
HEIGHT = 410
INIT_X = 50
INIT_Y = 200
GRAVITY = 0.6
JUMP_ACCEL = 12
GROUND_WIDTH_MIN_MODE1 = 50
GROUND_WIDTH_MAX_MODE1 = 100
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
SCROLL_SPEED = 3
MAX_JUMP_COUNT = 2
CHOICE_HEIGHT = 60


class BicycleMan:
    def __init__(self):
        self.manAngle = 0
        self.scrollX = 0
        self.groundList = []
        self.manCX = INIT_X
        self.manCY = INIT_Y
        self.manWidth =  WIDTH/100 * math.cos(math.pi*1.83+self.manAngle) + WIDTH/200  -(WIDTH/100 * math.cos(math.pi*1.16+self.manAngle) + WIDTH/200)
        self.manHeight = 20

        self.gameState = "START_SCREEN_1"
        self.enableGravity = True

        self.gStart = self.manCX - 50

        self.speedY = 0

        self.isNewHighScore = False

        self.meterCount = 0
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

        #Settings
        self.isLevelOptionOpen = False
        self.isLevelSelected =  True
        self.isModeOptionOpen = False
        self.isModeSelected = True

        self.level = 1 #[1, 2, 3]
        self.playMode = "Single play"

    
        pass

    def prepare(self):
        self.manAngle = 0
        self.scrollX = 0
        self.groundList = []
        self.manCX = INIT_X
        self.manCY = INIT_Y
        self.manWidth =  WIDTH/100 * math.cos(math.pi*1.83+self.manAngle) + WIDTH/200  -(WIDTH/100 * math.cos(math.pi*1.16+self.manAngle) + WIDTH/200)
        self.manHeight = 20

        self.gameState = "READY"
        self.enableGravity = True

        self.gStart = self.manCX - 50
        self.meterCount = 0
        self.speedY = 0


    def mousePressed(self, event):
        if self.gameState == "START_SCREEN_1":
            if(event.x >= WIDTH/2-100 and event.x <= WIDTH/2+100) and (event.y >= HEIGHT/2+100 and event.y <= HEIGHT/2+150):
                self.gameState = "START_SCREEN_2"
            elif(event.x >= WIDTH/7-50 and event.x <=  WIDTH/7+50) and (event.y >= HEIGHT/7-10 and event.y <= HEIGHT/7+10):
                self.gameState = "HELP"

        if self.gameState == "START_SCREEN_2":
            #if user clicks "Choose level" button 
            if(event.x >= WIDTH/3-150 and event.x <= WIDTH/3+150) and (event.y >= HEIGHT/4-20 and event.y <= HEIGHT/4+20):
                self.isLevelOptionOpen = True
                self.isLevelSelected = False

            #if user clicks "Choose mode" button 
            if(event.x >= WIDTH/3-150 and event.x <= WIDTH/3+150) and (event.y >= HEIGHT/2-20 and event.y <= HEIGHT/2+20):
                self.isModeOptionOpen = True
                self.isModeSelected = False

            if self.isLevelSelected == False:
            #if user clicks "level1" button 
                if(event.x >= WIDTH/3+150 and event.x <= WIDTH/3+450) and (event.y >= HEIGHT/4-20 and event.y <= HEIGHT/4+20):
                    self.level = 1
                    self.isLevelSelected = True

                #if user clicks "level2" button 
                elif(event.x >= WIDTH/3+150 and event.x <= WIDTH/3+450) and (event.y >= HEIGHT/4+20 and event.y <= HEIGHT/4+60):
                    self.level = 2
                    self.isLevelSelected = True

                #if user clicks "level3" button
                elif(event.x >= WIDTH/3+150 and event.x <= WIDTH/3+450) and (event.y >= HEIGHT/4+60 and event.y <= HEIGHT/4+100):
                    self.level = 3
                    self.isLevelSelected = True

             
            if self.isModeSelected == False:
                #if user clicks "Single play" button 
                if(event.x >= WIDTH/3+150 and event.x <= WIDTH/3+450) and (event.y >= HEIGHT/2-20 and event.y <= HEIGHT/2+20):
                    self.playMode = "Single Play"
                    self.isModeSelected = True
                
                #if user clicks "Double play" button
                elif(event.x >= WIDTH/3+150 and event.x <= WIDTH/3+450) and (event.y >= HEIGHT/2+20 and event.y <= HEIGHT/2+60):
                    self.playMode = "Double Play"
                    self.isModeSelected = True



        pass


    def keyPressed(self, event):
        if (event.keysym == "y"):
            self.manAngle += math.pi/18

        if (event.keysym == "s") and self.gameState == "READY":
            self.gameState = "PLAYING"

        if self.gameState == "READY" and event.keysym == "1":
            self.level = 1
            print(self.level)

        if self.gameState == "READY" and event.keysym == "2":
            self.level = 2
            print(self.level)

        if self.gameState == "READY" and event.keysym == "3":
            self.level = 3
            print(self.level)


        if (self.enableGravity == False  or self.jumpCount > 0) and (event.keysym == "Up"):
            self.jumpCount -= 1
            self.jump()

        if self.gameState == "GAMEOVER":
            if (event.keysym == "r"):
                self.prepare()
        pass


    def timerFired(self, canvas):
        self.time += self.timerDelay
        if self.gameState == "PLAYING":
            self.scrollX += SCROLL_SPEED

        if self.enableGravity:
            self.speedY += GRAVITY
        else:
            self.jumpCount = MAX_JUMP_COUNT

        self.manCY += self.speedY
        
        if self.gameState == "PLAYING":
            self.meterCount += 1
            self.manCX += SCROLL_SPEED


        self.lightStart += 0.25
  

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
        pass


    def redrawAll(self, canvas):
        self.collision()
        self.drawBackground(canvas)
        self.drawLight(canvas)
        self.drawBackgroundMountain(canvas)
        self.drawSun(canvas)
        self.drawFuji(canvas)
        self.drawCloud(canvas)
        self.drawBamboo(canvas)

        self.drawStart(canvas)
        self.drawGround(canvas)
        # self.deleteGround(canvas)
        self.drawMan(canvas)
        self.isGameOver()
        self.drawGameOver(canvas)
        self.drawMeterCount(canvas)
        self.createGround()
        self.drawStartScreen1(canvas)
        self.drawStartScreen2(canvas)

        pass


    def man(self, canvas, cx, cy):
        # r = WIDTH/1000
        # canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="blue")
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
            self.man(canvas, self.manCX-self.scrollX, self.manCY)
        if self.gameState == "START_SCREEN_1":
            self.man(canvas, self.sunCX, self.sunCY-self.sunR-7)

    def drawStartScreen1(self,canvas):
        if self.gameState == "START_SCREEN_1":
            titleFont = tkinter.font.Font(family = "Optima Extrablack", size = 120)
            buttonFont = tkinter.font.Font(family = "Optima", size = 15)
            canvas.create_text(WIDTH/2, HEIGHT/2-30, text="BIKE MAN", font=titleFont, fill="black")
            canvas.create_rectangle(WIDTH/2-100, HEIGHT/2+100, WIDTH/2+100, HEIGHT/2+150,fill ="#273622",activefill="#32462c", width = 0)
            canvas.create_text(WIDTH/2,HEIGHT/2+125, text="PLESS TO START",fill = "white", font=buttonFont)
            canvas.create_rectangle(WIDTH/7-50, HEIGHT/7-10, WIDTH/7+50, HEIGHT/7+10,fill ="#ba5954",activefill="#c06762", width = 0)
            canvas.create_text(WIDTH/7,HEIGHT/7, text="HELP",fill = "white", font=buttonFont)

    def drawStartScreen2(self, canvas):
        if self.gameState == "START_SCREEN_2":
            settingFont = tkinter.font.Font(family = "Optima Extrablack", size = 30)
            chooseLevelFont = tkinter.font.Font(family = "Optima Bold", size = 20)
            optionFont = tkinter.font.Font(family = "Optima Bold", size = 20)
            canvas.create_rectangle(0,0,WIDTH, HEIGHT, fill="#B8B694")
            canvas.create_text(WIDTH/2, HEIGHT/10, text="Settings", font=settingFont)
            canvas.create_rectangle(WIDTH/3-150, HEIGHT/4-20, WIDTH/3+150, HEIGHT/4+20, fill ="#e7d541", width = 0, activefill ="#ebdd64")
            canvas.create_text(WIDTH/3, HEIGHT/4, text="Choose level", font=chooseLevelFont)
            canvas.create_rectangle(WIDTH/3-150, HEIGHT/2-20, WIDTH/3+150, HEIGHT/2+20, fill ="#e7d541", width = 0, activefill ="#ebdd64")
            canvas.create_text(WIDTH/3, HEIGHT/2, text="Choose mode", font=chooseLevelFont)
            canvas.create_rectangle(WIDTH/3-150, HEIGHT*3/4-20, WIDTH/3+150, HEIGHT*3/4+20, fill ="#e7d541", width = 0, activefill ="#ebdd64")
            canvas.create_text(WIDTH/3, HEIGHT*3/4, text="Choose character", font=chooseLevelFont)

            if self.isLevelOptionOpen:
                canvas.create_rectangle(WIDTH/3+150, HEIGHT/4-20, WIDTH/3+450, HEIGHT/4+20, fill ="#f0e486", width=0, activefill ="#f6f0ba")
                canvas.create_text(WIDTH/3+300, HEIGHT/4, text ="level1",font=optionFont)
                canvas.create_rectangle(WIDTH/3+150, HEIGHT/4+20, WIDTH/3+450, HEIGHT/4+60, fill ="#e9d952", width=0, activefill ="#f6f0ba")
                canvas.create_text(WIDTH/3+300, HEIGHT/4+40, text ="level2",font=optionFont)
                canvas.create_rectangle(WIDTH/3+150, HEIGHT/4+60, WIDTH/3+450, HEIGHT/4+100, fill ="#e2ce1e", width=0, activefill ="#f6f0ba")
                canvas.create_text(WIDTH/3+300, HEIGHT/4+80, text ="level3",font=optionFont)

            if self.isLevelSelected:
                self.isLevelOptionOpen = False
                canvas.create_rectangle(WIDTH/3+150, HEIGHT/4-20, WIDTH/3+450, HEIGHT/4+20, fill ="#f0e486", width=0)
                canvas.create_text(WIDTH/3+300, HEIGHT/4, text ="level%d" % (self.level),font=optionFont)

            if self.isModeOptionOpen:
                canvas.create_rectangle(WIDTH/3+150, HEIGHT/2-20, WIDTH/3+450, HEIGHT/2+20, fill ="#f0e486", width=0, activefill ="#f6f0ba")
                canvas.create_text(WIDTH/3+300, HEIGHT/2, text ="Single Play",font=optionFont)
                canvas.create_rectangle(WIDTH/3+150, HEIGHT/2+20, WIDTH/3+450, HEIGHT/2+60, fill ="#e9d952", width=0, activefill ="#f6f0ba")
                canvas.create_text(WIDTH/3+300, HEIGHT/2+40, text ="Double Play",font=optionFont)


            if self.isModeSelected:
                self.isModeOptionOpen = False
                canvas.create_rectangle(WIDTH/3+150, HEIGHT/2-20, WIDTH/3+450, HEIGHT/2+20, fill ="#f0e486", width=0)
                canvas.create_text(WIDTH/3+300, HEIGHT/2, text ="%s" % (self.playMode),font=optionFont)



    def drawStart(self, canvas):
        if self.gameState == "READY":
            canvas.create_text(WIDTH/2, HEIGHT/2-50, text="BIKE MAN", font="Times 56", fill="black")
            canvas.create_text(WIDTH/2, HEIGHT/2, text="press s to start", font="Times 35", fill="black")

    def drawMeterCount(self, canvas):
        if self.gameState == "PLAYING":
            canvas.create_text(WIDTH * 1/10, HEIGHT * 1/10, text = "%dm" % (self.meterCount), fill = "black", font="Times 20")


    def distance(x1, y1, x2, y2):
        return ((x2-x1)**2 + (x2-x1)**2)**.5

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
        self.enableGravity = True
        for rect in self.groundList:
            # print("trying to check ", [line[0]-self.scrollX, line[1]], [line[2]-self.scrollX, line[3]])
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

    def createGround(self):
        if self.gameState == "READY" or self.gameState == "PLAYING":
        # cStartPoint = WIDTH+1
            #adding initial ground

            while(self.gStart < self.scrollX + WIDTH):
                
                if self.level == 1:
                    gWidth = random.randint(GROUND_WIDTH_MIN_MODE1, GROUND_WIDTH_MAX_MODE1)
                    gHeight = random.randint(GROUND_HEIGHT_MIN_MODE1, GROUND_HEIGHT_MAX_MODE1)
                    colors = ["#273622"]
                    # "#3A322B"
                    # "#2C523C"
                    # "#595E3C"
                    color = random.choice(colors)
                    self.groundList.append([self.gStart, HEIGHT-gHeight, self.gStart+gWidth, HEIGHT, color])
                    self.gStart += gWidth + random.randint(GROUND_MERGIN_MIN_MODE1, GROUND_MERGIN_MAX_MODE1)

                elif self.level == 2:
                    self.gStart
                    gWidth = random.randint(GROUND_WIDTH_MIN_MODE2, GROUND_WIDTH_MAX_MODE2)
                    gHeight = random.randint(GROUND_HEIGHT_MIN_MODE2, GROUND_HEIGHT_MAX_MODE2)
                    colors = ["#bf7a4a"]
                    # "#3A322B"
                    # "#2C523C"
                    # "#595E3C"
                    color = random.choice(colors)
                    self.groundList.append([self.gStart, HEIGHT-gHeight, self.gStart+gWidth, HEIGHT, color])
                    self.gStart += gWidth + random.randint(GROUND_MERGIN_MIN_MODE2, GROUND_MERGIN_MAX_MODE2)

                elif self.level == 3:
                    self.gStart
                    gWidth = random.randint(GROUND_WIDTH_MIN_MODE3, GROUND_WIDTH_MAX_MODE3)
                    gHeight = random.randint(GROUND_HEIGHT_MIN_MODE3, GROUND_HEIGHT_MAX_MODE3)
                    colors = ["#bf4a55"]
                    # "#3A322B"
                    # "#2C523C"
                    # "#595E3C"
                    color = random.choice(colors)
                    self.groundList.append([self.gStart, HEIGHT-gHeight, self.gStart+gWidth, HEIGHT, color])
                    self.gStart += gWidth + random.randint(GROUND_MERGIN_MIN_MODE3, GROUND_MERGIN_MAX_MODE3)

            while self.groundList[0][2] < 0:
                self.groundList.pop(0)


    def drawGround(self, canvas):
        if self.gameState == "READY" or self.gameState == "PLAYING":
            for coord in self.groundList:
                canvas.create_rectangle(coord[0]-self.scrollX, coord[1], coord[2]-self.scrollX, coord[3], fill=coord[4], outline =coord[4])

    def jump(self):
        self.speedY = -JUMP_ACCEL

    def isGameOver(self):
        if self.gameState != "PLAYING":
            return 
        if self.manCY > HEIGHT or self.manCX - self.scrollX< 0:
            self.gameState = "GAMEOVER"
            if self.bestMeter < self.meterCount:
                self.bestMeter = self.meterCount
                self.isNewHighScore = True
            else:
                self.isNewHighScore = False

    def drawGameOver(self, canvas):
        if self.gameState == "GAMEOVER":
            canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill = "#F22547", width = 0)
            canvas.create_text(WIDTH/2, HEIGHT/2-10, text="Game over", fill = "white", font="Times 50 italic")
            canvas.create_text(WIDTH/2, HEIGHT/2+30, text="press r to start again", fill = "white", font="Times 30 italic")
            if self.isNewHighScore:
                canvas.create_text(WIDTH/2, HEIGHT/2-120, text="NEW HIGH SCORE!", fill = "white", font="Times 30 italic")
            else:
                canvas.create_text(WIDTH/2, HEIGHT/2-120, text="score", fill = "white", font="Times 40 italic")
            canvas.create_text(WIDTH/2, HEIGHT/2-80, text="%dm" % self.meterCount, fill = "white", font="Times 30 italic")

    def drawSun(self,canvas):
        canvas.create_oval(self.sunCX-self.sunR, self.sunCY-self.sunR,self.sunCX+self.sunR, self.sunCY+self.sunR, fill="#F22547",width=0)
    
    def drawBackground(self, canvas):
            canvas.create_rectangle(0, 0, WIDTH, HEIGHT,fill="#EDEACC", width=0)
    
    def drawFuji(self, canvas):
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
    
    def drawLight(self, canvas):
        if self.gameState == "READY" or self.gameState == "PLAYING":
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
            pass
        

    def cloud(self, canvas, x, y):
        canvas.create_oval(x-WIDTH/25*5/3, y-HEIGHT/300*5/3, x+WIDTH/60*5/3, y+HEIGHT/50*5/3,fill="#FFFFFF", width = 0)
        canvas.create_oval(x-WIDTH/60*5/3, y-HEIGHT/50*5/3, x+WIDTH/25*5/3, y+HEIGHT/300*5/3,fill="#FFFFFF", width = 0)
        # canvas.create_oval(x-WIDTH/20, y-HEIGHT/20, x+WIDTH/10, y+HEIGHT/20,fill="#FFFFFF", width = 0)

    def drawCloud(self, canvas):
        self.cloud(canvas, self.c1x, HEIGHT * 2/5)
        self.cloud(canvas, self.c2x, HEIGHT * 1/7)
        self.cloud(canvas, self.c3x, HEIGHT * 4/7)

    def bamboo(self, canvas, cx, cy, r, angle, n):
        space = WIDTH/200
        color = "#5A5239"
        for i in range(n):
            if i == 0:
                p0 = (cx, cy) 
            bamX1 = cx + (i+1)* r * math.cos(angle)
            bamY1 = cy - (i+1)* r * math.sin(angle)
            p1 = (bamX1, bamY1)
            canvas.create_line(p0, p1, fill=color, width=WIDTH/75)
            bamX1S = cx + ((i+1) * r+space) * math.cos(angle)
            bamY1S = cy - ((i+1) * r+space) * math.sin(angle)
            p1S = (bamX1S, bamY1S)
            p0 = p1S


    def drawBamboo(self, canvas):
        if self.gameState == "READY" or self.gameState == "PLAYING":
            self.bamboo(canvas, WIDTH*38/40, HEIGHT, HEIGHT*(2/3)*(1/4) ,math.pi/2*7/6, 5)
            self.bamboo(canvas, WIDTH*34/40, HEIGHT, HEIGHT*(2/3)*(1/4) ,math.pi/2*11/10, 7)
            
    def putCloud(self, canvas):
        gif1 = PhotoImage(master=canvas, file="cloud_03.gif")
        label = Label(image=gif1)
        label.image = gif1 # keep a reference!
        label.pack()
        canvas.create_image(WIDTH/2,HEIGHT/2, image = gif1)


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
        m2cx = WIDTH*1.25-WIDTH*2/3
        m2cy = HEIGHT*3/2+HEIGHT*1/10
        m2r = WIDTH*3/5*0.8
        m1cx = WIDTH*1.25
        m1cy = HEIGHT*1.45
        m1r = WIDTH*3/5*0.8


    # CITATION: I got the tkinter drawing funtions from https://www.cs.cmu.edu/~112/notes/notes-graphics.html
    def run(self):
        def redrawAllWrapper(self, canvas):
            canvas.delete(ALL)
            canvas.create_rectangle(0, 0, WIDTH, HEIGHT,
                                    fill='white', width=0)
            self.redrawAll(canvas)
            canvas.update()
    
        def mousePressedWrapper(self, event, canvas):
            self.mousePressed(event)
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
