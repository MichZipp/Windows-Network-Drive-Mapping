# Windows-Network-Drive-Mapping
## Discription
Simple tool to automatically map or unmap network drives on a windows machine.
This tool is usefull, if you have a large number of network drives and a large number of windows devices where the network drives have to be mapped.

This tool was tested sucessfully under Python 2.7.14!

## Configuration 
If user authentication is set, the `UserConfig.json` defines the user of the network drive:
```json
{
    "authentication": true,
    "username":"Michael",
    "password":"password"
}
```

The `MappingConfig.json` defines the network drives to map:
```json
{
    "drives":[
        {
            "driveletter":"m",
            "drivefolder":"music"
        },
        {
            "driveletter":"v",
            "drivefolder":"video"
        }
    ]
}
```

## Running
### Mapping
Make sure that the `NetworkDriveMapping.py`, `UserConig.json` and 'MappingConfig' are in the same directory. If not, change the path in the `NetworkDriveMapping.py`. To run the tool just type in the console:
```console
python NetworkDriveMapping.py
```

### Unmapping
To run the tool just type in the console:
```console
python NetworkDriveUnmapping.py
```

## Building
If you want to run this tool on machines without a python installation. You can build stand-alone executables. 
Install `pyinstaller`:
```console
pip install pyinstaller
```
### Mapping
Build stand-alone executables:
```console
pyinstaller NetworkDriveMapping.py
```

### Unmapping
Build stand-alone executables:
```console
pyinstaller NetworkDriveUnmapping.py
```