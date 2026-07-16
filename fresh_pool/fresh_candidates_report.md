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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-58MS` (url=208ms, nekobox=240ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-62MS` (url=210ms, nekobox=248ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-66MS` (url=209ms, nekobox=237ms, status=yes)
4. `AKUN-004-WEBEX-VLESS-WS-60MS` (url=217ms, nekobox=345ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-66MS` (url=225ms, nekobox=242ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-75MS` (url=206ms, nekobox=233ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-72MS` (url=196ms, nekobox=255ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-72MS` (url=210ms, nekobox=249ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-69MS` (url=224ms, nekobox=255ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-85MS` (url=226ms, nekobox=250ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-75MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-83MS` (url=219ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-74MS` (url=220ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-73MS` (url=220ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-107MS` (url=239ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-104MS` (url=201ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-112MS` (url=219ms, status=HTTP 204)
18. `AKUN-018-DEV-VLESS-WS-102MS` (url=220ms, status=HTTP 204)
19. `AKUN-019-466688-VLESS-WS-111MS` (url=234ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-115MS` (url=225ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-96MS` (url=209ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-110MS` (url=222ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-112MS` (url=223ms, status=HTTP 204)
24. `AKUN-024-DEV-VLESS-WS-74MS` (url=212ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-72MS` (url=214ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
