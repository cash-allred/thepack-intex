# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554011123.9086628
_enable_loop = True
_template_filename = 'C:/Users/the_m/Desktop/first_tutorial/mysite/catalog/templates/cart.html'
_template_uri = 'cart.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        si = context.get('si', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        self = context.get('self', UNDEFINED)
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
        def content():
            return render_content(context)
        si = context.get('si', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <table style="width:100%">\r\n        <tr>\r\n            <th>Product Image</th>\r\n            <th>Product Name</th>\r\n            <th>Quantity</th>\r\n            <th>Price</th>\r\n            <th>Extended</th>\r\n            <th>Actions</th>\r\n        </tr>\r\n')
        for i in si:
            __M_writer('            <tr>\r\n                <td><img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(i.product.image_url()))
            __M_writer('" height="50px" alt=""></td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(i.product.name))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(i.quantity))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(i.product.price))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(i.product.price*i.quantity))
            __M_writer('</td>\r\n            </tr>\r\n')
        __M_writer('            <tr>\r\n                <td></td>\r\n                <td>Tax</td>\r\n                <td></td>\r\n                <td></td>\r\n                <td>$')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(cart.tax))
        __M_writer('</td>\r\n            </tr>\r\n    <table>\r\n    <a class="btn btn-success" href="/catalog/checkout/">Checkout</a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/the_m/Desktop/first_tutorial/mysite/catalog/templates/cart.html", "uri": "cart.html", "source_encoding": "utf-8", "line_map": {"29": 0, "39": 1, "49": 3, "58": 3, "59": 14, "60": 15, "61": 16, "62": 16, "63": 17, "64": 17, "65": 18, "66": 18, "67": 19, "68": 19, "69": 20, "70": 20, "71": 23, "72": 28, "73": 28, "79": 73}}
__M_END_METADATA
"""
