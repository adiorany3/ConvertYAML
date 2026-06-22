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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-58MS` (url=218ms, nekobox=253ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-61MS` (url=225ms, nekobox=245ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS` (url=221ms, nekobox=234ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-80MS` (url=207ms, nekobox=182ms, status=no)
5. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-97MS`
6. `AKUN-005-GO-DADDY-COM-LLC-VLESS-WS-112MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-83MS` (url=221ms, nekobox=7178ms, status=no)
8. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-108MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-99MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-77MS` (url=257ms, nekobox=195ms, status=no)
11. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-72MS`
12. `AKUN-009-CLOUDFLARE-VLESS-WS-111MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-76MS` (url=230ms, nekobox=182ms, status=no)
14. `AKUN-010-UNKNOWN-VLESS-WS-77MS`
15. `AKUN-015-UNKNOWN-VLESS-WS-74MS` (url=233ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-362MS` (url=782ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-73MS` (url=234ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-359MS` (url=783ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-380MS` (url=899ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-416MS` (url=828ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-383MS` (url=774ms, status=HTTP 204)
22. `AKUN-022-SPEEDTEST-VLESS-WS-388MS` (url=841ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-129MS` (url=225ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-391MS` (url=810ms, status=HTTP 204)
25. `AKUN-027-KAWAII520-VLESS-WS-633MS` (url=1014ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
