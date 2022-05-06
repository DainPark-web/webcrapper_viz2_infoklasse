import csv

def save_to_csv(jobs):
    file = open("job.csv", mode="w")
    writer = csv.writer(file)

    writer.writerow(["Company"])
    for job in jobs:
        writer.writerow(job.values())
    return