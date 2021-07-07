import os
from os import listdir, path
from os.path import isfile, join
import pathlib
import json
import random

class Person:
    def __init__(self, local_file_path: str = "\\FREG_manual\\", file_name: str = None, file_position_in_directory: int = -1) -> None:
        person_from_file = self._read_person_from_file(local_file_path=local_file_path, file_name=file_name, file_position_in_directory=file_position_in_directory)
        self._parse_freg_person_json(json_object=person_from_file)

        # self._list_all_keys(person_from_file)

    def _read_person_from_file(self, local_file_path, file_name: str, file_position_in_directory: int):
        parent_filepath = pathlib.Path(__file__).parent.resolve()
        freg_manual_path = str(parent_filepath) + local_file_path
        files_in_directory = [f for f in listdir(freg_manual_path) if isfile(join(freg_manual_path, f))]

        # If a specific filename is set
        if file_name is not None:
            file_to_open = freg_manual_path + files_in_directory[file_name]
            with open(file_to_open, "r") as file:
                return json.loads(file)
                
        # If a specific position in the directory containing freg persons is set
        if file_position_in_directory >= 0:
            file_to_open = freg_manual_path + files_in_directory[file_position_in_directory]
            with open(file_to_open, "r") as file:
                return json.loads(file)

        # If no file is specified, pick a random file
        else:
            if len(files_in_directory) > 1:
                file_position_in_directory = random.randrange(0, len(files_in_directory)-1)
            else: 
                file_position_in_directory = 0

            file_to_open = freg_manual_path + files_in_directory[file_position_in_directory]
            with open(file_to_open, "r") as file:
                return json.loads(file.read())

    def _list_all_keys(self, json_object: json):
        for key in json_object:
            print (key)

    # Saving relevant attributes to variables and discards the rest. 
    def _parse_freg_person_json(self, json_object: json):
        self._identifikasjonsnummer = json_object["identifikasjonsnummer"]
        self._delt_bosted = json_object["deltBosted"]
        self._sivilstand = json_object["sivilstand"]
        self._familierelasjon = json_object["familierelasjon"]
        self._navn = json_object["navn"]
        self._adressebeskyttelse = json_object["adressebeskyttelse"]
        self._bostedsadresse = json_object["bostedsadresse"]
        self._preferert_kontaktadresse = json_object["preferertKontaktadresse"]
        self._postadresse = json_object["postadresse"]
        self._foreldreansvar = json_object["foreldreansvar"]
        self._foedsel = json_object["foedsel"]
        
    # Checks to see if any element in adressebeskyttelse has "graderingsnivaa: strengtFortrolig"
    def _is_address_guarded(self):
        if self.adressebeskyttelse is None:
            return False

        adressebeskyttelse = self.adressebeskyttelse
 
        for i in range(len(adressebeskyttelse)):
            if "graderingsnivaa" in adressebeskyttelse[i] and adressebeskyttelse[i]["graderingsnivaa"] == "strengtFortrolig":
                return True
        
        return False

    @property
    def identifikasjonsnummer(self):
        return self._identifikasjonsnummer

    @property
    def delt_bosted(self):
        return self._delt_bosted

    @property
    def sivilstand(self):
        return self._sivilstand

    @property
    def familierelasjon(self):
        return self._familierelasjon

    @property
    def navn(self):
        return self._navn

    @property
    def adressebeskyttelse(self):
        return self._adressebeskyttelse

    
    @property
    def bostedsadresse(self):
        # Removes any address for a person with "adressebeskyttelse: strengtFortrolig"
        if self._is_address_guarded():
            return None

        # Loop through all adresses and remove anyone with "graderingsnivaa: strengtFortrolig"
        for i in range (len(self._bostedsadresse)):
            if "graderingsnivaa" in self._bostedsadresse[i] and self._bostedsadresse[i]["graderingsnivaa"] == "strengtFortrolig":
                print("Bostedsadresse gradert strengt fortrolig")
                self._bostedsadresse[i] = None

        return self._bostedsadresse
        
    @property
    def preferert_kontaktadresse(self):
        # Removes any address for a person with "adressebeskyttelse: strengtFortrolig"
        if self._is_address_guarded():
            return None

        # Loop through all adresses and remove anyone with "graderingsnivaa: strengtFortrolig"
        for i in range (len(self._preferert_kontaktadresse)):
            if "graderingsnivaa" in self._preferert_kontaktadresse[i] and self._preferert_kontaktadresse[i]["graderingsnivaa"] == "strengtFortrolig":
                print("Bostedsadresse gradert strengt fortrolig")
                self._preferert_kontaktadresse[i] = None

        return self._preferert_kontaktadresse
             
    @property
    def postadresse(self):
        # Removes any address for a person with "adressebeskyttelse: strengtFortrolig"
        if self._is_address_guarded():
            return None

        # Loop through all adresses and remove anyone with "graderingsnivaa: strengtFortrolig"
        for i in range (len(self._postadresse)):
            if "graderingsnivaa" in self._postadresse[i] and self._postadresse[i]["graderingsnivaa"] == "strengtFortrolig":
                print("Postadresse gradert strengt fortrolig")
                self._postadresse[i] = None
        
        return self._postadresse
             
    @property
    def foreldreansvar(self):
        return self._foreldreansvar

    @property
    def foedsel(self):
        return self._foedsel

    # All relevant information on a person
    @property
    def batch(self):
        return {
            "identifikasjonsnummer": self.identifikasjonsnummer,
            "deltBosted": self.delt_bosted,
            "sivilstand": self.sivilstand,
            "familierelasjon": self.familierelasjon,
            "navn": self.navn,
            "bostedsadresse": self.bostedsadresse,
            "preferertKontaktadresse": self.preferert_kontaktadresse,
            "postadresse": self.postadresse,
            "foreldreansvar": self.foreldreansvar,
            "foedsel": self.foedsel
        }
    
# person = Person()

# for key in person.batch:
#     print (person.batch[key])


# print (len(person._bostedsadresse))