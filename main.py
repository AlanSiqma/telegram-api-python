import telebot
import os 
import dotenv

dotenv.load_dotenv();

TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['teste'])
def teste(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id,
                     "Sainda a pizza para sua casa: Tempo de espera em 20 min")


@bot.message_handler(commands=['pizza'])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id,
                     "Sainda a pizza para sua casa: Tempo de espera em 20 min")


@bot.message_handler(commands=['hamburger'])
def hamburger(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo o Brabo: em 10 min chega ai")


@bot.message_handler(commands=['salada'])
def salada(mensagem):
    bot.send_message(mensagem.chat.id,
                     "não tem salada não, clique aqui para iniciar: /iniciar")


@bot.message_handler(commands=['opcao1'])
def opcao1(mensagem):

    texto = """
    O que você quer? (Clique no item)
        /pizza Pizza
        /hamburger Hamburger
        /salada Salada
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['opcao2'])
def opcao2(mensagem):
    bot.send_message(
        mensagem.chat.id, "Para enviar uma reclamação, mande um e-mal para alansiqma@gmail.com")


@bot.message_handler(commands=['opcao3'])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Valeu! Alan mandou um abraço de volta")


def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item)
        /opcao1 Fazer um pedido
        /opcao2 Reclamar de um pedido
        /opcao3 Mandar um abraço para o Alan
    Responder qualquer outra coisa não vai funcionar, lique em uma das opções
    """
    bot.reply_to(mensagem, texto)


bot.polling()
