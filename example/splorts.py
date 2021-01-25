from underleague_toolbox.splorts import SplortsGenerator

if __name__=="__main__":

    sg = SplortsGenerator()
    for spl in sg.generate(N=10, adjectives=True):
        print(f"{spl}")
