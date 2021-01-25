from underleague_toolbox.locations import LocationGenerator

NLOCS = 8

if __name__=="__main__":

    print("AZ Locations:")
    azlg = LocationGenerator(module="usa_az")
    for loc in azlg.generate(N=NLOCS):
        print(f" - {loc}")

    print("VT Locations:")
    vtlg = LocationGenerator(module="usa_vt")
    for loc in vtlg.generate(N=NLOCS):
        print(f" - {loc}")

    print("MS Locations:")
    mslg = LocationGenerator(module="usa_ms")
    for loc in mslg.generate(N=NLOCS):
        print(f" - {loc}")

