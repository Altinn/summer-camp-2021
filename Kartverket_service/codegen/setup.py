# coding: utf-8

"""
    Åpent adresse-API fra Kartverket

    API for oppslag av adresser i matrikkelen.             Det er ikke nødvendig med innlogging/autorisasjon for å bruke API-et.             Større funksjonalitetsødeleggende endringer i API-et vil bli annonsert minst 3 måneder i forveien på https://geonorge.no/aktuelt/varsler/Tjenestevarsler/             API-et returnerer kun de første 10 000 resultatene. Hvis man ønsker å hente ned større datasett så anbefales det å laste ned filene som er tilgjengelige fra https://geonorge.no .           # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Åpent adresse-API fra Kartverket",
    author_email="",
    url="",
    keywords=["Swagger", "Åpent adresse-API fra Kartverket"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    API for oppslag av adresser i matrikkelen.             Det er ikke nødvendig med innlogging/autorisasjon for å bruke API-et.             Større funksjonalitetsødeleggende endringer i API-et vil bli annonsert minst 3 måneder i forveien på https://geonorge.no/aktuelt/varsler/Tjenestevarsler/             API-et returnerer kun de første 10 000 resultatene. Hvis man ønsker å hente ned større datasett så anbefales det å laste ned filene som er tilgjengelige fra https://geonorge.no .           # noqa: E501
    """
)