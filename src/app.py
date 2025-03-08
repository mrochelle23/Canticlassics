from flask import Flask, request, redirect, render_template, url_for
from flask_pymongo import PyMongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask_mail import Mail, Message
import certifi
from email.utils import formataddr
from flask import send_from_directory
# import openai

app = Flask(__name__)

def create_app():
    # Register Blueprints (modular route handling)
    # app.register_blueprint(main_bp)
    # app.register_blueprint(chatbot_bp, url_prefix="/chatbot")
    # app.register_blueprint(events_bp, url_prefix="/events")
    return app
############################################################


############################################################
# SETUP
############################################################


############################################################
# ROUTES
############################################################

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/events')
def events():
    """Events page"""
    return render_template('events.html')

@app.route('/recordings')
def recordings():
    """Recordings page"""
    return render_template('recording.html')

@app.route('/static/audio/<filename>')
def get_audio(filename):
    return send_from_directory('static/audio', filename, mimetype='audio/mpeg')

@app.route('/static/images/<filename>')
def serve_image(filename):
    return send_from_directory('static/images', filename)

@app.route('/artists')
def artists():
    """Artists page"""
    return render_template('artists.html')

@app.route('/archives')
def archives():
    """Archives page"""
    return render_template('archives.html')

@app.route('/about')
def about():
    """About page"""
    return render_template('about-us.html')

@app.route('/chatbot')
def chatbot():
    """Chatbot page"""
    return render_template('chatbot.html')

if __name__ == "__main__":
    app.run(debug=True)  # Set debug=False in production

#mongodb+srv://rochellm:buiV4fmis4nUgVxG@cluster0.ndryv.mongodb.net/
#buiV4fmis4nUgVxG
