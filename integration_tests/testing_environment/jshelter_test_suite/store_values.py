import json
import os
from values_tested import TestedValues

def read_browsers(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        browsers = data.get('browsers', [])
        browser_dict = {browser: [] for browser in browsers}
        return browser_dict

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


def create_browser_data():
    results = os.listdir('/usr/app/src/fingerprinting_server/outputs')
    browsers_tested = read_browsers('/usr/app/src/client_simulator/example_configs/client.json')

    jshelter_tested = False

    for file_name in results:
                if "log--" in file_name:
                    split = file_name.split('_')
                    browser = split[1]

                    if "None" in split:
                        browsers_tested[browser].insert(0, file_name)
                    if "JSc=0" in split or "JSf=0" in split or "JSc=1" in split or "JSf=1" in split or "JSc=2" in split or "JSf=2" in split or "JSc=3" in split or "JSf=3" in split:
                        jshelter_tested = True
                        browsers_tested[browser] += [file_name]

    
    if not jshelter_tested:
        return False

    for browser, values in browsers_tested.items():
       
        noaddon = '/usr/app/src/fingerprinting_server/outputs/' + values[0]
        testedNoaddon = read_data(noaddon)
        browsers_tested[browser][0] = testedNoaddon

        for value in values[1:]:
            jsaddon = '/usr/app/src/fingerprinting_server/outputs/' + value
            testedJS = read_data(jsaddon)
            browsers_tested[browser][values.index(value)] = testedJS
          
    return browsers_tested
