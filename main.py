from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (adjust for your browser)
url = input("Active Url - ")


driver = webdriver.Chrome()  # Use `webdriver.Firefox()` for Firefox or Safari setup

driver.get(url)

# Define the forbidden texts
forbidden_locations = ['Laughlin', 'Pahrump', 'Bullhead', 'Bullhead City']

# Initialize the refresh count
refresh_count = 0

while True:
    refresh_count += 1  # Increment refresh count
    print(f"Page refreshed {refresh_count} times...")
    
    # Check for forbidden text before clicking the 'Accept' button
    forbidden_found = False
    for text in forbidden_locations:
        try:
            # Check if the forbidden text is present on the page
            driver.find_element(By.XPATH, f"//*[contains(text(), '{text}')]")
            print(f"{text}, did not accept offer")
            forbidden_found = True
            break  # Exit the loop once a forbidden text is found
        except:
            continue

    if not forbidden_found:
        # Look for the 'Accept' button and click it if no forbidden text was found
        try:
            accept_button = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, "//*[text()='Accept']"))
            )
            accept_button.click()
            print("Clicked 'Accept' button!")

            # Wait for the new page to load
            time.sleep(5)

            # Click the second radio button under the second 'Thursday' and print the text of the radio button
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
                print("No available location.")
                break
            
        except Exception as e:
            print(f"An error occurred: {e}")

        # Refresh the page if not terminating the loop
        print("Refreshing the page...")
        driver.refresh()
        time.sleep(3)  # Add a short delay before the refresh

    else:
        print("Process terminated due to forbidden text.")
        break

# Clean up
driver.quit()