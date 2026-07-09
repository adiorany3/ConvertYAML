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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-89MS` (url=300ms, nekobox=263ms, status=yes)
2. `AKUN-002-WEBEX-VLESS-WS-94MS` (url=229ms, nekobox=237ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-95MS` (url=216ms, nekobox=240ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-95MS` (url=227ms, nekobox=260ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-99MS` (url=244ms, nekobox=258ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-95MS` (url=206ms, nekobox=240ms, status=yes)
7. `AKUN-007-466688-VLESS-WS-90MS` (url=215ms, nekobox=345ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-111MS` (url=221ms, nekobox=233ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-108MS` (url=239ms, nekobox=234ms, status=yes)
10. `AKUN-010-PUBLICDOMAINREGISTRY-NET-VLESS-WS-100MS` (url=211ms, nekobox=231ms, status=yes)
11. `AKUN-011-PAGES-VLESS-WS-110MS` (url=257ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-94MS` (url=217ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-100MS` (url=222ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-118MS` (url=209ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-125MS` (url=389ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-141MS` (url=206ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-107MS` (url=218ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-374MS` (url=775ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-383MS` (url=818ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-391MS` (url=834ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-377MS` (url=868ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-401MS` (url=872ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-407MS` (url=839ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-385MS` (url=768ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-650MS` (url=1058ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
