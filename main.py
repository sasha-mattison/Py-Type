import time
import random

word_array = [
    "the","be","to","of","and","a","in","that","have","i",
    "it","for","not","on","with","he","as","you","do","at",
    "this","but","his","by","from","they","we","say","her","she",
    "or","an","will","my","one","all","would","there","their",
    "is","are","was","were","been","being","has","had","did","done",
    "if","then","than","when","where","why","how","what","which",
    "who","whom","whose","because","while","before","after","so",
    "no","yes","can","could","should","would","may","might","must",
    "shall","very","just","more","most","some","any","many","much",
    "each","every","either","neither","such","only","own","same",
    "other","another","again","still","even","also","too","well",
    "back","here","there","up","down","out","over","under","now",
    "then","today","tomorrow","yesterday","time","year","day","week",
    "man","woman","child","people","thing","world","life","hand",
    "eye","head","face","place","work","case","point","government",
    "company","number","group","problem","fact","way","system",
    "program","question","work","play","run","move","live","believe",
    "bring","happen","write","provide","sit","stand","lose","pay",
    "meet","include","continue","set","learn","change","lead","understand",
    "watch","follow","stop","create","speak","read","allow","add",
    "spend","grow","open","walk","win","offer","remember","love",
    "consider","appear","buy","wait","serve","die","send","expect",
    "build","stay","fall","cut","reach","kill","remain","suggest",
    "raise","pass","sell","require","report","decide","pull","return",
    "explain","hope","develop","carry","break","receive","agree",
    "support","hit","produce","eat","cover","catch","draw","choose",
    "cause","point","listen","six","five","four","three","two","first",
    "second","new","old","long","great","little","own","right","big",
    "high","different","small","large","next","early","young","important",
    "few","public","bad","same","able","best","better","certain"
]

words = int(input("words: "))
test = ""
previous_word = ""
for i in range(words):
    next_word = random.choice(word_array)
    test = test + " " + next_word
    previous_word = next_word

print(test)
user_input = str(input)