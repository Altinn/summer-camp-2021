from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint



api_instance = swagger_client.DefaultApi(swagger_client.ApiClient())
adressenavn = 'ringveien' # str | Navn på gate, veg, sti, plass eller område som er ført i matrikkelen (eksempel Sørumvegen). (optional)


try:
    # Standard søk.
    api_response = api_instance.sok_get(adressenavn=adressenavn)
    print(api_response.adresser[0].adressekode)
except ApiException as e:
    print("Exception when calling DefaultApi->sok_get: %s\n" % e)