# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552527741.529559
_enable_loop = True
_template_filename = 'C:/Users/the_m/Desktop/first_tutorial/mysite/catalog/templates/index.html'
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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        page = context.get('page', UNDEFINED)
        category = context.get('category', UNDEFINED)
        numpages = context.get('numpages', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
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
        page = context.get('page', UNDEFINED)
        category = context.get('category', UNDEFINED)
        numpages = context.get('numpages', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <h1 class = "text-center">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'Product' if category is None else category.name ))
        __M_writer('</h1>\r\n        <h3>Here are the products!</h3>\r\n        <h4 class="utc-time">I could have put some lorem ipsum here but I didn\'t....</h4>\r\n    </div>\r\n\r\n    <div id="catalog">\r\n')
        for product in products:
            __M_writer('            <span class="product-container" data-product-id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.id ))
            __M_writer('"></span>\r\n')
        __M_writer('    </div>\r\n\r\n    <div id="paginator" class="text-right">\r\n')
        if page > 1:
            __M_writer('            <a class="btn btn-secondary" href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 0 if category is None else category.id))
            __M_writer('/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page-1))
            __M_writer('/">Previous</a>\r\n')
        if page < numpages:
            __M_writer('            <a class="btn btn-secondary" id="move" href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 0 if category is None else category.id))
            __M_writer('/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page+1))
            __M_writer('/">Next</a>\r\n')
        __M_writer('    </div>\r\n    <br>\r\n    <br>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/the_m/Desktop/first_tutorial/mysite/catalog/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 26, "52": 3, "63": 3, "64": 5, "65": 5, "66": 11, "67": 12, "68": 12, "69": 12, "70": 14, "71": 17, "72": 18, "73": 18, "74": 18, "75": 18, "76": 18, "77": 20, "78": 21, "79": 21, "80": 21, "81": 21, "82": 21, "83": 23, "89": 83}}
__M_END_METADATA
"""
