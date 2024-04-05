#
#  JavaScript Restrictor is a browser extension which increases level
#  of security, anonymity and privacy of the user while browsing the
#  internet.
#
#  Copyright (C) 2020  Martin Bednar
#  Copyright (C) 2021  Matus Svancar
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

## Module define class which contains variables that are tested.


## Variables about navigator that are checked during testing.
class Navigator:
    def __init__(self,
                 userAgent,
                 appVersion,
                 platform,
                 vendor,
                 language,
                 languages,
                 doNotTrack,
                 cookieEnabled,
                 oscpu,
                 plugins,
                 mimeTypes):
        self.userAgent = userAgent
        self.appVersion = appVersion
        self.platform = platform
        self.vendor = vendor
        self.language = language
        self.languages = languages
        self.doNotTrack = doNotTrack
        self.cookieEnabled = cookieEnabled
        self.oscpu = oscpu
        self.plugins = plugins
        self.mimeTypes = mimeTypes



## Variables about geolocation that are checked during testing.
        
class Geolocation:
    def __init__(self,
                 accuracy,
                 altitude,
                 altitudeAccurac,
                 heading,
                 latitude,
                 longitude,
                 speed,
                 timestamp,
                 valid):
        self.accuracy = accuracy
        self.altitude = altitude
        self.altitudeAccurac = altitudeAccurac
        self.heading = heading
        self.latitude = latitude
        self.longitude = longitude
        self.speed = speed
        self.timestamp = timestamp
        self.valid = valid


## Variables about device that are checked during testing.

class Device:
    def __init__(self,
                 deviceMemory,
                 hardwareConcurrency,
                 IOdevices):
        self.deviceMemory = deviceMemory
        self.hardwareConcurrency = hardwareConcurrency
        self.IOdevices = IOdevices


class Audio:
    def __init__(self,
                 get_channel,
                 get_channel2,
                 copy_channel,
                 copy_channel2,
                 byte_time_domain,
                 float_time_domain,
                 byte_frequency,
                 float_frequency):
        self.get_channel = get_channel
        self.get_channel2 = get_channel2
        self.copy_channel = copy_channel
        self.copy_channel2 = copy_channel2
        self.byte_time_domain = byte_time_domain
        self.float_time_domain = float_time_domain
        self.byte_frequency = byte_frequency
        self.float_frequency = float_frequency
## Variables about audio that are checked during testing.

## All variables that are checked during testing.
class TestedValues:
    def __init__(self,
                 addons=None,
                 userAgent=None,
                 appVersion=None,
                 platform=None,
                 vendor=None,
                 language=None,
                 languages=None,
                 doNotTrack=None,
                 cookieEnabled=None,
                 oscpu=None,
                 plugins=None,
                 mimeTypes=None,

                 gpsAccuracy=None,
                 altitude=None,
                 altitudeAccurac=None,
                 heading=None,
                 latitude=None,
                 longitude=None,
                 speed=None,
                 timestamp=None,
                 valid=None,

                 deviceMemory=None,
                 hardwareConcurrency=None,
                 IOdevices=None,

                 get_channel=None,
                 get_channel2=None,
                 copy_channel=None,
                 copy_channel2=None,
                 byte_time_domain=None,
                 float_time_domain=None,
                 byte_frequency=None,
                 float_frequency=None,
 

                 time=None,
                 performance=None,
                 protectCanvas=None,

                 canvasImageData=None,
                 canvasDataURL=None,
                 canvasBlob=None,
                 canvasPointPath=None,
                 canvasPointStroke=None,

                 webglParameters=None,
 
                 webglPrecisions=None,
                 webglPixels=None,
                 webglDataURL=None,

                 worker=None,

                 methods_toString=None,

                 ECMAarrays=None

                 ):
        self.addons = addons
        self.navigator = Navigator(
            userAgent,
            appVersion,
            platform,
            vendor,
            language,
            languages,
            doNotTrack,
            cookieEnabled,
            oscpu,
            plugins,
            mimeTypes
        )
        self.geolocation = Geolocation(
            gpsAccuracy,
            altitude,
            altitudeAccurac,
            heading,
            latitude,
            longitude,
            speed,
            timestamp,
            valid
        )
        self.device = Device(
            deviceMemory,
            hardwareConcurrency,
            IOdevices
        )

        self.audio = Audio(
            get_channel,
            get_channel2,
            copy_channel,
            copy_channel2,
            byte_time_domain,
            float_time_domain,
            byte_frequency,
            float_frequency
        )

        self.time = time
        self.performance = performance
        self.protectCanvas = protectCanvas
        self.canvasImageData = canvasImageData
        self.canvasDataURL = canvasDataURL
        self.canvasBlob = canvasBlob
        self.canvasPointPath = canvasPointPath
        self.canvasPointStroke = canvasPointStroke
        self.webglParameters = webglParameters
        self.webglPrecisions = webglPrecisions
        self.webglPixels = webglPixels
        self.webglDataURL = webglDataURL
        self.worker = worker
        self.methods_toString = methods_toString
        self.ECMAarrays = ECMAarrays

