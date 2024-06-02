from graphics import *

win = GraphWin("Esempio", 500, 500)
win.setBackground("white")
win.setCoords(0,0,6500,500)

ciclistaImage = Image(Point(0,0), "cycling.gif")
#centerPoint = ciclistaImage.getAnchor()
ciclistaImage.draw(win)



def potenza(v, sinalfa):
    m = 70 #70 kg
    g = 9.8 #9.8 m/s^2
    c = 0.6
    d = 1.29 # 1,29 kg/m^3
    S = 1 #1m^2
    potenza = m * g * sinalfa + 1/2 * c * d * S * v * v * v
    return potenza

h0=0
h1=300
h2=100
h3=200
h4=0

def altimetria(x) :
    if x<1000:
        return 0
    if x>=1000 and x<2000:  
        return (x-1000)/1000* (h1-h0)+h0
    if x>=2000 and x<2500:
        return (x-2000)/500*(h2-h1)+h1
    if x>=2500 and x<3000:
        return(x-2500)/500*(h3-h2)+h2
    if x>=3000 and x<5000:
        return (x-3000)/2000*(h4-h3)+h3
    if x>=5000 and x<6500:
        return 0
    if x>=6500:
        return -1

def pendenza(x) :
    h1 = altimetria(x)
    h2 = altimetria(x + 10)
    sinalfa = (h2 - h1)/ 10
    return sinalfa

dt = 2 # 2 s
x = 0
v = 20 # 20 m/s
er = 1e6


for x in range(6500):
    h=altimetria(x)
    win.plot(x,h,"black")
x=0

while x<6500 :
    sinalfa = pendenza(x)
    p = potenza(v,sinalfa)
    er= er - p * dt
    x=x+v*dt
    ciclistaImage.move(v*dt,altimetria(x)-altimetria(x-v*dt))
    print ("sinalfa=",sinalfa,"potenza=",p,"energia residua=",er,"x=",x,"velocità=",v)
    
