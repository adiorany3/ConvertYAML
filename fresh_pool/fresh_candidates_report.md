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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-109MS` (url=290ms, nekobox=298ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-115MS` (url=303ms, nekobox=355ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-106MS` (url=286ms, nekobox=313ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-117MS` (url=261ms, nekobox=328ms, status=yes)
5. `AKUN-005-COMPREND-NET-VLESS-WS-135MS` (url=277ms, nekobox=272ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-138MS` (url=299ms, nekobox=334ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-119MS` (url=314ms, nekobox=297ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-134MS` (url=363ms, nekobox=306ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-119MS` (url=253ms, nekobox=291ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-136MS` (url=281ms, nekobox=294ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-118MS` (url=255ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-144MS` (url=304ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-149MS` (url=277ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-138MS` (url=287ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-120MS` (url=323ms, status=HTTP 204)
16. `AKUN-016-SAINT-PETERSBURG-VLESS-WS-156MS` (url=280ms, status=HTTP 204)
17. `AKUN-017-COMPREND-NET-VLESS-WS-146MS` (url=263ms, status=HTTP 204)
18. `AKUN-018-466688-VLESS-WS-165MS` (url=272ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-297MS` (url=732ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-322MS` (url=660ms, status=HTTP 204)
21. `AKUN-021-CONFLU-VLESS-WS-330MS` (url=678ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-308MS` (url=4062ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-331MS` (url=722ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-385MS` (url=783ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-339MS` (url=806ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
