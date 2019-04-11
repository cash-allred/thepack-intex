# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554946849.0149817
_enable_loop = True
_template_filename = 'C:/Users/USER/intex2/thepack-intex/prescribers/templates/details.html'
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
        avgs1 = context.get('avgs1', UNDEFINED)
        relusers = context.get('relusers', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        doctor = context.get('doctor', UNDEFINED)
        average = context.get('average', UNDEFINED)
        prescriptions = context.get('prescriptions', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        avgs1 = context.get('avgs1', UNDEFINED)
        relusers = context.get('relusers', UNDEFINED)
        def content():
            return render_content(context)
        doctor = context.get('doctor', UNDEFINED)
        average = context.get('average', UNDEFINED)
        prescriptions = context.get('prescriptions', UNDEFINED)
        self = context.get('self', UNDEFINED)
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
        __M_writer('\r\n        <h3>Presriber Drug Prescriptions</h3>\r\n        <table>\r\n            <tr>\r\n                <th>Drug Name</th>\r\n                <th>Ammount Prescribed</th>\r\n                <th>Average Prescribed in the Country</th>\r\n            </tr>\r\n            \r\n')
        for script in prescriptions:
            __M_writer('            <tr>                \r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(script.drugName.drugName))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(script.quantity))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(average[script.drugName]))
            __M_writer('</td>\r\n            </tr>\r\n')
        for value in avgs1:
            __M_writer('            <tr>                \r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(value[18:23]))
            __M_writer('</td>\r\n            </tr>\r\n')
        __M_writer('        </table>\r\n        <div>\r\n            <p>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relusers[37]))
        __M_writer('</p>\r\n            <p>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relusers[39]))
        __M_writer('</p>\r\n            <p>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relusers[41]))
        __M_writer('</p>\r\n            <p>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relusers[43]))
        __M_writer('</p>\r\n            <p>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relusers[45]))
        __M_writer('</p>\r\n        </div>\r\n        \r\n\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/USER/intex2/thepack-intex/prescribers/templates/details.html", "uri": "details.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "52": 4, "64": 4, "65": 7, "66": 8, "67": 8, "68": 8, "69": 8, "70": 8, "71": 19, "72": 19, "73": 20, "74": 20, "75": 21, "76": 21, "77": 22, "78": 22, "79": 23, "80": 23, "81": 24, "82": 24, "83": 28, "84": 37, "85": 38, "86": 39, "87": 39, "88": 40, "89": 40, "90": 41, "91": 41, "92": 44, "93": 45, "94": 46, "95": 46, "96": 49, "97": 51, "98": 51, "99": 52, "100": 52, "101": 53, "102": 53, "103": 54, "104": 54, "105": 55, "106": 55, "112": 106}}
__M_END_METADATA
"""
