from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import keyboard

a = []

with open("words", "r") as file:
    for line in file:
        a.append(line.strip())

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://skribbl.io")

driver.implicitly_wait(20)

prev_word = ""

while True:
    while keyboard.is_pressed('q') == False:
        same_length_words = []
        current_word = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "currentWord"))).text
        input_word = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "inputChat")))
        if current_word != prev_word:
            prev_word = current_word
            current_word_length = len(current_word)
            print(str(current_word_length), "letter words")
            print()
            for word in a:
                if len(word) == current_word_length:
                    if not(" " in word and " " not in current_word):
                        if not("-" in word and "-" not in current_word):
                            same_length_words.append(word)
            probably = []
            for word in same_length_words:
                position = -1
                for letter in current_word:
                    position += 1
                    if letter != "_":
                        if letter != word[position]:
                            break
                    if position == current_word_length-1:
                        print(word)
                        probably.append(word)
            if len(probably) < 10:
                for word in probably:
                    input_word.send_keys(word)
                    input_word.send_keys(Keys.RETURN)
                    time.sleep(1)
            print()
            print()