import requests


class TestCinetpay :
 
    def __init__(self,apikey,site_id):
  
        self.url_base_1 = 'https://api-checkout.cinetpay.com/v2/payment'  
        self.url_base_2 =  'https://api-checkout.cinetpay.com/v2/payment/check'
        self.apikey = apikey  
        self.site_id = site_id
                                                                                                                                           
    def TestPaymentInitialization(self):

        r = requests.post(self.url_base_1,                                   
                data = {                                                                                  
                    "amount": "50000",                                                                       
                    "apikey": self.apikey,                                                                       
                    "site_id": self.site_id,                                                                     
                    "currency": "XOF",                                                                                                                        
                    "description": "TRANSACTION TEST",                                                             
                    "return_url:": 'https://test/return/',                                                              
                    "notify_url:": 'https://test/notify/',                                                              
                    "customer_name:": 'test',                                                        
                    "customer_surname:": 'test'                                                   
                },                                                                                          
            )   
        print("Payment initialization succeeded")                                                                                            
                                                                                                            
        return r.json()                                                                                                                                                                                   
                                                                                                            
    def TestTransactionVerfication_trx(self) :                                              
                                                                  
        r = requests.post(self.url_base_2,                         
        data = {                                                                                        
        "apikey": self.apikey,                                                                               
        "site_id": self.site_id,                                                                             
        "transaction_id":'DFGHHNJ566666666666666'                                                                
        },                                                                                              
        )   
        print("Transaction verification by transaction ID succeeded")                                                                                              
        print(r.json)                                                                                                  
        return r.json()  

    def TestTransactionVerfication_token(self) :
                                                                                                                                                                                                     
        r = requests.post(self.url_base_2,                         
            data = {                                                                                    
            "apikey": self.apikey,                                                                           
            "site_id": self.site_id,                                                                         
            "token": 'vchcndjjd8522@etrbd'                                                                             
        },                                                                                              
        )        
        print("Transaction verification by token succeeded")                                                                                              
        print(r.json)  
        return r.json()                                                                                      
                                                                                                            

if __name__ == '__main__' :
    test = TestCinetpay("test","test")
    test.TestPaymentInitialization()
    test.TestTransactionVerfication_token()
    test.TestTransactionVerfication_trx()



