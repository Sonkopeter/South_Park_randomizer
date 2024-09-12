from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time

#Passing Robot test

def Am_I_robot(driver):
    ActionChains(driver).move_by_offset(510, 350).click().perform()
    time.sleep(1)   
    
    return
    
#Selecting random episode  
 
def navigate_window_first(driver):
    
    scroll_origin = ScrollOrigin.from_viewport(510, 350)
    ActionChains(driver)\
        .scroll_from_origin(scroll_origin, 0, 800).perform()  
        
    hoverable = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td[2]/div/div[2]/span")
    ActionChains(driver)\
        .move_to_element(hoverable)\
        .perform()  
    time.sleep(1)
    
    click_button = driver.find_element(by=By.LINK_TEXT, value="Этого мульта")                       
    click_button.click()
    time.sleep(1) 
      
    return

#Setting original voiceover, entering full screen mode

def navigate_window_second(driver):
    click_button_language = driver.find_element(by=By.LINK_TEXT, value="Оригинал")                       
    click_button_language.click()
    time.sleep(1)
    
    hoverable1 = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td[1]/div[2]/div[2]/div[4]/pjsdiv/pjsdiv[4]/pjsdiv[11]/pjsdiv[3]")
    ActionChains(driver)\
        .move_to_element(hoverable1)\
        .perform()
    ActionChains(driver).click().perform()
    #time.sleep(1)
    
    ActionChains(driver).move_by_offset(-100, -100).click().perform()
    
    return

   
def __main__():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://southpark.mult-fan.tv/')
    
    Am_I_robot(driver)
    navigate_window_first(driver)
    navigate_window_second(driver)
        
    time.sleep(1500) #25min timer

    return 


__main__()