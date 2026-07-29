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
1. `AKUN-001-UNKNOWN-VLESS-WS-61MS` (url=217ms, nekobox=232ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-64MS` (url=220ms, nekobox=177ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-60MS`
4. `AKUN-003-ICOOK-VLESS-WS-67MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-63MS`
6. `AKUN-005-HOSTINGER-VLESS-WS-71MS`
7. `AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-75MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-74MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-81MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-105MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-90MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-92MS` (url=221ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-106MS` (url=230ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-133MS` (url=222ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-109MS` (url=232ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-55MS` (url=214ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-149MS` (url=221ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-166MS` (url=257ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-131MS` (url=210ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-69MS` (url=222ms, status=HTTP 204)
21. `AKUN-021-090227-VLESS-WS-168MS` (url=339ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-117MS` (url=226ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-223MS` (url=549ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-185MS` (url=264ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-221MS` (url=494ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
