import subprocess, base64,sys
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key

priv_path=sys.argv[1]
pub_pth=sys.argv[2]

commmit=subprocess.check_output(["git","log","-1","--format=%H"]).decode().strip()

with open(priv_path, "rb") as f:
	priv=load_pem_private_key(f.read(), password=None)
with open(pub_path, "rb") as f:
	pub=load_pem_public_key(f.read())

sig=priv.sign(
	commit.encode(),
	padding.PSS(mgf=padding.MGF(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
	hashes.SHA256()
)

enc=pub.encrypt(
	sig,
	padding.OAEP(mgf=padding.MGF(hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)

print("COMMIT_HASH:", commit)
print("ENCRYPTED_SIGNATURE_BASE64:", base64.b64encode(enc).decode())
