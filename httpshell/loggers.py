from ansicolors import colorize
from ansicolors import Color
from ansicolors import Attribute
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import guess_lexer


# ANSI color terminal logger
# use color sparingly or the UI looks like a bowl of fruit loops
class AnsiLogger(object):
    def print_text(self, text=None):
        if text:
            print text
        else:
            print

    def print_response_code(self, response):
        colors = [Color.GREY, Color.GREEN, Color.YELLOW, Color.RED, Color.RED]
        print "HTTP/{0} {1} {2}".format(
            response.version / 10.0,
            response.status,
            colorize(response.reason, colors[response.status / 100 - 1],
                     Attribute.BRIGHT))

    def print_headers(self, headers, sending=False):
        for header in headers:
            print "{0}{1}: {2}".format(
                colorize("<" if sending else ">", Color.WHITE),
                colorize(header[0], Color.BLUE, Attribute.BRIGHT),
                header[1])

    def print_tackons(self, params):
        for param in params:
            print "{0}{1}{2}".format(
                colorize(param[0], Color.BLUE, Attribute.BRIGHT),
                "=" if len(param[1]) > 0 else "",
                param[1])

    def print_cookies(self, cookie):
        for morsel in cookie.values():
            print colorize("Name:", Color.BLUE), morsel.key
            print colorize("Value:", Color.BLUE), morsel.value
            print colorize("Expires:", Color.BLUE), morsel["expires"]
            print colorize("Domain:", Color.BLUE), morsel["domain"]
            print colorize("Path:", Color.BLUE), morsel["path"]
            print

    def print_data(self, data):
        if data:
            print
            print highlight(data,
                            guess_lexer(data),
                            TerminalFormatter())

    def print_command(self, command, params=None):
        if params is None:
            print " ", colorize(command, Color.WHITE, Attribute.BRIGHT)
        else:
            print " ", colorize(command, Color.WHITE, Attribute.BRIGHT), \
                colorize(params, Color.GREY, Attribute.BRIGHT)

    def print_help(self):
        print "Verbs"
        self.print_command("head", "[</path/to/resource>]")
        self.print_command("get", "[</path/to/resource>] [| <external command>]")
        self.print_command("post", "[</path/to/resource>] [| <external command>]")
        self.print_command("put", "[</path/to/resource>] [| <external command>]")
        self.print_command("delete", "</path/to/resource> [| <external command>]")
        self.print_command("options", "[</path/to/resource>] [| <external command>]")
        self.print_command("trace", "[</path/to/resource>] [| <external command>]")

        print "Navigation"
        self.print_command("cd", "</path/to/resource> or ..")
        self.print_command("open", "<url>")

        print "Metacommands"
        self.print_command("headers", "[<name>]:[<value>]")
        self.print_command("tackons", "[<name>]=[<value>]")
        self.print_command("cookies", "[<name>]=[<value>]")
        self.print_command("debuglevel", "[#]")
        self.print_command("quit")

        print
        print "Full documentation available at https://github.com/chrislongo/HttpShell#readme"

    def print_error(self, text):
        print text
