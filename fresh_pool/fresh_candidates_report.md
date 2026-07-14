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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-74MS` (url=228ms, nekobox=242ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-87MS` (url=203ms, nekobox=211ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-93MS`
4. `AKUN-003-DEV-VLESS-WS-97MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-91MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-103MS`
7. `AKUN-006-WEBEX-VLESS-WS-96MS`
8. `AKUN-009-CLOUDFLARE-VLESS-WS-85MS` (url=199ms, nekobox=177ms, status=no)
9. `AKUN-007-CLOUDFLARE-VLESS-WS-101MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-90MS`
11. `AKUN-009-GO-DADDY-COM-LLC-VLESS-WS-92MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-109MS`
13. `AKUN-014-CLOUDFLARE-VLESS-WS-103MS` (url=202ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-91MS` (url=222ms, status=HTTP 204)
15. `AKUN-016-DEV-VLESS-WS-79MS` (url=225ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-92MS` (url=210ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-116MS` (url=236ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-92MS` (url=200ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-91MS` (url=218ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-101MS` (url=203ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-70MS` (url=230ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-115MS` (url=323ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-80MS` (url=218ms, status=HTTP 204)
24. `AKUN-025-3666888-VLESS-WS-137MS` (url=210ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-101MS` (url=202ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
