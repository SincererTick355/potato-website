from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/potato/russet")
def russet():
    return render_template("potato_type.html",
                           title="Russet Potatoes",
                           description="Russet potatoes are among the most popular and widely cultivated potato varieties in North America. Recognized by their large size, rough brown skin, and white, fluffy interior, russets are a staple in many kitchens. They originated from selective breeding in the United States during the late 19th century, with the Russet Burbank being the most famous cultivar. These potatoes thrive in cooler climates and are typically grown in states like Idaho and Washington. Their high starch content makes them ideal for baking, mashing, and frying, as they develop a light, airy texture when cooked. Farmers favor russets for their high yield and good storage qualities. In the culinary world, russets are the go-to choice for classic baked potatoes, crispy French fries, and creamy mashed potatoes. Their neutral flavor pairs well with a variety of toppings and seasonings. Nutritionally, russets provide a good source of complex carbohydrates, dietary fiber (especially with the skin), potassium, and vitamin C. They are naturally low in fat and contain some protein. When prepared healthily, russet potatoes can be part of a balanced diet, offering energy and essential nutrients.",
                           uses="Best for baked potatoes, French fries, mashed potatoes, and potato wedges due to their fluffy texture.",
                           nutrition="Rich in carbohydrates, potassium, vitamin C, and fiber when eaten with the skin. Low in fat and protein.",
                           image_url="https://upload.wikimedia.org/wikipedia/commons/6/60/Russet_potato.jpg")

@app.route("/potato/red")
def red():
    return render_template("potato_type.html",
                           title="Red Potatoes",
                           description="Red potatoes are small to medium-sized tubers characterized by their smooth, thin red skin and white, waxy flesh. They are believed to have originated from South American potato varieties and have been cultivated for centuries. Their waxy texture allows them to hold their shape well during cooking, making them ideal for dishes that require boiling or roasting. Red potatoes mature relatively quickly and are often harvested as 'new potatoes' with tender skins. They are popular in salads, soups, and roasted dishes because they maintain a firm, creamy consistency. The skin is rich in nutrients and antioxidants, so it is best consumed unpeeled. Red potatoes are a good source of vitamin C, potassium, and fiber, contributing to heart health and digestive wellness. Their subtle, slightly sweet flavor complements herbs and spices beautifully. Farmers appreciate red potatoes for their disease resistance and adaptability to various soil types. Overall, red potatoes are versatile, nutritious, and add vibrant color to many recipes.",
                           uses="Ideal for boiling, roasting, potato salads, and soups due to their firm texture.",
                           nutrition="Good source of fiber, vitamin C, potassium, and antioxidants, especially in the skin.",
                           image_url="https://upload.wikimedia.org/wikipedia/commons/2/2f/Red_potatoes.jpg")

@app.route("/potato/yukon-gold")
def yukon_gold():
    return render_template("potato_type.html",
                           title="Yukon Gold Potatoes",
                           description="Yukon Gold potatoes are a popular yellow-fleshed variety developed in Canada in the 1960s. They are known for their smooth, thin, golden skin and buttery, creamy interior. This variety was bred to combine the best qualities of waxy and starchy potatoes, making them extremely versatile in the kitchen. Yukon Golds have a naturally rich flavor that requires minimal seasoning, and their texture holds up well to boiling, roasting, and frying. They are excellent for making mashed potatoes with a naturally buttery taste and smooth consistency. Nutritionally, Yukon Golds provide vitamin C, potassium, and some fiber, especially if the skin is left on. Their appealing color comes from carotenoids, which have antioxidant properties. Farmers favor Yukon Golds for their good yield and resistance to bruising. In culinary use, they are prized for their ability to create creamy mashed potatoes, crispy roasted dishes, and flavorful potato salads. Their balanced texture and rich flavor make them a favorite among chefs and home cooks alike.",
                           uses="Versatile: great for mashing, roasting, frying, and potato salads.",
                           nutrition="Contains vitamin C, potassium, fiber, and antioxidants from the yellow pigments.",
                           image_url="https://upload.wikimedia.org/wikipedia/commons/4/4c/Yukon_Gold_potatoes.jpg")

@app.route("/potato/fingerling")
def fingerling():
    return render_template("potato_type.html",
                           title="Fingerling Potatoes",
                           description="Fingerling potatoes are small, elongated tubers resembling fingers, hence their name. They come in various skin and flesh colors, including yellow, red, and purple. Originating from heirloom varieties in South America, fingerlings have gained popularity for their unique appearance and rich, nutty flavor. Their waxy texture holds up well during roasting and boiling, making them ideal for salads and side dishes. Fingerlings are often harvested when small and tender, providing a delicate bite. They are typically cooked whole or halved, with the thin skin left on to retain nutrients and add texture. Nutritionally, fingerlings are a good source of fiber, vitamin C, potassium, and antioxidants, especially in the colored varieties. Their distinctive look and taste make them a favorite in gourmet cooking and farmers' markets. They require well-drained soil and careful handling during harvest to avoid damage. Fingerlings add visual appeal and a unique flavor profile to many dishes, from roasted platters to warm salads.",
                           uses="Excellent roasted whole or halved, in salads, or as a colorful side dish.",
                           nutrition="Provides fiber, vitamin C, potassium, and antioxidants depending on color.",
                           image_url="https://upload.wikimedia.org/wikipedia/commons/3/3b/Fingerling_potatoes.jpg")

@app.route("/potato/purple")
def purple():
    return render_template("potato_type.html",
                           title="Purple and Blue Potatoes",
                           description="Purple and blue potatoes are heirloom varieties known for their vibrant skin and flesh colors, which come from anthocyanins—powerful antioxidants. These potatoes originated in the Andes mountains and have been cultivated for thousands of years. Their striking appearance adds color and nutritional benefits to meals. Purple potatoes have a slightly nutty, earthy flavor and a moist, firm texture that holds up well during cooking. They can be roasted, boiled, or used in salads to add visual interest. The anthocyanins not only provide color but also have anti-inflammatory and antioxidant properties, contributing to overall health. Nutritionally, these potatoes are rich in fiber, vitamin C, potassium, and antioxidants. Farmers appreciate their hardiness and resistance to certain pests. In the kitchen, they are often used to create colorful dishes that appeal to both the eye and palate. Their unique color remains vibrant even after cooking, making them a popular choice for creative culinary presentations.",
                           uses="Can be roasted, boiled, mashed, or used in salads for color and nutrition.",
                           nutrition="High in antioxidants, vitamin C, potassium, and fiber.",
                           image_url="https://upload.wikimedia.org/wikipedia/commons/4/4b/Purple_potatoes.jpg")

@app.route("/potato/new")
def new_potatoes():
    return render_template("potato_type.html",
                           title="New Potatoes",
                           description="New potatoes are young, immature potatoes harvested early in the growing season before their skins have fully set. They can be of any variety but are characterized by their thin, delicate skins and sweeter, more tender flesh. Because of their freshness, new potatoes have a higher moisture content and a crisp texture. They are best enjoyed boiled or roasted with the skin on to preserve nutrients and flavor. New potatoes are popular in spring and early summer dishes, often paired with fresh herbs and light dressings. Nutritionally, they provide vitamin C, potassium, and fiber, especially when eaten with the skin. Their delicate flavor and texture make them ideal for salads and simple side dishes. Farmers harvest new potatoes by gently digging around the plants, taking care not to damage the tender tubers. Their short storage life means they are best consumed soon after harvest, offering a fresh, seasonal taste.",
                           uses="Best boiled or roasted with skins on, in salads, or as a fresh side dish.",
                           nutrition="Slightly higher moisture content, good source of vitamin C, potassium, and fiber.",
                           image_url="https://upload.wikimedia.org/wikipedia/commons/2/2b/New_potatoes.jpg")

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)