#!/usr/bin/python

"""gl-resolve - Mark a file with conflicts as resolved.

Implements the gl-resolve command, part of the Gitless suite.
"""

import argparse

import cmd
import pprint
import sync_lib


def main():
  parser = argparse.ArgumentParser(
      description='Mark a file with conflicts as resolved')
  parser.add_argument(
      'files', nargs='+', help='the file(s) in conflict to mark as resolved')
  args = parser.parse_args()
  errors_found = False

  for fp in args.files:
    ret = sync_lib.resolve(fp)
    if ret is sync_lib.FILE_NOT_FOUND:
      pprint.err('Can\'t mark as resolved an inexistent file: %s' % fp)
      errors_found = True
    elif ret is sync_lib.FILE_NOT_IN_CONFLICT:
      pprint.err('File %s has no conflicts' % fp)
      errors_found = True
    elif ret is sync_lib.SUCCESS:
      pprint.msg('File %s has been marked as resolved' % fp)
    else:
      raise Exception('Unrecognized ret code %s' % ret)

  return cmd.ERRORS_FOUND if errors_found else cmd.SUCCESS


if __name__ == '__main__':
  cmd.run(main)