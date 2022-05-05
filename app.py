from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)
logo_url = 'https://media.contentapi.ea.com/content/dam/ea/fifa/fifa-21/pro-clubs/common/pro-clubs/crest-default.png'

def getMemberInfo():
    headers_dict = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
        "Host": "proclubs.ea.com"}

    response = requests.get(
        "https://proclubs.ea.com/api/fifa/members/stats?platform=ps4&clubId=552898", headers=headers_dict).json()
    return response

def getSeasonalInfo():
    headers_dict = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
        "Host": "proclubs.ea.com"}

    response = requests.get(
        "https://proclubs.ea.com/api/fifa/clubs/seasonalStats?platform=ps4&clubIds=552898", headers=headers_dict).json()
    return response

def getClubInfo():
    headers_dict = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
        "Host": "proclubs.ea.com"}

    response = requests.get(
        "https://proclubs.ea.com/api/fifa/clubs/info?matchType=gameType13&platform=ps4&clubIds=552898",
        headers=headers_dict).json()
    return response

@app.route('/')
def hello_world():  # put application's code here
    return render_template('base.html')

@app.route("/members")
def members():
    response = getMemberInfo()['members']
    return render_template('members.html', data=response)






@app.route("/getMembers")
def getMembers():
    return getMemberInfo()


if __name__ == '__main__':
    app.run()
