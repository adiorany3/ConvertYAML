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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-56MS` (url=229ms, nekobox=250ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-59MS` (url=226ms, nekobox=246ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-58MS` (url=215ms, nekobox=264ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-53MS` (url=220ms, nekobox=262ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-56MS` (url=213ms, nekobox=255ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-58MS` (url=223ms, nekobox=240ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-62MS` (url=217ms, nekobox=247ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-64MS` (url=236ms, nekobox=253ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-72MS` (url=223ms, nekobox=259ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-68MS` (url=236ms, nekobox=259ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-62MS` (url=225ms, status=HTTP 204)
12. `AKUN-012-ZOOM-VLESS-WS-58MS` (url=237ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-99MS` (url=224ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-106MS` (url=238ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-102MS` (url=214ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-71MS` (url=244ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-127MS` (url=343ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-79MS` (url=262ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-56MS` (url=229ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-133MS` (url=238ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-65MS` (url=222ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-138MS` (url=225ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-125MS` (url=256ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-99MS` (url=231ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-112MS` (url=255ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
