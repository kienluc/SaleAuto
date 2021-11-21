import tkinter as tk
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import threading, schedule, time, os, sys


myBot = Tk()
myBot.geometry("300x500")
myBot.title("BY KEYWORDS")


keyword1_label = Label(myBot, text="Keyword1: ")
keyword1_label.pack()
keyword1_input = Entry(myBot, bd=2)
keyword1_input.pack()

keyword2_label = Label(myBot, text="Keyword2: ")
keyword2_label.pack()
keyword2_input = Entry(myBot, bd=2)
keyword2_input.pack()

keyword3_label = Label(myBot, text="Keyword3: ")
keyword3_label.pack()
keyword3_input = Entry(myBot, bd=2)
keyword3_input.insert(0, "cargo")
keyword3_input.pack()


province_label = Label(myBot, text="Province: ")
province_label.pack()
province_input = Entry(myBot, bd=2)
province_input.insert(0, "50")
province_input.pack()

district_label = Label(myBot, text="District: ")
district_label.pack()
district_input = Entry(myBot, bd=2)
district_input.insert(0, "478")
district_input.pack()

ward_label = Label(myBot, text="Ward: ")
ward_label.pack()
ward_input = Entry(myBot, bd=2)
ward_input.insert(0, "26902")
ward_input.pack()

timecop_label = Label(myBot, text="Time: ")
timecop_label.pack()
timecop_input = Entry(myBot, bd=2)
timecop_input.pack()

class Account:
    def __init__(self, mail, password, size, quantity):
        self.mail = mail
        self.password = password
        self.quantity = quantity
        self.size = size

ac1 = Account("nqvy0901@gmail.com", "fireblood1", "M", 1)
ac2 = Account("cmtry0901@gmail.com", "fireblood1", "L", 1)
ac3 = Account("ktran2246@gmail.com", "fireblood1", "XL", 1)
ac4 = Account("tkiencop@gmail.com", "fireblood1", "L", 1)
ac5 = Account("macopping123@gmail.com", "fireblood1", "L", 1)
ac6 = Account("macamping123@gmail.com", "fireblood1", "M", 1)

def login(driver, account):
    ele_emailLogin = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "customer_email")))
    ele_passLogin = driver.find_element_by_id("customer_password")
    ele_loginButton = WebDriverWait(driver, 5, poll_frequency=0.05).until(
        ec.visibility_of_element_located((By.CLASS_NAME, "btn-signin")))
    ele_emailLogin.send_keys(account.mail)
    ele_passLogin.send_keys(account.password)
    time.sleep(0.25)
    ele_loginButton.click()
def checkout(driver):
    province = province_input.get()
    district = district_input.get()
    ward = ward_input.get()
    time.sleep(0.25)
    WebDriverWait(driver, 10, poll_frequency=0.5).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, "option[value='50']")))
    ele_customerProvince = Select(driver.find_element_by_id("customer_shipping_province"))
    ele_customerProvince.select_by_value(province)
    time.sleep(0.25)

    ele_customerDistrict = Select(driver.find_element_by_id("customer_shipping_district"))
    ele_customerDistrict.select_by_value(district)
    time.sleep(0.25)

    ele_customerWard = Select(driver.find_element_by_id("customer_shipping_ward"))
    ele_customerWard.select_by_value(ward)
    time.sleep(0.25)
    # ele_complete = WebDriverWait(driver, 20, poll_frequency=0.05).until(
    #     ec.presence_of_element_located((By.CSS_SELECTOR, ".step-footer-continue-btn")))
    # ele_complete.click()
def copping(account):
    driver = webdriver.Edge(executable_path="venv/msedgedriver.exe")
    driver.get("https://maverikstudio.vn/account/login")
    keyword1 = keyword1_input.get().lower()
    keyword2 = keyword2_input.get().lower()
    keyword3 = keyword3_input.get().lower()
    size = account.size.lower()
    quantity = account.quantity

    login(driver, account)
    while True:
        try:
            ele_error = driver.find_element_by_class_name("errors")
            time.sleep(0.25)
            login(driver, account)
        except:
            driver.get("https://maverikstudio.vn/collections/all")
            break


    while True:
        try:
            ele_allItems = driver.find_elements_by_css_selector(".image-resize")
            for ele in ele_allItems:
                ele_title = ele.get_attribute("title").lower()
                if keyword1 in ele_title and keyword2 in ele_title and keyword3 in ele_title:
                    ele.click()
            break
        except:
            driver.refresh()

    while True:
        try:
            ele_size = driver.find_element_by_css_selector(f"label[for='swatch-0-{size}']")
            ele_size.click()
            break
        except:
            driver.refresh()

    ele_plus = WebDriverWait(driver, 10, poll_frequency=0.05).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, "input[value='+']")))

    if quantity == "1":
        pass
    elif quantity == "2":
        ele_plus.click()
    elif quantity == "3":
        ele_plus.click()
        ele_plus.click()
    time.sleep(0.25)
    ele_addToCart = WebDriverWait(driver, 5, poll_frequency=0.05).until(
        ec.visibility_of_element_located((By.ID, "add-to-cart")))
    ele_addToCart.click()

    driver.get("https://maverikstudio.vn/checkout")
    time.sleep(0.25)
    checkout(driver)

def start(account):
    timecop=timecop_input.get()
    if not timecop:
        copping(account)
    else:
        schedule.every().day.at(timecop).do(lambda: copping(account))
    while True:
        schedule.run_pending()
        time.sleep(1)
thread1 = threading.Thread(target=start, args=[ac1])
#thread2 = threading.Thread(target=start, args=[ac2])
# thread3 = threading.Thread(target=start, args=[ac3])
thread4 = threading.Thread(target=start, args=[ac4])
# thread5 = threading.Thread(target=start, args=[ac5])
# thread6 = threading.Thread(target=start, args=[ac6])

def threadCreator():
    try:
        thread1.start()
        # thread2.start()
        # thread3.start()
        thread4.start()
        # thread5.start()
        # thread6.start()
    except:
        pass
def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def close():
    myBot.destroy()

start_btn = Button(myBot, width=10, height=10, bd=3, bg="green", text="START", command=threadCreator)
start_btn.pack(side=tk.LEFT)

restart_btn = Button(myBot, width=5, height=5, bd=3, bg="blue", text="RESTART", command=restart)
restart_btn.pack(side=tk.BOTTOM)

exit_btn = Button(myBot, width=10, height=10, bd=3, bg="red", text="EXIT", command=close)
exit_btn.pack(side=tk.RIGHT)
myBot.mainloop()

