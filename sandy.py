from twython import Twython
t=Twython()
def print_phrases(keyword):
    res=t.search(q=keyword,rpp='1000')
    a=res['results']
    for x in a:
        try:
            print "%s \t--@%s  " % (x['text'],x['from_user'])
            print '-'*30
        except:
            #this is just for unicode chars
            pass

    print " %s results in %ss" % (len(a), res['completed_in'])

print_phrases('hurricane sandy')
print_phrases('massachusetts sandy')
print_phrases('boston hurricane sandy')
print_phrases('dear sandy')
#print_phrases('MIT hurricane sandy')
#print_phrases('Massachusetts Institute of Tech')
