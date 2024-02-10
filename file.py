import csv
import wwr

# import remote


def save_csv():
    file = open("jobs.csv", "w", encoding="utf-8")
    writter = csv.writer(file)
    writter.writerow(
        ["Title", "Company", "Position", "region", "url"]
    )  # writerow는 list를 넣어줘야 한다.
    for job in wwr.all_jobs:
        writter.writerow(job.values())
    file.close()


def save(keyword, job_datas):
    file = open(f"{keyword}_jobs.csv", "w", encoding="utf-8")
    writter = csv.writer(file)
    writter.writerow(
        ["Title", "Company", "Position", "region", "url"]
    )  # writerow는 list를 넣어줘야 한다.
    for job_data in job_datas:
        writter.writerow(job_data.values())
    file.close()
