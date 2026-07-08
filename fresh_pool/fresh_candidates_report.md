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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=310ms, nekobox=229ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-62MS` (url=221ms, nekobox=219ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS` (url=223ms, nekobox=250ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-76MS` (url=208ms, nekobox=246ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-68MS` (url=249ms, nekobox=228ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-77MS` (url=242ms, nekobox=223ms, status=yes)
7. `AKUN-007-WEBEX-VLESS-WS-70MS` (url=206ms, nekobox=262ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-67MS` (url=199ms, nekobox=223ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-80MS` (url=231ms, nekobox=267ms, status=yes)
10. `AKUN-010-PUBLICDOMAINREGISTRY-NET-VLESS-WS-88MS` (url=199ms, nekobox=260ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-78MS` (url=212ms, status=HTTP 204)
12. `AKUN-012-466688-VLESS-WS-74MS` (url=225ms, status=HTTP 204)
13. `AKUN-013-ZVC-VLESS-WS-68MS` (url=227ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-75MS` (url=216ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-107MS` (url=205ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-111MS` (url=201ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-69MS` (url=207ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-109MS` (url=3875ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-88MS` (url=220ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-79MS` (url=223ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-120MS` (url=823ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-77MS` (url=221ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-120MS` (url=210ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-88MS` (url=198ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-346MS` (url=770ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
