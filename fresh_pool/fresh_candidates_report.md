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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=218ms, nekobox=236ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-76MS` (url=210ms, nekobox=240ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-67MS` (url=212ms, nekobox=243ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-82MS` (url=211ms, nekobox=243ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-63MS` (url=226ms, nekobox=171ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-88MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-77MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-78MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-87MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-91MS`
11. `AKUN-011-UNKNOWN-VLESS-WS-86MS` (url=233ms, nekobox=7178ms, status=no)
12. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS`
13. `AKUN-013-008500-VLESS-WS-82MS` (url=212ms, status=HTTP 204)
14. `AKUN-014-DEV-VLESS-WS-74MS` (url=229ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-67MS` (url=204ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-76MS` (url=229ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-116MS` (url=222ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-128MS` (url=228ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-97MS` (url=223ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-73MS` (url=320ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-73MS` (url=208ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-137MS` (url=231ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-284MS` (url=630ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-375MS` (url=686ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-76MS` (url=227ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
