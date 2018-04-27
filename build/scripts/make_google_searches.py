# Currently set to search National Review's website for SENATORS
import json

# with open('../input/organization_list.json') as organization_list:
#     organizations = json.load(organization_list)
with open('../input/senator_list.json') as organization_list:
    organizations = json.load(organization_list)


def get_template(organization):
    return 'allintext: "%s" site:www.nationalreview.com' % (organization)

def get_alt_template(organization, altname):
    return 'allintext: "%s" OR "%s" site:www.nationalreview.com' % (organization, altname)


def make_searches():
    searches = []
    for organization in organizations:
        if 'altname' not in organization:
            searches.append(get_template(organization["name"]))
        else:
            searches.append(get_alt_template(organization["name"], organization["altname"]))
    return searches

def write(path):
    with open(path, 'w') as outfile:
        json.dump(make_searches(), outfile)

# write('../output/organizations_2017/queries/nationalreview.json')
write('../output/senators/nationalreview_senators.json')
