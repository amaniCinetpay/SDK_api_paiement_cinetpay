# Réussir l’intégration de CinetPay sur sa plateforme

Ce SDK facilite l'intégration de la solution de paiement de Cinetpay.
Vous avez la possibilité de l'importer dans votre code comme un package de python.
Pour se faire , 

# 1-vous devez taper la ligne de commande suivante :

pip install -i https://test.pypi.org/simple/ cinetpay-sdk-amaniCinetpay==0.0.1

# 2-Importez le package en tapant la ligne de code suivante dans votre code :

from cinetpay_sdk.s_d_k import Cinetpay

# 3-Utilisation du SDK

Avec ce import, vous avez accès à la classe Cinetpay ainsi que ses méthodes qui vous permettront de communiquer avec le système de Cinetpay à travers des envois de données.

Nous vous conseillons de consulter l'exemple qui se trouve dans le dossier src pour plus de compréhension.



# Préréquis

Avant de procéder à l’intégration de l’api de collecte de fonds, vous devez :
    • Avoir un compte marchand sur www.cinetpay.com ;
    • Récupérer votre APIKEY et votre SITEID dans votre compte marchand ;
Pour ce faire :
    • Rendez-vous sur www.cinetpay.com/login et connectez-vous avec vos accès
    • Cliquer ensuite sur le menu « Intégrations » ;
    • Vous y trouverez votre APIKEY et votre SITEID .

# a-Initialisation de paiement

Pour l'initialisation du paiement, vous avez juste besoin d'instancier la classe Cinetpay puis utiliser 
sa méthode PaymentInitialization en lui passant les variables correctement remplies et ensuite vous aurez 
des retours de Cinetpay que vous exploiterez.
NB : Vous devez sauvegarder le payment_token dans le retour de Cinetpay dans votre base de données.
Nous vous conseillons de consulter l'exemple dans ce SDK pour plus de compréhension.

# b-Page de paiement

Après avoir obtenu l’url de paiement à la requête précédente, il vous suffit juste de lancer cette url dans un
navigateur web pour vous retrouver sur le guichet de paiement, dans le cas des applications mobile, vous
pouvez faire appel à une WebView pour l’exécution du guichet de paiement.Vous avez ainsi fini la première partie de l’intégration CinetPay.

# c-Notification 

Le lien/url de notification (notify_url) est appelé par CinetPay pour vous notifier de l’état d’un paiement.
Cette url doit être disponible pour accueillir des requêtes HTTP de type GET et POST.
Le notify_url doit être le seul mécanisme à implémenter pour synchroniser automatiquement les paiements
vers votre site marchand. CinetPay appellera ce lien après chaque update pour vous notifier du changement
de statuts pendant le déroulement d'une transaction.
A la fin d’un paiement, CinetPay appelle systématiquement l’url de notification pour le service concerné.
Cet appel a pour but d’informer le site marchand de l’état du paiement (même si le client ne revient pas sur
le site). Le marchand pourra ainsi valider sa commande si le paiement est vérifié et accepté.
NB : l’url de notification n’est pas nécessaire si vous n’avez pas besoin d’avoir le statut des paiements dans
votre base de données, car vous avez l’historique de vos paiements dans votre backoffice CinetPay.
Ex : Application de collecte de dons


# d-Configurer l’url de notification

Le serveur exécute une requête de type POST contenant :
    • cpm_trans_id: la variable transaction_id que vous avez envoyé à l’initialisation
    • cpm_site_id : la variable site_id que vous avez envoyé à l’initialisation
NB :
    • CinetPay ne vous enverra pas les informations sur le statut de la transaction pour éviter certaine faille
de sécurité comme le man in the middle.
    • L’url de notification peut être appelée plusieurs fois.
    • Il faudra toujours effectuer un appel à l’API de « Vérification de transaction » de paiement pour
avoir les vraies valeurs du paiement.
Pour vous assurer de l’intégrité des données que vous traitez, vous devez effectuer certaines vérifications :
    - Votre url de notification doit être une api qui attend un appel en POST et en paramètre le
cpm_trans_id (Correspondant à la variable transaction_id) ;
    - Après l’avoir obtenu, vous devez vérifier dans votre base de données que le statut du paiement
concerné est déjà à succès ;
    - Si oui alors vous ne faites plus de mise à jour ;
    - Si non vous devez faire un appel à l’api de vérification de transaction avec le cpm_trans_id, pour
obtenir le statut de la transaction chez CinetPay et mettre ainsi à jour le statut dans votre base de
données.

Afin de l'utiliser dans ce SDk, vous avez juste qu'à instancier la classe Cinetpay puis utiliser soit la méthode
TransactionVerfication_token ou la méthode TransactionVerfication_trx en lui passant le paramètre qui convient.


