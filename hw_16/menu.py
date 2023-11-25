import sys
import json

from diarybook import Diary, DiaryBook
from util import read_from_json_into_application
from users import User

class Menu:

    def __init__(self):
        self.diarybook = DiaryBook()
        self.current_user = User()

        """
        მოწმდება ბაზაში უკვე არის თუ არამომხმარებელი შესაბამისი სახელით და პაროლით, 
        და თუ არ არის, იქმნება ახალი მომხარებელი უკვე შეყვანილი მონაცემების საფუძველზე.
        """
        with open('users.json', 'r') as file:
            exists = False
            users = json.load(file)
            for user in users["users"]:
                if user["username"] == self.current_user.username and user["password"] == self.current_user.password:
                    exists = True
                    self.current_user.user_id = user["id"]
                    break
            if not exists:
                self.current_user.create_user()


        self.choices = {
            "1": self.show_diaries,
            "2": self.add_diary,
            "3": self.search_diaries,
            "4": self.populate_database,
            '5': self.quit,
            '6': self.sorted_diary
        }

    def display_menu(self):
        print(""" 
                     Notebook Menu  
                    1. Show diaries
                    2. Add diary
                    3. Search diaries
                    4. Populate database
                    5. Quit program
                    6. Sorted Diary
                    """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_diaries(self):
        """
        დღიურების ფაილიდან ამოიკითხება ჩანაწერები და მხოლოდ ისინი დაიბეჭდება,
        რომლებიც აპლიკაციის მიმდინარე სესიის მომხმარებელს ეკუთვნის
        """
        with open("diaries.json", "r") as file:
            diaries = json.load(file)
            for diary in diaries["diaries"]:
                if self.current_user.user_id == diary["owner"]:
                    print(f"{diary['memo']}")


    def add_diary(self):
        """
        მომხმარებლის შეყვანილ მონაცემებს ემატება მომხმარებლის უნიკალური კოდი და
        new_diary ბრძანებით შეიქმნება ახალი ჩანაწერი დღიურების ფაილში
        """
        memo = input("Enter a memo:         ")
        tags = input("add tags:             ")
        owner = self.current_user.user_id
        self.diarybook.new_diary(memo, owner, tags)
        print("Your note has been added")

    def search_diaries(self):
        """
        მიწოდებული საძებო ტექსტის მიხედვით მოიძებნება ყველა ჩანაწერი, რომელიც
        ამ სიტყვებს შეიცავს და შემდეგ დაიბეჭდება მხოლოდ ისინი, რომლებიც მიმდინარე
        მომხმარებელს ეკუთვნის.
        """
        filter_text = input("Search for:  ")
        diaries = self.diarybook.search_diary(filter_text)
        for diary in diaries:
            if diary["owner"] == self.current_user.user_id:
                print(f"{diary['memo']}")

    def quit(self):
        print("Thank you for using diarybook today")
        sys.exit(0)

    def populate_database(self):
        diaries1 = read_from_json_into_application('data.json')
        for diary in diaries1:
            self.diarybook.diaries.append(diary)


    def sorted_diary(self, option="m"):
        """
        მოიძებნება ყველა ჩანაწერი, რომელიც რომლებიც მიმდინარე
        მომხმარებელს ეკუთვნის და დალაგდება ანბანის მიხედვით (დიდ ასოებს
        პატარა ასოებთან შედარებით დალაგებისას უპირატესობა გააჩნია).
        """
        with open("diaries.json", "r+") as file:
            diaries = json.load(file)
            sorted_diaries = []
            for diary in diaries["diaries"]:
                if diary["owner"] == self.current_user.user_id:
                    sorted_diaries.append(diary['memo'])
            print(sorted(sorted_diaries))



if __name__ == "__main__":
    Menu().run()
