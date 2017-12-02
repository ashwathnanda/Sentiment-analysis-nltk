import requests

api_version = 'v2.9'
access_token = 'EAACEdEose0cBABTYYi5XtNwy0CiKFkTtcdyGHMrkJH2Poxyy9Tyg8RE2ZAwdK1RZBxB5CXbL6FTl4YQZBUkgSc5U777BoNZAqZCScD6iqpP8wZAkTFWz5cClDDPiSrI6gr8Iln85LBG6XuSxwK1MqDtqnYCnlaQigqTcrZAvBZAqS2iSwrMSkdFrA9M1O3ZCDJrdlpfiIb9VmVQZDZD'

# Modi's Facebook user id
u_id = '177526890164'

# the id of Modi's response post at https://www.facebook.com/narendramodi/posts/10159368293025165
p_id = '10159633354695165'

# the graph API endpoint for comments on Modi's post
url = 'https://graph.facebook.com/{}/{}_{}/comments'.format(api_version, u_id, p_id)

comments = []

r = requests.get(url, params={'access_token': access_token})
while True:
    data = r.json()

    # catch errors returned by the Graph API
    if 'error' in data:
        raise Exception(data['error']['message'])

    # append the text of each comment into the comments list
    for comment in data['data']:
        # remove line breaks in each comment
        text = comment['message'].replace('\n', ' ')
        comments.append(text)

    print('got {} comments'.format(len(data['data'])))

    # check if there are more comments
    if 'paging' in data and 'next' in data['paging']:
        r = requests.get(data['paging']['next'])
    else:
        break

# save the comments to a file
with open('comments.txt', 'w', encoding='utf-8') as f:
    for comment in comments:
        f.write(comment + '\n')
