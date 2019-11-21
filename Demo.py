
from selenium import webdriver
#引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.maximize_window()
#driver.get(r'C:\Users\ian\workspace\HtmlDemo\WebContent\NewFile.html')
#22222222222
999999999999999999
8888888888888888888
#33333333333
#0000000000000000
time.sleep(3)
#1111111111111111111
#定位到要悬停的元素
stop =driver.find_element_by_class_name("icon-arrow-down") 
#对定位到的元素执行鼠标悬停操作
ActionChains(driver).context_click(stop).perform()
777777777777777
aaaaaaaaaaa
