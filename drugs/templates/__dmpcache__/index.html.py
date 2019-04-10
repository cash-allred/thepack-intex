# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554928406.213135
_enable_loop = True
_template_filename = 'C:/Users/USER/intex2/thepack-intex/drugs/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


from homepage import models as hmod 

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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <h3>This is the Drug Page</h3>\r\n    </div>\r\n    <div>\r\n        <ul id="limheight">\r\n')
        for object in hmod.Drug.objects.all():
            __M_writer('                <li><a href="#">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(object.drugName))
            __M_writer('</a></li>\r\n')
        __M_writer('        </ul>\r\n        \r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/USER/intex2/thepack-intex/drugs/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "39": 1, "40": 2, "45": 16, "51": 4, "58": 4, "59": 10, "60": 11, "61": 11, "62": 11, "63": 13, "69": 63}}
__M_END_METADATA
"""
