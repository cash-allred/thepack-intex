# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554948104.7451525
_enable_loop = True
_template_filename = 'C:/Users/USER/intex2/thepack-intex/drugs/templates/details.html'
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
        relitems = context.get('relitems', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        range = context.get('range', UNDEFINED)
        drug = context.get('drug', UNDEFINED)
        doctors = context.get('doctors', UNDEFINED)
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
        relitems = context.get('relitems', UNDEFINED)
        def content():
            return render_content(context)
        range = context.get('range', UNDEFINED)
        drug = context.get('drug', UNDEFINED)
        doctors = context.get('doctors', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <h3>Drug Details</h3>\r\n        <div class="doctor-name">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug.drugName))
        __M_writer('</div>\r\n\r\n        <table>\r\n            <tr>\r\n                <th>Name</th>\r\n                <th>Opioid (T/F)</th>\r\n            </tr>\r\n            <tr>                \r\n                <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug.drugName))
        __M_writer('</td>\r\n                <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'T' if drug.isOpioid == 1 else 'F' ))
        __M_writer('</td>\r\n            </tr>\r\n        </table>\r\n        <br>\r\n        <br>\r\n        <br>\r\n        <h3>Top Prescribers of ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug.drugName))
        __M_writer('</h3>\r\n        <table>\r\n            <tr>\r\n                <th>Doctor ID</th>\r\n                <th>Ammount Prescribed</th>\r\n            </tr>\r\n')
        for x in range(10):
            __M_writer('                <tr>                \r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doctors[x].doctorID_id))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doctors[x].quantity))
            __M_writer('</td>\r\n                </tr>\r\n')
        __M_writer('        </table>\r\n        <div>\r\n            <h3>These are related Drugs based on prescription habits:</h3>\r\n            <p>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relitems[37]))
        __M_writer('</p>\r\n            <p>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relitems[39]))
        __M_writer('</p>\r\n            <p>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relitems[41]))
        __M_writer('</p>\r\n            <p>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relitems[43]))
        __M_writer('</p>\r\n            <p>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relitems[45]))
        __M_writer('</p>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/USER/intex2/thepack-intex/drugs/templates/details.html", "uri": "details.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "51": 3, "62": 3, "63": 6, "64": 6, "65": 14, "66": 14, "67": 15, "68": 15, "69": 21, "70": 21, "71": 27, "72": 28, "73": 29, "74": 29, "75": 30, "76": 30, "77": 33, "78": 36, "79": 36, "80": 37, "81": 37, "82": 38, "83": 38, "84": 39, "85": 39, "86": 40, "87": 40, "93": 87}}
__M_END_METADATA
"""
