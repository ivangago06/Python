
class Participant:
    def __init__(self):
        self.points = 0
        self.choice = ""

class GameRound:

 class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant()
        self.secondParticipant = Participant()

class Square:
     def __init__(self):
         self.height = 2
         self.width = 2
     def set_side(self, new_side):
         self.height = new_side
         self.width = new_side
     def get_height(self):
          return self.__height
     def set_height(self, h):
          if h >= 0:
              self.__height = h
          else:
              raise Exception("value needs to be 0 or larger")

square = Square()
square.__height = 3 # raises AttributeErrorre