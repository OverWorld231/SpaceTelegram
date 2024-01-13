import telegram
import os
import random
import time


def main():
    tg_token = os.environ['TG_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    bot = telegram.Bot(token=tg_token)
    
    while True:
        files = os.listdir("images")
        random.shuffle(files)
        for file in files:
            files_path = os.path.join("images",file)
            with open(files_path,"rb") as f:
                bot.send_document(chat_id=chat_id, document=f)
            time.sleep(secs=14400)


if __name__ == "__main__":
   main()
