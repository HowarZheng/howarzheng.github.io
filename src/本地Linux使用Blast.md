---
layout: post
title: 本地Linux使用Blast
slug: 本地Linux使用Blast
date: 2020-12-31 16:50
status: publish
author: HowarZheng
categories: 
  - 生物信息学
tags:
  - 生物信息学
  - Blast
  - Linux
excerpt: 本地Linux使用Blast。
---
# 【Linux】本地Linux使用Blast

## 第一步：下载Blast

```bash
wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.8.1+-x64-linux.tar.gz
```

## 第二步：解压缩

```bash
tar -zxvf ncbi-blast-2.8.1+-x64-linux.tar.gz
```

## 第三步：移动目录，改名

```bash
mv ncbi-blast-2.8.1+ /home/xizheng/local/app/ # 移动
cd /home/xizheng/local/app/                    # 进入本地程序安装路径
mv cbi-blast-2.8.1+ blast        # 修改目录名
```

## 设置环境变量

**将BLAST+可执行程序所在目录（bin）的绝对路径加入到环境变量$PATH中，方便通过程序名直接调用。**

```bash
echo "export PATH=/home/xizheng/local/app/blast/bin:\$PATH" >> ~/.bashrc
```

**让配置生效**

```bash
source ~/.bashrc
```

到此，本地blast安装完毕，可以利用blast的子程序了。输入 blastn -version试试:

```bash
blastn: 2.8.1+
 Package: blast 2.8.1, build Nov 26 2018 11:55:45
```

