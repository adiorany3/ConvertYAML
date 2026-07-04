# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=214ms, nekobox=244ms, status=yes)
2. `AKUN-002-UK-GB-DCL-01-20191003-VLESS-WS-65MS` (url=208ms, nekobox=236ms, status=yes)
3. `AKUN-003-WPENG-VLESS-WS-63MS` (url=198ms, nekobox=231ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-68MS` (url=225ms, nekobox=254ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-72MS` (url=219ms, nekobox=243ms, status=yes)
6. `AKUN-006-DIGITALOCEAN-VLESS-WS-89MS` (url=237ms, nekobox=260ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-85MS` (url=214ms, nekobox=249ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-94MS` (url=227ms, nekobox=235ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-75MS` (url=208ms, nekobox=232ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-83MS` (url=214ms, nekobox=237ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-83MS` (url=206ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-98MS` (url=227ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-105MS` (url=202ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-80MS` (url=205ms, status=HTTP 204)
15. `AKUN-015-ZOOM-VLESS-WS-65MS` (url=223ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-93MS` (url=205ms, status=HTTP 204)
17. `AKUN-017-466688-VLESS-WS-111MS` (url=215ms, status=HTTP 204)
18. `AKUN-018-PAGES-VLESS-WS-120MS` (url=215ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-78MS` (url=216ms, status=HTTP 204)
20. `AKUN-020-1PASSWORD-VLESS-WS-87MS` (url=221ms, status=HTTP 204)
21. `AKUN-021-MYBB-VLESS-WS-74MS` (url=215ms, status=HTTP 204)
22. `AKUN-022-SPEEDTEST-VLESS-WS-226MS` (url=491ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-233MS` (url=507ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-229MS` (url=493ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-239MS` (url=534ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
