# Skribll.io-word-guesser
This is a script I made to help with the skribll.io game.
It uses selenium to spawn a new browser window and open skribll.io. You can play along with the script but if it finds less than 10 words that match it will start inputing them automatically. 

## Requirements
- python 3
- browser driver
## Libraries
- selenium
- keyboard

## How To
You will need to download the apropriate driver for your browser, I used [Google Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads). Unzip the driver in the same folder as the rest of the files, open command line or powershell and run:
```python scribblio.py```

## Other Stuff
The dictionary is small but every word in it is used in the game. You can add any extra words you find in the words file or make a bigger one yourself. It is really good in finding words containing space or dash but on smaller words it is more difficult as there are a lot of words and the hint letters don't narrow the search much.
