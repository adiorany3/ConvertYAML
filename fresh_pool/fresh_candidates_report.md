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
1. `AKUN-001-ZVC-VLESS-WS-61MS` (url=228ms, nekobox=248ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-58MS` (url=222ms, nekobox=267ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-58MS` (url=237ms, nekobox=252ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-67MS` (url=230ms, nekobox=261ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-59MS` (url=236ms, nekobox=264ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-73MS` (url=231ms, nekobox=254ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-67MS` (url=239ms, nekobox=259ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-68MS` (url=236ms, nekobox=257ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-78MS` (url=217ms, nekobox=244ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-89MS` (url=237ms, nekobox=264ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-56MS` (url=236ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-70MS` (url=236ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-74MS` (url=225ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-95MS` (url=214ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-91MS` (url=228ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-104MS` (url=215ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-98MS` (url=239ms, status=HTTP 204)
18. `AKUN-019-ZVC-VLESS-WS-101MS` (url=229ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-83MS` (url=209ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-126MS` (url=260ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-118MS` (url=272ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-154MS` (url=280ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-349MS` (url=5532ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-362MS` (url=1095ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-363MS` (url=826ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
