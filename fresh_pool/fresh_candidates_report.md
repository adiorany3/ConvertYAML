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
1. `AKUN-001-UNKNOWN-VLESS-WS-62MS` (url=223ms, nekobox=263ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=224ms, nekobox=264ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS` (url=220ms, nekobox=264ms, status=yes)
4. `AKUN-004-IONOS-VLESS-WS-66MS` (url=247ms, nekobox=264ms, status=yes)
5. `AKUN-005-PUBLICDOMAINREGISTRY-NET-VLESS-WS-70MS` (url=228ms, nekobox=292ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-100MS` (url=230ms, nekobox=251ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-62MS` (url=220ms, nekobox=255ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-79MS` (url=219ms, nekobox=276ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-73MS` (url=224ms, nekobox=266ms, status=yes)
10. `AKUN-010-ZVC-VLESS-WS-106MS` (url=232ms, nekobox=256ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-119MS` (url=246ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-107MS` (url=212ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-75MS` (url=219ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-107MS` (url=226ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-144MS` (url=228ms, status=HTTP 204)
16. `AKUN-017-WEBEX-VLESS-WS-78MS` (url=230ms, status=HTTP 204)
17. `AKUN-018-466688-VLESS-WS-124MS` (url=255ms, status=HTTP 204)
18. `AKUN-019-WEBEX-VLESS-WS-79MS` (url=269ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-215MS` (url=636ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-354MS` (url=764ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-364MS` (url=777ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-114MS` (url=234ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-393MS` (url=886ms, status=HTTP 204)
24. `AKUN-025-CELESTARA-VLESS-WS-413MS` (url=845ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-673MS` (url=1081ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
