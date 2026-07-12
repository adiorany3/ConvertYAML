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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-90MS` (url=219ms, nekobox=246ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-87MS` (url=216ms, nekobox=244ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-91MS` (url=209ms, nekobox=239ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-93MS` (url=207ms, nekobox=264ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-96MS` (url=203ms, nekobox=244ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-113MS` (url=212ms, nekobox=260ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-100MS` (url=212ms, nekobox=234ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-88MS` (url=219ms, nekobox=241ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-109MS` (url=216ms, nekobox=236ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-101MS` (url=215ms, nekobox=234ms, status=yes)
11. `AKUN-011-HGC-GLOBAL-COMMUNICATION-VLESS-WS-123MS` (url=211ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-132MS` (url=228ms, status=HTTP 204)
13. `AKUN-013-HETZNER-VLESS-WS-128MS` (url=211ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-106MS` (url=246ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-124MS` (url=226ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-156MS` (url=244ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-121MS` (url=218ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-223MS` (url=576ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-170MS` (url=215ms, status=HTTP 204)
20. `AKUN-021-QZZ-VLESS-WS-299MS` (url=1050ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-363MS` (url=784ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-367MS` (url=837ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-141MS` (url=225ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-384MS` (url=824ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-378MS` (url=786ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
