# Summer Camp 2021

Backlog for sommercamp 2021.

#### Kort beskrivelse av utfordringen  

Det skal utarbeides brukersentrerte konsepter for en sammenhengende proaktiv tjeneste som gir redusert foreldrebetaling og gratis kjernetid i barnehage og SFO for husholdninger som faller under inntektsgrensen fastsatt av Stortinget. Det skal utvikles en eller flere prototyper for å teste og vise fram konseptet. Konseptet bør legge vekt på enkle og oppsøkende interaksjoner der brukeren befinner seg, uavhengig av situasjon eller kontekst. Digital assistent.  

#### Teamsammensetning 

Fem systemutviklere, to designere, to jurister og én forvaltningsinformatiker.  
![Illustrasjon av teamet](https://github.com/Altinn/summer-camp-2021/blob/main/Misc/Teamet.png "Illustrasjon av teamet")

#### Prosjektets varighet 

*21. juni til 13. august 2021.*



### Repositories
Løsningen er satt sammen av fem mikrotjenester som til sammen utgjør backend, pluss en react app som frontend. Dokumentasjon finnes i deres respektive repositories.

Type | Link til repo | Beskrivelse
--- | --- | ---
Frontend | [React App](https://github.com/Digihelgeland-Sommercamp/Prototype) | Brukergrensesnitt for søknadsprosessen om redusert foreldrebetaling
Backend | [Hub](https://github.com/Digihelgeland-Sommercamp/hubService) | Hovedmodul som organiserer søknadsprosessen
Backend | [Evaluator](https://github.com/Digihelgeland-Sommercamp/evaluator) | Modul som evaluerer en søknad basert på inputdata
Backend | [Skatteservice](https://github.com/Digihelgeland-Sommercamp/skatteservice) | Modul som henter mockdata basert på data fra Skatteetaten 
Backend | [Folkeregservice](https://github.com/Digihelgeland-Sommercamp/fregService) | Modul som henter mockdata basert på data fra Folkeregistere
Backend | [Expose user](https://github.com/Digihelgeland-Sommercamp/exposeUser) | Modul som har ansvar for interaksjon med intern database

Oversikt over sammensetningen av moduler:

![Oversiktsdiagram over moduler](https://github.com/Altinn/summer-camp-2021/blob/main/Documentation/Architecture/Microservice%20overview.png)

