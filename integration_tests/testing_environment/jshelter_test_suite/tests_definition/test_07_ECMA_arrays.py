from shared_set import get_shared_browser
import pytest

def test_crypto_getRandomValues(addonRun):
    random_crypto_values = addonRun.ECMAarrays['cryptoGetRandomValues']

    for array_type in random_crypto_values:
        nums = random_crypto_values[array_type]
        if len(nums) > 0:
            assert nums['0'] != nums['1'] or nums['0'] != nums['2'] or  nums['0'] != nums['3'] # It is highly unlikely that all three numbers are the same
            assert nums['1'] != nums['0'] or nums['1'] != nums['2'] or  nums['1'] != nums['3'] # It is highly unlikely that all three numbers are the same
            assert nums['2'] != nums['0'] or nums['2'] != nums['1'] or  nums['2'] != nums['3'] # It is highly unlikely that all three numbers are the same
            assert nums['3'] != nums['0'] or nums['3'] != nums['1'] or  nums['3'] != nums['2']
        else:
            pytest.fail("No random value generated (%s). Probable JavaScript error: Crypto.getRandomValues: Argument 1 does not implement interface ArrayBufferView." + array_type)

def test_ArrayBufferViews(addonRun):
    arrays = addonRun.ECMAarrays['arrayBufferViews']
    for array in arrays:
        assert arrays[array] == True
	
def test_TypedArraysInit(addonRun):
    assert addonRun.ECMAarrays['typedArraysInt'] == True

def test_TypedArraysParams32(addonRun):
    arrays = addonRun.ECMAarrays['typedArraysParams32']
    for array in arrays:
        assert arrays[array] == True
	
def test_TypedArraysInitByLength(addonRun):
    assert addonRun.ECMAarrays['typedArraysInitByLenght'] == True

def test_TypedArraysOverwriteElement(addonRun):
    assert addonRun.ECMAarrays['typedArraysOverwriteElement'] == True

def test_TypedArraysOverwriteFull(addonRun):
    assert addonRun.ECMAarrays['typedArraysOverwriteFull'] == True 

def test_TypedArraysParams8(addonRun):
    arrays = addonRun.ECMAarrays['typedArraysParams8']
    for array in arrays:
        assert arrays[array] == True

def test_TypedArrayFromBuffer(addonRun):
    arrays = addonRun.ECMAarrays['typedArrayFromBuffer']
    for array in arrays:
        assert arrays[array] == True

def test_TypedArraysMethods_set(addonRun):
    assert addonRun.ECMAarrays['typedArraysMethodsSet'] == True

def test_TypedArraysMethods_reverse(addonRun):
    assert addonRun.ECMAarrays['typedArraysMethodsReverse'] == True

def test_TypedArraysMethods_sort(addonRun):
    assert addonRun.ECMAarrays['typedArraysMethodsSort'] == True

def test_TypedArraysMethods_fill(addonRun):
    assert addonRun.ECMAarrays['typedArraysMethodsFill'] == True

def test_TypedArraysMethods_copyWithin(addonRun):
    assert addonRun.ECMAarrays['typedArraysMethodsCopyWithin'] == True

def test_TypedArraysMethods_subarray(addonRun):
    arrays = addonRun.ECMAarrays['typedArrayMethodsSubarray']
    for array in arrays:
        assert arrays[array] == True
	
def test_TypedArraysMethods_slice(addonRun):
    arrays = addonRun.ECMAarrays['typedArraysMethodsSlice']
    for array in arrays:
        assert arrays[array] == True

def test_TypedArraysMethods_map(addonRun):
    assert addonRun.ECMAarrays['typedArraysMethodsMap'] == True

def test_TypedArraysMethods_filter(addonRun):
    assert addonRun.ECMAarrays['typedArrayMethodsFilter'] == True

def test_TypedArraysMethods_reduce(addonRun):
    assert addonRun.ECMAarrays['typedArrayMethodsReduce'] == True

def test_TypedArraysMethods_reduceR(addonRun):
    assert addonRun.ECMAarrays['typedArraysMethodsReduceR'] == True

def test_TypedArraysMethods_lastIndexOf(addonRun):
    assert addonRun.ECMAarrays['typedArraysMethodsLastIndexOf'] == True

def test_TypedArraysMethods_forEach(addonRun):
    assert addonRun.ECMAarrays['typedArraysMethodsForEach'] == True

def test_TypedArraysMethods_find(addonRun):
    assert addonRun.ECMAarrays['typedArraysMethodsFind'] == True
	
def test_TypedArraysMethods_join(addonRun):
    assert addonRun.ECMAarrays['typedArraysMethodsJoin'] == True
	
def test_TypedArraysMethods_entrieskeysvalues(addonRun):
    arrays = addonRun.ECMAarrays['typedArraysMethodsEntriesKeysValues']
    for array in arrays:
        assert arrays[array] == True
	
def test_TypedArraysMethods_from(addonRun):
    assert addonRun.ECMAarrays['typedArrayMethodsFrom'] == True

def test_DataViewInit(addonRun):
    arrays = addonRun.ECMAarrays['dataViewInit']
    for array in arrays:
        assert arrays[array] == True

def test_DataViewAccessors(addonRun):
    arrays = addonRun.ECMAarrays['dataViewAccessors']
    for array in arrays['loopSetGet']:
        assert array == True
    assert arrays['floatSet'] == True
    assert arrays['intSet'] == True
    assert arrays['bigSet'] == True

def test_OneBufferMoreViews(addonRun):
    assert addonRun.ECMAarrays['oneBufferMoreViews'] == True

@pytest.mark.xfail(("chrome" in get_shared_browser()), reason="See https://pagure.io/JShelter/webextension/issue/80")
def test_worker_basic(addonRun, expected):
    if expected.worker == "REMOVED":
        assert addonRun.worker['workerBasics']['isWorkerRemoved'] == True
        return
    assert addonRun.worker['workerBasics']['onMessage'] == True
    assert addonRun.worker['workerBasics']['onError'] == True
    assert addonRun.worker['workerBasics']['onMessageError'] == True
    assert addonRun.worker['workerBasics']['eventListener'] == True
    assert addonRun.worker['workerBasics']['postMessage'] == True
    assert addonRun.worker['workerBasics']['removeEventListener'] == True
    assert addonRun.worker['workerBasics']['terminate'] == True

'''
def test_worker_implements_dispatchEvent(addonRun):
    assert addonRun.worker['workerImplementsDispatchEvent'] == True

def test_worker_check_communication_handler(addonRun):
    assert addonRun.worker['workerCheckCommunicationHandler'] == True

def test_worker_error(addonRun):
    assert addonRun.worker['workerError'] == True

def test_worker_check_communication_listener(addonRun):
    assert addonRun.worker['workerCheckCommunicationListener'] == True


def test_worker_terminate(addonRun):
    assert addonRun.worker['workerTerminate'] == True

def test_worker_dispatchEvent(addonRun):
    assert addonRun.worker['workerDispatchEvent'] == True
'''
