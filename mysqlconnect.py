import mysql.connector
from difflib import get_close_matches


conn = mysql.connector.connect(
user = 'ardit700_student',
password = 'ardit700_student',
host = '108.167.140.122',
database = 'ardit700_pm1database'
)

cursor = conn.cursor()

word = input('Enter a word: ')
query = cursor.execute("select Expression from Dictionary")
keyslist = cursor.fetchall()
finallist = []
for i in keyslist:
    finallist.append(i[0])

exists = False
if word in finallist:
    exists = True
elif len(get_close_matches(word,finallist)) > 0:
    yn = input("Did you mean %s instead. press Y for yes or N for no: " %get_close_matches(word,finallist)[0])
    if yn == 'Y':
        word = get_close_matches(word,finallist)[0]
        exists = True
    elif yn == 'N':
        exists = False
else:
    exists = False
    
if exists == True:
    query = cursor.execute("select * from Dictionary where Expression = '%s'" % word)
    results = cursor.fetchall()
    for result in results:
        print(result[1])
else:
    print('no word found')
