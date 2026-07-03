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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-101MS` (url=260ms, nekobox=295ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-91MS` (url=257ms, nekobox=314ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-103MS` (url=315ms, nekobox=281ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-105MS` (url=270ms, nekobox=292ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-97MS` (url=252ms, nekobox=298ms, status=yes)
6. `AKUN-006-WEBEX-VLESS-WS-129MS` (url=314ms, nekobox=314ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-128MS` (url=289ms, nekobox=329ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-123MS` (url=291ms, nekobox=292ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-131MS` (url=264ms, nekobox=301ms, status=yes)
10. `AKUN-010-466688-VLESS-WS-115MS` (url=286ms, nekobox=282ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-129MS` (url=260ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-133MS` (url=315ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-145MS` (url=259ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-140MS` (url=335ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-129MS` (url=262ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-124MS` (url=237ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-121MS` (url=286ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-131MS` (url=268ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-126MS` (url=290ms, status=HTTP 204)
20. `AKUN-020-1PASSWORD-VLESS-WS-100MS` (url=232ms, status=HTTP 204)
21. `AKUN-021-PAGES-VLESS-WS-136MS` (url=296ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-173MS` (url=366ms, status=HTTP 204)
23. `AKUN-023-ZOOM-VLESS-WS-120MS` (url=324ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-309MS` (url=750ms, status=HTTP 204)
25. `AKUN-025-SPEEDTEST-VLESS-WS-314MS` (url=588ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
