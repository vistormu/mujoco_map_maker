import numpy as np


def hex_to_rgba(hex_code: str, alpha: float) -> tuple[float, float, float, float]:
    hex: str = hex_code.lstrip('#')
    rgb: tuple[int, int, int] = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

    rgba: tuple[float, float, float, float] = (round(rgb[0]/255.0, 4), round(rgb[1]/255.0, 4), round(rgb[2]/255.0, 4), alpha)

    return rgba


def euler_to_quaternion(roll: float, pitch: float, yaw: float) -> tuple[float, float, float, float]:
    cy: float = np.cos(yaw * 0.5)
    sy: float = np.sin(yaw * 0.5)
    cp: float = np.cos(pitch * 0.5)
    sp: float = np.sin(pitch * 0.5)
    cr: float = np.cos(roll * 0.5)
    sr: float = np.sin(roll * 0.5)

    w: float = cr * cp * cy + sr * sp * sy
    x: float = sr * cp * cy - cr * sp * sy
    y: float = cr * sp * cy + sr * cp * sy
    z: float = cr * cp * sy - sr * sp * cy

    return w, x, y, z
