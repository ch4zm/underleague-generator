from underleague_toolbox.teams import TeamNameGenerator

if __name__=="__main__":

    tg = TeamNameGenerator()
    for tn in tg.generate(N=10):
        print(f"{tn}")

