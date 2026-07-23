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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-118MS` (url=275ms, nekobox=287ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-123MS` (url=264ms, nekobox=288ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-121MS` (url=253ms, nekobox=294ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-116MS` (url=264ms, nekobox=274ms, status=yes)
5. `AKUN-005-HETZNER-VLESS-WS-125MS` (url=253ms, nekobox=298ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-126MS` (url=271ms, nekobox=296ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-126MS` (url=286ms, nekobox=295ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-134MS` (url=256ms, nekobox=282ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-130MS` (url=259ms, nekobox=324ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-154MS` (url=246ms, nekobox=280ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-131MS` (url=264ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-151MS` (url=249ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-123MS` (url=258ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-150MS` (url=256ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-126MS` (url=264ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-132MS` (url=290ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-169MS` (url=259ms, status=HTTP 204)
18. `AKUN-018-ZVC-VLESS-WS-126MS` (url=286ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-123MS` (url=264ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-179MS` (url=289ms, status=HTTP 204)
21. `AKUN-021-HETZNER-VLESS-WS-181MS` (url=270ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-161MS` (url=280ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-393MS` (url=840ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-417MS` (url=5165ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-415MS` (url=810ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
