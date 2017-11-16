import subprocess, json

print('Mapping Started!')

with open('MappingConfig.json') as mappingConfig:    
    mapping = json.load(mappingConfig)

with open('UserConfig.json') as userConfig:    
    user = json.load(userConfig)
    authentication = user['authentication']
    if(authentication == True):
        username = user['username']
        password = user['password']

for drive in mapping['drives']:
    letter = drive['driveletter']
    folder = drive['drivefolder']
    if(authentication == True):
         print('net use ' + letter + ': ' + folder + ' /user:' + username + ' ' + password)
        # Connect to shared drive, use drive letter M
        # subprocess.call(r'net use ' + letter + ': ' + folder + ' /user:' + username + ' ' + password, shell=True)
    else:
         print('net use ' + letter + ': ' + folder)
        # Connect to shared drive, use drive letter M
        # subprocess.call(r'net use ' + letter + ': ' + folder, shell=True)

print('Mapping Finished!')

