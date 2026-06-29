import time
import requests
from urllib.robotparser import RobotFileParser


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}


def can_fetch(url):
    """
    Checks whether scraping is allowed using robots.txt.
    Returns True if allowed, False otherwise.
    """

    try:
        robots_url = url.rstrip("/") + "/robots.txt"

        rp = RobotFileParser()
        rp.set_url(robots_url)
        rp.read()

        return rp.can_fetch(HEADERS["User-Agent"], url)

    except Exception:
        # If robots.txt cannot be reached,
        # allow scraping instead of crashing.
        return True


def polite_delay():
    """
    Wait for one second between requests.
    """

    time.sleep(1)


def get_page(url):
    """
    Downloads a webpage safely.
    Returns the HTML if successful.
    """

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=10
        )

        response.raise_for_status()

        return response.text

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: No internet connection.")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

    return None