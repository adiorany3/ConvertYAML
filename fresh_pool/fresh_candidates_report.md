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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-113MS` (url=342ms, nekobox=280ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-111MS` (url=263ms, nekobox=275ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-131MS` (url=290ms, nekobox=388ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-146MS` (url=257ms, nekobox=367ms, status=yes)
5. `AKUN-005-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-137MS` (url=272ms, nekobox=392ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-143MS` (url=255ms, nekobox=295ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-142MS` (url=262ms, nekobox=296ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-138MS` (url=341ms, nekobox=360ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-163MS` (url=261ms, nekobox=290ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-132MS` (url=272ms, nekobox=230ms, status=no)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-160MS` (url=263ms, nekobox=211ms, status=no)
12. `AKUN-012-UK-GB-DCL-01-20191003-VLESS-WS-122MS` (url=239ms, nekobox=226ms, status=no)
13. `AKUN-010-UNKNOWN-VLESS-WS-144MS`
14. `AKUN-014-UNKNOWN-VLESS-WS-119MS` (url=340ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-146MS` (url=263ms, status=HTTP 204)
16. `AKUN-016-GO-DADDY-COM-LLC-VLESS-WS-132MS` (url=349ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-302MS` (url=694ms, status=HTTP 204)
18. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-356MS` (url=672ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-347MS` (url=683ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-359MS` (url=717ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-363MS` (url=676ms, status=HTTP 204)
22. `AKUN-022-MICROSOFT-VLESS-WS-346MS` (url=770ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-122MS` (url=336ms, status=HTTP 204)
24. `AKUN-029-CONFLU-VLESS-WS-311MS` (url=662ms, status=HTTP 204)
25. `AKUN-030-CLOUDFLARE-VLESS-WS-658MS` (url=851ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
