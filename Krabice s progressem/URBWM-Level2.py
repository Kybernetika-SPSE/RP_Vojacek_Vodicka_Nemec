import random
Jackpot=[]

As = ["káryA" , "pikyA" , "srdceA" , "křížeA"]
symbol= ["piky", "kříže", "káry", "srdce"]
číslo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
Counter = 0 
running = True

Balík= []
Balík2 = []
Jackpot=[]
karta=[]


for i in range(len(symbol)*len(číslo)):
    while True:
        karta=[]
        X = random.randrange(0,4)
        Y = random.randrange(0,14)
        karta.append(str(symbol[X]))
        karta.append(str(číslo[Y]))

        if not karta in Balík :
            break
    Balík.append(karta)
    Balík2.append(karta)



random.shuffle(Balík2)
random.shuffle(Balík)


for cock in range(len(symbol)*len(číslo)):
    if Balík[cock] == Balík2[cock]:
        Jackpot.append(Balík[cock])


print(Jackpot)
check=[]
for As in (Jackpot[:4]):
    if "A" in As:
        check.append("A")
if len(check) == 4:
    final="WHAT"
else:
    final="bigX"
check=[]

print(final)

