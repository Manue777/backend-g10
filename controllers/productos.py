class ProductosController:
    def listaProductos(self):
        productos = [
            {
                'nombre': 'zapatillas Nike',
                'precio': 200.00,
                'talla': 42
            },
            {
                'nombre': 'zapatillas Pumba',
                'precio': 150.00,
                'talla': 41
            }
        ]
        return productos