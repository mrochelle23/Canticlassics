# Boostrapers

The Boostrapers Team will redesign the Canti Classics website. Our goal is to modernize the website, enhance user experience, and add new features as per the client’s requirements. The redesign will focus on usability, accessibility, and functionality while maintaining the essence of the Canti Classics brand.

# Canti Classics

*Canti Classics* is a modernized music archive and artist showcase built with Flask. The project highlights a curated collection of recordings, artist profiles, and events related to Robert Sims and the Canti Classics label. Designed with accessibility, simplicity, and a dynamic user experience in mind.

## Technologies Used
- Python 3
- Flask
- Flask-Mail
- HTML/CSS (Jinja2 templating)
- JavaScript
- MongoDB
- Git & GitHub
- Figma (for wireframes)
- Jira (for ticket logging & burn-down charts)
- Lucid Chart (for object, sequence & use case diagrams)

## Project Structure
```
Canticlassics/ 
├── src/ 
│ ├── static/ # CSS, JavaScript, and images 
│ │ ├── audio/
│ │ │ ├── audio-sample.ogg
│ │ ├── css/
│ │ │ ├── about-us.css
│ │ │ ├── archives.css
│ │ │ ├── artists.css
│ │ │ ├── base.css
│ │ │ ├── events.css
│ │ │ ├── index.css
│ │ │ └── recordings.css
│ │ ├── images/
│ │ ├── js/
│ │ │ ├── base.js
│ ├──  templates/ # HTML templates (Jinja2) 
│ │ ├── about-us.html
│ │ ├── already_unsubscribed.html
│ │ ├── archives.html
│ │ ├── artists.html
│ │ ├── base.html
│ │ ├── events.html
│ │ ├── existing_user.html
│ │ ├── index.html
│ │ ├── recordings.html
│ │ ├── unsubscribe_confirmed.html
│ │ └── unsubscribe.html
│ ├── app.py # Core Flask application
│ ├── requirements.txt # Project dependencies
│ ├── README.md # You're here!
├── tests/ # Unit test script
│ ├── test_app.py
```
## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/mrochelle23/Canticlassics.git
cd Canticlassics
```

### 2. Set Up Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables
Create a `.env` file in the root directory with the following:
```bash
FLASK_APP=app.py
FLASK_ENV=development
MONGO_URI=your_mongo_uri
```

### 5. Run the Application
```bash
flask run
```
Visit `http://127.0.0.1:5000` in your browser.

# Team Members and Roles

* [Mikhai Rochelle](https://github.com/mrochelle23/CIS350-HW2-Rochelle) (Team Leader & Full-Stack Developer)
* [Kyle Raskay](https://github.com/kyleraskay/CIS350-HW2-Raskay) (Full-Stack Developer)
* [Joan Felber](https://github.com/DJessT/CIS350-HW2-felber) (UX/UI Design Leader & Back End Developer)

