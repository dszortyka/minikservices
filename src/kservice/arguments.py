import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(prog='PROG')
    
    group1=parser.add_argument_group("Start/Stop")
    group2=parser.add_argument_group("Startall/Stopall")

    group1.add_argument("--start", help='Start one or more services separated by \',\'', nargs='+', default=False)
    group1.add_argument('--stop', help='Stop one or more services separated by \',\'', nargs='+', default=False)

    group2.add_argument('--startall', help='Start all services', action='store_true', default=False)
    group2.add_argument('--stopall', help='Stop all services', action='store_true', default=False)
    
    
    parser.add_argument('--status', help='Show current service status', action='store_true', default=False)
    parser.add_argument('-n','--namespace', help='Specificy --namespace', default=False)

   
    return parser


def check_input_arguments(args):
    ''' function to validate if START or STOP action
        contains only ',' or ' ' to separate the list of services
    '''
    operation = return_argument(args)

    print("Check input parameters for: ", args[operation])

    if (str(args[operation]).find(',')):
        print("Service list splited by ,")


    return True


def check_arguments(args):
    ''' Run over the arguments namespace
        If more than 1 parameters is True, return False
        We expect only one parameter to be true
    '''
    count=0
    for arg in args:
        if arg == 'namespace':  # don't take into consideration if argument contains --namespace
            continue
        if args[arg] is not False:
            count+=1
    
    if count > 1:
        return False

    return True


def return_argument(args):
    for arg in args:
        if args[arg] is not False:
            return arg
    