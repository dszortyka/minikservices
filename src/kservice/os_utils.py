import os
from kservice.colors import bcolors

# minikube service argocd-server --url -n argocd
def run_command(operation=None, args=None, service_list=None):


    

    #os.system("nohup minikube service argocd-server --url -n argocd > /tmp/argocd.out 2>&1 &")
    # ps aux|egrep "minikube service argocd-server --url -n argocd"|egrep -v egrep|awk '{print $2}'|xargs kill -9
    # pgrep -f "minikube service simple-flask-app --url -n flaskapp"|xargs kill -9
    if operation == "start":
        pass
    if operation == "stop":
        print("running stop operation")
    if operation == "startall":
        for service in service_list:
            command = f"nohup minikube service {service.name} --url -n {service.namespace} > /tmp/.kservice.{service.namespace}.{service.name}.out 2>&1 &"
            # check if a specific namespace has been provided
            if (args['namespace'] is not False):
                if (args['namespace'] == service.namespace):
                    os.system(command)
                    continue
            else:
                # if no namespace provided, start all services              
                os.system(command)
                


    if operation == "stopall":
        for service in service_list:
            kill_command = f"pgrep -f \"minikube service {service.name} --url -n {service.namespace}\"|xargs kill -9"
            del_file_command = f"rm -f /tmp/.kservice.{service.namespace}.{service.name}.out"

            if (args['namespace'] is not False):
                if (args['namespace'] == service.namespace):
                    os.system(kill_command)
                    os.system(del_file_command)
                    continue
            else:
                # if no namespace provided, stop all services
                os.system(kill_command)
                os.system(del_file_command)


    if operation == "status":
        print("show status")
    


def delete_tmp_file(name=None, namespace=None):
    kill_command = f"pgrep -f \"minikube service {name} --url -n {namespace}\"|xargs kill -9"
    del_file_command = f"rm -f /tmp/.kservice.{namespace}.{name}.out"
    try:
        os.system(kill_command)
    except:
        print("Failed to kill the process.")
    
    try:
        os.system(del_file_command)
    except:
        print("Failed to delete temp file.")


def print_colored(msg=None):
    print(f"{bcolors.HEADER}{msg}{bcolors.ENDC}")

def print_error(msg=None):
    print(f"{bcolors.FAIL}{msg}{bcolors.ENDC}")