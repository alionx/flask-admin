# encoding=utf-8
# 2022/1/12 22:19

import argparse
import os


class Admin(object):
    '''
    管理项目创建
    '''

    def __init__(self, demo_name):
        '''
        实例化项目
        '''
        self.demo_name = demo_name

    def demo_file(self):
        '''
        根据项目路径创建项目文件夹
        :param input_name:输入的项目名称
        :return:
        '''
        # 拼接项目路径
        self.path = '.\\' + self.demo_name
        cmd_0 = 'md %s' % (self.demo_name)
        os.system(cmd_0)
        return

    def demo_type(self, demo_type):
        '''

        :param demo_type:
        :param demopath:
        :return:
        '''
        if demo_type == 'simple':
            with open('%s/manage.py' % (self.path), 'w', encoding='utf-8') as manage:
                manage.write('')
            with open('%s/README.md' % (self.path), 'w', encoding='utf-8') as readme:
                readme.write('本项目旨在让小白更快的熟悉flask，其中各类设置并非硬性要求和规定，都可以根据自己的需求进行设置。\n'
                             'demo(项目名称)\n'
                             '  manage.py(启动程序)\n'
                             '  config.py(环境配置，按照一般项目编写一些简单的配置)\n'
                             '  README.md(固定，编写生成器的介绍和各个文件的功用，也可以用于作者编写项目介绍)\n')
            with open('%s/config.py' % (self.path), 'w', encoding='utf-8') as config:
                config.write('')

        if demo_type == 'general':
            with open('%s/manage.py' % (self.path), 'w', encoding='utf-8') as manage:
                manage.write('')
            with open('%s/config.py' % (self.path), 'w', encoding='utf-8') as config:
                config.write('')
            with open('%s/requirements.txt' % (self.path), 'w', encoding='utf-8') as requirements:
                requirements.write('')
            with open('%s/demo.sql' % (self.path), 'w', encoding='utf-8') as sql:
                sql.write('')
            with open('%s/README.md' % (self.path), 'w', encoding='utf-8') as readme:
                readme.write('demo(项目名称)\n'
                             '│ config.py(环境配置，按照一般项目编写一些简单的配置)\n'
                             '│ manage.py(启动程序)\n'
                             '│ requirements.txt(所依赖的所有python包)\n'
                             '│ demo.sql(空文件，用于占位，方便后续替换)\n'
                             '│ README.md(固定，编写生成器的介绍和各个文件的功用，也可以用于作者编写项目介绍)\n'
                             '│\n'
                             '└─app\n'
                             '  │ __init__.py(包初始化文件，让项目识别此目录是一个包)\n'
                             '  │ forms.py(存放所有表单，数量过多的较大项目也可以单独写一个包)\n'
                             '  │ models.py(存放所有数据模型，数量过多的较大项目也可以单独写一个包)\n'
                             '  │ views.py(存放所有视图函数，数量过多的较大项目也可以单独写一个包)\n'
                             '  │\n'
                             '  ├─admin(蓝图目录)\n'
                             '  │\n'
                             '  ├─static(存放静态内容的地方)\n'
                             '  │  ├─css(样式表存放目录)\n'
                             '  │  ├─img(存放图片目录)\n'
                             '  │  └─js(js脚本存放目录)\n'
                             '  │\n'
                             '  └─templates(存放模板的地方)\n')

            # 拼接app文件目录
            app_path = self.path + '\\' + 'app'
            cmd_1 = 'md %s' % (app_path)
            os.system(cmd_1)
            with open('%s/__init__.py' % (app_path), 'w', encoding='utf-8') as init:
                init.write('')
            with open('%s/forms.py' % (app_path), 'w', encoding='utf-8') as forms:
                forms.write('')
            with open('%s/models.py' % (app_path), 'w', encoding='utf-8') as models:
                models.write('')
            with open('%s/views.py' % (app_path), 'w', encoding='utf-8') as views:
                views.write('')

            # 拼接admin文件目录
            admin_path = app_path + '\\' + 'admin'
            cmd_2 = 'md %s' % (admin_path)
            os.system(cmd_2)

            # 拼接static文件目录
            static_path = app_path + '\\' + 'static'
            cmd_3 = 'md %s' % (static_path)
            os.system(cmd_3)
            # 创建static文件子文件
            cmd_4 = 'md %s' % (static_path + '\\' + 'css')
            os.system(cmd_4)
            cmd_5 = 'md %s' % (static_path + '\\' + 'img')
            os.system(cmd_5)
            cmd_6 = 'md %s' % (static_path + '\\' + 'js')
            os.system(cmd_6)

            # 拼接templates文件目录
            templates_path = app_path + '\\' + 'templates'
            cmd_7 = 'md %s' % (templates_path)
            os.system(cmd_7)

        if demo_type == 'complex':
            with open('%s/manage.py' % (self.path), 'w', encoding='utf-8') as manage:
                manage.write('')
            with open('%s/config.py' % (self.path), 'w', encoding='utf-8') as config:
                config.write('')
            with open('%s/requirements.txt' % (self.path), 'w', encoding='utf-8') as requirements:
                requirements.write('')
            with open('%s/demo.sql' % (self.path), 'w', encoding='utf-8') as sql:
                sql.write('')

            # 拼接app文件目录
            app_path = self.path + '\\' + 'app'
            cmd_1 = 'md %s' % (app_path)
            os.system(cmd_1)
            with open('%s/__init__.py' % (app_path), 'w', encoding='utf-8') as init:
                init.write('')
            with open('%s/forms.py' % (app_path), 'w', encoding='utf-8') as forms:
                forms.write('')
            with open('%s/models.py' % (app_path), 'w', encoding='utf-8') as models:
                models.write('')
            with open('%s/views.py' % (app_path), 'w', encoding='utf-8') as views:
                views.write('')

            # 拼接admin文件目录
            admin_path = app_path + '\\' + 'admin'
            cmd_2 = 'md %s' % (admin_path)
            os.system(cmd_2)

            # 拼接static文件目录
            static_path = app_path + '\\' + 'static'
            cmd_3 = 'md %s' % (static_path)
            os.system(cmd_3)
            # 创建static文件子文件
            cmd_4 = 'md %s' % (static_path + '\\' + 'css')
            os.system(cmd_4)
            cmd_5 = 'md %s' % (static_path + '\\' + 'img')
            os.system(cmd_5)
            cmd_6 = 'md %s' % (static_path + '\\' + 'js')
            os.system(cmd_6)

            # 拼接templates文件目录
            templates_path = app_path + '\\' + 'templates'
            cmd_7 = 'md %s' % (templates_path)
            os.system(cmd_7)
            with open('%s/README.md' % (self.path), 'w', encoding='utf-8') as readme:
                readme.write('demo(项目名称)\n'
                             '│ config.py(环境配置，按照一般项目编写一些简单的配置)\n'
                             '│ manage.py(启动程序)\n'
                             '│ requirements.txt(所依赖的所有python包)\n'
                             '│ demo.sql(空文件，用于占位，方便后续替换)\n'
                             '│ README.md(固定，编写生成器的介绍和各个文件的功用，也可以用于作者编写项目介绍)\n'
                             '│\n'
                             '├─app\n'
                             '│  │ __init__.py(包初始化文件，让项目识别此目录是一个包)\n'
                             '│  │ forms.py(存放所有表单，数量过多的较大项目也可以单独写一个包)\n'
                             '│  │ models.py(存放所有数据模型，数量过多的较大项目也可以单独写一个包)\n'
                             '│  │ views.py(存放所有视图函数，数量过多的较大项目也可以单独写一个包)\n'
                             '│  │\n'
                             '│  ├─admin(蓝图目录)\n'
                             '│  │\n'
                             '│  ├─static(存放静态内容的地方)\n'
                             '│  │  ├─css(样式表存放目录)\n'
                             '│  │  ├─img(存放图片目录)\n'
                             '│  │  └─js(js脚本存放目录)\n'
                             '│  │\n'
                             '│  └─templates(存放模板的地方)\n'
                             '│\n'
                             '├─tests(测试代码包)\n'
                             '│    __init__.py(包初始化文件，让项目识别此目录是一个包)\n'
                             '│    test_1.py(测试代码1)\n'
                             '│    test_2.py(测试代码2)\n'
                             '│\n'
                             '└─migrations(项目迁移配置)\n'
                             '  new_sql.py(配置项目sql库和表单)\n'
                             '  new_env.py(需要线读取python版本，查看是否可以配置项目，否则提示警告)\n')
            # 拼接tests文件目录
            tests_path = self.path + '\\' + 'tests'
            cmd_8 = 'md %s' % (tests_path)
            os.system(cmd_8)
            with open('%s/__init__.py' % (tests_path), 'w', encoding='utf-8') as init:
                init.write('')
            with open('%s/test_1.py' % (tests_path), 'w', encoding='utf-8') as test1:
                test1.write('')
            with open('%s/test_2.py' % (tests_path), 'w', encoding='utf-8') as test2:
                test2.write('')

            # 拼接migrations文件目录
            migrations_path = self.path + '\\' + 'migrations'
            cmd_9 = 'md %s' % (migrations_path)
            os.system(cmd_9)
            with open('%s/new_sql.py' % (migrations_path), 'w', encoding='utf-8') as new_sql:
                new_sql.write('')
            with open('%s/new_env.py' % (migrations_path), 'w', encoding='utf-8') as new_env:
                new_env.write('')

        return


def main():
    parser = argparse.ArgumentParser(usage='You can use this command to create a flask project.')
    parser.add_argument("demo", help="Your project filename.")
    parser.add_argument('--type', default='simple', choices=['simple', 'general', 'complex'],
                        help='Select the type for your demo, such as simple, general and complex,Generate different types of project file structures.')
    args = parser.parse_args()
    admin = Admin(args.demo)
    admin.demo_file()
    admin.demo_type(args.type)


if __name__ == '__main__':
    main()
