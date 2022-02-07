from kandinsky import fill_rect as fRect,draw_string as dStr,get_pixel as gColor,set_pixel as pixel
from ion import *
from random import *
from time import *

SW,SH=320,222
GW,GH=300,200
help,h=["[ARROW]→ Move\n    [OK]→ Jump","[EXE]→ Restart\n    [BACKSPACE]→ Pause","[0]→ Quit"],0

yVel,t=0,10
pf_col=[(64,252,64),(0,0,0)]
rTime,rMax=0,10

pfRefresh,lvl=0,0
pf=[
[[20,180,30,10],[80,160,30,10],[140,140,30,10],[200,120,30,10],[260,100,30,10]],
[[20,180,30,10],[70,145,180,10],[280,120,30,10],[80,35,230,10],[220,90,30,10],[150,90,30,10],[80,90,30,10]],
[[10,60,280,10],[110,110,40,10],[180,60,10,80],[160,180,120,10],[280,70,10,120],[60,190,20,10],[40,160,20,10],[60,130,20,10],[150,110,10,80],[225,130,30,5],[260,150,5,5],[270,130,5,5],[240,100,40,5],[200,115,5,5],[220,90,30,5]],
[[100,180,20,10],[100,150,20,10],[100,120,20,10],[100,10,100,90],[135,120,5,5],[155,120,5,5],[175,120,5,5],[195,120,5,5],[220,120,30,10]],
[[270,180,10,10],[270,150,10,10],[270,120,10,10],[270,90,10,10],[200,90,10,10],[120,90,20,10],[50,160,210,10],[50,100,10,60],[260,100,10,70],[50,10,10,80],[50,90,20,10]]
]
class GameEngine:
  def init():
    fRect(0,0,SW,SH,pf_col[1])
    fRect(10,10,GW,GH,'gray')
    dStr("PLATFORMER",110,100,'black','gray')
    dStr("by OJd_dJO",110,114,'black','gray')
    dStr("PRESS [OK]",110,190,'black','gray')
    menu=True
    while menu:
      if keydown(KEY_OK):
        menu=False
    GameEngine.transition()
    return True
  def quit():
    global run
    if keydown(KEY_ZERO):fRect(0,0,SW,SH,'black');return False
    elif run:return True
  def refresh():
    global rTime,rMax
    if rTime==0:fRect(10,10,300,200,'gray');rTime=rMax
    else:rTime-=1
  def pause():
    if keydown(KEY_BACKSPACE):
      p=True;sleep(0.2)
      dStr("PAUSED",int(SW/2-30),int(SH/2-4),'black','white')
      while p:
        if keydown(KEY_BACKSPACE):
          p=False;sleep(0.2)
        GameEngine.quit()
  def transition():
    global x,y,help,h
    col='black'
    for e in range(2):
      for i in range(20):
        for s in range(300):
          for l in range(10):
            pixel(10+s,10+10*i+l,col)
      if col=='black':
        dStr("LOADING...",200,180,'white','black')
        dStr("How to play ?\n\n    "+help[h],25,70,'white','black')
        if not h==2:h+=1
        elif h==2:h=0
        sleep(2)
      col='gray'
    x,y=10,15

class Entity:
  def player():
    for L in range(10):
      for l in range(10):
        pixel(x+l,y+L,'purple')
    def mvmt():
      global x,y
      def grounded():
        global x,y,t,yVel
        for i in range(10):
          if pf_col.count(gColor(x+i,y+11)):
            t=0;return True
        for i in range(10):
          if pf_col.count(gColor(x+i,y-1)):
            yVel=-1
      def gravity():
        global y,yVel,t
        if not grounded():
          if yVel>-5:
            if t==0:yVel-=1;t=10
            else:t-=1
          for s in range(abs(yVel)):
            for i in range(10):
              pixel(x+i,y-s,'gray')
          if yVel>0:
            for s in range(abs(yVel)+2):
              for i in range(10):
                pixel(x+i,y+10+s,'gray')
        else:yVel=0
        return yVel
      def jump():
        global y,yVel
        if keydown(KEY_OK):
          if grounded():
            yVel=3;y-=3
      def colision(key):
        for i in range(10):
          if key=="R":test=gColor(x+10,y+i)
          if key=="L":test=gColor(x-1,y+i)
          if pf_col.count(test)==1:return True
      if keydown(KEY_LEFT):
        if not colision("L"):
          x-=1
          for i in range(10):
            pixel(x+10,y+i,'gray')
      elif keydown(KEY_RIGHT):
        if not colision("R"):
          x+=1
          for i in range(10):
            pixel(x-1,y+i,'gray')
      jump();yVel=gravity()
      for i in range(abs(yVel)):
        if not grounded():
          if yVel>0:y-=1
          if yVel<0:y+=1
    def nxtLvl():
      global lvl,run
      for i in range(10):
        if gColor(x+i,y+11)==pf_col[0]:
          if not len(pf)-1==lvl:
            GameEngine.transition();lvl+=1;break
          else:
            for i in range(20):
              for s in range(300):
                for l in range(10):
                  pixel(10+s,10+10*i+l,'black')
            dStr("GG!",145,110,'white','black');run=False;break
    if keydown(KEY_EXE):
      GameEngine.transition()
    mvmt();nxtLvl()
  def platform():
    global pfRefresh,rMax
    def draw():
      for i in range(len(pf[lvl])-1):
        fRect(pf[lvl][i][0],pf[lvl][i][1],pf[lvl][i][2],pf[lvl][i][3],pf_col[1])
      fRect(pf[lvl][-1][0],pf[lvl][-1][1],pf[lvl][-1][2],pf[lvl][-1][3],pf_col[0])
    if pfRefresh==0:draw();pfRefresh=rMax
    else:pfRefresh-=1

run=GameEngine.init()

while run:
  GameEngine.pause()
  GameEngine.refresh()
  Entity.platform()
  Entity.player()
  run=GameEngine.quit()