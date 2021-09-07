from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class igfollow:
    def scroll(self):
        pop_up_window = WebDriverWait(
            driver, 2).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='isgrP']")))
        last_height = driver.execute_script("return arguments[0].scrollHeight",pop_up_window)

        while True:

            driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);",pop_up_window)
            time.sleep(2)
            new_height = driver.execute_script("return arguments[0].scrollHeight",pop_up_window)
            if new_height == last_height:
                break
            last_height = new_height
        return 0







driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.instagram.com/")
driver.implicitly_wait(5)
soc=input("For logging in with instagram enter 'ig' and for logging in with facebook enter 'fb' :")
if soc=='fb':
    driver.find_element_by_css_selector('[class="sqdOP yWX7d    y3zKF     "]').click()
    driver.implicitly_wait(3)
    driver.find_element_by_id("email").send_keys("__Enter Facebook Email/No.__")
    driver.implicitly_wait(3)
    driver.find_element_by_id("pass").send_keys("__Enter Facebook Password__")
    driver.find_element_by_id("loginbutton").click()
    driver.implicitly_wait(10)
elif soc=='ig':
    driver.find_element_by_name('username').send_keys("__Enter Instagram Username__")
    driver.implicitly_wait(3)
    driver.find_element_by_name('password').send_keys("__Enter Instagram Password__")
    driver.implicitly_wait(3)
    driver.find_element_by_css_selector('[class="sqdOP  L3NKy   y3zKF     "]').click()
    driver.implicitly_wait(10)
else :
    print("You can either login through Facebook('fb') or Instagram('ig')!\nRerun the program and enter appropriate codewords")
    driver.close()
    exit()
driver.find_element_by_css_selector('[class="aOOlW   HoLwm "]').click()
driver.implicitly_wait(1)
driver.find_element_by_css_selector('[class="_2dbep qNELH"]').click()
driver.implicitly_wait(2)
driver.find_element_by_css_selector('[class="-qQT3"]').click()
driver.implicitly_wait(4)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
driver.implicitly_wait(4)

obj=igfollow()
obj.scroll()
list=[]
list=driver.find_elements_by_css_selector('[class="FPmhX notranslate  _0imsa "]')
erlist=[]
for elm in list:
    erlist.append(elm.text);
driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/button').click()
driver.implicitly_wait(4)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
driver.implicitly_wait(4)

obj.scroll()
flist=[]
flist=driver.find_elements_by_css_selector('[class="FPmhX notranslate  _0imsa "]')
inglist=[]
for elms in flist:
    inglist.append(elms.text)
print("All account who you follow but don't follow you back:-")
for name in inglist:
    if(name not in erlist ):
        print(name)

driver.quit()


