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
1. `AKUN-001-UNKNOWN-VLESS-WS-86MS` (url=226ms, nekobox=255ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-99MS` (url=239ms, nekobox=236ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-92MS` (url=224ms, nekobox=259ms, status=yes)
4. `AKUN-004-VULTR-VLESS-WS-80MS` (url=219ms, nekobox=234ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-89MS` (url=203ms, nekobox=243ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-106MS` (url=205ms, nekobox=238ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-121MS` (url=209ms, nekobox=244ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-137MS` (url=224ms, nekobox=234ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-108MS` (url=282ms, nekobox=248ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-113MS` (url=205ms, nekobox=250ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-130MS` (url=208ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-97MS` (url=208ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-123MS` (url=212ms, status=HTTP 204)
14. `AKUN-014-DEV-VLESS-WS-98MS` (url=213ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-145MS` (url=200ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-148MS` (url=210ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-118MS` (url=216ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-96MS` (url=202ms, status=HTTP 204)
19. `AKUN-019-1PASSWORD-VLESS-WS-122MS` (url=216ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-130MS` (url=203ms, status=HTTP 204)
21. `AKUN-021-MYBB-VLESS-WS-130MS` (url=202ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-261MS` (url=579ms, status=HTTP 204)
23. `AKUN-023-OCTOPUSSS5-VLESS-WS-255MS` (url=578ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-274MS` (url=574ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-251MS` (url=521ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
