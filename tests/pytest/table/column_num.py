# -*- coding: utf-8 -*-

import sys
from util.log import *
from util.cases import *
from util.sql import *


class TDTestCase:
    def init(self, conn):
        tdLog.debug("start to execute %s" % __file__)
        tdSql.init(conn.cursor())

    def run(self):
        tdSql.prepare()

        # TSIM: system sh/stop_dnodes.sh
        # TSIM:
        # TSIM: system sh/ip.sh -i 1 -s up
        # TSIM: system sh/deploy.sh -n dnode1 -m 192.168.0.1 -i 192.168.0.1
        # TSIM: system sh/cfg.sh -n dnode1 -c walLevel -v 0
        # TSIM: system sh/exec.sh -n dnode1 -s start
        # TSIM:
        # TSIM: sleep 3000
        # TSIM: sql connect
        # TSIM:
        # TSIM: $i = 0
        # TSIM: $dbPrefix = lm_cn_db
        # TSIM: $tbPrefix = lm_cn_tb
        # TSIM: $db = $dbPrefix . $i
        # TSIM: $tb = $tbPrefix . $i
        # TSIM:
        # TSIM: print =============== step1
        tdLog.info('=============== step1')
        # TSIM: sql create database $db
        # TSIM: sql use $db
        # TSIM:
        # TSIM: sql create table $tb() -x step1
        tdLog.info('create table tb() -x step1')
        tdSql.error('create table tb()')
        # TSIM: return -1
        # TSIM: step1:
        # TSIM:
        # TSIM: sql show tables
        tdLog.info('show tables')
        tdSql.query('show tables')
        # TSIM: if $rows != 0 then
        tdLog.info('tdSql.checkRow(0)')
        tdSql.checkRows(0)
        # TSIM: return -1
        # TSIM: endi
        # TSIM:
        # TSIM: print =============== step2
        tdLog.info('=============== step2')
        # TSIM: sql create table $tb (ts timestamp)  -x step2
        tdLog.info('create table tb (ts timestamp)  -x step2')
        tdSql.error('create table tb (ts timestamp) ')
        # TSIM: return -1
        # TSIM: step2:
        # TSIM:
        # TSIM: sql show tables
        tdLog.info('show tables')
        tdSql.query('show tables')
        # TSIM: if $rows != 0 then
        tdLog.info('tdSql.checkRow(0)')
        tdSql.checkRows(0)
        # TSIM: return -1
        # TSIM: endi
        # TSIM:
        # TSIM: print =============== step3
        tdLog.info('=============== step3')
        # TSIM: sql create table $tb (ts int)  -x step3
        tdLog.info('create table tb (ts int)  -x step3')
        tdSql.error('create table tb (ts int) ')
        # TSIM: return -1
        # TSIM: step3:
        # TSIM:
        # TSIM: sql show tables
        tdLog.info('show tables')
        tdSql.query('show tables')
        # TSIM: if $rows != 0 then
        tdLog.info('tdSql.checkRow(0)')
        tdSql.checkRows(0)
        # TSIM: return -1
        # TSIM: endi
        # TSIM:
        # TSIM: print =============== step4
        tdLog.info('=============== step4')
        # TSIM: sql create table $tb (ts timestamp, a1 int, a2 int, a3 int, a4
        # int, a5 int, a6 int, a7 int, a8 int, a9 int, a10 int, a11 int, a12
        # int, a13 int, a14 int, a15 int, a16 int, a17 int, a18 int, a19 int,
        # a20 int, a21 int, a22 int, a23 int, a24 int, a25 int, a26 int, a27
        # int, a28 int,a29 int,a30 int,a31 int,a32 int, b1 int, b2 int, b3 int,
        # b4 int, b5 int, b6 int, b7 int, b8 int, b9 int, b10 int, b11 int, b12
        # int, b13 int, b14 int, b15 int, b16 int, b17 int, b18 int, b19 int,
        # b20 int, b21 int, b22 int, b23 int, b24 int, b25 int, b26 int, b27
        # int, b28 int,b29 int,b30 int,b31 int,b32 int)
        tdLog.info('create table tb (ts timestamp, a1 int, a2 int, a3 int, a4 int, a5 int, a6 int, a7 int, a8 int, a9 int, a10 int, a11 int, a12 int, a13 int, a14 int, a15 int, a16 int, a17 int, a18 int, a19 int, a20 int, a21 int, a22 int, a23 int, a24 int, a25 int, a26 int, a27 int, a28 int,a29 int,a30 int,a31 int,a32 int, b1 int, b2 int, b3 int, b4 int, b5 int, b6 int, b7 int, b8 int, b9 int, b10 int, b11 int, b12 int, b13 int, b14 int, b15 int, b16 int, b17 int, b18 int, b19 int, b20 int, b21 int, b22 int, b23 int, b24 int, b25 int, b26 int, b27 int, b28 int,b29 int,b30 int,b31 int,b32 int)')
        tdSql.execute('create table tb (ts timestamp, a1 int, a2 int, a3 int, a4 int, a5 int, a6 int, a7 int, a8 int, a9 int, a10 int, a11 int, a12 int, a13 int, a14 int, a15 int, a16 int, a17 int, a18 int, a19 int, a20 int, a21 int, a22 int, a23 int, a24 int, a25 int, a26 int, a27 int, a28 int,a29 int,a30 int,a31 int,a32 int, b1 int, b2 int, b3 int, b4 int, b5 int, b6 int, b7 int, b8 int, b9 int, b10 int, b11 int, b12 int, b13 int, b14 int, b15 int, b16 int, b17 int, b18 int, b19 int, b20 int, b21 int, b22 int, b23 int, b24 int, b25 int, b26 int, b27 int, b28 int,b29 int,b30 int,b31 int,b32 int)')
        # TSIM:
        # TSIM: sql show tables
        tdLog.info('show tables')
        tdSql.query('show tables')
        # TSIM: if $rows != 1 then
        tdLog.info('tdSql.checkRow(1)')
        tdSql.checkRows(1)
        # TSIM: return -1
        # TSIM: endi
        # TSIM:
        # TSIM: print =============== step5
        tdLog.info('=============== step5')
        # TSIM: $i = 1
        # TSIM: $tb = $tbPrefix . $i
        # TSIM:
        # TSIM: sql create table $tb (ts timestamp, a1 int, a2 int, a3 int, a4
        # int, a5 int, a6 int, a7 int, a8 int, a9 int, a10 int, a11 int, a12
        # int, a13 int, a14 int, a15 int, a16 int, a17 int, a18 int, a19 int,
        # a20 int, a21 int, a22 int, a23 int, a24 int, a25 int, a26 int, a27
        # int, a28 int,a29 int,a30 int,a31 int,a32 int, b1 int, b2 int, b3 int,
        # b4 int, b5 int)
        tdLog.info('create table tb1 (ts timestamp, a1 int, a2 int, a3 int, a4 int, a5 int, a6 int, a7 int, a8 int, a9 int, a10 int, a11 int, a12 int, a13 int, a14 int, a15 int, a16 int, a17 int, a18 int, a19 int, a20 int, a21 int, a22 int, a23 int, a24 int, a25 int, a26 int, a27 int, a28 int,a29 int,a30 int,a31 int,a32 int, b1 int, b2 int, b3 int, b4 int, b5 int)')
        tdSql.execute('create table tb1 (ts timestamp, a1 int, a2 int, a3 int, a4 int, a5 int, a6 int, a7 int, a8 int, a9 int, a10 int, a11 int, a12 int, a13 int, a14 int, a15 int, a16 int, a17 int, a18 int, a19 int, a20 int, a21 int, a22 int, a23 int, a24 int, a25 int, a26 int, a27 int, a28 int,a29 int,a30 int,a31 int,a32 int, b1 int, b2 int, b3 int, b4 int, b5 int)')
        # TSIM:
        # TSIM: sql show tables
        tdLog.info('show tables')
        tdSql.query('show tables')
        # TSIM: if $rows != 2 then
        tdLog.info('tdSql.checkRow(2)')
        tdSql.checkRows(2)
        # TSIM: return -1
        # TSIM: endi
        # TSIM:
        # TSIM: sql insert into $tb values (now, 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8
        # , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22
        # , 23 , 24 , 25 ,26 , 27 ,28 ,29,30,31, 32, 33, 34, 35, 36, 37)
        tdLog.info("insert into tb1 values (now, 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 ,26 , 27 ,28 ,29,30,31, 32, 33, 34, 35, 36, 37)")
        tdSql.execute("insert into tb1 values (now, 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 ,26 , 27 ,28 ,29,30,31, 32, 33, 34, 35, 36, 37)")
        # TSIM: sql select * from $tb
        tdLog.info('select * from tb1')
        tdSql.query('select * from tb1')
        # TSIM: if $rows != 1 then
        tdLog.info('tdSql.checkRow(1)')
        tdSql.checkRows(1)
        # TSIM: return -1
        # TSIM: endi
        # TSIM:
        # TSIM: sql drop table $tb
        tdLog.info('drop table tb1')
        tdSql.execute('drop table tb1')
        # TSIM: sql show tables
        tdLog.info('show tables')
        tdSql.query('show tables')
        # TSIM: if $rows != 1 then
        tdLog.info('tdSql.checkRow(1)')
        tdSql.checkRows(1)
        # TSIM: return -1
        # TSIM: endi
        # TSIM:
        # TSIM: sql drop database $db
        tdLog.info('drop database db')
        tdSql.execute('drop database db')
        # TSIM: sql show databases
        tdLog.info('show databases')
        tdSql.query('show databases')
        # TSIM: if $rows != 0 then
        tdLog.info('tdSql.checkRow(0)')
        tdSql.checkRows(0)
        # TSIM: return -1
        # TSIM: endi
# convert end

    def stop(self):
        tdSql.close()
        tdLog.success("%s successfully executed" % __file__)


tdCases.addWindows(__file__, TDTestCase())
tdCases.addLinux(__file__, TDTestCase())
