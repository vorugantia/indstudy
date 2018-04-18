import json

with open('../input/organization_list.json') as organization_list:
    organizations = json.load(organization_list)


def get_template(organization):
    keyword = organization.replace(' ', '+')
    return 'http://www.foxnews.com/search-results/search?q=' + keyword + '&ss=fn&sort=latest&section.path=fnc/politics&type=story&min_date=2017-01-01&max_date=2017-12-31&start=0'

def get_alt_template(organization, altname):
    keyword = organization.replace(' ', '+')
    altname = '+"' + altname + '"'
    return 'http://www.foxnews.com/search-results/search?q=' + keyword + altname + '&ss=fn&sort=latest&section.path=fnc/politics&type=story&min_date=2017-01-01&max_date=2017-12-31&start=0'


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

write('../output/organizations_2017/queries/foxnews.json')
