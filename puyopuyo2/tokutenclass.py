

class Tokuten():
    def __init__(self):
        self.behind = 0
        self.behind_behind = 0
        self.atack = 0
        self.end = 0
        self.hyouji = 0

   
    def sousai(self,aite,t):
        if self.behind_behind != 0 and t != 0:
            t += self.behind_behind
            self.behind_behind = 0
        if aite.behind == 0 and aite.atack == 0:
            self.behind += t
        elif aite.behind ==0:
            aite.atack -= t
            if aite.atack < 0:
                self.behind -= aite.atack
                aite.atack = 0
        else:
            aite.behind -= t
            if aite.behind < 0:
                aite.atack += aite.behind
                aite.behind = 0
            if aite.atack < 0:
                self.behind -= aite.atack
                aite.atack = 0
