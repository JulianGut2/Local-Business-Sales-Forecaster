# General imports
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Just gonna make our data consistent and replicatable here
random.seed(42)
np.random.seed(42)

# Lets create our date range for our data
start_date = datetime(2024, 12, 1)
end_date = datetime(2025,6, 30)
date_range = pd.date_range(start = start_date, end = end_date, freq = 'D')

# Create some services
services = [
    {"service_name": "Oil Change", "base_price" : 50},
    {"service_name": "Brake Replacement", "base_price" : 300},
    {"service_name": "Engine Diagnosis", "base_price": 100},
    {"service_name": "Tire Rotation", "base_price" : 40},
    {"service_name" : "Suspension Repair", "base_price" : 400},
    {"service_name": "Battery Replacement", "base_price": 120},
    {"service_name": "Tune Up", "base_price": 250}
]

# Create some mechanics
mechanics = [
    {"mechanic_id": 1, "name": "Julian", "skill_level": "Advanced"},
    {"mechanic_id": 2, "name": "Marc", "skill_level": "Beginner"},
    {"mechanic_id": 3, "name": "Diego", "skill_level": "Intermediate"},
    {"mechanic_id": 4, "name": "Daniel", "skill_level": "Intermediate"},
    {"mechanic_id": 5, "name": "Isabella", "skill_level": "Advanced"}
]

jobs = []

job_id = 1000

for date in date_range:
    # Around 4 jobs a day
    num_jobs = np.random.poisson(4)
    for _ in range(num_jobs):
        service = random.choice(services)
        mechanic = random.choice(mechanics)

        # Create some type of variation for price and duration
        price = round(np.random.normal(loc = service['base_price'], scale = 15), 2)
        duration = round(np.random.uniform(0.5, 4.0), 1)

        jobs.append({
            "job_id": job_id,
            "date": date.date(),
            "service_name": service["service_name"],
            "price": max(price, 20),
            "duration_hours": duration,
            "mechanic": mechanic["name"]
        })
        job_id += 1
        
df_jobs = pd.DataFrame(jobs)

#print(df_jobs)
df_jobs.to_csv("data/mechanic_shop_jobs.csv", index = False)