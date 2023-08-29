# ----------------------------------------------------------------------------
# Libraries Required
# ----------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
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

def setSelectedYear(select_years: Select, year: str)->Select:
    """
    Change the year to search, must be in the years list
    """
    select_years.select_by_value(year)
    
    return select_years

    
def getSelectedYear(select_years: Select)->str:
    """
    Get the year currently selected
    """
    selected_year = select_years.all_selected_options[0].get_attribute("value")

    return selected_year

    
def setSelectedDepartment(select_departments: Select, department: str)->Select:
    """
    Change the departments to search, must be in the departments list
    """
    if department == "Nacional":
        department = ""
    select_departments.select_by_visible_text(department)
    
    return select_departments

    
def getSelectedDepartment(select_departments: Select)->str:
    """
    Get the Department currently selected
    """
    selected_department = select_departments.all_selected_options[0].text
    if selected_department == "":
        selected_department = "Nacional"

    return selected_department

    
def searchData(driver, select_departments: Select):
    """
    Click the Search Button
    """
    selected_department = getSelectedDepartment(select_departments)
    
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


def saveData(driver, select_years: Select, select_departments: Select)->pd.DataFrame:
    """
    Save the data from the webpage to a DataFrame
    """
    df = pd.read_html(driver.page_source, attrs={"id": "_ctl0_ContentPlaceHolder1_dgInforme1"})[0]
    
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header
    df['Departamento'] = getSelectedDepartment(select_departments)
    df['Anio'] = getSelectedYear(select_years)
    df = df[['Departamento', 'Anio', 'Concepto', 'Cantidad']]

    return df


def concatenateDataframes(df1: pd.DataFrame, df2: pd.DataFrame)->pd.DataFrame:
    """
    Concatenate two dataframes with the same columns
    """
    concatenated_df = pd.concat([df1, df2], ignore_index=True)
    
    return concatenated_df
    

def getInstalledCapacity(driver, df1: pd.DataFrame, select_years: Select, year: str, select_departments: Select, department: str)->pd.DataFrame:
    select_years = setSelectedYear(select_years, year)
    select_departments = setSelectedDepartment(select_departments, department)
    searchData(driver, select_departments)
    df2 = saveData(driver, select_years, select_departments)
    df = concatenateDataframes(df1, df2)
    
    return df

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# End the Scraper
# ----------------------------------------------------------------------------

driver.quit()