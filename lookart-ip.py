import requests, json, ipaddress

info = ['city', 'region', 'region_code', 'country', 'country_name', 'continent_code', 'in_eu', 'postal', 'latitude', 'longitude', 'latlong', 'timezone', 'utc_offset', 'country_calling_code', 'currency', 'languages', 'asn', 'org', 'all']

class UnknownVariableToLookup(Exception):
	pass

def lookup(ip, info_to_lookup):
	ipaddress.ip_address(ip)
	if info_to_lookup in info:
		if info_to_lookup == "all":
			request = requests.get("https://ipapi.co/{}/json".format(ip))
			return request.json()
		else:
			request = requests.get("https://ipapi.co/{}/{}".format(ip, info_to_lookup)).text
			return request
	else: raise UnknownVariableToLookup("Argument {} is not a valid argument.\nValid arguments: {}.".format(info_to_lookup, ", ".join(info)))
