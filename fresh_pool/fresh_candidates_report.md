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
1. `AKUN-001-UNKNOWN-VLESS-WS-76MS` (url=456ms, nekobox=359ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-82MS` (url=283ms, nekobox=360ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-111MS` (url=290ms, nekobox=350ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-86MS` (url=355ms, nekobox=361ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-109MS` (url=370ms, nekobox=474ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-130MS` (url=373ms, nekobox=348ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-149MS` (url=272ms, nekobox=358ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-156MS` (url=406ms, nekobox=376ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-129MS` (url=397ms, nekobox=371ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-138MS` (url=299ms, nekobox=352ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-127MS` (url=264ms, status=HTTP 204)
12. `AKUN-013-UNKNOWN-VLESS-WS-180MS` (url=432ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-179MS` (url=484ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-226MS` (url=429ms, status=HTTP 204)
15. `AKUN-016-DE-CLOUDKLEYER-20190515-VLESS-WS-108MS` (url=372ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-167MS` (url=442ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-188MS` (url=392ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-176MS` (url=446ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-454MS` (url=845ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-487MS` (url=865ms, status=HTTP 204)
21. `AKUN-024-UNKNOWN-VLESS-WS-546MS` (url=933ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-519MS` (url=975ms, status=HTTP 204)
23. `AKUN-028-UNKNOWN-VLESS-WS-639MS` (url=1104ms, status=HTTP 204)
24. `AKUN-029-UNKNOWN-VLESS-WS-659MS` (url=3675ms, status=HTTP 204)
25. `AKUN-030-UNKNOWN-VLESS-WS-685MS` (url=4557ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
