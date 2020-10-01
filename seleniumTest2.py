from selenium import webdriver
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()

# 添加UA
options.add_argument('user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')

# 指定浏览器分辨率
options.add_argument('window-size=1920x3000')

# 谷歌文档提到需要加上这个属性来规避bug
#chrome_options.add_argument('--disable-gpu')

# 隐藏滚动条, 应对一些特殊页面
options.add_argument('--hide-scrollbars')

# 不加载图片, 提升速度
options.add_argument('blink-settings=imagesEnabled=false')

# 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
#options.add_argument('--headless')

# 以最高权限运行
options.add_argument('--no-sandbox')

# 手动指定使用的浏览器位置
options.binary_location = r"C:\Users\Amos\AppData\Local\Google\Chrome\Application\chrome.exe"

#添加crx插件
#options.add_extension('d:\crx\AdBlock_v2.17.crx')

# 禁用JavaScript
#options.add_argument("--disable-javascript")

# 设置开发者模式启动，该模式下webdriver属性为正常值
#options.add_experimental_option('excludeSwitches', ['enable-automation'])

# 禁用浏览器弹窗
prefs = {
    'profile.default_content_setting_values' :  {
        'notifications' : 2
     }
}
options.add_experimental_option('prefs',prefs)


driver=webdriver.Chrome(options=options)


driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()