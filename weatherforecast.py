'''
Weather forecast with Python
'''

#import the necessary package!
import requests

#input the city name
city = input('input the city name: ')
print(city)

# or you can also hard-code the value
# city = 'nellore'

#Display the message!
print('Displaying Weather report for: ' + city)

#fetch the weater details
url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)

#display the result!
print(res.text)
