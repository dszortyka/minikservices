import os
from kservice.colors import bcolors
from prettytable import PrettyTable

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
                # if no namespace provided, stop all services in mikube
                os.system(kill_command)
                os.system(del_file_command)


    if operation == "status":
        show_status(service_list)
    





def print_colored(msg=None):
    print(f"{bcolors.HEADER}{msg}{bcolors.ENDC}")

def print_error(msg=None):
    print(f"{bcolors.FAIL}{msg}{bcolors.ENDC}")




def show_status(service_list=None):
    
    t = PrettyTable(['Namespace', 'Service Name', 'URL'])

    for service in service_list:
        service_name = service.name
        namespace = service.namespace


        tmp_file = f"/tmp/.kservice.{namespace}.{service_name}.out"
        
        if os.path.exists(tmp_file):
            with open(tmp_file, "r") as a_file:
                for line in a_file:
                    stripped_line = line.strip()
                    if "http" in stripped_line:
                        t.add_row([namespace, service_name, stripped_line])
            a_file.close()
        else:
            t.add_row([namespace, service_name, ""])

    print(t)
