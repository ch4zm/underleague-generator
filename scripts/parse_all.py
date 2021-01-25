import xmltodict
import os
import re


# Only include nations with at least this population
NATION_POPLIM = 1e7

# Only include cities with at least this population
CITY_POPLIM = 1e3


# This script does the following:
# - load the XML file
# - iterate over each content/nation/state/city
# - for each nation above nation population limit:
#   - create <country-code>.txt with cities greater than city population limit
#   - create <country-code>_states.txt with names of states
# - cities and states shall be sorted in order from largest first to smallest last


with open('world_full.xml') as f:
    doc = xmltodict.parse(f.read())

world = doc['WORLD']
continents = world['CONTINENTS']

outputdir = 'output'
try:
    os.mkdir(outputdir)
except FileExistsError:
    pass


abbr_map = {}
continents_list = continents['CONTINENT']
for continent in continents_list:

    nations = continent['NATIONS']
    nations_list = nations['NATION']
    for nation in nations_list:

        # Store tuples - city/state name and population
        cities_pop = []
        states_pop = []

        # The final list of cities and states that will go into the files
        final_cities = []
        final_states = []

        try:
            pop = int(nation['@pop'])
        except:
            pop = 1

        abbr = nation['@abbr'].lower()

        if pop > NATION_POPLIM:
            print(f"Nation: {nation['@name']} ({abbr})")

            abbr_map[abbr] = nation['@name']

            states = nation['STATES']
            if states is None:
                continue
            states_list = states['STATE']
            for state in states_list:

                sname = state['@name']
                sname = re.sub(r' \(.*\)$', '', sname)
                final_states.append(sname)
                print(f"  State: {sname}")

                try:
                    spop = int(state['@pop'])
                except:
                    spop = 1

                # No population limit for states, save all of them
                states_pop.append((sname, spop))

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
                        final_cities.append(cname)
                        print(f"    City: {city['@name']}")

                        cities_pop.append((cname, cpop))

        cities_pop.sort(key=lambda x: x[1], reverse=True)
        final_cities = [c[0] for c in cities_pop]

        states_pop.sort(key=lambda x: x[1], reverse=True)
        final_states = [s[0] for s in states_pop]

        if len(final_cities)>0:
            cfname = os.path.join(outputdir, f'{abbr}.txt')
            with open(cfname, 'w') as f:
                f.write("\n".join(final_cities))

        if len(final_states)>0:
            sfname = os.path.join(outputdir, f'{abbr}_states.txt')
            with open(sfname, 'w') as f:
                f.write("\n".join(final_states))

keyfname = os.path.join(outputdir, '_ABBR_KEY')
with open(keyfname, 'w') as f:
    f.write("\n".join([f"{abbr.upper()} {name}" for abbr, name in abbr_map.items()]))
