import overpy

import overpass

api = overpy.Overpass()

results = api.query("""[out:json]
[timeout:25000]
;
area(3601766358)->.searchArea;
(
  node
    ["amenity"="place_of_worship"]
    (area.searchArea);
  way
    ["amenity"="place_of_worship"]
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
