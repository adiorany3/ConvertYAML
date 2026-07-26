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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-70MS` (url=238ms, nekobox=260ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-71MS` (url=231ms, nekobox=271ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-65MS` (url=225ms, nekobox=266ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS` (url=239ms, nekobox=185ms, status=no)
5. `AKUN-004-UNKNOWN-VLESS-WS-67MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-75MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-65MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-64MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-78MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-68MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-83MS` (url=218ms, nekobox=7177ms, status=no)
12. `AKUN-010-CLOUDFLARE-VLESS-WS-73MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-73MS` (url=243ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-73MS` (url=300ms, status=HTTP 204)
15. `AKUN-016-DEV-VLESS-WS-64MS` (url=226ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-77MS` (url=231ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-101MS` (url=282ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-76MS` (url=226ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-69MS` (url=251ms, status=HTTP 204)
20. `AKUN-021-VULTR-VLESS-WS-75MS` (url=244ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-159MS` (url=301ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-87MS` (url=224ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-248MS` (url=544ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-274MS` (url=537ms, status=HTTP 204)
25. `AKUN-026-ZVC-VLESS-WS-82MS` (url=281ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
