# coding: utf-8

"""
    Åpent adresse-API fra Kartverket

    API for oppslag av adresser i matrikkelen.             Det er ikke nødvendig med innlogging/autorisasjon for å bruke API-et.             Større funksjonalitetsødeleggende endringer i API-et vil bli annonsert minst 3 måneder i forveien på https://geonorge.no/aktuelt/varsler/Tjenestevarsler/             API-et returnerer kun de første 10 000 resultatene. Hvis man ønsker å hente ned større datasett så anbefales det å laste ned filene som er tilgjengelige fra https://geonorge.no .           # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.output_geo_point import OutputGeoPoint  # noqa: E501
from swagger_client.rest import ApiException


class TestOutputGeoPoint(unittest.TestCase):
    """OutputGeoPoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOutputGeoPoint(self):
        """Test OutputGeoPoint"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.output_geo_point.OutputGeoPoint()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()