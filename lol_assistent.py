import requests

def Summoner_data(summoner_name, api_key):
    url = ("https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}").format(summoner_name, api_key)
    request = requests.get(url)
    response = request.json()
    summoner_level = response['summonerLevel']
    response = [summoner_level]
    return response


def Summoner_ranked_data(summoner_id, api_key):
    url = ("https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/{}?api_key={}").format(summoner_id, api_key)
    request = requests.get(url)
    response = request.json()
    tier = response[0]['tier']
    rank = response[0]['rank']
    summoner_name = response[0]['summonerName']
    pdl = response[0]['leaguePoints']
    wins = response[0]['wins']
    losses = response[0]['losses']
    response = [tier,rank,summoner_name,pdl,wins,losses]
    return response

print(Summoner_data("rusher7", "RGAPI-4f3c507f-0c76-42cb-8bd6-f246415bc02e"))
print(Summoner_ranked_data("HhD2OXtWjSJ0Ve8-Imq-atiZ_anT9xhMgT085672qH10zQ", "RGAPI-4f3c507f-0c76-42cb-8bd6-f246415bc02e"))