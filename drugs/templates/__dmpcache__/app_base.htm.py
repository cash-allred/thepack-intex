# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
<<<<<<< HEAD
_modified_time = 1555003634.961567
_enable_loop = True
_template_filename = 'C:/Users/USER/intex2/thepack-intex/drugs/templates/app_base.htm'
=======
_modified_time = 1555004484.9012296
_enable_loop = True
_template_filename = 'C:/Users/the_m/Desktop/intex_website/mysite/drugs/templates/app_base.htm'
>>>>>>> d31b487aa03192863b6112820e4703e6b89099d7
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
<<<<<<< HEAD
_exports = ['navbar_items', 'left_menu']
=======
_exports = ['navbar_items', 'left_content']
>>>>>>> d31b487aa03192863b6112820e4703e6b89099d7


from catalog import models as cmod 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def navbar_items():
            return render_navbar_items(context._locals(__M_locals))
<<<<<<< HEAD
        def left_menu():
            return render_left_menu(context._locals(__M_locals))
=======
        def left_content():
            return render_left_content(context._locals(__M_locals))
>>>>>>> d31b487aa03192863b6112820e4703e6b89099d7
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_items'):
            context['self'].navbar_items(**pageargs)
        

        __M_writer('\r\n\r\n')
<<<<<<< HEAD
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_menu'):
            context['self'].left_menu(**pageargs)
=======
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
>>>>>>> d31b487aa03192863b6112820e4703e6b89099d7
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_items():
            return render_navbar_items(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


<<<<<<< HEAD
def render_left_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_menu():
            return render_left_menu(context)
=======
def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_content():
            return render_left_content(context)
>>>>>>> d31b487aa03192863b6112820e4703e6b89099d7
        __M_writer = context.writer()
        __M_writer('\r\n    \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
<<<<<<< HEAD
{"filename": "C:/Users/USER/intex2/thepack-intex/drugs/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"18": 3, "31": 0, "40": 1, "45": 5, "55": 2, "61": 2, "62": 3, "68": 7, "74": 7, "80": 74}}
=======
{"filename": "C:/Users/the_m/Desktop/intex_website/mysite/drugs/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"18": 3, "31": 0, "40": 1, "45": 5, "55": 2, "61": 2, "62": 3, "68": 7, "74": 7, "80": 74}}
>>>>>>> d31b487aa03192863b6112820e4703e6b89099d7
__M_END_METADATA
"""
