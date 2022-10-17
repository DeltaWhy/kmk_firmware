import csv
import sys


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        reader = csv.DictReader(f)
        for row in reader:
            keys = []
            for key in reader.fieldnames[0:8]:
                if row[key]:
                    keys.append('KC.'+key)
            if len(keys) < 2:
                continue
            base = row['base'] or None
            left_word = row['left word'] or None
            right_word = row['right word'] or None
            left_partials = row['left partials']
            right_partials = row['right partials']
            left_partials = tuple((x for x in left_partials.split(', ') if x))
            right_partials = tuple((x for x in right_partials.split(', ') if x))
            print(f'AsetniopCombo(({", ".join(keys)}), '
                    f'{repr(base)}, '
                    f'{repr(left_word)}, '
                    f'{repr(right_word)}, '
                    f'{repr(left_partials or None)}, '
                    f'{repr(right_partials or None)})')


if __name__ == '__main__':
    main()
