from selenium import webdriver
import csv

filename = 'starbucks_crawling.csv'
csv_open = open(filename, 'w+', encoding='utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow(
    ('menu', 'category', 'korean_name', 'english_name', 'description', 'img_url'))


driver = webdriver.Chrome('/Users/won/Downloads/chromedriver')
url = 'https://www.starbucks.co.kr/menu/drink_list.do'

driver.implicitly_wait(3)


driver.get(url)

get_prod_number = driver.find_elements_by_xpath(
    '//*[@id="container"]/div[2]/div[2]/div/dl/dd[1]/div[1]/dl/dd/ul/li/dl/dt/a')

prod_number = [element.get_attribute('prod') for element in get_prod_number]

for prod in prod_number:
    try:
        driver.get(
            'https://www.starbucks.co.kr/menu/drink_view.do?product_cd='+prod)
        driver.implicitly_wait(3)

        menu = driver.find_element_by_xpath(
            '//*[@id="container"]/div[1]/div/ul/li[5]/a').text
        category = driver.find_element_by_xpath(
            '//*[@id="container"]/div[1]/div/h2/img').get_attribute('alt')
        korean_name = driver.find_element_by_xpath(
            '//*[@id="container"]/div[1]/div/ul/li[9]/a').text
        english_name = driver.find_element_by_xpath(
            '//*[@id="container"]/div[2]/div[1]/div[2]/div[1]/h4/span').text
        description = driver.find_element_by_xpath(
            '//*[@id="container"]/div[2]/div[1]/div[2]/div[1]/p').text
        img_url = driver.find_element_by_xpath(
            '//*[@id="product_thum_wrap"]/ul/li/a/img').get_attribute('src')
        csv_writer.writerow(
            (menu, category, korean_name, english_name, description, img_url))
    except Exception:
        continue

csv_open.close()
driver.quit()
