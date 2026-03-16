import requests
import csv
import io
import string
import argparse

REPO_BASE = "https://raw.githubusercontent.com/emeryberger/CSRankings/gh-pages"

def fetch_researchers(university_name):
    results = []

    for letter in string.ascii_lowercase:
        url = f"{REPO_BASE}/csrankings-{letter}.csv"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"[SKIP] csrankings-{letter}.csv not found")
            continue

        reader = csv.DictReader(io.StringIO(response.text))
        for row in reader:
            affil = row.get("affiliation", "").strip()
            if affil.lower() == university_name.lower():
                results.append(row)

        print(f"[OK] csrankings-{letter}.csv processed")

    return results


def print_results(results, university_name):
    print(f"\nFound {len(results)} people affiliated with '{university_name}':\n")
    print(f"{'Name':<35} {'Affiliation':<45} {'Homepage'}")
    print("-" * 120)
    for r in results:
        name     = r.get("name", "N/A")
        affil    = r.get("affiliation", "N/A")
        homepage = r.get("homepage", "N/A")
        print(f"{name:<35} {affil:<45} {homepage}")


def save_results(results, university_name):
    # Create a safe filename from the university name
    safe_name = university_name.lower().replace(" ", "_").replace("/", "_")
    output_file = f"{safe_name}_researchers.csv"

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print(f"\nResults saved to '{output_file}'")


def main():
    parser = argparse.ArgumentParser(
        description="Filter researchers by university affiliation from CSRankings.",
        epilog='Example: python csrankings_filter.py "Florida International University"'
    )
    parser.add_argument(
        "university",
        type=str,
        help='University name to filter by (e.g. "Florida International University")'
    )
    args = parser.parse_args()

    university_name = args.university.strip()
    print(f"\nSearching for researchers at: {university_name}\n")

    results = fetch_researchers(university_name)

    if not results:
        print(f"\nNo researchers found for '{university_name}'.")
        print("Tip: Check the spelling or try a partial match variant.")
        return

    print_results(results, university_name)
    save_results(results, university_name)


if __name__ == "__main__":
    main()
