from geo_coor import __version__
from geo_coor.core import GeoCoordinate
from pathlib import Path


def main(input_setting_path=None):
    import argparse
    arg_parser = argparse.ArgumentParser(prog='geo_coor.exe',
                                         formatter_class=argparse.RawTextHelpFormatter)  # allow \n \t ...
    arg_parser.add_argument('--version', action='version', version='%(prog)s:' + f'{__version__}')
    arg_parser.add_argument('source_csv', type=Path, help="source file path")
    arg_parser.add_argument('output_file', type=Path, help="output file path")
    arg_parser.add_argument('fmt', type=Path, help="output format: csv, excel", default='csv')
    args = arg_parser.parse_args()


if __name__ == '__main__':
    main()
