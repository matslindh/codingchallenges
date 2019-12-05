def unfscker(s):
    return unfscker_halfsies(
        unfscker_pairsies(
            unfscker_long_trios(s)
        )
    )


def unfscker_halfsies(s):
    return s[len(s)//2:] + s[:len(s)//2]


def unfscker_pairsies(s):
    r = ''

    for i in range(0, len(s), 2):
        r += s[i+1]
        r += s[i]

    return r


def unfscker_long_trios(s):
    f = ''
    b = ''

    for i in range(0, len(s)//2, 3):
        e = len(s) - i
        f += s[e-3:e]
        b = s[i:i+3] + b

    return f + b


def test_unfscker_halfsies():
    assert 'PonnistallHoppeslottTrommesett' == unfscker_halfsies('slottTrommesettPonnistallHoppe')


def test_unfscker_pairsies():
    assert 'slottTrommesettPonnistallHoppe' == unfscker_pairsies('lstoTtormmsetePtnointslaHlpoep')


def test_unfscker_long_trios():
    assert 'lstoTtormmsetePtnointslaHlpoep' == unfscker_long_trios('oepHlpslainttnotePmseormoTtlst')


def test_unfscker():
    assert 'PonnistallHoppeslottTrommesett' == unfscker('oepHlpslainttnotePmseormoTtlst')


if __name__ == '__main__':
    print(unfscker('tMlsioaplnKlflgiruKanliaebeLlkslikkpnerikTasatamkDpsdakeraBeIdaegptnuaKtmteorpuTaTtbtsesOHXxonibmksekaaoaKtrssegnveinRedlkkkroeekVtkekymmlooLnanoKtlstoepHrpeutdynfSneloietbol'))