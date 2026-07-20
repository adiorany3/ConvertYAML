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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=217ms, nekobox=242ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS` (url=213ms, nekobox=255ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-80MS` (url=224ms, nekobox=321ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS` (url=233ms, nekobox=246ms, status=yes)
5. `AKUN-005-DEV-VLESS-WS-80MS` (url=226ms, nekobox=239ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-65MS` (url=246ms, nekobox=247ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-85MS` (url=217ms, nekobox=257ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-88MS` (url=240ms, nekobox=246ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-74MS` (url=237ms, nekobox=232ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-70MS` (url=237ms, nekobox=244ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-96MS` (url=253ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-71MS` (url=213ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-90MS` (url=226ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-86MS` (url=239ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-105MS` (url=327ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-124MS` (url=207ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-101MS` (url=252ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-106MS` (url=266ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-138MS` (url=266ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-85MS` (url=265ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-77MS` (url=215ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-95MS` (url=219ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-116MS` (url=240ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-158MS` (url=235ms, status=HTTP 204)
25. `AKUN-025-WPENG-VLESS-WS-126MS` (url=233ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
