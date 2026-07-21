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
1. `AKUN-001-UNKNOWN-VLESS-WS-108MS` (url=328ms, nekobox=349ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-109MS` (url=411ms, nekobox=328ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-109MS` (url=283ms, nekobox=311ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-109MS` (url=281ms, nekobox=321ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-126MS` (url=252ms, nekobox=311ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-121MS` (url=281ms, nekobox=308ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-109MS` (url=286ms, nekobox=316ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-125MS` (url=387ms, nekobox=350ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-127MS` (url=410ms, nekobox=424ms, status=yes)
10. `AKUN-010-ZVC-VLESS-WS-144MS` (url=390ms, nekobox=304ms, status=yes)
11. `AKUN-011-ORG-VLESS-WS-147MS` (url=456ms, status=HTTP 204)
12. `AKUN-012-ZVC-VLESS-WS-118MS` (url=294ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-142MS` (url=279ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-113MS` (url=303ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-158MS` (url=303ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-137MS` (url=418ms, status=HTTP 204)
17. `AKUN-017-PAGES-VLESS-WS-165MS` (url=309ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-144MS` (url=280ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-155MS` (url=327ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-149MS` (url=341ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-308MS` (url=643ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-303MS` (url=670ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-341MS` (url=659ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-345MS` (url=407ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-548MS` (url=996ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
