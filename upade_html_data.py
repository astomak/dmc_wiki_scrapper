from selenium import webdriver
import time

links_list = ["https://wiki.wdf.sap.corp/wiki/display/DigitalMfg/DevOps+Knowledge+Sharing",
              "https://wiki.wdf.sap.corp/wiki/display/DigitalMfg/DevOps+FAQ",
              "https://wiki.wdf.sap.corp/wiki/display/DigitalMfg/DevOps+HowTos",
              "https://wiki.wdf.sap.corp/wiki/display/DigitalMfg/Developer+HowTos",
              "https://wiki.wdf.sap.corp/wiki/display/DigitalMfg/DevOps+Links",
              "https://wiki.wdf.sap.corp/wiki/display/DigitalMfg/KBA+Sessions",
              "https://wiki.wdf.sap.corp/wiki/display/DigitalMfg/Learning",
              "https://wiki.wdf.sap.corp/wiki/pages/viewpage.action?pageId=2257533992"]

file_name = ["devops_knowledge.html",
             "devops_faq.html",
             "devops_how_to.html",
             "devops_links.html",
             "kba_sessions.html",
             "learn.html",
             "cheat_sheet.hmtl"]

chrome_browser = webdriver.Chrome("./chromedriver")

for i in range(len(links_list)):
    chrome_browser.get(links_list[i])
    html_source = chrome_browser.page_source
    with open("html_data\\" + file_name[i], 'w', encoding="utf-8") as file:
        file.write(html_source)
    time.sleep(2)

chrome_browser.close()
