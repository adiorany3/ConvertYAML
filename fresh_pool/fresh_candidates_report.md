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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=243ms, nekobox=249ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS` (url=206ms, nekobox=231ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-74MS` (url=213ms, nekobox=263ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-78MS` (url=212ms, nekobox=258ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-71MS` (url=212ms, nekobox=251ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-64MS` (url=232ms, nekobox=255ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-73MS` (url=219ms, nekobox=275ms, status=yes)
8. `AKUN-008-U1HOST-FRA-VLESS-WS-81MS` (url=214ms, nekobox=258ms, status=yes)
9. `AKUN-009-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-98MS` (url=222ms, nekobox=250ms, status=yes)
10. `AKUN-010-HOSTOFF-NET-VLESS-WS-91MS` (url=237ms, nekobox=251ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-86MS` (url=233ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-108MS` (url=233ms, status=HTTP 204)
13. `AKUN-013-CLOUDWEBMANAGE-EU-FR-VLESS-WS-75MS` (url=240ms, status=HTTP 204)
14. `AKUN-014-NETCUP-VLESS-WS-108MS` (url=245ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-96MS` (url=210ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-85MS` (url=235ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-110MS` (url=218ms, status=HTTP 204)
18. `AKUN-018-SPACECORE-VLESS-WS-122MS` (url=237ms, status=HTTP 204)
19. `AKUN-019-008500-VLESS-WS-75MS` (url=208ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-83MS` (url=256ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-80MS` (url=211ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-105MS` (url=229ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-400MS` (url=849ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-385MS` (url=836ms, status=HTTP 204)
25. `AKUN-025-CONFLU-VLESS-WS-345MS` (url=771ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
