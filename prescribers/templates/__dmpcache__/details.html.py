# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555005421.1713188
_enable_loop = True
_template_filename = 'C:/Users/USER/intex2/thepack-intex/prescribers/templates/details.html'
_template_uri = 'details.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'content']


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
        relusers = context.get('relusers', UNDEFINED)
        doctor = context.get('doctor', UNDEFINED)
        avgs1 = context.get('avgs1', UNDEFINED)
        prescriptions = context.get('prescriptions', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Dr. Details')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        doctor = context.get('doctor', UNDEFINED)
        avgs1 = context.get('avgs1', UNDEFINED)
        prescriptions = context.get('prescriptions', UNDEFINED)
        def content():
            return render_content(context)
        relusers = context.get('relusers', UNDEFINED)
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
            __M_writer('</td>\r\n                    </tr>\r\n                </tbody>\r\n            </table>\r\n            <!--ADD IF STATEMENT TO MAKE SURE ONLY DATACLERKS HAVE ACCESS-->\r\n            <a href="/homepage/updateDoctor/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc.doctorID))
            __M_writer('"> Update Doctor</a>\r\n')
        __M_writer('        <h3>Prescriber Drug Prescriptions</h3>\r\n        <table class="table">\r\n            <thead class="thead-light">\r\n                <tr>\r\n                    <th scope="col">Drug Name</th>\r\n                    <th scope="col">Amount Prescribed</th>\r\n                    <th scope="col">Average Prescribed in the Country</th>\r\n                    <th scope="col">Details</th>\r\n                </tr>\r\n            </thead>\r\n            <tbody>\r\n                ')
        i = 0 
        
        __M_writer('\r\n')
        for script in prescriptions:
            __M_writer('                <tr>                \r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(script.drugName.drugName))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(script.quantity))
            __M_writer('</td>\r\n                    <td><strong>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(avgs1[i][18:23]))
            __M_writer('</strong></td>\r\n                    <td><a class="btn btn-primary" href="/drugs/details/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(script.drugName.id))
            __M_writer('" role="button">Details</a><td>\r\n                </tr>\r\n                ')
            i += 1 
            
            __M_writer('\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n        <h3>Top 5 Related Doctors:</h3>\r\n        <table class="table">\r\n            <thead class="thead-light">\r\n                <tr>\r\n                    <th scope="col">#</th>\r\n                    <th scope="col">Doctor ID:</th>\r\n                    <th scope="col">Details</th>\r\n                </tr>\r\n            </thead>\r\n            <tbody>\r\n                <tr>\r\n                    <th scope="row">1</th>\r\n                    <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relusers[37]))
        __M_writer('</td>\r\n                    <td><a  class="btn btn-primary" href="/prescribers/details/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relusers[37]))
        __M_writer('" role="button">Details</a><td>\r\n                </tr>\r\n                <tr>\r\n                    <th scope="row">2</th>\r\n                    <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relusers[39]))
        __M_writer('</td>\r\n                    <td><a  class="btn btn-primary" href="/prescribers/details/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relusers[39]))
        __M_writer('" role="button">Details</a><td>\r\n                </tr>\r\n                <tr>\r\n                    <th scope="row">3</th>\r\n                    <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relusers[41]))
        __M_writer('</td>\r\n                    <td><a  class="btn btn-primary" href="/prescribers/details/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relusers[39]))
        __M_writer('" role="button">Details</a><td>\r\n                </tr>\r\n                <tr>\r\n                    <th scope="row">4</th>\r\n                    <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relusers[43]))
        __M_writer('</td>\r\n                    <td><a  class="btn btn-primary" href="/prescribers/details/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relusers[39]))
        __M_writer('" role="button">Details</a><td>\r\n                </tr>\r\n                <tr>\r\n                    <th scope="row">5</th>\r\n                    <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relusers[45]))
        __M_writer('</td>\r\n                    <td><a  class="btn btn-primary" href="/prescribers/details/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relusers[39]))
        __M_writer('" role="button">Details</a><td>\r\n                </tr>\r\n            </tbody>\r\n        </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/USER/intex2/thepack-intex/prescribers/templates/details.html", "uri": "details.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 3, "58": 3, "64": 3, "70": 5, "81": 5, "82": 7, "83": 8, "84": 8, "85": 8, "86": 8, "87": 8, "88": 23, "89": 23, "90": 24, "91": 24, "92": 25, "93": 25, "94": 26, "95": 26, "96": 27, "97": 27, "98": 28, "99": 28, "100": 33, "101": 33, "102": 35, "103": 46, "105": 46, "106": 47, "107": 48, "108": 49, "109": 49, "110": 50, "111": 50, "112": 51, "113": 51, "114": 52, "115": 52, "116": 54, "118": 54, "119": 56, "120": 70, "121": 70, "122": 71, "123": 71, "124": 75, "125": 75, "126": 76, "127": 76, "128": 80, "129": 80, "130": 81, "131": 81, "132": 85, "133": 85, "134": 86, "135": 86, "136": 90, "137": 90, "138": 91, "139": 91, "145": 139}}
__M_END_METADATA
"""
