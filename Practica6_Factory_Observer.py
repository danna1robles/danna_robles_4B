#Factory Pattern — Fábrica de métodos de entrega 

#Idea: la florería decide automáticamente qué tipo de entrega usar (bicicleta, coche, dron) según la distancia, el tamaño del pedido o restricciones. La Factory encapsula la lógica de creación de objetos concretos (Delivery) y evita if/elif repartidos por toda la app.
#Cuándo usar: cuando tienes varias implementaciones intercambiables de una familia de objetos y quieres delegar la creación a un único lugar (fácil extensión y pruebas).

"""
Factory Pattern - Fábrica de medios de entrega para una florería.

Clases:
- Delivery (interface/base): método deliver()
- BikeDelivery, CarDelivery, DroneDelivery: implementaciones concretas
- DeliveryFactory: clase que decide qué Delivery crear según parámetros
"""

from abc import ABC, abstractmethod

# ---------- Interfaz / Clase base ----------
class Delivery(ABC):
    @abstractmethod
    def deliver(self, order_id: str):
        """Realiza la entrega (simulada)."""
        pass

# ---------- Implementaciones concretas ----------
class BikeDelivery(Delivery):
    def __init__(self):
        # parámetros específicos (velocidad, costo base, etc.)
        self.speed_kmh = 15

    def deliver(self, order_id: str):
        print(f"[Bike] Entrega del pedido {order_id}: entregando en zona cercana. (vel {self.speed_kmh} km/h)")

class CarDelivery(Delivery):
    def __init__(self):
        self.speed_kmh = 50

    def deliver(self, order_id: str):
        print(f"[Car] Entrega del pedido {order_id}: ruta interurbana o pedidos grandes. (vel {self.speed_kmh} km/h)")

class DroneDelivery(Delivery):
    def __init__(self):
        self.speed_kmh = 60
        self.requires_clear_weather = True

    def deliver(self, order_id: str):
        print(f"[Drone] Entrega del pedido {order_id}: entrega rápida y aérea (vel {self.speed_kmh} km/h).")

# ---------- Factory ----------
class DeliveryFactory:
    @staticmethod
    def create_delivery(distance_km: float, weight_kg: float, weather_ok: bool = True) -> Delivery:
        """
        Decide qué tipo de medio de entrega crear según:
        - distance_km: distancia aproximada
        - weight_kg: peso del pedido
        - weather_ok: si el clima permite drones
        Reglas de ejemplo (ajustables):
        - Drones para distancias <= 5km y peso <= 2kg y clima favorable
        - Bicicleta para distancias <= 7km y peso <= 8kg
        - Coche para el resto
        """
        # Nota: lógica centralizada → fácil de probar y modificar
        if distance_km <= 5 and weight_kg <= 2 and weather_ok:
            return DroneDelivery()
        if distance_km <= 7 and weight_kg <= 8:
            return BikeDelivery()
        return CarDelivery()

# ---------- Simulación de uso ----------
def simulate_order(order_id, distance_km, weight_kg, weather_ok=True):
    print(f"\n-- Pedido {order_id}: distancia={distance_km}km, peso={weight_kg}kg, clima_ok={weather_ok}")
    delivery = DeliveryFactory.create_delivery(distance_km, weight_kg, weather_ok)
    delivery.deliver(order_id)

if __name__ == "__main__":
    # Casos de prueba
    simulate_order("ORD-001", distance_km=2.0, weight_kg=1.0, weather_ok=True)   # drone
    simulate_order("ORD-002", distance_km=4.0, weight_kg=5.0, weather_ok=True)   # bike
    simulate_order("ORD-003", distance_km=15.0, weight_kg=10.0, weather_ok=True) # car
    simulate_order("ORD-004", distance_km=3.0, weight_kg=1.5, weather_ok=False)  # car (drone no puede)


#Observer Pattern — Seguimiento de estado del pedido 

#Idea: cuando el estado de un pedido cambia (aceptado, en preparación, en reparto, entregado), queremos notificar automáticamente a varios observadores (cliente — notificación, panel de administrador, tracker de entrega, sistema de estadísticas). El patrón Observer (sujeto/observables + observadores) resuelve esto.
#Cuándo usar: cuando múltiples objetos deben reaccionar a cambios en otro objeto sin acoplarse fuertemente; facilita añadir nuevos observadores sin tocar el sujeto.

"""
Observer Pattern - Notificaciones del estado del pedido

Clases:
- Subject / Order: mantiene estado y lista de observers
- Observer (interface) y varios observers concretos:
   - CustomerNotifier: notifica al cliente
   - AdminDashboard: muestra logs en consola (simulación)
   - DeliveryTracker: actualiza estado del repartidor
"""

from abc import ABC, abstractmethod
from typing import List

# ---------- Observer base ----------
class Observer(ABC):
    @abstractmethod
    def update(self, subject, message: str):
        pass

# ---------- Subject ----------
class Order:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self._observers: List[Observer] = []
        self._status = "CREADO"

    # métodos de gestión de observadores
    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str):
        # Notifica a todos los observadores
        for obs in list(self._observers):  # copia para evitar problemas si un observer se quita dentro del loop
            obs.update(self, message)

    # cambios de estado del pedido (ejemplo de API del Subject)
    def set_status(self, new_status: str):
        self._status = new_status
        full_message = f"Pedido {self.order_id}: {new_status}"
        print(f"\n[Order] Cambio de estado: {full_message}")
        self.notify(full_message)

    @property
    def status(self):
        return self._status

# ---------- Observers concretos ----------
class CustomerNotifier(Observer):
    def __init__(self, customer_email: str):
        self.customer_email = customer_email

    def update(self, subject: Order, message: str):
        # Simulamos envío de notificación
        print(f"[CustomerNotifier -> {self.customer_email}] Notificación: {message}")

class AdminDashboard(Observer):
    def update(self, subject: Order, message: str):
        # Simula actualización del panel de administración
        print(f"[AdminDashboard] Actualizado estado del pedido en panel: {message}")

class DeliveryTracker(Observer):
    def update(self, subject: Order, message: str):
        # Podría activar acciones del sistema de reparto (ej. asignar repartidor)
        print(f"[DeliveryTracker] Repartidor recibido: {message}")
        # Ejemplo: si se marca 'EN_REPARTO', iniciar tracking GPS (simulado)
        if "EN_REPARTO" in message:
            print(f"[DeliveryTracker] Iniciando tracking GPS para {subject.order_id}")

# ---------- Simulación de flujo ----------
def simulate_order_flow():
    order = Order("ORD-100")
    customer_notifier = CustomerNotifier("cliente@example.com")
    admin_panel = AdminDashboard()
    tracker = DeliveryTracker()

    # Adjuntamos observadores
    order.attach(customer_notifier)
    order.attach(admin_panel)
    order.attach(tracker)

    # Flujo normal del pedido
    order.set_status("ACEPTADO")
    order.set_status("EN_PREPARACION")
    order.set_status("EN_REPARTO")
    order.set_status("ENTREGADO")

    # Ejemplo: cliente decide cancelar notificaciones
    order.detach(customer_notifier)
    order.set_status("ARCHIVADO")

if __name__ == "__main__":
    simulate_order_flow()