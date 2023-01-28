import pandas as pd
import requests
import json

from requests import Response
# link https://disease.sh/docs/#/COVID-19%3A%20Worldometers/get_v3_covid_19_all
# link https://disease.sh/docs/#/COVID-19%3A%20Worldometers/get_v3_covid_19_countries__country_

# https://disease.sh/v3/covid-19/countries
class CountriesInfo():
    def __init__(self):
        self.url: str = 'https://disease.sh/v3/covid-19/countries'
        self.response: Response = requests.get(self.url)
        # Creo una lista vacia
        self.data_list: any = []
        if not self.response.status_code == 200:
            self._check_status_code()
        else:
            self._load_data_info()

    def _load_data_info(self):
        self.data: any = self.response.json()
        for self.data in self.data:
            self.updated_value: int = self.data["updated"]
            self.country_name: str = self.data['country']
            self.country_flag: any = self.data['countryInfo']['flag']
            self.country_iso2: str = self.data['countryInfo']['iso2']
            self.country_iso3: str = self.data['countryInfo']['iso3']
            self.country_population: int = self.data['population']
            # print('El pais es {} su bandera es {} su iso2 {} e iso3 {} con poblacion {}'.format(self.country_name, self.country_flag, self.country_iso2, self.country_iso3, self.country_population))
            # agrega esta línea para agregar los datos a la lista
            self.data_list.append({"updated": self.updated_value, "country": self.country_name,
                                   "flag": self.country_flag, "iso2": self.country_iso2, "iso3": self.country_iso3,
                                   "population": self.country_population})
        # Crea el DataFrame a partir de la lista
        self.dataframe = pd.DataFrame(self.data_list)
        # imprime el DataFrame para verificar si los datos estan correctos
        print(self.dataframe)

    def _check_status_code(self):
        status_code: int = self.response.status_code
        if status_code == 200:
            print("La petición se ha realizado correctamente.")
        elif status_code == 404:
            print("La página no ha sido encontrada.")
        else:
            print(f"Se ha producido un error con código {status_code}.")


# https://disease.sh/v3/covid-19/all
class InfoAll():
    def __init__(self):
        self.url: str = 'https://disease.sh/v3/covid-19/all'
        self.response: Response = requests.get(self.url)

        if not self.response.status_code == 200:
            self._check_status_code()
        else:
            self.data: any = self.response.json()
            self.updata: int = self.data['updated']
            print('All info {}'.format(str(self.updata)))

    def _check_status_code(self):
        status_code = self.response.status_code
        if status_code == 200:
            print("La petición se ha realizado correctamente.")
        elif status_code == 404:
            print("La página no ha sido encontrada.")
        else:
            print(f"Se ha producido un error con código {status_code}.")


if __name__ == '__main__':
    countries = CountriesInfo()
    infoAll = InfoAll()