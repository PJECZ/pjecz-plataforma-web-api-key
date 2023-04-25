"""
Schemas Base
"""
from pydantic import BaseModel


class OneBaseOut(BaseModel):
    """BaseOut"""

    success: bool = True
    message: str = "Consulta realizada con éxito"
