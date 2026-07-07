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
1. `AKUN-001-UNKNOWN-VLESS-WS-133MS` (url=284ms, nekobox=318ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-144MS` (url=349ms, nekobox=312ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-143MS` (url=288ms, nekobox=327ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-143MS` (url=310ms, nekobox=321ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-142MS` (url=291ms, nekobox=294ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-159MS` (url=355ms, nekobox=332ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-157MS` (url=293ms, nekobox=301ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-155MS` (url=275ms, nekobox=262ms, status=no)
9. `AKUN-008-UNKNOWN-VLESS-WS-150MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-165MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-144MS` (url=281ms, nekobox=250ms, status=no)
12. `AKUN-010-CLOUDFLARE-VLESS-WS-155MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-166MS` (url=324ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-174MS` (url=290ms, status=HTTP 204)
15. `AKUN-015-WPENG-VLESS-WS-167MS` (url=360ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-172MS` (url=276ms, status=HTTP 204)
17. `AKUN-017-466688-VLESS-WS-183MS` (url=286ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-172MS` (url=261ms, status=HTTP 204)
19. `AKUN-019-WPENG-VLESS-WS-150MS` (url=332ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-180MS` (url=279ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-374MS` (url=721ms, status=HTTP 204)
22. `AKUN-024-SPEEDTEST-VLESS-WS-378MS` (url=741ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-367MS` (url=757ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-402MS` (url=804ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-408MS` (url=844ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
