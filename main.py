from itertools import count
import functions.functions as f
import rations.rations as r


def main():
    while True:
        print("1. Start New Game ")
        print("2. View Game History")
        print("3. View Statistics ")
        print("4. Exit ")


        choice=input("choice___:")
        if choice=="1":
            f.start_game(f.new_game)
        if choice=="2":
            o=r.lpad()
            # for i in o:
            print(o)
        if choice == "3":
            d=r.lpad()
            computr=0
            player=0

            for i in d:
                if i["winner"]=="computer":
                    computr+=1
                if i["winner"]=="player":
                    player+=1
            draw=len(d)-computr-player
            Victory_statistics_computer=len(d)/computr
            Victory_statistics_player = len(d) / player
            umber_of_games=len(d)
            print(f"Number of games:   {umber_of_games}")
            print(f"  Number of computer wins:    {computr}")
            print(f"  Number of player wins:    {player}")
            print(f"  Number of draw wins:    {draw}")
            print(f"Computer win percentage   {Victory_statistics_computer}")
            print(f"Computer win player   {Victory_statistics_player}")

        if choice=="4":
            break


if __name__ == "__main__":
    main()