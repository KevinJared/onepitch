# ONE MINUTE PITCH
#### This is an application that lets a user post pitches of different categories
#### By **Kevin Jared**
# Description
One pitch is an application where a user can
* A user can see the pitches other people have posted.
* A user can vote on the pitch they liked and give it a downvote or upvote.
* A user can be signed in for me to leave a comment
* A user can receive a welcoming email once I sign up.
* A user can view the pitches I have created in my profile page.
* A user can comment on the different pitches and leave feedback.
* A user can submit a pitch in any category.
* A user can view the different categories.

Note: This is an academic project.
# Setup

## clone this repo:

* git clone https://github.com/KevinJared/onepitch.git

You need to have Python 3.6 installed to run this program.

`$ git clone <this-repository>`<br />

Create a virtual enironment and activate it.

`$ virtualenv -p python`<br>
`$ source virtual/bin/acivate` and `(virtual)$ deactivate` is to deactivate the environment.

In the virtual environment:

`(virtual)$ pip install -r requirements.txt`<br />

Running the app.

    Prepare the environment variables.
    
        (virtual)$exportDATABASE_URL='postgresqlpsycopg2://username:password@localhost/pitch'`<br/>
        `(virtual)$ export SECRET_KEY='Your secret key'

    Run Database Migrations.

        (virtual)$ python manage.py db init
        (virtual)$ python manage.py db migrate -m "Initial migration"
        (virtual)$ python manage.py db upgrade

    Run the app.

        (virtual)$ touch start.sh

        Put #!/usr/bin/env bash as the first line in start.sh
        Put python3.6 manage.py server as the second line in start.sh

        (virtual)$ chmod a+x start.sh
        (virtual)$ ./start.sh

## View on Heroku
https://onepitchgoall.herokuapp.com/

## Technologies Used
Python
HTML
CSS
## Support and contact details
For any questions please feel free to reach out to me through
* kevinjaredkip@gmail.com
### License
* This project is licensed under the MIT Open Source license, please refer to Licence.md for more info
Copyright (c) 2018 **Kevin Jared**
