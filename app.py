from flask import Flask, render_template
app = Flask(__name__)

# import crawling


@app.route('/')
def hello():

    # myList, myList_href = crawling.daum()
    # todayhumor, todayhumor_href = crawling.today_humor()
    # clien, clien_href = crawling.clien()

    return render_template("asd")

@app.route('/about')
def about():
    return "여기는 어바웃입니다."


if __name__ == '__main__':
    app.run('0,0,0,0', port=80)