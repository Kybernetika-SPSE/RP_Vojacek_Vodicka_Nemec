import random
from os import path
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

#____________________________________________________
with open(path.join(dir,"sources","progress")) as negrum:
    amorgor=negrum.read()
fucking=amorgor.split(";")
fucking=fucking[:-1]
amorgor=""
print(len(fucking))

#_________________________________________________

if 200> len(fucking)>100:
    číslo = [8, 9, 10, "J", "Q", "K", "A"]
    symbol= ["piky", "kříže", "káry", "srdce","piky", "kříže", "káry", "srdce"]
elif len(fucking)>200:
    číslo = ["A"]
    symbol= ["piky", "kříže", "káry", "srdce","piky", "kříže", "káry", "srdce","piky", "kříže", "káry", "srdce"]


for l in range(len(symbol)):
    karta=[]   
    karta.append(str(symbol[l]))
    if karta==["srdce"]:
        for z in range(len(číslo)):
            karta = ["srdce"]
            karta.append(str(číslo[z]))        
            Balík.append(karta)
            Balík2.append(karta)
    if karta==["káry"]:
        for z in range(len(číslo)):
            karta = ["káry"]
            karta.append(str(číslo[z]))        
            Balík.append(karta)
            Balík2.append(karta)
    if karta==["kříže"]:
        for z in range(len(číslo)):
            karta = ["kříže"]
            karta.append(str(číslo[z]))        
            Balík.append(karta)
            Balík2.append(karta)
    if karta==["piky"]:
        for z in range(len(číslo)):
            karta = ["piky"]
            karta.append(str(číslo[z]))        
            Balík.append(karta)
            Balík2.append(karta)


random.shuffle(Balík2)
random.shuffle(Balík)


for cock in range(len(symbol)*len(číslo)):
    if Balík[cock] == Balík2[cock]:
        Jackpot.append(Balík[cock])


#--------------dolízávando---------------------------
cum = random.randrange(1,11)

if len(Jackpot) ==1 or len(Jackpot) ==2:
    if cum > 2:
        karta=[]
        X = random.randrange(0,len(symbol))
        Y = random.randrange(0,len(číslo))
        karta.append(str(symbol[X]))
        karta.append(str(číslo[Y]))
        if karta not in Jackpot:
            Jackpot.append(karta)
        else:
            pass
        print("ihavedonemypart")
    elif cum > 1:
        for kj in range(2):
            karta=[]
            X = random.randrange(0,len(symbol))
            Y = random.randrange(0,len(číslo))
            karta.append(str(symbol[X]))
            karta.append(str(číslo[Y]))
            if karta not in Jackpot:
                Jackpot.append(karta)
            else:
                pass
            print("ihavedonemypart")
    else:
        pass
elif Jackpot==[]:
    if cum > 5:
        ser= random.randrange(4)
        for i in range (ser):
            karta=[]
            X = random.randrange(0,len(symbol))
            Y = random.randrange(len(číslo))
            karta.append(str(symbol[X]))
            karta.append(str(číslo[Y]))
            if karta not in Jackpot:
                Jackpot.append(karta)
            else:
                pass
            print("ihavedoneitall")

if len(Jackpot)==1:
    Jackpot.append("0")
    Jackpot.append("0")
    Jackpot.append("0")
elif len(Jackpot)==2:
    Jackpot.append("0")
    Jackpot.append("0")
elif len(Jackpot)==3:
    Jackpot.append("0")
print(Jackpot)

check=[]
final="nothing"
if Jackpot==[]:
    final="OOOF"

#----conditions-----------------------------------------

for Js in (Jackpot[:4]):
    if "J" in Js:
        check.append("J")
if len(check) == 1:
    final="badluck"
check=[]

for As in (Jackpot[:4]):
    if "A" in As:
        check.append("A")
if len(check)>0:
    final="highcard"
check=[]

for piky in (Jackpot[:4]):
    if "piky" in piky:
        check.append("P")
if len(check) == 2:
    final = "two"
elif len(check) == 3:
    final= "three" 
elif len(check) == 4:
    final= "full"  
check=[]

for srdce in (Jackpot[:4]):
    if "srdce" in srdce:
        check.append("S")
if len(check) == 2:
    final = "two"
elif len(check) == 3:
    final= "three" 
elif len(check) == 4:
    final= "full" 
check=[]

for káry in (Jackpot[:4]):
    if "káry" in káry:
        check.append("K")
if len(check) == 2:
    final = "two"
elif len(check) == 3:
    final= "three" 
elif len(check) == 4:
    final= "full" 
check=[]

for kříže in (Jackpot[:4]):
    if "kříže" in kříže:
        check.append("C")  
if len(check) == 2:
    final = "two"
elif len(check) == 3:
    final= "three" 
elif len(check) == 4:
    final= "full"    
check=[]



if len(Jackpot)== 1 or len(Jackpot)== 2 or len(Jackpot)== 3:
    pass
else:
    if Jackpot==[]:
        final="OOOF"
    elif "1" in Jackpot[0] and "2" in Jackpot[1] and "3" in Jackpot[2] and "4" in Jackpot[3]:
        final="fullflush"
    elif "2" in Jackpot[0] and "3" in Jackpot[1] and "4" in Jackpot[2] and "5" in Jackpot[3]:
        final="fullflush"
    elif "3" in Jackpot[0] and "4" in Jackpot[1] and "5" in Jackpot[2] and "6" in Jackpot[3]:
        final="fullflush"
    elif "4" in Jackpot[0] and "5" in Jackpot[1] and "6" in Jackpot[2] and "7" in Jackpot[3]:
        final="fullflush"
    elif "5" in Jackpot[0] and "6" in Jackpot[1] and "7" in Jackpot[2] and "8" in Jackpot[3]:
        final="fullflush"
    elif "6" in Jackpot[0] and "7" in Jackpot[1] and "8" in Jackpot[2] and "9" in Jackpot[3]:
        final="fullflush"
    elif "7" in Jackpot[0] and "8" in Jackpot[1] and "9" in Jackpot[2] and "10" in Jackpot[3]:
        final="fullflush"
    else:
        pass

for Qs in (Jackpot[:4]):
    if "Q" in Qs:
        check.append("Q")
if len(check) == 3:
    final="sixqueens"
check=[]


for As in (Jackpot[:4]):
    if "A" in As:
        check.append("A")
if len(check) == 4:
    final="WHAT"
check=[]

for Js in (Jackpot[:4]):
    if "J" in Js:
        check.append("J")
if len(check) == 4:
    final="death"
check=[]


#-------------next-------------------



if final== "sixqueens":
    rollin = random.randrange(20)
    if rollin < 4:
        final="two"
    elif 4<=rollin<8:
        final="three"
    elif 8<=rollin<12:
        final="highcard"
    elif 12<=rollin<16:
        final="badluck"
    elif 16<=rollin<18:
        final="death"
    elif rollin ==20:
        final="fullflush"
    else:
        final="full"


if final == "highcard":
    if len(fucking)>=220:
        for sos in range(20):
            fucking.pop(-1)
    else:
        for sos in range(10):
            fucking.append("I")

if final == "badluck":
    if len(fucking)>40:
        fucking = fucking[:len(fucking)-40]
    else:
        for sos in range(len(fucking)):
            fucking.pop(-1)

if final == "two":
    for sos in range(15):
        fucking.append("I")
if final == "three":
    for sos in range(20):
        fucking.append("I")
if final == "full":
    for sos in range(25):
        fucking.append("I")

if final == "fullflush":
    for sos in range(30):
        fucking.append("I")

if final == "death":
        for sos in range(len(final)):
            fucking.pop(-1)

if final == "OOOF":
    if 100>len(fucking)>35:
        if len(fucking)>10:
            fucking = fucking[:len(fucking)-10]
        else:
            for sos in range(len(fucking)):
                fucking.pop(-1)
    if len(fucking)>100:
        fucking = fucking[:len(fucking)-20]
    else:
        pass

    

if final =="nothing":
    if 51>len(fucking)>24:
        for sos in range(10):
            fucking.append("I")
    elif len(fucking)<25:
        for sos in range(5):
            fucking.append("I")
    elif 100>len(fucking)>50:
        pass
    elif len(fucking)>100:
        for sos in range(5):
            fucking.pop(-1)
    elif len(fucking)>100 and "piky" in Jackpot and "srdce" in Jackpot and "kříže" in Jackpot and "káry" in Jackpot:
        final="toopicky"
        for sos in range(100):
            fucking.pop(-1)

if final =="WHAT":
    BIGWIN=1






print(len(fucking))

for kula in fucking:
    amorgor += (str(kula)+";")
with open(path.join(dir,"sources","progress"),"w") as porno:
    porno.write(amorgor)
print(Jackpot)
print(final)

