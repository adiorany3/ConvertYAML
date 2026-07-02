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
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-94MS` (url=216ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-102MS` (url=216ms, nekobox=333ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-96MS` (url=232ms, nekobox=239ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-115MS` (url=265ms, nekobox=257ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-92MS` (url=222ms, nekobox=249ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-105MS` (url=214ms, nekobox=261ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-119MS` (url=216ms, nekobox=249ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-125MS` (url=232ms, nekobox=282ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-117MS` (url=212ms, nekobox=235ms, status=yes)
10. `AKUN-010-WPENG-VLESS-WS-104MS` (url=340ms, nekobox=250ms, status=yes)
11. `AKUN-011-UK-GB-DCL-01-20191003-VLESS-WS-140MS` (url=237ms, status=HTTP 204)
12. `AKUN-012-DIGITALOCEAN-VLESS-WS-107MS` (url=238ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-117MS` (url=217ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-141MS` (url=256ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-159MS` (url=272ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-183MS` (url=225ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-150MS` (url=257ms, status=HTTP 204)
18. `AKUN-018-COMPREND-NET-VLESS-WS-170MS` (url=256ms, status=HTTP 204)
19. `AKUN-020-COMPREND-NET-VLESS-WS-183MS` (url=253ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-390MS` (url=813ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-405MS` (url=768ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-388MS` (url=848ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-416MS` (url=788ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-418MS` (url=913ms, status=HTTP 204)
25. `AKUN-027-WPENG-VLESS-WS-443MS` (url=891ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
