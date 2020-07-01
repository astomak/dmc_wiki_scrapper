from bs4 import BeautifulSoup
import csv
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def scrapy_fn(page_name, page_url, html_file):
    html_path = os.path.join(BASE_DIR, html_file)
    soup = BeautifulSoup(
        open(html_path), "html.parser")

    all_links = soup.select(f'a[href^="#{page_name}"]')
    base_ans = f"Hellooo There! I have found something for you in {page_name} page. Go to the link below and see if its helpful :)."

    csv_file = page_name.lower() + ".csv"
    csv_path = os.path.join(BASE_DIR, csv_file)

    with open(csv_path, 'w', encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Questions", "Answer"])
        for link in all_links:
            question = link.getText()
            href = link.get("href")
            answer = base_ans + page_url + href
            writer.writerow([question, answer])

    return "CSV file created(updated) successfully!"


links_list = {"DevOpsFAQ": "https://wiki.wdf.sap.corp/wiki/display/DigitalMfg/DevOps+FAQ",
              #   "DeveloperFAQ": "https://wiki.wdf.sap.corp/wiki/display/DigitalMfg/Developer+FAQ",
              "DevOpsHowTos": "https://wiki.wdf.sap.corp/wiki/display/DigitalMfg/DevOps+HowTos",
              "DeveloperHowTos": "https://wiki.wdf.sap.corp/wiki/display/DigitalMfg/Developer+HowTos",
              "DevOpsLinks": "https://wiki.wdf.sap.corp/wiki/display/DigitalMfg/DevOps+Links",
              "KBASessions": "https://wiki.wdf.sap.corp/wiki/display/DigitalMfg/KBA+Sessions", }
#   "Learning": "https://wiki.wdf.sap.corp/wiki/display/DigitalMfg/Learning", }
#   "CheatSheet": "https://wiki.wdf.sap.corp/wiki/pages/viewpage.action?pageId=2257533992"}

file_name = ["devops_faq.html",
             #  "developer_faq.html",
             "devops_how_to.html",
             "deveoper_how_to.html",
             "devops_links.html",
             "kba_sessions.html", ]
#  "learn.html", ]
#  "cheat_sheet.hmtl"

if __name__ == '__main__':
    key = "DevOpsFAQ"
    scrapy_fn(key, links_list[key], file_name[0])
    # i = 0
    # for key, value in links_list.items():
    #     scrapy_fn(key, value, file_name[i])
    #     i += 1
