# Load the JSON output files that came directly from ParseHub
# Output JSON file is a of objects, with each object containing the keys: senator, party, source, numResults
import json
import re

with open('../output/parsehub-nyt-senators.json') as nyt:
    parsehub_nyt = json.load(nyt)

with open('../output/parsehub-wsj-senators.json') as wsj:
    parsehub_wsj = json.load(wsj)

with open('../input/senator_list.json') as senator_list:
    senators = json.load(senator_list)

table = []
def fill_table(parsehub):
    for i in parsehub['results']:
        search_terms = i['searchTerm'].split(" AND ")

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
    return re.sub('[(")]', '', term)

def find_party(senator_term):
    senator = find_senator(senator_term)
    for i in senators:
        if senator in i['name']:
            return i['party']

def find_source(term):
    return re.sub('[(")]', '', term)[3:]

def find_numResults(num):
    return re.sub('[^0-9]','', num)

fill_table(parsehub_nyt)
fill_table(parsehub_wsj)

with open('../output/results_formatted.json', 'w') as outfile:
    json.dump(table, outfile)
