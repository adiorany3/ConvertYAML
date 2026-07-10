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
1. `AKUN-001-UNKNOWN-VLESS-WS-88MS` (url=227ms, nekobox=241ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-88MS` (url=231ms, nekobox=250ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-95MS` (url=219ms, nekobox=256ms, status=yes)
4. `AKUN-004-PUBLICDOMAINREGISTRY-NET-VLESS-WS-96MS` (url=233ms, nekobox=248ms, status=yes)
5. `AKUN-005-HOSTSYMBOL2-SG-VLESS-WS-99MS` (url=233ms, nekobox=241ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS` (url=275ms, nekobox=257ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-108MS` (url=225ms, nekobox=254ms, status=yes)
8. `AKUN-008-VULTR-VLESS-WS-96MS` (url=210ms, nekobox=250ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-99MS` (url=282ms, nekobox=635ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-107MS` (url=228ms, nekobox=242ms, status=yes)
11. `AKUN-011-WPENG-VLESS-WS-101MS` (url=305ms, status=HTTP 204)
12. `AKUN-012-NET-82-21-84-0-24-VLESS-WS-122MS` (url=234ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-123MS` (url=238ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-117MS` (url=240ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-99MS` (url=202ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-112MS` (url=203ms, status=HTTP 204)
17. `AKUN-017-ILOVEZHENJIU-VLESS-WS-173MS` (url=827ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-150MS` (url=245ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-374MS` (url=798ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-381MS` (url=828ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-399MS` (url=1042ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-338MS` (url=494ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-459MS` (url=1192ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-449MS` (url=1830ms, status=HTTP 204)
25. `AKUN-029-QZZ-VLESS-WS-587MS` (url=1116ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
