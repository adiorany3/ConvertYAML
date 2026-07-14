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
1. `AKUN-001-UNKNOWN-VLESS-WS-81MS` (url=303ms, nekobox=318ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-96MS` (url=278ms, nekobox=315ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-104MS` (url=285ms, nekobox=315ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-111MS` (url=296ms, nekobox=337ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-98MS` (url=363ms, nekobox=351ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-110MS` (url=375ms, nekobox=326ms, status=yes)
7. `AKUN-007-466688-VLESS-WS-116MS` (url=309ms, nekobox=343ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-119MS` (url=297ms, nekobox=7176ms, status=no)
9. `AKUN-008-UNKNOWN-VLESS-WS-114MS`
10. `AKUN-009-CZ-LOTUNA-19970206-VLESS-WS-102MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-128MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-132MS` (url=341ms, status=HTTP 204)
13. `AKUN-013-CCWU-VLESS-WS-129MS` (url=312ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-128MS` (url=313ms, status=HTTP 204)
15. `AKUN-015-ZVC-VLESS-WS-143MS` (url=380ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-136MS` (url=329ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-130MS` (url=287ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-163MS` (url=326ms, status=HTTP 204)
19. `AKUN-019-WPENG-VLESS-WS-136MS` (url=379ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-126MS` (url=308ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-316MS` (url=646ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-308MS` (url=684ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-309MS` (url=603ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-310MS` (url=549ms, status=HTTP 204)
25. `AKUN-025-DE-CLOUDKLEYER-20190515-VLESS-WS-311MS` (url=1122ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
