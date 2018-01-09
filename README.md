# Battleship-AI
Battleship game with probalistic learning 

## Introduction
Battleship is a two-player grid-based game. Both players have ships of different sizes and have them concealed from the other player. They have to guess the position of the opponent's ships and attack. The playes get alternative turns. The winner is the one that destroys all the shipsof other one first. 

## Implementation
The purpose of the project is to introduce artificial intelligence in the game so that the players can guess the position of other player's ships more precisely. The way I did it is using probabilistic approach. Each player learns which grid position it found the ship most of the times after playing many games and the position has the highest probability of having the opponent's ship. So it hits that position. If ship is found at that position, the probability of that position having the ship in next games increases. If not found, the probability decreases and the player hits the next most probable position next time. 
