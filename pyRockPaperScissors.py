import random

option= ["rock", "paper", "scissors"]
def play():
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
  play= int(input("\nChoose the number that corresponds with the move you want to make\n> "))
  #play=play.lower();
  if play!=1 and play!=2 and play!=3:
    print("Invalid Play!")
  elif play==1:
    userplay= option[0]
  elif play==2:
   userplay= option[1]
  elif play==3:
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
    userplay= Human()
    randomplay= Computer()
    print("\n",userplay,"vs",randomplay,"\n")
    if (userplay=="rock" and randomplay=="paper"):
      uscore=uscore+1
      print(name,"won")
    elif (randomplay=="rock" and userplay=="paper"):
      cscore=cscore+1
      print("Computer won")
    elif (userplay=="scissors" and randomplay=="paper"):
      uscore=uscore+1
      print(name,"won")
    elif (randomplay=="scissors" and userplay=="paper"):
      cscore=cscore+1
      print("Computer won")
    elif (userplay=="rock" and randomplay=="scissors"):
      uscore=uscore+1
      print(name,"won")
    elif (randomplay=="rock" and randomplay=="scissors"):
      cscore=cscore+1
      print("Computer won")
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
