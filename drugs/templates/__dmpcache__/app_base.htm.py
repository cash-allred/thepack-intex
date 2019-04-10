# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554928406.2290924
_enable_loop = True
_template_filename = 'C:/Users/USER/intex2/thepack-intex/drugs/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['navbar_items', 'left_menu']


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
        self = context.get('self', UNDEFINED)
        def left_menu():
            return render_left_menu(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_items'):
            context['self'].navbar_items(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_menu'):
            context['self'].left_menu(**pageargs)
        

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


def render_left_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        def left_menu():
            return render_left_menu(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <h3>Categories</h3>\r\n    <ul class=\'no_bullets\'>\r\n        <!--Do we need to have the category ID be dynamic?-->\r\n        <li><a href="/catalog/index/">All categories</a></li>\r\n')
        for cat in cmod.Category.objects.order_by('name'):
            __M_writer('            <li><a href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cat.id ))
            __M_writer('/">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cat.name ))
            __M_writer('</a></li>  \r\n')
        __M_writer('    <ul>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/USER/intex2/thepack-intex/drugs/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"18": 3, "31": 0, "41": 1, "46": 5, "56": 2, "62": 2, "63": 3, "69": 7, "76": 7, "77": 12, "78": 13, "79": 13, "80": 13, "81": 13, "82": 13, "83": 15, "89": 83}}
__M_END_METADATA
"""
