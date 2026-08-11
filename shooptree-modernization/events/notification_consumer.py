from event_bus import Observer


class NotificationConsumer(Observer):

    def update(self, evento):
        if evento["tipo"] == "CompraRealizada":
            print(
                f"Notificação enviada para o cliente "
                f"do pedido {evento['pedido_id']}."
            )