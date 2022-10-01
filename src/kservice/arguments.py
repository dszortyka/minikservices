""" Module used to parse and check arguments
"""
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(prog='PROG')
    
    group1=parser.add_argument_group("Start/Stop")
    group2=parser.add_argument_group("Startall/Stopall")

    group1.add_argument("--start", help='Start one or more services separated by \',\' or space', nargs='+', default=False)
    group1.add_argument('--stop', help='Stop one or more services separated by \',\' or space', nargs='+', default=False)

    group2.add_argument('--startall', help='Start all services', action='store_true', default=False)
    group2.add_argument('--stopall', help='Stop all services', action='store_true', default=False)
    
    
    parser.add_argument('--status', help='Show current service status', action='store_true', default=False)
    parser.add_argument('-n','--namespace', help='Specificy --namespace', default=False)

    return parser


def check_arguments(args):
    """ Run over the arguments namespace
        If more than 1 argument is True, return False
        We expect only one argument like stop or start, etc. 
    """
    count=0
    for arg in args:
        # don't take into consideration argument namespace
        if arg == 'namespace':
            continue

        if args[arg] is not False:
            count+=1
    
    if count > 1:
        return False

    return True


def return_operation(args):
    """ Since only one argument is expected and previously validated
        This function will return the first argument that is True
        It should be either start, stop, status, startall or stopall
    """
    for arg in args:
        if args[arg] is not False:
            return arg
    