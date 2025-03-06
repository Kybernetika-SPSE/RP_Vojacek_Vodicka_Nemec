import random
from os import path
dir = path.dirname(__file__)
from flask import Flask, render_template, render_template_string, request, session, redirect, url_for, g
import json

app = Flask(__name__)
#session["data"]["roll"] = 0
#session["data"]["body"] = 0
#session["data"]["savio"]=0
#session["data"]["wolfo"]=0
#session["data"]["impo"]=0
#session["data"]["blackj"]=0
#session["data"]["posobecheck"]=[]

app.config["DEFAULT_DATA"] = {
    "roll": 0,
    "body": 0,
    "savio": 0,
    "wolfo": 0,
    "impo": 0,
    "blackj": 0,
    "posobecheck": []
}
try:
    with open(path.join(dir,"MEGA_SECRET_HYPER_PASSWORD")) as securiti:
        app.secret_key = securiti.read().strip()
except:
    print("Kliuč voe, pokud nevíš, jak se ti tohle vůbec povedlo???")
    exit()

@app.before_request
def setup():
    if "data" not in session:
        session["data"] = app.config["DEFAULT_DATA"].copy()
        print("koulesex")

@app.route("/")
def main():
    session["name"] = str(random.randrange(1,40))
    session["data"]["roll"] = 0
    session["data"]["body"] = 0
    session["data"]["savio"]=0
    session["data"]["wolfo"]=0
    session["data"]["impo"]=0
    session["data"]["blackj"]=0
    session["data"]["posobecheck"]=[]
    session.modified = True

    return render_template("Welcome.html")


#_______________________________________________________________________________________________
@app.route("/game1/rules")
def gamerules1():
    return render_template("game1rules.html")
#_______________________________________________________________________________________________
@app.route("/game1/running")
def gamerunning1():
    #-----FVTXT2----------------------------------------------------

    fvtxt2 = "Zkouška Zkouška"
    symbol= ["piky", "kříže", "káry", "srdce"]
    číslo = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]


    balík1= []
    balík2 = []
    balík3 = []
    balík4 = []
    karta=[]

    #____________________________________________________
    counterer = session["data"]["roll"]
    counterer = counterer + 1

    kapr = session["data"]["body"]
    #_________________________________________________

    if 200> kapr>100:
        číslo = [8, 9, 10, "J", "Q", "K", "A"]
        symbol= ["piky", "kříže", "káry", "srdce","piky", "kříže", "káry", "srdce"]
    elif kapr>200:
        číslo = ["A"]
        symbol= ["piky", "kříže", "káry", "srdce","piky", "kříže", "káry", "srdce","piky", "kříže", "káry", "srdce"]


    for l in range(len(symbol)):
        karta=[]   
        karta.append(str(symbol[l]))
        if karta==["srdce"]:
            for z in range(len(číslo)):
                karta = ["srdce"]
                karta.append(str(číslo[z]))
                karta = str(karta) + ".png"
                karta = karta.replace("'","")      
                balík1.append(karta)
                balík2.append(karta)
                balík3.append(karta)
                balík4.append(karta)
        if karta==["káry"]:
            for z in range(len(číslo)):
                karta = ["káry"]
                karta.append(str(číslo[z]))
                karta = str(karta) + ".png"
                karta = karta.replace("'","")         
                balík1.append(karta)
                balík2.append(karta)
                balík3.append(karta)
                balík4.append(karta)
        if karta==["kříže"]:
            for z in range(len(číslo)):
                karta = ["kříže"]
                karta.append(str(číslo[z]))
                karta = str(karta) + ".png"
                karta = karta.replace("'","")        
                balík1.append(karta)
                balík2.append(karta)
                balík3.append(karta)
                balík4.append(karta)
        if karta==["piky"]:
            for z in range(len(číslo)):
                karta = ["piky"]
                karta.append(str(číslo[z]))
                karta = str(karta) + ".png"
                karta = karta.replace("'","")        
                balík1.append(karta)
                balík2.append(karta)
                balík3.append(karta)
                balík4.append(karta)

    random.shuffle(balík1)
    random.shuffle(balík2)
    random.shuffle(balík3)
    random.shuffle(balík4)


    #---------------------------------------------------------------
    return render_template("game1running.html", flavourtext2 = fvtxt2, balák1 = balík1, balák2 = balík2, balák3 = balík3, balák4 = balík4 )
#_______________________________________________________________________________________________
@app.route("/game1/results")
def gameresults1():
    print(session["name"])
    Jackpot=[]
    symbol= ["piky", "kříže", "káry", "srdce"]
    číslo = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]


    Balík= []
    Balík2 = []
    Jackpot=[]
    karta=[]

    #____________________________________________________

    counterer = session["data"]["roll"]
    counterer = counterer + 1

    kapr = session["data"]["body"]
    jauznevim = kapr
    #_________________________________________________

    if 200> kapr>100:
        číslo = [8, 9, 10, "J", "Q", "K", "A"]
        symbol= ["piky", "kříže", "káry", "srdce","piky", "kříže", "káry", "srdce"]
    elif kapr>200:
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


    for chicken in range(len(symbol)*len(číslo)):
        if Balík[chicken] == Balík2[chicken]:
            Jackpot.append(Balík[chicken])


    #--------------dolízávando---------------------------
    come = random.randrange(1,11)

    if len(Jackpot) ==1 or len(Jackpot) ==2:
        if come > 2:
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
        elif come > 1:
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
        if come > 5:
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
    final="nothing"
    if Jackpot==[]:
        final="OOOF"

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
        if kapr>=220:
            kapr = kapr - 20
        else:
            kapr = kapr+10
    elif final == "badluck":
        kapr -= 40
    elif final == "two":
        kapr+=15
    elif final == "three":
        kapr+=20
    elif final == "full":
        kapr+=25
    elif final == "fullflush":
        kapr +=30
    elif final == "death":
        kapr=0
    elif final == "OOOF":
        if 100>kapr>35:
            kapr -= 10
        elif kapr>100:
            kapr -= 20
        else:
            pass    
    elif final =="nothing":
        if 51>kapr>24:
            kapr-=10
        elif kapr<25:
            kapr-=5
        elif 100>kapr>50:
            pass
        elif kapr>100:
            kapr-=5
        elif kapr>100 and "piky" in Jackpot and "srdce" in Jackpot and "kříže" in Jackpot and "káry" in Jackpot:
            final="toopicky"
            kapr-=100

    #-----------------aux-----------------------------

    karta11=str(Jackpot[0]) + ".png"
    karta22=str(Jackpot[1]) + ".png"
    karta33=str(Jackpot[2]) + ".png"
    karta44=str(Jackpot[3]) + ".png"

    karta11 = karta11.replace("'","")
    karta22 = karta22.replace("'","")
    karta33 = karta33.replace("'","")
    karta44 = karta44.replace("'","")
    #print(final)
    #print(kapr)
    if final == "nothing":
        final = "Nothing"
    if final == "toopicky":
        final = "Too Picky"
    if final =="OOOF":
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
    
    if kapr<0:
        kapr=0
    opakuj = kapr - jauznevim
    nerozumim = kapr/2


    #------------FVTXT1-----------------------------------------------
    numero = random.randrange(1,30)
    r1 = random.randrange(1,9)
    r2 = random.randrange(1,5)
    if final == "Nothing":
        if r1 ==1:
            fvtxt1 = "Nechceš něco rollnout??"
        elif r1 ==2:
            fvtxt1 = "Timhle tempem to nikdy nedohraješ"
        elif r1 ==3:
            fvtxt1 = "Nuuudaaa"
        elif r1 ==4:
            fvtxt1 = "Víš že od určitýho bodu ti to bere body že?"
        elif r1 ==5:
            fvtxt1 = "Nic..."
        elif r1 ==6:
            fvtxt1 = "Nope"
        elif r1 ==7:
            fvtxt1 = "Nuh Uh"
        elif r1 ==8:
            fvtxt1 = "Hodláš tohle dělat často?" 
        else:
            fvtxt1 = "nedostatek sýra v sektoru 3"     
    elif final =="OOF":
        if r2 == 1:
            fvtxt1 = "OOF"
        elif r2 == 2:
            fvtxt1 = "AJAJAJJ"
        elif r2 == 3:
            fvtxt1 = "Tohle ovšem... je smůla"
        elif r2 == 4:
            fvtxt1 = "UUUF... Nádhera"
        else:
            fvtxt1 = "nedostatek sýra v sektoru 3"
    elif final == "Death":
        if r2 > 2:
            fvtxt1 = "Víš vůbec jak MALOU šanci tohle má?"
        else:
            fvtxt1 = "Tohle je stejně vzácný jako výhra BTW"
    elif final == "Straight":
        fvtxt1 = "Tak tohle jsem snad v životě neviděl"
    elif final =="Four of a Kind":
        if r1 == 1:
            fvtxt1 = "Slušný"
        elif r1 == 2:
            fvtxt1 = "Pěkný"
        elif r1 == 3:
            fvtxt1 = "Hele, možná to i někam dotáhneš"
        elif r1 == 4:
            fvtxt1 = "Možná..."
        elif r1 == 5:
            fvtxt1 = "No moment!"
        elif r1 == 6:
            fvtxt1 = "Žádná cesta ono to dostává body!"
        elif r1 == 7:
            fvtxt1 = "Jako jarní vánek... Co to znamená? Jak to mam vědět"
        elif r1 == 8:
            fvtxt1 = "No dobrá, vem si ty svoje Drobný"
        else:
            fvtxt1 = "nedostatek sýra v sektoru 3"
    elif final =="Three of a Kind":
        if r1 == 1:
            fvtxt1 = "Slušný"
        elif r1 == 2:
            fvtxt1 = "Pěkný"
        elif r1 == 3:
            fvtxt1 = "Hele, možná to i někam dotáhneš"
        elif r1 == 4:
            fvtxt1 = "Možná..."
        elif r1 == 5:
            fvtxt1 = "No moment!"
        elif r1 == 6:
            fvtxt1 = "Žádná cesta ono to dostává body!"
        elif r1 == 7:
            fvtxt1 = "Jako jarní vánek... Co to znamená? Jak to mam vědět"
        elif r1 == 8:
            fvtxt1 = "No dobrá, vem si ty svoje Drobný"
        else:
            fvtxt1 = "nedostatek sýra v sektoru 3"
    elif final =="Two of a Kind" :
        if r1 == 1:
            fvtxt1 = "Slušný"
        elif r1 == 2:
            fvtxt1 = "Pěkný"
        elif r1 == 3:
            fvtxt1 = "Hele, možná to i někam dotáhneš"
        elif r1 == 4:
            fvtxt1 = "Možná..."
        elif r1 == 5:
            fvtxt1 = "No moment!"
        elif r1 == 6:
            fvtxt1 = "Žádná cesta ono to dostává body!"
        elif r1 == 7:
            fvtxt1 = "Jako jarní vánek... Co to znamená? Jak to mam vědět"
        elif r1 == 8:
            fvtxt1 = "No dobrá, vem si ty svoje Drobný"
        else:
            fvtxt1 = "nedostatek sýra v sektoru 3"
    elif final == "Bad Luck":
        if r1 == 1 or 2:
            fvtxt1 = "Zpátky dolů"
        elif r1 == 3:
            fvtxt1 = "*Zlověstný smích*"
        elif r1 == 4 or 5:
            fvtxt1 = "Jak se píše slovo: Loser?"
        elif r1 == 6:
            fvtxt1 = "Žer Jengla"
        elif r1 == 7 or 8:
            fvtxt1 = "The joke's on YOU"
        else:
            fvtxt1 = "nedostatek sýra v sektoru 3"
    elif final =="High Card":
        if kapr < 220:
            if r1 == 1:
                fvtxt1 = "Alespoň ňeco"
            elif r1 == 2:
                fvtxt1 = "Snaž se trochu"
            elif r1 == 3:
                fvtxt1 = "Samozřejmě Skill Based"
            elif r1 == 4:
                fvtxt1 = "I to se počítá"
            elif r1 == 5:
                fvtxt1 = "Už zase?"
            elif r1 == 6:
                fvtxt1 = "Nebylo tu tohle před chvílí?"
            elif r1 == 7:
                fvtxt1 = "-sample text-"
            elif r1 == 8:
                fvtxt1 = "Už mi dochází nápady"
            else:
                fvtxt1 = "nedostatek sýra v sektoru 3"
        else:
            if r2 == 1:
                fvtxt1 = "Takhle,    ,Blízko"
            elif r2 == 2:
                fvtxt1 = "Už to bude"
            elif r2 == 3:
                fvtxt1 = "Dont give up, skeleton!"
            elif r2 == 4:
                fvtxt1 = "Vždyť už jsou to JENOM Ačka"
            else:
                fvtxt1 = "nedostatek sýra v sektoru 3"
    elif final == "The Six Queens":
        fvtxt1 = "DAMN IT! SIX QUEENS"
    elif final == "???":
        fvtxt1 = "DING DING DING"
    elif final =="Too Picky":
        fvtxt1 = "Too Picky neexistuje"
    elif random.randrange(1,81) == 42:
        if r2 == 1:
            fvtxt1 = "What are we? Some kind of... League of Legends?"
        elif r2 == 2:
            fvtxt1 = "Možná tou skutečnou výhrou jsou ti přátelé..."
        elif r2 == 3:
            fvtxt1 = "...které jsme si udělali cestou"
        elif r2 == 4:
            fvtxt1 = "Anime tiddies"
        else:
            fvtxt1 = "nedostatek sýra v sektoru 3"
    else:
        if r2 == 1:
            fvtxt1 = "Napoleon Napoleon Napoleon"
        elif r2 == 2:
            fvtxt1 = "+++Press Reset+++"
        elif r2 == 3:
            fvtxt1 = "Koupili jsme rohožku "
        elif r2 == 4:
            fvtxt1 = "Myš"
    #----------------------------------------------------------------

    session["data"]["body"] = kapr
    session.modified = True
    session["data"]["roll"] = counterer
    session.modified = True

    return render_template("game1results.html",finalni = final,fidlovacka = kapr,brokovnice =nerozumim,kount=counterer,karta1=karta11,karta2=karta22,karta3=karta33,karta4=karta44,zmena = opakuj, flavourtext1 = fvtxt1)
#_______________________________________________________________________________________________
#_______________________________________________________________________________________________
@app.route("/game2/rules")
def gamerules2():
    return render_template("game2rules.html",)
#_______________________________________________________________________________________________
@app.route("/game2/running")
def gamerunning2():
    fvtxt2 = "Zkouška Zkouška"
    symbol= ["piky", "kříže", "káry", "srdce"]
    číslo = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]


    balík1= []
    balík2 = []
    balík3 = []
    balík4 = []
    karta=[]

    #____________________________________________________

    for l in range(len(symbol)):
        karta=[]   
        karta.append(str(symbol[l]))
        if karta==["srdce"]:
            for z in range(len(číslo)):
                karta = ["srdce"]
                karta.append(str(číslo[z]))
                karta = str(karta) + ".png"
                karta = karta.replace("'","")      
                balík1.append(karta)
                balík2.append(karta)
                balík3.append(karta)
                balík4.append(karta)
        if karta==["káry"]:
            for z in range(len(číslo)):
                karta = ["káry"]
                karta.append(str(číslo[z]))
                karta = str(karta) + ".png"
                karta = karta.replace("'","")         
                balík1.append(karta)
                balík2.append(karta)
                balík3.append(karta)
                balík4.append(karta)
        if karta==["kříže"]:
            for z in range(len(číslo)):
                karta = ["kříže"]
                karta.append(str(číslo[z]))
                karta = str(karta) + ".png"
                karta = karta.replace("'","")        
                balík1.append(karta)
                balík2.append(karta)
                balík3.append(karta)
                balík4.append(karta)
        if karta==["piky"]:
            for z in range(len(číslo)):
                karta = ["piky"]
                karta.append(str(číslo[z]))
                karta = str(karta) + ".png"
                karta = karta.replace("'","")        
                balík1.append(karta)
                balík2.append(karta)
                balík3.append(karta)
                balík4.append(karta)

    random.shuffle(balík1)
    random.shuffle(balík2)
    random.shuffle(balík3)
    random.shuffle(balík4)
    
    return render_template("game2running.html",flavourtext2 = fvtxt2, balák1 = balík1, balák2 = balík2, balák3 = balík3, balák4 = balík4 )
#_______________________________________________________________________________________________
@app.route("/game2/results")
def gameresults2():
    Jackpot=[]

    As = ["káryA" , "pikyA" , "srdceA" , "křížeA"]
    symbol= ["piky", "kříže", "káry", "srdce"]
    číslo = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

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


    for chicken in range(len(symbol)*len(číslo)):
        if Balík[chicken] == Balík2[chicken]:
            Jackpot.append(Balík[chicken])

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
    
#-----------------aux-----------------------------

    karta11=str(Jackpot[0]) + ".png"
    karta22=str(Jackpot[1]) + ".png"
    karta33=str(Jackpot[2]) + ".png"
    karta44=str(Jackpot[3]) + ".png"

    karta11 = karta11.replace("'","")
    karta22 = karta22.replace("'","")
    karta33 = karta33.replace("'","")
    karta44 = karta44.replace("'","")
    #print(final)
    #print(kapr)

    if final == "nothing":
        final = "Nuh Uh"
    if final == "toopicky":
        final = "Nuh Uh"
    if final =="OOF":
        final = "Nuh Uh"
    if final =="death":
        final = "Nuh Uh"
    if final =="fullflush":
        final = "Nuh Uh"
    if final =="full":
        final = "Nuh Uh"
    if final =="three":
        final = "Nuh Uh"
    if final =="two":
        final = "Nuh Uh"
    if final =="badluck":
        final = "Nuh Uh"
    if final =="highcard":
        final = "Nuh Uh"
    if final =="sixqueens":
        final = "Nuh Uh"
    if final =="WHAT":
        final = "???"
    if final == "bigX":
        final = "Nuh uh"

#----------------------------------------------------------------
    counterer = session["data"]["roll"]
    counterer = counterer + 1
    session["data"]["roll"]=counterer
    session.modified = True
    
    return render_template("game2results.html",finalni = final,kount=counterer,karta1=karta11,karta2=karta22,karta3=karta33,karta4=karta44)
#_______________________________________________________________________________________________
#_______________________________________________________________________________________________
@app.route("/game3/rules")
def gamerules3():
    return render_template("game3rules.html",)
#_______________________________________________________________________________________________
@app.route("/game3/running")
def gamerunning3():
    kapr = session["data"]["body"]
    saviour = session["data"]["savio"]
    thewolf = session["data"]["wolfo"]
    Imps = session["data"]["impo"]
    blackJs = session["data"]["blackj"]

 #-------------------------------------------------------------------------------   
    Balík= []
    Balík2 = []
    Balík3 = []
    Balík4 = []
    karta=[]

    symbol= ["piky", "kříže", "káry", "srdce"]
    číslo = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    
    if 200> kapr>100:
        číslo = [8, 9, 10, "J", "Q", "K", "A"]
        symbol= ["piky", "kříže", "káry", "srdce","piky", "kříže", "káry", "srdce"]
    elif kapr>200:
        číslo = ["J", "Q", "K", "A"]
        symbol= ["piky", "kříže", "káry", "srdce","piky", "kříže", "káry", "srdce"]
    elif kapr>250:
        číslo = ["A"]
        symbol= ["piky", "kříže", "káry", "srdce","piky", "kříže", "káry", "srdce"]


    for l in range(len(symbol)):
        karta=[]   
        karta.append(str(symbol[l]))
        if karta==["srdce"]:
            for z in range(len(číslo)):
                karta = ["srdce"]
                karta.append(str(číslo[z]))
                karta = str(karta) + ".png"
                karta = karta.replace("'","")        
                Balík.append(karta)
                Balík2.append(karta)
                Balík3.append(karta)
                Balík4.append(karta)
        if karta==["káry"]:
            for z in range(len(číslo)):
                karta = ["káry"]
                karta.append(str(číslo[z]))
                karta = str(karta) + ".png"
                karta = karta.replace("'","")        
                Balík.append(karta)
                Balík2.append(karta)
                Balík3.append(karta)
                Balík4.append(karta)
        if karta==["kříže"]:
            for z in range(len(číslo)):
                karta = ["kříže"]
                karta.append(str(číslo[z]))
                karta = str(karta) + ".png"
                karta = karta.replace("'","")        
                Balík.append(karta)
                Balík2.append(karta)
                Balík3.append(karta)
                Balík4.append(karta)
        if karta==["piky"]:
            for z in range(len(číslo)):
                karta = ["piky"]
                karta.append(str(číslo[z]))
                karta = str(karta) + ".png"
                karta = karta.replace("'","")        
                Balík.append(karta)
                Balík2.append(karta)
                Balík3.append(karta)
                Balík4.append(karta)

    blaJ = ["black","J"]
    if blackJs==1:
        for serio in range(100):
            Balík.append(blaJ)
            Balík2.append(blaJ)
            Balík3.append(blaJ)
            Balík4.append(blaJ)
        blackJs=0

    Imp=["imp"]
    for ses in range(Imps):
        Balík.append(Imp)
        Balík2.append(Imp)
        Balík3.append(Imp)
        Balík4.append(Imp)  

    wolf=["Wolf"]
    if thewolf==1:
        Balík.append(wolf)
        Balík2.append(wolf)
        Balík3.append(wolf)
        Balík4.append(wolf)
        thewolf=0 

    savo=["saviour"]
    if saviour==1:
        Balík.append(savo)
        Balík2.append(savo)
        Balík3.append(savo)
        Balík4.append(savo)
        saviour=0  

    random.shuffle(Balík4)
    random.shuffle(Balík3)
    random.shuffle(Balík2)
    random.shuffle(Balík)

    return render_template("game3running.html",balák1 = Balík, balák2 = Balík2, balák3 = Balík3, balák4 = Balík4)
#_______________________________________________________________________________________________
@app.route("/game3/results")
def gameresults3():
    counterer = session["data"]["roll"]
    kapr = session["data"]["body"]
    saviour = session["data"]["savio"]
    thewolf = session["data"]["wolfo"]
    Imps = session["data"]["impo"]
    blackJs = session["data"]["blackj"]
    posobecheck = session["data"]["posobecheck"]
    counterer +=1

 #-------------------------------------------------------------------------------   
    Balík= []
    Balík2 = []
    Jackpot=[]
    karta=[]
    jauznevim = kapr

    symbol= ["piky", "kříže", "káry", "srdce"]
    číslo = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    
    if 200> kapr>100:
        číslo = [8, 9, 10, "J", "Q", "K", "A"]
        symbol= ["piky", "kříže", "káry", "srdce","piky", "kříže", "káry", "srdce"]
    elif kapr>200:
        číslo = ["J", "Q", "K", "A"]
        symbol= ["piky", "kříže", "káry", "srdce","piky", "kříže", "káry", "srdce"]
    elif kapr>250:
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
    if blackJs==1:
        for serio in range(100):
            Balík.append(blaJ)
            Balík2.append(blaJ)
        blackJs=0

    Imp=["imp"]
    for ses in range(Imps):
        Balík.append(Imp)
        Balík2.append(Imp)  

    wolf=["Wolf"]
    if thewolf==1:
        Balík.append(wolf)
        Balík2.append(wolf) 

    savo=["saviour"]
    if saviour==1:
        Balík.append(savo)
        Balík2.append(savo)  

    random.shuffle(Balík2)
    random.shuffle(Balík)


    for chicken in range(len(symbol)*len(číslo)):
        if Balík[chicken] == Balík2[chicken]:
            Jackpot.append(Balík[chicken])


    #--------------dolízávando---------------------------
    come = random.randrange(1,11)

    if len(Jackpot) ==1 or len(Jackpot) ==2:
        if come > 2:
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
        elif come > 1:
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
        if come > 3:
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
    final="nothing"
    if Jackpot==[]:
        final="OOOF"
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
        thewolf=0

    wolfcheck=[]
    for vlk in (Jackpot[:4]):
        if "saviour" in vlk:
            wolfcheck.append("W")
    if len(wolfcheck)>0:
        final="saviour"
        saviour=0

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

    if counterer%15==0:
        muhaha=random.randrange(4)
        if muhaha==3:
            final="sixqueens"
            Jackpot = Jackpot[:-3]
            zymboli = ["piky", "kříže", "káry", "srdce"]
            for i in range(3):
                sss = random.randrange(len(zymboli))
                krata = []
                krata.append(zymboli[sss])
                krata.append("Q")
                Jackpot.append(krata)
            random.shuffle(Jackpot)
        else:
            pass


    #-------------next-------------------



    if final== "sixqueens":
        if kapr<150:
            posobecheck=[]
        rollin = random.randrange(20)
        if rollin < 4:
            final="SIXQUEENS:TheStalker"
            thewolf = 1
        elif 4<=rollin<8:
            final="SIXQUEENS:TheImpmageddon"
            Imps +=20
        elif 8<=rollin<12:
            final="SIXQUEENS:CurseofRa"
            blackJs = 1
        elif 12<=rollin<16:
            final="SIXQUEENS:TheSaviour"
            saviour = 1
        elif 16<=rollin<18:
            final="SIXQUEENS:death"
        elif rollin ==20:
            final="SIXQUEENS:fullflush"
        else:
            final="SIXQUEENS:full"
    elif final == "highcard":
        if kapr<150:
            posobecheck=[]
        if kapr>=300:
            kapr-=20
        else:
            kapr+=10
    elif final == "badluck":
        if kapr<150:
            posobecheck=[]
        if kapr<150:
            kapr-=40
        #else:
            #kapr-=60
    elif final == "two":
        if posobecheck==["2"] or posobecheck==[]:
            kapr+=30
            posobecheck.append("2")
        elif "2" not in posobecheck and len(posobecheck)>0:
            kapr+=30
            posobecheck=[]
            posobecheck.append("2") 
        elif posobecheck==["2","2"]:
            final="toorepetetive"
            kapr -=60
            posobecheck=[]
    elif final == "three":
        if posobecheck==["3"] or posobecheck==[]:
            kapr+=35
            posobecheck.append("3")
        elif "3" not in posobecheck and len(posobecheck)>0:
            kapr+=35
            posobecheck=[]
            posobecheck.append("3")
        elif posobecheck==["3","3"]:
            final="toorepetetive"
            kapr-=70
            posobecheck=[]
    elif final == "full" or final=="SIXQUEENS:full":
        if posobecheck==["4"] or posobecheck==[]:
            kapr+=45
            posobecheck.append("4")
        elif "4" not in posobecheck and len(posobecheck)>0:
            kapr+=45
            posobecheck=[]
            posobecheck.append("4")
        elif posobecheck==["4","4"]:
            final="toorepetetive"
            kapr-=90
            posobecheck=[]
    elif final == "fullflush" or final=="SIXQUEENS:fullflush":
        if kapr<150:
            posobecheck=[]
        kapr+=75
    elif final == "death" or final=="SIXQUEENS:death":
        if kapr<150:
            posobecheck=[]
        kapr = 0
    elif final == "OOOF":
        if kapr<150:
            posobecheck=[]
        if 100>kapr>35:
            kapr-=10
        if kapr>100:
            kapr-=20
        else:
            pass
    elif final =="nothing":
        if kapr>120:
            for kjhg in range(2):
                Imps.append(Imp)
        if kapr<150:
            posobecheck=[]
        if 51>kapr>24:
            kapr +=10
            for kkot in range(len(Jackpot)):
                for sexus in range(5):
                    kapr -=1
        elif kapr<25:
            kapr +=5
            for kkot in range(len(Jackpot)):
                for sexus in range(5):
                    kapr +=1
        elif 100>kapr>50:
            pass
        elif kapr>175:
            kapr-=5
        elif kapr>100 and "piky" in Jackpot and "srdce" in Jackpot and "kříže" in Jackpot and "káry" in Jackpot:
            final="toopicky"
            kapr-=100

    checkusimpus=[]
    for impáci in (Jackpot[:4]):
        if "imp" in impáci:
            checkusimpus.append("impus")
    for sulivahn in range(len(checkusimpus)):
        Imps-=1
        kapr -=5       
    if len(checkusimpus)==4:
        final="impeyes"
        kapr -=40

    if final=="theWOLF":
            kapr = kapr/2

    if final=="saviour":
            kapr = kapr*2 
    checkusimpus=[]


    session["data"]["roll"] = counterer
    session.modified = True
    session["data"]["body"] = kapr
    session.modified = True
    session["data"]["savio"] = saviour
    session.modified = True
    session["data"]["wolfo"] = thewolf
    session.modified = True
    session["data"]["impo"] = Imps
    session.modified = True
    session["data"]["blackj"] = blackJs
    session.modified = True
    session["data"]["posobecheck"] = posobecheck
    session.modified = True

#--------------aux------------------------------

    karta11=str(Jackpot[0]) + ".png"
    karta22=str(Jackpot[1]) + ".png"
    karta33=str(Jackpot[2]) + ".png"
    karta44=str(Jackpot[3]) + ".png"

    karta11 = karta11.replace("'","")
    karta22 = karta22.replace("'","")
    karta33 = karta33.replace("'","")
    karta44 = karta44.replace("'","")

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
    if final =="impeyes":
        final = "ImpEyes"
    if final =="theWOLF":
        final = "TheWOLF"
    if final =="saviour":
        final = "TheSAVIOR"
    if final == "toopicky":
        final = "TooPicky"
    if final =="toorepetetive":
        final = "Too Repetetive"

    if kapr<0:
        kapr=0
    opakuj = kapr - jauznevim
    nerozumim = kapr/2.5

#--------------------------------------------------------------------
    
    return render_template("game3results.html",finalni = final,fidlovacka = kapr,brokovnice =nerozumim,kount=counterer,karta1=karta11,karta2=karta22,karta3=karta33,karta4=karta44,zmena = opakuj)


if __name__ == "__main__":
    app.run(debug=True)