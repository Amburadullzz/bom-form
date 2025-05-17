# ---- isi file Python mulai di sini ----
import pandas as pd
import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

CHROME_DRIVER_PATH = "/usr/local/bin/chromedriver"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScWaaIiq0ZFarrNf71RUKyFJLwE2RMhRHFmh7XZW6WZGWTBjA/viewform"
CSV_FILE = "data.csv"
DELAY = 0.05
FIELD_XPATH = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'


def type_slow(elem, text):
    for ch in str(text):
        elem.send_keys(ch)
        time.sleep(DELAY)

def submit_row(address):
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=opts)
    try:
        driver.get(FORM_URL)
        time.sleep(1)
        inp = driver.find_element(By.XPATH, FIELD_XPATH)
        type_slow(inp, address)

        submit_btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit_btn.click()
        time.sleep(1)
    finally:
        driver.quit()

def main():
    if not os.path.exists(CSV_FILE):
        print(f"{CSV_FILE} tidak ditemukan."); return
    df = pd.read_csv(CSV_FILE)
    for i, addr in enumerate(df['address'], 1):
        print(f"Row {i}/{len(df)}: {addr}")
        submit_row(addr)
    print("Selesai!")

if __name__ == "__main__":
    main()
# ---- isi file Python selesai di sini ----
