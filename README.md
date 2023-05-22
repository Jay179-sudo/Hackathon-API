
# Hackathon-API

This is a simple a simple Hackathon Hosting Application. 

The hackathon can be posted by anyone and they will be authorized before they are allowed to post hackathons. Users should be able to come and submit some code or files as hackathon submissions.

# API Specification

● Create hackathons by authorized users only. All the hackathons should have some basic fields like

    ■ Title

    ■ description

    ■ Background image

    ■ Hackathon image

    ■ type of submission - Only one of these types should be selected while creating the hackathon - image, file or a link. You can assume that this field cannot be changed after the hackathon has started.

    ■ Start datetime

    ■ End datetime

    ■ Reward prize

● Listing of hackathons

● Register to a hackathon

● Make Submissions

● Submissions should contain the following information

    ■ A name for the submission

    ■ Summary of the submission

    ■ Submission - Based on the type of submission mentioned above, submissions should be accepted. API should validate it.

● Users should be able to list the hackathons they are enrolled to

● Users should be able to view their submissions in the hackathon they were
enrolled in

# Technologies Used

● Django

● SqLite

● DjangoRESTFramework

● DjangoRESTframework-simplejwt

● Pillow

● Drf-Spectacular

● Pillow



# Setting it up

The project can be set up in your local environment by following the steps

● Clone github repository

● Setup environment files   
    
    ● Create a '.env.dev' file and use the following values

        DEBUG=1
        SECRET_KEY=foo
        DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

● Run the following commands
    
    ● docker-compose up -d --build
    ● In the docker's terminal, execute the following commands
        ● python manage.py makemigrations
        ● python manage.py migrate
        ● python manage.py runserver

That's it! You should be setup by now!



# Using The Project

Go to http://127.0.0.1:8000/api/schema/swagger-ui#/ to view the schema of the API

In order to access user-specific JWT Tokens, you need to signup! Once you have the tokens, you have to present it in every subsequent request in order to access the endpoints!

View the Swagger-UI API url in order to perform the operations mentioned in the API Specification.

You can either use Django's Local Server or some special application such as Postman or Insomnia to perform the API calls


