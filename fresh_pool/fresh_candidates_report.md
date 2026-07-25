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
1. `AKUN-001-ZVC-VLESS-WS-59MS` (url=212ms, nekobox=221ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-65MS` (url=211ms, nekobox=236ms, status=yes)
3. `AKUN-003-3666888-VLESS-WS-66MS` (url=201ms, nekobox=239ms, status=yes)
4. `AKUN-004-SPEEDTEST-VLESS-WS-69MS` (url=209ms, nekobox=173ms, status=no)
5. `AKUN-004-CLOUDFLARE-VLESS-WS-76MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-74MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-71MS`
8. `AKUN-007-ZVC-VLESS-WS-89MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-78MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-77MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-77MS`
12. `AKUN-013-CLOUDFLARE-VLESS-WS-79MS` (url=200ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-79MS` (url=200ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-126MS` (url=215ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-224MS` (url=479ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-223MS` (url=478ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-116MS` (url=201ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-140MS` (url=331ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-91MS` (url=200ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-96MS` (url=219ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-128MS` (url=271ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-114MS` (url=220ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-91MS` (url=220ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-88MS` (url=212ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-226MS` (url=484ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
