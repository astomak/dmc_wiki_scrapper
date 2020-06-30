# dmc_wiki_scrapper
This is web_scrapper built specifically for SAP_DMC wiki.
What the scrapper is doing? ==>
Get all the relevant a tags from the page.
Extracting href attribute from the a tags.
Then making question-answer pair through the extracted data.
Saving that question-answer pair in csv format.


To Run ==>
<!-- Replace or Update chromedriver.exe according to your versions of Google Chrome-->
1. First run update_html_data.py(Uses Selenium) which we will download the page sources from all the dmc wiki links.
(not able to use requests.get() due to page being built on SAML)

2. Then run scrapper.py to scrap all the html page source to get relevant data and buld csv from it.

