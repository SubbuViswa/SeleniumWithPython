from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
tags = (By.XPATH, "//ul//li")
remove_all_btn = (By.XPATH, "//button[text()='Remove All']")
text_content_field = (By.XPATH, "//div[@class='content']//input")
remaining_tags_loc = (By.XPATH,"//div[@class='details']//p")
tag_list = ["path","selenium","learning","test","locators","xpath","css","links","id","name"]
tag_test_content = ["<script> alert() </script>"]
driver.get("https://qaplayground.dev/apps/tags-input-box/")
actions = ActionChains(driver)

def print_no_of_added_tags(element):
    no_of_tags = driver.find_elements(*element)
    print("The Number of Tags added is:",len(no_of_tags))

def print_no_of_remaining_tags(element):
    remaining_tags_text = driver.find_element(*element).get_property("textContent")
    print("The Number of Remaining tags is:",remaining_tags_text.split(" ")[0])

def add_tags(tag_list):
    for tag in tag_list:
        driver.find_element(*text_content_field).send_keys(tag)
        time.sleep(2)
        driver.find_element(*text_content_field).send_keys(Keys.RETURN)

def print_tag_values(element):
    tags_list = driver.find_elements(*element)
    for tag in tags_list:
        tag_value = tag.get_property("textContent")
        print("The value in the tag is",tag_value)

print_no_of_added_tags(tags)
print_no_of_remaining_tags(remaining_tags_loc)
driver.find_element(*remove_all_btn).click()
add_tags(tag_list)
print_no_of_added_tags(tags)
print_no_of_remaining_tags(remaining_tags_loc)
driver.find_element(*remove_all_btn).click()
add_tags(tag_test_content)
print_tag_values(tags)

