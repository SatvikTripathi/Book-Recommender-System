from flask import Flask, render_template, request
import pickle
import numpy as np

popular_df = pickle.load(open('popular.pkl', "rb"))
pt = pickle.load(open("pivotTable.pkl", "rb"))
books = pickle.load(open("books.pkl", "rb"))
similarity_score = pickle.load(open("similarity_score.pkl", "rb"))

app = Flask(__name__)

@app.route('/')

def index():
    return render_template("index.html",
                           book_name = list(popular_df["Book-Title"].values),
                           author = list(popular_df["Book-Author"].values),
                           votes = list(popular_df["numberOfRatings"].values),
                           rating = list(popular_df["avg_ratings"].values),
                           image = list(popular_df["Image-URL-M"].values)
                           )

@app.route('/recommend')
def reccomend_ui():
    return render_template("recommend.html")

@app.route("/recommend_books", methods = ["POST"])
def recommend():
    user_input = request.form.get("user_input")
    # fetching index with book name:
    suggestions = []
    index = np.where(pt.index == user_input)[0][0]
    suggested_books = sorted(list(enumerate(similarity_score[index])), key = lambda x : x[1], reverse = True)[1 : 11]

    for i in suggested_books:
        items = []
        temp_df = books[books["Book-Title"] == pt.index[i[0]]]
        items.extend(list(temp_df.drop_duplicates("Book-Title")["Book-Title"].values))
        items.extend(list(temp_df.drop_duplicates("Book-Title")["Book-Author"].values))
        items.extend(list(temp_df.drop_duplicates("Book-Title")["Image-URL-M"].values))

        suggestions.append(items)
    print(suggestions)

    return render_template("recommend.html", data = suggestions)

if __name__ == "__main__":
    app.run(debug = True)



