from collections import defaultdict

base = ord('a')


def fubarer(inp):
    counter = defaultdict(int)
    out = ''

    for char in inp:
        n = ord(char) - base

        if n == counter[n]:
            out += char

        counter[n] += 1

    return out


def test_fubarer():
    assert fubarer('csfgunqvmiotgixxqeexdnwrtrgftpafkqepkvwwscotfahzneobiipslnbmgyxxumdwxeymprtjrhapxqvguqazkwiorstwcjii') == 'abec'


if __name__ == '__main__':
    print(fubarer('phzvjbrsnkeehvglzpveenyjycwzpukigcdiotomuankejhqdhqtojmezmfqtuasuhzbbgawjlxbrqotwgythqsrzfbgisnakeopxtzbbdfbjdnuqymqqihylyszwuezoigjoxhavuyzqnqfnzvtazagvahullujteapqeogyfelzygcqujnxshrivkmhwkkmfiqpqoihcxarewxffyrwmmfghharnijxondraglvemdqfnxdhxilweqcxxsvviuxzshpfjttoymplfahmaskvtimvirhmqoudvqagacqsoeyvpouejmamchbhqfhidpsyovxeazzfbbocuydquadffumpmhwwiotpqiznyvmlnthupvvgfwrpeirltvlorgjqpwzstgjwpsixrbbjsuiumaxydtkcjxvgazonghhfgswunxjhnxvzqxnvtrdujblkbeebsdfgawvholjddwezacxiumyvhlwwbqdpfxzvhyqxcqlnqpvqnvjnygvwrzzaojhnfeywptbttgyyhtkpdbsqcaxpuzsqpadjzssfdiguijlycugnbftcmmpjjjxrjkygethmfvkxbhjkjhrrhgyplasjiunhnqkcvdyzlzxnbdlyxbthmpwrwovuibuypptvgligepclvyxvwkhziqucrnkdelmvdaecdnzeapebfkhocdoaljciemcdasdxqqzjbzhetmovgitntxmvgnfqzrtlaymmxepetgrdsqwmjsodqqrgccnahycqpltphhaeyjnnytjctmkoysduumnurtyzodhsaqdhpyytwrkvymwikkxoolrcgipaftzvwbqounhxriykepdahubsijtwsvtzjihpatpmuemzwthfzypjpiwzhckuxvfrlxlmcvmdujwsghltaukprsancpooxywxccnqgqkgmscstoupxilycjumybfcnjtycichjvkxwfqqqinzrzpthesxlcgcifvjuhyegmjrkb'))
