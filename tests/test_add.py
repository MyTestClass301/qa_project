from selenium.webdriver.common.by import By


# Use By.ID
def test_add_task(driver):
    driver.find_element(By.ID, "taskInput").send_keys("Test task")
    driver.find_element(By.ID, "addBtn").click()
    tasks = driver.find_elements(By.TAG_NAME, "li")

    assert len(tasks) == 1
