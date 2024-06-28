from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
links = []
links.append("https://www.lambdatest.com/blog/selenium-best-practices-for-web-testing/")
links.append("https://www.ministryoftesting.com/articles/websites-to-practice-testing")
links.append("https://naveenautomationlabs.com/opencart/")
links.append("https://demo.guru99.com/")
url_details = []
for link in links:
    driver.get(link)
    l = driver.find_elements(By.TAG_NAME,'a')
    len_l = len(l)
    title = driver.title
    url = driver.current_url
    url_details.append({'linkcount':len_l, 'title': title, 'url': url})

max_link = max(url_details, key=lambda x:x['linkcount'])
print(max_link)
print(f"Page with maximum links: {max_link['title']} is {max_link['linkcount']} links")