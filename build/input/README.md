# Input data

## 1. Senators

I've compiled a list of senators from the 115th Congress (2017-2019) which will us used in the analysis of newspapers from the year 2017. This can be extended to the 114th Congress (2015-2017) later if needed.

[List of senators in the 115th Congress](https://en.wikipedia.org/wiki/List_of_United_States_Senators_in_the_115th_Congress_by_seniority) ([Alternate reference](https://www.senate.gov/artandhistory/history/common/briefing/senators_chronological.htm))

Data is listed in `senator_list.json` as an array of objects (with keys `name` and `party`).

### Notes:

1. Should I investigate Independent senators Bernie Sanders and Angus King to determine whether they belong more in the Democratic or Republican parties?


## Sources

For now I'm selecting the New York Times and the Wall Street Journal as my two news sources, as they're both NYC-based and are supposed to have opposite political leanings.

Data is listed in `source_list.json` as a simple array of source names.

## ParseHub results

The JSON files beginning with `parsehub` are the raw file outputs after running a web scrape on ProQuest.
