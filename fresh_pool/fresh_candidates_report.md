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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-72MS` (url=223ms, nekobox=262ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS` (url=234ms, nekobox=258ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=230ms, nekobox=272ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-87MS` (url=265ms, nekobox=290ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-70MS` (url=267ms, nekobox=252ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-73MS` (url=228ms, nekobox=253ms, status=yes)
7. `AKUN-007-VULTR-VLESS-WS-67MS` (url=231ms, nekobox=264ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-74MS` (url=234ms, nekobox=262ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-85MS` (url=240ms, nekobox=256ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-104MS` (url=228ms, nekobox=250ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-132MS` (url=227ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-123MS` (url=238ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-72MS` (url=244ms, status=HTTP 204)
14. `AKUN-014-ZOOM-VLESS-WS-108MS` (url=245ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-132MS` (url=240ms, status=HTTP 204)
16. `AKUN-017-COMPREND-NET-VLESS-WS-70MS` (url=259ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-262MS` (url=562ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-287MS` (url=544ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-293MS` (url=633ms, status=HTTP 204)
20. `AKUN-021-MICROSOFT-VLESS-WS-284MS` (url=623ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-289MS` (url=623ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-303MS` (url=614ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-294MS` (url=651ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-260MS` (url=564ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-356MS` (url=642ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
