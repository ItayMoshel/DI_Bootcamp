import requests


def loadingtime(link):
    time = requests.get(link).elapsed.total_seconds()
    return time


print(loadingtime("https://www.ynet.co.il/"))
print(loadingtime("https://www.google.com/"))
print(loadingtime("https://www.youtube.com/"))
print(loadingtime("https://www.imdb.com/"))
