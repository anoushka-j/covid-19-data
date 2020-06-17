from flask import Flask, render_template, request, url_for, redirect
import requests

app = Flask(__name__)

@app.route("/")
def returnSite() : 
  return render_template("index.html")
    
@app.route('/getData', methods=['POST'])
def getData():
  try: 
    variable = request.form['variable'] 
    url = "https://api.covid19api.com/total/country/{country}/status/confirmed?from=2020-03-01T00:00:00Z&to=2020-04-01T00:00:00Z".format(country=variable.lower())
    data = requests.get(url)
    new_data = data.json()
    for countrydata in new_data : 
      if countrydata['Date'] == '2020-04-01T00:00:00Z' : 
        formatted_data = variable.title() + " has " + str(countrydata["Cases"]) + " COVID-19 cases"
        return render_template('data.html', formatted_data = formatted_data, countryname = variable)
  except TypeError : 
    return render_template('error.html', formatted_data = "No data found, invalid country", countryname = variable)

if __name__ == "__main__" : 
  app.run(debug=True)