from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/generate',methods=['POST'])
def generate():
    ingredients=request.form['ingredients']
    cuisine=request.form['cuisine']
    diet=request.form['diet']

    recipe=f"Recipe generated with ingredients: {ingredients} in cuisine style : {cuisine} and diet: {diet}"

    return render_template("result.html",recipe=recipe)

if __name__=='__main__':
    app.run(debug=True)




