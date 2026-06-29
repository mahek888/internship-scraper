from bs4 import BeautifulSoup

from utils import get_page, polite_delay, can_fetch


URL = "https://realpython.github.io/fake-jobs/"


def scrape_jobs(keyword):
    """
    Scrapes internship/job listings matching the keyword.
    Returns a list of dictionaries.
    """

    jobs = []

    if not can_fetch(URL):
        print("Scraping is not allowed by robots.txt.")
        return jobs

    html = get_page(URL)

    if html is None:
        return jobs

    polite_delay()

    soup = BeautifulSoup(html, "html.parser")

    cards = soup.find_all("div", class_="card-content")

    print(f"Found {len(cards)} listings.\n")

    keyword = keyword.lower()

    for card in cards:

        try:
            title = card.find("h2").get_text(strip=True)
        except AttributeError:
            title = "N/A"

        try:
            company = card.find("h3").get_text(strip=True)
        except AttributeError:
            company = "N/A"

        try:
            location = card.find("p", class_="location").get_text(strip=True)
        except AttributeError:
            location = "N/A"

        try:
            date = card.find("time").get_text(strip=True)
        except AttributeError:
            date = "N/A"

        try:
            link = card.find("a")["href"]
        except (AttributeError, TypeError, KeyError):
            link = "N/A"

        searchable = (
            title.lower()
            + " "
            + company.lower()
            + " "
            + location.lower()
        )

        if keyword in searchable:
            jobs.append(
                {
                    "Title": title,
                    "Company": company,
                    "Location": location,
                    "Date": date,
                    "Link": link,
                }
            )

    return jobs