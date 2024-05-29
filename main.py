from models.data import users
from utils.crud import read_users


if __name__ == "__main__":
        print("Witaj użytkowniku")
        while True:
            print("Menu:")
            print("0.Zakoncz program")
            print("1.Wyswietl co u znajomych")
            manu_option: str = input("Dokonaj wyboru")
            if manu_option == "0":
                print("Program kończy prace")
                break
            if manu_option == "1":
                read_users(users)