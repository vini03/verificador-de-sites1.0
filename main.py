import requests

def menu():
  escolha = str(input("Verifica mais um site s/n?")).lower()
  if escolha == "s":
    main()
  elif escolha == "n":
    print("Verificacao encerrada!")
    return
  else:
    print("Opcao Invalida")
    menu()

def main():
   #print de boas vindas
   print('Insira um site para a verificação:')
   #pega urls (input)
   urls = str(input()).lower().split(",")
   #percorre cada url ////
   for url in urls:
      url = url.strip()
      if "." not in url:
         print(url, "url invalida")
      else:
        if "http" not in url:
          url = f"http://{url}"
          print(url)
        try:
           requisicao = requests.get(url)
           if requisicao.status_code == 200:
              print("O Site esta online")
           else:
              print("O Site esta offline")
        except:
           print (url, "erro") 

   menu()

main()



## Já deixei instalado o package do Requests e também importado aqui para você. Está pronto para usar.
## E não se esquece de pesquisar sobre try: e except: para tratar erros do Request. (isso pode te ajudar)

## pode apagar esses comentários haha.

 
## Bom desafio!