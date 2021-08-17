from s_d_k import Cinetpay


apikey = "39955468c7a8c0cef1.68322505"    # Votre Apikey                                                                |   #
site_id = "124598"     # Votre site_id  

exemple = Cinetpay(apikey,site_id)


# """"""""""""""""""""""""""""""""""INITIALISATION DE PAIEMENT"""""""""""""""""""""""""""""""""""""""""""""""
#                                                                                                           #
#                                                                                                           #
# ----------------------------Les paramètres obligatoires que vous devez remplir -------------------------  #
#                                                                                                        |  #
data = {               #                                                                                 |  #
    'amount' : 00000,  #  Le montant de la transaction                                                   |  #                                                                                                                             |
    'currency' : "XOF",  # La devise monétaire (XOF, XAF, CDF, GNF)                                      |  #                
    'transaction_id' : "GRD123456789",  # Identification de la transaction (unique)                      |  #                
    'description' : "TRANSACTION DESCRIPTION", # Description du paiement en cours                        |  #         
    'return_url' : "https://www.exemple.com/return",#Le lien où le client sera redirigé après le paiement|  #
    'notify_url' : "https://www.exemple.com/notify", #Le lien de notification du paiement                |  #
    'customer_name' : "exemple", # Le nom du client                                                      |  #                                                  
    'customer_surname' : "exemple", #Le prénom du client                                                 |  #                                                        
}                                   #                                                                    |  #
#---------------------------------------------------------------------------------------------------------  #
exemple.PaymentInitialization(data)                                                                         #
#                                                                                                           #
#                   *****************************************************************                       #
#                   *                 Exemple Réponse Succès:                       *                       #
#                   *                                                               *                       #
#                   *  {                                                            *                       #
#                   *     "code": "201",                                            *                       #
#                   *     "message": "CREATED",                                     *                       #
#                   *     "description": "Transaction created with success",        *                       #
#                   *     "data": {                                                 *                       #
#                   *     "payment_token": "YOUR_TOKEN_HERE",                       *                       #
#                   *     "payment_url": "PAYMENT_URL_HERE"                         *                       #
#                   *     },                                                        *                       #
#                   *    "api_response_id": "RESPONSE_ID_HERE"                      *                       #
#                   *  }                                                            *                       #
#                   *****************************************************************                       #
#                                                                                                           #
#                                                                                                           #
#                   *****************************************************************                       #
#                   *                 Exemple Réponse Erreur                        *                       #
#                   *                                                               *                       #
#                   * {                                                             *                       #
#                   *    "code": "ERROR_CODE",                                      *                       #
#                   *    "message": "ERROR_MESSAGE ",                               *                       #
#                   *    "description": "ERROR_DESCRIPTION",                        *                       #
#                   *    "api_response_id": "RESPONSE_ID_HERE"                      *                       #
#                   * }                                                             *                       #
#                   *****************************************************************                       #
#                                                                                                           #
############################################################################################################




#""""""""""""""""""""""""""""""""""""VERIFICATION DE TRANSACTION""""""""""""""""""""""""""""""""""""""""""""#
#                                                                                                           #
# --------------------Les paramètres obligatoires que vous devez remplir ----------------------------       #
#                                                                                                   |       #
transaction_id = "XXXXXX"  # Votre transaction_id                                                   |       #
token ="XXXXXX"  # Le payment_token obtenu lors de l’initialisation du paiement                     |       #
# ---------------------------------------------------------------------------------------------------       #                                                                                                  
exemple.TransactionVerfication_token("xxxxxxxx")                                                            #
#                                                                                                           #
#                                                                                                           #
#                  *****************************************************************                        #
#                  *                 Exemple Réponse Succès:                       *                        #
#                  *                                                               *                        #
#                  *    {                                                          *                        #
#                  *        "code": "00",                                          *                        #
#                  *        "message": "SUCCES",                                   *                        #
#                  *        "api_response_id": "1617808789.7749",                  *                        #
#                  *        "data": {                                              *                        #
#                  *        "operator_id": "8210407187720",                        *                        #
#                  *        "payment_method": "FLOOZ",                             *                        #
#                  *        "payment_date": "2021-04-07 14:07:24",                 *                        #
#                  *        "phone_number": "0102324373",                          *                        #
#                  *        "phone_prefix": "225"                                  *                        #
#                  *        }                                                      *                        #
#                  *    }                                                          *                        #
#                  *****************************************************************                        #
#                                                                                                           #
#                                                                                                           #                                                                                                         
#                                                                                                           #
#                  *****************************************************************                        #
#                  *                 Exemple Réponse Erreur                        *                        #
#                  *                                                               *                        #
#                  *    {                                                          *                        #
#                  *        "code": "600",                                         *                        #
#                  *        "message": "PAYMENT_FAILED",                           *                        #
#                  *        "api_response_id": "1617808521.2503",                  *                        #
#                  *        "data": {                                              *                        #
#                  *        "payment_method": "OM",                                *                        #
#                  *        "payment_date": " ",                                   *                        #
#                  *        "phone_number": "0749012966",                          *                        #
#                  *        "phone_prefix": "225"                                  *                        #
#                  *        }                                                      *                        #   
#                  *    }                                                          *                        #
#                  *****************************************************************                        #
#                                                                                                           #
#############################################################################################################
