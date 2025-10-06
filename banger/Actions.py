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