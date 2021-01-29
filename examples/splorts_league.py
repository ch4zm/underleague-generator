import json
from underleague_generator.splortsleague import SplortsLeagueGenerator


def main():
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

    print("\n")
    print("-"*40)
    print("\n")


if __name__ == "__main__":
    main()
