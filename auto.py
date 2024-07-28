from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup



#handling alert
def alertHandler(driver, accept):
    try:
        alert = driver.switch_to.alert
        if accept:
            alert.accept()
        else:
            alert.dismiss()
    except:
        pass

#find elements after loading and alert
def findElementSafe(type,text, accept = False):
    try:
        alertHandler(driver,accept)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((type,text)))
        time.sleep(1)
        return driver.find_element(type, text)
    
    except UnexpectedAlertPresentException:
        alertHandler(driver,accept)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((type,text)))
        time.sleep(1)
        return driver.find_element(type, text)

#auto-uploading articles
def upload( source:str ):
    try:
        global driver 
        driver = webdriver.Chrome()
        #login
        soup = BeautifulSoup(source, 'html.parser')
        titleText = soup.find('title').get_text()
        driver.get('https://testcarsleep.tistory.com/manage/newpost/')
        findElementSafe(By.CLASS_NAME,'btn_login').click()
        findElementSafe(By.ID,'loginId--1').send_keys('hw1115.lee1115@gmail.com')
        findElementSafe(By.ID,'password--2').send_keys('LHWlhw5050')
        findElementSafe(By.CLASS_NAME,'submit').click()
        #editor
        findElementSafe(By.ID,'editor-mode-layer-btn-open').click()
        findElementSafe(By.ID,'editor-mode-html').click()
        findElementSafe(By.ID,'post-title-inp', True).send_keys(titleText)
        findElementSafe(By.CSS_SELECTOR, ".CodeMirror ").click()
        findElementSafe(By.CSS_SELECTOR, ".CodeMirror textarea").send_keys(source)
        findElementSafe(By.ID,'publish-layer-btn').click()
        findElementSafe(By.ID,'publish-btn').click()
        driver.quit()
        return 0
    
    except:
        return 1