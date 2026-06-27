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
1. `AKUN-001-UNKNOWN-VLESS-WS-76MS` (url=245ms, nekobox=256ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-79MS` (url=251ms, nekobox=272ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS` (url=249ms, nekobox=270ms, status=yes)
4. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-75MS` (url=232ms, nekobox=258ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-88MS` (url=242ms, nekobox=278ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-89MS` (url=236ms, nekobox=259ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-87MS` (url=235ms, nekobox=271ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-98MS` (url=271ms, nekobox=174ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-123MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-83MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-101MS` (url=242ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-152MS` (url=236ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-115MS` (url=276ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-259MS` (url=551ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-267MS` (url=569ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-284MS` (url=661ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-303MS` (url=633ms, status=HTTP 204)
19. `AKUN-019-OCTOPUSSS5-VLESS-WS-313MS` (url=661ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-317MS` (url=679ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-275MS` (url=576ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-330MS` (url=588ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-316MS` (url=667ms, status=HTTP 204)
24. `AKUN-029-CLOUDFLARE-VLESS-WS-536MS` (url=923ms, status=HTTP 204)
25. `AKUN-032-UNKNOWN-VLESS-WS-617MS` (url=926ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
