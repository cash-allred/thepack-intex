# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553741278.1287699
_enable_loop = True
_template_filename = 'C:/Users/the_m/Desktop/first_tutorial/mysite/catalog/templates/product.html'
_template_uri = 'product.html'
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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        images = context.get('images', UNDEFINED)
        product = context.get('product', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        images = context.get('images', UNDEFINED)
        product = context.get('product', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <div>\r\n')
        for i in images:
            __M_writer('        <img class="thumbnail" src=\'')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(i))
            __M_writer("'>\r\n")
        __M_writer('    <img class="main-image" src=')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(images[0]))
        __M_writer('>\r\n    <div class="product-name">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.name))
        __M_writer('</div>\r\n    <div class="product-price">Price: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.price))
        __M_writer('</div>\r\n    <div class="product-description">Description: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.description))
        __M_writer('</div>\r\n\r\n  <form  method="post">\r\n    <table>\r\n      ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_table() ))
        __M_writer(' \r\n    </table>\r\n    <input type="submit" value="Submit">\r\n  </form>\r\n  </div>\r\n<div><br><br></div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/the_m/Desktop/first_tutorial/mysite/catalog/templates/product.html", "uri": "product.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 22, "51": 3, "61": 3, "62": 5, "63": 6, "64": 6, "65": 6, "66": 8, "67": 8, "68": 8, "69": 9, "70": 9, "71": 10, "72": 10, "73": 11, "74": 11, "75": 15, "76": 15, "82": 76}}
__M_END_METADATA
"""
