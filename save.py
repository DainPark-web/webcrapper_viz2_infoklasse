import csv 


def save_csv(jobs):
    file = open("jobs.csv", mode="w")
    writer = csv.writer(file)

    writer.writerow(["Company"])
    for job in jobs:
        writer.writerow(job.values())
    return
