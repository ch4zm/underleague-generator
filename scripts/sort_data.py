import os
import glob


DRY_RUN = False

HERE = os.path.abspath(os.path.dirname(__file__))
DATA = os.path.abspath(os.path.join(HERE, '..', 'src', 'data'))


dat_files = sorted(glob.glob(DATA + "/*.txt"))
for dat_file in dat_files:
    print(f"Sorting dat file {dat_file}")
    with open(dat_file, 'r') as f:
        contents = f.readlines()
    # Strip whitespace/newlines
    contents = [s.strip() for s in contents if len(s.strip()) > 0]
    # Eliminate duplicates
    contents = list(set(contents))
    # Sort
    contents.sort()
    if DRY_RUN is False:
        with open(dat_file, 'w') as f:
            f.write("\n".join(contents))

