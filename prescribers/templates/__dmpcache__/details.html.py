# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554919736.2598896
_enable_loop = True
_template_filename = 'C:/Users/the_m/Desktop/intex_website/mysite/prescribers/templates/details.html'
_template_uri = 'details.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        prescriptions = context.get('prescriptions', UNDEFINED)
        self = context.get('self', UNDEFINED)
        doctor = context.get('doctor', UNDEFINED)
        average = context.get('average', UNDEFINED)
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
        prescriptions = context.get('prescriptions', UNDEFINED)
        self = context.get('self', UNDEFINED)
        doctor = context.get('doctor', UNDEFINED)
        average = context.get('average', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <h3>Presriber Details</h3>\r\n')
        for doc in doctor:
            __M_writer('            <div class="doctor-name">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc.fName))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc.lName))
            __M_writer('</div>\r\n            <table>\r\n                <tr>\r\n                    <th>Credentials</th>\r\n                    <th>Opioid Presriber</th>\r\n                    <th>Specialty</th>\r\n                    <th>State</th>\r\n                    <th>Gender</th>\r\n                    <th>Total Prescriptions/Year</th>\r\n                </tr>\r\n                <tr>                \r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc.credentials))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)('Yes' if doc.opioidPrescriber == 1 else 'No'))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc.specialty))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc.state))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)('Male' if doc.gender == 'M' else 'Female'))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc.totalPrescriptions))
            __M_writer('</td>\r\n                </tr>\r\n            </table>\r\n')
        __M_writer('\r\n        <h3>Presriber Drug Prescriptions</h3>\r\n        <table>\r\n                <tr>\r\n                    <th>Drug Name</th>\r\n                    <th>Ammount Prescribed</th>\r\n                    <th>Average Prescribed in the Country</th>\r\n                </tr>\r\n')
        for script in prescriptions:
            __M_writer('                <tr>                \r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(script.drugName.drugName))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(script.quantity))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(average[script.drugName]))
            __M_writer('\r\n                </tr>\r\n')
        __M_writer('            </table>\r\n        \r\n\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/the_m/Desktop/intex_website/mysite/prescribers/templates/details.html", "uri": "details.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "50": 3, "60": 3, "61": 6, "62": 7, "63": 7, "64": 7, "65": 7, "66": 7, "67": 18, "68": 18, "69": 19, "70": 19, "71": 20, "72": 20, "73": 21, "74": 21, "75": 22, "76": 22, "77": 23, "78": 23, "79": 27, "80": 35, "81": 36, "82": 37, "83": 37, "84": 38, "85": 38, "86": 39, "87": 39, "88": 42, "94": 88}}
__M_END_METADATA
"""
