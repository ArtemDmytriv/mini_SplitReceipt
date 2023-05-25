import requests

curr_api_url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies'

cache_rates = { 'uah/uah' : 1.0 }

def schedule_rate_update():
    global cache_rates
    print("Updating current currencies rates")
    for k in cache_rates.keys():
        new_rate = get_curr_rate(k)
        if new_rate:
            cache_rates[k] = new_rate

def get_curr_rate(conv_str: str) -> float | None:
    r = requests.get(curr_api_url + f'/{conv_str}.json')
    if not r.ok:
        print(f"Error to parse {conv_str}")
        return None

    print(f"Parse OK: {conv_str}")
    _, to_str = conv_str.split('/')
    return float(r.json()[to_str])

def convert_rate(from_c: str, to_c: str):
    global cache_rates
    from_c = from_c.lower()
    to_c = to_c.lower()

    rate_str = f'{from_c}/{to_c}'
    
    val = None
    if rate_str not in cache_rates : 
        val = get_curr_rate(rate_str)
        if val:
            cache_rates[rate_str] = val
    else:
        val = cache_rates[rate_str]

    return val

def get_amount_different_currency(amount, from_c: str, to_c: str = 'UAH'):
    conv_r = convert_rate(from_c, to_c)
    return conv_r * amount

