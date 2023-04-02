import httpx


# Methods for get balance 

def transactions_history(address: str, chain: str, asset: str, limit:int = 25):
    """Get transactions history for an address

    Args:
        address (str): Address to get the transactions history for Ex: 0x8261c13d6c675f7e8Ec27Eb6d5278023cDdA74E6
        chain (str): Chain to get the transactions history for Ex: bitcoin, smartchain, avalanchec
        asset (str): Asset to get the transactions history for Ex: c0, c10009000, c20000714
        limit (int, optional): Limit of transactions to get. Defaults to 25.

    Returns:
        dict: Transactions history for the address
        Ex: {'total': 0, 'docs': []}
    """
    params = {
        'address': address,
        'asset': asset,
        'version': '4',
        'limit': limit,
    }

    url = f"https://api.trustwallet.com/v2/chains/{chain}/transactions"
    response = httpx.get(url, params=params)
    return response.json()

# for bitcoin
# transactions_history(
#     address='bc1qaarw5djeqzywj4egnlq5lxy9psxwk2x720crkq',
#     chain='bitcoin',
#     asset='c0',
#     limit=25
# )

# for avax
# print(transactions_history(
#     address='0x8261c13d6c675f7e8Ec27Eb6d5278023cDdA74E6',
#     chain='avalanchec',
#     asset='c10009000',
#     limit=25
# ))

# for smartchain
# print(transactions_history(
#     address='0x8261c13d6c675f7e8Ec27Eb6d5278023cDdA74E6',
#     chain='smartchain',
#     asset='c20000714',
#     limit=25
# ))