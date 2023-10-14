'''Implement a class called Player that represents a cricket player. The Player class should have a method called play() which prints "The player is playing cricket. Derive two classes, Batsman and Bowler, from the Player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object. '''
class player:
  def play(self):
    print("The player is playing cricket.")
class batsman(player):
  def play(self):
    print("The batsman is batting.")
class bowler(player):
  def play(self):
    print("The bowler is bowling.")
batsman=batsman()
bowler=bowler()
batsman.play()
bowler.play()
    