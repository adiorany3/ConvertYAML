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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-79MS` (url=286ms, nekobox=373ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-83MS` (url=355ms, nekobox=293ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-78MS` (url=343ms, nekobox=400ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-88MS` (url=321ms, nekobox=377ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-93MS` (url=277ms, nekobox=401ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-102MS` (url=292ms, nekobox=297ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-107MS` (url=336ms, nekobox=357ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-114MS` (url=399ms, nekobox=378ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-108MS` (url=325ms, nekobox=391ms, status=yes)
10. `AKUN-010-SM-VLESS-WS-119MS` (url=363ms, nekobox=308ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-107MS` (url=323ms, status=HTTP 204)
12. `AKUN-012-MYBB-VLESS-WS-90MS` (url=365ms, status=HTTP 204)
13. `AKUN-013-EU-VLESS-WS-114MS` (url=327ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-122MS` (url=322ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-97MS` (url=333ms, status=HTTP 204)
16. `AKUN-016-SPEEDTEST-VLESS-WS-108MS` (url=352ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-94MS` (url=297ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-93MS` (url=380ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-149MS` (url=363ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-174MS` (url=448ms, status=HTTP 204)
21. `AKUN-022-090227-VLESS-WS-173MS` (url=410ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-97MS` (url=362ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-193MS` (url=457ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-191MS` (url=446ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-195MS` (url=405ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
