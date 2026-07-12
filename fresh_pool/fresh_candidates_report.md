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
1. `AKUN-001-UNKNOWN-VLESS-WS-78MS` (url=227ms, nekobox=256ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-80MS` (url=218ms, nekobox=259ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-74MS` (url=212ms, nekobox=257ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-83MS` (url=230ms, nekobox=260ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-98MS` (url=207ms, nekobox=195ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-96MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-99MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-103MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-121MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-111MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-92MS`
12. `AKUN-012-466688-VLESS-WS-106MS` (url=214ms, status=HTTP 204)
13. `AKUN-013-DEV-VLESS-WS-113MS` (url=212ms, status=HTTP 204)
14. `AKUN-014-DEV-VLESS-WS-98MS` (url=214ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-118MS` (url=234ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-81MS` (url=210ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-85MS` (url=206ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-102MS` (url=214ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-124MS` (url=260ms, status=HTTP 204)
20. `AKUN-020-PUBLICDOMAINREGISTRY-NET-VLESS-WS-160MS` (url=234ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-92MS` (url=205ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-255MS` (url=557ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-255MS` (url=521ms, status=HTTP 204)
24. `AKUN-024-UK-GB-DCL-01-20191003-VLESS-WS-287MS` (url=3482ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-235MS` (url=515ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
