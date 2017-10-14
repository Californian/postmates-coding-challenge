import json
import urllib.request

from ordered_geo_services import ordered_geo_services

# convert address to coordinates
def address_to_coords(address):
    status = 999
    coords = []
    i = 0
    num_geo_services = len(ordered_geo_services)

    # until a valid response is received
    while status >= 400 and i < num_geo_services:
        geo_service = ordered_geo_services[i]
        print("trying service: '" + geo_service.service_name + "'")
        # send request to geocoding service
        (status, coords) = geo_service.get_coords(address)
        i += 1

    return coords