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

# Flask-Mail configuration (replace with Canti Classics' email details)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False  # Must be False for TLS
app.config['MAIL_USERNAME'] = "k72003361@gmail.com"
app.config['MAIL_PASSWORD'] = "rzgfnwdjddxgqhxd"  # Use the correct app password
app.config['MAIL_NAME'] = "Canti Classics"
sender_name = "Canti Classics"
sender_email = "k72003361@gmail.com"
formatted_sender = formataddr((sender_name, sender_email))
mail = Mail(app)
mongo.cx

@app.route('/send_inquiry', methods=['POST'])
def submit_form():
    """Submit form page"""
    # Get the form data
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    try:
        # Send confirmation email to Canti Classics (notification)
        msg_to_canti = Message(subject=f"New Inquiry from {name}",
                        sender=formatted_sender,  # Replace with Canti Classics' email
                        recipients=["k72003361@gmail.com"],
                        body=f"New inquiry from {name} ({email}):\n\n{message}")  # Replace with Canti Classics' email

        # Send confirmation email to User's Email (notification)
        msg_to_user = Message(
            subject="New Inquiry",
            sender=formatted_sender,  # Replace with Canti Classics' email
            recipients=[email],  # Use square brackets for recipients
            html=f"""
            <p style="color: black;">Hi {name}!</p>
            <p style="color: black;">Thank you for sending an inquiry! We will get back to you soon.</p><br>
            <p style="color: black;">Canti Classics Team</p>
            <p style="color: black;">Follow Us</p>

            <!-- Footer Section -->
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="margin-top: 20px; padding-top: 10px; border-top: 1px solid #ddd; background-color: #782F37;">
                <tr>
                    <td align="center" style="padding: 10px;">
                        <p style="color: white; font-size: 14px; margin: 0;">Follow Us</p>
                        <br>
                        <a href="https://facebook.com/canticlassics" style="margin-right: 10px; text-decoration: none;">
                            <img width="30" height="30" alt="Facebook" style="vertical-align:middle" src="https://images.meredith.com/Investopedia/Newsletters/Images/2023/04/Investopedia_Facebook_Icon.png">
                        </a>
                        <a href="https://instagram.com/canticlassics" style="margin-right: 10px; text-decoration: none;">
                            <img width="30" height="30" alt="Instagram" style="vertical-align:middle" src="https://images.meredith.com/Investopedia/Newsletters/Images/2023/04/Investopedia_Instagram_Icon.png">
                        </a>
                        <a href="https://youtube.com/canticlassics1" style="margin-right: 10px; text-decoration: none;">
                            <img width="30" height="30" alt="YouTube" style="vertical-align:middle" src="https://images.meredith.com/Investopedia/Newsletters/Images/2023/04/Investopedia_Youtube_Icon.png">
                        </a>
                    </td>
                </tr>
                <tr>
                    <td align="center" style="font-size: 12px; color: #782F37; padding: 5px;">
                        <p style="margin: 0; color: white;">© 2025 Canti Classics. All Rights Reserved.</p>
                        <p style="margin: 0;"><a href="http://127.0.0.1:5000/#contact"; style="color: white; text-decoration: none;">Subscribe to Our Newsletter</a></p>
                    </td>
                </tr>
            </table>
            """
        )
        mail.send(msg_to_canti)
        mail.send(msg_to_user)
        return redirect('/')

    except Exception as e:
        print(f"Full error: {e}") # log full error
        return f"Error sending email: {str(e)}"  # In case there's an error sending the emailv


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

    try:
        # Send confirmation email to Canti Classics (notification)
        msg_to_canti = Message(subject=f"Someone Signed Up For The Newsletter!",
                        sender=formatted_sender,  # Replace with Canti Classics' email
                        recipients=["k72003361@gmail.com"], # Replace with Canti Classics' email
                        body=f"({email})")

        # Send confirmation email to User's Email (notification)

        # Send confirmation email to User's Email (notification)
        msg_to_user = Message(
            subject="Newsletter Confirmation",
            sender=formatted_sender,  # Replace with Canti Classics' email
            recipients=[email],  # Use square brackets for recipients
            html=f"""
            <!-- Main Email Content -->
            <p style="color: black;">Thank you for signing up for our newsletter!</p>
            <br>
            <p style="color: black;">Canti Classics Team</p>

            <!-- Footer Section -->
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="margin-top: 20px; padding-top: 10px; border-top: 1px solid #ddd; background-color: #782F37;">
                <tr>
                    <td align="center" style="padding: 10px;">
                        <p style="color: white; font-size: 14px; margin: 0;">Follow Us</p>
                        <br>
                        <a href="https://facebook.com/canticlassics" style="margin-right: 10px; text-decoration: none;">
                            <img width="30" height="30" alt="Facebook" style="vertical-align:middle" src="https://images.meredith.com/Investopedia/Newsletters/Images/2023/04/Investopedia_Facebook_Icon.png">
                        </a>
                        <a href="https://instagram.com/canticlassics" style="margin-right: 10px; text-decoration: none;">
                            <img width="30" height="30" alt="Instagram" style="vertical-align:middle" src="https://images.meredith.com/Investopedia/Newsletters/Images/2023/04/Investopedia_Instagram_Icon.png">
                        </a>
                        <a href="https://youtube.com/canticlassics1" style="margin-right: 10px; text-decoration: none;">
                            <img width="30" height="30" alt="YouTube" style="vertical-align:middle" src="https://images.meredith.com/Investopedia/Newsletters/Images/2023/04/Investopedia_Youtube_Icon.png">
                        </a>
                    </td>
                </tr>
                <tr>
                    <td align="center" style="font-size: 12px; color: #782F37; padding: 5px;">
                        <p style="margin: 0; color: white;">© 2025 Canti Classics. All Rights Reserved.</p>
                        <p style="margin: 0;"><a href="http://127.0.0.1:5000/unsubscribe?email={email}" style="color: white; text-decoration: none;">Unsubscribe</a></p>
                    </td>
                </tr>
            </table>
            """
        )
        mail.send(msg_to_canti)
        mail.send(msg_to_user)
        return redirect('/')

    except Exception as e:
        print(f"Full error: {e}") # log full error
        return f"Error sending email: {str(e)}"

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
            if result.deleted_count > 0:
                msg_to_canti = Message(subject=f"No Longer Subscribed",
                        sender=formatted_sender,  # Replace with Canti Classics' email
                        recipients=["k72003361@gmail.com"],
                        body=f"{email} unsubscribed from the newsletter")  # Replace with Canti Classics' email
                mail.send(msg_to_canti)

                msg_to_user = Message(
                    subject="Unscubscribe Confirmation",
                    sender=formatted_sender,  # Replace with Canti Classics' email
                    recipients=[email],  # Use square brackets for recipients
                    html=f"""
                    <!-- Main Email Content -->
                    <h1 style="color: black">Unsubscribe Successful</h1>
                    <p style="color: black">You have successfully unsubscribed from our newsletter. We're sorry to see you go!</p>

                    <!-- Footer Section -->
                    <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="margin-top: 20px; padding-top: 10px; border-top: 1px solid #ddd; background-color: #782F37;">
                    <tr>
                        <td align="center" style="font-size: 12px; color: white; padding: 5px;">
                            <p style="margin: 0; color: white">© 2025 Canti Classics. All Rights Reserved.</p>
                            <p style="margin: 0;"><a href="http://127.0.0.1:5000/#contact" style="color: white; text-decoration: none;">Resubscribe</a></p>
                        </td>
                    </tr>
                    """
                )
                mail.send(msg_to_user)
                return render_template('unsubscribe_confirmed.html')
            else:
                return "Error: Could not delete the email."
        if not user:
            return render_template('already_unsubscribed.html')  # Display message for already unsubscribed user

    return "Error: No email provided."


if __name__ == "__main__":
    app.run(debug=True)  # Set debug=False in production

#mongodb+srv://rochellm:buiV4fmis4nUgVxG@cluster0.ndryv.mongodb.net/
#buiV4fmis4nUgVxG
