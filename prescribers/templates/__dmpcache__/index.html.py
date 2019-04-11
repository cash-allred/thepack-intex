# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555005349.5096774
_enable_loop = True
_template_filename = 'C:/Users/USER/intex2/thepack-intex/prescribers/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'content', 'left_content']


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
        def left_content():
            return render_left_content(context._locals(__M_locals))
        doctors = context.get('doctors', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Prescribers')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        doctors = context.get('doctors', UNDEFINED)
        def content():
            return render_content(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        \r\n    </div>\r\n\r\n    <div id="catalog">\r\n    <table class="table table-hover">\r\n        <thead>\r\n            <tr>\r\n                <th scope="col">Doctor ID</th>\r\n                <th scope="col">Name</th>\r\n                <th scope="col">Details</th>\r\n            </tr>\r\n        </thead>\r\n        <tbody>\r\n            ')
        i = 1 
        
        __M_writer('\r\n')
        for doctor in doctors:
            __M_writer('                <span class="product-container" data-product-id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctor.doctorID ))
            __M_writer('"></span>\r\n                <tr>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctor.doctorID ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctor.fName ))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctor.lName ))
            __M_writer('</td>\r\n                    <td><a  class="btn btn-primary" href="/prescribers/details/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doctor.doctorID))
            __M_writer('" role="button">Details</a><td>\r\n                </tr>\r\n                ')
            i += 1 
            
            __M_writer('\r\n')
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
        __M_writer('\r\n    <br>\r\n    <h3>Doctor Search</h3>\r\n    <br>\r\n    <form method="POST">\r\n        <table>\r\n            ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_table() ))
        __M_writer('\r\n        </table>\r\n        <input type="submit" value="Search"> \r\n    </form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/USER/intex2/thepack-intex/prescribers/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 2, "53": 31, "63": 2, "69": 2, "75": 3, "83": 3, "84": 18, "86": 18, "87": 19, "88": 20, "89": 20, "90": 20, "91": 22, "92": 22, "93": 23, "94": 23, "95": 23, "96": 23, "97": 24, "98": 24, "99": 26, "101": 26, "102": 28, "108": 33, "116": 33, "117": 39, "118": 39, "124": 118}}
__M_END_METADATA
"""
