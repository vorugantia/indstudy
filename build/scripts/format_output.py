# Load the JSON output files that came directly from ParseHub
# Output file is the formatted table combining the results from every news source
import json
import re

with open('../input/senator_list.json') as senator_list:
    senators = json.load(senator_list)

table = []
def fill_table(parsehub):
    for i in parsehub['results']:
        search_terms = i['searchTerm'].split(" AND ")

        # TODO: make a row in the table called "ideology" to give more weight to most polarizing figures.
        row = {
            'senator': '',
            'party': '',
            'source': '',
            'numResults': ''
        }
        row['senator'] = find_senator(search_terms[1])
        row['party'] = find_party(search_terms[1])
        row['source'] = find_source(search_terms[0])
        if(i.get('numberofResults') is not None):
            numResults = find_numResults(i['numberofResults'])
        else:
            numResults = '0'
        row['numResults'] = numResults

        table.append(row)

def find_senator(term):
    str = re.sub('[(")]', '', term) # Removes backslashes
    str = re.sub(r'\s+$', '', str) # Removes trailing spaces
    return str

def find_party(senator_term):
    senator = find_senator(senator_term)
    for i in senators:
        if senator in i['name']:
            return i['party']

def find_source(term):
    return re.sub('[(")]', '', term)[3:]

def find_numResults(num):
    return re.sub('[^0-9]','', num)

# TODO: Don't call this in the script. Instead pass the individual filepaths in CONSOLE, while running the script.
with open('../output/nyt_2017.json') as new_york_times:
    nyt = json.load(new_york_times)
with open('../output/wsj_2017.json') as wall_street_journal:
    wsj = json.load(wall_street_journal)
with open('../output/usatoday_2017.json') as usa_today:
    usatoday = json.load(usa_today)
with open('../output/nypost_2017.json') as new_york_post:
    nypost = json.load(new_york_post)
with open('../output/huffpost_2017.json') as huffington_post:
    huffpost = json.load(huffington_post)
with open('../output/washingtonpost_2017.json') as washington_post:
    washingtonpost = json.load(washington_post)
with open('../output/latimes_2017.json') as los_angeles_times:
    latimes = json.load(los_angeles_times)
with open('../output/chicagotribune_2017.json') as chicago_tribune:
    chicagotribune = json.load(chicago_tribune)
with open('../output/dailybeast_2017.json') as the_daily_beast:
    dailybeast = json.load(the_daily_beast)

fill_table(nyt)
fill_table(wsj)
fill_table(usatoday)
fill_table(nypost)
fill_table(huffpost)
fill_table(washingtonpost)
fill_table(latimes)
fill_table(chicagotribune)
fill_table(dailybeast)

with open('../output/results_formatted.json', 'w') as outfile:
    json.dump(table, outfile)
