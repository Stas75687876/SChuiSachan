from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json

app = Flask(__name__, 
            template_folder='../../templates',
            static_folder='../../static')

# Themes configuration
themes = {
    "boy": {
        "primary": "#1E88E5",
        "secondary": "#64B5F6",
        "gradient": "linear-gradient(135deg, #1E88E5 0%, #64B5F6 100%)",
        "accent": "#0D47A1",
        "emoji": "🦸‍♂️",
        "decorative_emojis": ["🦸‍♂️", "⚡", "🚀", "🦁", "🐯", "🎮", "⚽", "🏈", "🎯"]
    },
    "girl": {
        "primary": "#EC407A",
        "secondary": "#F48FB1",
        "gradient": "linear-gradient(135deg, #EC407A 0%, #F48FB1 100%)",
        "accent": "#C2185B",
        "emoji": "👸",
        "decorative_emojis": ["👸", "🦄", "🎀", "🌸", "🌺", "🦋", "💝", "🎭", "🌈"]
    }
}

# Questions list
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

def handler(event, context):
    """Handle incoming requests."""
    if event['httpMethod'] == 'GET':
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html',
                'Cache-Control': 'no-cache'
            },
            'body': render_template('index.html', 
                                  questions=questions,
                                  themes=themes)
        }
    elif event['httpMethod'] == 'POST':
        try:
            data = json.loads(event['body'])
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'text/html',
                    'Cache-Control': 'no-cache'
                },
                'body': render_template('profile.html',
                                      answers=data.get('answers', {}),
                                      questions=questions,
                                      datetime=datetime,
                                      theme=themes[data.get('theme', 'girl')])
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }
    else:
        return {
            'statusCode': 405,
            'body': 'Method not allowed'
        } 