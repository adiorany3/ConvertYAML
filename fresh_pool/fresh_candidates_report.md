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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-86MS` (url=222ms, nekobox=234ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-86MS` (url=230ms, nekobox=266ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-85MS` (url=198ms, nekobox=245ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-87MS` (url=230ms, nekobox=257ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-101MS` (url=255ms, nekobox=248ms, status=yes)
6. `AKUN-006-WPENG-VLESS-WS-89MS` (url=200ms, nekobox=264ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-90MS` (url=210ms, nekobox=257ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-97MS` (url=230ms, nekobox=241ms, status=yes)
9. `AKUN-009-OVH-VLESS-WS-105MS` (url=217ms, nekobox=256ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-90MS` (url=204ms, nekobox=263ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-105MS` (url=236ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-90MS` (url=226ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-84MS` (url=209ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-117MS` (url=215ms, status=HTTP 204)
15. `AKUN-015-PAGES-VLESS-WS-107MS` (url=210ms, status=HTTP 204)
16. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-129MS` (url=231ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-111MS` (url=217ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-254MS` (url=560ms, status=HTTP 204)
19. `AKUN-020-SPEEDTEST-VLESS-WS-247MS` (url=534ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-267MS` (url=520ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-275MS` (url=572ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-268MS` (url=561ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-248MS` (url=507ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-290MS` (url=585ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-255MS` (url=558ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
