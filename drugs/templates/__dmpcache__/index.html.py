# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555004016.6089537
_enable_loop = True
_template_filename = 'C:/Users/the_m/Desktop/intex_website/mysite/drugs/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content', 'left_content']


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
        def left_content():
            return render_left_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

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
        drugs = context.get('drugs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        \r\n    </div>\r\n    <div id="catalog">\r\n    <table class="table table-hover">\r\n        <thead>\r\n            <tr>\r\n                <th scope="col">Drug Name</th>\r\n                <th scope="col">Opioid(T/F)</th>\r\n                <th scope="col">Details</th>\r\n            </tr>\r\n        </thead>\r\n        <tbody>\r\n')
        for d in drugs:
            __M_writer('                <tr>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( d.drugName ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'T' if d.isOpioid == 1 else 'F' ))
            __M_writer('</td>\r\n                    <td><a  class="btn btn-primary" href="/drugs/details/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(d.id))
            __M_writer('" role="button">Details</a><td>\r\n                </tr>\r\n')
        __M_writer('        </tbody>\r\n    </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def left_content():
            return render_left_content(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <form method="POST">\r\n        <table>\r\n            ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_table() ))
        __M_writer('\r\n        </table>\r\n        <input type="submit" value="Search"> \r\n    </form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/the_m/Desktop/intex_website/mysite/drugs/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "43": 1, "44": 2, "49": 28, "54": 37, "60": 4, "68": 4, "69": 18, "70": 19, "71": 20, "72": 20, "73": 21, "74": 21, "75": 22, "76": 22, "77": 25, "83": 30, "91": 30, "92": 33, "93": 33, "99": 93}}
__M_END_METADATA
"""
