[![Build Status](https://travis-ci.org/IEEE-Python-Review/RockPaperScissors.svg?branch=master)](https://travis-ci.org/IEEE-Python-Review/RockPaperScissors)

# PyRock Paper Scissors
### Recreate this game to match this *EXACT* output

Welcome To PyRock Paper Scissors Best of 3

Enter Name: Lomar
1. Rock
2. Papar
3. scissors

Choose the number that corresponds with the move you want to make

\> 1

rock vs paper

Computer won

1. Rock
2. Papar
3. scissors

Choose the number that corresponds with the move you want to make

\> 3

scissors vs rock

Computer won

1. Rock
2. Papar
3. scissors

Choose the number that corresponds with the move you want to make

\> 2

paper vs scissors

Computer won

Lomar Score: 0

Computer Score: 3

Computer won the best of 3 match

You _MUST_ use the functions provided in pyRockPaperScissors.py to complete this task 
## DO NOT MAKE ANY CHANGES TO THE FUNCTION NAMES OR ELSE YOU WILL FAIL!

# Function Descriptions

## play():
This function simply returns the option the player selected.

### Computer():
This function should simply return the computers SINGLE choice of rock, paper, or scissors _IN LOWERCASE_

## Human():
This function should display a menu, prompting the player to select either *1 for rock, 2 for paper, or 3 scissors* and return what the player selected _IN LOWERCASE_ . If the player selects an invalid option, _RETURN_** the error message "Invalid Play"

## main():
This function should prompt the player to enter his/her name, get the player and computer play, check if the player made and invalid play and display the message "Invalid Play", displays what the player and the computer played and displays who won. For Example:
```
scissors vs rock
Computer won
```
or
```
scissors vs rock
PlayerName won
```
Remember this is a best of 3 match so this function should also keep track of who won each round and displays the final scores and the overall winner. For Example:
```
PlayerName Score: 0
Computer Score: 3
Computer won the best of 3 match
```
## Scoring
* For each win 1 point should be awarded
* For each draw 0 point should be awarded

## Testing
Now I have built a testing module you can use to test your solutions to make sure you on the right track. To use the test module simple run it like how you'd run any other python script.

## Submissions
This will be done via github classroom
