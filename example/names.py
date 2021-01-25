from underleague_toolbox.players import PlayerNameGenerator

NPLAYERS = 30

if __name__=="__main__":
    png = PlayerNameGenerator()
    print("\n".join(png.generate(N=NPLAYERS)))
