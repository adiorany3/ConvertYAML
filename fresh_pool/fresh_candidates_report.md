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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=211ms, nekobox=238ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-67MS` (url=210ms, nekobox=241ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-67MS` (url=218ms, nekobox=240ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS` (url=225ms, nekobox=248ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-89MS` (url=221ms, nekobox=255ms, status=yes)
6. `AKUN-006-466688-VLESS-WS-70MS`
7. `AKUN-007-US-VLESS-WS-87MS`
8. `AKUN-008-PUBLICDOMAINREGISTRY-NET-VLESS-WS-69MS`
9. `AKUN-009-UNKNOWN-VLESS-WS-84MS`
10. `AKUN-010-PAGES-VLESS-WS-84MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-108MS` (url=231ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-72MS` (url=212ms, status=HTTP 204)
13. `AKUN-014-GO-DADDY-COM-LLC-VLESS-WS-58MS` (url=211ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-106MS` (url=221ms, status=HTTP 204)
15. `AKUN-016-ES-FORNEX-20160629-VLESS-WS-101MS` (url=221ms, status=HTTP 204)
16. `AKUN-017-SPEEDTEST-VLESS-WS-145MS` (url=223ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-144MS` (url=217ms, status=HTTP 204)
18. `AKUN-019-DEV-VLESS-WS-170MS` (url=222ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-69MS` (url=221ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-177MS` (url=274ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-359MS` (url=753ms, status=HTTP 204)
22. `AKUN-026-CLOUDFLARE-VLESS-WS-564MS` (url=655ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-658MS` (url=1067ms, status=HTTP 204)
24. `AKUN-028-SPEEDTEST-VLESS-WS-657MS` (url=739ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-342MS` (url=737ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
