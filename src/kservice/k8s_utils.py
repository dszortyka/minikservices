from kubernetes import client, config
from kservice import os_utils



class Service:
    def __init__(self, namespace=None, name=None):
        self.namespace = namespace
        self.name = name

    def start_service(self, all_services=False):
        pass

    def stop_service(self, all_services=False):
        pass




class MK:
    def __init__(self, host=None):
        self.host = None
        self.all_services = []

    def check_cluster(self, host=None):
        try:
            config.load_kube_config()
            return True
        except:
            return False

    def get_services(self, host=None):
        v1 = client.CoreV1Api()
        ret = v1.list_service_for_all_namespaces()
        for i in ret.items:
            if (i.metadata.namespace == "kube-system") or (i.metadata.name == "kubernetes"):    # by default, don't include kubernetes pod or kube-system namespace in the list of services
                continue

            service = Service(namespace=i.metadata.namespace, name=i.metadata.name)
            self.all_services.append(service)

        return self.all_services

    
    def run(self, operation=None, args=None):
        service_list = self.get_services()
        os_utils.run_command(operation, args, service_list)

        