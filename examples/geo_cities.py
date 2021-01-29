from underleague_generator.geography import (
    CitiesGenerator,
    BigCitiesGenerator,
    SmallTownsGenerator
)


def main():

    print("\n\nDemo of the underleague generator geography submodule\n\n")

    demo("usa", "USA")
    demo("mex", "Mexico")
    demo("can", "Canada")
    demo("fra", "France")
    demo("rus", "Russia")


def demo(country_code, country_name):

    print("\n")
    print("-"*40)
    print(f"Country Name: {country_name}")
    print(f"Country Code: {country_code}")
    
    print(f"\n  List of randomly generated cities in {country_name} (any size):")
    
    cg = CitiesGenerator(country_code=country_code)
    for city in cg.generate(size=8):
        print(f"    - {city}")
    
    print(f"\n  List of randomly generated big cities in {country_name}:")
    
    bcg = BigCitiesGenerator(country_code=country_code)
    for city in bcg.generate(size=4):
        print(f"    - {city}")
    
    print(f"\n  List of randomly generated small cities in {country_name}:")
    
    scg = SmallTownsGenerator(country_code=country_code)
    for city in scg.generate(size=4):
        print(f"    - {city}")

    print("\n\n")


if __name__ == "__main__":
    main()
