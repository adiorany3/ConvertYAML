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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=213ms, nekobox=246ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-59MS` (url=212ms, nekobox=235ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-57MS` (url=220ms, nekobox=240ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-72MS` (url=225ms, nekobox=236ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-62MS` (url=210ms, nekobox=237ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-62MS` (url=226ms, nekobox=249ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-61MS` (url=230ms, nekobox=251ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-73MS` (url=211ms, nekobox=244ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-80MS` (url=237ms, nekobox=255ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-71MS` (url=226ms, nekobox=247ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-69MS` (url=225ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-74MS` (url=215ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-59MS` (url=225ms, status=HTTP 204)
14. `AKUN-014-ZVC-VLESS-WS-56MS` (url=230ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-58MS` (url=234ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-114MS` (url=274ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-70MS` (url=225ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-146MS` (url=287ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-87MS` (url=224ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-271MS` (url=577ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-337MS` (url=716ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-346MS` (url=693ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-380MS` (url=3956ms, status=HTTP 204)
24. `AKUN-024-CN-CF-VLESS-WS-424MS` (url=887ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-331MS` (url=743ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
