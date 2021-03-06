# Input data

## 1. Senators

I've compiled a list of senators from the ~~115th Congress (2017-2019) which will us used in the analysis of newspapers from the year 2017.~~

[List of senators in the 115th Congress](https://en.wikipedia.org/wiki/List_of_United_States_Senators_in_the_115th_Congress_by_seniority) ([Alternate reference](https://www.senate.gov/artandhistory/history/common/briefing/senators_chronological.htm))

Data is listed in `senator_list.json` as an array of objects (with keys `name` and `party`, and `altname` if any senator has a common alternative name/nickname).

**First, I'm compiling a list of senators for 2016 (saved as `senator_list.json`). Once the year 2017 is completed, I will switch the senator list to the 2017 version.**

## 2. Think tanks/policy groups

I've compiled a list of the 50 most prominent think tanks and policy groups according to Tim Groseclose's 2005 paper, "A measure of media bias." Each organization is given a score either derived from Groseclose's paper or from the [Media Bias/Fact Check](https://mediabiasfactcheck.com/) website.

Data is listed in `organization_list.json` in a similar format to `senator_list.json`.

## Sources

For now I'm selecting the New York Times and the Wall Street Journal as my two news sources, as they're both NYC-based and are supposed to have opposite political leanings.

Data is listed in `source_list.json` as a simple array of source names.

## ParseHub results

The JSON files beginning with `parsehub` are the raw file outputs after running a web scrape on ProQuest.
