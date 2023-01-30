# / v3 / covid - 19 / countries / {country}
from dataclasses import dataclass
import requests
from requests import Response


'''
 En Python existe un módulo llamado dataclass que permite agregar código auto 
 generado a los métodos especiales de la clase con una sola línea de código
'''
@dataclass
class AllResult:
    updated: int
    cases: int
    flag: str


@dataclass
class AllCountry:
    updated: int
    cases: int
    # flag: str
    countryInfo: dict


# Clase principal
class CovidAPI:
    def __init__(self):
        self._info_url: str = 'https://disease.sh/v3/covid-19/all'
        self._info_country_url: str = 'https://disease.sh/v3/covid-19/countries/'

    '''
    La anotación -> AllResult es una anotación de tipo de retorno, que indica que la función retornará un objeto de 
    tipo AllResult. La anotación de tipo de retorno es opcional en Python, pero ayuda a documentar el tipo de retorno 
    esperado y facilita la tarea de debugging en algunos casos
    '''
    def get_info(self) -> AllResult | dict:
        r: Response = requests.get(self._info_url)
        if r.status_code != 200:
            print('No se ha podido conectar con el servidor')
            return AllResult(updated=0, cases=0, flag='')
        data: dict = r.json()
        # flag = data.get("flag")
        return AllResult(updated=data.get("updated"), cases=data.get("cases"), flag=data.get("flag"))

    def get_country_info(self, country: str) -> AllCountry | dict:
        print(country)
        r: Response = requests.get(self._info_country_url + country)
        if r.status_code != 200:
            print('No se ha podido conectar con el servidor')
            return AllCountry(updated=0, cases=0, countryInfo={})
        data: dict = r.json()
        # flag = self.get_flag(country) flag=flag, flag='',
        return AllCountry(updated=data.get("updated"), cases=data.get("cases"),
                          countryInfo=data.get("countryInfo", {}))


if __name__ == '__main__':
    info: CovidAPI = CovidAPI()
    info_data: AllResult = info.get_info()
    info_country: AllCountry = info.get_country_info('spain')
    print(" Mostramos la info de la url ALL")
    print(info_data.updated)
    print(info_data.cases)
    print(info_data.flag)
    print(" Mostramos la info de la url Country")
    print(info_country.updated)
    print(info_country.cases)
    print(info_country.countryInfo['flag'])
