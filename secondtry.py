# / v3 / covid - 19 / countries / {country}
from dataclasses import dataclass
import requests
from requests import Response


@dataclass
class AllResult:
    updated: int
    cases: int
    flag: str


class CovidAPI:
    def __init__(self):
        self._info_url: str = 'https://disease.sh/v3/covid-19/all'
        self._info_country_url: str = 'https://disease.sh/v3/covid-19/countries/'

    def get_info(self) -> AllResult:
        r: Response = requests.get(self._info_url)
        if r.status_code != 200:
            print('No se ha podido conectar con el servidor')
            return AllResult(updated=0, cases=0, flag='')
        data: dict = r.json()
        return AllResult(updated=data.get("updated"), cases=data.get("cases"), flag=data.get("flag"))

    def get_country_info(self, country: str) -> AllResult | dict:
        print(country)
        r: Response = requests.get(self._info_country_url + country)
        if r.status_code != 200:
            print('No se ha podido conectar con el servidor')
            return AllResult(updated=0, cases=0, flag='')
        data: dict = r.json()
        return AllResult(updated=data.get("updated"), cases=data.get("cases"), flag=data.get("flag"))


if __name__ == '__main__':
    info: CovidAPI = CovidAPI()
    info_data: AllResult = info.get_info()
    info_data_country: AllResult = info.get_country_info('spain')
    print(" Mostramos la info de la url ALL")
    print(info_data.updated)
    print(info_data.cases)
    print(info_data.flag)
    print(" Mostramos la info de la url Country")
    print(info_data_country.updated)
    print(info_data_country.cases)
    print(info_data_country.flag)
