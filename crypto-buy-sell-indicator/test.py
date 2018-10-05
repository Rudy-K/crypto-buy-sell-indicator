import json
import cryptocompare
import datetime
print(json.loads(cryptocompare.get_historical_price('XMR', 'USD', datetime.datetime.now())))