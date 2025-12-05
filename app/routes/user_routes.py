from fastapi import APIRouter

router = APIRouter(
	prefix="/user",
	tags=["User"]
)

@router.get("/info")
def get_user_info():
	return {"username: "sridhar", "status": "active"}
