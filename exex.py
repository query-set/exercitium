import json
from typing import Tuple

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


def fetch_login_data() -> Tuple[str, str]:
    with open(PASS_FILE, "r") as f:
        data = json.loads(f.read())
        return data["email"], data["password"]


def start():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    e, p = fetch_login_data()
    driver.get(LOGIN_URL)
    driver.find_element_by_id("user_email").send_keys(e)
    driver.find_element_by_id("user_password").send_keys(p)
    driver.find_element_by_name("button").click()
    driver.get(TRACK_URL)


if __name__ == "__main__":
    start()
