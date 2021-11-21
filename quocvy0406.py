import tkinter as tk
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import threading

import time

class MaverikBot:
    def __init__(self, mail, password, link, sizing, quantity, province, district, ward):
        self.mail = mail
        self.password = password
        self.link = link
        self.sizing = sizing
        self.quantity = quantity
        self.province = province
        self.district = district
        self.ward = ward
    def login(self, driver):
        ele_emailLogin = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "customer_email")))
        ele_passLogin = driver.find_element_by_id("customer_password")
        ele_loginButton = WebDriverWait(driver, 5, poll_frequency=0.05).until(
            ec.visibility_of_element_located((By.CLASS_NAME, "btn-signin")))
        ele_emailLogin.send_keys(self.mail)
        ele_passLogin.send_keys(self.password)
        ele_loginButton.click()

    def copping(self):
        driver = webdriver.Edge(executable_path="venv/msedgedriver.exe")
        driver.get("https://maverikstudio.vn/account/login")

        try:
            ele_wait = driver.find_element_by_id("challenge-form")
            time.sleep(4)
        except:
            pass

        self.login(driver)
        try:
            ele_wait = driver.find_element_by_id("challenge-form")
            time.sleep(4)
        except:
            pass
        while True:
            try:
                ele_error = WebDriverWait(driver, 1, poll_frequency=0.5).until(ec.visibility_of_element_located((By.CLASS_NAME, "errors")))
                try:
                    ele_wait = driver.find_element_by_id("challenge-form")
                    time.sleep(4)
                except:
                    pass
                self.login(driver)
            except:
                break
        try:
            ele_wait = driver.find_element_by_id("challenge-form")
            time.sleep(3)
        except:
            pass

        driver.get(self.link)

        try:
            ele_wait = driver.find_element_by_id("challenge-form")
            time.sleep(4)
        except:
            pass

        while True:
            try:
                ele_size = driver.find_element_by_css_selector(f"label[for='swatch-0-{self.sizing}']")
                ele_size.click()
                break
            except:
                time.sleep(0.5)
                driver.refresh()


        time.sleep(0.25)
        ele_addToCart = driver.find_element_by_id("add-to-cart")
        ele_addToCart.click()
        time.sleep(0.25)

        driver.get("https://maverikstudio.vn/checkout")
        try:
            ele_wait = driver.find_element_by_id("challenge-form")
            time.sleep(4)
        except:
            pass
        time.sleep(0.3)
        WebDriverWait(driver, 10, poll_frequency=0.5).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "option[value='50']")))
        ele_customerProvince = Select(driver.find_element_by_id("customer_shipping_province"))
        ele_customerProvince.select_by_value(self.province)

        WebDriverWait(driver, 10, poll_frequency=0.5).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "option[value='480']")))

        ele_customerDistrict = Select(driver.find_element_by_id("customer_shipping_district"))
        ele_customerDistrict.select_by_value(self.district)
        time.sleep(0.3)

        ele_customerWard = Select(driver.find_element_by_id("customer_shipping_ward"))
        ele_customerWard.select_by_value(self.ward)
        time.sleep(0.3)
        ele_complete = driver.find_element_by_class_name("step-footer-continue-btn")
        ele_complete.click()
        time.sleep(300)

bot1 = MaverikBot("nqvy090120@gmail.com", "fireblood1", "https://maverikstudio.vn/products/vintage-cargo-pants-black", "s", 1, "50", "480", "26914")
bot2 = MaverikBot("ngqvy0901@gmail.com", "fireblood1", "https://maverikstudio.vn/products/vintage-cargo-pants-black", "m", 1, "50", "480", "26914")

thread1 = threading.Thread(target=bot1.copping)
thread2 = threading.Thread(target=bot2.copping)


thread1.start()
thread2.start()

