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
1. `AKUN-001-UNKNOWN-VLESS-WS-61MS` (url=219ms, nekobox=244ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-61MS` (url=229ms, nekobox=247ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-67MS` (url=215ms, nekobox=238ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-60MS` (url=203ms, nekobox=236ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-59MS` (url=225ms, nekobox=233ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-77MS` (url=214ms, nekobox=251ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-89MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-105MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-71MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-73MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-96MS` (url=222ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-103MS` (url=220ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-90MS` (url=210ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-109MS` (url=196ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-115MS` (url=275ms, status=HTTP 204)
16. `AKUN-017-WEBEX-VLESS-WS-117MS` (url=240ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-96MS` (url=216ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-105MS` (url=213ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-73MS` (url=231ms, status=HTTP 204)
20. `AKUN-021-466688-VLESS-WS-71MS` (url=220ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-77MS` (url=216ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-119MS` (url=219ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-145MS` (url=203ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-141MS` (url=227ms, status=HTTP 204)
25. `AKUN-026-SPEEDTEST-VLESS-WS-148MS` (url=203ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
