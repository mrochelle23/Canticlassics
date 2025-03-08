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
# DATABASE CONNECTION
ca = certifi.where()
# get this path from the panel on mongodb.com
MONGO_URI = "mongodb+srv://rochellm:1x1Sk5Xq6GpW1ENc@cluster0.iipgw.mongodb.net/userDB?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
# Get the database names (database name)
db = client.userDB  # Database name
users_collection = db.users  # Collection name
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

except Exception as e:
    print(e)

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

#Initializes a connection to the flask_db Database
app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app, MONGO_URI, connectTimeoutMS=3000)

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

@app.route('/add', methods=['POST'])
def add_user():
    """Add a user to the database"""
    email = request.form.get('email2')
    if email:
        # Check if the email already exists in the database
        existing_user = users_collection.find_one({'email2': email})
        if existing_user:
            # If the email already exists, render the "already signed up" page
            return render_template('existing_user.html', email=email)

        # If the email doesn't exist, proceed with adding the user
        users_collection.insert_one({'email2': email})

    return redirect('/')

@app.route('/unsubscribe', methods=['GET', 'POST'])
def unsubscribe():
    """Handle unsubscribe request by deleting user from database"""
    if request.method == 'POST':
        email = request.form.get('email')
        if email:
            print(f"Unsubscribe email: {email}")
            user = users_collection.find_one({'email2': email})
            if user:
                return redirect(url_for('confirm_unsubscribe', email=email))
            else:
                return render_template('already_unsubscribed.html')
            
    return render_template('unsubscribe.html')

@app.route('/confirm_unsubscribe', methods=['GET', 'POST'])
def confirm_unsubscribe():
    """Confirm Unsubscribe page"""
    email = request.args.get('email')  # Get email from URL query params
    print(f"Received unsubscribe confirmation for email: {email}")  # Debugging line
    
    if email:
        # Check if email exists in the database
        user = users_collection.find_one({'email2': email})
        if user:
            # Delete the user's information from MongoDB
            result = users_collection.delete_one({'email2': email})
            return render_template('unsubscribe_confirmed.html')
        if not user:
            return render_template('already_unsubscribed.html')  # Display message for already unsubscribed user
        else:
            return "Error: Could not delete the email."
    
    # If email exists, proceed to delete
    users_collection.delete_one({'email2': email})

    return "Error: No email provided."

if __name__ == "__main__":
    app.run(debug=True)  # Set debug=False in production

#mongodb+srv://rochellm:buiV4fmis4nUgVxG@cluster0.ndryv.mongodb.net/
#buiV4fmis4nUgVxG
