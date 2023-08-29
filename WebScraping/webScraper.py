# ----------------------------------------------------------------------------
# Libraries Required
# ----------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


# ----------------------------------------------------------------------------
# Connect to Website
# ----------------------------------------------------------------------------

# Original URL to connect
siho_url = "https://prestadores.minsalud.gov.co/SIHO/"

# Config of the browser and the driver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

# Instatiating the driver
driver = webdriver.Chrome(options)
driver.get(siho_url)


# ----------------------------------------------------------------------------
# Enter the Frame
# ----------------------------------------------------------------------------

# Find all frame HTML tags
frame_elements = driver.find_elements(By.TAG_NAME, "frame")

# Enter the frame
driver.switch_to.frame(frame_elements[1])

# Find and click the button to Log In
login_button = driver.find_element(By.ID, "btnIngresar")
login_button.click()

# Check if there is only one browser window
assert len(driver.window_handles) == 1

# Find and click the link to the element we need
link_new_tab = driver.find_element(By.LINK_TEXT, "Capacidad Instalada")
link_new_tab.click()


# ----------------------------------------------------------------------------
# Enter the New Tab
# ----------------------------------------------------------------------------

# Check if there is a new browser window
assert len(driver.window_handles) == 2

# Get out of the frame and get into the original website
driver.switch_to.default_content()

# Switch to the other window
driver.switch_to.window(driver.window_handles[1])

# Get the list of years to select
search_select_years = driver.find_element(By.ID, "_ctl0_ContentPlaceHolder1_ddano")
select_years = Select(search_select_years)
options_select_years = select_years.options
years = [option.get_attribute("value") for option in options_select_years]

# Get the list of departments to select
search_select_departments = driver.find_element(By.ID, "_ctl0_ContentPlaceHolder1_dddepa_codigo")
select_departments = Select(search_select_departments)
options_select_departments = select_departments.options
departments = [option.text for option in options_select_departments]


# ----------------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------------

def changeYear(select_years: Select, year: str):
    """
    Change the year to search, must be in the years list
    """
    select_years.select_by_value(year)
    
def changeDepartment(select_departments: Select, department: str):
    """
    Change the departments to search, must be in the departments list
    """
    select_departments.select_by_visible_text(department)
    
def searchData(driver, select_departments: Select)->pd.DataFrame:
    """
    Click the Search Button
    """
    selected_department = select_departments.all_selected_options[0].text
    if selected_department == "":
        selected_department = "NACIONAL"
    
    search_button = driver.find_element(By.ID, "_ctl0_ibBuscarFtr")
    search_button.click()
    
    wait = WebDriverWait(driver, 10)

    def is_condition_met(driver):
        try:
            span_element = driver.find_element(By.ID, "_ctl0_ContentPlaceHolder1_lblConsulta")
            return span_element.text == selected_department.upper()
        except:
            return False

    wait.until(is_condition_met)


# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------