# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554846768.8879507
_enable_loop = True
_template_filename = 'C:/Users/the_m/Desktop/intex_website/mysite/prescribers/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


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
        doctors = context.get('doctors', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        doctors = context.get('doctors', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <h3>Here are the Doctors!</h3>\r\n        <h4 class="utc-time">I could have put some lorem ipsum here but I didn\'t....</h4>\r\n    </div>\r\n\r\n    <div id="catalog">\r\n    <table>\r\n        <tr>\r\n            <th>Doctor ID</th>\r\n            <th>Name</th>\r\n        </tr>\r\n')
        for doctor in doctors:
            __M_writer('            <span class="product-container" data-product-id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctor.doctorID ))
            __M_writer('"></span>\r\n            <tr>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctor.doctorID ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctor.fName ))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctor.lName ))
            __M_writer('</td>\r\n            </tr>\r\n')
        __M_writer('\r\n    </table>\r\n    </div>\r\n\r\n    <br>\r\n    <br>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/the_m/Desktop/intex_website/mysite/prescribers/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "48": 3, "56": 3, "57": 15, "58": 16, "59": 16, "60": 16, "61": 18, "62": 18, "63": 19, "64": 19, "65": 19, "66": 19, "67": 22, "73": 67}}
__M_END_METADATA
"""
