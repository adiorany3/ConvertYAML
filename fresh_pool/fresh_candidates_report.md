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
1. `AKUN-001-ZVC-VLESS-WS-113MS` (url=319ms, nekobox=310ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-113MS` (url=253ms, nekobox=315ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-111MS` (url=312ms, nekobox=317ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-122MS` (url=304ms, nekobox=287ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-121MS` (url=325ms, nekobox=313ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-134MS` (url=336ms, nekobox=324ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-101MS` (url=288ms, nekobox=261ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-146MS` (url=281ms, nekobox=294ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-148MS` (url=294ms, nekobox=314ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-119MS` (url=273ms, nekobox=300ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-141MS` (url=270ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-162MS` (url=273ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-170MS` (url=269ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-178MS` (url=345ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-155MS` (url=271ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-132MS` (url=305ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-305MS` (url=677ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-335MS` (url=774ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-370MS` (url=810ms, status=HTTP 204)
20. `AKUN-021-WPENG-VLESS-WS-401MS` (url=775ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-352MS` (url=437ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-310MS` (url=835ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-576MS` (url=1336ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-601MS` (url=1097ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-633MS` (url=1000ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
