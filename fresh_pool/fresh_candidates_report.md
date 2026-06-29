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
1. `AKUN-001-UNKNOWN-VLESS-WS-65MS` (url=221ms, nekobox=252ms, status=yes)
2. `AKUN-002-ZOOM-VLESS-WS-58MS` (url=220ms, nekobox=242ms, status=yes)
3. `AKUN-003-UK-GB-DCL-01-20191003-VLESS-WS-59MS` (url=218ms, nekobox=235ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-68MS` (url=228ms, nekobox=240ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-73MS` (url=209ms, nekobox=190ms, status=no)
6. `AKUN-005-UNKNOWN-VLESS-WS-77MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-66MS`
8. `AKUN-007-US-VLESS-WS-64MS`
9. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-81MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-100MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-84MS`
12. `AKUN-012-AEZA-NETWORK-VLESS-WS-134MS` (url=205ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-106MS` (url=210ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-106MS` (url=226ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-345MS` (url=758ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-361MS` (url=713ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-103MS` (url=242ms, status=HTTP 204)
18. `AKUN-019-WPENG-VLESS-WS-391MS` (url=872ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-378MS` (url=801ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-398MS` (url=822ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-383MS` (url=843ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-375MS` (url=593ms, status=HTTP 204)
23. `AKUN-024-BIGCOMMERCE-VLESS-WS-661MS` (url=1083ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-696MS` (url=815ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-749MS` (url=1054ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
