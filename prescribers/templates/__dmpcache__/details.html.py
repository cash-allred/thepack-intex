# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554998350.497595
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
        relusers = context.get('relusers', UNDEFINED)
        self = context.get('self', UNDEFINED)
        doctor = context.get('doctor', UNDEFINED)
        prescriptions = context.get('prescriptions', UNDEFINED)
        avgs1 = context.get('avgs1', UNDEFINED)
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
        def content():
            return render_content(context)
        relusers = context.get('relusers', UNDEFINED)
        self = context.get('self', UNDEFINED)
        doctor = context.get('doctor', UNDEFINED)
        prescriptions = context.get('prescriptions', UNDEFINED)
        avgs1 = context.get('avgs1', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n')
        for doc in doctor:
            __M_writer('            <div class="doctor-name"><h2>Dr. ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc.fName))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc.lName))
            __M_writer(':</h2></div>\r\n            <h3>Prescriber Details</h3>\r\n            <table class="table">\r\n                <thead class="thead-light">\r\n                    <tr>\r\n                        <th scope="col">Credentials</th>\r\n                        <th scope="col">Opioid Presriber</th>\r\n                        <th scope="col">Specialty</th>\r\n                        <th scope="col">State</th>\r\n                        <th scope="col">Gender</th>\r\n                        <th scope="col">Total Prescriptions/Year</th>\r\n                    </tr>\r\n                </thead>\r\n                <tbody>\r\n                    <tr>                \r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc.credentials))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)('Yes' if doc.opioidPrescriber == 1 else 'No'))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc.specialty))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc.state))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)('Male' if doc.gender == 'M' else 'Female'))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc.totalPrescriptions))
            __M_writer('</td>\r\n                    </tr>\r\n                </tbody>\r\n            </table>\r\n')
        __M_writer('        <h3>Prescriber Drug Prescriptions</h3>\r\n        <table class="table">\r\n            <thead class="thead-light">\r\n                <tr>\r\n                    \r\n                    <th scope="col">Drug Name</th>\r\n                    <th scope="col">Amount Prescribed</th>\r\n                    <th scope="col">Average Prescribed in the Country</th>\r\n                </tr>\r\n            </thead>\r\n            <tbody>\r\n                ')
        i = 0 
        
        __M_writer('\r\n')
        for script in prescriptions:
            __M_writer('                <tr>                \r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(script.drugName.drugName))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(script.quantity))
            __M_writer('</td>\r\n                    <td><strong>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(avgs1[i][18:23]))
            __M_writer('</strong></td>\r\n                </tr>\r\n                ')
            i += 1 
            
            __M_writer('\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n        <h3>Top 5 Related Doctors:</h3>\r\n        <table class="table">\r\n            <thead class="thead-light">\r\n                <tr>\r\n                    <th scope="col">#</th>\r\n                    <th scope="col">Doctor ID:</th>\r\n                </tr>\r\n            </thead>\r\n            <tbody>\r\n                <tr>\r\n                    <th scope="row">1</th>\r\n                    <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relusers[37]))
        __M_writer('</td>\r\n                </tr>\r\n                <tr>\r\n                    <th scope="row">2</th>\r\n                    <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relusers[39]))
        __M_writer('</td>\r\n                </tr>\r\n                <tr>\r\n                    <th scope="row">3</th>\r\n                    <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relusers[41]))
        __M_writer('</td>\r\n                </tr>\r\n                <tr>\r\n                    <th scope="row">4</th>\r\n                    <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relusers[43]))
        __M_writer('</td>\r\n                </tr>\r\n                <tr>\r\n                    <th scope="row">5</th>\r\n                    <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relusers[45]))
        __M_writer('</td>\r\n                </tr>\r\n            </tbody>\r\n        </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/the_m/Desktop/intex_website/mysite/prescribers/templates/details.html", "uri": "details.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "51": 4, "62": 4, "63": 6, "64": 7, "65": 7, "66": 7, "67": 7, "68": 7, "69": 22, "70": 22, "71": 23, "72": 23, "73": 24, "74": 24, "75": 25, "76": 25, "77": 26, "78": 26, "79": 27, "80": 27, "81": 32, "82": 43, "84": 43, "85": 44, "86": 45, "87": 46, "88": 46, "89": 47, "90": 47, "91": 48, "92": 48, "93": 50, "95": 50, "96": 52, "97": 65, "98": 65, "99": 69, "100": 69, "101": 73, "102": 73, "103": 77, "104": 77, "105": 81, "106": 81, "112": 106}}
__M_END_METADATA
"""
