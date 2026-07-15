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
1. `AKUN-001-ZOOM-VLESS-WS-85MS` (url=285ms, nekobox=365ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-85MS` (url=330ms, nekobox=309ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-95MS` (url=239ms, nekobox=7177ms, status=no)
4. `AKUN-003-UNKNOWN-VLESS-WS-87MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-93MS`
6. `AKUN-005-PUBLICDOMAINREGISTRY-NET-VLESS-WS-91MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-103MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-91MS`
9. `AKUN-008-090227-VLESS-WS-96MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-98MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-90MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-103MS` (url=365ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-91MS` (url=251ms, status=HTTP 204)
14. `AKUN-014-ES-FORNEX-20160629-VLESS-WS-100MS` (url=408ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-119MS` (url=286ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-88MS` (url=283ms, status=HTTP 204)
17. `AKUN-017-466688-VLESS-WS-105MS` (url=340ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-103MS` (url=325ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-100MS` (url=288ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-114MS` (url=300ms, status=HTTP 204)
21. `AKUN-021-DEV-VLESS-WS-100MS` (url=337ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-105MS` (url=328ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-127MS` (url=291ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-134MS` (url=340ms, status=HTTP 204)
25. `AKUN-025-ORG-VLESS-WS-109MS` (url=367ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
