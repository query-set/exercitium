import json
from typing import Tuple, List

from bs4 import BeautifulSoup, element
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Defaults:
PASS_FILE = "pass.json"
TRACK = "python"
EX = "sieve"

# Links storage
M = "https://exercism.io/"
LOGIN_URL = M + "users/sign_in"
TRACK_URL = M + f"my/tracks/{TRACK}"
EX_URL = M + f"my/solutions?exercise_id={EX}&track_id={TRACK}"
MOCKED = True
BS_FEAT = "lxml"

EX_DIV_CLS_NAME = "pure-u-1 pure-u-md-1-2 pure-u-lg-1-3"

# list of exercises class=pure-g exercises
# exercise  pure-u-1 pure-u-md-1-2 pure-u-lg-1-3
# completed = widged-side-exercise completed
# unlocked = widged-side-exercise unlocked
# in-progress = widged-side-exercise in-progress



def fetch_login_data() -> Tuple[str, str]:
    with open(PASS_FILE, "r") as f:
        data = json.loads(f.read())
        return data["email"], data["password"]


class Exercise:
    def __init__(self, src):
        """ Storage for singular exercise data retrieved from HTML. """
        self.src = src
        self.state, self.link = self._get_link_and_state(src)
        self.title = src.find("div", {"class": "title"}).text.strip()
        self.level = src.find("div", {"class": "stats"}).text.strip()
        self.topics = self._get_topics(src)

    def __str__(self):
        return self.title

    @staticmethod
    def _get_link_and_state(src: element.Tag) -> List[str]:
        marker = src.find("a", {"class": "widget-side-exercise"})
        return marker.attrs.get("class")[-1], marker.attrs.get("href")

    @staticmethod
    def _get_topics(src: element.Tag) -> List[str]:
        return [topic.text.strip() for topic in src.findAll("div", {"class": "topic"})]



def start():
    if not MOCKED:
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        e, p = fetch_login_data()
        driver.get(LOGIN_URL)
        driver.find_element_by_id("user_email").send_keys(e)
        driver.find_element_by_id("user_password").send_keys(p)
        driver.find_element_by_name("button").click()
        driver.get(TRACK_URL)
        soup = BeautifulSoup(driver.page_source, features=BS_FEAT)
    else:
        with open("html.html", "r") as f:
            soup = BeautifulSoup(f.read(), features=BS_FEAT)

    exercises = soup.findAll(
        "div", {"class": EX_DIV_CLS_NAME}
    )
    models = [Exercise(e) for e in exercises]
    print(len(models))
    return 0


if __name__ == "__main__":
    start()
