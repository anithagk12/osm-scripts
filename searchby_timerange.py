import overpy

import overpass

api = overpy.Overpass()

results = api.query("""[out:json]
[timeout:25000]
;
area(3601766358)->.searchArea;
(
  node
    ["amenity"="place_of_worship"](changed:"2018-03-01T00:00:00Z","2018-03-12T11:59:59Z")
    (area.searchArea);
  way
    ["amenity"="place_of_worship"](changed:"2018-03-01T00:00:00Z","2018-03-12T11:59:59Z")
    (area.searchArea);
  relation
    ["amenity"="place_of_worship"]
    (area.searchArea);
);
out;
>;
out skel qt;
""")


print (results)

results.nodes
len(results.nodes)
