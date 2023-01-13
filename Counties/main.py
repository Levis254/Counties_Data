import json
path="kenya_wards.csv"
with open(path,"r") as file:
    data=[i.split(";") for i in file.readlines()]
    counties_dict={data[i][2]:{data[key][3]:[data[ward][4] for ward in range(1,len(data)) if data[ward][3]==data[key][3]] for key in range(1,len(data)) if data[key][2]==data[i][2]} for i in range(1,len(data))}
with open("counties_data.json","w") as file:
    json.dump(counties_dict,file,indent=3,sort_keys=True)