import paho.mqtt.client as mqtt
import json
from sympy import symbols, integrate, csc, log, sqrt, oo
from math import pi


print("--------------------------Question 1!---------SOra ITO-----------------\n")
x = symbols('y')
y = (csc(sqrt(x) + (pi/3)))**2
print('f(x) = {}'.format(y))
y_diff = y.diff(x)
print("f'(x) = {}".format(y_diff))
y_diff2 = y_diff.diff(x)
print("f''(x) = {}".format(y_diff2))
y_diff3 = y_diff2.diff(x)
print("f'''(x) = {}".format(y_diff3))

#Substitution
print("--------------------------Substitution--------------------------")
value = pi/2
sub1 = y_diff.subs(x,value)
sub2 = y_diff2.subs(x,value)
sub3 = y_diff3.subs(x,value)

print("f'({}) = {}".format(value, sub1))
print("f''({}) = {}".format(value, sub2))
print("f'''({}) = {}".format(value, sub3))



#PROTOCOL CONFIG START
host = 'test.mosquitto.org' # URL/ IP toward the MQTT Broker
port = 1883 # Specifies the port toward the MQTT Broker
group = 'calculus2' 
yourname = 'Jirat'
topic = group + '/' + yourname # Topic for data storage
username = '' # AUTHENTICATION username
password = '' # AUTHENTICATION password
# PROTOCOL CONFIG END

client = mqtt.Client() #initialize the connecting gateway to MQTT server
client.username_pw_set(username, password) # Initalize the AUTHENTICATION for the MQTT Broker
client.connect(host, port) #Initalize the MQTT Broker

#Define DATA

data = {}
data['1. f(x)'] = [str(y)]
data["f'(x)"] = [str(y_diff)]
data["f''(x)"] = [str(y_diff2)]
data["f'''(x)"] = [str(y_diff3)]
data['value of a'] = [str(value)]
data["f'(a)"] = [str(sub1)]
data["f''(a)"] = [str(sub2)]
data["f'''(a)"] = [str(sub3)]

data

print("Original Input Data Type: {}".format(type(data)))

data = json.dumps(data)

print('Converted Input Data Type: {}'.format(type(data)))

try:
    client.publish(topic = topic, payload = data, qos = 0, retain = True)
    print('Publication Success!')
    
except:
    print("Publication Failed")


    #Sora Ito 1234567789
        #Sora Ito 1234567789sajdiosajdisajdjojiodasjiodosjdaio