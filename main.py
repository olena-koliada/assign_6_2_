import csv
from degrees import degrees_v
from distance_data import distance_v
from convertor import temperature, distance 

# Temperature
# writing data from file degrees (where the datas are generated)

with open('data_degrees_inp.csv', 'w') as file:
    fieldnames = ['Date', 'Value of the temperature']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(degrees_v)


def convert_temperature(temp_value, target_grad):
    # Extract the numeric part and type of grad
    num_temp_value = temp_value[:-2]
    type_grad = temp_value[-1]

    # Check if conversion is necessary based on target_grad and existing type of grad
    if (target_grad == 'C' and type_grad == 'F') or (target_grad == 'F' and type_grad == 'C'):
        # Convert the temperature only if type_grad differ from target
        if target_grad == 'C':
            converted_temp = temperature.temperature_c(float(num_temp_value))
        else:
            converted_temp = temperature.temperature_f(float(num_temp_value))
        return int(converted_temp)
    else:
        # No conversion needed, return the original value, including type_grad
        return temp_value[:-1]

# defining the func to open/write  new info with target grad


target_grad = input('Input appropriate type of temperature measurement (for Celsius - "C" and for Fahrenheit - "F"): ')
with open('data_degrees_inp.csv', "r") as file, open('data_degrees_outp.csv', "w") as output_file:
    reader = csv.DictReader(file)
    fieldnames = ['Date', 'Value of the temperature', 'Converted Value of the temperature']
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()

    converted__temp_data = []
    for row in reader:
        date = row["Date"]
        temp_value = row["Value of the temperature"]
        # Append original data to list without conversion
        converted__temp_data.append({"Date": date, "Value of the temperature": temp_value})

    # Convert temperatures after reading all data
    for item in converted__temp_data:
        temp_value = item["Value of the temperature"]
        converted_temp = convert_temperature(temp_value, target_grad)
        # Update the "Converted Value" field with converted temperature
        item["Converted Value of the temperature"] = f"{converted_temp}{target_grad}"

    # Write the converted data to the output file
    for item in converted__temp_data:
        writer.writerow(item)


# Adding Distance

with open('data_degrees_dist_inp.csv', 'w') as dist_file:
    fieldnames = ['Date', 'Distance', 'Value of the temperature']
    writer = csv.DictWriter(dist_file, fieldnames=fieldnames)
    writer.writeheader()

    # Iterate through both lists at once using zip
    for degree_data, distance_data in zip(degrees_v, distance_v):
        # Combine data into a single dictionary
        combined_data = {
            'Date': degree_data['Date'],
            'Distance': distance_data,
            'Value of the temperature': degree_data['Value of the temperature']
        }
        writer.writerow(combined_data)


def convert_distance(dist_value, target_dist):
    # if target_dist == 'm' and dist_value[-len(target_dist):] == "ft":
    if target_dist == 'm' and dist_value.strip().endswith("ft"):
        num_dist_value = int(dist_value[:-2])
        # print(num_dist_value)
        converted_dist = int(distance.distance_m(num_dist_value))
        return converted_dist
    elif target_dist == 'm' and dist_value.strip().endswith("m"):
        return dist_value[:-1]
    elif target_dist == "ft" and dist_value.strip().endswith("m"):
        num_dist_value = int(dist_value[:-1])
        converted_dist = int(distance.distance_ft(num_dist_value))
        return converted_dist
    elif target_dist == "ft" and dist_value.strip().endswith("ft"):
        return dist_value[:-2]


target_dist = input('Input appropriate type of distance measurement (for meters - "m" and for feet - "ft"): ')
with open('data_degrees_dist_inp.csv', 'r') as dist_file, open('data_degrees_dist_outp.csv', "w") as output_dist_file:
    reader = csv.DictReader(dist_file)
    fieldnames = ['Date', 'Distance', 'Converted Value of Distance', 'Value of the temperature']
    writer = csv.DictWriter(output_dist_file, fieldnames=fieldnames)
    writer.writeheader()

    converted__dist_data = []
    for row in reader:
        date = row["Date"]
        dist_value = row["Distance"]
        temp_value = row["Value of the temperature"]
        # Append original data to list without conversion
        converted__dist_data.append({"Date": date, "Distance": dist_value, "Value of the temperature": temp_value})

    # Convert distances after reading all data
    for item in converted__dist_data:
        dist_value = item["Distance"]
        converted_dist = convert_distance(dist_value, target_dist)
        # Update the "Converted distance" field with converted distance
        item["Converted Value of Distance"] = f"{converted_dist}{target_dist}"

    # Write the converted data to the output file
    for item in converted__dist_data:
        writer.writerow(item)