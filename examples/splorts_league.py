import json
from underleague_generator.splortsleague import SplortsLeagueGenerator


def default_splorts_league():
    slg = SplortsLeagueGenerator()
    res = slg.generate()

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


def can_splorts_league():
    slg = SplortsLeagueGenerator(country_code="can", geo="bigcities")
    res = slg.generate()

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
    default_splorts_league()
    can_splorts_league()
