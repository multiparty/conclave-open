import sys, os
from random import randint


def generate(out_path, num_cols, num_rows, col_names):
    num_cols = int(num_cols)
    num_rows = int(num_rows)

    col_names = col_names.split(',')

    assert (len(col_names) == num_cols), \
        'Number of columns is unequal to number of column names.'

    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    with open(out_path, 'w') as f:

        f.write(','.join(col_names) + '\n')
        f.write('\n'.join([','.join([str(randint(0,9))
                                     for i in range(num_cols)])
                           for j in range(num_rows)]))

if __name__ == "__main__":

    generate(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

