from GeoService import GeoService

ordered_geo_service_names = [
    "here",
    "google"
]

ordered_geo_services = []

for name in ordered_geo_service_names:
    geo_service = GeoService(name)
    ordered_geo_services.append(geo_service)