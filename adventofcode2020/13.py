# https://math.stackexchange.com/questions/2218763/how-to-find-lcm-of-two-numbers-when-one-starts-with-an-offset
def combine_phased_rotations(a_period, a_phase, b_period, b_phase):
    """Combine two phased rotations into a single phased rotation

    Returns: combined_period, combined_phase

    The combined rotation is at its reference point if and only if both a and b
    are at their reference points.
    """
    gcd, s, t = extended_gcd(a_period, b_period)
    phase_difference = a_phase - b_phase
    pd_mult, pd_remainder = divmod(phase_difference, gcd)
    if pd_remainder:
        raise ValueError("Rotation reference points never synchronize.")

    combined_period = a_period // gcd * b_period
    combined_phase = (a_phase - s * pd_mult * a_period) % combined_period
    return combined_period, combined_phase


def arrow_alignment(red_len, green_len, advantage):
    """Where the arrows first align, where green starts shifted by advantage"""
    period, phase = combine_phased_rotations(
        red_len, 0, green_len, -advantage % green_len
    )
    return -phase % period


def extended_gcd(a, b):
    """Extended Greatest Common Divisor Algorithm

    Returns:
        gcd: The greatest common divisor of a and b.
        s, t: Coefficients such that s*a + t*b = gcd

    Reference:
        https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient, remainder = divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def travelizer(goal, s):
    m_value = None

    for s in s.split(','):
        try:
            v = int(s)
            offset = v - (goal % v)

            if not m_value or offset < m_value[1]:
                m_value = (v, offset)

        except ValueError:
            pass

    return m_value[0] * m_value[1]


def alignmenter(inp):
    periods = []

    for xdx, x in enumerate(inp[1:]):
        if x is None:
            continue

        periods.append(arrow_alignment(inp[0], x, -(xdx+1)))

    """            
    for xdx, x in enumerate(inp[:-1]):
        if x is None:
            continue

        for ydx, y in enumerate(inp[xdx+1:]):
            ydx += xdx + 1
            if y is None:
                continue

            print(x, y, xdx, ydx, y - ydx, x - xdx)
            periods.append(arrow_alignment(x, y, 2))"""
    print(periods)


def test_travelizer():
    assert travelizer(939, '7,13,x,x,59,x,31,19') == 295


def test_alignmenter():
    #assert alignmenter([7, 6]) == 3417
    assert alignmenter([17, None, 13, 19]) == 3417


if __name__ == '__main__':
    print(travelizer(1002632, '23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,829,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,677,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19'))
