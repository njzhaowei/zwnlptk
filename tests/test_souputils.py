# -*- coding: utf-8 -*-
import pytest
from bs4 import BeautifulSoup
from zwnlptk.souputils import *

def test_calc_word():
    htmlstr = '''
    <html>
    <head>HAHA</head>
    <body>
        <table>
            <thead></thead>
            <tbody>
                <tr><td>这是标题，不是主体</td></tr>
                <tr></tr>
            </tbody>
        </table>
        <table>
            <thead>这是header，也不是主体</thead>
            <tbody>
                <tr><td>这是主体了</td></tr>
                <tr><td>厅机关各处室，中心、所：</td></tr>
                <tr><td>根据军队转业干部接收安置有关政策，经厅党组研究决定，确定姜学明同志为四级调研员。</td></tr>
                <tr><td>中共江苏省商务厅党组</td></tr>
                <tr><td>2020年2月13日</td></tr>
                <tr><td>这是主体了</td></tr>
                <tr></tr>
            </tbody>
        </table>
        <div>这仍然不是主体</div>
    </body>
    </html>
    '''
    soup = BeautifulSoup(htmlstr, features='lxml')
    r = calc_word(soup)
    arr = sorted(r, key=lambda o: o['gscore'], reverse=True)
    assert 1
