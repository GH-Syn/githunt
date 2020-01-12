""" Browse most stared repositories by date on Github """

# Standard library imports
from datetime import datetime, timedelta

# Third party imports
import click
import requests

API_URL = "https://api.github.com/search/repositories"


@click.command()
@click.option("--language", default="", help="language filter (eg: python)")
@click.option(
    "--date",
    default="",
    help="date in the ISO8601 format which is YYYY-MM-DD (year-month-day)",
)
def search(language, date):
    """ Returns repositories based on the language.
        repositories are sorted by stars
    """

    if not date:
        start_date = datetime.fromisoformat(
            datetime.utcnow().date().isoformat()
        )  # today's timestamp in YYYY-MM-DD:00:00:00 format
        end_date = datetime.fromisoformat(
            (datetime.utcnow() + timedelta(days=1)).date().isoformat()
        )  # next day's timestamp in YYYY-MM-DD:00:00:00 format
    else:
        start_date = datetime.fromisoformat(date)
        end_date = datetime.fromisoformat(
            (start_date + timedelta(days=1)).date().isoformat()
        )

    query = (
        f"language:{language}+created:{start_date.isoformat()}..{end_date.isoformat()}"
    )
    url = f"{API_URL}?q={query}&sort=stars&order=desc"
    repositories = requests.get(url).json()
    print(repositories)


if __name__ == "__main__":
    search()