# Read and process the data
plant_data = {}

with open("milestone.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            name, weight = parts
            attribute = "normal"
        elif len(parts) == 3:
            name, weight, attribute = parts
        else:
            continue  # skip malformed lines
        
        weight = float(weight)
        
        if name not in plant_data:
            plant_data[name] = {
                "max_weight": weight,
                "attributes": set([attribute]),
                "count": 1
            }
        else:
            plant_data[name]["max_weight"] = max(plant_data[name]["max_weight"], weight)
            plant_data[name]["attributes"].add(attribute)
            plant_data[name]["count"] += 1

# Write the processed data to a new file
with open("output.txt", "w") as file:
    for name, info in plant_data.items():
        attr_list = sorted(info["attributes"])
        #file.write(f"- {name} {info['max_weight']} {attr_list}\n")
        file.write(f"- {name} {info['count']}\n")