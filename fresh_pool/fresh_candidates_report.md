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
1. `AKUN-001-UNKNOWN-VLESS-WS-90MS` (url=221ms, nekobox=243ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-94MS` (url=226ms, nekobox=246ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-90MS` (url=214ms, nekobox=287ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-94MS` (url=248ms, nekobox=235ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-97MS` (url=221ms, nekobox=239ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-105MS` (url=224ms, nekobox=278ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-96MS` (url=216ms, nekobox=281ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-99MS` (url=215ms, nekobox=254ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS` (url=224ms, nekobox=279ms, status=yes)
10. `AKUN-010-NODEHOST-VLESS-WS-95MS` (url=276ms, nekobox=284ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-95MS` (url=282ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-116MS` (url=238ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-108MS` (url=248ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-121MS` (url=234ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-132MS` (url=233ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-105MS` (url=217ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-103MS` (url=343ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-148MS` (url=327ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-124MS` (url=238ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-146MS` (url=297ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-189MS` (url=244ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-124MS` (url=240ms, status=HTTP 204)
23. `AKUN-023-HETZNER-VLESS-WS-139MS` (url=247ms, status=HTTP 204)
24. `AKUN-024-HETZNER-VLESS-WS-166MS` (url=290ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-395MS` (url=858ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
