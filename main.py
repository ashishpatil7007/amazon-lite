from flask import Flask,render_template
import os
app= Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/product_details")
def product_details():
    return render_template("product_details.html")



if __name__ == '__main__':
   if 'PORT' in os.environ:
      port = os.environ['PORT']
   else:
      port= 5000
   app.run(debug=True,host="0.0.0.0",port=port)

