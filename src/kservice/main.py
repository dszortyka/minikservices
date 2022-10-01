""" main """
import sys
from kservice.k8s_utils import MK
from kservice.arguments import parse_arguments, return_operation, check_arguments
from kservice.os_utils import print_colored, print_error


def main():
    """ main """
    
    minikube = MK()

    if minikube.check_cluster() is False:
        print_error("Minikube is not running. Exit.")
        exit(0)
    
    arguments = parse_arguments()
    args = vars(arguments.parse_args())

    if check_arguments(args) is False:
        print_error("Please, select only one operation.")
        exit(1)

    if len(sys.argv) == 1:
        arguments.print_help()

    operation = return_operation(args)
    minikube.run(operation, args)


if __name__ == "__main__":
    main()