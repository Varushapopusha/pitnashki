from play import*
from random import*
set_backdrop((191,48,48))
class Lalka():
    def __init__(self,color,x,y,width,height,number):
        self.color=color
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.number=number
        self.box=new_box(self.color,self.x,self.y,self.width,self.height)
        self.text=new_text(str(self.number),self.x,self.y,None,160,'black') 
    def update(self):
        self.box.x=self.x
        self.text.x=self.x
        self.box.y=self.y
        self.text.y=self.y
    def muvright(self,empty):
        if self.x+200==empty.x and self.y==empty.y:  
            self.x+=200
            empty.x-=200
    def muvleft(self,empty):
        if self.x-200==empty.x and self.y==empty.y:  
            self.x-=200
            empty.x+=200
    def muvdown(self,empty):
        if self.y-200==empty.y and self.x==empty.x:  
            self.y-=200
            empty.y+=200
    def muvup(self,empty):
        if self.y+200==empty.y and self.x==empty.x:  
            self.y+=200
            empty.y-=200
qs =[]  
num_listochek=(list(range(1,16)))
shuffle(num_listochek)
field=new_box('black', 0, 0,820,820)
lula=new_box('black', 300, -300,180,180)
for i in range(4):
    for g in range(4):
        if i==g==3:
            break
        q=Lalka((191,48,48),-300+i*200,300-200*g,180,180,num_listochek[4*i+g])
        qs.append(q)
@repeat_forever
def game():
    for i in range(len(qs)):
        if qs[i].box.is_clicked:
            if qs[i].x+200==lula.x:
                qs[i].muvright(lula)
            elif qs[i].x-200==lula.x:
                qs[i].muvleft(lula)
            elif qs[i].y-200==lula.y:
                qs[i].muvdown(lula)  
            elif qs[i].y+200==lula.y:
                qs[i].muvup(lula)                                                   
            qs[i].update()
start_program()


