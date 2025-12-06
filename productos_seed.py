import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()



from productos.models import Categoria, Producto, Etiqueta, DetalleProducto
from decimal import Decimal
import random

# --------------------
# 1. Categorías
# --------------------
categorias_data = [
    ("Pociones", "Preparados líquidos de alquimia con efectos mágicos o medicinales."),
    ("Insumos Alquímicos", "Materiales base utilizados en la creación de pócimas."),
    ("Artefactos Mágicos", "Objetos encantados utilizados por alquimistas y magos."),
    ("Catalizadores", "Objetos especiales que potencian la alquimia."),
]

categorias = {}
for nombre, descripcion in categorias_data:
    cat = Categoria.objects.create(nombre=nombre, descripcion=descripcion)
    categorias[nombre] = cat

# --------------------
# 2. Etiquetas
# --------------------
etiquetas_data = [
    "curación", "veneno", "fuego", "hielo", "raro", "legendario", "oscuro",
    "luminoso", "rápido", "lento", "best seller", "experimental", "antiguo",
    "fragante", "peligroso", "bendito", "maldito", "estable", "inestable",
]

etiquetas = {}
for nombre in etiquetas_data:
    tag = Etiqueta.objects.create(nombre=nombre)
    etiquetas[nombre] = tag

# --------------------
# 3. Productos (50 ítems aprox)
# --------------------

productos_data = [
    # 15 Pociones
    ("Poción de Curación Menor", "Restaura una pequeña cantidad de salud.", 50, "Pociones"),
    ("Poción de Curación Mayor", "Restaura una gran cantidad de salud.", 120, "Pociones"),
    ("Poción de Maná", "Permite recuperar energía mágica.", 80, "Pociones"),
    ("Elixir de Fuego", "Otorga poder ígneo durante unos minutos.", 200, "Pociones"),
    ("Tónico de Resistencia", "Aumenta temporalmente la resistencia física.", 150, "Pociones"),
    ("Vial de Agilidad", "Incrementa la velocidad del usuario brevemente.", 95, "Pociones"),
    ("Poción Antídoto", "Neutraliza toxinas.", 60, "Pociones"),
    ("Poción de Invisibilidad Breve", "Oculta al usuario por pocos segundos.", 300, "Pociones"),
    ("Té Arcano Concentrado", "Potencia la concentración del mago.", 110, "Pociones"),
    ("Tónico Somnífero", "Induce al sueño profundo.", 40, "Pociones"),
    ("Vial Criogénico", "Inflige daño de hielo al contacto.", 130, "Pociones"),
    ("Brebaje Explosivo", "Perfecto para experimentos… o problemas.", 180, "Pociones"),
    ("Poción de Regeneración", "Regenera salud de forma continua.", 250, "Pociones"),
    ("Poción de Huesos Fuertes", "Refuerza la estructura ósea.", 70, "Pociones"),
    ("Mezcla de Vitalidad", "Energiza cuerpo y mente.", 90, "Pociones"),

    # 20 Insumos alquímicos
    ("Raíz de Mandrágora", "Ingrediente fundamental para pociones de vida.", 35, "Insumos Alquímicos"),
    ("Polvo de Hada", "Material brillante con propiedades estabilizantes.", 55, "Insumos Alquímicos"),
    ("Escamas de Dragón", "Potente catalizador mágico.", 500, "Insumos Alquímicos"),
    ("Lágrimas de Fénix", "Material extremadamente raro.", 800, "Insumos Alquímicos"),
    ("Musgo Arcano", "Absorbe energía mágica del ambiente.", 30, "Insumos Alquímicos"),
    ("Fragmento de Obsidiana Viva", "Reacciona al calor espiritual.", 120, "Insumos Alquímicos"),
    ("Raíz de Belladona", "Elemento extremadamente tóxico.", 25, "Insumos Alquímicos"),
    ("Polen Sombrío", "Utilizado en pociones de invisibilidad.", 60, "Insumos Alquímicos"),
    ("Aceite Etéreo", "Base de elixires avanzados.", 95, "Insumos Alquímicos"),
    ("Cristal Arcano", "Fuente estable de energía mágica.", 150, "Insumos Alquímicos"),
    ("Alga Espectral", "Crece solo bajo lunas llenas.", 40, "Insumos Alquímicos"),
    ("Mineral Lumínico", "Brilla sin emitir calor.", 70, "Insumos Alquímicos"),
    ("Sangre de Basilisco", "Extremadamente peligrosa.", 350, "Insumos Alquímicos"),
    ("Corteza de Yggdrasil", "Muy difícil de conseguir.", 400, "Insumos Alquímicos"),
    ("Hueso Molido", "Base común de alquimia oscura.", 15, "Insumos Alquímicos"),
    ("Hierba Plateada", "Muy usada en alquimia curativa.", 20, "Insumos Alquímicos"),
    ("Flor Umbría", "Se marchita al contacto con la luz.", 60, "Insumos Alquímicos"),
    ("Gelatina Abisal", "Perfecta para experimentos inestables.", 140, "Insumos Alquímicos"),
    ("Semilla Astral", "Rara y cargada de energía cósmica.", 220, "Insumos Alquímicos"),
    ("Tinta de Kraken", "Valiosa para rituales arcanos.", 180, "Insumos Alquímicos"),

    # 15 Artefactos y Catalizadores
    ("Amuleto de Transmutación", "Permite convertir materiales básicos en otros más complejos.", 900, "Artefactos Mágicos"),
    ("Guantes del Alquimista", "Resistentes a ácidos y magia.", 250, "Artefactos Mágicos"),
    ("Orbe de Energía Pura", "Potencia hechizos.", 650, "Artefactos Mágicos"),
    ("Cuchara Ritual", "Usada para mezclar esencias delicadas.", 45, "Artefactos Mágicos"),
    ("Báculo Catalítico", "Concentra la energía del usuario.", 1200, "Catalizadores"),
    ("Anillo de Confluencia", "Sincroniza energías mágicas.", 400, "Catalizadores"),
    ("Cáliz Rúnico", "Mantiene estable cualquier mezcla alquímica.", 550, "Catalizadores"),
    ("Plato Adivinador", "Revela la naturaleza de ingredientes desconocidos.", 210, "Artefactos Mágicos"),
    ("Lupa Espectral", "Permite ver corrientes mágicas.", 180, "Artefactos Mágicos"),
    ("Cámara de Estabilización", "Imprescindible para pociones inestables.", 800, "Catalizadores"),
    ("Martillo Runificado", "Sirve para romper cristales mágicos.", 300, "Artefactos Mágicos"),
    ("Cubo Enigmático", "Se activa con energía mental.", 900, "Artefactos Mágicos"),
    ("Vara de Ampliación", "Incrementa efectos mágicos.", 500, "Catalizadores"),
    ("Pergamino Arcaico", "Contiene recetas antiquísimas.", 200, "Artefactos Mágicos"),
    ("Caja de Contención", "Evita que materiales peligrosos escapen.", 350, "Catalizadores"),
]

productos_creados = []

for nombre, descripcion, precio, categoria_nombre in productos_data:
    producto = Producto.objects.create(
        nombre=nombre,
        descripcion=descripcion,
        precio=Decimal(precio),
        categoria=categorias[categoria_nombre]
    )

    # asignar etiquetas aleatorias (entre 1 y 5 por producto)
    producto.etiquetas.add(*random.sample(list(etiquetas.values()), random.randint(1, 5)))

    productos_creados.append(producto)

# --------------------
# 4. Detalles de producto
# --------------------

for p in productos_creados:
    DetalleProducto.objects.create(
        producto=p,
        detalles=f"Detalles adicionales del producto {p.nombre}.",
        dimensiones=f"{random.randint(5, 50)}x{random.randint(5, 50)} cm",
        peso=Decimal(random.randint(1, 500)) / Decimal(10),
    )

print("Base de datos poblada exitosamente 🔮✨")
