from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import winsound
import time

partner_links = {
    "Amazon": "https://gracehoppercelebration.com/flow/anitab/vcf25/exhcatalog/page/ghc25sponsorcatalog/exhibitor/1720020857770001nrcJ",
    "Apple": "https://gracehoppercelebration.com/flow/anitab/vcf25/exhcatalog/page/ghc25sponsorcatalog/exhibitor/1712942120293001LSc4",
    "Meta": "https://gracehoppercelebration.com/flow/anitab/vcf25/exhcatalog/page/ghc25sponsorcatalog/exhibitor/1716993408943001dxfK",
    "Google": "https://gracehoppercelebration.com/flow/anitab/vcf25/exhcatalog/page/ghc25sponsorcatalog/exhibitor/1713188687975001PkXb",
    "Jane Street": "https://gracehoppercelebration.com/flow/anitab/vcf25/exhcatalog/page/ghc25sponsorcatalog/exhibitor/1713188688221001PBYL",
    "Morgan Stanley": "https://gracehoppercelebration.com/flow/anitab/vcf25/exhcatalog/page/ghc25sponsorcatalog/exhibitor/1713912142724001YIax",
    "Goldman Sachs": "https://gracehoppercelebration.com/flow/anitab/vcf25/exhcatalog/page/ghc25sponsorcatalog/exhibitor/1713361999165001RGIP",
    "Two Sigma": "https://gracehoppercelebration.com/flow/anitab/vcf25/exhcatalog/page/ghc25sponsorcatalog/exhibitor/1719414268768001c7dq"
    # "Vanguard": "https://gracehoppercelebration.com/flow/anitab/vcf25/exhcatalog/page/ghc25sponsorcatalog/exhibitor/1713188689461001PWIM"
}


options = Options()
options.headless = False
service = Service("geckodriver.exe")
driver = webdriver.Firefox(service=service, options=options)
wait = WebDriverWait(driver, 10)

try:
    print("Opening browser... please log in now.")
    time.sleep(10)
    print("Starting monitoring...\n")

    while True:
        for partner, url in partner_links.items():
            driver.get(url)

            try:
                button = wait.until(
                    EC.presence_of_element_located((By.XPATH, "//a[@data-analytics-name='request-meeting']"))
                )

                is_disabled = (
                    button.get_attribute("disabled") is not None
                    or button.get_attribute("aria-disabled") == "true"
                )

                if not is_disabled:
                    winsound.Beep(1500, 1000)
                    print(f"[ALERT] '{partner}' Request Meeting button is AVAILABLE! ✅")
                    with open("meeting_alerts.log", "a") as f:
                        f.write(f"{time.ctime()} - {partner} button available\n")
                else:
                    print(f"[INFO] '{partner}' Request Meeting button is disabled ❌")

            except (TimeoutException, NoSuchElementException):
                print(f"[INFO] No Request Meeting button found for {partner} ❌")

        print("Sleeping 60 seconds before next check...\n")
        time.sleep(60)

finally:
    driver.quit()