from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

partner_links = {
    "Amazon": "https://gracehoppercelebration.com/flow/anitab/vcf25/exhcatalog/page/ghc25sponsorcatalog/exhibitor/1720020857770001nrcJ",
    "Google": "https://gracehoppercelebration.com/flow/anitab/vcf25/exhcatalog/page/ghc25sponsorcatalog/exhibitor/1712942120293001LSc4",
}

options = Options()
options.headless = True  

service = Service("geckodriver.exe")

driver = webdriver.Firefox(service=service, options=options)

try:
    while True:
        for partner, url in partner_links.items():
            driver.get(url)
            time.sleep(2)

            try:
                button = driver.find_element(By.XPATH, "//button[contains(., 'Request Meeting')]")
                print(f"[ALERT] '{partner}' has a Request Meeting button available! ✅")
            except:
                print(f"[INFO] No button for {partner} right now ❌")

        print("Sleeping 60 seconds before next check...\n")
        time.sleep(60)

finally:
    driver.quit()
