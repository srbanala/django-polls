kubectl apply -f k8s
kubectl set image deployments/polls-deployment polls-container=anreddy/django-polls:$GIT-SHA
