import requests
import datetime


def get_current_time(request):
    url = 'https://api.taxideli.ru/test/gettime'
    response = requests.post(url)
    ms = response.json().get('dataAns')
    date = datetime.datetime.fromtimestamp(ms / 1000).strftime('%a, %d.%M.%Y %H:%M ')

    return {"current_date": date}
