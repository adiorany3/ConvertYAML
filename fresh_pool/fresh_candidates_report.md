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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=239ms, nekobox=252ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-71MS` (url=252ms, nekobox=274ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS` (url=222ms, nekobox=256ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS` (url=236ms, nekobox=263ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-72MS` (url=249ms, nekobox=258ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-65MS` (url=250ms, nekobox=303ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-86MS` (url=240ms, nekobox=269ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-87MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-83MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-85MS`
11. `AKUN-012-ZVC-VLESS-WS-92MS` (url=273ms, status=HTTP 204)
12. `AKUN-013-LEVIKOGJGFDD-VLESS-WS-108MS` (url=279ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-108MS` (url=236ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-123MS` (url=241ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-125MS` (url=282ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-146MS` (url=337ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-136MS` (url=311ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-138MS` (url=315ms, status=HTTP 204)
19. `AKUN-020-ZVC-VLESS-WS-168MS` (url=283ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-266MS` (url=2459ms, status=HTTP 204)
21. `AKUN-022-LT-LRTC-20060503-VLESS-WS-247MS` (url=603ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-252MS` (url=557ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-271MS` (url=596ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-263MS` (url=662ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-427MS` (url=312ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
