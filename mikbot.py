import telebot
import requests
from requests.auth import HTTPBasicAuth

#otentikasi
#Untuk login mikrotik, buat user dengan akses read
login = HTTPBasicAuth('username_mikrotik','password_mikrotik')
endpoint = 'https://ip_mikrotik/rest'

#telegram
#Buat bot di @BotFather Telegram dan ambil bot token dan chat:id
bot_token = 'token_bot_telegram_disini'
bot       = telebot.Telebot(bot_token)

#check user active hotspot
@bot.message_handler(commands=['hotspot-active'])
def active_user(message):
        count = 0
        user_active = requests.get(endpoint+'/ip/hotspot/active', auth=login, verify=False)
        for ua in user_active.json():
                count+=1
        bot.reply_to(message, '<b>🙎 User Aktif Saat Ini : '+str(count)+'</b>', parse_mode='html')
        print('log: active_user function')
        
#check pppoe active
@bot.message_handler(commands=['pppoe-active'])
def active_pppoe(message):
        count = 0
        pppoe_active = requests.get(endpoint+'/ppp/active' auth=login, verify=False)
        for pa in pppoe_active.json():
                count+=1
        bot.reply_to(message, '<b>PPPoE Aktif Saat Ini : '+str(count)+'</b>', parse_mode='html')
        print('log: pppoe_active function')

bot.infinity_polling()
