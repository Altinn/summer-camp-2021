# OutputGeoPoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adressekode** | **int** | Nummer som entydig identifiserer adresserbare gater, veger, stier, plasser og områder som er ført i matrikkelen innen kommunen | [optional] 
**adressenavn** | **str** | Navn på gate, veg, sti, plass eller område som er ført i matrikkelen (eksempel Sørumvegen). | [optional] 
**adressetekst** | **str** | Del av offisiell adresse, men uten bruksenhetsnummer som ligger til bruksenheter/boliger (ligger her som egenskap til vegadressen) Eksempel: \&quot;Storgata 2B\&quot; eller \&quot;123/4-2\&quot; Der det i tillegg er adressetilleggsnavn: \&quot;Haugen, Storgata 2B\&quot; eller \&quot;Midtgard, 123/4-2\&quot; | [optional] 
**adressetekstutenadressetilleggsnavn** | **str** | Del av offisiell adresse, men uten bruksenhetsnummer som ligger til bruksenheter/boliger og adressetilleggsnavn Eksempel: \&quot;Storgata 2B\&quot; eller \&quot;123/4-2\&quot; | [optional] 
**adressetilleggsnavn** | **str** | Nedarvet bruksnavn, navn på en institusjon eller bygning eller grend brukt som del av den offisielle adressen | [optional] 
**bokstav** | **str** | Del av adressenummer (husnummer) som er et nummer og en eventuelt en bokstav, f.eks 23B. For å kun søke på adresser uten noen bokstav så inkluderer man \&quot;bokstav&#x3D;\&quot; i søkestrengen uten å fylle inn noen verdi. | [optional] 
**bruksenhetsnummer** | **list[str]** |  | [optional] 
**bruksnummer** | **int** | Del av en matrikkeladresse der vegadresse ikke er innført, - eller vegadressens knytning til matrikkelenhet (grunneiendom eller feste, - gir her ikke knyting mot seksjon) | [optional] 
**festenummer** | **int** | Del av en matrikkeladresse der vegadresse ikke er innført, - eller vegadressens knytning til matrikkelenhet (grunneiendom eller feste, - gir her ikke knytning mot seksjon) | [optional] 
**gardsnummer** | **int** | Del av en matrikkeladresse der vegadresse ikke er innført, - eller vegadressens knytning til matrikkelenhet (grunneiendom eller feste, - gir her ikke knyting mot seksjon) | [optional] 
**kommunenavn** | **str** | Navn (norsk) på en kommune | [optional] 
**kommunenummer** | **str** | Nummerering av kommunen i henhold til Statistisk sentralbyrå sin offisielle liste. Tekstverdi som må bestå av 4 tall. 0301 er for eksempel gyldig, mens 301 er ikke gyldig. | [optional] 
**meter_distanse_til_punkt** | **float** |  | [optional] 
**nummer** | **int** | Del av adressenummer (husnummer) som er et nummer og eventuelt en bokstav, f.eks 23B | [optional] 
**objtype** | **str** | Vegadresse er offisiell adresse i form av et adressenavn og et adressenummer (Storgata 10). Der kommunen ikke har gått over til vegadresser, vil det finnes matrikkeladresse på formen: gårdsnummer/ bruksnummer/ev festenummer-ev undernummer (10/2) Begge adressetypene kan ha bruksenhetsnummer (leiligheter) og adressetilleggsnavn. Begge adressetypene vises som standard, hvis man kun ønsker å se en av de kan man spesifisere adressetypen via dette parameteret. | [optional] 
**oppdateringsdato** | **datetime** | Dato for siste endring på objektdataene | [optional] 
**postnummer** | **str** | Unik identifikasjon av et postnummerområde. Tekstverdi som må bestå av 4 tall. 0340 er for eksempel gyldig, mens 340 er ikke gyldig. | [optional] 
**poststed** | **str** | Navn på poststed i henhold til Postens egne lister | [optional] 
**representasjonspunkt** | [**GeomPoint**](GeomPoint.md) |  | [optional] 
**stedfestingverifisert** | **bool** | Angivelse om stedfestingen (koordinatene) er kontrollert og funnet i orden (verifisert) | [optional] 
**undernummer** | **int** | Fortløpende nummerering av matrikkeladresser med samme gårds-, bruks- og festenummer. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

