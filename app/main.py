from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
	return {"message": "FastAPI is working!"}

@app.get("/generate-secret")
def generate_secret():
	secret = pyotp.random_base32()
	return {"secret": secret}

@app.get("/get-otp/{secret}")
def get_otp(secret: str):
	totp = pyotp.TOTP(secret)
	otp = totp.now()
	return {"otp": otp}
