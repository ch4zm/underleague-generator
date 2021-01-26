from underleague_generator.geography import (
    CitiesGenerator,
    BigCitiesGenerator,
    SmallTownsGenerator
)


def main():

    print("\n\nDemo of the underleague generator geography submodule\n\n")

    demo("usa")
    demo("mex")
    demo("can")
    demo("fra")
    demo("rus")


def demo(country_code):

    print("\n")
    print("-"*40)
    print(f"Country: {country_code}")
    
    print("  List of randomly generated cities (any size):")
    
    cg = CitiesGenerator(country_code=country_code)
    for city in cg.generate(size=8):
        print(f"    - {city}")
    
    print("  List of randomly generated big cities:")
    
    bcg = BigCitiesGenerator(country_code=country_code)
    for city in bcg.generate(size=4):
        print(f"    - {city}")
    
    print("  List of randomly generated small cities:")
    
    scg = SmallTownsGenerator(country_code=country_code)
    for city in scg.generate(size=4):
        print(f"    - {city}")


if __name__ == "__main__":
    main()


