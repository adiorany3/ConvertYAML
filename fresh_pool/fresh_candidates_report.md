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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=228ms, nekobox=250ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-67MS` (url=230ms, nekobox=259ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=266ms, nekobox=288ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-72MS` (url=233ms, nekobox=253ms, status=yes)
5. `AKUN-005-DEV-VLESS-WS-78MS` (url=234ms, nekobox=275ms, status=yes)
6. `AKUN-006-DEV-VLESS-WS-77MS` (url=224ms, nekobox=259ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-75MS` (url=248ms, nekobox=279ms, status=yes)
8. `AKUN-008-CZ-LOTUNA-19970206-VLESS-WS-73MS` (url=238ms, nekobox=272ms, status=yes)
9. `AKUN-009-DE5-VLESS-WS-87MS` (url=255ms, nekobox=303ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-91MS` (url=225ms, nekobox=252ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-81MS` (url=255ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-93MS` (url=249ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-77MS` (url=238ms, status=HTTP 204)
14. `AKUN-014-ZVC-VLESS-WS-84MS` (url=280ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-81MS` (url=252ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-90MS` (url=270ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-74MS` (url=236ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-110MS` (url=237ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-104MS` (url=246ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-110MS` (url=276ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-134MS` (url=225ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-85MS` (url=233ms, status=HTTP 204)
23. `AKUN-023-WPENG-VLESS-WS-122MS` (url=384ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-158MS` (url=552ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-115MS` (url=273ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
