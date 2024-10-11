# Coworking Space Service Extension
The Coworking Space Service is a set of APIs that enables users to request one-time tokens and administrators to authorize access to a coworking space. This service follows a microservice pattern and the APIs are split into distinct services that can be deployed and managed independently of one another.

For this project, you are a DevOps engineer who will be collaborating with a team that is building an API for business analysts. The API provides business analysts basic analytics data on user activity in the service. The application they provide you functions as expected locally and you are expected to help build a pipeline to deploy it in Kubernetes.

## Getting Started

### Dependencies
#### Local Environment
1. Python Environment - run Python 3.6+ applications and install Python dependencies via `pip`
2. Docker CLI - build and run Docker images locally
3. `kubectl` - run commands against a Kubernetes cluster
4. `helm` - apply Helm Charts to a Kubernetes cluster

#### Remote Resources
1. AWS CodeBuild - build Docker images remotely
2. AWS ECR - host Docker images
3. Kubernetes Environment with AWS EKS - run applications in k8s
4. AWS CloudWatch - monitor activity and logs in EKS
5. GitHub - pull and clone code

### Setup
#### 1. Prepare environment
##### 1.1. Get project from BitBucket
###### git clone https://github.com/thanhbt4/cd12355-microservices-aws-kubernetes-project-starter.git

##### 1.2. Set the AWS credentials
###### aws configure

##### 1.3. Create K8s cluster
###### eksctl create cluster --name my-cluster --region us-east-1 --nodegroup-name my-nodes --node-type t3.small --nodes 1 --nodes-min 1 --nodes-max 2

##### 1.4. Update the context in your local Kubeconfig file
###### aws eks --region us-east-1 update-kubeconfig --name coworking

##### 1.5. Run some K8s yaml to starting up the DB service.
######  kubectl apply -f pvc.yaml
######  kubectl apply -f pv.yaml
######  kubectl apply -f postgresql-deployment.yaml
######   kubectl apply -f postgresql-service.yaml

##### 1.6. Install some required library for add data into Database
######  Update the local package index with the latest packages from the repositories apt install: apt-get install python3-dev -y
	
###### Install a couple of packages to successfully install postgresql server locally:
###### apt install build-essential libpq-dev -y
######  Update python modules to successfully build the required modules:
######  apt install postgresql-client -y
######  apt install postgresql postgresql-contrib

##### 1.7. Set up port-forwarding for the postgresql service
###### kubectl port-forward svc/postgresql-service 5433:5432 &

##### 1.8. Run script for seeding data
######  Export variable
###### export POSTGRES_PASSWORD=$(kubectl get secret --namespace default db-secret -o jsonpath="{.data.DB_PASSWORD}" | base64 -d)
###### export DB_USERNAME=thanhbt4
###### export DB_PASSWORD=${POSTGRES_PASSWORD}
###### export DB_HOST=127.0.0.1
###### export DB_PORT=5433
###### export DB_NAME=coworking
###### Seeding data
###### PGPASSWORD="$DB_PASSWORD" psql --host 127.0.0.1 -U thanhbt4 -d coworking -p 5433 < /workspace/db/1_create_tables.sql
###### PGPASSWORD="$DB_PASSWORD" psql --host 127.0.0.1 -U thanhbt4 -d coworking -p 5433 < /workspace/db/2_seed_users.sql
###### PGPASSWORD="$DB_PASSWORD" psql --host 127.0.0.1 -U thanhbt4 -d coworking -p 5433 < /workspace/db/3_seed_tokens.sql

##### 1.9. Create AWS Codebuild with appropriate IAM role, setting it using webhook to detect if there is new commit from Github repo.

##### 1.10. Run K8s configuration yaml
######  Create config map
###### kubectl apply -f deployment/configmap.yaml
######  Create secret
###### kubectl apply -f deployment/db-secret.yaml

##### 1.11. Commit some code into Github repo so AWS Codebuild will trigger

##### 1.12. Run K8s yaml for running coworking app
###### kubectl apply -f deployment/coworking.yaml

##### 1.13. After AWS EKS has already finish build pods and services, check if pods and services is running
###### kubectl get pods
###### kubectl describe deployment
###### kubectl get svc
###### kubectl describe svc postgresql-service

##### 1.14. Check AWS CloudWatch for application logs

### 2. Get API URL
##### Get the load balancer external IP:
##### kubectl get svc
##### Call 2 API and view the log in AWS CloudWatch:
##### curl <EXTERNAL_IP>/api/reports/daily_usage
##### curl <EXTERNAL_IP>/api/reports/user_visits