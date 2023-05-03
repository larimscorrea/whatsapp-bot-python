from selenium import webdriver
import time 

class whatsappBot: 
    def __init__(self):
        self.mensagem = "Bom dia pessoal"
        self.grupos = ["GRUPO FAMÍLiA"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

        def EnviarMensagens(self):
           
           print('Bom dia')
           self.driver.get('https://web.whatsapp.com')
           time.sleep(30)
           for grupo in self.grupos:
                grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
                time.sleep(3)
                grupo.click()
                chat_box = self.driver.find_element_by_class_name('_13mgZ')
                time.sleep(3)
                chat_box.click()
                chat_box.send_keys(self.mensagem)
                botao_enviar = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
                time.sleep(3)
                botao_enviar.click()
                time.sleep(5)


bot = whatsappBot()
bot.EnviarMensagens()
