from pydantic import BaseModel
          
class Athletes(BaseModel):
    """Modelo de dados para um atleta."""
    name: str
    age: int
