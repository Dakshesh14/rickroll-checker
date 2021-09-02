import requests

from time import sleep

# beautifulsoup4
# https://pypi.org/project/beautifulsoup4/

from bs4 import BeautifulSoup

# termcolor (for making colorfull text in the console)
# https://pypi.org/project/termcolor/

from termcolor import colored

prev_views = 0

def main(url):

    # requests send request to the url and get all the html
    request_data = requests.get(url)

    # BeautifulSoup parser that data to html so that we can extrate all the data like views, like, etc.. in this case
    s = BeautifulSoup(request_data.text, "html.parser")

    views = s.find("meta", itemprop="interactionCount")['content'] # this find function actually finds the views

    return int(views)

if __name__ == "__main__":
    print("Main function ran")
    while True:
        sleep(10)
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

        # calling the function
        new_view = main(url)

        if new_view > prev_views:
            prev_views = new_view
            print(colored("Someone got rickrolled", "green"))