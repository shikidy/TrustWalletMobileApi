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

