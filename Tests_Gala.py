from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get('https://rahulshettyacademy.com/loginpagePractise/')

driver.find_element(By.CSS_SELECTOR, "a.blinkingText").click()
windowsOpened =driver.window_handles
driver.switch_to.window(windowsOpened[1])
driver.implicitly_wait(4)
textNewWindow=driver.find_element(By.CSS_SELECTOR, "p.im-para:nth-child(2)").text
words=textNewWindow.split()
email=words[4]
driver.switch_to.window(windowsOpened[0])

driver.find_element(By.ID, "username1").send_keys(email)
driver.implicitly_wait(5)
driver.find_element(By.ID, "password").send_keys("1132")
driver.find_element(By.CSS_SELECTOR, "input[value='admin']").click()
driver.find_element(By.CSS_SELECTOR, "select.form-control").click()
driver.implicitly_wait(3)
driver.find_element(By.CSS_SELECTOR, "select option[value=teach]").click()
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "signInBtn").click()

element = WebDriverWait(driver, 4).until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/div[1]/div/div/div/div/form/div[1]'),"Incorrect username/password."))
errorMessage=driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/form/div[1]').text
print(errorMessage)
driver.quit()