# CSRankings University Filter

A simple Python script to filter researchers by university affiliation from the [CSRankings](https://github.com/emeryberger/CSRankings) dataset.

## Author

Khamidullokhon Abdurakhmonov
GitHub: https://github.com/KhamidullokhonA  
Email: hamidulloielts7782@gmail.com

## Requirements

- Python 3.x
- `requests` library

## Installation

```bash
pip install requests
```

## Usage

```bash
python csrankings_filter.py "University Name"
```

### Examples

```bash
python csrankings_filter.py "Florida International University"
python csrankings_filter.py "Massachusetts Institute of Technology"
python csrankings_filter.py "University of Florida"
```

## Output

- Prints a table of matching researchers (name, affiliation, homepage) to the terminal
- Saves results to a CSV file named after the university (e.g. `florida_international_university_researchers.csv`)

## Sample Output

```
Searching for researchers at: Florida International University

[OK] csrankings-a.csv processed
...

Found 5 people affiliated with 'Florida International University':

Name                                Affiliation                                   Homepage
------------------------------------------------------------------------------------------------------------------------
John Doe                            Florida International University              https://example.com
...

Results saved to 'florida_international_university_researchers.csv'
```

## Data Source

All data is fetched directly from the [CSRankings GitHub repository](https://github.com/emeryberger/CSRankings) — no need to clone or download anything manually.

## License

MIT

