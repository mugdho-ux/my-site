from selenium import webdriver
from selenium.webdriver.common.by import By
import os

def test_homepage():
    # Use relative path for ChromeDriver or ensure it's in PATH
    driver = webdriver.Chrome()  
    
    # Jenkins workspace environment variable
    workspace = os.getenv('WORKSPACE', '.')  
    driver.get(f"file://{workspace}/index.html")
    
    heading = driver.find_element(By.TAG_NAME, "h1").text
    assert heading == "Welcome to My Website!", f"Heading mismatch: {heading}"
    
    driver.quit()

if __name__ == "__main__":
    test_homepage()
