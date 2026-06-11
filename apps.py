from flask import Flask, render_template

app = Flask(__name__)

homestay_data = [

    {
        "id": 1,
        "name": "Lakhamandal Homestay",
        "owner": "Soniya",
        "village": "Lakhamandal",
        "district": "Dehradun",
        "description": "Stay in the historic village of Lakhamandal and experience traditional Himalayan hospitality, scenic surroundings, and peaceful village life.",
        "images": [
            "images/lakhamandal/img1.jpeg",
            "images/lakhamandal/img2.jpeg"
        ]
    },

    {
        "id": 2,
        "name": "Tunalka Homestay",
        "owner": "Hemlata Parmar",
        "village": "Tunalka",
        "district": "Uttarkashi",
        "description": "Enjoy an authentic village experience in Tunalka with beautiful mountain views, local cuisine, and a welcoming family atmosphere.",
        "images": [
            "images/tunalka/img1.jpeg",
            "images/tunalka/img2.jpeg"
        ]
    },

    {
        "id": 3,
        "name": "Rana Gaon Homestay",
        "owner": "Baldev Singh",
        "village": "Rana Gaon",
        "district": "Uttarkashi",
        "description": "Discover the beauty of Rana Gaon through traditional village living, nature walks, and a relaxing Himalayan environment.",
        "images": [
            "images/rana-gaon/img1.jpeg",
            "images/rana-gaon/img2.jpeg"
        ]
    },

    {
        "id": 4,
        "name": "Dangurgaon Homestay",
        "owner": "Sandeep Rawat",
        "village": "Dangurgaon",
        "district": "Uttarkashi",
        "description": "Experience the rich culture of Dangurgaon while enjoying comfortable accommodation, local traditions, and stunning mountain landscapes.",
        "images": [
            "images/dangurgaon-sandeep/img1.jpeg",
            "images/dangurgaon-sandeep/img2.jpeg"
        ]
    },

    {
        "id": 5,
        "name": "Dangurgaon Heritage Homestay",
        "owner": "Santosh Rawat",
        "village": "Dangurgaon",
        "district": "Uttarkashi",
        "description": "A heritage-style homestay offering traditional village hospitality, cultural experiences, and a peaceful stay in Dangurgaon.",
        "images": [
            "images/dangurgaon-santosh/img1.jpeg",
            "images/dangurgaon-santosh/img2.jpeg"
        ]
    },

    {
        "id": 6,
        "name": "Bariya Homestay",
        "owner": "Viraj",
        "village": "Bariya",
        "district": "Uttarkashi",
        "description": "Relax in the serene village of Bariya, surrounded by Himalayan beauty, fresh air, and authentic local traditions.",
        "images": [
            "images/bariya/img1.jpeg",
            "images/bariya/img2.jpeg"
        ]
    }

]


@app.route("/")
def home():
    return render_template(
        "home.html",
        homestays=homestay_data
    )


@app.route("/homestays")
def homestays_page():
    return render_template(
        "homestays.html",
        homestays=homestay_data
    )


@app.route("/homestay/<int:id>")
def detail(id):

    homestay = next(
        (h for h in homestay_data if h["id"] == id),
        None
    )

    return render_template(
        "detail.html",
        homestay=homestay
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

# To this (for production):
if __name__ == "__main__":
    app.run(debug=False)