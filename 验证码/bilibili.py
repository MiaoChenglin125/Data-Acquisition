from selenium import webdriver
from time import sleep
from PIL import Image
from selenium.webdriver import ActionChains
import random
import requests
from hashlib import md5
import logging

class Chaojiying_Client(object):
    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf-8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        logging.info(r.json())
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        logging.info(r.json())
        return r.json()

# 日志输出配置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
# 初始化一个webdriver.Chrome()对象
chrome_driver = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
options = webdriver.ChromeOptions()
# 关闭左上方 Chrome 正受到自动测试软件的控制的提示
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ['enable-automation'])
browser = webdriver.Chrome(options=options, executable_path=chrome_driver)

# 登录函数   访问页面->输出账号、密码->点击登录
def login():
    browser.get('https://passport.bilibili.com/login')
    browser.maximize_window()
    # ID定位用户名，密码输入框
    username = browser.find_element_by_id('login-username')
    password = browser.find_element_by_id('login-passwd')
    username.send_keys('19121712563')
    password.send_keys('67537mclL')
    # Xpath定位登录按钮并点击
    browser.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()
    sleep(random.random()*3)

def save_img():
    # save_screenshot：将当前页面进行截图并保存下来
    browser.save_screenshot('page.png')
    # Xpath定位验证码图片的位置
    code_img_ele = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div/div')
    location = code_img_ele.location  # 验证码左上角的坐标x,y
    size = code_img_ele.size  # 验证码图片对应的长和宽

    # 得到左上角和右下角的坐标
    rangle = (
        int(location['x'] * 1.25), int(location['y'] * 1.25), int((location['x'] + size['width']) * 1.25),
        int((location['y'] + size['height']) * 1.25)
    )
    image1 = Image.open('./page.png')
    # code_img_name = './code.png'
    # crop根据rangle元组内的坐标进行裁剪 裁剪出验证码区域
    frame = image1.crop(rangle)
    frame.save('./code.png')
    return code_img_ele

def narrow_img():
    # 缩小图片
    code = Image.open('./code.png')
    small_img = code.resize((169, 216))
    small_img.save('./small_img.png')
    print(code.size, small_img.size)

def submit_img():
    # 将验证码提交给超级鹰进行识别
    # 用户中心->软件ID 生成你的软件ID->替换掉96001  绑定微信可以得到1000积分 免费使用
    chaojiying = Chaojiying_Client('19121712563', '67537mcl', '927288')
    with open('./small_img.png', 'rb') as f:
        im = f.read()
    # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    result = chaojiying.PostPic(im, 9004)['pic_str']
    logging.info(result)
    return result

def parse_data(result):
    node_list = []  # 存储即将被点击的点的坐标  [[x1,y1],[x2,y2]]
    print(result)
    if '|' in result:
        nums = result.split('|')
        for i in range(len(nums)):
            x = int(nums[i].split(',')[0])
            y = int(nums[i].split(',')[1])
            xy_list = [x, y]
            node_list.append(xy_list)
    else:
        print(result.split(',')[0])
        print(result.split(',')[1])
        x = int(result.split(',')[0])
        y = int(result.split(',')[1])
        xy_list = [x,y]
        node_list.append(xy_list)
    return node_list

def click_codeImg(all_list, code_img_ele):
    # 遍历列表，使用动作链对每一个列表元素对应的x,y指定的位置进行点击操作
    for item in all_list:
        x = item[0] * 1.6
        y = item[1] * 1.6
        # move_to_element_with_offset移动到距某个元素（左上角坐标）多少距离的位置
        ActionChains(browser).move_to_element_with_offset(code_img_ele, x, y).click().perform()
        sleep(random.random())
        logging.info('点击成功！')

    sleep(random.random()*2)
    # 完成动作链点击操作后，定位确认按钮并点击
    # browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div/div/div[3]/a').click()
    browser.find_element_by_xpath('/ html / body / div[2] / div[2] / div[6] / div / div / div[3] / a / div').click()

# -*- coding: UTF-8 -*-
def main():
    # 进入登录界面，输入账号密码
    login()
    # 保存页面截图，并根据坐标裁剪获取验证码图片
    code_img_ele = save_img()
    # 缩小图片
    narrow_img()
    # 将图片提交给超级鹰,获取返回的识别结果
    result = submit_img()
    # 解析返回结果,将数据格式化
    all_list = parse_data(result)
    # 在页面验证码上完成点击操作并登录
    click_codeImg(all_list, code_img_ele)

main()