import datetime


def parse_entries(lines):
    day = None
    year = []

    for line in lines:
        if line[0] != "\t":
            if day:
                year.append(day)

            ds = line.strip()[:-1] + ' 2018'
            d = datetime.datetime.strptime(ds, '%b %d %Y').date()

            day = {
                'date': d.strftime('%Y-%m-%d'),
                'day': d.strftime('%w'),
                'toothieouchistopper': 0,
                'hairmagicifier': 0,
                'noshitsherlockers': 0,
            }

            continue

        parts = line.strip().split(' ')
        parts.pop(0)  # remove *

        if parts[2] == 'tannkrem':
            day['toothieouchistopper'] += int(parts[0])
        if parts[2] == 'sjampo':
            day['hairmagicifier'] += int(parts[0])
        if parts[2] == 'toalettpapir':
            day['noshitsherlockers'] += int(parts[0])

    year.append(day)
    return year


def test_parse_entries():
    result = parse_entries("""Dec 05:
	* 3 meter toalettpapir
	* 5 ml tannkrem
	* 18 ml sjampo
Dec 06:
	* 4 meter toalettpapir
	* 16 ml sjampo
	* 4 ml tannkrem""".split("\n"))

    assert len(result) == 2
    assert result[0]['date'] == '2018-12-05'


if __name__ == '__main__':
    year = parse_entries(open('input/10').readlines())

    sums = {
        'toothieouchistopper': 0,
        'hairmagicifier': 0,
        'noshitsherlockers': 0,
        'sunday_shampoos': 0,
        'tp_wednesdays': 0,
    }

    for day in year:
        if day['day'] == '3':
            sums['tp_wednesdays'] += day['noshitsherlockers']

        if day['day'] == '0':
            sums['sunday_shampoos'] += day['hairmagicifier']

        sums['noshitsherlockers'] += day['noshitsherlockers']
        sums['hairmagicifier'] += day['hairmagicifier']
        sums['toothieouchistopper'] += day['toothieouchistopper']

    print(sums)
    print(
        (sums['toothieouchistopper'] // 125) *
        (sums['hairmagicifier'] // 300) *
        (sums['noshitsherlockers'] // 25) *
        (sums['sunday_shampoos'] * sums['tp_wednesdays'])
    )
