from shared.data_processor import DateProcessor

class User:

    def __init__(self, data):
        self.index = data[0]
        self.user_id = data[1]
        self.username = data[2]
        self.followers_count = int(data[3])
        self.location = data[4]
        self.sex = data[5]
        self.date_of_creation = DateProcessor.parse_dateformat(data[6], "%d/%m/%Y").date()

    def __str__(self):
        return (f"{self.index} {self.user_id} {self.username} {self.followers_count} {self.location} "
                f"{self.sex} {self.date_of_creation}")
