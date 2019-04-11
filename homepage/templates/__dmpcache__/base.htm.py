# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554998840.9101605
_enable_loop = True
_template_filename = 'C:/Users/USER/intex2/thepack-intex/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'navbar_items', 'left_menu', 'content', 'right_content']


import datetime  

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def left_menu():
            return render_left_menu(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def navbar_items():
            return render_navbar_items(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n        <link rel="icon" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/circle.jpg">\r\n        <title>OTF &mdash; ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('</title>\r\n\r\n')
        __M_writer('        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/jquery-3.3.1.js"></script>\r\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/js/bootstrap.js"></script>\r\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/css/bootstrap.css">\r\n\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n\r\n    </head>\r\n\r\n    <body>\r\n')
        __M_writer('        <header>\r\n            <div class="title">\r\n                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/otflogo.png" alt="Opioid Task Force Logo">\r\n            </div>\r\n            <nav class="navbar navbar-expand-lg navbar-light bg-light">\r\n                <img class="small_logo" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/circle.jpg" alt="logo" />\r\n                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">\r\n                    <span class="navbar-toggler-icon"></span>\r\n                </button>\r\n                <div class="collapse navbar-collapse" id="navbarSupportedContent">\r\n                    <ul class="navbar-nav mr-auto">\r\n                    <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'index' else ''))
        __M_writer('">\r\n                        <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>\r\n                    </li>\r\n                    <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == '/prescribers/Index' else ''))
        __M_writer('">\r\n                        <a class="nav-link" href="/prescribers/">Prescribers</a>\r\n                    </li>\r\n                    <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == '/drugs/index/' else ''))
        __M_writer('">\r\n                        <a class="nav-link" href="/drugs/">Drugs</a>\r\n                    </li>\r\n                    <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'index' else ''))
        __M_writer('">\r\n                        <a class="nav-link" href="/homepage/dashboard/">Dashboard <span class="sr-only">(current)</span></a>\r\n                    </li>\r\n                    <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'index' else ''))
        __M_writer('">\r\n                        <a class="nav-link" href="/homepage/map/">Map <span class="sr-only">(current)</span></a>\r\n                    </li>\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_items'):
            context['self'].navbar_items(**pageargs)
        

        __M_writer('\r\n')
        if not request.user.is_authenticated:
            __M_writer('                        <li class="nav-item ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'login' else ''))
            __M_writer('"><a class="nav-link" href="/account/login/">Login</a></li>\r\n')
        __M_writer('\r\n')
        if request.user.is_authenticated:
            __M_writer('                        <li class="nav-item dropdown">\r\n                            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n                            Account\r\n                            </a>\r\n                            <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">\r\n                            <a class="dropdown-item" href="#">Cart</a>\r\n                            <a class="dropdown-item" href="#">Settings</a>\r\n                            <a class="dropdown-item" href="/account/logout/">Log Out</a>\r\n                            </div>\r\n                        </li>\r\n')
        __M_writer('                    </ul>\r\n                </div>\r\n            </nav>\r\n            \r\n\r\n        </header>\r\n\r\n        <main>\r\n            <div id="site_left">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_menu'):
            context['self'].left_menu(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div id="site_center">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div id="site_right">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </main>\r\n\r\n        <footer>\r\n           <div class="footer_text">\r\n            Copyright &copy; ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( datetime.datetime.today().year ))
        __M_writer(' PACK Consulting  \r\n            </div>     \r\n        </footer>\r\n\r\n    </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_items():
            return render_navbar_items(context)
        __M_writer = context.writer()
        __M_writer('                    \r\n                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_menu():
            return render_left_menu(context)
        __M_writer = context.writer()
        __M_writer('\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/USER/intex2/thepack-intex/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 2, "20": 0, "38": 2, "39": 7, "40": 7, "45": 8, "46": 11, "47": 11, "48": 11, "49": 12, "50": 12, "51": 13, "52": 13, "53": 17, "54": 18, "55": 18, "56": 24, "57": 26, "58": 26, "59": 29, "60": 29, "61": 35, "62": 35, "63": 38, "64": 38, "65": 41, "66": 41, "67": 44, "68": 44, "69": 47, "70": 47, "75": 51, "76": 52, "77": 53, "78": 53, "79": 53, "80": 55, "81": 56, "82": 57, "83": 68, "88": 78, "93": 83, "98": 88, "99": 94, "100": 94, "106": 8, "117": 50, "123": 50, "129": 77, "135": 77, "141": 81, "147": 81, "153": 86, "159": 86, "165": 159}}
__M_END_METADATA
"""
