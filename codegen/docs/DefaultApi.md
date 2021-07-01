# swagger_client.DefaultApi

All URIs are relative to *https://ws.geonorge.no/adresser/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**punktsok_get**](DefaultApi.md#punktsok_get) | **GET** /punktsok | Geografisk punktsøk.
[**sok_get**](DefaultApi.md#sok_get) | **GET** /sok | Standard søk.

# **punktsok_get**
> OutputGeoPointList punktsok_get(radius, lat, lon, treff_per_side=treff_per_side, side=side, utkoordsys=utkoordsys, ascii_kompatibel=ascii_kompatibel, koordsys=koordsys, filtrer=filtrer)

Geografisk punktsøk.

Søk etter adresser innen en viss radius. Sortert etter distanse fra punkt. Respons inkluderer distansen fra punktet i meter. Geografiske koordinater må benyttes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
radius = 56 # int | Radius for søket i hele meter
lat = 3.4 # float | Geografiske lat/nord koordinater, med mindre annet er spesifisert.
lon = 3.4 # float | Geografiske lon/øst koordinater, med mindre annet er spesifisert.
treff_per_side = 10 # int | Antall treff per side. (optional) (default to 10)
side = 0 # int | Sidenummeret som vises. Første side = 0 (optional) (default to 0)
utkoordsys = 4258 # int | Koordinatsystem som adressegeometrien skal returneres i. Oppgis som srid, f.eks. 25833 eller 3857. Standardinnstilling er 4258 (optional) (default to 4258)
ascii_kompatibel = true # bool | Garanterer at dataene som returneres er ascii-kompatible. (optional) (default to true)
koordsys = 4258 # int | Koordinatsystem for punktet du søker etter. Oppgis som srid, f.eks. 25833 eller 3857. Standardinnstilling er 4258 (optional) (default to 4258)
filtrer = 'filtrer_example' # str | Kommaseparert liste med objekter du ikke ønsker å filtrere ut. For å hente ut underobjekter bruk \".\"-notasjon, f.eks.: &filtrer=adresser.kommunenummer,adresser.representasjonspunkt (optional)

try:
    # Geografisk punktsøk.
    api_response = api_instance.punktsok_get(radius, lat, lon, treff_per_side=treff_per_side, side=side, utkoordsys=utkoordsys, ascii_kompatibel=ascii_kompatibel, koordsys=koordsys, filtrer=filtrer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->punktsok_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radius** | **int**| Radius for søket i hele meter | 
 **lat** | **float**| Geografiske lat/nord koordinater, med mindre annet er spesifisert. | 
 **lon** | **float**| Geografiske lon/øst koordinater, med mindre annet er spesifisert. | 
 **treff_per_side** | **int**| Antall treff per side. | [optional] [default to 10]
 **side** | **int**| Sidenummeret som vises. Første side &#x3D; 0 | [optional] [default to 0]
 **utkoordsys** | **int**| Koordinatsystem som adressegeometrien skal returneres i. Oppgis som srid, f.eks. 25833 eller 3857. Standardinnstilling er 4258 | [optional] [default to 4258]
 **ascii_kompatibel** | **bool**| Garanterer at dataene som returneres er ascii-kompatible. | [optional] [default to true]
 **koordsys** | **int**| Koordinatsystem for punktet du søker etter. Oppgis som srid, f.eks. 25833 eller 3857. Standardinnstilling er 4258 | [optional] [default to 4258]
 **filtrer** | **str**| Kommaseparert liste med objekter du ikke ønsker å filtrere ut. For å hente ut underobjekter bruk \&quot;.\&quot;-notasjon, f.eks.: &amp;filtrer&#x3D;adresser.kommunenummer,adresser.representasjonspunkt | [optional] 

### Return type

[**OutputGeoPointList**](OutputGeoPointList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sok_get**
> OutputAdresseList sok_get(adressenavn=adressenavn, festenummer=festenummer, adressetekst=adressetekst, undernummer=undernummer, sokemodus=sokemodus, bokstav=bokstav, side=side, bruksnummer=bruksnummer, postnummer=postnummer, objtype=objtype, adressekode=adressekode, adressetilleggsnavn=adressetilleggsnavn, ascii_kompatibel=ascii_kompatibel, kommunenummer=kommunenummer, poststed=poststed, nummer=nummer, treff_per_side=treff_per_side, bruksenhetsnummer=bruksenhetsnummer, utkoordsys=utkoordsys, sok=sok, kommunenavn=kommunenavn, filtrer=filtrer, gardsnummer=gardsnummer)

Standard søk.

Søk etter adresser. Minst ett søkeparameter må benyttes. For generelle søk så anbefales det å benytte søkeparameteret \"sok\", og så eventuelt snevre inn resultatet ved å bruke de andre parameterene. For eksempel sok?sok=munkegata&kommunenummer=5001

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
adressenavn = 'adressenavn_example' # str | Navn på gate, veg, sti, plass eller område som er ført i matrikkelen (eksempel Sørumvegen). (optional)
festenummer = 56 # int | Del av en matrikkeladresse der vegadresse ikke er innført, - eller vegadressens knytning til matrikkelenhet (grunneiendom eller feste, - gir her ikke knytning mot seksjon) (optional)
adressetekst = 'adressetekst_example' # str | Offisiell adresse som tekststreng (eksempel «Ven, Sørumvegen 45»), men uten eventuelt bruksenhetsnummer for leiligheter (optional)
undernummer = 56 # int | Fortløpende nummerering av matrikkeladresser med samme gårds-, bruks- og festenummer. (optional)
sokemodus = 'sokemodus_example' # str | Modifiserer \"sok\"-feltet, standardverdi er \"AND\". Velg om søket skal kreve at hver eneste søkeparameter finnes i treffet, eller om det holder med treff på kun ett parameter. F.eks. vil \"?sok=munkegata 1 trondheim&sokemodus=OR\" returnere alt som inneholder \"munkegata\" OG/ELLER tallet \"1\" OG/ELLER \"trondheim\". (optional)
bokstav = 'bokstav_example' # str | Del av adressenummer (husnummer) som er et nummer og en eventuelt en bokstav, f.eks 23B. For å kun søke på adresser uten noen bokstav så inkluderer man \"bokstav=\" i søkestrengen uten å fylle inn noen verdi. (optional)
side = 0 # int | Sidenummeret som vises. Første side = 0 (optional) (default to 0)
bruksnummer = 56 # int | Del av en matrikkeladresse der vegadresse ikke er innført, - eller vegadressens knytning til matrikkelenhet (grunneiendom eller feste, - gir her ikke knyting mot seksjon) (optional)
postnummer = 'postnummer_example' # str | Unik identifikasjon av et postnummerområde. Tekstverdi som må bestå av 4 tall. 0340 er for eksempel gyldig, mens 340 er ikke gyldig. (optional)
objtype = 'objtype_example' # str | Vegadresse er offisiell adresse i form av et adressenavn og et adressenummer (Storgata 10). Der kommunen ikke har gått over til vegadresser, vil det finnes matrikkeladresse på formen: gårdsnummer/ bruksnummer/ev festenummer-ev undernummer (10/2) Begge adressetypene kan ha bruksenhetsnummer (leiligheter) og adressetilleggsnavn. Begge adressetypene vises som standard, hvis man kun ønsker å se en av de kan man spesifisere adressetypen via dette parameteret. (optional)
adressekode = 56 # int | Nummer som entydig identifiserer adresserbare gater, veger, stier, plasser og områder som er ført i matrikkelen innen kommunen (optional)
adressetilleggsnavn = 'adressetilleggsnavn_example' # str | Nedarvet bruksnavn, navn på en institusjon eller bygning eller grend brukt som del av den offisielle adressen (optional)
ascii_kompatibel = true # bool | Garanterer at dataene som returneres er ascii-kompatible. (optional) (default to true)
kommunenummer = 'kommunenummer_example' # str | Nummerering av kommunen i henhold til Statistisk sentralbyrå sin offisielle liste. Tekstverdi som må bestå av 4 tall. 0301 er for eksempel gyldig, mens 301 er ikke gyldig. (optional)
poststed = 'poststed_example' # str | Navn på poststed i henhold til Postens egne lister (optional)
nummer = 56 # int | Del av adressenummer (husnummer) som er et nummer og eventuelt en bokstav, f.eks 23B (optional)
treff_per_side = 10 # int | Antall treff per side. (optional) (default to 10)
bruksenhetsnummer = 'bruksenhetsnummer_example' # str | Del av offisiell adresse (bruksenhetsnummer) til f.eks en leilighet i flerboligbygg. Bokstaven og de to første tallene angir etasje, de to siste angir leilighetens nummer i etasjen, regnet fra venstre mot høyre. Eksempel: \"H0102\", \"K0101\" (optional)
utkoordsys = 4258 # int | Koordinatsystem som adressegeometrien skal returneres i. Oppgis som srid, f.eks. 25833 eller 3857. Standardinnstilling er 4258 (optional) (default to 4258)
sok = 'sok_example' # str | Generelt adressesøk over nesten alle feltene. Wildcard-søk med \"*\" er støttet. Flere detaljer vil gi mer nøyaktige søk. Bare legg til ekstra opplysninger adskilt med mellomrom. F.eks.: ?sok=munkegata 1 trondheim   (optional)
kommunenavn = 'kommunenavn_example' # str | Navn (norsk) på en kommune (optional)
filtrer = 'filtrer_example' # str | Kommaseparert liste med objekter du ikke ønsker å filtrere ut. For å hente ut underobjekter bruk \".\"-notasjon, f.eks.: &filtrer=adresser.kommunenummer,adresser.representasjonspunkt (optional)
gardsnummer = 56 # int | Del av en matrikkeladresse der vegadresse ikke er innført, - eller vegadressens knytning til matrikkelenhet (grunneiendom eller feste, - gir her ikke knyting mot seksjon) (optional)

try:
    # Standard søk.
    api_response = api_instance.sok_get(adressenavn=adressenavn, festenummer=festenummer, adressetekst=adressetekst, undernummer=undernummer, sokemodus=sokemodus, bokstav=bokstav, side=side, bruksnummer=bruksnummer, postnummer=postnummer, objtype=objtype, adressekode=adressekode, adressetilleggsnavn=adressetilleggsnavn, ascii_kompatibel=ascii_kompatibel, kommunenummer=kommunenummer, poststed=poststed, nummer=nummer, treff_per_side=treff_per_side, bruksenhetsnummer=bruksenhetsnummer, utkoordsys=utkoordsys, sok=sok, kommunenavn=kommunenavn, filtrer=filtrer, gardsnummer=gardsnummer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sok_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adressenavn** | **str**| Navn på gate, veg, sti, plass eller område som er ført i matrikkelen (eksempel Sørumvegen). | [optional] 
 **festenummer** | **int**| Del av en matrikkeladresse der vegadresse ikke er innført, - eller vegadressens knytning til matrikkelenhet (grunneiendom eller feste, - gir her ikke knytning mot seksjon) | [optional] 
 **adressetekst** | **str**| Offisiell adresse som tekststreng (eksempel «Ven, Sørumvegen 45»), men uten eventuelt bruksenhetsnummer for leiligheter | [optional] 
 **undernummer** | **int**| Fortløpende nummerering av matrikkeladresser med samme gårds-, bruks- og festenummer. | [optional] 
 **sokemodus** | **str**| Modifiserer \&quot;sok\&quot;-feltet, standardverdi er \&quot;AND\&quot;. Velg om søket skal kreve at hver eneste søkeparameter finnes i treffet, eller om det holder med treff på kun ett parameter. F.eks. vil \&quot;?sok&#x3D;munkegata 1 trondheim&amp;sokemodus&#x3D;OR\&quot; returnere alt som inneholder \&quot;munkegata\&quot; OG/ELLER tallet \&quot;1\&quot; OG/ELLER \&quot;trondheim\&quot;. | [optional] 
 **bokstav** | **str**| Del av adressenummer (husnummer) som er et nummer og en eventuelt en bokstav, f.eks 23B. For å kun søke på adresser uten noen bokstav så inkluderer man \&quot;bokstav&#x3D;\&quot; i søkestrengen uten å fylle inn noen verdi. | [optional] 
 **side** | **int**| Sidenummeret som vises. Første side &#x3D; 0 | [optional] [default to 0]
 **bruksnummer** | **int**| Del av en matrikkeladresse der vegadresse ikke er innført, - eller vegadressens knytning til matrikkelenhet (grunneiendom eller feste, - gir her ikke knyting mot seksjon) | [optional] 
 **postnummer** | **str**| Unik identifikasjon av et postnummerområde. Tekstverdi som må bestå av 4 tall. 0340 er for eksempel gyldig, mens 340 er ikke gyldig. | [optional] 
 **objtype** | **str**| Vegadresse er offisiell adresse i form av et adressenavn og et adressenummer (Storgata 10). Der kommunen ikke har gått over til vegadresser, vil det finnes matrikkeladresse på formen: gårdsnummer/ bruksnummer/ev festenummer-ev undernummer (10/2) Begge adressetypene kan ha bruksenhetsnummer (leiligheter) og adressetilleggsnavn. Begge adressetypene vises som standard, hvis man kun ønsker å se en av de kan man spesifisere adressetypen via dette parameteret. | [optional] 
 **adressekode** | **int**| Nummer som entydig identifiserer adresserbare gater, veger, stier, plasser og områder som er ført i matrikkelen innen kommunen | [optional] 
 **adressetilleggsnavn** | **str**| Nedarvet bruksnavn, navn på en institusjon eller bygning eller grend brukt som del av den offisielle adressen | [optional] 
 **ascii_kompatibel** | **bool**| Garanterer at dataene som returneres er ascii-kompatible. | [optional] [default to true]
 **kommunenummer** | **str**| Nummerering av kommunen i henhold til Statistisk sentralbyrå sin offisielle liste. Tekstverdi som må bestå av 4 tall. 0301 er for eksempel gyldig, mens 301 er ikke gyldig. | [optional] 
 **poststed** | **str**| Navn på poststed i henhold til Postens egne lister | [optional] 
 **nummer** | **int**| Del av adressenummer (husnummer) som er et nummer og eventuelt en bokstav, f.eks 23B | [optional] 
 **treff_per_side** | **int**| Antall treff per side. | [optional] [default to 10]
 **bruksenhetsnummer** | **str**| Del av offisiell adresse (bruksenhetsnummer) til f.eks en leilighet i flerboligbygg. Bokstaven og de to første tallene angir etasje, de to siste angir leilighetens nummer i etasjen, regnet fra venstre mot høyre. Eksempel: \&quot;H0102\&quot;, \&quot;K0101\&quot; | [optional] 
 **utkoordsys** | **int**| Koordinatsystem som adressegeometrien skal returneres i. Oppgis som srid, f.eks. 25833 eller 3857. Standardinnstilling er 4258 | [optional] [default to 4258]
 **sok** | **str**| Generelt adressesøk over nesten alle feltene. Wildcard-søk med \&quot;*\&quot; er støttet. Flere detaljer vil gi mer nøyaktige søk. Bare legg til ekstra opplysninger adskilt med mellomrom. F.eks.: ?sok&#x3D;munkegata 1 trondheim   | [optional] 
 **kommunenavn** | **str**| Navn (norsk) på en kommune | [optional] 
 **filtrer** | **str**| Kommaseparert liste med objekter du ikke ønsker å filtrere ut. For å hente ut underobjekter bruk \&quot;.\&quot;-notasjon, f.eks.: &amp;filtrer&#x3D;adresser.kommunenummer,adresser.representasjonspunkt | [optional] 
 **gardsnummer** | **int**| Del av en matrikkeladresse der vegadresse ikke er innført, - eller vegadressens knytning til matrikkelenhet (grunneiendom eller feste, - gir her ikke knyting mot seksjon) | [optional] 

### Return type

[**OutputAdresseList**](OutputAdresseList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

