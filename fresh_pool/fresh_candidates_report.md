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
1. `AKUN-001-OVH-VLESS-WS-64MS` (url=239ms, nekobox=253ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-61MS` (url=228ms, nekobox=250ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-74MS` (url=236ms, nekobox=260ms, status=yes)
4. `AKUN-004-WPENG-VLESS-WS-83MS` (url=234ms, nekobox=278ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-64MS` (url=231ms, nekobox=260ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-97MS` (url=245ms, nekobox=263ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-101MS` (url=274ms, nekobox=275ms, status=yes)
8. `AKUN-008-SPACECORE-VLESS-WS-103MS` (url=253ms, nekobox=269ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-90MS` (url=259ms, nekobox=290ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-81MS` (url=251ms, nekobox=258ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-108MS` (url=264ms, status=HTTP 204)
12. `AKUN-012-HOSTOFF-NET-VLESS-WS-110MS` (url=273ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-95MS` (url=242ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-90MS` (url=247ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-86MS` (url=260ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-111MS` (url=263ms, status=HTTP 204)
17. `AKUN-017-PAGES-VLESS-WS-116MS` (url=290ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-171MS` (url=227ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-263MS` (url=581ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-275MS` (url=587ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-279MS` (url=607ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-296MS` (url=613ms, status=HTTP 204)
23. `AKUN-025-SPEEDTEST-VLESS-WS-275MS` (url=534ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-303MS` (url=647ms, status=HTTP 204)
25. `AKUN-027-WPENG-VLESS-WS-76MS` (url=226ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
