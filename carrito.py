import math
from numbers import Real


class CarritoCompras:
    """Representa un carrito de compras y sus operaciones."""

    def __init__(self):
        """Inicializa un carrito vacío sin descuento aplicado."""
        self.productos = []
        self.descuento = 0

    def agregar_producto(self, nombre, precio, cantidad):
        """Agrega un producto válido al carrito.

        Args:
            nombre: Nombre descriptivo del producto.
            precio: Precio unitario no negativo.
            cantidad: Cantidad entera mayor que cero.

        Raises:
            ValueError: Si los datos del producto no son válidos.
        """
        self._validar_nombre(nombre)
        self._validar_precio(precio)
        self._validar_cantidad(cantidad)

        self.productos.append({
            "nombre": nombre.strip(),
            "precio": precio,
            "cantidad": cantidad,
        })

    def calcular_subtotal(self):
        """Calcula el subtotal de los productos sin aplicar descuentos."""
        subtotal = sum(
            producto["precio"] * producto["cantidad"]
            for producto in self.productos
        )
        return round(subtotal, 2)

    def aplicar_descuento(self, porcentaje_descuento):
        """Aplica un descuento comprendido entre el 0% y el 50%.

        Raises:
            ValueError: Si el porcentaje no es válido.
        """
        if (
            isinstance(porcentaje_descuento, bool)
            or not isinstance(porcentaje_descuento, Real)
            or not math.isfinite(porcentaje_descuento)
            or not 0 <= porcentaje_descuento <= 50
        ):
            raise ValueError(
                "El descuento debe ser un número entre 0% y 50%"
            )

        self.descuento = porcentaje_descuento

    def calcular_total(self):
        """Calcula el total del carrito después de aplicar el descuento."""
        subtotal = self.calcular_subtotal()
        total = subtotal * (1 - self.descuento / 100)
        return round(total, 2)

    @staticmethod
    def _validar_nombre(nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío")

    @staticmethod
    def _validar_precio(precio):
        if (
            isinstance(precio, bool)
            or not isinstance(precio, Real)
            or not math.isfinite(precio)
            or precio < 0
        ):
            raise ValueError("El precio debe ser un número no negativo")

    @staticmethod
    def _validar_cantidad(cantidad):
        if (
            isinstance(cantidad, bool)
            or not isinstance(cantidad, int)
            or cantidad <= 0
        ):
            raise ValueError("La cantidad debe ser un entero mayor que cero")