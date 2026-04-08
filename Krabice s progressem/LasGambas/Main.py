
import random
from os import path
from flask import Flask, render_template, render_template_string, request, session, redirect, url_for, g, jsonify, flash
import json
import uuid
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import re

dir = path.dirname(__file__)
app = Flask(__name__)


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
    "maxus": 0,
    "savio": 0,
    "wolfo": 0,
    "impo": 0,
    "blackj": 0,
    "posobecheck": [],
    "victory": 0,
    "datum": ""
}
try:
    with open(path.join(dir,"MEGA_SECRET_HYPER_PASSWORD")) as securiti:
        app.secret_key = securiti.read().strip()
except:
    print("Kliuč voe, pokud nevíš, jak se ti tohle vůbec povedlo???")
    exit()

def censor(texto, word):
    for w in word:
        pattern = re.compile(re.escape(w), re.IGNORECASE)
        texto = pattern.sub("***", texto)
    return texto
nopewords = ["neg","nig","nag","卐"]
    

@app.before_request
def setup():
    if "data" not in session:
        session["data"] = app.config["DEFAULT_DATA"].copy()
        print("Felix")

@app.route("/")
def main():
    session["name"] = str(random.randrange(1,40))
    session["data"]["roll"] = 0
    session["data"]["body"] = 0
    session["data"]["maxus"] = 0
    session["data"]["savio"]=0
    session["data"]["wolfo"]=0
    session["data"]["impo"]=0
    session["data"]["blackj"]=0
    session["data"]["posobecheck"]=[]
    session["data"]["victory"] = 0
    session.modified = True

    with open(path.join(dir,"users","users1.json")) as rum:
        saving = json.load(rum)
    for i in saving:
        saving[i]["jmeno"] = censor(saving[i]["jmeno"],nopewords)
    with open(path.join(dir,"users","users1.json"),"w") as rum:
        json.dump(saving,rum)


    with open(path.join(dir,"users","users1.json")) as rum:
        saving = json.load(rum)
    for i in saving:
        saving[i]["jmeno"] = censor(saving[i]["jmeno"],nopewords)
    with open(path.join(dir,"users","users1.json"),"w") as rum:
        json.dump(saving,rum)


    with open(path.join(dir,"users","users1.json")) as rum:
        saving = json.load(rum)
    for i in saving:
        saving[i]["jmeno"] = censor(saving[i]["jmeno"],nopewords)
    with open(path.join(dir,"users","users1.json"),"w") as rum:
        json.dump(saving,rum)

    return render_template("welcome.html")
#_______________________________________________________________________________________________
@app.route("/secret")
def secret():
    return render_template("secretum.html")

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

    balíky = {
        "balák1":balík1,
        "balák2":balík2,
        "balák3":balík3,
        "balák4":balík4,
    }
    for key in balíky:
        balíky[key] = [url_for('static', filename=img) for img in balíky[key]]

    return jsonify(balíky)


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
    maximus = session["data"]["maxus"]
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
        final="OOF"

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
            final="OOF"
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
    elif final == "OOF":
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
        session["data"]["victory"] = 1
        session.modified = True
    
    if kapr<0:
        kapr=0
    if maximus < kapr:
        maximus = kapr
    else:
        pass

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
            fvtxt1 = "Myš"
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
                fvtxt1 = "Alespoň něco"
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
    session["data"]["maxus"] = maximus
    session["data"]["roll"] = counterer
    session.modified = True
    carto = []

    progbar = kapr/2
    datosRES = {
        "carto": carto,
        "maximalka": [maximus],
        "flavour":[fvtxt1],
        "finalni":[final],
        "progreso":[progbar],
        "kount":[counterer],
        "karta1":karta11,
        "karta2":karta22,
        "karta3":karta33,
        "karta4":karta44,
    }

    print(Jackpot)
    print(final)
    print(kapr)

    return datosRES 
    # render_template("game1results.html",finalni = final,fidlovacka = kapr,brokovnice =nerozumim,kount=counterer,karta1=karta11,karta2=karta22,karta3=karta33,karta4=karta44,zmena = opakuj, flavourtext1 = fvtxt1)
#_______________________________________________________________________________________________
#_______________________________________________________________________________________________
@app.route("/game2/rules")
def gamerules2():
    return render_template("game2rules.html",)
#_______________________________________________________________________________________________
@app.route("/game2/running")
def gamerunning2():
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

    balíky = {
        "balák1":balík1,
        "balák2":balík2,
        "balák3":balík3,
        "balák4":balík4,
    }
    for key in balíky:
        balíky[key] = [url_for('static', filename=img) for img in balíky[key]]

    return jsonify(balíky)
    
    #return render_template("game2running.html",flavourtext2 = fvtxt2, balák1 = balík1, balák2 = balík2, balák3 = balík3, balák4 = balík4 )
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
        session["data"]["victory"] = 1
        session.modified = True
    if final == "bigX":
        final = "Nuh uh"

#----------------------------------------------------------------
    counterer = session["data"]["roll"]
    counterer = counterer + 1
    session["data"]["roll"]=counterer
    session.modified = True

    datosRES = {
        "finalni":[final],
        "kount":[counterer],
        "karta1":karta11,
        "karta2":karta22,
        "karta3":karta33,
        "karta4":karta44,
    }
    
    return datosRES
    
    #return render_template("game2results.html",finalni = final,kount=counterer,karta1=karta11,karta2=karta22,karta3=karta33,karta4=karta44)
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

    blaJ = "[black, J].png"
    if blackJs==1:
        for serio in range(100):
            Balík.append(blaJ)
            Balík2.append(blaJ)
            Balík3.append(blaJ)
            Balík4.append(blaJ)
        blackJs=0

    Imp="[imp].png"
    for ses in range(Imps):
        Balík.append(Imp)
        Balík2.append(Imp)
        Balík3.append(Imp)
        Balík4.append(Imp)  

    wolf="[Wolf].png"
    if thewolf>=1:
        for nod in range(thewolf):
            Balík.append(wolf)
            Balík2.append(wolf)
            Balík3.append(wolf)
            Balík4.append(wolf) 

    savo="[saviour].png"
    if saviour>=1:
        for don in range(saviour):
            Balík.append(savo)
            Balík2.append(savo)
            Balík3.append(savo)
            Balík4.append(savo)  

    random.shuffle(Balík4)
    random.shuffle(Balík3)
    random.shuffle(Balík2)
    random.shuffle(Balík)

    balíky = {
        "balák1":Balík,
        "balák2":Balík2,
        "balák3":Balík3,
        "balák4":Balík4,
    }
    for key in balíky:
        balíky[key] = [url_for('static', filename=img) for img in balíky[key]]

    return jsonify(balíky)
    #return balíky  #render_template("game3running.html",balák1 = Balík, balák2 = Balík2, balák3 = Balík3, balák4 = Balík4)
#_______________________________________________________________________________________________
@app.route("/game3/results")
def gameresults3():
    counterer = session["data"]["roll"]
    kapr = session["data"]["body"]
    maximus = session["data"]["maxus"]
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
    carto = []
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
    if thewolf>=1:
        for nod in range(thewolf):
            Balík.append(wolf)
            Balík2.append(wolf) 

    savo=["saviour"]
    if saviour>=1:
        for don in range(saviour):
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
        final="OOF"
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
    #-#
    for piky in (Jackpot[:4]):
        if "K" in piky:
            check.append("P")
    if len(check) == 2:
        final = "two"
    elif len(check) == 3:
        final= "three" 
    elif len(check) == 4:
        final= "full"  
    check=[]

    for srdce in (Jackpot[:4]):
        if "Q" in srdce:
            check.append("S")
    if len(check) == 2:
        final = "two"
    elif len(check) == 4:
        final= "full" 
    check=[]


    for Js in (Jackpot[:4]):
        if "J" in Js:
            check.append("J")
    if len(check) == 1:
        final="badluck"
    if len(check) == 2:
        final="2Bad2Luck"
    check=[]

    if len(Jackpot)== 1 or len(Jackpot)== 2 or len(Jackpot)== 3:
        pass
    else:
        if Jackpot==[]:
            final="OOF"
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
        thewolf-=1

    wolfcheck=[]
    for vlk in (Jackpot[:4]):
        if "saviour" in vlk:
            wolfcheck.append("W")
    if len(wolfcheck)>0:
        final="saviour"
        saviour-=1

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
        for Qs in (Jackpot[:4]):
            if "Q" in Qs:
                check.append("Q")
        if len(check) == 4:
            final="FOURQUEENS???"
        check=[]
        rollin = random.randrange(20)
        if rollin < 4:
            final="SIXQUEENS:TheStalker"
            thewolf = 1
            carto.append(wolf)
        elif 4<=rollin<8:
            final="SIXQUEENS:TheImpmageddon"
            Imps +=20
            for i in range(10):
                carto.append(Imp)
        elif 8<=rollin<12:
            final="SIXQUEENS:CurseofRa"
            blackJs = 1
            carto.append(blaJ)
        elif 12<=rollin<16:
            final="SIXQUEENS:TheSaviour"
            saviour = 1
            carto.append(savo)
        elif 16<=rollin<18:
            final="SIXQUEENS:TheSQUAD"
            thewolf = 1
            saviour = 1
            imps += 5
            carto.append(savo)
            carto.append(wolf)
            for n in range(5):
                carto.append(Imp)
        elif rollin ==20:
            if random.randrange(1,2)==1:
                final="SIXQUEENS:TheCursedArmy"
                thewolf = 5
                for ssa in range(5):
                    carto.append(wolf)
            else:
                final = "SIXQUEENS:TheBlessedArmy"
                saviour = 5
                for ssa in range(5):
                    carto.append(savo)
        else:
            final="SIXQUEENS:TheSaviour"
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
        else:
            kapr-=60
    elif final == "2Bad2Luck":
        kapr-= 90
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
    elif final == "OOF":
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
            Imps+=2
            for i in range(2):
                carto.append(Imp)
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

    if kapr<0:
        kapr=0
    if maximus < kapr:
        maximus = kapr
    else:
        pass

    session["data"]["roll"] = counterer
    session.modified = True
    session["data"]["body"] = kapr
    session.modified = True
    session["data"]["maxus"] = maximus
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
        session["data"]["victory"] = 1
        session.modified = True
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
    #-----------------------------------FVTXT--------------------------------
    flávour ={
        "Nothing": ["Meloun", "To bude na dlouho", "Za warudo", "Nic", "Ani omylem", ],
        "Too Picky": ["+++Press Reset+++", "Tady máš odměnu : )", ":3"],
        "OOF":["OOF", "UUF", "Nuh UH"],
        "Death":["JUDGEMENT", "Zkus si zahrát getting over it", "*I CAST: TESTICULAR TORSION!*"],
        "Straight": ["👍"],
        "High Card": ["šuby duby dub", "raz dva tři hej rup", "pidimužík pracuje", "pidimužík kutá"],
        "Four of a Kind":["FOUR"],
        "Three of a Kind":["THREE", "sýr", "Mám problémy s Nergigante", "Kontaktujte zprávce sítě"],
        "Two of a Kind":["TWO", "Prepare for trouble...", "\"Proč si snědla tu bramboru?\"", "Sedmimílové boty", "get a life"],
        "Bad Luck":["I am Malenia, Blade of Miquella", "The jokes on YOU!", "Občas vyhraješ, často prohráváš","samozřejmě skill based"],
        "2Bad2Luck":["So close, yet so far...", "\"two\" bad"],
        "SIXQUEENS:TheStalker": ["Woof Woof", "Sniffa", "AWOOOOOOOO"],
        "SIXQUEENS:TheImpmageddon": ["fearmagneto.exe", "God damn the SUN", "Nesnáším Warlock hráče"],
        "SIXQUEENS:TheSaviour": ["kontaktujte Němce", "pomoc", "kristova noho", "volejte záchranku", "WHY HE SO UGLY"],
        "SIXQUEENS:TheSQUAD": ["The gangs all here", "5 on 1", "P"],
        "SIXQUEENS:CurseofRa": ["𓀀𓀀𓁐𓂀𓃀𓄿𓅓𓆑𓇳𓁲𓈖𓉔𓀇𓀓𓁡𓊵𓋴𓌡𓍱𓎛𓏏𓀘𓀿𓁁𓁁𓂀"],
        "SIXQUEENS:TheCursedArmy":["Vlkodlaci", "Who let the Dawgs out???", "  * "],
        "SIXQUEENS:TheBlessedArmy":["Jsme spraseni!", "Výborně, teď je tu těch oblud pět",],
        "FOURQUEENS???":["WHAT", "ČTYŘI??", "MOC KRÁLOVEN"],
        "???":["PLIN PLIN PLON"],
        "ImpEyes":["Down you go", "Zbohem, už se nevracej", "dont give up, skeleton!" ],
        "TheWOLF":["The DAWG", "Damn bro, ok", "S I T"],
        "TheSAVIOR":["en nomine patris et filii et spiritu sancti. Kámen", "Popálen buď Ležíš Citrus...","...Aš na Veky" ],
        "Too Repetetive":["něco jinýho","buď originální", "stop spamming", "HŘEBÍK DO FÁZE"],
    }

    fvtxt = random.choice(flávour[final])

    if kapr<0:
        kapr=0
    opakuj = kapr - jauznevim
    nerozumim = kapr/2.5
    print(kapr)
    print(Jackpot)
    bar = random.randrange(1,25)
    for i in range(len(carto)):
        carto[i]= str(carto[i]) + ".png"
        carto[i]= (carto[i]).replace("'","")
    if carto == []:
        carto = None

#--------------------------------------------------------------------
    progbar = kapr/2.5
    datosRES = {
        "carto": carto,
        "baro": [bar],
        "maximalka": [maximus],
        "flavour":[fvtxt],
        "finalni":[final],
        "progreso":[progbar],
        "kount":[counterer],
        "karta1":karta11,
        "karta2":karta22,
        "karta3":karta33,
        "karta4":karta44,
    }
    
    return datosRES 

@app.route("/game/Game1")
def gamba1():
    counterer = session["data"]["roll"]
    kapr = session["data"]["body"]

    #delet
    carto = []
    fvtxt = "testfvtxt"
    final = "testfinal"
    karta11="0.png"
    karta22="0.png"
    karta33="0.png"
    karta44="0.png"

    return render_template("gamble1.html",carto = carto, flavour = fvtxt, finalni = final,kount=counterer,karta1=karta11,karta2=karta22,karta3=karta33,karta4=karta44,)
    

@app.route("/game/Game2")
def gamba2():
    counterer = session["data"]["roll"]

    #delet
    final = "testfinal"
    karta11="0.png"
    karta22="0.png"
    karta33="0.png"
    karta44="0.png"

    return render_template("gamble2.html",finalni = final,kount=counterer,karta1=karta11,karta2=karta22,karta3=karta33,karta4=karta44,)
    

@app.route("/game/Game3")
def gamba3():
    counterer = session["data"]["roll"]
    kapr = session["data"]["body"]
    saviour = session["data"]["savio"]
    thewolf = session["data"]["wolfo"]
    Imps = session["data"]["impo"]
    blackJs = session["data"]["blackj"]

    #delet
    carto = []
    fvtxt = "testfvtxt"
    final = "testfinal"
    karta11="0.png"
    karta22="0.png"
    karta33="0.png"
    karta44="0.png"

    for i in range(len(carto)):
        carto[i]= str(carto[i]) + ".png"
        carto[i]= (carto[i]).replace("'","")
    return render_template("gamble3.html",cartos = carto, flavour = fvtxt, finalni = final,fidlovacka = kapr,kount=counterer,karta1=karta11,karta2=karta22,karta3=karta33,karta4=karta44,)

@app.route("/game3/legend")
def legend():
    return render_template("legend.html")
#-------------------------------------------------------------------
@app.route("/victorier")
def victorier():
    vic = session["data"]["victory"]
    return jsonify(vic)
#----------------------------Lboardy--------------------------------
@app.route("/Lboard3")
def lboard3():
    with open(path.join(dir, "users", "users3.json")) as rum:
        step0 = json.load(rum)

    keys_to_delete = []

    # Clean entries before sorting
    valid_items = {}
    for key, value in step0.items():
        try:
            # Check that all required keys exist and values are valid for math
            if all(k in value for k in ["body", "rolly"]) and isinstance(value["body"], (int, float)) and isinstance(value["rolly"], (int, float)) and value["rolly"] != 0:
                # Calculate score once to avoid recalculating later
                score = (value["body"] / value["rolly"]) + value["body"]
                valid_items[key] = (score, value)
            else:
                raise ValueError("Missing or invalid keys/values")
        except Exception as e:
            print(f"Excluding from sort due to error ({key}): {e}")
            keys_to_delete.append(key)

    # Now sort the valid items
    step1 = dict(sorted(
        ((k, v[1]) for k, v in valid_items.items()),
        key=lambda item: valid_items[item[0]][0],
        reverse=True
    ))

    AbhorrentTemplate = "<tr><td>0</td><td>{jmeno}</td><td>{body}</td><td>{rolly}</td><td>{vyhra}</td><td>{datte}</td></tr>"

    Lbord = ""
    keys_to_delete = []

    for i in list(step1):  # convert to list to safely delete during iteration
        try:
            if all(k in step1[i] for k in ["jmeno", "body", "rolly", "vyhra", "datte"]):
                if len(step1[i]["jmeno"]) <= 20:
                    Lbord += AbhorrentTemplate.format(kluc=i, **step1[i])
                else:
                    print(f"Skipping long name: {step1[i]['jmeno']}")
                    keys_to_delete.append(i)
            else:
                print(f"Skipping incomplete record: {step1[i]}")
                keys_to_delete.append(i)
        except Exception as e:
            print(f"Error processing record {i}: {e}")
            keys_to_delete.append(i)

    # Delete the problematic entries
    for key in keys_to_delete:
        del step0[key]

    # Optional: write the cleaned data back to file
    with open(path.join(dir, "users", "users3.json"), "w") as fixfile:
        json.dump(step0, fixfile, indent=4)
    
    return render_template("L-Board3.html",board = Lbord)
#-----------------
@app.route("/Lboard2")
def lboard2():
    with open(path.join(dir, "users", "users2.json")) as rum:
        step0 = json.load(rum)
    step1 = step0


    AbhorrentTemplate = "<tr><td>0</td><td>{jmeno}</td><td>{rolly}</td><td>{vyhra}</td><td>{datte}</td></tr>"

    Lbord = ""
    keys_to_delete = []

    for i in list(step1):  # convert to list to safely delete during iteration
        try:
            if all(k in step1[i] for k in ["jmeno", "rolly", "vyhra", "datte"]):
                if len(step1[i]["jmeno"]) <= 20:
                    Lbord += AbhorrentTemplate.format(kluc=i, **step1[i])
                else:
                    print(f"Skipping long name: {step1[i]['jmeno']}")
                    keys_to_delete.append(i)
            else:
                print(f"Skipping incomplete record: {step1[i]}")
                keys_to_delete.append(i)
        except Exception as e:
            print(f"Error processing record {i}: {e}")
            keys_to_delete.append(i)

    # Delete the problematic entries
    for key in keys_to_delete:
        del step0[key]

    # Optional: write the cleaned data back to file
    with open(path.join(dir, "users", "users2.json"), "w") as fixfile:
        json.dump(step0, fixfile, indent=4)
    
    return render_template("L-Board2.html",board = Lbord)
#----------
@app.route("/Lboard1")
def lboard1():
    with open(path.join(dir, "users", "users1.json")) as rum:
        step0 = json.load(rum)

    keys_to_delete = []

    # Clean entries before sorting
    valid_items = {}
    for key, value in step0.items():
        try:
            # Check that all required keys exist and values are valid for math
            if all(k in value for k in ["body", "rolly"]) and isinstance(value["body"], (int, float)) and isinstance(value["rolly"], (int, float)) and value["rolly"] != 0:
                # Calculate score once to avoid recalculating later
                score = (value["body"] / value["rolly"]) + value["body"]
                valid_items[key] = (score, value)
            else:
                raise ValueError("Missing or invalid keys/values")
        except Exception as e:
            print(f"Excluding from sort due to error ({key}): {e}")
            keys_to_delete.append(key)

    # Now sort the valid items
    step1 = dict(sorted(
        ((k, v[1]) for k, v in valid_items.items()),
        key=lambda item: valid_items[item[0]][0],
        reverse=True
    ))
    AbhorrentTemplate = "<tr><td>0</td><td>{jmeno}</td><td>{body}</td><td>{rolly}</td><td>{vyhra}</td><td>{datte}</td></tr>"

    Lbord = ""
    keys_to_delete = []

    for i in list(step1):  # convert to list to safely delete during iteration
        try:
            if all(k in step1[i] for k in ["jmeno", "body", "rolly", "vyhra", "datte"]):
                if len(step1[i]["jmeno"]) <= 20:
                    Lbord += AbhorrentTemplate.format(kluc=i, **step1[i])
                else:
                    print(f"Skipping long name: {step1[i]['jmeno']}")
                    keys_to_delete.append(i)
            else:
                print(f"Skipping incomplete record: {step1[i]}")
                keys_to_delete.append(i)
        except Exception as e:
            print(f"Error processing record {i}: {e}")
            keys_to_delete.append(i)

    # Delete the problematic entries
    for key in keys_to_delete:
        del step0[key]

    # Optional: write the cleaned data back to file
    with open(path.join(dir, "users", "users1.json"), "w") as fixfile:
        json.dump(step0, fixfile, indent=4)
    
    return render_template("L-Board1.html",board = Lbord)


#--------------------------konec game3-----------------------------------------

@app.route('/game/end3')
def index3():
    final = session["data"]["victory"]
    return render_template('konec3.html',finalll = final)

@app.route('/game/end/thankyou3', methods=['POST'])
def submit3():
    savename = request.form['username']
    savename = censor(savename,nopewords)
    
    if savename.isalnum() == True and len(savename)<21:
        zz = datetime.datetime.now()
        date = str(zz.strftime("%x"))
        
        counterer = session["data"]["roll"]
        kapr = session["data"]["body"]
        if session["data"]["victory"] == 1:
            verdict = "Ano"
        else:
            verdict = "Ne"

        with open(path.join(dir,"users","users3.json")) as rum:
            saving = json.load(rum)
        klic = str(uuid.uuid4())

        saving[klic] = {"jmeno": savename, "body": kapr, "rolly": counterer, "vyhra": verdict, "datte": date} 

        with open(path.join(dir,"users","users3.json"),"w") as rum:
            json.dump(saving,rum)

        return render_template("thankyou.html")
    else:
        return render_template("fuckyou.html")
#---------------------------------------------------------------------------

#--------------------------konec game2-----------------------------------------
@app.route('/game/end2')
def index2():
    final = session["data"]["victory"]
    return render_template('konec2.html',finalll = final)

@app.route('/game/end/thankyou2', methods=['POST'])
def submit2():
    savename = request.form['username']
    savename = censor(savename,nopewords)

    if savename.isalnum() == True and len(savename)<21:
        zz = datetime.datetime.now()
        date = str(zz.strftime("%x"))

        counterer = session["data"]["roll"]
        if session["data"]["victory"] == 1:
            verdict = "Ano"
        else:
            verdict = "Ne"

        with open(path.join(dir,"users","users2.json")) as rum:
            saving = json.load(rum)
        klic = str(uuid.uuid4())

        saving[klic] = {"jmeno": savename, "rolly": counterer, "vyhra": verdict, "datte": date} 

        with open(path.join(dir,"users","users2.json"),"w") as rum:
            json.dump(saving,rum)

        return render_template("thankyou.html")
    else:
        return render_template("fuckyou.html")
#---------------------------------------------------------------------------

#--------------------------konec game1-----------------------------------------
@app.route('/game/end1')
def index1():
    final = session["data"]["victory"]
    return render_template('konec1.html',finalll = final)

@app.route('/game/end/thankyou1', methods=['POST'])
def submit1():
    savename = request.form['username']
    savename = censor(savename,nopewords)

    if savename.isalnum() == True and len(savename)<21:
        zz = datetime.datetime.now()
        date = str(zz.strftime("%x"))

        counterer = session["data"]["roll"]
        kapr = session["data"]["body"]
        if session["data"]["victory"] == 1:
            verdict = "Ano"
        else:
            verdict = "Ne"

        with open(path.join(dir,"users","users1.json")) as rum:
            saving = json.load(rum)
        klic = str(uuid.uuid4())

        saving[klic] = {"jmeno": savename, "body": kapr, "rolly": counterer, "vyhra": verdict, "datte": date} 

        with open(path.join(dir,"users","users1.json"),"w") as rum:
            json.dump(saving,rum)

        return render_template("thankyou.html")
    else:
        return render_template("fuckyou.html")
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#-------------------------------------TWIST---------------------------------
#---------------------------------------------------------------------------

#--------------------------------general-----------------------------------
def openjson(file,request):
    if file == "users":
        with open(path.join(dir, "jsons", f"{file}.json")) as rum:
                jason = json.load(rum)
                requested = jason[session["username"]][request]
    else:
        with open(path.join(dir, "jsons", f"{file}.json")) as rum:
                jason = json.load(rum) 
                requested = jason[request]
    return requested
def closejson(file,nazev,data):
    with open(path.join(dir, "jsons", f"{file}.json")) as rum:
            jason = json.load(rum)
            jason[session["username"]][nazev] = data
    with open(path.join(dir, "jsons", "users.json"),"w") as rum:
            json.dump(jason, rum, indent=4)

def presorter(inventory,tier,loc):
    b=[]
    a=[]
    c=[]
    for i in inventory.values():
        if loc == "inv":
            k = [i["name"], i["desc"],i["type"]]
        elif loc == "shop":
            if i["name"] == "0":
                k = ["0","-","-"]
            elif i["name"] != "0":
                k = [i["name"], i["desc"], i["price"]]
        
        if i["tier"] == tier:
            if i["type"] == "boon":
                b.append(k)
            elif i["type"] == "apex":
                a.append(k)
            elif i["type"] == "curse":
                c.append(k)
        else:
                pass
    pack = {
        "b": b,
        "a": a,
        "c":c
    }
    return pack

def sorter(pack,loc):
    template = ""

    if loc == "inv":
            for x in pack:
                button_class = "deckbuilderA" if x[2] == "apex" else "deckbuilder"
                item = f"""<tr><td>{x[0]},{x[1]}</td><td><button class='{button_class}' id={x[0]} onclick='pickcard(\"{x[0]}\")'></button></td></tr>
"""
                template += item

    elif loc == "shop":
        for x in pack:
            if x[0] == "0":
                item = f"""<tr><td><span class="item-name">{x[0]}</span><span class="price">{x[1]}</span>{x[2]}</td></tr>
"""
            else:
                item = (
                    f"""<tr><td><span class="item-name">{x[0]}</span><span class="price">{x[1]}</span>{x[2]}</td>                  
"""
                    f"""<td><button onclick='buy(\"{x[0]}\")'>buy</button></td></tr>
"""
                )
            print(item)
            template += item

    return template

def tabularInv(tier,boons,apex,curses):
    invtab = f"""
<table>
<tr><th colspan="2">Tier{tier}</th></tr>
<tr><th colspan="2">boony</th></tr>
{boons}
<tr><th colspan="2">apexy</th></tr>
{apex}
<tr><th colspan="2">kletby</th></tr>
{curses}
</table>
"""
    return invtab

def shopavail(shop,inv):
    shopwindow = {}
    for i in shop.values():
        if i["name"] not in inv:
            shopwindow[i["name"]] = i
        else:
            shopwindow[i["name"]] = i
            shopwindow[i["name"]]["name"] = "0"
    return shopwindow
#-----------------------------------------------------------------------------------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('You need to log in first.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
def gototwist():
    return redirect(url_for('twist'))

@app.route("/twist")
def twist():
    return render_template("first.html")

@app.route("/twist/signin", methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with open(path.join(dir, "jsons", "users.json")) as rum:
            users = json.load(rum) 

        if username in users:
            flash('Username already exists!')
            return redirect(url_for('sign_in'))

        hashed_password = generate_password_hash(password)
#----------------------------base stats---------------------------------------------
        users[username] = {
            "password": hashed_password,
            "balance": 0,             
            "admin": 0,
            "ban": 0,
            "issue":0,
            "inventory": {
            "X2": {
                "name": "X2",
                "desc": "Doubles points",
                "tier": 1,
                "type": "boon"
            },
            "plus20": {
                "name": "plus20",
                "desc": "Points + 20",
                "tier": 1,
                "type": "boon"
            },
            "Flipper":{
                "name": "Flipper",
                "desc": "Flips 'polarity', cannot exceed 150pts",
                "tier": 1,
                "type": "boon" 
            },
            "Stack5": {
                "name": "Stack5",
                "desc": "increases points by 5",
                "tier": 1,
                "type": "boon"   
            },
            "NullNext2": {
                "name": "NullNext2",
                "desc": "Points this turn and the next are 0",
                "tier": 1,
                "type": "apex"
            }
            },
        "deck": {
            "deck1": {
                "name": "deck1",
                "slot1": "X2",
                "slot2": "plus20",
                "slot3": "Flipper",
                "slot4": "Stack5",
                "slotA": "NullNext2"
            },
            "deck2": {
                "name": "deck2",
                "slot1": "0",
                "slot2": "0",
                "slot3": "0",
                "slot4": "0",
                "slotA": "0"
            },
            "deck3": {
                "name": "deck3",
                "slot1": "0",
                "slot2": "0",
                "slot3": "0",
                "slot4": "0",
                "slotA": "0"
            },
            "deck4": {
                "name": "deck4",
                "slot1": "0",
                "slot2": "0",
                "slot3": "0",
                "slot4": "0",
                "slotA": "0"
            },
            "deck5": {
                "name": "deck5",
                "slot1": "0",
                "slot2": "0",
                "slot3": "0",
                "slot4": "0",
                "slotA": "0"
            }
        }
    }

        with open(path.join(dir, "jsons", "users.json"),"w") as rum:
            json.dump(users, rum, indent=4)
#-----------------------------------------------------------------------------------------------------
        flash('Registration successful! You can now log in.')
        return redirect(url_for('twist'))

    return render_template('register.html')

@app.route("/twist/login", methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        with open(path.join(dir, "jsons", "users.json")) as rum:
            users = json.load(rum)

        user_password_hash = users[username].get("password")

        if user_password_hash and check_password_hash(user_password_hash, password):
            session['username'] = username
            return redirect(url_for('setup'))
        else:
            flash('Invalid credentials')
            return redirect(url_for('log_in'))

    return render_template('login.html')

@app.route("/twist/setup")
@login_required
def setup():
    dataAdmin = openjson("users", "admin")
    dataBan = openjson("users", "ban")
    session["deck"] = {
            "deckNo": "",
            "slot1": "0",
            "slot2": "0",
            "slot3": "0",
            "slot4": "0",
            "slotA": "0",
            "valid": 0
        }
    session["cards"] = {}
    session["cards"]["pack"] = []
    session["misc"] = {}
    session["misc"]["bank"] = 0
    session["prop"] = {}
    session.modified = True
    if dataBan == 1:
        return redirect(url_for("banned"))
    elif dataAdmin == 1 or dataAdmin == 2:
        return redirect(url_for("houseadmin"))
    elif dataAdmin == 0:
        return redirect(url_for("house"))

@app.route("/twist/banned")
@login_required
def banned():
    return render_template("banned.html")

@app.route("/twist/houseadmin")
@login_required
def houseadmin():
    name = session["username"]
    
    try:
        bal = openjson("users", "balance")
        bal += session["misc"]["bank"]
        closejson("users","balance",bal)
    except Exception as e:
        pass

    return render_template("houseadmin.html", name = name)

@app.route("/twist/house")
@login_required
def house():
    name = session["username"]
    
    try:
        bal = openjson("users", "balance")
        bal += session["misc"]["bank"]
        closejson("users","balance",bal)
    except Exception as e:
        pass


    return render_template("house.html", name = name)

@app.route("/twist/inventory")
@login_required
def inventory():

    return render_template("inventory.html",)

@app.route("/twist/shop")
@login_required
def shop():

    return render_template("shop.html")

@app.route("/twist/pregame")
@login_required
def pregame():

    if session["deck"]["deckNo"] == "":
        session["deck"]["deckNo"] = "deck1"
    deckNo = session["deck"]["deckNo"]

    return render_template("pregame.html", deckNo = deckNo)

@app.route("/twist/twist_game")
@login_required
def twistgame():


    return render_template("twist_game.html",vec = session["deck"])

@app.route("/twist/twist_victory")
@login_required
def victory():
    set_defaults()
    bank = session["misc"]["bank"]
    bank += 5*(2**session["misc"]["round"])
    session["misc"]["bank"] = bank
    
    ro = session["misc"]["round"]
    ro += 1
    session["misc"]["round"] = ro

    return render_template("victory.html", bank = bank)

@app.route("/twist/twist_gameover")
@login_required
def gameover():
    set_defaults()
    bank = session["misc"]["bank"]
    bank = 0
    session["misc"]["bank"] = bank

    return render_template("gameover.html")

@app.route("/twist/userscreen")
@login_required
def userscreen():
    listU = ""
    adlevel = openjson("users","admin")
    if adlevel == 2:
        issues = openjson("users", "issues")
        for i in issues:
            listU += i + "<br>"
    
    return render_template("userscreen.html", listU = listU)
#--------------fet--------------------

@app.route("/twist/fet/balance")
@login_required
def balanc():
        balance = openjson("users","balance")
        return jsonify(balance=balance)

@app.route("/twist/fet/decktab")
def decktab():
        deck = openjson("users","deck")
        decktab = {
        "deck1": {
            "name": deck["deck1"]["name"],
            "slot1": deck["deck1"]["slot1"],
            "slot2": deck["deck1"]["slot2"],
            "slot3": deck["deck1"]["slot3"],
            "slot4": deck["deck1"]["slot4"],
            "slotA": deck["deck1"]["slotA"]
        },"deck2": {
            "name": deck["deck2"]["name"],
            "slot1": deck["deck2"]["slot1"],
            "slot2": deck["deck2"]["slot2"],
            "slot3": deck["deck2"]["slot3"],
            "slot4": deck["deck2"]["slot4"],
            "slotA": deck["deck2"]["slotA"]
        },"deck3": {
            "name": deck["deck3"]["name"],
            "slot1": deck["deck3"]["slot1"],
            "slot2": deck["deck3"]["slot2"],
            "slot3": deck["deck3"]["slot3"],
            "slot4": deck["deck3"]["slot4"],
            "slotA": deck["deck3"]["slotA"]
        },"deck4": {
            "name": deck["deck4"]["name"],
            "slot1": deck["deck4"]["slot1"],
            "slot2": deck["deck4"]["slot2"],
            "slot3": deck["deck4"]["slot3"],
            "slot4": deck["deck4"]["slot4"],
            "slotA": deck["deck4"]["slotA"]
        },"deck5": {
            "name": deck["deck5"]["name"],
            "slot1": deck["deck5"]["slot1"],
            "slot2": deck["deck5"]["slot2"],
            "slot3": deck["deck5"]["slot3"],
            "slot4": deck["deck5"]["slot4"],
            "slotA": deck["deck5"]["slotA"]
        }
    }
        return decktab

@app.route("/twist/fet/transaction", methods=['GET', 'POST'])
@login_required
def transaction():
    item = request.data.decode("utf-8")
    shop = openjson("shop","shop")
    inv = openjson("users","inventory")
    balance = openjson("users","balance")

    if balance >= shop[item]["price"]:
        inv[shop[item]["name"]]=shop[item].copy()
        balance -= shop[item]["price"]
        closejson("users","inventory",inv)
        closejson("users","balance",balance)

        message = "úspěch!"

        return message
    else:
         message = "nedostatek"
         return message

@app.route("/twist/fet/shop")
@login_required
def shopfet():
    shop = openjson("shop","shop")
    inv = openjson("users","inventory")

    shopwindow = shopavail(shop,inv)
    
    sort1 = presorter(shopwindow,1,"shop")
    sort2 = presorter(shopwindow,2,"shop")
    sort3 = presorter(shopwindow,3,"shop")

    boons1 = sorter(sort1["b"],"shop")
    apex1 = sorter(sort1["a"],"shop")
    curses1 = sorter(sort1["c"],"shop")

    boons2 = sorter(sort2["b"],"shop")
    apex2 = sorter(sort2["a"],"shop")
    curses2 = sorter(sort2["c"],"shop")

    boons3 = sorter(sort3["b"],"shop")
    apex3 = sorter(sort3["a"],"shop")
    curses3 = sorter(sort3["c"],"shop")

    tab = ""
    tab+= tabularInv(1,boons1,apex1,curses1)
    tab+= tabularInv(2,boons2,apex2,curses2)
    tab+= tabularInv(3,boons3,apex3,curses3)

    #tomasi tohle pak smaz
    print(tab)

    return tab

@app.route("/twist/fet/inventory")
@login_required
def inventoryfet():
    inventory = openjson("users","inventory")

    pack1 = presorter(inventory,1,"inv")
    pack2 = presorter(inventory,2,"inv")
    pack3 = presorter(inventory,3,"inv")

    boons1 = sorter(pack1["b"],"inv")
    apex1 = sorter(pack1["a"],"inv")
    curses1 = sorter(pack1["c"],"inv")

    boons2 = sorter(pack2["b"],"inv")
    apex2 = sorter(pack2["a"],"inv")
    curses2 = sorter(pack2["c"],"inv")

    boons3 = sorter(pack3["b"],"inv")
    apex3 = sorter(pack3["a"],"inv")
    curses3 = sorter(pack3["c"],"inv")

    invt = ""
    invt+= tabularInv(1,boons1,apex1,curses1)
    invt+= tabularInv(2,boons2,apex2,curses2)
    invt+= tabularInv(3,boons3,apex3,curses3)
    #tomasi tohle pak smaz
    print(invt)

    return invt

@app.route("/twist/fet/deckeditor", methods=['GET', 'POST'])
@login_required
def deckedit():
    decks = openjson("users", "deck")
    data = request.get_json()
    dupe = 0

    cardpicked = data.get('cardpicked')
    slotedited = data.get('slotedited')
    deckedited = data.get("deckedited")

    for i in decks[deckedited].values():
        if i == cardpicked:
            dupe = 1
    
    if dupe == 1:
        response = "Karta již v decku"
    else:
        decks[deckedited][slotedited] = cardpicked
        response = "ok", 200

    closejson("users","deck", decks)

    return response

@app.route("/twist/fet/pregame", methods=['GET', 'POST'])
@login_required
def pregamedeck():  
    curses = openjson("curses","curses")
    deckdata = request.get_json()
    session["deck"]["valid"] = 1

    for i in deckdata:
        session["deck"][i] = deckdata[i]
        if session["deck"][i] == "0":
            session["deck"]["valid"] = 0
    session.modified = True

    if session["deck"]["valid"] == 1:
        resposne = "ok"
        session["misc"]["round"] = 1
        session["misc"]["points"] = 0
        session["misc"]["pointstotal"] = 0
        session["misc"]["turn"] = 0 
        session["misc"]["text"] = ""
        session["misc"]["decknumber"] = deckdata["deckNo"]
        session["misc"]["lossposible"] = 0
        session["misc"]["bank"] = 0

        session["prop"]["reproc"] = 0
        session["prop"]["propscale1"] = 0
        session["prop"]["propscale2"] = 0
        session["prop"]["propscale3"] = 0
        session["prop"]["propscale4"] = 0
        session["prop"]["propscale5"] = 0
        session["prop"]["reprocer"] = None

        session["cards"]["symbols"] = ["srdce", "káry", "kříže", "piky"]
        session["cards"]["values"] = ["2","3","4","5","6","7","8","9","10","A","J","Q","K"]
        session["cards"]["pack"] = []
        session["cards"]["jack1"] = []
        session["cards"]["jack2"] = []
        session["cards"]["jack3"] = []
        session["cards"]["jack4"] = []
        session["cards"]["jack5"] = []

        session["curses"] = curses
        session.modified = True
    else:
        resposne = "Nevalidní deck" 
    
    return resposne

@app.route("/twist/fet/defaults")
@login_required
def set_defaults():
    session["misc"]["points"] = 0
    session["misc"]["pointstotal"] = 0
    session["misc"]["turn"] = 0 
    session["misc"]["lossposible"] = 0

    session["prop"]["reproc"] = 0
    session["prop"]["propscale1"] = 0
    session["prop"]["propscale2"] = 0
    session["prop"]["propscale3"] = 0
    session["prop"]["propscale4"] = 0
    session["prop"]["propscale5"] = 0
    session["prop"]["reprocer"] = None

    session["cards"]["symbols"] = ["srdce", "káry", "kříže", "piky"]
    session["cards"]["values"] = ["2","3","4","5","6","7","8","9","10","A","J","Q","K"]
    session["cards"]["pack"] = []
    session["cards"]["jack1"] = []
    session["cards"]["jack2"] = []
    session["cards"]["jack3"] = []
    session["cards"]["jack4"] = []
    session["cards"]["jack5"] = []
    session.modified = True
        
    return


@app.route("/twist/fet/draw_phase")
@login_required
def draw_phase():
    
    check = sum(1 for v in session["deck"].values() if v == "0")
    if check == 5 or session["prop"]["reproc"] == 69:
        D = openjson("users", "deck")
        C = openjson("curses", "curses")
        deckdefault = D[session["misc"]["decknumber"]]
        pool = []
        for i in range(1,5):
            pool.append(deckdefault[f"slot{i}"])
        random.shuffle(pool)
        session["deck"]["slot2"] = pool[0]
        session["deck"]["slot3"] = pool[1]

        session["deck"]["slot1"] = random.choice(C)
        session["deck"]["slot4"] = random.choice(C)

        if session["prop"]["reproc"] == 69:
           session["prop"]["reproc"] = 0
           session.modified = True 
           session["deck"]["slotA"] = "0"
        else:
            session["deck"]["slotA"] = deckdefault["slotA"]

        session.modified = True
    

    symbols = session["cards"]["symbols"]
    values = session["cards"]["values"]
    
    pack = []
    for suit in symbols:
        for val in values:
            card = [suit, val]
            pack.append(card)

    jack = []
    picturepack = []
    for n in pack:
        n = str(n) + ".png"
        n = n.replace("'", "")
        picturepack.append(n)
    for i in range(5):
        ppack = picturepack[:]              
        random.shuffle(ppack)               
        session["cards"]["pack" + str(i+1)] = ppack
        session.modified = True
    for i in range(5):
        jack.append(random.choice(pack))
    print(jack)
    jackpics = [card[:] for card in jack]

    figures = {
        "Duo": {
            "ClubsDuo": ["kříže", 2, -1],
            "SpadesDuo": ["piky", 2, -1],
            "HeartsDuo": ["srdce", 2, 2],
            "DiamonsDuo": ["káry", 2, 2],
        },
        "Trio": {
            "ClubsTrio": ["kříže", 3, -1.5],
            "SpadesTrio": ["piky", 3, -1.5],
            "HeartsTrio": ["srdce", 3, 3],
            "DiamonsTrio": ["káry", 3, 3],
        },
        "OddOneOut": {
            "ClubsGang": ["kříže", 4, 0.5],
            "SpadesGang": ["piky", 4, 0.5],
            "HeartsGang": ["srdce", 4, 0.5],
            "DiamonsGang": ["káry", 4, 0.5],
        },
        "FullSuite": {
            "AllClubs": ["kříže", 5, -2.5],
            "AllSpades": ["piky", 5, -2.5],
            "AllHearts": ["srdce", 5, 5],
            "AllDiamons": ["káry", 5, 5],
        }
    }
    faces = {
        "J":11,
        "Q":12,
        "K":13,
        "A":14
    }
    vals1 = []
    for i in jack:
        if i[1] in faces:
            val = faces[i[1]]
        else:
            val = int(i[1])
        i[1] = val #---
        vals1.append(val)
    
    valses = {
        "piky":0,
        "kříže":0,
        "srdce":0,
        "káry":0
    }

    for z in jack:
        valses[z[0]] += z[1]
            
    ro = session["misc"]["round"]
    turn = session["misc"]["turn"]
    finalmath = []
    finaltext = ""
    for figs in figures:
        for keys, subfigures in figures[figs].items():
            count = 0
            for card in jack:
                if subfigures[0] in card:
                    count += 1
            if count == subfigures[1]:
                vals = valses[subfigures[0]]
                finalmath = [figs, subfigures[2]*vals]
                finaltext = f"{keys} => {subfigures[2]*vals}"
                if finalmath[1] < 0:
                    if session["misc"]["lossposible"] == 1:
                        finalmath = [figs, round(subfigures[2] * vals * (1 + ((turn / 100)+(ro))), 2)*ro]
                        finaltext = f"{keys} => {round(subfigures[2]*vals*(1+((turn/100)+(ro))),2)*ro}"
    
    if finalmath == []:
        finalmath = ["Highcard", 1*max(vals1)]
        finaltext = f"Highcard - 1*{max(vals1)}"
    
    finaltext = finaltext.replace("'", "")
    finaltext = finaltext.replace("[", "")
    finaltext = finaltext.replace("]", "")

    turn = session["misc"]["turn"]
    turn += 1

    session["misc"]["text"] = finaltext
    session["misc"]["points"] = finalmath[1]
    session["misc"]["turn"] = turn
    session["cards"]["pack"] = picturepack
    for i in range(1,6):
        z = str(jackpics[i-1]) + ".png"
        z = z.replace("'", "")
        session["cards"]["jack" + str(i)] = z
    session.modified = True

    displaydata = {
                "deck":{
                    "slot1":session["deck"]["slot1"],
                    "slot2":session["deck"]["slot2"],
                    "slot3":session["deck"]["slot3"],
                    "slot4":session["deck"]["slot4"],
                    "slotA":session["deck"]["slotA"]
                },
                "misc":{
                    "points":session["misc"]["points"],
                    "pointstotal":session["misc"]["pointstotal"],
                    "turn":session["misc"]["turn"],
                    "round":session["misc"]["round"],
                    "text":session["misc"]["text"]
                },
                "cards":{
                    "pack1":session["cards"]["pack1"],
                    "pack2":session["cards"]["pack2"],
                    "pack3":session["cards"]["pack3"],
                    "pack4":session["cards"]["pack4"],
                    "pack5":session["cards"]["pack5"],
                    "jack1":session["cards"]["jack1"],
                    "jack2":session["cards"]["jack2"],
                    "jack3":session["cards"]["jack3"],
                    "jack4":session["cards"]["jack4"],
                    "jack5":session["cards"]["jack5"]
                }
            }


    return displaydata

@app.route("/twist/fet/processor", methods=['GET', 'POST'])
@login_required
def processor():
    import Actions
    actionplayed = request.get_data(as_text=True)
    maxpoints = (250*(2**session["misc"]["round"]))
    

    if session["prop"]["reprocer"] != None:
        action = session["prop"]["reprocer"]
    else:
        action = session["deck"][actionplayed]
    
    if session["deck"][actionplayed] =="0":
        verdict = 0
    elif session["prop"]["reprocer"] != None:
        session["prop"]["reprocer"] = None
        verdict = 1
    else:
        session["deck"][actionplayed] = "0"
        verdict = 1

    reproc = session["prop"]["reproc"]
    pts = session["misc"]["points"]
    propscale1 = session["prop"]["propscale1"]
    propscale2 = session["prop"]["propscale2"]
    propscale3 = session["prop"]["propscale3"]
    propscale4 = session["prop"]["propscale4"]
    propscale5 = session["prop"]["propscale5"]
#-------------------------kdyztak predelat---------------------
    cards = session["cards"].values()

    if "Hope" in cards and "Dreams" in cards:
        propscale5 = 1
    propscale4 = session["misc"]["pointstotal"]
    propscale3 = session["prop"]["propscale3"]
    session["prop"]["propscale3"] = action
    session.modified = True
#---------------------------------------------------------------
    if verdict == 1:
        print(action)
        resultdict = getattr(Actions, action)(reproc,pts,propscale1,propscale2,propscale3,propscale4,propscale5,)
        
        pointsafter = resultdict["pointsafter"]
        session["prop"]["reproc"] = resultdict["reproc"]
        
        if session["prop"]["reproc"] == 1:
            session["prop"]["reprocer"] = action
        elif session["prop"]["reproc"] == 69:
            session["misc"]["turn"] =session["misc"]["turn"] + 5
        session.modified = True

        pointstotal = session["misc"]["pointstotal"]
        pointstotal += pointsafter
        if pointstotal < 0:
            pointstotal = 0
        if pointstotal >= (maxpoints/2):
            session["misc"]["lossposible"] = 1
        if  pointstotal >= maxpoints:
            gameover = 1
            
            D = openjson("users", "deck")
            C = openjson("curses", "curses")
            deckdefault = D[session["misc"]["decknumber"]]
            pool = []
            for i in range(1,5):
                pool.append(deckdefault[f"slot{i}"])
            random.shuffle(pool)
            session["deck"]["slot2"] = pool[0]
            session["deck"]["slot3"] = pool[1]

            session["deck"]["slot1"] = random.choice(C)
            session["deck"]["slot4"] = random.choice(C)

            session["deck"]["slotA"] = deckdefault["slotA"]

            session["prop"]["reproc"] = 0
            session["prop"]["reprocer"] = None
            session.modified = True
        

        elif pointstotal == 0 and session["misc"]["lossposible"] == 1:
            gameover = 2
        else:
            gameover = 0
        session["misc"]["pointstotal"] = pointstotal
        
        session.modified = True
    else:
        pointsafter = 0
        pointstotal = 0
        gameover = 0

    results = {
        "pointsafter": round(pointsafter,2),
        "pointstotal": pointstotal,
        "validity": verdict,
        "gameover": gameover
    }

    return results


@app.route("/twist/fet/userlist", methods=['GET', 'POST'])
@login_required
def userlist():

    with open(path.join(dir, "jsons", "users.json")) as rum:
        userdata = json.load(rum)

    userslist = "<table>"
    for key, i in userdata.items():
        if i["admin"] == 2:
            continue
        else:
            userslist += f"""
            <tr>
                <td>{key}</td>
                <td>Admin:</td><td>{i["admin"]}</td>
                <td>Ban:</td><td>{i["ban"]}</td>
                <td><button class='smallbutton' onclick='ban("{key}")'>B</button></td>
                <td><button class='smallbutton' onclick='adminize("{key}")'>A</button></td>
            </tr>"""
    userslist += "</table>"

    return userslist

@app.route("/twist/fet/userlistaction", methods=['GET', 'POST'])
@login_required
def userlistaction():

    data = request.get_json()
    with open(path.join(dir, "jsons", "users.json")) as rum:
        js = json.load(rum)

    username = data["user"]
    action = data["action"]

    current = js[username][action]
    js[username][action] = 1 if current == 0 else 0

    with open(path.join(dir, "jsons", "users.json"), "w") as rum:
        json.dump(js, rum, indent=4)

    with open(path.join(dir, "jsons", "users.json")) as rum:
        js = json.load(rum)

    usernameA = "Admin"
    actionA = "issues"

    problem = username

    currentA = js[usernameA][actionA]
    if problem in currentA:
        currentA.remove(problem)
    js[usernameA][actionA] = currentA

    with open(path.join(dir, "jsons", "users.json"), "w") as rum:
        json.dump(js, rum, indent=4)
    
    return "", 200

@app.route("/twist/fet/issue", methods=['GET', 'POST'])
@login_required
def sendissue():
    dats = request.get_json()
    iss = openjson("users", "issue")
    if iss == 0:
        iss = 1
        with open(path.join(dir, "jsons", "users.json")) as rum:
            js = json.load(rum)

        username = "Admin"
        action = "issues"

        problem = session["username"]

        current = js[username][action]
        current.append(problem)
        js[username][action] = current

        with open(path.join(dir, "jsons", "users.json"), "w") as rum:
            json.dump(js, rum, indent=4)
    closejson("users", "issue", iss)

    return "", 200




@app.errorhandler(500)
def internal_error(error):
    import traceback
    traceback.print_exc()
    return "Internal Server Error", 500


#---------------------------------------------------------------------------
if __name__ == "__main__":
    app.secret_key = "23431bea-b546-4e3a-80fd-7de8fca65430" #pls nezapomen tohle zmenit to by bylo BAAAAD/done, ale imperfektne
    app.run(debug=True)
