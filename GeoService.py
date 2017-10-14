from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import URLError
import json

class GeoService:

    """
    provides a standardized interface for retrieval of geographic coordinates
    from an external API
    """

    def get_raw_coord_res(self, address):
        """
        default means of requesting coordinates from an external API

        assumes address is a query parameter
        """

        query_params = self.api_key_params

        # add address to query params
        query_params[self.address_query_name] = address

        # construct URL from base URL and query parameters
        query_str       = "?" + urlencode(query_params)
        constructed_url = self.base_url + query_str
        
        # get response from API
        res = urlopen(constructed_url)
        
        return res
        
    def parse_coord_res(self, res):
        encoding   = res.info().get_content_charset("utf-8")
        res_code   = res.getcode()
        coord_data = res.read()
        coords     = json.loads(coord_data.decode(encoding))
        for key in self.coord_obj_keys:
            if type(key) != list:
                try:
                    coords = coords[key]
                except IndexError:
                    return [400, []]
                except KeyError:
                    return [400, []]
                
        coords = [coords[key[0]], coords[key[1]]]

        return [res_code, coords]

    def get_coords(self, address):
        """
        uses given functions to request coordinates and parse response to
        return a tuple with the coordinates for given address
        """

        try:
            raw_coord_res = self.get_raw_coord_res(address)
            coord_data    = self.parse_coord_res(raw_coord_res)
        except URLError:
            return [404, []]
        
        return coord_data

    def __init__(self, service_name):
        self.service_name = service_name

        # get base URL and address query parameter name from config file
        with open("config.json", "r") as config_file:
            config                  = json.loads(config_file.read())
            service_config          = config[self.service_name]
            self.base_url           = service_config["base_url"]
            self.address_query_name = service_config["address_query_name"]
            self.coord_obj_keys     = service_config["coord_obj_keys"]

        # get API key from secrets file
        with open("config.secret.json", "r") as secrets_file:
            secrets             = json.loads(secrets_file.read())
            service_secrets     = secrets[self.service_name]
            self.api_key_params = service_secrets["api_key_params"]