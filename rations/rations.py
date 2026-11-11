import random

import json
player_score=0
computer_score=0
new_listi=[]
player_1=0
computer_1=0
m=[]

def non_empty_check(x):
    return bool(str(x).strip())

def number_check(x):
    if isinstance(x,int) and x>0 and x<11:
        return True
    return False

def roll_dice():
    x=(random.randint(1, 6))
    return x

def victory_check(player,player_score,computer,computer_score):
    if player > computer:
         player_score += 1
    if player < computer:
         computer_score += 1
    if computer_score>player_score:
        contemporary_conductor="computer"
        return contemporary_conductor
    if computer_score<player_score:
        contemporary_conductor="player"
        return contemporary_conductor
    if computer_score==player_score:
        contemporary_conductor="draw"
        return contemporary_conductor


def victory(player,player_score,computer,computer_score):
    if player > computer:
         return player_score + 1
    if player < computer:
         return computer_score + 1

def play_round(i,player_score,computer_score,new_game):
    player=roll_dice()
    computer = roll_dice()
    print(f"The results of the round are: player: {player} computer:  {computer}")
    u=victory_check(player,player_score,computer,computer_score)
    l=victory(player, player_score, computer, computer_score)
    game = {"round": i+1, "player_dice": player, "computer_dice":computer, "winner": u}
    if game["winner"]=="player":
        new_game["player_score"]+=1
    if game["winner"] == "computer":
        new_game["computer_score"]+=1
    new_listi.append(game)

    victory_check(player, player_score, computer, computer_score)
    return new_listi





def display_game_json(m):
    with open("game_history.json", "w", encoding="utf-8") as file:
        json.dump(m, file, indent=2, ensure_ascii=False)

def lpad():
    try:
        with open("game_history.json", "r", encoding="utf-8") as file:
            datao=json.load(file)
            return datao
    except Exception:
        return []



def calculate_winner(player_score,computer_score):
    if player_score > computer_score:
        return "player"
    if player_score < computer_score:
        return "computer"
    if player_score == computer_score:
       return "Draw"


