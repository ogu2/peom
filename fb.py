import simplejson, urllib
res=simplejson.load(urllib.urlopen("https://graph.facebook.com/search?q=sandy&type=post&limit=100"))
for x in res['data']:
    if 'message' in x:
        print x['message']
        print '*'*40
