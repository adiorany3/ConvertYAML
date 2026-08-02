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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-78MS` (url=319ms, nekobox=314ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-75MS` (url=298ms, nekobox=306ms, status=yes)
3. `AKUN-003-SPEEDTEST-VLESS-WS-93MS` (url=356ms, nekobox=196ms, status=no)
4. `AKUN-003-ADF-VLESS-WS-107MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-103MS`
6. `AKUN-005-877774-VLESS-WS-103MS`
7. `AKUN-007-SPEEDTEST-VLESS-WS-85MS` (url=290ms, nekobox=214ms, status=no)
8. `AKUN-006-CLOUDFLARE-VLESS-WS-125MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-116MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-115MS`
11. `AKUN-009-MEDIUM-VLESS-WS-116MS`
12. `AKUN-010-1PASSWORD-VLESS-WS-100MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-102MS` (url=341ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-114MS` (url=423ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-102MS` (url=358ms, status=HTTP 204)
16. `AKUN-016-008500-VLESS-WS-86MS` (url=299ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-110MS` (url=340ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-113MS` (url=268ms, status=HTTP 204)
19. `AKUN-019-CMLIUSSSS-VLESS-WS-134MS` (url=369ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-121MS` (url=359ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-127MS` (url=474ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-82MS` (url=315ms, status=HTTP 204)
23. `AKUN-024-RMGYVPN-VLESS-WS-198MS` (url=402ms, status=HTTP 204)
24. `AKUN-025-DEV-VLESS-WS-102MS` (url=295ms, status=HTTP 204)
25. `AKUN-026-DEV-VLESS-WS-102MS` (url=332ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
