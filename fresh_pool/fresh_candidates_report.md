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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-77MS` (url=215ms, nekobox=255ms, status=yes)
2. `AKUN-002-WEBEX-VLESS-WS-78MS` (url=230ms, nekobox=239ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-82MS` (url=218ms, nekobox=257ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-88MS` (url=202ms, nekobox=259ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-84MS` (url=232ms, nekobox=247ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-79MS` (url=224ms, nekobox=255ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-90MS` (url=221ms, nekobox=250ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-102MS` (url=203ms, nekobox=233ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-99MS` (url=199ms, nekobox=261ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-101MS` (url=226ms, nekobox=249ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-111MS` (url=233ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-106MS` (url=238ms, status=HTTP 204)
13. `AKUN-013-DEV-VLESS-WS-115MS` (url=226ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-87MS` (url=224ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-131MS` (url=236ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-94MS` (url=240ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-92MS` (url=213ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-104MS` (url=227ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-171MS` (url=225ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-183MS` (url=386ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-123MS` (url=242ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-89MS` (url=225ms, status=HTTP 204)
23. `AKUN-024-NET-141-11-202-0-23-VLESS-WS-246MS` (url=505ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-238MS` (url=510ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-139MS` (url=271ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
