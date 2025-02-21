from ninja import ModelSchema,Schema
from .models import Transactions
from decimal import Decimal
from datetime import datetime
from typing import Optional
class TransactionSchema(ModelSchema):
    class Meta:
        model=Transactions
        exclude=['id','date']
        
        
class DepositSchema(Schema):
    user_id:int
    amount:float
    
class TransactionResponseSchema(Schema):
    id: int
    amount: Decimal
    payer:Optional[str]=None
    payee: str  
    date: datetime
 