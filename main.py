from flask import Flask
from flask import render_template, request
import requests
import os

STATIC_DIR = os.path.abspath('./static')
app = Flask(__name__, static_folder=STATIC_DIR)
logo_url = 'https://media.contentapi.ea.com/content/dam/ea/fifa/fifa-21/pro-clubs/common/pro-clubs/crest-default.png'

def getMemberInfo():
    headers_dict = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
        "Host": "proclubs.ea.com"}

    response = requests.get(
        "https://proclubs.ea.com/api/fifa/members/stats?platform=ps5&clubId=6462498", headers=headers_dict).json()
    return response

def getSeasonalInfo():
    headers_dict = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
        "Host": "proclubs.ea.com"}

    response = requests.get(
        "https://proclubs.ea.com/api/fifa/clubs/seasonalStats?platform=ps5&clubIds=6462498", headers=headers_dict).json()
    return response

def getClubInfo(clubId='6462498'):
    headers_dict = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
        "Host": "proclubs.ea.com"}

    response = requests.get(
        f"https://proclubs.ea.com/api/fifa/clubs/info?matchType=gameType13&platform=ps5&clubIds={clubId}",
        headers=headers_dict).json()
    return response

def getMatchHistory():
    headers_dict = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
        "Host": "proclubs.ea.com"}

    response = requests.get(
        "https://proclubs.ea.com/api/fifa/clubs/matches?platform=ps5&matchType=gameType9&clubIds=6462498",
        headers=headers_dict).json()
    return response

@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route("/members")
def members():
    response = getMemberInfo()['members']
    return render_template('members.html', data=response)

@app.route("/club")
def club():
    clubInfo = getClubInfo()['6462498']
    seasonalInfo = getSeasonalInfo()[0]
    return render_template('club.html',     club=clubInfo, seasonal=seasonalInfo)

@app.route("/games")
def matchHistory():
    response = getMatchHistory()

    return render_template('match-history.html', matches=response)


@app.route("/getClubInfo")
def getClubInfoById():

    clubId = request.args.get("clubId")
    clubInfo = getClubInfo(clubId)

    return clubInfo


if __name__ == '__main__':
    print(getMatchHistory())
    app.run(host='127.0.0.1', port=8080, debug=True)

