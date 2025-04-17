from flask import Flask, request, redirect, render_template, url_for
from flask_pymongo import PyMongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask_mail import Mail, Message
import certifi
from email.utils import formataddr
from flask import send_from_directory
from flask_cors import CORS
# Initialize Flask application
app = Flask(__name__)
CORS(app) # Enable Cross-Origin Resource Sharing (CORS)

############################################################
# DATABASE CONNECTION
############################################################
ca = certifi.where() # Get the path to the CA certificate
# get this path from the panel on mongodb.com
MONGO_URI = "mongodb+srv://rochellm:1x1Sk5Xq6GpW1ENc@cluster0.iipgw.mongodb.net/userDB"

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

############################################################
# SETUP
############################################################

#Initializes a connection to the flask_db Database
app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app)

############################################################
# ROUTES
############################################################

@app.route('/')
def index():
    """Home page"""
    users = users_collection.find() # Retrieve all users from the database
    return render_template('index.html', users=users) # Render the home page with user data

@app.route('/events')
def events():
    """Events page"""
    return render_template('events.html') # Render the events page

@app.route('/recordings')
def recordings():
    """Recordings page"""
    return render_template('recordings.html') # Render the recordings page

@app.route('/static/audio/<filename>')
def get_audio(filename):
    return send_from_directory('static/audio', filename, mimetype='audio/mpeg')

@app.route('/static/images/<filename>')
def serve_image(filename):
    return send_from_directory('static/images', filename)

@app.route('/artists')
def artists():
    """Artists page"""
    return render_template('artists.html') # Render the artists page

@app.route('/archives')
def archives():
    """Archives page"""
    return render_template('archives.html') # Render the archives page

@app.route('/about')
def about():
    """About page"""
    return render_template('about-us.html') # Render the about-us page

# Flask-Mail configuration (replace with Canti Classics' email details)
app.config['MAIL_SERVER'] = 'smtp.gmail.com' # Mail server
app.config['MAIL_PORT'] = 587 # Mail server port
app.config['MAIL_USE_TLS'] = True # Enable TLS
app.config['MAIL_USE_SSL'] = False  # Must be False for TLS
app.config['MAIL_USERNAME'] = "k72003361@gmail.com" # Sender email address
app.config['MAIL_PASSWORD'] = "bzobywejgfrujtod"  # App password for the sender email
app.config['MAIL_NAME'] = "Canti Classics" # Sender name
sender_name = "Canti Classics"
sender_email = "k72003361@gmail.com"
formatted_sender = formataddr((sender_name, sender_email)) # Format sender email
mail = Mail(app) # Initialize Flask-Mail

@app.route('/send_inquiry', methods=['POST'])
def submit_form():
    """Submit form page"""
    import re  # Import regex for email validation

    # Get the form data
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    # Server-side validation for form data
    if not name or not email or not message:
        return "All fields are required.", 400
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email): # Validate email format
        return "Invalid email format.", 400

    try:
        # Send confirmation email to Canti Classics (notification)
        msg_to_canti = Message(subject=f"New Inquiry from {name}",
                        sender=formatted_sender,
                        recipients=["k72003361@gmail.com"],
                        body=f"New inquiry from {name} ({email}):\n\n{message}")

        # Send confirmation email to User's Email (notification)
        msg_to_user = Message(
            subject="New Inquiry",
            sender=formatted_sender,
            recipients=[email],
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
        mail.send(msg_to_canti) # Send email to Canti Classics
        mail.send(msg_to_user) # Send email to the user
        return redirect('/') # Redirect to the home page

    except Exception as e:
        print(f"Full error: {e}") # Log the error
        return f"Error sending email: {str(e)}"

@app.route('/add', methods=['POST', 'GET'])
def add_user():
    """Add a user to the database"""
    import re # Import regex for email validation

    email = request.form.get('email2') # Get email from the form

    # Server-side validation for email
    if not email:
        return "Email is required.", 400
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email): # Validate email format
        return "Invalid email format.", 400

    # Check if the email already exists in the database
    existing_user = users_collection.find_one({'email2': email})
    if existing_user:
        return render_template('existing_user.html', email=email) # Render existing user page

    users_collection.insert_one({'email2': email})

    try:
        # Send notification email to Canti Classics
        msg_to_canti = Message(subject=f"Someone Signed Up For The Newsletter!",
                        sender=formatted_sender,
                        recipients=["k72003361@gmail.com"],
                        body=f"({email})")

        # Send confirmation email to the user
        msg_to_user = Message(
            subject="Newsletter Confirmation",
            sender=formatted_sender,
            recipients=[email],
            html=f"""
            <!-- Main Email Content -->
            <h1 style="color: black">Thanks For Subscribing!</h1>
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
        mail.send(msg_to_canti) # Send email to Canti Classics
        mail.send(msg_to_user) # Send email to the user
        return redirect('/') # Redirect to the home page

    except Exception as e:
        print(f"Full error: {e}") # Log the error
        return f"Error sending email: {str(e)}"


@app.route('/unsubscribe', methods=['GET', 'POST'])
def unsubscribe():
    """Handle unsubscribe request by deleting user from database"""
    import re #Import regex for email validation

    if request.method == 'POST':
        email = request.form.get('email') # Get email from the form

        # Server-side validation for email
        if not email:
            return "Email is required.", 400
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return "Invalid email format.", 400

        print(f"Unsubscribe email: {email}")
        user = users_collection.find_one({'email2': email}) # Check if the email exists
        if user:
            return redirect(url_for('confirm_unsubscribe', email=email)) # Redirect to confirmation page
        else:
            return render_template('already_unsubscribed.html') # Render already unsubscribed page

    return render_template('unsubscribe.html') # Render unsubscribe page


@app.route('/confirm_unsubscribe', methods=['GET', 'POST'])
def confirm_unsubscribe():
    """Confirm Unsubscribe page"""
    import re # Import regex for email validation

    email = request.args.get('email') # Get email from query parameters
    print(f"Received unsubscribe confirmation for email: {email}")

    if not email:
        return "Error: No email provided."

    # Email format check
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):  # Validate email format
        return "Invalid email format.", 400

    user = users_collection.find_one({'email2': email}) # Check if the email exists
    if user:
        result = users_collection.delete_one({'email2': email}) # Delete the email from the database
        if result.deleted_count > 0:
            # Send notification email to Canti Classics
            msg_to_canti = Message(subject=f"No Longer Subscribed",
                        sender=formatted_sender,
                        recipients=["k72003361@gmail.com"],
                        body=f"{email} unsubscribed from the newsletter")
            mail.send(msg_to_canti) # Send email to Canti Classics

            # Send confirmation email to the user
            msg_to_user = Message(
                subject="Unsubscribe Confirmation",
                sender=formatted_sender,
                recipients=[email],
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
            mail.send(msg_to_user) # Send email to the user
            return render_template('unsubscribe_confirmed.html')  # Render unsubscribe confirmation page
        else:
            return "Error: Could not delete the email." # Return error message
    else:
        return render_template('already_unsubscribed.html') # Render already unsubscribed page


if __name__ == "__main__":
    app.run(debug=True)  # Set debug=False in production
