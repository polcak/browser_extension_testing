#
#  JShelter is a browser extension which increases level
#  of security, anonymity and privacy of the user while browsing the
#  internet.
#
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

# Test WebGLRenderingContext.getParameter for unmaskedVendor
def test_unmasked_vendor(noaddon, jsrun, expected):
    if expected.webglParameters == 'REAL VALUE':
        assert jsrun.webglParameters['webglVendor'] == noaddon.webglParameters['webglVendor']
    else:
        if jsrun.webglParameters['webglVendor'] == noaddon.webglParameters['webglVendor']:
            assert jsrun.webglParameters['webglVendor'] == ""
        else:
            assert True

# Test WebGLRenderingContext.getParameter for unmaskedRenderer
def test_unmasked_renderer(noaddon, jsrun, expected):
    if expected.webglParameters == 'REAL VALUE':
        assert jsrun.webglParameters['webglRenderer'] == noaddon.webglParameters['webglRenderer']
    else:
        assert jsrun.webglParameters['webglRenderer'] != noaddon.webglParameters['webglRenderer']

# Test WebGLRenderingContext.getParameter
def test_other_parameters(noaddon, jsrun, expected):
    if expected.webglParameters == 'SPOOF VALUE':
        spoof_sum = 0
        if noaddon.webglParameters['maxVertexUniformComponents'] != None:
            assert 0 <= jsrun.webglParameters['maxVertexUniformComponents'] <= noaddon.webglParameters['maxVertexUniformComponents']
            spoof_sum += noaddon.webglParameters['maxVertexUniformComponents'] - jsrun.webglParameters['maxVertexUniformComponents']
        if noaddon.webglParameters['maxVertexUniformBlocks'] != None:
            assert 0 <= jsrun.webglParameters['maxVertexUniformBlocks'] <= noaddon.webglParameters['maxVertexUniformBlocks']
            spoof_sum += noaddon.webglParameters['maxVertexUniformBlocks'] - jsrun.webglParameters['maxVertexUniformBlocks']
        if noaddon.webglParameters['maxVertexOutputComponents'] != None:
            assert 0 <= jsrun.webglParameters['maxVertexOutputComponents'] <= noaddon.webglParameters['maxVertexOutputComponents']
            spoof_sum += noaddon.webglParameters['maxVertexOutputComponents'] - jsrun.webglParameters['maxVertexOutputComponents']
        if noaddon.webglParameters['maxVaryingComponents'] != None:
            assert 0 <= jsrun.webglParameters['maxVaryingComponents'] <= noaddon.webglParameters['maxVaryingComponents']
            spoof_sum += noaddon.webglParameters['maxVaryingComponents'] - jsrun.webglParameters['maxVaryingComponents']
        if noaddon.webglParameters['maxTransformFeedbackInterleavedComponents'] != None:
            assert 0 <= jsrun.webglParameters['maxTransformFeedbackInterleavedComponents'] <= noaddon.webglParameters['maxTransformFeedbackInterleavedComponents']
            spoof_sum += noaddon.webglParameters['maxTransformFeedbackInterleavedComponents'] - jsrun.webglParameters['maxTransformFeedbackInterleavedComponents']
        if noaddon.webglParameters['maxFragmentUniformComponents'] != None:
            assert 0 <= jsrun.webglParameters['maxFragmentUniformComponents'] <= noaddon.webglParameters['maxFragmentUniformComponents']
            spoof_sum += noaddon.webglParameters['maxFragmentUniformComponents'] - jsrun.webglParameters['maxFragmentUniformComponents']
        if noaddon.webglParameters['maxFragmentUniformBlocks'] != None:
            assert 0 <= jsrun.webglParameters['maxFragmentUniformBlocks'] <= noaddon.webglParameters['maxFragmentUniformBlocks']
            spoof_sum += noaddon.webglParameters['maxFragmentUniformBlocks'] - jsrun.webglParameters['maxFragmentUniformBlocks']
        if noaddon.webglParameters['maxFragmentInputComponents'] != None:
            assert 0 <= jsrun.webglParameters['maxFragmentInputComponents'] <= noaddon.webglParameters['maxFragmentInputComponents']
            spoof_sum += noaddon.webglParameters['maxFragmentInputComponents'] - jsrun.webglParameters['maxFragmentInputComponents']
        if noaddon.webglParameters['maxUniformBufferBindings'] != None:
            assert 0 <= jsrun.webglParameters['maxUniformBufferBindings'] <= noaddon.webglParameters['maxUniformBufferBindings']
            spoof_sum += noaddon.webglParameters['maxUniformBufferBindings'] - jsrun.webglParameters['maxUniformBufferBindings']
        if noaddon.webglParameters['maxCombinedUniformBlocks'] != None:
            assert 0 <= jsrun.webglParameters['maxCombinedUniformBlocks'] <= noaddon.webglParameters['maxCombinedUniformBlocks']
            spoof_sum += noaddon.webglParameters['maxCombinedUniformBlocks'] - jsrun.webglParameters['maxCombinedUniformBlocks']
        if noaddon.webglParameters['maxCombinedVertexUniformComponents'] != None:
            assert 0 <= jsrun.webglParameters['maxCombinedVertexUniformComponents'] <= noaddon.webglParameters['maxCombinedVertexUniformComponents']
            spoof_sum += noaddon.webglParameters['maxCombinedVertexUniformComponents'] - jsrun.webglParameters['maxCombinedVertexUniformComponents']
        if noaddon.webglParameters['maxCombinedFragmentUniformComponents'] != None:
            assert 0 <= jsrun.webglParameters['maxCombinedFragmentUniformComponents'] <= noaddon.webglParameters['maxCombinedFragmentUniformComponents']
            spoof_sum += noaddon.webglParameters['maxCombinedFragmentUniformComponents'] - jsrun.webglParameters['maxCombinedFragmentUniformComponents']
        if noaddon.webglParameters['maxVertexAttribs'] != None:
            assert 0 <= jsrun.webglParameters['maxVertexAttribs'] <= noaddon.webglParameters['maxVertexAttribs']
            spoof_sum += noaddon.webglParameters['maxVertexAttribs'] - jsrun.webglParameters['maxVertexAttribs']
        if noaddon.webglParameters['maxVertexUniformVectors'] != None:
            assert 0 <= jsrun.webglParameters['maxVertexUniformVectors'] <= noaddon.webglParameters['maxVertexUniformVectors']
            spoof_sum += noaddon.webglParameters['maxVertexUniformVectors'] - jsrun.webglParameters['maxVertexUniformVectors']
        if noaddon.webglParameters['maxVertexTextureImageUnits'] != None:
            assert 0 <= jsrun.webglParameters['maxVertexTextureImageUnits'] <= noaddon.webglParameters['maxVertexTextureImageUnits']
            spoof_sum += noaddon.webglParameters['maxVertexTextureImageUnits'] - jsrun.webglParameters['maxVertexTextureImageUnits']
        if noaddon.webglParameters['maxTextureSize'] != None:
            assert 0 <= jsrun.webglParameters['maxTextureSize'] <= noaddon.webglParameters['maxTextureSize']
            spoof_sum += noaddon.webglParameters['maxTextureSize'] - jsrun.webglParameters['maxTextureSize']
        if noaddon.webglParameters['maxCubeMapTextureSize'] != None:
            assert 0 <= jsrun.webglParameters['maxCubeMapTextureSize'] <= noaddon.webglParameters['maxCubeMapTextureSize']
            spoof_sum += noaddon.webglParameters['maxCubeMapTextureSize'] - jsrun.webglParameters['maxCubeMapTextureSize']
        if noaddon.webglParameters['max3DTextureSize'] != None:
            assert 0 <= jsrun.webglParameters['max3DTextureSize'] <= noaddon.webglParameters['max3DTextureSize']
            spoof_sum += noaddon.webglParameters['max3DTextureSize'] - jsrun.webglParameters['max3DTextureSize']
        if noaddon.webglParameters['maxArrayTextureLayers'] != None:
            assert 0 <= jsrun.webglParameters['maxArrayTextureLayers'] <= noaddon.webglParameters['maxArrayTextureLayers']
            spoof_sum += noaddon.webglParameters['maxArrayTextureLayers'] - jsrun.webglParameters['maxArrayTextureLayers']
        assert spoof_sum > 0
    elif expected.webglParameters == 'ZERO VALUE':
        assert (jsrun.webglParameters['maxVertexUniformComponents'] == 0)
        assert (jsrun.webglParameters['maxVertexUniformBlocks'] == 0)
        assert (jsrun.webglParameters['maxVertexOutputComponents'] == 0)
        assert (jsrun.webglParameters['maxVaryingComponents'] == 0)
        assert (jsrun.webglParameters['maxTransformFeedbackInterleavedComponents'] == 0)
        assert (jsrun.webglParameters['maxFragmentUniformComponents'] == 0)
        assert (jsrun.webglParameters['maxFragmentUniformBlocks'] == 0)
        assert (jsrun.webglParameters['maxFragmentInputComponents'] == 0)
        assert (jsrun.webglParameters['maxUniformBufferBindings'] == 0)
        assert (jsrun.webglParameters['maxCombinedUniformBlocks'] == 0)
        assert (jsrun.webglParameters['maxCombinedVertexUniformComponents'] == 0)
        assert (jsrun.webglParameters['maxCombinedFragmentUniformComponents'] == 0)
        assert (jsrun.webglParameters['maxVertexAttribs'] == 0)
        assert (jsrun.webglParameters['maxVertexUniformVectors'] == 0)
        assert (jsrun.webglParameters['maxVertexTextureImageUnits'] == 0)
        assert (jsrun.webglParameters['maxTextureSize'] == 0)
        assert (jsrun.webglParameters['maxCubeMapTextureSize'] == 0)
        assert (jsrun.webglParameters['max3DTextureSize'] == 0)
        assert (jsrun.webglParameters['maxArrayTextureLayers'] == 0)
    else:
        assert (jsrun.webglParameters['maxVertexUniformComponents'] == noaddon.webglParameters['maxVertexUniformComponents'] )
        assert (jsrun.webglParameters['maxVertexUniformBlocks'] == noaddon.webglParameters['maxVertexUniformBlocks'])
        assert (jsrun.webglParameters['maxVertexOutputComponents'] == noaddon.webglParameters['maxVertexOutputComponents'])
        assert (jsrun.webglParameters['maxVaryingComponents'] == noaddon.webglParameters['maxVaryingComponents'])
        assert (jsrun.webglParameters['maxTransformFeedbackInterleavedComponents'] == noaddon.webglParameters['maxTransformFeedbackInterleavedComponents'])
        assert (jsrun.webglParameters['maxFragmentUniformComponents'] == noaddon.webglParameters['maxFragmentUniformComponents'])
        assert (jsrun.webglParameters['maxFragmentUniformBlocks']  == noaddon.webglParameters['maxFragmentUniformBlocks'])
        assert (jsrun.webglParameters['maxFragmentInputComponents'] == noaddon.webglParameters['maxFragmentInputComponents'])
        assert (jsrun.webglParameters['maxUniformBufferBindings'] == noaddon.webglParameters['maxUniformBufferBindings'])
        assert (jsrun.webglParameters['maxCombinedUniformBlocks'] == noaddon.webglParameters['maxCombinedUniformBlocks'])
        assert (jsrun.webglParameters['maxCombinedVertexUniformComponents'] == noaddon.webglParameters['maxCombinedVertexUniformComponents'])
        assert (jsrun.webglParameters['maxCombinedFragmentUniformComponents'] == noaddon.webglParameters['maxCombinedFragmentUniformComponents'])
        assert (jsrun.webglParameters['maxVertexAttribs'] == noaddon.webglParameters['maxVertexAttribs'])
        assert (jsrun.webglParameters['maxVertexUniformVectors'] == noaddon.webglParameters['maxVertexUniformVectors'])
        assert (jsrun.webglParameters['maxVertexTextureImageUnits'] == noaddon.webglParameters['maxVertexTextureImageUnits'])
        assert (jsrun.webglParameters['maxTextureSize'] == noaddon.webglParameters['maxTextureSize'])
        assert (jsrun.webglParameters['maxCubeMapTextureSize'] == noaddon.webglParameters['maxCubeMapTextureSize'])
        assert (jsrun.webglParameters['max3DTextureSize'] == noaddon.webglParameters['max3DTextureSize'])
        assert (jsrun.webglParameters['maxArrayTextureLayers'] == noaddon.webglParameters['maxArrayTextureLayers'])

# Test WebGLRenderingContext.getShaderPrecisionFormat
def test_webgl_precisions(noaddon, jsrun, expected):
    if expected.webglPrecisions == 'ZERO VALUE':
        assert jsrun.webglPrecisions != noaddon.webglPrecisions
    else:
        assert jsrun.webglPrecisions == noaddon.webglPrecisions

# Test WebGLRenderingContext.readPixels
def test_webgl_read_pixels(noaddon, jsrun, expected):
    if jsrun.webglPixels == "ERROR":
        print("\nWebGLRenderingContext.readPixels failed.")
        assert False
    if expected.webglPixels == 'SPOOF VALUE':
        assert jsrun.webglPixels != noaddon.webglPixels
    else:
        assert jsrun.webglPixels == noaddon.webglPixels

# Test HTMLCanvasElement.toDataURL on webgl canvas
def test_webgl_to_data_URL(noaddon, jsrun, expected):
    if expected.webglDataURL == 'SPOOF VALUE':
        assert jsrun.webglDataURL != noaddon.webglDataURL
    else:
        assert jsrun.webglDataURL == noaddon.webglDataURL
