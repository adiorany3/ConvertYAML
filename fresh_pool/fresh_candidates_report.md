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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-68MS` (url=225ms, nekobox=271ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS` (url=237ms, nekobox=285ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS` (url=246ms, nekobox=283ms, status=yes)
4. `AKUN-004-DIXONS-VLESS-WS-78MS` (url=261ms, nekobox=296ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-70MS` (url=235ms, nekobox=268ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-83MS` (url=221ms, nekobox=269ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-84MS` (url=246ms, nekobox=264ms, status=yes)
8. `AKUN-008-FMN5-RENTED-NET2-VLESS-WS-88MS` (url=258ms, nekobox=274ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-73MS` (url=229ms, nekobox=269ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-97MS` (url=276ms, nekobox=284ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-81MS` (url=232ms, status=HTTP 204)
12. `AKUN-012-POLICE-VLESS-WS-95MS` (url=267ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-103MS` (url=274ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-116MS` (url=271ms, status=HTTP 204)
15. `AKUN-015-466688-VLESS-WS-113MS` (url=260ms, status=HTTP 204)
16. `AKUN-016-POLICE-VLESS-WS-122MS` (url=312ms, status=HTTP 204)
17. `AKUN-017-WEBEX-VLESS-WS-107MS` (url=271ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-122MS` (url=252ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-86MS` (url=285ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-121MS` (url=325ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-157MS` (url=361ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-186MS` (url=288ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-263MS` (url=628ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-290MS` (url=603ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-306MS` (url=664ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
