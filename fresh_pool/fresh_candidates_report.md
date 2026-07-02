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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-74MS` (url=276ms, nekobox=275ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=251ms, nekobox=290ms, status=yes)
3. `AKUN-003-DIGITALOCEAN-VLESS-WS-84MS` (url=262ms, nekobox=276ms, status=yes)
4. `AKUN-004-UK-GB-DCL-01-20191003-VLESS-WS-86MS` (url=278ms, nekobox=274ms, status=yes)
5. `AKUN-005-AEZA-NETWORK-VLESS-WS-95MS` (url=281ms, nekobox=270ms, status=yes)
6. `AKUN-006-WPENG-VLESS-WS-99MS` (url=316ms, nekobox=298ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-93MS` (url=279ms, nekobox=280ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-103MS` (url=287ms, nekobox=276ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-94MS` (url=274ms, nekobox=293ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-106MS` (url=249ms, nekobox=306ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-83MS` (url=249ms, status=HTTP 204)
12. `AKUN-012-COMPREND-NET-VLESS-WS-88MS` (url=255ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-117MS` (url=240ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-106MS` (url=280ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-90MS` (url=219ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-111MS` (url=285ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-104MS` (url=261ms, status=HTTP 204)
18. `AKUN-018-PAGES-VLESS-WS-129MS` (url=250ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-261MS` (url=560ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-281MS` (url=578ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-265MS` (url=581ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-290MS` (url=651ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-293MS` (url=653ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-299MS` (url=620ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-306MS` (url=616ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
