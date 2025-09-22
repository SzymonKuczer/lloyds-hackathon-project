from geopy import Nominatim, distance


def calculate_euclidian_distance(address_a: str, address_b: str) -> float:
    """
    Calculates the straight-line (Euclidean) distance between two addresses using geopy.
    Args:
        address_a (str): The first address.
        address_b (str): The second address.
    Returns:
        float: The Euclidean (geodesic) distance between the two locations in kilometers.
    Raises:
        ValueError: If either address cannot be geocoded or any other error occurs during processing - Will return `-1` in this case
    """
    geolocator = Nominatim(user_agent="b2b-app")
    d = -1
    try:
        a_address = geolocator.geocode(address_a.strip(","))
        b_address = geolocator.geocode(address_b.strip(","))

        a_coords = (a_address.latitude, a_address.longitude)
        b_coords = (b_address.latitude, b_address.longitude)

        d = distance.distance(a_coords, b_coords)
        d = round(d.kilometers, 2)
    except Exception:
        raise ValueError("Error calculating distance")
    return d

