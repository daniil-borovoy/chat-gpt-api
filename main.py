import g4f
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from dotenv import load_dotenv
from security import api_key_auth

load_dotenv()

g4f.debug.logging = False  # enable logging
g4f.check_version = False  # Disable automatic version checking

# print(g4f.version)  # check version
# print(g4f.Provider.Ails.params)  # supported args

app = FastAPI()


class PromptInput(BaseModel):
    prompt: str


@app.post("/", dependencies=[Depends(api_key_auth)])
def root(req: PromptInput):

    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo,
        messages=[{"content": req.prompt}],
    )

    return response
