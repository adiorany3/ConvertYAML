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
1. `AKUN-001-CCWU-VLESS-WS-70MS` (url=214ms, nekobox=251ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-59MS` (url=249ms, nekobox=173ms, status=no)
3. `AKUN-002-UNKNOWN-VLESS-WS-75MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-65MS` (url=222ms, nekobox=169ms, status=no)
6. `AKUN-004-CLOUDFLARE-VLESS-WS-66MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-76MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-69MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-86MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-103MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-91MS`
13. `AKUN-014-CLOUDFLARE-VLESS-WS-87MS` (url=226ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-76MS` (url=222ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-65MS` (url=214ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-94MS` (url=209ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-69MS` (url=212ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-105MS` (url=212ms, status=HTTP 204)
19. `AKUN-020-DEV-VLESS-WS-122MS` (url=212ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-82MS` (url=228ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-81MS` (url=240ms, status=HTTP 204)
22. `AKUN-024-008500-VLESS-WS-120MS` (url=215ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-89MS` (url=225ms, status=HTTP 204)
24. `AKUN-026-PAGES-VLESS-WS-116MS` (url=262ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-81MS` (url=216ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
