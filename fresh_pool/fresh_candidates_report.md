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
1. `AKUN-001-ZVC-VLESS-WS-61MS` (url=212ms, nekobox=227ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-75MS` (url=231ms, nekobox=241ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS` (url=481ms, nekobox=234ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS` (url=214ms, nekobox=233ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-89MS` (url=199ms, nekobox=189ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-90MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-81MS` (url=223ms, nekobox=181ms, status=no)
10. `AKUN-008-ES-FORNEX-20160629-VLESS-WS-103MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-87MS`
12. `AKUN-010-UNKNOWN-VLESS-WS-88MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-99MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-99MS` (url=206ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-84MS` (url=204ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-101MS` (url=230ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-88MS` (url=212ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-126MS` (url=199ms, status=HTTP 204)
19. `AKUN-019-DEV-VLESS-WS-70MS` (url=226ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-96MS` (url=201ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-118MS` (url=200ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-106MS` (url=196ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-63MS` (url=213ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-209MS` (url=516ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-259MS` (url=549ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
