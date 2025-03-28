from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Verbesserte Fragen für den Steckbrief
questions = [
    {
        "id": "name",
        "text": "Wie heißt du?",
        "icon": "👤"
    },
    {
        "id": "age",
        "text": "Wie alt bist du?",
        "icon": "🎂"
    },
    {
        "id": "birthday",
        "text": "Wann hast du Geburtstag?",
        "icon": "🎈"
    },
    {
        "id": "color",
        "text": "Was ist deine Lieblingsfarbe?",
        "icon": "🎨"
    },
    {
        "id": "animal",
        "text": "Was ist dein Lieblingstier?",
        "icon": "🐾"
    },
    {
        "id": "subject",
        "text": "Was ist dein Lieblingsfach in der Schule?",
        "icon": "📚"
    },
    {
        "id": "hobby",
        "text": "Was machst du gerne in deiner Freizeit?",
        "icon": "⚽"
    },
    {
        "id": "food",
        "text": "Was isst du am liebsten?",
        "icon": "🍕"
    },
    {
        "id": "dream",
        "text": "Was möchtest du später einmal werden?",
        "icon": "✨"
    },
    {
        "id": "friend",
        "text": "Wer ist dein bester Freund oder deine beste Freundin?",
        "icon": "🤝"
    },
    {
        "id": "music",
        "text": "Was ist deine Lieblingsmusik oder dein Lieblingslied?",
        "icon": "🎵"
    },
    {
        "id": "movie",
        "text": "Was ist dein Lieblingsfilm oder deine Lieblingsserie?",
        "icon": "🎬"
    },
    {
        "id": "special",
        "text": "Was macht dich besonders?",
        "icon": "🌟"
    }
]

# Verbesserte Farbthemen für Jungen und Mädchen
themes = {
    "boy": {
        "primary": "#1E88E5",  # Kräftiges Blau
        "secondary": "#64B5F6",  # Helles Blau
        "gradient": "linear-gradient(135deg, #1E88E5 0%, #64B5F6 100%)",  # Blau Verlauf
        "accent": "#0D47A1",  # Dunkles Blau
        "emoji": "🦸‍♂️",  # Superheld
        "decorative_emojis": [
            "🦸‍♂️", "⚡", "🚀", "🦁", "🐯", "🎮", "⚽", "🏈", "🎯",
            "🛡️", "⚔️", "🏃‍♂️", "🦾", "🤖", "🎪", "🌟", "✨", "💫"
        ]
    },
    "girl": {
        "primary": "#EC407A",  # Helles Pink
        "secondary": "#F48FB1",  # Zartes Rosa
        "gradient": "linear-gradient(135deg, #EC407A 0%, #F48FB1 100%)",  # Pink Verlauf
        "accent": "#C2185B",  # Dunkles Pink
        "emoji": "👸",  # Prinzessin
        "decorative_emojis": [
            "👸", "🦄", "🎀", "🌸", "🌺", "🦋", "💝", "🎭", "🌈",
            "⭐", "🌟", "✨", "💫", "🎪", "🎨", "🎭", "🧚‍♀️", "🎠"
        ]
    }
}

@app.route('/')
def index():
    return render_template('index.html', questions=questions, themes=themes)

@app.route('/generate_profile', methods=['POST'])
def generate_profile():
    data = request.json
    answers = data.get('answers', {})
    theme = data.get('theme', 'girl')  # Standard ist Mädchen-Theme
    return render_template('profile.html', 
                         answers=answers, 
                         questions=questions, 
                         datetime=datetime,
                         theme=themes[theme])

if __name__ == '__main__':
    app.run(debug=True) 