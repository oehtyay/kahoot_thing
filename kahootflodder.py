from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import time


s = Service("C:\\Users\\AlexO\\Desktop\\edgedriver_win64\\msedgedriver.exe")
driver = webdriver.Edge(service=s)


name = "e"
total_bots = 10
n = 0


while True:
    pin = input("Enter Kahoot Game PIN: ")
    if pin != "":
        break

url = "https://kahoot.it"


for a in range(total_bots+1):
    start = time.time()
    driver.execute_script("window.open('', '_blank');")  # Open a new tab
    driver.switch_to.window(driver.window_handles[n])

    try:
        driver.get(url)

        alert = driver.switch_to.alert
        alert.dismiss()
    except NoAlertPresentException:
        pass

    try:
        game = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="game-input"]')))
        game.send_keys(pin)

        enter = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '''//*[@id="root"]/div[1]/div/
            div/div/div[3]/div[2]/main/div/form/button'''))
        )
        enter.click()
        time.sleep(0.5)

        if driver.find_element(By.XPATH, '//*[@id="nickname"]').is_displayed():
            driver.find_element(By.XPATH, '//*[@id="nickname"]').send_keys(name)
            enter1 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '''//*[@id="root"]/div[1]/div/
                div/div/div[3]/div[2]/main/div/form/button'''))
            )
            enter1.click()
            name = name + "e"
            n = n + 1
            end = time.time()
            total_time = end - start
            print(f"Added a bot in {total_time:.2f} seconds.")
    except NoSuchElementException:
        print("Error: Incorrect Kahoot PIN")
        driver.quit()
        quit()

print(f"Successfully added {total_bots} bots")
driver.quit()
