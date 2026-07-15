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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-67MS` (url=229ms, nekobox=283ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-76MS` (url=239ms, nekobox=301ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-82MS` (url=265ms, nekobox=418ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS` (url=245ms, nekobox=266ms, status=yes)
5. `AKUN-005-MGN-20250528-VLESS-WS-93MS` (url=268ms, nekobox=280ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-84MS` (url=246ms, nekobox=258ms, status=yes)
7. `AKUN-007-WPENG-VLESS-WS-97MS` (url=270ms, nekobox=283ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-93MS` (url=245ms, nekobox=286ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-85MS` (url=248ms, nekobox=267ms, status=yes)
10. `AKUN-010-DIXONS-VLESS-WS-89MS` (url=253ms, nekobox=284ms, status=yes)
11. `AKUN-011-US-VLESS-WS-89MS` (url=265ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-83MS` (url=259ms, status=HTTP 204)
13. `AKUN-013-466688-VLESS-WS-101MS` (url=253ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-110MS` (url=308ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-128MS` (url=290ms, status=HTTP 204)
16. `AKUN-016-NEXUSMODS-VLESS-WS-111MS` (url=277ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-131MS` (url=298ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-103MS` (url=234ms, status=HTTP 204)
19. `AKUN-019-466688-VLESS-WS-97MS` (url=273ms, status=HTTP 204)
20. `AKUN-020-POLICE-VLESS-WS-135MS` (url=285ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-89MS` (url=257ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-144MS` (url=265ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-92MS` (url=332ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-263MS` (url=546ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-159MS` (url=360ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
