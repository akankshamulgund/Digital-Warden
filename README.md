Overview
A web app for women’s safety and empowerment. It features women related news
articles to highlight current women issues, and crimes against women, has an
emergency button for connecting women in need to their trusted ones, various maps
features, and awareness about women’s rights and laws.
Run Instructions
After cloning repository, open a terminal from the repository folder, install all the
requirements from requirements.txt by running a command in terminal/cmd:
For Linux/macOS users:
1. Check for virtual env: python3 -m pip install virtualenv
2. Create virtual env with name Suraksha: python3 -m venv Suraksha
3. Activate virtual env: source Suraksha/bin/activate
4. Install required dependencies: pip install -r requirements.txt
5. Run the web app server: ./run.sh
For Windows users:
1. Check for virtual env: py -m pip install --user virtualenv
2. Create virtual env with name Suraksha: py -m venv Suraksha
3. Activate virtual env: .\suraksha\Scripts\activate
4. Install required dependencies: pip install -r requirements.txt
5. Change directory to the website: cd website
6. Run Project Server: python manage.py runserver
2
Project APIs
1) Twilio for messaging service:
The Twilio messaging service has been used in the project. Due to the trial version
messages can be sent only to the verified numbers (currently of Parikh Goyal and Ankit
Goyal). Upon licking the emergency button the API is used to send an emergency message
to the above mentioned verified mobile numbers.
2) Mapmyindia for maps:
The project used Mapmyindia APIs for displaying maps, geocoding, reverse geocoding, and
embedding of Corona updates. The routing, navigating, and safe route could not be
integrated with the current version of the project as mapmyindia was using PHP scripts at
the backend for the above-mentioned tasks, which was not possible to run on a Django
server.
3) Geolocation:
The find me feature of the project uses geolocation API for finding current location
coordinates through the IP address. And then the coordinates are reverse geocoded to get
the address information, which is then displayed on mapmyindia maps.
Project Structure
I. website
The name of the Django project
II. website/main_app
The main App of the project.
III. website/main_app/templates/main_app
The directory containing all the HTML templates of the project.
IV. website/main_app/static
The directory for all the images used in the project.
3
V. website/main_app/forms.py
The file with the emergency contact registration form.
VI. website/main_app/mail.py
The file with a send_mail function to send mail.
VII. website/main_app/Scraper.py
The file to scrape the news content.
VIII. website/newsdb.db
The database to store news data.
IX. website/main_app/SmsSender.py
The file with a send message function to send a message using Twilio API.
X. Html templates
city_map.html - for finding places in the find_in_city page.
common.html - file with navbar and footer common to all pages.
corona_updates.html - file with the corona updates page.
create_contact.html - create emergency contact page.
delete_contact.html - delete emergency contact page.
developers.html - developers page.
emergency.html - emergency page after the emergency button is pressed.
emergency_contacts.html - display emergency contacts page.
find_me.html - find me page to display current location.
helpline _numbers.html - page with state-wise helpline numbers listed.
home.html - homepage of the project.
login.html - login page.
news.html - quick glance to see women related news.
register.html - register page.
women_laws.html - women laws page.
4
women_rights.html - women rights page.
