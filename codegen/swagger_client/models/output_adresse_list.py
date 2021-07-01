# coding: utf-8

"""
    Åpent adresse-API fra Kartverket

    API for oppslag av adresser i matrikkelen.             Det er ikke nødvendig med innlogging/autorisasjon for å bruke API-et.             Større funksjonalitetsødeleggende endringer i API-et vil bli annonsert minst 3 måneder i forveien på https://geonorge.no/aktuelt/varsler/Tjenestevarsler/             API-et returnerer kun de første 10 000 resultatene. Hvis man ønsker å hente ned større datasett så anbefales det å laste ned filene som er tilgjengelige fra https://geonorge.no .           # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OutputAdresseList(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'adresser': 'list[OutputAdresse]',
        'metadata': 'HitMetadata'
    }

    attribute_map = {
        'adresser': 'adresser',
        'metadata': 'metadata'
    }

    def __init__(self, adresser=None, metadata=None):  # noqa: E501
        """OutputAdresseList - a model defined in Swagger"""  # noqa: E501
        self._adresser = None
        self._metadata = None
        self.discriminator = None
        if adresser is not None:
            self.adresser = adresser
        if metadata is not None:
            self.metadata = metadata

    @property
    def adresser(self):
        """Gets the adresser of this OutputAdresseList.  # noqa: E501


        :return: The adresser of this OutputAdresseList.  # noqa: E501
        :rtype: list[OutputAdresse]
        """
        return self._adresser

    @adresser.setter
    def adresser(self, adresser):
        """Sets the adresser of this OutputAdresseList.


        :param adresser: The adresser of this OutputAdresseList.  # noqa: E501
        :type: list[OutputAdresse]
        """

        self._adresser = adresser

    @property
    def metadata(self):
        """Gets the metadata of this OutputAdresseList.  # noqa: E501


        :return: The metadata of this OutputAdresseList.  # noqa: E501
        :rtype: HitMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this OutputAdresseList.


        :param metadata: The metadata of this OutputAdresseList.  # noqa: E501
        :type: HitMetadata
        """

        self._metadata = metadata

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(OutputAdresseList, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OutputAdresseList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
