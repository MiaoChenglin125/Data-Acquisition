# encoding: utf-8
'''
  @author 李华鑫
  @create 2020-10-10 11:41
  Mycsdn：https://buwenbuhuo.blog.csdn.net/
  @contact: 459804692@qq.com
  @software: Pycharm
  @file: 超级鹰图片验证.py
  @Version：1.0

'''
from time import sleep
from selenium import webdriver
from PIL import Image
from chaojiying import Chaojiying_Client
import time

screen_name = "./screen.png"
code_name = "./code.png"

def save_screen(driver, filename):
    # 访问网页
    # driver.get('http://www.chaojiying.com/user/login/')
    url = 'https://ids.tongji.edu.cn:8443/nidp/app/login?id=Login&sid=0&option=credential&sid=0&target=https%3A%2F%2Fids.tongji.edu.cn%3A8443%2Fnidp%2Foauth%2Fnam%2Fauthz%3Fscope%3Dprofile%26response_type%3Dcode%26redirect_uri%3Dhttps%3A%2F%2F1.tongji.edu.cn%2Fapi%2Fssoservice%2Fsystem%2FloginIn%26client_id%3D5fcfb123-b94d-4f76-89b8-475f33efa194'
    driver.get(url)



def save_code(src, dest, rectangle):
    # 加载屏幕图
    img = Image.open(src)
    # 截取
    img_new = img.crop(rectangle)
    # 保存
    img_new.save(dest)


def decern_code(filename):
    """识别"""
    chaojiying = Chaojiying_Client('19121712563', '67537mcl', '927288')  # 用户中心>>软件ID 生成一个替换 96001
    im = open(filename, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    content = chaojiying.PostPic(im, 9004)  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    return content.get("pic_str")


def login(driver, username, password, code):
    """登录"""
    # driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input").send_keys(username)
    # driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input").send_keys(password)
    # driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input").send_keys(code)
    # driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input").click()
    # 进入子界面(传网址或0-第一个frame)
    # driver.switch_to.frame(0)
    driver.find_element_by_xpath('//*[@id="username"]').send_keys("1851804")
    driver.find_element_by_xpath('//*[@id="password"]').send_keys("67537mclL")
    driver.find_element_by_xpath('//*[@id="reg"]').click()
    time.sleep(2)
    print(driver.title)
    # 保存当前网页图片
    driver.save_screenshot("./screen.png")
    if driver.title == "Tongji University Login":
        return False
    else:
        return True


def main():
    """主程序"""
    # 驱动文件路径
    driverfile_path = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
    # 启动浏览器
    driver = webdriver.Chrome(driverfile_path)
    # 最大化
    driver.maximize_window()
    # 循环
    while True:
        # 保存屏幕图片
        save_screen(driver, filename=screen_name)
        # 保存验证码图片
        save_code(screen_name, code_name, (1022, 495, 1521, 813))
        # 识别验证码图片
        code = decern_code(code_name)
        # 登录
        ret = login(driver, "1851804", "67537mclL", code)
        if ret:  # 登录成功
            print("登录成功")
            break
        else:  # 登录失败
            print("失败...重新再来...")
    # 退出
    #driver.quit()


if __name__ == '__main__':
    main()


