import random
from os import path
dir = path.dirname(__file__)
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    with open(path.join(dir,"sources","progress")) as negrum:
        amorgor=negrum.read()
    fucking=amorgor.split(";")
    fucking=fucking[:-1]
    amorgor=""
    print(len(fucking))

    with open(path.join(dir,"sources","counter")) as negrum:
        amorgor=negrum.read()
    counterer=amorgor.split(";")
    counterer=counterer[:-1]
    amorgor=""
    counterer.append("I")

    with open(path.join(dir,"sources","triposobe")) as negrum:
        amorgor=negrum.read()
    posobecheck=amorgor.split(";")
    posobecheck=posobecheck[:-1]
    amorgor=""

    with open(path.join(dir,"sources","cernojecka")) as negrum:
        amorgor=negrum.read()
    blackJs=amorgor.split(";")
    blackJs=blackJs[:-1]
    amorgor=""

    with open(path.join(dir,"sources","impove")) as negrum:
        amorgor=negrum.read()
    Imps=amorgor.split(";")
    Imps=Imps[:-1]
    amorgor=""

    with open(path.join(dir,"sources","wolfe")) as negrum:
        amorgor=negrum.read()
    thewolf=amorgor.split(";")
    thewolf=thewolf[:-1]
    amorgor=""

    with open(path.join(dir,"sources","victorthesaviour")) as negrum:
        amorgor=negrum.read()
    saviour=amorgor.split(";")
    saviour=saviour[:-1]
    amorgor=""

    counterer=[]
    fucking=[]
    saviour=[]
    thewolf=[]
    Imps=[]
    blackJs=[]
    posobecheck=[]

    amorgor=""
    for kula in counterer:
        amorgor += (str(kula)+";")
    with open(path.join(dir,"sources","counter"),"w") as porno:
        porno.write(amorgor)
    amorgor=""

    for kula in fucking:
        amorgor += (str(kula)+";")
    with open(path.join(dir,"sources","progress"),"w") as porno:
        porno.write(amorgor)

    amorgor=""
    for kula in posobecheck:
        amorgor += (str(kula)+";")
    with open(path.join(dir,"sources","triposobe"),"w") as porno:
        porno.write(amorgor)
    amorgor=""

    amorgor=""
    for kula in blackJs:
        amorgor += (str(kula)+";")
    with open(path.join(dir,"sources","cernojecka"),"w") as porno:
        porno.write(amorgor)
    amorgor=""

    amorgor=""
    for kula in Imps:
        amorgor += (str(kula)+";")
    with open(path.join(dir,"sources","impove"),"w") as porno:
        porno.write(amorgor)
    amorgor=""

    amorgor=""
    for kula in thewolf:
        amorgor += (str(kula)+";")
    with open(path.join(dir,"sources","wolfe"),"w") as porno:
        porno.write(amorgor)
    amorgor=""

    amorgor=""
    for kula in saviour:
        amorgor += (str(kula)+";")
    with open(path.join(dir,"sources","victorthesaviour"),"w") as porno:
        porno.write(amorgor)
    amorgor=""

    return render_template("Stránka.html")


#_______________________________________________________________________________________________
@app.route("/game1/rules")
def gamerules1():
    amorgor = "spust"
    return render_template("game1rules.html", buton = amorgor)
#_______________________________________________________________________________________________
@app.route("/game1/running")
def gamerunning1():
    x = random.randrange(1,10)
    return render_template("gameruning.html",tohlechcu = x)
#_______________________________________________________________________________________________
@app.route("/game1/results")
def gameresults1():
    Jackpot=[]
    symbol= ["piky", "kříže", "káry", "srdce"]
    číslo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]


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
    fuckingreverse = fucking

    with open(path.join(dir,"sources","counter")) as negrum:
        amorgor=negrum.read()
    counterer=amorgor.split(";")
    counterer=counterer[:-1]
    amorgor=""
    counterer.append("I")
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
    elif len(Jackpot)==0:
        Jackpot.append("0")
        Jackpot.append("0")
        Jackpot.append("0")
        Jackpot.append("0")
    Jackpot=Jackpot[:4]
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

    karta11=str(Jackpot[0])
    karta22=str(Jackpot[1])
    karta33=str(Jackpot[2])
    karta44=str(Jackpot[3])
    #print(final)
    #print(len(fucking))
    if final == "nothing":
        final = "Nothing"
    if final == "toopicky":
        final = "Too Picky"
    if final =="OOF":
        final = "OOF"
    if final =="death":
        final = "Death"
    if final =="fullflush":
        final = "Straight"
    if final =="full":
        final = "Four of a Kind"
    if final =="three":
        final = "Three of a Kind"
    if final =="two":
        final = "Two of a Kind"
    if final =="badluck":
        final = "Bad Luck"
    if final =="highcard":
        final = "High Card"
    if final =="sixqueens":
        final = "The Six Queens"
    if final =="WHAT":
        final = "???"

    amorgor=""
    for kula in counterer:
        amorgor += (str(kula)+";")
    with open(path.join(dir,"sources","counter"),"w") as porno:
        porno.write(amorgor)
    amorgor=""


    for kula in fucking:
        amorgor += (str(kula)+";")
    with open(path.join(dir,"sources","progress"),"w") as porno:
        porno.write(amorgor)
    print(Jackpot)
    print(final)
    fuckos = len(fucking)-len(fuckingreverse)
    fuckov = len(fucking)/2

    return render_template("gameresults.html",finalni = final,fuckovani = len(fucking),fuckovnice =fuckov ,carka="/",kount=len(counterer),karta1=karta11,karta2=karta22,karta3=karta33,karta4=karta44,zmenafucku = fuckos)
#_______________________________________________________________________________________________
#_______________________________________________________________________________________________
@app.route("/game2/rules")
def gamerules2():
    amorgor = "spust"
    return render_template("game2rules.html", buton = amorgor)
#_______________________________________________________________________________________________
@app.route("/game2/running")
def gamerunning2():
    x = random.randrange(1,10)
    return render_template("gameruning2.html",tohlechcu = x)
#_______________________________________________________________________________________________
@app.route("/game2/results")
def gameresults2():
    Jackpot=[]

    As = ["káryA" , "pikyA" , "srdceA" , "křížeA"]
    symbol= ["piky", "kříže", "káry", "srdce"]
    číslo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

    Balík= []
    Balík2 = []
    Jackpot=[]
    karta=[]

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

    if len(Jackpot)==1:
        Jackpot.append("0")
        Jackpot.append("0")
        Jackpot.append("0")
    elif len(Jackpot)==2:
        Jackpot.append("0")
        Jackpot.append("0")
    elif len(Jackpot)==3:
        Jackpot.append("0")
    elif len(Jackpot)==0:
        Jackpot.append("0")
        Jackpot.append("0")
        Jackpot.append("0")
        Jackpot.append("0")
    Jackpot=Jackpot[:4]

    check=[]
    for As in (Jackpot[:4]):
        if "A" in As:
            check.append("A")
    if len(check) == 4:
        final="WHAT"
    else:
        final="bigX"
    check=[]
    
    karta11=str(Jackpot[0])
    karta22=str(Jackpot[1])
    karta33=str(Jackpot[2])
    karta44=str(Jackpot[3])

        

    with open(path.join(dir,"sources","counter")) as negrum:
        amorgor=negrum.read()
    counterer=amorgor.split(";")
    counterer=counterer[:-1]
    amorgor=""
    counterer.append("I")
    
    amorgor=""
    for kula in counterer:
        amorgor += (str(kula)+";")
    with open(path.join(dir,"sources","counter"),"w") as porno:
        porno.write(amorgor)
    amorgor=""
    
    return render_template("gameresults2.html",finalni = final,carka="/",kount=len(counterer),karta1=karta11,karta2=karta22,karta3=karta33,karta4=karta44)
#_______________________________________________________________________________________________
#_______________________________________________________________________________________________
@app.route("/game3/rules")
def gamerules3():
    amorgor = "spust"
    return render_template(".html", buton = amorgor)
#_______________________________________________________________________________________________
@app.route("/game3/running")
def gamerunning3():
    x = random.randrange(1,10)
    return render_template(".html",tohlechcu = x)
#_______________________________________________________________________________________________
@app.route("/game3/results")
def gameresults3():
    with open(path.join(dir,"sources","progress")) as negrum:
        amorgor=negrum.read()
    fucking=amorgor.split(";")
    fucking=fucking[:-1]
    amorgor=""
    print(len(fucking))

    with open(path.join(dir,"sources","counter")) as negrum:
        amorgor=negrum.read()
    counterer=amorgor.split(";")
    counterer=counterer[:-1]
    amorgor=""
    counterer.append("I")

    with open(path.join(dir,"sources","triposobe")) as negrum:
        amorgor=negrum.read()
    posobecheck=amorgor.split(";")
    posobecheck=posobecheck[:-1]
    amorgor=""

    with open(path.join(dir,"sources","cernojecka")) as negrum:
        amorgor=negrum.read()
    blackJs=amorgor.split(";")
    blackJs=blackJs[:-1]
    amorgor=""

    with open(path.join(dir,"sources","impove")) as negrum:
        amorgor=negrum.read()
    Imps=amorgor.split(";")
    Imps=Imps[:-1]
    amorgor=""

    with open(path.join(dir,"sources","wolfe")) as negrum:
        amorgor=negrum.read()
    thewolf=amorgor.split(";")
    thewolf=thewolf[:-1]
    amorgor=""

    with open(path.join(dir,"sources","victorthesaviour")) as negrum:
        amorgor=negrum.read()
    saviour=amorgor.split(";")
    saviour=saviour[:-1]
    amorgor=""

 #-------------------------------------------------------------------------------   
    Balík= []
    Balík2 = []
    Jackpot=[]
    karta=[]
    counterer=[]
    
    if 200> len(fucking)>100:
        číslo = [8, 9, 10, "J", "Q", "K", "A"]
        symbol= ["piky", "kříže", "káry", "srdce","piky", "kříže", "káry", "srdce"]
    elif len(fucking)>200:
        číslo = ["J", "Q", "K", "A"]
        symbol= ["piky", "kříže", "káry", "srdce","piky", "kříže", "káry", "srdce"]
    elif len(fucking)>250:
        číslo = ["A"]
        symbol= ["piky", "kříže", "káry", "srdce","piky", "kříže", "káry", "srdce"]


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

    blaJ = ["black","J"]
    if len(blackJs)>0:
        for serio in range(100):
            Balík.append(blaJ)
            Balík2.append(blaJ)
        blackJs=[]

    Imp=["imp"]
    for ses in range(len(Imps)):
        Balík.append(Imp)
        Balík2.append(Imp)  

    wolf=["Wolf"]
    if len(thewolf)>0:
        Balík.append(wolf)
        Balík2.append(wolf) 

    savo=["saviour"]
    if len(saviour)>0:
        Balík.append(savo)
        Balík2.append(savo)  

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
        if cum > 3:
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
    Jackpot=Jackpot[:4]

    check=[]
    final="nothing"
    if Jackpot==[]:
        final="OOOF"

    #----conditions-----------------------------------------


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

    for Js in (Jackpot[:4]):
        if "J" in Js:
            check.append("J")
    if len(check) == 1:
        final="badluck"
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

    wolfcheck=[]
    for vlk in (Jackpot[:4]):
        if "Wolf" in vlk:
            wolfcheck.append("W")
    if len(wolfcheck)>0:
        final="theWOLF"
        thewolf=[]

    wolfcheck=[]
    for vlk in (Jackpot[:4]):
        if "saviour" in vlk:
            wolfcheck.append("W")
    if len(wolfcheck)>0:
        final="saviour"
        saviour=[]

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

    if len(counterer)%15==0:
        muhaha=random.randrange(4)
        if muhaha==3:
            final="sixqueens"
        else:
            pass


    #-------------next-------------------



    if final== "sixqueens":
        if len(fucking)<150:
            posobecheck=[]
        rollin = random.randrange(20)
        if rollin < 4:
            final="SIXQUEENS:TheStalker"
            thewolf.append("wolf")
        elif 4<=rollin<8:
            final="SIXQUEENS:TheImpmageddon"
            for sxs in range(20):
                Imps.append(Imp)
        elif 8<=rollin<12:
            final="SIXQUEENS:CurseofRa"
            blackJs.append("BJ")
        elif 12<=rollin<16:
            final="SIXQUEENS:TheSaviour"
            saviour.append("victor")
        elif 16<=rollin<18:
            final="SIXQUEENS:death"
        elif rollin ==20:
            final="SIXQUEENS:fullflush"
        else:
            final="SIXQUEENS:full"


    if final == "highcard":
        if len(fucking)<150:
            posobecheck=[]
        if len(fucking)>=300:
            for sos in range(20):
                fucking.pop(-1)
        else:
            for sos in range(10):
                fucking.append("I")

    if final == "badluck":
        if len(fucking)<150:
            posobecheck=[]
        if len(fucking)<150:
            if len(fucking)>40:
                fucking = fucking[:len(fucking)-40]
            else:
                for sos in range(len(fucking)):
                    fucking.pop(-1)
        else:
            for sos in range(60):
                    fucking.pop(-1)


    if final == "two":
        if posobecheck==["2"] or posobecheck==[]:
            for sos in range(30):
                fucking.append("I")
            posobecheck.append("2")
        elif "2" not in posobecheck and len(posobecheck)>0:
            for sos in range(30):
                fucking.append("I")
            posobecheck=[]
            posobecheck.append("2") 
        elif posobecheck==["2","2"]:
            final="toorepetetive"
            if len(fucking)>=40:
                for sos in range(60):
                    fucking.pop(-1)
            else:
                for sos in range(len(fucking)):
                    fucking.pop(-1)
            posobecheck=[]

    if final == "three":
        if posobecheck==["3"] or posobecheck==[]:
            for sos in range(35):
                fucking.append("I")
            posobecheck.append("3")
        elif "3" not in posobecheck and len(posobecheck)>0:
            for sos in range(35):
                fucking.append("I")
            posobecheck=[]
            posobecheck.append("3")
        elif posobecheck==["3","3"]:
            final="toorepetetive"
            if len(fucking)>=50:
                for sos in range(70):
                    fucking.pop(-1)
            else:
                for sos in range(len(fucking)):
                    fucking.pop(-1)
            posobecheck=[]

    if final == "full" or final=="SIXQUEENS:full":
        if posobecheck==["4"] or posobecheck==[]:
            for sos in range(45):
                fucking.append("I")
            posobecheck.append("4")
        elif "4" not in posobecheck and len(posobecheck)>0:
            for sos in range(45):
                fucking.append("I")
            posobecheck=[]
            posobecheck.append("4")
        elif posobecheck==["4","4"]:
            final="toorepetetive"
            if len(fucking)>=60:
                for sos in range(90):
                    fucking.pop(-1)
            else:
                for sos in range(len(fucking)):
                    fucking.pop(-1)
            posobecheck=[]

    if final == "fullflush" or final=="SIXQUEENS:fullflush":
        if len(fucking)<150:
            posobecheck=[]
        for sos in range(75):
            fucking.append("I")

    if final == "death" or final=="SIXQUEENS:death":
        if len(fucking)<150:
            posobecheck=[]
        for sos in range(len(fucking)):
            fucking.pop(-1)

    if final == "OOOF":
        if len(fucking)<150:
            posobecheck=[]
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
        if len(fucking)>120:
            for kjhg in range(2):
                Imps.append(Imp)
        if len(fucking)<150:
            posobecheck=[]
        if 51>len(fucking)>24:
            for sos in range(10):
                fucking.append("I")
            for kkot in range(len(Jackpot)):
                for sexus in range(5):
                    fucking.append("I")
        elif len(fucking)<25:
            for sos in range(5):
                fucking.append("I")
            for kkot in range(len(Jackpot)):
                for sexus in range(5):
                    fucking.append("I")
        elif 100>len(fucking)>50:
            pass
        elif len(fucking)>175:
            for sos in range(5):
                fucking.pop(-1)
        elif len(fucking)>100 and "piky" in Jackpot and "srdce" in Jackpot and "kříže" in Jackpot and "káry" in Jackpot:
            final="toopicky"
            for sos in range(100):
                fucking.pop(-1)


    checkusimpus=[]
    for impáci in (Jackpot[:4]):
        if "imp" in impáci:
            checkusimpus.append("impus")
    for sulivahn in range(len(checkusimpus)):
        Imps.pop(-1)
        if len(fucking)>=5:
            for i in range(5):
                fucking.pop(-1)
        else:
            for kkl in range(len(fucking)):
                fucking.pop(-1)       
    if len(checkusimpus)==4:
        final="impeyes"
        if len(fucking)>=40:
            for kkl in range(40):
                fucking.pop(-1)
        else:
            for kkl in range(len(fucking)):
                fucking.pop(-1)

    if final=="theWOLF":
            for kkl in range(len(fucking)/2):
                fucking.pop(-1) 

    if final=="saviour":
            for kkl in range(len(fucking)):
                fucking.append("I") 
    checkusimpus=[]


    if final =="WHAT":
        BIGWIN=1
    amorgor=""
    for kula in counterer:
        amorgor += (str(kula)+";")
    with open(path.join(dir,"sources","counter"),"w") as porno:
        porno.write(amorgor)
    amorgor=""

    for kula in fucking:
        amorgor += (str(kula)+";")
    with open(path.join(dir,"sources","progress"),"w") as porno:
        porno.write(amorgor)

    amorgor=""
    for kula in posobecheck:
        amorgor += (str(kula)+";")
    with open(path.join(dir,"sources","triposobe"),"w") as porno:
        porno.write(amorgor)
    amorgor=""

    amorgor=""
    for kula in blackJs:
        amorgor += (str(kula)+";")
    with open(path.join(dir,"sources","cernojecka"),"w") as porno:
        porno.write(amorgor)
    amorgor=""

    amorgor=""
    for kula in Imps:
        amorgor += (str(kula)+";")
    with open(path.join(dir,"sources","impove"),"w") as porno:
        porno.write(amorgor)
    amorgor=""

    amorgor=""
    for kula in thewolf:
        amorgor += (str(kula)+";")
    with open(path.join(dir,"sources","wolfe"),"w") as porno:
        porno.write(amorgor)
    amorgor=""

    amorgor=""
    for kula in saviour:
        amorgor += (str(kula)+";")
    with open(path.join(dir,"sources","victorthesaviour"),"w") as porno:
        porno.write(amorgor)
    amorgor=""
    
    karta11=str(Jackpot[0])
    karta22=str(Jackpot[1])
    karta33=str(Jackpot[2])
    karta44=str(Jackpot[3])
    
    return render_template(".html",finalni = final,fuckovani = len(fucking),carka="/",kount=len(counterer),karta1=karta11,karta2=karta22,karta3=karta33,karta4=karta44)


if __name__ == "__main__":
    app.run(debug=True)
#"<img src=C:\\Users\\Jonatán\\Documents\\školní nesmysly\\sová nožka\\chechboard.png, width="2000", height="2500""
# <img src="{{ url_for('static', filename='chechboard.png') }}" width="200" height="267" alt="me">{{tohlechcu}}