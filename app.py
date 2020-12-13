import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

with open('data.json') as json_file:
    data = json.load(json_file)
    for p in data['plugins']:
        print('Pluginname: ' + p['pluginname'])
        url =  p['url_ending']
        url_new = 'https://api.wordpress.org/plugins/info/1.0/' + url + '.json'
        #print(url_new)
        response = requests.get(url_new)
        #print(response.status_code)
        print(response.json()['version'])  
        print()
