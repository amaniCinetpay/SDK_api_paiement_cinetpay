class Exceptions :
    def __init__(self) :
        pass
    def exceptions(data) :
        if "amount" not in data :
            msg = "amount is required"
            return msg
        elif "currency" not in  data:
            msg = "currency is required"
            return msg
        elif "return_url" not in  data:
            msg = "return_url is required"
            return msg
        elif "notify_url" not in  data:
            msg = "notify_url is required"
            return msg
        elif "customer_name" not in  data:
            msg = "customer_name is required"
            return msg
        elif "customer_surname" not in  data:
            msg = "customer_surname is required"
            return msg