from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# 선물 목록 (공 번호별)
GIFTS = {
    1:  {"name": "🍫 수제 초콜릿 박스",     "grade": "S", "color": "#FF1493"},
    2:  {"name": "💐 장미 꽃다발",           "grade": "A", "color": "#FF6B6B"},
    3:  {"name": "🧸 곰인형 세트",           "grade": "A", "color": "#FF8C69"},
    4:  {"name": "💌 손편지 + 커플링",       "grade": "S", "color": "#FF1493"},
    5:  {"name": "🍰 케이크 교환권",         "grade": "B", "color": "#FFB347"},
    6:  {"name": "☕ 카페 데이트 교환권",    "grade": "B", "color": "#FFB347"},
    7:  {"name": "🎀 리본 머리띠",           "grade": "C", "color": "#DDA0DD"},
    8:  {"name": "🕯️ 로맨틱 캔들",          "grade": "B", "color": "#FFB347"},
    9:  {"name": "💝 하트 쿠키 세트",        "grade": "A", "color": "#FF6B6B"},
    10: {"name": "🌹 영화관 데이트 교환권", "grade": "S", "color": "#FF1493"},
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/draw")
def draw():
    ball_number = random.randint(1, 10)
    gift = GIFTS[ball_number]
    return jsonify({
        "ball": ball_number,
        "gift": gift["name"],
        "grade": gift["grade"],
        "color": gift["color"],
    })

if __name__ == "__main__":
    app.run(debug=True)
