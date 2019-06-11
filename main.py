from task import kufar_parser


def get_params(**kwargs) -> dict:
    '''Returns the parameters by which the website is looking for ads.'''
    params = {
        'cat': 1010,
        'cur': 'USD',
        'gbx': 'b:27.479209899902344,53.829230976746196,27.699966430664066,53.9764838398327',
        'cmp': 0,
        'prc': f'r:150,300',
        'size': "300",
        'sort': 'lst.d',
        'typ': 'let',
        'oph': 1
    }
    for param in kwargs:
        if param in params:
            params[param] = kwargs[param]
    return params


def get_api_url() -> str:
    '''Returns the link by which the frontend accesses the site for ads.'''
    return "https://re.kufar.by/api/search/ads-search/v1/engine/v1/search/raw"


if __name__ == '__main__':
    params = get_params()
    api_url = get_api_url()
    links = kufar_parser(api_url, params)
    print(links)
