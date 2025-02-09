import os
import telebot
import random

# Lista de caminhos das imagens (coloque os caminhos corretos)
imagens = [
    "/storage/emulated/0/meu_modulo/imagens/f1.jpg",
        "/storage/emulated/0/meu_modulo/imagens/f2.jpg",
            "/storage/emulated/0/meu_modulo/imagens/f3.jpg",
                '/storage/emulated/0/meu_modulo/imagens/f4.jpg',
                    '/storage/emulated/0/meu_modulo/imagens/f5.jpg',
                        '/storage/emulated/0/meu_modulo/imagens/f6.jpg',
                            '/storage/emulated/0/meu_modulo/imagens/f7.jpg',
                                '/storage/emulated/0/meu_modulo/imagens/f8.jpg',
                                    "/storage/emulated/0/meu_modulo/imagens/f9.jpg",
                                        "/storage/emulated/0/meu_modulo/imagens/f10.jpg",
                                            "/storage/emulated/0/meu_modulo/imagens/f11.jpg",
                                                '/storage/emulated/0/meu_modulo/imagens/f12.jpg',
                                                    '/storage/emulated/0/meu_modulo/imagens/f13.jpg',
                                                        '/storage/emulated/0/meu_modulo/imagens/f14.jpg',
                                                            '/storage/emulated/0/meu_modulo/imagens/f15.jpg',
                                                                '/storage/emulated/0/meu_modulo/imagens/f16.jpg',
                                                                    '/storage/emulated/0/meu_modulo/imagens/f17.jpg'
                                                                    ]

                                                                    def sorteio():
                                                                        if not imagens:
                                                                                return "Todas as imagens já foram sorteadas!"
                                                                                    imagem_sorteada = random.choice(imagens)  # Sorteia uma imagem
                                                                                        imagens.remove(imagem_sorteada)  # Remove a imagem sorteada da lista
                                                                                            return imagem_sorteada  # Retorna o caminho da imagem sorteada

                                                                                            # Usar a função
                                                                                            escolha = sorteio()

                                                                                            Chave_Api = "Sua Chave API"  # Substitua pela sua chave API do Telegram

                                                                                            bot = telebot.TeleBot(Chave_Api)

                                                                                            @bot.message_handler(commands=["Yes"])
                                                                                            def opcao1(mensagem):
                                                                                                bot.reply_to(mensagem, "Oh")

                                                                                                @bot.message_handler(commands=["Nop"])
                                                                                                def opcao2(mensagem):
                                                                                                    bot.reply_to(mensagem, "Oh não")

                                                                                                    @bot.message_handler(commands=["Talvez"])
                                                                                                    def opcao3(mensagem):
                                                                                                        bot.reply_to(mensagem, "Hmmmmm")

                                                                                                        @bot.message_handler(commands=["Sorteio_misterioso"])
                                                                                                        def opcao4(mensagem):
                                                                                                            imagem_sorteada = sorteio()
                                                                                                                if imagem_sorteada == "Todas as imagens já foram sorteadas!":
                                                                                                                        bot.reply_to(mensagem, imagem_sorteada)
                                                                                                                            else:
                                                                                                                                    with open(imagem_sorteada, 'rb') as foto:
                                                                                                                                                bot.send_photo(mensagem.chat.id, foto)
                                                                                                                                                        bot.reply_to(mensagem, "O sorteio foi realizado com sucesso!")

                                                                                                                                                        def verificar(mensagem):
                                                                                                                                                            return True

                                                                                                                                                            @bot.message_handler(func=verificar)
                                                                                                                                                            def responder(mensagem):
                                                                                                                                                                texto = """(Selecione uma opção):
                                                                                                                                                                    /Yes
                                                                                                                                                                        /Nop
                                                                                                                                                                            /Talvez 
                                                                                                                                                                                /Sorteio_misterioso """
                                                                                                                                                                                    bot.reply_to(mensagem, texto)

                                                                                                                                                                                    bot.polling()+
