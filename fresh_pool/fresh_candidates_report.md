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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-79MS` (url=279ms, nekobox=252ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-85MS` (url=238ms, nekobox=250ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-77MS` (url=231ms, nekobox=254ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-87MS` (url=200ms, nekobox=240ms, status=yes)
5. `AKUN-005-ZVC-VLESS-WS-99MS` (url=236ms, nekobox=229ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-90MS` (url=225ms, nekobox=232ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-105MS` (url=233ms, nekobox=209ms, status=no)
8. `AKUN-007-CLOUDFLARE-VLESS-WS-107MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-100MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-103MS` (url=227ms, nekobox=191ms, status=no)
11. `AKUN-009-CLOUDFLARE-VLESS-WS-106MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-120MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-101MS` (url=221ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-122MS` (url=252ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-127MS` (url=210ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-110MS` (url=250ms, status=HTTP 204)
17. `AKUN-017-466688-VLESS-WS-119MS` (url=209ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-133MS` (url=210ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-145MS` (url=217ms, status=HTTP 204)
20. `AKUN-020-PAGES-VLESS-WS-163MS` (url=226ms, status=HTTP 204)
21. `AKUN-021-WEBEX-VLESS-WS-90MS` (url=278ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-98MS` (url=203ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-261MS` (url=516ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-252MS` (url=526ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-254MS` (url=510ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
