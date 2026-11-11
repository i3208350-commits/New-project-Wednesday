from itertools import count
import functions.functions as f
import rations.rations as r


def main():
    while True:
        print("1. Start New Game ")
        print("2. View Game History")
        print("3. View Statistics ")
        print("4. Exit ")

        choice = input("choice___:").strip()
        if choice == "1":
            f.start_game()
        elif choice == "2":
            o = r.lpad()
            if not o:
                print("No games")
            else:
                for idx, game in enumerate(o, 1):
                    print(f"Player: {game.get('player_name')}")
                    print(f"Rounds: {game.get('rounds')}")
                    print(f"Score: {game.get('player_score')} - {game.get('computer_score')}")
                    print(f"Winner: {game.get('winner')}")
        elif choice == "3":
            d = r.lpad()
            if not d:
                print("No games played yet.")
                continue
            computr = 0
            player = 0

            for i in d:
                winner = str(i.get("winner", "")).lower()
                player_name = str(i.get("player_name", "")).lower()
                if winner == "computer":
                    computr += 1
                elif winner == "player" or winner == player_name:
                    player += 1
            draw = len(d) - computr - player
            umber_of_games = len(d)
            if umber_of_games > 0:

                Victory_statistics_computer = (computr / umber_of_games) * 100
                Victory_statistics_player = (player / umber_of_games) * 100
            else:
                Victory_statistics_computer = 0
                Victory_statistics_player = 0
            print(f"Number of games:   {umber_of_games}")
            print(f"  Number of computer wins:    {computr}")
            print(f"  Number of player wins:    {player}")
            print(f"  Number of draw wins:    {draw}")
            print(f"Computer win percentage   {Victory_statistics_computer}")
            print(f"Computer win player   {Victory_statistics_player}")

        if choice == "4":
            break


if __name__ == "__main__":
    main()