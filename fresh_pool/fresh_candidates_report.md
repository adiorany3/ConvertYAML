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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-74MS` (url=239ms, nekobox=251ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-73MS` (url=245ms, nekobox=264ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-77MS` (url=250ms, nekobox=312ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-84MS` (url=284ms, nekobox=257ms, status=yes)
5. `AKUN-005-UK-GB-DCL-01-20191003-VLESS-WS-83MS` (url=235ms, nekobox=258ms, status=yes)
6. `AKUN-006-OVH-VLESS-WS-89MS` (url=241ms, nekobox=270ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-80MS` (url=284ms, nekobox=267ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-81MS` (url=231ms, nekobox=265ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-86MS` (url=243ms, nekobox=263ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-77MS` (url=231ms, nekobox=259ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-97MS` (url=250ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-71MS` (url=230ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-83MS` (url=234ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-87MS` (url=233ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-92MS` (url=270ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-105MS` (url=248ms, status=HTTP 204)
17. `AKUN-017-COMPREND-NET-VLESS-WS-137MS` (url=236ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-132MS` (url=258ms, status=HTTP 204)
19. `AKUN-019-COMPREND-NET-VLESS-WS-93MS` (url=217ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-109MS` (url=240ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-95MS` (url=236ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-260MS` (url=582ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-284MS` (url=542ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-282MS` (url=644ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-293MS` (url=641ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
