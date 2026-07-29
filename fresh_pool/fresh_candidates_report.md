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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-93MS` (url=300ms, nekobox=317ms, status=yes)
2. `AKUN-002-HOSTINGER-VLESS-WS-108MS` (url=244ms, nekobox=270ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-131MS` (url=264ms, nekobox=330ms, status=yes)
4. `AKUN-004-LEVIKOGJGFDD-VLESS-WS-131MS` (url=287ms, nekobox=330ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-121MS` (url=220ms, nekobox=218ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-140MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-145MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-148MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-134MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-152MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-148MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-170MS` (url=239ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-124MS` (url=313ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-132MS` (url=265ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-177MS` (url=340ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-179MS` (url=375ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-197MS` (url=305ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-150MS` (url=327ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-206MS` (url=463ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-222MS` (url=405ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-138MS` (url=272ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-192MS` (url=354ms, status=HTTP 204)
23. `AKUN-023-CONFLU-VLESS-WS-302MS` (url=642ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-516MS` (url=765ms, status=HTTP 204)
25. `AKUN-030-CLOUDFLARE-VLESS-WS-621MS` (url=1062ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
