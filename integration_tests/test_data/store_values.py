import json
import os
from values_tested import TestedValues

def read_browsers(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        testing = data.get('integration_testing')
        if not testing:
             return False
        else:
            return True


def read_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        navigator = data.get('navigator', {})
        geolocation = data.get('geolocation', {})
        device = data.get('device', {})
        audio = data.get('audio', {})
        canvas = data.get('canvas', {})
        webgl = data.get('WebGL', {})


        test_case = TestedValues(data.get('_pet'),
                                 navigator.get('userAgent'),
                                 navigator.get('appVersion'),
                                 navigator.get('platform'),
                                 navigator.get('vendor'),
                                 navigator.get('language'),
                                 navigator.get('languages'),
                                 navigator.get('doNotTrack'),
                                 navigator.get('cookieEnabled'),
                                 navigator.get('oscpu'),
                                 navigator.get('plugins'),
                                 navigator.get('mimeTypes'),

                                 geolocation.get('accuracy'),
                                 geolocation.get('altitude'),
                                 geolocation.get('altitudeAccuracy'),
                                 geolocation.get('heading'),
                                 geolocation.get('latitude'),
                                 geolocation.get('longitude'),
                                 geolocation.get('speed'),
                                 geolocation.get('timestamp'),
                                 geolocation.get('valid'),

                                 device.get('deviceMemory'),
                                 device.get('hardwareConcurrency'),
                                 data.get('io_devices'),

                                 audio.get('channelDataResult'),
                                 audio.get('channelDataResult2'),
                                 audio.get('copyResult'),
                                 audio.get('copyResult2'),
                                 
                                 audio.get('byteFrequencyResult'),
                                 audio.get('floatFrequencyResult'),                                 
                                 audio.get('byteTimeResult'),
                                 audio.get('floatTimeResult'),

                                 data.get('time'),
                                 data.get('performance'),
                                 canvas.get('spoof'),

                                 canvas.get('imageData'),
                                 canvas.get('dataURL'),
                                 data.get('canvas_blob'),
                                 canvas.get('pointInPath'),
                                 canvas.get('pointInStroke'),

                                 data.get('WebGL'),
                                 webgl.get('webGLpercisions'), 
                                 webgl.get('webGLpixels'),
                                 webgl.get('webGLdataURL'),

                                 data.get('worker'),
                                 
                                 data.get('methodsToString'),
                                 data.get('ECMAarrays')
                                 )
        return test_case
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format.")
    except Exception as e:
        print("An error occurred:", e)


def create_browser_data(subfolder):

    results = os.path.join('/usr/app/src/fingerprinting_server/outputs', subfolder)
    
    start_testing = read_browsers('/usr/app/src/client_simulator/example_configs/client.json')

    if not start_testing:
         return False
    
    testing_data = []

    for filename in os.listdir(results):
        if "None" in filename:
            testing_data.insert(0, read_data(results + "/" + filename))
        else: 
            testing_data.append(read_data(results + "/" + filename))

    return testing_data
