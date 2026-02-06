resulttemplate = {
    "pointsafter": 0,
    "reproc": 0
    }

def reprocing(procs,reproc):
    if reproc == procs:
        return (reproc - 1)

def NullNext2(reproc,pts,ph1,ph2,ph3,ph4,ph5):
    result = resulttemplate.copy()

    result["pointsafter"] = 0
    if reproc == 1:
        result["reproc"] = reprocing(1,reproc)
    else:
        result["reproc"] = 1
    
    return result

def X2(reproc,pts,ph1,ph2,ph3,ph4,ph5):
    result = resulttemplate.copy()
    
    result["pointsafter"] = pts*2
    result["reproc"] = 0

    return result

def Stack5(reproc,pts,ph1,ph2,ph3,ph4,ph5):
    result = resulttemplate.copy()
    
    result["pointsafter"] = pts+5
    result["reproc"] = 0

    return result


def plus20(reproc,pts,ph1,ph2,ph3,ph4,ph5):
    result = resulttemplate.copy()

    result["pointsafter"] = pts + 20
    result["reproc"] = 0

    return result

def Flipper(reproc,pts,ph1,ph2,ph3,ph4,ph5):
    result = resulttemplate.copy()

    result["pointsafter"] = -pts
    if result["pointsafter"] > 150:
        result["pointsafter"] = 150
    result["reproc"] = 0

    return result

def add40(reproc,pts,ph1,ph2,ph3,ph4,ph5):
    result = resulttemplate.copy()

    if pts < 0:
        result["pointsafter"] = pts - 40
    else:
        result["pointsafter"] = pts + 40
    
    result["reproc"] = 0

    return result

def X3(reproc,pts,ph1,ph2,ph3,ph4,ph5):
    result = resulttemplate.copy()
    
    result["pointsafter"] = pts*3
    result["reproc"] = 0

    return result

def Hope(reproc,pts,ph1,ph2,ph3,ph4,ph5):
    result = resulttemplate.copy()
    
    result["pointsafter"] = pts +5
    if ph5 == 1:
        result["pointsafter"] = ph4*1.2 
    result["reproc"] = 0

    return result

def Dreams(reproc,pts,ph1,ph2,ph3,ph4,ph5):
    result = resulttemplate.copy()
    
    result["pointsafter"] = pts +5
    if ph5 == 1:
        result["pointsafter"] = ph4*1.2 
    result["reproc"] = 0

def Postmortem(reproc,pts,ph1,ph2,ph3,ph4,ph5):
    result = resulttemplate.copy()
    
    if pts<0:
        result["pointsafter"] = 0
    else:
        result["pointsafter"] = -pts
    
    result["reproc"] = 0

    return result

def Kebab(reproc,pts,ph1,ph2,ph3,ph4,ph5):
    result = resulttemplate.copy()

    result["pointsafter"] = 0
    if reproc == 1:
        result["reproc"] = reprocing(1,reproc)
        result["pointsafter"] = pts*4
    else:
        result["reproc"] = 1
    
    return result

def Red(reproc,pts,ph1,ph2,ph3,ph4,ph5):
    result = resulttemplate.copy()

    if pts <= -200:
        result["pointsafter"] = 300
    else:
        result["pointsafter"] = pts

    if ph3 == "Blue":
        if pts < 0:
            pts = pts*(-1)
        result["pointsafter"] = pts/2 + 300
    result["reproc"] = 0
    
    return result

def Blue(reproc,pts,ph1,ph2,ph3,ph4,ph5):
    result = resulttemplate.copy()

    if pts < 0:
        result["pointsafter"] = pts*(-0.5)
    else:
        result["pointsafter"] = pts
    result["reproc"] = 0
    
    return result

def Violent_Hunger(reproc,pts,ph1,ph2,ph3,ph4,ph5):
    result = resulttemplate.copy()

    if pts > 0:
       result["pointsafter"] = pts*(-3) 
    else:
       result["pointsafter"] = 100 + 100*((pts*(-1))/200) 
    result["reproc"] = 0
    
    return result

def Hex(reproc,pts,ph1,ph2,ph3,ph4,ph5):
    result = resulttemplate.copy()

    result["pointsafter"] = pts
    if reproc == 1:
        result["reproc"] = reprocing(1,reproc)
        result["pointsafter"] = pts*(-2)
    else:
        result["reproc"] = 1
    
    return result

def White_Monster(reproc,pts,ph1,ph2,ph3,ph4,ph5):
    result = resulttemplate.copy()

    result["pointsafter"] = pts
    result["reproc"] = 69  
    
    return result


#-----------Curses-----------------------

def Half(reproc,pts,ph1,ph2,ph3,ph4,ph5):
    result = resulttemplate.copy()

    result["pointsafter"] = pts/2
    result["reproc"] = 0

    return result

def Minus20(reproc,pts,ph1,ph2,ph3,ph4,ph5):
    result = resulttemplate.copy()

    result["pointsafter"] = pts-20
    result["reproc"] = 0

    return result