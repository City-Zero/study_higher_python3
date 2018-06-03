# coding=utf-8
import os
ROOT_DIR = os.getcwd()
from mako.template import Template
from mako.lookup import TemplateLookup
# hello ${name}
t = Template('hello ${name}')

# 从文件中加载模板,可以指定module_directory生成.py文件缓存，提高加载速度。
# filename最好用相对路径，否则缓存文件会包含在很长的路径下。
# tf = Template(filename='tt/index.html',module_directory=ROOT_DIR)
print(t.render(name='lyt'))

# 使用templateLookup，可以方便的设置模板目录，当模板中include别的模板时可以只写模板名
# collection_size设置加载到内存中的模板上限
# filesystem_checks为True会在每次加载模板缓存判断模板文件是否有改动，会重新编译。
lookup = TemplateLookup(directories=['tt'],module_directory=ROOT_DIR+'/tt',
                        collection_size=500,filesystem_checks=True)
tf = lookup.get_template('index.html')
print(tf.render(name='init',lis = list(range(10))))
