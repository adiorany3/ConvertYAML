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
1. `AKUN-001-UNKNOWN-VLESS-WS-76MS` (url=262ms, nekobox=275ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-83MS` (url=237ms, nekobox=285ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-88MS` (url=353ms, nekobox=285ms, status=yes)
4. `AKUN-004-COMPREND-NET-VLESS-WS-92MS` (url=247ms, nekobox=277ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-87MS` (url=250ms, nekobox=294ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-104MS` (url=266ms, nekobox=285ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-84MS` (url=267ms, nekobox=278ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-94MS` (url=245ms, nekobox=291ms, status=yes)
9. `AKUN-009-COMPREND-NET-VLESS-WS-100MS` (url=286ms, nekobox=314ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-93MS` (url=280ms, nekobox=309ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-121MS` (url=254ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-120MS` (url=264ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-138MS` (url=330ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-140MS` (url=240ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-109MS` (url=268ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-77MS` (url=247ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-113MS` (url=230ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-266MS` (url=462ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-260MS` (url=582ms, status=HTTP 204)
20. `AKUN-021-MICROSOFT-VLESS-WS-301MS` (url=696ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-304MS` (url=663ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-324MS` (url=672ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-305MS` (url=732ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-278MS` (url=560ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-308MS` (url=607ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
