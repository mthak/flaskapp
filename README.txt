A 3 tier app using pythong flask
POST : The app reads and returns hashsum of a message(store message in mongodb)
GET : given a hashsum return the message
it uses 
* nginx for web ( ssl termination and load balancer)
flask for app ( simple python flask port 5000) 
mongodb for the database tier
All 3 tiers are baked in to docker containers and linked via docker-compose
Nginx works for ssl termination as well as load balancer.
Services are always running using supervisor
We can scale up or scale down the flask app using the myflask docker container and add it in the nginx conf file. We need to rebuild nginx docker container(today) everytime we scale up/down.

TODO : Anytime we scale up flask(web app) Nginx shall auto register it ( shall be done using Consul)
Can I do better ? Oh yeah We can easily do all of this using API Gateway,Lambda & DynamoDb in AWS ( may be some other day ;0)) 

