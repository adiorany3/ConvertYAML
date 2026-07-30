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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=227ms, nekobox=233ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-61MS`
3. `AKUN-003-CLOUDFLARE-VLESS-WS-61MS` (url=228ms, nekobox=171ms, status=no)
4. `AKUN-002-BIGCOMMERCE-VLESS-WS-58MS`
5. `AKUN-003-ZVC-VLESS-WS-74MS`
6. `AKUN-004-CLOUDFLARE-VLESS-WS-78MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-73MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-82MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-81MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-68MS` (url=210ms, nekobox=173ms, status=no)
11. `AKUN-008-CLOUDFLARE-VLESS-WS-71MS`
12. `AKUN-009-CLOUDFLARE-VLESS-WS-79MS`
13. `AKUN-010-UNKNOWN-VLESS-WS-80MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-78MS` (url=209ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-78MS` (url=226ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-94MS` (url=218ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-97MS` (url=211ms, status=HTTP 204)
18. `AKUN-018-DEV-VLESS-WS-88MS` (url=229ms, status=HTTP 204)
19. `AKUN-019-008500-VLESS-WS-69MS` (url=220ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-92MS` (url=213ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-102MS` (url=224ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-97MS` (url=222ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-77MS` (url=219ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-97MS` (url=200ms, status=HTTP 204)
25. `AKUN-025-DEV-VLESS-WS-110MS` (url=220ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
