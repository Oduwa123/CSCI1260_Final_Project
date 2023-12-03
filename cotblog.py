from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


posts = {
"U.S. DOLLAR" : ["ADP Non-Farm Employment Change", "The Institute for Supply Management (ISM), Purchasing Managers' Index (PMI)", "Non-Manufacturing ISM Report On Business", 	
"Unemployment Claims", "Consumer Price Index (CPI)",  "Producer Price Index (PPI)"],
"BRITISH POUND" : ["Gross Domestic Product (GDP)", "Retail Sales m/m", "Consumer Price Index (CPI)" , "Monetary Policy Committee (MPC)", "Purchasing Managers' Index (PMI)"],
"AUSTRALIAN DOLLAR" : ["Wage Price Index", "Unemployment Rate", "Reserve Bank of Australia Release", "Consumer Price Index (CPI)", "Interest Rates"],
"CANADIAN DOLLAR": ["Consumer Price Index (CPI)", "Bank of Canada Release", "Gross Domestic Product (GDP)"],
"SWISS FRANC": ["Consumer Price Index (CPI)"],
"EURO" : ["French Purchasing Managers' Index (PMI)", "Germany Purchasing Managers' Index (PMI)"],
"JAPANESE YEN" : ["	Bank of Japan Release"],
"NEW ZEALAND DOLLAR" : ["Reserve Bank of New Zealand Release", "Interest Rate Statement"]
}


@app.route("/")
def hello():
    return render_template("home.html", posts=posts )

# @app.route("/about")
# def about():
#     return "This is about the COT report and developers "

if __name__ == "__main__":
    app.run(debug=True)



