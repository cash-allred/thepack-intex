# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554008491.9772904
_enable_loop = True
_template_filename = 'C:/Users/the_m/Desktop/first_tutorial/mysite/catalog/templates/checkout.html'
_template_uri = 'checkout.html'
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
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        settings = context.get('settings', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        form = context.get('form', UNDEFINED)
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
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context)
        settings = context.get('settings', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <form method="POST">\r\n        <script\r\n            src="https://checkout.stripe.com/checkout.js" class="stripe-button"\r\n            data-key="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( settings.STRIPE_PUBLIC_KEY ))
        __M_writer('"\r\n            data-amount=$')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cart.total * 100))
        __M_writer('\r\n            data-name="Demo Site"\r\n            data-description="Widget"\r\n            data-image="https://stripe.com/img/documentation/checkout/marketplace.png"\r\n            data-locale="auto">\r\n        </script>\r\n    <table>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_table() ))
        __M_writer('\r\n    </table>\r\n        <input type="submit" value="Submit">\r\n    </form>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/the_m/Desktop/first_tutorial/mysite/catalog/templates/checkout.html", "uri": "checkout.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "50": 3, "60": 3, "61": 8, "62": 8, "63": 9, "64": 9, "65": 16, "66": 16, "72": 66}}
__M_END_METADATA
"""
