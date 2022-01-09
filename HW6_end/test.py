from selenium import webdriver
import time
#实例化谷歌浏览器
driver=webdriver.Chrome(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
#访问网页

url='https://ids.tongji.edu.cn:8443/nidp/app/login?id=Login&sid=0&option=credential&sid=0&target=https%3A%2F%2Fids.tongji.edu.cn%3A8443%2Fnidp%2Foauth%2Fnam%2Fauthz%3Fscope%3Dprofile%26response_type%3Dcode%26redirect_uri%3Dhttps%3A%2F%2F1.tongji.edu.cn%2Fapi%2Fssoservice%2Fsystem%2FloginIn%26client_id%3D5fcfb123-b94d-4f76-89b8-475f33efa194'
driver.get(url)
#进入子界面(传网址或0-第一个frame)
# driver.switch_to.frame(0)
driver.find_element_by_xpath('//*[@id="username"]').send_keys("1851804")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("67537mclL")
driver.find_element_by_xpath('//*[@id="reg"]').click()
time.sleep(2)

