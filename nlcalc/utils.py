# Returns True if String can be converted to Numeric Type
# otherwise return False
def is_numeric(value):
    try:
        int(value)
        return True
    except (ValueError,TypeError):
        try:
            float(value)
            return True
        except (ValueError, TypeError):
            return False


# Converts String to Numeric Type
# Raises Error if not Possible
# int conversion is tried first so that high precision of
# int in python can be utilized
def convert_to_numeric(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return float(value)
