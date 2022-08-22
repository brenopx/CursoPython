"""
Aula 112 - Selenium - Automatizando tarefas no navegador
"""
from selenium import webdriver
from time import sleep


class MozillaAuto:
    def __init__(self):
        self.driver_path = 'geckodriver-0.30.0'
        self.options = webdriver.MozillaOptions()
        self.options.add_argument('user-data-dir=Perfil')
        self.mozilla = webdriver.Mozilla(
            self.driver_path,
            options=self.options
        )

    def clica_sing_in(self):
        try:
            btn_sign_in = self.mozilla.find_element_by_link_text('Sing in')
            btn_sign_in.click()
        except Exception as e:
            print('Error ao clicar em Sign in: ', e)

    def acessa(self, site):
        self.mozilla.get(site)

    def sair(self):
        self.mozilla.quit()

    def clica_perfil(self):
        try:
            perfil = self.mozilla.find_element_by_css_selector(
                'body > div.position-relative.js-header-wrapper > header >'
                ' div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details')
            perfil.click()
        except Exception as e:
            print('Erro ao clicar no perfil: ')

    def faz_logout(self):
        try:
            perfil = self.mozilla.find_element_by_css_selector(
                'body > div.position-relative.js-header-wrapper > header >'
                ' div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > details-menu > form > button')
            perfil.click()
        except Exception as e:
            print('Erro fazer logout:', e)

    def verifica_usuario(self, usuario):
        profile_link = self.mozilla.find_element_by_class_name(
            'user-profile-link')
        profile_link_html = profile_link.get_attribute('innerHTML')
        assert usuario in profile_link_html


    def faz_login(self):
        try:
            input_login = self.mozilla.find_element_by_link_text('login_field')
            input_password = self.mozilla.find_element_by_id('password')
            btn_login = self.mozilla.find_element_by_name('commit')

            input_login.send_keys('otaviomirandabr@gmail.com')
            input_password.send_keys('0t@v10MirandaB3')
            sleep(3)
            btn_login.click()

        except Exception as e:
            print('Erro as fazer login: ', e)

if __name__ == '__main__':
    mozilla = MozillaAuto()
    mozilla.acessa('https://github.com/')

    mozilla.clica_perfil()
    mozilla.faz_logout()

    mozilla.clica_sing_in()
    mozilla.faz_login()

    mozilla.clica_perfil()
    mozilla.verifica_usuario('otaviomirandabr')

    sleep(30)
    mozilla.sair()





