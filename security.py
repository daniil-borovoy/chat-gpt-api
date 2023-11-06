from dotenv import dotenv_values
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette import status

api_key = config = dotenv_values(".env")['API_KEY']

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def api_key_auth(key: str = Depends(oauth2_scheme)):
    if key != api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )
