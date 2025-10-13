import random
from os import path
from flask import Flask, render_template, render_template_string, request, session, redirect, url_for, g, jsonify, flash
import json
import uuid
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

dir = path.dirname(__file__)
app = Flask(__name__)

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
                item = f"<tr><td>{x[0]},{x[1]}</td><td><button class='{button_class}' id={x[0]} onclick='pickcard(\"{x[0]}\")'></button></td></tr>"
                template += item

    elif loc == "shop":
        for x in pack:
            if x[0] == "0":
                item = f"<tr><td>{x[0]},{x[1]},{x[2]}</td></tr>"
            else:
                item = (
                    f"<tr><td>{x[0]},{x[1]},{x[2]}</td>"
                    f"<td><button onclick='buy(\"{x[0]}\")'>buy</button></td></tr>"
                )
            print(item)
            template += item

    return template

def tabularInv(tier,boons,apex,curses):
    invtab = f"\
            <table>\
            <tr>\
            <th>Tier{tier}</th>\
            </tr>\
            <tr>\
            <th>boony</th>\
            </tr>\
            {boons}\
            <tr>\
            <th>apexy</th>\
            </tr>\
            {apex}\
            <tr>\
            <th>kletby</th>\
            </tr>\
            {curses}\
            </table>\
            "
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
                "desc": "increases points by 5, increse by 5 for every turn this is in your hand",
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
                "slot1": "none",
                "slot2": "none",
                "slot3": "none",
                "slot4": "none",
                "slotA": "none"
            },
            "deck3": {
                "name": "deck3",
                "slot1": "none",
                "slot2": "none",
                "slot3": "none",
                "slot4": "none",
                "slotA": "none"
            },
            "deck4": {
                "name": "deck4",
                "slot1": "none",
                "slot2": "none",
                "slot3": "none",
                "slot4": "none",
                "slotA": "none"
            },
            "deck5": {
                "name": "deck5",
                "slot1": "none",
                "slot2": "none",
                "slot3": "none",
                "slot4": "none",
                "slotA": "none"
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
            "slot1": "none",
            "slot2": "none",
            "slot3": "none",
            "slot4": "none",
            "slotA": "none",
            "valid": 0
        }
    session["cards"] = {}
    session["cards"]["pack"] = []
    session["misc"] = {}
    session["misc"]["bank"] = 0
    session["misc"]["round"] = 1
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
    session["misc"]["round"] = 1
    session.modified = True
    
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

    invtab = ""
    invtab+= tabularInv(1,boons1,apex1,curses1)
    invtab+= tabularInv(2,boons2,apex2,curses2)
    invtab+= tabularInv(3,boons3,apex3,curses3)

    return invtab

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
        if session["deck"][i] == "none":
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
    if check == 5:
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

    if verdict == 1:
        resultdict = getattr(Actions, action)(reproc,pts,propscale1,propscale2,propscale3,propscale4,propscale5,)
        
        pointsafter = resultdict["pointsafter"]
        session["prop"]["reproc"] = resultdict["reproc"]
        
        if session["prop"]["reproc"] == 1:
            session["prop"]["reprocer"] = action

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

if __name__ == '__main__':
    app.secret_key = 'your_mom69' #pls nezapomen tohle zmenit to by bylo BAAAAD
    app.run(debug=True)