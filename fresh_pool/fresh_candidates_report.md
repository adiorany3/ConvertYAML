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
1. `AKUN-001-ALIBABA-VLESS-WS-64MS` (url=233ms, nekobox=253ms, status=yes)
2. `AKUN-002-DIGITALOCEAN-VLESS-WS-81MS` (url=308ms, nekobox=338ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-80MS` (url=251ms, nekobox=293ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS` (url=256ms, nekobox=265ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-78MS` (url=301ms, nekobox=273ms, status=yes)
6. `AKUN-006-DIGITALOCEAN-VLESS-WS-83MS` (url=259ms, nekobox=272ms, status=yes)
7. `AKUN-007-DIGITALOCEAN-VLESS-WS-87MS` (url=267ms, nekobox=276ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-95MS` (url=258ms, nekobox=188ms, status=no)
9. `AKUN-008-COMPREND-NET-VLESS-WS-83MS`
10. `AKUN-009-ZVC-VLESS-WS-101MS`
11. `AKUN-010-COMPREND-NET-VLESS-WS-101MS`
12. `AKUN-012-DEV-VLESS-WS-93MS` (url=257ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-87MS` (url=243ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-96MS` (url=250ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-113MS` (url=265ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-113MS` (url=253ms, status=HTTP 204)
17. `AKUN-017-COMPREND-NET-VLESS-WS-103MS` (url=268ms, status=HTTP 204)
18. `AKUN-018-466688-VLESS-WS-107MS` (url=243ms, status=HTTP 204)
19. `AKUN-019-COMPREND-NET-VLESS-WS-97MS` (url=280ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-125MS` (url=251ms, status=HTTP 204)
21. `AKUN-021-DEV-VLESS-WS-113MS` (url=238ms, status=HTTP 204)
22. `AKUN-022-SPEEDTEST-VLESS-WS-110MS` (url=260ms, status=HTTP 204)
23. `AKUN-023-COMPREND-NET-VLESS-WS-102MS` (url=329ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-95MS` (url=272ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-99MS` (url=263ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
