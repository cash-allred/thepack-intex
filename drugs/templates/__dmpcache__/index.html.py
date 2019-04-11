# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554947564.8278525
_enable_loop = True
_template_filename = 'C:/Users/USER/intex2/thepack-intex/drugs/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content', 'right_content']


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
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context)
        drugs = context.get('drugs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <h3>This is the Drug Page</h3>\r\n    </div>\r\n    <div id="catalog">\r\n    <table>\r\n        <tr>\r\n            <th>Drug Name</th>\r\n            <th>Opioid(T/F)</th>\r\n            <th>Details</th>\r\n        </tr>\r\n')
        for d in drugs:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( d.drugName ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'T' if d.isOpioid == 1 else 'F' ))
            __M_writer('</td>\r\n                <td><a href="/drugs/details/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(d.id))
            __M_writer('">Details</a><td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        self = context.get('self', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <form method="POST">\r\n        <table>\r\n            ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_table() ))
        __M_writer('\r\n        </table>\r\n        <input type="submit" value="Search"> \r\n    </form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/USER/intex2/thepack-intex/drugs/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "43": 1, "44": 2, "49": 24, "54": 33, "60": 4, "68": 4, "69": 15, "70": 16, "71": 17, "72": 17, "73": 18, "74": 18, "75": 19, "76": 19, "77": 22, "83": 26, "91": 26, "92": 29, "93": 29, "99": 93}}
__M_END_METADATA
"""
