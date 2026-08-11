from event_bus import EventBus


class PurchaseProducer:

    def __init__(self, event_bus):
        self.event_bus = event_bus

    def realizar_compra(self, pedido_id, produto_id, valor):
        evento = {
            "tipo": "CompraRealizada",
            "pedido_id": pedido_id,
            "produto_id": produto_id,
            "valor": valor
        }

        print(f"Compra realizada: pedido {pedido_id}")

        self.event_bus.publish(evento)