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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=213ms, nekobox=246ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-68MS` (url=219ms, nekobox=226ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-66MS` (url=202ms, nekobox=263ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-81MS` (url=221ms, nekobox=256ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-80MS` (url=220ms, nekobox=239ms, status=yes)
6. `AKUN-006-DIGITALOCEAN-VLESS-WS-81MS` (url=224ms, nekobox=247ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-89MS` (url=211ms, nekobox=258ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-95MS` (url=224ms, nekobox=243ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-97MS` (url=235ms, nekobox=256ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-104MS` (url=214ms, nekobox=232ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-105MS` (url=205ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-99MS` (url=208ms, status=HTTP 204)
13. `AKUN-013-PAGES-VLESS-WS-103MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-WEBEX-VLESS-WS-95MS` (url=203ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-125MS` (url=227ms, status=HTTP 204)
16. `AKUN-016-466688-VLESS-WS-82MS` (url=214ms, status=HTTP 204)
17. `AKUN-017-ZOOM-VLESS-WS-91MS` (url=221ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-167MS` (url=230ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-165MS` (url=202ms, status=HTTP 204)
20. `AKUN-024-UNKNOWN-VLESS-WS-357MS` (url=752ms, status=HTTP 204)
21. `AKUN-025-UNKNOWN-VLESS-WS-359MS` (url=758ms, status=HTTP 204)
22. `AKUN-026-UNKNOWN-VLESS-WS-384MS` (url=788ms, status=HTTP 204)
23. `AKUN-027-466688-VLESS-WS-188MS` (url=333ms, status=HTTP 204)
24. `AKUN-028-UNKNOWN-VLESS-WS-392MS` (url=810ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-389MS` (url=792ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
