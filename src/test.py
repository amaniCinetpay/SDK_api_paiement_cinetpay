from s_d_k import Cinetpay

exemple = Cinetpay("xxxxxx","xxxxxxxxx")

data = {
    'amount' : 00000,  #  Le montant de la transaction                                                                                                                                                                         |
    'currency' : "xxxxx",  # La devise monétaire (XOF, XAF, CDF, GNF)                                       
    'transaction_id' : "xxxxxxxxxxxxxx",  # Identification de la transaction (unique)                       
    'description' : "TRANSACTION DESCRIPTION", # Description du paiement en cours                            
    'return_url' : "https://www.exemple.com/return", # Le lien où le client sera redirigé après le paiement 
    'notify_url' : "https://www.exemple.com/notify", #Le lien de notification du paiement                   
    'customer_name' : "xxxxxxx", # Le nom du client                                                                                                              |
    'customer_surname' : "xxxxxxxxx", #Le prénom du client  
    'apikey' : "XXXXXXX",    # Votre Apikey                                                                
    'site_id' : "XXXXX" ,    # Votre site_id                                                               
    'transaction_id' : "XXXXXX",  # Votre transaction_id                                                    
    'token' : "XXXXXX"  # Le payment_token obtenu lors de l’initialisation du paiement 
}

print(exemple.PaymentInitialization(data))
print(exemple.TransactionVerfication_token("xxxxxxxx"))
