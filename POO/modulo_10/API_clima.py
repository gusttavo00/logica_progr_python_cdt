import requests

def obter_clima(cidade, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"
    
    try:
        resposta = requests.get(url, timeout=5)  # timeout evita travar se a API não responder
        resposta.raise_for_status()  # gera erro se o código HTTP for 4xx ou 5xx

        dados = resposta.json()

        if "main" in dados and "weather" in dados:
            temperatura = dados["main"]["temp"]
            condicao = dados["weather"][0]["description"]
            print(f" Cidade: {cidade}")
            print(f" Temperatura: {temperatura}°C")
            print(f" Condições: {condicao}")
        else:
            print("Resposta inesperada da API:", dados)

    except requests.exceptions.ConnectionError:
        print(" Erro de conexão. Verifique sua internet.")
    except requests.exceptions.Timeout:
        print(" A requisição demorou muito e foi cancelada.")
    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    API_KEY = "Sf972xxxxxxxxxxxxxxxxxxxxxxx178"
    cidade = input("Digite o nome da cidade: ")
    obter_clima(cidade, API_KEY)
