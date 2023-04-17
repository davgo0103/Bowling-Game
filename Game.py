rolls = []
class Game:
    def __init__(self):
        self.rolls = []
    
    def roll(self, pins):
        self.rolls.append(pins)
    
    def score(self):
        score = 0
        roll_index = 0
        for frame in range(10): #10個計分格
            if self.is_strike(roll_index): 
                score += 10 + self.strike_bonus(roll_index) #第一球全倒
                roll_index += 1
            elif self.is_spare(roll_index):
                score += 10 + self.spare_bonus(roll_index) #第二球全倒
                roll_index += 2
            else:
                score += self.frame_score(roll_index) 
                roll_index += 2
        return score
    
    def is_strike(self, roll_index): #如果全倒
        return self.rolls[roll_index] == 10
    
    def is_spare(self, roll_index): #第二球全倒
        return self.frame_score(roll_index) == 10
    
    def strike_bonus(self, roll_index): #第一球全倒額外獎勵
        return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
    
    def spare_bonus(self, roll_index): #第二球全倒額外獎勵
        return self.rolls[roll_index+2]
    
    def frame_score(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1]


def Play(arr):
    rolls = arr
    
    game = Game()
    
    for pins in rolls: #丟球
        game.roll(pins)

    print(game.score()) 
    return(game.score())


