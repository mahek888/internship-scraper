import csv

def save_to_csv(jobs, filename="internships.csv"):
    """
    Saves the scraped jobs to a CSV file.
    """

    if not jobs:
        print("No matching jobs found. CSV file was not created.")
        return

    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "Title",
                    "Company",
                    "Location",
                    "Date",
                    "Link"
                ]
            )

            writer.writeheader()
            writer.writerows(jobs)

        print(f"\nSuccessfully saved {len(jobs)} job(s) to '{filename}'.")

    except PermissionError:
        print("Error: Unable to write to the CSV file. Please close it if it is already open.")

    except Exception as e:
        print(f"Error while saving CSV: {e}")