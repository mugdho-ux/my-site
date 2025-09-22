from selenium import webdriver
from selenium.webdriver.common.by import By

def test_homepage():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get("http://localhost:8000/index.html")
    heading = driver.find_element(By.TAG_NAME, "h1").text
    assert heading == "Welcome to My Website!"
    driver.quit()
