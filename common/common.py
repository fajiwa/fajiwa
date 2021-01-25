# 打开网页,返回title
import time


def open_url(driver, url):
    driver.get(url)
    title = driver.title
    return title


# 输入用户名、密码登录
def login(driver, username, password):
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_xpath('//button').click()


def find_func(driver, number, url, username, password):
    title = open_url(driver, url)
    if title == '柠檬ERP':
        # 登录
        login(driver, username, password)
        # 验证搜索功能
        driver.find_element_by_xpath('//span[text()="零售出库"]').click()
        # 转换iframe
        id1 = driver.find_element_by_xpath("//a[@title='零售出库']").get_attribute('data-tab-id')
        iframe_id = id1 + '-frame'
        driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@id="{}"]'.format(iframe_id)))

        # # 搜索单号
        driver.find_element_by_name("searchNumber").send_keys(number)
        driver.find_element_by_xpath('//span[text()="查询"]').click()
        time.sleep(2)

        # 判断搜索是否生效
        contain = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text
        if number in contain:
            return True
        else:
            return False
