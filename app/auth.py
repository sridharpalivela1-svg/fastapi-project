import pyotp

def generete_otp_sectret():
	return pyotp.random_base32()
def get_otp)(secret):
	totp = pyotp.TOTP(secret)
	return totp.now()
