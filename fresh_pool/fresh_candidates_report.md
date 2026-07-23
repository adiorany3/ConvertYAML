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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-57MS` (url=201ms, nekobox=225ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-65MS` (url=206ms, nekobox=227ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-63MS` (url=220ms, nekobox=243ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-63MS` (url=201ms, nekobox=228ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-65MS` (url=209ms, nekobox=234ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-62MS` (url=198ms, nekobox=233ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-68MS` (url=200ms, nekobox=234ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-79MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-80MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-69MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-100MS` (url=203ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-101MS` (url=207ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-108MS` (url=215ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-84MS` (url=195ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-63MS` (url=202ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-114MS` (url=239ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-132MS` (url=225ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-121MS` (url=206ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-123MS` (url=203ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-149MS` (url=280ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-223MS` (url=500ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-102MS` (url=237ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-227MS` (url=499ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-116MS` (url=218ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-215MS` (url=484ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
