# Use this script to query DNS for A records
# requirements
#   python 3.8
#   pip install dnspython

import dns.resolver


domain_list = [
    'google.com',
    'www.google.com',
    
    ]

    
for domain in domain_list:
    print('\nIPs for ' + domain + ':')
    query = dns.resolver.resolve(domain, 'A').rrset.items
    for key, item in query.items():
        print(key)
print('\n')
