A 3 tier app using pythong flask
POST : The app reads and returns hashsum of a message(store message in mongodb)
GET : givena hashsum return the message
it uses nginx for web flask for app and mongodb for the database tier
All 3 tiers are baked in to docker containers and linked via docker-compose
Nginx works for ssl termination as well as load balancer.
We can scale up scale down the flask app using the docker container and add it in the nginx.

TODO : Anytime we scale up flask(web app) Nginx shall auto register it ( shall be done using Consul)

