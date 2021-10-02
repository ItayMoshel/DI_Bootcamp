import requests


def loadingtime(link):
    time = requests.get(link).elapsed.total_seconds()
    print(time)


loadingtime("https://www.ynet.co.il/")
loadingtime("https://www.google.com/")
loadingtime("https://www.youtube.com/")
loadingtime("https://www.imdb.com/")
