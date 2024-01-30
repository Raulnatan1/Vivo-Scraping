from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def click_element_xpath(driver, xpath):
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

def wait_for_element(driver, element, timer: float = 60):
    try:
        wait = WebDriverWait(driver, timer)
        return wait.until(EC.element_to_be_clickable((By.XPATH, element)))
    except Exception:
        return False

def create_pdf(nome, preco, descricao, prazo, nome_arquivo):
    c = canvas.Canvas(nome_arquivo, pagesize=letter)

    produto_info = f"""
    Informações do Produto: \n
    Nome: {nome} \n
    Preço: {preco} \n
    Descrição: {descricao} \n
    Prazo de entrega: {prazo} \n
    """

    c.setFont("Helvetica", 12)
    c.drawString(100, 750, produto_info)

    c.save()

    print(f"PDF com as informações do produto criado: {nome_arquivo}")