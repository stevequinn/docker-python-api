from dataclasses import dataclass, field
from fastapi import FastAPI, HTTPException, Response

app = FastAPI()

@dataclass
class UselessThing:
    id: str
    name: str
    tags: list[str] = field(default_factory=list)
    description: str = ""

things: dict[str, UselessThing] = {}

for id in range(10):
    thing = UselessThing(id=id,
                         name=f'Thing{id}',
                         tags=['thing', f'T{id}'],
                         description=f'Very useless thing number {id}')
    things[thing.id] = thing

@app.get('/thing/{thing_id}', response_model=UselessThing)
def read_thing(thing_id: int) -> UselessThing:
    if thing_id not in things:
        raise HTTPException(status_code=404, detail='Useless thing not found')
    return things[thing_id]

@app.get("/")
def read_root() -> Response:
    return Response(f'There are {len(things)} useless things available.')
