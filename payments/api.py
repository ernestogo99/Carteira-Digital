from ninja import Router
from .schemas import TransactionSchema,DepositSchema,TransactionResponseSchema
from django.shortcuts import get_object_or_404
from django.db.models import Q
from users.models import User
from.models import Transactions
from rolepermissions.checkers import has_permission
from django.db import transaction as django_transaction
from django.conf import settings
from decimal import Decimal
from datetime import datetime
import requests
payments_router=Router(tags=['Operações'])


@payments_router.post('/',response={200:dict,400:dict,403:dict})
def transaction(request,transaction:TransactionSchema):
    """ 
     Rota para realizar a transferência de dinheiro de um usuário para outro
    """ 
    
    payer=get_object_or_404(User,id=transaction.payer)
    payee=get_object_or_404(User,id=transaction.payee)
    
    if payer.amount<transaction.amount:
        return 400, {'error':'Saldo insuficiente'}
    
    if not has_permission(payer,"make_transfer"):
        return 403, {"error":'você não possui permissão para realizar transferências'}
    
   
    with django_transaction.atomic():
        payer.pay(transaction.amount)
        payee.receive(transaction.amount)
        
        transct=Transactions(
            amount=transaction.amount,
            payer_id=transaction.payer,
            payee_id=transaction.payee
        )
        payer.save()
        payee.save()
        transct.save()
        
        response=requests.get(settings.AUTHORIZE_TRANSFER_ENDPOINT).json()
        if response.get('status')!='authorized':
            raise Exception()

       
    return 200, {'transaction_id':1}


@payments_router.post('/deposit',response={200:dict,400:dict})
def deposit(request,deposit:DepositSchema):
    """
    Rota para realizar um depósito na conta do usuário
    """
    user=get_object_or_404(User,id=deposit.user_id)
    
    if deposit.amount <= 0:
        return 400, {"error": "O valor do depósito deve ser maior que zero."}
    
    with django_transaction.atomic():
        user.receive(Decimal(deposit.amount))
        user.save()
    return 200, {"message": f"Depósito de R$ {deposit.amount:.2f} foi realizado com sucesso!", "novo saldo": float(user.amount)}    
    

@payments_router.get('/transactions/{user_id}', response={200: list[TransactionResponseSchema], 400: dict})
def list_transactions_by_id(request, user_id: int, start_date: datetime = None, end_date: datetime = None):
    """ 
    Rota para obter as transações realizadas por certo usuário,com filtro opcional por data
    """
    user = get_object_or_404(User, id=user_id)

   
    filters = Q(payer=user)


    if start_date:
        filters &= Q(date__gte=start_date)  
    if end_date:
        filters &= Q(date__lte=end_date)  

    transactions = Transactions.objects.filter(filters).order_by('-date')  
    
 
    response_data = [
        {
            "id": trans.id,
            "amount": trans.amount,
            "payee": trans.payee.get_full_name(),  
            "date": trans.date
        }
        for trans in transactions
    ]

    return 200, response_data

@payments_router.get('/transactions/', response={200: list[TransactionResponseSchema], 400: dict})
def get_all_transactions(request):
    """
    Rota para obter todas as transações realizadas.
    """
    transactions=Transactions.objects.all()
    
    response_data = [
        {
            "id": trans.id,
            "amount": trans.amount,
            "payer":trans.payer.get_full_name(),
            "payee": trans.payee.get_full_name(),  
            "date": trans.date
        }
        for trans in transactions
    ]

    return 200, response_data