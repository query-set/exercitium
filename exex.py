from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def start():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    # driver = webdriver.Remote(
    #     command_executor="http://127.0.0.1:4444/wd/hub",
    #     options=options,
    #     desired_capabilities=DesiredCapabilities.FIREFOX)
    page = driver.get("https://exercism.io/")
    print("-----")
    print(dir(page))
    print("-----")
    # soup = BeautifulSoup(open(page), features="lxml")
    # print(type(soup))
    driver.quit()


if __name__ == "__main__":
    start()
