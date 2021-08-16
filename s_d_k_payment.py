import requests



# """"""""""""""""""""""""""""""""""INITIALISATION DE PAIEMENT"""""""""""""""""""""""""""""""""""""""""""
#                                                                                                       #
#                                                                                                       #
# ----------------------Les paramètres obligatoires que vous devez remplir --------------------------   #
#                                                                                                   |   #
amount = 00000  #  Le montant de la transaction                                                     |   #
apikey = "XXXXXXXXXXXXXXXX" # Votre apikey                                                          |   #
site_id= "XXXXX",  # Votre site_id                                                                  |   #                                                      |
currency= "xxxxx"  # La devise monétaire (XOF, XAF, CDF, GNF)                                       |   #
transaction_id= "xxxxxxxxxxxxxx"  # Identification de la transaction (unique)                       |   #
description="TRANSACTION DESCRIPTION" # Description du paiement en cours                            |   #
return_url= "https://www.exemple.com/return" # Le lien où le client sera redirigé après le paiement |   #
notify_url= "https://www.exemple.com/notify" #Le lien de notification du paiement                   |   #
customer_name= "xxxxxxx" # Le nom du client                                                         |   #                                                     |
customer_surname= "xxxxxxxxx" #Le prénom du client                                                  |   #
#----------------------------------------------------------------------------------------------------   #
#                                                                                                       #
#                                                                                                       #
def PaymentInitialization():                                                                            #                                                   
                                                                                                        #
    r = requests.post('https://api-checkout.cinetpay.com/v2/payment',                                   #
              data = {                                                                                  #
                "amount": amount,                                                                       #
                "apikey": apikey,                                                                       #
                "site_id": site_id,                                                                     #
                "currency": currency,                                                                   #
                "transaction_id": transaction_id,                                                       #
                "description": description,                                                             #
                "return_url:": return_url,                                                              #
                "notify_url:": notify_url,                                                              #
                "customer_name:": customer_name,                                                        #
                "customer_surname:": customer_surname                                                   #
            },                                                                                          #
        )                                                                                               #
                                                                                                        #
    return r.json()                                                                                     #
#                                                                                                       #
#                                                                                                       #
#                                                                                                       #
#                   *****************************************************************                   #
#                   *                 Exemple Réponse Succès:                       *                   #
#                   *                                                               *                   #
#                   *  {                                                            *                   #
#                   *     "code": "201",                                            *                   #
#                   *     "message": "CREATED",                                     *                   #
#                   *     "description": "Transaction created with success",        *                   #
#                   *     "data": {                                                 *                   #
#                   *     "payment_token": "YOUR_TOKEN_HERE",                       *                   #
#                   *     "payment_url": "PAYMENT_URL_HERE"                         *                   #
#                   *     },                                                        *                   #
#                   *    "api_response_id": "RESPONSE_ID_HERE"                      *                   #
#                   *  }                                                            *                   #
#                   *****************************************************************                   #
#                                                                                                       #
#                                                                                                       #
#                   *****************************************************************                   #
#                   *                 Exemple Réponse Erreur                        *                   #
#                   *                                                               *                   #
#                   * {                                                             *                   #
#                   *    "code": "ERROR_CODE",                                      *                   #
#                   *    "message": "ERROR_MESSAGE ",                               *                   #
#                   *    "description": "ERROR_DESCRIPTION",                        *                   #
#                   *    "api_response_id": "RESPONSE_ID_HERE"                      *                   #
#                   * }                                                             *                   #
#                   *****************************************************************                   #
#                                                                                                       #
#########################################################################################################




#""""""""""""""""""""""""""""""""""""VERIFICATION DE TRANSACTION""""""""""""""""""""""""""""""""""""""""#
#                                                                                                       #
# --------------------Les paramètres obligatoires que vous devez remplir ----------------------------   #
apikey = "XXXXXXX"    # Votre Apikey                                                                |   #
site_id = "XXXXX"     # Votre site_id                                                               |   #
transaction_id = "XXXXXX"  # Votre transaction_id                                                    |   #
token ="XXXXXX"  # Le payment_token obtenu lors de l’initialisation du paiement                     |   #
# ---------------------------------------------------------------------------------------------------   #                                                                                                  
                                                                                                        #
def TransactionVerfication(token,transaction_id) :                                                      #
                                                                                                        #
    if token != 'XXXXXX' :                                                                              #                                                                         #
                                                                                                        #
        r = requests.post('https://api-checkout.cinetpay.com/v2/payment/check',                         #
            data = {                                                                                    #
            "apikey": apikey,                                                                           #
            "site_id": site_id,                                                                         #
            "token": token                                                                              #
        },                                                                                              #
        )                                                                                               #
                                                                                                        #
    elif transaction_id != 'XXXXXX' :                                                                    #
        r = requests.post('https://api-checkout.cinetpay.com/v2/payment/check',                         #
        data = {                                                                                        #
        "apikey": apikey,                                                                               #
        "site_id": site_id,                                                                             #
        "transaction_id": transaction_id                                                                #
        },                                                                                              #
        )                                                                                               #
                                                                                                        #
    return r.json()                                                                                     #
#                                                                                                       #
#                                                                                                       #
#                                                                                                       #
#                  *****************************************************************                    #
#                  *                 Exemple Réponse Succès:                       *                    #
#                  *                                                               *                    #
#                  *    {                                                          *                    #
#                  *        "code": "00",                                          *                    #
#                  *        "message": "SUCCES",                                   *                    #
#                  *        "api_response_id": "1617808789.7749",                  *                    #
#                  *        "data": {                                              *                    #
#                  *        "operator_id": "8210407187720",                        *                    #
#                  *        "payment_method": "FLOOZ",                             *                    #
#                  *        "payment_date": "2021-04-07 14:07:24",                 *                    #
#                  *        "phone_number": "0102324373",                          *                    #
#                  *        "phone_prefix": "225"                                  *                    #
#                  *        }                                                      *                    #
#                  *    }                                                          *                    #
#                  *****************************************************************                    #
#                                                                                                       #
#                                                                                                       #                                                                                                        
#                                                                                                       #
#                  *****************************************************************                    #
#                  *                 Exemple Réponse Erreur                        *                    #
#                  *                                                               *                    #
#                  *    {                                                          *                    #
#                  *        "code": "600",                                         *                    #
#                  *        "message": "PAYMENT_FAILED",                           *                    #
#                  *        "api_response_id": "1617808521.2503",                  *                    #
#                  *        "data": {                                              *                    #
#                  *        "payment_method": "OM",                                *                    #
#                  *        "payment_date": " ",                                   *                    #
#                  *        "phone_number": "0749012966",                          *                    #
#                  *        "phone_prefix": "225"                                  *                    #
#                  *        }                                                      *                    #
#                  *    }                                                          *                    #
#                  *****************************************************************                    #
#                                                                                                       #
#########################################################################################################
