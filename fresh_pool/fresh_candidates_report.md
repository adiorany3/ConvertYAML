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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-73MS` (url=230ms, nekobox=240ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-75MS` (url=211ms, nekobox=253ms, status=yes)
3. `AKUN-003-COMPREND-NET-VLESS-WS-90MS` (url=217ms, nekobox=245ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-116MS` (url=212ms, nekobox=246ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-114MS` (url=233ms, nekobox=240ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-88MS` (url=218ms, nekobox=245ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-113MS` (url=202ms, nekobox=238ms, status=yes)
8. `AKUN-008-DIGITALOCEAN-VLESS-WS-120MS` (url=234ms, nekobox=303ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-121MS` (url=222ms, nekobox=244ms, status=yes)
10. `AKUN-010-DIGITALOCEAN-VLESS-WS-102MS` (url=226ms, nekobox=254ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-86MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-109MS` (url=220ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-110MS` (url=228ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-122MS` (url=220ms, status=HTTP 204)
15. `AKUN-015-466688-VLESS-WS-123MS` (url=226ms, status=HTTP 204)
16. `AKUN-016-WEBEX-VLESS-WS-94MS` (url=228ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-120MS` (url=250ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-231MS` (url=496ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-244MS` (url=505ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-270MS` (url=588ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-247MS` (url=500ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-273MS` (url=605ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-270MS` (url=588ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-289MS` (url=591ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-262MS` (url=713ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
