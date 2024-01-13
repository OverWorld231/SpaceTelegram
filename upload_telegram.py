import telegram
import os
import random
import time
tg_token = os.environ['TG_TOKEN']
chat_id = os.environ['CHAT_ID']
bot = telegram.Bot(token=tg_token)
print(bot.get_me())
bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")

while True:
  files = os.listdir("images")
  random.shuffle(files)
  for file in files:
    files_path = os.path.join("images",file)
    with open(files_path,"rb") as f:
      bot.send_document(chat_id=chat_id, document=f)
      time.sleep(secs=14400)
