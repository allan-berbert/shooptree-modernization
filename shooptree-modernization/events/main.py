from event_bus import EventBus
from producer import PurchaseProducer
from payment_consumer import PaymentConsumer
from notification_consumer import NotificationConsumer


event_bus = EventBus()

payment_consumer = PaymentConsumer()
notification_consumer = NotificationConsumer()

event_bus.subscribe(payment_consumer)
event_bus.subscribe(notification_consumer)

producer = PurchaseProducer(event_bus)

producer.realizar_compra(
    pedido_id=1001,
    produto_id=1,
    valor=4500.00
)