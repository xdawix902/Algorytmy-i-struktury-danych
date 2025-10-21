import random

kierunek = [random.choice([-1,1]) for i in range(6)]
wspolrzedne = []
x = 2;

for y in range(6):
    if(x + kierunek[y] == 0):
        x = 2
    elif(x + kierunek[y] > 8):
        x = 7
    else:
        x += kierunek[y];
        wspolrzedne.append([x,y+2]);

print(wspolrzedne)