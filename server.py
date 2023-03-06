from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/<path:page_name>')
@app.route('/')
def page(page_name='home'):
    if not page_name.endswith('.html'):
        page_name += '.html'
    return render_template(page_name)


def write_to_file(data):
    with open("database", mode="a") as database:
        email = data["email"]
        subjuct = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subjuct},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subjuct = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subjuct, message])


@app.route('/thankyou', methods=['POST', 'GET'])
def thankyou(thanks_page="thankyou"):
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            thanks_page += ".html"
            return redirect(thanks_page)
        except:
            return "did not save to database"
    else:
        return "Something went wrong. Try again."


if __name__ == '__main__':
    app.run(debug=True)
