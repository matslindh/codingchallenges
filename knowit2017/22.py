def find_smallest_set_containing(string, elements):
    best_length = len(string)
    best_seq = None

    for i in range(0, len(string) - len(elements)):
        if string[i] not in elements:
            continue

        found = list(elements)
        seq = None

        for j in range(i, len(string)):
            if string[j] in found:
                del found[found.index(string[j])]

            if not found:
                seq = (i, j)
                break

        if seq and (seq[1] - seq[0]) < best_length:
            best_length = seq[1] - seq[0]
            best_seq = seq

    return string[best_seq[0]:best_seq[1] + 1]


def test_find_smallest_set_containing():
    assert 'CBFA' == find_smallest_set_containing('ADOBECODECBFANETS', 'ABC')


if __name__ == "__main__":
    print(find_smallest_set_containing('FJKAUNOJDCUTCRHBYDLXKEODVBWTYPTSHASQQFCPRMLDXIJMYPVOHBDUGSMBLMVUMMZYHULSUIZIMZTICQORLNTOVKVAMQTKHVRIFMNTSLYGHEHFAHWWATLYAPEXTHEPKJUGDVWUDDPRQLUZMSZOJPSIKAIHLTONYXAULECXXKWFQOIKELWOHRVRUCXIAASKHMWTMAJEWGEESLWRTQKVHRRCDYXNTLDSUPXMQTQDFAQAPYBGXPOLOCLFQNGNKPKOBHZWHRXAWAWJKMTJSLDLNHMUGVVOPSAMRUJEYUOBPFNEHPZZCLPNZKWMTCXERPZRFKSXVEZTYCXFRHRGEITWHRRYPWSVAYBUHCERJXDCYAVICPTNBGIODLYLMEYLISEYNXNMCDPJJRCTLYNFMJZQNCLAGHUDVLYIGASGXSZYPZKLAWQUDVNTWGFFYFFSMQWUNUPZRJMTHACFELGHDZEJWFDWVPYOZEVEJKQWHQAHOCIYWGVLPSHFESCGEUCJGYLGDWPIWIDWZZXRUFXERABQJOXZALQOCSAYBRHXQQGUDADYSORTYZQPWGMBLNAQOFODSNXSZFURUNPMZGHTAJUJROIGMRKIZHSFUSKIZJJTLGOEEPBMIXISDHOAIFNFEKKSLEXSJLSGLCYYFEQBKIZZTQQXBQZAPXAAIFQEIXELQEZGFEPCKFPGXULLAHXTSRXDEMKFKABUTAABSLNQBNMXNEPODPGAORYJXCHCGKECLJVRBPRLHORREEIZOBSHDSCETTTNFTSMQPQIJBLKNZDMXOTRBNMTKHHCZQQMSLOAXJQKRHDGZVGITHYGVDXRTVBJEAHYBYRYKJAVXPOKHFFMEPHAGFOOPFNKQAUGYLVPWUJUPCUGGIXGRAMELUTEPYILBIUOCKKUUBJROQFTXMZRLXBAMHSDTEKRRIKZUFNLGTQAEUINMBPYTWXULQNIIRXHHGQDPENXAJNWXULFBNKBRINUMTRBFWBYVNKNKDFR', 'ABCDA'))