""" Utils module to run OS commands
"""
import os
from kservice.colors import bcolors
from prettytable import PrettyTable


def run_command(operation=None, args=None, service_list=None):
    """ run a specific command based on its operation (start/stop/etc..) """

    if operation == "start":
        required_services = ""

        # check if required service list contains , as separator
        if ',' in args['start'][0]:
            required_services = str(args['start'][0]).split(',')
        else:
            required_services = args['start']

        for service in service_list:
            if (args['namespace'] is False):
                if service.name in required_services:
                    command = f"nohup minikube service {service.name} --url -n {service.namespace} > /tmp/.kservice.{service.namespace}.{service.name}.out 2>&1 &"
                    os.system(command)
            else:
                if (service.name in required_services) and (args['namespace'] == service.namespace):
                    command = f"nohup minikube service {service.name} --url -n {service.namespace} > /tmp/.kservice.{service.namespace}.{service.name}.out 2>&1 &"
                    os.system(command)


    if operation == "stop":
        required_services = ""

        if ',' in args['stop'][0]:
            required_services = str(args['stop'][0]).split(',')
        else:
            required_services = args['stop']

        for service in service_list:
            kill_command = f"pgrep -f \"minikube service {service.name} --url -n {service.namespace}\"|xargs kill -9"
            del_file_command = f"rm -f /tmp/.kservice.{service.namespace}.{service.name}.out"
            if (args['namespace'] is False):
                if service.name in required_services:
                    os.system(kill_command)
                    os.system(del_file_command)
            else:
                if (service.name in required_services) and (args['namespace'] == service.namespace):
                    os.system(kill_command)
                    os.system(del_file_command)


    if operation == "startall":
        for service in service_list:
            command = f"nohup minikube service {service.name} --url -n {service.namespace} > /tmp/.kservice.{service.namespace}.{service.name}.out 2>&1 &"
            
            # check if a specific namespace has been provided
            if (args['namespace'] is not False):
                if (args['namespace'] == service.namespace):
                    os.system(command)
            else:
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
