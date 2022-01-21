from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from sys import platform
import time
import re
import config


print("\nSETTING UP VARIABLE")
user_n = getattr(config, "username")
pass_w = getattr(config, "password")
headless = getattr(config, "headless")
options = Options()


if platform == "linux" or platform == "linux2":
    chrm = Service('./chromedriver')
else:
    chrm = Service('./chromedriver.exe')


print("CHECKING CREDENTIALS")
if not bool(user_n) or bool(pass_w) == False:
    print("Please add your kingdomlikes.com username and password in config.py")
    exit(0)
else:
    print("FOUND CREDENTIALS")


print("CHECKING SETTINGS")
if headless.lower() == "true":
    print("HEADLESS ENABLED")
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
else:
    print("HEADLESS DISABLED")
    options.add_argument("--log-level=3")


driver = webdriver.Chrome(service=chrm, options=options)


def ctimer(t):
    while t:
        mins = t // 60
        secs = t % 60
        timer = 'Waiting for {:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


def login():
    print()
    print("OPENING WEBSITE https://kingdomlikes.com/")
    driver.get("https://kingdomlikes.com")

    print()
    print("PLEASE WAIT WHILE WE LOGIN")
    username = driver.find_element(By.NAME, "email")
    username.send_keys(str(user_n))
    password = driver.find_element(By.NAME, "password")
    password.send_keys(str(pass_w) + Keys.RETURN)
    print("DONE")


def check_points():
    print()
    ctimer(5)
    earned_points = driver.find_element(By.XPATH, "//*[@id='divpoints']/h4").text
    print("You currently have " + earned_points + "\n")


def goto_free_points():
    print()
    ctimer(5)
    print("NAVIGATING TO PAGE https://kingdomlikes.com/free_points")
    free_points = driver.find_element(By.XPATH, "//img[@class='icon min sprite sprite-thumb-up120']")
    free_points.click()


def youtube_view():
    print()
    ctimer(5)
    print("NAVIGATING TO PAGE https://kingdomlikes.com/free_points/youtube-views")
    youtube_views = driver.find_element(By.XPATH, "//a[@href='https://kingdomlikes.com/free_points/youtube-views']")
    youtube_views.click()


def web_traffic_view():
    print()
    ctimer(5)
    print("NAVIGATING TO PAGE https://kingdomlikes.com/free_points/web-traffic")
    web_traffics = driver.find_element(By.XPATH, "//a[@href='https://kingdomlikes.com/free_points/web-traffic']")
    web_traffics.click()


def link_clicker():
    print()
    print("WAITING FOR PAGE TO REFRESH")
    print()
    ctimer(10)
    link_title = driver.find_element(By.XPATH, "//div[@data-token='999999999']").text
    print()
    print()
    print("Title : " + str(link_title))

    time_length = driver.find_element(By.XPATH, "//*[@id='idpage5']/div/div[5]/h5").text
    time_length_split = re.split("[/ :]", time_length)
    time_minutes = int(time_length_split[5])
    time_seconds = int(time_length_split[6])
    min2sec = time_minutes * 60
    total_time_length = min2sec + time_seconds
    print()
    print("Required time is " + str(time_length_split[5]) + " min and " + str(time_length_split[6]) + " sec.")

    clicker = driver.find_element(By.XPATH, "//button[@class='button blue']")
    clicker.click()
    print()
    ctimer(total_time_length)


def youtube_loop():
    youtube_view()
    while True:
        try:
            link_clicker()
            check_points()
        except:
            print("No Available website to view. Will now wait for 150 seconds then switch to web traffic")
            ctimer(150)
            goto_free_points()
            web_traffic_loop()
        else:
            youtube_loop()


def web_traffic_loop():
    web_traffic_view()
    while True:
        try:
            link_clicker()
            check_points()
        except:
            print("No Available website to view. Will now wait for 150 seconds then switch to youtube view")
            ctimer(150)
            goto_free_points()
            youtube_loop()
        else:
            web_traffic_loop()


login()
check_points()
goto_free_points()
youtube_loop()

# EXIT
driver.quit()
