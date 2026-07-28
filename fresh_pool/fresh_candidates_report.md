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
1. `AKUN-001-UNKNOWN-VLESS-WS-115MS` (url=1658ms, nekobox=414ms, status=no)
2. `AKUN-001-UNKNOWN-VLESS-WS-126MS`
3. `AKUN-002-UNKNOWN-VLESS-WS-130MS`
4. `AKUN-003-UNKNOWN-VLESS-WS-146MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-156MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-186MS`
7. `AKUN-008-CLOUDFLARE-VLESS-WS-177MS` (url=241ms, nekobox=229ms, status=no)
8. `AKUN-009-CLOUDFLARE-VLESS-WS-161MS` (url=264ms, nekobox=234ms, status=no)
9. `AKUN-006-CLOUDFLARE-VLESS-WS-146MS`
10. `AKUN-007-SKK-VLESS-WS-177MS`
11. `AKUN-008-CLOUDFLARE-VLESS-WS-236MS`
12. `AKUN-009-CLOUDFLARE-VLESS-WS-290MS`
13. `AKUN-010-CLOUDFLARE-VLESS-WS-305MS`
14. `AKUN-016-CLOUDFLARE-VLESS-WS-399MS` (url=822ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-175MS` (url=237ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-141MS` (url=248ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-425MS` (url=831ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-146MS` (url=256ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-141MS` (url=247ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-509MS` (url=2122ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-179MS` (url=224ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-733MS` (url=1106ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-726MS` (url=1159ms, status=HTTP 204)
24. `AKUN-028-SHOPIFY-NET-VLESS-WS-639MS` (url=780ms, status=HTTP 204)
25. `AKUN-030-CLOUDFLARE-VLESS-WS-774MS` (url=1325ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
