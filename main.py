from requests import session

url = "https://nfgoiana.economia.go.gov.br/nfg/cidadao/"

def getToken(s, cookie):                                          header = {"Host": "nfgoiana.economia.go.gov.br", "Connection": "keep-alive", "Cache-Control": "max-age=0", "sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"', "sec-ch-ua-mobile": "?1", "sec-ch-ua-platform": '"Android"', "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Linux; Android 10; M2010J19SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Mobile Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7", "Cookie": cookie}

  response = s.get(url + "cadastrar", headers = header)

  return response.text[458:478]

def getCookie(s):
  header = {"Host": "nfgoiana.economia.go.gov.br", "Connection": "keep-alive", "sec-ch-ua": '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"', "sec-ch-ua-mobile": "?1", "sec-ch-ua-platform": '"Android"', "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Linux; Android 10; M2010J19SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"}

  response = s.get(url + "login", headers = header)

  response_headers = response.headers
  response_content = response.text
  cookie_list = []

  for i in response_headers['Set-Cookie'].split(","):
    cookie_list.append(i.replace(" ", "").split(";")[0])

  return f"{cookie_list[0]}; {cookie_list[3]}; {cookie_list[1]}; {cookie_list[2]}"

def createRegister(s, token, cookie, cpf, nome, nomeDaMae, dataDeNascimento):
  header = {"Host": "nfgoiana.economia.go.gov.br", "Connection": "keep-alive", "sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"', "X-CSRF-TOKEN": token, "sec-ch-ua-mobile": "?1", "User-Agent": "Mozilla/5.0 (Linux; Android 10; M2010J19SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Mobile Safari/537.36", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "*/*", "X-Requested-With": "XMLHttpRequest", "sec-ch-ua-platform": '"Android"', "Origin": "https://nfgoiana.economia.go.gov.br", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://nfgoiana.economia.go.gov.br/nfg/cidadao/cadastrar", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7", "Cookie": cookie}
  payload = f"nome={nome}&email=&telefone=61+999999999&senha=mmmWWW%40%40%401&senhaAtual=&nomeDaMae={nomeDaMae}&cpf={cpf}&dataDeNascimento={dataDeNascimento}&cep=71261000&tipoLogradouro=765&nomeLogradouro=Mmm&nomeBairro=Mmm&numero=&complemento=&municipio=20000&endHomologado=&participaSortreio=true&recebeEmail=true"

  s.post(url + "efetuarcadastro", headers = header, data = payload)

def registerTeam(s, token, cookie, id):
  header = {"Host": "nfgoiana.economia.go.gov.br", "Connection": "keep-alive", "sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"', "X-CSRF-TOKEN": token, "sec-ch-ua-mobile": "?1", "User-Agent": "Mozilla/5.0 (Linux; Android 10; M2010J19SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Mobile Safari/537.36", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "*/*", "X-Requested-With": "XMLHttpRequest", "sec-ch-ua-platform": '"Android"', "Origin": "https://nfgoiana.economia.go.gov.br", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://nfgoiana.economia.go.gov.br/nfg/cidadao/inicioSite", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7", "Cookie": cookie}

  return s.post(url + "gravaTimeFutebol", data = "idTime=" + id, headers = header)

def main(cpf, nome, nomeDaMae, dataDeNascimento, id="4"):
  with session() as s:
    cookie = getCookie(s)
    token = getToken(s, cookie)

    createRegister(s, token, cookie, cpf, nome, nomeDaMae, dataDeNascimento)
    return registerTeam(s, token, cookie, id)
