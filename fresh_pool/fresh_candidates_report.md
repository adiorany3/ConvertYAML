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
1. `AKUN-001-UNKNOWN-VLESS-WS-58MS` (url=209ms, nekobox=243ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-58MS` (url=213ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-67MS` (url=212ms, nekobox=250ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-67MS` (url=195ms, nekobox=244ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-69MS` (url=230ms, nekobox=257ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-70MS` (url=204ms, nekobox=260ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-80MS` (url=231ms, nekobox=240ms, status=yes)
8. `AKUN-008-WEBEX-VLESS-WS-64MS` (url=219ms, nekobox=227ms, status=yes)
9. `AKUN-009-ZVC-VLESS-WS-67MS` (url=219ms, nekobox=244ms, status=yes)
10. `AKUN-010-WEYRO-NET-VLESS-WS-88MS` (url=219ms, nekobox=262ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-76MS` (url=228ms, status=HTTP 204)
12. `AKUN-012-MELBICOM-VLESS-WS-111MS` (url=218ms, status=HTTP 204)
13. `AKUN-013-WEBEX-VLESS-WS-74MS` (url=218ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-104MS` (url=209ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-135MS` (url=222ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-67MS` (url=216ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-80MS` (url=335ms, status=HTTP 204)
18. `AKUN-018-PAGES-VLESS-WS-136MS` (url=275ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-359MS` (url=739ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-383MS` (url=814ms, status=HTTP 204)
21. `AKUN-021-RC-PRO-5-VLESS-WS-383MS` (url=763ms, status=HTTP 204)
22. `AKUN-022-GUARDNETWORK-VLESS-WS-378MS` (url=795ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-385MS` (url=841ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-75MS` (url=224ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-347MS` (url=737ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
