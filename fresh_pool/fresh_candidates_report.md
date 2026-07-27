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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-81MS` (url=206ms, nekobox=246ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-72MS` (url=234ms, nekobox=234ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-79MS` (url=218ms, nekobox=261ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-82MS` (url=232ms, nekobox=201ms, status=no)
5. `AKUN-004-ZVC-VLESS-WS-71MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-82MS`
7. `AKUN-006-DEV-VLESS-WS-82MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-83MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-84MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-87MS` (url=204ms, nekobox=7178ms, status=no)
11. `AKUN-009-CLOUDFLARE-VLESS-WS-91MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-91MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-91MS` (url=257ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-98MS` (url=223ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-86MS` (url=220ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-94MS` (url=234ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-105MS` (url=238ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-112MS` (url=219ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-124MS` (url=262ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-112MS` (url=215ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-88MS` (url=223ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-129MS` (url=228ms, status=HTTP 204)
23. `AKUN-023-MYBB-VLESS-WS-95MS` (url=202ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-115MS` (url=232ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-81MS` (url=224ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
