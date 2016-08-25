import socket
import ssl
import base64

def get_cert_pem(domain):
	s = socket.socket()
	c = ssl.wrap_socket(s)
	try:
		c.connect((domain,443))
		cert = c.getpeercert(True)
		pem = "-----BEGIN CERTIFICATE-----\n"+base64.b64encode(cert)+"\n-----END CERTIFICATE-----"
	except:
		pem = 0
	return pem

