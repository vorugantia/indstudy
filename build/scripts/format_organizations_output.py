import json
import re

with open('../input/organization_list.json') as organization_list:
    organizations = json.load(organization_list)

table = []
def fill_table(parsehub):
    for i in parsehub['results']:
        search_terms = i['searchTerm'].split(" AND ")

        row = {
            'organization': '',
            'score': '',
            'source': '',
            'numResults': ''
        }
