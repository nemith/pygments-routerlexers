# -*- coding: utf-8 -*-
from pygments.lexer import RegexLexer,bygroups,include
from pygments.token import *

class IOSLexer(RegexLexer):
    name="Cisco IOS"
    aliases = ['ios', 'IOS configuration file']
    filenames = ['*.ios']
    tokens={
        "root" : [
            (r"^!.*", Comment),
            (r"^(version\s+)(.*)$", bygroups(Keyword, Number.Float)),
            (r"(desc*r*i*p*t*i*o*n*)(.*?)$", bygroups(Keyword,Comment)),
            (r"(password|secret)(\s+[57]\s+)(\S+)", bygroups(Keyword,Number,String.Double)),
            (r"^(inte*r*f*a*c*e*|controller|router \S+|voice translation-\S+|voice-port|line)(.*?)$", bygroups(Keyword.Type,Name.Function)),
            (r"(permit|deny)", Operator.Word),
            (r"^(banner\s+)(motd\s+|login\s+)(#)", bygroups(Keyword, Keyword, Name.Function), "text"),
            (r"^(dial-peer\s+\S+\s+)(\S+)(.*?)$", bygroups(Keyword,Name.Attribute,Keyword)),
            (r"^(vlan\s+)(\d+)$", bygroups(Keyword,Name.Attribute)),
            (r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(/\d{1,2})?", Number), # IPv4 Address/Prefix
            (r"49\.\d{4}\.\d{4}\.\d{4}\.\d{4}\.\d{2}",           Number), # NSAP
            (r"[a-f0-9]{4}\.[a-f0-9]{4}\.[a-f0-9]{4}",           Number.Hex), # MAC Address
            (r"^(\s*no\s+)(\S+)", bygroups(Keyword.Constant, Keyword)),
            (r"^[^\n\r]\s*\S+", Keyword),
            (r"\*+", Name.Entity),  #Obfuscated Passwords
            (r"(?<= )\d+(?= )", Number),
            (r".", Text),
        ],
        "text" : [
            (r'[^#]', Text),
            (r'#', Name.Function, '#pop'),
        ],
    }
