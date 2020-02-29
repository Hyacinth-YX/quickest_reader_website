import sys
sys.path.append("..")
from django.shortcuts import render
from django.http import HttpResponse
import base64
import json
import django
import datetime
import time
import pymysql
from utils.errors import *

def HttpWrapper(func):

    def exception2message(exception):

        if isinstance(exception,NoValue):
            return [0,"No such File"]
        if isinstance(exception,DuplicateUser):
            return [2,"重复的用户名"]
        if isinstance(exception,MethodError):
            return [3,"请求方法错误"]
        if isinstance(exception,NoUser):
            return [4,"用户不存在"]
        if isinstance(exception,PasswordIncorrect):
            return [5,"密码错误"]
        else:            
            return [1000,str(exception)]

    def Wrapped(*args,**kwargs):

        try:            
            return_value = func(*args,**kwargs)
            if return_value == None:
                return_value = []
        except Exception as e:
            return_value = e
        keys = ["code","message","data"]
        if isinstance(return_value,Exception) :
            values = exception2message(return_value) + [[]]
        else:
            values = [1,"success",return_value]
        response = dict([keys[i],values[i]] for i in range(3))
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return HttpResponse(json.dumps(response))    
            
    return Wrapped

def base64toBytes(base64str):

    import base64
    
    return base64.b64decode(base64str)