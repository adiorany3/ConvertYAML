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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-70MS` (url=223ms, nekobox=267ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS` (url=229ms, nekobox=254ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=237ms, nekobox=255ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS` (url=239ms, nekobox=264ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-78MS` (url=225ms, nekobox=254ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-92MS` (url=230ms, nekobox=265ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-92MS` (url=236ms, nekobox=262ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS` (url=279ms, nekobox=269ms, status=yes)
9. `AKUN-009-ZVC-VLESS-WS-90MS` (url=300ms, nekobox=251ms, status=yes)
10. `AKUN-010-PUBLICDOMAINREGISTRY-NET-VLESS-WS-79MS` (url=253ms, nekobox=253ms, status=yes)
11. `AKUN-011-DEV-VLESS-WS-79MS` (url=233ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-104MS` (url=241ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-105MS` (url=222ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-124MS` (url=239ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-131MS` (url=244ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-80MS` (url=235ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-195MS` (url=675ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-259MS` (url=604ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-268MS` (url=657ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-286MS` (url=656ms, status=HTTP 204)
21. `AKUN-022-US-VLESS-WS-98MS` (url=246ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-87MS` (url=271ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-82MS` (url=242ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-299MS` (url=729ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-287MS` (url=558ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
