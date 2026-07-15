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
1. `AKUN-001-UNKNOWN-VLESS-WS-67MS` (url=223ms, nekobox=278ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-73MS` (url=235ms, nekobox=270ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-71MS` (url=221ms, nekobox=255ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-86MS` (url=223ms, nekobox=259ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-88MS` (url=218ms, nekobox=261ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS` (url=299ms, nekobox=286ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-73MS` (url=229ms, nekobox=267ms, status=yes)
8. `AKUN-008-CZ-LOTUNA-19970206-VLESS-WS-110MS` (url=255ms, nekobox=286ms, status=yes)
9. `AKUN-009-WEBEX-VLESS-WS-102MS` (url=274ms, nekobox=270ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-93MS` (url=242ms, nekobox=265ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-84MS` (url=278ms, status=HTTP 204)
12. `AKUN-012-OVH-VLESS-WS-101MS` (url=250ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-108MS` (url=289ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-118MS` (url=318ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-102MS` (url=263ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-86MS` (url=258ms, status=HTTP 204)
17. `AKUN-017-DIXONS-VLESS-WS-147MS` (url=258ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-117MS` (url=240ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-100MS` (url=253ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-116MS` (url=264ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-86MS` (url=303ms, status=HTTP 204)
22. `AKUN-023-NEXUSMODS-VLESS-WS-112MS` (url=287ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-263MS` (url=567ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-269MS` (url=624ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-293MS` (url=653ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
