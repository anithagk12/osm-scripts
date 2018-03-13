from osmapi import OsmApi
import time


MyApi = OsmApi()

api = OsmApi(username="A******", password="a*******")



import csv
 
with open('temple2.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)
        #print ("anitha")
        api.ChangesetCreate({u"comment": u"Siva Temple "+row[1].title()})
        data = { u"lat": row[3], u"lon": row[4], u"tag": { u"amenity": u"temple", u"name": row[1].title(),  u"location": row[2].title(), u"religion":u"hindu" } }
        api.NodeCreate(data)
        api.ChangesetClose()

        print (data)
        time.sleep(1)
