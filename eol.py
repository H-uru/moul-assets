#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import argparse
import re
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--fail-fast", action="store_true")
parser.add_argument("-v", "--verbose", action="store_true")

exitcode = 0

if __name__ == "__main__":
    args = parser.parse_args()

    regex = re.compile(r"i\/(?P<index>\S+)\s+w\/(?P<working>\S+)\s+attr\/(?P<attribute>\S+)?(?:\s+eol=(?P<eol>\S+))?\s+(?P<path>\S+)")
    result = subprocess.Popen(
        ["git", "ls-files", "--eol"],
        stdout=subprocess.PIPE,
        text=True
    )

    # Iterate over lines returned from git... Trying to buffer the entire
    # result of git lfs-files in a Python stream is SLOW.
    for line in result.stdout:
        result = regex.match(line)
        if result is None:
            raise RuntimeError(line)

        path = result.group("path")
        if result.group("attribute") == "-text":
            if args.verbose:
                print(f"'{path}'\tnot a text file")
            continue

        if eol := result.group("eol"):
            indexEol = result.group("index")
            workingEol = result.group("working")
            if (eol, eol) != (indexEol, workingEol):
                print(f"'{path}'\teol mismatch - expected: '{eol}', git index: '{indexEol}', working copy: '{workingEol}'")
                exitcode = 1
                if args.fail_fast:
                    sys.exit(exitcode)
            elif args.verbose:
                print(f"'{path}'\tgood eols")
        elif args.verbose:
            print(f"'{path}'\tno defined eols")

    sys.exit(exitcode)
