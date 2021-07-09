import os
from os import listdir, path
from os.path import isfile, join
import pathlib
import json
import random
from werkzeug.exceptions import BadRequest, HTTPException

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
            try:
                file_name_index = files_in_directory.index(file_name)
            except ValueError:
                raise BadRequest

            file_to_open = freg_manual_path + files_in_directory[file_name_index]
            with open(file_to_open, "r") as file:
                return json.loads(file.read())
                
        # If a specific position in the directory containing freg persons is set
        if file_position_in_directory >= 0:
            file_to_open = freg_manual_path + files_in_directory[file_position_in_directory]
            with open(file_to_open, "r") as file:
                return json.loads(file.read())

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

    def get_number_of_files_in_directory(self, local_file_path: str = "\\FREG_manual\\"):
        filepath = str(pathlib.Path(__file__).parent.resolve()) + local_file_path
        return len([f for f in listdir(filepath) if isfile(join(filepath, f))])

    # Saving relevant attributes to variables and discards the rest. 
    def _parse_freg_person_json(self, json_object: json):
        self._identifikasjonsnummer = json_object["identifikasjonsnummer"]
        self._delt_bosted = json_object["deltBosted"] # likely not needed, only relevant for kids
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

    # Helper function to populate the target_dict with values from the original_dict
    def _copy_key_from_dict_to_target(self, key: str, original_dict: dict, target_dict: dict):
        try:
            target_dict[key] = original_dict[key]
        except KeyError:
            target_dict[key] = None

    @property
    def identifikasjonsnummer(self):
        id = {}

        self._copy_key_from_dict_to_target("foedselsEllerDNummer", self._identifikasjonsnummer[0], id)
        self._copy_key_from_dict_to_target("identifikatortype", self._identifikasjonsnummer[0], id)

        return id

    @property
    def delt_bosted(self):
        return self._delt_bosted

    @property
    def sivilstand(self):
        sivil = {}
        self._copy_key_from_dict_to_target("sivilstand", self._sivilstand[0], sivil)
        self._copy_key_from_dict_to_target("sivilstandsdato", self._sivilstand[0], sivil)
        self._copy_key_from_dict_to_target("gyldighetstidspunkt", self._sivilstand[0], sivil)

        return sivil

    @property
    def familierelasjon(self):
        if self._familierelasjon is None:
            return None

        relasjon = [dict() for x in range(len(self._familierelasjon))]
        
        for i in range(len(self._familierelasjon)):
            self._copy_key_from_dict_to_target("minRolleForPerson", self._familierelasjon[i], relasjon[i])
            self._copy_key_from_dict_to_target("relatertPersonsRolle", self._familierelasjon[i], relasjon[i])
            self._copy_key_from_dict_to_target("relatertPerson", self._familierelasjon[i], relasjon[i])

        return relasjon

    @property
    def navn(self):
        navn_dict = {}
        self._copy_key_from_dict_to_target("fornavn", self._navn[0], navn_dict)
        self._copy_key_from_dict_to_target("mellomnavn", self._navn[0], navn_dict)
        self._copy_key_from_dict_to_target("etternavn", self._navn[0], navn_dict)
        self._copy_key_from_dict_to_target("forkortetNavn", self._navn[0], navn_dict)
        self._copy_key_from_dict_to_target("originaltNavn", self._navn[0], navn_dict)

        return navn_dict

    @property
    def adressebeskyttelse(self):
        return self._adressebeskyttelse

    
    @property
    def bostedsadresse(self):
        # Removes any address for a person with "adressebeskyttelse: strengtFortrolig"
        if self._is_address_guarded() or self._bostedsadresse is None:
            return None

        bosted = {}

        # Loop through all adresses and remove anyone with "graderingsnivaa: strengtFortrolig"
        for i in range (len(self._bostedsadresse)):
            if "graderingsnivaa" in self._bostedsadresse[i] and self._bostedsadresse[i]["graderingsnivaa"] == "strengtFortrolig":
                print("Bostedsadresse gradert strengt fortrolig")
                self._bostedsadresse[i] = None
            if "erGjeldende" in self._bostedsadresse[i] and self._bostedsadresse[i]["erGjeldende"]:
                self._copy_key_from_dict_to_target("adresseIdentifikatorFraMatrikkelen", self._bostedsadresse[i], bosted)
                self._copy_key_from_dict_to_target("skolekrets", self._bostedsadresse[i], bosted)
                self._copy_key_from_dict_to_target("vegadresse", self._bostedsadresse[i], bosted)
                self._copy_key_from_dict_to_target("ukjentBosted", self._bostedsadresse[i], bosted)            

        return bosted
        
    @property
    def preferert_kontaktadresse(self):
        # Removes any address for a person with "adressebeskyttelse: strengtFortrolig"
        if self._is_address_guarded() or self._preferert_kontaktadresse is None:
            return None

        kontaktadresse = {}

        # Loop through all adresses and remove anyone with "graderingsnivaa: strengtFortrolig"
        for i in range (len(self._preferert_kontaktadresse)):
            if "graderingsnivaa" in self._preferert_kontaktadresse[i] and self._preferert_kontaktadresse[i]["graderingsnivaa"] == "strengtFortrolig":
                print("Bostedsadresse gradert strengt fortrolig")
                self._preferert_kontaktadresse[i] = None
            if "erGjeldende" in self._preferert_kontaktadresse[i] and self._preferert_kontaktadresse[i]["erGjeldende"]:
                self._copy_key_from_dict_to_target("kontaktadresseIFrittFormat", self._preferert_kontaktadresse[i], kontaktadresse)
                self._copy_key_from_dict_to_target("valg", self._preferert_kontaktadresse[i], kontaktadresse)

        return kontaktadresse
             
    @property
    def postadresse(self):
        # Removes any address for a person with "adressebeskyttelse: strengtFortrolig"
        if self._is_address_guarded() or self._postadresse is None:
            return None

        post = {}

        # Loop through all adresses and remove anyone with "graderingsnivaa: strengtFortrolig"
        for i in range (len(self._postadresse)):
            if "graderingsnivaa" in self._postadresse[i] and self._postadresse[i]["graderingsnivaa"] == "strengtFortrolig":
                print("Postadresse gradert strengt fortrolig")
                self._postadresse[i] = None
            if "erGjeldende" in self._postadresse[i] and self._postadresse[i]["erGjeldende"]:
                self._copy_key_from_dict_to_target("postadresseIFrittFormat", self._postadresse[i], post)
                self._copy_key_from_dict_to_target("postboksadresse", self._postadresse[i], post)
                self._copy_key_from_dict_to_target("vegadresse", self._postadresse[i], post)

        return post
             
    @property
    def foreldreansvar(self):
        ansvar = {}
        if self._foreldreansvar is not None:
            ansvar = [dict() for x in range(len(self._foreldreansvar))]

            for i in range(len(self._foreldreansvar)):
                if "erGjeldende" in self._foreldreansvar[i] and self._foreldreansvar[i]["erGjeldende"]:
                    self._copy_key_from_dict_to_target("ansvar", self._foreldreansvar[i], ansvar[i])
                    self._copy_key_from_dict_to_target("ansvarssubjekt", self._foreldreansvar[i], ansvar[i])
                    self._copy_key_from_dict_to_target("ansvarlig", self._foreldreansvar[i], ansvar[i])
                    self._copy_key_from_dict_to_target("ansvarligUtenIdentifikator", self._foreldreansvar[i], ansvar[i])
                    self._copy_key_from_dict_to_target("ansvarssubjektUtenIdentifikator", self._foreldreansvar[i], ansvar[i])

        return ansvar

    @property
    def foedsel(self):
        birth = {}
        self._copy_key_from_dict_to_target("foedselsaar", self._foedsel[0], birth)
        self._copy_key_from_dict_to_target("foedselsdato", self._foedsel[0], birth)

        return birth

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


# from datetime import date, datetime
# def list_personnummer_of_adults():
#     for i in range(24):
#         person = Person(file_position_in_directory=i)
#         date_of_birth = datetime.strptime(person.foedsel["foedselsdato"], "%Y-%m-%d").date()
#         if date_of_birth < date(2003, 1, 1):
#             print (person.identifikasjonsnummer["foedselsEllerDNummer"])
#             # print (date_of_birth)

# list_personnummer_of_adults()

# person = Person()
# print (person.get_number_of_files_in_directory())