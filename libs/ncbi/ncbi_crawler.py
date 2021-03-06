import requests
from bs4 import BeautifulSoup

def getSubPageContent(pageString):
    bs_obj = BeautifulSoup(pageString, "html.parser")
    journal = ""
    cit = bs_obj.find("div", {"class":"cit"})
    try:
        journal = cit.text.split(" doi")[0]
    except Exception:
        journal = cit.text
        # print("error")
    rprt_all = bs_obj.find("div", {"class":"rprt_all"})
    title = rprt_all.find("h1").text

    authors = []
    try:
        rprt_all = bs_obj.find("div", {"class":"rprt_all"})

        auths = rprt_all.find("div", {"class":"auths"})
        atags = auths.findAll("a")
        authors = [atag.text for atag in atags]
    except Exception:
        print("error auths")

    institutions = []
    try:
        afflist = bs_obj.find("div", {"class":"afflist"})
        dds = afflist.findAll("dd")
        institutions = [dd.text for dd in dds]
    except Exception:
        institutions = []
        # print("error authors")

    abstract = ""
    try:
        abstr = bs_obj.find("div", {"class":"abstr"})
        abstract = abstr.find("div").text
    except Exception:
        abstract = ""
        # print("error abstract")

    keywords = ""
    try:
        keywords = bs_obj.find("div", {"class":"keywords"}).text
        keywords = keywords.split("; ")
    except Exception:
        keywords = []
        # print("keywords error")

    return {"journal": journal, "title":title, "institutions":institutions, "abstract":abstract, "keywords":keywords,
            "authors":authors}