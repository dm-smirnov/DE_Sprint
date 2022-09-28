#import requests as req
from bs4 import BeautifulSoup
from requests_tor import RequestsTor
import json, tqdm, time

MAX_PAGES_PARSE = 3

req = RequestsTor()
data = { 'data': [] }
baseUrl = "https://spb.hh.ru/search/vacancy?text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA";
resp = req.get(baseUrl)
soup = BeautifulSoup(resp.text, 'lxml')
# if banned from hh
if len(resp.text) < 150:
    print(soup.find("title").text)
else:
    resultData = { 'data': [] }

    # get pages count
    pages = 1
    tag = soup.find(class_="pager").find_all(class_="pager-item-not-in-short-range")
    for item in tag:
        tag2 = item.find(class_="bloko-button")
        pageNumber = int(tag2.text)
        if pageNumber > pages: pages = pageNumber
    print("Total pages: %d, analyze first %d pages\n" % (pages, MAX_PAGES_PARSE))
    pages = MAX_PAGES_PARSE if pages > MAX_PAGES_PARSE else pages

    # scan pages
    itemNo = 0
    for page in range(1, pages+1):
        if page > 1:
            resp = req.get(baseUrl + f"&page={page}&hhtmFrom=vacancy_search_list")
            soup = BeautifulSoup(resp.text, 'lxml')
        pageVacs = soup.find_all(class_="serp-item")
        # parse vacs
        for vac in pageVacs:
            itemNo = itemNo + 1
            vacTitleTag = vac.find(class_="serp-item__title")
            vacTitle = vacTitleTag.text
            vacSalaryTag = vac.find(attrs={'data-qa': "vacancy-serp__vacancy-compensation"})
            vacSalary = "[ salary not published ]" if vacSalaryTag == None else vacSalaryTag.text
            vacAddress = vac.find(attrs={'data-qa': "vacancy-serp__vacancy-address"}).text
            vacDetailResp = req.get(vacTitleTag.attrs['href'])
            vacDetail = BeautifulSoup(vacDetailResp.text, 'lxml')
            vacExpTag = vacDetail.find(attrs={'data-qa': 'vacancy-experience'})
            vacExp = "[ exp not published ]" if vacExpTag == None else vacExpTag.text

            print("[%2d] '%s', %s, %s, %s" % (itemNo, vacTitle, vacSalary, vacAddress, vacExp))
            resultData['data'].append({
                'title': vacTitle,
                'salary': vacSalary,
                'region': vacAddress,
                'work experience': vacExp
            })
        time.sleep(2)

    #print(resultData)
    with open('hh-vac-parser.json', 'w') as fl:
        json.dump(resultData, fl, ensure_ascii=False)
