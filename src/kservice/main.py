import sys
from kservice.k8s_utils import MK
from kservice.arguments import parse_arguments, return_argument, check_arguments, check_input_arguments
from kservice.os_utils import print_colored, print_error




def main():
    
    minikube = MK()

    # Check if minikube cluster is running
    if minikube.check_cluster() is False:
        print("Minikube is not running. Exit.")
        exit(0)
    
    # parse arguments
    arguments = parse_arguments()
    args = vars(arguments.parse_args())

    if check_arguments(args) is False:
        print_error("Please, select only one operation.")
        exit(1)

    #if check_input_arguments(args) is False:
    #    print_error("Please, use either \',\' or \' \' to provide the service list.")
    #    exit(1)

    # get operation to be executed
    operation = return_argument(args)

    # if no arguments, just print the usage and available services
    if len(sys.argv) == 1:
        arguments.print_help()

    # run app with required operation
    minikube.run(operation, args)




    
    





    
if __name__ == "__main__":
    main()