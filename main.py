from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from function import wait_for_element, click_element_xpath, create_pdf
import time
import random

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 60)
driver.get("https://store.vivo.com.br")

click_element_xpath(driver, "/html/body/app-root/custom-storefront/header/cx-page-layout[1]/cx-page-slot[6]/custom-searchbox/div/button")
search_modal = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/ngb-modal-window/div/div")))
click_element_xpath(driver, "/html/body/ngb-modal-window/div/div/search-modal-content/div/vsp-input/section/label")
input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "input")))
input.send_keys("Iphone")
input.send_keys(Keys.ENTER)

search_sort = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "sortingSelect-button")))
sort = driver.find_element(By.ID, "sortingSelect-button").click()
driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, "/html/body/app-root/custom-storefront/main/cx-page-layout/cx-page-slot[2]/cx-product-list/div/section/div/div/div/div[1]/div/div[3]/div/vsp-select/section/ul"))
click_element_xpath(driver, "/html/body/app-root/custom-storefront/main/cx-page-layout/cx-page-slot[2]/cx-product-list/div/section/div/div/div/div[1]/div/div[3]/div/vsp-select/section/ul/li[5]")

# driver.find_element(By.ID, "consent").click()
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/custom-storefront/main/cx-page-layout/cx-page-slot[2]/cx-product-list/div/section/div/div/div/div[2]/div/product-card[2]/a/div[1]")))
click_element_xpath(driver, "/html/body/app-root/custom-storefront/main/cx-page-layout/cx-page-slot[2]/cx-product-list/div/section/div/div/div/div[2]/div/product-card[2]/a/div[1]")

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/custom-storefront/main/cx-page-layout/cx-page-slot[1]/product-delivery-time/div/div/div[1]/div[1]")))

cep = driver.find_element(By.TAG_NAME, "input")
cep.send_keys("87430-000")

time.sleep(3)
button = driver.find_element(By.ID, "applyPostalCode")
button.click()

product_name = driver.find_element(By.XPATH, "/html/body/app-root/custom-storefront/main/cx-page-layout/cx-page-slot[1]/custom-product-intro/div/h1")
price = driver.find_element(By.XPATH, "/html/body/app-root/custom-storefront/main/cx-page-layout/cx-page-slot[1]/custom-product-summary/div/div[2]/p[1]")
description = driver.find_element(By.XPATH, "/html/body/app-root/custom-storefront/main/cx-page-layout/cx-page-slot[5]/custom-product-details-tab/div/div")
shipping = driver.find_element(By.XPATH, "/html/body/app-root/custom-storefront/main/cx-page-layout/cx-page-slot[1]/product-delivery-time/div/div/div/div/span[1]")


nome = product_name.text
preco = price.text
descricao = description.text
prazo = shipping.text

create_pdf(
    nome,
    preco,
    descricao,
    prazo,
    "celular.pdf"
)