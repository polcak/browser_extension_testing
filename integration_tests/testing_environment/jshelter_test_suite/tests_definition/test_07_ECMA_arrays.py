from shared_set import get_shared_browser
import pytest

def test_crypto_getRandomValues(jsrun):
    random_crypto_values = jsrun.ECMAarrays['cryptoGetRandomValues']

    for array_type in random_crypto_values:
        nums = random_crypto_values[array_type]
        if len(nums) > 0:
            assert nums['0'] != nums['1'] or nums['0'] != nums['2'] or  nums['0'] != nums['3'] # It is highly unlikely that all three numbers are the same
            assert nums['1'] != nums['0'] or nums['1'] != nums['2'] or  nums['1'] != nums['3'] # It is highly unlikely that all three numbers are the same
            assert nums['2'] != nums['0'] or nums['2'] != nums['1'] or  nums['2'] != nums['3'] # It is highly unlikely that all three numbers are the same
            assert nums['3'] != nums['0'] or nums['3'] != nums['1'] or  nums['3'] != nums['2']
        else:
            pytest.fail("No random value generated (%s). Probable JavaScript error: Crypto.getRandomValues: Argument 1 does not implement interface ArrayBufferView." + array_type)

def test_ArrayBufferViews(jsrun):
    arrays = jsrun.ECMAarrays['arrayBufferViews']
    for array in arrays:
        assert arrays[array] == True
	
def test_TypedArraysInit(jsrun):
    assert jsrun.ECMAarrays['typedArraysInt'] == True

def test_TypedArraysParams32(jsrun):
    arrays = jsrun.ECMAarrays['typedArraysParams32']
    for array in arrays:
        assert arrays[array] == True
	
def test_TypedArraysInitByLength(jsrun):
    assert jsrun.ECMAarrays['typedArraysInitByLenght'] == True

def test_TypedArraysOverwriteElement(jsrun):
    assert jsrun.ECMAarrays['typedArraysOverwriteElement'] == True

def test_TypedArraysOverwriteFull(jsrun):
    assert jsrun.ECMAarrays['typedArraysOverwriteFull'] == True 

def test_TypedArraysParams8(jsrun):
    arrays = jsrun.ECMAarrays['typedArraysParams8']
    for array in arrays:
        assert arrays[array] == True

def test_TypedArrayFromBuffer(jsrun):
    arrays = jsrun.ECMAarrays['typedArrayFromBuffer']
    for array in arrays:
        assert arrays[array] == True

def test_TypedArraysMethods_set(jsrun):
    assert jsrun.ECMAarrays['typedArraysMethodsSet'] == True

def test_TypedArraysMethods_reverse(jsrun):
    assert jsrun.ECMAarrays['typedArraysMethodsReverse'] == True

def test_TypedArraysMethods_sort(jsrun):
    assert jsrun.ECMAarrays['typedArraysMethodsSort'] == True

def test_TypedArraysMethods_fill(jsrun):
    assert jsrun.ECMAarrays['typedArraysMethodsFill'] == True

def test_TypedArraysMethods_copyWithin(jsrun):
    assert jsrun.ECMAarrays['typedArraysMethodsCopyWithin'] == True

def test_TypedArraysMethods_subarray(jsrun):
    arrays = jsrun.ECMAarrays['typedArrayMethodsSubarray']
    for array in arrays:
        assert arrays[array] == True
	
def test_TypedArraysMethods_slice(jsrun):
    arrays = jsrun.ECMAarrays['typedArraysMethodsSlice']
    for array in arrays:
        assert arrays[array] == True

def test_TypedArraysMethods_map(jsrun):
    assert jsrun.ECMAarrays['typedArraysMethodsMap'] == True

def test_TypedArraysMethods_filter(jsrun):
    assert jsrun.ECMAarrays['typedArrayMethodsFilter'] == True

def test_TypedArraysMethods_reduce(jsrun):
    assert jsrun.ECMAarrays['typedArrayMethodsReduce'] == True

def test_TypedArraysMethods_reduceR(jsrun):
    assert jsrun.ECMAarrays['typedArraysMethodsReduceR'] == True

def test_TypedArraysMethods_lastIndexOf(jsrun):
    assert jsrun.ECMAarrays['typedArraysMethodsLastIndexOf'] == True

def test_TypedArraysMethods_forEach(jsrun):
    assert jsrun.ECMAarrays['typedArraysMethodsForEach'] == True

def test_TypedArraysMethods_find(jsrun):
    assert jsrun.ECMAarrays['typedArraysMethodsFind'] == True
	
def test_TypedArraysMethods_join(jsrun):
    assert jsrun.ECMAarrays['typedArraysMethodsJoin'] == True
	
def test_TypedArraysMethods_entrieskeysvalues(jsrun):
    arrays = jsrun.ECMAarrays['typedArraysMethodsEntriesKeysValues']
    for array in arrays:
        assert arrays[array] == True
	
def test_TypedArraysMethods_from(jsrun):
    assert jsrun.ECMAarrays['typedArrayMethodsFrom'] == True

def test_DataViewInit(jsrun):
    arrays = jsrun.ECMAarrays['dataViewInit']
    for array in arrays:
        assert arrays[array] == True

def test_DataViewAccessors(jsrun):
    arrays = jsrun.ECMAarrays['dataViewAccessors']
    for array in arrays['loopSetGet']:
        assert array == True
    assert arrays['floatSet'] == True
    assert arrays['intSet'] == True
    assert arrays['bigSet'] == True

def test_OneBufferMoreViews(jsrun):
    assert jsrun.ECMAarrays['oneBufferMoreViews'] == True

@pytest.mark.xfail(("chrome" in get_shared_browser()), reason="See https://pagure.io/JShelter/webextension/issue/80")
def test_worker_basic(jsrun, expected):
    if expected.worker == "REMOVED":
        assert jsrun.worker['workerBasics']['isWorkerRemoved'] == True
        return
    assert jsrun.worker['workerBasics']['onMessage'] == True
    assert jsrun.worker['workerBasics']['onError'] == True
    assert jsrun.worker['workerBasics']['onMessageError'] == True
    assert jsrun.worker['workerBasics']['eventListener'] == True
    assert jsrun.worker['workerBasics']['postMessage'] == True
    assert jsrun.worker['workerBasics']['removeEventListener'] == True
    assert jsrun.worker['workerBasics']['terminate'] == True

'''
def test_worker_implements_dispatchEvent(jsrun):
    assert jsrun.worker['workerImplementsDispatchEvent'] == True

def test_worker_check_communication_handler(jsrun):
    assert jsrun.worker['workerCheckCommunicationHandler'] == True

def test_worker_error(jsrun):
    assert jsrun.worker['workerError'] == True

def test_worker_check_communication_listener(jsrun):
    assert jsrun.worker['workerCheckCommunicationListener'] == True


def test_worker_terminate(jsrun):
    assert jsrun.worker['workerTerminate'] == True

def test_worker_dispatchEvent(jsrun):
    assert jsrun.worker['workerDispatchEvent'] == True
'''
