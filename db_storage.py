from codecs import open
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatterbot = ChatBot("Training Example")
chatterbot.set_trainer(ListTrainer)

f = open("C:/Python36/Lib/site-packages/chatterbot_corpus/data/korean/inputdata.txt", "rb", "utf-8")
lines = f.readlines()

tmp_question = ""
tmp_ansure = ""

for line in lines:
    if line[0] == "Q":
        tmp_question = line
        #print(tmp_question)
    elif line[0] == "A":
        tmp_ansure = line
        #print(tmp_ansure)
    elif line[0] == "\t":
        tmp_ansure = tmp_ansure + line
        #print(tmp_ansure)
    elif "set" in line:
        #print(tmp_question)
        #print(tmp_ansure)
        chatterbot.train([
            tmp_question,
            tmp_ansure
        ])

        tmp_question = ""
        tmp_ansure = ""