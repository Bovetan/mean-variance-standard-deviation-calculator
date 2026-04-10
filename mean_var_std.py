import numpy as np


def calculate(lista):
    # Validar que la lista tenga exactamente 9 números
    if len(lista) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convertir la lista en una matriz 3x3
    matriz = np.array(lista).reshape(3, 3)

    # Calcular la media
    mean = [
        matriz.mean(axis=0).tolist(),
        matriz.mean(axis=1).tolist(),
        matriz.mean().item()
    ]

    # Calcular la varianza
    variance = [
        matriz.var(axis=0).tolist(),
        matriz.var(axis=1).tolist(),
        matriz.var().item()
    ]

    # Calcular la desviación estándar
    standard_deviation = [
        matriz.std(axis=0).tolist(),
        matriz.std(axis=1).tolist(),
        matriz.std().item()
    ]

    # Calcular el máximo
    maximo = [
        matriz.max(axis=0).tolist(),
        matriz.max(axis=1).tolist(),
        matriz.max().item()
    ]

    # Calcular el mínimo
    minimo = [
        matriz.min(axis=0).tolist(),
        matriz.min(axis=1).tolist(),
        matriz.min().item()
    ]

    # Calcular la suma
    suma = [
        matriz.sum(axis=0).tolist(),
        matriz.sum(axis=1).tolist(),
        matriz.sum().item()
    ]

    # Retornar el diccionario en el formato exacto pedido
    return {
        "mean": mean,
        "variance": variance,
        "standard deviation": standard_deviation,
        "max": maximo,
        "min": minimo,
        "sum": suma
    }