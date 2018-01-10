import random

option= ["rock", "paper", "scissors"]
def play():
  play= int(input("\nChoose the number that corresponds with the move you want to make\n> "))
  return play;
  """
  This function simply returns the option the player selected.
  """

def Computer():
  randomplay= random.choice(option)
  return randomplay
  """
  This function should simply return the computers SINGLE choice of rock, paper, or scissors IN LOWERCASE
  """

def Human():
  for x in range(0,3):
    print(str(x+1)+".\t",option[x])
  player=play()
  if player!=1 and player!=2 and player!=3:
    print("Invalid Play!")
  elif player==1:
    userplay= option[0]
  elif player==2:
   userplay= option[1]
  elif player==3:
    userplay= option[2]
  return userplay
  """
  This function should display a menu, prompting the player to select either rock, paper, or scissors and return what the player 
  selected IN LOWERCASE . If the player selects an invalid option, display the error message "Invalid Play"
  """

def main():
  cscore=0
  uscore=0
  print("Welcome To PyRock Paper Scissors Best of 3\n")
  name=input("Enter Name: ")
  for x in range(1,4):
    user= Human()
    comp= Computer()
    print("\n",user,"vs",comp,"\n")
    if (user=="paper" and comp=="rock"):
      uscore=uscore+1
      print(name,"won")
    elif (comp=="paper" and user=="rock"):
      cscore=cscore+1
      print("Computer won")
    elif (user=="scissors" and comp=="paper"):
      uscore=uscore+1
      print(name,"won")
    elif (comp=="scissors" and user=="paper"):
      cscore=cscore+1
      print("Computer won")
    elif (user=="rock" and comp=="scissors"):
      uscore=uscore+1
      print(name,"won")
    elif (comp=="rock" and user=="scissors"):
      cscore=cscore+1
      print("Computer won")
    else:
      print("Draw")
    print("\n")
  print(name,"Score:",uscore)
  print("Computer Score:",cscore)
  if cscore>uscore:
    print("Computer won the best of 3 match")
  elif uscore>cscore:
    print(name,"won the best of 3 match")
  else:
    print("There was a draw")
  """
  This function should prompt the player to enter his/her name, get the player's and computer's play, displays what the player and the 
  computer played and displays who won. Remember this is a best of 3 match so this function should also keep track of who won each round 
  and displays the final scores and the overall winner.
  """

if __name__ == '__main__':
	main()
