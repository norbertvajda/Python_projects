import requests


def main():
    url = "http://index.hu"
    r = requests.get(url)
    print(r.text)

##############################################################


if __name__ == "__main__":
    main()
