from flask import Flask, render_template, request, jsonify
from deepface import DeepFace
import base64
import io
from PIL import Image
import numpy as np
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotion", methods=["POST"])
def emotion():
   
    data = request.get_json()
    image_data = data["image"]

    image_data = image_data.split(",")[1]

    image_bytes = base64.b64decode(image_data)

    image = Image.open(io.BytesIO(image_bytes))
    image = np.array(image)

    result = DeepFace.analyze(
        image,
        actions=["emotion"],
        enforce_detection=False
    )

    detected_emotion = result[0]["dominant_emotion"]

    stories = {
   "happy": {
    "title": "== 23.5 ==",
    "story": "== kisah cinta pelajar siswi pemalu yg nyamar jadi cowok di medsos demi mendekati siswi populer yg ceria. ==",
    "class": "== (🌏)Ongsa-(☀️)sun ==",
    "spirit": "== MilkVosbein-LovePattranite ==",
    "rank": "== 2024 =="
},
"sad": {
    "title": "== BAD BUDDY ==",
    "story": "== Dua mahasiwa dr keluarga bermusuhan diam2 saling jatuh cinta dan berani memutus rantai kebencian masa lalu. ==",
    "class": "== (🥁)Pat-Pran(🎸) ==",
    "spirit": "== OhmPawat-NanonKorapat ==",
    "rank": "== 2021 =="
},
"angry": {
    "title": "== WHO ARE YOU==",
    "story": "== korban perundungan menyamar sebagai kembaran populernya untuk mengungkap misteri hilangnya sang saudari. ==",
    "class": "== (📿)Meen-(📒)Mind-(🩹)Gun-(🥇)Natee ==",
    "spirit": "== NamtanTipnaree-KristPerawat-KayLertsittichai ==",
    "rank": "== 2020 =="
},

"surprise": {
    "title": "== MY PRECIOUS ==",
    "story": "== Nostalgia manis cinta pertama tahun 1999 antara murid berandal dan siswi teladan yg mengubah hidupnya ==",
    "class": "== (📘)Tong-Lin(📖🖊️) ==",
    "spirit": "== NanonKorapat-FilmRachanun ==",
    "rank": "== 2024 =="
},

"fear": {
    "title": "== FRIENDSHIT FOREVER ==",
    "story": "== topeng persahabatan manis yg menyembunyikan manipulasi dan balas dendam mematikan. ==",
    "class": "== (🧪)Baikhaw-(🌷)Tulip-(📷)Tao(📲)Namo ==",
    "spirit": "== PatChayanit-EmiThasorn-NewThitipoom-BounNoppanut ==",
    "rank": "== 2025 =="
},

"neutral": {
    "title": "== UNIDENTIFIED MYSTERIOUS GIRLFRIEND ==",
    "story": "== cinta masa kecil yg hilang 10 tahun lalu kembali dengan kekuatan aneh layaknya alien ==",
    "class": "== (🥽)Mew-Erng(👽)-Fah(🛸) ==",
    "spirit": "== NanonKorapat-MilkPansa-NamtanTipnaree ==",
    "rank": "== 2023 =="
}
}

    anime = stories.get(
    detected_emotion,
    stories["neutral"]
) 
    return jsonify({
    "emotion": detected_emotion,
    "title": anime["title"],
    "story": anime["story"],
    "class": anime["class"],
    "spirit": anime["spirit"],
    "rank": anime["rank"]
})

if __name__ == "__main__":
    app.run(debug=True)

