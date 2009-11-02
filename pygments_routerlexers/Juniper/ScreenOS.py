# -*- coding: utf-8 -*-
from pygments.lexer import RegexLexer
from pygments.token import *

class ScreenOSLexer(RegexLexer):
    name="Juniper ScreenOS"
    aliases = ['screenos', 'ScreenOS configuration file']
    tokens={
        "root" : [
            (r"^!.*", Comment),
            (r"^(?:un)set\s+?\S+", Keyword),
            (r".*\n", Text),
        ]
    }
