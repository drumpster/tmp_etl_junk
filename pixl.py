#!/usr/bin/python3

import sys

import pandas


def parse_file(xlname, sheetname):
    sep="|"
    df=pandas.read_excel(xlname, sheet_name=sheetname)
    nr=len(df)
    nc=len(df.columns)
    for r in range(0, nr-1):
        for c in range(0, nc-1):
            val = str(df.loc[r][c])
            val=val.replace("\r", ",")
            val=val.replace("\n", ",")
            val=val.replace(sep, ":")
            sys.stdout.write(val)
            sys.stdout.write(sep)
        sys.stdout.write(str(r))
        sys.stdout.write("\n")



if __name__ == '__main__':
    #int main()
    scriptname=sys.argv[0]
    if(len(sys.argv) != 3):
        sys.stderr.write("Usage: $scriptname xlfile sheetname\n")
    parse_file('pixtest.xlsx', 'Sheet A')
