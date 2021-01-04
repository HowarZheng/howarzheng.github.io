# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Kepler",
    "type": "git",
    "url": "https://github.com/AlanDecode/Maverick-Theme-Kepler.git",
    "branch": "latest"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "HowarZheng/howarzheng.github.io@master"
}

# 站点设置
site_name = "HowarZheng Wiki"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020-01-03T16:51+08:00"
author = "HowarZheng"
email = "howar.zheng@gmail.com"
author_homepage = "https://www.howarzheng.com"
description = "技术改变世界，理论改变世界观。"
key_words = ['Biology',  'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Github",
        "url": "https://github.com/HowarZheng",
        "brief": "🏄‍ Debug the Universe!"
    },
    {
        "name": "博客",
        "url": "https://www.howarzheng.com",
        "brief": "howarzheng blog"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/HowarZheng",
        "icon": "gi gi-github"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
