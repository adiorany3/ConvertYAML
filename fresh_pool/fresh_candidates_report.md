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
1. `AKUN-001-CLOUDWEBMANAGE-EU-FR-VLESS-WS-79MS` (url=214ms, nekobox=235ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=228ms, nekobox=247ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-91MS` (url=201ms, nekobox=187ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-93MS`
5. `AKUN-005-UNKNOWN-VLESS-WS-85MS` (url=330ms, nekobox=197ms, status=no)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-75MS` (url=201ms, nekobox=214ms, status=no)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-86MS` (url=228ms, nekobox=181ms, status=no)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-89MS` (url=246ms, nekobox=184ms, status=no)
9. `AKUN-009-UNKNOWN-VLESS-WS-95MS` (url=206ms, nekobox=183ms, status=no)
10. `AKUN-004-CLOUDFLARE-VLESS-WS-99MS`
11. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS`
12. `AKUN-006-CLOUDFLARE-VLESS-WS-91MS`
13. `AKUN-007-CLOUDFLARE-VLESS-WS-75MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-76MS` (url=231ms, nekobox=184ms, status=no)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-95MS` (url=228ms, nekobox=217ms, status=no)
16. `AKUN-008-CLOUDFLARE-VLESS-WS-90MS`
17. `AKUN-017-CLOUDFLARE-VLESS-WS-91MS` (url=198ms, nekobox=196ms, status=no)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-80MS` (url=215ms, nekobox=203ms, status=no)
19. `AKUN-009-BIGCOMMERCE-VLESS-WS-98MS`
20. `AKUN-021-CLOUDFLARE-VLESS-WS-85MS` (url=200ms, nekobox=172ms, status=no)
21. `AKUN-010-UNKNOWN-VLESS-WS-78MS`
22. `AKUN-023-UNKNOWN-VLESS-WS-84MS` (url=206ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-91MS` (url=274ms, status=HTTP 204)
24. `AKUN-025-DEV-VLESS-WS-95MS` (url=197ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-74MS` (url=222ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
