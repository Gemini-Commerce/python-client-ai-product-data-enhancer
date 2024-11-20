# aiproductdataenhancer.AiProductDataEnhancerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_product_data_enhancer_fill_product_data**](AiProductDataEnhancerApi.md#ai_product_data_enhancer_fill_product_data) | **POST** /aiproductdataenhancer.AiProductDataEnhancer/FillProductData | 
[**ai_product_data_enhancer_fill_product_data_check**](AiProductDataEnhancerApi.md#ai_product_data_enhancer_fill_product_data_check) | **POST** /aiproductdataenhancer.AiProductDataEnhancer/FillProductDataCheck | 
[**ai_product_data_enhancer_generate_product_data**](AiProductDataEnhancerApi.md#ai_product_data_enhancer_generate_product_data) | **POST** /aiproductdataenhancer.AiProductDataEnhancer/GenerateProductData | 
[**ai_product_data_enhancer_translate_data**](AiProductDataEnhancerApi.md#ai_product_data_enhancer_translate_data) | **POST** /aiproductdataenhancer.AiProductDataEnhancer/TranslateData | 


# **ai_product_data_enhancer_fill_product_data**
> AiproductdataenhancerFillProductDataResponse ai_product_data_enhancer_fill_product_data(body)



### Example


```python
import aiproductdataenhancer
from aiproductdataenhancer.models.aiproductdataenhancer_fill_product_data_request import AiproductdataenhancerFillProductDataRequest
from aiproductdataenhancer.models.aiproductdataenhancer_fill_product_data_response import AiproductdataenhancerFillProductDataResponse
from aiproductdataenhancer.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aiproductdataenhancer.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with aiproductdataenhancer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aiproductdataenhancer.AiProductDataEnhancerApi(api_client)
    body = aiproductdataenhancer.AiproductdataenhancerFillProductDataRequest() # AiproductdataenhancerFillProductDataRequest | 

    try:
        api_response = api_instance.ai_product_data_enhancer_fill_product_data(body)
        print("The response of AiProductDataEnhancerApi->ai_product_data_enhancer_fill_product_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiProductDataEnhancerApi->ai_product_data_enhancer_fill_product_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AiproductdataenhancerFillProductDataRequest**](AiproductdataenhancerFillProductDataRequest.md)|  | 

### Return type

[**AiproductdataenhancerFillProductDataResponse**](AiproductdataenhancerFillProductDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_product_data_enhancer_fill_product_data_check**
> AiproductdataenhancerFillProductDataCheckResponse ai_product_data_enhancer_fill_product_data_check(body)



### Example


```python
import aiproductdataenhancer
from aiproductdataenhancer.models.aiproductdataenhancer_fill_product_data_check_request import AiproductdataenhancerFillProductDataCheckRequest
from aiproductdataenhancer.models.aiproductdataenhancer_fill_product_data_check_response import AiproductdataenhancerFillProductDataCheckResponse
from aiproductdataenhancer.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aiproductdataenhancer.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with aiproductdataenhancer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aiproductdataenhancer.AiProductDataEnhancerApi(api_client)
    body = aiproductdataenhancer.AiproductdataenhancerFillProductDataCheckRequest() # AiproductdataenhancerFillProductDataCheckRequest | 

    try:
        api_response = api_instance.ai_product_data_enhancer_fill_product_data_check(body)
        print("The response of AiProductDataEnhancerApi->ai_product_data_enhancer_fill_product_data_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiProductDataEnhancerApi->ai_product_data_enhancer_fill_product_data_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AiproductdataenhancerFillProductDataCheckRequest**](AiproductdataenhancerFillProductDataCheckRequest.md)|  | 

### Return type

[**AiproductdataenhancerFillProductDataCheckResponse**](AiproductdataenhancerFillProductDataCheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_product_data_enhancer_generate_product_data**
> AiproductdataenhancerGenerateProductDataResponse ai_product_data_enhancer_generate_product_data(body)



### Example


```python
import aiproductdataenhancer
from aiproductdataenhancer.models.aiproductdataenhancer_generate_product_data_request import AiproductdataenhancerGenerateProductDataRequest
from aiproductdataenhancer.models.aiproductdataenhancer_generate_product_data_response import AiproductdataenhancerGenerateProductDataResponse
from aiproductdataenhancer.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aiproductdataenhancer.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with aiproductdataenhancer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aiproductdataenhancer.AiProductDataEnhancerApi(api_client)
    body = aiproductdataenhancer.AiproductdataenhancerGenerateProductDataRequest() # AiproductdataenhancerGenerateProductDataRequest | 

    try:
        api_response = api_instance.ai_product_data_enhancer_generate_product_data(body)
        print("The response of AiProductDataEnhancerApi->ai_product_data_enhancer_generate_product_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiProductDataEnhancerApi->ai_product_data_enhancer_generate_product_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AiproductdataenhancerGenerateProductDataRequest**](AiproductdataenhancerGenerateProductDataRequest.md)|  | 

### Return type

[**AiproductdataenhancerGenerateProductDataResponse**](AiproductdataenhancerGenerateProductDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_product_data_enhancer_translate_data**
> AiproductdataenhancerTranslateDataResponse ai_product_data_enhancer_translate_data(body)



### Example


```python
import aiproductdataenhancer
from aiproductdataenhancer.models.aiproductdataenhancer_translate_data_request import AiproductdataenhancerTranslateDataRequest
from aiproductdataenhancer.models.aiproductdataenhancer_translate_data_response import AiproductdataenhancerTranslateDataResponse
from aiproductdataenhancer.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aiproductdataenhancer.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with aiproductdataenhancer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aiproductdataenhancer.AiProductDataEnhancerApi(api_client)
    body = aiproductdataenhancer.AiproductdataenhancerTranslateDataRequest() # AiproductdataenhancerTranslateDataRequest | 

    try:
        api_response = api_instance.ai_product_data_enhancer_translate_data(body)
        print("The response of AiProductDataEnhancerApi->ai_product_data_enhancer_translate_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiProductDataEnhancerApi->ai_product_data_enhancer_translate_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AiproductdataenhancerTranslateDataRequest**](AiproductdataenhancerTranslateDataRequest.md)|  | 

### Return type

[**AiproductdataenhancerTranslateDataResponse**](AiproductdataenhancerTranslateDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

