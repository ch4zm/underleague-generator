import json
import xmltodict
import os
import re


CITY_POPLIM = 1e3


# This script does the following:
# - load the XML file
# - find usa
# - iterate over each state
# - for each state:
#   - create usa_az.txt with all az cities, etc.


with open('world_full.xml') as f:
    doc = xmltodict.parse(f.read())

world = doc['WORLD']
continents = world['CONTINENTS']

outputdir = 'output'
try:
    os.mkdir(outputdir)
except FileExistsError:
    pass


continents_list = continents['CONTINENT']
for continent in continents_list:

    nations = continent['NATIONS']
    nations_list = nations['NATION']
    for nation in nations_list:

        if nation['@abbr'].lower() == 'usa':

            # Iterate over each state
            states = nation['STATES']
            if states is None:
                continue
            states_list = states['STATE']
            for state in states_list:

                abbr = state['@abbr'].lower()
                sname = state['@name']
                print(f"  State: {sname}")

                # Tuple of city names and populations
                cities_pop = []

                cities = state['CITIES']
                if cities is None:
                    continue
                cities_list = cities['CITY']
                for city in cities_list:

                    try:
                        cpop = int(city['@pop'])
                    except:
                        cpop = 1

                    if cpop > CITY_POPLIM:

                        cname = city['@name']
                        cname = re.sub(r' \(.*\)$', '', cname)

                        cities_pop.append((cname, cpop))

                cities_pop.sort(key=lambda x: x[1])
                sorted_cities = [c[0] for c in cities_pop]

                # Output to file
                scfname = os.path.join(outputdir, f'usa{abbr}.json')
                json_output = {
                    "description": f"Names of cities in {sname}",
                    "cities": sorted_cities
                }
                for city in sorted_cities:
                    print(f"    City: {city}")
                with open(scfname, 'w') as f:
                    json.dump(json_output, f, indent=4)
