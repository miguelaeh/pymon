import telebot # Libreria de la API del bot.
from telebot import * # Tipos para la API del bot.
import time # Libreria para hacer que el programa que controla el bot no se acabe.

 
 
# Aqui definiremos aparte del Token, por ejemplo los ids de los grupos y pondriamos grupo= -XXXXX 
 
TOKEN = '563209742:AAHsXl1ZoUIZDYCBTR52oxezfxHKdCoDb8E' # Nuestro token del bot.
 
AYUDA = 'Puedes utilizar los siguientes comandos : \n\n/ayuda - Guia para utilizar el bot. \n/info - Informacion De interes \n/hola - Saludo del Bot \n/piensa3D - Informacion sobre Piensa3D \n\n'
 
 
 
 
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.

@bot.message_handler(commands=['prueba'])
def command_prueba(m, update):

	cid = m.chat.id
	bot.send_message(cid,'Envia')
	time.sleep(5)
	mensaje = update.m.text
	bot.send_message(cid,mensaje)


bot.polling()