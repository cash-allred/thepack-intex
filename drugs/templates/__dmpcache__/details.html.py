# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555003719.981039
_enable_loop = True
_template_filename = 'C:/Users/USER/intex2/thepack-intex/drugs/templates/details.html'
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
        self = context.get('self', UNDEFINED)
        links = context.get('links', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        range = context.get('range', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        doctors = context.get('doctors', UNDEFINED)
        drug = context.get('drug', UNDEFINED)
        relitems = context.get('relitems', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n')
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
        __M_writer('Drug Details')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        links = context.get('links', UNDEFINED)
        def content():
            return render_content(context)
        range = context.get('range', UNDEFINED)
        doctors = context.get('doctors', UNDEFINED)
        drug = context.get('drug', UNDEFINED)
        relitems = context.get('relitems', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <h3>Drug Details</h3>\r\n        <table class="table">\r\n            <thead class="thead-light">\r\n                <tr>\r\n                    <th>Name</th>\r\n                    <th>Opioid (T/F)</th>\r\n                </tr>\r\n            </thead>\r\n            <tbody>\r\n                <tr>                \r\n                    <th>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug.drugName))
        __M_writer('</th>\r\n                    <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'T' if drug.isOpioid == 1 else 'F' ))
        __M_writer('</td>\r\n                </tr>\r\n            </tbody>\r\n        </table>\r\n        <br>\r\n        <br>\r\n        <br>\r\n        <h3>Top Prescribers of ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug.drugName))
        __M_writer('</h3>\r\n        <table class="table">\r\n            <thead class="thead-light">\r\n                <tr>\r\n                    <th scope="col">Doctor ID</th>\r\n                    <th scope="col">Ammount Prescribed</th>\r\n                    <th scope="col">Details</th>\r\n                </tr>\r\n            </thead>\r\n            <tbody>\r\n')
        for x in range(10):
            __M_writer('                <tr>                \r\n                    <th scope="row">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doctors[x].doctorID_id))
            __M_writer('</th>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doctors[x].quantity))
            __M_writer('</td>\r\n                    <td><a  class="btn btn-primary" href="/prescribers/details/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doctors[x].doctorID_id))
            __M_writer('" role="button">Details</a><td>\r\n                </tr>\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n         <h3>Top 5 Drugs Commonly Prescribed with ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug.drugName))
        __M_writer(':</h3>\r\n        <table class="table">\r\n            <thead class="thead-light">\r\n                <tr>\r\n                    <th scope="col">#</th>\r\n                    <th scope="col">Drug Name:</th>\r\n                    <th scope="col">Details</th>\r\n                </tr>\r\n            </thead>\r\n            <tbody>\r\n                <tr>\r\n                    <th scope="row">1</th>\r\n                    <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relitems[37]))
        __M_writer('</td>\r\n                    <td><a class="btn btn-primary" href="/drugs/details/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(links[0].id))
        __M_writer('" role="button">Details</a><td>\r\n                </tr>\r\n                <tr>\r\n                    <th scope="row">2</th>\r\n                    <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relitems[39]))
        __M_writer('</td>\r\n                    <td><a class="btn btn-primary" href="/drugs/details/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(links[1].id))
        __M_writer('" role="button">Details</a><td>\r\n                </tr>\r\n                <tr>\r\n                    <th scope="row">3</th>\r\n                    <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relitems[41]))
        __M_writer('</td>\r\n                    <td><a class="btn btn-primary" href="/drugs/details/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(links[2].id))
        __M_writer('" role="button">Details</a><td>\r\n                </tr>\r\n                <tr>\r\n                    <th scope="row">4</th>\r\n                    <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relitems[43]))
        __M_writer('</td>\r\n                    <td><a class="btn btn-primary" href="/drugs/details/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(links[3].id))
        __M_writer('" role="button">Details</a><td>\r\n                </tr>\r\n                <tr>\r\n                    <th scope="row">5</th>\r\n                    <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(relitems[45]))
        __M_writer('</td>\r\n                    <td><a class="btn btn-primary" href="/drugs/details/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(links[4].id))
        __M_writer('" role="button">Details</a><td>\r\n                </tr>\r\n            </tbody>\r\n        </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/USER/intex2/thepack-intex/drugs/templates/details.html", "uri": "details.html", "source_encoding": "utf-8", "line_map": {"29": 0, "44": 1, "49": 3, "59": 3, "65": 3, "71": 4, "83": 4, "84": 16, "85": 16, "86": 17, "87": 17, "88": 24, "89": 24, "90": 34, "91": 35, "92": 36, "93": 36, "94": 37, "95": 37, "96": 38, "97": 38, "98": 41, "99": 43, "100": 43, "101": 55, "102": 55, "103": 56, "104": 56, "105": 60, "106": 60, "107": 61, "108": 61, "109": 65, "110": 65, "111": 66, "112": 66, "113": 70, "114": 70, "115": 71, "116": 71, "117": 75, "118": 75, "119": 76, "120": 76, "126": 120}}
__M_END_METADATA
"""
