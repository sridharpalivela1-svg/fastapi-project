import pyotp

def generate_otp():
	secret = pyotp.random_base32()
	totp = pyotp.TOTP(secret)
	return {"secret": secret, "otp": totp.now()}
