# Load senators_list.json and source_list.json.
# With a template, make search terms by iterating through these two lists.
# Write the array of search terms to output JSON file.
import json

with open('../input/senator_list_2017.json') as senator_list:
    senators = json.load(senator_list)

with open('../input/source_list.json') as source_list:
    sources = json.load(source_list)

# Note: I temporarily removed 'AND stype.exact("Newspapers")' from the search to accommodate for the National Review, Mother Jones, and other magazine sources
# Note: Changed year to 2017.
def get_template(source, senator):
    return 'pub(%s) AND ("%s")  AND pd(20170101-20171231)' % (source, senator)

def make_searches():
    searches = []
    for source in sources:
        for senator in senators:
            searches.append(get_template(source, senator["name"]))
    return {"searches": searches}

with open('../output/query.json', 'w') as outfile:
    json.dump(make_searches(), outfile)
