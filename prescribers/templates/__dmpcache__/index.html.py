# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
<<<<<<< HEAD
_modified_time = 1554865014.2508924
_enable_loop = True
_template_filename = 'C:/Users/the_m/Desktop/intex_website/mysite/prescribers/templates/index.html'
=======
_modified_time = 1554912805.6456318
_enable_loop = True
_template_filename = 'C:/Users/Katrina/Documents/INTEXII/thepack-intex/prescribers/templates/index.html'
>>>>>>> ff5af270e52db116cac38f9c6aa0d0b120798fe1
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content', 'right_content']


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
<<<<<<< HEAD
        def content():
            return render_content(context._locals(__M_locals))
        doctors = context.get('doctors', UNDEFINED)
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
=======
        def right_content():
            return render_right_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        doctors = context.get('doctors', UNDEFINED)
        self = context.get('self', UNDEFINED)
>>>>>>> ff5af270e52db116cac38f9c6aa0d0b120798fe1
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
<<<<<<< HEAD
        doctors = context.get('doctors', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <h3>Here are the Doctors!</h3>\r\n    </div>\r\n\r\n    <div id="catalog">\r\n    <table>\r\n        <tr>\r\n            <th>Doctor ID</th>\r\n            <th>Name</th>\r\n            <th>Details</th>\r\n        </tr>\r\n')
=======
        def content():
            return render_content(context)
        doctors = context.get('doctors', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <h3>Here are the Doctors!</h3>\r\n    </div>\r\n\r\n    <div id="catalog">\r\n    <table>\r\n        <tr>\r\n            <th>Doctor ID</th>\r\n            <th>Name</th>\r\n        </tr>\r\n')
>>>>>>> ff5af270e52db116cac38f9c6aa0d0b120798fe1
        for doctor in doctors:
            __M_writer('            <span class="product-container" data-product-id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctor.doctorID ))
            __M_writer('"></span>\r\n            <tr>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctor.doctorID ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctor.fName ))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctor.lName ))
<<<<<<< HEAD
            __M_writer('</td>\r\n                <td><a href="/prescribers/details/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doctor.doctorID))
            __M_writer('">Details</a><td>\r\n            </tr>\r\n')
=======
            __M_writer('</td>\r\n            </tr>\r\n')
>>>>>>> ff5af270e52db116cac38f9c6aa0d0b120798fe1
        __M_writer('\r\n    </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
<<<<<<< HEAD
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <form method="POST">\r\n        <table>\r\n            ')
=======
        self = context.get('self', UNDEFINED)
        def right_content():
            return render_right_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <!-- This is not the django form, this is a simple HTML form\r\n    <form class="form-inline my-2 my-lg-0">\r\n        <input class="form-control mr-sm-2" type="search" placeholder="First Name" aria-label="First Name">\r\n        <input class="form-control mr-sm-2" type="search" placeholder="Last Name" aria-label="Last Name">\r\n        <input class="form-control mr-sm-2" type="search" placeholder="Gender" aria-label="Gender">\r\n        <input class="form-control mr-sm-2" type="search" placeholder="Credentials" aria-label="Credentials">\r\n        <input class="form-control mr-sm-2" type="search" placeholder="State" aria-label="State">        \r\n        <input class="form-control mr-sm-2" type="search" placeholder="Specialty" aria-label="Specialty">\r\n        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search Prescribers</button>\r\n    </form>-->\r\n    <form method="POST">\r\n        <table>\r\n            ')
>>>>>>> ff5af270e52db116cac38f9c6aa0d0b120798fe1
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_table() ))
        __M_writer('\r\n        </table>\r\n        <input type="submit" value="Search"> \r\n    </form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
<<<<<<< HEAD
{"filename": "C:/Users/the_m/Desktop/intex_website/mysite/prescribers/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 26, "56": 3, "64": 3, "65": 15, "66": 16, "67": 16, "68": 16, "69": 18, "70": 18, "71": 19, "72": 19, "73": 19, "74": 19, "75": 20, "76": 20, "77": 23, "83": 28, "91": 28, "92": 31, "93": 31, "99": 93}}
=======
{"filename": "C:/Users/Katrina/Documents/INTEXII/thepack-intex/prescribers/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 24, "56": 3, "64": 3, "65": 14, "66": 15, "67": 15, "68": 15, "69": 17, "70": 17, "71": 18, "72": 18, "73": 18, "74": 18, "75": 21, "81": 26, "89": 26, "90": 39, "91": 39, "97": 91}}
>>>>>>> ff5af270e52db116cac38f9c6aa0d0b120798fe1
__M_END_METADATA
"""
