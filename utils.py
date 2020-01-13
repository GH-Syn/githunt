""" Formats repositories in console """

from colorama import init, Fore, Style
from tabulate import tabulate


def colored_output(repos):
    """ Displays repositories using colorama """

    init()  # initialize coloroma
    seperator = "+---------------------------------------------------------------+"
    print(Fore.WHITE, Style.BRIGHT, seperator)
    for repo in repos:
        print(Fore.LIGHTRED_EX, Style.BRIGHT, f"{repo['full_name']}")
        print()
        print(Fore.RESET, Style.NORMAL, f"{repo['html_url']}")
        print()
        print(Fore.LIGHTCYAN_EX, Style.BRIGHT, f"{repo['language']}", end="\t")
        print(
            Fore.LIGHTCYAN_EX,
            Style.BRIGHT,
            f"{repo['stargazers_count']} Stars",
            end="\t",
        )
        print(Fore.LIGHTCYAN_EX, Style.BRIGHT, f"{repo['forks_count']} Forks", end="\t")
        print(Fore.LIGHTCYAN_EX, Style.BRIGHT, f"{repo['watchers_count']} Watchers")
        print()
        print(Fore.WHITE, Style.BRIGHT, seperator)


def tabular_output(repos):
    """ Displays repositories as tables using tabulate """
    table_headers = ["Name", "URL", "Language", "Stars"]
    repositories = [
        [repo["full_name"], repo["html_url"], repo["stargazers_count"]]
        for repo in repos
    ]
    print(tabulate(repositories, headers=table_headers, tablefmt="fancy_grid"))


def beautify(repos, display_format):
    """ Beautfies the output based on display format given """
    if display_format == "colored":
        colored_output(repos)
    elif display_format == "table":
        tabular_output(repos)
    else:
        print("Can't output anything. Invalid display format!")