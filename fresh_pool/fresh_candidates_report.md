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
1. `AKUN-001-UNKNOWN-VLESS-WS-91MS` (url=244ms, nekobox=241ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-97MS` (url=223ms, nekobox=241ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-93MS` (url=204ms, nekobox=244ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-115MS` (url=235ms, nekobox=263ms, status=yes)
5. `AKUN-005-GO-DADDY-COM-LLC-VLESS-WS-105MS` (url=238ms, nekobox=244ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-117MS` (url=220ms, nekobox=246ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-107MS` (url=222ms, nekobox=231ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-118MS` (url=219ms, nekobox=248ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-131MS` (url=289ms, nekobox=299ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-108MS` (url=208ms, nekobox=237ms, status=yes)
11. `AKUN-011-466688-VLESS-WS-96MS` (url=265ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-127MS` (url=294ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-142MS` (url=220ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-157MS` (url=273ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-152MS` (url=214ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-126MS` (url=269ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-90MS` (url=231ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-149MS` (url=410ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-137MS` (url=324ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-166MS` (url=217ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-89MS` (url=216ms, status=HTTP 204)
22. `AKUN-022-WEBEX-VLESS-WS-89MS` (url=231ms, status=HTTP 204)
23. `AKUN-023-POLICE-VLESS-WS-156MS` (url=272ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-146MS` (url=213ms, status=HTTP 204)
25. `AKUN-025-ORG-VLESS-WS-157MS` (url=280ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
