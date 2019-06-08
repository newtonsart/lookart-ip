import requests, json

def city(ip):
	return requests.get("https://ipapi.co/" + ip + "/city").text

def postal(ip):
	return requests.get("https://ipapi.co/" + ip + "/postal").text
	
def isprov(ip):
	return requests.get("https://ipapi.co/" + ip + "/org").text

def latlong(ip):
	return requests.get("https://ipapi.co/" + ip + "/latlong").text

def country(ip):
	return requests.get("https://ipapi.co/" + ip + "/country").text

def region(ip):
	return requests.get("https://ipapi.co/" + ip + "/region").text

def currency(ip):
	return requests.get("https://ipapi.co/" + ip + "/currency").text

def region_code(ip):
	return requests.get("https://ipapi.co/" + ip + "/region_code").text

def country_name(ip):
	return requests.get("https://ipapi.co/" + ip + "/country_name").text

def continent_code(ip):
	return requests.get("https://ipapi.co/" + ip + "/continent_code").text

def latitude(ip):
	return requests.get("https://ipapi.co/" + ip + "/latitude").text

def longitude(ip):
	return requests.get("https://ipapi.co/" + ip + "/longitude").text

def timezone(ip):
	return requests.get("https://ipapi.co/" + ip + "/timezone").text

def country_calling_code(ip):
	return requests.get("https://ipapi.co/" + ip + "/country_calling_code").text

def all(ip):
	request = requests.get("https://ipapi.co/" + ip + "/json").text
	all_dictionary = json.loads(request)
	return all_dictionary