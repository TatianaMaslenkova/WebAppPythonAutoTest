import yaml
from module import Site
import time

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])


def test_check_added_post(x_selector1, x_selector2, x_selector4, btn_selector, add_post_btn, add_title,
                          add_description, add_content, save_post, check_title, new_post_title):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(testdata["password"])
    button = site.find_element("css", btn_selector)
    button.click()
    time.sleep(testdata["sleep_time"])

    button = site.find_element("xpath", add_post_btn)
    button.click()
    input3 = site.find_element("xpath", add_title)
    input3.clear()
    input3.send_keys(testdata["title"])
    input4 = site.find_element("xpath", add_description)
    input4.clear()
    input4.send_keys(testdata["description"])
    input5 = site.find_element("xpath", add_content)
    input5.clear()
    input5.send_keys(testdata["content"])
    button = site.find_element("xpath", save_post)
    button.click()
    time.sleep(testdata["sleep_time"])

    code_label = site.find_element("xpath", check_title).text
    assert code_label == new_post_title, "test 'check_added_post' Failed"

    site.driver.close()
