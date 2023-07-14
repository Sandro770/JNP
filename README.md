# MicroWarehouse
Project made as a part of Languages and Programming Tools II course at the University of Warsaw (microservices group).

Before You start the front app do the following: (React Typescript, default port 3000)
1. cd front
2. npm install -g create-react-app
3. npm install react-scripts
4. npm install react-router-dom @types/react-router-dom
5. npm start (to start the React app)

For the admin app: (Django, default port 8000)
1. Install requirements from requirements.txt
2. Create account at https://customer.cloudamqp.com/
3. Create new instance of RabbitMQ
4. Copy AMQP URL and paste it to the .env file in the admin folder
5. Create .env file in the admin folder and in admin/products folder
6. Place in the .env files the URL from AMQP Details 
7. python3 manage.py runserver (to start the django server)

For the Flask app: (Flask, default port 5000)
1. Install requirements from requirements.txt
2. Copy AMQP URL and paste it to the .env file flask folder
3. python3 main.py (to start the flask server)
4. python3 consumer.py (to start the consumer)


Creating docker images:
sudo docker build -t front_image .
sudo docker build -t main_db_image .
sudo docker build -t admin_image .

Importing docker image from tar file:
docker load < my-image.tar

Running docker containers:
sudo docker run -p 3000:3000 front_image
sudo docker run -p 5000:5000 main_db_image
sudo docker run --network host admin_image

Additional docker commands: 
docker build -t kondrado1234990/jnp2-microservices-{name(admin / flask / front)} .
docker push kondrado1234990/jnp2-microservices-{name(admin / flask / front)}
