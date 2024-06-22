from bs4 import BeautifulSoup
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver(is_headless: bool, browser: str):
    if browser == "chrome":
        driver = webdriver.Chrome(options=configure_driver(is_headless))
        return driver

def configure_driver(is_headless: bool):
    options = Options()
    options.headless = is_headless
    return options

def save_html(output_file, html):
    with open(output_file, 'w') as file:
        file.write(html)

def load_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def prettify_html_file(input_file, output_file):
    # Charger le contenu du fichier HTML
    with open(input_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Analyser le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Utiliser prettify pour formater le HTML
    pretty_html = soup.prettify()

    # Écrire le HTML formaté dans un nouveau fichier
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(pretty_html)