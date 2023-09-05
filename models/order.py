class Order():

    def __init__(self, customer_name, order_date, quantity, game_title, delivery_method):
        self.name = customer_name
        self.date = order_date
        self.quantity = quantity
        self.title = game_title
        self.delivery_method = delivery_method
