# SEC Parsers
Parses non-standardized SEC 10-K filings into well structured xml. Currently can parse about 75% of SEC 10 K filings. XML includes parts, items (such as item1a risk factors), as well as subheadings (e.g. seasonality).

A sample of parsed 10k xmls are available [here](https://www.dropbox.com/scl/fo/np1lpow7r3bissz80ze3o/AKGM8skBrUfEGlSweofAUDU?rlkey=cz1r78jofntjeq4ax2vb2yd0u&e=1&st=mdcwgfcm&dl=0). I would like to upload every parsed 10k xml, but I lack the storage (I need ~50gb, and I have 2gb.) If you can help me with this problem please let me know!

## Functions
* ```parse_10k(html)``` converts a sec filing from non-standardized html into well structured xml
* ```get_table_of_contents(html)``` reads the table of contents from a sec filing html
* ```download_sec_filing(url)``` downloads a sec filing from url using headers
* ```print_xml_structure(tree)``` prints tree structure of parsed html file
* ```get_text_from_node(node)``` gets the text from an xml node

## Quickstart
### Download
```pip install sec-parsers```
### Sample Code
```
from sec_parsers import parse_10k, download_sec_filing, print_xml_structure, get_text_from_node

# downloads 10k
html = download_sec_filing('https://www.sec.gov/Archives/edgar/data/1018724/000101872423000004/amzn-20221231.htm')

tree = parse_10k(html)
root = tree.getroot()

# print xml structure
print_xml_structure(root)

# get text for risk factors
get_text_from_node(root.find(".//item1a"))
```

## Important Notes:
* Import issues. from sec_parsers.sec_parsers import parser_10k is now from sec_parsers import parse_10k
* Some jupyter / answers notebooks use old notation. I'm not going to update them right now, because there will soon be a parse 10k update that includes detailed subsections, and I'm waiting for that update to fix/make docs.

## Next release:
* conversion to xml with detailed subsections
* metadata

## Notes:
* Last update to main branch was very WIP with beginner mistakes (never wrote a python package before). I've now settled on a more concrete structure.

## Statistics
Statistics are likely better than they look. Small / weird companies are less likely to parse - make this section generate automatically from tests

Table of Contents Parsing:
* 79.7% parsed
* 14.4% had an issue that can be resolved
* 3% were not parsed has table without links is not supported yet
* remainder unclear

Conversion to xml:
* 93.1% parsed succesfully
* 6.9% had an issue

Total parse rate is 74%.

Last test run on 1039 10-Ks on June 27 2024.