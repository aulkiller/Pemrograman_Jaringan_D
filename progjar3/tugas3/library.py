import logging
import requests
import os
import time
import datetime


def get_targets():
    targets = dict()
    targets[
        'rec1'] = 'ip1'
    targets['rec2'] = 'ip2'
    targets['rec3'] = 'ip3'
    targets['rec4'] = 'ip4'
    return targets


def send_file(ip):
    waktu_awal = datetime.datetime.now()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    namafile = "bart.png"
    ukuran = os.stat(namafile).st_size

    fp = open('bart.png', 'rb')
    k = fp.read()
    terkirim = 0
    for x in k:
        k_bytes = bytes([x])
        sock.sendto(k_bytes, (ip, 5005))
        terkirim = terkirim + 1
        print(k_bytes, f"terkirim {terkirim} of {ukuran} ")
    waktu_process = datetime.datetime.now() - waktu_awal
    waktu_akhir = datetime.datetime.now()
    logging.warning(f"writing {namafile}.{ekstensi} dalam waktu {waktu_process} {waktu_awal} s/d {waktu_akhir}")