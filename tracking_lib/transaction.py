import inspect
from fastapi import FastAPI, Request
from flask import Flask, g

class Transaction:

    @classmethod
    def find_object_of_type(cls, obj_type):
        frame = inspect.currentframe()
        while frame:
            local_vars = frame.f_locals
            for var_name, var_value in local_vars.items():
                if isinstance(var_value, obj_type):
                    return var_value
            frame = frame.f_back
        return None

    @classmethod
    def find_flask_app(cls):
        return cls.find_object_of_type(Flask)
    
    @classmethod
    def find_fastapi_app(cls):
        return cls.find_object_of_type(FastAPI)
        
    @classmethod
    def find_fast_api_request_object(cls):
        return cls.find_object_of_type(Request)
    
    @classmethod
    def set_flask_transaction_id(cls, transaction_id):
        g.transaction_id = transaction_id

    @classmethod
    def set_fastapi_transaction_id(cls, transaction_id):
        req_obj = cls.find_fast_api_request_object()
        if req_obj:
            req_obj.state.transaction_id = transaction_id
        else:
            print("Request object not found")

    @classmethod
    def set_transaction_id(cls, transaction_id):
        if cls.find_flask_app():
            print("FLASK-1")
            cls.set_flask_transaction_id(transaction_id)
        elif cls.find_fastapi_app():
            print(" FAST API")
            cls.set_fastapi_transaction_id(transaction_id)
        else:
            print("NO APP", flush=True)
            cls.set_fastapi_transaction_id(transaction_id)
            #cls.set_flask_transaction_id(transaction_id)
            print("No app found")

    @classmethod
    def read_transaction_id(cls):
        if cls.find_flask_app():
            return g.transaction_id
        elif cls.find_fastapi_app():
            req_obj = cls.find_fast_api_request_object()
            if req_obj:
                return req_obj.state.transaction_id
            else:
                return None
        else:
            print("No app found")
            return g.transaction_id