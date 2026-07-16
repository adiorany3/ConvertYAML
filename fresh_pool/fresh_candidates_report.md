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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-67MS` (url=237ms, nekobox=259ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-65MS` (url=242ms, nekobox=280ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-76MS` (url=247ms, nekobox=264ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-82MS` (url=286ms, nekobox=264ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-74MS` (url=237ms, nekobox=254ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-78MS` (url=229ms, nekobox=7177ms, status=no)
7. `AKUN-006-UNKNOWN-VLESS-WS-79MS`
8. `AKUN-007-ES-FORNEX-20160629-VLESS-WS-77MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-77MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-81MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-77MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-87MS` (url=269ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-76MS` (url=245ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-91MS` (url=251ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-94MS` (url=254ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-90MS` (url=246ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-76MS` (url=220ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-81MS` (url=242ms, status=HTTP 204)
19. `AKUN-019-MYBB-VLESS-WS-97MS` (url=231ms, status=HTTP 204)
20. `AKUN-020-DEV-VLESS-WS-94MS` (url=248ms, status=HTTP 204)
21. `AKUN-021-DEV-VLESS-WS-70MS` (url=234ms, status=HTTP 204)
22. `AKUN-022-466688-VLESS-WS-101MS` (url=250ms, status=HTTP 204)
23. `AKUN-023-NEXUSMODS-VLESS-WS-87MS` (url=267ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-107MS` (url=243ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-100MS` (url=290ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
