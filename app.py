#!/usr/bin/env python3

import asyncio
import json
import os
import random
import time
import threading
from datetime import datetime
from typing import Dict, Optional, Tuple, List

from flask import Flask, request, jsonify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import aiohttp
import urllib3

import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'proto'))

from MajoRLoGinrEq_pb2 import MajorLogin, GameSecurity
from MajoRLoGinrEs_pb2 import MajorLoginRes
from GetLoginDataRes_pb2 import GetLoginData

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

_L = "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3"
_D = "100067"
_H = "https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant"
_H2 = "https://loginbp.ggpolarbear.com/MajorLogin"

_K = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
_I = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])

_B = 32768

_Z = []  # online bots
_Targets = {}  # {target_uid: {"active": bool, "total": int, "thread": thread}}
_T_Lock = threading.Lock()

def _V(v: int) -> bytes:
    r = []
    while True:
        b = v & 0x7F
        v >>= 7
        if v:
            b |= 0x80
        r.append(b)
        if not v:
            break
    return bytes(r)

async def BlACk_Gay(f: dict) -> bytes:
    p = bytearray()
    for k, v in f.items():
        kn = int(k)
        if isinstance(v, dict):
            n = await BlACk_Gay(v)
            p.extend(_V((kn << 3) | 2))
            p.extend(_V(len(n)))
            p.extend(n)
        elif isinstance(v, int):
            p.extend(_V((kn << 3) | 0))
            p.extend(_V(v))
        elif isinstance(v, str):
            d = v.encode('utf-8')
            p.extend(_V((kn << 3) | 2))
            p.extend(_V(len(d)))
            p.extend(d)
        elif isinstance(v, bytes):
            p.extend(_V((kn << 3) | 2))
            p.extend(_V(len(v)))
            p.extend(v)
    return bytes(p)

async def RiZEr_GAy(h: str) -> str:
    c = AES.new(_K, AES.MODE_CBC, _I)
    p = pad(bytes.fromhex(h), AES.block_size)
    return c.encrypt(p).hex()

async def LaUdA_LasAn(h: str, k: bytes, i: bytes) -> str:
    c = AES.new(k, AES.MODE_CBC, i)
    p = pad(bytes.fromhex(h), 16)
    return c.encrypt(p).hex()

async def IsHu_TouRter(n: int) -> str:
    h = hex(n)[2:]
    return h if len(h) % 2 == 0 else '0' + h

async def GaNdU(p_h: str, p_t: str, k: bytes, i: bytes) -> bytes:
    e = await LaUdA_LasAn(p_h, k, i)
    l = len(e) // 2
    l_h = await IsHu_TouRter(l)
    if len(l_h) == 2:
        hdr = p_t + "000000"
    elif len(l_h) == 3:
        hdr = p_t + "00000"
    elif len(l_h) == 4:
        hdr = p_t + "0000"
    else:
        hdr = p_t + "000000"
    return bytes.fromhex(hdr + l_h + e)

async def BhOsDiWaLa(u: str, p: str) -> Tuple[Optional[str], Optional[str]]:
    hd = {
        "Host": "100067.connect.garena.com",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-A305F Build/RP1A.200720.012)",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    dt = {
        "uid": u, "password": p, "response_type": "token",
        "client_type": "2", "client_secret": _L, "client_id": _D
    }
    async with aiohttp.ClientSession() as s:
        try:
            async with s.post(_H, headers=hd, data=dt) as r:
                if r.status == 200:
                    j = await r.json()
                    return j.get("open_id"), j.get("access_token")
        except:
            pass
    return None, None

async def ChUtIa_PaRkAr(o: str, a: str) -> Optional[Dict]:
    req = MajorLogin()
    req.event_time = str(datetime.now())[:-7]
    req.game_name = "free fire"
    req.platform_id = 1
    req.client_version = "1.123.1"
    req.system_software = "Android OS 9 / API-28"
    req.system_hardware = "Handheld"
    req.telecom_operator = "Verizon"
    req.network_type = "WIFI"
    req.screen_width = 1920
    req.screen_height = 1080
    req.screen_dpi = "280"
    req.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    req.memory = 3003
    req.gpu_renderer = "Adreno (TM) 640"
    req.gpu_version = "OpenGL ES 3.1 v1.46"
    req.unique_device_id = f"Google|{random.randint(10000000, 99999999)}"
    req.client_ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
    req.language = "en"
    req.open_id = o
    req.open_id_type = "4"
    req.device_type = "Handheld"
    req.memory_available.version = 55
    req.memory_available.hidden_value = 81
    req.access_token = a
    req.platform_sdk_id = 1
    req.network_operator_a = "Verizon"
    req.network_type_a = "WIFI"
    req.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    req.external_storage_total = 36235
    req.external_storage_available = 31335
    req.internal_storage_total = 2519
    req.internal_storage_available = 703
    req.game_disk_storage_available = 25010
    req.game_disk_storage_total = 26628
    req.external_sdcard_avail_storage = 32992
    req.external_sdcard_total_storage = 36235
    req.login_by = 3
    req.cpu_type = 2
    req.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
    req.reg_avatar = 1
    req.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
    req.channel_type = 3
    req.cpu_architecture = "2"
    req.client_version_code = "2019118695"
    req.graphics_api = "OpenGLES2"
    req.supported_astc_bitset = 16383
    req.login_open_id_type = 4
    req.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWA0FUgsvA1snWlBaO1kFYg=="
    req.loading_time = 13564
    req.release_channel = "android"
    req.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
    req.android_engine_init_flag = 110009
    req.if_push = 1
    req.is_vpn = 1
    req.origin_platform_type = "4"
    req.primary_platform_type = "4"
    
    s = req.SerializeToString()
    e = await RiZEr_GAy(s.hex())
    
    hd = {
        "X-Unity-Version": "2018.4.11f1", "ReleaseVersion": "OB53",
        "Content-Type": "application/x-www-form-urlencoded", "X-GA": "v1 1",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    }
    async with aiohttp.ClientSession() as sess:
        try:
            async with sess.post(_H2, data=bytes.fromhex(e), headers=hd, ssl=False) as r:
                if r.status != 200:
                    return None
                d = await r.read()
                res = MajorLoginRes()
                res.ParseFromString(d)
                return {"key": res.key, "iv": res.iv, "token": res.token, "account_uid": res.account_uid,
                        "url": res.url, "region": res.region, "timestamp": res.timestamp}
        except:
            return None

async def HaRaMi_KoDa(b_url: str, e_m: str, t: str) -> Optional[Dict]:
    url = f"{b_url}/GetLoginData"
    hd = {
        "Authorization": f"Bearer {t}", "X-Unity-Version": "2018.4.11f1",
        "ReleaseVersion": "OB53", "Content-Type": "application/x-www-form-urlencoded",
        "X-GA": "v1 1", "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    }
    async with aiohttp.ClientSession() as sess:
        try:
            async with sess.post(url, data=bytes.fromhex(e_m), headers=hd, ssl=False) as r:
                if r.status != 200:
                    return None
                d = await r.read()
                res = GetLoginData()
                res.ParseFromString(d)
                return {"online_ip_port": res.Online_IP_Port, "account_name": res.AccountName}
        except:
            return None

async def KuTtA_Ki_AuLaD(a_uid: int, t: str, ts: int, k: bytes, i: bytes) -> str:
    u_h = hex(a_uid)[2:]
    u_l = len(u_h)
    e_ts = await IsHu_TouRter(ts)
    e_t = t.encode().hex()
    e_p = await LaUdA_LasAn(e_t, k, i)
    p_l = len(e_p) // 2
    p_l_h = hex(p_l)[2:]
    if u_l == 9:
        hdr = '0000000'
    elif u_l == 8:
        hdr = '00000000'
    elif u_l == 10:
        hdr = '000000'
    else:
        hdr = '0000000'
    return f"0115{hdr}{u_h}{e_ts}00000{p_l_h}{e_p}"

async def RaNdI_Ka_BacCha():
    av = [
        '902050001', '902050002', '902050003', '902039016', '902050004',
        '902047011', '902047010', '902049015', '902050006', '902049020'
    ]
    return random.choice(av)

async def BeHeNcHoD_JoIn(t_uid: int, b_v: int, k: bytes, i: bytes, r: str):
    f = {
        1: 33,
        2: {
            1: int(t_uid),
            2: r.upper(),
            3: 1,
            4: 1,
            5: bytes([1, 7, 9, 10, 11, 18, 25, 26, 32]),
            6: "[C][B][FF0000] User",
            7: 330,
            8: 1000,
            10: r.upper(),
            11: bytes([49, 97, 99, 52, 98, 56, 48, 101, 99, 102, 48, 52, 55, 56,
                       97, 52, 52, 50, 48, 51, 98, 102, 56, 102, 97, 99, 54, 49, 50, 48, 102, 53]),
            12: 1,
            13: int(t_uid),
            14: {
                1: 2203434355,
                2: 8,
                3: "\u0010\u0015\b\n\u000b\u0013\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"
            },
            16: 1,
            17: 1,
            18: 312,
            19: 46,
            23: bytes([16, 1, 24, 1]),
            24: int(await RaNdI_Ka_BacCha()),
            26: "",
            28: "",
            31: {1: 1, 2: b_v},
            32: b_v,
            34: {
                1: int(t_uid),
                2: 8,
                3: bytes([15, 6, 21, 8, 10, 11, 19, 12, 17, 4, 14, 20, 7, 2, 1, 5, 16, 3, 13, 18])
            }
        },
        10: "en",
        13: {2: 1, 3: 1}
    }
    
    p = (await BlACk_Gay(f)).hex()
    
    if r.lower() == "ind":
        p_t = '0514'
    elif r.lower() == "bd":
        p_t = "0519"
    else:
        p_t = "0515"
        
    return await GaNdU(p, p_t, k, i)

async def HaRaMi_PaCkEt(uid: int, k: bytes, i: bytes) -> bytes:
    e = []
    v = uid
    while v:
        e.append((v & 0x7F) | (0x80 if v > 0x7F else 0))
        v >>= 7
    u_e = bytes(e).hex()
    if len(u_e) == 8:
        pk = f'080112080a04{u_e}1005'
    elif len(u_e) == 10:
        pk = f"080112090a05{u_e}1005"
    else:
        pk = f'080112090a05{u_e}1005'
    return await GaNdU(pk, '0f15', k, i)

class HaramiBot:
    def __init__(self, uid: str, pwd: str):
        self.u = uid
        self.p = pwd
        self.k = None
        self.i = None
        self.t = None
        self.a = None
        self.w = None
        self.r = None
        self.on = False
        self.reg = "BD"

    async def Chutiya_Ban(self):
        try:
            o, a = await BhOsDiWaLa(self.u, self.p)
            if not o or not a:
                return False
            
            ld = await ChUtIa_PaRkAr(o, a)
            if not ld:
                return False
            
            self.k = ld["key"]
            self.i = ld["iv"]
            self.t = ld["token"]
            self.a = ld["account_uid"]
            self.reg = ld.get("region", "BD")
            ts = ld["timestamp"]
            
            req = MajorLogin()
            req.event_time = str(datetime.now())[:-7]
            req.game_name = "free fire"; req.platform_id = 1; req.client_version = "1.123.1"
            req.system_software = "Android OS 9 / API-28"; req.system_hardware = "Handheld"
            req.telecom_operator = "Verizon"; req.network_type = "WIFI"
            req.screen_width = 1920; req.screen_height = 1080; req.screen_dpi = "280"
            req.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"; req.memory = 3003
            req.gpu_renderer = "Adreno (TM) 640"; req.gpu_version = "OpenGL ES 3.1 v1.46"
            req.unique_device_id = f"Google|{random.randint(10000000, 99999999)}"
            req.client_ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
            req.language = "en"; req.open_id = o; req.open_id_type = "4"; req.device_type = "Handheld"
            req.memory_available.version = 55; req.memory_available.hidden_value = 81
            req.access_token = a; req.platform_sdk_id = 1
            req.network_operator_a = "Verizon"; req.network_type_a = "WIFI"
            req.client_using_version = "7428b253defc164018c604a1ebbfebdf"
            req.external_storage_total = 36235; req.external_storage_available = 31335
            req.internal_storage_total = 2519; req.internal_storage_available = 703
            req.game_disk_storage_available = 25010; req.game_disk_storage_total = 26628
            req.external_sdcard_avail_storage = 32992; req.external_sdcard_total_storage = 36235
            req.login_by = 3; req.cpu_type = 2
            req.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
            req.reg_avatar = 1
            req.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
            req.channel_type = 3; req.cpu_architecture = "2"; req.client_version_code = "2019118695"
            req.graphics_api = "OpenGLES2"; req.supported_astc_bitset = 16383; req.login_open_id_type = 4
            req.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWA0FUgsvA1snWlBaO1kFYg=="
            req.loading_time = 13564; req.release_channel = "android"
            req.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
            req.android_engine_init_flag = 110009; req.if_push = 1; req.is_vpn = 1
            req.origin_platform_type = "4"; req.primary_platform_type = "4"
            serialized = req.SerializeToString()
            e_m = await RiZEr_GAy(serialized.hex())
            
            s_d = await HaRaMi_KoDa(ld["url"], e_m, self.t)
            if not s_d:
                return False
            
            ip, port = s_d["online_ip_port"].split(":")
            
            a_t = await KuTtA_Ki_AuLaD(int(self.a), self.t, ts, self.k, self.i)
            
            rdr, wtr = await asyncio.open_connection(ip, int(port))
            wtr.write(bytes.fromhex(a_t))
            await wtr.drain()
            
            self.r = rdr
            self.w = wtr
            self.on = True
            
            asyncio.create_task(self._GandMaro())
            asyncio.create_task(self._BhenChodo())
            
            print(f"[+] {self.u[:8]}... ONLINE")
            return True
        except:
            return False

    async def _GandMaro(self):
        await asyncio.sleep(10)
        while self.on:
            try:
                ka = await HaRaMi_PaCkEt(self.a, self.k, self.i)
                if ka and self.w:
                    self.w.write(ka)
                    await self.w.drain()
                await asyncio.sleep(25)
            except:
                self.on = False
                break

    async def _BhenChodo(self):
        while self.on:
            try:
                d = await self.r.read(65535)
                if not d:
                    self.on = False
                    break
            except:
                self.on = False
                break

    async def Chod(self, t_uid: int):
        if not self.on:
            return False
        try:
            pkt = await BeHeNcHoD_JoIn(t_uid, _B, self.k, self.i, self.reg)
            self.w.write(pkt)
            await self.w.drain()
            return True
        except:
            return False

    async def Band(self):
        self.on = False
        if self.w:
            self.w.close()
            await self.w.wait_closed()

async def SabKoJodo():
    global _Z
    
    acc = {}
    if os.path.exists('accounts.txt'):
        with open('accounts.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line and ':' in line:
                    parts = line.split(':', 1)
                    acc[parts[0].strip()] = parts[1].strip()
    
    if not acc:
        print("No accounts found")
        return
    
    print(f"\n{'='*50}")
    print(f"Logging in {len(acc)} accounts...")
    print(f"{'='*50}\n")
    
    bots = []
    tasks = []
    for uid, pwd in acc.items():
        b = HaramiBot(uid, pwd)
        bots.append(b)
        tasks.append(b.Chutiya_Ban())
    
    results = await asyncio.gather(*tasks)
    
    for i, s in enumerate(results):
        if s:
            _Z.append(bots[i])
    
    print(f"\n{'='*50}")
    print(f"Online: {len(_Z)}/{len(acc)}")
    print(f"{'='*50}\n")

def SpamForTarget(target_uid: int):
    """Run spam loop for a specific target"""
    global _Z, _Targets
    
    async def loop():
        with _T_Lock:
            if target_uid not in _Targets:
                return
            _Targets[target_uid]["active"] = True
            _Targets[target_uid]["total"] = 0
        
        lc = 0
        while True:
            with _T_Lock:
                if target_uid not in _Targets or not _Targets[target_uid]["active"]:
                    break
            
            lc += 1
            sent_in_loop = 0
            
            for b in _Z:
                if not b.on:
                    continue
                if await b.Chod(target_uid):
                    sent_in_loop += 1
                    with _T_Lock:
                        if target_uid in _Targets:
                            _Targets[target_uid]["total"] += 1
                            total = _Targets[target_uid]["total"]
                    print(f"[📨] #{total} | {target_uid} | Bot: {b.u[:8]}")
                await asyncio.sleep(0.3)
            
            if sent_in_loop > 0:
                with _T_Lock:
                    if target_uid in _Targets:
                        total = _Targets[target_uid]["total"]
                print(f"[📊] {target_uid} | Loop {lc} | Total: {total}")
            
            await asyncio.sleep(0.5)
    
    def run():
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        new_loop.run_until_complete(loop())
    
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
    
    with _T_Lock:
        if target_uid in _Targets:
            _Targets[target_uid]["thread"] = thread

@app.route('/spam', methods=['GET'])
def spam():
    t = request.args.get('uid')
    
    if not t:
        return jsonify({'success': False, 'error': 'Missing uid. Use /spam?uid=123456789'}), 400
    
    try:
        t = int(t)
    except:
        return jsonify({'success': False, 'error': 'UID must be a number'}), 400
    
    if len(_Z) == 0:
        return jsonify({'success': False, 'error': 'No bots online'}), 400
    
    with _T_Lock:
        if t in _Targets and _Targets[t]["active"]:
            return jsonify({
                'success': False, 
                'error': f'Already spamming on {t}. Use /stop?uid={t} first',
                'current_total': _Targets[t]["total"]
            }), 400
        
        if t in _Targets:
            _Targets[t]["active"] = True
            _Targets[t]["total"] = 0
        else:
            _Targets[t] = {"active": True, "total": 0, "thread": None}
    
    SpamForTarget(t)
    
    return jsonify({
        'success': True,
        'badge': _B,
        'target': t,
        'bots': len(_Z),
        'message': f'Started spamming on {t}'
    })

@app.route('/stop', methods=['GET'])
def stop():
    t = request.args.get('uid')
    
    if not t:
        return jsonify({'success': False, 'error': 'Missing uid. Use /stop?uid=123456789'}), 400
    
    try:
        t = int(t)
    except:
        return jsonify({'success': False, 'error': 'UID must be a number'}), 400
    
    with _T_Lock:
        if t not in _Targets:
            return jsonify({'success': False, 'error': f'No spam running on {t}'}), 400
        
        if not _Targets[t]["active"]:
            return jsonify({'success': False, 'error': f'Spam already stopped on {t}'}), 400
        
        _Targets[t]["active"] = False
        total = _Targets[t]["total"]
    
    return jsonify({
        'success': True,
        'target': t,
        'total_sent': total,
        'message': f'Stopped spamming on {t}. Total {total} invites sent'
    })

@app.route('/stop-all', methods=['GET'])
def stop_all():
    with _T_Lock:
        targets = list(_Targets.keys())
        for t in targets:
            if _Targets[t]["active"]:
                _Targets[t]["active"] = False
    
    return jsonify({
        'success': True,
        'stopped_targets': len(targets),
        'message': f'Stopped all spam on {len(targets)} targets'
    })

@app.route('/status', methods=['GET'])
def status():
    t = request.args.get('uid')
    
    if t:
        try:
            t = int(t)
        except:
            return jsonify({'success': False, 'error': 'UID must be a number'}), 400
        
        with _T_Lock:
            if t not in _Targets:
                return jsonify({
                    'success': True,
                    'target': t,
                    'active': False,
                    'total_sent': 0
                })
            
            return jsonify({
                'success': True,
                'target': t,
                'active': _Targets[t]["active"],
                'total_sent': _Targets[t]["total"]
            })
    
    # No UID provided - return all targets
    with _T_Lock:
        all_targets = []
        for t_uid, data in _Targets.items():
            all_targets.append({
                'target': t_uid,
                'active': data["active"],
                'total_sent': data["total"]
            })
    
    return jsonify({
        'success': True,
        'bots_online': len([b for b in _Z if b.on]),
        'bots_total': len(_Z),
        'active_targets': len([t for t in _Targets.values() if t["active"]]),
        'targets': all_targets,
        'badge': _B
    })

@app.route('/targets', methods=['GET'])
def targets():
    with _T_Lock:
        return jsonify({
            'targets': list(_Targets.keys()),
            'details': {str(t): {"active": d["active"], "sent": d["total"]} for t, d in _Targets.items()}
        })

@app.route('/bots', methods=['GET'])
def bots():
    return jsonify({
        'total': len(_Z),
        'online': len([b for b in _Z if b.on]),
        'list': [b.u[:8] for b in _Z if b.on]
    })

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(SabKoJodo())
    loop.close()
    
    print(f"\n{'='*50}")
    print(f"API Server Starting...")
    print(f"Badge: {_B}")
    print(f"Bots: {len(_Z)}")
    print(f"{'='*50}")
    print(f"📌 Commands:")
    print(f"   GET /spam?uid=8809806596     - Start spam on UID")
    print(f"   GET /spam?uid=123456789      - Add another target")
    print(f"   GET /stop?uid=8809806596     - Stop spam on UID")
    print(f"   GET /stop-all                - Stop all spam")
    print(f"   GET /status                  - Show all targets")
    print(f"   GET /status?uid=8809806596   - Show specific target")
    print(f"   GET /targets                 - List all targets")
    print(f"   GET /bots                    - List all bots")
    print(f"{'='*50}\n")
    
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)