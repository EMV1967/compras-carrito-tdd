import pytest

from carrito import CarritoCompras


def test_agregar_producto():
    carrito = CarritoCompras()

    carrito.agregar_producto("Teclado", 25000, 2)

    assert carrito.calcular_subtotal() == 50000


def test_no_agregar_producto_con_precio_negativo():
    carrito = CarritoCompras()

    with pytest.raises(ValueError):
        carrito.agregar_producto("Teclado", -25000, 2)


def test_no_agregar_producto_con_cantidad_cero():
    carrito = CarritoCompras()

    with pytest.raises(ValueError):
        carrito.agregar_producto("Teclado", 25000, 0)


def test_no_agregar_producto_con_cantidad_negativa():
    carrito = CarritoCompras()

    with pytest.raises(ValueError):
        carrito.agregar_producto("Teclado", 25000, -1)


def test_calcular_subtotal_correctamente():
    carrito = CarritoCompras()
    carrito.agregar_producto("Teclado", 25000, 2)
    carrito.agregar_producto("Mouse", 15000, 1)

    assert carrito.calcular_subtotal() == 65000


def test_aplicar_descuento_del_diez_por_ciento():
    carrito = CarritoCompras()
    carrito.agregar_producto("Teclado", 25000, 2)
    carrito.aplicar_descuento(10)

    assert carrito.calcular_total() == 45000


def test_no_permitir_descuento_superior_al_cincuenta_por_ciento():
    carrito = CarritoCompras()

    with pytest.raises(ValueError):
        carrito.aplicar_descuento(51)


def test_permitir_descuento_del_cincuenta_por_ciento():
    carrito = CarritoCompras()
    carrito.agregar_producto("Teclado", 25000, 2)

    carrito.aplicar_descuento(50)

    assert carrito.calcular_total() == 25000


def test_carrito_vacio_tiene_total_cero():
    carrito = CarritoCompras()

    assert carrito.calcular_total() == 0
