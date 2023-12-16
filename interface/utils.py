from interface.models import *


def get_features():
    features = Feature.objects.all()
    return features


def get_vendors():
    vendors = Vendor.objects.all()
    return vendors


def get_networks():
    networks = Network.objects.all()
    return networks
