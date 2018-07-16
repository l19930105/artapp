from selenium import webdriver

# 浏览器参数化
def browser():
    # driver=webdriver.Firefox()
    driver=webdriver.Chrome()
    # driver=webdriver.Ie()
    #driver=webdriver.PhantomJS()
    #driver=webdriver.PhantomJS()
    # driver.get("http://www.baidu.com")

    return driver

if __name__ == '__main__':
    browser()