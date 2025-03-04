import math
def process(a:float, b:float, c:float)->dict:
  
    diag = (a**2 + b**2 + c**2) ** 0.5

    volume = a * b * c

    surface_area = 2 * (a*b + a*c + b*c)

    alpha = math.degrees(math.acos(a / diag))

    beta = math.degrees(math.acos(b / diag))

    gamma = math.degrees(math.acos(c / diag))

    radius_described_sphere = diag / 2

    volume_described_sphere = (4/3) * math.pi * (radius_described_sphere **3)

    return {
        "diag": str(diag),
        "volume": str(volume),
        "surface_area": str(surface_area),
        "alpha": str(alpha),
        "beta": str(beta),
        "gamma": str(gamma),
        "radius_described_sphere": str(radius_described_sphere),
        "volume_described_sphere": str(volume_described_sphere)
    }