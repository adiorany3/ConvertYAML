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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-79MS` (url=223ms, nekobox=264ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-86MS` (url=202ms, nekobox=261ms, status=yes)
3. `AKUN-003-COMPREND-NET-VLESS-WS-88MS` (url=201ms, nekobox=244ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-84MS` (url=234ms, nekobox=256ms, status=yes)
5. `AKUN-005-AEZA-NETWORK-VLESS-WS-86MS` (url=272ms, nekobox=254ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-82MS` (url=215ms, nekobox=261ms, status=yes)
7. `AKUN-007-COMPREND-NET-VLESS-WS-99MS` (url=231ms, nekobox=259ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-113MS` (url=212ms, nekobox=260ms, status=yes)
9. `AKUN-009-COMPREND-NET-VLESS-WS-87MS` (url=227ms, nekobox=242ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-95MS` (url=217ms, nekobox=290ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-80MS` (url=231ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-136MS` (url=233ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-104MS` (url=205ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-134MS` (url=234ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-95MS` (url=202ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-122MS` (url=212ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-114MS` (url=203ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-248MS` (url=539ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-264MS` (url=512ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-285MS` (url=607ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-284MS` (url=619ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-290MS` (url=605ms, status=HTTP 204)
23. `AKUN-025-SPEEDTEST-VLESS-WS-253MS` (url=3817ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-273MS` (url=613ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-104MS` (url=241ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
