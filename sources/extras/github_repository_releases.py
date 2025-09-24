#!/usr/bin/env python3
#
####################################################
# Copyright (c) 2025 by Manfred Rosenboom          #
# https://maroph.github.io/ (maroph@pm.me)         #
#                                                  #
# This work is licensed under a CC-BY 4.0 License. #
# https://creativecommons.org/licenses/by/4.0/     #
####################################################
#
# 24-SEP-2025
#
from datetime import datetime
# python3 -m pip install beautifulsoup4
from bs4 import BeautifulSoup
# python3 -m pip install requests
import requests


def print_releases(repository: str = None, max_versions: int = 1) -> None:
    """
    List the most recent GitHub repository release versions to stdout.

    Parameters:
        repository (str):   Name of the GitHub Repository (user/repository).
                            Example: "openssl/openssl"
        max_versions (int): Maximum number of GitHub repository release versions to print.
                            Default: 1

    Returns:
        None.
    """
    if repository is None:
        print("repository is None")
        return
    if not isinstance(repository, str):
        print("repository is not of type str")
        return
    if len(repository) == 0:
        print("repository is an empty string")
        return

    url_release_page = f"https://github.com/{repository}/releases"
    print(f"GitHub Repository: {repository}: {url_release_page}")

    if max_versions is None:
        print("max_versions is None")
        return
    if not isinstance(max_versions, int):
        print("max_versions is not of type str")
        return
    if max_versions < 1:
        print(f"max_versions < 1 [{max_versions}]")
        return

    try:
        response = requests.get(url_release_page)
        soup = BeautifulSoup(response.text, "html.parser")
    except Exception as e:
        print(e)
        return

    # each <section> describes a version
    release_sections = soup.select("div[data-hpc] section")
    if release_sections is None:
        print("no release sections found")
        return
    # print(f"release_sections: {release_sections}")

    if len(release_sections) == 0:
        print("no releases available")
        return

    count = 0
    for rel in release_sections:
        # <h2>: version name
        # <relative-time datetime="...">: release datetime
        # https://github.com/github/relative-time-element
        try:
            version = rel.find("h2").text.strip()
            version_date = rel.find("relative-time").get("datetime")
        except Exception as e:
            print(e)
            continue

        mark = False
        if version_date is not None and len(version_date) > 0:
            try:
                dt = datetime.strptime(version_date, '%Y-%m-%dT%H:%M:%S%z')
                days = (dt.date().today() - dt.date()).days + 1
                if days < 31:
                    mark = True
            except Exception as e:
                pass

        if mark:
            print(f"** {version} - {version_date}")
        else:
            print(f"{version} - {version_date}")
        count += 1
        if count >= max_versions:
            break

if __name__ == "__main__":
    print_releases("curl/curl")
    print('----------')
    print_releases("gohugoio/hugo")
    print('----------')
    print_releases("microsoft/edit")
    print('----------')
    print_releases("mkdocs/mkdocs")
    print('----------')
    print_releases("squidfunk/mkdocs-material")
    print('----------')
    print_releases("jgm/pandoc")
    print('----------')
    print_releases("openssl/openssl", max_versions=8)
