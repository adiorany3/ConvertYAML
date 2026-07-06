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
1. `AKUN-001-UNKNOWN-VLESS-WS-83MS` (url=225ms, nekobox=224ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-87MS` (url=231ms, nekobox=202ms, status=no)
3. `AKUN-002-UNKNOWN-VLESS-WS-73MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-91MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-89MS`
6. `AKUN-005-OVH-VLESS-WS-92MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-106MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-103MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-92MS` (url=220ms, nekobox=221ms, status=no)
10. `AKUN-008-CLOUDFLARE-VLESS-WS-102MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-89MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-111MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-71MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-DEV-VLESS-WS-90MS` (url=236ms, status=HTTP 204)
15. `AKUN-015-PAGES-VLESS-WS-123MS` (url=226ms, status=HTTP 204)
16. `AKUN-016-WEBEX-VLESS-WS-122MS` (url=236ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-83MS` (url=207ms, status=HTTP 204)
18. `AKUN-018-466688-VLESS-WS-137MS` (url=224ms, status=HTTP 204)
19. `AKUN-019-WEBEX-VLESS-WS-130MS` (url=227ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-90MS` (url=221ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-160MS` (url=516ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-260MS` (url=538ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-285MS` (url=608ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-279MS` (url=604ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-296MS` (url=661ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
