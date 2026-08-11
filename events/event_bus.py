from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, evento):
        pass


class EventBus:

    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def publish(self, evento):
        print(f"\nEvento publicado: {evento['tipo']}")

        for observer in self.observers:
            observer.update(evento)