import schedule
import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
input('Enter anything after scanning QR code')

def job():
    print("I'm working...")
    name = "Palak"
    msg = "Hi Palak jadi, pagal, magaj vagarni!!!!!!!!!!"
    count = 1
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
        button.click()







schedule.every(1).seconds.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)