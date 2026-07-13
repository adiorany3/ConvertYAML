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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=235ms, nekobox=224ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-65MS` (url=207ms, nekobox=231ms, status=yes)
3. `AKUN-003-PUBLICDOMAINREGISTRY-NET-VLESS-WS-63MS` (url=219ms, nekobox=231ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-66MS` (url=194ms, nekobox=239ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-67MS` (url=220ms, nekobox=246ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-71MS` (url=215ms, nekobox=244ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-79MS` (url=216ms, nekobox=234ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-78MS` (url=225ms, nekobox=233ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-73MS` (url=224ms, nekobox=234ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-81MS` (url=202ms, nekobox=242ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-89MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-WPENG-VLESS-WS-81MS` (url=205ms, status=HTTP 204)
13. `AKUN-013-ZVC-VLESS-WS-66MS` (url=214ms, status=HTTP 204)
14. `AKUN-014-DPDNS-VLESS-WS-99MS` (url=230ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-108MS` (url=201ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-121MS` (url=205ms, status=HTTP 204)
17. `AKUN-017-HETZNER-VLESS-WS-100MS` (url=210ms, status=HTTP 204)
18. `AKUN-018-NET-82-21-84-0-24-VLESS-WS-112MS` (url=206ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-87MS` (url=218ms, status=HTTP 204)
20. `AKUN-020-HETZNER-VLESS-WS-146MS` (url=197ms, status=HTTP 204)
21. `AKUN-021-INTERNETWORKS-45-131-210-VLESS-WS-217MS` (url=485ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-236MS` (url=492ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-232MS` (url=490ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-253MS` (url=523ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-410MS` (url=718ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
