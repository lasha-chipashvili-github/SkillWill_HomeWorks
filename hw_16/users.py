import json
import uuid

class User:
    """
    თუ არგუმენტების გარეშე შეიქმნება User კლასის ობიექტი, მისი ინიციალიზაციისას
    მომხმარებელს შესაძლებლობა ექნება კონსოლში შეიყვანოს შესაბამისი მონაცემები.
    """

    def __init__(self, username=None, password=None ):
        self.user_id = uuid.uuid4().hex
        if username is None:
            self.username = input("გთხოვთ შეიყვანოთ მომხმარებლის სახელი: ").lower()
        else:
            self.username = username.lower()
        if password is None:
            self.password = input("გთხოვთ შეიყვანოთ მომხმარებლის პაროლი: ").lower()
        else:
            self.password = password.lower()

        self.dairies = [] # აქ თავიდან ვფიქრობდი დღიურებისთვის მიმეცა id-ები და მომხმარებლების შესაბამისად აქ ჩამესვა. ახლა უფუნქციოა.

    def read_users(self):
        with open('users.json') as users:
            users = users.read()
        print(users)

    def create_user(self):
        """
        იქმნება მომხმარებელი უნიკალური კოდით, სახელით, პაროლით და იწერება შესაბამის ფაილში
        """
        with open('users.json', 'r') as file:
            users = json.load(file)

            user = {
                "id": self.user_id,
                "username": self.username,
                "password": self.password,
                "dairies": self.dairies
            }

            users["users"].append(user)

        with open('users.json', 'w') as data:
            json.dump(users, data, indent=4)



if __name__ == "__main__":
    user = User()
    user.create_user()
    user.read_users()
