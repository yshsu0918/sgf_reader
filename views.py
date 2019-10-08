from django.shortcuts import render
from django.http import HttpResponse
from django import template
from django.shortcuts import render_to_response

# Create your views here.
import os

def math(request, a=3,b=2):
    a = int(a)
    b = int(b)
    s = a + b
    d = a - b
    p = a * b
    q = a / b
    return render_to_response('a.html',locals())

def QQ(requests):
    #path = '/home/samox0918/VM_SYNC/chessboard_partition/web/sgf_reader/read/sgfs'

    sgfs = []
    #path = '/home/samox0918/VM_SYNC/chessboard_partition/切棋譜/gen_askelf_script/結果統計/result_30000_v2_output/wrong'
    #path = '/media/sf_VM_sync/chessboard_partition/切棋譜/chao232_category/todeath_ans_byprogram'
    #path = '/home/samox0918/VM_SYNC/chessboard_partition/切棋譜/死活中級RZST/死活中級RZST_human/ans'
    #path = '/home/samox0918/VM_SYNC/chessboard_partition/切棋譜/rotate_flip/chao253'
    #path = '/home/samox0918/VM_SYNC/chessboard_partition/切棋譜/rotate_flip/chao253_spin'
    path = '/home/samox0918/VM_SYNC/chessboard_partition/切棋譜/rotate_flip/chao70/chao70_result_80000/wrong'
    #path = '/home/samox0918/VM_SYNC/chessboard_partition/切棋譜/chao232_category/tolive_ans_byhuman'
    dirs = os.listdir( path )
    dirs.sort()
    for fname in dirs: 
        if 'sgf' not in fname.lower():
            continue
        with open( os.path.join(path,fname) ,encoding='UTF-8') as f:
            print(os.path.join(path,fname))
            sgf = f.read()
            sgfs.append({'content': sgf,'name': fname})

    return render_to_response('demo3.html',locals())

def QQQ(requests):
    #path = '/home/samox0918/VM_SYNC/chessboard_partition/web/sgf_reader/read/sgfs'

    sgfs = []
    #path = '/home/samox0918/VM_SYNC/chessboard_partition/切棋譜/gen_askelf_script/結果統計/result_30000_v2_output/wrong'
    #path = '/media/sf_VM_sync/chessboard_partition/切棋譜/chao232_category/todeath_ans_byprogram'
    #path = '/home/samox0918/VM_SYNC/chessboard_partition/切棋譜/死活中級RZST/死活中級RZST_human/ans'
    #path = '/home/samox0918/VM_SYNC/chessboard_partition/切棋譜/rotate_flip/chao253'
    #path = '/home/samox0918/VM_SYNC/chessboard_partition/切棋譜/rotate_flip/chao253_spin'
    path = '/home/samox0918/VM_SYNC/chessboard_partition/切棋譜/rotate_flip/chao70/chao70_spin'
    #path = '/home/samox0918/VM_SYNC/chessboard_partition/切棋譜/chao232_category/tolive_ans_byhuman'
    dirs = os.listdir( path )
    dirs.sort()
    for fname in dirs: 
        if 'sgf' not in fname.lower():
            continue
        with open( os.path.join(path,fname) ,encoding='UTF-8') as f:
            print(os.path.join(path,fname))
            sgf = f.read()
            sgfs.append({'content': sgf,'name': fname})

    return render_to_response('demo3.html',locals())
