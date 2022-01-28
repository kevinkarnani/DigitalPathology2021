from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/server', methods=['GET', 'POST'])
def server():
    if request.method == 'GET':
        # if the status is 200, then send the data to the ML algorithm. Update the main page with a loading bar 
        # to show the progress on classification.
        return '<p> GET </p>'
    elif request.method == 'POST':
        return '<p> POST </p>'
    else:
        abort(401)


@app.route('/')
def home_page():
    return """<!DOCTYPE html>
<html>
<head>
<style>
.button {
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}

.button1 {background-color: #4CAF50;} /* Green */
.button2 {background-color: #008CBA;} /* Blue */
</style>
</head>
<body>
<p> Choose Files for Upload  </p>
<form action="/server">
  <input class="button button1" type="file" id="myFile" name="filename" multiple>
  <input class="button button2" type="submit">
</form>

<script>
</script>
</body>
</html> """


if __name__ == '__main__':
    app.run()
