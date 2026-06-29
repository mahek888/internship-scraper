from scraper import scrape_jobs
from csv_utils import save_to_csv

def main():

    print("=" * 40)
    print("       Internship Scraper")
    print("=" * 40)

    keyword = input("\nEnter keyword to search: ").strip()

    if not keyword:
        print("Error: Keyword cannot be empty.")
        return

    jobs = scrape_jobs(keyword)

    if not jobs:
        print(f"No internships found matching '{keyword}'.")
        return

    print(f"Found {len(jobs)} matching internship(s).\n")

    print("Saving results to CSV...")

    save_to_csv(jobs)

    print("\nDone!")


if __name__ == "__main__":
    main()