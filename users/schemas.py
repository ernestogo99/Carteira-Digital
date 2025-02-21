from ninja import ModelSchema,Schema
from .models import User
#o esquema a gente define do 0
# o modelSchema a gente define de um model a partir do banco de dados
#eu espero receber o fields numa requisição do django
class UserSchema(ModelSchema):
    class Meta:
        model=User
        fields=['username','first_name','last_name','cpf','email','password']
        
        
class TypeSchema(Schema):
    type:str
    
    
class TypeUserSchema(Schema):
    user:UserSchema
    type_user:TypeSchema