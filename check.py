# use an appropriate path to import
from verifier.verifier import Verifier

# Use normal SMTP to connect to the server
# normal_verifier = Verifier(source_addr='user@example.com') # No proxy
# results = normal_verifier.verify('slabengine@gmail.com')

# Use socks proxy to connect over SMTP
socks_verifier = Verifier(
    source_addr='noreply@verifyemailaddress.org',
    proxy_type='socks5',
    proxy_addr='142.93.51.220',
    proxy_port=61872,
)
response = socks_verifier.verify('test@gmail.com')

print(response)
