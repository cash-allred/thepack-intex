# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552174967.3912017
_enable_loop = True
_template_filename = 'C:/Users/the_m/Desktop/first_tutorial/mysite/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'navbar_items', 'left_menu', 'content', 'right_content']


import datetime  

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def left_menu():
            return render_left_menu(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def navbar_items():
            return render_navbar_items(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n        <link rel="icon" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/favicon.ico">\r\n        <title>Jedi &mdash; ')
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
        __M_writer('\r\n\r\n    </head>\r\n\r\n    <body>\r\n        <div id="maintenance_message" class="alert alert-danger">The site is going down tonight. I know... Shucks</div>\r\n        <header>\r\n            <nav class="navbar navbar-expand-lg navbar-light bg-light">\r\n                <img class="small_logo" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/python.png" alt="python" />\r\n                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">\r\n                    <span class="navbar-toggler-icon"></span>\r\n                </button>\r\n                <div class="collapse navbar-collapse" id="navbarSupportedContent">\r\n                    <ul class="navbar-nav mr-auto">\r\n                    <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'index' else ''))
        __M_writer('">\r\n                        <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>\r\n                    </li>\r\n                    ')
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
        __M_writer('                    </ul>\r\n                    <form class="form-inline my-2 my-lg-0">\r\n                    <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">\r\n                    <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>\r\n                    </form>\r\n                </div>\r\n            </nav>\r\n            \r\n            <div class="title">do or do not<br/> there is no try</div>\r\n        </header>\r\n\r\n        <main>\r\n            <div id="site_left">\r\n                ')
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
        __M_writer(' Cash Allred  \r\n            </div>     \r\n        </footer>\r\n\r\n    </body>\r\n</html>\r\n')
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
        __M_writer('\r\n                    Left side\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    center side\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    right text\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/the_m/Desktop/first_tutorial/mysite/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 2, "20": 0, "38": 2, "39": 7, "40": 7, "45": 8, "46": 11, "47": 11, "48": 11, "49": 12, "50": 12, "51": 13, "52": 13, "53": 17, "54": 18, "55": 18, "56": 26, "57": 26, "58": 32, "59": 32, "64": 36, "65": 37, "66": 38, "67": 38, "68": 38, "69": 40, "70": 41, "71": 42, "72": 53, "77": 68, "82": 73, "87": 78, "88": 84, "89": 84, "95": 8, "106": 35, "112": 35, "118": 66, "124": 66, "130": 71, "136": 71, "142": 76, "148": 76, "154": 148}}
__M_END_METADATA
"""
