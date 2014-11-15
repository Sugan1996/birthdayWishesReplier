import requests
import json
from random import randint

#http://www.timestampgenerator.com/
#Use this link to generate the timeStamp.
timeStamp =  InsertUTCTimeStampHere(eg.1415994915)


# Initialize the Graph API with a valid access token  
#Generate access token here: https://developers.facebook.com/tools/explorer/
accessToken = 'Access token here. Do not delete the quotes.'


query = " SELECT post_id, actor_id, created_time, message FROM stream WHERE \
                filter_key = 'others' AND source_id = me() AND \
                created_time > " + str(timeStamp) + " LIMIT 200 "


comment = {'access_token': accessToken, 'q': query}
r = requests.get('https://graph.facebook.com/fql', params = comment)
result = json.loads(r.text)
wallposts = result['data']

print str(len(wallposts)) + " to handle"
baseUrl = "https://graph.facebook.com/"
count = 1
for wallpost in wallposts:
    url = baseUrl + '%s/comments' % wallpost['post_id']
    likesUrl = baseUrl + str(wallpost['post_id']) + "/likes/?access_token=" + accessToken + "&method=POST"
    requests.post(likesUrl)
    #Add as many replies you want inside this list.
    #Make sure to change the randint() method's second parameter
    #with the number of replies - 1.
    messages = [ 'Thank you :)', 'Thanks :)'] 
    comment = {'access_token': accessToken, 'message': messages[randint(0,1)]}
    s = requests.post(url, data = comment)
    print "Wall post %d done" % count
    count += 1


