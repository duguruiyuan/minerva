import urllib
import simplejson
from pprint import pprint

gateway = 'http://api.zemanta.com/services/rest/0.0/'
args = {'method': 'zemanta.suggest',
        'api_key': 'em6dgfq7dhyxdfxmyp8jknf3',
        'text': '''syrian chemical weapons''',
        'return_categories': 'dmoz',
        'format': 'json'}            
args_enc = urllib.urlencode(args)

raw_output = urllib.urlopen(gateway, args_enc).read()

output = simplejson.loads(raw_output)

pprint(output)