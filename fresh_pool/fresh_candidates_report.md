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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-75MS` (url=220ms, nekobox=260ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-82MS` (url=215ms, nekobox=258ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-83MS` (url=199ms, nekobox=249ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-81MS` (url=223ms, nekobox=245ms, status=yes)
5. `AKUN-005-US-VLESS-WS-90MS` (url=202ms, nekobox=234ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-83MS` (url=214ms, nekobox=254ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-97MS` (url=231ms, nekobox=231ms, status=yes)
8. `AKUN-008-POLICE-VLESS-WS-99MS` (url=216ms, nekobox=242ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-85MS` (url=228ms, nekobox=7176ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-86MS`
11. `AKUN-010-UK-GB-DCL-01-20191003-VLESS-WS-103MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-87MS` (url=229ms, status=HTTP 204)
13. `AKUN-013-DEV-VLESS-WS-107MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-CZ-LOTUNA-19970206-VLESS-WS-90MS` (url=238ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-105MS` (url=200ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-108MS` (url=218ms, status=HTTP 204)
17. `AKUN-017-WPENG-VLESS-WS-104MS` (url=237ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-85MS` (url=208ms, status=HTTP 204)
19. `AKUN-019-DIGITALOCEAN-VLESS-WS-99MS` (url=210ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-100MS` (url=230ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-100MS` (url=213ms, status=HTTP 204)
22. `AKUN-022-UK-GB-DCL-01-20191003-VLESS-WS-111MS` (url=233ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-115MS` (url=227ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-109MS` (url=233ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-116MS` (url=222ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
