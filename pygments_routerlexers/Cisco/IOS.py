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
            (r"(description)(.*?)$", bygroups(Keyword,Comment)),
            (r"(password|secret)(\s+[57]\s+)(\S+)", bygroups(Keyword,Number,String.Double)),
            (r"^(interface|controller|router \S+|voice translation-\S+|voice-port)(.*?)$", bygroups(Keyword,Name.Attribute)),
            (r"^(dial-peer\s+\S+\s+)(\S+)(.*?)$", bygroups(Keyword,Name.Attribute,Keyword)),
            (r"^(vlan\s+)(\d+)$", bygroups(Keyword,Name.Attribute)),
            (r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(/\d{1,2})?", Number), # IPv4 Address/Prefix
            (r"49\.\d{4}\.\d{4}\.\d{4}\.\d{4}\.\d{2}",           Number), # NSAP
            (r"^(?:no\s+)?\S+", Keyword),
            (r"\d+", Number),
            (r".", Text),
        ],
        
    }

