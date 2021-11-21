from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path="venv/chromedriver.exe")

driver.get("https://maverikstudio.vn/account/login")

#Smiley Embroidery  T-Shirt ( Black )
item_name = "Smiley Embroidery  T-Shirt ( White )"
# total_items = len(driver.find_elements(By.CSS_SELECTOR, "product-img"))
item_quantity = 2
item_size = "L"
customer_mail_login = "tkiencop@gmail.com"
customer_pass_login = "fireblood1"
customer_name = "tuấn kiện"
customer_email = "ktran2246@gmail.com"
customer_phone = "0834697489"
customer_address = "154/6 đường số 2, phường 3, gò vấp"
customer_province = "50"
customer_district = "478"
customer_ward = "26902"

# ele_login = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, "icon-account")))
# ele_login.click()

ele_emailLogin = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "customer_email")))
ele_emailLogin.send_keys(customer_mail_login)

ele_passLogin = driver.find_element_by_id("customer_password")
ele_passLogin.send_keys(customer_pass_login)

ele_loginButton = WebDriverWait(driver, 5, poll_frequency=0.05).until(ec.visibility_of_element_located((By.CLASS_NAME, "btn-signin")))
ele_loginButton.click()

driver.get("https://maverikstudio.vn/products/smiley-t-shirt-white")
while True:
    try:
        ele_size = driver.find_element(By.CSS_SELECTOR, f"div[data-value='{item_size}']")
        ele_size.click()
        break
    except:
        driver.refresh()

ele_plus = WebDriverWait(driver, 10, poll_frequency=0.05).until(ec.element_to_be_clickable((By.CSS_SELECTOR,  "input[value='+']")))

if item_quantity == 1:
    pass
elif item_quantity == 2:
    ele_plus.click()
elif item_quantity == 3:
    ele_plus.click()
    ele_plus.click()
ele_addToCart = WebDriverWait(driver, 5, poll_frequency=0.05).until(ec.visibility_of_element_located((By.ID, "add-to-cart")))
ele_addToCart.click()

ele_checkOut = WebDriverWait(driver, 10, poll_frequency=0.05).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']")))
ele_checkOut.click()

WebDriverWait(driver, 10, poll_frequency=0.5).until(ec.presence_of_element_located((By.CSS_SELECTOR, "option[value='50']")))
ele_customerProvince = Select(driver.find_element_by_id("customer_shipping_province"))
ele_customerProvince.select_by_value(customer_province)

WebDriverWait(driver, 10, poll_frequency=0.5).until(ec.presence_of_element_located((By.CSS_SELECTOR, "option[value='478']")))
ele_customerDistrict = Select(driver.find_element_by_id("customer_shipping_district"))
ele_customerDistrict.select_by_value(customer_district)

WebDriverWait(driver, 10, poll_frequency=0.5).until(ec.presence_of_element_located((By.CSS_SELECTOR, "option[value='26902']")))

ele_customerWard = Select(driver.find_element_by_id("customer_shipping_ward"))
ele_customerWard.select_by_value(customer_ward)

ele_complete = WebDriverWait(driver, 20, poll_frequency=0.05).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".step-footer-continue-btn")))
ele_complete.click()



