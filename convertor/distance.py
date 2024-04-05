# Create module distance to convert between units using this formula:
# meters=feet×0.3048

# converting feet into meters


def distance_m(ft_value):
    m = ft_value * 0.3048
    return float(m)

# converting meters into feet


def distance_ft(m_value):
    ft = m_value / 0.3048
    return float(ft)


# print(distance_m(25))
# print(distance_ft(7.62))