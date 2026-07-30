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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-UNKNOWN-VLESS-WS-82MS` (url=219ms, nekobox=250ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-88MS` (url=232ms, nekobox=265ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-101MS` (url=260ms, nekobox=240ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-99MS` (url=218ms, nekobox=260ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-99MS` (url=215ms, nekobox=252ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-92MS` (url=209ms, nekobox=236ms, status=yes)
7. `AKUN-007-FMN5-RENTED-NET2-VLESS-WS-119MS` (url=212ms, nekobox=268ms, status=yes)
8. `AKUN-009-CLOUDFLARE-VLESS-WS-112MS` (url=230ms, nekobox=216ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-122MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-95MS`
11. `AKUN-010-ZOOM-VLESS-WS-127MS`
12. `AKUN-013-CLOUDFLARE-VLESS-WS-139MS` (url=198ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-161MS` (url=269ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-100MS` (url=218ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-135MS` (url=265ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-134MS` (url=236ms, status=HTTP 204)
17. `AKUN-018-090227-VLESS-WS-256MS` (url=550ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-356MS` (url=757ms, status=HTTP 204)
19. `AKUN-024-UNKNOWN-VLESS-WS-408MS` (url=811ms, status=HTTP 204)
20. `AKUN-025-CLOUDFLARE-VLESS-WS-555MS` (url=1028ms, status=HTTP 204)
21. `AKUN-026-UNKNOWN-VLESS-WS-80MS` (url=950ms, status=HTTP 204)
22. `AKUN-027-CLOUDFLARE-VLESS-WS-627MS` (url=1002ms, status=HTTP 204)
23. `AKUN-028-UNKNOWN-VLESS-WS-710MS` (url=1139ms, status=HTTP 204)
24. `AKUN-029-CLOUDFLARE-VLESS-WS-701MS` (url=1174ms, status=HTTP 204)
25. `AKUN-031-CLOUDFLARE-VLESS-WS-794MS` (url=1325ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
