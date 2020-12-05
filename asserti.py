import requests
from unidecode import unidecode
from bs4 import BeautifulSoup

class Crawler():
    def __init__(self):
        self.sendLogToSystem('DEBUG', 'Start Crawler')
        self.getListEmpresas()
        self.sendLogToSystem('DEBUG', 'Finish Crawler')

    def sendLogToSystem(self, type_log, message):
        print (f'[ {type_log} ] {message}')

    def getListEmpresas(self):
        req  = requests.get('http://asserti.org/pages/associados.aspx?tp=full&fbclid=IwAR2Q1DTJPyVHhIs-sBHKxnWVLGj837KBqAi5AYrV4qZF3Ig_l4I51IuTR1Q')
        soup = BeautifulSoup(req.content, 'html.parser')

        for empresa_tag_a in soup.select('div.boxApresentacao a'):
            url_empresa = 'http://asserti.org/pages/' + str(empresa_tag_a['href']).strip()

            req_empresa = requests.get(url_empresa)
            soup_empresa = BeautifulSoup(req_empresa.content, 'html.parser')

            data_empresa = {
                'nome_empresa' : self.tratarString(soup_empresa.select_one("span#lblNome")),
                'telefone_empresa' : self.tratarString(soup_empresa.select_one("span#lblTelefone")),
                'endereco_empresa' : self.tratarString(soup_empresa.select_one("span#lblEndereco")),
                'email_empresa' : self.tratarString(soup_empresa.select_one("span#lblEmail")),
                'site_empresa' : self.tratarString(soup_empresa.select_one("span#lnkSite")),
                'atuacao_empresa' : self.tratarString(soup_empresa.select_one("textarea#txtAtuacao")),
            }

            self.sendLogToSystem('DEBUG', 'Empresa Coletada - {}'.format(data_empresa['nome_empresa']))
            self.saveInFile(data_empresa)

    def saveInFile(self, dict_empresa):
        file = open('empresas.csv', 'a+', encoding='utf-8')
        file.write('{};{};{};{};{};{}\n'.format(
            dict_empresa['nome_empresa'],
            dict_empresa['telefone_empresa'],
            dict_empresa['endereco_empresa'],
            dict_empresa['email_empresa'],
            dict_empresa['site_empresa'],
            dict_empresa['atuacao_empresa'],
        ))

        file.close()

    def tratarString(self, obj_bs4):
        if obj_bs4 != None:
            return unidecode(str(obj_bs4.text).replace('\r','').replace('\n','').strip())
        else:
            return ''        

Crawler()