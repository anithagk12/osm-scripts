from geopy.distance import great_circle
import geocoder
p1=geocoder.osm("trichy")
p1.latlng
p2=geocoder.osm("chennai")
p2.latlng
p3=geocoder.osm("thanjavur, tamilnadu")
p3.latlng
p4=geocoder.osm("coimbatore")
p4.latlng
tr=p1.latlng
ch=p2.latlng
sa=p3.latlng
co=p4.latlng
dis1=great_circle(tr,sa).miles
dis2=great_circle(tr,ch).miles
dis3=great_circle(tr,co).miles
dis4=great_circle(sa,ch).miles
dis5=great_circle(co,sa).miles
dis6=great_circle(co,ch).miles

if ((dis1<dis2)and(dis1<dis3)):
	print ("Trichy to thanjavur is smallest distance")
	print (dis1)
	if (dis4 < dis5):
		print ("thanjavur to chennai is smallest distance")
		print (dis4)
	else:
		print ("thanjavur to coimbatore is smallest distance")
		print (dis5)
elif((dis2 < dis3) and (dis2 < dis1)):
	print ("Trichy to chennai is smallest distance")
	print (dis2)
	if (dis4 < dis6):
		print ("chennai to thanjavur is smallest distance")
		print (dis4)
	else:
		print ("chennai to coimbatore is smallest distance")
		print (dis6)
else:
	print ("Trichy to coimbatore is smallest distance")
	print (dis3)
	print (dis5)
	print (dis6)

