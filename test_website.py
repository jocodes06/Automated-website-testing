from selenium.webdriver.support.ui import Select
from selenium import webdriver
import os


def test_website_title():
    driver = webdriver.Chrome()

    try:
        path = os.path.abspath("testare - tema 2/test_webpage.html")
        driver.get("file:///" + path.replace("\\", "/"))

        assert driver.title == "Test Playground 1"
        print("Title is correct!")

    finally:
        driver.quit()


def test_website_link():
    driver = webdriver.Chrome()

    try:
        path = os.path.abspath("testare - tema 2/test_webpage.html")
        driver.get("file:///" + path.replace("\\", "/"))

        link = driver.find_element("link text", "About")
        link.click()

        assert driver.title == "About"
        print("Link to about page worked!")

    finally:
        driver.quit()


def test_about_page_link():
    driver = webdriver.Chrome()

    try:
        path = os.path.abspath("testare - tema 2/test_webpage.html")
        driver.get("file:///" + path.replace("\\", "/"))

        link = driver.find_element("link text", "TestPlayground")
        link.click()

        assert driver.title == "Test Playground 1"
        print("Link back to home page worked!")

    finally:
        driver.quit()

def test_form_empty_name():
    driver = webdriver.Chrome()

    try:

        path = os.path.abspath("testare - tema 2/test_webpage.html")
        driver.get("file:///" + path.replace("\\", "/"))

        email = driver.find_element("id", "email")
        email.send_keys("johndoe@gmail.com")
        assert email.get_attribute("value") == "johndoe@gmail.com"

        name = driver.find_element("id", "name")
        name.send_keys("")
        assert name.get_attribute("value") == ""

        topic = driver.find_element("id", "topic")
        Select(topic).select_by_value("support")
        assert topic.get_attribute("value") == "support"

        messages = driver.find_element("id", "message")
        messages.send_keys("Hello! Bye!")
        assert messages.get_attribute("value") == "Hello! Bye!"

        terms = driver.find_element("id", "terms")
        terms.click()

        submit = driver.find_element("id", "submit-btn")
        submit.click()

        success = driver.find_element("id", "success")
        assert not success.is_displayed()

        print("Form doesn't accept empty name!")
    finally:
       driver.quit()


def test_form_terms_not_accepted():
    driver = webdriver.Chrome()

    try:

        path = os.path.abspath("testare - tema 2/test_webpage.html")
        driver.get("file:///" + path.replace("\\", "/"))

        email = driver.find_element("id", "email")
        email.send_keys("johndoe@gmail.com")
        assert email.get_attribute("value") == "johndoe@gmail.com"

        name = driver.find_element("id", "name")
        name.send_keys("John")
        assert name.get_attribute("value") == "John"

        topic = driver.find_element("id", "topic")
        Select(topic).select_by_value("support")
        assert topic.get_attribute("value") == "support"

        messages = driver.find_element("id", "message")
        messages.send_keys("Hello! Bye!")
        assert messages.get_attribute("value") == "Hello! Bye!"

        submit = driver.find_element("id", "submit-btn")
        submit.click()

        success = driver.find_element("id", "success")
        assert not success.is_displayed()

        print("Form doesn't submit when the terms aren't accepted!")
    finally:
        driver.quit()


def test_form_empty_message():
    driver = webdriver.Chrome()

    try:

        path = os.path.abspath("testare - tema 2/test_webpage.html")
        driver.get("file:///" + path.replace("\\", "/"))

        email = driver.find_element("id", "email")
        email.send_keys("johndoe@gmail.com")
        assert email.get_attribute("value") == "johndoe@gmail.com"

        name = driver.find_element("id", "name")
        name.send_keys("John")
        assert name.get_attribute("value") == "John"

        topic = driver.find_element("id", "topic")
        Select(topic).select_by_value("support")
        assert topic.get_attribute("value") == "support"

        terms = driver.find_element("id", "terms")
        terms.click()

        submit = driver.find_element("id", "submit-btn")
        submit.click()

        success = driver.find_element("id", "success")
        assert not success.is_displayed()

        print("Form doesn't submit when the message is empty!")
    finally:
        driver.quit()



def test_form_invalid_email():
    driver = webdriver.Chrome()

    try:
        path = os.path.abspath("testare - tema 2/test_webpage.html")
        driver.get("file:///" + path.replace("\\", "/"))

        email = driver.find_element("id", "email")
        email.send_keys("j")

        name = driver.find_element("id", "name")
        name.send_keys("John Doe")
        assert name.get_attribute("value") == "John Doe"

        topic = driver.find_element("id", "topic")
        Select(topic).select_by_value("support")
        assert topic.get_attribute("value") == "support"

        messages = driver.find_element("id", "message")
        messages.send_keys("Hello! Bye!")
        assert messages.get_attribute("value") == "Hello! Bye!"

        terms = driver.find_element("id", "terms")
        terms.click()

        submit = driver.find_element("id", "submit-btn")
        submit.click()

        success = driver.find_element("id", "success")
        assert not success.is_displayed()

        print("Form doesn't accept this email!")

    finally:
        driver.quit()


def test_valid_form():
    driver = webdriver.Chrome()

    try:
        path = os.path.abspath("testare - tema 2/test_webpage.html")
        driver.get("file:///" + path.replace("\\", "/"))

        name = driver.find_element("id", "name")
        name.send_keys("John Doe")
        assert name.get_attribute("value") == "John Doe"

        email = driver.find_element("id", "email")
        email.send_keys("johndoe@gmail.com")
        assert email.get_attribute("value") == "johndoe@gmail.com"

        topic = driver.find_element("id", "topic")
        Select(topic).select_by_value("support")
        assert topic.get_attribute("value") == "support"

        messages = driver.find_element("id", "message")
        messages.send_keys("Hello! Bye!")
        assert messages.get_attribute("value") == "Hello! Bye!"

        terms = driver.find_element("id", "terms")
        terms.click()

        submit = driver.find_element("id", "submit-btn")
        submit.click()

        success = driver.find_element("id", "success")
        assert success.is_displayed()

        print("Form accepts this data!")

    finally:
        driver.quit()


def test_invalid_form():
    driver = webdriver.Chrome()

    try:
        path = os.path.abspath("testare - tema 2/test_webpage.html")
        driver.get("file:///" + path.replace("\\", "/"))

        submit = driver.find_element("id", "submit-btn")
        submit.click()

        success = driver.find_element("id", "success")
        assert not success.is_displayed()

        print("Form didn't submit, data is invalid!")

    finally:
        driver.quit()
