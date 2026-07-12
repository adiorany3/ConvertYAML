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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=234ms, nekobox=271ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-59MS` (url=226ms, nekobox=249ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-65MS` (url=215ms, nekobox=265ms, status=yes)
4. `AKUN-004-ZOOM-VLESS-WS-78MS` (url=257ms, nekobox=251ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS` (url=238ms, nekobox=261ms, status=yes)
6. `AKUN-006-OVH-VLESS-WS-80MS` (url=329ms, nekobox=268ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-80MS` (url=240ms, nekobox=253ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-66MS` (url=279ms, nekobox=265ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-81MS` (url=198ms, nekobox=7178ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-86MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-81MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-77MS` (url=260ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-83MS` (url=220ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-89MS` (url=234ms, status=HTTP 204)
15. `AKUN-015-HETZNER-VLESS-WS-96MS` (url=250ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-67MS` (url=227ms, status=HTTP 204)
17. `AKUN-017-US-VLESS-WS-81MS` (url=232ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-121MS` (url=238ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-74MS` (url=252ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-118MS` (url=248ms, status=HTTP 204)
21. `AKUN-021-DEV-VLESS-WS-81MS` (url=231ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-85MS` (url=359ms, status=HTTP 204)
23. `AKUN-023-MYBB-VLESS-WS-76MS` (url=236ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-193MS` (url=497ms, status=HTTP 204)
25. `AKUN-025-ADF-VLESS-WS-84MS` (url=233ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
