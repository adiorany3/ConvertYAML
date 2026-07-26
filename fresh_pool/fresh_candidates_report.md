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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-74MS` (url=277ms, nekobox=308ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-79MS` (url=375ms, nekobox=357ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-86MS` (url=316ms, nekobox=337ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-87MS` (url=313ms, nekobox=342ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-80MS` (url=279ms, nekobox=339ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-91MS` (url=352ms, nekobox=376ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-89MS` (url=310ms, nekobox=374ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-89MS` (url=284ms, nekobox=331ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-100MS` (url=358ms, nekobox=335ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-100MS` (url=292ms, nekobox=331ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-115MS` (url=287ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-112MS` (url=363ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-92MS` (url=275ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-97MS` (url=379ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-110MS` (url=288ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-88MS` (url=274ms, status=HTTP 204)
17. `AKUN-017-ZVC-VLESS-WS-125MS` (url=371ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-123MS` (url=410ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-116MS` (url=368ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-219MS` (url=390ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-304MS` (url=703ms, status=HTTP 204)
22. `AKUN-022-SPEEDTEST-VLESS-WS-308MS` (url=679ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-309MS` (url=596ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-325MS` (url=661ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-311MS` (url=1099ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
