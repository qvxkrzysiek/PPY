import requests

url = input("Podaj URL strony do wczytania: ")
dates = ["20200101", "20210101", "20220101"]

for date in dates:
    js = requests.get(f"https://archive.org/wayback/available?url={url}&timestamp={date}").json()
    archivedUrl = js["archived_snapshots"]["closest"]["url"]
    html = requests.get(archivedUrl).text
    with open(f"page_{date}.html", "w") as f:
        f.write(html)
