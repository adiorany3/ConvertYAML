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
1. `AKUN-001-UNKNOWN-VLESS-WS-77MS` (url=257ms, nekobox=292ms, status=yes)
2. `AKUN-002-ORG-VLESS-WS-75MS` (url=235ms, nekobox=285ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-74MS` (url=265ms, nekobox=276ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-80MS` (url=241ms, nekobox=286ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-72MS` (url=225ms, nekobox=257ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-110MS` (url=271ms, nekobox=290ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-75MS` (url=254ms, nekobox=272ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-79MS` (url=245ms, nekobox=178ms, status=no)
9. `AKUN-008-NEXUSMODS-VLESS-WS-112MS`
10. `AKUN-009-RTCOMM-SRAVNI-RU-VLESS-WS-87MS`
11. `AKUN-010-WEBEX-VLESS-WS-94MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-84MS` (url=237ms, status=HTTP 204)
13. `AKUN-013-466688-VLESS-WS-125MS` (url=240ms, status=HTTP 204)
14. `AKUN-014-DIXONS-VLESS-WS-92MS` (url=285ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-72MS` (url=239ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-122MS` (url=236ms, status=HTTP 204)
17. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-100MS` (url=244ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-180MS` (url=345ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-154MS` (url=262ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-257MS` (url=579ms, status=HTTP 204)
21. `AKUN-021-RS-RAPIDSEEDBOX-20190717-VLESS-WS-283MS` (url=591ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-293MS` (url=4408ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-310MS` (url=921ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-308MS` (url=2102ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-310MS` (url=695ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
