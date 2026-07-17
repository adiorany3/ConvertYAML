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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-70MS` (url=245ms, nekobox=256ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-68MS` (url=233ms, nekobox=255ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-76MS` (url=232ms, nekobox=264ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-86MS` (url=235ms, nekobox=260ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-91MS` (url=248ms, nekobox=274ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-107MS` (url=256ms, nekobox=265ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-96MS` (url=234ms, nekobox=256ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-104MS` (url=257ms, nekobox=272ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-102MS` (url=221ms, nekobox=257ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-94MS` (url=270ms, nekobox=272ms, status=yes)
11. `AKUN-011-DEV-VLESS-WS-112MS` (url=234ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-99MS` (url=228ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-113MS` (url=261ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-98MS` (url=265ms, status=HTTP 204)
15. `AKUN-015-GO-DADDY-COM-LLC-VLESS-WS-82MS` (url=245ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-126MS` (url=244ms, status=HTTP 204)
17. `AKUN-017-POLICE-VLESS-WS-98MS` (url=300ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-109MS` (url=234ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-134MS` (url=253ms, status=HTTP 204)
20. `AKUN-020-DEV-VLESS-WS-127MS` (url=227ms, status=HTTP 204)
21. `AKUN-021-UK-GB-DCL-01-20191003-VLESS-WS-145MS` (url=256ms, status=HTTP 204)
22. `AKUN-022-WPENG-VLESS-WS-82MS` (url=259ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-126MS` (url=271ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-152MS` (url=243ms, status=HTTP 204)
25. `AKUN-025-UK-GB-DCL-01-20191003-VLESS-WS-162MS` (url=252ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
