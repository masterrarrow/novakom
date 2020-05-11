from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from os import path, environ
from platform import system
from time import sleep


def main(street: str, house_number: str, code: str, flat_number: str = None):
    """
        Check data from novakom

        :param street: street name
        :param house_number: house number
        :param code: communal code
        :param flat_number: flat number (0 - no flat)
        :return: bool
    """
    # Headless
    opts = Options()
    opts.headless = False

    geckodriver = path.join(path.curdir, 'geckodriver.exe' if system() == 'Windows' else 'geckodriver')
    driver = webdriver.Firefox(executable_path=geckodriver, options=opts)

    try:
        driver.get('https://www.novakom.com.ua/abonent')
        assert 'Кабінет абонента' in driver.title

        # Cookies
        cookies = wait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Я зрозумів, не показувати більше"))
        )
        sleep(1)
        cookies.click()

        # Enter address
        driver.find_element_by_id('select2-chosen-1').click()
        webdriver.ActionChains(driver).send_keys(street[:-1]).perform()
        sleep(1)
        webdriver.ActionChains(driver).send_keys(street[-1:]).perform()
        sleep(1)
        webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()

        if flat_number:
            driver.find_element_by_id('abonentaddr-flat').send_keys(flat_number)

        house = driver.find_element_by_id('abonentaddr-nhouse')
        house.send_keys(house_number)
        house.submit()

        # Enter code
        com_code = wait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "hc"))
        )
        com_code.send_keys(code)
        com_code.submit()
        sleep(1)

        # Show data
        driver.find_element_by_link_text('Друкувати').click()
        sleep(1)
    except Exception as e:
        print(str(e))
        return False
    finally:
        driver.close()

    return True


if __name__ == '__main__':
    # Loading environment variables
    BASE_DIR = path.dirname(path.abspath(__file__))
    env = path.join(BASE_DIR, '.env')
    load_dotenv(env)

    # Get arguments
    street_name = environ.get('STREET')
    house = environ.get('HOUSE')
    code_number = environ.get('CODE')
    flat = environ.get('FLAT')

    # street name, house, code, flat
    if main(street_name, house, code_number, flat):
        print('Successfully checked')
    else:
        print('Checking data has been failed')
