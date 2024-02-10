# import wwr
from remote import Scraper
from file import save
from flask import Flask, render_template, request, redirect, send_file

# save_wwr = wwr.scrape_page("https://weworkremotely.com/remote-full-time-jobs?page=1")

# keywords = list(map(str, input("key: ").split(",")))
# scrap = remote.Scraper(keywords=keywords)
# scrap.scraping_jobs()


# flask 시작
app = Flask("new scrapper")

db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        scrap = Scraper(keywords=keyword)
        jobs = scrap.scraping_jobs()
        db[keyword] = jobs
        print(db[keyword])
        print("\n\n\n")
        print(db)
    return render_template("search.html", keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save(keyword, db[keyword])
    print(f"{keyword}_job.csv")
    return send_file(f"{keyword}_jobs.csv", as_attachment=True)


app.run("127.0.0.1", port=5000)
