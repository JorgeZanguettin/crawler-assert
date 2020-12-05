# **Asserti**

## O que é Asserti?

ASSERTI representa a integração entre as atividades empresariais e o poder público em todas as suas esferas. Neste contexto, a Asserti, como principal órgão representativo do setor de Tecnologia da Informação da região, elaborou o projeto para reconhecimento do Arranjo Produtivo Local de Tecnologia da Informação de Marília – APL TI Marília, junto ao Governo do Estado de São Paulo.

## **Dados Coletados**

## Variaveis

```yaml
{
nome_empresa : String,
telefone_empresa : String,
endereco_empresa : String,
email_empresa : String,
site_empresa : String,
atuacao_empresa : String
}
```

## Amostra

| NOME_EMPRESA | TELEFONE_EMPRESA | ENDERECO_EMPRESA | EMAIL_EMPRESA | SITE_EMPRESA | ATUACAO_EMPRESA  | 
| --- | --- | --- | --- | --- | --- |
| ADJ SISTEMAS | 3316-9968 | RUA CAMPOS SALLES | ageu@adjsistemas.com.br | http://www.adjsistemas.com.br/ | Estamos no mercado de tecnologia da informacao desde 1994, no inicio desenvolviamos sob encomenda softwares especificos para diversos tipos de atividades e negocios. |
| AFL Sistemas | (14) 3405-1199 | Rua Brasilia | adilson@aflsistemas.com.br | http://aflsistemas.com.br | Desenvolvimento de Software: Enterprise Resource Planning (ERP), Customer Relationship Management (CRM), Business Intelligence (BI), E-commerce, Site Institucional, Portal de Conhecimento |
| AG Sistemas | (14) 3441-7013 | Rua Leticiano Jesus Costa | galdino@agsistemasonline.com.br | http://www.agsistemasonline.com.br | Sistemas de Gestao Empresarial - ERPSistema para Gestao de empresas de Formaturas, Eventos, e Recordacao EscolarPet Shop, clinicas veterinariasLojas de Confeccao |
| ALIVE IT | (14) 3367-1999 | AVENIDA BRIGADEIRO EDUARDO GOMES | NETO@ALIVE.INF.BR | http://WWW.ALIVE.INF.BR | DESENVOLVIMENTO DE SOFTWARE PARA POSTO DE COMBUSTIVEL |
| Acacia Consultoria | 14-2105-3333 | AVENIDA RIO BRANCO | acacia@acaciaconsultoria.com.br | http://www.acaciaconsultoria.com.br | Desenvolvimento de Solucoes de Mobilidade - especialista em venda, treinamento, customizacao e suporte de softwares para Automacao da Forca de Vendas, Trade Marketing, Logistica e Produtos Especiais |

## Como executar?

1. Faça o download e instalação do Python 3 [Aqui](https://www.python.org/).
2. Direcione o seu bash de preferencia a pasta raiz do repositorio e instale as dependencias utilizando o comando ```pip install -r requirements.txt``` ou ```pip3 install -r requirements.txt``` .
3. Execute o Crawler com o comando ```python asserti.py``` ou ```python3 asserti.py``` .
4. Pronto! Os dados coletados serão armazenados em um arquivo CSV na raiz do projeto com o nome **empresas.csv**.
