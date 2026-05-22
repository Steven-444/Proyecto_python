"""
Nombre: Nixon Steven Angarita Serrano
Grupo: 213022_285
Programa: Ingeniería de sistemas
Código fuente: Autoría propia
"""


def calcular_pedido(stock_actual, stock_minimo):
    """
    Calcula la cantidad a pedir según el stock actual.

    Args:
        stock_actual: Cantidad actual en inventario
        stock_minimo: Cantidad mínima requerida

    Returns:
        Cantidad a pedir o 0 si no es necesario
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


INVENTARIO = [
    [101, "Acetaminofen", 5, 10],
    [102, "Clotrimazol", 15, 10],
    [103, "Montelukast", 3, 8],
    [104, "Cetirizina", 20, 15],
    [105, "Prueba de embarazo casera", 2, 5]
]


def main():
    """Función principal para mostrar lista de reabastecimiento."""
    print("LISTA DE REABASTECIMIENTO")
    print("-------------------------")

    for articulo in INVENTARIO:
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]
        stock_maximo = stock_minimo * 2
        cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

        print(f"Artículo: {nombre}")
        print(f"Cantidad actual en inventario: {stock_actual}")
        print(f"Cantidad mínima de abastecimiento: {stock_minimo}")
        print(f"Cantidad máxima de abastecimiento: {stock_maximo}")
        print(f"Cantidad a pedir: {cantidad_pedir}")
        print("-------------------------")


if __name__ == "__main__":
    main()