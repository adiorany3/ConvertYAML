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
1. `AKUN-001-UNKNOWN-VLESS-WS-64MS` (url=220ms, nekobox=227ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS` (url=210ms, nekobox=238ms, status=yes)
3. `AKUN-003-WPENG-VLESS-WS-64MS` (url=213ms, nekobox=248ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-69MS` (url=231ms, nekobox=265ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-77MS` (url=216ms, nekobox=242ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-80MS` (url=214ms, nekobox=242ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-71MS` (url=225ms, nekobox=181ms, status=no)
8. `AKUN-007-ZVC-VLESS-WS-65MS`
9. `AKUN-008-TRANSIP-NL-AMS4-CUST-VLESS-WS-103MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-104MS`
11. `AKUN-010-WEYRO-NET-VLESS-WS-89MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-123MS` (url=217ms, status=HTTP 204)
13. `AKUN-013-ES-FORNEX-20160629-VLESS-WS-122MS` (url=205ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-99MS` (url=213ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-102MS` (url=207ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-74MS` (url=228ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-225MS` (url=500ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-234MS` (url=635ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-227MS` (url=485ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-267MS` (url=597ms, status=HTTP 204)
21. `AKUN-021-PUBLICDOMAINREGISTRY-NET-VLESS-WS-272MS` (url=581ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-269MS` (url=596ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-273MS` (url=606ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-198MS` (url=4265ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-341MS` (url=351ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
