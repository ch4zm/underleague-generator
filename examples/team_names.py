from underleague_generator.teams import TeamNameGenerator


def main():
    tg = TeamNameGenerator()
    res = tg.generate(size=8)
    print("\n".join(res))


if __name__ == "__main__":
    main()
