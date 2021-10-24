from requests import post,get

def gravaTime(cookie,token):
  h7 = {
    "Host": "nfgoiana.economia.go.gov.br",
    "Connection": "keep-alive",
    "Content-Length": "8",
    "sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    "X-CSRF-TOKEN": token,
    "sec-ch-ua-mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; M2010J19SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua-platform": '"Android"',
    "Origin": "https://nfgoiana.economia.go.gov.br",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://nfgoiana.economia.go.gov.br/nfg/cidadao/inicioSite",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": cookie
  }
  url="https://nfgoiana.economia.go.gov.br/nfg/cidadao/gravaTimeFutebol"
  return post(url, data="idTime=5", headers=h7).text
  
def geraCookie():
  h2 = {
    "Host": "nfgoiana.economia.go.gov.br",
    "Connection": "keep-alive",
    "sec-ch-ua": '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; M2010J19SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
  }
  url="https://nfgoiana.economia.go.gov.br/nfg/cidadao/login"
  data = get(url,headers=h2)
  newdata = data.text
  data = str(data.headers)
  dados = data[0:776]
  dados = dados.split(";")
  primeiraParte=dados[0][16:76]+";"
  segundaParte=dados[5][9:]+";"
  terceiraParte=dados[2][12:]+";"
  ultimaParte=dados[4][11:]
  csrf= newdata.split('<meta name="_csrf" content="')[0]
 
  return f'''{primeiraParte} {segundaParte} {terceiraParte} {ultimaParte}'''

def obterToken(cookie):
  headers = {
    "Host": "nfgoiana.economia.go.gov.br",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; M2010J19SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": cookie
  }
  url="https://nfgoiana.economia.go.gov.br/nfg/cidadao/cadastrar"
  return get(url,headers=headers).text[458:478]


def criaCadastro(cpf,nome,nomeDaMae,dataDeNascimento):
  data=f"nome={nome}&email=&telefone=61+999999999&senha=mmmWWW%40%40%401&senhaAtual=&nomeDaMae={nomeDaMae}&cpf={cpf}&dataDeNascimento={dataDeNascimento}&cep=71261000&tipoLogradouro=765&nomeLogradouro=Mmm&nomeBairro=Mmm&numero=&complemento=&municipio=20000&endHomologado=&participaSortreio=true&recebeEmail=true"
  cookie = geraCookie()
  token = obterToken(cookie)
  h5 = {
    "Host": "nfgoiana.economia.go.gov.br",
    "Connection": "keep-alive",
    "Content-Length": "336",
    "sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    "X-CSRF-TOKEN": token,
    "sec-ch-ua-mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; M2010J19SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua-platform": '"Android"',
    "Origin": "https://nfgoiana.economia.go.gov.br",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://nfgoiana.economia.go.gov.br/nfg/cidadao/cadastrar",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": cookie
  }
  url="https://nfgoiana.economia.go.gov.br/nfg/cidadao/efetuarcadastro"
  cadastro = post(url,data=data, headers=h5)
  return gravaTime(cookie,token)
