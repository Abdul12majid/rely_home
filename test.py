from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (adjust for your browser)
url = input("Active Url - ")
driver = webdriver.Chrome()  # Use `webdriver.Firefox()` for Firefox or Safari setup
#driver.add_cookie({"name": "COOKIE", "value": "!U10adPrIInZPRcEOTrqneA6i3HfRP9O38fem6sKr4K0OCX/bGQYtuk68a0fOr0kU+9t6b60LRXcjSg=="})
#driver.add_cookie({"name": "PHPSESSID", "value": "2dtsslobde7js0rattrl0d7jp0"})
driver.get(url)

print("okay")
thursdays = driver.find_elements(By.XPATH, "//strong[contains(text(), 'Thursday')]")

if len(thursdays) >= 2:
	try:
	    # Locate the second Thursday's <strong> element using its XPath
	    second_thursday_strong = driver.find_element(By.XPATH, '//*[@id="frm"]/div[2]/div[2]/ul/li[5]/strong')

	    # Navigate to the second radio button under this specific Thursday
	    second_radio_button = second_thursday_strong.find_element(
	        By.XPATH, "//*[@id='frm']/div[2]/div[2]/ul/li[5]/div[2]/label"
	    )

	    # Find the label text associated with the second radio button
	    radio_button_label_element = second_radio_button.text

	    # Click the second radio button
	    second_radio_button.click()

	    # Print the text of the selected radio button
	    print(f"Selected radio button text: {radio_button_label_element}")

	    # Click the confirm button
	    confirm_button =driver.find_element(By.XPATH, "//*[@id='frm']/div[2]/div[3]/input")
	    time.sleep(2)
	    confirm_button.click()
	    print("Clicked 'Confirm' button. Script stopping.")

	except Exception as e:
		print(f"An error occurred: {e}")

else:
	print("No available.")


time.sleep(5)
driver.quit()
