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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-75MS` (url=392ms, nekobox=310ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-114MS` (url=381ms, nekobox=321ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-92MS` (url=380ms, nekobox=424ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-84MS` (url=242ms, nekobox=7182ms, status=no)
5. `AKUN-004-CLOUDFLARE-VLESS-WS-115MS`
6. `AKUN-005-MEDIUM-VLESS-WS-113MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-128MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-132MS`
9. `AKUN-009-SPEEDTEST-VLESS-WS-120MS` (url=281ms, nekobox=204ms, status=no)
10. `AKUN-010-SPEEDTEST-VLESS-WS-150MS` (url=301ms, nekobox=203ms, status=no)
11. `AKUN-008-CHATGPT-VLESS-WS-112MS`
12. `AKUN-009-CLOUDFLARE-VLESS-WS-138MS`
13. `AKUN-010-CLOUDFLARE-VLESS-WS-148MS`
14. `AKUN-014-UNKNOWN-VLESS-WS-148MS` (url=296ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-156MS` (url=320ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-144MS` (url=290ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-163MS` (url=325ms, status=HTTP 204)
18. `AKUN-018-008500-VLESS-WS-163MS` (url=296ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-145MS` (url=462ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-180MS` (url=367ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-122MS` (url=378ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-152MS` (url=334ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-308MS` (url=612ms, status=HTTP 204)
24. `AKUN-024-SPEEDTEST-VLESS-WS-310MS` (url=659ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-327MS` (url=450ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
