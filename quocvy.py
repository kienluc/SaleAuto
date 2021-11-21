from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path="venv/chromedriver.exe")

driver.get("https://maverikstudio.vn/collections/all")
driver.maximize_window()
#Smiley Embroidery  T-Shirt ( White )
item_name = "Smiley Embroidery  T-Shirt ( Black )"
# total_items = len(driver.find_elements(By.CSS_SELECTOR, "product-img"))
item_quantity = 2
item_size = "M"
customer_mail_login = "tkiencop@gmail.com"
customer_pass_login = "fireblood1"
customer_name = "Cao hoàng sơn"
customer_email = "tkiencop@gmail.com"
customer_phone = "0966388477"
customer_address = "154/6 đường số 2, phường 3, gò vấp"
customer_province = "50"
customer_district = "478"
customer_ward = "26902"

ele_login = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, "icon-account")))
ele_login.click()

ele_emailLogin = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "customer_email")))
ele_emailLogin.send_keys(customer_mail_login)

driver.implicitly_wait(2)

ele_passLogin = driver.find_element_by_id("customer_password")
ele_passLogin.send_keys(customer_pass_login)

ele_loginButton = WebDriverWait(driver, 5, poll_frequency=0.05).until(ec.visibility_of_element_located((By.CLASS_NAME, "btn-signin")))
ele_loginButton.click()

ele_collectionAll = WebDriverWait(driver, 5, poll_frequency=0.05).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/collections/all']")))
ele_collectionAll.click()

ele_allItems = driver.find_elements_by_class_name("product-img")
while True:
    # new_total_items = len(driver.find_elements(By.CSS_SELECTOR, "product-img")) + 1
    try:
        ele_item = driver.find_element_by_link_text(item_name)
        ele_item.click()
        break
    except:
        driver.refresh()
# ele_items = driver.find_elements(By.CSS_SELECTOR, ".product-img > a")
#
# for item in ele_items:
#     if str(item.get_attribute("title")).lower().__contains__(item_name.lower()):
#         ele_item = item

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



# ele_customerName = WebDriverWait(driver, 10, poll_frequency=0.05).until(ec.presence_of_element_located((By.CSS_SELECTOR, "#billing_address_full_name")))
# ele_customerName.send_keys(customer_name)
#
# ele_customerEmail = WebDriverWait(driver, 10, poll_frequency=0.05).until(ec.presence_of_element_located((By.CSS_SELECTOR, "#checkout_user_email")))
# ele_customerEmail.send_keys(customer_email)
#
# ele_customerPhone = WebDriverWait(driver, 10, poll_frequency=0.05).until(ec.presence_of_element_located((By.CSS_SELECTOR, "#billing_address_phone")))
# ele_customerPhone.send_keys(customer_phone)
#
# ele_customerAddress = driver.find_element_by_id("billing_address_address1")
# ele_customerAddress.send_keys(customer_address)

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



