import datetime
import json


class Diary:
    """
    აქ შექმნილ დღიურის id-ს და დროს არ ვიყენებ არსად (რამდენადაც მახსოვს), მაგრამ წასაშლელად და
    ექსპერიმენტირებისთვის დრო აღარ მეყო.
    """
    last_id = 0

    def __init__(self, memo, owner, tags=' '):
        self.memo = memo
        self.tags = tags
        self.owner = owner
        self.creation_date = datetime.date.today()

        Diary.last_id += 1

        self.id = Diary.last_id

    def match(self, filter_text):
        with open("diaries.json", "r+") as file:
            diaries = json.load(file)
            return filter_text in diaries["memo"] or filter_text in self.diaries["tags"]


class DiaryBook:
    """
    აქ შეიძლება ამგვარი ინიციალიზაცია საჭირო არც იყოს, უბრალოდ დრო აღარ მეყო ექსპერიმენტებისთვის და
    აზრობრივად ბოლომდე გასაყოლად
    """
    def __init__(self):
        self.diaries = []

        """ განუხორციელებელი ვარიანტის ნარჩენები """
        # self.diaries = {
        # "memo" : memo,
        # "owner" : owner,
        # "tags" : tags
        #
        # }

    def new_diary(self, memo, owner, tags=' '):
        # self.diaries.append(Diary(memo, owner, tags)) # """ განუხორციელებელი ვარიანტის ნარჩენები """
        with open("diaries.json", "r+") as file:
            diaries = json.load(file)

            diary = {
                    "memo": memo,
                    "owner": owner,
                    "tags": tags
                     }

            diaries["diaries"].append(diary)

            with open('diaries.json', 'w') as data:
                json.dump(diaries, data, indent=4)



    def search_diary(self, filter_text):
        filtered_diaries = []
        with open("diaries.json", "r+") as file:
            diaries = json.load(file)
            for diary in diaries["diaries"]:
                if filter_text in diary["memo"] or filter_text in diary["tags"]:
                # if match(diary, filter_text): # ორიგინალი კოდის ნარჩენი
                    filtered_diaries.append(diary)
            return filtered_diaries


