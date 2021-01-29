from underleague_generator.geography import (
    StatesGenerator,
    BigStatesGenerator,
    SmallStatesGenerator
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
    print(f"Country: {country_code}")
    
    print(f"\n  List of randomly generated states in {country_name} (any size):")
    
    sg = StatesGenerator(country_code=country_code)
    for state in sg.generate(size=8):
        print(f"    - {state}")
    
    print(f"\n  List of randomly generated big states in {country_name}:")
    
    bsg = BigStatesGenerator(country_code=country_code)
    for state in bsg.generate(size=4):
        print(f"    - {state}")
    
    print(f"\n  List of randomly generated small states in {country_name}:")
    
    ssg = SmallStatesGenerator(country_code=country_code)
    for state in ssg.generate(size=4):
        print(f"    - {state}")

    print("\n\n")


if __name__ == "__main__":
    main()

