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
1. `AKUN-001-UNKNOWN-VLESS-WS-64MS` (url=205ms, nekobox=232ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=208ms, nekobox=242ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-67MS` (url=213ms, nekobox=235ms, status=yes)
4. `AKUN-004-CZ-LOTUNA-19970206-VLESS-WS-70MS` (url=211ms, nekobox=245ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-68MS` (url=204ms, nekobox=251ms, status=yes)
6. `AKUN-006-ORG-VLESS-WS-79MS` (url=237ms, nekobox=255ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-95MS` (url=202ms, nekobox=253ms, status=yes)
8. `AKUN-008-UK-GB-DCL-01-20191003-VLESS-WS-97MS` (url=211ms, nekobox=240ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-69MS` (url=220ms, nekobox=249ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-100MS` (url=216ms, nekobox=238ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-88MS` (url=209ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-104MS` (url=208ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-70MS` (url=198ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-88MS` (url=205ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-74MS` (url=216ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-107MS` (url=199ms, status=HTTP 204)
17. `AKUN-017-POLICE-VLESS-WS-113MS` (url=205ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-81MS` (url=221ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-105MS` (url=206ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-101MS` (url=206ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-132MS` (url=227ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-107MS` (url=205ms, status=HTTP 204)
23. `AKUN-023-POLICE-VLESS-WS-92MS` (url=210ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-148MS` (url=230ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-179MS` (url=526ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
