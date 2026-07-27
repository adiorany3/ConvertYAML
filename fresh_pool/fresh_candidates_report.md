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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-53MS` (url=211ms, nekobox=235ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-61MS` (url=219ms, nekobox=260ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-61MS` (url=216ms, nekobox=251ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-60MS` (url=230ms, nekobox=7179ms, status=no)
5. `AKUN-004-008500-VLESS-WS-60MS`
6. `AKUN-005-ZVC-VLESS-WS-61MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-63MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-66MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-59MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-57MS`
11. `AKUN-010-DEV-VLESS-WS-61MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-68MS` (url=215ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-57MS` (url=213ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-73MS` (url=224ms, status=HTTP 204)
15. `AKUN-015-ZVC-VLESS-WS-69MS` (url=200ms, status=HTTP 204)
16. `AKUN-016-MEDIUM-VLESS-WS-62MS` (url=229ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-70MS` (url=200ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-74MS` (url=214ms, status=HTTP 204)
19. `AKUN-019-CCWU-VLESS-WS-76MS` (url=212ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-68MS` (url=213ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-71MS` (url=228ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-73MS` (url=333ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-70MS` (url=216ms, status=HTTP 204)
24. `AKUN-024-1PASSWORD-VLESS-WS-62MS` (url=224ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-326MS` (url=1962ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
