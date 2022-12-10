from selenium import webdriver

url = 'https://investors.att.com/stock-information/historical-stock-information/historical-common-dividends/att-inc'
browser = webdriver.Chrome()
browser.get(url)

table = browser.find_element("xpath", '//*[@id="tab"]').text
print(table)