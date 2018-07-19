import numpy as np

def find_coords(lat, long, rad, theta):
    delta = np.divide(rad,6371000)
    def to_radians(theta):
        return np.divide(np.dot(theta, np.pi), 180.0)

    def to_degrees(theta):
        return np.divide(np.dot(theta, 180.0), np.pi)

    theta = to_radians(theta)
    lat1 = to_radians(lat)
    lng1 = to_radians(long)

    lat2 = np.arcsin( np.sin(lat1) * np.cos(delta) +
                      np.cos(lat1) * np.sin(delta) * np.cos(theta) )

    lng2 = lng1 + np.arctan2( np.sin(theta) * np.sin(delta) * np.cos(lat1),
                              np.cos(delta) - np.sin(lat1) * np.sin(lat2))

    lng2 = (lng2 + 3 * np.pi) % (2 * np.pi) - np.pi

    return[to_degrees(lat2), to_degrees(lng2)]

def triangle_point(point1, point2, r, theta):
    x1 = point1[0]; y1 = point1[1]; x2 = point2[0]; y2 = point2[1];
    x3 = (x1+x2)/2; y3 = (y1+y2)/2;
    return find_coords(x3, y3, r, theta + 90)
