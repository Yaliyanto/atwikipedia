import os
from selenium.common.exceptions import NoSuchElementException

class AksiSwipe:
    def __init__(self, driver):
        self.driver = driver  # Simpan driver sebagai atribut kelas

    def scroll_using_adb_until_element_found(self, element_locator):
        max_attempts = 10  # Batasi jumlah swipe agar tidak infinite loop
        attempts = 0
        
        while attempts < max_attempts:
            try:
                # Cek apakah elemen sudah ada di halaman
                element = self.driver.find_element(*element_locator)
                if element.is_displayed():
                    return element
            except NoSuchElementException:
                # Jika elemen belum ditemukan, lakukan swipe dengan adb
                os.system("adb shell input swipe 332 1119 332 626 600")
            
            attempts += 1
        
        raise NoSuchElementException(f"Element {element_locator} not found after scrolling.")
