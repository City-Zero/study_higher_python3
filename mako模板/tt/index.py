# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1527141061.8349707
_enable_loop = True
_template_filename = 'tt/index.html'
_template_uri = 'tt/index.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        name = context.get('name', UNDEFINED)
        __M_writer = context.writer()
        runtime._include_file(context, 'base', _template_uri)
        __M_writer('\nHello ')
        __M_writer(str(name))
        __M_writer('!')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "tt/index.html", "uri": "tt/index.html", "source_encoding": "ascii", "line_map": {"16": 0, "22": 1, "23": 1, "24": 2, "25": 2, "31": 25}}
__M_END_METADATA
"""
