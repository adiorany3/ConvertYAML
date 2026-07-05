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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=196ms, nekobox=231ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-76MS` (url=200ms, nekobox=242ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-80MS` (url=212ms, nekobox=243ms, status=yes)
4. `AKUN-004-CHSL-HEL-VLESS-WS-81MS` (url=230ms, nekobox=230ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-106MS` (url=211ms, nekobox=243ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-103MS` (url=212ms, nekobox=255ms, status=yes)
7. `AKUN-007-WEYRO-NET-VLESS-WS-111MS` (url=228ms, nekobox=257ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-86MS` (url=198ms, nekobox=236ms, status=yes)
9. `AKUN-009-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-67MS` (url=196ms, nekobox=227ms, status=yes)
10. `AKUN-010-WPENG-VLESS-WS-73MS` (url=222ms, nekobox=245ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-107MS` (url=198ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-96MS` (url=214ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-115MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-89MS` (url=195ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-125MS` (url=216ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-75MS` (url=206ms, status=HTTP 204)
17. `AKUN-017-466688-VLESS-WS-124MS` (url=213ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-192MS` (url=289ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-223MS` (url=510ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-228MS` (url=485ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-240MS` (url=596ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-245MS` (url=574ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-242MS` (url=550ms, status=HTTP 204)
24. `AKUN-025-SPEEDTEST-VLESS-WS-232MS` (url=492ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-380MS` (url=668ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
