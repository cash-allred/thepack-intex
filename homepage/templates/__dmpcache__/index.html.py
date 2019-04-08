# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1549650626.917415
_enable_loop = True
_template_filename = 'C:/Users/the_m/Desktop/first_tutorial/mysite/homepage/templates/index.html'
_template_uri = 'index.html'
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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
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
        __M_writer('Homepage')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h3>Welcome, Jedi</h3>\r\n      <h4>I bet you can\'t guess which Jedi wrote the text below!</h4>\r\n      <iframe width="560" height="315" src="https://www.youtube.com/embed/cED1NnOpEJ8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\r\n      <p>I have a 10 year old son. He has words. He is so good with these words it\'s unbelievable. He’s not a word hero. He’s a word hero because he was captured. I like text that wasn’t captured. I think the only difference between me and the other placeholder text is that I’m more honest and my words are more beautiful.</p>\r\n      <p>Lorem Ipsum better hope that there are no "tapes" of our conversations before he starts leaking to the press! I think the only card she has is the Lorem card.</p>\r\n      <p>Lorem Ipsum better hope that there are no "tapes" of our conversations before he starts leaking to the press!</p>\r\n      <p>The other thing with Lorem Ipsum is that you have to take out its family.<p>\r\n      <p>Lorem Ipsum\'s father was with Lee Harvey Oswald prior to Oswald\'s being, you know, shot. It’s about making placeholder text great again. That’s what people want, they want placeholder text to be great again. Trump Ipsum is calling for a total and complete shutdown of Muslim text entering your website. He’s not a word hero. He’s a word hero because he was captured. I like text that wasn’t captured.</p>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/the_m/Desktop/first_tutorial/mysite/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "43": 3, "53": 3, "59": 3, "65": 5, "71": 5, "77": 71}}
__M_END_METADATA
"""
