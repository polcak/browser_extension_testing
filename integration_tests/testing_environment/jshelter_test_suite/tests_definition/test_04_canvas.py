#
#  JShelter is a browser extension which increases level
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

## Test canvas - if canvas is spoofed: Reading from canvas returns white image.
##
## This test fails in Google Chrome on JShelter level 3 - expected failure because of known bug:
## selenium.common.exceptions.JavascriptException: Message: javascript error:
## Failed to execute 'getRandomValues' on 'Crypto': parameter 1 is not of type 'ArrayBufferView'.
def test_canvas(jsrun, expected):
    is_spoofed = jsrun.protectCanvas
    if is_spoofed == "ERROR":
        print("\nCan not read Canvas data.")
        assert False
    else:
        if expected.protectCanvas == True:
            assert is_spoofed ==  True
        else:
            assert is_spoofed ==  False

def test_getImageData(noaddon, jsrun, expected):
    if jsrun.canvasImageData == "ERROR":
        print("\n getImageData error.")
        assert False
    else:
        if expected.canvasImageData == 'SPOOF VALUE':
            assert jsrun.canvasImageData != noaddon.canvasImageData
        else:
            assert jsrun.canvasImageData == noaddon.canvasImageData


def test_to_data_URL(noaddon, jsrun, expected):
    if jsrun.canvasDataURL == "ERROR":
        print("\n toDataURL error.")
        assert False
    else:
        if expected.canvasDataURL == 'SPOOF VALUE':
            assert jsrun.canvasDataURL != noaddon.canvasDataURL
        else:
            assert jsrun.canvasDataURL == noaddon.canvasDataURL


def test_to_blob(noaddon, jsrun, expected):
    if jsrun.canvasBlob == "ERROR":
        print("\n toBlob error.")
        assert False
    else:
        if expected.canvasBlob == 'SPOOF VALUE':
            assert jsrun.canvasBlob != noaddon.canvasBlob
        else:
            assert jsrun.canvasBlob == noaddon.canvasBlob

def test_is_point_in_path(jsrun, expected):
    if jsrun.canvasPointPath == "ERROR":
        print("\n isPointInPath error.")
        assert False
    else:
        if expected.canvasPointPath in {'SPOOF VALUE','FALSE VALUE'}:
            assert jsrun.canvasPointPath == False
        else:
            assert jsrun.canvasPointPath == True

def test_is_point_in_stroke(jsrun, expected):
    if jsrun.canvasPointStroke == "ERROR":
        print("\n isPointInStroke error.")
        assert False
    else:
        if expected.canvasPointStroke in {'SPOOF VALUE','FALSE VALUE'} :
            assert jsrun.canvasPointStroke == False
        else:
            assert jsrun.canvasPointStroke == True