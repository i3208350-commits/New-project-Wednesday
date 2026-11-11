
import rations.rations  as r
new_game={"player_name": 0,
           "rounds": 3,
           "player_score": 0,
           "computer_score": 0,
            "winner": 0,
            "results": []}

def start_game():
    player_score=0
    computer_score=0
    player_nameinput = input("What is the name of the actor:____").strip()
    if not r.non_empty_check(player_nameinput):
        print("Entered an incorrect name.")
    try:
        several_rounds = int(input("several rounds___"))
        if not r.number_check(several_rounds):
            print("Entered an incorrect naumber.")

    except Exception:
        print("aror")
    r.new_listi = []
    new_game = {"player_score": 0, "computer_score": 0}
    for i in range(several_rounds):
        r.play_round(i,player_score,computer_score,new_game)
    for i in r.new_listi:
        if i.get("winner") == "player":
            player_score += 1
        elif i.get("winner") == "computer":
            computer_score += 1
    t = r.calculate_winner(player_score, computer_score)
    if t == "player":
        winner_name = player_nameinput
    elif t =="computer":
        winner_name = "Computer"
    else:
        winner_name="Draw"



    new_game = {"player_name":player_nameinput,
                    "rounds": several_rounds,
                    "player_score": player_score,
                    "computer_score": computer_score,
                    "winner": winner_name,
                    "results": r.new_listi}

    if new_game["player_score"]>new_game["computer_score"]:
        print("Player won!!")
    elif new_game["player_score"]<new_game["computer_score"]:
        print("computer won!!")
    else:
        print("Draw!!")

    e = r.lpad()
    e.append(new_game)
    r.display_game_json(e)



