import os,time,base64
from datetime import datetime,timezone
import pyotp

DATA_SEED = "/data/seed.txt"
OUT_FILE = "/cron/last_code.txt"

def hex_to_base32(hex_seed: str) -> str:
	b = bytes.fromhex(hex-seed)
	return base64.b32encode(b).decode("utf-8")

def main():
	try:
		if not os.path.exists(DATA_SEED):
			raise FileNotFoundError("seed not found")

		with open(DATA_SEED, "r") as f:
			seed = f.read().strip()
		b32 = hex_to_base32(seed)
		totp= pyotp.TOTP(b32, digits=6, interval=30)
		code = totp.now()
		ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
		print(f"{ts} - 2FA Code: {code}")
	exceptn Exception as e:
		print(f"ERR: {e}", flush=True)

if __name__ == "__main__":
	main()
