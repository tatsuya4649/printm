import sys
import termios
import tty
import io
import os
from .placeholder import PlaceHolder

class MoreIOError(IOError):
    pass


class MoreAttributeError(AttributeError):
    pass


class More:
    def __init__(
        self,
        output,
        placeholder=None,
    ):
        self.placeholder = placeholder
        if not sys.stdin.isatty():
            raise MoreIOError(
                "stdin must be tty."
            )
        if not sys.stdout.isatty():
            raise MoreIOError(
                "stdout must be tty."
            )

        _buffer = io.StringIO(
            initial_value=output,
            newline="\n"
        )
        _buffer_lines = _buffer.getvalue().splitlines()
        _oldattr = termios.tcgetattr(sys.stdin.fileno())
    
    @property
    def placeholder(self):
        return self._paceholder

    @placeholder.setter
    def placeholder(self, value):
        if type(value) is not PlaceHolder.__class__ and \
                value is not None:
            raise TypeError(
                "placeholder must be PlaceHolder class."
            )
        self._placeholder = value
        

    def _flush_screen(self):
        sys.stdout.write("\033[2J\033[H")

    def _terminal_size(self):
        columns, lines = os.get_terminal_size()
        return columns, lines

    def _terminal_full_size(self):
        columns, lines = self._terminal_size()
        return columns * lines

    def _termline(self, lines, placeholder="hello", brank_lines=1):
        _placelines = len(placeholder.splitlines())
        return lines - _placelines - brank_lines

    def print(self):
        self._setcbreak()
        now_line = 0
        try:
            while True:
                self._flush_screen()
                columns, lines = self._terminal_size()
                _scrlines = list()
                for line in file_lines[now_line:]:
                    if len(line) > columns:
                        _scrlines.append(line[:columns])
                        _scrlines.append(line[columns:])
                    else:
                        _scrlines.append(line)

                if self.placeholder is not None:
                    _placeline = \
                        self.placeholder.placelines(
                            lines=lines
                        )
                else:
                    _placeline = 0
                total_line = 0
                for line in _scrlines:
                    print(line)
                    total_line += 1
                    if total_line == (lines-_placeline):
                        break
                for _ in range(_BLANK_LINES):   print("")
                print(_PLACE_HOLDER)

                if (len(_scrlines)-len(_scrlines[now_line+total_line:])) < _totallines:
                    sys.exit(0)
                _input = sys.stdin.read(1)
                if ord(_input) == 0x71:
                    # quit
                    sys.exit(0)
                elif ord(_input) == 0x20:
                    # space
                    now_line += total_line
                elif ord(_input) == 0x0a:
                    # enter
                    now_line += 1
                else:
                    continue
        finally:
            self._resetattr()

    # raw mode
    def _setrawmode(self):
        tty.setraw(sys.stdin.fileno())

    # cbreak mode
    def _setcbreak(self):
        tty.setcbreak(sys.stdin.fileno())

    def _resetattr(self):
        if not hasattr(self, "_oldattr"):
            raise MoreAttributeError(
                ""
            )
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self._oldattr)
