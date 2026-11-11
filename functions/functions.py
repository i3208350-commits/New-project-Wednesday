
import rations.rations  as r
new_game={"player_name": 0,
           "rounds": 3,
           "player_score": 0,
           "computer_score": 0,
            "winner": 0,
"            results": []}

def start_game(new_game):
    player_score=0
    computer_score=0
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
        r.play_round(i,player_score,computer_score,new_game)

    t = r.calculate_winner(player_score, computer_score)
    # print(r.calculate_winner(player_score,computer_score))
    new_game = {"player_name":player_nameinput,
                    "rounds": several_rounds,
                    "player_score": player_score,
                    "computer_score": computer_score,
                    "winner": t,
                    "results": [r.new_listi]}

    if new_game["player_score"]>new_game["computer_score"]:
        print("Player won!!")
    if new_game["player_score"]<new_game["computer_score"]:
        print("computer won!!")
    e = r.lpad()
    r.m.append(e)
    r.display_game_json(new_game)


    print(new_game)
