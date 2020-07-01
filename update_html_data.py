from selenium import webdriver
import time

links_list = {"DevOpsFAQ": "https://wiki.wdf.sap.corp/wiki/display/DigitalMfg/DevOps+FAQ",
              "DeveloperFAQ": "https://wiki.wdf.sap.corp/wiki/display/DigitalMfg/Developer+FAQ",
              "DevOpsHowTos": "https://wiki.wdf.sap.corp/wiki/display/DigitalMfg/DevOps+HowTos",
              "DeveloperHowTos": "https://wiki.wdf.sap.corp/wiki/display/DigitalMfg/Developer+HowTos",
              "DevOpsLinks": "https://wiki.wdf.sap.corp/wiki/display/DigitalMfg/DevOps+Links",
              "KBASessions": "https://wiki.wdf.sap.corp/wiki/display/DigitalMfg/KBA+Sessions",
              "Learning": "https://wiki.wdf.sap.corp/wiki/display/DigitalMfg/Learning",
              "CheatSheet": "https://wiki.wdf.sap.corp/wiki/pages/viewpage.action?pageId=2257533992"}

file_name = ["devops_faq.html",
             "developer_faq.html",
             "devops_how_to.html",
             "deveoper_how_to.html",
             "devops_links.html",
             "kba_sessions.html",
             "learn.html",
             "cheat_sheet.hmtl"]

chrome_browser = webdriver.Chrome("./chromedriver")

i = 0
for page_name, page_url in links_list.items():
    chrome_browser.get(page_url)
    html_source = chrome_browser.page_source
    html_path = f"html_data\\{file_name[i]}"
    with open(html_path, 'w', encoding="utf-8") as file:
        file.write(html_source)
    time.sleep(2)
    i += 1

chrome_browser.quit()
