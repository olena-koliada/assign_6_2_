import random


# list of measurement distance
distance_v = []
for _ in range(10):
    dist_value = random.randint(1, 100)
    dist_type = random.choice(["ft", "m"])
    combined_dist_value = f"{dist_value}{dist_type}"
    # dist_value_dataset = {"Date": date, "Value of the temperature": combined_dist_value}
    distance_v.append(combined_dist_value)
    # print(distance_v)