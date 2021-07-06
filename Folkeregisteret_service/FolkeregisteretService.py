import os
from os import listdir, path
from os.path import isfile, join
import pathlib
import json
import random

# parent_filepath = pathlib.Path(__file__).parent.resolve()
# parent_filepath = pathlib.Path().resolve()
# freg_manual_path = str(parent_filepath) + "/FREG_manual"
# files = [f for f in listdir(freg_manual_path) if isfile(join(freg_manual_path, f))]


class Person:
    def __init__(self, local_file_path: str = "\\FREG_manual\\", file_name: str = None, file_position_in_directory: int = -1) -> None:
        person_from_file = self._read_person_from_file(local_file_path=local_file_path, file_name=file_name, file_position_in_directory=file_position_in_directory)
        self._parse_freg_person_json(json_object=person_from_file)

        self._list_all_keys(person_from_file)

    def _read_person_from_file(self, local_file_path, file_name: str, file_position_in_directory: int):
        parent_filepath = pathlib.Path().resolve()
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
        pass

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
        return self._bostedsadresse
        
    @property
    def preferert_kontaktadresse(self):
        return self._preferert_kontaktadresse
             
    @property
    def postadresse(self):
        return self._postadresse
             
    @property
    def foreldreansvar(self):
        return self._foreldreansvar
    


person = Person()
