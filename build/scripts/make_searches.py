# Load senators_list.json and source_list.json.
# With a template, make search terms by iterating through these two lists.
# Write the array of search terms to output JSON file.
import json

with open('../input/senator_list.json') as senator_list:
    senators = json.load(senator_list)

with open('../input/source_list.json') as source_list:
    sources = json.load(source_list)

# TODO: Add an "altname" option in this template, for senators who are commonly referred to with two different names.
def get_template(source, senator):
    return 'pub(%s) AND ("%s") AND stype.exact("Newspapers") AND pd(20170101-20171231)' % (source, senator)

def make_searches():
    searches = []
    for source in sources:
        for senator in senators:
            searches.append(get_template(source, senator["name"]))
    return {"searches": searches}

with open('../output/query.json', 'w') as outfile:
    json.dump(make_searches(), outfile)
