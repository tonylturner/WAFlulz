#!/usr/bin/env python

def fingerprint(req):
	#instantiate product
	product = None
	#Do headers exist?
	if 'set-cookie' in req.headers:
		retval = re.search(r"X-dotDefender-denied", req.headers)
	else:
		retval = None
    #If value was returned, identify WAF
	if retval:
		product = "dotDefender (Applicure Technologies)"
	if product is not None:
		return product
