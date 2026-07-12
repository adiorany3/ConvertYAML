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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-60MS` (url=217ms, nekobox=260ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-61MS` (url=215ms, nekobox=240ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-65MS` (url=221ms, nekobox=250ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-82MS` (url=225ms, nekobox=264ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-88MS` (url=212ms, nekobox=240ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS` (url=217ms, nekobox=266ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-105MS` (url=218ms, nekobox=249ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-90MS` (url=236ms, nekobox=261ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-93MS` (url=231ms, nekobox=242ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-84MS` (url=256ms, nekobox=242ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-119MS` (url=233ms, status=HTTP 204)
12. `AKUN-012-HGC-GLOBAL-COMMUNICATION-VLESS-WS-85MS` (url=229ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-76MS` (url=219ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-110MS` (url=215ms, status=HTTP 204)
15. `AKUN-015-ZVC-VLESS-WS-166MS` (url=235ms, status=HTTP 204)
16. `AKUN-016-CLOUDWEBMANAGE-EU-FR-VLESS-WS-178MS` (url=231ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-199MS` (url=319ms, status=HTTP 204)
18. `AKUN-018-SPEEDTEST-VLESS-WS-74MS` (url=780ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-82MS` (url=224ms, status=HTTP 204)
20. `AKUN-020-SPEEDTEST-VLESS-WS-68MS` (url=782ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-82MS` (url=225ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-344MS` (url=769ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-345MS` (url=792ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-422MS` (url=768ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-629MS` (url=1648ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
