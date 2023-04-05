import string
import time

import pyrebase

from flask import Flask, render_template, request, jsonify, redirect, url_for,session
from flask_cors import CORS
from connectDB import workingWithBackend
from flask_session import Session

# Plotting using libraries
from bokeh.embed import components
from bokeh.resources import CDN

import requests
from zipfile import ZipFile

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
cors = CORS(app)

config = {
    "apiKey": "AIzaSyD7IYK6nNprDHxFEWWsGEfR_u13ECdlJ34",
    "authDomain": "tempbackend-7c9b3.firebaseapp.com",
    "databaseURL": "https://tempbackend-7c9b3-default-rtdb.firebaseio.com",
    "projectId": "tempbackend-7c9b3",
    "storageBucket": "tempbackend-7c9b3.appspot.com",
    "messagingSenderId": "17153523147",
    "appId": "1:17153523147:web:d597c786940c4392c08a4e",
    "measurementId": "G-W4KBLDEWDL"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

usersI = db.child("kidcommImages").get()
dictI = usersI.val()
img_data = list(dictI.values())

usersT = db.child("kicommText").get()
dictT = usersT.val()
story_data = list(dictT.values())

# drive_imgPaths = \
#     ["https://drive.google.com/file/d/1NAR015rAWp498T_bCEuSYBQb5FAIoWy8/view?usp=sharing",
#      "https://drive.google.com/file/d/1xgaOzROCiGf1qumDSwxkV24IOS7oa3jb/view?usp=sharing",
#      "https://drive.google.com/file/d/1zof_WoC6DPgp-MbvI_YWCDiUG2LB7DUH/view?usp=sharing",
#      "https://drive.google.com/file/d/1_mEoh9VYZQhTKvBja667aWKTD-rSZrYi/view?usp=sharing",
#      "https://drive.google.com/file/d/1FyhW-1pxMwoVzYRssvkzeTX_yV0PHyF7/view?usp=sharing",
#      "https://drive.google.com/file/d/1wmyYT3kHqr3cj-z-SKZQIVdXeadIgEs_/view?usp=sharing",
#      "https://drive.google.com/file/d/1BQ69tSDN3s7EAH18iu2UBSsJCJjDmdUU/view?usp=sharing",
#      "https://drive.google.com/file/d/1asm_CZOftj96ZHiuRBrb_LTPuTTWIxc7/view?usp=sharing",
#      "https://drive.google.com/file/d/1wHpaZ90ZBGMWgBrzBg1CH2Yn--c_T3Xm/view?usp=sharing",
#      "https://drive.google.com/file/d/15sG2ngJES6qK0eS6i3Kd-OiABscKxAzQ/view?usp=sharing",
#      "https://drive.google.com/file/d/1cNonl2PDqJN0G2XXig2g1-DdkSvfnqRV/view?usp=sharing",
#      "https://drive.google.com/file/d/1ssMcNds6VMq9UqGKuug-VOYgxpcKD4zv/view?usp=sharing",
#      "https://drive.google.com/file/d/1nnO2M1Hf5qnwlSXrM4JyhEFAwMoMbVMP/view?usp=sharing",
#      "https://drive.google.com/file/d/1PdXB4-40azir82o2WsyHcCzvzD_nzmAJ/view?usp=sharing",
#      "https://drive.google.com/file/d/160rk1PwOhWaULUKAyvUbjyLAaDUs6VKL/view?usp=sharing",
#      "https://drive.google.com/file/d/1dw_bpEvmUPOBNQv3L5aHK2ktuCJtRdPv/view?usp=sharing",
#      "https://drive.google.com/file/d/1hueRpPSpphfdenzyKjxdx9Jar5i4uDBG/view?usp=sharing",
#      "https://drive.google.com/file/d/1ZAWZZowOVWDP4wfO91VQbXgjeH234LSS/view?usp=sharing",
#      "https://drive.google.com/file/d/1G_AvQyDZi0bAJRw2IDQ8tQV4EMm5BVJi/view?usp=sharing",
#      "https://drive.google.com/file/d/1Yg38M0gHqpTKJDgC_fyB5-huChwZtAvf/view?usp=sharing"]


# line = 1
# start = 0
# end = 0
# time_taken = 0

# performance_dict = {}

# Keeps track whether the story is currently paused or in play
# story_play = 1

# Values tracker block-----------------------------------------
user_data = {'Accuracy': 0, 'Time': 0, 'Speed': 0,
            'Score': 0, 'Difficulty': [0, 0, 0], 'WrongWords': []}
            
# accuracy = 0
# total_accuracy = 0
# total_time_taken = 0
# total_speed = 0
# # Difficulty levels
# easy = 0
# medium = 0
# difficult = 0
# # Wrong words
# wrong_words_list = []
# # Score
# max_line_score = 0
# user_line_score= 0
# score = 0
# total_user_score = 0
# total_max_score = 0

# User name is "guest" by default
# user_name = "Kalam"


@app.route('/', methods = ['POST', 'GET'])
def login():
    session["Username"]='Kalam'

    session["line"]=1
    session["start"]=0
    session["end"]=0
    session["time_taken"]=0
    session["performance_dict"]={}
    session["story_play"]=1
    # session["user_data"] = {'Accuracy': 0, 'Time': 0, 'Speed': 0,
    #                         'Score': 0, 'Difficulty': [0, 0, 0], 'WrongWords': []}
    session["accuracy"] = 0
    session["speed"]=0
    session["total_accuracy"] = 0
    session["total_time_taken"] = 0
    session["total_speed"] = 0
    # Difficulty levels
    session["easy"] = 0
    session["medium"] = 0
    session["difficult"] = 0
    # Wrong words
    session["wrong_words_list"] = []
    # Score
    session["max_line_score"] = 0
    session["user_line_score"]= 0
    session["score"] = 0
    session["total_user_score"] = 0
    session["total_max_score"] = 0

    # Other
    session["avg_accuracy"]=0
    session["avg_time_per_line"]=0
    session["avg_words_per_sec"]=0


    if request.method == 'POST':
        session["Username"] = request.form.get('Username')
        return redirect(url_for('story'))  
    print(session["Username"])
    return render_template('home.html')


@app.route("/")
def home_page():
    if not session.get("Username"):
        return redirect("/")
    return redirect(url_for('story'))



def createWordlist(s):
    new_s = s.translate(str.maketrans('', '', string.punctuation))
    word_list = []
    upper_s = new_s.upper()
    for word in upper_s.split(" "):
        if word is '':
            continue
        else :
            word_list.append(word)
    return word_list


# def createTranscript(s, common_words):
#     new_s = s.translate(str.maketrans('', '', string.punctuation))
#     new_s = new_s.lower()
#     word_list = []
#     for word in new_s.split(" "):
#         if word in common_words:
#             word_list.append(word.upper())
#         else:
#             word_list.append(word)
#     sentence = ' '.join(word_list)
#     return sentence


# def speechMatch(speechLine, storyLine):
#     # Remove all punctuations, convert everything to lowercase
#     # Create a dictionary of words (hashmap)
#     # If more than half words are matched, then goto next page
#     speechList = createWordlist(speechLine)
#     storyList = createWordlist(storyLine)
#     common_words = set(speechList) & set(storyList)
#     wrong_words = set(storyList).difference((set(speechList) & set(storyList)))
#     common_words_len = len(set(speechList) & set(storyList))
#     total_words = len(set(storyList))
#     percent_overlap = common_words_len / float(total_words)
#     return percent_overlap, common_words, wrong_words


def extract_zipFile():
    print('Downloading started')
    url = "https://drive.google.com/uc?export=view&id=1xtKA-otCL1WGM9yfxkaRqy8j561Q6FK8"

    # Downloading the file by sending the request to the URL
    req = requests.get(url)

    # Writing the file to the local file system
    with open("Woodcutter.zip", 'wb') as output_file:
        output_file.write(req.content)
    print('Downloading Completed')

    # Extracting images from zip file
    with ZipFile("Woodcutter.zip", 'r') as zObject:
        zObject.extractall(path="static/images")


# def retrieveFirebaseData():
#     user_dict = (db.child("Data").child("Kalam").get()).val()

#     date_keys = list(user_dict.keys())

#     user_data = []
#     # for time stamps in a date
#     for date in date_keys:
#         time_keys = list(user_dict[date].keys())
#         for time in time_keys:
#             acc = user_dict[date][time]["Accuracy"]
#             speed = user_dict[date][time]["Speed"]
#             time_taken = user_dict[date][time]["Time"]
#             user_data.append([date, time, acc, speed, time_taken])

#     with open('users.csv', 'w', newline='') as file:
#         fieldnames = ['Date', 'Time', 'Accuracy', 'Speed', 'Time taken']
#         writer = csv.DictWriter(file, fieldnames=fieldnames)

#         writer.writeheader()
#         for row in user_data:
#             writer.writerow({'Date': row[0], 'Time': row[1], 'Accuracy': row[2], 'Speed': row[3], 'Time taken': row[4]})


def speechMatch(speechLine, storyLine):
    print(speechLine,"165") # Break sentence into array of lowercase words
    speechList = createWordlist(speechLine)
    storyList = createWordlist(storyLine)

    print(speechList,"166")
    print(storyList,"167")

    common_words = set(speechList) & set(storyList)
    wrong_words = set(storyList).difference((set(speechList) & set(storyList)))
    common_words_len = len(set(speechList) & set(storyList))
    total_words = len(set(storyList))
    percent_overlap = common_words_len / float(total_words)

    transcript = ""

    # Define a set of noise words
    noise = {'um', 'ah','','007'}

    # if len(speechList) > len(storyList):
    #     speechList = speechList[:len(storyList)] # Trim off the extra words at end to make it equal to storyList

    print(speechList,"179")
    
    i = 0
    while i < len(speechList):
        if speechList[i] not in noise and speechList[i] in storyList:
            transcript += speechList[i] + "(2) "
        elif speechList[i] not in noise and speechList[i] not in storyList:
            transcript += speechList[i] + "(3) "
        i = i+1
    
    # while i < len(speechList):
    #     if speechList[i]==storyList[i]:
    #         transcript = transcript + storyList[i] + "(2) " # Right word spoken - Green(2)
    #     else:
    #         transcript = transcript + storyList[i] + "(3) " # Wrong word spoken - Red(3)
    #     i = i+1

    # Incorrect words to make as storylist's words
    words = transcript.split()
    transcript = ""
    if len(storyList)<len(words):
        words = words[:len(storyList)]
    for j in range(len(words)):
        if "(3)" in words[j]:
            transcript += storyList[j] + words[j][-3:] + " "
        elif "(2)" in words[j]:
            transcript += storyList[j] + words[j][-3:] + " "

    if i < len(storyList):
        transcript = transcript + storyList[i] + "(1) " # Next word to speak out - Blue(1)
        i = i+1

    while(i < len(storyList)):
        transcript = transcript + storyList[i] + "(0) "
        i = i+1

    print(transcript,"216")
    # print(new_transcript,"217")
    return transcript, percent_overlap, common_words, wrong_words


def endOfStory():
    # global total_accuracy, total_time_taken, total_speed, avg_accuracy, avg_time_per_line, avg_words_per_sec
    # global easy, medium, difficult
    # global wrong_words_list, score
    global user_data

    session["avg_accuracy"] = round((session["total_accuracy"]  / (session["line"] - 1)), 2)
    session["avg_time_per_line"] = round((session["total_time_taken"] / (session["line"] - 1)), 2)
    session["avg_words_per_sec"] = round((session["total_speed"] / (session["line"] - 1)), 2)

    wrong_words_set = set(session["wrong_words_list"])
    wrong_words_ten = list(sorted(wrong_words_set, reverse=True))[:10]
    wrong_words = ""
    for word in wrong_words_ten:
        wrong_words += word + ","

    session["score"] = session["total_user_score"] / session["total_max_score"] * 100

    user_data = {'Accuracy': int(session["avg_accuracy"] * 100), 'Time': round(session["avg_time_per_line"], 2),
                 'Speed': round(session["avg_words_per_sec"], 2),
                 'Score': int(session["score"]), 'Difficulty': [session["easy"], session["medium"], session["difficult"]], 'WrongWords': wrong_words}
    print(user_data)

    return user_data




@app.route('/story')
def story():
    session["line"]=1
    extract_zipFile()
    return render_template('speech_recog.html',user_name =session["Username"])


@app.route('/story/receiver', methods=['POST'])
def changeStory():
    # global total_accuracy, avg_accuracy, total_time_taken, avg_time_per_line, avg_words_per_sec, total_speed
    # global plot_flag, accuracy
    # global line, start, end, time_taken, story_play
    # global wrong_words_list, easy, medium, difficult
    # global max_line_score, user_line_score, total_user_score, total_max_score, score

    speech_data = request.get_json()

    new_transcript, session["accuracy"], common_words, wrong_words = speechMatch(speech_data, story_data[session["line"]])
    # session["accuracy"], common_words, wrong_words = speechMatch(speech_data, story_data[session["line"]])
    session["accuracy"] = round(session["accuracy"], 2)

    session["max_line_score"] = len(story_data[session["line"]].split(" "))
    session["user_line_score"] = session["accuracy"] * session["max_line_score"]
    session["total_user_score"] += session["user_line_score"]
    session["total_max_score"] += session["max_line_score"]

    session["wrong_words_list"] += wrong_words

    # new_transcript = createTranscript(speech_data, common_words)

    session["end"] = time.time()
    session["time_taken"] = round(session["end"] - session["start"], 2)
    session["start"] = session["end"]

    session["speed"] = round((session["time_taken"] / len(story_data[session["line"]].split())), 2)
    # if speech is greater than threshold
    if speech_data[-3:]=="007":
        print(speech_data,"365")
        if session["accuracy"] >= 0.4 and session["story_play"] == 1:
            # if session["line"] == 1:  # First line is getting wrong values for time, so omit it for time being by making them 0
            #     session["accuracy"] = 0
            #     session["speed"] = 0
            #     session["time_taken"] = 0

            if 0.4 <= session["accuracy"] < 0.7:
                session["medium"] += 1
            else:
                session["easy"] += 1

            session["total_accuracy"]  += session["accuracy"]
            session["total_speed"] += session["speed"]
            session["total_time_taken"] += session["time_taken"]

            session["performance_dict"][session["line"]] = [session["accuracy"], session["time_taken"], session["speed"]]
            print("line:"+str(session["line"])+" ,"+str(session["performance_dict"][session["line"]]))

            session["line"] += 1
    print(speech_data[-3:],session["line"],385)
    image = img_data[session["line"]]
    story_line = story_data[session["line"]]
    if speech_data[-3:]=="007" or session["accuracy"] >= 0.6:
        data = new_transcript + ";" + image + ";" + "1" + ";" + str(session["line"]) + ";" + story_line
    else:
        data = new_transcript + ";" + image + ";" + "0" + ";" + str(session["line"]) + ";" + story_line
    
    if speech_data[-3:]=="007":
        print(data,"393")
        if session["accuracy"] >= 0.4 and session["story_play"] == 1:
            print(data,"395")
            data = data + "1"
    else:
        data = data + "0"

    session["accuracy"] = 0

    print(data,"401")

    jsonified_data = jsonify(data)
    return jsonified_data


@app.route('/story/button', methods=['POST'])
def buttonDetector():
    button_data = request.get_json()
    print(button_data)
    # global story_play, line, difficult, max_line_score, total_max_score
    if button_data == "PREV":
        if session["line"] != 0: session["line"] -= 1
        image = img_data[session["line"]]
        story_line = story_data[session["line"]]
        data = "_ _ _ _ _" + ";" + image + ";" + "1" + ";" + str(session["line"]) + ";" + story_line + "1"
        print(session["story_play"])
    elif button_data == "NEXT":
        session["line"] += 1
        image = img_data[session["line"]]
        story_line = story_data[session["line"]]
        data = "_ _ _ _ _" + ";" + image + ";" + "1" + ";" + str(session["line"]) + ";" + story_line + "1"
        session["difficult"] += 1
        session["max_line_score"] = len(story_data[session["line"]].split(" "))
        session["total_max_score"] += session["max_line_score"]
        print(session["story_play"])
    # elif button_data == "PAUSE":
    #     image = img_data[session["line"]]
    #     data = "Story Paused" + ";" + image + ";" + "1" + ";" + str(session["line"])
    #     session["story_play"] = 0
    # elif button_data == "PLAY":
    #     image = img_data[session["line"]]
    #     data = "_ _ _ _ _" + ";" + image + ";" + "1" + ";" + str(session["line"])
    #     session["story_play"] = 1
    session["accuracy"] = 0
    return jsonify(data)

@app.route('/output')
def output_page():
    performance_data = endOfStory()
    return render_template('output1.html',user_name =session["Username"], data=performance_data)

@app.route('/plots')
def home_page2():
    print(user_data)
    g1 = workingWithBackend(user_data, [session["easy"], session["medium"], session["difficult"]], session["Username"])
    demo_script_code1 , chart_code1 = components(g1)
    cdn_js=CDN.js_files[0]
    return render_template('datetime_3.html',user_name =session["Username"], demo_script_code1=demo_script_code1,chart_code1=chart_code1,cdn_js=cdn_js)

@app.route("/logout")
def logout():
    session["Username"] = None
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
