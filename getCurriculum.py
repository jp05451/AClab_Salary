from ast import If
from cmath import nan
import time
import pandas as pd
from playwright.sync_api import sync_playwright


#    browser.close()

def readCurriculumTable(table):
    df = pd.read_html(table)
    dict = df[0].to_dict()

    classList = []
    for i in range(1, len(dict[0])):
        temp = []
        for j in range(2, len(dict)):
            if(i >= 1 and j >= 2):
                if(str(dict[j][i]) != "nan"):
                    temp.append(1)
                else:
                    temp.append(0)
            if(j == 1):
                continue
            #print(dict[j][i], end="\t")
        #print()
        classList.append(temp)
    return classList

def curriculum(id: str, passwd: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(
            "https://stuinfosys.ntust.edu.tw/NTUSTSSOServ/SSO/Login/CourseSelection")
        print(page.title())
        page.fill(
            "#login-input-container > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)", id)
        page.fill(
            "#login-input-container > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > input:nth-child(1)", passwd)
        page.click(
            "#btnLogIn")
        page.click(
            "li.dropdown:nth-child(4) > a:nth-child(1) > span:nth-child(1)")
        page.click(
            "li.dropdown:nth-child(4) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)")

        locator = page.locator(
            '#PrintArea > table:nth-child(5)')
        table = "<table>"+locator.inner_html()+"</table>"
        
        classList=readCurriculumTable(table)

        output=open("curriculum.txt",mode="w")
        
        for row in classList:      
            print(row)
        browser.close()


if __name__ == "__main__":
    studentID = "B10915045"
    identity = "4672"
    birthday = "0116"
    passwd = "Yyh910116@"
    curriculum(studentID, passwd)
