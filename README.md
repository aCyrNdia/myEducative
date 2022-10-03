# myEducative

## Why this repository ?
This is where I will put my templates.
These templates are such an explanation on how to use some tools for doing somes projects

### Technologies...
The main used tools are :
- Kubernetes when it comes to microservices,
- Flask for Python app development,
- Helm for all about infrastructure templating,
- Lambda for serverless models,
- Elastic Beanstalk for PaaS hosting

## Structure...
The repositories are named as following the model : <main technology>-<infratype>

For the templates, if you see these files, here are what they contain :
- AppModel/		: contain the model app for our serverless function with the handler and are based on Application/
- Application/		: contain the application files and the Dockerfile used to create the image based on that application or for serverless model
- InfraOnCluster/	: contain the Kubernetes objects used to deploy our cluster
- MyChart/		: contain the structure of a from scratch developed chart
- .Notes.txt		: contain the procedure and the explanation of the Lab
