import mechanize
from bs4 import BeautifulSoup
import http.cookiejar
from json import loads
import requests
import re

class getIds :
    def __init__(self, id) :
        cj = http.cookiejar.CookieJar()
        br = mechanize.Browser()
        br.addheaders = [('User-agent', "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148")]
        br.set_handle_robots(False)
        br.set_cookiejar(cj)
        br.open(f"https://fr.buddysecret.com/s/sync-quiz/{id}")
        br.select_form(nr=0)
        br.form['userFullName'] = 'username'
        br.submit()
        res = str(br.response().read()).replace('\\', '')

        buddyJson = re.findall(r'var arrQuizDetail=.*?({.*}).*?(?=;)', res, flags=re.S)[0].partition(';')[0]
        buddyJson = loads(buddyJson)

        self.categoryId = re.search("(?<=var categoryId=')(\d+)';", res).group(1)
        self.quizId = buddyJson["id"]
        self.questionId1 = buddyJson["questions"][0]["questionId"]
        self.questionId2 = buddyJson["questions"][1]["questionId"]
        self.questionId3 = buddyJson["questions"][2]["questionId"]
        self.questionId4 = buddyJson["questions"][3]["questionId"]
        self.questionId5 = buddyJson["questions"][4]["questionId"]
        self.questionId6 = buddyJson["questions"][5]["questionId"]
        self.questionId7 = buddyJson["questions"][6]["questionId"]
        self.questionId8 = buddyJson["questions"][7]["questionId"]
        self.questionId9 = buddyJson["questions"][8]["questionId"]
        self.questionId10 = buddyJson["questions"][9]["questionId"]

if __name__ == '__main__' :

    id = 'E1md' #the random thing after "https://fr.buddysecret.com/s/sync-quiz/"
    n = 15

    username = 'username'
    
    question1 = 'answer'
    question2 = 'answer'
    question3 = 'answer'
    question4 = 'answer'
    question5 = 'answer'
    question6 = 'answer'
    question7 = 'answer'
    question8 = 'answer'
    question9 = 'answer'
    question10 = 'answer'

    ids = getIds(id)

    payload = {
        "userFullName" : username,
        "categoryId" : ids.categoryId,
        "quizId" : ids.quizId,
        "encUserQuizId" : id,
        "userQuestionId[0]" : ids.questionId1,
        "userQuestionOptionText[0]" : question1,
        "userQuestionId[1]" : ids.questionId2,
        "userQuestionOptionText[1]" : question2,
        "userQuestionId[2]" : ids.questionId3,
        "userQuestionOptionText[2]" : question3,
        "userQuestionId[3]" : ids.questionId4,
        "userQuestionOptionText[3]" : question4,
        "userQuestionId[4]" : ids.questionId5,
        "userQuestionOptionText[4]" : question5,
        "userQuestionId[5]" : ids.questionId6,
        "userQuestionOptionText[5]" : question6,
        "userQuestionId[6]" : ids.questionId7,
        "userQuestionOptionText[6]" : question7,
        "userQuestionId[7]" : ids.questionId8,
        "userQuestionOptionText[7]" : question8,
        "userQuestionId[8]" : ids.questionId9,
        "userQuestionOptionText[8]" : question9,
        "userQuestionId[9]" : ids.questionId10,
        "userQuestionOptionText[9]" : question10,
        "useMeta" : 1,
        "customQuestion" : 1,
        "oneSignalUserId" : "null"
    }

    r = requests.Session()
    headers = { "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148" }
    url = 'https://fr.buddysecret.com/save-user-quiz'
    
    for x in range(0, n) :
        r.post(url, headers=headers, data=payload)
        print('sent')
