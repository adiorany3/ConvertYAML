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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-75MS` (url=243ms, nekobox=264ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-69MS` (url=265ms, nekobox=264ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-78MS` (url=272ms, nekobox=271ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-78MS` (url=234ms, nekobox=263ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-80MS` (url=254ms, nekobox=270ms, status=yes)
6. `AKUN-006-PUBLICDOMAINREGISTRY-NET-VLESS-WS-82MS` (url=253ms, nekobox=278ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-90MS` (url=236ms, nekobox=288ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-96MS` (url=245ms, nekobox=252ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-81MS` (url=236ms, nekobox=272ms, status=yes)
10. `AKUN-010-ES-FORNEX-20160629-VLESS-WS-86MS` (url=245ms, nekobox=286ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-97MS` (url=231ms, status=HTTP 204)
12. `AKUN-012-NODEJS-VLESS-WS-67MS` (url=256ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-93MS` (url=269ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-119MS` (url=222ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-80MS` (url=253ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-107MS` (url=236ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-143MS` (url=239ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-176MS` (url=921ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-258MS` (url=563ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-270MS` (url=671ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-259MS` (url=566ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-255MS` (url=646ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-284MS` (url=725ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-286MS` (url=678ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-220MS` (url=377ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
