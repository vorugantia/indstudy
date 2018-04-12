import json


with open('../input/source_list.json') as source_list:
    sources = json.load(source_list)

with open('../input/organization_list.json') as organization_list:
    organizations = json.load(organization_list)


def get_template(source, organization):
    return 'pub(%s) AND ("%s") AND pd(20170101-20171231)' % (source, organization)

def get_alt_template(source, organization, altname):
    return 'pub(%s) AND ("%s" OR "%s") AND pd(20170101-20171231)' % (source, organization, altname)

def make_searches(source):
    searches = []
    for organization in organizations:
        if 'altname' not in organization:
            searches.append(get_template(source, organization["name"]))
        else:
            searches.append(get_alt_template(source, organization['name'],
            organization['altname']))
    return {"searches": searches}

def write(path):
    with open(path, 'w') as outfile:
        json.dump(make_searches(source), outfile)

for source in sources:
    write('../output/organizations_2017/queries/%s.json' % source)
