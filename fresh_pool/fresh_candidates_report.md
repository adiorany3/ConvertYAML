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
1. `AKUN-001-ADF-VLESS-WS-69MS` (url=219ms, nekobox=232ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-82MS` (url=217ms, nekobox=244ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-78MS` (url=228ms, nekobox=228ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-75MS` (url=219ms, nekobox=246ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-81MS` (url=210ms, nekobox=245ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS` (url=203ms, nekobox=237ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-86MS` (url=230ms, nekobox=237ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-69MS` (url=228ms, nekobox=234ms, status=yes)
9. `AKUN-009-CZ-LOTUNA-19970206-VLESS-WS-91MS` (url=213ms, nekobox=240ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-93MS` (url=221ms, nekobox=248ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-90MS` (url=223ms, status=HTTP 204)
12. `AKUN-012-UK-GB-DCL-01-20191003-VLESS-WS-97MS` (url=223ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-101MS` (url=213ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-88MS` (url=223ms, status=HTTP 204)
15. `AKUN-015-MEDIUM-VLESS-WS-81MS` (url=220ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-100MS` (url=212ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-95MS` (url=227ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-79MS` (url=525ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-74MS` (url=206ms, status=HTTP 204)
20. `AKUN-021-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-88MS` (url=202ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-93MS` (url=209ms, status=HTTP 204)
22. `AKUN-023-RS-RAPIDSEEDBOX-20190717-VLESS-WS-93MS` (url=211ms, status=HTTP 204)
23. `AKUN-024-WEBEX-VLESS-WS-73MS` (url=210ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-101MS` (url=218ms, status=HTTP 204)
25. `AKUN-026-1PASSWORD-VLESS-WS-76MS` (url=220ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
