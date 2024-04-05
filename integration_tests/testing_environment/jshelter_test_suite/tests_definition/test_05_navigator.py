#
#  JShelter is a browser extension which increases level
#  of security, anonymity and privacy of the user while browsing the
#  internet.
#
#  Copyright (C) 2021  Matus Svancar
#  Copyright (C) 2022  Martin Bednar
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


## Setup method - it is run before navigator tests execution starts.
#
#  This setup method initialize variable navigator that contains current data about navigator and
#  this variable is provided to navigator tests and values in device variable are compared with expected values.
#pytest.fixture(scope='module', autouse=True)
#def noaddon_navigator(run):
#    return get_navigator(run)

#@pytest.fixture(scope='module', autouse=True)
##def jshelter_navigator(run):
#    return get_navigator(run)


## Test user agent.
def test_user_agent(noaddon, jsrun, browser, expected):
    if expected.navigator.userAgent[browser] == 'REAL VALUE':
        assert jsrun.navigator.userAgent == noaddon.navigator.userAgent
    else:
        assert jsrun.navigator.userAgent == expected.navigator.userAgent[browser]

def test_app_version(noaddon, jsrun, expected):
    if expected.navigator.appVersion == 'REAL VALUE':
        assert jsrun.navigator.appVersion == noaddon.navigator.appVersion
    else:
        assert jsrun.navigator.appVersion == expected.navigator.appVersion

	
def test_platform(noaddon, jsrun, expected):
    if expected.navigator.platform == 'REAL VALUE':
        assert jsrun.navigator.platform == noaddon.navigator.platform
    else:
        assert jsrun.navigator.platform == expected.navigator.platform

def test_vendor(noaddon, jsrun, browser, expected):
    if expected.navigator.vendor[browser] == 'REAL VALUE':
        assert jsrun.navigator.vendor == noaddon.navigator.vendor
    else:
        assert jsrun.navigator.vendor == expected.navigator.vendor[browser]

def test_language(noaddon, jsrun, expected):
    if expected.navigator.language  == 'REAL VALUE':
        assert jsrun.navigator.language == noaddon.navigator.language 
    else:
        assert jsrun.navigator.language == expected.navigator.language 

def test_languages(noaddon, jsrun, expected):
    if expected.navigator.languages  == 'REAL VALUE':
        assert jsrun.navigator.languages == noaddon.navigator.languages 
    else:
        assert jsrun.navigator.languages == expected.navigator.languages 

def test_cookie_enabled(noaddon, jsrun, expected):
    if expected.navigator.cookieEnabled  == 'REAL VALUE':
        assert jsrun.navigator.cookieEnabled == noaddon.navigator.cookieEnabled 
    else:
        assert jsrun.navigator.cookieEnabled == expected.navigator.cookieEnabled 

def test_do_not_track(noaddon, jsrun, expected):
    if expected.navigator.doNotTrack == 'REAL VALUE':
        assert jsrun.navigator.doNotTrack == noaddon.navigator.doNotTrack  
    else:
        assert jsrun.navigator.doNotTrack == expected.navigator.doNotTrack 

def test_oscpu(noaddon, jsrun, expected):
    if expected.navigator.oscpu == 'REAL VALUE':
        assert jsrun.navigator.oscpu == noaddon.navigator.oscpu   
    else:
        assert jsrun.navigator.oscpu == expected.navigator.oscpu  

	
LIVING_STANDARD_PLUGINS = [
            {'description': 'Portable Document Format', 'filename': 'internal-pdf-viewer', 'name': 'PDF Viewer'},
            {'description': 'Portable Document Format', 'filename': 'internal-pdf-viewer', 'name': 'Chrome PDF Viewer'},
            {'description': 'Portable Document Format', 'filename': 'internal-pdf-viewer', 'name': 'Chromium PDF Viewer'},
            {'description': 'Portable Document Format', 'filename': 'internal-pdf-viewer', 'name': 'Microsoft Edge PDF Viewer'},
            {'description': 'Portable Document Format', 'filename': 'internal-pdf-viewer', 'name': 'WebKit built-in PDF'},
        ]

	
def test_plugins_count(noaddon, jsrun, browser, expected):
    if jsrun.navigator.plugins == LIVING_STANDARD_PLUGINS and noaddon.navigator.plugins == LIVING_STANDARD_PLUGINS:
        return # JShelter should not modify the plugins that are the same in all conformant browsers
    if expected.navigator.plugins['count'][browser] == 'IGNORE':
        return
    elif expected.navigator.plugins['count'][browser] == 'REAL VALUE':
        assert len(jsrun.navigator.plugins) == len(noaddon.navigator.plugins)
    elif expected.navigator.plugins['count'][browser] == 'PLUS_2':
        assert len(jsrun.navigator.plugins) == len(noaddon.navigator.plugins) + 2
    else:
        assert len(jsrun.navigator.plugins) == expected.navigator.plugins['count'][browser]

	
def test_plugins(noaddon, jsrun, browser, expected):
    if jsrun.navigator.plugins == LIVING_STANDARD_PLUGINS and noaddon.navigator.plugins == LIVING_STANDARD_PLUGINS:
        return # JShelter should not modify the plugins that are the same in all conformant browsers
    if expected.navigator.plugins['count'][browser] == 'IGNORE':
        return
    elif expected.navigator.plugins['count'][browser] == 'REAL VALUE':
        assert jsrun.navigator.plugins == noaddon.navigator.plugins
    elif expected.navigator.plugins['value'][browser] == 'EMPTY':
        assert not jsrun.navigator.plugins
    else:
        assert jsrun.navigator.plugins != noaddon.navigator.plugins

	
LIVING_STANDARD_MIME_TYPES = [
            {'description': 'Portable Document Format', 'enabledPlugin': 'PDF Viewer', 'suffixes':
             'pdf', 'type': 'application/pdf'},
            {'description': 'Portable Document Format', 'enabledPlugin': 'PDF Viewer', 'suffixes':
             'pdf', 'type': 'text/pdf'},
        ]

def test_mime_types(noaddon, jsrun, expected):
    if jsrun.navigator.mimeTypes == LIVING_STANDARD_MIME_TYPES and noaddon.navigator.mimeTypes == LIVING_STANDARD_MIME_TYPES:
        return # JShelter should not modify the plugins that are the same in all conformant browsers
    if expected.navigator.mimeTypes == 'IGNORE':
        return
    elif expected.navigator.mimeTypes == 'EMPTY':
        assert jsrun.navigator.mimeTypes == []
    elif expected.navigator.mimeTypes == 'SPOOF VALUE':
        if noaddon.navigator.mimeTypes == []:
            assert jsrun.navigator.mimeTypes == []
        else:
            assert jsrun.navigator.mimeTypes != noaddon.navigator.mimeTypes
    else:
        assert jsrun.navigator.mimeTypes == noaddon.navigator.mimeTypes


## Test app version.
