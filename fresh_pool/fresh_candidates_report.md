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
1. `AKUN-001-UNKNOWN-VLESS-WS-57MS` (url=296ms, nekobox=267ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-58MS` (url=219ms, nekobox=271ms, status=yes)
3. `AKUN-003-877774-VLESS-WS-61MS` (url=218ms, nekobox=254ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-58MS` (url=228ms, nekobox=254ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-64MS` (url=219ms, nekobox=257ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-69MS` (url=219ms, nekobox=268ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-73MS` (url=227ms, nekobox=250ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-103MS` (url=228ms, nekobox=191ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-72MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-116MS`
11. `AKUN-011-DEV-VLESS-WS-76MS` (url=227ms, nekobox=173ms, status=no)
12. `AKUN-010-CLOUDFLARE-VLESS-WS-136MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-100MS` (url=228ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-167MS` (url=264ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-114MS` (url=245ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-262MS` (url=3136ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-370MS` (url=685ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-382MS` (url=826ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-392MS` (url=682ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-396MS` (url=799ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-361MS` (url=733ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-414MS` (url=756ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-417MS` (url=693ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-455MS` (url=781ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-441MS` (url=740ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
