# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528032028.80846
_enable_loop = True
_template_filename = 'tt/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        loop = __M_loop = runtime.LoopStack()
        name = context.get('name', UNDEFINED)
        lis = context.get('lis', UNDEFINED)
        __M_writer = context.writer()
        runtime._include_file(context, 'base', _template_uri)
        __M_writer('\nHello ')
        __M_writer(str(name.upper()))
        __M_writer('!\n')
        loop = __M_loop._enter(lis)
        try:
            for i in loop:
                if i != 5:
                    __M_writer('        <li>')
                    __M_writer(str(loop.index))
                    __M_writer(':')
                    __M_writer(str(i))
                    __M_writer('</li>\n')
        finally:
            loop = __M_loop._exit()
        __M_writer('\n')
        __M_writer('\n')


        x = 'lyt'
        x.upper()
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['x'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n')
        __M_writer(str(x))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "tt/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"16": 0, "24": 2, "25": 2, "26": 3, "27": 3, "28": 4, "31": 5, "32": 6, "33": 6, "34": 6, "35": 6, "36": 6, "39": 9, "40": 13, "41": 14, "49": 18, "50": 19, "56": 50}}
__M_END_METADATA
"""
