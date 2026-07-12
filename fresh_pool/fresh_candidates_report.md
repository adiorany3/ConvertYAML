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
1. `AKUN-001-090227-VLESS-WS-80MS` (url=325ms, nekobox=354ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-91MS` (url=290ms, nekobox=334ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-93MS` (url=290ms, nekobox=323ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-92MS` (url=326ms, nekobox=390ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-84MS` (url=334ms, nekobox=202ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-95MS`
7. `AKUN-007-SPEEDTEST-VLESS-WS-100MS` (url=368ms, nekobox=203ms, status=no)
8. `AKUN-006-UNKNOWN-VLESS-WS-99MS`
9. `AKUN-007-ZVC-VLESS-WS-107MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-109MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-86MS`
12. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-110MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-95MS` (url=321ms, status=HTTP 204)
14. `AKUN-014-ORG-VLESS-WS-126MS` (url=305ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-111MS` (url=354ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-106MS` (url=285ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-121MS` (url=400ms, status=HTTP 204)
18. `AKUN-018-PUBLICDOMAINREGISTRY-NET-VLESS-WS-107MS` (url=307ms, status=HTTP 204)
19. `AKUN-019-NET-82-21-84-0-24-VLESS-WS-163MS` (url=357ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-258MS` (url=498ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-323MS` (url=706ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-299MS` (url=730ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-339MS` (url=4237ms, status=HTTP 204)
24. `AKUN-024-LT-LRTC-20060503-VLESS-WS-319MS` (url=959ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-87MS` (url=310ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
