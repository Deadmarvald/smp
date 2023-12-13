import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

ASCII_ART_GENERATOR = "./data/lab3/output.txt"
ASCII_ART_GENERATOR_OUTPUT = "./data/lab4/output.txt"
OWN_ASCII_ART_GENERATOR_OUTPUT_FONT = "./data/lab4/fori.txt"
FIGURE_2D = "./data/lab5/2d.txt"
FIGURE_3D = "./data/lab5/3d.txt"
TWITTER_ACC_INFO_JSON = "./data/lab7/result.json"
TWITTER_ACC_INFO_CSV = "./data/lab7/result.csv"
TWITTER_ACC_INFO_TXT = "./data/lab7/result.txt"
DIFFERENCE_IN_THOUSANDS_HISTOGRAM = "./data/lab8/difference-in-thousands-histogram.png"
SEX_PIE_CHART_PHOTO = "./data/lab8/sex-pie-chart.png"
STATE_BAR_CHART_PHOTO = "./data/lab8/state-bar-chart.png"
COMBINED_DIAGRAM_PHOTO = "./data/lab8/combined-diagram.png"
USERS_DATA = "./data/lab8/users.csv"

# credentials
# used for service RapidApi for Twitter API
X_RAPID_API_KEY = "ee8508bd6dmshae5f9005d644543p131c2djsn551016d9c8c9"
# used for service RapidApi for Twitter API
X_RAPID_API_HOST = "twitter154.p.rapidapi.com"
# urls
GET_PERSONAL_PROFILE = "https://twitter154.p.rapidapi.com/user/details"
