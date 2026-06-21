# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 27

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-UNKNOWN-VLESS-WS-65MS` (url=222ms, nekobox=249ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS` (url=215ms, nekobox=250ms, status=yes)
3. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-62MS` (url=220ms, nekobox=261ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-94MS` (url=220ms, nekobox=250ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS` (url=227ms, nekobox=250ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-76MS` (url=226ms, nekobox=245ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-97MS` (url=223ms, nekobox=245ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-163MS` (url=207ms, nekobox=232ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-102MS` (url=212ms, nekobox=250ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-230MS` (url=508ms, nekobox=535ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-246MS` (url=564ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-234MS` (url=492ms, status=HTTP 204)
13. `AKUN-013-SPEEDTEST-VLESS-WS-263MS` (url=582ms, status=HTTP 204)
14. `AKUN-014-SPEEDTEST-VLESS-WS-243MS` (url=533ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-279MS` (url=561ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-72MS` (url=211ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-265MS` (url=582ms, status=HTTP 204)
18. `AKUN-018-SPEEDTEST-VLESS-WS-91MS` (url=211ms, status=HTTP 204)
19. `AKUN-022-KAWAII520-VLESS-WS-401MS` (url=661ms, status=HTTP 204)
20. `AKUN-029-UNKNOWN-VLESS-WS-557MS` (url=923ms, status=HTTP 204)
21. `AKUN-033-UNKNOWN-VLESS-WS-507MS` (url=865ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
