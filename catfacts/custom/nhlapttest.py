#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    nhl = requests.get("https://statsapi.web.nhl.com/api/v1/teams")

    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library
    #print(nhl.json())

    teams = nhl.json().get('teams')

    for team in teams:
        team_name = team.get('teamName')
        print(team_name)
main()


