import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def commandHistory():
    history = driver.find_element(By.ID, "all")
    history.click()
    driver.fullscreen_window()


def start():
    global driver
    options = Options()
    options.add_experimental_option("detach", True)



    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("http://127.0.0.1:5500/web%20ui/index.html")

    driver.fullscreen_window()

