import random


# dates of measurement temperature
def generate_random_tempdates():
    year = random.randint(2020, 2024)
    month = random.randint(1, 12)
    if month != 2:
        day = random.randint(1, 30)
    else:
        day = random.randint(1, 28)
    return f"{day}.{month}.{year}"

# temperature list


degrees_v = []
for _ in range(10):
    temp_value = random.randint(0, 30)
    # temp_value = random.choice(temp_values)
    grad_type = random.choice(["°C", "°F"])
    date = generate_random_tempdates()
    # Combine temp_value and grad_type using string formatting
    combined_temp_value = f"{temp_value}{grad_type}"
    temp_dataset = {"Date": date, "Value of the temperature": combined_temp_value}
    degrees_v.append(temp_dataset)

# print(degrees_v)

# for temp_dataset in degrees_v:
#     print(f"{temp_dataset['Date']} {temp_dataset['Value of the temperature']}")
