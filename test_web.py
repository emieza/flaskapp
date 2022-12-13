import pytest
from selenium.webdriver.common.by import By

def test_home(selenium):
    selenium.get('http://localhost:5000')
    # podem examinar el què ens retorna el browser a "page_source"
    assert "Hello, World" in selenium.page_source


def test_form(selenium):
    # carreguem la pàgina del formulari
    selenium.get('http://localhost:5000/formulari')

    # busquem el quadre de text i hi escrivim un nom
    elem = selenium.find_element(By.TAG_NAME,"input")
    elem.send_keys("manolo")

    # cerquem el botó de submit i el cliquem
    submit = selenium.find_element(By.XPATH,"//input[@type='submit']")
    submit.click()

    # comprovem que el missatge de salutació contingui
    # el nom introduit prèviament al formulari
    assert "Salut, manolo" in selenium.page_source