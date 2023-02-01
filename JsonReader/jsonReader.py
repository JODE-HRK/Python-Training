import json

with open('./neighbourhoods.geojson', 'r') as json_file:
    with open('./coordinates.txt', 'wt') as f:
        json_data = json.load(json_file)
        # print(json_data)
        # print(json.dumps(json_data, indent=4))
        features = json_data["features"]
        for feature in features:
            # print(feature)
            print(feature["properties"]["neighbourhood"], file=f)
            # print(len(feature["geometry"]["coordinates"]))
            # print(feature["geometry"]["coordinates"][0][0])
            for x in feature["geometry"]["coordinates"][0][0]:
                print(str(x[0]) + ',' + str(x[1]), end=' ', file=f)
            print('', file=f)
