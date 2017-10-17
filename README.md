# Dockers

Just a list of docker-composer repos for several tecnologies

# Requirements

* You must have docker working properly and make sure your user belongs to docker group
* Make usre you have docker-compose

# Pre-setup

Create a default docker network

```
docker network create dockers
```

# Requirements

Just select the docker you want to start.

Portainer could be used to manage all this in a grafical interface.

In case you use conky and the following in .conkyrc

```
${color}${execi 300  docker ps --format "{{.Names}}" }${color}
```

Check this repo for an example:  https://github.com/rramos/conkyrc

# Testing dockers

Testing dockers in _draft folder

