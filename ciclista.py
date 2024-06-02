from graphics import*
win = GraphWin("Esempio",500,500)
win.setBackground("white")
win.setCoords(0,0,6500,1000)


def Power (sinalfa, v):
    m = 70 #70 kg
    g = 9.81 #9.81 m/s^2
    c = 0.6
    d = 1.29 #1.29 kg/m^3
    S = 1 #1m^2


    Power = m*g*v*sinalfa+1/2*c*d*S*v*v*v
    return Power


def altimetria (x):
    if x<1000:
        return 0
    if x>=1000 and x<2000:  
        return x/5 - 200
    if x>=2000 and x<2500:
        return -x/5 + 600
    if x>=2500 and x<3000:
        return 3*x/10 - 650
    if x>=3000 and x<5000:
        return -x/8 + 625
    if x>=5000 and x<6500:
        return 0
    if x>=6500:
        return -1

    
def pendenza (x):
    h1 = altimetria(x)
    h2 = altimetria(x+10)
    sinalfa= (h2 - h1)/10
    return sinalfa

x = 0
v = 20
dt = 2
er = 1e6

for x in range(6500):
    h = altimetria(x)
    win.plot(x,h,"black")

    
while x<=6500:
    sinalfa = pendenza(x)
    P = Power (sinalfa, v)
    er = er - P*dt
    x = x + v*dt

    print (sinalfa,"Power =", P,"energia_residua =",er,"x =",x,"v =",v) 

    
    
    
    
        
    
         
        
