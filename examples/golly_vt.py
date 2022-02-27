import json
from underleague_generator.splortsleague import SplortsLeagueGenerator


def vt():
    slg = SplortsLeagueGenerator(country_code="usatn", geo="cities")
    res = slg.generate(nleagues=2, ndivisions=3, teams_per_division=6)

    teams = []
    for league in res:
        divisions = res[league]
        for division in divisions:
            teams += divisions[division]


    with open('teams.txt', 'w') as f:
        f.write("\n".join(teams))


    print("\n")
    print("-"*40)
    print("\n")

    for league in res:
        print(" "*4 + f"{league} League:\n")
        divisions = res[league]
        for division in divisions:
            print(" "*8 + f"{division} Division:\n")
            teams = divisions[division]
            for team in teams:
                print(f" "*12 + f"{team}")
            print("\n")


if __name__ == "__main__":
    vt()
