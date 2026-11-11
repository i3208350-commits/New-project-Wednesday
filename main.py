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
            for i in o:
                print(i)
        # if choice == "3":

        if choice=="0":
            break


if __name__ == "__main__":
    main()