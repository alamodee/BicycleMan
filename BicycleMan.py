from tkinter import *
import math
import random
import numpy as np


class BicycleMan:
    def __init__(self):
        self.manAngle = 0

        self.width = 710
        self.height = 410
        self.scrollX = 0

        self.gravity = 1
        self.numOfGround = 100
        self.groundList = []
        self.upperList = []
        self.GroundHeight = 100

        # self.startPoint = self.width/2
        self.manCX = 50
        self.manCY = 200
        self.manWidth =  self.width/100 * math.cos(math.pi*1.83+self.manAngle) + self.width/200  -(self.width/100 * math.cos(math.pi*1.16+self.manAngle) + self.width/200)
        self.manHeight = 20


        self.gameState = "PREPARE"
        self.enableGravity = True

        self.xy1 = []
        self.manCollisionSide = False

        self.speedY = 0

        self.jumpDuration = 10
        self.jumpingTime = 0

        # back ground
        self.sunCX = self.width/2
        self.sunCY = self.height/2
        self.sunR = self.width/10
        self.lightStart = 30
        self.lightR = self.sunR * 10
        self.fujiUB = self.width/10
        self.fujiLB = self.width/5
        self.moveCloud1 = 0.25
        self.moveCloud2 = 0.35
        self.moveCloud3 = 0.4
        self.c1Return = False
        self.c2Return = False
        self.c3Return = False
        self.c1x = self.width * 1/5
        self.c2x = self.width * 1/2
        self.c3x = self.width * 3/4
        self.cherryList = []
        self.time = 0

        self.meterCount = 0


        pass


    def mousePressed(self, event):
        pass


    def keyPressed(self, event):
        if (event.keysym == "y"):
            self.manAngle += math.pi/18

        if (event.keysym == "s") and self.gameState == "READY":
            self.gameState = "PLAYING"

        if self.enableGravity == False and  (event.keysym == "Up"):
            self.jump()

        if self.gameState == "GAMEOVER":
            if (event.keysym == "r"):
                self.__init__()

        pass


    def timerFired(self, canvas):
        self.time += self.timerDelay
        if self.gameState == "PLAYING":
            self.scrollX += 3

        if self.enableGravity:
            self.speedY += self.gravity
        self.manCY += self.speedY

        
        if self.gameState == "PLAYING":
            self.meterCount += 1
            self.manCX += 3

        self.bestMeter = 0

    
        # for coord in self.upperList:
        #     if self.manCX >= coord[0] and self.manCX <= coord[1]:
        #         self.enableGravity = 0
        #         return 

        # print(self.enableGravity)

        self.lightStart += 0.25
        # for i in range(len(self.cherryList)):
        #     self.cherryList[i][1] += 2
        # if self.time % 100 == 0:
        #     self.createCherry()

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

        self.isNewHighScore = False

        pass


    def redrawAll(self, canvas):
        self.collision()
        self.createGround(canvas)
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

        # self.deleteGround(canvas)
        # self.drawCherry(canvas)
        pass


    def man(self, canvas, cx, cy):
        # r = self.width/1000
        # canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="blue")
        headCX = cx + self.width/75 * math.cos(math.pi/3+self.manAngle)
        headCY = cy - self.width/75 * math.sin(math.pi/3+self.manAngle)
        headR = self.width/200
        canvas.create_oval(headCX - headR, headCY - headR, headCX + headR, headCY + headR, fill = "black",outline="black", width=self.width/1000)

        fwheelCX = cx + self.width/100 * math.cos(math.pi*1.83+self.manAngle)
        fwheelCY = cy - self.width/100 * math.sin(math.pi*1.83+self.manAngle)
        fwheelR = self.width/200
        canvas.create_oval(fwheelCX - fwheelR, fwheelCY - fwheelR, fwheelCX + fwheelR, fwheelCY + fwheelR, fill = "white", outline="black", width=self.width/1000)

        bwheelCX = cx + self.width/100 * math.cos(math.pi*1.16+self.manAngle)
        bwheelCY = cy - self.width/100 * math.sin(math.pi*1.16+self.manAngle)
        bwheelR = self.width/200
        canvas.create_oval(bwheelCX - bwheelR, bwheelCY - bwheelR, bwheelCX + bwheelR, bwheelCY + bwheelR, fill = "white", outline="black", width=self.width/1000)

        bodyX1 = cx + self.width/150 * math.cos(math.pi+self.manAngle)
        bodyX2 = headCX
        bodyY1 = cy
        bodyY2 = headCY
        canvas.create_line(bodyX1, bodyY1, bodyX2, bodyY2, fill="black", width=self.width/300)

        bbodyX1 = cx + self.width/100 * math.cos(math.pi*1.1+self.manAngle)
        bbodyX2 = cx + self.width/100 * math.cos(math.pi/18+self.manAngle)
        bbodyY1 = cy - self.width/100 * math.sin(math.pi*1.1+self.manAngle)
        bbodyY2 = cy - self.width/100 * math.sin(math.pi/18+self.manAngle)
        canvas.create_line(bbodyX1, bbodyY1, bbodyX2, bbodyY2, fill="red", width=self.width/300)


        legX1 = bodyX1
        legX2 = cx
        legY1 = bodyY1
        legY2 = cy - self.width/75 * math.sin(math.pi*1.8 + self.manAngle)
        canvas.create_line(legX1, legY1, legX2, legY2, fill="black", width=self.width/300)

        armX1 = cx + self.width/150 * math.cos(math.pi/3+self.manAngle)
        armX2 = cx + self.width/100 * math.cos(math.pi*1.94+self.manAngle)
        armY1 = cy - self.width/150 * math.sin(math.pi/3+self.manAngle)
        armY2 = cy - self.width/100 * math.sin(math.pi*1.94+self.manAngle)
        canvas.create_line(armX1, armY1, armX2, armY2, fill="black", width=self.width/300)



    def drawMan(self, canvas):
        if not self.gameState == "GAMEOVER":
            self.man(canvas, self.manCX-self.scrollX, self.manCY)


    def drawStart(self, canvas):
        if self.gameState == "READY":
            canvas.create_text(self.width/2, self.height/2-50, text="Bicycle Man", font="Times 56", fill="black")
            canvas.create_text(self.width/2, self.height/2, text="press s to start", font="Times 35", fill="black")

    def drawMeterCount(self, canvas):
        if self.gameState == "PLAYING":
            canvas.create_text(self.width * 1/10, self.height * 1/10, text = "%dm" % (self.meterCount), fill = "black", font="Times 20")

    def distance(x1, y1, x2, y2):
        return ((x2-x1)**2 + (x2-x1)**2)**.5

    #CITATION algorithm from http://tokibito.hatenablog.com/entry/20121227/1356581559
    def collisionB(self, a, b, p, distance):
        vAP = np.array([p[0]-a[0], p[1]-a[1]])
        vAB = np.array([b[0]-a[0], b[1]-a[1]])
        PX = np.cross(vAP, vAB)/ np.linalg.norm(vAB)
        AX = np.dot(vAP, vAB)/ np.linalg.norm(vAB)
        A = np.array(a)
        B = np.array(b)
        P = np.array(p)
        AB = np.linalg.norm(B-A)
        AP = np.linalg.norm(P-A)
        # if p is right of the left top point of ground
        if AB >= AP:
            #if p is left of the left top point of ground
            if AX < 0:
                return False
            #collide
            if PX <= distance:
                if PX == distance:
                    return True
                if PX < distance:
                    #calcurate gap
                    gap = distance - PX
                    # modify gap
                    self.manCY -= gap
                    return True
            else:
                return False
        else:
            # print("false3")
            return False

    def collisionS(self, a, b, p, distance):
        vAP = np.array([p[0]-a[0], p[1]-a[1]])
        vAB = np.array([b[0]-a[0], b[1]-a[1]])
        PX = np.cross(vAP, vAB)/ np.linalg.norm(vAB)
        AX = np.dot(vAP, vAB)/ np.linalg.norm(vAB)
        A = np.array(a)
        B = np.array(b)
        P = np.array(p)
        AB = np.linalg.norm(B-A)
        AP = np.linalg.norm(P-A)
        # if p is right of the left top point of ground
        if AB >= AP:
            #collide
            if PX <= distance:
                if PX == distance:
                    return True
                if PX < distance:
                    #calcurate gap
                    # gap = distance - PX
                    # # modify gap
                    # self.manCX -= gap
                    return True
            else:
                # print("false1")
                return False
        else:
            # print("false2")
            return False

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





    # def collisionBottom(self):
    #     for line in self.groundList:
    #         # print("trying to check ", [line[0]-self.scrollX, line[1]], [line[2]-self.scrollX, line[3]])
    #         if self.collisionB([line[0]-self.scrollX, line[1]], [line[2]-self.scrollX, line[3]], [self.manCX-self.manScrollX, self.manCY], 8):
    #             self.enableGravity = 0
    #             return
    #     self.enableGravity = 1

    # def collisionSide(self):
    #     for line in self.groundList:
    #         if self.collisionS([line[0]-self.scrollX, line[3]], [line[0]-self.scrollX, line[1]], [self.manCX-self.manScrollX, self.manCY], 8):
    #             self.manCollisionSide = True
    #             return True
    #     self.manScrollX = 0
    #     self.manCollisionSide = False
    #     return False


    def createGround(self, canvas):
        # cStartPoint = self.width+1
        if self.gameState == "PREPARE":
            #adding initial ground
            self.groundList.append([self.scrollX, self.height * 7/10, self.scrollX + 100, self.height, "#273622"])
           
            gStart = 0
            for i in range(self.numOfGround):
                gWidth = random.randint(50, 100)
                gHeight = random.randint(10, 200)
                colors = ["#273622"]
                # "#3A322B"
                # "#2C523C"
                # "#595E3C"
                color = random.choice(colors)

                self.groundList.append([gStart, self.height-gHeight, gStart+gWidth, self.height, color])
                

                gStart += gWidth + random.randint(10, 40)

            self.gameState = "READY"

    # def deleteGround(self, canvas):
    #      for i in range(len(self.upperList)):
    #          if self.upperList[i][2]-self.scrollX < 0:
    #              self.groundList.pop(i)
    #              self.upperList.pop(i)


    def drawGround(self, canvas, mode=0):
        if not self.gameState == "GAMEOVER":
            for coord in self.groundList:
                canvas.create_rectangle(coord[0]-self.scrollX, coord[1], coord[2]-self.scrollX, coord[3], fill=coord[4], outline =coord[4])

    def jump(self):
        self.speedY -= 20

    def isGameOver(self):
        if self.manCY > self.height or self.manCX - self.scrollX< 0:
            print(self.scrollX)
            print((self.manCX, self.manCY))
            self.gameState = "GAMEOVER"
            if self.bestMeter < self.meterCount:
                self.bestMeter = self.meterCount
                self.isNewHighScore = True
            else:
                self.isNewHighScore = False

    def drawGameOver(self, canvas):
        if self.gameState == "GAMEOVER":
            canvas.create_rectangle(0, 0, self.width, self.height, fill = "#F22547", width = 0)
            canvas.create_text(self.width/2, self.height/2-10, text="Game over", fill = "white", font="Times 50 italic")
            canvas.create_text(self.width/2, self.height/2+30, text="press r to start again", fill = "white", font="Times 30 italic")
            if self.isNewHighScore:
                canvas.create_text(self.width/2, self.height/2-120, text="NEW HIGH SCORE!", fill = "white", font="Times 30 italic")
            else:
                canvas.create_text(self.width/2, self.height/2-120, text="score", fill = "white", font="Times 40 italic")
            canvas.create_text(self.width/2, self.height/2-80, text="%dm" % self.meterCount, fill = "white", font="Times 30 italic")

    def drawSun(self,canvas):
        canvas.create_oval(self.sunCX-self.sunR, self.sunCY-self.sunR,self.sunCX+self.sunR, self.sunCY+self.sunR, fill="#F22547",width=0)
    
    def drawBackground(self, canvas):
            canvas.create_rectangle(0, 0, self.width, self.height,fill="#EDEACC", width=0)
    
    def drawFuji(self, canvas):
        g1 = (self.sunCX-self.width/3, self.height)
        g2 = (self.sunCX+self.width*2/10, self.height)
        g3 = (self.sunCX-self.width/10, self.sunCY)
        g4 = (self.sunCX-self.width/7, self.sunCY)
        w1 = (g4[0]-abs(g1[0]-g4[0])*1/4*1.195, g4[1]+(g1[1]+g4[1])*1/10)
        w2 = (g3[0]+abs(g2[0]-g3[0])*1/2*0.75, g3[1]+abs(g2[1]+g3[1])*5/40)
        w3 = g3
        w4 = g4
        canvas.create_polygon(g1, g2, g3, g4, fill="#727176",width=0)
        canvas.create_polygon(w1, w2, w3, w4, fill="#FFFFFF",width=0)
    
    def drawLight(self, canvas):
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
    
    # def drawGround(self, canvas):
    #     c1 = (0, self.height * 9/10)
    #     c2 = (self.width, self.height)
    #     canvas.create_rectangle(c1, c2,fill="#E09197",width=0)

    def cloud(self, canvas, x, y):
        canvas.create_oval(x-self.width/25*5/3, y-self.height/300*5/3, x+self.width/60*5/3, y+self.height/50*5/3,fill="#FFFFFF", width = 0)
        canvas.create_oval(x-self.width/60*5/3, y-self.height/50*5/3, x+self.width/25*5/3, y+self.height/300*5/3,fill="#FFFFFF", width = 0)
        # canvas.create_oval(x-self.width/20, y-self.height/20, x+self.width/10, y+self.height/20,fill="#FFFFFF", width = 0)

    def drawCloud(self, canvas):
        self.cloud(canvas, self.c1x, self.height * 2/5)
        self.cloud(canvas, self.c2x, self.height * 1/7)
        self.cloud(canvas, self.c3x, self.height * 4/7)

    def bamboo(self, canvas, cx, cy, r, angle, n):
        space = self.width/200
        color = "#5A5239"

        for i in range(n):
            if i == 0:
                p0 = (cx, cy) 
            bamX1 = cx + (i+1)* r * math.cos(angle)
            bamY1 = cy - (i+1)* r * math.sin(angle)
            p1 = (bamX1, bamY1)
            canvas.create_line(p0, p1, fill=color, width=self.width/75)
            bamX1S = cx + ((i+1) * r+space) * math.cos(angle)
            bamY1S = cy - ((i+1) * r+space) * math.sin(angle)
            p1S = (bamX1S, bamY1S)
            p0 = p1S


    def drawBamboo(self, canvas):
        self.bamboo(canvas, self.width*38/40, self.height, self.height*(2/3)*(1/4) ,math.pi/2*7/6, 5)
        self.bamboo(canvas, self.width*34/40, self.height, self.height*(2/3)*(1/4) ,math.pi/2*11/10, 7)
        
    def putCloud(self, canvas):
        gif1 = PhotoImage(master=canvas, file="cloud_03.gif")
        label = Label(image=gif1)
        label.image = gif1 # keep a reference!
        label.pack()
        canvas.create_image(self.width/2,self.height/2, image = gif1)

    # def fan(self, canvas, x, y, r, start):
    #     outColor = "#663399"
    #     inColor = "#DAA520"
    #     handleColor = "#000000"
    #     canvas.create_arc(x-r, y-r, x+r, y+r, start = start, extent = 130, style="pieslice",fill=outColor, width=0, outline=outColor)
    #     canvas.create_arc(x-r, y-r, x+r, y+r, start = start+10, extent = 10, style="pieslice",fill=inColor, width=0, outline=inColor)
    #     canvas.create_arc(x-r, y-r, x+r, y+r, start = start+30, extent = 10, style="pieslice",fill=inColor, width=0, outline=inColor)
    #     canvas.create_arc(x-r, y-r, x+r, y+r, start = start+50, extent = 10, style="pieslice",fill=inColor, width=0, outline=inColor)
    #     canvas.create_arc(x-r, y-r, x+r, y+r, start = start+70, extent = 10, style="pieslice",fill=inColor, width=0, outline=inColor)
    #     canvas.create_arc(x-r, y-r, x+r, y+r, start = start+90, extent = 10, style="pieslice",fill=inColor, width=0, outline=inColor)
    #     canvas.create_arc(x-r, y-r, x+r, y+r, start = start+110, extent = 10, style="pieslice",fill=inColor, width=0, outline=inColor)
    #     canvas.create_arc(x-r/4, y-r/4, x+r/4, y+r/4, start = start, extent = 130, style="pieslice",fill=handleColor, width=0)

    # def createFan(self, x, y, start):
    #     self.fanList.append([x, y, start])

    # def drawFan(self, canvas):
    #     for coord in self.fanList:
    #         self.fan(canvas, coord[0], coord[1], self.width/20, coord[2])

    def cherry(self, canvas, x, y):
        color = "#FCD3DC"
        r = self.width/30
        canvas.create_oval(x-r*4/10, y-r/6, x+r*4/10, y+r/6, fill = color, width=0)
        
        # canvas.create_arc(x-r, y-r, x+r, y+r, start = 50, extent = 50, style="chord",fill=color, width=0, outline = color)
        # canvas.create_arc(x-r, y-3*r, x+r, y-2*r, start = 230, extent = 50, style="chord",fill=color, width=0, outline = color)
    def createCherry(self):
        x = random.randint(1, self.width)
        self.cherryList.append([x, 0])


    def drawCherry(self, canvas):
        for coord in self.cherryList:
            self.cherry(canvas, coord[0], coord[1])


    def drawBackgroundMountain(self, canvas):
        p1 = (-self.width*1/7, self.height)
        p2 = (self.width*1/2, self.height)
        p3 = (self.width*1/10, self.height*8/10)
        p4 = (self.width*2/10, self.height*8/10)
        canvas.create_polygon(p1, p2, p4, p3,fill="#B8B694", width=0)
        q1 = (self.width*4/10, self.height)
        q2 = (self.width*11/10, self.height)
        q3 = (self.width*6/10, self.height*9/10)
        q4 = (self.width*8/10, self.height*9/10)
        canvas.create_polygon(q1, q2, q4, q3,fill="#B8B694", width=0)
        # m1cx = self.width*1.25
        # m1cy = self.height*1.45
        # m1r = self.width*3/5*0.8
        # canvas.create_oval(m1cx-m1r,m1cy-m1r,m1cx+m1r,m1cy+m1r,fill="#B8B694", width=0)
        m2cx = self.width*1.25-self.width*2/3
        m2cy = self.height*3/2+self.height*1/10
        m2r = self.width*3/5*0.8
        # canvas.create_oval(m2cx-m2r,m2cy-m2r,m2cx+m2r,m2cy+m2,fill="#B8B694", width=0)
        m1cx = self.width*1.25
        m1cy = self.height*1.45
        m1r = self.width*3/5*0.8
        # canvas.create_oval(m1cx-m1r,m1cy-m1r,m1cx+m1r,m1cy+m1r,fill="#B8B694", width=0)


    # CITATION: I got the tkinter drawing funtions from https://www.cs.cmu.edu/~112/notes/notes-graphics.html
    def run(self, width=300, height=300):
        def redrawAllWrapper(self, canvas):
            canvas.delete(ALL)
            canvas.create_rectangle(0, 0, self.width, self.height,
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
        self.width = width
        self.height = height
        self.timerDelay = 10 # milliseconds
        #initiate visualizer
        bicycleman = BicycleMan()
        # create the root and the canvas
        root = Tk()
        canvas = Canvas(root, width=self.width, height=self.height)
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
        viewWidth = 710
        viewHeight = 410
        self.run(viewWidth, viewHeight)
        
    def main(self):
        self.play()

b = BicycleMan()
b.main()
