import overpy
import csv
import overpass
api = overpy.Overpass()
fobj=open("temple.csv","a")
#fobj.write("Temples in Trichy")
#head=("Month,No of Nodes")
#fobj.write('\n'+head)
results = api.query("""[out:json]
[timeout:25]
;
(
  node
    ["amenity"="place_of_worship"](changed:"2017-12-01T00:00:00Z","2017-12-31T11:59:59Z")
    (10.719309373438,78.604431152344,10.898042159726,78.829650878906);
  way
    ["amenity"="place_of_worship"]
    (10.719309373438,78.604431152344,10.898042159726,78.829650878906);
  relation
    ["amenity"="place_of_worship"]
    (10.719309373438,78.604431152344,10.898042159726,78.829650878906);
);
out;
>;
out skel qt;
""")


print (results)
mon="December"
results.nodes
w=str(len(results.nodes))
inp=(mon+","+w)
fobj.write('\n'+inp)
