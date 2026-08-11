from event_bus import Observer


class PaymentConsumer(Observer):

    def update(self, evento):
        if evento["tipo"] == "CompraRealizada":
            print(
                f"Pagamento recebido para o pedido "
                f"{evento['pedido_id']}: R$ {evento['valor']:.2f}"
            )

            print("Pagamento processado com sucesso.")