import requests

api_key = "RGAPI-4a1c6b07-9405-4e3e-a803-068e01d604cd"
summoner_id = "HhD2OXtWjSJ0Ve8-Imq-atiZ_anT9xhMgT085672qH10zQ"
account_id = "C5Ixs54L_9EhAjxf2lbGx9Y2FNd79WOaOVgsIfhstTxPwtw"
puuid = "-LFTrXUiRNSwEJQ1ZCA43OGGBbvjPvaalWs66VDQM5Wn1rSXyQp--BIOWJ9JfZWlL9j4DoOPuEs72w"


def summoner_data(summoner_name, api_key):
    url = "https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}".format(summoner_name, api_key)
    request = requests.get(url)
    response = request.json()
    summoner_level = response['summonerLevel']
    response = [summoner_level]
    return response


def summoner_ranked_data(summoner_id, api_key):
    url = "https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/{}?api_key={}".format(summoner_id, api_key)
    request = requests.get(url)
    response = request.json()
    tier = response[0]['tier']
    rank = response[0]['rank']
    summoner_name = response[0]['summonerName']
    pdl = response[0]['leaguePoints']
    wins = response[0]['wins']
    losses = response[0]['losses']
    response = [tier, rank, summoner_name, pdl, wins, losses]
    return response


def champion(id):
    url = "http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json"
    request = requests.get(url)
    response = request.json()
    for champion in response['data'].values():
        if champion['key'] == id:
            print(champion)


print(summoner_data("rusher7", api_key))
print(summoner_ranked_data(summoner_id, api_key))
champion('245')