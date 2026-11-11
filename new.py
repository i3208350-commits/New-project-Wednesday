import rations.rations as r
import rations
new_game={"player_name": 0,
           "rounds": 3,
           "player_score": 0,
           "computer_score": 0,
            "winner": 0,
"            results": []}



def start_game(new_game):
    player_nameinput = input("What is the name of the actor:____")
    if not r.non_empty_check(player_nameinput):
        print("Entered an incorrect name.")
    try:
        several_rounds = int(input("several rounds___"))
        if not r.number_check(several_rounds):
            print("Entered an incorrect naumber.")

    except Exception:
        print("aror")
        return
    for i in range(several_rounds):
        r.play_round(i,player_score, computer_score, new_game)



def play_round(i, player_score, computer_score):
    player = roll_dice()
    computer = roll_dice()

def roll_dice(x):
    x=(random.randint(0, 6))
    return x