import requests

def obter_previsao(cidade, chave_api):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric"
    resposta = requests.get(url)
    dados = resposta.json()
    return dados

def exibir_previsao(previsao):
    if previsao["cod"] == 200:
        temperatura = previsao["main"]["temp"]
        descricao = previsao["weather"][0]["description"]
        print(f"Temperatura: {temperatura}°C")
        print(f"Condição: {descricao}")
    else:
        print("Cidade não encontrada.")

if __name__ == "__main__":
    cidade = input("Digite o nome da cidade: ")
    chave_api = "sua_chave_api_aqui"  # Substitua pela sua chave de API
    previsao = obter_previsao(cidade, chave_api)
    exibir_previsao(previsao)
