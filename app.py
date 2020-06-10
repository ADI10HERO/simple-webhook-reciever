from  flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/alerts', methods = ["POST"])
def alters():
    data = request.json
    alerts = data['alerts']
    with open('templates/alerts.html','a') as f:
        to_write = ''
        for all_alerts in alerts:
            to_write += ' <tr>' 
            for tags in all_alerts:
                to_write += ' <td>' + all_alerts[tags] + ' </td>'
            to_write += ' </tr>'
        f.write(to_write)
    return '', 200

@app.route('/alerts', methods = ["GET"])
def render_alerts():
    return render_template('alerts.html')


if __name__ == '__main__':
   app.run(host='0.0.0.0',debug = True)

