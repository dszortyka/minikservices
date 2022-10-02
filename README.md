# Minikube Services

__minikservices__ is a small and very simple python project that aims to help with the start and stop of __Minikube__ services.

Instead of creating multiple terminal tabs to expose minikube services, you can use __kservice__ command line tool to start and stop services. It will also display the exposed services and its addresses. 


## Build/Dev local
```
git clone https://github.com/dszortyka/minikservices.git
cd minikservices
python3 -m venv .pyenv
source .pyenv/bin/activate
pip install -r requirements.txt
pip install . 
kservice -h
```

## Python Package (PyPI)
```
pip install minikservices
```


## Usage
```
kservice --start service1 service2
kservice --start service1 service2 -n namespace

kservice --stop service1 service2
kservice --stop service1 service2 -n namespace

kservice --startall
kservice --stopall

kservice --status
```

## How it works
* The application will start the minikube service in background and store and temp file in /tmp folder. 
* If you have an Application deployed in two different namespaces and run the __--start__ operation without specifying the -n (namespace), it will start the application on both namespaces. The same is valid for __--stop__
* __--startall__ and __--stopall__ works in the same way, it will start all services in all namespaces unless you specify which __-n__ (namespace) in want. 
* __--status__ will print a table with service names, namespace and the current URL for the exposed services. 

```
❯ kservice --start simple-flask-app

❯ kservice --status
+-----------+-----------------------------------------+------------------------+
| Namespace |               Service Name              |          URL           |
+-----------+-----------------------------------------+------------------------+
|   argocd  |     argocd-applicationset-controller    |                        |
|   argocd  |            argocd-dex-server            |                        |
|   argocd  |              argocd-metrics             |                        |
|   argocd  | argocd-notifications-controller-metrics |                        |
|   argocd  |               argocd-redis              |                        |
|   argocd  |            argocd-repo-server           |                        |
|   argocd  |              argocd-server              |                        |
|   argocd  |          argocd-server-metrics          |                        |
|  default  |             simple-flask-app            | http://127.0.0.1:64888 |
|  flaskapp |             simple-flask-app            | http://127.0.0.1:64885 |
+-----------+-----------------------------------------+------------------------+
```