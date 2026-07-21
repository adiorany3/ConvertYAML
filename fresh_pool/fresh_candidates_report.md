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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-81MS` (url=230ms, nekobox=251ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-80MS` (url=213ms, nekobox=251ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-87MS` (url=253ms, nekobox=254ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-86MS` (url=237ms, nekobox=261ms, status=yes)
5. `AKUN-005-ZVC-VLESS-WS-91MS` (url=222ms, nekobox=259ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-102MS` (url=225ms, nekobox=258ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-88MS` (url=207ms, nekobox=246ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-99MS` (url=220ms, nekobox=221ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-102MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-95MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-96MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-96MS` (url=224ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-102MS` (url=201ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-98MS` (url=212ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-106MS` (url=231ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-98MS` (url=235ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-108MS` (url=223ms, status=HTTP 204)
18. `AKUN-018-WEBEX-VLESS-WS-118MS` (url=208ms, status=HTTP 204)
19. `AKUN-019-PAGES-VLESS-WS-129MS` (url=232ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-133MS` (url=209ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-115MS` (url=218ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-139MS` (url=252ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-251MS` (url=519ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-255MS` (url=511ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-259MS` (url=544ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
