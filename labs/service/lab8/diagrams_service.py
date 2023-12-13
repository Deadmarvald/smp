from collections import Counter
import abc
from matplotlib import pyplot as plt
from config import (DIFFERENCE_IN_THOUSANDS_HISTOGRAM, SEX_PIE_CHART_PHOTO,
                    STATE_BAR_CHART_PHOTO, COMBINED_DIAGRAM_PHOTO, logger)
from entity.user import User
from shared.file_processors import CsvProcessor as csv_processor


class DiagramService(abc.ABC):

    def __init__(self):
        self._users = []


class DiagramServiceImpl(DiagramService):

    def __init__(self, file_path: str):
        super().__init__()
        logger.info("Loading user data from CSV")
        users_dataframe = csv_processor.read(file_path)
        for data in users_dataframe.values:
            self._users.append(User(data))

    def get_difference_in_thousands(self):
        return [user.followers_count / 1000 for user in self._users]

    def get_sex(self):
        return [user.sex for user in self._users]

    def get_state(self):
        return [user.location for user in self._users]

    def create_difference_in_thousands_histogram(self, has_to_be_downloaded=False):
        logger.info("Creating histogram of difference in thousands")
        difference_in_thousands = self.get_difference_in_thousands()
        plt.hist(difference_in_thousands, bins=20, edgecolor='black')
        plt.title('Histogram of Followers Count in Thousands')
        plt.xlabel('Thousands of Followers')
        plt.ylabel('Frequency')
        if has_to_be_downloaded:
            plt.savefig(DIFFERENCE_IN_THOUSANDS_HISTOGRAM)
        plt.show()

    def create_sex_pie_chart(self, has_to_be_downloaded=False):
        logger.info("Creating sex pie chart")
        sex = self.get_sex()
        sex_counter = Counter(sex)
        plt.pie(list(sex_counter.values()), labels=list(sex_counter), startangle=90, colors=['blue', 'pink'])
        plt.title('Pie Chart of User Sex')
        if has_to_be_downloaded:
            plt.savefig(SEX_PIE_CHART_PHOTO)
        plt.show()

    def create_state_bar_chart(self, has_to_be_downloaded=False):
        logger.info("Creating state bar chart")
        state = self.get_state()
        state_counter = Counter(state)
        plt.figure(figsize=(10, 6))
        plt.bar(state_counter.keys(), state_counter.values(), color='green')
        plt.title('Bar Chart of Users per State')
        plt.xlabel('State')
        plt.ylabel('Number of Users')
        plt.xticks(rotation=45)
        if has_to_be_downloaded:
            plt.savefig(STATE_BAR_CHART_PHOTO)
        plt.show()

    def create_combined_diagram(self, has_to_be_downloaded=False):
        logger.info("Creating combined diagram")
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 15))

        difference_in_thousands = self.get_difference_in_thousands()
        ax1.hist(difference_in_thousands, bins=20, color='blue', edgecolor='black')
        ax1.set_title('Histogram of Followers Count in Thousands')

        sex = self.get_sex()
        sex_counter = Counter(sex)
        ax2.pie(list(sex_counter.values()), labels=list(sex_counter), startangle=90, colors=['blue', 'pink'])
        ax2.set_title('Pie Chart of User Sex')

        state = self.get_state()
        state_counter = Counter(state)
        ax3.bar(state_counter.keys(), state_counter.values(), color='green')
        ax3.set_title('Bar Chart of Users per State')
        ax3.tick_params(axis='x', labelrotation=45)

        plt.tight_layout()

        if has_to_be_downloaded:
            plt.savefig(COMBINED_DIAGRAM_PHOTO)

        plt.show()
        logger.info("Combined diagram created successfully")
