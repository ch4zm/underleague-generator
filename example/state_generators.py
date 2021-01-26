from underleague_generator.geography import (
    StatesGenerator,
    BigStatesGenerator,
    SmallStatesGenerator
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
    
    print("  List of randomly generated states (any size):")
    
    sg = StatesGenerator(country_code=country_code)
    for state in sg.generate(size=8):
        print(f"    - {state}")
    
    print("  List of randomly generated big states:")
    
    bsg = BigStatesGenerator(country_code=country_code)
    for state in bsg.generate(size=4):
        print(f"    - {state}")
    
    print("  List of randomly generated small states:")
    
    ssg = SmallStatesGenerator(country_code=country_code)
    for state in ssg.generate(size=4):
        print(f"    - {state}")


if __name__ == "__main__":
    main()

