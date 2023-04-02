import httpx


def get_tickers(asset_list: list, currency: str = 'usd') -> dict:
    """Get tickers for a list of assets
    
    Args:
        asset_list (list): List of assets Ex: ['c10009000', 'c20000714', 'c0']
        currency (str, optional): Currency to get the price in. Defaults to 'usd'.

    Returns:
        dict: Tickers for the assets
        Ex: {'currency': 'usd', 'tickers': [{'change_24h': -0.19475179, 'provider': 'coinmarketcap', 'price': 17.72365797702719, 'id': 'c10009000', 'slug': 'avalanche'}, {'change_24h': -0.1163446, 'provider': 'coinmarketcap', 'price': 315.6576053766448, 'id': 'c20000714', 'slug': 'bnb'}, {'change_24h': -0.23351999, 'provider': 'coinmarketcap', 'price': 28487.54578954601, 'id': 'c0', 'slug': 'bitcoin'}]}
    """
    data = {
        'assets': asset_list,
        'currency': currency
    }
    response = httpx.post('https://market.trustwallet.com/v1/tickers', json=data)
    return response.json()


def search_asset(query: str, limit: int = 30, offset: int = 0) -> dict:
    """Search for an asset by name or symbol or part of name

    Args:
        query (str): Name or symbol or part of name to search for Ex: avax
        limit (int, optional): Limit of assets to get. Defaults to 30.
        offset (int, optional): Offset of assets to get. Defaults to 0.

    Returns:
        dict: Assets that match the query
        Ex: {"total":9,"docs":[{"name":"AVAX (Portal)","symbol":"AVAX","type":"POLYGON","decimals":18,"asset_id":"c966_t0x7Bb11E7f8b10E9e571E5d8Eace04735fDFB2358a"},{"name":"Staked AVAX","symbol":"sAVAX","type":"AVALANCHE","decimals":18,"asset_id":"c10009000_t0x2b2C81e08f1Af8835a78Bb2A90AE924ACE0eA4bE"},{"name":"AVAX (Portal)","symbol":"AVAX","type":"CW20","decimals":8,"asset_id":"c330_tterra1hj8de24c3yqvcsv9r8chr03fzwsak3hgd8gv3m"},{"name":"AVAX (Portal)","symbol":"AVAX","type":"ERC20","decimals":18,"asset_id":"c60_t0x85f138bfEE4ef8e540890CFb48F620571d67Eda3"},{"name":"Avalanche","symbol":"AVAX","type":"BEP20","decimals":18,"asset_id":"c20000714_t0x1CE0c2827e2eF14D5C4f29a091d735A204794041"},{"name":"Wrapped AVAX","symbol":"WAVAX","type":"AVALANCHE","decimals":18,"asset_id":"c10009000_t0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7"},{"name":"Ankr Staked AVAX","symbol":"ankrAVAX","type":"AVALANCHE","decimals":18,"asset_id":"c10009000_t0xc3344870d52688874b06d844E0C36cc39FC727F6"},{"name":"Wrapped AVAX (Wormhole)","symbol":"WAVAX","type":"SPL","decimals":8,"asset_id":"c501_tKgV1GvrHQmRBY8sHQQeUKwTm2r2h8t4C8qt12Cw1HVE"},{"name":"Wrapped AVAX","symbol":"WAVAX","type":"BEP20","decimals":18,"asset_id":"c20000714_t0x96412902aa9aFf61E13f085e70D3152C6ef2a817"}]}
    """
    params = {
        'query': query,
        'limit': limit,
        'offset': offset,
        'networks' : '',
        'type': 'all',
        'version': 11,
    }
    response = httpx.get('https://api.trustwallet.com/v1/search/assets', params=params)
    return response.json()
