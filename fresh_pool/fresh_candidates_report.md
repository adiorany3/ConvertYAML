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
1. `AKUN-001-UNKNOWN-VLESS-WS-71MS` (url=221ms, nekobox=241ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS` (url=226ms, nekobox=241ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-74MS` (url=219ms, nekobox=239ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-84MS` (url=201ms, nekobox=257ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-92MS` (url=217ms, nekobox=247ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-98MS` (url=208ms, nekobox=240ms, status=yes)
7. `AKUN-007-NET-USA-VLESS-WS-93MS` (url=236ms, nekobox=260ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-96MS` (url=228ms, nekobox=247ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-92MS` (url=219ms, nekobox=249ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-97MS` (url=214ms, nekobox=249ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-85MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-108MS` (url=230ms, status=HTTP 204)
13. `AKUN-013-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-107MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-114MS` (url=220ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-83MS` (url=231ms, status=HTTP 204)
16. `AKUN-016-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-80MS` (url=1408ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-257MS` (url=542ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-345MS` (url=765ms, status=HTTP 204)
19. `AKUN-023-UNKNOWN-VLESS-WS-367MS` (url=726ms, status=HTTP 204)
20. `AKUN-024-UNKNOWN-VLESS-WS-376MS` (url=903ms, status=HTTP 204)
21. `AKUN-025-130209-VLESS-WS-397MS` (url=3893ms, status=HTTP 204)
22. `AKUN-026-UNKNOWN-VLESS-WS-483MS` (url=989ms, status=HTTP 204)
23. `AKUN-027-UNKNOWN-VLESS-WS-651MS` (url=980ms, status=HTTP 204)
24. `AKUN-033-UNKNOWN-VLESS-WS-694MS` (url=1157ms, status=HTTP 204)
25. `AKUN-035-UNKNOWN-VLESS-WS-785MS` (url=1430ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
