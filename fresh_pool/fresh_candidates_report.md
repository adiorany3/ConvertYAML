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
1. `AKUN-001-UNKNOWN-VLESS-WS-113MS` (url=235ms, nekobox=270ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-112MS` (url=238ms, nekobox=267ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-116MS` (url=232ms, nekobox=265ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-117MS` (url=234ms, nekobox=262ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-114MS` (url=248ms, nekobox=287ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-115MS` (url=242ms, nekobox=258ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-122MS` (url=234ms, nekobox=272ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-116MS` (url=238ms, nekobox=262ms, status=yes)
9. `AKUN-009-GOOGLE-VLESS-WS-127MS` (url=242ms, nekobox=268ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-129MS` (url=312ms, nekobox=277ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-151MS` (url=238ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-117MS` (url=342ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-132MS` (url=242ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-170MS` (url=268ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-132MS` (url=330ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-117MS` (url=318ms, status=HTTP 204)
17. `AKUN-017-ZOOM-VLESS-WS-115MS` (url=251ms, status=HTTP 204)
18. `AKUN-018-3666888-VLESS-WS-126MS` (url=251ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-229MS` (url=301ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-383MS` (url=782ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-353MS` (url=778ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-399MS` (url=748ms, status=HTTP 204)
23. `AKUN-024-SUKARIO-VLESS-WS-318MS` (url=1374ms, status=HTTP 204)
24. `AKUN-026-SUKARIO-VLESS-WS-674MS` (url=1088ms, status=HTTP 204)
25. `AKUN-032-UNKNOWN-VLESS-WS-861MS` (url=1412ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
